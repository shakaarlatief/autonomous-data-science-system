"""Synthetic negative validation for F1 scoring-boundary review candidates.

The tests validate source provenance and review boundaries only. They are not
tests of a production/owner-trial scorer and do not approve any policy choice.
"""
from __future__ import annotations

import copy
import json

import pytest

from scripts.check_r0_p01_scoring_boundary_candidates import (
    CATALOGUE, GATES, INVENTORY, ROOT, validate, validate_payload,
)


@pytest.fixture
def candidate():
    return json.loads(CATALOGUE.read_text(encoding="utf-8"))


@pytest.fixture
def original_inventory():
    return json.loads(INVENTORY.read_text(encoding="utf-8"))


def test_bounded_source_anchored_review_catalogue_passes() -> None:
    status=validate()
    assert status["scenario_count"]==17
    assert len(status["per_gate"])==4
    assert set(status["per_gate"])==set(GATES)
    assert status["determinations"]=={"SOURCE_DETERMINED":12,"CANDIDATE_BLOCKED":5}


def test_unapproved_source_hash_is_rejected(candidate, original_inventory) -> None:
    candidate["approved_source_sha256"]["policy"]="0"*64
    with pytest.raises(ValueError,match="source byte hash changed"):
        validate_payload(candidate,original_inventory)


def test_unknown_source_unit_is_rejected(candidate, original_inventory) -> None:
    candidate["cases"][0]["source_basis"][0]="REV04_CONTRACT-L9999"
    with pytest.raises(ValueError,match="uncaptured source ref"):
        validate_payload(candidate,original_inventory)


def test_unreviewed_score_status_not_allowed(candidate, original_inventory) -> None:
    candidate["cases"][0]["determination"]="FULLY_FROZEN_EXPECTED_CLASS"
    with pytest.raises(ValueError,match="unreviewed determination"):
        validate_payload(candidate,original_inventory)


def test_duplicate_case_identity_rejected(candidate, original_inventory) -> None:
    candidate["cases"][1]["id"]=candidate["cases"][0]["id"]
    with pytest.raises(ValueError,match="duplicate or malformed"):
        validate_payload(candidate,original_inventory)


def test_missing_gate_family_is_rejected(candidate, original_inventory) -> None:
    candidate["cases"]=[x for x in candidate["cases"] if x["gate"]!="B08-A1"]
    with pytest.raises(ValueError,match="insufficient cross-boundary"):
        validate_payload(candidate,original_inventory)


def test_scoring_class_sensitive_cases_remain_blocked(candidate) -> None:
    blocked={x["id"] for x in candidate["cases"] if x["determination"]=="CANDIDATE_BLOCKED"}
    assert {"S1-04","S1-05","S2-03","S3-03","S4-01"}.issubset(blocked)
    assert all(
        "INVALID_INSTRUMENT" not in x["slug"] or x["determination"]!="CANDIDATE_BLOCKED"
        for x in candidate["cases"]
    )


def test_source_determined_cases_do_not_claim_entire_scored_result(candidate) -> None:
    """Scenario-local event outcomes are not unconditional whole-attempt scores."""
    by_id={x["id"]:x for x in candidate["cases"]}
    assert "not a valid proof" in by_id["S1-02"]["f1_evidence_or_test"]
    assert "higher-priority" in by_id["S2-02"]["source_grounded_conclusion"]
    assert "all flags" in by_id["S3-04"]["qualification_boundary"]
    assert "before final scored class" in by_id["S4-03"]["qualification_boundary"]


def test_reviewer_counts_and_approval_boundary_are_not_overwritten(candidate, original_inventory) -> None:
    candidate["claude_audit_results"]["reviewer_pending"]=0
    with pytest.raises(ValueError,match="Claude audit count"):
        validate_payload(candidate,original_inventory)
    candidate["claude_audit_results"]["reviewer_pending"]=55
    candidate["status"]="F1_FROZEN"
    with pytest.raises(ValueError,match="status change"):
        validate_payload(candidate,original_inventory)
