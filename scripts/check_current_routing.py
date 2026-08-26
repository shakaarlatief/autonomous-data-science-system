from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


MANIFEST_RELATIVE_PATH = Path("docs/current_routing.json")
EXPECTED_KEYS = {
    "schema_version",
    "current_checkpoint",
    "active_development_branch",
    "active_pr",
    "promoted_integration_branch",
    "promoted_integration_sha",
    "latest_specification",
    "latest_experiment_outcome",
    "current_boundary",
}
SHA_RE = re.compile(r"^[0-9a-f]{40}$")
BRANCH_RE = re.compile(r"^[A-Za-z0-9._/-]+$")
SPEC_RE = re.compile(r"^\d{3}$")


@dataclass(frozen=True)
class RoutingState:
    current_checkpoint: int
    active_development_branch: str
    active_pr: int | None
    promoted_integration_branch: str
    promoted_integration_sha: str
    latest_specification: str
    latest_experiment_outcome: str
    current_boundary: str


class ManifestError(ValueError):
    pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate the small machine-readable current-routing manifest and "
            "ensure current human-facing routing documents do not contradict it."
        )
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root. Defaults to the parent of scripts/.",
    )
    return parser.parse_args()


def require_type(data: dict[str, Any], key: str, expected_type: type) -> Any:
    value = data[key]
    if not isinstance(value, expected_type) or isinstance(value, bool):
        raise ManifestError(
            f"{key!r} must be {expected_type.__name__}; got {type(value).__name__}"
        )
    return value


