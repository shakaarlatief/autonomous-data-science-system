"""Execute an exploratory explicit-citation expansion retrieval proxy.

Not an implementation of R0-P03 B2 CARRIER_LINKS. A literal historical
source-path reference is not a source-authored governing editorial link, J2
realization, or substantive authority. This program tests only whether those
existing mentions can affect retrieval under a fixed, inspectable rule.

The ranking policy, comparison data and interpretive boundaries are fixed
in EXPLORATORY_LEGACY_B2_SOURCE_LINK_PROXY_CONTRACT_V01.md before execution.
The published prior V01 result is checked unchanged before each run.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, CATALOG, OUT as PRIOR_RESULT, ROOT, SCENARIOS,
    load, metrics, source_at_revision, tokenize_query,
)

IDENTIFIER = "R0_P03_EXPLORATORY_LEGACY_B2_EXPLICIT_CITATION_PROXY_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_legacy_b2_source_link_proxy_result_v01.json"
PRIOR_SHA256 = "498bb12d906639642da943e8366194ec8b0c7f6817d20ae5b8fa89a43f8a2acb"
TOP_SEEDS = 5
RETURN_LIMIT = 10
LINK = re.compile(r"(?<![A-Za-z0-9_])docs/[A-Za-z0-9_./-]+\.(?:md|json)(?![A-Za-z0-9_./-])", re.IGNORECASE)


def references(text: str, own_path: str, corpus: set[str]) -> set[str]:
    """Extract explicit literal references only, never infer edge authority.

    Path mentions in text, Markdown code and reference blocks are all treated
    identically. An exact corpus member match is mandatory; trailing prose
    and malformed or unresolved references are excluded, without silently
    substituting another file. Self-edges do not add retrieval information.
    """
    return (set(LINK.findall(text)) & corpus) - {own_path}


def citation_expansion(
    bm25_full_paths: list[str],
    edges: dict[str, set[str]],
    *,
    seed_count: int = TOP_SEEDS,
    limit: int = RETURN_LIMIT,
) -> tuple[list[str], int]:
    """Five literal BM25 seeds, one outbound hop, then baseline fallback.

    Link target priority depends only on frequency among the seeds, shared
    baseline rank and stable full path. The answer/gold file is not an input.
    """
    if len(bm25_full_paths) != len(set(bm25_full_paths)):
        raise ValueError("Duplicate baseline paths")
    if not 1 <= seed_count <= limit <= len(bm25_full_paths):
        raise ValueError("Invalid immutable probe ranking budget")
    seeds = bm25_full_paths[:seed_count]
    chosen = list(seeds)
    seen = set(chosen)
    reference_support = Counter(
        target
        for source in seeds
        for target in edges[source]
        if target not in seen
    )
    rank = {p: pos for pos, p in enumerate(bm25_full_paths)}
    candidates = sorted(
        reference_support,
        key=lambda p: (-reference_support[p], rank.get(p, len(rank)), p),
    )
    added = 0
    for candidate in candidates:
        if len(chosen) == limit:
            break
        if candidate not in seen:
            chosen.append(candidate)
            seen.add(candidate)
            added += 1
    for candidate in bm25_full_paths[seed_count:]:
        if len(chosen) == limit:
            break
        if candidate not in seen:
            chosen.append(candidate)
            seen.add(candidate)
    if len(chosen) != limit or len(set(chosen)) != limit:
        raise AssertionError("Incorrect proxy result budget")
    return chosen, added


def run() -> dict[str, Any]:
    original_bytes = PRIOR_RESULT.read_bytes()
    if sha256(original_bytes).hexdigest() != PRIOR_SHA256:
        raise ValueError("Original V01 empirical result identity changed")
    prior = json.loads(original_bytes)
    scenarios = load(SCENARIOS)
    annotations = load(ANNOTATIONS)
    catalog = load(CATALOG)
    revision = scenarios["source_boundary"]
    if (
        revision != prior["source_revision"]
        or revision != annotations["source_boundary"]
        or revision != catalog["source_boundary"]
    ):
        raise ValueError("Source provenance mismatch")
    paths = sorted(x["path"] for x in annotations["annotations"])
    if len(paths) != 65 or len(set(paths)) != 65 or len(scenarios["scenarios"]) != 9:
        raise ValueError("Prior empirical fixture cardinality changed")
    source = {p: source_at_revision(revision, p).decode("utf-8") for p in paths}
    corpus = set(paths)
    edges = {p: references(source[p], p, corpus) for p in paths}
    count = sum(len(x) for x in edges.values())
    members = sum(bool(x) for x in edges.values())
    if count == 0:
        raise ValueError("No actual source-path citations present; cannot test proxy")
    by_subject = {x["id"]: x for x in catalog["subjects"]}
    by_old_scenario = {r["scenario"]: r for r in prior["scenarios"]}
    if len(by_old_scenario) != len(scenarios["scenarios"]):
        raise ValueError("Missing original experimental scenario")

    connection = sqlite3.connect(":memory:")
    try:
        connection.execute(
            "CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, body, tokenize='unicode61')"
        )
        for path in paths:
            connection.execute("INSERT INTO lex(path,body) VALUES (?,?)", (path, source[path]))
        connection.commit()
        connection.execute("PRAGMA query_only=ON")

        observations = []
        for scenario in scenarios["scenarios"]:
            label = " / ".join(by_subject[s]["label"] for s in scenario["candidate_subjects"])
            query = tokenize_query([by_subject[s]["label"] for s in scenario["candidate_subjects"]])
            full = [
                p for (p,) in connection.execute(
                    "SELECT path FROM lex WHERE lex MATCH ? "
                    "ORDER BY bm25(lex) ASC,path ASC LIMIT 65", (query,)
                )
            ]
            if len(full) < RETURN_LIMIT:
                raise ValueError("Insufficient matched real documents in fixed lexical fixture")
            old = by_old_scenario[scenario["id"]]
            if full[:RETURN_LIMIT] != old["b0_ranked_paths"] or label != old["human_label_query"]:
                raise ValueError("Exact baseline and fixed query drift")
            top, added = citation_expansion(full, edges)
            observations.append({
                "scenario": scenario["id"],
                "human_label_query": label,
                "b0_like": old["b0_like"],
                "b1_like": old["b1_like"],
                "b2_citation_proxy": metrics(top, scenario),
                "b0_ranked_paths": full[:RETURN_LIMIT],
                "b1_ranked_paths": old["b1_ranked_paths"],
                "b2_ranked_paths": top,
                "citation_added_to_seeds": added,
            })
    finally:
        connection.close()

    summary = {}
    for arm in ("b0_like", "b1_like", "b2_citation_proxy"):
        parts = [x[arm] for x in observations]
        required = sum(x["positives"] for x in parts)
        hits = sum(x["true_positive_count"] for x in parts)
        summary[arm] = {
            "scenario_count": len(parts),
            "strict_complete_scenario_passes": sum(x["strict_pass"] for x in parts),
            "relevant_instances_found_at_10": hits,
            "total_relevant_instances": required,
            "micro_recall_at_10": round(hits / required, 6),
            "macro_recall_at_10": round(sum(x["recall_at_10"] for x in parts) / len(parts), 6),
            "explicit_negative_intrusions": sum(x["explicit_negative_intrusions"] for x in parts),
            "returned_slots": sum(x["returned_count"] for x in parts),
        }
    return {
        "identifier": IDENTIFIER,
        "classification": "POSTHOC_EXPLORATORY_REAL_SOURCE_CITATION_PROXY_COMPARISON",
        "original_executed_v01_sha256": PRIOR_SHA256,
        "source_revision": revision,
        "same_historical_original_count": len(paths),
        "scenario_count": len(observations),
        "citation_directed_edge_count": count,
        "citation_source_documents": members,
        "literal_source_path_mentions_are_not_governing_links": True,
        "citation_expansion_seed_budget": TOP_SEEDS,
        "retrieval_limit": RETURN_LIMIT,
        "citation_retrieval_slots_added_across_scenarios": sum(x["citation_added_to_seeds"] for x in observations),
        "limitations": [
            "B2-like explicit path citation proxy, NOT actual governed editorial B2 CARRIER_LINKS",
            "B1 reused authored W5 V0.2 fixture; not independent or blind",
            "No B3/B4, accepted V03 common substrate, fresh 12-primary, independently re-adjudicated legacy gold, current authority or scored architecture decision",
        ],
        "aggregate": summary,
        "observations": observations,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, sort_keys=True, ensure_ascii=True, indent=2) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(data)
    print(json.dumps({
        "identifier": result["identifier"],
        "classification": result["classification"],
        "source_count": result["same_historical_original_count"],
        "scenario_count": result["scenario_count"],
        "citation_directed_edges": result["citation_directed_edge_count"],
        "citation_sources": result["citation_source_documents"],
        "source_link_slots_after_seeds": result["citation_retrieval_slots_added_across_scenarios"],
        "aggregate": result["aggregate"],
        "result_written": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
