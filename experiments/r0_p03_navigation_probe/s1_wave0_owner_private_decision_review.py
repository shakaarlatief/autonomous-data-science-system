"""Owner-local protected review of authenticated Wave0 semantic proposals.

This module never accepts/rejects any source, never changes prior CMS evidence,
and never transfers source-specific private findings to the public coordinator.
Only owner-interactive PowerShell may run it on the real protected directory.
All tests use invented sources and disposable keys.
"""
from __future__ import annotations

import argparse
from collections import Counter
from hashlib import sha256
from io import BytesIO
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

from experiments.r0_p03_navigation_probe import (
    s1_wave0_semantic_decision_report as decision,
)

NAME = "R0_P03_S1_WAVE0_OWNER_PRIVATE_DECISION_REVIEW.md"
MAX_REVIEW_BYTES = 5_000_000


def fence(value: str, language: str = "") -> str:
    """Quote exact evidence as inert Markdown code, not active markup."""
    tick = chr(96)
    largest = max(
        (len(match.group(0)) for match in re.finditer(tick + "+", value)),
        default=0,
    )
    bound = tick * max(4, largest + 1)
    return f"{bound}{language}\n{value}\n{bound}\n"


def render(packet: bytes, report: dict) -> bytes:
    """Assemble an owner-private dossier from source-authenticated evidence."""
    decision.validate_report(report, packet)
    _, rows, _ = decision.inspect_packet(packet)
    with ZipFile(BytesIO(packet)) as bundle:
        zip_bytes = bundle.read("ORIGINAL_WAVE0_SOURCES.zip")
        previous = decision.parse(bundle.read("PAIRED_FIRST_PASSES.json"))
        critique = decision.parse(bundle.read("SUBSTANTIVE_CHALLENGE.json"))
    prior = previous["private_paired_source_records"]
    challenges = critique["records"]
    decisions = report["records"]
    counts = Counter(item["decision"] for item in decisions)
    tick = chr(96)
    lines = [
        "# RESTRICTED: Wave0 owner source-status qualification review",
        "",
        "**OWNER PRIVATE. Do not publish, upload, sync, or share this review with",
        "public coordinator, future task authors, reference writers, arms or scorers.**",
        "",
        "This review reproduces real, authenticated proposals with their sources.",
        "**It makes NO scientific decision and releases NO source.**",
        "",
        "Original source pin: " + tick + decision.SOURCE_REF + tick,
        "Original archive SHA-256: " + tick + decision.ORIGINAL_SOURCE_SHA + tick,
        "Input packet SHA-256: " + tick + sha256(packet).hexdigest() + tick,
        "",
        "## Restricted proposal summary",
        "",
        "| Proposed outcome | Count |",
        "| --- | ---: |",
    ]
    for outcome in sorted(decision.DECISIONS):
        lines.append("| " + tick + outcome + tick + f" | {counts.get(outcome, 0)} |")
    lines.extend([
        "",
        "These are proposals, not owner-accepted statuses or source admissions.",
        "Material unavailable context is a HOLD unless defensible exclusion",
        "is established for the prospectively fixed experiment source world.",
        "",
        "## Owner source-by-source review",
        "",
    ])
    with ZipFile(BytesIO(zip_bytes)) as original:
        for index, (source, first_pair, challenge, proposal) in enumerate(
            zip(rows, prior, challenges, decisions, strict=True), start=1
        ):
            raw = original.read("sources/" + source["path"])
            try:
                original_text = raw.decode("utf-8-sig")
            except UnicodeDecodeError:
                original_text = (
                    "NOT RENDERABLE AS UTF-8. Original archive must be separately "
                    "examined before accepting source claims. Exact SHA-256: "
                    + sha256(raw).hexdigest()
                )
            pretty = lambda data: json.dumps(
                data, sort_keys=True, ensure_ascii=True, indent=2
            )
            lines.extend([
                f"### Source {index:02d} / 10",
                "",
                "**Adjudicator proposal:** " + tick + proposal["decision"] + tick,
                "",
                "#### Exact identity",
                fence(pretty(source), "json"),
                "#### Original historical source",
                fence(original_text, "text"),
                "#### Both original first-pass reviews and paired evidence",
                fence(pretty(first_pair), "json"),
                "#### Substantive adversarial challenge",
                fence(pretty(challenge), "json"),
                "#### Proposed semantic decision with complete reasoning",
                fence(pretty(proposal), "json"),
                "#### Owner qualification",
                "",
                "Check the original evidence against all three assessments.",
                "Distinguish supported historical claims, material missing",
                "context, author disclosure/old-gold exposure and mere suspicion.",
                "For candidates, consider combined exposure with other sources.",
                "Do not accept a status because two reviewers agreed.",
                "",
                "**Owner finding:** PENDING",
                "",
                "**Owner evidence basis, unresolved questions and next action:** PENDING",
                "",
            ])
    raw = ("\n".join(lines).rstrip() + "\n").encode("utf-8")
    if not 500 <= len(raw) <= MAX_REVIEW_BYTES:
        raise decision.Hold("OWNER_REVIEW_SIZE_INVALID")
    return raw


