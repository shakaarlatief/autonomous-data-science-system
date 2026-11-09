"""Standalone restricted Wave0 adversarial challenger report and CMS sender.

This file is deliberately self-contained for a fresh, non-arm Temporary Chat
with the owner-authorized challenge ZIP attached. It contains no private key
and uses the public recipient certificate INSIDE the challenge ZIP to seal
a complete original-source-bound ten-record adversarial challenge.

A valid schema proves accounting and authenticated transport, not truthful
inspection or scientific source-status correctness. The owner must inspect
and adjudicate the actual restricted findings separately.
"""
from __future__ import annotations

import argparse
import getpass
from hashlib import sha1, sha256
from io import BytesIO
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

FORMAT = "ads-r0-p03-s1-wave0-substantive-adversarial-challenge-v1"
PACKET_FORMAT = "ads-r0-p03-s1-wave0-adversarial-input-v1"
REPORT_NAME = "R0_P03_S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE.cms"
SOURCE_HASH = "c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
PAIRED_CIPHERTEXT_HASH = "f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3"
FIRST_HASH = "9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
SECOND_HASH = "50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64"
SOURCE_REF = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
PACKET_MEMBERS = frozenset({
    "CHALLENGE_MANIFEST.json", "CHALLENGE_BRIEF.txt",
    "WAVE0_ORIGINAL_SOURCES.zip", "OWNER_PRIVATE_PAIRED_EVIDENCE.json",
    "OWNER_PUBLIC_ENCRYPTION_CERT.pem", "CHALLENGE_SUBMIT.py",
})
MANIFEST_KEYS = frozenset({
    "format", "source_zip_sha256", "private_paired_evidence_sha256",
    "public_certificate_sha256", "submission_tool_sha256",
    "complete_source_records", "first_reviewer_ciphertext_sha256",
    "independent_first_pass_ciphertext_sha256",
    "owner_comparison_ciphertext_sha256", "evidence_status",
    "new_adversarial_challenge_completed", "new_author_source_admissions",
})
TOP_KEYS = frozenset({
    "format", "source_ref", "source_zip_sha256", "private_paired_evidence_sha256",
    "input_packet_sha256", "role", "stage", "first_reviewer_reasoning_seen",
    "independent_first_pass_reasoning_seen", "independence_limitations",
    "session_exposure_notes", "report_nonce", "records",
    "challenge_state", "author_world", "source_admissions",
})
RECORD_KEYS = frozenset({
    "path", "git_blob_oid", "sha256",
    "original_source_inspected", "first_reviewer_reasoning_examined",
    "independent_first_pass_reasoning_examined",
    "first_reviewer_assessment", "independent_first_pass_assessment",
    "material_disagreement", "shared_blindspot",
    "strongest_counterargument", "source_grounded_evidence",
    "missing_or_uninspectable_context", "claim_materiality",
    "disclosure_materiality", "provisional_outcome", "restricted_reasoning",
})
ASSESSMENTS = frozenset({"SUPPORTED", "DISPUTED", "PARTIALLY_SUPPORTED", "UNRESOLVED"})
YES_NO_UNKNOWN = frozenset({"YES", "NO", "UNCERTAIN"})
OUTCOMES = frozenset({"SUPPORTED_PROVISIONALLY", "DISPUTED", "HOLD_FOR_EVIDENCE"})
MAX_PACKET_BYTES = 950_000
MAX_REPORT_BYTES = 400_000
MAX_CIPHERTEXT_BYTES = 550_000
HEX32 = re.compile(r"[0-9a-f]{32}\Z")
MAX_FIELD_CHARS = 15000


class Hold(ValueError):
    """Safe scoped hold. Do not expose protected content in exception text."""


