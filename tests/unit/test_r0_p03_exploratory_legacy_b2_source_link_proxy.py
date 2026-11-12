"""Deterministic real-source B2-like citation-navigation proxy regression.

The source-link proxy is an empirical retrieval mechanism; it does not
establish governing carrier-to-authority links. Original legacy labels are
known and B1-authored. Assertions test exact execution and protect against
reinterpreting the proxy as official scored B2 or an architecture selection.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    OUT as PRIOR,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import (
    IDENTIFIER, PRIOR_SHA256, RESULT, citation_expansion, references, run,
)

EXACT_BYTES = 27987
EXACT_SHA256 = "136b7037515f97ea253abee6b1d9394a4f7770edddbc108a8174f29b48aae404"


def test_fixed_graph_construction_does_not_hallucinate_paths_or_self_edges() -> None:
    corpus = {"docs/a.md", "docs/b.md", "docs/c.json"}
    raw = "refs docs/b.md and docs/b.md, docs/c.json; unrelated docs/z.md. docs/a.md"
    assert references(raw, "docs/a.md", corpus) == {"docs/b.md", "docs/c.json"}


def test_fixed_one_hop_ranking_and_baseline_fallback_are_deterministic() -> None:
    ranked = [f"docs/{i}.md" for i in range(12)]
    edges = {x: set() for x in ranked}
    edges[ranked[0]] = {ranked[8], ranked[9]}
    edges[ranked[1]] = {ranked[8], ranked[10]}
    edges[ranked[2]] = {ranked[9]}
    chosen, added = citation_expansion(ranked, edges)
    assert chosen == ranked[:5] + [ranked[8], ranked[9], ranked[10], ranked[5], ranked[6]]
    assert added == 3
    no_links, no_additions = citation_expansion(ranked, {x: set() for x in ranked})
    assert no_links == ranked[:10] and no_additions == 0


def test_actual_saved_three_way_result_and_rerun_match_exactly() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXACT_BYTES
    assert sha256(raw).hexdigest() == EXACT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    stored = json.loads(raw)
    assert stored == run()
    assert stored["identifier"] == IDENTIFIER
    assert stored["source_revision"] == "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
    assert stored["same_historical_original_count"] == 65
    assert len(stored["observations"]) == 9
    assert stored["citation_directed_edge_count"] == 110
    assert stored["citation_source_documents"] == 31
    assert stored["citation_retrieval_slots_added_across_scenarios"] == 33
    assert sha256(PRIOR.read_bytes()).hexdigest() == PRIOR_SHA256


def test_reported_metrics_and_unchanged_frozen_baselines() -> None:
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    old = json.loads(PRIOR.read_text(encoding="utf-8"))
    old_by_case = {r["scenario"]: r for r in old["scenarios"]}
    assert result["literal_source_path_mentions_are_not_governing_links"]
    assert result["classification"] == "POSTHOC_EXPLORATORY_REAL_SOURCE_CITATION_PROXY_COMPARISON"
    a = result["aggregate"]
    for arm, passes, relevant, negatives, slots in (
        ("b0_like", 1, 28, 4, 90),
        ("b1_like", 9, 39, 0, 51),
        ("b2_citation_proxy", 2, 25, 6, 90),
    ):
        r = a[arm]
        assert r["strict_complete_scenario_passes"] == passes
        assert r["relevant_instances_found_at_10"] == relevant
        assert r["explicit_negative_intrusions"] == negatives
        assert r["returned_slots"] == slots
        assert r["total_relevant_instances"] == 39
    for row in result["observations"]:
        prior = old_by_case[row["scenario"]]
        assert row["b0_ranked_paths"] == prior["b0_ranked_paths"]
        assert row["b1_ranked_paths"] == prior["b1_ranked_paths"]
        assert row["b0_like"] == prior["b0_like"]
        assert row["b1_like"] == prior["b1_like"]
        assert len(row["b2_ranked_paths"]) == 10
        assert len(set(row["b2_ranked_paths"])) == 10
    assert "NOT actual governed editorial B2 CARRIER_LINKS" in result["limitations"][0]
