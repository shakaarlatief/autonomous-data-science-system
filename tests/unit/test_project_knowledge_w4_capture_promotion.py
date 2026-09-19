"""W4 production capture/promotion qualification against the real repository state."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.capture import CaptureValidationError, build_promotion_plan
from tools.project_knowledge.model import (
    PromotionDisposition,
    PromotionUnitDisposition,
    SemanticId,
)
from tools.project_knowledge.services.cli_ops import _without_generated_entries
from tools.project_knowledge.services.validation import validate_repository


ROOT = Path(__file__).resolve().parents[2]
OPEN_POINTER = ROOT / "docs/project_knowledge/captures/open/w4_branch_boundary_scope.json"
HISTORICAL_CAPTURE = ROOT / "docs/project_knowledge/captures/historical/w4_branch_boundary_scope.json"
BOUNDARY_SOURCE = ROOT / "docs/project_knowledge/project_integration_boundary.md"

CAPTURE_ID = "CAPTURE:W4-BRANCH-BOUNDARY-SCOPE"
TARGET_ID = "PROJECT-INTEGRATION-BOUNDARY"
UNIT_ID = "UNIT:PROJECT-INTEGRATION-BOUNDARY-BRANCH-LIFECYCLE-NONOWNERSHIP"
HISTORICAL_PATH = "docs/project_knowledge/captures/historical/w4_branch_boundary_scope.json"


def _validated_commit():
    snapshot = commit_snapshot(ROOT, "HEAD")
    result = validate_repository(
        _without_generated_entries(snapshot),
        durable_evidence=True,
    )
    assert result.ok
    return result


def _historical_capture(result):
    return next(
        capture
        for capture in result.captures
        if capture.source.semantic_id
        and capture.source.semantic_id.value == CAPTURE_ID
    )


def _target(result):
    return next(
        source
        for source in result.sources
        if source.semantic_id
        and source.semantic_id.value == TARGET_ID
    )


def test_w4_open_capture_is_replaced_by_inert_archival_pointer() -> None:
    pointer = json.loads(OPEN_POINTER.read_text(encoding="utf-8"))

    assert "profile" not in pointer
    assert pointer == {
        "archived_to": HISTORICAL_PATH,
        "capture_semantic_id": CAPTURE_ID,
        "note": "This is an inert archival pointer, not a capture.v1 declaration.",
        "status": "ARCHIVED",
    }

    result = _validated_commit()
    matching = [
        capture
        for capture in result.captures
        if capture.source.semantic_id
        and capture.source.semantic_id.value == CAPTURE_ID
    ]
    assert len(matching) == 1
    assert matching[0].source.carrier_path == HISTORICAL_PATH
    assert matching[0].source.declaration.fields["state"] == "COMPLETED"


def test_w4_promoted_boundary_materializes_accepted_nonownership_and_provenance() -> None:
    result = _validated_commit()
    target = _target(result)
    text = BOUNDARY_SOURCE.read_text(encoding="utf-8")
    provenance = target.declaration.fields["provenance"]

    assert target.declaration.fields["promoted_branch"] == "v1-frontend-spike"
    assert (
        target.declaration.fields["promoted_commit"]
        == "2480109fadeee1e480ef03b82e335aacdf9adf91"
    )
    assert "does not own the policy that determines when Git development branches are created" in text
    assert "must therefore not be interpreted as a branch-lifecycle policy" in text
    assert "path:" + HISTORICAL_PATH in provenance
    assert "path:docs/OPEN_ARCHITECTURE_BACKLOG.md#AB-032" in provenance


def test_w4_archived_capture_cannot_reenter_promotion_planning() -> None:
    result = _validated_commit()
    capture = _historical_capture(result)
    target = _target(result)
    unit = SemanticId(UNIT_ID)

    with pytest.raises(CaptureValidationError) as error:
        build_promotion_plan(
            capture,
            result.sources,
            target_semantic_id=SemanticId(TARGET_ID),
            expected_target_revision=target.revision,
            review_disposition="ACCEPTED_FOR_PROMOTION",
            accepted_understanding=(
                "The Project Integration Boundary does not own Git branch-lifecycle policy."
            ),
            required_semantic_units=(unit,),
            unit_dispositions=(
                PromotionUnitDisposition(
                    unit,
                    PromotionDisposition.MATERIALIZED_IN_CANONICAL_SOURCE,
                ),
            ),
        )

    assert error.value.code == "CAPTURE_NOT_OPEN"


def test_w4_accepted_meaning_and_provenance_survive_capture_archival() -> None:
    result = _validated_commit()
    capture = _historical_capture(result)
    target_text = BOUNDARY_SOURCE.read_text(encoding="utf-8")

    assert "does not own or imply policy" in capture.summary
    assert "branch-lifecycle policy" in target_text
    assert "interaction:chatgpt-27" in capture.provenance_chain
    assert "path:docs/OPEN_ARCHITECTURE_BACKLOG.md#AB-032" in capture.provenance_chain
    assert "path:" + HISTORICAL_PATH in _target(result).declaration.fields["provenance"]
