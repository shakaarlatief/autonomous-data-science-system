"""Real source-event qualification for the previously frozen P03 composite realizer.

The source event was actually committed after a separately published owner
policy acceptance and a separate executable/scope freeze. This test consumes
Git objects, executes the frozen production-backed composite, and preserves
J2/S1/J3 as deliberately independent postexecution decisions.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_delegated_s1_composite_realizer_v01 as runner,
)

EVENT = "ca91cbc27dc47f6efa383a788d4c9c02689bb9bd"
FREEZE = "c523340a20dd7628bc2a470594e28b48929a29dc"


@pytest.fixture(scope="module")
def source():
    return runner.observe_event(EVENT, FREEZE)


@pytest.fixture(scope="module")
def result():
    return runner.execute(EVENT, FREEZE)


def test_event_has_exact_frozen_parent_and_only_three_source_paths(source):
    _, _, facts = source
    assert facts["source_event_commit"] == EVENT
    assert facts["freeze_commit"] == FREEZE
    assert facts["changes"] == [
        {"status": "A", "path": runner.AFTER},
        {"status": "A", "path": runner.INTENT},
        {"status": "D", "path": runner.BEFORE},
    ]


def test_event_preserves_authored_identity_without_covered_authority(source):
    before, after, _ = source
    assert before["governed_source"] == after["governed_source"]
    assert after["governed_source"]["semantic_id"] == runner.SEMANTIC_ID
    assert after["source_owner_claim"]["natural_owner_relational_j2_qualified"] is False
    assert after["revision_provenance"]["successor_j1_activation"] == "NOT_ACTIVATED"
    assert after["asserted_implementation_coverage"] is None


def test_g006_production_index_executes_on_new_source_revisions(result):
    g = result["g006"]
    assert g["production_g006_executed"] is True
    assert g["identity_preserved"] is True
    assert g["serialization_order_independent"] is True
    assert g["current_carrier"] == runner.AFTER
    assert set(g["historical_carriers"]) == {runner.BEFORE, runner.AFTER}


def test_g013_production_and_full_generation_equivalence(result):
    g = result["g013"]
    assert g["production_g013_g009_executed"] is True
    assert g["affected_view"] == runner.VIEW_ID
    assert g["selected_equals_full"] is True
    assert g["selection_reason"] == [[runner.VIEW_ID, "DEPENDENCY_BINDING_CHANGED"]]
    assert g["previous_manifest"] == "STALE"
    assert g["current_manifest"] == "FRESH"
    assert g["G010_fixture_used_only_as_execution_prerequisite"] is True
    assert g["whole_ADS_corpus_G013_claimed"] is False


def test_newly_executed_components_do_not_self_admit_j2_or_j3(result):
    assert result["component_ids"] == list(runner.COMPONENTS)
    assert result["source_author_independently_authenticated"] is False
    assert result["postexecution_covers_admitted"] is False
    assert result["qualified_relational_j2"] is False
    assert result["s1_activated"] is False
    assert result["j3"].startswith("HOLD_")
    assert result["formal_R0_P03"] == "INCOMPLETE"
    assert result["production_modified"] is False
    assert result["physical_architecture_selected"] is False


def test_execution_receipt_exactly_matches_regeneration(result):
    assert json.loads(runner.OUTPUT.read_text("utf8")) == result


@pytest.mark.parametrize("field, spoofed", [
    ("realizer_id", "HISTORICAL_G006"),
    ("relationship", "FULL_COVERS"),
    ("execution_status", "EXECUTED"),
    ("qualified_relational_j2", True),
    ("s1_activated", True),
    ("j3", "SATISFIED"),
    ("author_identity_assurance", "INDEPENDENTLY_AUTHENTICATED_MODEL"),
])
def test_reject_source_action_claim_after_the_fact(source, field, spoofed):
    _, _, facts = source
    intent = json.loads(runner.git("show", f"{EVENT}:{runner.INTENT}"))
    intent[field] = spoofed
    with pytest.raises(ValueError, match="FALSE_AUTHORITY"):
        runner.validate_intent(intent, runner.load_scope(), FREEZE)


@pytest.mark.parametrize("field, spoofed", [
    ("natural_owner_j2_coverage", "FULL"),
    ("successor_j1_activation", "ACTIVATED"),
    ("prior_git_commit", "a" * 40),
    ("source_event_scope_id", "OTHER"),
    ("composite_realizer_id", "HISTORICAL_G013"),
])
def test_reject_source_carrier_relational_self_certification(source, field, spoofed):
    before, after, _ = source
    modified = deepcopy(after)
    modified["revision_provenance"][field] = spoofed
    with pytest.raises(ValueError, match="PROVENANCE_INVALID"):
        runner.validate_carrier(before, modified, runner.load_scope(), FREEZE)


def test_wrong_freeze_parent_rejected_before_any_execution():
    with pytest.raises(ValueError, match="PARENT_MISMATCH"):
        runner.observe_event(EVENT, "a" * 40)


def test_preacceptance_event_not_accepted_as_new_source():
    with pytest.raises(ValueError, match="PARENT_MISMATCH"):
        runner.observe_event(runner.BEFORE_COMMIT, FREEZE)
