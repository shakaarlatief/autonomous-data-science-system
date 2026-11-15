"""Adversarial source-relative RELATIONAL J2 admission tests for one actual P03 event.

These checks distinguish postexecution authorial COVERS from accepted policy,
immutable Git facts and independently replayed G006/G013 component observations.
A matching hash and self-declared same author are not independent actor proof.
The resulting one J2 fact is experiment-only and this test never activates S1
or claims J3. There is no primary-task author, formal corpus or scoring here.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_delegated_s1_j2_admission_v01 as admission,
)


@pytest.fixture(scope="module")
def facts():
    return admission.validate_original_sources()


@pytest.fixture(scope="module")
def result():
    return admission.qualify()


def test_exact_one_source_only_declaration_and_chronology(facts):
    claim, scope, intent, receipt = facts
    assert admission.direct_parent(admission.CLAIM_COMMIT) == admission.EVIDENCE_COMMIT
    assert admission.changed_paths(admission.CLAIM_COMMIT) == [
        ("A", admission.CLAIM_PATH)
    ]
    assert intent["relationship"] == "PROSPECTIVE_EXECUTION_INTENT_NOT_J2_COVERS"
    assert receipt["postexecution_covers_admitted"] is False
    assert claim["declaration_status"].endswith("SEPARATE_J2_ADMISSION")


def test_source_relative_qualifies_only_accepted_weak_assurance(result):
    assert result["status"] == "QUALIFIED_SOURCE_RELATIVE_EXPERIMENTAL_J2_WEAK_ACTOR_ASSURANCE"
    assert result["qualified_experimental_relational_j2_count"] == 1
    assert result["all_component_evidence_replayed"] is True
    assert result["one_fact_tuple_in_bounded_source_world"] is True
    assert result["assurance_class"] == admission.ASSURANCE
    assert result["independent_model_identity_proven"] is False
    assert result["production_j2_qualified"] is False
    assert result["prior_948_j2_upgraded"] is False
    assert result["previous_s0_execution_credited_to_s1"] is False
    assert result["s1_activated_by_this_j2_verifier"] is False
    assert result["j3_satisfied_by_this_j2_verifier"] is False


def test_exact_declared_owner_is_not_historical_library_owner(facts):
    claim, scope, intent, receipt = facts
    admission.validate_claim(claim, scope, intent, receipt)
    assert claim["natural_owner"]["natural_owner_scope"] == "AUTHOR_OF_EXPERIMENT_ORCHESTRATION_ONLY"
    assert claim["natural_owner"]["independently_authenticated"] is False
    assert claim["realizer"]["historical_g006_g013_library_ownership_asserted"] is False


def test_bounded_source_world_contains_exactly_one_matching_relation():
    relations = admission.admissible_source_relations()
    assert any(p == admission.CLAIM_PATH and d["relation"] == "COVERS"
               for p, d in relations)


@pytest.mark.parametrize("field,value", [
    ("declaration_id", "OTHER"),
    ("declaration_status", "GOVERNING_J2_SATISFIED"),
    ("fact_class", "OBSERVABLE"),
    ("relation", "OWNED_BY_GIT_AUTHOR"),
    ("relation_scope", "ALL_PRODUCTION_SOURCES"),
    ("world_id", "UNRELATED"),
    ("accepted_effect_id", "P03PKA-E01-S0-IDENTITY-CONTINUITY"),
    ("authorial_coverage_summary", "CERTIFIED_FULL_BY_AUTHOR"),
])
def test_source_cannot_expand_its_own_relation_authority(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate[field] = value
    with pytest.raises(ValueError, match="SCOPE_OR_FALSE_AUTHORITY"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("independently_authenticated", True),
    ("production_implementation_author", True),
    ("provenance", "PROVIDER_ATTESTED"),
    ("role", "CLAIMED_PRODUCTION_IMPLEMENTATION_OWNER"),
    ("natural_owner_scope", "G006_G013_HISTORICAL_LIBRARIES"),
    ("self_declared_same_source_author_as_at_action_intent", False),
])
def test_weak_model_authentication_not_upgradable(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["natural_owner"][field] = value
    with pytest.raises(ValueError, match="OWNER_OR_AUTHENTICATION"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("id", "G006_HISTORICAL_AUTHOR"),
    ("executable_path", "tools/project_knowledge/identity.py"),
    ("executable_sha256", "a" * 64),
    ("historical_g006_g013_library_ownership_asserted", True),
])
def test_realizer_must_be_exact_owned_composite(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["realizer"][field] = value
    with pytest.raises(ValueError, match="NOT_OWNED_COMPOSITE"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("owner_acceptance_commit", "a" * 40),
    ("scope_freeze_commit", "b" * 40),
    ("proposal_sha256", "c" * 64),
    ("scope_id", "UNRELATED"),
])
def test_policy_decision_and_scope_are_exact(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["accepted_policy"][field] = value
    with pytest.raises(ValueError, match="WRONG_ACCEPTED_POLICY"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("commit", admission.CLAIM_COMMIT),
    ("parent", "d" * 40),
    ("after_path", "invented.json"),
    ("at_action_relationship", "POSTEXECUTION_COVERS_AT_SOURCE_EVENT"),
])
def test_old_event_or_fake_intent_not_admissible(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["source_event"][field] = value
    with pytest.raises(ValueError, match="WRONG_SOURCE_EVENT"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("published_evidence_commit", "d" * 40),
    ("receipt_sha256", "e" * 64),
    ("formal_ads_corpus_rebuild", True),
    ("independent_model_or_provider_actor_attestation", True),
    ("source_role", "SIGNED_PROVIDER_RECEIPT"),
])
def test_new_execution_source_must_be_exact_and_bounded(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["execution_evidence"][field] = value
    with pytest.raises(ValueError, match="EVIDENCE_SOURCE_WRONG"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field", [
    "formal_b0_b4_scored",
    "historical_s0_evidence_carryover",
    "j3_satisfied",
    "physical_target_selected",
    "production_j2_accepted",
    "qualified_relational_j2",
    "s1_activated",
])
def test_source_authored_assertion_cannot_self_certify(field, facts):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["authority"][field] = True
    with pytest.raises(ValueError, match="SCOPE_OR_FALSE_AUTHORITY"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("execution_receipt_precedes_declaration", False),
    ("new_source_event_already_committed", False),
    ("not_backdated_as_at_action_covers", False),
])
def test_false_temporal_claim_rejected(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["postexecution_timing"][field] = value
    with pytest.raises(ValueError, match="TIMING_CLAIM_WRONG"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("field,value", [
    ("coverage_assertion", "FULL_CERTIFIED_J3"),
    ("component_id", "OUTSIDE_ACCEPTED_S1"),
    ("evidence_field", "older_g013.selected_equals_full"),
    ("observation_kind", "UNEXECUTED_CLAIM"),
])
def test_component_claim_cannot_upgrade_coverage(facts, field, value):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["all_required_component_claims"][0][field] = value
    with pytest.raises(ValueError, match="COMPONENT_CLAIM_CHANGED"):
        admission.validate_claim(candidate, scope, intent, receipt)


def test_omitting_component_fails_closed(facts):
    claim, scope, intent, receipt = facts
    candidate = deepcopy(claim)
    candidate["all_required_component_claims"].pop()
    with pytest.raises(ValueError, match="ALL_REQUIRED_INCOMPLETE"):
        admission.validate_claim(candidate, scope, intent, receipt)


@pytest.mark.parametrize("path,value", [
    (("g006", "identity_preserved"), False),
    (("g006", "production_g006_executed"), False),
    (("g013", "selected_equals_full"), False),
    (("g013", "current_manifest"), "STALE"),
    (("g013", "previous_manifest"), "FRESH"),
    (("g013", "affected_view"), "wrong"),
    (("event", "source_event_commit"), admission.CLAIM_COMMIT),
    (("postexecution_covers_admitted",), True),
])
def test_engineering_observation_not_satisfied_by_author_claim(facts, path, value):
    claim, scope, intent, receipt = facts
    bad = deepcopy(receipt)
    target = bad
    for field in path[:-1]:
        target = target[field]
    target[path[-1]] = value
    with pytest.raises(ValueError, match="COMPONENTS_NOT_PROVEN"):
        admission.validate_claim(claim, scope, intent, bad)


def test_no_extra_source_claim_fields_can_set_acceptance(facts):
    claim, scope, intent, receipt = facts
    bad = deepcopy(claim)
    bad["admitted_j2"] = True
    with pytest.raises(ValueError, match="CLOSED_SCHEMA"):
        admission.validate_claim(bad, scope, intent, receipt)


def test_admission_immutable_replay_result(result):
    assert json.loads(admission.OUTPUT.read_text("utf8")) == result
