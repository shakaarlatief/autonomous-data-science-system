"""Execute Route B's first 12-question source-grounded primary B0 baseline.

The twelve exposed coordinator-authored questions and source-backed answer
anchors were frozen before this implementation was constructed. Only
retrieval of one cited required source per case is evaluated. This is
not the original blind B0–B4 trial, and the title/char/fusion comparators
are non-arm diagnostics rather than fraudulent B1/B2/B3/B4 replacements.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import io
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import tarfile
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_t2_no_id_retrieval_and_selective_evidence_v04 import (
    ROOT, fts_query, sparse_char_index, char_rank, rrf_fusion,
)

PIN = "47ed6344a9153dcf366769e95722840fbf1a8f8b"
CONTRACT = "ROUTE_B_FIRST_PRIMARY_BASELINE_EXECUTION_CONTRACT_V01.md"
TASKS = ROOT / "experiments/r0_p03_navigation_probe/ROUTE_B_PRIMARY_12_SOURCE_ANSWER_MANIFEST_V01.json"
TASK_BYTES = 9784
TASK_SHA = "c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/route_b_primary_b0_baseline_result_v01.json"
BUILD_PREFIX = "R0_P03_ROUTE_B_BUILD_V01"
HOLDOUT_PREFIX = "R0_P03_ROUTE_B_HELDOUT_V01"
FILL = {"research": 20, "checkpoint": 16, "specification": 4, "foundation": 4, "tool": 4}
HOLDOUT = {"research": 8, "checkpoint": 8, "specification": 2, "foundation": 1, "tool": 1}
RANKERS = (
    "B0_SUBSTRATE_LEXICAL_BASELINE",
    "TITLE_LEXICAL_DIAGNOSTIC",
    "CHAR_TRIGRAM_DIAGNOSTIC",
    "DIAGNOSTIC_THREE_WAY_RRF",
)
K = 10
INDEX_CHAR_LIMIT = 12000


def git(*args: str) -> bytes:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, check=True, timeout=25
    ).stdout


def classify_path(path: str) -> str | None:
    """Classify by exact path strata, never by whether it supports a query."""
    if path in ("docs/CURRENT_STATE.md", "docs/DECISIONS.md"):
        return "root_primary"
    if path.startswith("docs/research/") and "/" not in path[len("docs/research/"):] and path.endswith(".md"):
        return "research"
    if path.startswith("docs/checkpoints/") and "/" not in path[len("docs/checkpoints/"):] and path.endswith(".md"):
        return "checkpoint"
    if path.startswith("docs/specifications/") and "/" not in path[len("docs/specifications/"):] and path.endswith(".md"):
        return "specification"
    if path.startswith("docs/foundations/") and "/" not in path[len("docs/foundations/"):] and path.endswith(".md"):
        return "foundation"
    if path.startswith("tools/") and path.endswith(".py"):
        return "tool"
    return None


def prospective_draw(required_paths: set[str]) -> tuple[list[str], list[str], dict[str, Any]]:
    """Select candidate original Git paths using fixed hash strata and 60/20.

    Required source closure is included before any fill/draw, without
    retrieving results or selecting what an existing ranker finds easy.
    """
    names = git("ls-tree", "-r", "--name-only", PIN).decode("utf-8").splitlines()
    eligible = {path: classify_path(path) for path in names}
    eligible = {p: category for p, category in eligible.items() if category is not None}
    if not required_paths <= set(eligible):
        raise ValueError(f"Missing required source closure: {sorted(required_paths - set(eligible))}")
    if len(required_paths) != 12:
        raise ValueError("The frozen task manifest must contain 12 distinct required source carriers")

    def ordered(name: str, paths: list[str], role: str) -> list[str]:
        return sorted(
            paths,
            key=lambda p: (sha256(f"{name}|{role}|{p}".encode("utf-8")).hexdigest(), p),
        )

    build = set(required_paths)
    fill_details = {}
    for kind, quota in FILL.items():
        candidates = ordered(
            BUILD_PREFIX, [p for p, role in eligible.items() if role == kind and p not in build], kind
        )
        if len(candidates) < quota:
            raise ValueError(f"Insufficient {kind} original Git build candidates")
        new = candidates[:quota]
        build.update(new)
        fill_details[kind] = len(new)
    if len(build) != 60:
        raise ValueError(f"Build target 60 violated: {len(build)}")

    held = set()
    hold_details = {}
    for kind, quota in HOLDOUT.items():
        candidates = ordered(
            HOLDOUT_PREFIX,
            [p for p, role in eligible.items() if role == kind and p not in build],
            kind,
        )
        if len(candidates) < quota:
            raise ValueError(f"Insufficient {kind} original Git heldout candidates")
        new = candidates[:quota]
        held.update(new)
        hold_details[kind] = len(new)
    if len(held) != 20 or build & held:
        raise ValueError("Heldout is not exactly 20 source-distinct carriers")

    return sorted(build), sorted(held), {
        "original_eligible_source_path_count": len(eligible),
        "eligible_path_counts_by_role": dict(sorted(Counter(eligible.values()).items())),
        "source_required_closure_count": len(required_paths),
        "build_count": len(build),
        "heldout_count": len(held),
        "build_filler_quotas": fill_details,
        "heldout_quotas": hold_details,
        "strata_are_path_heuristics_not_source_authority": True,
        "representative_role_semantics_or_independently_heldout_gold_verified": False,
    }


def original_contents(paths: list[str]) -> dict[str, bytes]:
    """Read exactly 80 prospective original Git blobs via one path-limited archive."""
    archive = git("archive", "--format=tar", PIN, *paths)
    result = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as content:
        for member in content:
            if member.isfile():
                stream = content.extractfile(member)
                if stream is None:
                    raise ValueError("Original Git archive member missing content stream")
                if member.name in result:
                    raise ValueError("Original archive duplicates carrier identity")
                result[member.name] = stream.read()
    if set(result) != set(paths):
        raise ValueError("Exact original source roster does not match requested 80 paths")
    return result


def first_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def witness_lines(text: str, expected: list[str]) -> list[dict[str, Any]]:
    """Exact original line witness, no paraphrase fabricated from a substring."""
    lines = text.splitlines()
    evidence = []
    for wanted in expected:
        found = [(i + 1, line) for i, line in enumerate(lines) if wanted.strip() in line.strip()]
        if not found:
            raise ValueError(f"Declared frozen source reference line absent: {wanted[:100]}")
        if len(found) > 1:
            # Repeated exactly identical text remains a valid source quote
            # only with an explicit deterministic first occurrence.
            found.sort(key=lambda pair: pair[0])
        no, original = found[0]
        evidence.append({
            "line_number": no, "original_line": original,
            "sha256_of_original_line": sha256(original.encode("utf-8")).hexdigest(),
        })
    return evidence


def fts_db(documents: dict[str, dict[str, str]]) -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE VIRTUAL TABLE body_fts USING fts5(path UNINDEXED, text, tokenize='unicode61')")
    db.execute("CREATE VIRTUAL TABLE title_fts USING fts5(path UNINDEXED, text, tokenize='unicode61')")
    for p, r in sorted(documents.items()):
        db.execute("INSERT INTO body_fts VALUES (?,?)", (p, r["original_section_text"]))
        db.execute("INSERT INTO title_fts VALUES (?,?)", (p, r["title"]))
    db.commit()
    db.execute("PRAGMA query_only=ON")
    return db


def rank_fts(db: sqlite3.Connection, table: str, question: str) -> list[str]:
    if table not in ("body_fts", "title_fts"):
        raise ValueError("Invalid fixed comparator table")
    query = fts_query(question)
    if not query:
        return []
    return [
        row[0] for row in db.execute(
            f"SELECT path FROM {table} WHERE {table} MATCH ? "
            f"ORDER BY bm25({table}),path ASC LIMIT ?", (query, K)
        )
    ]


def run() -> dict[str, Any]:
    raw_tasks = TASKS.read_bytes()
    if len(raw_tasks) != TASK_BYTES or sha256(raw_tasks).hexdigest() != TASK_SHA:
        raise ValueError("Before-implementation frozen task/answer manifest changed")
    tasks = json.loads(raw_tasks)["tasks"]
    if len(tasks) != 12 or len({t["id"] for t in tasks}) != 12:
        raise ValueError("Invalid source-grounded twelve-primary-task manifest")
    groups = Counter(t["category"] for t in tasks)
    if sorted(groups.values()) != [3, 3, 3, 3] or len(groups) != 4:
        raise ValueError("Original four-category task balance changed")

    required = {t["required_source_for_evaluation_only"] for t in tasks}
    build, heldout, sampling = prospective_draw(required)
    source = original_contents(build + heldout)
    records = {
        path: {
            "path": path,
            "original_source_sha256": sha256(data).hexdigest(),
            "bytes": len(data),
            "is_build": path in build,
            "is_heldout": path in heldout,
            "title": first_heading(data.decode("utf-8")),
            "indexed_content_characters": min(len(data.decode("utf-8")), INDEX_CHAR_LIMIT),
        }
        for path, data in sorted(source.items())
    }
    text_by_path = {path: blob.decode("utf-8") for path, blob in source.items()}
    answered = []
    for item in tasks:
        src = item["required_source_for_evaluation_only"]
        if src not in build:
            raise ValueError("Missing reference source in common B0 build")
        originals = witness_lines(text_by_path[src], item["required_source_witness_lines"])
        answered.append({
            "id": item["id"],
            "category": item["category"],
            "question": item["question"],
            "reference_answer_for_evaluation_only": item["reference_answer_for_evaluation_only"],
            "required_source_for_evaluation_only": src,
            "required_source_body_sha256": records[src]["original_source_sha256"],
            "required_witnesses_original_source": originals,
            "reference_status": "EXPOSED_COORDINATOR_SOURCE_CITED_PROVISIONAL",
            "no_operative_deployment_inferred_from_header_status": True,
        })

    # Ranking inputs are constructed from exactly the 60 common build sources.
    # Evaluation-only source IDs and answer texts never flow into rankers.
    docs = {
        p: {"title": records[p]["title"],
            "original_section_text": text_by_path[p][:INDEX_CHAR_LIMIT]}
        for p in build
    }
    db = fts_db(docs)
    char_docs, idf, char_cost = sparse_char_index(docs)
    outputs = []
    try:
        for ref in answered:
            query = ref["question"]
            initial = {
                "B0_SUBSTRATE_LEXICAL_BASELINE": rank_fts(db, "body_fts", query),
                "TITLE_LEXICAL_DIAGNOSTIC": rank_fts(db, "title_fts", query),
                "CHAR_TRIGRAM_DIAGNOSTIC": char_rank(query, char_docs, idf),
            }
            # Function uses the legacy three identifiers, so provide a
            # stable, explicit adapter. No reference label is involved.
            adapter = {
                "BODY_FTS5_BM25": initial["B0_SUBSTRATE_LEXICAL_BASELINE"],
                "TITLE_FTS5_BM25": initial["TITLE_LEXICAL_DIAGNOSTIC"],
                "CHARACTER_NGRAM_TFIDF": initial["CHAR_TRIGRAM_DIAGNOSTIC"],
            }
            initial["DIAGNOSTIC_THREE_WAY_RRF"] = rrf_fusion(adapter)
            expected = ref["required_source_for_evaluation_only"]
            ranks = {kind: (paths.index(expected) + 1 if expected in paths else None)
                     for kind, paths in initial.items()}
            outputs.append({
                "id": ref["id"],
                "category": ref["category"],
                "question": query,
                "intended_source_for_evaluation_only": expected,
                "source_status_gold_independent": False,
                "common_source_candidate_rankings": initial,
                "reference_source_rank_after_retrieval": ranks,
                "B0_top_5_candidate_sources_with_original_SHA256": [
                    {"path": p, "sha256": records[p]["original_source_sha256"]}
                    for p in initial["B0_SUBSTRATE_LEXICAL_BASELINE"][:5]
                ],
            })
    finally:
        db.close()

    metrics = {}
    for name in RANKERS:
        ranks = [r["reference_source_rank_after_retrieval"][name] for r in outputs]
        metrics[name] = {
            f"required_source_hit_at_{k}": sum(r is not None and r <= k for r in ranks)
            for k in (1, 3, 5, 10)
        } | {
            "required_source_mrr_at_10": sum((1 / r) if r else 0 for r in ranks) / len(ranks),
            "tasks": len(ranks),
            "missing_required_source_at_10": [
                output["id"] for output in outputs if output["reference_source_rank_after_retrieval"][name] is None
            ],
        }
    return {
        "id": "R0_P03_ROUTE_B_PRAGMATIC_PRIMARY_B0_EXECUTION_ATTEMPT_V01",
        "contract": CONTRACT,
        "source_git_pin": PIN,
        "source_manifest_bytes": TASK_BYTES,
        "source_manifest_sha256": TASK_SHA,
        "sampling": sampling,
        "source_roster": list(records.values()),
        "build_sources": build,
        "heldout_sources": heldout,
        "provisional_reference_answers": answered,
        "comparative_retrieval_trace": outputs,
        "metrics": metrics,
        "runtime_indexes": {
            "sqlite_version": sqlite3.sqlite_version,
            "char_index": char_cost,
            "B0_uses_metadata_gold_for_ranking": False,
            "source_context_cap": INDEX_CHAR_LIMIT,
            "retrieval_top_k": K,
        },
        "scientific_limits": [
            "First real primary-task B0 navigation retrieval execution under owner-approved pragmatic Path B, but coordinator-written reference answers are exposed and not independent.",
            "A source-referenced answer and single required source are not a neutral exhaustive relevance gold set.",
            "B0 is a source-text FTS5 diagnostic for the proposed common substrate, not a proven equalized complete V03 relation substrate.",
            "Title-only, char-trigram and fused rankers are diagnostics and DO NOT IMPLEMENT B1/B2/B3/B4.",
            "60/20 fixed candidate corpus is path-stratified and lacks independently verified representative role/effect/migration coverage or maintenance gold.",
            "The initial 12 primary task slots are not formally qualified for Research 513 >=10/12 answer PASS scoring.",
            "No nine-case independently neutralized legacy score, two blind independent evaluators, held-out agreement score or zero-authority safety certification.",
            "No source status proves real-world operative authority, and no architecture family selection or source migration is supported.",
            "Private C01/C02 references and historical HOLDs remain unchanged and inaccessible to this exposed arm coordinator.",
        ],
        "formal_R0_P03_scored": False,
        "physical_architecture_selected": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    raw = json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(raw)
    print(json.dumps({
        "id": result["id"],
        "sampling": result["sampling"],
        "metrics": result["metrics"],
        "saved": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
