"""Owner-only, explicitly authorized Wave0 adversarial challenger packet.

The only plaintext export is written with exclusive creation into the existing
owner ACL-protected directory, after fresh authentication of all THREE owner
CMS artifacts and exact deterministic recomputation of the paired dossier.

Never run Export / VerifyExport on the real owner data via Runtime Bridge.
Run through the owner's ordinary interactive local PowerShell only.
The packet is RESTRICTED PLAINTEXT, for exactly one non-arm challenger.
It is not blind-author material, scoring gold, or evidence of adjudication.
"""
from __future__ import annotations

import argparse
import getpass
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZIP_STORED, ZipFile, ZipInfo

from experiments.r0_p03_navigation_probe import (
    s1_source_status_protected_route as source,
    s1_wave0_owner_private_compare as paired,
)

FORMAT = "ads-r0-p03-s1-wave0-adversarial-input-v1"
NAME = "R0_P03_S1_WAVE0_RESTRICTED_ADVERSARIAL_INPUT.zip"
COMPARISON_SHA256 = "f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3"
SOURCE_ZIP_MEMBER = "WAVE0_ORIGINAL_SOURCES.zip"
PAIRED_MEMBER = "OWNER_PRIVATE_PAIRED_EVIDENCE.json"
CERT_MEMBER = "OWNER_PUBLIC_ENCRYPTION_CERT.pem"
SUBMIT_MEMBER = "CHALLENGE_SUBMIT.py"
MANIFEST_MEMBER = "CHALLENGE_MANIFEST.json"
BRIEF_MEMBER = "CHALLENGE_BRIEF.txt"
MAX_PACKET_BYTES = 950_000
MAX_SUBMIT_BYTES = 75_000
OUTPUT_STATE = "AUTHOR_WORLD_UNFROZEN_SOURCE_STATUS_CHALLENGE_ONLY"
FROZEN_ZIP_DATE = (2026, 1, 1, 0, 0, 0)

BRIEF = """RESTRICTED WAVE0 ADVERSARIAL SOURCE-STATUS CHALLENGE

This is the explicitly owner-authorized SECOND STAGE, not another blind first
pass. Its recipient must be an exclusively NON-ARM challenger, never a future
scored author, gold/reference writer, arm author, evaluator, or coordinator.

Original first-pass independence is preserved by keeping both prior reports
immutable. The first reviewer and independent first-pass challenger records
are now deliberately exposed to THIS challenger for adversarial criticism.

Read all ten exact original source files in WAVE0_ORIGINAL_SOURCES.zip and
the full paired reviewer records in OWNER_PRIVATE_PAIRED_EVIDENCE.json.
The latter includes proposed dispositions, claims, complete restricted
reasoning, exposure risks, and exact-text differences. All ten require
substantive challenge, including matching dispositions or similar reasoning.

Assess each prior claim against the actual original historical bytes.
Challenge unsupported assumptions, incomplete temporal authority, genuine
context requirements, absent source bodies, relevant modalities, confirmed
vs merely suspected design/gold disclosure, and shared blind spots.
Explain the strongest counterinterpretation and falsifying evidence for both
claim materiality and disclosure materiality. Phrase differences are not
necessarily scientific disagreements. Agreement is never automatic acceptance.
Where essential source context is absent, HOLD rather than invent it.

Do not consult external repositories, chat history, connected apps, web
search, old gold, or prior tasks. Do not transfer evidence to anyone other
than this authorized challenger session. Report truthful unknowns and
limitations, including source/context gaps and actual session exposure.

Produce a NEW complete 10-record, source-bound restricted report according
to CHALLENGE_SUBMIT.py; do not change either first-pass report. Seal the
new report to OWNER_PUBLIC_ENCRYPTION_CERT.pem with AES-256-GCM CMS and
return ONLY the resulting CMS file plus a safe size/hash receipt. Never
return private source findings in chat. Never request the owner private key
or passphrase. Challenge findings are provisional, not author admissions,
source-world freeze, hidden gold, or B0-B4 results.

If source contents cannot be examined, the report cannot honestly declare
the challenge complete. Explicitly HOLD rather than invent inspection.
"""

