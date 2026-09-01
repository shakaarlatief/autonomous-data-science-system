from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FIELD_RE = re.compile(r"^\*\*(?P<name>[^*]+):\*\*\s*(?P<value>.*?)(?:\s{2})?$")
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
HEADER_SCAN_LINES = 100
PUBLIC_CHECKPOINT_FIELD = "Public continuity checkpoint"
PUBLIC_COMMIT_FIELD = "Public continuity commit"


def read_header_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[:HEADER_SCAN_LINES]:
        if line.startswith("## "):
            break
        match = FIELD_RE.match(line.strip())
        if match:
            fields[match.group("name").strip()] = match.group("value").strip()
    return fields


def evaluate_private_continuity(
    private_state_path: Path | None,
    expected_checkpoint: int,
    expected_commit: str,
) -> tuple[str, list[str]]:
    if expected_checkpoint <= 0:
        raise ValueError("expected public checkpoint must be a positive integer")
    if not SHA_RE.fullmatch(expected_commit):
        raise ValueError("expected public commit must be a lowercase 40-character SHA")

    if private_state_path is None or not private_state_path.is_file():
        return "NOT_VERIFIED", []

    fields = read_header_fields(private_state_path)
    errors: list[str] = []

    checkpoint_raw = fields.get(PUBLIC_CHECKPOINT_FIELD, "").strip()
    commit_raw = fields.get(PUBLIC_COMMIT_FIELD, "").strip()

    if not checkpoint_raw.isdigit() or int(checkpoint_raw) <= 0:
        errors.append(
            f"{PUBLIC_CHECKPOINT_FIELD} must be a positive integer"
        )
    elif int(checkpoint_raw) != expected_checkpoint:
        errors.append(
            f"{PUBLIC_CHECKPOINT_FIELD} mismatch: "
            f"private={int(checkpoint_raw)}, expected={expected_checkpoint}"
        )

    if not SHA_RE.fullmatch(commit_raw):
        errors.append(
            f"{PUBLIC_COMMIT_FIELD} must be a lowercase 40-character SHA"
        )
    elif commit_raw != expected_commit:
        errors.append(
            f"{PUBLIC_COMMIT_FIELD} mismatch: "
            f"private={commit_raw}, expected={expected_commit}"
        )

    return ("FAIL", errors) if errors else ("PASS", [])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate the minimal private-companion public continuity anchor without "
            "fabricating private verification when the companion is inaccessible."
        )
    )
    parser.add_argument(
        "--private-state",
        type=Path,
        help="Accessible CURRENT_PRIVATE_STATE.md path. Omit when private state is inaccessible.",
    )
    parser.add_argument("--expected-checkpoint", required=True, type=int)
    parser.add_argument("--expected-commit", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        status, errors = evaluate_private_continuity(
            args.private_state,
            args.expected_checkpoint,
            args.expected_commit,
        )
    except ValueError as exc:
        print(f"Private continuity checker configuration error: {exc}", file=sys.stderr)
        return 2

    for error in errors:
        print(f"  ERROR {error}")
    print(f"PRIVATE_CONTINUITY_INTEGRITY={status}")
    return 1 if status == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
