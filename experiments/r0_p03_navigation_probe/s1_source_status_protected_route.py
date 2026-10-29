"""Bounded owner-mediated CMS transport for a real-source S1 reviewer report.

This is NOT an accepted source-status method, reviewer admission, source
disclosure authorization, or proof of same-user process isolation. The tool
validates one exact local review ZIP and complete original-file accounting.
Reviewer-only reasoning is never emitted as public stdout, receipt, or Git.
The sender may pass a report object directly to seal() without writing
plaintext. The CLI accepts report JSON over stdin, not an argv value.

The owner verifier decrypts solely into process memory, discards any provisional
AES-GCM plaintext when OpenSSL fails, validates canonical report completeness,
and returns only fixed safe status markers. Its encrypted-key passphrase is
collected locally and sent only on the OpenSSL subprocess stdin. Do not run an
owner-verification operation via an exposed coordinator or an untrusted chat.
"""
from __future__ import annotations

import argparse
from hashlib import sha1, sha256
import getpass
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from typing import Any
from zipfile import ZipFile

FORMAT = "ads-r0-p03-s1-source-status-restricted-v1"
SOURCE_PIN = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
BATCH_ID = "R0_P03_FIRST_SOURCE_STATUS_REVIEW_WAVE_CANDIDATE_V1"
BATCH_ZIP_SHA256 = "c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
BATCH_MANIFEST_SHA256 = "6c175bbba3d35bc0432762a66e738fc80cadbc8ab16e1c804118d51486220e10"
CIPHERTEXT_FILENAME = "R0_P03_S1_WAVE0_OWNER_REVIEW.cms"
MAX_ARCHIVE_BYTES = 2_000_000
MAX_PLAINTEXT_BYTES = 250_000
MAX_CIPHERTEXT_BYTES = 400_000
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
HEX32 = re.compile(r"[0-9a-f]{32}\Z")
DISPOSITIONS = frozenset({
    "CANDIDATE_FULL", "CANDIDATE_EXCERPT", "AUXILIARY_EVIDENCE_ONLY",
    "PROHIBIT_DESIGN_OR_GOLD", "HOLD_FOR_SOURCE_REVIEW",
})
RECORD_FIELDS = frozenset({
    "path", "git_blob_oid", "sha256", "received", "inspected",
    "scope", "proposed_disposition", "proposed_claims",
    "source_bound_private_reasoning", "context_and_representation_gaps",
    "contamination_and_author_exposure_risks",
    "challenge_state",
})
REPORT_FIELDS = frozenset({
    "format", "batch_identifier", "source_ref", "batch_zip_sha256",
    "batch_manifest_sha256", "reviewer_role",
    "independence_not_cryptographically_proven", "method_status",
    "report_nonce", "restricted_reviewer_exposure_notes", "records",
    "authorization", "author_world",
})
MAX_FIELD_CHARS = 12_000


class RouteHold(ValueError):
    """Fixed failure scope; never include source-specific contents."""


def canonical(obj: object) -> bytes:
    try:
        return json.dumps(obj, sort_keys=True, ensure_ascii=True,
                          separators=(",", ":"), allow_nan=False).encode("ascii")
    except (ValueError, TypeError, UnicodeError) as exc:
        raise RouteHold("REPORT_NOT_CANONICALIZABLE") from exc


def digest(b: bytes) -> str:
    return sha256(b).hexdigest()


def unique_pairs(pairs: list[tuple[str, object]]) -> dict:
    ret: dict = {}
    for key, value in pairs:
        if key in ret:
            raise RouteHold("DUPLICATE_JSON_FIELD")
        ret[key] = value
    return ret


def safe_json(raw: bytes) -> dict:
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_pairs,
                           parse_constant=lambda _: (_ for _ in ()).throw(
                               RouteHold("NONFINITE_JSON_NUMBER")))
    except RouteHold:
        raise
    except (ValueError, UnicodeError, TypeError) as exc:
        raise RouteHold("REPORT_JSON_INVALID") from exc
    if not isinstance(value, dict):
        raise RouteHold("REPORT_OBJECT_INVALID")
    return value


def exact_fields(obj: object, names: frozenset[str], code: str) -> dict:
    if not isinstance(obj, dict) or set(obj) != names:
        raise RouteHold(code)
    return obj


def text_field(value: object, *, permit_empty: bool = True) -> str:
    if not isinstance(value, str) or len(value) > MAX_FIELD_CHARS:
        raise RouteHold("REPORT_TEXT_FIELD_INVALID")
    if not permit_empty and not value.strip():
        raise RouteHold("REPORT_REQUIRED_TEXT_MISSING")
    return value