def create_review(
    *, packet: Path, ciphertext: Path, cert: Path, key: Path,
    output: Path, expected_sha256: str, password: bytes,
    openssl: str | None = None,
) -> dict:
    """Authenticate before rendering, write once inside the protected folder."""
    if (
        output.name != NAME or output.is_symlink() or output.exists()
        or not output.parent.is_dir()
        or output.parent.resolve() != packet.parent.resolve()
        or output.parent.resolve() != ciphertext.parent.resolve()
        or ciphertext.is_symlink() or packet.is_symlink()
        or not ciphertext.is_file() or not packet.is_file()
        or not re.fullmatch(r"[0-9a-f]{64}", expected_sha256)
    ):
        raise decision.Hold("OWNER_REVIEW_FILE_SCOPE_INVALID")
    cipher = ciphertext.read_bytes()
    pack = packet.read_bytes()
    if sha256(cipher).hexdigest() != expected_sha256:
        raise decision.Hold("OWNER_REVIEW_CIPHERTEXT_IDENTITY_INVALID")
    # The existing owner-only crypto/schema verifier authenticates the CMS
    # and exact source, first-pass, challenge and decision bindings.
    summary = decision.owner_verify(
        cipher, pack, cert, key, password, openssl=openssl
    )
    if summary["owner_adjudication_cms_authenticated"] != "PASS":
        raise decision.Hold("OWNER_REVIEW_AUTHENTICATION_FAILED")
    binary = decision.binary_path(openssl)
    with TemporaryDirectory() as tmp:
        encrypted = Path(tmp) / "owner-review.cms"
        encrypted.write_bytes(cipher)
        p = subprocess.run([
            binary, "cms", "-decrypt", "-binary", "-inform", "DER",
            "-in", str(encrypted), "-recip", str(cert), "-inkey", str(key),
            "-passin", "stdin",
        ], input=password + b"\n", capture_output=True,
            timeout=40, check=False)
    if p.returncode:
        raise decision.Hold("OWNER_REVIEW_AUTHENTICATED_READ_FAILED")
    obj = decision.parse(p.stdout)
    if decision.canonical(obj) != p.stdout:
        raise decision.Hold("OWNER_REVIEW_REPORT_NONCANONICAL")
    body = render(pack, obj)
    with output.open("xb") as target:
        target.write(body)
    return {
        "private_review_created": "PASS",
        "source_bound_decision_records": 10,
        "output_bytes": len(body),
        "output_sha256": sha256(body).hexdigest(),
        "source_specific_findings_printed": False,
        "owner_scientific_acceptance": "PENDING",
        "author_release": "NONE",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Owner-only authenticated restricted Wave0 decision review"
    )
    for name in (
        "packet", "ciphertext", "public-cert", "private-key",
        "expected-sha256", "output",
    ):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--openssl")
    args = parser.parse_args()
    if not sys.stdin.isatty():
        raise decision.Hold("OWNER_REVIEW_INTERACTIVE_REQUIRED")
    password = __import__("getpass").getpass(
        "Existing owner encrypted-key passphrase: "
    ).encode("utf-8")
    result = create_review(
        packet=Path(args.packet), ciphertext=Path(args.ciphertext),
        cert=Path(args.public_cert), key=Path(args.private_key),
        output=Path(args.output), expected_sha256=args.expected_sha256,
        password=password, openssl=args.openssl,
    )
    print(json.dumps(result, sort_keys=True))
    print("S1_WAVE0_OWNER_PRIVATE_DECISION_REVIEW=PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (decision.Hold, OSError, ValueError, TypeError, EOFError,
            subprocess.SubprocessError, TimeoutError):
        print("S1_WAVE0_OWNER_PRIVATE_DECISION_REVIEW_HOLD", file=sys.stderr)
        sys.exit(2)
