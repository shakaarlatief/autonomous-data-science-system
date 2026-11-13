"""Exact original Git and sealed reviewer-message integrity for R0-P03 audits.

This is a retrospective evidence aggregation after all three Claude reviews
completed independently of the unmasking script. The tests never promote a
source quotation or Claude grade to independent reference gold, governing
authority, or the original Research 513 formal architecture selection.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.route_b_three_claude_masked_review_consolidation_v01 import (
    ARMS, CLAIM_GRADES, GRADES, ORIGINAL_ANSWERS, OUTPUT, PACKET_AND_REVIEW, PIN,
    REVIEW_DIR, ROOT, SOURCE_PACKET, frozen_bytes, parse_review, run,
)

SIZE = 28645
DIGEST = "8a59c63e4fab9e0a86afb7d0b3d3b7e9fc6dc5bbf9539fef228ba97ca0753f69"


def saved() -> dict:
    blob = OUTPUT.read_bytes()
    assert len(blob) == SIZE
    assert sha256(blob).hexdigest() == DIGEST
    assert blob.endswith(b"\n") and b"\r\n" not in blob
    return json.loads(blob)


def test_prior_reviewers_and_packet_bytes_exact_and_separately_frozen() -> None:
    for p,size,digest,r,rsize,rdigest in PACKET_AND_REVIEW:
        packet = frozen_bytes(ROOT/p,size,digest)
        review = frozen_bytes(REVIEW_DIR/r,rsize,rdigest)
        assert len(packet) == size
        assert len(review) == rsize
        parsed=parse_review(review)
        assert len(parsed) == 8
    for name,size,sha in (SOURCE_PACKET,ORIGINAL_ANSWERS):
        assert len(frozen_bytes(ROOT/name,size,sha)) == size


def test_review_case_ids_claim_ids_and_grade_sum_original_without_rewrites() -> None:
    d=saved()
    records=d["complete_per_question_unmasked_after_reviewer_submission"]
    assert len(records)==24
    assert [c["question_id"] for c in records]==[
        f"P{i:02d}" for i in range(1,13) for _ in ARMS
    ]
    assert sorted({(c["question_id"],c["original_method_revealed_after_all_three_reviews"])
                   for c in records})==sorted((f"P{i:02d}",arm) for i in range(1,13) for arm in ARMS)
    for case in records:
        assert case["independent_model_excerpt_entailment_grade"] in GRADES
        assert case["original_method_revealed_after_all_three_reviews"] in ARMS
        assert case["not_independent_answer_gold"] is True
        assert case["current_operative_authority_test_outcome"]=="NO_FALSE_ASSERTIONS_REPORTED_BY_CLAUDE"
        assert all(v["verdict"] in CLAIM_GRADES for v in case["claim_verdicts"])
    assert sum(len(c["claim_verdicts"]) for c in records)==47


def test_all_360_cited_source_lines_original_git_verified_by_end_to_end_replay() -> None:
    d=saved()
    assert d["source_git_horizon"]==PIN
    assert d["original_git_exact_source_lines_verified_with_multiplicity"]==360
    assert d["original_git_source_paths_verified"]>=12
    assert run()==d


def test_reviewers_report_full_evidence_and_proper_abstentions_without_inflating() -> None:
    d=saved()
    all_result=d["counts"]["all"]
    assert all_result["whole_answer_grade_counts"]=={
        "FULLY_SUPPORTED":20,"PARTIALLY_SUPPORTED":2,
        "PROPER_ABSTENTION":2,"MISLEADING_OR_UNSUPPORTED":0
    }
    assert all_result["claim_verdict_counts"]=={
        "SUPPORTED":45,"PARTIAL":2,"UNSUPPORTED":0
    }
    assert all_result["answers"]==24
    b0=d["counts"]["B0_ORIGINAL"]
    b1=d["counts"]["B1_EXPOSED_SUBJECT_B0"]
    assert b0["whole_answer_grade_counts"]=={
        "FULLY_SUPPORTED":10,"PARTIALLY_SUPPORTED":0,
        "PROPER_ABSTENTION":2,"MISLEADING_OR_UNSUPPORTED":0
    }
    assert b1["whole_answer_grade_counts"]=={
        "FULLY_SUPPORTED":10,"PARTIALLY_SUPPORTED":2,
        "PROPER_ABSTENTION":0,"MISLEADING_OR_UNSUPPORTED":0
    }
    assert b0["claim_verdict_counts"]=={"SUPPORTED":23,"PARTIAL":0,"UNSUPPORTED":0}
    assert b1["claim_verdict_counts"]=={"SUPPORTED":22,"PARTIAL":2,"UNSUPPORTED":0}


def test_P01_P02_P03_P11_original_source_boundaries_survive_unmasking() -> None:
    data=saved()
    case={(r["question_id"],r["original_method_revealed_after_all_three_reviews"]):r
          for r in data["complete_per_question_unmasked_after_reviewer_submission"]}
    assert case["P01","B0_ORIGINAL"]["independent_model_excerpt_entailment_grade"]=="PROPER_ABSTENTION"
    assert case["P01","B1_EXPOSED_SUBJECT_B0"]["independent_model_excerpt_entailment_grade"]=="FULLY_SUPPORTED"
    assert case["P02","B1_EXPOSED_SUBJECT_B0"]["independent_model_excerpt_entailment_grade"]=="FULLY_SUPPORTED"
    assert [x["verdict"] for x in case["P02","B1_EXPOSED_SUBJECT_B0"]["claim_verdicts"]]==["SUPPORTED","PARTIAL"]
    assert case["P03","B0_ORIGINAL"]["independent_model_excerpt_entailment_grade"]=="PROPER_ABSTENTION"
    assert case["P03","B1_EXPOSED_SUBJECT_B0"]["independent_model_excerpt_entailment_grade"]=="PARTIALLY_SUPPORTED"
    assert case["P11","B1_EXPOSED_SUBJECT_B0"]["independent_model_excerpt_entailment_grade"]=="PARTIALLY_SUPPORTED"
    assert case["P11","B0_ORIGINAL"]["independent_model_excerpt_entailment_grade"]=="FULLY_SUPPORTED"


def test_scientific_independence_authority_and_formal_decision_gates_not_claimed() -> None:
    d=saved()
    assert d["source_authorship_independent"] is False
    assert d["source_excerpt_judgments_separate_model"] is True
    assert d["reviewer_fresh_sessions_reported"]==3
    assert d["different_reviewer_model_families"]==1
    assert d["reviewer_has_full_original_source"] is False
    assert d["independently_authored_reference_gold"] is False
    assert d["formal_original_R0_P03_scored"] is False
    assert d["selected_physical_architecture"] is False
    limits = "\n".join(d["interpretation_limits"]).lower()
    assert "not a full" not in limits or "not" in limits
    assert "independent reference" in limits
    assert "r0-p03" in limits and "incomplete" in limits
