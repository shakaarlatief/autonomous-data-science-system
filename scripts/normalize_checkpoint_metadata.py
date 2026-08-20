#!/usr/bin/env python3
"""Normalize checkpoint headers to the repository metadata contract.

This utility exists to repair metadata drift in historical checkpoint records
without rewriting their substantive content. It replaces only the metadata
block immediately below the checkpoint H1 title. The historical body is left
unchanged.

The default migration target is Checkpoints 000-099, which were all created in
the first ChatGPT design session. Their ChatGPT project/session provenance is
now known and is preserved explicitly. The script also accepts post-contract
checkpoints when requested, but it does not invent session provenance for them.

The normalizer is deliberately conservative:

* existing supported metadata is preserved where possible;
* legacy aliases such as ``Stage`` and ``Development stage`` are promoted into
  the mandatory ``Project stage`` field;
* absent core metadata is filled using coarse historical classifications;
* a missing historical date is recovered from Git creation history rather than
  guessed from the current date;
* the checkpoint title and substantive body are never reinterpreted;
* historical records are not granted stronger present-day authority.
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

CORE_KEYS = (
    "Date",
    "Status",
    "Checkpoint class",
    "Project stage",
    "Scope",
    "Authority",
)

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
    "chatgpt project": "ChatGPT project",
    "session title": "Session title",
    "chatgpt chat": "Session title",
    "design session": "Design session",
}

# Checkpoints 000-099 were created in the first ChatGPT project session. This
# provenance is now explicitly confirmed and should be preserved consistently.
LEGACY_CHATGPT_PROJECT = "Autonomous Data Science System"
LEGACY_SESSION_TITLE = "01 - Foundations & Checkpoint 0"
LEGACY_DESIGN_SESSION = "01"


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


def git_creation_date(path: Path) -> str:
    """Return the file's first Git commit date as YYYY-MM-DD.

    Historical checkpoints should never receive today's date merely because
    their metadata are being normalized later. A full-history checkout allows
    the migration to recover the creation date when legacy header metadata is
    missing or malformed.
    """

    command = [
        "git",
        "log",
        "--follow",
        "--diff-filter=A",
        "--format=%cs",
        "--",
        path.as_posix(),
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    dates = [line.strip() for line in result.stdout.splitlines() if DATE_RE.match(line.strip())]
    if dates:
        return dates[-1]
    raise ValueError(f"{path}: historical date unavailable in header and Git creation history")


def extract_historical_date(
    path: Path,
    lines: list[str],
    metadata: list[tuple[str, str]],
) -> str:
    """Recover a trustworthy historical date from metadata, header text, or Git."""

    for key, value in metadata:
        if CORE_ALIASES.get(key.casefold()) == "Date" and DATE_RE.match(value):
            return value

    # A few legacy files may have a date line separated from the compact
    # metadata block. Search only the opening section so body examples cannot be
    # mistaken for checkpoint metadata.
    for line in lines[1:40]:
        parsed = parse_metadata_line(line)
        if parsed is None:
            continue
        key, value = parsed
        if CORE_ALIASES.get(key.casefold()) == "Date" and DATE_RE.match(value):
            return value

    return git_creation_date(path)


def parse_checkpoint(path: Path) -> ParsedCheckpoint:
    """Parse title and contiguous legacy metadata for one checkpoint."""

    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    if not lines:
        raise ValueError(f"{path}: empty checkpoint")

    first_line = lines[0].rstrip("\r\n")
    title_match = TITLE_RE.match(first_line)
    file_match = CHECKPOINT_FILE_RE.match(path.name)
    if file_match is None:
        raise ValueError(f"{path}: filename does not match checkpoint convention")

    file_number = int(file_match.group("number"))
    if title_match is None:
        # Preserve the historical H1 exactly, but use the filename number for
        # migration classification. This avoids blocking the entire repair on a
        # cosmetic legacy title variation.
        number = file_number
        title_text = first_line.removeprefix("#").strip() or f"Checkpoint {number}"
    else:
        number = int(title_match.group("number"))
        if number != file_number:
            raise ValueError(
                f"{path}: checkpoint number mismatch between filename ({file_number}) "
                f"and H1 ({number})"
            )
        title_text = (title_match.group("title") or f"Checkpoint {number}").strip()

    metadata: list[tuple[str, str]] = []
    index = 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    while index < len(lines):
        if not lines[index].strip():
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

    date = extract_historical_date(path, lines, metadata)

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
    """Classify a checkpoint conservatively from title and historical phase."""

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
    """Map checkpoint class to a conservative historical lifecycle status."""

    return {
        "DESIGN": "Historical design checkpoint",
        "EXPERIMENT_EXECUTION": "Historical experiment record",
        "EXPERIMENT_VERIFICATION": "Historical verification record",
        "INFRASTRUCTURE": "Historical infrastructure record",
        "PRESERVATION_METHOD": "Historical preservation-method record",
        "CONTINUITY": "Historical continuity boundary",
        "MIXED": "Historical mixed checkpoint",
    }[checkpoint_class]


def canonical_value(parsed: ParsedCheckpoint, canonical_key: str) -> str | None:
    """Return an existing canonical value, accepting known legacy aliases."""

    aliases = CORE_ALIASES | SESSION_ALIASES
    for key, value in parsed.metadata:
        if aliases.get(key.casefold()) == canonical_key and value:
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
    return (
        "Historical provenance; current canonical documents and promoted sources govern "
        "current interpretation."
    )


def preserved_extensions(parsed: ParsedCheckpoint) -> list[tuple[str, str]]:
    """Preserve non-core/session legacy metadata in original order without duplication."""

    recognized = CORE_ALIASES | SESSION_ALIASES
    result: list[tuple[str, str]] = []
    seen: set[str] = set()
    for key, value in parsed.metadata:
        folded = key.casefold()
        if folded in recognized:
            continue
        if folded in seen:
            continue
        seen.add(folded)
        result.append((key, value))
    return result


def normalized_text(parsed: ParsedCheckpoint) -> str:
    """Return checkpoint text with only the metadata block normalized."""

    checkpoint_class = canonical_value(parsed, "Checkpoint class") or infer_checkpoint_class(
        parsed.number, parsed.title_text
    )
    status = canonical_value(parsed, "Status") or infer_status(checkpoint_class)
    project_stage = canonical_value(parsed, "Project stage") or infer_project_stage(parsed.number)
    scope = canonical_value(parsed, "Scope") or infer_scope(parsed)
    authority = canonical_value(parsed, "Authority") or authority_text(checkpoint_class)

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

    # All pre-100 checkpoints belong to the first ChatGPT project session. Keep
    # this as provenance metadata, not as methodological authority.
    if parsed.number < 100:
        session_fields = [
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
        header_lines.extend(f"**{key}:** {value}  " for key, value in session_fields)

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
        help="Write normalized metadata headers in place. Without this flag only report changes.",
    )
    parser.add_argument(
        "--include-post-contract",
        action="store_true",
        help="Also normalize checkpoints 100 and above. The legacy migration normally targets 000-099.",
    )
    args = parser.parse_args()

    changed: list[Path] = []
    failures: list[tuple[Path, str]] = []

    for path in checkpoint_paths(args.include_post_contract):
        try:
            parsed = parse_checkpoint(path)
            new_text = normalized_text(parsed)
            old_text = "".join(parsed.lines)
            if new_text == old_text:
                continue
            changed.append(path)
            if args.write:
                path.write_text(new_text, encoding="utf-8")
        except Exception as exc:  # migration must report every problematic file
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
