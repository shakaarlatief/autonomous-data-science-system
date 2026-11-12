"""Execute a source-grounded directed-link navigation and abstention experiment.

One question in each direction is generated from the first H1 of all 65
historical documents. Answer references are exact literal repository-path
mentions, not trust-qualified governed relations or independent semantic gold.
The directed index shares this parser with the structural oracle; its expected
high score is a functional consistency check, not an unbiased architectural
superiority estimate.

Original preregistered R0-P03 B0-B4 arms are NOT scored here. Previous
exploratory traces are immutable and independently checked before execution.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, CATALOG, ROOT, load, source_at_revision, tokenize_query,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import references
from experiments.r0_p03_navigation_probe.exploratory_65_source_heading_query_stress import first_h1
from experiments.r0_p03_navigation_probe.exploratory_hybrid_fusion_and_routing_v01 import (
    ARMS as PRIOR_ARMS,
    PIN, RRF_K, SOURCE_SHA256, RESULT as PRIOR_RESULT, candidate_outputs,
    normalized_heading, rrf,
)

IDENTIFIER = "R0_P03_EXPLORATORY_DIRECTED_RELATION_AND_ABSTENTION_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_directed_relation_retrieval_result_v01.json"
CONTRACT = "EXPLORATORY_DIRECTED_RELATION_RETRIEVAL_CONTRACT_V01.md"
PRIOR_SHA256 = "e07bcf10e4f04cbde6cbd08b33fb77c02ca17efa03d1a4dbffb73c7a9439334f"
LIMIT = 10
FORWARD_PREFIX = 'Which documents does the document titled "'
FORWARD_SUFFIX = '" explicitly reference by repository path?'
REVERSE_PREFIX = 'Which documents explicitly reference the document titled "'
REVERSE_SUFFIX = '" by repository path?'
ADDITIONAL = (
    "relation_index",
    "relation_b0_naive_rrf",
    "relation_b0_gated_rrf",
    "typed_intent_router",
)
ARMS = PRIOR_ARMS + ADDITIONAL


def relation_question(direction: str, title: str) -> str:
    if direction == "forward":
        return FORWARD_PREFIX + title + FORWARD_SUFFIX
    if direction == "reverse":
        return REVERSE_PREFIX + title + REVERSE_SUFFIX
    raise ValueError("Unknown direction")


def parse_relation_question(query: str, title_index: dict[str, str]) -> tuple[str, str] | None:
    """Parse the exact synthetic request grammar using only visible query text.

    The title resolver comes from source H1 metadata. It never consults the
    oracle target set or any old task ID. Nonmatching queries return None and
    must be delegated without changing previous router behavior.
    """
    for direction, prefix, suffix in (
        ("forward", FORWARD_PREFIX, FORWARD_SUFFIX),
        ("reverse", REVERSE_PREFIX, REVERSE_SUFFIX),
    ):
        if query.startswith(prefix) and query.endswith(suffix):
            title = query[len(prefix):-len(suffix)]
            path = title_index.get(normalized_heading(title))
            if path is not None:
                return direction, path
    return None


def reverse_edges(edges: dict[str, set[str]]) -> dict[str, set[str]]:
    """Exact inverse of the bounded directed literal source-path graph."""
    backward = {source: set() for source in edges}
    for source, targets in edges.items():
        for target in targets:
            if target not in backward or source == target:
                raise ValueError("Invalid directed source graph")
            backward[target].add(source)
    return backward


def rank_neighbors(
    neighbors: set[str],
    full_lexical: list[str],
    *,
    k: int = LIMIT,
) -> list[str]:
    """Order all structurally indexed neighbors by common BM25 rank, then path."""
    lexical_rank = {p: i for i, p in enumerate(full_lexical)}
    return sorted(neighbors, key=lambda p: (lexical_rank.get(p, len(lexical_rank)), p))[:k]


def source_relation_outputs(
    query: str,
    *,
    connection: sqlite3.Connection,
    title_index: dict[str, str],
    outgoing: dict[str, set[str]],
    incoming: dict[str, set[str]],
    annotations: dict[str, dict[str, Any]],
    catalog: list[dict[str, Any]],
    title_set: frozenset[str],
) -> tuple[dict[str, list[str]], dict[str, Any], tuple[str, str]]:
    """Compute every ranker before caller asks for expected graph neighbors."""
    parsed = parse_relation_question(query, title_index)
    if parsed is None:
        raise ValueError("Not one of the fixed directed reference questions")

    ranked, route = candidate_outputs(
        query=query,
        connection=connection,
        annotations=annotations,
        subjects=catalog,
        links=outgoing,
        titles_normalized=title_set,
    )
    full = [
        p for (p,) in connection.execute(
            "SELECT path FROM lex WHERE lex MATCH ? "
            "ORDER BY bm25(lex) ASC,path ASC LIMIT 65",
            (tokenize_query([query]),),
        )
    ]
    direction, source = parsed
    relations = outgoing if direction == "forward" else incoming
    neighbors = relations[source]
    indexed = rank_neighbors(neighbors, full)
    # The index is sourced from document-body mentions, not external gold.
    naive, union_size = rrf(("relation_index", "b0"), {
        "relation_index": indexed, "b0": ranked["b0"],
    }, full)
    gated = naive.copy() if indexed else []
    typed = indexed.copy()
    combined = {
        **ranked,
        "relation_index": indexed,
        "relation_b0_naive_rrf": naive,
        "relation_b0_gated_rrf": gated,
        "typed_intent_router": typed,
    }
    if tuple(combined) != ARMS:
        raise AssertionError("Unexpected directed relation comparison arms")
    pools = {
        **route["candidate_pool_sizes"],
        "relation_index": len(indexed),
        "relation_b0_naive_rrf": union_size,
        "relation_b0_gated_rrf": union_size if indexed else 0,
        "typed_intent_router": len(indexed),
    }
    for name, values in combined.items():
        if len(values) > LIMIT or len(values) != len(set(values)):
            raise ValueError("Invalid output budget for " + name)
        if pools[name] < len(values):
            raise AssertionError("Candidate pool smaller than output")
    return combined, {
        "parsed_direction": direction,
        "source_h1_lookup_succeeded": True,
        "relation_index_nonempty": bool(indexed),
        "relation_index_truncated_by_k": len(neighbors) > LIMIT,
        "old_b1_topic_inferred": route["inferred_subject"],
        "old_router_selected": route["router_selected"],
        "candidate_pool_sizes": pools,
    }, parsed


def graph_score(ranked: list[str], expected: set[str]) -> dict[str, Any]:
    """Mechanically evaluate exact directed path-mention set against top ten.

    Empty references are not counted as vacuous perfect recall. Exact-set
    success requires equality of full sets, and is impossible for >K neighbors.
    """
    actual = set(ranked)
    if len(ranked) != len(actual) or len(ranked) > LIMIT:
        raise ValueError("Invalid ranked list for structural score")
    positives = len(actual & expected)
    extras = len(actual - expected)
    return {
        "required_count": len(expected),
        "retrieved_required_count": positives,
        "irrelevant_to_raw_graph_count": extras,
        "returned_count": len(ranked),
        "positive_recall_at_10": round(positives / len(expected), 6) if expected else None,
        "exact_set": actual == expected,
        "empty_target_correct_abstention": (not ranked) if not expected else None,
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    totals = {}
    for arm in ARMS:
        scores = [row["scores"][arm] for row in rows]
        positive = [s for s in scores if s["required_count"]]
        zeros = [s for s in scores if not s["required_count"]]
        required = sum(s["required_count"] for s in positive)
        found = sum(s["retrieved_required_count"] for s in positive)
        totals[arm] = {
            "questions": len(scores),
            "positive_questions": len(positive),
            "empty_questions": len(zeros),
            "required_link_instances": required,
            "required_instances_found_at_10": found,
            "micro_positive_recall_at_10": round(found / required, 6) if required else None,
            "mean_positive_query_recall_at_10": round(
                sum(s["positive_recall_at_10"] for s in positive) / len(positive), 6
            ) if positive else None,
            "exact_set_questions": sum(s["exact_set"] for s in scores),
            "correct_empty_abstentions": sum(s["empty_target_correct_abstention"] for s in zeros),
            "empty_questions_returning_any_results": sum(bool(s["returned_count"]) for s in zeros),
            "false_positive_slots_on_empty_questions": sum(s["returned_count"] for s in zeros),
            "irrelevant_to_graph_slots_all_questions": sum(s["irrelevant_to_raw_graph_count"] for s in scores),
            "returned_slots_all_questions": sum(s["returned_count"] for s in scores),
            "upstream_candidate_union_instances": sum(
                row["route"]["candidate_pool_sizes"][arm] for row in rows
            ),
        }
    return totals


def run() -> dict[str, Any]:
    prior_bytes = PRIOR_RESULT.read_bytes()
    if sha256(prior_bytes).hexdigest() != PRIOR_SHA256:
        raise ValueError("Published Checkpoint 908 result changed")
    prior = json.loads(prior_bytes)
    if prior["source_pin"] != PIN or prior["source_fingerprint_sha256"] != SOURCE_SHA256:
        raise ValueError("Published source corpus identity changed")

    annotations = load(ANNOTATIONS)
    catalog = load(CATALOG)
    if annotations["source_boundary"] != PIN or catalog["source_boundary"] != PIN:
        raise ValueError("Historical source pin mismatch")
    rows = annotations["annotations"]
    if len(rows) != 65 or len({r["path"] for r in rows}) != 65:
        raise ValueError("Exact 65-document source population changed")
    by_path = {r["path"]: r for r in rows}
    paths = sorted(by_path)
    originals = {p: source_at_revision(PIN, p) for p in paths}
    fingerprint = sha256(
        json.dumps(
            [[p, sha256(originals[p]).hexdigest()] for p in paths],
            separators=(",", ":"), ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()
    if fingerprint != SOURCE_SHA256:
        raise ValueError("Original Git file contents changed")
    bodies = {p: original.decode("utf-8") for p, original in originals.items()}
    titles = {p: first_h1(bodies[p]) for p in paths}
    title_lookup = {normalized_heading(title): p for p, title in titles.items()}
    if len(title_lookup) != 65:
        raise ValueError("Nonunique normalized source title")
    edges = {p: references(bodies[p], p, set(paths)) for p in paths}
    incoming = reverse_edges(edges)
    assert sum(map(len, edges.values())) == sum(map(len, incoming.values())) == 110

    outgoing_positive = sum(bool(values) for values in edges.values())
    incoming_positive = sum(bool(values) for values in incoming.values())
    budget_truncated = sum(len(x) > LIMIT for x in list(edges.values()) + list(incoming.values()))
    if (outgoing_positive, incoming_positive, budget_truncated) != (31, 39, 2):
        raise ValueError("Actual historical graph task preflight drift")
    total_instances = 2 * sum(len(v) for v in edges.values())
    max_observable = sum(min(len(x), LIMIT) for x in list(edges.values()) + list(incoming.values()))
    assert (total_instances, max_observable) == (220, 208)

    connection = sqlite3.connect(":memory:")
    try:
        connection.execute(
            "CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, body, tokenize='unicode61')"
        )
        for p in paths:
            connection.execute("INSERT INTO lex(path,body) VALUES (?,?)", (p, bodies[p]))
        connection.commit()
        connection.execute("PRAGMA query_only=ON")

        observations = []
        for direction in ("forward", "reverse"):
            links = edges if direction == "forward" else incoming
            for source in paths:
                query = relation_question(direction, titles[source])
                # First compute every ranker without passing expected target paths.
                ranked, metadata, parsed = source_relation_outputs(
                    query, connection=connection, title_index=title_lookup,
                    outgoing=edges, incoming=incoming, annotations=by_path,
                    catalog=catalog["subjects"],
                    title_set=frozenset(title_lookup),
                )
                if parsed != (direction, source):
                    raise AssertionError("Source title / direction parser drift")
                expected = links[source]
                observations.append({
                    "direction": direction,
                    "query": query,
                    "source_historical_path": source,
                    "expected_literal_relation_targets": sorted(expected),
                    "route": metadata,
                    "ranked": ranked,
                    "scores": {
                        arm: graph_score(ranked[arm], expected)
                        for arm in ARMS
                    },
                })

        # Old 74 known previous queries are a regression only, never rescored.
        regression = {"old_nine_subject_queries": 0, "all_65_heading_locator_queries": 0}
        for family, original_rows in prior["observations"].items():
            for old in original_rows:
                query = old["query"]
                if parse_relation_question(query, title_lookup) is not None:
                    raise AssertionError("Old nonrelation query parsed as new typed relation")
                ranked, _ = candidate_outputs(
                    query=query, connection=connection, annotations=by_path,
                    subjects=catalog["subjects"], links=edges,
                    titles_normalized=frozenset(title_lookup),
                )
                if ranked["router"] != old["ranked"]["router"]:
                    raise AssertionError("Original nonrelation router behavior changed")
                regression[family] += 1
        if regression != {"old_nine_subject_queries": 9, "all_65_heading_locator_queries": 65}:
            raise ValueError("Old 74-query regression not exhaustive")
    finally:
        connection.close()

    outputs_by_direction = {
        direction: [r for r in observations if r["direction"] == direction]
        for direction in ("forward", "reverse")
    }
    if len(observations) != 130:
        raise AssertionError("Missing a structural reference task")
    return {
        "identifier": IDENTIFIER,
        "classification": "SOURCE_DERIVED_EXPLORATORY_RELATION_INDEX_FUNCTION_AND_ABSTENTION_TEST",
        "experimental_contract": CONTRACT,
        "formal_r0_p03_scored": False,
        "limitations": [
            "Gold and directed relation-index share the same literal source-path extractor; graph-index perfection is mechanically expected, not blind generalization.",
            "Every question is generated from a known historical H1 and fixed typed relation grammar; title resolution and intent classification are synthetic.",
            "Absent path mentions within the 65 bodies do not prove absent real relationships, executions, or governing obligations.",
            "Literal source-path references are not authority-validated editorial B2 links or actual B3 selective concerns.",
            "Other arms have unequal metadata authoring/graph construction costs, B2 remains a proxy, and no B4 model, answer key, primary 12-task P03 score or physical architecture target is selected.",
        ],
        "historical_revision": PIN,
        "source_body_fingerprint_sha256": fingerprint,
        "prior_checkpoint_908_result_sha256": PRIOR_SHA256,
        "source_documents": len(paths),
        "outbound_reference_edges": sum(len(v) for v in edges.values()),
        "inbound_reference_edges": sum(len(v) for v in incoming.values()),
        "positive_forward_questions": outgoing_positive,
        "positive_reverse_questions": incoming_positive,
        "questions": len(observations),
        "zero_target_questions": len(observations) - outgoing_positive - incoming_positive,
        "required_directed_relation_instances": total_instances,
        "maximum_achievable_required_hits_at_k10": max_observable,
        "over_budget_relation_questions": budget_truncated,
        "return_limit": LIMIT,
        "rrf_k": RRF_K,
        "arm_names": list(ARMS),
        "nonrelation_router_regression": regression,
        "aggregate": {
            "all_130_relation_questions": aggregate(observations),
            "forward_65": aggregate(outputs_by_direction["forward"]),
            "reverse_65": aggregate(outputs_by_direction["reverse"]),
        },
        "observations": observations,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(data)
    print(json.dumps({
        "identifier": result["identifier"],
        "classification": result["classification"],
        "source_documents": result["source_documents"],
        "edge_count": result["outbound_reference_edges"],
        "tasks": result["questions"],
        "empty_tasks": result["zero_target_questions"],
        "over_budget_tasks": result["over_budget_relation_questions"],
        "maximum_observable_hits": result["maximum_achievable_required_hits_at_k10"],
        "nonrelation_router_regression": result["nonrelation_router_regression"],
        "aggregate": result["aggregate"]["all_130_relation_questions"],
        "result_written": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
