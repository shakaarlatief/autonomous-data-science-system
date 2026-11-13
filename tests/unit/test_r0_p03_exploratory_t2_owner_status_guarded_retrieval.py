"""Regression of a real 24-question, 120-source T2 status-assertion pilot.

Every source is original Git content from a new frozen commit, excluding the
historically exposed W5 65. Status labels describe only what source headers
say; tests do not qualify independent owner decisions or actual governance.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_t2_owner_status_guarded_retrieval_v01 import (
    PIN, RESULT, CLASS_ORDER, classified_status, first_h1,
    naive_body_status, query_from_heading, run, status_witness, source_archive,
    source_records,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import ANNOTATIONS, load

RESULT_BYTES = 224009
RESULT_SHA256 = "b56b2f173cb69f34e5d6a009421ce738fab5640c47b615796a51a3005b77e843"


def test_status_semantics_are_bounded_not_live_governing_assumptions() -> None:
    assert classified_status("OWNER ACCEPTED / no physical migration") == CLASS_ORDER[0]
    assert classified_status("OWNER-ACCEPTED / target not yet selected") == CLASS_ORDER[0]
    assert classified_status("CANDIDATE FROZEN / OWNER DECISION REQUIRED") == CLASS_ORDER[1]
    assert classified_status("CANDIDATE QUALIFIED / publication pending") == CLASS_ORDER[2]
    assert classified_status("RESEARCH ACCEPTED / CANDIDATE") is None
    assert classified_status("HISTORICAL VERIFICATION RECORD") is None
    assert classified_status("OWNER DECISION PENDING") is None
    assert classified_status("") is None


def test_naive_whole_body_claim_has_real_structural_false_positive_hazard() -> None:
    text = (
        "# New candidate\n"
        + "**Status:** CANDIDATE FROZEN\n"
        + "\n## Past implementation example\n"
        + "The example quotes a superseded record saying OWNER ACCEPTED.\n"
    )
    assert naive_body_status(text) == CLASS_ORDER[0]
    assert classified_status("CANDIDATE FROZEN") == CLASS_ORDER[2]
    witness = status_witness(text, "CANDIDATE FROZEN")
    assert witness["line_number"] == 2
    assert witness["original_line"] == "**Status:** CANDIDATE FROZEN"


def test_topic_query_does_not_include_status_trigger_words_from_target_heading() -> None:
    title = "Research 476: owner-approved hybrid candidate decision pending"
    topic, question = query_from_heading(title)
    assert topic == "Research 476: - hybrid"
    assert "Research 476: - hybrid" in question
    assert "candidate decision pending" not in topic
    assert "owner-approved" not in topic
    assert "CANDIDATE" in CLASS_ORDER[2]


def test_frozen_new_original_source_manifest_excludes_every_old_65_path() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    old = {x["path"] for x in load(ANNOTATIONS)["annotations"]}
    assert len(old) == 65
    current = {x["path"] for x in d["sources"]}
    assert len(current) == 120
    assert current.isdisjoint(old)
    assert d["source_commit"] == PIN
    originals = source_archive()
    assert len(originals) == 1680
    for row in d["sources"]:
        data = originals[row["path"]]
        assert sha256(data).hexdigest() == row["body_sha256"]
        assert len(data) == row["bytes"]
    assert sum(row["is_target"] for row in d["sources"]) == 24


def test_sourcing_and_sampling_are_recomputed_without_reusing_result_labels() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    originals = source_archive()
    old = {x["path"] for x in load(ANNOTATIONS)["annotations"]}
    cases, roster, bodies, snapshot = source_records(originals, old)
    assert snapshot == data["source_cohort"]
    assert roster == data["sources"]
    for case, actual in zip(cases, data["test_cases_and_results"]):
        for key, value in case.items():
            assert actual[key] == value
        body = bodies[case["expected_source"]]
        assert first_h1(body) == case["original_first_h1"]
        witness = case["expected_source_header_witness"]
        line = body.splitlines()[witness["line_number"] - 1]
        assert line == witness["original_line"]
        assert sha256(line.encode("utf-8")).hexdigest() == witness["line_sha256"]
    assert len(cases) == 24


def test_exact_result_reexecutes_byte_identically_on_real_historical_git_objects() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == RESULT_BYTES
    assert sha256(raw).hexdigest() == RESULT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    current = json.loads(raw)
    assert run() == current
    assert current["formal_r0_p03_scored"] is False


def test_all_24_question_and_answer_records_and_negative_controls() -> None:
    r = json.loads(RESULT.read_text(encoding="utf-8"))
    m = r["metrics"]
    assert m["questions"] == 24
    assert m["status_classes"] == {k: 8 for k in CLASS_ORDER}
    assert m["lexical_target_hit_at"] == {"1": 22, "5": 24, "10": 24}
    assert m["source_header_exact_status_correct_at_rank_1"] == 22
    assert m["naive_body_exact_status_correct_at_rank_1"] == 22
    assert m["naive_claim_disagrees_with_own_top_source_header"] == 1
    assert m["wrong_source_with_nonempty_header_status"] == 1
    assert m["governed_header_false_owner_acceptance_nonaccepted_target"] == 0
    assert m["naive_false_owner_acceptance_nonaccepted_target"] == 0
    assert m["no_operative_governance_claims"]
    assert m["all_cases_return_nonassertive_candidates_separately"]

    assert len(r["sources"]) == 120
    for row in r["test_cases_and_results"]:
        assert len(row["candidate_ranking"]) <= 10
        assert row["two_channel_guarded"]["candidate_documents_not_authoritative"] == row["candidate_ranking"]
        assert row["two_channel_guarded"]["assertion"] == row["governed_header_assertion"]
        assert row["lexical_only"]["assertion_state"] == "NO_ASSERTION_BY_DESIGN"
        assert row["governed_header_assertion"]["state"] in {
            "ASSERTED_SOURCE_STATUS_ONLY", "NOT_FOUND_IN_COVERED_SCOPE",
        }
        assert not row["governed_header_assertion"]["operative_governance_claim"]
        assert row["target_rank"] is None or 1 <= row["target_rank"] <= 10
        if row["top_candidate"] != row["expected_source"]:
            assert not row["exact_source_and_status_correct"]


def test_failed_rank1_cases_preserved_without_answer_repair() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    missed = [x for x in data["test_cases_and_results"] if x["target_rank"] != 1]
    assert [x["id"] for x in missed] == ["T2-08", "T2-24"]
    assert [x["target_rank"] for x in missed] == [3, 2]
    assert missed[0]["governed_header_assertion"]["state"] == "NOT_FOUND_IN_COVERED_SCOPE"
    assert missed[0]["naive_conflicts_with_top_source_native_status"]
    assert missed[1]["wrong_source_with_nonempty_header_status"]
