#!/usr/bin/env python3
"""Normalize checkpoint headers to the repository metadata contract.

This migration utility repairs checkpoint metadata without rewriting historical
substance. Only the metadata block immediately below the H1 title is replaced;
the remaining checkpoint body is preserved.

By default the utility targets legacy Checkpoints 000-099. Pass
``--include-post-contract`` to normalize all numbered checkpoints. Legacy
checkpoints have confirmed Session 01 provenance. Later checkpoints preserve
whatever session provenance is already recorded rather than receiving inferred
session metadata.
"""

from __future__ import annotations

import argparse
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


CHECKPOINT_DIR = Path("docs/checkpoints")
CHECKPOINT_FILE_RE = re.compile(r"^(?P<number>\d{3})_.*\.md$")
TITLE_RE = re.compile(
    r"^#\s+Checkpoint\s+(?P<number>\d+)(?:\s*[:\-–—]\s*(?P<title>.+?))?\s*$",
    re.IGNORECASE,
)
BOLD_META_RE = re.compile(r"^\*\*(?P<key>[^*:\n]+):\*\*\s*(?P<value>.*?)\s*$")
PLAIN_META_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9 /_-]*):\s*(?P<value>.*?)\s*$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

CORE_ALIASES = {
    "date": "Date",
    "status": "Status",
    "checkpoint class": "Checkpoint class",
    "project stage": "Project stage",
    "development stage": "Project stage",
    "stage": "Project stage",
    "scope": "Scope",
    "authority": "Authority",
}
SESSION_ALIASES = {
    "design session": "Design session",
    "chatgpt project": "ChatGPT project",
    "session title": "Session title",
    "chatgpt chat": "Session title",
}
RECOGNIZED_ALIASES = CORE_ALIASES | SESSION_ALIASES

LEGACY_DESIGN_SESSION = "01"
LEGACY_CHATGPT_PROJECT = "Autonomous Data Science System"
LEGACY_SESSION_TITLE = "01 - Foundations & Checkpoint 0"


@dataclass(frozen=True)
class ParsedCheckpoint:
    path: Path
    number: int
    title_line: str
    title_text: str
    metadata: tuple[tuple[str, str], ...]
    body_start: int
    lines: tuple[str, ...]
    date: str


def parse_metadata_line(line: str) -> tuple[str, str] | None:
    """Parse one bold or plain legacy metadata line."""

    stripped = line.rstrip("\r\n")
    for pattern in (BOLD_META_RE, PLAIN_META_RE):
        match = pattern.match(stripped)
        if match:
            return match.group("key").strip(), match.group("value").strip()
    return None


