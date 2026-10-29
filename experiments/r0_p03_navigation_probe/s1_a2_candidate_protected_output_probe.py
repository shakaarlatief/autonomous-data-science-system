"""Source-free A2 candidate-to-owner protected output probe.

This executable is intentionally NOT an operational historical reviewer
ledger, recipient-account provisioner, or author-world release mechanism.
The only accepted source inputs are the two previously verified invented
file-fidelity fixtures, identified by their exact byte length and SHA-256.
The variable-length output adds optional explicitly absent fictional records
to exercise completeness accounting. The candidate generates fresh private
canaries and never writes the plaintext report to disk.

The public-certificate sender and owner-held private-key reader are separate
subcommands. Only the owner may invoke the latter in an environment whose
credential and storage boundary the owner has separately approved. A successful
CMS authentication demonstrates payload integrity and possession of the
recipient key, but does NOT demonstrate owner-only OS privileges, provider
confidentiality, a distinct independent reviewer, challenger admission or
denial from the eventual primary-author route.

AES-256-GCM CMS decryption may release provisional plaintext to a subprocess
buffer before its final tag check. This code discards ALL decrypt output unless
the process succeeded, the envelope digest matched independently, and complete
canonical fictional schema validation passed. Errors emit fixed public-safe
codes and never print plaintext, canaries, private paths or key material.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import getpass
from pathlib import Path
import re
import secrets
import shutil
import subprocess
import sys
from typing import Any

MARKER = "ADS_S1_A2_PROTECTED_OUTPUT_SOURCE_FREE_ONLY"
FORMAT = "ads-s1-a2-source-free-owner-envelope-v1"
OUTPUT_NAME = "a2_candidate_protected_source_free_v1.cms"
RECEIPT_NAME = "a2_candidate_protected_source_free_receipt.json"
MAX_PLAINTEXT = 8192
MAX_CIPHERTEXT = 32000
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
CANARY = re.compile(r"A2_FICTIONAL_PRIVATE_CANARY_[0-9a-f]{48}\Z")
REQUIRED = (
    ("a2_fake_unicode", 193,
     "8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb",
     "UTF8_CRLF"),
    ("a2_fake_png", 291,
     "fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f",
     "PNG_RGB"),
)
OPTIONAL_COUNT_MAX = 3
FIELDS = frozenset({
    "format", "marker", "synthetic_only", "candidate_actor", "challenge_state",
    "actual_independence_qualified", "real_source_reviewed",
    "restricted_output_qualified", "report_nonce", "records",
})
RECORD_FIELDS = frozenset({
    "fixture_id", "delivered", "inspected", "byte_count",
    "source_sha256", "representation", "disposition", "private_canary",
})
# Only these source-free diagnostic identifiers may leave the owner's private
# verifier. Exception text, OpenSSL stderr, decrypted data, key paths, report
# contents and passphrase properties must never be printed.
OWNER_SAFE_HOLD_CODES = frozenset({
    "OWNER_PASSPHRASE_INPUT_INVALID",
    "OWNER_INPUT_NOT_AVAILABLE",
    "CIPHERTEXT_INTEGRITY_MISMATCH",
    "PUBLIC_CERT_NOT_READABLE",
    "PUBLIC_CERT_FORMAT_INVALID",
    "PUBLIC_CERT_VERIFICATION_ERROR",
    "PUBLIC_CERT_VERIFICATION_FAILED",
    "CMS_DECRYPTION_EXECUTION_FAILED",
    "CMS_AUTHENTICATION_FAILED",
    "REPORT_SIZE_INVALID",
    "REPORT_JSON_INVALID",
    "SCHEMA_FIELDS_INVALID",
    "DUPLICATE_JSON_FIELD",
    "NONCANONICAL_REPORT",
    "REPORT_IDENTITY_INVALID",
    "ROLE_OR_SOURCE_HOLD_MISSING",
    "REPORT_NONCE_INVALID",
    "RECORD_COMPLETENESS_INVALID",
    "PRIVATE_RECORD_ID_INVALID",
    "REQUIRED_FAKE_RECORD_INVALID",
    "OPTIONAL_FAKE_HOLD_INVALID",
    "PRIVATE_CANARY_DUPLICATED",
    "OPENSSL_NOT_AVAILABLE",
    "CIPHERTEXT_DIGEST_ARGUMENT_INVALID",
})


class ProbeHold(ValueError):
    """Reject an incomplete, invalid, untrusted or out-of-scope probe input."""


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _canonical(value: object) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("ascii")


def _unique_json(pairs: list[tuple[str, object]]) -> dict[str, object]:
    data: dict[str, object] = {}
    for k, v in pairs:
        if k in data:
            raise ProbeHold("DUPLICATE_JSON_FIELD")
        data[k] = v
    return data


def _keys(obj: object, expected: frozenset[str]) -> dict[str, Any]:
    if not isinstance(obj, dict) or set(obj) != expected:
        raise ProbeHold("SCHEMA_FIELDS_INVALID")
    return obj


def validate_report(raw: bytes) -> dict[str, Any]:
    """Reject anything except a complete canonical invented-source report.

    This strict check is applied only *after* CMS successful return. It
    establishes local byte-level report consistency, not confidentiality
    against another process, adversarial model or hosting platform.
    """
    if not isinstance(raw, bytes) or not 200 <= len(raw) <= MAX_PLAINTEXT:
        raise ProbeHold("REPORT_SIZE_INVALID")
    try:
        document = json.loads(raw.decode("ascii"), object_pairs_hook=_unique_json,
                              parse_constant=lambda _: (_ for _ in ()).throw(
                                  ProbeHold("NONFINITE_JSON_NUMBER")))
    except (UnicodeError, ValueError) as exc:
        raise ProbeHold("REPORT_JSON_INVALID") from exc
    obj = _keys(document, FIELDS)
    if raw != _canonical(obj):
        raise ProbeHold("NONCANONICAL_REPORT")
    if (obj["format"] != FORMAT or obj["marker"] != MARKER or
        type(obj["synthetic_only"]) is not bool or not obj["synthetic_only"] or
        obj["candidate_actor"] != "PROSPECTIVE_UNADMITTED_REVIEWER" or
        obj["challenge_state"] != "NOT_CHALLENGED"):
        raise ProbeHold("REPORT_IDENTITY_INVALID")
    for name in (
        "actual_independence_qualified", "real_source_reviewed",
        "restricted_output_qualified",
    ):
        if type(obj[name]) is not bool or obj[name]:
            raise ProbeHold("ROLE_OR_SOURCE_HOLD_MISSING")
    nonce = obj["report_nonce"]
    if not isinstance(nonce, str) or not re.fullmatch("[0-9a-f]{48}", nonce):
        raise ProbeHold("REPORT_NONCE_INVALID")
    records = obj["records"]
    if not isinstance(records, list) or not 2 <= len(records) <= 2 + OPTIONAL_COUNT_MAX:
        raise ProbeHold("RECORD_COMPLETENESS_INVALID")
    expected_ids = [item[0] for item in REQUIRED] + [
        f"a2_fake_optional_{n}" for n in range(len(records) - 2)
    ]
    for record, name in zip(records, expected_ids, strict=True):
        r = _keys(record, RECORD_FIELDS)
        if r["fixture_id"] != name or not isinstance(r["private_canary"], str) or \
           not CANARY.fullmatch(r["private_canary"]):
            raise ProbeHold("PRIVATE_RECORD_ID_INVALID")
        if name in {fixture[0] for fixture in REQUIRED}:
            source = next(item for item in REQUIRED if item[0] == name)
            if (r["delivered"] is not True or r["inspected"] is not True or
                type(r["byte_count"]) is not int or
                r["byte_count"] != source[1] or
                r["source_sha256"] != source[2] or
                r["representation"] != source[3] or
                r["disposition"] != "FAKE_HOLD_PENDING_CHALLENGE"):
                raise ProbeHold("REQUIRED_FAKE_RECORD_INVALID")
        else:
            if (r["delivered"] is not False or r["inspected"] is not False or
                type(r["byte_count"]) is not int or r["byte_count"] != 0 or
                r["source_sha256"] != "0" * 64 or
                r["representation"] != "NOT_DELIVERED" or
                r["disposition"] != "FAKE_HOLD_MISSING_BYTES"):
                raise ProbeHold("OPTIONAL_FAKE_HOLD_INVALID")
    canaries = [r["private_canary"] for r in records]
    if len(set(canaries)) != len(canaries):
        raise ProbeHold("PRIVATE_CANARY_DUPLICATED")
    return obj


def build_source_free_report(text_bytes: bytes, png_bytes: bytes,
                             optional_missing: int = 1) -> bytes:
    """Construct a *new* synthetic-only report from exactly verified fixtures.

    A missing optional record is explicitly held, never silently omitted or
    counted as inspected. Random canaries are generated only in the candidate
    runtime; none of the concrete values are part of the published script,
    the public transport receipt, or coordinator-visible instrumentation.
    """
    if type(optional_missing) is not int or not 0 <= optional_missing <= OPTIONAL_COUNT_MAX:
        raise ProbeHold("OPTIONAL_COUNT_INVALID")
    for raw, (_, expected_size, sha, _) in zip(
        (text_bytes, png_bytes), REQUIRED, strict=True
    ):
        if len(raw) != expected_size or digest(raw) != sha:
            raise ProbeHold("RECEIVED_FAKE_SOURCE_MISMATCH")
    records: list[dict[str, object]] = []
    for name, size, sha, representation in REQUIRED:
        records.append({
            "fixture_id": name, "byte_count": size, "source_sha256": sha,
            "representation": representation, "delivered": True,
            "inspected": True, "disposition": "FAKE_HOLD_PENDING_CHALLENGE",
            "private_canary": "A2_FICTIONAL_PRIVATE_CANARY_" + secrets.token_hex(24),
        })
    for index in range(optional_missing):
        records.append({
            "fixture_id": f"a2_fake_optional_{index}",
            "byte_count": 0, "source_sha256": "0" * 64,
            "representation": "NOT_DELIVERED", "delivered": False,
            "inspected": False, "disposition": "FAKE_HOLD_MISSING_BYTES",
            "private_canary": "A2_FICTIONAL_PRIVATE_CANARY_" + secrets.token_hex(24),
        })
    output = _canonical({
        "format": FORMAT, "marker": MARKER, "synthetic_only": True,
        "candidate_actor": "PROSPECTIVE_UNADMITTED_REVIEWER",
        "challenge_state": "NOT_CHALLENGED",
        "actual_independence_qualified": False, "real_source_reviewed": False,
        "restricted_output_qualified": False,
        "report_nonce": secrets.token_hex(24), "records": records,
    })
    validate_report(output)
    return output


def _openssl(executable: str | None = None) -> str:
    found = executable or shutil.which("openssl")
    if not found and sys.platform == "win32":
        fallback = Path(r"C:\Program Files\Git\usr\bin\openssl.exe")
        if fallback.is_file():
            found = str(fallback)
    if not found:
        raise ProbeHold("OPENSSL_NOT_AVAILABLE")
    return found


def _public_certificate(cert: Path, openssl: str) -> None:
    if not cert.is_file() or cert.is_symlink():
        raise ProbeHold("PUBLIC_CERT_NOT_READABLE")
    data = cert.read_bytes()
    if not data.startswith(b"-----BEGIN CERTIFICATE-----") or \
       b"PRIVATE KEY" in data or len(data) > 10000:
        raise ProbeHold("PUBLIC_CERT_FORMAT_INVALID")
    try:
        result = subprocess.run([openssl, "x509", "-in", str(cert), "-noout"],
                                capture_output=True, timeout=20, check=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProbeHold("PUBLIC_CERT_VERIFICATION_ERROR") from exc
    if result.returncode:
        raise ProbeHold("PUBLIC_CERT_VERIFICATION_FAILED")


def seal_report(raw: bytes, cert: Path, output: Path, *, executable: str | None = None
                ) -> dict[str, object]:
    """Encrypt in memory and emit a safe receipt, never a plaintext report.

    Output uses exclusive creation to prevent overwriting another review
    attempt. The caller must use a fresh approved public recipient certificate.
    This code has no private-key argument and cannot decrypt a report.
    """
    validate_report(raw)
    if output.name != OUTPUT_NAME or not output.parent.is_dir() or \
       output.is_symlink() or output.exists():
        raise ProbeHold("OUTPUT_LOCATION_OR_VERSION_INVALID")
    openssl = _openssl(executable)
    _public_certificate(cert, openssl)
    try:
        result = subprocess.run(
            [openssl, "cms", "-encrypt", "-binary", "-outform", "DER",
             "-aes-256-gcm", "-recip", str(cert)],
            input=raw, capture_output=True, timeout=25, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProbeHold("CMS_ENCRYPTION_EXECUTION_FAILED") from exc
    ciphertext = result.stdout
    if result.returncode != 0 or not 100 <= len(ciphertext) <= MAX_CIPHERTEXT:
        raise ProbeHold("CMS_ENCRYPTION_FAILED")
    if raw in ciphertext or b"A2_FICTIONAL_PRIVATE_CANARY_" in ciphertext:
        raise ProbeHold("PLAINTEXT_VISIBLE_IN_ENVELOPE")
    with output.open("xb") as stream:
        stream.write(ciphertext)
        stream.flush()
    return {
        "source_free_only": True, "ciphertext_file": OUTPUT_NAME,
        "ciphertext_sha256": digest(ciphertext),
        "ciphertext_bytes": len(ciphertext),
        "private_report_printed": False,
        "owner_private_custody_qualified": False,
        "actual_reviewer_admitted": False, "real_source_reviewed": False,
    }


def owner_verify_ciphertext(ciphertext: Path, cert: Path, private_key: Path,
                            expected_cipher_sha256: str, *,
                            passphrase: bytes,
                            executable: str | None = None) -> dict[str, object]:
    """Owner-side full in-memory recovery without private report disclosure.

    An owner must run this function outside the exposed coordinator and only
    with a recipient key and destination whose access has been assessed. The
    local agent is never entitled to execute it against a real owner key.
    """
    if not isinstance(expected_cipher_sha256, str) or \
       not HEX64.fullmatch(expected_cipher_sha256):
        raise ProbeHold("CIPHERTEXT_DIGEST_ARGUMENT_INVALID")
    # The owner key already exists and its passphrase was accepted by OpenSSL
    # during creation. Do not impose a new eight-byte minimum when reading it:
    # authentication of the encrypted key and CMS report remains mandatory.
    # Still reject empty/line-delimited stdin input and unbounded input size.
    if not isinstance(passphrase, bytes) or not 1 <= len(passphrase) <= 256 or \
       b"\n" in passphrase or b"\r" in passphrase:
        raise ProbeHold("OWNER_PASSPHRASE_INPUT_INVALID")
    if ciphertext.name != OUTPUT_NAME or not ciphertext.is_file() or \
       ciphertext.is_symlink() or not private_key.is_file() or \
       private_key.is_symlink():
        raise ProbeHold("OWNER_INPUT_NOT_AVAILABLE")
    sealed = ciphertext.read_bytes()
    if not 100 <= len(sealed) <= MAX_CIPHERTEXT or \
       digest(sealed) != expected_cipher_sha256:
        raise ProbeHold("CIPHERTEXT_INTEGRITY_MISMATCH")
    openssl = _openssl(executable)
    _public_certificate(cert, openssl)
    try:
        result = subprocess.run(
            [openssl, "cms", "-decrypt", "-binary", "-inform", "DER",
             "-in", str(ciphertext), "-recip", str(cert),
             "-inkey", str(private_key), "-passin", "stdin"],
            input=passphrase + b"\n", capture_output=True,
            timeout=25, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProbeHold("CMS_DECRYPTION_EXECUTION_FAILED") from exc
    # Authentication may fail after a provisional plaintext output. Do not
    # inspect or expose result.stdout until the process exit status is success.
    if result.returncode:
        raise ProbeHold("CMS_AUTHENTICATION_FAILED")
    report = validate_report(result.stdout)
    return {
        "source_free_only": True,
        "owner_full_readback": "PASS",
        "ciphertext_integrity": "PASS",
        "report_schema_and_manifest": "PASS",
        "record_count": len(report["records"]),
        "private_canary_records_validated": len(report["records"]),
        "private_report_printed": False,
        "owner_exclusive_access_proven": False,
        "author_route_access_denial_proven": False,
        "real_reviewer_admitted": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    seal = sub.add_parser("seal", help="Candidate: source-free fixtures -> CMS ciphertext")
    seal.add_argument("--text-fixture", required=True, type=Path)
    seal.add_argument("--png-fixture", required=True, type=Path)
    seal.add_argument("--recipient-public-cert", required=True, type=Path)
    seal.add_argument("--output", required=True, type=Path)
    seal.add_argument("--optional-missing", type=int, default=1)
    seal.add_argument("--openssl")
    owner = sub.add_parser("owner-verify", help="Owner only: authenticate full report privately")
    owner.add_argument("--ciphertext", type=Path, required=True)
    owner.add_argument("--recipient-public-cert", type=Path, required=True)
    owner.add_argument("--recipient-private-key", type=Path, required=True)
    owner.add_argument("--expected-ciphertext-sha256", required=True)
    owner.add_argument("--openssl")
    try:
        args = parser.parse_args()
        if args.command == "seal":
            raw = build_source_free_report(
                args.text_fixture.read_bytes(), args.png_fixture.read_bytes(),
                args.optional_missing,
            )
            receipt = seal_report(raw, args.recipient_public_cert, args.output,
                                  executable=args.openssl)
        else:
            if not sys.stdin.isatty():
                raise ProbeHold("OWNER_INTERACTIVE_PASSPHRASE_REQUIRED")
            owner_passphrase = getpass.getpass(
                "Passphrase for owner-held encrypted test key: "
            ).encode("utf-8")
            receipt = owner_verify_ciphertext(
                args.ciphertext, args.recipient_public_cert,
                args.recipient_private_key, args.expected_ciphertext_sha256,
                passphrase=owner_passphrase, executable=args.openssl,
            )
        print(_canonical(receipt).decode("ascii"))
        return 0
    except ProbeHold as exc:
        # Diagnostic-only stage identifier: a static allowlist of synthetic
        # verifier errors. Never print arbitrary exception text or OpenSSL
        # stderr because they may contain owner-only paths or private output.
        if args.command == "owner-verify":
            code = str(exc)
            safe_code = code if code in OWNER_SAFE_HOLD_CODES else "OWNER_UNCLASSIFIED_HOLD"
            print(f"SOURCE_FREE_A2_OWNER_HOLD_CODE={safe_code}", file=sys.stderr)
        print("SOURCE_FREE_A2_PROBE_HOLD", file=sys.stderr)
        return 2
    except (FileNotFoundError, FileExistsError, OSError, ValueError):
        # No exception messages: a process or path error could contain an
        # owner-only directory, private filename, or certificate material.
        print("SOURCE_FREE_A2_PROBE_HOLD", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
