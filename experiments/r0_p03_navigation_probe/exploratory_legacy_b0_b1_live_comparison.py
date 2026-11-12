"""Execute a deliberately limited B0-like vs B1-like navigation comparison.

This executable pilot compares two actual retrieval mechanisms over identical
historical source bytes. It is NOT the preregistered R0-P03 scored experiment.
It uses the previously published W5-T1-V02 nine-scenario and 65-carrier fixture,
which is an already explored research fixture, and it does not demonstrate
independent fresh task origination, blind gold, source admission, current
authority, equalized B2/B3/B4 capability, or live source-world validity.

Experiment and limitations:
- Source snapshot: exactly the 65 source paths listed in frozen V0.2 author
  annotations, retrieved as blobs at its recorded Git SHA, not the worktree.
- Queries: each scenario's frozen candidate subject's human-readable label.
  Scenario-specific gold must_retrieve/must_not_retrieve paths are never read by
  either retrieval algorithm; they are evaluated only after both rank lists.
- B0-like: SQLite FTS5 Unicode-token full-text BM25 over all 65 exact texts,
  with a literal-token OR query derived from the human-readable subject labels.
- B1-like: select the union of carriers with authored semantic-subject
  membership in the existing W5 V0.2 research annotation; order selected
  carriers by preferred-subject match, then shared full-text BM25 rank, then
  stable path. This is a semantic metadata addition, not a learned model.
- Both see exactly the same 65 documents and the same query label. B1 alone
  sees the pre-authored subject ID/membership metadata, which is its treatment.
  Thus engineering effort and prior fixture exposure are materially unequal.
- Retrieval budget: at most 10 returned carriers per scenario. Missing matches
  are never silently filled with worktree or future-revision source files.
- Metrics: recall@10 on must-retrieve, explicit must-not intrusions, strict
  complete-scenario pass, micro and macro recall, and top-10 candidate burden.
  This is a document retrieval test, not answer correctness or authority proof.
- Inputs and ranking rules are fixed in this file before pilot results are run;
  no post-run tuning, query editing, or replacement scenarios is permitted.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "experiments" / "project_knowledge_subject_navigation_t1_v02"
SCENARIOS = FIXTURES / "navigation_scenarios_v02.json"
ANNOTATIONS = FIXTURES / "corpus_annotations_v02.json"
CATALOG = FIXTURES / "subject_catalog_candidate_v02.json"
OUT = ROOT / "experiments" / "r0_p03_navigation_probe" / "exploratory_legacy_b0_b1_live_result_v01.json"
LIMIT = 10
STOPWORDS = frozenset({"a", "an", "and", "as", "by", "for", "from", "in", "of", "on", "or", "the", "to", "with"})
PILOT_ID = "R0_P03_EXPLORATORY_LEGACY_B0_B1_REAL_RETRIEVAL_V01"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def source_at_revision(revision: str, path: str) -> bytes:
    if not path.startswith("docs/") or ".." in Path(path).parts:
        raise ValueError("Non-document or traversal source path in fixed fixture")
    x = subprocess.run(
        ["git", "--no-pager", "show", f"{revision}:{path}"],
        cwd=ROOT, check=True, capture_output=True, timeout=15,
    )
    return x.stdout


def tokenize_query(labels: list[str]) -> str:
    words = []
    for label in labels:
        for word in re.findall(r"[a-z0-9]+", label.casefold()):
            if word not in STOPWORDS and len(word) >= 2 and word not in words:
                words.append(word)
    if not words:
        raise ValueError("No usable literal query terms")
    return " OR ".join('"' + w + '"' for w in words)


def metrics(returned: list[str], scenario: dict[str, Any]) -> dict[str, Any]:
    positives = set(scenario["must_retrieve"])
    negatives = set(scenario["must_not_retrieve"])
    hits = positives.intersection(returned)
    intrusions = negatives.intersection(returned)
    return {
        "returned_count": len(returned),
        "positives": len(positives),
        "true_positive_count": len(hits),
        "recall_at_10": round(len(hits) / len(positives), 6),
        "explicit_negative_count": len(negatives),
        "explicit_negative_intrusions": len(intrusions),
        "strict_pass": len(hits) == len(positives) and not intrusions,
    }


def run() -> dict[str, Any]:
    scenarios = load(SCENARIOS)
    annotations = load(ANNOTATIONS)
    catalog = load(CATALOG)
    revisions = {scenarios["source_boundary"], annotations["source_boundary"], catalog["source_boundary"]}
    if len(revisions) != 1 or len(next(iter(revisions))) != 40:
        raise ValueError("Unmatched immutable historical revision")
    revision = revisions.pop()
    if len(scenarios["scenarios"]) != 9:
        raise ValueError("Unexpected scenario count")
    members = annotations["annotations"]
    if len(members) != 65:
        raise ValueError("Unexpected 65-carrier fixture size")
    paths = [record["path"] for record in members]
    if len(set(paths)) != 65:
        raise ValueError("Duplicate source carrier in existing research fixture")
    by_path = {x["path"]: x for x in members}
    by_subject = {x["id"]: x for x in catalog["subjects"]}
    all_gold = set()
    for scenario in scenarios["scenarios"]:
        all_gold.update(scenario["must_retrieve"])
        all_gold.update(scenario["must_not_retrieve"])
        if not scenario["must_retrieve"] or not scenario["candidate_subjects"]:
            raise ValueError("Invalid fixed scenario")
        if set(scenario["must_retrieve"]) & set(scenario["must_not_retrieve"]):
            raise ValueError("Contradictory fixed reference")
        if not set(scenario["candidate_subjects"]) <= set(by_subject):
            raise ValueError("Unknown fixed scenario subject")
    if not all_gold <= set(paths):
        raise ValueError("Reference paths outside common 65-carrier corpus")
    bodies = {p: source_at_revision(revision, p) for p in sorted(paths)}
    contents = {p: raw.decode("utf-8") for p, raw in bodies.items()}
    source_digest = sha256(
        json.dumps([[p, sha256(bodies[p]).hexdigest()] for p in sorted(paths)],
                   separators=(",", ":"), ensure_ascii=True).encode("ascii")
    ).hexdigest()

    conn = sqlite3.connect(":memory:")
    try:
        conn.execute("CREATE VIRTUAL TABLE lex USING fts5(path UNINDEXED, body, tokenize='unicode61')")
        for path in sorted(paths):
            conn.execute("INSERT INTO lex (path,body) VALUES (?,?)", (path, contents[path]))
        conn.commit()
        conn.execute("PRAGMA query_only=ON")
        rows = []
        for scenario in scenarios["scenarios"]:
            subs = scenario["candidate_subjects"]
            phrase = [by_subject[s]["label"] for s in subs]
            query = tokenize_query(phrase)
            ranking = [
                (path, score) for path, score in conn.execute(
                    "SELECT path,bm25(lex) FROM lex WHERE lex MATCH ? "
                    "ORDER BY bm25(lex) ASC,path ASC LIMIT 65", (query,)
                )
            ]
            b0 = [path for path, _ in ranking[:LIMIT]]
            rank = {p: i for i, (p, _score) in enumerate(ranking)}
            eligible = [
                a["path"] for a in members
                if set(a["subjects"]).intersection(subs)
            ]
            b1 = sorted(
                eligible,
                key=lambda p: (
                    0 if by_path[p]["preferred_subject"] in subs else 1,
                    rank.get(p, 65),
                    p,
                ),
            )[:LIMIT]
            rows.append({
                "scenario": scenario["id"],
                "human_label_query": " / ".join(phrase),
                "b0_like": metrics(b0, scenario),
                "b1_like": metrics(b1, scenario),
                "b0_ranked_paths": b0,
                "b1_ranked_paths": b1,
            })
    finally:
        conn.close()

    stats = {}
    for arm in ("b0_like", "b1_like"):
        scored = [row[arm] for row in rows]
        total_relevant = sum(m["positives"] for m in scored)
        total_hits = sum(m["true_positive_count"] for m in scored)
        stats[arm] = {
            "scenarios": len(scored),
            "strict_complete_scenario_passes": sum(m["strict_pass"] for m in scored),
            "micro_recall_at_10": round(total_hits / total_relevant, 6),
            "macro_recall_at_10": round(sum(m["recall_at_10"] for m in scored) / len(scored), 6),
            "explicit_negative_intrusions": sum(m["explicit_negative_intrusions"] for m in scored),
            "returned_carriers_total": sum(m["returned_count"] for m in scored),
            "total_required_positive_instances": total_relevant,
            "positive_instances_found_at_10": total_hits,
        }

    return {
        "pilot_id": PILOT_ID,
        "classification": "ACTUAL_EXECUTED_EXPLORATORY_LEGACY_NAVIGATION_COMPARISON",
        "not": [
            "NOT_ORIGINAL_R0_P03_SCORED_B0_B4_EXPERIMENT",
            "NOT_BLIND_OR_INDEPENDENT_REFERENCE_GOLD",
            "NOT_CURRENT_PROJECT_OR_SOURCE_AUTHORITY_PROOF",
            "NOT_B2_B3_B4_IMPLEMENTATION_OR_COMPARISON",
        ],
        "source_revision": revision,
        "fixed_scenarios": str(SCENARIOS.relative_to(ROOT)).replace("\\", "/"),
        "fixed_annotations": str(ANNOTATIONS.relative_to(ROOT)).replace("\\", "/"),
        "same_historical_source_count": len(paths),
        "source_contents_sha256": source_digest,
        "retrieval_limit": LIMIT,
        "fts5_sqlite_version": sqlite3.sqlite_version,
        "prior_fixture_exposure": "PUBLIC_LEGACY_W5_V02_PREVIOUSLY_USED_IN_SUBJECT_ARCHITECTURE_ACCEPTANCE",
        "method": {
            "b0_like": "LITERAL_LABEL_TERMS_FTS5_BM25_OR_ON_FULL_TEXT",
            "b1_like": "EXISTING_AUTHORED_SEMANTIC_SUBJECT_MEMBERSHIP_PREFERRED_FIRST_SHARED_BM25",
        },
        "aggregate": stats,
        "scenarios": rows,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true",
                        help="Write deterministic real experimental result, fail on preexisting result")
    args = parser.parse_args()
    result = run()
    content = json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.output:
        with OUT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(content)
    print(json.dumps({
        "pilot_id": result["pilot_id"],
        "classification": result["classification"],
        "source_revision": result["source_revision"],
        "source_count": result["same_historical_source_count"],
        "scenario_count": len(result["scenarios"]),
        "retrieval_limit": result["retrieval_limit"],
        "aggregate": result["aggregate"],
        "result_json_written": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
