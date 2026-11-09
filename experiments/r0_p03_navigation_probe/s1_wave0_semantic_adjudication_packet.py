"""Owner-only Wave0 final source decision packet export and exact recompute.

NEVER invoke real Export/VerifyExport through the exposed Runtime Bridge.
No real owner-protected file may be read by this engineering coordinator.

Re-authenticates original reviewer, independent first pass, their comparison,
and the returned substantive challenge before constructing one restricted
PLAINTEXT package for exactly one additional, owner-authorized non-arm
semantic adjudicator. All ciphertext originals remain untouched.
"""
from __future__ import annotations

import argparse
import getpass
from io import BytesIO
import json
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile, ZipInfo, ZIP_STORED

from experiments.r0_p03_navigation_probe import (
    s1_wave0_adversarial_packet as earlier,
    s1_wave0_adversarial_challenge_report as challenge,
    s1_wave0_semantic_decision_report as decision,
    s1_source_status_protected_route as original,
)

PACKET_NAME = "R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip"
CHALLENGE_SHA256 = "e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03"
CHALLENGE_BYTES = 49653
FROZEN_ZIP_DATE = (2026, 1, 1, 0, 0, 0)

BRIEF = """WAVE0 RESTRICTED OWNER-AUTHORIZED SEMANTIC ADJUDICATION

This is ONE FINAL FOCUSED TEN-SOURCE DECISION PASS, not another generic
first-pass review or a model-arm experiment. You are one new distinct non-arm
semantic adjudicator. You must not be a prospective primary-task author,
reference/gold writer, B0–B4 arm author, scorer, or project coordinator.

Inspect ORIGINAL_WAVE0_SOURCES.zip: every original source exact bytes.
Inspect PAIRED_FIRST_PASSES.json: both full preserved first-pass proposals,
claims, reasoning and exact-text difference flags.
Inspect SUBSTANTIVE_CHALLENGE.json: all ten real adversarial counterarguments,
challenged claims, missing-context limits, and materiality assessments.
No prior report may be changed or retroactively attributed to another actor.

For EACH of the ten source records, make a fact-grounded reasoned decision
or HOLD. Examine historical/current authority, representation omissions,
provenance, claim materiality, author-exposure/old-gold contamination risk,
strong counterinterpretations, and genuine governing context dependencies.
Separate confirmed author spoilers from mere keyword suspicion. Shared
prior errors must be investigated even where two first passes agreed.

Decisions are only:
- PROSPECTIVE_WHOLE_FILE_CANDIDATE: justified *candidate* for a future source
  admission process, NOT automatically admitted; all needed contexts observed.
- AUXILIARY_ONLY_EXCLUDED_FROM_AUTHOR: scientifically useful internal evidence
  that must not be supplied to scored source/tool/context surface.
- PROHIBIT_AUTHOR_EXPOSURE: source-grounded evidence of impermissible
  design/gold leakage or other exclusion.
- HOLD_FOR_MATERIAL_EVIDENCE: substantial required context, evidence or
  representation cannot be resolved from permitted inputs.

Do not force consensus or pretend a reference outside the packet was checked.
State precisely what is unverified and what would resolve it. It is fine for
a material HOLD to remain; name an actionable gap or justified unavailable
evidence. For all ten give explicit source-based and disclosure-based reasons.
No item is RELEASED, and this packet does not freeze the source world.

Before inspection, disclose your actual tools, prior source/project exposure,
and session independence limitations. No GitHub, web, connected apps, earlier
conversations, project memory, or external material may be consulted.

Complete exactly ten records using ADJUDICATION_SUBMIT.py's TOP_FIELDS,
RECORD_FIELDS and validate_report contract. Encrypt one canonical report
using the bundled owner's PUBLIC certificate via AES-256-GCM CMS (DER).
Return only R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms and a safe receipt
with byte size, SHA-256, ten-record completion and limitations. Never print
private source-specific decisions in a chat transcript, or request the owner's
private key/passphrase. If you cannot actually inspect the sources or encrypt
the binary, explicitly HOLD without fabricating completion.
"""


