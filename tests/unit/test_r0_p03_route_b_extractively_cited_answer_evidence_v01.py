"""Regress source-only answer quotation and retrospective evidence coverage.

The generated drafts are deterministic original-source quotes. These
tests explicitly do not certify independently correct natural-language
answers, source ownership, or formal Research513 success thresholds.
"""
from __future__ import annotations

from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe.route_b_extractively_cited_answer_evidence_v01 import (
    BASE, B0, B123, B4, BUDGET, CONTRACT, EXTRA, FROZEN, LINE_CAP,
    MANIFEST, METHODS, RESULT, SCAN, TOP_SOURCES, accessible_lines,
    draft, evidence, evaluate_after_generation, frozen, generate_all,
    original_contents, ranker_inputs, run, verify_quoted_lines,
)

RESULT_BYTES = 995317
RESULT_SHA256 = "17f5bae16a96530008ea954e7145e3903e25386d83eeee7e69b983de91b908f8"


def saved_result() -> dict:
    raw = RESULT.read_bytes()
    assert len(raw) == RESULT_BYTES
    assert sha256(raw).hexdigest() == RESULT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    return json.loads(raw)


def test_all_four_older_exact_original_source_and_reference_files_are_unchanged() -> None:
    for name, (length, digest) in FROZEN.items():
        b = (BASE / name).read_bytes()
        assert len(b) == length
        assert sha256(b).hexdigest() == digest
    b0 = frozen(B0)
    assert len(b0["build_sources"]) == 60
    assert len(b0["heldout_sources"]) == 20
    assert len(frozen(MANIFEST)["tasks"]) == 12
    assert len(frozen(B123)["retrieval_trace"]) == 12
    assert len(frozen(B4)["cases"]) == 12


def test_quoted_lines_only_come_from_same_complete_original_source_prefix() -> None:
    original = "# Example\n**Status:** ORIGINAL\n" + "other stuff\n" * 4
    original += "~~" + "~" + "\n**Status:** FALSE FENCED\n" + "~~" + "~" + "\n"
    original += "after\n"
    selected = evidence("What is the example status?", original)
    assert selected and selected[0]["original_source_line"] == "# Example"
    assert "**Status:** ORIGINAL" in [x["original_source_line"] for x in selected]
    assert "**Status:** FALSE FENCED" not in [x["original_source_line"] for x in selected]
    assert all(x["sha256_of_original_line"] == sha256(x["original_source_line"].encode("utf8")).hexdigest()
               for x in selected)
    assert len(selected) <= EXTRA + 1
    assert all(len(x["original_source_line"]) <= LINE_CAP for x in selected)


def test_partial_original_last_line_is_dropped_not_cited_as_complete() -> None:
    text = "# Heading\n**Status:** KNOWN\nTRUNCATED LINE HAS MORE CONTENT"
    assert accessible_lines(text, 20) == ["# Heading"]
    assert accessible_lines(text, len("# Heading\n**Status:** KNOWN\n")) == ["# Heading", "**Status:** KNOWN"]
    assert accessible_lines(text, BUDGET)[-1] == "TRUNCATED LINE HAS MORE CONTENT"
    with pytest.raises(ValueError):
        accessible_lines(text, 0)


def test_model_free_renderer_reports_attributed_records_without_inventing_authority() -> None:
    example = [{
        "path": "docs/example.md",
        "sha256": "1" * 64,
        "quotes": [{
            "line": 1, "original_source_line": "# Historical Example",
            "sha256_of_original_line": sha256(b"# Historical Example").hexdigest(),
            "is_H1": True,
        }],
    }]
    result = draft(example)
    assert "docs/example.md@sha256:" + "1" * 64 in result
    assert "Original line 1" in result
    assert "or proof of current operative governing authority" in result
    assert "Historical Example" in result
    assert "insufficient" in draft([])


def test_ranker_dataflow_has_no_reference_answers_or_required_source_labels() -> None:
    inputs = ranker_inputs(frozen(B0), frozen(B123), frozen(B4))
    assert len(inputs) == 12
    assert [i["id"] for i in inputs] == [t["id"] for t in frozen(MANIFEST)["tasks"]]
    assert set().union(*(set(record.keys()) for record in inputs)) == {
        "id", "question", "ranks"
    }
    assert all(set(x["ranks"]) == set(METHODS) for x in inputs)
    raw = json.dumps(inputs)
    for task in frozen(MANIFEST)["tasks"]:
        # Reference text must never flow into an arm-visible construction.
        assert task["reference_answer_for_evaluation_only"] not in raw
        assert task["required_source_witness_lines"][0] not in raw


def test_all_84_drafts_and_1260_original_line_sources_reverify_against_git() -> None:
    actual = saved_result()
    b0 = frozen(B0)
    sources = original_contents(b0["build_sources"])
    provenance = verify_quoted_lines(actual["generated_source_only_answer_drafts"], sources)
    assert provenance == actual["exact_original_citation_verification"]
    assert provenance["drafts"] == 84
    assert provenance["source_records_cited"] == 252
    assert provenance["verbatim_original_lines_verified"] == 1260
    assert provenance["draft_characters"] == 251190
    assert provenance["all_citations_genuine_original_Git_lines"]
    all_heldout = set(b0["heldout_sources"])
    for case in actual["generated_source_only_answer_drafts"]:
        assert len(case["arm_drafts"]) == len(METHODS)
        for response in case["arm_drafts"]:
            assert not response["gold_source_or_answer_used_in_draft"]
            assert not response["operative_authority_asserted"]
            assert len(response["consumed_source_paths"]) <= TOP_SOURCES
            assert not all_heldout.intersection(response["consumed_source_paths"])
            assert all(c["sha256"] == sha256(sources[c["path"]]).hexdigest()
                       for c in response["cited_source_records"])