def sha(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def canonical(obj: object) -> bytes:
    try:
        return json.dumps(
            obj, sort_keys=True, ensure_ascii=True,
            separators=(",", ":"), allow_nan=False,
        ).encode("ascii")
    except (TypeError, ValueError, UnicodeError) as exc:
        raise Hold("CANNOT_CANONICALIZE") from exc


def unique_pairs(pairs: list[tuple[str, object]]) -> dict:
    obj: dict = {}
    for name, value in pairs:
        if name in obj:
            raise Hold("DUPLICATE_JSON_KEYS")
        obj[name] = value
    return obj


def json_object(raw: bytes) -> dict:
    try:
        obj = json.loads(
            raw.decode("utf-8"), object_pairs_hook=unique_pairs,
            parse_constant=lambda x: (_ for _ in ()).throw(Hold("NONFINITE_JSON")),
        )
    except (ValueError, TypeError, UnicodeError) as exc:
        raise Hold("INVALID_JSON") from exc
    if not isinstance(obj, dict):
        raise Hold("EXPECTED_OBJECT")
    return obj


def exact(obj: object, fields: frozenset[str]) -> dict:
    if not isinstance(obj, dict) or set(obj) != fields:
        raise Hold("SCHEMA_FIELDS_INVALID")
    return obj


def substantive(value: object) -> str:
    if (not isinstance(value, str) or not 8 <= len(value.strip()) <= MAX_FIELD_CHARS):
        raise Hold("SUBSTANTIVE_REASONING_MISSING")
    return value


def packet_inputs(packet: bytes) -> tuple[dict, dict, list[dict], bytes]:
    if not 1000 <= len(packet) <= MAX_PACKET_BYTES:
        raise Hold("INPUT_PACKET_SIZE_INVALID")
    try:
        with ZipFile(BytesIO(packet)) as archive:
            names = [i.filename for i in archive.infolist()]
            if len(names) != len(PACKET_MEMBERS) or set(names) != PACKET_MEMBERS:
                raise Hold("INPUT_PACKET_MEMBERS_INVALID")
            if any(i.is_dir() or i.flag_bits & 1 for i in archive.infolist()):
                raise Hold("INPUT_PACKET_MEMBER_INVALID")
            manifest_raw = archive.read("CHALLENGE_MANIFEST.json")
            orig = archive.read("WAVE0_ORIGINAL_SOURCES.zip")
            pair_raw = archive.read("OWNER_PRIVATE_PAIRED_EVIDENCE.json")
            cert = archive.read("OWNER_PUBLIC_ENCRYPTION_CERT.pem")
            sender = archive.read("CHALLENGE_SUBMIT.py")
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        raise Hold("INPUT_PACKET_UNREADABLE") from exc
    manifest = exact(json_object(manifest_raw), MANIFEST_KEYS)
    if manifest_raw != canonical(manifest):
        raise Hold("INPUT_MANIFEST_NONCANONICAL")
    if (
        manifest["format"] != PACKET_FORMAT
        or manifest["complete_source_records"] != 10
        or manifest["new_adversarial_challenge_completed"] is not False
        or manifest["new_author_source_admissions"] != 0
        or manifest["source_zip_sha256"] != SOURCE_HASH
        or manifest["first_reviewer_ciphertext_sha256"] != FIRST_HASH
        or manifest["independent_first_pass_ciphertext_sha256"] != SECOND_HASH
        or manifest["owner_comparison_ciphertext_sha256"] != PAIRED_CIPHERTEXT_HASH
        or manifest["evidence_status"] !=
            "AUTHOR_WORLD_UNFROZEN_SOURCE_STATUS_CHALLENGE_ONLY"
        or sha(orig) != SOURCE_HASH
        or sha(pair_raw) != manifest["private_paired_evidence_sha256"]
        or sha(cert) != manifest["public_certificate_sha256"]
        or sha(sender) != manifest["submission_tool_sha256"]
        or b"-----BEGIN CERTIFICATE-----" not in cert
    ):
        raise Hold("INPUT_PACKET_BINDING_INVALID")
    pair = json_object(pair_raw)
    if pair_raw != canonical(pair):
        raise Hold("PAIRED_REPORT_NONCANONICAL")
    if (pair.get("format") != "ads-r0-p03-wave0-owner-private-paired-comparison-v1"
        or pair.get("source_ref") != SOURCE_REF
        or pair.get("source_batch_sha256") != SOURCE_HASH
        or pair.get("first_reviewer_ciphertext_sha256") != FIRST_HASH
        or pair.get("independent_challenger_ciphertext_sha256") != SECOND_HASH
        or pair.get("complete_record_count") != 10
        or pair.get("actual_adversarial_challenge") != "PENDING"
        or pair.get("author_world") != "WORLD_UNFROZEN"
        or pair.get("release_authorization") != "NONE"):
        raise Hold("PAIRED_REPORT_PROVENANCE_INVALID")
    records = pair.get("private_paired_source_records")
    if not isinstance(records, list) or len(records) != 10:
        raise Hold("PAIRED_REPORT_COUNT_INVALID")
    try:
        with ZipFile(BytesIO(orig)) as archive:
            manifest_source = json_object(archive.read("SOURCE_MANIFEST.json"))
            rows = manifest_source["source_manifest"]
            if not isinstance(rows, list) or len(rows) != 10:
                raise Hold("ORIGINAL_SOURCE_COUNT_INVALID")
            for row, item in zip(rows, records, strict=True):
                if (not isinstance(row, dict) or not isinstance(item, dict)):
                    raise Hold("ORIGINAL_SOURCE_RECORD_INVALID")
                path = row["path"]
                if (not isinstance(path, str) or
                    PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts
                    or "\\" in path):
                    raise Hold("ORIGINAL_SOURCE_PATH_INVALID")
                raw = archive.read("sources/" + path)
                oid = sha1(
                    b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw
                ).hexdigest()
                if (
                    oid != row["git_blob_oid"] or sha(raw) != row["sha256"]
                    or len(raw) != row["bytes"]
                    or item.get("original_path") != path
                    or item.get("git_blob_oid") != oid
                    or item.get("source_sha256") != sha(raw)
                ):
                    raise Hold("ORIGINAL_SOURCE_BINDING_INVALID")
    except (OSError, ValueError, RuntimeError, KeyError, TypeError) as exc:
        raise Hold("ORIGINAL_SOURCE_ZIP_INVALID") from exc
    return manifest, pair, rows, cert


def validate_report(obj: dict, packet: bytes) -> bytes:
    manifest, _, rows, _ = packet_inputs(packet)
    exact(obj, TOP_KEYS)
    if (
        obj["format"] != FORMAT
        or obj["source_ref"] != SOURCE_REF
        or obj["source_zip_sha256"] != SOURCE_HASH
        or obj["private_paired_evidence_sha256"] !=
            manifest["private_paired_evidence_sha256"]
        or obj["input_packet_sha256"] != sha(packet)
        or obj["role"] != "NON_ARM_SOURCE_STATUS_ADVERSARIAL_CHALLENGER"
        or obj["stage"] != "AFTER_TWO_PRESERVED_BLIND_FIRST_PASSES"
        or obj["first_reviewer_reasoning_seen"] is not True
        or obj["independent_first_pass_reasoning_seen"] is not True
        or obj["challenge_state"] != "SUBSTANTIVE_CHALLENGE_REPORTED_NOT_ADJUDICATED"
        or obj["author_world"] != "WORLD_UNFROZEN"
        or obj["source_admissions"] != 0
        or not isinstance(obj["report_nonce"], str)
        or HEX32.fullmatch(obj["report_nonce"]) is None
    ):
        raise Hold("CHALLENGE_ROLE_OR_STATE_INVALID")
    substantive(obj["independence_limitations"])
    substantive(obj["session_exposure_notes"])
    records = obj["records"]
    if not isinstance(records, list) or len(records) != 10:
        raise Hold("CHALLENGE_RECORD_COUNT_INVALID")
    for ref, item in zip(rows, records, strict=True):
        exact(item, RECORD_KEYS)
        if (
            item["path"] != ref["path"]
            or item["git_blob_oid"] != ref["git_blob_oid"]
            or item["sha256"] != ref["sha256"]
            or item["original_source_inspected"] is not True
            or item["first_reviewer_reasoning_examined"] is not True
            or item["independent_first_pass_reasoning_examined"] is not True
            or item["first_reviewer_assessment"] not in ASSESSMENTS
            or item["independent_first_pass_assessment"] not in ASSESSMENTS
            or item["material_disagreement"] not in YES_NO_UNKNOWN
            or item["shared_blindspot"] not in YES_NO_UNKNOWN
            or item["provisional_outcome"] not in OUTCOMES
        ):
            raise Hold("CHALLENGE_SOURCE_RECORD_INVALID")
        for name in (
            "strongest_counterargument", "source_grounded_evidence",
            "missing_or_uninspectable_context", "claim_materiality",
            "disclosure_materiality", "restricted_reasoning",
        ):
            substantive(item[name])
    plaintext = canonical(obj)
    if len(plaintext) > MAX_REPORT_BYTES:
        raise Hold("CHALLENGE_REPORT_TOO_LARGE")
    return plaintext


def openssl_path(proposed: str | None) -> str:
    found = proposed or shutil.which("openssl")
    if not found or not Path(found).is_file():
        raise Hold("OPENSSL_NOT_AVAILABLE")
    return str(found)


def seal(obj: dict, packet: bytes, *, openssl: str | None = None) -> bytes:
    plaintext = validate_report(obj, packet)
    _, _, _, cert = packet_inputs(packet)
    binary = openssl_path(openssl)
    with TemporaryDirectory() as folder:
        # A public certificate is not secret. The private report remains in memory.
        certfile = Path(folder) / "owner-public-cert.pem"
        certfile.write_bytes(cert)
        p = subprocess.run(
            [binary, "cms", "-encrypt", "-binary", "-aes-256-gcm",
             "-outform", "DER", "-recip", str(certfile)],
            input=plaintext, capture_output=True, timeout=40, check=False,
        )
    if (
        p.returncode != 0 or not 100 <= len(p.stdout) <= MAX_CIPHERTEXT_BYTES
        or plaintext in p.stdout
    ):
        raise Hold("CHALLENGE_CMS_ENCRYPTION_FAILED")
    return p.stdout


def owner_verify(
    ciphertext: bytes, packet: bytes, cert_path: Path, key_path: Path,
    password: bytes, *, openssl: str | None = None,
) -> dict:
    if (
        not 100 <= len(ciphertext) <= MAX_CIPHERTEXT_BYTES
        or not isinstance(password, bytes) or not 1 <= len(password) <= 256
        or b"\n" in password or b"\r" in password
        or cert_path.is_symlink() or not cert_path.is_file()
        or key_path.is_symlink() or not key_path.is_file()
    ):
        raise Hold("CHALLENGE_OWNER_INPUT_INVALID")
    _, _, _, bundled_cert = packet_inputs(packet)
    if cert_path.read_bytes() != bundled_cert:
        raise Hold("CHALLENGE_OWNER_CERT_BINDING_INVALID")
    if not key_path.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----"):
        raise Hold("CHALLENGE_OWNER_KEY_NOT_ENCRYPTED")
    binary = openssl_path(openssl)
    with TemporaryDirectory() as directory:
        ciphertext_file = Path(directory) / "sealed.cms"
        ciphertext_file.write_bytes(ciphertext)
        p = subprocess.run(
            [binary, "cms", "-decrypt", "-binary", "-inform", "DER",
             "-in", str(ciphertext_file), "-recip", str(cert_path),
             "-inkey", str(key_path), "-passin", "stdin"],
            input=password + b"\n", capture_output=True,
            timeout=40, check=False,
        )
    if p.returncode:
        raise Hold("CHALLENGE_OWNER_CMS_AUTHENTICATION_FAILED")
    report = json_object(p.stdout)
    if canonical(report) != p.stdout:
        raise Hold("CHALLENGE_OWNER_NONCANONICAL_REPORT")
    validate_report(report, packet)
    return {
        "owner_challenge_cms_authenticated": "PASS",
        "exact_challenge_packet_bound": "PASS",
        "complete_source_challenge_records": 10,
        "source_specific_findings_printed": False,
        "actual_challenge_report_recovered": "PASS",
        "semantic_acceptance": "NOT_YET_ADJUDICATED",
        "author_world": "WORLD_UNFROZEN",
    }


def cli() -> int:
    parser = argparse.ArgumentParser(description="Wave0 owner-only encrypted challenge report route")
    sub = parser.add_subparsers(dest="action", required=True)
    send = sub.add_parser("seal")
    send.add_argument("--packet", type=Path, required=True)
    send.add_argument("--ciphertext-output", type=Path, required=True)
    send.add_argument("--openssl")
    receive = sub.add_parser("owner-verify")
    receive.add_argument("--packet", type=Path, required=True)
    receive.add_argument("--public-cert", type=Path, required=True)
    receive.add_argument("--private-key", type=Path, required=True)
    receive.add_argument("--ciphertext", type=Path, required=True)
    receive.add_argument("--expected-sha256", required=True)
    receive.add_argument("--openssl")
    args = parser.parse_args()
    if args.action == "seal":
        if (
            args.ciphertext_output.name != REPORT_NAME
            or args.ciphertext_output.is_symlink()
            or args.ciphertext_output.exists()
            or not args.ciphertext_output.parent.is_dir()
        ):
            raise Hold("CHALLENGE_CIPHERTEXT_OUTPUT_INVALID")
        raw = sys.stdin.buffer.read(MAX_REPORT_BYTES + 1)
        obj = json_object(raw)
        sealed = seal(obj, args.packet.read_bytes(), openssl=args.openssl)
        with args.ciphertext_output.open("xb") as f:
            f.write(sealed)
        print(json.dumps({
            "challenge_cms_sealed": "PASS",
            "ciphertext_sha256": sha(sealed),
            "ciphertext_bytes": len(sealed),
            "paired_record_count": 10,
            "source_specific_findings_printed": False,
            "adversarial_challenge_reported": True,
            "source_status_adjudication": "PENDING",
        }, sort_keys=True))
        return 0
    if (
        args.ciphertext.name != REPORT_NAME
        or args.ciphertext.is_symlink() or not args.ciphertext.is_file()
        or not isinstance(args.expected_sha256, str)
        or re.fullmatch(r"[0-9a-f]{64}", args.expected_sha256) is None
        or sha(args.ciphertext.read_bytes()) != args.expected_sha256
    ):
        raise Hold("CHALLENGE_OWNER_CIPHERTEXT_MISMATCH")
    if not sys.stdin.isatty():
        raise Hold("CHALLENGE_OWNER_INTERACTIVE_REQUIRED")
    password = getpass.getpass("Existing owner encrypted-key passphrase: ")
    result = owner_verify(
        args.ciphertext.read_bytes(), args.packet.read_bytes(),
        args.public_cert, args.private_key, password.encode("utf-8"),
        openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_SUBSTANTIVE_CHALLENGE_READBACK=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except (Hold, OSError, ValueError, TypeError, UnicodeError, EOFError,
            subprocess.SubprocessError, TimeoutError):
        print("S1_WAVE0_ADVERSARIAL_CHALLENGE_HOLD", file=sys.stderr)
        sys.exit(2)
