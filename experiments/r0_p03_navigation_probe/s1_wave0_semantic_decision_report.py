"""Standalone restricted ten-source Wave0 semantic adjudication report.

Only invented fixtures may be exercised from the exposed coordinator.
For a real restricted packet, a separate owner-authorized NON-ARM adjudicator
inspects original historical source bytes, both prior full source assessments,
and the full authenticated adversarial report, then seals its own independent
decision register under the owner's PUBLIC certificate.

These proposed decisions never release a source to the blind author world.
"""
from __future__ import annotations

import argparse
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

FORMAT = "ads-r0-p03-wave0-source-status-semantic-decision-register-v1"
INPUT_FORMAT = "ads-r0-p03-wave0-semantic-adjudication-input-v1"
REPORT_NAME = "R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms"
ORIGINAL_SOURCE_SHA = "c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387"
CHALLENGE_CMS_SHA = "e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03"
COMPARISON_CMS_SHA = "f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3"
SOURCE_REF = "c57556a8bf993a1d327e9197acb7b7c745071cd8"
INPUT_MEMBERS = frozenset({
    "ORIGINAL_WAVE0_SOURCES.zip", "PAIRED_FIRST_PASSES.json",
    "SUBSTANTIVE_CHALLENGE.json", "OWNER_PUBLIC_CERT.pem",
    "ADJUDICATION_MANIFEST.json", "ADJUDICATION_BRIEF.txt",
    "ADJUDICATION_SUBMIT.py",
})
MANIFEST_FIELDS = frozenset({
    "format", "original_source_sha256", "paired_plaintext_sha256",
    "challenge_plaintext_sha256", "public_cert_sha256", "sender_code_sha256",
    "prior_comparison_ciphertext_sha256", "prior_challenge_ciphertext_sha256",
    "source_ref", "source_count", "author_release", "source_world",
})
TOP_FIELDS = frozenset({
    "format", "input_packet_sha256", "original_source_sha256",
    "paired_plaintext_sha256", "challenge_plaintext_sha256", "source_ref",
    "role", "session_exposure_and_independence_limitations",
    "decision_basis_and_limits", "report_nonce", "records",
    "source_world", "author_release", "record_status",
})
RECORD_FIELDS = frozenset({
    "path", "git_blob_oid", "sha256", "original_source_inspected",
    "two_first_pass_records_inspected", "adversarial_challenge_inspected",
    "historical_authority_and_version", "supported_prior_evidence",
    "disputed_or_unproven_prior_evidence", "strongest_counterinterpretation",
    "claim_materiality", "disclosure_materiality",
    "evidence_gaps_and_missing_representations", "decision",
    "decision_rationale", "falsification_or_resolution_trigger",
    "required_next_action", "author_release",
})
DECISIONS = frozenset({
    "PROSPECTIVE_WHOLE_FILE_CANDIDATE",
    "AUXILIARY_ONLY_EXCLUDED_FROM_AUTHOR",
    "PROHIBIT_AUTHOR_EXPOSURE",
    "HOLD_FOR_MATERIAL_EVIDENCE",
})
MAX_PACKET_BYTES = 1_200_000
MAX_REPORT_BYTES = 480_000
MAX_CMS_BYTES = 620_000
MAX_TEXT_CHARS = 18000
HEX32 = re.compile(r"[0-9a-f]{32}\Z")


class Hold(ValueError):
    """Fixed-safe error class. Never print restricted source details."""


def sha(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def pairs_unique(pairs: list[tuple[str, object]]) -> dict:
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise Hold("DUPLICATE_JSON_FIELD")
        obj[key] = value
    return obj


def canonical(obj: object) -> bytes:
    try:
        return json.dumps(
            obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
            allow_nan=False,
        ).encode("ascii")
    except (ValueError, TypeError, UnicodeError) as exc:
        raise Hold("NONCANONICAL_VALUE") from exc


def parse(raw: bytes) -> dict:
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs_unique)
    except (ValueError, UnicodeError) as exc:
        raise Hold("INVALID_JSON") from exc
    if not isinstance(value, dict):
        raise Hold("EXPECTED_JSON_OBJECT")
    return value


def exact(obj: object, fields: frozenset[str]) -> dict:
    if not isinstance(obj, dict) or set(obj) != fields:
        raise Hold("SCHEMA_FIELDS_INVALID")
    return obj


def explained(text: object, *, min_chars: int = 12) -> None:
    if (
        not isinstance(text, str) or
        not min_chars <= len(text.strip()) <= MAX_TEXT_CHARS
    ):
        raise Hold("SOURCE_GROUNDED_EXPLANATION_REQUIRED")