def check_bundle(
    original_zip: bytes, comparison_plaintext: bytes, certificate: bytes,
    sender_code: bytes,
) -> bytes:
    _, sources = source.load_batch(original_zip)
    if not sender_code or len(sender_code) > MAX_SUBMIT_BYTES:
        raise source.RouteHold("CHALLENGE_SUBMISSION_MODULE_INVALID")
    obj = source.safe_json(comparison_plaintext)
    if source.canonical(obj) != comparison_plaintext:
        raise source.RouteHold("CHALLENGE_COMPARISON_NONCANONICAL")
    if (
        obj.get("format") != paired.FORMAT
        or obj.get("source_batch_sha256") != source.BATCH_ZIP_SHA256
        or obj.get("source_manifest_sha256") != source.BATCH_MANIFEST_SHA256
        or obj.get("first_reviewer_ciphertext_sha256") != paired.REVIEWER_SHA
        or obj.get("independent_challenger_ciphertext_sha256") != paired.CHALLENGER_SHA
        or obj.get("complete_record_count") != 10
        or obj.get("actual_adversarial_challenge") != "PENDING"
        or obj.get("release_authorization") != "NONE"
        or obj.get("author_world") != "WORLD_UNFROZEN"
    ):
        raise source.RouteHold("CHALLENGE_COMPARISON_BINDING_INVALID")
    records = obj.get("private_paired_source_records")
    if not isinstance(records, list) or len(records) != len(sources):
        raise source.RouteHold("CHALLENGE_PAIR_COUNT_INVALID")
    for index, (row, rec) in enumerate(zip(sources, records, strict=True)):
        if not isinstance(rec, dict) or any((
            rec.get("manifest_index") != index,
            rec.get("original_path") != row["path"],
            rec.get("git_blob_oid") != row["git_blob_oid"],
            rec.get("source_sha256") != row["sha256"],
            rec.get("source_status_adjudication") != "NOT_ADJUDICATED",
            rec.get("targeted_evidential_challenge") != "PENDING",
            not isinstance(rec.get("first_reviewer_restricted_record"), dict),
            not isinstance(rec.get("independent_challenger_restricted_record"), dict),
        )):
            raise source.RouteHold("CHALLENGE_PAIR_SOURCE_MISMATCH")
    if b"-----BEGIN CERTIFICATE-----" not in certificate or len(certificate) > 20000:
        raise source.RouteHold("CHALLENGE_PUBLIC_CERT_INVALID")
    manifest = {
        "format": FORMAT,
        "source_zip_sha256": source.digest(original_zip),
        "private_paired_evidence_sha256": source.digest(comparison_plaintext),
        "public_certificate_sha256": source.digest(certificate),
        "submission_tool_sha256": source.digest(sender_code),
        "complete_source_records": 10,
        "first_reviewer_ciphertext_sha256": paired.REVIEWER_SHA,
        "independent_first_pass_ciphertext_sha256": paired.CHALLENGER_SHA,
        "owner_comparison_ciphertext_sha256": COMPARISON_SHA256,
        "evidence_status": OUTPUT_STATE,
        "new_adversarial_challenge_completed": False,
        "new_author_source_admissions": 0,
    }
    output = BytesIO()
    with ZipFile(output, "w", allowZip64=False) as archive:
        for name, value in (
            (MANIFEST_MEMBER, source.canonical(manifest)),
            (BRIEF_MEMBER, BRIEF.encode("utf-8")),
            (SOURCE_ZIP_MEMBER, original_zip),
            (PAIRED_MEMBER, comparison_plaintext),
            (CERT_MEMBER, certificate),
            (SUBMIT_MEMBER, sender_code),
        ):
            info = ZipInfo(name, date_time=FROZEN_ZIP_DATE)
            info.compress_type = ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o600 << 16
            archive.writestr(info, value)
    data = output.getvalue()
    if not 1000 <= len(data) <= MAX_PACKET_BYTES:
        raise source.RouteHold("CHALLENGE_PACKET_SIZE_INVALID")
    return data


def authenticate_inputs(
    batch: Path, reviewer: Path, independent: Path, comparison: Path,
    cert: Path, key: Path, password: bytes, *, openssl: str | None = None,
) -> tuple[bytes, bytes, bytes]:
    if not isinstance(password, bytes) or not 1 <= len(password) <= 256 or (
        b"\n" in password or b"\r" in password
    ):
        raise source.RouteHold("CHALLENGE_OWNER_PASSWORD_INVALID")
    if any(p.is_symlink() or not p.is_file() for p in (
        batch, reviewer, independent, comparison, cert, key
    )):
        raise source.RouteHold("CHALLENGE_INPUT_FILE_INVALID")
    binary = source.openssl_path(openssl)
    source.certificate_ok(cert, binary)
    if not key.read_bytes().startswith(b"-----BEGIN ENCRYPTED PRIVATE KEY-----"):
        raise source.RouteHold("CHALLENGE_OWNER_KEY_NOT_ENCRYPTED")
    paired.check_cipher_file(
        comparison, COMPARISON_SHA256,
        max_size=paired.MAX_DOSSIER_CIPHERTEXT_BYTES,
    )
    rows = paired.load_inputs(batch, reviewer, independent)
    a = paired.decrypt_authenticated(
        reviewer, cert, key, password, openssl=binary,
        first_report=True, rows=rows,
    )
    b = paired.decrypt_authenticated(
        independent, cert, key, password, openssl=binary,
        first_report=False, rows=rows,
    )
    expected = paired.make_plaintext(rows, a, b)
    p = subprocess.run([
        binary, "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(comparison), "-recip", str(cert), "-inkey", str(key),
        "-passin", "stdin",
    ], input=password + b"\n", capture_output=True, timeout=40, check=False)
    if p.returncode:
        raise source.RouteHold("CHALLENGE_COMPARISON_AUTHENTICATION_FAILED")
    if p.stdout != expected:
        raise source.RouteHold("CHALLENGE_COMPARISON_RECOMPUTATION_MISMATCH")
    return batch.read_bytes(), expected, cert.read_bytes()


