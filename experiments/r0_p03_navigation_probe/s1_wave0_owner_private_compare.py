"""Owner-local authenticated comparison of two real Wave0 restricted reports.

NEVER run on actual owner material through an exposed assistant coordinator.
This code is reviewed/qualified with invented source/report/key fixtures only.

Both CMS inputs are authenticated before plaintext is interpreted. Original
source identity and both strict report schemas are validated. A paired,
non-adjudicated dossier of full restricted records and mechanical differences
is encrypted to the existing owner certificate BEFORE it is stored. No source
path, disposition, dispute count, evidence reason, decrypted content, original
CMS, or private key is emitted in the safe console receipt.

An exact match is not scientific agreement or adversarial acceptance. The
dossier remains owner-only and every record requires substantive challenge.
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
    s1_source_status_protected_route as reviewer,
    s1_wave0_independent_challenger_first_pass as challenger,
)

FORMAT = "ads-r0-p03-wave0-owner-private-paired-comparison-v1"
OUTPUT_NAME = "R0_P03_S1_WAVE0_OWNER_PRIVATE_COMPARISON.cms"
REVIEWER_SHA = challenger.ORIGINAL_CIPHERTEXT_SHA256
CHALLENGER_SHA = "50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64"
MAX_DOSSIER_PLAINTEXT_BYTES = 500_000
MAX_DOSSIER_CIPHERTEXT_BYTES = 600_000
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
MECHANICAL_FIELDS = (
    ("inspected", "INSPECTION_STATE_TEXT_DIFF"),
    ("proposed_disposition", "SOURCE_DISPOSITION_TOKEN_DIFF"),
    ("proposed_claims", "SOURCE_CLAIMS_EXACT_TEXT_DIFF"),
    ("context_and_representation_gaps", "CONTEXT_GAPS_EXACT_TEXT_DIFF"),
    ("contamination_and_author_exposure_risks", "EXPOSURE_RISKS_EXACT_TEXT_DIFF"),
    ("source_bound_private_reasoning", "REASONING_EXACT_TEXT_DIFF"),
)


def check_cipher_file(path: Path, expected_hash: str, *, max_size: int) -> None:
    if (
        not path.is_file() or path.is_symlink()
        or not 100 <= path.stat().st_size <= max_size
        or reviewer.digest(path.read_bytes()) != expected_hash
    ):
        raise reviewer.RouteHold("PRIVATE_CIPHERTEXT_IDENTITY_INVALID")


def load_inputs(batch_path: Path, first: Path, second: Path) -> list[dict]:
    if batch_path.is_symlink() or not batch_path.is_file():
        raise reviewer.RouteHold("WAVE0_OWNER_SOURCE_ARCHIVE_UNAVAILABLE")
    _, rows = reviewer.load_batch(batch_path.read_bytes())
    check_cipher_file(first, REVIEWER_SHA, max_size=reviewer.MAX_CIPHERTEXT_BYTES)
    check_cipher_file(second, CHALLENGER_SHA, max_size=reviewer.MAX_CIPHERTEXT_BYTES)
    return rows


def decrypt_authenticated(
    path: Path, cert: Path, key: Path, passphrase: bytes,
    *, openssl: str, first_report: bool, rows: list[dict],
) -> dict:
    # OpenSSL reads ciphertext from an explicit file, not passphrase stdin.
    p = subprocess.run([
        openssl, "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(path), "-recip", str(cert),
        "-inkey", str(key), "-passin", "stdin",
    ], input=passphrase + b"\n", capture_output=True, timeout=40, check=False)
    if p.returncode != 0:
        # Any partial stdout is untrusted until GCM verification succeeds.
        raise reviewer.RouteHold("PRIVATE_CMS_AUTHENTICATION_FAILED")
    if first_report:
        return reviewer.validate_report(p.stdout, rows)
    return challenger.validate_report(p.stdout, rows)


def paired_dossier(first: dict, second: dict, rows: list[dict]) -> dict:
    if (
        len(first["records"]) != len(second["records"])
        or len(first["records"]) != len(rows)
        or len(rows) != 10
    ):
        raise reviewer.RouteHold("PRIVATE_COMPARISON_RECORD_COUNT_INVALID")
    pairs = []
    for index, (a, b, source) in enumerate(
        zip(first["records"], second["records"], rows, strict=True)
    ):
        for item in (a, b):
            if (
                item["path"] != source["path"]
                or item["git_blob_oid"] != source["git_blob_oid"]
                or item["sha256"] != source["sha256"]
                or item["challenge_state"] != "CHALLENGE_PENDING"
            ):
                raise reviewer.RouteHold("PRIVATE_COMPARISON_SOURCE_BINDING_INVALID")
        differences = [
            label for field, label in MECHANICAL_FIELDS if a[field] != b[field]
        ]
        pairs.append({
            "manifest_index": index,
            "original_path": source["path"],
            "git_blob_oid": source["git_blob_oid"],
            "source_sha256": source["sha256"],
            "first_reviewer_restricted_record": a,
            "independent_challenger_restricted_record": b,
            "mechanical_exact_text_differences": differences,
            "exact_text_comparison_is_not_semantic_agreement": True,
            "source_status_adjudication": "NOT_ADJUDICATED",
            "targeted_evidential_challenge": "PENDING",
        })
    return {
        "format": FORMAT,
        "source_ref": reviewer.SOURCE_PIN,
        "source_batch_sha256": reviewer.BATCH_ZIP_SHA256,
        "source_manifest_sha256": reviewer.BATCH_MANIFEST_SHA256,
        "first_reviewer_ciphertext_sha256": REVIEWER_SHA,
        "independent_challenger_ciphertext_sha256": CHALLENGER_SHA,
        "first_reviewer_role": first["reviewer_role"],
        "challenger_role": second["candidate_role"],
        "blind_first_pass_unverified_provider_isolation": True,
        "owner_comparison_kind": "EXACT_TEXT_DIFFERENCES_NOT_SEMANTIC_ADJUDICATION",
        "private_paired_source_records": pairs,
        "complete_record_count": len(pairs),
        "every_source_requires_substantive_adversarial_review": True,
        "reviewer_report_preserved": True,
        "challenger_report_preserved": True,
        "release_authorization": "NONE",
        "author_world": "WORLD_UNFROZEN",
        "actual_adversarial_challenge": "PENDING",
    }


def make_plaintext(rows: list[dict], first: dict, second: dict) -> bytes:
    data = reviewer.canonical(paired_dossier(first, second, rows))
    if not 500 <= len(data) <= MAX_DOSSIER_PLAINTEXT_BYTES:
        raise reviewer.RouteHold("PRIVATE_COMPARISON_SIZE_INVALID")
    return data


def seal_dossier(plaintext: bytes, cert: Path, *, openssl: str) -> bytes:
    p = subprocess.run([
        openssl, "cms", "-encrypt", "-binary", "-aes-256-gcm",
        "-outform", "DER", "-recip", str(cert),
    ], input=plaintext, capture_output=True, timeout=40, check=False)
    if (
        p.returncode != 0
        or not 100 <= len(p.stdout) <= MAX_DOSSIER_CIPHERTEXT_BYTES
        or plaintext in p.stdout
    ):
        raise reviewer.RouteHold("PRIVATE_COMPARISON_SEAL_FAILED")
    return p.stdout


def owner_operation(
    batch: Path, first_path: Path, second_path: Path,
    cert: Path, key: Path, out: Path, password: bytes,
    *, action: str, openssl: str | None = None,
) -> dict:
    if action not in ("Compare", "Verify"):
        raise reviewer.RouteHold("PRIVATE_COMPARISON_ACTION_INVALID")
    if (
        not isinstance(password, bytes)
        or not 1 <= len(password) <= 256
        or b"\n" in password or b"\r" in password
    ):
        raise reviewer.RouteHold("OWNER_PASSPHRASE_INPUT_INVALID")
    binary = reviewer.openssl_path(openssl)
    reviewer.certificate_ok(cert, binary)
    if (
        not key.is_file() or key.is_symlink()
        or not key.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----")
    ):
        raise reviewer.RouteHold("OWNER_ENCRYPTED_PRIVATE_KEY_INVALID")
    if (
        out.name != OUTPUT_NAME or out.is_symlink() or
        not out.parent.is_dir() or out.parent.resolve() != first_path.parent.resolve()
        or second_path.parent.resolve() != first_path.parent.resolve()
        or key.parent.resolve() != first_path.parent.resolve()
        or cert.parent.resolve() != first_path.parent.resolve()
    ):
        raise reviewer.RouteHold("OWNER_PRIVATE_COMPARISON_OUTPUT_INVALID")
    if action == "Compare" and out.exists():
        raise reviewer.RouteHold("OWNER_COMPARISON_ALREADY_EXISTS")
    rows = load_inputs(batch, first_path, second_path)
    first = decrypt_authenticated(
        first_path, cert, key, password, openssl=binary,
        first_report=True, rows=rows,
    )
    second = decrypt_authenticated(
        second_path, cert, key, password, openssl=binary,
        first_report=False, rows=rows,
    )
    expected = make_plaintext(rows, first, second)
    if action == "Compare":
        sealed = seal_dossier(expected, cert, openssl=binary)
        with out.open("xb") as file:
            file.write(sealed)
        label = "STORED_ENCRYPTED"
        saved = sealed
    else:
        if not out.is_file() or out.is_symlink():
            raise reviewer.RouteHold("OWNER_COMPARISON_CIPHERTEXT_MISSING")
        saved = out.read_bytes()
        if not 100 <= len(saved) <= MAX_DOSSIER_CIPHERTEXT_BYTES:
            raise reviewer.RouteHold("OWNER_COMPARISON_CIPHERTEXT_SIZE_INVALID")
        # The stored dossier is independently authenticated and rechecked
        # against freshly decrypted, strictly validated original reports.
        r = subprocess.run([
            binary, "cms", "-decrypt", "-binary", "-inform", "DER",
            "-in", str(out), "-recip", str(cert),
            "-inkey", str(key), "-passin", "stdin",
        ], input=password + b"\n", capture_output=True, timeout=40, check=False)
        if r.returncode:
            raise reviewer.RouteHold("OWNER_COMPARISON_CMS_AUTHENTICATION_FAILED")
        if r.stdout != expected:
            raise reviewer.RouteHold("OWNER_COMPARISON_RECOMPUTATION_MISMATCH")
        label = "INDEPENDENT_RECOMPUTATION_PASS"
    return {
        "owner_private_comparison": label,
        "original_reviewer_authenticated": "PASS",
        "independent_challenger_authenticated": "PASS",
        "original_source_batch_bound": "PASS",
        "paired_complete_record_count": len(rows),
        "private_encrypted_dossier_sha256": reviewer.digest(saved),
        "private_encrypted_dossier_bytes": len(saved),
        "source_specific_differences_printed": False,
        "source_status_adjudication": "NOT_STARTED",
        "actual_adversarial_challenge": "PENDING",
        "author_world": "WORLD_UNFROZEN",
    }


def cli() -> int:
    parser = argparse.ArgumentParser(description="Owner-only Wave0 dual CMS comparison")
    parser.add_argument("--action", choices=["Compare", "Verify"], required=True)
    parser.add_argument("--batch-zip", type=Path, required=True)
    parser.add_argument("--reviewer-cms", type=Path, required=True)
    parser.add_argument("--challenger-cms", type=Path, required=True)
    parser.add_argument("--public-cert", type=Path, required=True)
    parser.add_argument("--private-key", type=Path, required=True)
    parser.add_argument("--comparison-cms", type=Path, required=True)
    parser.add_argument("--openssl")
    args = parser.parse_args()
    if not sys.stdin.isatty():
        raise reviewer.RouteHold("OWNER_INTERACTIVE_TERMINAL_REQUIRED")
    password = getpass.getpass("Existing Wave0 owner key passphrase: ")
    result = owner_operation(
        args.batch_zip, args.reviewer_cms, args.challenger_cms,
        args.public_cert, args.private_key, args.comparison_cms,
        password.encode("utf-8"), action=args.action, openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_PRIVATE_COMPARISON_"+args.action.upper()+"=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(cli())
    except (
        reviewer.RouteHold, OSError, ValueError, TypeError, TimeoutError,
        subprocess.SubprocessError, EOFError,
    ):
        print("S1_WAVE0_OWNER_PRIVATE_COMPARISON_HOLD", file=sys.stderr)
        sys.exit(2)