def authenticated_evidence(
    *, source_zip: Path, first: Path, independent: Path, comparison: Path,
    challenge_packet: Path, challenge_cms: Path,
    cert: Path, key: Path, previous_sender: Path, password: bytes,
    openssl: str | None = None,
) -> tuple[bytes, bytes, bytes, bytes]:
    if (
        challenge_packet.is_symlink() or not challenge_packet.is_file()
        or challenge_cms.is_symlink() or not challenge_cms.is_file()
        or not challenge_cms.stat().st_size == CHALLENGE_BYTES
        or original.digest(challenge_cms.read_bytes()) != CHALLENGE_SHA256
        or previous_sender.is_symlink() or not previous_sender.is_file()
    ):
        raise original.RouteHold("ADJUDICATION_PRIOR_CHALLENGE_INPUT_INVALID")
    raw_orig, paired, public_cert = earlier.authenticate_inputs(
        source_zip, first, independent, comparison, cert, key, password,
        openssl=openssl,
    )
    canonical_previous_packet = earlier.check_bundle(
        raw_orig, paired, public_cert, previous_sender.read_bytes()
    )
    actual_previous_packet = challenge_packet.read_bytes()
    if canonical_previous_packet != actual_previous_packet:
        raise original.RouteHold("ADJUDICATION_PRIOR_PACKET_RECOMPUTATION_MISMATCH")
    binary = original.openssl_path(openssl)
    # The prior challenge ciphertext has been identified by exact SHA-256;
    # its decrypted plaintext is accepted only after OpenSSL GCM authentication.
    p = subprocess.run([
        binary, "cms", "-decrypt", "-binary", "-inform", "DER",
        "-in", str(challenge_cms), "-recip", str(cert),
        "-inkey", str(key), "-passin", "stdin",
    ], input=password+b"\n", capture_output=True, timeout=40, check=False)
    if p.returncode:
        raise original.RouteHold("ADJUDICATION_PRIOR_CHALLENGE_CMS_AUTH_FAILED")
    report = challenge.json_object(p.stdout)
    if challenge.canonical(report) != p.stdout:
        raise original.RouteHold("ADJUDICATION_PRIOR_CHALLENGE_NOT_CANONICAL")
    challenge.validate_report(report, actual_previous_packet)
    return raw_orig, paired, p.stdout, public_cert


def make_packet(
    original_zip: bytes, paired_json: bytes, challenge_json: bytes,
    cert: bytes, sender: bytes,
) -> bytes:
    if (
        not 500 <= len(sender) <= 100_000
        or not cert.startswith(b"-----BEGIN CERTIFICATE-----")
    ):
        raise original.RouteHold("ADJUDICATION_SENDER_OR_CERT_INVALID")
    manifest = {
        "format": decision.INPUT_FORMAT,
        "original_source_sha256": original.digest(original_zip),
        "paired_plaintext_sha256": original.digest(paired_json),
        "challenge_plaintext_sha256": original.digest(challenge_json),
        "public_cert_sha256": original.digest(cert),
        "sender_code_sha256": original.digest(sender),
        "prior_comparison_ciphertext_sha256": earlier.COMPARISON_SHA256,
        "prior_challenge_ciphertext_sha256": CHALLENGE_SHA256,
        "source_ref": decision.SOURCE_REF,
        "source_count": 10,
        "author_release": "NONE",
        "source_world": "WORLD_UNFROZEN",
    }
    out = BytesIO()
    with ZipFile(out, "w", allowZip64=False) as archive:
        for name, payload in (
            ("ADJUDICATION_MANIFEST.json", original.canonical(manifest)),
            ("ADJUDICATION_BRIEF.txt", BRIEF.encode("utf-8")),
            ("ORIGINAL_WAVE0_SOURCES.zip", original_zip),
            ("PAIRED_FIRST_PASSES.json", paired_json),
            ("SUBSTANTIVE_CHALLENGE.json", challenge_json),
            ("OWNER_PUBLIC_CERT.pem", cert),
            ("ADJUDICATION_SUBMIT.py", sender),
        ):
            info = ZipInfo(name, date_time=FROZEN_ZIP_DATE)
            info.compress_type = ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o600 << 16
            archive.writestr(info, payload)
    packet = out.getvalue()
    # The public standalone recipient code independently checks all original
    # source SHA/blob and each prior assessment/challenge source identity.
    decision.inspect_packet(packet)
    return packet