def inspect_packet(raw: bytes) -> tuple[dict, list[dict], bytes]:
    if not 1000 <= len(raw) <= MAX_PACKET_BYTES:
        raise Hold("ADJUDICATION_PACKET_SIZE_INVALID")
    try:
        with ZipFile(BytesIO(raw)) as archive:
            infos = archive.infolist()
            if len(infos) != len(INPUT_MEMBERS) or {
                i.filename for i in infos
            } != INPUT_MEMBERS or any(
                i.is_dir() or (i.flag_bits & 1) for i in infos
            ):
                raise Hold("ADJUDICATION_PACKET_MEMBERS_INVALID")
            # Bound decompressed input before reading, including a file whose
            # compressed bytes fit the packet limit but inflate enormously.
            if sum(i.file_size for i in infos) > MAX_PACKET_BYTES:
                raise Hold("ADJUDICATION_PACKET_INFLATED_SIZE_INVALID")
            data = {name: archive.read(name) for name in INPUT_MEMBERS}
    except (OSError, ValueError, RuntimeError, KeyError) as exc:
        raise Hold("ADJUDICATION_PACKET_UNREADABLE") from exc
    manifest_raw = data["ADJUDICATION_MANIFEST.json"]
    manifest = exact(parse(manifest_raw), MANIFEST_FIELDS)
    if manifest_raw != canonical(manifest):
        raise Hold("ADJUDICATION_MANIFEST_NONCANONICAL")
    orig = data["ORIGINAL_WAVE0_SOURCES.zip"]
    paired = data["PAIRED_FIRST_PASSES.json"]
    challenged = data["SUBSTANTIVE_CHALLENGE.json"]
    certificate = data["OWNER_PUBLIC_CERT.pem"]
    if (
        manifest["format"] != INPUT_FORMAT
        or manifest["original_source_sha256"] != ORIGINAL_SOURCE_SHA
        or sha(orig) != ORIGINAL_SOURCE_SHA
        or sha(paired) != manifest["paired_plaintext_sha256"]
        or sha(challenged) != manifest["challenge_plaintext_sha256"]
        or sha(certificate) != manifest["public_cert_sha256"]
        or sha(data["ADJUDICATION_SUBMIT.py"]) != manifest["sender_code_sha256"]
        or manifest["prior_challenge_ciphertext_sha256"] != CHALLENGE_CMS_SHA
        or manifest["prior_comparison_ciphertext_sha256"] != COMPARISON_CMS_SHA
        or manifest["source_ref"] != SOURCE_REF
        or manifest["source_count"] != 10
        or manifest["author_release"] != "NONE"
        or manifest["source_world"] != "WORLD_UNFROZEN"
        or b"-----BEGIN CERTIFICATE-----" not in certificate
    ):
        raise Hold("ADJUDICATION_PACKET_IDENTITY_INVALID")
    first = parse(paired)
    third = parse(challenged)
    if (
        paired != canonical(first) or challenged != canonical(third)
        or first.get("complete_record_count") != 10
        or third.get("format") !=
            "ads-r0-p03-s1-wave0-substantive-adversarial-challenge-v1"
        or third.get("source_zip_sha256") != ORIGINAL_SOURCE_SHA
        or third.get("source_ref") != SOURCE_REF
    ):
        raise Hold("PREVIOUS_REPORT_BINDING_INVALID")
    p_records = first.get("private_paired_source_records")
    c_records = third.get("records")
    if (not isinstance(p_records, list) or len(p_records) != 10
        or not isinstance(c_records, list) or len(c_records) != 10):
        raise Hold("PREVIOUS_RECORD_COUNT_INVALID")
    try:
        with ZipFile(BytesIO(orig)) as archive:
            source_manifest = parse(archive.read("SOURCE_MANIFEST.json"))
            rows = source_manifest["source_manifest"]
            if not isinstance(rows, list) or len(rows) != 10:
                raise Hold("ORIGINAL_SOURCE_COUNT_INVALID")
            for i, (row, a, b) in enumerate(
                zip(rows, p_records, c_records, strict=True)
            ):
                path = row["path"]
                if (
                    not isinstance(path, str) or "\\" in path
                    or PurePosixPath(path).is_absolute()
                    or ".." in PurePosixPath(path).parts
                ):
                    raise Hold("SOURCE_PATH_INVALID")
                blob = archive.read("sources/" + path)
                git_oid = sha1(
                    b"blob " + str(len(blob)).encode("ascii") + b"\0" + blob
                ).hexdigest()
                if (
                    row["sha256"] != sha(blob) or row["git_blob_oid"] != git_oid
                    or row["bytes"] != len(blob)
                    or a.get("manifest_index") != i
                    or a.get("original_path") != path
                    or a.get("source_sha256") != sha(blob)
                    or b.get("path") != path
                    or b.get("sha256") != sha(blob)
                    or b.get("git_blob_oid") != git_oid
                ):
                    raise Hold("SOURCE_RECORD_PROVENANCE_INVALID")
    except (OSError, ValueError, TypeError, KeyError, RuntimeError) as exc:
        raise Hold("ORIGINAL_SOURCE_INVALID") from exc
    return manifest, rows, certificate


