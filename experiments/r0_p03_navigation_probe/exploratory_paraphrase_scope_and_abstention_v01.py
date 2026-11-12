"""Execute 719 fixed historical relation-wording and evidence-scope queries.

This is an exploratory implementation and coverage test, not a blind
natural-language interpretation benchmark. The guarded parser and the query
families were specified before execution. The answer oracle and relation
operator use the same historical literal-path-mention graph, so graph index
coverage is structurally expected only when intent recognition succeeds.

The program never promotes a raw file mention into a dependency, authority,
governed link or functioning hyperlink. Such requests abstain explicitly.
"""
from __future__ import annotations

from hashlib import sha256
import json
import re
from pathlib import Path
import sqlite3
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, ROOT, load, source_at_revision, tokenize_query,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import references
from experiments.r0_p03_navigation_probe.exploratory_65_source_heading_query_stress import first_h1
from experiments.r0_p03_navigation_probe.exploratory_hybrid_fusion_and_routing_v01 import (
    PIN, SOURCE_SHA256, normalized_heading,
)
from experiments.r0_p03_navigation_probe.exploratory_directed_relation_retrieval_v01 import (
    RESULT as PREVIOUS, parse_relation_question, rank_neighbors, reverse_edges,
)

IDENTIFIER = "R0_P03_EXPLORATORY_RELATION_PARAPHRASE_SCOPE_ABSTENTION_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_paraphrase_scope_and_abstention_result_v01.json"
PREVIOUS_SHA256 = "99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399"
CONTRACT = "EXPLORATORY_PARAPHRASE_SCOPE_AND_ABSTENTION_CONTRACT_V01.md"
LIMIT = 10
FAMILIES: dict[str, dict[str, str]] = {
    "S1": {
        "forward": 'In "{title}", which other documents are referenced by repository path?',
        "reverse": 'Which documents reference "{title}" by repository path?',
    },
    "S2": {
        "forward": 'List the docs/ paths mentioned inside "{title}".',
        "reverse": 'Find files that mention "{title}" via a docs/ path.',
    },
    "H1": {
        "forward": 'Which file paths are explicitly cited within "{title}"?',
        "reverse": 'Where is "{title}" explicitly cited by file path?',
    },
    "H2": {
        "forward": 'Give outbound docs/ path citations for "{title}".',
        "reverse": 'Give inbound docs/ path citations for "{title}".',
    },
}
UNSUPPORTED_FAMILIES = {
    "U1_dependency": 'Which documents actually depend on "{title}" in practice?',
    "U2_governance": 'Which documents does "{title}" govern authoritatively?',
    "U3_hyperlink": 'Which documents contain working hyperlinks to "{title}"?',
}
UNSUPPORTED_TOKENS = (
    "depend", "govern", "authorit", "hyperlink",
    "working link", "actually related",
)
ANCHORS = ("repository path", "file path", "file paths", "docs/")
CUES = ("referenc", "mention", "cit")
FORWARD_ENDING = re.compile(r"(?:^|\s)(?:in|inside|within)\s*$", re.IGNORECASE)
REVERSE_PREFIXES = (
    "which documents reference",
    "find files that mention",
    "where is",
)
ABSTENTION_STATES = (
    "unsupported_scope",
    "unparsed_in_scope",
    "unknown_title",
    "ambiguous_title",
    "malformed_unquoted_title",
)


def classify_intent(
    query: str,
    titles: dict[str, str],
) -> tuple[str, tuple[str, str] | None]:
    """Return explicit state plus an optional (direction, source-path) pair.

    Source-title lookup and intent parsing never receive expected neighbors,
    benchmark labels, source status or an answer. Disallowed real-world claim
    scopes must not fall back to lexical *relation answers*. Unknown and
    ambiguous identities must remain distinguishable from evidence absence.
    """
    parts = query.split('"')
    if len(parts) > 3:
        return "ambiguous_title", None
    if len(parts) != 3 or not parts[1].strip():
        return "malformed_unquoted_title", None
    before, title, after = parts
    path = titles.get(normalized_heading(title))
    if path is None:
        return "unknown_title", None
    context = normalized_heading(before + " " + after)
    if any(item in context for item in UNSUPPORTED_TOKENS):
        return "unsupported_scope", None
    if not any(item in context for item in ANCHORS):
        return "unsupported_scope", None
    if not any(item in context for item in CUES):
        return "unsupported_scope", None
    if FORWARD_ENDING.search(before):
        return "recognized_forward", ("forward", path)
    if any(normalized_heading(before).startswith(x) for x in REVERSE_PREFIXES):
        return "recognized_reverse", ("reverse", path)
    return "unparsed_in_scope", None


