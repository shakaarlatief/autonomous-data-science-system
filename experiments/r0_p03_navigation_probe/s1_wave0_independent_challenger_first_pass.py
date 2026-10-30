"""Blind-to-reviewer, owner-encrypted independent Wave0 second assessment.

Purpose: an independent second non-arm source-status judgment on exactly the
same ten original historical sources, *before* exposure to first-reviewer
private conclusions. It is not itself a completed adversarial challenge.
The second session must never receive the first private CMS, private owner key,
private reviewer notes, or historical gold. Later owner-local disagreement
reconciliation and targeted adversarial challenge are distinct operations.

This module inherits the exact approved batch loader and source content
proposal validation from the original reviewer module, but uses a DIFFERENT
actor identity, restricted canonical report format, ciphertext filename,
and owner-side verify contract. It does not reinterpret a second independent
judgment as an already challenged first reviewer disposition.
"""
from __future__ import annotations

import argparse
import getpass
import json
from pathlib import Path
import re
import subprocess
import sys

from experiments.r0_p03_navigation_probe import (
    s1_source_status_protected_route as original,
)

FORMAT = "ads-r0-p03-s1-independent-challenger-first-pass-v1"
OUTPUT_NAME = "R0_P03_S1_WAVE0_OWNER_CHALLENGER_FIRST_PASS.cms"
ORIGINAL_CIPHERTEXT_SHA256 = (
    "9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366"
)
REPORT_FIELDS = frozenset({
    "format", "batch_identifier", "source_ref",
    "batch_zip_sha256", "batch_manifest_sha256",
    "original_reviewer_ciphertext_sha256",
    "candidate_role", "initial_assessment_mode", "first_reviewer_report_seen",
    "first_reviewer_conclusions_seen", "prior_exposure_uncertainty",
    "method_status", "authorization", "author_world", "challenge_state",
    "report_nonce", "restricted_independent_assessment_notes", "records",
})
MODE = "INDEPENDENT_FIRST_PASS_BEFORE_REVIEWER_FINDINGS"
ROLE = "NON_ARM_SOURCE_STATUS_INDEPENDENT_CHALLENGER_CANDIDATE"
CHALLENGE = "ACTUAL_ADVERSARIAL_CHALLENGE_PENDING"
HEX32 = re.compile(r"[0-9a-f]{32}\Z")


def validate_report(raw: bytes, rows: list[dict]) -> dict:
    if not 200 <= len(raw) <= original.MAX_PLAINTEXT_BYTES:
        raise original.RouteHold("INDEPENDENT_REPORT_SIZE_INVALID")
    obj = original.exact_fields(
        original.safe_json(raw), REPORT_FIELDS, "INDEPENDENT_REPORT_SCHEMA_INVALID"
    )
    if original.canonical(obj) != raw:
        raise original.RouteHold("INDEPENDENT_REPORT_NONCANONICAL")
    if (
        obj["format"] != FORMAT
        or obj["batch_identifier"] != original.BATCH_ID
        or obj["source_ref"] != original.SOURCE_PIN
        or obj["batch_zip_sha256"] != original.BATCH_ZIP_SHA256
        or obj["batch_manifest_sha256"] != original.BATCH_MANIFEST_SHA256
        or obj["original_reviewer_ciphertext_sha256"] != ORIGINAL_CIPHERTEXT_SHA256
        or obj["candidate_role"] != ROLE
        or obj["initial_assessment_mode"] != MODE
        or obj["first_reviewer_report_seen"] is not False
        or obj["first_reviewer_conclusions_seen"] is not False
        or obj["method_status"] != "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED"
        or obj["authorization"] != "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE"
        or obj["author_world"] != "WORLD_UNFROZEN"
        or obj["challenge_state"] != CHALLENGE
        or not isinstance(obj["report_nonce"], str)
        or HEX32.fullmatch(obj["report_nonce"]) is None
    ):
        raise original.RouteHold("INDEPENDENT_ROLE_OR_STATE_INVALID")
    original.text_field(obj["prior_exposure_uncertainty"], permit_empty=False)
    original.text_field(obj["restricted_independent_assessment_notes"], permit_empty=False)
    # Reuse only the well-tested *per-source* original-version schema and
    # canonical validations, not its reviewer actor identity for this output.
    source_check = {
        "format": original.FORMAT,
        "batch_identifier": original.BATCH_ID,
        "source_ref": original.SOURCE_PIN,
        "batch_zip_sha256": original.BATCH_ZIP_SHA256,
        "batch_manifest_sha256": original.BATCH_MANIFEST_SHA256,
        "reviewer_role": "NON_ARM_SOURCE_STATUS_REVIEWER",
        "independence_not_cryptographically_proven": True,
        "method_status": "V06_PROSPECTIVE_NOT_INDEPENDENTLY_ACCEPTED",
        "report_nonce": obj["report_nonce"],
        "restricted_reviewer_exposure_notes": obj["restricted_independent_assessment_notes"],
        "records": obj["records"],
        "authorization": "REVIEW_ONLY_PROPOSED_NOT_AUTHOR_RELEASE",
        "author_world": "WORLD_UNFROZEN",
    }
    original.validate_report(original.canonical(source_check), rows)
    return obj


def report_bytes(obj: dict, rows: list[dict]) -> bytes:
    raw = original.canonical(obj)
    validate_report(raw, rows)
    return raw


