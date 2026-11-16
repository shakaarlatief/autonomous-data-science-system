"""Post-freeze W1 C_arm regression proof; not formal task scoring or gold."""
from __future__ import annotations

from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    w1_c_arm_postfreeze_mechanism_v01 as run,
    w1_primary_c_arm_v01 as arm,
)


@pytest.fixture(scope="module")
def frozen():
    return run.verify_freeze()


@pytest.fixture(scope="module")
def receipt():
    return json.loads(run.OUTPUT.read_text("utf8"))


def test_pre_task_frozen_versions(frozen):
    assert frozen["classification"]==(
        "C_ARM_W1_PRIMARY_B0_B3_SOURCE_AND_IMPL_FREEZE_BEFORE_INDEPENDENT_PRIMARY_TASKS"
    )
    assert frozen["freeze_source_implementation_commit"]==(
        "b987b1837f38479c3ccd34410de4ef52ab4c1edd"
    )
    assert frozen["preregistered_w1_rule_commit"]==arm.w1.RULE_COMMIT
    assert frozen["all_b0_b3_versions_frozen_before_task_origination"]
    assert len(frozen["w1_primary_arm_implementation_git_objects"])==7


def test_original_source_hashes_are_frozen(frozen):
    for entry in frozen["w1_primary_arm_implementation_git_objects"].values():
        raw=run._git("show",f'{entry["git_source_commit"]}:{entry["path"]}')
        assert len(raw)==entry["bytes"]
        assert sha256(raw).hexdigest()==entry["sha256"]
        assert run._git(
            "rev-parse",f'{entry["git_source_commit"]}:{entry["path"]}'
        ).decode().strip()==entry["git_blob_oid"]


def test_b4_omission_prospective_before_scoring(frozen,receipt):
    assert frozen["b4_omitted_prospectively_at_fixture_freeze"] is True
    assert frozen["treatment_specification"]["b4"]["policy"]==(
        "B4_OMITTED_PROSPECTIVELY_AT_W1_PRIMARY_C_ARM_FREEZE"
    )
    assert receipt["neural_b4"]=="PROSPECTIVELY_OMITTED_AT_PRIMARY_C_ARM_FREEZE"
    assert frozen["treatment_specification"]["b4"][
        "no_comparative_embedding_score_was_observed"
    ] is True


def test_fixed_equal_context_budget(frozen,receipt):
    b=frozen["per_task_context_pack"]
    assert b["top_source_count"]==6
    assert b["original_source_excerpt_max_chars_per_candidate"]==2800
    assert b["max_original_source_excerpt_chars_total"]==16800
    assert b["after_context_pack_fresh_answerer_extra_tool_reads"]==0
    assert b["answerer_direct_repo_or_web_connectors"]=="DISABLED"
    assert receipt["context_cap"]["source_candidates_per_query"]==6


def test_actual_60_source_8_probe_execution_not_formal_scoring(receipt):
    assert receipt["classification"]==(
        "W1_FROZEN_PRIMARY_B0_B3_REAL_EXECUTION_EXPOSED_UNSCORED"
    )
    assert receipt["exposed_probe_count"]==8
    assert receipt["source_count"]==60
    assert receipt["original_source_git_ref"]==arm.w1.PIN
    assert receipt["independent_primary_task_authorship"]=="NOT_STARTED"
    assert receipt["legacy_65_source_arm_work"]==(
        "NOT_STARTED_BEFORE_INDEPENDENT_NEUTRAL_NINE"
    )
    assert receipt["heldout_paths"]=="NOT_DRAWN"
    assert receipt["protected_reference"]=="NONE"
    assert receipt["research513_primary_or_legacy_pass_counts"]=="NONE"
    assert receipt["research673_m6_formal_attempt_used"] is False


def test_changed_rankings_not_accuracy(receipt):
    assert receipt["orders_different_from_b0_not_quality_score"]=={
        "B0":0,"B1":5,"B2":6,"B3":4
    }
    for q in receipt["exposed_diagnostic_order_by_arm"]:
        assert q["not_relevance_or_quality_scored"] is True
        assert len(q["candidate_order_by_arm"])==4
        assert all(len(x)==6 for x in q["candidate_order_by_arm"].values())
        assert all(0<=v<=16800 for v in
                   q["source_context_characters_by_arm"].values())


def test_actual_individual_arm_mechanisms_executed(receipt):
    operations=receipt["per_arm_method_operation_counts"]
    assert all(v["lexical_rank"]==8 and v["context_pack"]==8
               for v in operations.values())
    assert operations["B0"].get("subject_rank",0)==0
    assert operations["B0"].get("editorial_rank",0)==0
    assert operations["B0"].get("concern_rank",0)==0
    assert operations["B1"]["subject_rank"]==8
    assert operations["B2"]["editorial_rank"]==8
    assert operations["B3"]["concern_rank"]==8
    smoke=receipt["mechanism_browse_smoke_counts"]
    assert smoke["source_to_governing_editorial_links"]==23
    assert smoke["example_editorial_browse_count"]>0
    assert smoke["example_concern_browse_count"]>0
    assert smoke["subject_parent_browse_count"]>0


def test_prior_author_exposure_not_gold_or_natural_owner(frozen):
    a=frozen["authored_metadata_exposure"]
    assert a["author"]=="EXPOSED_CHATGPT_COORDINATOR"
    assert a["natural_owner_j2_attested"] is False
    assert a["independent_annotation_reliability"]=="NOT_MEASURED"
    assert a["curated_research217_memberships"]==120
    assert a["preferred_routes"]==60
    assert a["additional_source_to_governing_about_links"]==23
    assert a["cross_cutting_concern_assignments"]==115
    assert a["cross_cutting_concern_definitions"]==5


def test_no_tasks_hidden_gold_legacy_scoring_or_heldout(frozen):
    assert all(v is False for v in frozen["excluded_formal_operations"].values())


def test_create_only_receipt_recomputes_without_tuning(receipt):
    actual=run.OUTPUT.read_bytes()
    assert sha256(actual).hexdigest()==(
        "97403f0859b68ce1028944271014c7b0b6e963ccd9ac5d651cd4298e9623652c"
    )
    assert json.loads(actual)==receipt
    assert arm.canonical(run.diagnostic())==actual
