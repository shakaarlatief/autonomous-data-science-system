"""Source-qualified R0-P03-V2 semantic-world candidate tests.

This suite tests real original-Git content and source-role boundaries. It
neither authors independent gold nor accepts new J1 effects or J2 relations.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_semantic_candidate_audit_v01 as candidate,
)


@pytest.fixture(scope="module")
def record():
    return candidate.evaluate()


def test_real_original_source_frame_reused_not_replaced(record):
    assert record["original_git_source_pin"] == candidate.PIN
    assert record["scientific_method"] == "RESEARCH673_M1_M6_OWNER_ACCEPTED"
    assert record["original_preexisting_source_frame"] == {
        "distinct_paths": 15, "witness_count": 16, "source_role_count": 10,
    }


def test_single_candidate_has_actual_expanded_real_git_source_set(record):
    assert record["world_candidate"] == candidate.CANDIDATE_ID
    assert record["candidate_distinct_paths"] == 10
    assert record["combined_unique_source_paths"] == 19
    assert record["additional_candidate_witness_count"] == 12
    assert len(record["new_source_paths_not_in_original_fifteen"]) == 4
    assert "tools/project_knowledge/services/refresh.py" in record["new_source_paths_not_in_original_fifteen"]
    assert "tests/unit/test_project_knowledge_refresh.py" in record["new_source_paths_not_in_original_fifteen"]


def test_original_g006_and_g013_git_implementation_events_are_real_ancestors(record):
    original = record["original_git_implementation_events"]
    assert set(original) == {"G006", "G013"}
    assert original["G006"]["commit"] == candidate.G006
    assert original["G013"]["commit"] == candidate.G013
    assert original["G006"]["parent"] == candidate.G006_PARENT
    assert original["G013"]["parent"] == candidate.G013_PARENT
    for e in original.values():
        assert e["required_path_subset_verified"] is True
        assert e["is_ancestor_of_original_source_pin"] is True
        assert e["proves_historical_p03_j1_or_j2"] is False


def test_original_identity_change_set_contains_actual_code_and_test(record):
    assert candidate.REQUIRED_G006_PATHS.issubset(
        record["original_git_implementation_events"]["G006"]["changed_paths"]
    )


def test_original_refresh_change_set_contains_actual_code_test_and_view(record):
    assert candidate.REQUIRED_G013_PATHS.issubset(
        record["original_git_implementation_events"]["G013"]["changed_paths"]
    )


def test_witnesses_have_unique_source_ids_and_source_path_revision(record):
    rows = record["additional_candidate_witnesses"]
    assert len({r["witness_id"] for r in rows}) == len(rows)
    assert all(r["source_commit"] == candidate.PIN for r in rows)
    assert all(len(r["original_sha256"]) == 64 for r in rows)
    assert all(len(r["original_git_blob"]) == 40 for r in rows)
    assert all(r["line_1based"] >= 1 and r["original_byte_count"] > 0 for r in rows)
    assert all(r["authority"] == "VERIFIED_SOURCE_CONTENT_NOT_NEW_EXPERIMENT_J1_OR_J2" for r in rows)


@pytest.mark.parametrize("row", candidate.WITNESSES)
def test_each_original_witness_verified_at_exact_git_source(row, record):
    r = candidate.witness(row)
    assert r in record["additional_candidate_witnesses"]
    original = candidate._git_bytes("show", f"{candidate.PIN}:{row[1]}")
    assert sha256(original).hexdigest() == r["original_sha256"]
    lines = original.decode("utf8").splitlines()
    assert row[3] in lines[r["line_1based"] - 1]
    assert sum(row[3] in line for line in lines) == 1


def test_historical_gate_records_are_not_new_j1_decisions(record):
    gate = [r for r in record["additional_candidate_witnesses"]
            if r["source_role"] == "HISTORICAL_GATE_ACCEPTANCE_REPORTED_NOT_P03_J1"]
    assert {r["witness_id"] for r in gate} == {"G006_DECISION_RECORD", "G013_DECISION_RECORD"}
    assert record["new_experiment_only_j1_effects_accepted"] == 0


def test_code_source_and_test_definition_roles_are_distinct(record):
    roles = {
        r["witness_id"]: r["source_role"]
        for r in record["additional_candidate_witnesses"]
    }
    assert roles["G006_IMPLEMENTATION"] == "NATURAL_CODE_SOURCE"
    assert roles["G013_REFRESH_IMPLEMENTATION"] == "NATURAL_CODE_SOURCE"
    assert roles["G006_MOVE_TEST"] == "TEST_DEFINITION_NOT_EXECUTION"
    assert roles["G013_CROSS_SEMANTIC_TEST"] == "TEST_DEFINITION_NOT_EXECUTION"


def test_git_chronology_is_not_historical_effect_supersession(record):
    assert record["source_qualification"][
        "historical_git_commits_form_chronology_not_j1_effect_supersession"
    ] is True


def test_g006_and_g013_actual_semantic_research_makes_coherent_candidate(record):
    q = record["source_qualification"]
    assert q["g006_identity_move_supersede_and_history"] == "GIT_CODE_AND_TEST_DEFINITIONS_PRESENT"
    assert q["g013_refresh_and_rebuild_equivalence"] == "GIT_CODE_AND_TEST_DEFINITIONS_PRESENT"
    assert q["cross_semantic_move_refresh_test"] == "GIT_TEST_DEFINITION_PRESENT_NOT_EXECUTION"
    assert q["w5_subject_comparator"] == "ORIGINAL_HISTORICAL_W5_SOURCE_PRESENT"


def test_previously_accepted_d1_kept_as_negative_not_main_world(record):
    comparison = record["candidate_comparison"]
    assert comparison["D1_HISTORICAL_ONLY"]["experiment_only_j1_accepted"] == 4
    assert comparison["D1_HISTORICAL_ONLY"]["qualified_j2_relational"] == 0
    assert comparison["D1_HISTORICAL_ONLY"]["role"] == "RETAIN_AS_BOUNDED_UNKNOWN_NEGATIVE_CASE"


def test_ci_history_not_promoted_to_primary_navigation_world(record):
    assert record["candidate_comparison"]["GITHUB_CI_RECEIPT_CHAIN"][
        "enough_identity_lineage_and_semantic_breadth_alone"
    ] is False


def test_preferred_candidate_does_not_mean_qualified_world(record):
    c = record["candidate_comparison"]["G006_G013_PROJECT_KNOWLEDGE"]
    assert c["role"] == "PREFERRED_SOURCE_CANDIDATE_NOT_YET_FORMAL_WORLD"
    assert c["new_owner_experiment_j1_accepted"] is False
    assert c["natural_owner_j2_covers_qualified"] is False


def test_no_owner_acceptance_or_j2_signed_by_inference(record):
    assert record["new_experiment_only_j1_effects_accepted"] == 0
    assert record["existing_d1_experiment_only_j1_effects"] == 4
    assert record["new_qualified_j2_relations"] == 0
    assert record["integrated_j3_completion"] == "NOT_RUN_HOLD_MISSING_ADMISSIONS"


def test_no_scoring_task_source_frozen_or_physical_target_selected(record):
    assert record["frozen_formal_world"] is False
    assert record["formal_b0_b4_scores"] is None
    assert record["twelve_primary_tasks_originated"] is False
    assert record["physical_target_selected"] is False


def test_followon_boundaries_include_owner_realizer_and_independent_gold(record):
    required = record["next_required_substantive_steps"]
    assert len(required) == 6
    assert "owner packet" in required[1]
    assert "J2 COVERS" in required[2]
    assert "J3" in required[3]
    assert "B0-B4" in required[4]
    assert "twelve-primary" in required[5]


@pytest.mark.parametrize("wrong_row", [
    ("F", "docs/wrong.md", "SOURCE", "some function"),
    ("G006_IMPLEMENTATION", "docs/wrong.md", "NATURAL_CODE_SOURCE", "def build_identity_index("),
    ("G006_IMPLEMENTATION", "tools/project_knowledge/identity.py", "GOVERNING_J1", "def build_identity_index("),
])
def test_unapproved_source_witness_or_role_rejected(wrong_row):
    with pytest.raises(ValueError, match="CANDIDATE_UNAUTHORIZED_SOURCE_WITNESS"):
        candidate.witness(wrong_row)


def test_wrong_git_source_pin_rejected():
    with pytest.raises(ValueError, match="CANDIDATE_SOURCE_PIN_NOT_APPROVED"):
        candidate.witness(candidate.WITNESSES[0], pin="0" * 40)


def test_missing_exact_original_anchor_fails_closed(monkeypatch):
    row = candidate.WITNESSES[0]
    def missing_anchor(*args):
        if args[0] == "show" and args[1] == f"{candidate.PIN}:{row[1]}":
            return b"unchanged code with no target anchor\n"
        return candidate._git_bytes(*args)
    monkeypatch.setattr(candidate, "_git_bytes", missing_anchor)
    with pytest.raises(ValueError, match="CANDIDATE_ORIGINAL_ANCHOR_NOT_UNIQUE"):
        candidate.witness(row)


def test_false_git_parent_claim_fails_closed():
    with pytest.raises(ValueError, match="CANDIDATE_ORIGINAL_PARENT_CHANGED"):
        candidate.commit_facts(candidate.G006, "0" * 40, candidate.REQUIRED_G006_PATHS)


def test_absent_implementation_path_fails_closed():
    with pytest.raises(ValueError, match="CANDIDATE_ORIGINAL_IMPLEMENTATION_PATHS_ABSENT"):
        candidate.commit_facts(candidate.G013, candidate.G013_PARENT, {"wrong/unrelated/path.py"})


def test_wrong_source_commit_cannot_pass_as_historical_event():
    with pytest.raises(ValueError, match="CANDIDATE_ORIGINAL_PARENT_CHANGED"):
        candidate.commit_facts(candidate.G013_PARENT, candidate.G013_PARENT, candidate.REQUIRED_G013_PATHS)


def test_new_accepted_j1_drift_in_source_frame_rejected(monkeypatch):
    actual = candidate.original_j1.build_accepted_projection()
    forged = deepcopy(actual)
    forged["accepted_j1"]["effects"].append(deepcopy(forged["accepted_j1"]["effects"][0]))
    monkeypatch.setattr(candidate.original_j1, "build_accepted_projection", lambda: forged)
    with pytest.raises(ValueError, match="HISTORICAL_ACCEPTED_EXPERIMENT_SCOPE_DRIFT"):
        candidate.evaluate()


def test_source_only_qualification_not_navigation_selection(record):
    assert record["status"] == "SOURCE_VERIFIED_CANDIDATE_ONLY_NOT_A_QUALIFIED_V03_WORLD"


def test_immutable_result_matches_recomputed_real_source_evidence(record):
    assert json.loads(candidate.OUTPUT.read_text("utf8")) == record