def validate_report(obj: dict, packet: bytes) -> bytes:
    manifest, rows, _ = inspect_packet(packet)
    exact(obj, TOP_FIELDS)
    if (
        obj["format"] != FORMAT
        or obj["input_packet_sha256"] != sha(packet)
        or obj["original_source_sha256"] != ORIGINAL_SOURCE_SHA
        or obj["paired_plaintext_sha256"] != manifest["paired_plaintext_sha256"]
        or obj["challenge_plaintext_sha256"] != manifest["challenge_plaintext_sha256"]
        or obj["source_ref"] != SOURCE_REF
        or obj["role"] != "NON_ARM_SOURCE_STATUS_SEMANTIC_ADJUDICATOR"
        or not isinstance(obj["report_nonce"], str)
        or HEX32.fullmatch(obj["report_nonce"]) is None
        or obj["source_world"] != "WORLD_UNFROZEN"
        or obj["author_release"] != "NONE"
        or obj["record_status"] != "PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION"
    ):
        raise Hold("ADJUDICATION_REPORT_STATE_INVALID")
    explained(obj["session_exposure_and_independence_limitations"])
    explained(obj["decision_basis_and_limits"])
    records = obj["records"]
    if not isinstance(records, list) or len(records) != 10:
        raise Hold("ADJUDICATION_RECORD_COUNT_INVALID")
    for source, item in zip(rows, records, strict=True):
        exact(item, RECORD_FIELDS)
        if (
            item["path"] != source["path"]
            or item["git_blob_oid"] != source["git_blob_oid"]
            or item["sha256"] != source["sha256"]
            or item["original_source_inspected"] is not True
            or item["two_first_pass_records_inspected"] is not True
            or item["adversarial_challenge_inspected"] is not True
            or item["decision"] not in DECISIONS
            or item["author_release"] != "NONE"
        ):
            raise Hold("ADJUDICATION_SOURCE_RECORD_INVALID")
        if (
            item["decision"] == "HOLD_FOR_MATERIAL_EVIDENCE"
            and isinstance(item["required_next_action"], str)
            and item["required_next_action"].strip().upper() == "NONE"
        ):
            raise Hold("HOLD_REQUIRES_ACTION_OR_LIMITATION")
        for field in (
            "historical_authority_and_version", "supported_prior_evidence",
            "disputed_or_unproven_prior_evidence",
            "strongest_counterinterpretation", "claim_materiality",
            "disclosure_materiality", "evidence_gaps_and_missing_representations",
            "decision_rationale", "falsification_or_resolution_trigger",
            "required_next_action",
        ):
            explained(item[field])
    raw = canonical(obj)
    if not 500 <= len(raw) <= MAX_REPORT_BYTES:
        raise Hold("ADJUDICATION_REPORT_SIZE_INVALID")
    return raw


def binary_path(value: str | None) -> str:
    found = value or shutil.which("openssl")
    if not found or not Path(found).is_file():
        raise Hold("OPENSSL_UNAVAILABLE")
    return str(found)


def seal(obj: dict, packet: bytes, *, openssl: str | None = None) -> bytes:
    raw = validate_report(obj, packet)
    _, _, cert = inspect_packet(packet)
    binary = binary_path(openssl)
    with TemporaryDirectory() as folder:
        public = Path(folder) / "owner-public.pem"
        public.write_bytes(cert)
        process = subprocess.run([
            binary, "cms", "-encrypt", "-binary", "-aes-256-gcm",
            "-outform", "DER", "-recip", str(public),
        ], input=raw, capture_output=True, timeout=40, check=False)
    if (
        process.returncode != 0 or
        not 100 <= len(process.stdout) <= MAX_CMS_BYTES
        or raw in process.stdout
    ):
        raise Hold("ADJUDICATION_CMS_ENCRYPTION_FAILED")
    return process.stdout


