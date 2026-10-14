"""Disposable fake-only R0-P03 public-recipient encryption trial.

This demonstrator does not isolate OS principals, possess real private keys,
handle model output, or authorize benchmark gold. OpenSSL CMS AES-256-GCM
is exercised with a public-only encryptor directory. Decryption outputs are
treated as untrusted until both process success and SHA-256 equality hold.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / ".venv"
OPENSSL = Path(r"C:\Program Files\Git\usr\bin\openssl.exe")
FAKE_PACKET = b"SYNTHETIC_ONLY_R0P03_NOT_REAL_GOLD\n"


class FakeRecipientTrialError(RuntimeError):
    """Reject a failed synthetic-only envelope experiment."""


def _invoke(args: list[str], *, data: bytes | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [str(OPENSSL), *args],
        input=data, capture_output=True, timeout=20, check=False,
    )


def _safe_decrypt(
    encrypted: Path, certificate: Path, private_key: Path, expected_digest: str,
) -> bytes | None:
    """Return plaintext ONLY after successful CMS auth and independent digest.

    OpenSSL CMS may stream provisional plaintext to stdout before learning
    that the GCM tag or other message validation failed. Even on exit failure
    the subprocess may therefore contain untrusted plaintext bytes. Never
    forward them to the caller, a file, an evaluator, or an agent on failure.
    """
    attempt = _invoke([
        "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(encrypted), "-recip", str(certificate),
        "-inkey", str(private_key),
    ])
    if attempt.returncode != 0:
        return None
    if hashlib.sha256(attempt.stdout).hexdigest() != expected_digest:
        return None
    return attempt.stdout


def run_demo() -> dict:
    """Execute one fully disposable synthetic-only envelope and recovery trial."""
    if not OPENSSL.is_file():
        raise FakeRecipientTrialError("OpenSSL not available")
    if not SCRATCH.is_dir():
        raise FakeRecipientTrialError("scratch root unavailable")

    with tempfile.TemporaryDirectory(dir=SCRATCH, prefix=".r0p03-cms-owner-") as d:
        root = Path(d)
        owner = root / "mock_owner"
        encryptor = root / "mock_encryptor"
        owner.mkdir()
        encryptor.mkdir()

        private_key = owner / "synthetic_key.pem"
        recipient_cert = owner / "synthetic_recipient.pem"
        public_copy = encryptor / "synthetic_recipient.pem"
        envelope = encryptor / "synthetic_ciphertext.cms"
        altered = encryptor / "altered_ciphertext.cms"

        created = _invoke([
            "req", "-new", "-x509", "-newkey", "rsa:2048", "-nodes",
            "-keyout", str(private_key), "-out", str(recipient_cert),
            "-subj", "/CN=synthetic-p03-ephemeral", "-days", "1",
        ])
        if created.returncode != 0 or not private_key.is_file() or not recipient_cert.is_file():
            raise FakeRecipientTrialError("synthetic certificate generation failed")

        # This is *file placement*, not access-control separation. Both mock
        # roles run as the same sandbox user. Only fake keys exist here.
        public_copy.write_bytes(recipient_cert.read_bytes())
        cipher = _invoke([
            "cms", "-encrypt", "-binary", "-outform", "DER",
            "-aes-256-gcm", "-recip", str(public_copy),
        ], data=FAKE_PACKET)
        if cipher.returncode != 0 or not cipher.stdout:
            raise FakeRecipientTrialError("fake recipient encryption failed")
        envelope.write_bytes(cipher.stdout)

        alg = _invoke([
            "cms", "-cmsout", "-print", "-inform", "DER",
            "-in", str(envelope),
        ])
        if alg.returncode != 0 or b"aes-256-gcm" not in alg.stdout.lower():
            raise FakeRecipientTrialError("authenticated algorithm unverified")

        digest = hashlib.sha256(FAKE_PACKET).hexdigest()
        restored = _safe_decrypt(envelope, recipient_cert, private_key, digest)
        if restored != FAKE_PACKET:
            raise FakeRecipientTrialError("complete fake packet not recovered")

        changed = bytearray(envelope.read_bytes())
        changed[-1] ^= 0x01
        altered.write_bytes(changed)
        untrusted = _invoke([
            "cms", "-decrypt", "-binary", "-inform", "DER",
            "-in", str(altered), "-recip", str(recipient_cert),
            "-inkey", str(private_key),
        ])
        # Critically, OpenSSL can emit provisional stdout even on failure.
        # Do not surface its contents, and verify the safe wrapper refuses it.
        discarded = _safe_decrypt(altered, recipient_cert, private_key, digest)
        receipt = {
            "synthetic_only": True,
            "rsa_certificate_generated": True,
            "aes_256_gcm_confirmed": True,
            "fake_packet_digest_verified": True,
            "separate_subprocess_recovery_pass": True,
            "tampered_ciphertext_rejected": untrusted.returncode != 0,
            "tampered_provisional_stdout_was_possible": bool(untrusted.stdout),
            "unsafe_plaintext_returned_to_safe_caller": discarded is not None,
            "mock_encryptor_private_key_file_present": any(
                f.suffix in {".key", ".pfx"} or "key" in f.name
                for f in encryptor.iterdir()
            ),
            "plaintext_packet_file_created": False,
            "different_os_principals_tested": False,
            "owner_key_custody_qualified": False,
            "real_gold_custody_qualified": False,
        }
        if not receipt["tampered_ciphertext_rejected"]:
            raise FakeRecipientTrialError("corruption was not rejected")
        if receipt["unsafe_plaintext_returned_to_safe_caller"]:
            raise FakeRecipientTrialError("unsafe provisional plaintext escaped")
        return receipt


if __name__ == "__main__":
    print(json.dumps(run_demo(), sort_keys=True))
