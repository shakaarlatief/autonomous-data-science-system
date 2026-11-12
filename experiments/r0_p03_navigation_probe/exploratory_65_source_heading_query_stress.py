"""Run an actual 65-query source-heading locator stress test of three mechanisms.

This is a new mechanically generated query family, not a scored R0-P03
reference packet, an independent fresh human-question benchmark, or an
authority/answer-correctness test. The source and authoring fixture remains
the known W5-T1 V0.2 historical 65-carrier research population.

All queries are derived from the first level-one heading of each real
historical source. The target is mechanically the same document. B1 receives
no historical scenario ID or subject choice; it must derive its treatment
route from the heading words with a fully fixed label/description matcher.
B2 uses only explicit historical source-path references, not true
source-authored editorial links or accepted relation semantics.

The complete algorithm and fixed sampling frame are defined in
EXPLORATORY_65_SOURCE_HEADING_QUERY_STRESS_CONTRACT_V01.md.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, CATALOG, ROOT, load, source_at_revision, tokenize_query,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import (
    references,
)

IDENTIFIER = "R0_P03_EXPLORATORY_65_MECHANICAL_FIRST_HEADING_LOCATOR_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_65_source_heading_query_stress_result_v01.json"
CAP = 10
SEEDS = 5
MIN_TOPIC_LABEL_OVERLAP = 1
MIN_TOPIC_TOTAL_OVERLAP = 2
H1 = re.compile(r"^# (.+?)\s*$")
WORD = re.compile(r"[a-z0-9]+")
STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "in", "is", "of", "on", "or", "the", "to", "with",
})


def content_words(text: str) -> set[str]:
    """Tokens used exclusively for query-to-annotated-subject lookup."""
    return {
        token for token in WORD.findall(text.casefold())
        if token not in STOPWORDS and len(token) >= 2
    }


def first_h1(text: str) -> str:
    """No task selection: choose the first literal Markdown H1 or fail."""
    for line in text.splitlines():
        found = H1.fullmatch(line)
        if found:
            head = found.group(1).strip()
            if head:
                return head
    raise ValueError("The complete frozen population must have first H1 headings")


def infer_subject(query: str, subjects: list[dict]) -> str | None:
    """Reproducible arm-internal routing, without target/gold information.

    A subject must overlap at least one label content term and at least two
    distinct label+description terms total. Highest label overlap wins,
    followed by description overlap and lexicographically stable subject ID.
    This keyword heuristic is NOT an LLM semantic classifier or independent
    validation of the actual Research 217 authoring contract.
    """
    words = content_words(query)
    candidates = []
    for item in subjects:
        if not item["assignable"]:
            continue
        label = content_words(item["label"])
        description = content_words(item["description"])
        first = len(words & label)
        second = len(words & description)
        if first >= MIN_TOPIC_LABEL_OVERLAP and first + second >= MIN_TOPIC_TOTAL_OVERLAP:
            candidates.append((-first, -second, item["id"]))
    if not candidates:
        return None
    return min(candidates)[2]


def subject_route(
    text_query: str,
    matches: list[str],
    annotations: dict[str, dict],
    subject_catalog: list[dict],
) -> tuple[list[str], str | None]:
    """Actual subject-membership filtering with no scenario topic ID input."""
    sid = infer_subject(text_query, subject_catalog)
    if sid is None:
        return matches[:CAP], None
    rank = {path: i for i, path in enumerate(matches)}
    eligible = [
        path for path, item in annotations.items()
        if sid in item["subjects"]
    ]
    eligible.sort(key=lambda path: (
        0 if annotations[path]["preferred_subject"] == sid else 1,
        rank.get(path, len(matches)),
        path,
    ))
    chosen = []
    seen = set()
    for path in eligible + matches:
        if len(chosen) == CAP:
            break
        if path not in seen:
            chosen.append(path)
            seen.add(path)
    return chosen, sid


def citation_route(
    lexical_matches: list[str], edges: dict[str, set[str]],
) -> tuple[list[str], int]:
    """Same one-hop citation proxy as prior pilot, permitting short BM25 lists.

    The lexical-only B0 arm never returns nonmatching documents, but the
    citation augmentation may return a source-path-linked document that
    does not itself contain the literal query terms. This difference is
    an intentional observed treatment mechanism, not a source admission.
    """
    seeds = lexical_matches[:SEEDS]
    selected = list(seeds)
    seen = set(seeds)
    supports: dict[str, int] = {}
    for seed in seeds:
        for target in edges[seed]:
            if target not in seen:
                supports[target] = supports.get(target, 0) + 1
    ranks = {path: i for i, path in enumerate(lexical_matches)}
    linked = sorted(
        supports,
        key=lambda path: (-supports[path], ranks.get(path, len(ranks)), path),
    )
    added = 0
    for candidate in linked:
        if len(selected) == CAP:
            break
        if candidate not in seen:
            selected.append(candidate)
            seen.add(candidate)
            added += 1
    for candidate in lexical_matches[SEEDS:]:
        if len(selected) == CAP:
            break
        if candidate not in seen:
            selected.append(candidate)
            seen.add(candidate)
    assert len(selected) == len(set(selected)) and len(selected) <= CAP
    return selected, added


def target_score(paths: list[str], target: str) -> dict[str, Any]:
    """Mechanical exact-target source location only, no historical gold."""
    rank = paths.index(target) + 1 if target in paths else None
    return {
        "target_rank": rank,
        "hit_at_1": rank == 1,
        "hit_at_10": rank is not None,
        "rr_at_10": round(1 / rank, 8) if rank is not None else 0.0,
        "returned_count": len(paths),
    }


def run() -> dict[str, Any]:
    annotations = load(ANNOTATIONS)
    catalog = load(CATALOG)
    rev = annotations["source_boundary"]
    if rev != catalog["source_boundary"]:
        raise ValueError("Historical source revision drift")
    rows = annotations["annotations"]
    if len(rows) != 65 or len(set(a["path"] for a in rows)) != 65:
        raise ValueError("Must test every one of exactly 65 original sources")
    by_path = {a["path"]: a for a in rows}
    corpus = set(by_path)
    docs = {
        p: source_at_revision(rev, p).decode("utf-8")
        for p in sorted(corpus)
    }
    titles = {p: first_h1(docs[p]) for p in sorted(corpus)}
    if len(set(titles.values())) != 65:
        raise ValueError("Ambiguous duplicate heading task targets")
    edges = {p: references(docs[p], p, corpus) for p in sorted(corpus)}
    link_edges = sum(len(targets) for targets in edges.values())
    if link_edges != 110:
        raise ValueError("Historical citation graph changed relative to prior real pilot")
    source_digest = sha256(
        json.dumps(
            [[p, sha256(docs[p].encode("utf-8")).hexdigest()] for p in sorted(corpus)],
            separators=(",", ":"), ensure_ascii=True,
        ).encode("ascii")
    ).hexdigest()

    connection = sqlite3.connect(":memory:")
    try:
        connection.execute(
            "CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, body, tokenize='unicode61')"
        )
        for path in sorted(corpus):
            connection.execute(
                "INSERT INTO lex(path,body) VALUES (?,?)", (path, docs[path])
            )
        connection.commit()
        connection.execute("PRAGMA query_only=ON")
        measured = []
        for target in sorted(corpus):
            query = titles[target]
            expression = tokenize_query([query])
            lexical = [
                p for (p,) in connection.execute(
                    "SELECT path FROM lex WHERE lex MATCH ? "
                    "ORDER BY bm25(lex) ASC,path ASC LIMIT 65", (expression,)
                )
            ]
            if not lexical:
                raise ValueError("No lexical matches for source-derived heading")
            b0 = lexical[:CAP]
            b1, inferred = subject_route(
                query, lexical, by_path, catalog["subjects"]
            )
            b2, added = citation_route(lexical, edges)
            measured.append({
                "target_historical_path": target,
                "query_from_h1": query,
                "b1_inferred_subject": inferred,
                "citation_added_after_seeds": added,
                "b0_ranked_paths": b0,
                "b1_ranked_paths": b1,
                "b2_ranked_paths": b2,
                "b0": target_score(b0, target),
                "b1": target_score(b1, target),
                "b2": target_score(b2, target),
            })
    finally:
        connection.close()

    aggregate = {}
    for key in ("b0", "b1", "b2"):
        observations = [row[key] for row in measured]
        aggregate[key] = {
            "queries": len(observations),
            "hit_at_1": sum(x["hit_at_1"] for x in observations),
            "hit_at_10": sum(x["hit_at_10"] for x in observations),
            "mrr_at_10": round(
                sum(x["rr_at_10"] for x in observations) / len(observations), 6
            ),
            "total_returned_slots": sum(x["returned_count"] for x in observations),
        }

    return {
        "identifier": IDENTIFIER,
        "classification": "REAL_MECHANICALLY_GENERATED_HEADING_DOCUMENT_LOCATION_STRESS",
        "scope_limitations": [
            "All 65 query/targets derived from their own source H1 and mechanically verified, not independent human questions",
            "Known historical 65-document annotated W5 fixture; not blinded or a current ADS source-world release",
            "B0 full-text, B1 heuristic user-query-to-authored-subject routing, B2 literal mention expansion are proxies not equalized full Research 513 arms",
            "No original C01/C02 protected gold, historical answer, authority, governing B2 links, B3 concern obligations or B4 embedding retrieval",
        ],
        "source_revision": rev,
        "source_count": len(corpus),
        "heading_count": len(titles),
        "unique_heading_count": len(set(titles.values())),
        "source_digest": source_digest,
        "literal_directed_citation_edges": link_edges,
        "retrieval_limit": CAP,
        "b1_inferred_topic_count": sum(r["b1_inferred_subject"] is not None for r in measured),
        "b1_fallback_query_count": sum(r["b1_inferred_subject"] is None for r in measured),
        "b2_citation_added_after_seeds": sum(r["citation_added_after_seeds"] for r in measured),
        "aggregate": aggregate,
        "query_observations": measured,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    serialized = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(serialized)
    print(json.dumps({
        "identifier": result["identifier"],
        "source_count": result["source_count"],
        "queries": result["heading_count"],
        "b1_inferred": result["b1_inferred_topic_count"],
        "b1_fallback": result["b1_fallback_query_count"],
        "citation_edges": result["literal_directed_citation_edges"],
        "b2_added_after_seeds": result["b2_citation_added_after_seeds"],
        "aggregate": result["aggregate"],
        "written": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