def git_creation_date(path: Path) -> str:
    """Recover a checkpoint's first Git commit date as ``YYYY-MM-DD``."""

    result = subprocess.run(
        [
            "git",
            "log",
            "--follow",
            "--diff-filter=A",
            "--format=%cs",
            "--",
            path.as_posix(),
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    dates = [line.strip() for line in result.stdout.splitlines() if DATE_RE.match(line.strip())]
    if dates:
        return dates[-1]
    raise ValueError(f"{path}: no trustworthy historical date found")


def recover_date(
    path: Path,
    lines: tuple[str, ...],
    metadata: tuple[tuple[str, str], ...],
) -> str:
    """Recover the historical date from metadata, opening lines, or Git."""

    for key, value in metadata:
        if CORE_ALIASES.get(key.casefold()) == "Date" and DATE_RE.match(value):
            return value

    for line in lines[1:40]:
        parsed = parse_metadata_line(line)
        if parsed is None:
            continue
        key, value = parsed
        if CORE_ALIASES.get(key.casefold()) == "Date" and DATE_RE.match(value):
            return value

    return git_creation_date(path)


def parse_checkpoint(path: Path) -> ParsedCheckpoint:
    """Parse one checkpoint's title and contiguous opening metadata block."""

    lines = tuple(path.read_text(encoding="utf-8").splitlines(keepends=True))
    if not lines:
        raise ValueError(f"{path}: empty checkpoint")

    file_match = CHECKPOINT_FILE_RE.match(path.name)
    if file_match is None:
        raise ValueError(f"{path}: invalid checkpoint filename")
    file_number = int(file_match.group("number"))

    first_line = lines[0].rstrip("\r\n")
    title_match = TITLE_RE.match(first_line)
    if title_match is None:
        number = file_number
        title_text = first_line.removeprefix("#").strip() or f"Checkpoint {number}"
    else:
        number = int(title_match.group("number"))
        if number != file_number:
            raise ValueError(
                f"{path}: filename checkpoint number {file_number} != H1 number {number}"
            )
        title_text = (title_match.group("title") or f"Checkpoint {number}").strip()

    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    metadata: list[tuple[str, str]] = []
    while index < len(lines):
        parsed = parse_metadata_line(lines[index])
        if parsed is not None:
            metadata.append(parsed)
            index += 1
            continue

        if not lines[index].strip():
            probe = index + 1
            while probe < len(lines) and not lines[probe].strip():
                probe += 1
            if probe < len(lines) and parse_metadata_line(lines[probe]) is not None:
                index = probe
                continue
        break

    while index < len(lines) and not lines[index].strip():
        index += 1

    frozen_metadata = tuple(metadata)
    return ParsedCheckpoint(
        path=path,
        number=number,
        title_line=lines[0],
        title_text=title_text,
        metadata=frozen_metadata,
        body_start=index,
        lines=lines,
        date=recover_date(path, lines, frozen_metadata),
    )


def canonical_value(parsed: ParsedCheckpoint, canonical_key: str) -> str | None:
    """Return an existing value using known legacy aliases."""

    for key, value in parsed.metadata:
        if RECOGNIZED_ALIASES.get(key.casefold()) == canonical_key and value:
            return value
    return None


def infer_project_stage(number: int) -> str:
    """Return a deliberately coarse historical stage when none was recorded."""

    if number == 0:
        return "Initial conceptual design"
    if 1 <= number <= 9:
        return "Conceptual research and system definition"
    if 10 <= number <= 17:
        return "Prototype V0 specification and real-model calibration"
    if 18 <= number <= 27:
        return "Prototype V0 development calibration"
    if 28 <= number <= 34:
        return "Prototype V0 held-out protocol and implementation preparation"
    if 35 <= number <= 45:
        return "Prototype V0 development correction and behavioral freeze"
    if 46 <= number <= 52:
        return "Prototype V0 held-out execution preparation"
    if 53 <= number <= 95:
        return "Prototype V0 held-out execution and evaluation"
    if number == 96:
        return "Prototype V0 final evaluation and closure"
    if 97 <= number <= 99:
        return "Post-V0 product and architecture design"
    return "Post-V0 methodological-navigation and reusable-knowledge design"


def infer_checkpoint_class(number: int, title: str) -> str:
    """Classify a checkpoint conservatively from its historical title/phase."""

    text = title.casefold()

    if number in {74, 75, 76} or any(
        token in text
        for token in (
            "knowledge preservation",
            "readme refreshed",
            "promoted to foundation",
            "promotion",
        )
    ):
        return "PRESERVATION_METHOD"
    if number == 99 or "continuity" in text or "session rotation" in text:
        return "CONTINUITY"
    if any(
        token in text
        for token in (
            "terminal record",
            "behavior-evaluable",
            "behavior evaluable",
            "calibration run",
            "real p0 run",
            "held-out attempt",
            "held out attempt",
            "provider failure",
            "budget exhaustion",
            "judge execution complete",
        )
    ):
        return "EXPERIMENT_EXECUTION"
    if any(
        token in text
        for token in (
            "verification",
            "validated",
            "validation complete",
            "preflight",
            "freeze",
            "verified",
            "comparison",
            "semantic results",
            "analysis",
            "protocol",
        )
    ):
        return "EXPERIMENT_VERIFICATION"
    if any(
        token in text
        for token in (
            "implemented",
            "infrastructure",
            "runner",
            "executor",
            "supervisor",
            "monitor",
            "decoder",
            "normalization",
            "implementation candidate",
            "technical specification",
            "workspace",
        )
    ):
        return "INFRASTRUCTURE"
    if number <= 10 or number in {22, 96, 97, 98}:
        return "DESIGN"
    return "MIXED"


def infer_status(checkpoint_class: str) -> str:
    """Map a checkpoint class to a conservative historical status."""

    return {
        "DESIGN": "Historical design checkpoint",
        "EXPERIMENT_EXECUTION": "Historical experiment record",
        "EXPERIMENT_VERIFICATION": "Historical verification record",
        "INFRASTRUCTURE": "Historical infrastructure record",
        "PRESERVATION_METHOD": "Historical preservation-method record",
        "CONTINUITY": "Historical continuity boundary",
        "MIXED": "Historical mixed checkpoint",
    }[checkpoint_class]


def infer_scope(parsed: ParsedCheckpoint) -> str:
    """Return a non-interpretive scope when no historical scope was recorded."""

    return (
        "Records the historical milestone described by this checkpoint: "
        f"{parsed.title_text.rstrip('.')}."
    )


def infer_authority(checkpoint_class: str) -> str:
    """Return conservative authority text for historical records."""

    if checkpoint_class in {"EXPERIMENT_EXECUTION", "EXPERIMENT_VERIFICATION"}:
        return (
            "Historical provenance for the recorded experiment milestone; frozen experiment "
            "contracts and final experiment conclusions govern their declared scopes."
        )
    return (
        "Historical provenance; current canonical documents and promoted sources govern "
        "current interpretation."
    )


def preserved_extensions(parsed: ParsedCheckpoint) -> list[tuple[str, str]]:
    """Preserve non-core/non-session metadata in original order."""

    result: list[tuple[str, str]] = []
    seen: set[str] = set()
    for key, value in parsed.metadata:
        folded = key.casefold()
        if folded in RECOGNIZED_ALIASES or folded in seen:
            continue
        seen.add(folded)
        result.append((key, value))
    return result


def session_fields(parsed: ParsedCheckpoint) -> list[tuple[str, str]]:
    """Return confirmed legacy defaults or explicit post-contract provenance."""

    if parsed.number < 100:
        return [
            ("Design session", canonical_value(parsed, "Design session") or LEGACY_DESIGN_SESSION),
            (
                "ChatGPT project",
                canonical_value(parsed, "ChatGPT project") or LEGACY_CHATGPT_PROJECT,
            ),
            (
                "Session title",
                canonical_value(parsed, "Session title") or LEGACY_SESSION_TITLE,
            ),
        ]

    result: list[tuple[str, str]] = []
    for key in ("Design session", "ChatGPT project", "Session title"):
        value = canonical_value(parsed, key)
        if value:
            result.append((key, value))
    return result


def normalized_text(parsed: ParsedCheckpoint) -> str:
    """Return checkpoint text with a normalized metadata header only."""

    checkpoint_class = canonical_value(parsed, "Checkpoint class") or infer_checkpoint_class(
        parsed.number, parsed.title_text
    )
    core = [
        ("Date", parsed.date),
        ("Status", canonical_value(parsed, "Status") or infer_status(checkpoint_class)),
        ("Checkpoint class", checkpoint_class),
        (
            "Project stage",
            canonical_value(parsed, "Project stage") or infer_project_stage(parsed.number),
        ),
        ("Scope", canonical_value(parsed, "Scope") or infer_scope(parsed)),
        ("Authority", canonical_value(parsed, "Authority") or infer_authority(checkpoint_class)),
    ]

    header_lines = [parsed.title_line.rstrip("\r\n"), ""]
    header_lines.extend(f"**{key}:** {value}  " for key, value in core)
    header_lines.extend(f"**{key}:** {value}  " for key, value in session_fields(parsed))
    header_lines.extend(
        f"**{key}:** {value}  " for key, value in preserved_extensions(parsed)
    )

    header = "\n".join(header_lines).rstrip() + "\n\n"
    body = "".join(parsed.lines[parsed.body_start :])
    return header + body


def checkpoint_paths(include_post_contract: bool) -> list[Path]:
    """Return numbered checkpoint files in numeric order."""

    items: list[tuple[int, Path]] = []
    for path in CHECKPOINT_DIR.glob("*.md"):
        match = CHECKPOINT_FILE_RE.match(path.name)
        if match is None:
            continue
        number = int(match.group("number"))
        if not include_post_contract and number >= 100:
            continue
        items.append((number, path))
    return [path for _, path in sorted(items)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write normalized headers. Without this flag only report affected files.",
    )
    parser.add_argument(
        "--include-post-contract",
        action="store_true",
        help="Normalize Checkpoints 100+ as well as legacy Checkpoints 000-099.",
    )
    args = parser.parse_args()

    changed: list[Path] = []
    failures: list[tuple[Path, str]] = []

    for path in checkpoint_paths(args.include_post_contract):
        try:
            parsed = parse_checkpoint(path)
            old_text = "".join(parsed.lines)
            new_text = normalized_text(parsed)
            if new_text == old_text:
                continue
            changed.append(path)
            if args.write:
                path.write_text(new_text, encoding="utf-8")
        except Exception as exc:
            failures.append((path, str(exc)))

    mode = "normalized" if args.write else "would normalize"
    print(f"{mode}: {len(changed)} checkpoint(s)")
    for path in changed:
        print(path.as_posix())

    if failures:
        print(f"failed: {len(failures)} checkpoint(s)")
        for path, error in failures:
            print(f"ERROR {path.as_posix()}: {error}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
