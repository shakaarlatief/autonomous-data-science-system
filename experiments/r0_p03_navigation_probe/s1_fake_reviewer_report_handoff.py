"""Standalone fictional-only R0-P03 reviewer report sealing and private readback.

This script is deliberately independent of the ADS Python package so that a
separate Temporary Chat can receive only this file and a public certificate.
It does not inspect actual project sources, reference gold or reviewer records.

The exact fictional source/record identifiers, permitted private note tokens,
disposition tokens and output schema are closed and hard-coded. This is a
source-free format and mechanics test, not a generic report encryptor or a
qualified secret-storage application. "verify" can authenticate and parse the
entire fake report without emitting its private note tokens to stdout.

Both operations require an installed OpenSSL CMS implementation with AES-256-GCM.
The private recipient key is accepted ONLY by the verify operation. The sender
must never receive or read a private key. False outputs, truncated records and
modified AEAD ciphertext fail closed. Provider transcripts and host OS file
access are outside these methods' assurance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
from typing import Any, Mapping

MARKER = "S1_FICTIONAL_REVIEWER_REPORT_NO_REAL_PROJECT_MATERIAL"
FORMAT = "s1-fictional-reviewer-report-v1"
MANIFEST = "s1-fictional-three-record-source-manifest-v1"
OUTPUT = "R0_P03_FAKE_REVIEWER_REPORT.cms"
MAX_PLAINTEXT = 16384
MAX_CIPHERTEXT = 65536
FAKE_SOURCES: Mapping[str, bytes] = {
    "s1_fake_history": b"S1_FAKE_SOURCE_HISTORY\nA fictional bridge was proposed at dawn.\n",
    "s1_fake_rule": b"S1_FAKE_SOURCE_RULE\nA fictional bridge is closed during festivals.\n",
    "s1_fake_design": b"S1_FAKE_SOURCE_DESIGN\nFAKE_PRIVATE_CUE: prefer fictional option K.\n",
}
NOTE_CODES = frozenset({
    "FAKE_NOTE_OBSERVATION_ONLY",
    "FAKE_NOTE_CONTROLLING_EXCEPTION",
    "FAKE_NOTE_RESTRICTED_DESIGN_CUE",
    "FAKE_NOTE_MISSING_SOURCE_BYTES",
    "FAKE_NOTE_UNINSPECTED_REPRESENTATION",
})
DISPOSITIONS = frozenset({
    "CANDIDATE_FULL",
    "CANDIDATE_EXCERPT",
    "AUXILIARY_EVIDENCE_ONLY",
    "PROHIBIT_DESIGN_OR_GOLD",
    "HOLD_FOR_SOURCE_REVIEW",
    "UNSUPPORTED_REPRESENTATION",
})
SCOPES = frozenset({"COMPLETE_FILE", "EXACT_SPAN", "REPRESENTATION_COMPONENT"})
ROSTER = frozenset(FAKE_SOURCES)
RECEIPT_FIELDS = frozenset({
    "synthetic_only", "report_format", "ciphertext_filename",
    "ciphertext_sha256", "ciphertext_bytes", "private_report_printed",
    "real_custody_qualified",
})
HEX_SHA = re.compile(r"[0-9a-f]{64}\Z")


class FakeReportError(ValueError):
    """Reject nonfictional, incomplete, malformed or inconsistent inputs."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _strict_fields(data: object, keys: set[str] | frozenset[str], description: str) -> dict[str, Any]:
    if not isinstance(data, dict) or set(data) != set(keys):
        raise FakeReportError("Unexpected " + description + " fields")
    return data


def _bool(value: object, expected: bool | None = None) -> bool:
    if type(value) is not bool or (expected is not None and value is not expected):
        raise FakeReportError("Invalid strict fictional boolean")
    return value


