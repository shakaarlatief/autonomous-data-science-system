"""Adversarial tests for the unaccepted, source-bound P03 J2 policy proposal.

All tests intentionally keep this policy inactive. A prospective model-authored
source statement, even with an exact Git hash, is not a credential, an owner
decision, a qualified J2 relation, an S1 activation or a J3 PASS.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_j2_experiment_assurance_preflight_rev01 as p,
)


@pytest.fixture
def candidate():
    return json.loads(p.SOURCE.read_text("utf8"))


def test_exact_original_source_byte_pin_and_proposed_state():
    proposal = p.load_source()
    assert proposal["decision_state"] == "PROPOSED_NOT_OWNER_ACCEPTED"
    assert p.build()["owner_decision"] == "NOT_RECEIVED"


def test_previous_exact_git_event_stays_hold_with_independent_source_replay():
    receipt = p.build()
    assert receipt["prior_event_git_structural_result"] == "PASS"
    assert receipt["prior_event_nat_owner_authentication"] == "NOT_INDEPENDENTLY_VERIFIED"
    assert receipt["prior_event_j2"] == receipt["prior_event_j3"] == "HOLD"
    assert receipt["prior_event_s1"] == "NOT_ACTIVATED"
    assert receipt["strong_actor_authentication_satisfied"] is False


def test_owner_acceptance_would_not_auto_qualify_j2_or_j3():
    receipt = p.build()
    assert receipt["eligible_to_admit_existing_j2"] is False
    assert receipt["auto_qualify_future_j2_if_policy_accepted"] is False
    assert receipt["future_source_revision_and_real_execution_required"] is True
    assert receipt["formal_r0_p03"] == "INCOMPLETE"
    assert receipt["production_authority_changed"] is False


@pytest.mark.parametrize("field,value", [
    ("decision_state", "ACCEPTED"),
    ("decision_kind", "PRODUCTION_SOURCE_OWNER_ASSURANCE"),
    ("source_head_preparation", "a" * 40),
])
def test_reject_source_level_claim_to_owner_decision_or_production(candidate, field, value):
    candidate[field] = value
    with pytest.raises(ValueError, match="AUTHORITY"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("field,value", [
    ("accepted_j1_effect_id", "P03PKA-E01-S0-IDENTITY-CONTINUITY"),
    ("required_components", ["EXPLICIT_IDENTITY_PRESERVING_MOVE"]),
    ("original_948_source_event", "b" * 40),
    ("original_948_qualified_relational_j2", 1),
    ("original_948_s1_activated", True),
    ("original_948_j3", "SATISFIED"),
])
def test_reject_accepted_j1_or_historical_j2_reinterpretation(candidate, field, value):
    candidate["source_context"][field] = value
    with pytest.raises(ValueError, match="AUTHORITY"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("field,value", [
    ("accepted_by_owner", True),
    ("eligible_to_admit_j2_now", True),
    ("qualified_relational_j2", 1),
    ("s1_activated", True),
    ("j3_certified", True),
    ("formal_r0_p03_completed", True),
    ("physical_architecture_selected", True),
    ("production_authority_changed", True),
])
def test_reject_policy_self_activation(candidate, field, value):
    candidate["authority"][field] = value
    with pytest.raises(ValueError, match="AUTHORITY"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("field,value", [
    ("policy_state", "ACCEPTED"),
    ("effective_rule", "RETROSPECTIVE_ALL_EVENTS"),
    ("owner_authenticity_class", "INDEPENDENTLY_VERIFIED_PRODUCTION_OWNER"),
    ("source_author_authenticity_class", "GIT_AUTHOR_EQUALS_AUTHENTICATED_MODEL"),
    ("source_author_scope", "OWNER_OF_ALL_G006_G013_CODE"),
    ("duration", "UNBOUNDED_PRODUCTION_POLICY"),
    ("automatic_qualification_if_owner_accepts", True),
    ("independent_strong_natural_owner_authentication_claimed", True),
    ("new_source_event_required_after_owner_acceptance", False),
    ("j3_re_evaluation_required", False),
    ("full_r0_p03_method_unchanged", False),
])
def test_reject_weak_assurance_promotion_or_temporal_backdating(candidate, field, value):
    candidate["candidate_policy"][field] = value
    with pytest.raises(ValueError, match="ASSURANCE"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("removed", [
    "ACTUAL_PRODUCTION_G006_AND_G013_G009_ON_EXACT_NEW_SOURCE_REVISION",
    "POSTEXECUTION_COVERS_DECLARATION_BY_SAME_SCOPED_SOURCE_AUTHOR_NOT_BACKDATED",
    "SCOPED_AUTHOR_CONTROLS_EXACT_EXECUTABLE_EXPERIMENT_REALIZER_NOT_JUST_NARRATIVE_SOURCE",
    "COVERAGE_BOUND_TO_COMPOSITE_REALIZER_NOT_HISTORICAL_G006_G013_IMPLEMENTATION_AUTHORSHIP",
    "NO_PREDECESSOR_S0_EVIDENCE_CARRIED_AS_S1_J3_PASS",
    "INDEPENDENT_SEPARATE_J3_EVALUATOR_WITH_EXACT_ADMITTED_J1_AND_J2",
    "SOURCE_RELATIVE_REFERENCE_TRUTH_EXPOSES_WEAK_ASSURANCE_TO_ALL_B0_B4_ARMS",
])
def test_reject_omission_of_essential_technical_controls(candidate, removed):
    candidate["candidate_policy"]["technical_requirements"].remove(removed)
    with pytest.raises(ValueError, match="ASSURANCE"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("removed", [
    "RETROACTIVE_948_J2_CERTIFICATION",
    "INDEPENDENT_MODEL_SESSION_ACTOR_AUTHENTICATION",
    "S1_ACTIVATION_FROM_SOURCE_CLAIM_ALONE",
    "J3_SATISFIED_FROM_SOURCE_CLAIM_ALONE",
    "HISTORICAL_G006_G013_IMPLEMENTATION_AUTHORSHIP",
    "PRODUCTION_NATURAL_OWNER_COVERS",
])
def test_reject_removal_of_false_authority_exclusion(candidate, removed):
    candidate["candidate_policy"]["non_delegable_claims"].remove(removed)
    with pytest.raises(ValueError, match="ASSURANCE"):
        p.validate_candidate(candidate)


@pytest.mark.parametrize("field", [
    "author_self_claim_cannot_self_admit",
    "source_hash_is_not_independent_actor_authentication",
    "structurally_valid_claim_can_still_fail_owner_assurance",
    "prior_source_result_stays_hold",
    "no_registered_authenticated_source_adapter_in_this_proposal",
    "formal_primary_and_legacy_reference_guards_unchanged",
])
def test_reject_mutated_safety_qualifier(candidate, field):
    candidate["independence_and_falsification"][field] = False
    with pytest.raises(ValueError, match="DECISION_AND_FALSIFIER"):
        p.validate_candidate(candidate)


def test_reject_surreptitious_new_record_fields(candidate):
    candidate["candidate_policy"]["preaccepted_j2"] = "YES"
    with pytest.raises(ValueError, match="CLOSED_INNER"):
        p.validate_candidate(candidate)


def test_reject_forged_decision_options(candidate):
    candidate["decision_choices"]["ACCEPT"] = "Unconditional source qualification"
    with pytest.raises(ValueError, match="DECISION_AND_FALSIFIER"):
        p.validate_candidate(candidate)


def test_immutable_unscored_preflight_matches_regeneration():
    assert json.loads(p.OUTPUT.read_text("utf8")) == p.build()
