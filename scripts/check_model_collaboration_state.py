#!/usr/bin/env python3
"""Validate guarded ADS model-collaboration thread state.

The guard is intentionally a coherence check, not an authenticated lock. It
validates declared ownership and write-surface structure so accidental
coordination drift becomes visible in CI. It cannot establish which model
actually authored a Git mutation because current provider integrations share
the user's GitHub authority.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "model_collaboration_thread_state_v1.schema.json"
ACTIVE_STATES = {"OPEN", "ACTIVE", "WAITING"}
GLOB_CHARS = {"*", "?", "["}


def _load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _schema_validator() -> Draft202012Validator:
    schema = _load_json(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema)


def _json_path(error: Any) -> str:
    if not error.absolute_path:
        return "$"
    parts: list[str] = ["$"]
    for item in error.absolute_path:
        if isinstance(item, int):
            parts.append(f"[{item}]")
        else:
            parts.append(f".{item}")
    return "".join(parts)


def validate_repo_path(value: str) -> str | None:
    if not value:
        return "path must not be empty"
    if "\\" in value:
        return "path must use forward slashes"
    if value.startswith("/"):
        return "path must be repository-relative"
    if re.match(r"^[A-Za-z]:", value):
        return "path must not be an absolute drive path"
    segments = value.split("/")
    if any(segment == "" for segment in segments):
        return "path must not contain empty segments"
    if any(segment in {".", ".."} for segment in segments):
        return "path must not contain '.' or '..' segments"
    return None


def _fixed_prefix(path: str) -> tuple[str, ...]:
    prefix: list[str] = []
    for segment in path.split("/"):
        if any(char in segment for char in GLOB_CHARS):
            break
        prefix.append(segment)
    return tuple(prefix)


def _is_component_prefix(left: tuple[str, ...], right: tuple[str, ...]) -> bool:
    return len(left) <= len(right) and left == right[: len(left)]


def paths_may_overlap(left: str, right: str) -> bool:
    """Return True when two V1 path declarations conservatively may overlap.

    V1 deliberately uses a simple lexical guard, not a full glob-intersection
    solver. Exact matches and component-prefix relationships are rejected. A
    globbed declaration is represented by its literal prefix; if that prefix
    contains the other declaration's prefix, the pair is considered unsafe.
    """

    if left == right:
        return True

    left_has_glob = any(char in left for char in GLOB_CHARS)
    right_has_glob = any(char in right for char in GLOB_CHARS)
    left_prefix = _fixed_prefix(left)
    right_prefix = _fixed_prefix(right)

    if not left_has_glob and not right_has_glob:
        return _is_component_prefix(left_prefix, right_prefix) or _is_component_prefix(right_prefix, left_prefix)

    if left_has_glob and _is_component_prefix(left_prefix, right_prefix):
        return True
    if right_has_glob and _is_component_prefix(right_prefix, left_prefix):
        return True
    return False


def validate_state_file(path: Path, validator: Draft202012Validator | None = None) -> list[str]:
    errors: list[str] = []
    try:
        state = _load_json(path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{path}: cannot read valid JSON: {exc}"]

    schema_validator = validator or _schema_validator()
    for error in sorted(schema_validator.iter_errors(state), key=lambda item: (_json_path(item), item.message)):
        errors.append(f"{path}: schema {_json_path(error)}: {error.message}")

    if errors:
        return sorted(errors)

    thread_dir = path.parent
    expected_thread_id = thread_dir.name
    if state["thread_id"] != expected_thread_id:
        errors.append(
            f"{path}: thread_id {state['thread_id']!r} does not match containing directory {expected_thread_id!r}"
        )

    if not (thread_dir / "THREAD.md").is_file():
        errors.append(f"{path}: adjacent THREAD.md is required")

    participants = state["participants"]
    participant_ids = [participant["collaborator_id"] for participant in participants]
    declared = set(participant_ids)
    duplicates = sorted({item for item in participant_ids if participant_ids.count(item) > 1})
    if duplicates:
        errors.append(f"{path}: duplicate participant IDs: {', '.join(duplicates)}")

    references: list[tuple[str, str | None]] = [
        ("task_owner", state["task_owner"]),
        ("target_write_owner", state["target_write_owner"]),
        ("next_expected_actor", state["next_expected_actor"]),
        ("last_transition.actor", state["last_transition"]["actor"]),
    ]
    for label, collaborator_id in references:
        if collaborator_id is not None and collaborator_id not in declared:
            errors.append(f"{path}: {label} references undeclared participant {collaborator_id!r}")

    for index, surface in enumerate(state["allowed_secondary_write_surfaces"]):
        collaborator_id = surface["collaborator_id"]
        if collaborator_id not in declared:
            errors.append(
                f"{path}: allowed_secondary_write_surfaces[{index}].collaborator_id references undeclared participant {collaborator_id!r}"
            )

    target_paths = state["target"]["write_paths"]
    secondary_paths: list[tuple[str, str]] = []
    for value in target_paths:
        problem = validate_repo_path(value)
        if problem:
            errors.append(f"{path}: invalid target write path {value!r}: {problem}")
    for surface in state["allowed_secondary_write_surfaces"]:
        collaborator_id = surface["collaborator_id"]
        for value in surface["paths"]:
            problem = validate_repo_path(value)
            if problem:
                errors.append(f"{path}: invalid secondary write path {value!r}: {problem}")
            secondary_paths.append((collaborator_id, value))

    for target_path in target_paths:
        if validate_repo_path(target_path):
            continue
        for collaborator_id, secondary_path in secondary_paths:
            if validate_repo_path(secondary_path):
                continue
            if paths_may_overlap(target_path, secondary_path):
                errors.append(
                    f"{path}: secondary write path {secondary_path!r} for {collaborator_id!r} may overlap target write path {target_path!r}"
                )

    lifecycle_state = state["lifecycle_state"]
    has_target_paths = bool(target_paths)
    if lifecycle_state in ACTIVE_STATES and has_target_paths and state["target_write_owner"] is None:
        errors.append(f"{path}: {lifecycle_state} state with target write paths requires target_write_owner")

    if lifecycle_state == "CLOSED":
        if state["target_write_owner"] is not None:
            errors.append(f"{path}: CLOSED state requires target_write_owner = null")
        if state["next_expected_actor"] is not None:
            errors.append(f"{path}: CLOSED state requires next_expected_actor = null")

    if state["last_transition"]["to_state"] != lifecycle_state:
        errors.append(
            f"{path}: last_transition.to_state {state['last_transition']['to_state']!r} must equal lifecycle_state {lifecycle_state!r}"
        )

    return sorted(errors)


def discover_state_files(repo_root: Path) -> list[Path]:
    root = repo_root / "docs" / "model_collaboration" / "threads"
    if not root.is_dir():
        return []
    return sorted(path for path in root.glob("MC-[0-9][0-9][0-9][0-9]/STATE.json") if path.is_file())


def validate_many(paths: Iterable[Path]) -> list[str]:
    validator = _schema_validator()
    errors: list[str] = []
    for path in sorted(paths):
        errors.extend(validate_state_file(path, validator))
    return sorted(errors)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate ADS model-collaboration STATE.json files")
    parser.add_argument("paths", nargs="*", type=Path, help="STATE.json files; omit to discover guarded MC threads")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    paths = args.paths or discover_state_files(REPO_ROOT)
    if not paths:
        print("No guarded model-collaboration STATE.json files found.")
        return 0

    errors = validate_many(paths)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(f"Validated {len(paths)} model-collaboration state file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
