from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


CHECKPOINT_NAME_RE = re.compile(r"^(?P<number>\d{3})_.*\.md$")
FIELD_RE = re.compile(r"^\*\*(?P<name>[^*]+):\*\*\s*(?P<value>.*?)(?:\s{2})?$")

HISTORICAL_AUTHORITY_FIELDS = (
    "Date",
    "Status",
    "Checkpoint class",
    "Project stage",
    "Scope",
    "Authority",
)

CHATGPT_PROVENANCE_FIELDS = (
    "Design session",
    "ChatGPT project",
    "Session title",
)

PROVIDER_NEUTRAL_PROVENANCE_FIELDS = (
    "Interaction environment",
    "Project / workspace",
    "Interaction session",
    "Conversation title",
    "Primary collaborator",
)

CONTRACT_START_CHECKPOINT = 100
PROVIDER_NEUTRAL_START_CHECKPOINT = 204
HEADER_SCAN_LINES = 60


@dataclass(frozen=True)
class Finding:
    path: Path
    checkpoint_number: int
    required_fields: tuple[str, ...]
    missing_fields: tuple[str, ...]
    empty_fields: tuple[str, ...]

    @property
    def compliant(self) -> bool:
        return not self.missing_fields and not self.empty_fields


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate checkpoint metadata against docs/checkpoints/README.md. "
            "The historical/authority core is stable. Checkpoints before 204 use "
            "the historical ChatGPT session-provenance contract; Checkpoint 204+ "
            "uses provider-neutral interaction provenance. By default, pre-100 "
            "deficiencies are reported as legacy warnings while Checkpoint 100+ "
            "deficiencies fail validation."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Treat metadata deficiencies in legacy checkpoints 000-099 as errors too.",
    )
    return parser.parse_args()


def required_fields_for_checkpoint(checkpoint_number: int) -> tuple[str, ...]:
    provenance_fields = (
        PROVIDER_NEUTRAL_PROVENANCE_FIELDS
        if checkpoint_number >= PROVIDER_NEUTRAL_START_CHECKPOINT
        else CHATGPT_PROVENANCE_FIELDS
    )
    return HISTORICAL_AUTHORITY_FIELDS + provenance_fields


def read_header_fields(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()[:HEADER_SCAN_LINES]
    fields: dict[str, str] = {}
    for line in lines:
        match = FIELD_RE.match(line.strip())
        if match:
            fields[match.group("name").strip()] = match.group("value").strip()
    return fields


def inspect_checkpoint(path: Path, checkpoint_number: int) -> Finding:
    fields = read_header_fields(path)
    required_fields = required_fields_for_checkpoint(checkpoint_number)
    missing = tuple(field for field in required_fields if field not in fields)
    empty = tuple(
        field for field in required_fields if field in fields and not fields[field]
    )
    return Finding(
        path=path,
        checkpoint_number=checkpoint_number,
        required_fields=required_fields,
        missing_fields=missing,
        empty_fields=empty,
    )


def iter_checkpoint_files(checkpoints_dir: Path) -> list[tuple[int, Path]]:
    checkpoints: list[tuple[int, Path]] = []
    for path in checkpoints_dir.iterdir():
        if not path.is_file():
            continue
        match = CHECKPOINT_NAME_RE.match(path.name)
        if not match:
            continue
        checkpoints.append((int(match.group("number")), path))
    return sorted(checkpoints)


def format_problem(finding: Finding) -> str:
    parts: list[str] = []
    if finding.missing_fields:
        parts.append("missing=" + ", ".join(finding.missing_fields))
    if finding.empty_fields:
        parts.append("empty=" + ", ".join(finding.empty_fields))
    return "; ".join(parts)


def main() -> int:
    args = parse_args()
    checkpoints_dir = args.root / "docs" / "checkpoints"
    if not checkpoints_dir.is_dir():
        print(f"Checkpoint directory not found: {checkpoints_dir}", file=sys.stderr)
        return 2

    checkpoints = iter_checkpoint_files(checkpoints_dir)
    if not checkpoints:
        print(f"No numbered checkpoint files found in {checkpoints_dir}", file=sys.stderr)
        return 2

    errors: list[Finding] = []
    legacy_warnings: list[Finding] = []

    for number, path in checkpoints:
        finding = inspect_checkpoint(path, number)
        if finding.compliant:
            continue

        if number < CONTRACT_START_CHECKPOINT and not args.all:
            legacy_warnings.append(finding)
        else:
            errors.append(finding)

    if legacy_warnings:
        print("Legacy checkpoint metadata still requiring normalization:")
        for finding in legacy_warnings:
            print(
                f"  WARN {finding.path.relative_to(args.root)}: "
                f"{format_problem(finding)}"
            )
        print()

    if errors:
        print("Checkpoint metadata contract violations:")
        for finding in errors:
            print(
                f"  ERROR {finding.path.relative_to(args.root)}: "
                f"{format_problem(finding)}"
            )
        print()

    compliant_count = len(checkpoints) - len(legacy_warnings) - len(errors)
    print(
        "Checkpoint metadata summary: "
        f"total={len(checkpoints)}, compliant={compliant_count}, "
        f"legacy_warnings={len(legacy_warnings)}, errors={len(errors)}, "
        f"provider_neutral_from={PROVIDER_NEUTRAL_START_CHECKPOINT}"
    )

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
