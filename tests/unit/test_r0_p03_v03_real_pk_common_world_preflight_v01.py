"""One original-source common semantics contract shared by all future navigation arms.

This is an engineering preflight; tests neither originate navigation tasks
nor construct model-specific ranking metadata or reference answers.
"""
from __future__ import annotations

from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_common_world_preflight_v01 as common,
)


@pytest.fixture(scope="module")
def world():
    return common.build()


def test_common_world_is_one_source_frame_not_a_scored_arm(world):
    assert world["world_id"] == common.j1.EXPERIMENT_ID
    assert world["world_status"] == "ONE_REAL_SOURCE_COMMON_SEMANTIC_PREFLIGHT_J2_J3_HOLD_NOT_FROZEN"
    assert world["scope"] == "R0_P03_V2_REAL_PROJECT_KNOWLEDGE_SOURCE_WORLD_EXPERIMENT_ONLY"


def test_all_19_original_pinned_sources_in_same_manifest(world):
    frame = world["original_project_source_catalog"]
    assert frame["source_pin"] == common.original.PIN
    assert frame["distinct_original_git_paths"] == 19
    paths = [x["source_path"] for x in frame["sources"]]
    assert len(paths) == len(set(paths)) == 19
    assert all(r["exact_source_commit"] == common.original.PIN for r in frame["sources"])
    assert all(len(r["sha256"]) == 64 and len(r["git_blob_oid"]) == 40
               for r in frame["sources"])


def test_original_d035_d036_share_source_no_duplicate_natural_owner(world):
    matching = [s for s in world["original_project_source_catalog"]["sources"]
                if s["source_path"] == "docs/DECISIONS.md"]
    assert len(matching) == 1
    assert "HISTORICAL_SELECTED_DECISION_REPORTED" in matching[0]["source_roles"]


def test_all_arms_receive_identical_mandatory_semantic_fields(world):
    common_inputs = world["shared_arm_input"]
    assert common_inputs["identical_mandatory_information_for_B0_B1_B2_B3_B4"] is True
    assert common_inputs["no_arm_specific_index_authority"] is True
    assert common_inputs["arm_implementations_frozen"] is False
    assert "J2_OBSERVABLE_RELATIONAL_EPHEMERAL_ASSURANCE" in common_inputs["common_semantics"]


def test_four_accepted_experiment_effects_are_not_hist_g006_gate(world):
    effects = world["accepted_j1"]["accepted_effects"]
    assert len(effects) == 4
    assert [e["id"] for e in effects] == list(common.j1.EXPECTED_IDS)
    assert world["accepted_j1"]["original_review_commit"] == common.j1.PROPOSAL_COMMIT


def test_current_s0_and_dormant_s1_lineage_are_distinct(world):
    assert world["accepted_lineage_currentness"]["active_state"] == "S0_INITIAL"
    assert world["accepted_lineage_currentness"]["S1_activation"] == "NOT_ACTIVATED"
    assert world["accepted_lineage_currentness"]["successor_realization_evidence_carryover"] == "FORBIDDEN_BY_OPEN_RESET"


def test_actual_source_move_preserves_current_and_history(world):
    assert world["semantic_identity"]["authored_id"] == common.movement.AUTHORED_ID
    assert world["semantic_identity"]["current_source"] == common.movement.REPLACEMENT_PATH
    assert world["semantic_identity"]["historical_sources"] == sorted(
        [common.movement.INITIAL_PATH, common.movement.REPLACEMENT_PATH]
    )
    assert world["semantic_identity"]["continuity_observed_by_g006"] is True


def test_git_source_revision_replay_is_exact_and_versioned(world):
    s = world["source_versions"]
    assert s["initial_git_commit"] == common.movement.INITIAL_COMMIT
    assert s["replacement_git_commit"] == common.movement.REPLACEMENT_COMMIT
    assert s["original_source_sha256"] == common.movement.INITIAL_SHA256
    assert s["current_source_sha256"] == common.movement.REPLACEMENT_SHA256
    assert s["git_paths_exact_verified"] is True


def test_actual_git_source_observation_not_turned_into_j2_completion(world):
    assert world["j2"]["observable"]["git_source_history_verified"] is True
    assert world["j2"]["observable"]["identity_continuity_and_history_executed_in_g006"] is True
    assert len(world["j2"]["source_local_relational_candidates_not_admitted"]) == 1
    assert world["j2"]["qualified_relational"] == []
    assert world["j2"]["qualified_relational_count"] == 0


def test_j3_and_formal_stay_open_before_owner_relational_qualification(world):
    assert world["j3"]["S0"] == "HOLD_UNQUALIFIED_SOURCE_OWNER_RELATION"
    assert world["j3"]["S1"] == "NOT_ACTIVATED"
    assert world["j3"]["completion_certified"] is False
    assert world["formality"]["formal_B0_B4_scores"] is None
    assert world["formality"]["physical_target_selected"] is False


def test_no_premature_source_or_arm_freeze(world):
    assert world["formality"]["sixty_build_twenty_heldout_or_fallback_frozen"] is False
    assert world["formality"]["twelve_independent_primary_tasks_originated"] is False
    assert world["formality"]["blinded_evaluators_assigned"] is False
    assert world["formality"]["nine_neutral_legacy_reference_gold_frozen_under_current_method"] is False


def test_remaining_requirements_are_concrete_and_finite(world):
    missing = world["remaining_qualification"]
    assert len(missing) == 6
    assert "SOURCE_OWNER_RELATIONAL" in missing[0]
    assert "G013" in missing[1]
    assert "J3" in missing[2]
    assert "B0_B4" in missing[4]
    assert "INDEPENDENT_TWELVE_PRIMARY" in missing[5]


def test_common_frame_matches_exact_source_regeneration(world):
    from experiments.r0_p03_navigation_probe import (
        v03_real_pk_semantic_candidate_audit_v01 as audit,
    )
    assert sha256(audit.OUTPUT.read_bytes()).hexdigest() == common.AUDIT_SHA256
    assert world["original_project_source_catalog"]["distinct_original_git_paths"] == (
        audit.evaluate()["combined_unique_source_paths"]
    )


def test_published_common_world_is_immutable_derived_output(world):
    assert json.loads(common.OUTPUT.read_text("utf8")) == world
