"""Executable exploratory fusion and routing with real historical Git source bytes.

This is a posthoc exploratory comparison of three already-defined retrieval
proxies, four fixed reciprocal-rank fusions and one query-only routing switch
over two separately interpreted old public source benchmark families. Neither
family is a fresh independent answer gold, and the source-link arm is not
actual R0-P03 governing B2 editorial links. Read the frozen V01 contract before
using the result for decisions. Never use this pilot to select a physical target.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sqlite3
import sys
import unicodedata
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, CATALOG, OUT as LEGACY_B01, ROOT, SCENARIOS,
    load, metrics, source_at_revision, tokenize_query,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import (
    RESULT as LEGACY_B02, references,
)
from experiments.r0_p03_navigation_probe.exploratory_65_source_heading_query_stress import (
    RESULT as HEADING_PRIOR, citation_route, first_h1, subject_route, target_score,
)

IDENTIFIER = "R0_P03_EXPLORATORY_HYBRID_FUSION_AND_QUERY_ROUTING_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_hybrid_fusion_and_routing_result_v01.json"
PIN = "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
SOURCE_SHA256 = "01206bdb2fdc3517627a94bdf6587efaa2f5d9ed10ad220f5799c496353c5a09"
PRIOR = {
    "legacy_b01": (LEGACY_B01, "498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb"),
    "legacy_b02": (LEGACY_B02, "136b7037515f97ea253abee6b1d9394a4f7770edddbc108a8174f29b48aae404"),
    "heading": (HEADING_PRIOR, "497cdfc559f7d2d56c97b12afb33de1210f5f8bf1945ca9978bd7b73b6ad58b4"),
}
LIMIT = 10
RRF_K = 60
SINGLES = ("b0", "b1", "b2")
FUSIONS = {
    "fusion_b0_b1": ("b0", "b1"),
    "fusion_b0_b2": ("b0", "b2"),
    "fusion_b1_b2": ("b1", "b2"),
    "fusion_all": ("b0", "b1", "b2"),
}
ARMS = SINGLES + tuple(FUSIONS) + ("router",)


def normalized_heading(text: str) -> str:
    """Casefold and collapse whitespace; do not use scenario or target labels."""
    return " ".join(unicodedata.normalize("NFKC", text).casefold().split())


def rrf(
    members: tuple[str, ...],
    lists: dict[str, list[str]],
    lexical_full: list[str],
) -> tuple[list[str], int]:
    """Fixed unweighted reciprocal-rank fusion and lexical tie-breaking.

    Each participating mechanism may supply up to ten unique candidates, so
    the pre-fusion pool may be larger than the returned top ten. No target,
    relevance label, scenario name or answer can affect scores or ranking.
    """
    assert len(members) in (2, 3)
    lexical_position = {path: i for i, path in enumerate(lexical_full)}
    scores: dict[str, float] = {}
    for member in members:
        ranking = lists[member]
        if len(set(ranking)) != len(ranking) or len(ranking) > LIMIT:
            raise ValueError("Duplicate or excessive candidate ranking")
        for rank, path in enumerate(ranking, start=1):
            scores[path] = scores.get(path, 0.0) + 1.0 / (RRF_K + rank)
    ordered = sorted(
        scores,
        key=lambda path: (-scores[path], lexical_position.get(path, len(lexical_full)), path),
    )
    return ordered[:LIMIT], len(scores)


def candidate_outputs(
    *,
    query: str,
    connection: sqlite3.Connection,
    annotations: dict[str, dict[str, Any]],
    subjects: list[dict[str, Any]],
    links: dict[str, set[str]],
    titles_normalized: frozenset[str],
) -> tuple[dict[str, list[str]], dict[str, Any]]:
    """Compute every method solely from the same unlabelled query and source world."""
    full = [
        p for (p,) in connection.execute(
            "SELECT path FROM lex WHERE lex MATCH ? "
            "ORDER BY bm25(lex) ASC,path ASC LIMIT 65",
            (tokenize_query([query]),),
        )
    ]
    if not full:
        raise ValueError("No literal matches in common historical corpus")
    b0 = full[:LIMIT]
    b1, topic = subject_route(query, full, annotations, subjects)
    b2, added = citation_route(full, links)
    singles = {"b0": b0, "b1": b1, "b2": b2}
    fusion = {}
    pools = {name: len(set(value)) for name, value in singles.items()}
    for label, members in FUSIONS.items():
        fusion[label], pools[label] = rrf(members, singles, full)
    exact_title = normalized_heading(query) in titles_normalized
    router_source = "b0" if exact_title else "fusion_b0_b1"
    router = (b0 if exact_title else fusion["fusion_b0_b1"]).copy()
    pools["router"] = pools[router_source]
    ranked = {**singles, **fusion, "router": router}
    if tuple(ranked) != ARMS:
        raise AssertionError("Unexpected hybrid arm list")
    for label, results in ranked.items():
        if len(results) > LIMIT or len(results) != len(set(results)):
            raise AssertionError("Invalid final budget for " + label)
    return ranked, {
        "inferred_subject": topic,
        "exact_heading_query": exact_title,
        "router_selected": router_source,
        "citation_candidates_added": added,
        "candidate_pool_sizes": pools,
    }


def aggregate_legacy(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}
    for arm in ARMS:
        observed = [row["scores"][arm] for row in rows]
        required = sum(v["positives"] for v in observed)
        found = sum(v["true_positive_count"] for v in observed)
        result[arm] = {
            "tasks": len(rows),
            "strict_passes": sum(v["strict_pass"] for v in observed),
            "positive_hits": found,
            "positive_opportunities": required,
            "micro_recall_at_10": round(found / required, 6),
            "macro_recall_at_10": round(sum(v["recall_at_10"] for v in observed) / len(rows), 6),
            "known_distractor_intrusions": sum(v["explicit_negative_intrusions"] for v in observed),
            "total_returned_slots": sum(v["returned_count"] for v in observed),
            "total_upstream_unique_candidates": sum(row["route"]["candidate_pool_sizes"][arm] for row in rows),
        }
    return result


def aggregate_heading(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    result = {}
    for arm in ARMS:
        observed = [row["scores"][arm] for row in rows]
        result[arm] = {
            "tasks": len(rows),
            "hit_at_1": sum(v["hit_at_1"] for v in observed),
            "hit_at_10": sum(v["hit_at_10"] for v in observed),
            "mrr_at_10": round(sum(v["rr_at_10"] for v in observed) / len(rows), 6),
            "total_returned_slots": sum(v["returned_count"] for v in observed),
            "total_upstream_unique_candidates": sum(row["route"]["candidate_pool_sizes"][arm] for row in rows),
        }
    return result


def run() -> dict[str, Any]:
    verified = {}
    for label, (path, digest) in PRIOR.items():
        data = path.read_bytes()
        if sha256(data).hexdigest() != digest:
            raise ValueError("Previously published exploratory result changed: " + label)
        verified[label] = json.loads(data)

    sources = load(ANNOTATIONS)
    catalog = load(CATALOG)
    scenarios = load(SCENARIOS)
    if {sources["source_boundary"], catalog["source_boundary"], scenarios["source_boundary"]} != {PIN}:
        raise ValueError("Source revision does not match exact historical pin")
    descriptions = sources["annotations"]
    if len(descriptions) != 65 or len({a["path"] for a in descriptions}) != 65:
        raise ValueError("Unexpected historical research corpus")
    by_path = {a["path"]: a for a in descriptions}
    paths = sorted(by_path)
    contents_bytes = {p: source_at_revision(PIN, p) for p in paths}
    content_fingerprint = sha256(
        json.dumps(
            [[p, sha256(contents_bytes[p]).hexdigest()] for p in paths],
            separators=(",", ":"), ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()
    if content_fingerprint != SOURCE_SHA256:
        raise ValueError("Actual Git original bytes do not match saved fixture identity")
    bodies = {p: contents_bytes[p].decode("utf-8") for p in paths}
    titles = {p: first_h1(bodies[p]) for p in paths}
    if len(set(titles.values())) != 65 or len({normalized_heading(v) for v in titles.values()}) != 65:
        raise ValueError("Nonunique exact-title metadata")
    title_keys = frozenset(normalized_heading(v) for v in titles.values())
    links = {p: references(bodies[p], p, set(paths)) for p in paths}
    if sum(len(v) for v in links.values()) != 110:
        raise ValueError("Source-link graph drift")
    old_b01 = {r["scenario"]: r for r in verified["legacy_b01"]["scenarios"]}
    old_b02 = {r["scenario"]: r for r in verified["legacy_b02"]["observations"]}
    old_heading = {r["target_historical_path"]: r for r in verified["heading"]["query_observations"]}
    if len(old_b01) != 9 or len(old_b02) != 9 or len(old_heading) != 65:
        raise ValueError("Prior task receipt cardinality drift")

    connection = sqlite3.connect(":memory:")
    try:
        connection.execute(
            "CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, body, tokenize='unicode61')"
        )
        for p in paths:
            connection.execute("INSERT INTO lex(path,body) VALUES (?,?)", (p, bodies[p]))
        connection.commit()
        connection.execute("PRAGMA query_only=ON")

        old_tasks = []
        for scenario in scenarios["scenarios"]:
            sid = scenario["id"]
            query = old_b01[sid]["human_label_query"]
            if query != old_b02[sid]["human_label_query"]:
                raise ValueError("Legacy textual query changed")
            ranked, route = candidate_outputs(
                query=query, connection=connection, annotations=by_path,
                subjects=catalog["subjects"], links=links, titles_normalized=title_keys,
            )
            if ranked["b0"] != old_b01[sid]["b0_ranked_paths"] or ranked["b2"] != old_b02[sid]["b2_ranked_paths"]:
                raise ValueError("Earlier B0/B2 returned ranks disagree with newly executed mechanism")
            gold = {"must_retrieve": scenario["must_retrieve"], "must_not_retrieve": scenario["must_not_retrieve"]}
            old_tasks.append({
                "scenario": sid,
                "query": query,
                "route": route,
                "ranked": ranked,
                "scores": {arm: metrics(ranked[arm], gold) for arm in ARMS},
            })

        heading_tasks = []
        for path in paths:
            query = titles[path]
            known = old_heading[path]
            if query != known["query_from_h1"]:
                raise ValueError("Earlier source heading drift")
            ranked, route = candidate_outputs(
                query=query, connection=connection, annotations=by_path,
                subjects=catalog["subjects"], links=links, titles_normalized=title_keys,
            )
            if any(ranked[arm] != known[f"{arm}_ranked_paths"] for arm in SINGLES):
                raise ValueError("Earlier B0/B1/B2 heading rankings changed")
            heading_tasks.append({
                "target": path,
                "query": query,
                "route": route,
                "ranked": ranked,
                "scores": {arm: target_score(ranked[arm], path) for arm in ARMS},
            })
    finally:
        connection.close()

    aggregate = {
        "old_nine_subject_queries": aggregate_legacy(old_tasks),
        "all_65_heading_locator_queries": aggregate_heading(heading_tasks),
    }
    return {
        "identifier": IDENTIFIER,
        "classification": "REAL_POSTHOC_EXPLORATORY_HYBRID_RRF_ABLATION_QUERY_ROUTING",
        "experiment_contract": "EXPLORATORY_HYBRID_FUSION_AND_QUERY_ROUTING_CONTRACT_V01.md",
        "limitations": [
            "Two known previously scored research query families; not unseen independent gold",
            "Nine original tasks B1-authored and heading targets lexically favored",
            "B1 automatic keyword inference and authored memberships have nonzero historical cost",
            "B2 literal citation proxy is NOT governed source-owned editorial B2",
            "Fusions may inspect up to 30 upstream candidates for ten returned slots",
            "Title router exact-match case reflects query-family setup, not learned generalization",
            "No actual B3 selective concerns, B4 semantic retrieval, formal R0-P03 answer/authority scoring, source admission or physical target selection",
        ],
        "source_pin": PIN,
        "source_members": 65,
        "source_fingerprint_sha256": content_fingerprint,
        "prior_result_sha256": {label: digest for label, (_, digest) in PRIOR.items()},
        "source_title_index_entries": len(title_keys),
        "literal_source_link_edges": sum(len(v) for v in links.values()),
        "rrf_k": RRF_K,
        "returned_budget": LIMIT,
        "all_arms": list(ARMS),
        "family_counts": {"old_nine_subject_queries": len(old_tasks), "all_65_heading_locator_queries": len(heading_tasks)},
        "router_selection_counts": {
            "old_nine_subject_queries": {
                "b0": sum(r["route"]["router_selected"] == "b0" for r in old_tasks),
                "fusion_b0_b1": sum(r["route"]["router_selected"] == "fusion_b0_b1" for r in old_tasks),
            },
            "all_65_heading_locator_queries": {
                "b0": sum(r["route"]["router_selected"] == "b0" for r in heading_tasks),
                "fusion_b0_b1": sum(r["route"]["router_selected"] == "fusion_b0_b1" for r in heading_tasks),
            },
        },
        "b1_inference_counts": {
            "old_nine_subject_queries": sum(r["route"]["inferred_subject"] is not None for r in old_tasks),
            "all_65_heading_locator_queries": sum(r["route"]["inferred_subject"] is not None for r in heading_tasks),
        },
        "aggregate": aggregate,
        "observations": {"old_nine_subject_queries": old_tasks, "all_65_heading_locator_queries": heading_tasks},
        "python_version": sys.version.split()[0],
        "sqlite_version": sqlite3.sqlite_version,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    output = json.dumps(result, sort_keys=True, ensure_ascii=True, indent=2) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(output)
    print(json.dumps({
        "identifier": IDENTIFIER,
        "classification": result["classification"],
        "source_pin": result["source_pin"],
        "families": result["family_counts"],
        "all_arms": result["all_arms"],
        "router_selection_counts": result["router_selection_counts"],
        "b1_inference_counts": result["b1_inference_counts"],
        "aggregate": result["aggregate"],
        "written": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
