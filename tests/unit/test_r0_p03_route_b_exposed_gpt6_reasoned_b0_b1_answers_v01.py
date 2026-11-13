"""Verifiable citation integrity for exposed GPT-6 source-limited prose answers.

This module verifies source and line witnesses and retrospective model
self-assessments, never asserts independent correctness of natural-language
entailment, complete governing status or formal R0-P03 architecture fitness.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    original_contents,
)
from experiments.r0_p03_navigation_probe.route_b_reasoned_b0_b1_source_packet_export_v01 import (
    METHODS, PRIOR_SHA256, ROOT, packet,
)

PACKET = ROOT / "route_b_reasoned_b0_b1_gold_free_source_packet_v01.json"
ANSWERS = ROOT / "route_b_reasoned_b0_b1_gpt6_exposed_answers_v01.json"
P_SIZE = 155794
P_SHA = "60ec37969aa3319ce195353a6f9cddb2103640b0e4f748564e0be4a4d839b508"
A_SIZE = 56283
A_SHA = "5e8848f444fee4234fe885d9350e872393ac20f24a043c2347e615dafccdc388"


def load_original() -> tuple[dict, dict]:
    raw_packet = PACKET.read_bytes()
    raw_answers = ANSWERS.read_bytes()
    assert len(raw_packet) == P_SIZE and sha256(raw_packet).hexdigest() == P_SHA
    assert len(raw_answers) == A_SIZE and sha256(raw_answers).hexdigest() == A_SHA
    assert raw_packet.endswith(b"\n") and b"\r\n" not in raw_packet
    assert raw_answers.endswith(b"\n") and b"\r\n" not in raw_answers
    return json.loads(raw_packet), json.loads(raw_answers)


def test_gold_free_export_is_exact_reproducible_original_source_bytes() -> None:
    reconstructed = packet()
    assert reconstructed["bytes"] == PACKET.read_bytes()
    p, a = load_original()
    assert p["source_quoted_parent_sha256"] == PRIOR_SHA256
    assert a["source_packet_sha256"] == P_SHA
    assert p["original_source_git_revision"] == a["original_source_git_pin"]


def test_export_has_only_source_question_and_lines_not_reference_gold() -> None:
    p, a = load_original()
    assert p["reference_answers_in_packet"] is False
    assert p["expected_reference_sources_in_packet"] is False
    assert p["answerer_has_prior_context_exposure"] is True
    raw = PACKET.read_text(encoding="utf8")
    forbidden = (
        "reference_answer_for_evaluation_only", "required_source_for_evaluation_only",
        "required_source_witness_lines", "source_evidence_status",
        "retrospective_reference_evidence_audit", "all_reference_excerpts_actually_cited",
    )
    assert all(term not in raw for term in forbidden)
    assert a["reference_answers_used_as_explicit_input"] is False
    assert a["model_has_prior_reference_exposure"] is True


def test_original_twelve_questions_all_have_exact_two_arm_contexts() -> None:
    p, a = load_original()
    questions = p["source_only_question_packets"]
    assert len(questions) == 12
    assert [q["id"] for q in questions] == [f"P{i:02}" for i in range(1, 13)]
    assert [x["id"] for x in a["paired_responses"]] == [
        q["id"] for q in questions for _ in METHODS
    ]
    assert len({(x["id"], x["arm"]) for x in a["paired_responses"]}) == 24
    assert len(a["paired_responses"]) == 24
    assert all([arm["arm"] for arm in question["arm_evidence"]] == list(METHODS)
               for question in questions)
    for row in questions:
        assert row["question"]
        for arm in row["arm_evidence"]:
            assert 1 <= len(arm["sources"]) <= 3
            for idx, source in enumerate(arm["sources"], 1):
                assert idx == source["source_rank"]
                assert len(source["original_cited_lines"]) <= 5


def test_twenty_four_answer_texts_are_actual_distinct_model_authored_prose() -> None:
    _, a = load_original()
    texts = [x["answer"] for x in a["paired_responses"]]
    assert len(texts) == 24
    assert len(set(texts)) == 24
    assert all(len(x) >= 100 and "\nSource " not in x for x in texts)
    assert all(x["claims"] and all(claim["statement"] and claim["citations"]
                                   for claim in x["claims"])
               for x in a["paired_responses"])
    assert a["model"] == "GPT-6 exposed coordinator, single authoring session"
    assert a["author_role"] == "EXPOSED_NOT_FRESH_NOT_BLIND_NOT_SCORED"


def test_all_exposed_answer_claim_citations_match_original_git_and_packet() -> None:
    p, a = load_original()
    cases = {case["id"]: case for case in p["source_only_question_packets"]}
    all_paths = sorted({
        source["path"] for case in cases.values()
        for arm in case["arm_evidence"] for source in arm["sources"]
    })
    source_bytes = original_contents(all_paths)
    assert set(source_bytes) == set(all_paths)
    inspected_citations = 0
    for row in a["paired_responses"]:
        case = cases[row["id"]]
        assert row["question"] == case["question"]
        arm = next(a for a in case["arm_evidence"] if a["arm"] == row["arm"])
        for claim in row["claims"]:
            for cited in claim["citations"]:
                rank = cited["source_rank"]
                assert 1 <= rank <= len(arm["sources"])
                source = arm["sources"][rank - 1]
                assert cited["path"] == source["path"]
                assert cited["original_source_sha256"] == source["sha256"]
                blob = source_bytes[source["path"]]
                assert sha256(blob).hexdigest() == cited["original_source_sha256"]
                real_lines = blob.decode("utf8").splitlines()
                cited_index = cited["line"]
                assert 1 <= cited_index <= len(real_lines)
                witness = next(
                    (l for l in source["original_cited_lines"] if l["line"] == cited_index),
                    None,
                )
                assert witness is not None
                assert real_lines[cited_index - 1] == witness["original_source_line"]
                assert cited["original_line_sha256"] == witness["original_line_sha256"]
                assert sha256(real_lines[cited_index - 1].encode("utf8")).hexdigest() == cited["original_line_sha256"]
                inspected_citations += 1
    assert inspected_citations >= 55


def test_every_answer_claim_uses_only_its_specific_arm_current_top_three() -> None:
    p, a = load_original()
    source_by_case = {q["id"]: q for q in p["source_only_question_packets"]}
    for response in a["paired_responses"]:
        row = source_by_case[response["id"]]
        arm = next(x for x in row["arm_evidence"] if x["arm"] == response["arm"])
        allowed = {(i, witness["line"])
                   for i, source in enumerate(arm["sources"], 1)
                   for witness in source["original_cited_lines"]}
        cited = {(q["source_rank"], q["line"])
                 for claim in response["claims"] for q in claim["citations"]}
        assert cited
        assert cited <= allowed
        assert response["coverage"] in {"SUPPORTED", "PARTIAL", "ABSTAIN"}


def test_P01_B0_abstains_and_B1_recovers_exact_historical_checkpoint_branch() -> None:
    _, a = load_original()
    b0, b1 = [r for r in a["paired_responses"] if r["id"] == "P01"]
    assert b0["coverage"] == "ABSTAIN"
    assert b1["coverage"] == "SUPPORTED"
    assert "Checkpoint 899" in b1["answer"]
    assert "v1-source-vault-bootstrap-resume" in b1["answer"]
    witness = {c["line"] for claim in b1["claims"]
               for c in claim["citations"] if c["path"] == "docs/CURRENT_STATE.md"}
    assert {3, 5} <= witness
    assert "present checkout" in b1["answer"]


def test_P02_P03_do_not_fill_missing_gold_from_previous_context() -> None:
    _, a = load_original()
    p02 = [r for r in a["paired_responses"] if r["id"] == "P02"]
    assert all(r["coverage"] == "PARTIAL" for r in p02)
    assert all("project-wide" in r["answer"] for r in p02)
    p03 = {r["arm"]: r for r in a["paired_responses"] if r["id"] == "P03"}
    assert p03["B0_ORIGINAL"]["coverage"] == "ABSTAIN"
    assert p03["B1_EXPOSED_SUBJECT_B0"]["coverage"] == "PARTIAL"
    assert "cannot" in p03["B1_EXPOSED_SUBJECT_B0"]["answer"]
    assert all("FROZEN / IMPLEMENTATION PENDING" not in r["answer"]
               for r in p03.values())


def test_P09_P10_answered_historical_candidate_and_later_supersession_separately() -> None:
    _, a = load_original()
    p09 = [r for r in a["paired_responses"] if r["id"] == "P09"]
    assert all(r["coverage"] == "SUPPORTED" for r in p09)
    assert all("NO PRODUCTION IMPLEMENTATION" in r["answer"] or "not authorization" in r["answer"]
               for r in p09)
    p10 = [r for r in a["paired_responses"] if r["id"] == "P10"]
    assert all(r["coverage"] == "SUPPORTED" for r in p10)
    assert all("R0-P02" in r["answer"] and "R0-P01" in r["answer"] for r in p10)
    assert all("prospectively superseded" in r["answer"] for r in p10)


def test_author_self_assessment_not_formal_research513_score() -> None:
    _, a = load_original()
    tally = {
        method: {value: sum(x["arm"] == method and x["coverage"] == value
                            for x in a["paired_responses"])
                 for value in ("SUPPORTED", "PARTIAL", "ABSTAIN")}
        for method in METHODS
    }
    assert tally == a["self_coverage_counts"]
    assert tally["B0_ORIGINAL"] == {
        "SUPPORTED": 9, "PARTIAL": 1, "ABSTAIN": 2,
    }
    assert tally["B1_EXPOSED_SUBJECT_B0"] == {
        "SUPPORTED": 10, "PARTIAL": 2, "ABSTAIN": 0,
    }
    assert a["coverage_is_author_self_classification_not_evaluator_gold"] is True
    assert not a["formal_R0_P03_scored"]
    assert not a["physical_architecture_selected"]
    assert a["no_current_operational_authority_claims"] is True


def test_older_legacy_and_scientific_exposure_limits_persist() -> None:
    _, a = load_original()
    limits = "\n".join(a["limitations"]).lower()
    assert "legacy" in limits
    assert "source and reference exposure" in limits
    assert "independent" in limits
    assert "not a full" not in limits or "not" in limits
    assert "not" in a["author_role"].lower()