def fake_report() -> dict[str, Any]:
    """Provide a three-item fixture; independently generated reports can vary.

    The fixture includes a harmless historical claim, an exception, and a
    deliberately invented restricted design cue. This is not an R0-P03 source
    classification and is not a hidden experimental reference.
    """
    return {
        "format": FORMAT,
        "marker": MARKER,
        "manifest": MANIFEST,
        "synthetic_only": True,
        "reviewer_exposure": "DECLARED_SYNTHETIC_ONLY_UNVERIFIED",
        "challenge": "NOT_CHALLENGED",
        "actual_independent_actor_verified": False,
        "real_source_reviewed": False,
        "source_world_admitted": False,
        "records": [
            {
                "source_id": "s1_fake_history",
                "source_sha256": _sha(FAKE_SOURCES["s1_fake_history"]),
                "delivered": True,
                "inspected": True,
                "scope": "COMPLETE_FILE",
                "disposition": "CANDIDATE_FULL",
                "private_notes": ["FAKE_NOTE_OBSERVATION_ONLY"],
            },
            {
                "source_id": "s1_fake_rule",
                "source_sha256": _sha(FAKE_SOURCES["s1_fake_rule"]),
                "delivered": True,
                "inspected": True,
                "scope": "EXACT_SPAN",
                "disposition": "CANDIDATE_EXCERPT",
                "private_notes": ["FAKE_NOTE_CONTROLLING_EXCEPTION"],
            },
            {
                "source_id": "s1_fake_design",
                "source_sha256": _sha(FAKE_SOURCES["s1_fake_design"]),
                "delivered": True,
                "inspected": True,
                "scope": "COMPLETE_FILE",
                "disposition": "PROHIBIT_DESIGN_OR_GOLD",
                "private_notes": ["FAKE_NOTE_RESTRICTED_DESIGN_CUE"],
            },
        ],
    }


def validate_fake_report(value: object) -> dict[str, Any]:
    """Accept complete variable decisions over exactly the three fake inputs.

    This validates shape, provenance identifiers, delivery/inspection
    consistency and absence of unexpected plaintext fields. It CANNOT decide
    whether semantic dispositions are true in a real document. The source
    hashes here are hashes of hardcoded invented text, not a live repository.
    """
    obj = _strict_fields(value, {
        "format", "marker", "manifest", "synthetic_only", "reviewer_exposure",
        "challenge", "actual_independent_actor_verified", "real_source_reviewed",
        "source_world_admitted", "records",
    }, "report")
    if (
        obj["format"] != FORMAT
        or obj["marker"] != MARKER
        or obj["manifest"] != MANIFEST
        or obj["reviewer_exposure"] not in {
            "DECLARED_SYNTHETIC_ONLY_UNVERIFIED", "UNKNOWN",
        }
        or obj["challenge"] not in {"NOT_CHALLENGED", "DISPUTED"}
    ):
        raise FakeReportError("Invalid fictional manifest, role or status")
    _bool(obj["synthetic_only"], True)
    for key in ("actual_independent_actor_verified", "real_source_reviewed", "source_world_admitted"):
        _bool(obj[key], False)
    records = obj["records"]
    if not isinstance(records, list) or len(records) != len(ROSTER):
        raise FakeReportError("Complete three-record accounting is required")
    seen: set[str] = set()
    for row in records:
        item = _strict_fields(row, {
            "source_id", "source_sha256", "delivered", "inspected",
            "scope", "disposition", "private_notes",
        }, "source record")
        source_id = item["source_id"]
        if not isinstance(source_id, str) or source_id not in FAKE_SOURCES or source_id in seen:
            raise FakeReportError("Nonfictional, duplicate or unknown source ID")
        seen.add(source_id)
        if item["source_sha256"] != _sha(FAKE_SOURCES[source_id]):
            raise FakeReportError("Fictional expected source identity mismatch")
        delivered = _bool(item["delivered"])
        inspected = _bool(item["inspected"])
        scope = item["scope"]
        disposition = item["disposition"]
        if scope not in SCOPES or disposition not in DISPOSITIONS:
            raise FakeReportError("Unknown typed scope or disposition")
        if not delivered and inspected:
            raise FakeReportError("Undelivered source cannot have been inspected")
        if not delivered and disposition != "HOLD_FOR_SOURCE_REVIEW":
            raise FakeReportError("Missing source must stay HOLD")
        if not inspected and delivered and disposition not in {
            "HOLD_FOR_SOURCE_REVIEW", "UNSUPPORTED_REPRESENTATION",
        }:
            raise FakeReportError("Uninspected source cannot be a candidate")
        if scope != "COMPLETE_FILE" and disposition == "CANDIDATE_FULL":
            raise FakeReportError("Full-file candidate must be scoped to complete file")
        if scope != "EXACT_SPAN" and disposition == "CANDIDATE_EXCERPT":
            raise FakeReportError("Exact excerpt candidate needs exact-span scope")
        if scope != "REPRESENTATION_COMPONENT" and disposition == "UNSUPPORTED_REPRESENTATION":
            raise FakeReportError("Unsupported representation belongs to component scope")
        notes = item["private_notes"]
        if (not isinstance(notes, list) or not 1 <= len(notes) <= 3
                or any(not isinstance(s, str) or s not in NOTE_CODES for s in notes)
                or len(set(notes)) != len(notes)):
            raise FakeReportError("Only known fictional private note codes allowed")
    if seen != ROSTER:
        raise FakeReportError("Incomplete fictional source roster")
    return obj