def owner_verify(
    ciphertext: bytes, packet: bytes, cert: Path, key: Path,
    password: bytes, *, openssl: str | None = None,
) -> dict:
    if (
        not 100 <= len(ciphertext) <= MAX_CMS_BYTES
        or not 1 <= len(password) <= 256 or b"\n" in password or b"\r" in password
        or cert.is_symlink() or not cert.is_file()
        or key.is_symlink() or not key.is_file()
    ):
        raise Hold("OWNER_ADJUDICATION_INPUT_INVALID")
    _, _, packet_cert = inspect_packet(packet)
    if cert.read_bytes() != packet_cert:
        raise Hold("OWNER_CERTIFICATE_MISMATCH")
    if not key.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----"):
        raise Hold("OWNER_KEY_NOT_ENCRYPTED")
    binary = binary_path(openssl)
    with TemporaryDirectory() as folder:
        cipher = Path(folder) / "cipher.cms"
        cipher.write_bytes(ciphertext)
        process = subprocess.run([
            binary, "cms", "-decrypt", "-binary", "-inform", "DER",
            "-in", str(cipher), "-recip", str(cert), "-inkey", str(key),
            "-passin", "stdin",
        ], input=password + b"\n", capture_output=True,
            timeout=40, check=False)
    if process.returncode:
        raise Hold("OWNER_ADJUDICATION_CMS_AUTHENTICATION_FAILED")
    obj = parse(process.stdout)
    if canonical(obj) != process.stdout:
        raise Hold("OWNER_ADJUDICATION_REPORT_NONCANONICAL")
    validate_report(obj, packet)
    return {
        "owner_adjudication_cms_authenticated": "PASS",
        "exact_original_sources_bound": "PASS",
        "both_first_passes_and_challenge_bound": "PASS",
        "complete_source_decisions_or_holds": 10,
        "source_specific_findings_printed": False,
        "author_release": "NONE",
        "final_owner_acceptance": "PENDING",
        "source_world": "WORLD_UNFROZEN",
    }


def cli() -> int:
    parser = argparse.ArgumentParser(description="Wave0 owner-encrypted source decision report")
    sub = parser.add_subparsers(dest="action", required=True)
    send = sub.add_parser("seal")
    send.add_argument("--packet", type=Path, required=True)
    send.add_argument("--ciphertext-output", type=Path, required=True)
    send.add_argument("--openssl")
    recv = sub.add_parser("owner-verify")
    recv.add_argument("--packet", type=Path, required=True)
    recv.add_argument("--public-cert", type=Path, required=True)
    recv.add_argument("--private-key", type=Path, required=True)
    recv.add_argument("--ciphertext", type=Path, required=True)
    recv.add_argument("--expected-sha256", required=True)
    recv.add_argument("--openssl")
    args = parser.parse_args()
    if args.action == "seal":
        if (
            args.ciphertext_output.name != REPORT_NAME
            or args.ciphertext_output.is_symlink()
            or args.ciphertext_output.exists()
            or not args.ciphertext_output.parent.is_dir()
        ):
            raise Hold("ADJUDICATION_CIPHERTEXT_OUTPUT_INVALID")
        obj = parse(sys.stdin.buffer.read(MAX_REPORT_BYTES + 1))
        ciphertext = seal(obj, args.packet.read_bytes(), openssl=args.openssl)
        with args.ciphertext_output.open("xb") as file:
            file.write(ciphertext)
        print(json.dumps({
            "adjudication_cms_sealed": "PASS",
            "ciphertext_sha256": sha(ciphertext),
            "ciphertext_bytes": len(ciphertext),
            "ten_source_decisions_or_holds": 10,
            "source_specific_findings_printed": False,
            "owner_acceptance": "PENDING",
        }, sort_keys=True))
        return 0
    if (
        args.ciphertext.name != REPORT_NAME
        or args.ciphertext.is_symlink() or not args.ciphertext.is_file()
        or re.fullmatch("[0-9a-f]{64}", args.expected_sha256) is None
        or sha(args.ciphertext.read_bytes()) != args.expected_sha256
    ):
        raise Hold("OWNER_ADJUDICATION_CIPHERTEXT_IDENTITY_INVALID")
    if not sys.stdin.isatty():
        raise Hold("OWNER_INTERACTIVE_REQUIRED")
    result = owner_verify(
        args.ciphertext.read_bytes(), args.packet.read_bytes(),
        args.public_cert, args.private_key,
        __import__("getpass").getpass(
            "Existing owner encrypted-key passphrase: "
        ).encode("utf-8"), openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_READBACK=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except (Hold, OSError, ValueError, TypeError, EOFError,
            subprocess.SubprocessError, TimeoutError):
        print("S1_WAVE0_SEMANTIC_ADJUDICATION_HOLD", file=sys.stderr)
        sys.exit(2)