def unique_task_population(
    titles: dict[str, str],
) -> list[dict[str, Any]]:
    """Complete source-first population, without answer-dependent filtering."""
    tasks = []
    for family, patterns in FAMILIES.items():
        for direction in ("forward", "reverse"):
            for path in sorted(titles):
                tasks.append({
                    "family": family,
                    "direction": direction,
                    "source": path,
                    "query": patterns[direction].format(title=titles[path]),
                    "scope": "literal_path_mention",
                })
    for family, template in UNSUPPORTED_FAMILIES.items():
        for path in sorted(titles):
            tasks.append({
                "family": family,
                "direction": None,
                "source": path,
                "query": template.format(title=titles[path]),
                "scope": "unqualified_real_world_claim",
            })
    unknown = "Unknown source outside historical snapshot"
    tasks.extend([
        {
            "family": "X_unknown_forward",
            "direction": "forward",
            "source": None,
            "query": FAMILIES["S1"]["forward"].format(title=unknown),
            "scope": "unresolved_identity",
        },
        {
            "family": "X_unknown_reverse",
            "direction": "reverse",
            "source": None,
            "query": FAMILIES["S1"]["reverse"].format(title=unknown),
            "scope": "unresolved_identity",
        },
    ])
    source_paths = sorted(titles)
    t0, t1 = titles[source_paths[0]], titles[source_paths[1]]
    tasks.extend([
        {
            "family": "X_ambiguous_forward",
            "direction": "forward",
            "source": None,
            "query": f'In "{t0}" and "{t1}", which other documents are referenced by repository path?',
            "scope": "ambiguous_identity",
        },
        {
            "family": "X_ambiguous_reverse",
            "direction": "reverse",
            "source": None,
            "query": f'Which documents reference "{t0}" or "{t1}" by repository path?',
            "scope": "ambiguous_identity",
        },
    ])
    if len(tasks) != 719 or len({t["query"] for t in tasks}) != 719:
        raise ValueError("New task population must contain 719 unique queries")
    return tasks


def lexical_candidates(connection: sqlite3.Connection, query: str) -> list[str]:
    """Pure source text candidates, not asserted relationship answers."""
    return [
        p for (p,) in connection.execute(
            "SELECT path FROM lex WHERE lex MATCH ? "
            "ORDER BY bm25(lex) ASC,path ASC LIMIT 65",
            (tokenize_query([query]),),
        )
    ]


