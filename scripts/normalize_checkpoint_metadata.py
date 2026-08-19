#!/usr/bin/env python3
"""Normalize checkpoint headers to the repository metadata contract.

This migration utility is intentionally conservative. It modifies only the
metadata block immediately below a checkpoint H1 title. The historical body is
left byte-for-byte unchanged apart from the blank-line boundary needed to
replace that header block.

The normalizer is designed for the legacy checkpoints that predate the
mandatory metadata contract in ``docs/checkpoints/README.md``. It preserves
existing supported metadata where possible, promotes legacy aliases such as
``Stage`` and ``Development stage`` into ``Project stage``, and fills missing
core fields using deliberately coarse historical classifications.

The script does not reinterpret historical conclusions, infer unavailable chat
session metadata, or grant stronger authority to old checkpoints.
"""

from __future__ import annotations

import argparse
import re
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

CORE_KEYS = (
    "Date",
    "Status",
    "Checkpoint class",
    "Project stage",
    "Scope",
    "Authority",
)

# Legacy field names that are semantically absorbed into the mandatory core.
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


@dataclass(frozen=True)
class ParsedCheckpoint:
    path: Path
    number: int
    title_line: str
    title_text: str
    date: str
    metadata: list[tuple[str, str]]
    body_start: int
    lines: list[str]


def parse_metadata_line(line: str) -> tuple[str, str] | None:
    """Return ``(key, value)`` for one metadata line, otherwise ``None``."""

    stripped = line.rstrip("\r\n")
    match = BOLD_META_RE.match(stripped)
    if match:
        return match.group("key").strip(), match.group("value").strip()

    match = PLAIN_META_RE.match(stripped)
    if match:
        return match.group("key").strip(), match.group("value").strip()

    return None


def parse_checkpoint(path: Path) -> ParsedCheckpoint:
    """Parse the title and contiguous legacy metadata block for one checkpoint."""

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines:
        raise ValueError(f"{path}: empty checkpoint")

    title_match = TITLE_RE.match(lines[0].rstrip("\r\n"))
    if not title_match:
        raise ValueError(f"{path}: first line is not a recognized checkpoint H1 title")

    number = int(title_match.group("number"))
    title_text = (title_match.group("title") or f"Checkpoint {number}").strip()

    metadata: list[tuple[str, str]] = []
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    while index < len(lines):
        if not lines[index].strip():
            # Blank lines inside the old header are tolerated only if the next
            # nonblank line is still metadata.
            probe = index + 1
            while probe < len(lines) and not lines[probe].strip():
                probe += 1
            if probe < len(lines) and parse_metadata_line(lines[probe]) is not None:
                index = probe
                continue
            break

        parsed = parse_metadata_line(lines[index])
        if parsed is None:
            break
        metadata.append(parsed)
        index += 1

    while index < len(lines) and not lines[index].strip():
        index += 1

    metadata_by_alias: dict[str, str] = {}
    for key, value in metadata:
        canonical = CORE_ALIASES.get(key.casefold())
        if canonical and canonical not in metadata_by_alias:
            metadata_by_alias[canonical] = value

    date = metadata_by_alias.get("Date", "")
    if not DATE_RE.match(date):
        raise ValueError(f"{path}: missing or invalid historical date {date!r}")

    return ParsedCheckpoint(
        path=path,
        number=number,
        title_line=lines[0],
        title_text=title_text,
        date=date,
        metadata=metadata,
        body_start=index,
        lines=lines,
    )


def infer_project_stage(number: int) -> str:
    """Return a coarse historical stage for checkpoints lacking one explicitly."""

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
    """Classify a checkpoint using conservative title and phase signals."""

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
    """Map checkpoint class to a historical lifecycle status."""

    return {
        "DESIGN": "Historical design checkpoint",
        "EXPERIMENT_EXECUTION": "Historical experiment record",
        "EXPERIMENT_VERIFICATION": "Historical verification record",
        "INFRASTRUCTURE": "Historical infrastructure record",
        "PRESERVATION_METHOD": "Historical preservation-method record",
        "CONTINUITY": "Historical continuity boundary",
        "MIXED": "Historical mixed checkpoint",
    }[checkpoint_class]


