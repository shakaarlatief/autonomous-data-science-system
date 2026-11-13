"""Original-source and synthetic challenge tests for T2 V02 subject binding.

Status is a document's self-description, never verified operative governing
authority. The exact-title challenge generator is exposed, not independent.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_t2_owner_status_guarded_retrieval_v01 import (
    RESULT as PRIOR, source_archive,
)
from experiments.r0_p03_navigation_probe.exploratory_t2_subject_binding_and_unsupported_authority_v02 import (
    ORIGINAL_RESULT_SHA256, RESULT, PIN, K,
    OPERATIVE_INTENT, STATUS_INTENT, REQUEST_KINDS,
    assess_subject, challenge_matrix, normalize_subject, run,
)

BYTES = 465797
HASH = "3648c2a0d6c75cd566a75a09453466a86697d530a88bca5bd91b74e2c849271f"


def test_subject_normalization_strict_but_punctuation_insensitive() -> None:
    assert normalize_subject("Research 476: Thin-Centred   HYBRID") == "research 476 thin centred hybrid"
    assert normalize_subject("Research 477: Thin-Centred Hybrid") != normalize_subject("Research 476: Thin-Centred Hybrid")
    assert normalize_subject("Partial Overview") != normalize_subject("Partial")


def test_fixture_challenges_generated_deterministically_before_ranking() -> None:
    old = json.loads(PRIOR.read_text(encoding="utf-8"))
    one = challenge_matrix(old["test_cases_and_results"])
    two = challenge_matrix(old["test_cases_and_results"])
    assert one == two
    assert len(one) == 118
    assert Counter(x["family"] for x in one) == {
        "BASE_RECORDED_STATUS": 24,
        "CONTRADICTORY_RECORD_NUMBER": 23,
        "UNKNOWN_RECORD_NUMBER": 23,
        "PARTIAL_TOPIC": 24,
        "OPERATIVE_GOVERNANCE": 24,
    }
    assert len({x["challenge_id"] for x in one}) == 118
    assert all(x["intent"] == OPERATIVE_INTENT for x in one if x["family"] == "OPERATIVE_GOVERNANCE")
    for x in one:
        if x["family"] == "UNKNOWN_RECORD_NUMBER":
            assert "999999" in x["topic"]


def test_identity_gate_must_prefer_exact_source_over_top_ranked_wrong_document() -> None:
    top = "docs/checkpoint.md"
    actual = "docs/research.md"
    source_headings = {
        top: "Checkpoint 812: integrated thin-centred hybrid frozen",
        actual: "Research 476: integrated thin-centred hybrid successor candidate V0.1",
    }
    response = assess_subject(
        "Research 476: integrated thin-centred hybrid successor V0.1",
        STATUS_INTENT, [top, actual], source_headings,
        {top: "CANDIDATE FROZEN", actual: "CANDIDATE FROZEN"},
        {top: "# " + source_headings[top] + "\n**Status:** CANDIDATE FROZEN\n",
         actual: "# " + source_headings[actual] + "\n**Status:** CANDIDATE FROZEN\n"},
    )
    assert response["state"] == "ASSERTED_SOURCE_STATUS_ONLY"
    assert response["bound_source"] == actual
    assert response["evidence"]["source_path"] == actual
    assert response["candidate_documents_not_authority"] == [top, actual]
    assert not response["operative_authority_asserted"]


def test_conflicting_number_and_incomplete_or_unknown_subject_abstain() -> None:
    source = "docs/real.md"
    title = "Research 476: thin-centred hybrid successor"
    body = "# " + title + "\n**Status:** OWNER ACCEPTED\n"
    args = ([source], {source: title}, {source: "OWNER ACCEPTED"}, {source: body})
    for topic in ("Research 999999: thin-centred hybrid successor",
                  "Research 477: thin-centred hybrid successor",
                  "thin centred overview"):
        resp = assess_subject(topic, STATUS_INTENT, *args)
        assert resp["state"] == "IDENTITY_NOT_VERIFIED"
        assert resp["evidence"] is None
        assert resp["bound_source"] is None
        assert resp["candidate_documents_not_authority"] == [source]


def test_duplicate_title_or_missing_h1_never_promoted_to_source_assertion() -> None:
    docs = ["docs/a.md", "docs/b.md", "docs/no_h1.md"]
    headings = {
        docs[0]: "Research 47: A title",
        docs[1]: "Research 47: A title",
        docs[2]: None,
    }
    statuses = {x: "OWNER ACCEPTED" for x in docs}
    bodies = {x: "# Research 47: A title\n**Status:** OWNER ACCEPTED\n" for x in docs}
    ambiguous = assess_subject("Research 47: A title", STATUS_INTENT, docs, headings, statuses, bodies)
    assert ambiguous["state"] == "AMBIGUOUS_SOURCE_IDENTITY"
    assert ambiguous["bound_source"] is None
    assert ambiguous["evidence"] is None
    unheaded = assess_subject("Research 47: A title", STATUS_INTENT, docs[2:], headings, statuses, bodies)
    assert unheaded["state"] == "IDENTITY_NOT_VERIFIED"


def test_current_operative_governance_always_refused_without_trusted_evidence() -> None:
    p = "docs/research/owner_accepted.md"
    h = "Research 1: owner-accepted historical record"
    doc = "# " + h + "\n**Status:** OWNER ACCEPTED\n"
    response = assess_subject(
        "Research 1: historical record",
        OPERATIVE_INTENT, [p], {p: h}, {p: "OWNER ACCEPTED"}, {p: doc},
    )
    assert response["state"] == "UNSUPPORTED_OPERATIVE_GOVERNANCE"
    assert response["bound_source"] is None
    assert response["evidence"] is None
    assert response["candidate_documents_not_authority"] == [p]


def test_exact_original_git_source_identities_and_candidate_world_are_unchanged() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    old = json.loads(PRIOR.read_text(encoding="utf-8"))
    assert sha256(PRIOR.read_bytes()).hexdigest() == ORIGINAL_RESULT_SHA256
    assert report["source_roster"] == old["sources"]
    assert report["original_120_source_manifest_sha256"] == old["source_cohort"]["sampled_source_sha256"]
    assert report["original_source_git_pin"] == PIN
    sources = source_archive()
    for row in report["source_roster"]:
        assert sha256(sources[row["path"]]).hexdigest() == row["body_sha256"]


def test_stored_results_equal_fresh_source_execution_exactly() -> None:
    data = RESULT.read_bytes()
    assert len(data) == BYTES
    assert sha256(data).hexdigest() == HASH
    assert data.endswith(b"\n") and b"\r\n" not in data
    assert json.loads(data) == run()


def test_baseline_24_rankings_match_and_status_evidence_is_original_source_line() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    old = json.loads(PRIOR.read_text(encoding="utf-8"))
    prior_by_id = {x["id"]: x for x in old["test_cases_and_results"]}
    for row in result["challenges_and_outputs"]:
        answer = row["subject_binding_and_answer"]
        assert len(row["lexical_top_ten"]) <= K
        assert answer["candidate_documents_not_authority"] == row["lexical_top_ten"]
        assert not answer["operative_authority_asserted"]
        if row["family"] == "BASE_RECORDED_STATUS":
            assert row["lexical_top_ten"] == prior_by_id[row["source_v01_case_id"]]["candidate_ranking"]
            assert row["correct_target_source_status_assertion_for_evaluation_only"]
            evidence = answer["evidence"]
            assert evidence and evidence["not_operative_governing_authority"]
            assert evidence["source_path"] == row["expected_source_for_evaluation_only"]
            assert sha256(evidence["original_line"].encode("utf-8")).hexdigest() == evidence["line_sha256"]


def test_saved_failures_and_all_94_challenge_abstentions_are_preserved() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    metrics = result["metrics"]
    assert metrics["requests"] == 118
    assert metrics["old_base_correct_rank1_source_and_status"] == 22
    assert metrics["old_base_wrong_source_assertions"] == 1
    assert metrics["v02_base_exact_source_and_status_answers"] == 24
    assert metrics["v02_base_wrong_source_assertions"] == 0
    assert metrics["v02_all_challenges_wrong_source_assertions"] == 0
    assert metrics["challenge_nonbase_status_assertions"] == 0
    assert metrics["operative_governance_assertions"] == 0
    assert metrics["retained_nonassertive_candidates_every_request"]
    assert not metrics["independent_currentness_gold"]
    assert not metrics["genuine_language_paraphrase_robustness_evaluated"]
    assert metrics["states_by_family"] == {
        "BASE_RECORDED_STATUS": {"ASSERTED_SOURCE_STATUS_ONLY": 24},
        "CONTRADICTORY_RECORD_NUMBER": {"IDENTITY_NOT_VERIFIED": 23},
        "UNKNOWN_RECORD_NUMBER": {"IDENTITY_NOT_VERIFIED": 23},
        "PARTIAL_TOPIC": {"IDENTITY_NOT_VERIFIED": 24},
        "OPERATIVE_GOVERNANCE": {"UNSUPPORTED_OPERATIVE_GOVERNANCE": 24},
    }
    rows = [r for r in result["challenges_and_outputs"] if r["family"] == "BASE_RECORDED_STATUS"]
    recovered = [x for x in rows if x["target_rank_for_evaluation_only"] != 1]
    assert [(x["source_v01_case_id"], x["target_rank_for_evaluation_only"]) for x in recovered] == [
        ("T2-08", 3), ("T2-24", 2),
    ]
    assert not result["formal_r0_p03_scored"]