def canonical_fake_bytes(report: object) -> bytes:
    accepted = validate_fake_report(report)
    raw = (json.dumps(accepted, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode()
    if len(raw) > MAX_PLAINTEXT:
        raise FakeReportError("Fictional reviewer report exceeds maximum size")
    return raw


def _openssl_executable() -> str:
    """Locate OpenSSL via PATH or the previously qualified Git-for-Windows path.

    Windows Codex command environments can have Git's OpenSSL installed yet
    not on PATH, as already documented in earlier fake-CMS recipient trials.
    This explicit known executable fallback changes only executable lookup;
    it never changes encryption, source permission or recipient validation.
    """
    binary = shutil.which("openssl")
    if binary:
        return binary
    if sys.platform == "win32":
        candidate = Path(r"C:\Program Files\Git\usr\bin\openssl.exe")
        if candidate.is_file() and not candidate.is_symlink():
            return str(candidate)
    raise FakeReportError("OpenSSL unavailable; refuse insecure fallback")


def _public_certificate(path: Path) -> None:
    if not path.is_file() or path.is_symlink() or not 0 < path.stat().st_size < 65536:
        raise FakeReportError("Missing, symlinked or oversized public certificate")
    data = path.read_bytes()
    if b"BEGIN CERTIFICATE" not in data or b"PRIVATE KEY" in data:
        raise FakeReportError("Only public certificate may be given to sender")
    process = subprocess.run(
        [_openssl_executable(), "x509", "-in", str(path), "-noout"],
        capture_output=True, timeout=20, check=False,
    )
    if process.returncode:
        raise FakeReportError("Unable to verify public certificate")


def seal_fake_report(report: object, certificate: Path, output: Path) -> dict[str, object]:
    """Write only ciphertext, never private note codes or a plaintext report file."""
    fake = canonical_fake_bytes(report)
    if output.name != OUTPUT or not output.parent.is_dir() or output.is_symlink():
        raise FakeReportError("Unexpected fictional-only ciphertext output location/name")
    if output.exists():
        raise FileExistsError("Refuse overwriting an earlier handoff")
    _public_certificate(certificate)
    result = subprocess.run(
        [_openssl_executable(), "cms", "-encrypt", "-binary",
         "-outform", "DER", "-aes-256-gcm", "-recip", str(certificate)],
        input=fake, capture_output=True, timeout=25, check=False,
    )
    if result.returncode or not 100 <= len(result.stdout) <= MAX_CIPHERTEXT:
        raise FakeReportError("Authenticated CMS sealing failed")
    if fake in result.stdout or any(note.encode() in result.stdout for note in NOTE_CODES):
        raise FakeReportError("Fictional private contents visible in ciphertext")
    with output.open("xb") as handle:
        handle.write(result.stdout)
        handle.flush()
    receipt = {
        "synthetic_only": True,
        "report_format": FORMAT,
        "ciphertext_filename": OUTPUT,
        "ciphertext_sha256": _sha(result.stdout),
        "ciphertext_bytes": len(result.stdout),
        "private_report_printed": False,
        "real_custody_qualified": False,
    }
    validate_public_receipt(receipt)
    return receipt


def validate_public_receipt(value: object) -> dict[str, object]:
    """Accept only the fixed, nonanswer-bearing public receipt field set."""
    r = _strict_fields(value, RECEIPT_FIELDS, "public receipt")
    _bool(r["synthetic_only"], True)
    _bool(r["private_report_printed"], False)
    _bool(r["real_custody_qualified"], False)
    if r["report_format"] != FORMAT or r["ciphertext_filename"] != OUTPUT:
        raise FakeReportError("Unexpected public report identity")
    if (not isinstance(r["ciphertext_sha256"], str) or
        not HEX_SHA.fullmatch(r["ciphertext_sha256"]) or
        type(r["ciphertext_bytes"]) is not int or
        not 100 <= r["ciphertext_bytes"] <= MAX_CIPHERTEXT):
        raise FakeReportError("Invalid public ciphertext digest/size")
    return r


def owner_fake_readback(ciphertext: Path, certificate: Path,
                        private_key: Path, expected_ciphertext_digest: str) -> bool:
    """Verify full fabricated report privately; emit no actual report content.

    IMPORTANT: OpenSSL may put *unauthenticated provisional plaintext* in its
    captured stdout when GCM authentication ultimately fails. Ignore stdout
    unless the subprocess returned success; do not print exception stderr,
    partial plaintext, or decrypted fake notes under any failure path.
    """
    if (not isinstance(expected_ciphertext_digest, str)
            or not HEX_SHA.fullmatch(expected_ciphertext_digest)):
        return False
    try:
        if (not ciphertext.is_file() or ciphertext.is_symlink()
                or not 100 <= ciphertext.stat().st_size <= MAX_CIPHERTEXT
                or not certificate.is_file() or not private_key.is_file()
                or certificate.is_symlink() or private_key.is_symlink()
                or _sha(ciphertext.read_bytes()) != expected_ciphertext_digest):
            return False
        response = subprocess.run(
            [_openssl_executable(), "cms", "-decrypt", "-binary", "-inform", "DER",
             "-in", str(ciphertext), "-recip", str(certificate),
             "-inkey", str(private_key)],
            capture_output=True, timeout=25, check=False,
        )
        if response.returncode or not 0 < len(response.stdout) <= MAX_PLAINTEXT:
            return False
        decoded = json.loads(response.stdout.decode("utf-8"))
        return canonical_fake_bytes(decoded) == response.stdout
    except (OSError, ValueError, UnicodeError, subprocess.SubprocessError):
        return False


def _main() -> int:
    parser = argparse.ArgumentParser(description="Only a fabricated S1 reviewer report")
    sub = parser.add_subparsers(dest="operation", required=True)
    send = sub.add_parser("send")
    send.add_argument("--cert", required=True, type=Path)
    send.add_argument("--output", required=True, type=Path)
    verify = sub.add_parser("verify")
    verify.add_argument("--cert", required=True, type=Path)
    verify.add_argument("--private-key", required=True, type=Path)
    verify.add_argument("--ciphertext", required=True, type=Path)
    verify.add_argument("--expected-ciphertext-sha256", required=True)
    args = parser.parse_args()
    if args.operation == "send":
        raw = sys.stdin.buffer.read(MAX_PLAINTEXT + 1)
        if len(raw) > MAX_PLAINTEXT:
            raise FakeReportError("Synthetic input is too large")
        result = seal_fake_report(json.loads(raw.decode("utf-8")), args.cert, args.output)
        print(json.dumps(result, sort_keys=True))
        return 0
    result = owner_fake_readback(args.ciphertext, args.cert, args.private_key,
                                 args.expected_ciphertext_sha256)
    print("S1_FAKE_OWNER_REVIEW_READBACK=PASS" if result
          else "S1_FAKE_OWNER_REVIEW_READBACK=FAIL")
    return 0 if result else 2


if __name__ == "__main__":
    try:
        raise SystemExit(_main())
    except (FakeReportError, ValueError, OSError, subprocess.SubprocessError):
        # Do not print the invalid record, certificate or private source bytes.
        print("S1_FAKE_HANDOFF=FAIL", file=sys.stderr)
        raise SystemExit(2)
