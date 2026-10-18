"""Bounded fake-only reference handoff with validated final stream and CMS AEAD.

This is a mechanics test, NOT an independent author, owner-held key system,
completed gold packet, reference-output privacy boundary or scored fixture.

A fabricated 9+12-case final result is parsed with the prior exact-only
collector, sealed to a mock recipient's public certificate, copied as ciphertext
and recovered in a *separate subprocess* with post-authentication SHA-256
verification. The mock roles share the same underlying test OS principal.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from experiments.r0_p03_navigation_probe import (
    synthetic_cms_recipient_preflight as cms,
    synthetic_output_collector_candidate as collector,
)

MAX_FAKE_BYTES = 128 * 1024
HIDDEN_GOLD_QUALIFIED = False


class SyntheticHandoffError(RuntimeError):
    """Reject a failed synthetic handoff rather than report it as admitted."""


def exact_fake_final(stream: bytes) -> bytes:
    """Require the strict preexisting 9+12 fixture before any encryption."""
    payload = collector.extract_synthetic_final(stream)
    if not payload or len(payload) > MAX_FAKE_BYTES:
        raise SyntheticHandoffError("Not a bounded synthetic final payload")
    packet = json.loads(payload)
    if packet != collector.fake_packet():
        raise SyntheticHandoffError("Synthetic reference payload changed")
    return payload


def recipient_readback(
    sealed_path: Path,
    recipient_cert: Path,
    recipient_private: Path,
    expected_digest: str,
) -> bool:
    """Do not release any decrypted bytes before auth and digest verification."""
    if len(expected_digest) != 64 or any(c not in "0123456789abcdef" for c in expected_digest):
        return False
    try:
        if not (sealed_path.is_file() and recipient_cert.is_file() and recipient_private.is_file()):
            return False
        plaintext = cms._safe_decrypt(
            sealed_path, recipient_cert, recipient_private, expected_digest
        )
    except (OSError, subprocess.SubprocessError):
        return False
    if plaintext is None:
        return False
    # Defense in depth: even a correctly authenticated message cannot become
    # unapproved answers in this synthetic-only stage.
    try:
        return plaintext == exact_fake_final(collector.fake_stream())
    except (ValueError, SyntheticHandoffError):
        return False


def _openssl(*arguments: str, data: bytes | None = None) -> subprocess.CompletedProcess:
    return cms._invoke(list(arguments), data=data)


def run_demo() -> dict:
    """Run one disposable complete-packet handoff, no model call or owner ACL."""
    if not cms.OPENSSL.is_file() or not cms.SCRATCH.is_dir():
        raise SyntheticHandoffError("Existing OpenSSL or .venv scratch not available")
    payload = exact_fake_final(collector.fake_stream())
    payload_sha = hashlib.sha256(payload).hexdigest()

    with tempfile.TemporaryDirectory(dir=cms.SCRATCH, prefix=".r0p03-fake-handoff-") as tmp:
        root = Path(tmp)
        author = root / "mock_author"
        owner = root / "mock_owner"
        author.mkdir()
        owner.mkdir()

        private_key = owner / "synthetic_private_key.pem"
        recipient_cert = owner / "synthetic_certificate.pem"
        public_cert = author / "synthetic_certificate.pem"

        created = _openssl(
            "req", "-new", "-x509", "-newkey", "rsa:2048", "-nodes",
            "-keyout", str(private_key), "-out", str(recipient_cert),
            "-subj", "/CN=r0-p03-fake-handoff", "-days", "1",
        )
        if created.returncode != 0 or not private_key.is_file() or not recipient_cert.is_file():
            raise SyntheticHandoffError("Unable to provision fake recipient identity")

        shutil.copyfile(recipient_cert, public_cert)
        if any(x.name.endswith((".key", ".pfx")) or "private" in x.name or "key" in x.name
               for x in author.iterdir()):
            raise SyntheticHandoffError("Mock author contains a private key")

        sealed = _openssl(
            "cms", "-encrypt", "-binary", "-outform", "DER",
            "-aes-256-gcm", "-recip", str(public_cert),
            data=payload,
        )
        if sealed.returncode != 0 or not sealed.stdout:
            raise SyntheticHandoffError("AEAD seal failed")

        outgoing = author / "fake-reference.cms"
        outgoing.write_bytes(sealed.stdout)
        cms_info = _openssl("cms", "-cmsout", "-print", "-inform", "DER", "-in", str(outgoing))
        if cms_info.returncode != 0 or b"aes-256-gcm" not in cms_info.stdout.lower():
            raise SyntheticHandoffError("Authenticated encryption algorithm not verified")

        delivered = owner / "received-fake-reference.cms"
        shutil.copyfile(outgoing, delivered)
        if hashlib.sha256(delivered.read_bytes()).digest() != hashlib.sha256(outgoing.read_bytes()).digest():
            raise SyntheticHandoffError("Ciphertext changed during simulated delivery")

        def verify_in_separate_process(candidate: Path) -> bool:
            res = subprocess.run(
                [sys.executable, "-B", "-m",
                 "experiments.r0_p03_navigation_probe.synthetic_reference_handoff_candidate",
                 "--mock-recipient-verify", str(candidate),
                 str(recipient_cert), str(private_key), payload_sha],
                cwd=cms.ROOT, capture_output=True, text=True, timeout=25, check=False,
            )
            return res.returncode == 0 and res.stdout.strip() == "MOCK_RECIPIENT_READBACK=PASS"

        readback = verify_in_separate_process(delivered)
        altered_bytes = bytearray(delivered.read_bytes())
        altered_bytes[-1] ^= 0x01
        altered = owner / "altered.cms"
        altered.write_bytes(altered_bytes)
        tampering_rejected = not verify_in_separate_process(altered)

        bad_digest = "0" * 64 if payload_sha != "0" * 64 else "1" * 64
        wrong_commitment_rejected = not subprocess.run(
            [sys.executable, "-B", "-m",
             "experiments.r0_p03_navigation_probe.synthetic_reference_handoff_candidate",
             "--mock-recipient-verify", str(delivered),
             str(recipient_cert), str(private_key), bad_digest],
            cwd=cms.ROOT, capture_output=True, text=True, timeout=25, check=False,
        ).returncode == 0

        if not readback or not tampering_rejected or not wrong_commitment_rejected:
            raise SyntheticHandoffError("Fake-only recipient verification/negative controls failed")

        result = {
            "synthetic_only": True,
            "source_stream_result_validated": True,
            "fictional_legacy_slots": 9,
            "fictional_primary_slots": 12,
            "aead_algorithm": "OpenSSL CMS AES-256-GCM",
            "mock_author_received_public_certificate_only": True,
            "mock_author_wrote_plaintext_packet_file": False,
            "mock_delivery_ciphertext_sha256_match": True,
            "fresh_subprocess_exact_full_packet_recovery": readback,
            "tampered_ciphertext_rejected": tampering_rejected,
            "wrong_commitment_rejected": wrong_commitment_rejected,
            "actual_distinct_windows_principals": False,
            "actual_model_author_invoked": False,
            "owner_held_key_or_real_answer_custody_qualified": False,
            "hidden_gold_qualified": HIDDEN_GOLD_QUALIFIED,
        }
        return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(json.dumps(run_demo(), sort_keys=True))
    elif len(sys.argv) == 6 and sys.argv[1] == "--mock-recipient-verify":
        success = recipient_readback(
            Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]), sys.argv[5]
        )
        if success:
            print("MOCK_RECIPIENT_READBACK=PASS")
        else:
            print("MOCK_RECIPIENT_READBACK=FAIL")
            raise SystemExit(2)
    else:
        raise SystemExit("usage: python -m ...synthetic_reference_handoff_candidate [--mock-recipient-verify CIPHER CERT KEY SHA256]")