def load_manifest(path: Path) -> RoutingState:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ManifestError(f"routing manifest not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ManifestError(f"routing manifest is invalid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ManifestError("routing manifest root must be an object")

    keys = set(data)
    missing = EXPECTED_KEYS - keys
    extra = keys - EXPECTED_KEYS
    if missing or extra:
        parts: list[str] = []
        if missing:
            parts.append("missing=" + ", ".join(sorted(missing)))
        if extra:
            parts.append("unexpected=" + ", ".join(sorted(extra)))
        raise ManifestError("routing manifest key contract violation: " + "; ".join(parts))

    schema_version = require_type(data, "schema_version", int)
    if schema_version != 1:
        raise ManifestError(f"unsupported schema_version: {schema_version}")

    current_checkpoint = require_type(data, "current_checkpoint", int)
    if current_checkpoint < 0:
        raise ManifestError("current_checkpoint must be non-negative")

    active_development_branch = require_type(data, "active_development_branch", str)
    promoted_integration_branch = require_type(data, "promoted_integration_branch", str)
    promoted_integration_sha = require_type(data, "promoted_integration_sha", str)
    latest_specification = require_type(data, "latest_specification", str)
    latest_experiment_outcome = require_type(data, "latest_experiment_outcome", str)
    current_boundary = require_type(data, "current_boundary", str)

    active_pr_raw = data["active_pr"]
    if active_pr_raw is None:
        active_pr = None
    elif isinstance(active_pr_raw, int) and not isinstance(active_pr_raw, bool) and active_pr_raw > 0:
        active_pr = active_pr_raw
    else:
        raise ManifestError("active_pr must be null or a positive integer")

    for key, branch in (
        ("active_development_branch", active_development_branch),
        ("promoted_integration_branch", promoted_integration_branch),
    ):
        if not branch or not BRANCH_RE.fullmatch(branch):
            raise ManifestError(f"{key} is not a valid bounded branch identifier: {branch!r}")

    if not SHA_RE.fullmatch(promoted_integration_sha):
        raise ManifestError("promoted_integration_sha must be one lowercase 40-character SHA")
    if not SPEC_RE.fullmatch(latest_specification):
        raise ManifestError("latest_specification must be a zero-padded three-digit identifier")
    if not latest_experiment_outcome.strip():
        raise ManifestError("latest_experiment_outcome must be non-empty")
    if not current_boundary.strip():
        raise ManifestError("current_boundary must be non-empty")

    return RoutingState(
        current_checkpoint=current_checkpoint,
        active_development_branch=active_development_branch,
        active_pr=active_pr,
        promoted_integration_branch=promoted_integration_branch,
        promoted_integration_sha=promoted_integration_sha,
        latest_specification=latest_specification,
        latest_experiment_outcome=latest_experiment_outcome,
        current_boundary=current_boundary,
    )


def expected_pr_text(active_pr: int | None) -> str:
    return "none" if active_pr is None else f"#{active_pr}"


def required_fragments(state: RoutingState) -> dict[Path, tuple[str, ...]]:
    pr_text = expected_pr_text(state.active_pr)
    return {
        Path("README.md"): (
            f"checkpoint            {state.current_checkpoint}",
            f"active branch         {state.active_development_branch}",
            f"active PR             {pr_text}",
            f"promoted V1 head      {state.promoted_integration_sha}",
            f"Specification {state.latest_specification}",
            state.latest_experiment_outcome,
        ),
        Path("docs/CURRENT_STATE.md"): (
            f"**Checkpoint:** {state.current_checkpoint}",
            f"**Active development branch:** `{state.active_development_branch}`",
            f"**Active PR:** {pr_text}",
            (
                f"**Promoted V1 integration branch:** `{state.promoted_integration_branch}` "
                f"at `{state.promoted_integration_sha}`"
            ),
            f"Specification {state.latest_specification}",
            state.latest_experiment_outcome,
        ),
        Path("docs/KNOWLEDGE_MAP.md"): (
            f"**Current checkpoint:** {state.current_checkpoint}",
            f"**Active development branch:** `{state.active_development_branch}`",
            f"**Active PR:** {pr_text}",
            (
                f"**Promoted V1 integration branch:** `{state.promoted_integration_branch}` "
                f"at `{state.promoted_integration_sha}`"
            ),
            f"Specification {state.latest_specification}",
            state.latest_experiment_outcome,
        ),
    }


def validate_document_fragments(root: Path, state: RoutingState) -> list[str]:
    errors: list[str] = []
    for relative_path, fragments in required_fragments(state).items():
        path = root / relative_path
        try:
            text = path.read_text(encoding="utf-8")
        except FileNotFoundError:
            errors.append(f"{relative_path}: file missing")
            continue
        for fragment in fragments:
            if fragment not in text:
                errors.append(f"{relative_path}: missing routing fragment {fragment!r}")
    return errors


def validate_checkpoint_exists(root: Path, checkpoint: int) -> list[str]:
    checkpoint_dir = root / "docs" / "checkpoints"
    prefix = f"{checkpoint:03d}_"
    matches = [path for path in checkpoint_dir.glob(f"{prefix}*.md") if path.is_file()]
    if len(matches) == 1:
        return []
    if not matches:
        return [f"no checkpoint file found for current_checkpoint={checkpoint:03d}"]
    return [
        f"multiple checkpoint files found for current_checkpoint={checkpoint:03d}: "
        + ", ".join(sorted(path.name for path in matches))
    ]


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    try:
        state = load_manifest(root / MANIFEST_RELATIVE_PATH)
    except ManifestError as exc:
        print(f"Current routing manifest error: {exc}", file=sys.stderr)
        return 2

    errors = validate_checkpoint_exists(root, state.current_checkpoint)
    errors.extend(validate_document_fragments(root, state))

    if errors:
        print("Current routing consistency violations:")
        for error in errors:
            print(f"  ERROR {error}")
        return 1

    print(
        "Current routing consistency: PASS "
        f"checkpoint={state.current_checkpoint:03d} "
        f"active_branch={state.active_development_branch} "
        f"active_pr={expected_pr_text(state.active_pr)} "
        f"promoted={state.promoted_integration_branch}@{state.promoted_integration_sha} "
        f"latest_specification={state.latest_specification} "
        f"latest_outcome={state.latest_experiment_outcome}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