def core_value(parsed: ParsedCheckpoint, canonical_key: str) -> str | None:
    """Return an existing core value, accepting legacy aliases."""

    for key, value in parsed.metadata:
        if CORE_ALIASES.get(key.casefold()) == canonical_key and value:
            return value
    return None


def infer_scope(parsed: ParsedCheckpoint) -> str:
    """Create a deliberately non-interpretive scope when none was recorded."""

    title = parsed.title_text.rstrip(".")
    return f"Records the historical milestone described by this checkpoint: {title}."


def authority_text(checkpoint_class: str) -> str:
    """Return the default authority statement for a legacy checkpoint."""

    if checkpoint_class in {"EXPERIMENT_EXECUTION", "EXPERIMENT_VERIFICATION"}:
        return (
            "Historical provenance for the recorded experiment milestone; frozen experiment "
            "contracts and final experiment conclusions govern their declared scopes."
        )
    return "Historical provenance; current canonical documents and promoted sources govern current interpretation."


def preserved_extensions(parsed: ParsedCheckpoint) -> list[tuple[str, str]]:
    """Preserve non-core legacy metadata in original order without duplication."""

    result: list[tuple[str, str]] = []
    seen: set[str] = set()
    for key, value in parsed.metadata:
        folded = key.casefold()
        if folded in CORE_ALIASES:
            continue
        if folded in seen:
            continue
        seen.add(folded)
        result.append((key, value))
    return result


def normalized_text(parsed: ParsedCheckpoint) -> str:
    """Return checkpoint text with only the metadata block normalized."""

    checkpoint_class = core_value(parsed, "Checkpoint class") or infer_checkpoint_class(
        parsed.number, parsed.title_text
    )
    status = core_value(parsed, "Status") or infer_status(checkpoint_class)
    project_stage = core_value(parsed, "Project stage") or infer_project_stage(parsed.number)
    scope = core_value(parsed, "Scope") or infer_scope(parsed)
    authority = core_value(parsed, "Authority") or authority_text(checkpoint_class)

    core = [
        ("Date", parsed.date),
        ("Status", status),
        ("Checkpoint class", checkpoint_class),
        ("Project stage", project_stage),
        ("Scope", scope),
        ("Authority", authority),
    ]

    header_lines = [parsed.title_line.rstrip("\r\n"), ""]
    header_lines.extend(f"**{key}:** {value}  " for key, value in core)

    extensions = preserved_extensions(parsed)
    if extensions:
        header_lines.extend(f"**{key}:** {value}  " for key, value in extensions)

    header = "\n".join(header_lines).rstrip() + "\n\n"
    body = "".join(parsed.lines[parsed.body_start :])
    return header + body


def checkpoint_paths(include_post_contract: bool) -> list[Path]:
    """Return checkpoint files in numeric order, excluding the contract README."""

    paths: list[tuple[int, Path]] = []
    for path in CHECKPOINT_DIR.glob("*.md"):
        match = CHECKPOINT_FILE_RE.match(path.name)
        if not match:
            continue
        number = int(match.group("number"))
        if not include_post_contract and number >= 100:
            continue
        paths.append((number, path))
    return [path for _, path in sorted(paths)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write normalized metadata headers in place. Without this flag the script only reports changes.",
    )
    parser.add_argument(
        "--include-post-contract",
        action="store_true",
        help="Also normalize checkpoints 100 and above. The historical migration normally targets 000-099 only.",
    )
    args = parser.parse_args()

    changed: list[Path] = []
    for path in checkpoint_paths(args.include_post_contract):
        parsed = parse_checkpoint(path)
        new_text = normalized_text(parsed)
        old_text = "".join(parsed.lines)
        if new_text == old_text:
            continue
        changed.append(path)
        if args.write:
            path.write_text(new_text, encoding="utf-8")

    mode = "normalized" if args.write else "would normalize"
    print(f"{mode}: {len(changed)} checkpoint(s)")
    for path in changed:
        print(path.as_posix())

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