def owner_export(
    *, action: str, source_zip: Path, first: Path, independent: Path,
    comparison: Path, challenge_packet: Path, challenge_cms: Path,
    cert: Path, key: Path, previous_sender: Path,
    sender: Path, output: Path, password: bytes, openssl: str | None = None,
) -> dict:
    if action not in ("Export", "VerifyExport"):
        raise original.RouteHold("ADJUDICATION_EXPORT_ACTION_INVALID")
    root = comparison.parent.resolve()
    if (
        output.name != PACKET_NAME
        or not output.parent.is_dir()
        or any(x.is_symlink() or x.parent.resolve() != root for x in (
            first, independent, comparison, challenge_packet, challenge_cms,
            cert, key, output,
        ))
        or sender.is_symlink() or not sender.is_file()
    ):
        raise original.RouteHold("ADJUDICATION_EXPORT_SCOPE_INVALID")
    if action == "Export" and output.exists():
        raise original.RouteHold("ADJUDICATION_PACKET_ALREADY_EXISTS")
    raw_orig, paired, challenged, public_cert = authenticated_evidence(
        source_zip=source_zip, first=first, independent=independent,
        comparison=comparison, challenge_packet=challenge_packet,
        challenge_cms=challenge_cms, cert=cert, key=key,
        previous_sender=previous_sender, password=password, openssl=openssl,
    )
    expected = make_packet(
        raw_orig, paired, challenged, public_cert, sender.read_bytes()
    )
    if action == "Export":
        with output.open("xb") as file:
            file.write(expected)
        status = "RESTRICTED_SEMANTIC_PACKET_CREATED"
    else:
        if not output.is_file() or output.is_symlink():
            raise original.RouteHold("ADJUDICATION_PACKET_MISSING")
        if output.read_bytes() != expected:
            raise original.RouteHold("ADJUDICATION_PACKET_RECOMPUTATION_MISMATCH")
        status = "RESTRICTED_PACKET_INDEPENDENT_RECOMPUTATION_PASS"
    return {
        "owner_semantic_packet": status,
        "both_first_passes_authenticated": "PASS",
        "prior_pair_recomputed": "PASS",
        "original_adversarial_challenge_authenticated": "PASS",
        "exact_source_count": 10,
        "restricted_plaintext_packet": True,
        "packet_bytes": len(expected),
        "packet_sha256": original.digest(expected),
        "private_source_specific_findings_printed": False,
        "actual_new_adjudication": "PENDING",
        "source_world": "WORLD_UNFROZEN",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Owner-only restricted semantic packet exporter")
    parser.add_argument("--action", choices=["Export", "VerifyExport"], required=True)
    for arg in (
        "source-zip", "first-cms", "independent-cms", "comparison-cms",
        "challenge-packet", "challenge-cms", "public-cert", "private-key",
        "previous-sender", "sender", "output",
    ):
        parser.add_argument("--"+arg, type=Path, required=True)
    parser.add_argument("--openssl")
    args = parser.parse_args()
    if not sys.stdin.isatty():
        raise original.RouteHold("ADJUDICATION_OWNER_INTERACTIVE_REQUIRED")
    password = getpass.getpass("Existing owner encrypted-key passphrase: ").encode("utf-8")
    result = owner_export(
        action=args.action, source_zip=args.source_zip, first=args.first_cms,
        independent=args.independent_cms, comparison=args.comparison_cms,
        challenge_packet=args.challenge_packet, challenge_cms=args.challenge_cms,
        cert=args.public_cert, key=args.private_key,
        previous_sender=args.previous_sender, sender=args.sender,
        output=args.output, password=password, openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_SEMANTIC_PACKET_"+args.action.upper()+"=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (original.RouteHold, decision.Hold, OSError, ValueError,
            TypeError, EOFError, subprocess.SubprocessError, TimeoutError):
        print("S1_WAVE0_OWNER_SEMANTIC_PACKET_HOLD", file=sys.stderr)
        sys.exit(2)