def run_owner(
    *, action: str, batch: Path, reviewer: Path, independent: Path,
    comparison: Path, cert: Path, key: Path, sender: Path,
    output: Path, password: bytes, openssl: str | None = None,
) -> dict:
    if action not in ("Export", "VerifyExport"):
        raise source.RouteHold("CHALLENGE_ACTION_INVALID")
    home = comparison.parent.resolve()
    if (
        output.name != NAME or not output.parent.is_dir()
        or any(p.parent.resolve() != home for p in (
            reviewer, independent, comparison, cert, key, output
        ))
        or output.is_symlink() or sender.is_symlink() or not sender.is_file()
    ):
        raise source.RouteHold("CHALLENGE_OUTPUT_SCOPE_INVALID")
    if action == "Export" and output.exists():
        raise source.RouteHold("CHALLENGE_PACKET_ALREADY_EXISTS")
    original_zip, comparison_plain, public_cert = authenticate_inputs(
        batch, reviewer, independent, comparison, cert, key, password,
        openssl=openssl,
    )
    expected = check_bundle(
        original_zip, comparison_plain, public_cert, sender.read_bytes()
    )
    if action == "Export":
        with output.open("xb") as file:
            file.write(expected)
        status = "RESTRICTED_PLAINTEXT_PACKET_CREATED"
    else:
        if not output.is_file() or output.is_symlink():
            raise source.RouteHold("CHALLENGE_PACKET_MISSING")
        if output.read_bytes() != expected:
            raise source.RouteHold("CHALLENGE_PACKET_RECOMPUTATION_MISMATCH")
        status = "INDEPENDENT_PACKET_RECOMPUTATION_PASS"
    return {
        "owner_adversarial_input": status,
        "first_reviewer_authenticated": "PASS",
        "independent_first_pass_authenticated": "PASS",
        "owner_pair_authenticated_and_recomputed": "PASS",
        "pinned_original_sources": 10,
        "packet_bytes": len(expected),
        "packet_sha256": source.digest(expected),
        "restricted_plaintext_packet": True,
        "source_specific_content_printed": False,
        "second_stage_challenge": "PENDING",
        "author_world": "WORLD_UNFROZEN",
    }


def main() -> int:
    cli = argparse.ArgumentParser(description="Owner-only Wave0 real challenge input exporter")
    cli.add_argument("--action", choices=["Export", "VerifyExport"], required=True)
    for name in ("batch-zip", "reviewer-cms", "challenger-cms", "comparison-cms",
                 "public-cert", "private-key", "sender-module", "output"):
        cli.add_argument("--" + name, type=Path, required=True)
    cli.add_argument("--openssl")
    args = cli.parse_args()
    if not sys.stdin.isatty():
        raise source.RouteHold("CHALLENGE_OWNER_INTERACTIVE_REQUIRED")
    password = getpass.getpass("Existing Wave0 owner encrypted-key passphrase: ")
    result = run_owner(
        action=args.action, batch=args.batch_zip,
        reviewer=args.reviewer_cms, independent=args.challenger_cms,
        comparison=args.comparison_cms, cert=args.public_cert,
        key=args.private_key, sender=args.sender_module,
        output=args.output, password=password.encode("utf-8"),
        openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_ADVERSARIAL_PACKET_"+args.action.upper()+"=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (source.RouteHold, OSError, ValueError, TypeError, EOFError,
            subprocess.SubprocessError, TimeoutError):
        print("S1_WAVE0_OWNER_ADVERSARIAL_PACKET_HOLD", file=sys.stderr)
        sys.exit(2)