def text_list(value: object) -> list[str]:
    if (not isinstance(value, list) or len(value) > 12 or
            any(not isinstance(x, str) for x in value)):
        raise RouteHold("REPORT_TEXT_LIST_INVALID")
    for val in value:
        text_field(val, permit_empty=False)
    return value


def load_batch(raw_zip: bytes) -> tuple[dict, list[dict]]:
    """Validate the complete original source ZIP, not just its outer digest.

    The zip is the owner-local artifact authored and verified in Validation 288.
    Fixed public hashes identify one approved-for-staging candidate, not
    authorization for reviewer access or an accepted source universe.
    """
    if not 1000 <= len(raw_zip) <= MAX_ARCHIVE_BYTES or digest(raw_zip) != BATCH_ZIP_SHA256:
        raise RouteHold("BATCH_ZIP_IDENTITY_INVALID")
    import io
    try:
        with ZipFile(io.BytesIO(raw_zip), "r") as archive:
            infos = archive.infolist()
            filenames = [x.filename for x in infos]
            if len(set(filenames)) != len(filenames):
                raise RouteHold("BATCH_DUPLICATE_MEMBER")
            if any(x.is_dir() or x.flag_bits & 1 for x in infos):
                raise RouteHold("BATCH_MEMBER_INVALID")
            if "SOURCE_MANIFEST.json" not in filenames or len(filenames) != 11:
                raise RouteHold("BATCH_MEMBER_COUNT_INVALID")
            for name in filenames:
                parts = PurePosixPath(name).parts
                if (name.startswith("/") or "\\" in name or ".." in parts or
                        name != str(PurePosixPath(name))):
                    raise RouteHold("BATCH_MEMBER_PATH_INVALID")
            raw_manifest = archive.read("SOURCE_MANIFEST.json")
            if digest(raw_manifest) != BATCH_MANIFEST_SHA256:
                raise RouteHold("BATCH_MANIFEST_DIGEST_INVALID")
            manifest = safe_json(raw_manifest)
            if (manifest.get("identifier") != BATCH_ID or
                    manifest.get("source_ref") != SOURCE_PIN or
                    manifest.get("selected_count") != 10 or
                    manifest.get("classification") !=
                    "OWNER_LOCAL_FIRST_WAVE_REVIEW_INPUT_NOT_AUTHOR_PACKET"):
                raise RouteHold("BATCH_MANIFEST_IDENTITY_INVALID")
            rows = manifest.get("source_manifest")
            if not isinstance(rows, list) or len(rows) != 10:
                raise RouteHold("BATCH_SOURCE_COUNT_INVALID")
            expected = {"SOURCE_MANIFEST.json"}
            for entry in rows:
                if not isinstance(entry, dict) or entry.get("admission") != "REVIEW_ONLY_NOT_ADMITTED":
                    raise RouteHold("BATCH_ENTRY_STATUS_INVALID")
                path = entry.get("path")
                if not isinstance(path, str):
                    raise RouteHold("BATCH_ENTRY_PATH_INVALID")
                name = "sources/" + path
                expected.add(name)
                if name not in filenames:
                    raise RouteHold("BATCH_SOURCE_MISSING")
                contents = archive.read(name)
                oid = sha1(b"blob " + str(len(contents)).encode("ascii") + b"\0" + contents).hexdigest()
                if (oid != entry.get("git_blob_oid") or
                        digest(contents) != entry.get("sha256") or
                        len(contents) != entry.get("bytes")):
                    raise RouteHold("BATCH_SOURCE_INTEGRITY_INVALID")
            if set(filenames) != expected:
                raise RouteHold("BATCH_UNDECLARED_MEMBER")
    except (OSError, KeyError, EOFError, RuntimeError) as exc:
        raise RouteHold("BATCH_ARCHIVE_UNREADABLE") from exc
    return manifest, rows


