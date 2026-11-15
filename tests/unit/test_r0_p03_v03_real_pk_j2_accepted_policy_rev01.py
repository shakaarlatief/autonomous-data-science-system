"""Negative qualification controls for the accepted forward-only P03 J2 policy.

The owner accepts the policy but no natural-owner J2, S1 activation or J3
certification. These tests distinguish a published policy from unauthorized
retroactive provenance or automatic future completion.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_j2_experiment_assurance_accepted_policy_rev01 as policy,
)


def specimen():
    return json.loads(policy.BINDING.read_text("utf8"))


def test_original_git_proposal_is_exact_and_still_predecision():
    source = policy.verify_original_git()
    assert source["decision_state"] == "PROPOSED_NOT_OWNER_ACCEPTED"
    assert source["authority"]["eligible_to_admit_j2_now"] is False


def test_exact_policy_acceptance_does_not_qualify_j2_or_j3():
    result = policy.build()
    assert result["policy"]["status"] == "OWNER_ACCEPTED_PROSPECTIVE_EXPERIMENT_ONLY_POLICY"
    assert result["policy"]["owner_independent_authentication"] is False
    assert result["qualified_experimental_relational_j2"] == 0
    assert result["preexisting_event"]["natural_owner_j2_qualified"] is False
    assert result["s1_activated"] is False
    assert result["j3_satisfied"] is False


def test_future_event_requires_published_acceptance_and_source_freeze():
    result = policy.build()
    assert result["policy"]["usable_before_binding_publication"] is False
    assert result["next_gates"]["one_source_realizer_scope_freeze"] == "REQUIRED_BEFORE_NEW_EVENT"
    assert result["next_gates"]["new_exact_git_event"] == "NOT_YET_PERFORMED"
    assert result["next_gates"]["g006_and_g013_execution_for_new_event"] == "NOT_YET_PERFORMED"
    assert result["next_gates"]["independent_j3"] == "NOT_EVALUATED"


@pytest.mark.parametrize("name, forged", [
    ("decision", "AMEND"),
    ("verbatim_owner_reply", "I ACCEPT. Proceed."),
    ("decision_date", "2026-11-14"),
    ("decision_provenance_class", "CRYPTOGRAPHICALLY_AUTHENTICATED_OWNER"),
    ("policy_proposal_git_commit", "a" * 40),
    ("policy_proposal_sha256", "b" * 64),
    ("policy_proposal_id", "UNRELATED_POLICY"),
    ("prospective_event_count", 3),
    ("accepted_scope", "PRODUCTION_J2_ALL_EVENTS"),
    ("effect_id", "P03PKA-E01-S0-IDENTITY-CONTINUITY"),
    ("previous_event_qualifying_j2_count", 1),
    ("previous_s1_activated", True),
    ("previous_j3", "SATISFIED"),
])
def test_binding_must_not_forge_owner_provenance_or_rewrite_history(name, forged):
    data = specimen()
    data[name] = forged
    with pytest.raises(ValueError, match="DRIFT"):
        policy.validate_binding(data)


@pytest.mark.parametrize("name", [
    "requires_separate_source_realizer_scope_freeze",
    "requires_new_git_event_after_acceptance",
    "requires_actual_new_revision_g006_g013",
    "requires_postexecution_source_author_covers",
    "requires_independent_j3_evaluation",
    "accepted_policy_not_an_admission",
])
def test_acceptance_cannot_waive_postdecision_evidence(name):
    data = specimen()
    data[name] = False
    with pytest.raises(ValueError, match="DRIFT"):
        policy.validate_binding(data)


@pytest.mark.parametrize("excluded", [
    "INDEPENDENT_MODEL_ACTOR_AUTHENTICATION",
    "RETROSPECTIVE_CHECKPOINT_948_J2",
    "AUTOMATIC_FUTURE_J2_FROM_OWNER_ACCEPTANCE",
    "AUTOMATIC_S1_ACTIVATION",
    "AUTOMATIC_J3_SATISFIED",
    "PRODUCTION_CHANGE_MIGRATION_OR_CUTOVER",
])
def test_acceptance_cannot_remove_authority_exclusions(excluded):
    data = specimen()
    data["excluded_authorizations"].remove(excluded)
    with pytest.raises(ValueError, match="DRIFT"):
        policy.validate_binding(data)


def test_extra_authority_field_cannot_self_authorize():
    data = specimen()
    data["automatic_j2_satisfied"] = True
    with pytest.raises(ValueError, match="CLOSED_SCHEMA"):
        policy.validate_binding(data)


def test_accepted_receipt_is_immutable_replay():
    assert json.loads(policy.OUTPUT.read_text("utf8")) == policy.build()