def run() -> dict[str, Any]:
    if sha256(PREVIOUS.read_bytes()).hexdigest() != PREVIOUS_SHA256:
        raise ValueError("Previous 130-question result was mutated")
    prior = json.loads(PREVIOUS.read_text(encoding="utf-8"))
    if prior["historical_revision"] != PIN or prior["source_body_fingerprint_sha256"] != SOURCE_SHA256:
        raise ValueError("Historical source identity drift")
    annotations = load(ANNOTATIONS)
    if annotations["source_boundary"] != PIN:
        raise ValueError("Original source boundary drift")
    records = annotations["annotations"]
    paths = sorted(item["path"] for item in records)
    if len(paths) != 65 or len(set(paths)) != 65:
        raise ValueError("Expected exactly 65 historical originals")
    sources = {p: source_at_revision(PIN, p) for p in paths}
    digest = sha256(json.dumps(
        [[p, sha256(sources[p]).hexdigest()] for p in paths],
        separators=(",", ":"), ensure_ascii=True,
    ).encode("ascii")).hexdigest()
    if digest != SOURCE_SHA256:
        raise ValueError("Original Git byte identity mismatch")
    bodies = {p: raw.decode("utf-8") for p, raw in sources.items()}
    titles = {p: first_h1(bodies[p]) for p in paths}
    if len({normalized_heading(t) for t in titles.values()}) != 65:
        raise ValueError("Nonunique original headings")
    if any('"' in title for title in titles.values()):
        raise ValueError("Quoted heading unsupported in this fixed evaluator")
    heading_index = {normalized_heading(title): p for p, title in titles.items()}
    outgoing = {p: references(bodies[p], p, set(paths)) for p in paths}
    incoming = reverse_edges(outgoing)
    if (sum(map(len, outgoing.values())), sum(map(len, incoming.values()))) != (110, 110):
        raise ValueError("Source path-mention graph was modified")

    tasks = unique_task_population(titles)
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
        for task in tasks:
            query = task["query"]
            old = parse_relation_question(query, heading_index)
            state, parsed = classify_intent(query, heading_index)
            lexical_full = lexical_candidates(connection, query)
            lexical_top = lexical_full[:LIMIT]
            proposed = []
            if parsed is not None:
                direction, source = parsed
                proposed = rank_neighbors(
                    outgoing[source] if direction == "forward" else incoming[source],
                    lexical_full,
                )
                if not proposed:
                    state = "no_matching_literal_mentions"
            else:
                if proposed:
                    raise AssertionError("Rejected query emitted relation assertions")

            if task["scope"] == "literal_path_mention":
                expected = (outgoing if task["direction"] == "forward" else incoming)[task["source"]]
                hits = len(set(proposed) & expected)
                wrong = len(set(proposed) - expected)
                correct_direction = parsed == (task["direction"], task["source"])
                evaluation = {
                    "required": len(expected),
                    "found": hits,
                    "irrelevant_relation_assertions": wrong,
                    "exact_set": set(proposed) == expected,
                    "direction_recognized": correct_direction,
                    "correct_no_edge_state": (
                        state == "no_matching_literal_mentions"
                        if not expected else None
                    ),
                }
            else:
                expected = set()
                evaluation = {
                    "required": None,
                    "found": None,
                    "irrelevant_relation_assertions": len(proposed),
                    "exact_set": None,
                    "direction_recognized": None,
                    "correct_no_edge_state": None,
                    "safe_abstention": (
                        not proposed
                        and state == (
                            "unsupported_scope" if task["scope"] == "unqualified_real_world_claim"
                            else "unknown_title" if task["family"].startswith("X_unknown")
                            else "ambiguous_title"
                        )
                    ),
                }
            observations.append({
                **task,
                "old_exact_grammar_recognized": old is not None,
                "guarded_state": state,
                "guarded_parsed": list(parsed) if parsed else None,
                "asserted_literal_relation_paths": proposed,
                "lexical_candidate_paths": lexical_top,
                "reference_targets_for_structural_audit": sorted(expected)
                    if task["scope"] == "literal_path_mention" else None,
                "evaluation": evaluation,
            })
    finally:
        connection.close()

    groups: dict[str, list[dict[str, Any]]] = {}
    for row in observations:
        groups.setdefault(row["family"], []).append(row)
    results = {}
    for name, group in groups.items():
        if name in FAMILIES:
            total = sum(row["evaluation"]["required"] for row in group)
            hits = sum(row["evaluation"]["found"] for row in group)
            ceiling = sum(min(row["evaluation"]["required"], LIMIT) for row in group)
            results[name] = {
                "scope": "literal_path_mention",
                "questions": len(group),
                "required_reference_instances": total,
                "found_reference_instances": hits,
                "top10_ceiling": ceiling,
                "positive_questions": sum(row["evaluation"]["required"] > 0 for row in group),
                "structurally_empty_questions": sum(row["evaluation"]["required"] == 0 for row in group),
                "direction_recognized": sum(row["evaluation"]["direction_recognized"] for row in group),
                "exact_structural_sets": sum(row["evaluation"]["exact_set"] for row in group),
                "correct_no_edge_states": sum(row["evaluation"]["correct_no_edge_state"] is True for row in group),
                "old_exact_parser_recognized": sum(row["old_exact_grammar_recognized"] for row in group),
                "unparsed_in_scope": sum(row["guarded_state"] == "unparsed_in_scope" for row in group),
                "lexical_candidate_slots": sum(len(row["lexical_candidate_paths"]) for row in group),
            }
        else:
            results[name] = {
                "scope": group[0]["scope"],
                "questions": len(group),
                "safe_abstentions": sum(row["evaluation"]["safe_abstention"] for row in group),
                "unsupported_relational_assertions": sum(len(row["asserted_literal_relation_paths"]) for row in group),
                "lexical_candidate_slots": sum(len(row["lexical_candidate_paths"]) for row in group),
                "old_exact_parser_recognized": sum(row["old_exact_grammar_recognized"] for row in group),
            }

    if (len(observations), sum(results[k]["required_reference_instances"] for k in FAMILIES)) != (719, 880):
        raise AssertionError("Full fixed cohort or target cardinality changed")
    if sum(results[k]["top10_ceiling"] for k in FAMILIES) != 832:
        raise AssertionError("Expected K=10 structural ceiling changed")
    return {
        "identifier": IDENTIFIER,
        "classification": "EXPLORATORY_FINITE_WORDING_ROBUSTNESS_AND_EVIDENCE_SCOPE",
        "source_pin": PIN,
        "source_fingerprint_sha256": digest,
        "prior_checkpoint_909_result_sha256": PREVIOUS_SHA256,
        "contract": CONTRACT,
        "source_documents": len(paths),
        "directed_literal_reference_edges": 110,
        "new_queries": len(observations),
        "semantic_scope_limitations": [
            "All four source-mention paraphrase patterns were hand-authored before execution, not independent user utterances or an unseen natural-language distribution.",
            "Source graph and structural scorer share the exact path-mention extractor; high index scores are expected when parser resolves intent.",
            "Held-out H1/H2 wording is held out of parser-design examples, but not independent of author's conceptual study; failures remain uncorrected.",
            "Unsupported actual dependency, governance and hyperlink questions are deliberately rejected, not answered negatively.",
            "Lexical B0 returns candidates only; a returned lexical document is not an asserted false relationship or generated answer.",
            "No source-owned governed B2/B3 semantics, execution receipts, independent answer gold, B4, or scored Research 513 architecture selection.",
        ],
        "top10_limit": LIMIT,
        "families": results,
        "observations": observations,
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    data = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(data)
    print(json.dumps({
        "identifier": result["identifier"],
        "source_count": result["source_documents"],
        "questions": result["new_queries"],
        "families": result["families"],
        "saved": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
