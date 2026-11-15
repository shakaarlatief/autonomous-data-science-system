"""Adversarial J3 evaluation of accepted P03 S1 REPLACE/OPEN_RESET semantics.

The accepted-J1 owner effects, a distinct source-relative J2 receipt, and
production-backed new-event observations are separate inputs. No authorial
FULL/status field or derived navigation output is a governing acceptance.
S1 activation and J3 ALL_REQUIRED are independently tested. A failed
component is HOLD, never carried over from the retired S0 requirement.
"""
from __future__ import annotations

from copy import deepcopy
import itertools
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_delegated_s1_j3_lifecycle_v01 as j3,
    v03_real_pk_accepted_j1_projection_v01 as j1,
    v03_real_pk_delegated_s1_j2_admission_v01 as j2,
    v03_real_pk_delegated_s1_composite_realizer_v01 as realizer,
)


@pytest.fixture(scope="module")
def inputs():
    world = j1.build()
    admitted = json.loads(j2.OUTPUT.read_text("utf8"))
    execution = json.loads(realizer.OUTPUT.read_text("utf8"))
    return world, admitted, execution


@pytest.fixture(scope="module")
def output():
    return j3.build()


def test_exact_published_source_relative_s1_j3_evaluated(output):
    assert output["status"] == "SEPARATE_EXPERIMENTAL_SOURCE_RELATIVE_J3_PREDICATE_PASS"
    assert output["model_actor_independently_authenticated"] is False
    assert output["qualified_experiment_only_j2_count"] == 1
    assert output["evaluator_mechanically_separate_from_source_claim"] is True
    assert output["evaluator_independently_authored_blind"] is False
    assert output["formal_r0_p03"] == "INCOMPLETE"
    assert output["production_authority_activated"] is False
    assert output["physical_architecture_selected"] is False


def test_currentness_is_s1_not_legacy_s0_after_qualified_source_event(output):
    value = output["derived_semantics"]
    assert value["activation_status"] == j3.CURRENTNESS_STATUS
    assert value["current_effect_ids"] == [j3.E02, j3.E04]
    assert value["retired_current_requirement"] == j3.E01
    assert value["new_current_requirement"] == j3.E02
    assert value["lineage_relation"] == "REPLACE"
    assert value["realization_succession"] == "OPEN_RESET"


def test_open_reset_initializes_no_carried_credit_then_new_s1_requalifies(output):
    value = output["derived_semantics"]
    assert value["s1_open_reset"] is True
    assert value["initial_successor_component_credit"] == 0
    assert value["previous_s0_evidence_carried"] is False
    assert value["previous_s0_j3_not_backfilled"] is True
    assert value["s1_components"] == {name: True for name in realizer.COMPONENTS}
    assert value["s1_component_count"] == 4
    assert value["s1_required_count"] == 4
    assert value["s1_j3"] == j3.J3_PASS
    assert value["s1_j3_satisfied"] is True
    assert value["production_j3_satisfied"] is False


def test_no_path_or_generated_view_as_governing_authority(output):
    value = output["derived_semantics"]
    assert value["e04_path_or_generated_index_as_authority"] is False
    assert value["j1_authority_source"] == "EXACT_EXPERIMENT_ONLY_OWNER_ACCEPTED_J1_GIT_BINDING"
    assert value["j2_authority_source"] == "SEPARATELY_QUALIFIED_EXPERIMENT_ONLY_SOURCE_RELATIVE_COVERS"
    assert value["execution_evidence_source"] == j3.SOURCE_EVIDENCE_ROLE


