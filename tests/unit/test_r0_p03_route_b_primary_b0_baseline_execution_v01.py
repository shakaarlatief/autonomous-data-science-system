"""Regress the first executed, explicitly provisional Route B primary B0 pass.

The reference answers are source-cited coordinator drafts, not independent
blind scoring or a replacement for the original twelve-primary plus
nine-neutral-legacy Research 513 architecture-selection protocol.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    BUILD_PREFIX, CONTRACT, HOLDOUT_PREFIX, PIN, RANKERS,
    RESULT, TASKS, TASK_BYTES, TASK_SHA, classify_path, git,
    original_contents, prospective_draw, run, witness_lines,
)

RESULT_BYTES = 122682
RESULT_SHA256 = "59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab"


def test_original_route_b_questions_and_provisional_answers_are_fixed_before_output() -> None:
    raw = TASKS.read_bytes()
    assert len(raw) == TASK_BYTES
    assert sha256(raw).hexdigest() == TASK_SHA
    manifest = json.loads(raw)
    assert manifest["source_git_pin"] == PIN
    assert manifest["authored_by"] == "EXPOSED_COORDINATOR_CHATGPT_NOT_FRESH_OR_INDEPENDENT"
    assert len(manifest["tasks"]) == 12
    assert len({x["id"] for x in manifest["tasks"]}) == 12
    assert len({x["required_source_for_evaluation_only"] for x in manifest["tasks"]}) == 12
    assert Counter(x["category"] for x in manifest["tasks"]) == {
        k: 3 for k in manifest["primary_categories"]
    }
    assert all(x["reference_answer_for_evaluation_only"] and x["required_source_witness_lines"]
               for x in manifest["tasks"])


def test_eligible_git_source_strata_and_root_record_exception_remain_explicit() -> None:
    assert classify_path("docs/CURRENT_STATE.md") == "root_primary"
    assert classify_path("docs/DECISIONS.md") == "root_primary"
    assert classify_path("docs/research/503_example.md") == "research"
    assert classify_path("docs/checkpoints/917_example.md") == "checkpoint"
    assert classify_path("docs/specifications/028_example.md") == "specification"
    assert classify_path("docs/foundations/022_example.md") == "foundation"
    assert classify_path("tools/project_knowledge/identity.py") == "tool"
    assert classify_path("docs/README.md") is None
    assert classify_path("docs/research/hidden/other.md") is None


def test_independently_resampled_60_20_split_is_exact_original_git() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    required = {
        t["required_source_for_evaluation_only"]
        for t in json.loads(TASKS.read_text(encoding="utf-8"))["tasks"]
    }
    build, held, stats = prospective_draw(required)
    assert build == d["build_sources"]
    assert held == d["heldout_sources"]
    assert stats == d["sampling"]
    assert len(build) == 60 and len(held) == 20
    assert not set(build) & set(held)
    assert required <= set(build)
    assert stats["source_required_closure_count"] == 12
    assert stats["build_filler_quotas"] == {
        "research": 20, "checkpoint": 16, "specification": 4,
        "foundation": 4, "tool": 4,
    }
    assert stats["heldout_quotas"] == {
        "research": 8, "checkpoint": 8, "specification": 2,
        "foundation": 1, "tool": 1,
    }
    assert len(BUILD_PREFIX) > 0 and len(HOLDOUT_PREFIX) > 0


def test_all_80_original_git_source_carriers_have_exact_byte_identity() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    sources = original_contents(d["build_sources"] + d["heldout_sources"])
    assert len(sources) == 80
    for row in d["source_roster"]:
        blob = sources[row["path"]]
        assert row["bytes"] == len(blob)
        assert sha256(blob).hexdigest() == row["original_source_sha256"]
        assert row["is_build"] != row["is_heldout"]


def test_reference_answer_excerpts_are_exact_original_lines_with_hash_witnesses() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    originals = original_contents(d["build_sources"] + d["heldout_sources"])
    manifest = {t["id"]: t for t in json.loads(TASKS.read_text(encoding="utf-8"))["tasks"]}
    for answer in d["provisional_reference_answers"]:
        task = manifest[answer["id"]]
        source = answer["required_source_for_evaluation_only"]
        body = originals[source].decode("utf-8")
        assert answer["reference_answer_for_evaluation_only"] == task["reference_answer_for_evaluation_only"]
        assert answer["required_source_body_sha256"] == sha256(originals[source]).hexdigest()
        actual_witnesses = witness_lines(body, task["required_source_witness_lines"])
        assert actual_witnesses == answer["required_witnesses_original_source"]
        original_lines = body.splitlines()
        for evidence in actual_witnesses:
            text = original_lines[evidence["line_number"] - 1]
            assert text == evidence["original_line"]
            assert sha256(text.encode("utf-8")).hexdigest() == evidence["sha256_of_original_line"]
        assert answer["reference_status"] == "EXPOSED_COORDINATOR_SOURCE_CITED_PROVISIONAL"
        assert answer["no_operative_deployment_inferred_from_header_status"]


def test_exact_122682_byte_result_replays_identically_without_task_or_answer_mutation() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == RESULT_BYTES
    assert sha256(raw).hexdigest() == RESULT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert json.loads(raw) == run()


def test_b0_real_misses_and_diagnostic_method_outcomes_are_preserved() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    m = d["metrics"]
    assert m["B0_SUBSTRATE_LEXICAL_BASELINE"]["required_source_hit_at_1"] == 8
    assert m["B0_SUBSTRATE_LEXICAL_BASELINE"]["required_source_hit_at_3"] == 10
    assert m["B0_SUBSTRATE_LEXICAL_BASELINE"]["required_source_hit_at_5"] == 10
    assert m["B0_SUBSTRATE_LEXICAL_BASELINE"]["required_source_hit_at_10"] == 11
    assert m["B0_SUBSTRATE_LEXICAL_BASELINE"]["missing_required_source_at_10"] == ["P01"]
    assert m["TITLE_LEXICAL_DIAGNOSTIC"]["required_source_hit_at_1"] == 10
    assert m["TITLE_LEXICAL_DIAGNOSTIC"]["missing_required_source_at_10"] == ["P02"]
    assert m["CHAR_TRIGRAM_DIAGNOSTIC"]["required_source_hit_at_1"] == 12
    assert m["DIAGNOSTIC_THREE_WAY_RRF"]["required_source_hit_at_1"] == 12
    assert len(d["comparative_retrieval_trace"]) == 12
    for entry in d["comparative_retrieval_trace"]:
        expected = entry["intended_source_for_evaluation_only"]
        assert expected in d["build_sources"]
        assert set(entry["common_source_candidate_rankings"]) == set(RANKERS)
        assert all(len(v) <= 10 and len(v) == len(set(v))
                   and set(v) <= set(d["build_sources"])
                   for v in entry["common_source_candidate_rankings"].values())
        for name, candidates in entry["common_source_candidate_rankings"].items():
            actual = candidates.index(expected) + 1 if expected in candidates else None
            assert actual == entry["reference_source_rank_after_retrieval"][name]


def test_b0_is_not_mislabeled_as_a_formal_12_task_viability_or_full_B0_B4_comparison() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    assert d["contract"] == CONTRACT
    assert d["source_git_pin"] == PIN
    assert not d["formal_R0_P03_scored"]
    assert not d["physical_architecture_selected"]
    assert not d["runtime_indexes"]["B0_uses_metadata_gold_for_ranking"]
    assert d["runtime_indexes"]["source_context_cap"] == 12000
    assert d["runtime_indexes"]["retrieval_top_k"] == 10
    assert any("DO NOT IMPLEMENT B1/B2/B3/B4" in v for v in d["scientific_limits"])
    assert any("held-out" in v.lower() for v in d["scientific_limits"])
    assert any("nine-case" in v for v in d["scientific_limits"])


def test_bad_reference_witness_cannot_be_silently_counted_as_qualified() -> None:
    original = "A full original source line mentioning two relations.\n"
    output = witness_lines(original, ["source line mentioning"])
    assert output[0]["original_line"].strip() == original.strip()
    import pytest
    with pytest.raises(ValueError, match="absent"):
        witness_lines(original, ["invented external deployment occurred"])