def seal(obj: dict, batch_bytes: bytes, cert: Path, *,
         openssl: str | None = None) -> bytes:
    binary = original.openssl_path(openssl)
    original.certificate_ok(cert, binary)
    _, rows = original.load_batch(batch_bytes)
    report = report_bytes(obj, rows)
    p = subprocess.run(
        [binary, "cms", "-encrypt", "-binary", "-aes-256-gcm",
         "-outform", "DER", "-recip", str(cert)],
        input=report, capture_output=True, timeout=40, check=False,
    )
    if (
        p.returncode != 0
        or not 100 <= len(p.stdout) <= original.MAX_CIPHERTEXT_BYTES
        or report in p.stdout
    ):
        raise original.RouteHold("INDEPENDENT_SEAL_FAILED")
    return p.stdout


def verify(cipher_file: Path, batch_bytes: bytes, cert: Path, key: Path,
           password: bytes, *, openssl: str | None = None) -> dict:
    if (
        not isinstance(password, bytes)
        or not 1 <= len(password) <= 256
        or b"\n" in password or b"\r" in password
    ):
        raise original.RouteHold("OWNER_PASSPHRASE_INPUT_INVALID")
    if (
        cipher_file.is_symlink() or not cipher_file.is_file()
        or not 100 <= cipher_file.stat().st_size <= original.MAX_CIPHERTEXT_BYTES
    ):
        raise original.RouteHold("INDEPENDENT_CIPHERTEXT_FILE_INVALID")
    binary = original.openssl_path(openssl)
    original.certificate_ok(cert, binary)
    if (
        key.is_symlink() or not key.is_file()
        or not key.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----")
    ):
        raise original.RouteHold("OWNER_PRIVATE_KEY_INVALID")
    _, rows = original.load_batch(batch_bytes)
    p = subprocess.run(
        [binary, "cms", "-decrypt", "-binary", "-inform", "DER",
         "-in", str(cipher_file), "-recip", str(cert),
         "-inkey", str(key), "-passin", "stdin"],
        input=password + b"\n", capture_output=True, timeout=40, check=False,
    )
    if p.returncode:
        # GCM subprocess stdout, if any, has not yet been authenticated.
        raise original.RouteHold("INDEPENDENT_CMS_AUTHENTICATION_FAILED")
    obj = validate_report(p.stdout, rows)
    return {
        "owner_independent_challenger_cms_authenticated": "PASS",
        "original_source_batch_bound": "PASS",
        "complete_independent_source_records": len(obj["records"]),
        "original_reviewer_conclusions_exposed_to_challenger": False,
        "original_reviewer_report_opened_by_coordinator": False,
        "independent_source_dispositions": "RESTRICTED_NOT_PRINTED",
        "actual_adversarial_challenge": "PENDING",
        "author_world": "WORLD_UNFROZEN",
    }


def cli() -> int:
    parser = argparse.ArgumentParser(description="Independent Wave0 first pass CMS route")
    sub = parser.add_subparsers(dest="action", required=True)
    send = sub.add_parser("seal")
    send.add_argument("--batch-zip", type=Path, required=True)
    send.add_argument("--public-cert", type=Path, required=True)
    send.add_argument("--ciphertext-output", type=Path, required=True)
    send.add_argument("--openssl")
    owner = sub.add_parser("owner-verify")
    owner.add_argument("--batch-zip", type=Path, required=True)
    owner.add_argument("--public-cert", type=Path, required=True)
    owner.add_argument("--private-key", type=Path, required=True)
    owner.add_argument("--ciphertext", type=Path, required=True)
    owner.add_argument("--expected-ciphertext-sha256", required=True)
    owner.add_argument("--openssl")
    args = parser.parse_args()
    if args.action == "seal":
        output = args.ciphertext_output
        if (
            output.name != OUTPUT_NAME or output.exists()
            or output.is_symlink() or not output.parent.is_dir()
        ):
            raise original.RouteHold("INDEPENDENT_CIPHERTEXT_OUTPUT_INVALID")
        obj = original.safe_json(sys.stdin.buffer.read(original.MAX_PLAINTEXT_BYTES + 1))
        cipher = seal(obj, args.batch_zip.read_bytes(), args.public_cert,
                      openssl=args.openssl)
        with output.open("xb") as stream:
            stream.write(cipher)
        print(json.dumps({
            "independent_challenger_first_pass": "SEALED_REPORTED",
            "ciphertext_filename": OUTPUT_NAME,
            "ciphertext_sha256": original.digest(cipher),
            "ciphertext_bytes": len(cipher),
            "restricted_report_printed": False,
            "actual_adversarial_challenge": "PENDING",
            "author_world": "WORLD_UNFROZEN",
        }, sort_keys=True))
        return 0
    if (
        not re.fullmatch("[0-9a-f]{64}", args.expected_ciphertext_sha256)
        or args.ciphertext.is_symlink() or not args.ciphertext.is_file()
        or original.digest(args.ciphertext.read_bytes())
        != args.expected_ciphertext_sha256
    ):
        raise original.RouteHold("INDEPENDENT_CIPHERTEXT_DIGEST_INVALID")
    if not sys.stdin.isatty():
        raise original.RouteHold("OWNER_INTERACTIVE_TERMINAL_REQUIRED")
    passphrase = getpass.getpass(
        "Passphrase for existing owner-held encrypted reviewer key: "
    )
    summary = verify(
        args.ciphertext, args.batch_zip.read_bytes(),
        args.public_cert, args.private_key, passphrase.encode("utf-8"),
        openssl=args.openssl,
    )
    print(json.dumps(summary, sort_keys=True))
    print("S1_WAVE0_OWNER_INDEPENDENT_FIRST_PASS_READBACK=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except (original.RouteHold, OSError, ValueError, TypeError, TimeoutError,
            subprocess.SubprocessError, EOFError):
        print("S1_WAVE0_INDEPENDENT_FIRST_PASS_HOLD", file=sys.stderr)
        sys.exit(2)
