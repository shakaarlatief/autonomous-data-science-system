"""Test exact original two-snapshot decision records and safe assertion semantics.

A source-owned documented decision Status is not proof of current operative
authority, independent natural language task gold or a physical architecture.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe.exploratory_t2_decision_ledger_snapshot_and_scope_v03 import (
    RESULT, REVISIONS, SOURCE_PATH, K,
    create_questions, git_blob_id, guarded_answer, lexical_query,
    normalized_title, original_git_blob, parse_sections, run,
)

EXACT_BYTES = 710228
EXACT_SHA256 = "c22d6b1e62616066f55e22b8811feb21e383e6a568de36a06faf38de7d6d8a27"


def test_exact_saved_result_reruns_from_both_original_git_blobs() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXACT_BYTES
    assert sha256(raw).hexdigest() == EXACT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert json.loads(raw) == run()


def test_real_original_git_blob_source_and_each_decision_witness_identity() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    for snap in ("S0", "S1"):
        raw = original_git_blob(REVISIONS[snap])
        info = data["original_git_blobs"][snap]
        assert info["bytes"] == len(raw)
        assert info["sha256"] == sha256(raw).hexdigest()
        assert info["git_blob_sha1"] == git_blob_id(raw)
        rows = parse_sections(raw, snap)
        assert rows == data["actual_source_sections"][snap]
        source_lines = raw.decode("utf-8").splitlines()
        for decision_id, record in rows.items():
            assert record["id"] == decision_id
            assert record["heading_fragment"] == decision_id
            assert record["source_document"] == SOURCE_PATH
            assert not record["operative_authority_proven"]
            for entry in (record["heading_witness"], record["status_witness"]):
                text = source_lines[entry["line"] - 1]
                assert text == entry["source_line"]
                assert sha256(text.encode("utf-8")).hexdigest() == entry["line_sha256"]
            assert record["section_start_line"] < record["section_end_line"]


def test_actual_git_snapshot_transition_records_D036_only_in_later_revision() -> None:
    saved = json.loads(RESULT.read_text(encoding="utf-8"))
    early = saved["actual_source_sections"]["S0"]
    later = saved["actual_source_sections"]["S1"]
    assert len(early) == 35 and len(later) == 36
    assert set(later) - set(early) == {"D-036"}
    assert set(early) - set(later) == set()
    for decision_id in ("D-035", "D-036"):
        assert later[decision_id]["source_status_category"] == "RECORDED_SELECTED_NOT_OPERATIVE"
        assert "not yet operational authority" in later[decision_id]["source_status"]
    assert early["D-035"]["source_status_category"] == "RECORDED_SELECTED_NOT_OPERATIVE"
    assert "D-036" not in early


def test_supersession_scope_preserved_per_section_not_global_status_assumption() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    for snapshot in ("S0", "S1"):
        for did in ("D-003", "D-011", "D-015"):
            row = d["actual_source_sections"][snapshot][did]
            assert row["source_status_category"] == "RECORDED_SUPERSESSION_WITH_SCOPE"
            assert row["superseded_in_scope"] is not None
            assert row["superseded_in_scope"]["normalized_value"]
            assert row["source_status"].startswith("Superseded")
        assert d["actual_source_sections"][snapshot]["D-012"]["source_status_category"] == "OTHER_RECORDED_DECISION"


def test_duplicate_id_missing_status_and_partial_document_rejected() -> None:
    sample = (
        "# Decisions\n"
        "## D-001. Start\n"
        "**Status:** Accepted\n"
        "## D-001. Again\n"
        "**Status:** Accepted\n"
    )
    with pytest.raises(ValueError, match="duplicate decision"):
        parse_sections(sample.encode(), "S0")
    missing = (
        "# Decisions\n"
        "## D-001. No status\n"
        "**Date:** 2026-08-07\n"
    )
    with pytest.raises(ValueError, match="missing explicit Status"):
        parse_sections(missing.encode(), "S0")


def test_exact_id_asof_and_conflicting_title_semantics() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    older = d["actual_source_sections"]["S0"]
    newer = d["actual_source_sections"]["S1"]
    for snap, decisions in (("S0", older), ("S1", newer)):
        question = {
            "requested_decision_id": "D-035",
            "requested_title": None,
            "intent": "RECORDED_STATUS",
        }
        original = guarded_answer(question, decisions, REVISIONS[snap], d["original_git_blobs"][snap]["git_blob_sha1"])
        assert original["state"] == "ASSERTED_RECORDED_DECISION_STATUS"
        assert original["evidence"]["decision_id"] == "D-035"
        assert original["evidence"]["revision"] == REVISIONS[snap]
        assert not original["operative_governance_claimed"]
        bad = dict(question, requested_title=newer["D-036"]["title"])
        guarded = guarded_answer(bad, decisions, REVISIONS[snap], d["original_git_blobs"][snap]["git_blob_sha1"])
        assert guarded["state"] == "CONFLICTING_IDENTITY"
        assert guarded["evidence"] is None
    assert normalized_title(newer["D-035"]["title"]) != normalized_title(newer["D-036"]["title"])


def test_absence_means_not_in_covered_git_source_not_global_nonexistence() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    for snap in REVISIONS:
        question = {
            "requested_decision_id": "D-903",
            "requested_title": None,
            "intent": "RECORDED_STATUS",
        }
        answer = guarded_answer(
            question, d["actual_source_sections"][snap], REVISIONS[snap],
            d["original_git_blobs"][snap]["git_blob_sha1"],
        )
        assert answer["state"] == "NOT_RECORDED_IN_THIS_SNAPSHOT"
        assert answer["evidence"] is None
        assert answer["coverage"].endswith(REVISIONS[snap])
        assert "Only " + SOURCE_PATH in answer["coverage"]
    early = d["actual_source_sections"]["S0"]
    answer = guarded_answer(
        {"requested_decision_id": "D-036", "requested_title": None, "intent": "RECORDED_STATUS"},
        early, REVISIONS["S0"], d["original_git_blobs"]["S0"]["git_blob_sha1"],
    )
    assert answer["state"] == "NOT_RECORDED_IN_THIS_SNAPSHOT"


def test_operative_request_only_permits_literal_negative_recorded_statement() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    for snap in REVISIONS:
        table = d["actual_source_sections"][snap]
        for did in ("D-035", "D-036", "D-024"):
            q = {"requested_decision_id": did, "requested_title": None, "intent": "OPERATIVE_GOVERNANCE"}
            output = guarded_answer(q, table, REVISIONS[snap], d["original_git_blobs"][snap]["git_blob_sha1"])
            assert not output["operative_governance_claimed"]
            if did == "D-036" and snap == "S0":
                assert output["state"] == "NOT_RECORDED_IN_THIS_SNAPSHOT"
            elif did in ("D-035", "D-036"):
                assert output["state"] == "RECORDED_NOT_YET_OPERATIONAL"
                assert output["evidence"]["source_status_category"] == "RECORDED_SELECTED_NOT_OPERATIVE"
            else:
                assert output["state"] == "UNSUPPORTED_OPERATIVE_GOVERNANCE"
                assert output["evidence"] is None


def test_fixed_request_matrix_and_source_section_lexical_comparator_results() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    qs = create_questions(d["actual_source_sections"])
    saved = d["requests_and_results"]
    assert len(qs) == len(saved) == 94
    assert len({q["id"] for q in qs}) == 94
    for q, row in zip(qs, saved):
        assert all(row[k] == v for k, v in q.items())
        assert row["two_channel_guarded"]["lexical_candidate_decision_ids_not_authority"] == row["lexical_top_k_decision_sections"]
        assert row["two_channel_guarded"]["evidence_assertion"] == row["guarded_id_and_snapshot"]
        assert len(row["lexical_top_k_decision_sections"]) <= K
        if row["guarded_id_and_snapshot"]["evidence"] is not None:
            assert row["guarded_id_and_snapshot"]["evidence"]["decision_id"] == row["requested_decision_id"]
    assert lexical_query("D-036", None) == '"D" OR "036"'
    m = d["metrics"]
    assert m["requests"] == 94
    assert m["family_counts"] == {
        "CONFLICTING_ID_TITLE": 10,
        "OPERATIVE_GOVERNANCE": 4,
        "RECORDED_STATUS": 72,
        "UNKNOWN_ID": 8,
    }
    assert m["documented_source_status_correct_for_existing_ledger_sections"] == 71
    assert m["naive_latest_snapshot_leakage"] == 1
    assert m["lexical_top1_false_decision_identity_all_requests"] == 39
    assert m["naive_accepted_operative_false_positive_against_explicit_source_statement"] == 1
    assert m["guarded_false_recorded_status_claims"] == 0
    assert m["guarded_positive_operative_authority_claims"] == 0
    assert m["scope_preserved_supersession_sections"] == 6
    assert m["nonassertive_candidates_preserved_for_every_request"]
    assert m["missing_at_s0_D_036_is_scoped_absence"]
    assert m["states_by_family"] == {
        "RECORDED_STATUS": {"ASSERTED_RECORDED_DECISION_STATUS": 71, "NOT_RECORDED_IN_THIS_SNAPSHOT": 1},
        "UNKNOWN_ID": {"NOT_RECORDED_IN_THIS_SNAPSHOT": 8},
        "CONFLICTING_ID_TITLE": {"CONFLICTING_IDENTITY": 10},
        "OPERATIVE_GOVERNANCE": {"RECORDED_NOT_YET_OPERATIONAL": 3, "NOT_RECORDED_IN_THIS_SNAPSHOT": 1},
    }
    assert not d["formal_r0_p03_scored"]
