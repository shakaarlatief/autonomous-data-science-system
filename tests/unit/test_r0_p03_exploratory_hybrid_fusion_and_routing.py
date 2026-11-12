"""Reproduce real Git-source hybrid retrieval without promoting pilot to scored P03.

The eight candidate outputs and both benchmark-family references are verified
separately. No scenario ID, old B1 oracle topic, exact gold target or private
C01/C02 case is allowed into query-time fusion or adaptive routing. The known
historical W5 labels and heading self-targets are retained as limitations.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_hybrid_fusion_and_routing_v01 import (
    ARMS,
    FUSIONS,
    LEGACY_B01,
    LEGACY_B02,
    LIMIT,
    PIN,
    RRF_K,
    RESULT,
    SOURCE_SHA256,
    candidate_outputs,
    normalized_heading,
    rrf,
    run,
)

EXPECTED_BYTES = 642735
EXPECTED_SHA = "e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f"


def test_normalized_heading_and_rank_fusion_with_lexical_ties() -> None:
    assert normalized_heading("  A   Title\n") == "a title"
    assert normalized_heading("Ｃａｓｅ Ｔｅｓｔ") == "case test"
    lexical = ["docs/a.md", "docs/b.md", "docs/c.md", "docs/d.md"]
    lists = {"b0": ["docs/a.md", "docs/b.md"], "b1": ["docs/b.md", "docs/c.md"]}
    top, unique = rrf(("b0", "b1"), lists, lexical)
    assert unique == 3
    assert top == ["docs/b.md", "docs/a.md", "docs/c.md"]
    assert RRF_K == 60 and LIMIT == 10
    assert set(FUSIONS) == {"fusion_b0_b1", "fusion_b0_b2", "fusion_b1_b2", "fusion_all"}


def test_same_query_router_never_consumes_gold_or_scenario_ids() -> None:
    import inspect
    args = inspect.signature(candidate_outputs).parameters
    assert set(args) == {
        "query", "connection", "annotations", "subjects", "links", "titles_normalized",
    }
    assert "target" not in args and "gold" not in args and "scenario" not in args


def test_actual_historical_git_run_matches_exact_persisted_output() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXPECTED_BYTES
    assert sha256(raw).hexdigest() == EXPECTED_SHA
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    original = json.loads(raw)
    assert run() == original
    assert original["source_pin"] == PIN
    assert original["source_fingerprint_sha256"] == SOURCE_SHA256
    assert original["source_members"] == 65
    assert original["literal_source_link_edges"] == 110
    assert original["all_arms"] == list(ARMS)
    assert original["family_counts"] == {
        "old_nine_subject_queries": 9,
        "all_65_heading_locator_queries": 65,
    }


def test_known_references_and_measured_hybrid_ablations_are_separate() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    family = data["aggregate"]
    old = family["old_nine_subject_queries"]
    heading = family["all_65_heading_locator_queries"]

    for arm, strict, hits, negatives, total_pool in (
        ("b0", 1, 28, 4, 90),
        ("b1", 6, 39, 3, 90),
        ("b2", 2, 25, 6, 90),
        ("fusion_b0_b1", 4, 37, 3, 109),
        ("fusion_b0_b2", 1, 27, 4, 113),
        ("fusion_b1_b2", 4, 37, 4, 120),
        ("fusion_all", 4, 36, 3, 131),
        ("router", 4, 37, 3, 109),
    ):
        value = old[arm]
        assert value["strict_passes"] == strict
        assert value["positive_hits"] == hits
        assert value["positive_opportunities"] == 39
        assert value["known_distractor_intrusions"] == negatives
        assert value["total_upstream_unique_candidates"] == total_pool
        assert value["total_returned_slots"] == 90

    for arm, top1, top10, mrr, total_pool in (
        ("b0", 45, 64, 0.80359, 650),
        ("b1", 33, 63, 0.65359, 650),
        ("b2", 45, 64, 0.802949, 650),
        ("fusion_b0_b1", 47, 64, 0.834359, 805),
        ("fusion_b0_b2", 45, 64, 0.803223, 875),
        ("fusion_b1_b2", 47, 64, 0.832198, 921),
        ("fusion_all", 43, 64, 0.797582, 1016),
        ("router", 45, 64, 0.80359, 650),
    ):
        value = heading[arm]
        assert value["hit_at_1"] == top1
        assert value["hit_at_10"] == top10
        assert value["mrr_at_10"] == mrr
        assert value["total_returned_slots"] == 650
        assert value["total_upstream_unique_candidates"] == total_pool


def test_all_scenario_rankings_and_query_router_are_deterministically_bounded() -> None:
    from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import metrics
    from experiments.r0_p03_navigation_probe.exploratory_65_source_heading_query_stress import target_score

    data = json.loads(RESULT.read_text(encoding="utf-8"))
    for family, rows in data["observations"].items():
        for row in rows:
            assert set(row["ranked"]) == set(ARMS)
            pool = row["route"]["candidate_pool_sizes"]
            for arm in ARMS:
                ranked = row["ranked"][arm]
                assert 1 <= len(ranked) <= 10
                assert len(set(ranked)) == len(ranked)
                assert pool[arm] >= len(ranked)
                assert pool[arm] <= 30
                if family == "all_65_heading_locator_queries":
                    assert row["scores"][arm] == target_score(ranked, row["target"])
            if family == "all_65_heading_locator_queries":
                assert row["route"]["router_selected"] == "b0"
                assert row["ranked"]["router"] == row["ranked"]["b0"]
            else:
                assert row["route"]["router_selected"] == "fusion_b0_b1"
                assert row["ranked"]["router"] == row["ranked"]["fusion_b0_b1"]
    assert data["router_selection_counts"]["old_nine_subject_queries"] == {
        "b0": 0, "fusion_b0_b1": 9
    }
    assert data["router_selection_counts"]["all_65_heading_locator_queries"] == {
        "b0": 65, "fusion_b0_b1": 0
    }


def test_classification_does_not_claim_formal_architecture_selection() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    assert data["classification"] == "REAL_POSTHOC_EXPLORATORY_HYBRID_RRF_ABLATION_QUERY_ROUTING"
    assert any("NOT governed" in text or "NOT" in text for text in data["limitations"])
    assert any("known" in text.lower() for text in data["limitations"])
    assert data["prior_result_sha256"]["legacy_b01"] == sha256(LEGACY_B01.read_bytes()).hexdigest()
    assert data["prior_result_sha256"]["legacy_b02"] == sha256(LEGACY_B02.read_bytes()).hexdigest()