def test_evaluation_runs_only_after_frozen_answer_drafts_exist() -> None:
    b0 = frozen(B0)
    original = original_contents(b0["build_sources"])
    pre_gold = ranker_inputs(b0, frozen(B123), frozen(B4))
    generated = generate_all(pre_gold, original)
    assert generated == saved_result()["generated_source_only_answer_drafts"]
    assert all(not variant["gold_source_or_answer_used_in_draft"]
               for case in generated for variant in case["arm_drafts"])
    evaluations, metrics = evaluate_after_generation(
        generated, frozen(MANIFEST), original
    )
    d = saved_result()
    assert metrics == d["metrics"]
    assert evaluations == d["retrospective_reference_evidence_audit"]


def test_real_original_frozen_case_metrics_include_failing_evidence() -> None:
    m = saved_result()["metrics"]
    assert m["B0_ORIGINAL"]["required_source_in_cited_top3"] == 10
    assert m["B0_ORIGINAL"]["all_reference_excerpts_actually_cited"] == 9
    assert m["B0_ORIGINAL"]["cases_missing_complete_cited_reference_evidence"] == [
        "P01", "P02", "P03",
    ]
    assert m["B1_EXPOSED_SUBJECT_B0"]["required_source_in_cited_top3"] == 11
    assert m["B1_EXPOSED_SUBJECT_B0"]["all_reference_excerpts_actually_cited"] == 10
    assert m["B1_EXPOSED_SUBJECT_B0"]["cases_missing_complete_cited_reference_evidence"] == [
        "P02", "P03",
    ]
    assert m["B2_SOURCE_WRITTEN_LINK_B0"]["all_reference_excerpts_actually_cited"] == 9
    assert m["B3_EXPOSED_CONCERN_B0"]["all_reference_excerpts_actually_cited"] == 8
    assert m["B4_CLASSICAL_LSA_DENSE_ONLY"]["all_reference_excerpts_actually_cited"] == 7
    assert m["B4_CLASSICAL_LSA_B0_FUSION"]["all_reference_excerpts_actually_cited"] == 9
    assert m["B4_CLASSICAL_LSA_B2_FUSION"]["all_reference_excerpts_actually_cited"] == 9
    assert all(v["semantic_answer_correctness_unqualified"]
               and v["semantic_answer_correctness_score"] is None for v in m.values())


def test_real_P02_is_retrieved_but_not_all_quotes_selected_and_P03_is_out_of_top3() -> None:
    d = saved_result()
    cases = {c["id"]: c for c in d["retrospective_reference_evidence_audit"]}
    p2 = next(a for a in cases["P02"]["method_evidence"] if a["arm"] == "B0_ORIGINAL")
    assert p2["required_source_consumed_top_3"]
    assert p2["all_frozen_source_excerpts_available_in_original_12000_chars"]
    assert not p2["all_frozen_source_excerpts_emitted_in_citations"]
    assert p2["source_evidence_status"] == "REFERENCES_ACCESSIBLE_NOT_ALL_QUOTED"
    p3 = next(a for a in cases["P03"]["method_evidence"] if a["arm"] == "B0_ORIGINAL")
    assert p3["source_evidence_status"] == "REQUIRED_SOURCE_NOT_RETRIEVED"
    assert not p3["required_source_consumed_top_3"]


def test_negative_evaluation_cannot_turn_missing_reference_source_into_pass() -> None:
    d = saved_result()
    candidate = [x for x in d["generated_source_only_answer_drafts"] if x["id"] == "P01"]
    keys = frozen(MANIFEST)
    original = original_contents(frozen(B0)["build_sources"])
    audit, grade = evaluate_after_generation(candidate, keys, original)
    assert len(audit) == 1
    b0 = next(x for x in audit[0]["method_evidence"] if x["arm"] == "B0_ORIGINAL")
    assert not b0["all_frozen_source_excerpts_emitted_in_citations"]
    assert grade["B0_ORIGINAL"]["all_reference_excerpts_actually_cited"] == 0


def test_full_end_to_end_original_git_replay_is_exact_without_tuning() -> None:
    assert run() == saved_result()


def test_scientific_and_owner_authority_claims_remain_explicitly_unqualified() -> None:
    r = saved_result()
    assert r["contract"] == CONTRACT
    assert len(r["build_carriers"]) == 60
    assert r["heldout_carrier_count_excluded"] == 20
    assert len(r["generated_source_only_answer_drafts"]) == 12
    assert not r["independent_source_answer_gold"]
    assert not r["formal_R0_P03_scored"]
    assert not r["physical_architecture_selected"]
    assert not r["renderer"]["gold_in_renderer"]
    assert not r["renderer"]["source_status_as_current_governing_authority"]
    assert r["renderer"]["model_free_extract_only"]
    assert any("nine-case" in x for x in r["limits"])
    assert any("Claude" in x for x in r["limits"])