def validate_report(raw: bytes, batch_rows: list[dict]) -> dict:
    if not 200 <= len(raw) <= MAX_PLAINTEXT_BYTES:
        raise RouteHold("REPORT_SIZE_INVALID")
    obj = exact_fields(safe_json(raw), REPORT_FIELDS, "REPORT_SCHEMA_INVALID")
    if canonical(obj) != raw:
        raise RouteHold("REPORT_NOT_CANONICAL")
    if (obj["format"] != FORMAT or obj["batch_identifier"] != BATCH_ID or
            obj["source_ref"] != SOURCE_PIN or
            obj["batch_zip_sha256"] != BATCH_ZIP_SHA256 or
            obj["batch_manifest_sha256"] != BATCH_MANIFEST_SHA256 or
            obj["reviewer_role"] != "NON_ARM_SOURCE_STATUS_REVIEWER" or
            obj["independence_not_cryptographically_proven"] is not True or
            obj["method_status"] != "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED" or
            obj["authorization"] != "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE" or
            obj["author_world"] != "WORLD_UNFROZEN" or
            not isinstance(obj["report_nonce"], str) or
            HEX32.fullmatch(obj["report_nonce"]) is None):
        raise RouteHold("REPORT_IDENTITY_INVALID")
    text_field(obj["restricted_reviewer_exposure_notes"], permit_empty=False)
    records = obj["records"]
    if not isinstance(records, list) or len(records) != len(batch_rows):
        raise RouteHold("REPORT_INCOMPLETE")
    for actual, expected in zip(records, batch_rows, strict=True):
        record = exact_fields(actual, RECORD_FIELDS, "RECORD_SCHEMA_INVALID")
        if (record["path"] != expected["path"] or
                record["git_blob_oid"] != expected["git_blob_oid"] or
                record["sha256"] != expected["sha256"] or
                record["scope"] != "COMPLETE_FILE" or
                type(record["received"]) is not bool or not record["received"] or
                type(record["inspected"]) is not bool or
                record["proposed_disposition"] not in DISPOSITIONS or
                record["challenge_state"] != "CHALLENGE_PENDING"):
            raise RouteHold("RECORD_IDENTITY_OR_STATE_INVALID")
        # This first-wave transport is intentionally COMPLETE_FILE only.
        # Exact-span proposals require source-bound byte offsets, an excerpt
        # hash and separately inspected co-release context, which this v1
        # report format does not yet represent. Never invent that evidence.
        if record["proposed_disposition"] == "CANDIDATE_EXCERPT":
            raise RouteHold("RECORD_SCOPE_INVALID")
        if not record["inspected"] and record["proposed_disposition"] != "HOLD_FOR_SOURCE_REVIEW":
            raise RouteHold("UNINSPECTED_SOURCE_NOT_HELD")
        text_list(record["proposed_claims"])
        text_list(record["context_and_representation_gaps"])
        text_list(record["contamination_and_author_exposure_risks"])
        text_field(record["source_bound_private_reasoning"], permit_empty=False)
    return obj


def report_bytes(obj: dict, batch_rows: list[dict]) -> bytes:
    raw = canonical(obj)
    validate_report(raw, batch_rows)
    return raw


def openssl_path(explicit: str | None = None) -> str:
    if explicit is not None:
        candidate = Path(explicit)
        if not candidate.is_file() or candidate.is_symlink():
            raise RouteHold("OPENSSL_NOT_AVAILABLE")
        return str(candidate)
    executable = shutil.which("openssl")
    if executable:
        return executable
    if sys.platform == "win32":
        candidate = Path(r"C:\Program Files\Git\usr\bin\openssl.exe")
        if candidate.is_file() and not candidate.is_symlink():
            return str(candidate)
    raise RouteHold("OPENSSL_NOT_AVAILABLE")


def certificate_ok(path: Path, binary: str) -> None:
    if path.is_symlink() or not path.is_file() or not 0 < path.stat().st_size <= 10000:
        raise RouteHold("PUBLIC_CERT_INVALID")
    raw = path.read_bytes()
    if not raw.startswith(b"-----BEGIN CERTIFICATE-----") or b"PRIVATE KEY" in raw:
        raise RouteHold("PUBLIC_CERT_INVALID")
    r = subprocess.run([binary, "x509", "-in", str(path), "-noout"],
                       capture_output=True, timeout=20, check=False)
    if r.returncode:
        raise RouteHold("PUBLIC_CERT_INVALID")


def seal(obj: dict, batch_zip: bytes, cert: Path, *, openssl: str | None = None) -> bytes:
    binary = openssl_path(openssl)
    certificate_ok(cert, binary)
    _, rows = load_batch(batch_zip)
    plaintext = report_bytes(obj, rows)
    p = subprocess.run([
        binary, "cms", "-encrypt", "-binary", "-aes-256-gcm",
        "-outform", "DER", "-recip", str(cert)
    ], input=plaintext, capture_output=True, timeout=40, check=False)
    if (p.returncode != 0 or not 100 <= len(p.stdout) <= MAX_CIPHERTEXT_BYTES
            or plaintext in p.stdout):
        raise RouteHold("CMS_SEAL_FAILED")
    return p.stdout


