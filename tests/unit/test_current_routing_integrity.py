from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "scripts" / "check_current_routing.py"
SPEC = importlib.util.spec_from_file_location("check_current_routing_integrity", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def state(*, checkpoint: int = 268, boundary: str = "repository-integrity"):
    return MODULE.RoutingState(
        current_checkpoint=checkpoint,
        active_development_branch="v1-source-vault-bootstrap-resume",
        active_pr=None,
        promoted_integration_branch="v1-frontend-spike",
        promoted_integration_sha="a" * 40,
        latest_specification="026",
        latest_experiment_outcome="TEST_OUTCOME",
        current_boundary=boundary,
    )


def write_checkpoint(root: Path, number: int) -> None:
    path = root / "docs" / "checkpoints" / f"{number:03d}_test.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Checkpoint {number:03d}\n", encoding="utf-8")


def manifest_payload(boundary: str) -> dict:
    return {
        "schema_version": 1,
        "current_checkpoint": 269,
        "active_development_branch": "v1-source-vault-bootstrap-resume",
        "active_pr": None,
        "promoted_integration_branch": "v1-frontend-spike",
        "promoted_integration_sha": "a" * 40,
        "latest_specification": "026",
        "latest_experiment_outcome": "TEST_OUTCOME",
        "current_boundary": boundary,
    }


def test_stale_but_agreeing_live_state_fails_on_active_branch(tmp_path: Path) -> None:
    write_checkpoint(tmp_path, 268)
    write_checkpoint(tmp_path, 269)

    errors = MODULE.validate_checkpoint_freshness(
        tmp_path,
        state(checkpoint=268),
        "v1-source-vault-bootstrap-resume",
    )

    assert any("stale" in error and "branch_max=269" in error for error in errors)


def test_unrelated_branch_does_not_create_false_active_branch_freshness_failure(tmp_path: Path) -> None:
    write_checkpoint(tmp_path, 268)
    write_checkpoint(tmp_path, 269)

    errors = MODULE.validate_checkpoint_freshness(
        tmp_path,
        state(checkpoint=268),
        "independent-review-branch",
    )

    assert errors == []


def test_active_branch_matching_max_checkpoint_passes(tmp_path: Path) -> None:
    write_checkpoint(tmp_path, 268)
    write_checkpoint(tmp_path, 269)

    errors = MODULE.validate_checkpoint_freshness(
        tmp_path,
        state(checkpoint=269),
        "v1-source-vault-bootstrap-resume",
    )

    assert errors == []


@pytest.mark.parametrize(
    "boundary",
    [
        "repository-integrity-269",
        "Repository-integrity",
        "repository_integrity",
        "repository/integrity",
        "repository integrity",
        "repository--integrity",
        "a" * 65,
    ],
)
def test_volatile_or_nonsemantic_current_boundary_is_rejected(
    tmp_path: Path, boundary: str
) -> None:
    path = tmp_path / "routing.json"
    path.write_text(json.dumps(manifest_payload(boundary)), encoding="utf-8")

    with pytest.raises(MODULE.ManifestError, match="current_boundary"):
        MODULE.load_manifest(path)


def test_stable_semantic_current_boundary_is_accepted(tmp_path: Path) -> None:
    path = tmp_path / "routing.json"
    path.write_text(
        json.dumps(manifest_payload("repository-integrity-hardening")),
        encoding="utf-8",
    )

    loaded = MODULE.load_manifest(path)

    assert loaded.current_boundary == "repository-integrity-hardening"