@pytest.mark.parametrize("mutation", [
    "owner_decision", "world_id", "count", "prestate", "s1_dormancy",
    "activation_already_done", "source_qualified_before", "s0_j2_qualified",
    "j3_auto_pass", "production_migration",
])
def test_reject_original_j1_or_prestate_promotion(inputs, mutation):
    world, admitted, execution = inputs
    changed = deepcopy(world)
    if mutation == "owner_decision":
        changed["owner_decision"]["verdict"] = "NOT_ACCEPTED"
    elif mutation == "world_id":
        changed["world_id"] = "NOT_P03"
    elif mutation == "count":
        changed["accepted_j1"]["count"] = 3
    elif mutation == "prestate":
        changed["accepted_j1"]["current_effect_ids"] = [j3.E02, j3.E04]
    elif mutation == "s1_dormancy":
        changed["accepted_j1"]["dormant_until_source_revision"] = []
    elif mutation == "activation_already_done":
        changed["currentness"]["activation_status"] = "ACTIVATED"
    elif mutation == "source_qualified_before":
        changed["currentness"]["actual_source_revision_qualified"] = True
    elif mutation == "s0_j2_qualified":
        changed["j2"]["qualified_count"] = 1
    elif mutation == "j3_auto_pass":
        changed["j3"]["satisfaction_certified"] = True
    elif mutation == "production_migration":
        changed["production_migration_authorized"] = True
    with pytest.raises(ValueError, match="ORIGINAL_ACCEPTED_J1"):
        j3.evaluate_snapshot(changed, admitted, execution)


@pytest.mark.parametrize("mutation", [
    "composition_any", "missing_component", "changed_s1_effect",
    "replace_becomes_refine", "succession_carry", "wrong_lineage",
    "false_authority_disabled", "future_evidence_carry",
    "no_observable_execution_required",
])
def test_unchanged_s1_and_open_reset_contract_is_required(inputs, mutation):
    world, admitted, execution = inputs
    changed = deepcopy(world)
    effects = changed["accepted_j1"]["effects"]
    if mutation == "composition_any":
        effects[1]["completion_contract"]["composition"] = "ANY"
    elif mutation == "missing_component":
        effects[1]["completion_contract"]["required_components"].pop()
    elif mutation == "changed_s1_effect":
        effects[1]["id"] = "EFFECT_RENAMED"
    elif mutation == "replace_becomes_refine":
        effects[2]["lineage"]["relation"] = "REFINE"
    elif mutation == "succession_carry":
        effects[2]["lineage"]["realization_succession"] = "CARRY"
    elif mutation == "wrong_lineage":
        effects[2]["lineage"]["predecessor_id"] = "UNRELATED"
    elif mutation == "false_authority_disabled":
        effects[3]["standing_check"] = "DISABLED"
    elif mutation == "future_evidence_carry":
        changed["currentness"]["on_future_qualified_activation"]["evidence_carryover_allowed"] = True
    elif mutation == "no_observable_execution_required":
        effects[1]["completion_contract"]["exact_source_revision_and_executed_evidence_required"] = False
    with pytest.raises(ValueError, match="EFFECT_OR_OPEN_RESET"):
        j3.evaluate_snapshot(changed, admitted, execution)


@pytest.mark.parametrize("key,value", [
    ("status", "SOURCE_AUTHOR_FULL_DECLARED"),
    ("accepted_effect_id", j3.E01),
    ("source_event_commit", j2.CLAIM_COMMIT),
    ("declaration_commit", j2.EVENT),
    ("realizer_id", "HISTORICAL_G013_CODE_OWNER"),
    ("assurance_class", "INDEPENDENT_MODEL_ATTESTED"),
    ("qualified_experimental_relational_j2_count", 0),
    ("all_component_evidence_replayed", False),
    ("one_fact_tuple_in_bounded_source_world", False),
    ("previous_s0_execution_credited_to_s1", True),
    ("prior_948_j2_upgraded", True),
    ("independent_model_identity_proven", True),
    ("production_j2_qualified", True),
    ("s1_activated_by_this_j2_verifier", True),
    ("j3_satisfied_by_this_j2_verifier", True),
    ("formal_r0_p03_scored", True),
])
def test_separately_admitted_j2_cannot_be_forged_or_backdated(inputs, key, value):
    world, admitted, execution = inputs
    changed = deepcopy(admitted)
    changed[key] = value
    with pytest.raises(ValueError, match="J2_NOT_SEPARATELY_QUALIFIED"):
        j3.evaluate_snapshot(world, changed, execution)


def test_injected_source_claim_as_j2_field_is_not_accepted(inputs):
    world, admitted, execution = inputs
    changed = deepcopy(admitted)
    changed["author_declares_j3_complete"] = True
    with pytest.raises(ValueError, match="J2_UNRECOGNIZED"):
        j3.evaluate_snapshot(world, changed, execution)