def verify(ciphertext_path: Path, batch_zip: bytes, cert: Path, key: Path,
           passphrase: bytes, *, openssl: str | None = None) -> dict:
    """Use OpenSSL -passin stdin; never pass the passphrase in argv or output."""
    if not isinstance(passphrase, bytes) or not 1 <= len(passphrase) <= 256 or b"\n" in passphrase or b"\r" in passphrase:
        raise RouteHold("OWNER_PASSPHRASE_INPUT_INVALID")
    if ciphertext_path.is_symlink() or not ciphertext_path.is_file():
        raise RouteHold("CIPHERTEXT_FILE_INVALID")
    if not 100 <= ciphertext_path.stat().st_size <= MAX_CIPHERTEXT_BYTES:
        raise RouteHold("CIPHERTEXT_SIZE_INVALID")
    binary = openssl_path(openssl)
    certificate_ok(cert, binary)
    if key.is_symlink() or not key.is_file() or not key.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----"):
        raise RouteHold("OWNER_PRIVATE_KEY_INVALID")
    _, rows = load_batch(batch_zip)
    p = subprocess.run([
        binary, "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(ciphertext_path), "-recip", str(cert),
        "-inkey", str(key), "-passin", "stdin"
    ], input=passphrase + b"\n", capture_output=True, timeout=40, check=False)
    # All stdout is unauthenticated until the GCM tag check succeeds.
    if p.returncode:
        raise RouteHold("CMS_AUTHENTICATION_FAILED")
    obj = validate_report(p.stdout, rows)
    return {
        "source_ref_and_batch": "PASS",
        "authenticated_ciphertext": "PASS",
        "complete_reviewer_records": len(obj["records"]),
        "reviewer_dispositions": "RESTRICTED_NOT_PRINTED",
        "challenge_state": "PENDING",
        "author_world": "WORLD_UNFROZEN",
        "reviewer_private_report_printed": False,
    }


def cli() -> int:
    parser = argparse.ArgumentParser(description="S1 owner-mediated protected source-status route")
    sub = parser.add_subparsers(dest="action", required=True)
    send = sub.add_parser("seal")
    send.add_argument("--batch-zip", required=True, type=Path)
    send.add_argument("--public-cert", required=True, type=Path)
    send.add_argument("--ciphertext-output", required=True, type=Path)
    send.add_argument("--openssl")
    receive = sub.add_parser("owner-verify")
    receive.add_argument("--batch-zip", required=True, type=Path)
    receive.add_argument("--public-cert", required=True, type=Path)
    receive.add_argument("--private-key", required=True, type=Path)
    receive.add_argument("--ciphertext", required=True, type=Path)
    receive.add_argument("--expected-ciphertext-sha256", required=True)
    receive.add_argument("--openssl")
    args = parser.parse_args()
    if args.action == "seal":
        if (args.ciphertext_output.name != CIPHERTEXT_FILENAME or
                args.ciphertext_output.exists() or
                not args.ciphertext_output.parent.is_dir()):
            raise RouteHold("CIPHERTEXT_OUTPUT_INVALID")
        raw = sys.stdin.buffer.read(MAX_PLAINTEXT_BYTES + 1)
        obj = safe_json(raw)
        cipher = seal(obj, args.batch_zip.read_bytes(),
                      args.public_cert, openssl=args.openssl)
        with args.ciphertext_output.open("xb") as output:
            output.write(cipher)
        print(json.dumps({
            "format": FORMAT,
            "batch_identifier": BATCH_ID,
            "ciphertext_filename": CIPHERTEXT_FILENAME,
            "ciphertext_bytes": len(cipher),
            "ciphertext_sha256": digest(cipher),
            "restricted_report_printed": False,
            "real_reviewer_admitted": False,
            "author_world": "WORLD_UNFROZEN",
        }, sort_keys=True))
        return 0
    if (not HEX64.fullmatch(args.expected_ciphertext_sha256) or
            not args.ciphertext.is_file() or args.ciphertext.is_symlink() or
            digest(args.ciphertext.read_bytes()) != args.expected_ciphertext_sha256):
        raise RouteHold("CIPHERTEXT_INTEGRITY_INVALID")
    if not sys.stdin.isatty():
        raise RouteHold("OWNER_INTERACTIVE_TERMINAL_REQUIRED")
    password = getpass.getpass("Passphrase for owner-held encrypted reviewer key: ")
    summary = verify(args.ciphertext, args.batch_zip.read_bytes(),
                     args.public_cert, args.private_key, password.encode("utf-8"),
                     openssl=args.openssl)
    print(json.dumps(summary, sort_keys=True))
    print("S1_REVIEWER_OWNER_COMPLETE_PRIVATE_READBACK=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except (RouteHold, OSError, ValueError, TypeError, TimeoutError,
            subprocess.SubprocessError, EOFError):
        print("S1_REVIEWER_PROTECTED_ROUTE_HOLD", file=sys.stderr)
        sys.exit(2)
