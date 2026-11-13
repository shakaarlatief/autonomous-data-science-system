"""Exact Git-source replay and falsification checks for exposed no-ID T2 V04.

Author-intended labels are NOT independent semantic or operational authority
gold. A conditional source-Status hypothesis can still point to the wrong
decision under unseen queries despite the observed 29/29 author agreement.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

from experiments.r0_p03_navigation_probe.exploratory_t2_no_id_retrieval_and_selective_evidence_v04 import (
    RESULT, MANIFEST, MANIFEST_SHA256, METHODS, REVISIONS, SOURCE_PATH,
    char_rank, fts_query, grams, guarded_provisional_hypothesis, manifest,
    norm_text, rrf_fusion, run, sparse_char_index, tokens,
)
from experiments.r0_p03_navigation_probe.exploratory_t2_decision_ledger_snapshot_and_scope_v03 import (
    original_git_blob, parse_sections, git_blob_id,
)

RESULT_BYTES = 245742
RESULT_SHA256 = "327278182a3ea6793ca999be9d5b6e179cdf8bbf89d37bdacdf6f6147773dc1b"


def test_frozen_author_question_manifest_is_hash_pinned_and_has_no_ids_in_text() -> None:
    raw = MANIFEST.read_bytes()
    assert len(raw) == 8668
    assert sha256(raw).hexdigest() == MANIFEST_SHA256
    data = manifest()
    assert data["author"].endswith("NOT_INDEPENDENT")
    assert len(data["positive"]) == 26
    assert len(data["negative"]) == 6
    assert len({x["id"] for x in data["positive"] + data["negative"]}) == 32
    assert all("D-" not in x["query"] for x in data["positive"] + data["negative"])
    assert [x["id"] for x in data["positive"] if x["expected_id_for_evaluation_only"] == "D-036"] == ["Q22"]


def test_four_methods_have_different_computational_semantics() -> None:
    assert len(METHODS) == 4
    assert tokens("What is the status of the local SQLite database for this project?") == ["status", "local", "sqlite", "database"]
    assert fts_query("Does the model use SQLite or vector embeddings?") == '"model" OR "use" OR "sqlite" OR "vector" OR "embeddings"'
    assert norm_text("Private-to-public   GIT") == "private to public git"
    assert grams("abc")["abc"] == 1
    ranks = {
        "BODY_FTS5_BM25": ["D-002", "D-001"],
        "TITLE_FTS5_BM25": ["D-001", "D-002"],
        "CHARACTER_NGRAM_TFIDF": ["D-001", "D-003"],
    }
    assert rrf_fusion(ranks)[0] == "D-001"
    assert set(rrf_fusion(ranks)) == {"D-001", "D-002", "D-003"}


def test_full_source_sha_sections_and_snapshot_membership_match_real_git() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    for snap in ("S0", "S1"):
        raw = original_git_blob(REVISIONS[snap])
        src = d["source_blob_identifiers"][snap]
        assert src["source_path"] == SOURCE_PATH
        assert src["revision"] == REVISIONS[snap]
        assert src["sha256"] == sha256(raw).hexdigest()
        assert src["git_blob_sha1"] == git_blob_id(raw)
        original = parse_sections(raw, snap)
        assert len(original) == src["decisions"] == (35 if snap == "S0" else 36)
        for did, rec in original.items():
            saved = d["source_decision_manifest"][snap][did]
            assert rec["section_sha256"] == saved["section_sha256"]
            assert rec["title"] == saved["title"]
            assert rec["source_status"] == saved["source_status"]
            assert rec["status_witness"] == saved["status_witness"]
        assert len(d["source_decision_manifest"][snap]) == len(original)
    assert "D-036" not in d["source_decision_manifest"]["S0"]
    assert "D-036" in d["source_decision_manifest"]["S1"]


def test_saved_result_is_exact_byte_reproduced_by_real_source_rerun() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == RESULT_BYTES
    assert sha256(raw).hexdigest() == RESULT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert json.loads(raw) == run()


def test_all_64_queries_all_methods_and_negative_controls_retained() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    m = d["metrics"]
    cases = d["cases"]
    assert len(cases) == 64
    assert len({r["id"] for r in cases}) == 64
    assert Counter(r["snapshot"] for r in cases) == {"S0": 32, "S1": 32}
    assert m["questions_in_manifest"] == 32
    assert m["source_snapshot_instances"] == 64
    assert m["author_intended_present"] == 51
    assert m["author_intended_absent_or_unmatched"] == 13
    assert m["positive_id_missing_S0"] == ["Q22"]
    assert m["provisional_correct_by_author_label"] == 29
    assert m["provisional_wrong_by_author_label"] == 0
    assert m["provisional_status_admissions"] == 29
    assert m["abstentions"] == 35
    assert m["provisional_on_absent_or_author_no_target"] == 0
    assert m["provisional_precision_by_author_label"] == 1.0
    assert m["correct_provisional_coverage_of_present"] == 29 / 51
    assert m["all_candidate_lists_kept_separate"]
    assert not m["question_author_independent"]
    assert not m["semantic_embedding_retrieval_executed"]
    assert m["operative_governance_claim_count"] == 0
    assert not d["formal_r0_p03_scored"]
    for row in cases:
        assert set(row["rankings"]) == set(METHODS)
        assert all(len(x) <= 10 and len(x) == len(set(x)) for x in row["rankings"].values())
        assert row["selective_status_response"]["all_lexical_candidate_ids_not_authority"] == row["rankings"]["THREE_WAY_RRF"]
        assert not row["selective_status_response"]["operative_governance_asserted"]
        assert not row["selective_status_response"]["subject_identity_independently_verified"]
        if row["selective_status_response"]["provisional_decision_id"]:
            cited = row["selective_status_response"]["source_status_and_provenance"]
            assert cited and cited["revision"] == REVISIONS[row["snapshot"]]
            assert cited["decision_id"] == row["selective_status_response"]["provisional_decision_id"]
            assert cited["not_independent_operational_governance"]
        else:
            assert row["selective_status_response"]["source_status_and_provenance"] is None


def test_real_ranking_results_compare_competing_mechanisms_not_invented_success() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    scores = d["metrics"]["retrieval_by_method"]
    assert scores["BODY_FTS5_BM25"]["hit_at_1"] == 45
    assert scores["TITLE_FTS5_BM25"]["hit_at_1"] == 37
    assert scores["CHARACTER_NGRAM_TFIDF"]["hit_at_1"] == 47
    assert scores["THREE_WAY_RRF"]["hit_at_1"] == 47
    assert scores["TITLE_FTS5_BM25"]["hit_at_10"] == 47
    for name in ("BODY_FTS5_BM25", "CHARACTER_NGRAM_TFIDF", "THREE_WAY_RRF"):
        assert scores[name]["hit_at_10"] == 51
    assert scores["THREE_WAY_RRF"]["hit_at_3"] == 51
    assert scores["CHARACTER_NGRAM_TFIDF"]["hit_at_3"] == 51
    assert scores["BODY_FTS5_BM25"]["hit_at_3"] == 49
    assert scores["TITLE_FTS5_BM25"]["hit_at_3"] == 45
    assert scores["THREE_WAY_RRF"]["mrr_at_10"] == scores["CHARACTER_NGRAM_TFIDF"]["mrr_at_10"]
    # Both exposed Q24 and Q25 defeat fused top-one, in each original snapshot.
    misses = [x["id"] for x in d["cases"] if x["author_intended_record_in_snapshot"]
              and x["ranks_of_author_intended_section"]["THREE_WAY_RRF"] != 1]
    assert misses == ["Q24_S0", "Q25_S0", "Q24_S1", "Q25_S1"]


def test_all_provisional_status_witnesses_are_original_source_lines() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    for snap in ("S0", "S1"):
        lines = original_git_blob(REVISIONS[snap]).decode("utf-8").splitlines()
        for row in data["cases"]:
            if row["snapshot"] != snap:
                continue
            a = row["selective_status_response"]
            if a["state"] != "PROVISIONAL_SOURCE_STATUS_HYPOTHESIS":
                continue
            evidence = a["source_status_and_provenance"]
            witness = evidence["status_witness"]
            actual = lines[witness["line"] - 1]
            assert actual == witness["source_line"]
            assert sha256(actual.encode("utf-8")).hexdigest() == witness["line_sha256"]
            assert evidence["decision_fragment"] == a["provisional_decision_id"]


def test_consensus_gate_can_still_emit_wrong_referent_on_unseen_query() -> None:
    # This synthetic deliberately makes the *three retrieval methods agree*
    # on D-001 while the hypothetical questioner's intended referent may
    # still be elsewhere. The guard is NOT independent identity verification.
    actual = parse_sections(original_git_blob(REVISIONS["S1"]), "S1")
    rankings = {
        "BODY_FTS5_BM25": ["D-001", "D-002"],
        "TITLE_FTS5_BM25": ["D-001", "D-002"],
        "CHARACTER_NGRAM_TFIDF": ["D-001", "D-002"],
        "THREE_WAY_RRF": ["D-001", "D-002"],
    }
    answer = guarded_provisional_hypothesis(
        "Create a dedicated separate data project", rankings, actual,
        "S1", git_blob_id(original_git_blob(REVISIONS["S1"])),
    )
    assert answer["state"] == "PROVISIONAL_SOURCE_STATUS_HYPOTHESIS"
    assert answer["provisional_decision_id"] == "D-001"
    assert not answer["subject_identity_independently_verified"]
    assert not answer["operative_governance_asserted"]
    # A query author wanting D-002 would still get this wrong provisional
    # hypothesis. The observed 29/29 is not a general guaranteed precision.


def test_source_index_costs_are_exposed_not_presented_as_free() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    cost_s0 = d["index_characterization"]["S0"]["char_sparse"]
    cost_s1 = d["index_characterization"]["S1"]["char_sparse"]
    assert cost_s0["indexed_sections"] == 35
    assert cost_s1["indexed_sections"] == 36
    assert cost_s0["unique_3gram_features"] == 2117
    assert cost_s1["unique_3gram_features"] == 2149
    assert cost_s0["nonzero_document_3gram_weights"] == 11394
    assert cost_s1["nonzero_document_3gram_weights"] == 11724
    assert cost_s0["original_section_bytes"] == 50835
    assert cost_s1["original_section_bytes"] == 54975