@pytest.mark.parametrize("key,value", [
    ("source_event_commit", "faf8ff2686c6b09f53d3569470cf2057c11e5971"),
    ("freeze_commit", j2.CLAIM_COMMIT),
    ("after_sha256", "a" * 64),
])
def test_real_source_event_identity_is_strict(inputs, key, value):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed["event"][key] = value
    with pytest.raises(ValueError, match="SOURCE_EXECUTION_EVENT"):
        j3.evaluate_snapshot(world, admitted, changed)


@pytest.mark.parametrize("key,value", [
    ("source_author_independently_authenticated", True),
    ("postexecution_covers_admitted", True),
    ("qualified_relational_j2", True),
    ("s1_activated", True),
    ("j3", j3.J3_PASS),
    ("production_modified", True),
    ("physical_architecture_selected", True),
    ("formal_R0_P03", "COMPLETE"),
    ("status", "CERTIFIED_J3_BY_SOURCE_AUTHOR"),
])
def test_authorial_execution_output_cannot_certify_j3(inputs, key, value):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed[key] = value
    with pytest.raises(ValueError, match="SOURCE_EXECUTION_EVENT"):
        j3.evaluate_snapshot(world, admitted, changed)


def test_added_generated_navigation_authority_field_is_rejected(inputs):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed["generated_index_governs_j1"] = True
    with pytest.raises(ValueError, match="EXECUTION_UNRECOGNIZED"):
        j3.evaluate_snapshot(world, admitted, changed)


@pytest.mark.parametrize("position", range(16))
def test_all_s1_evidence_combinations_apply_all_required(inputs, position):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    flips = [
        lambda ex: ex["g006"].__setitem__("identity_preserved", False),
        lambda ex: ex["g013"].__setitem__("affected_view", "unaffected"),
        lambda ex: ex["g013"].__setitem__("selected_equals_full", False),
        lambda ex: ex["g013"].__setitem__("current_manifest", "STALE"),
    ]
    for bit, change in enumerate(flips):
        if position & (1 << bit):
            change(changed)
    value = j3.evaluate_snapshot(world, admitted, changed)
    if position == 0:
        assert value["s1_j3"] == j3.J3_PASS
        assert value["s1_component_count"] == 4
        assert value["initial_successor_component_credit"] == 0
    elif position & 1:
        assert value["activation_status"] == "HOLD_SOURCE_REVISION_IDENTITY_UNQUALIFIED"
        assert value["current_effect_ids"] == [j3.E01, j3.E04]
        assert value["s1_j3"] == "NOT_ACTIVATED"
    else:
        assert value["activation_status"] == j3.CURRENTNESS_STATUS
        assert value["current_effect_ids"] == [j3.E02, j3.E04]
        assert value["s1_j3"] == j3.J3_HOLD
        assert value["previous_s0_evidence_carried"] is False


@pytest.mark.parametrize("field", [
    "selected_equals_full", "affected_view", "current_manifest",
    "previous_manifest", "generated_current_view_sha256",
])
def test_missing_required_component_evidence_becomes_hold(inputs, field):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed["g013"].pop(field)
    result = j3.evaluate_snapshot(world, admitted, changed)
    assert result["activation_status"] == j3.CURRENTNESS_STATUS
    assert result["s1_j3"] == j3.J3_HOLD
    assert result["s1_j3_satisfied"] is False


def test_wrong_digest_metadata_is_not_completion_evidence(inputs):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed["g013"]["generated_current_view_sha256"] = "arbitrary"
    assert j3.evaluate_snapshot(world, admitted, changed)["s1_j3"] == j3.J3_HOLD


def test_prior_s0_evidence_cannot_fill_missing_s1_component(inputs):
    world, admitted, execution = inputs
    changed = deepcopy(execution)
    changed["g013"]["selected_equals_full"] = False
    changed["g006"]["historical_carriers"] = [realizer.BEFORE, realizer.AFTER]
    result = j3.evaluate_snapshot(world, admitted, changed)
    assert result["s1_open_reset"] is True
    assert result["initial_successor_component_credit"] == 0
    assert result["s1_components"]["INCREMENTAL_EQUALS_CURRENT_FULL_BUILD"] is False
    assert result["s1_j3"] == j3.J3_HOLD


def test_immutable_separate_j3_receipt_matches_replay(output):
    assert json.loads(j3.OUTPUT.read_text("utf8")) == output
