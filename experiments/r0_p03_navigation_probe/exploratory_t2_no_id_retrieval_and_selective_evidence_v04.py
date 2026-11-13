"""Compare matched lexical, character and fused decision retrieval without IDs.

All questions are manually authored by an EXPOSED coordinator; document
labels are evaluation hints, not independent semantic or authority gold.
Source evidence is exact numbered decision sections at two original Git pins.
The selective guard emits only provisional source-recorded status hypotheses.
No modern embedding model is used or claimed.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path
import re
import sqlite3
import sys
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import ROOT
from experiments.r0_p03_navigation_probe.exploratory_t2_decision_ledger_snapshot_and_scope_v03 import (
    REVISIONS, SOURCE_PATH, git_blob_id, original_git_blob, parse_sections, source_evidence,
)

IDENTIFIER = "R0_P03_T2_EXPLORATORY_NO_ID_COMPETING_RETRIEVAL_AND_SELECTIVE_STATUS_V04"
CONTRACT = "EXPLORATORY_T2_NO_ID_RETRIEVAL_AND_SELECTIVE_EVIDENCE_CONTRACT_V04.md"
MANIFEST = ROOT / "experiments/r0_p03_navigation_probe/EXPLORATORY_T2_NO_ID_MANUAL_QUESTION_MANIFEST_V01.json"
MANIFEST_SHA256 = "d632b334ec39e88f5fcaa2c1761e0b2f7ea2aa4d5b8126df962b092918495d05"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_t2_no_id_retrieval_and_selective_evidence_result_v04.json"
METHODS = ("BODY_FTS5_BM25", "TITLE_FTS5_BM25", "CHARACTER_NGRAM_TFIDF", "THREE_WAY_RRF")
TOKEN = re.compile(r"[a-z0-9]+", re.I)
STOPWORDS = frozenset(
    "a an and are as at be been but by can could did do does for from has have how i in "
    "is it its of on or our should so than that the their there these this those to was we "
    "were what when where which who why will with would you your about already any all "
    "actually currently official officially selected decision decided decisions source "
    "project projects system platform still into out not yet only was".split()
)
TOP_K = 10
RRF_K = 60
NGRAM = 3
NGRAM_SECTION_PREFIX = 600


def tokens(text: str) -> list[str]:
    """Fixed low-information-word filter, no fitted labels or target IDs."""
    return list(dict.fromkeys(
        v for v in TOKEN.findall(text.casefold()) if len(v) >= 2 and v not in STOPWORDS
    ))


def manifest() -> dict[str, Any]:
    original = MANIFEST.read_bytes()
    if len(original) != 8668 or sha256(original).hexdigest() != MANIFEST_SHA256:
        raise ValueError("Frozen author manifest changed after pre-execution freeze")
    content = json.loads(original)
    if len(content["positive"]) != 26 or len(content["negative"]) != 6:
        raise ValueError("Fixed original question population drift")
    entries = content["positive"] + content["negative"]
    if len({x["id"] for x in entries}) != len(entries):
        raise ValueError("Duplicate author-question ID")
    if any(re.search(r"\bD-\d{3}\b", e["query"], re.I) for e in entries):
        raise ValueError("Explicit decision ID leaks into no-ID question")
    return content


def fts_query(text: str) -> str:
    return " OR ".join(f'"{t}"' for t in tokens(text))


def norm_text(text: str) -> str:
    return " ".join(TOKEN.findall(text.casefold()))


def grams(text: str) -> Counter[str]:
    s = " " + norm_text(text) + " "
    return Counter(s[i:i + NGRAM] for i in range(max(0, len(s) - NGRAM + 1)))


def sparse_char_index(
    records: dict[str, dict[str, Any]],
) -> tuple[dict[str, dict[str, float]], dict[str, float], dict[str, int]]:
    raw_docs = {
        did: grams(row["title"] + " " + row["original_section_text"][:NGRAM_SECTION_PREFIX])
        for did, row in records.items()
    }
    df = Counter(g for counts in raw_docs.values() for g in counts)
    n = len(records)
    idf = {g: 1.0 + math.log((n + 1) / (count + 1)) for g, count in df.items()}
    normalized = {}
    for did, counts in raw_docs.items():
        w = {g: (1.0 + math.log(c)) * idf[g] for g, c in counts.items()}
        length = math.sqrt(sum(v * v for v in w.values())) or 1.0
        normalized[did] = {g: v / length for g, v in w.items()}
    sizes = {
        "indexed_sections": n,
        "unique_3gram_features": len(idf),
        "nonzero_document_3gram_weights": sum(len(v) for v in normalized.values()),
        "original_section_bytes": sum(len(v["original_section_text"].encode("utf-8")) for v in records.values()),
    }
    return normalized, idf, sizes


def char_rank(
    query: str,
    index: dict[str, dict[str, float]],
    idf: dict[str, float],
) -> list[str]:
    counts = grams(query)
    weights = {g: (1 + math.log(c)) * idf[g] for g, c in counts.items() if g in idf}
    magnitude = math.sqrt(sum(w * w for w in weights.values()))
    if not magnitude:
        return []
    q = {g: w / magnitude for g, w in weights.items()}
    scores = [
        (did, sum(w * index[did].get(g, 0.0) for g, w in q.items()))
        for did in index
    ]
    return [did for did, score in sorted(scores, key=lambda x: (-x[1], x[0]))
            if score > 0][:TOP_K]


def sqlite_index(records: dict[str, dict[str, Any]]) -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE VIRTUAL TABLE body_fts USING fts5(id UNINDEXED, text, tokenize='unicode61')")
    db.execute("CREATE VIRTUAL TABLE title_fts USING fts5(id UNINDEXED, text, tokenize='unicode61')")
    for did, record in sorted(records.items()):
        db.execute("INSERT INTO body_fts (id, text) VALUES (?,?)",
                   (did, record["original_section_text"]))
        db.execute("INSERT INTO title_fts (id, text) VALUES (?,?)",
                   (did, record["title"]))
    db.commit()
    db.execute("PRAGMA query_only=ON")
    return db


def fts_rank(db: sqlite3.Connection, which: str, query: str) -> list[str]:
    if which not in ("body_fts", "title_fts"):
        raise ValueError("Not a declared FTS5 mechanism")
    match = fts_query(query)
    if not match:
        return []
    return [
        x[0] for x in db.execute(
            f"SELECT id FROM {which} WHERE {which} MATCH ? "
            f"ORDER BY bm25({which}) ASC, id ASC LIMIT ?", (match, TOP_K)
        )
    ]


def rrf_fusion(rankings: dict[str, list[str]]) -> list[str]:
    votes = defaultdict(float)
    for name in METHODS[:3]:
        for rank, did in enumerate(rankings[name], 1):
            votes[did] += 1.0 / (RRF_K + rank)
    return [did for did, _ in sorted(votes.items(), key=lambda x: (-x[1], x[0]))][:TOP_K]


def guarded_provisional_hypothesis(
    question: str,
    rankings: dict[str, list[str]],
    records: dict[str, dict[str, Any]],
    snapshot: str,
    blob_sha: str,
) -> dict[str, Any]:
    """Never receive author-intended evaluation target, even in a callback."""
    fused = rankings["THREE_WAY_RRF"]
    candidate = fused[0] if fused else None
    if candidate is None:
        state = "REFERENT_NOT_SUFFICIENTLY_VERIFIED"
        reasons = ["no_candidate"]
    else:
        top_votes = sum(
            bool(rankings[method]) and rankings[method][0] == candidate
            for method in METHODS[:3]
        )
        third_in_top3 = all(candidate in rankings[method][:3] for method in METHODS[:3])
        query_overlap = sorted(set(tokens(question)) & set(tokens(records[candidate]["title"])))
        reasons = []
        if top_votes < 2:
            reasons.append("fewer_than_two_top_one_votes")
        if not third_in_top3:
            reasons.append("missing_from_other_method_top_three")
        if len(query_overlap) < 2:
            reasons.append("fewer_than_two_heading_content_words")
        state = (
            "PROVISIONAL_SOURCE_STATUS_HYPOTHESIS" if not reasons
            else "REFERENT_NOT_SUFFICIENTLY_VERIFIED"
        )
    accepted = candidate if state == "PROVISIONAL_SOURCE_STATUS_HYPOTHESIS" else None
    citation = (
        source_evidence(records[accepted], REVISIONS[snapshot], blob_sha)
        if accepted is not None else None
    )
    return {
        "state": state,
        "provisional_decision_id": accepted,
        "source_status_and_provenance": citation,
        "gate_reasons": reasons,
        "source_title_overlap_tokens": (
            sorted(set(tokens(question)) & set(tokens(records[candidate]["title"])))
            if candidate is not None else []
        ),
        "all_lexical_candidate_ids_not_authority": list(fused),
        "operative_governance_asserted": False,
        "subject_identity_independently_verified": False,
    }


def run() -> dict[str, Any]:
    prepared = manifest()
    originals = {s: original_git_blob(sha) for s, sha in REVISIONS.items()}
    decisions = {s: parse_sections(originals[s], s) for s in REVISIONS}
    blobs = {s: git_blob_id(v) for s, v in originals.items()}
    indexes = {}
    for s in ("S0", "S1"):
        char, idf, sizes = sparse_char_index(decisions[s])
        indexes[s] = (sqlite_index(decisions[s]), char, idf, sizes)

    cases = []
    items = prepared["positive"] + prepared["negative"]
    try:
        for snapshot in ("S0", "S1"):
            db, char, idf, sizes = indexes[snapshot]
            for row in items:
                query = row["query"]   # Only query is sent to the four rankers.
                ranked = {
                    "BODY_FTS5_BM25": fts_rank(db, "body_fts", query),
                    "TITLE_FTS5_BM25": fts_rank(db, "title_fts", query),
                    "CHARACTER_NGRAM_TFIDF": char_rank(query, char, idf),
                }
                ranked["THREE_WAY_RRF"] = rrf_fusion(ranked)
                gate = guarded_provisional_hypothesis(
                    query, ranked, decisions[snapshot], snapshot, blobs[snapshot]
                )
                # Evaluation-only labels are consulted AFTER all model outputs
                # have been fixed for this question.
                expected = row["expected_id_for_evaluation_only"]
                present = expected is not None and expected in decisions[snapshot]
                target_rank = {
                    method: (ids.index(expected) + 1 if present and expected in ids else None)
                    for method, ids in ranked.items()
                }
                admitted = gate["provisional_decision_id"]
                cases.append({
                    "id": row["id"] + "_" + snapshot,
                    "author_question_id": row["id"],
                    "question": query,
                    "topic_family": row["topic_family"],
                    "snapshot": snapshot,
                    "source_revision": REVISIONS[snapshot],
                    "author_intended_decision_for_evaluation_only": expected,
                    "author_intended_record_in_snapshot": bool(present),
                    "query_tokens": tokens(query),
                    "rankings": ranked,
                    "ranks_of_author_intended_section": target_rank,
                    "selective_status_response": gate,
                    "provisional_status_source_correct_by_author_label": (
                        admitted is not None and admitted == expected and present
                    ),
                    "provisional_status_source_wrong_by_author_label": (
                        admitted is not None and (not present or admitted != expected)
                    ),
                })
    finally:
        for db, _, _, _ in indexes.values():
            db.close()
    if len(cases) != 64:
        raise AssertionError("Not all predeclared no-ID snapshot questions were evaluated")

    eligible = [r for r in cases if r["author_intended_record_in_snapshot"]]
    counts = {
        method: {
            f"hit_at_{k}": sum(
                row["ranks_of_author_intended_section"][method] is not None
                and row["ranks_of_author_intended_section"][method] <= k
                for row in eligible
            )
            for k in (1, 3, 5, 10)
        } | {
            "mrr_at_10": sum(
                (1.0 / row["ranks_of_author_intended_section"][method])
                if row["ranks_of_author_intended_section"][method] else 0.0
                for row in eligible
            ) / len(eligible),
            "eligible_positive_cases": len(eligible),
        }
        for method in METHODS
    }
    admitted = [r for r in cases if r["selective_status_response"]["provisional_decision_id"]]
    correct = sum(r["provisional_status_source_correct_by_author_label"] for r in admitted)
    wrong = sum(r["provisional_status_source_wrong_by_author_label"] for r in admitted)
    positive = [r for r in cases if r["author_intended_record_in_snapshot"]]
    absent = [r for r in cases if not r["author_intended_record_in_snapshot"]]
    matrix = {
        "questions_in_manifest": len(items),
        "source_snapshot_instances": len(cases),
        "author_intended_present": len(positive),
        "author_intended_absent_or_unmatched": len(absent),
        "author_negative_questions_per_snapshot": 6,
        "positive_id_missing_S0": [
            r["author_question_id"] for r in cases
            if r["snapshot"] == "S0" and r["author_intended_decision_for_evaluation_only"] is not None
            and not r["author_intended_record_in_snapshot"]
        ],
        "retrieval_by_method": counts,
        "provisional_status_admissions": len(admitted),
        "provisional_correct_by_author_label": correct,
        "provisional_wrong_by_author_label": wrong,
        "provisional_precision_by_author_label": correct / len(admitted) if admitted else None,
        "correct_provisional_coverage_of_present": correct / len(positive),
        "provisional_on_absent_or_author_no_target": sum(
            r["selective_status_response"]["provisional_decision_id"] is not None
            for r in absent
        ),
        "abstentions": len(cases) - len(admitted),
        "all_candidate_lists_kept_separate": all(
            r["selective_status_response"]["all_lexical_candidate_ids_not_authority"] ==
            r["rankings"]["THREE_WAY_RRF"]
            for r in cases
        ),
        "operative_governance_claim_count": sum(
            r["selective_status_response"]["operative_governance_asserted"]
            for r in cases
        ),
        "question_author_independent": False,
        "semantic_embedding_retrieval_executed": False,
        "formal_R0_P03_scored": False,
    }
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "question_manifest_sha256": MANIFEST_SHA256,
        "source_git_revisions": REVISIONS,
        "source_blob_identifiers": {
            s: {"revision": REVISIONS[s], "source_path": SOURCE_PATH,
                "bytes": len(originals[s]), "sha256": sha256(originals[s]).hexdigest(),
                "git_blob_sha1": blobs[s], "decisions": len(decisions[s])}
            for s in ("S0", "S1")
        },
        "source_decision_manifest": {
            s: {
                did: {
                    "title": record["title"],
                    "source_status": record["source_status"],
                    "source_status_category": record["source_status_category"],
                    "section_sha256": record["section_sha256"],
                    "status_witness": record["status_witness"],
                    "superseded_in_scope": record["superseded_in_scope"],
                }
                for did, record in records.items()
            }
            for s, records in decisions.items()
        },
        "index_characterization": {
            s: {"methods": list(METHODS), "char_sparse": indexes[s][3],
                "rrf_k": RRF_K, "top_k": TOP_K, "source_status_authority": "recorded_only"}
            for s in ("S0", "S1")
        },
        "cases": cases,
        "metrics": matrix,
        "scientific_limits": [
            "All 32 questions were manually authored by an exposed model with knowledge of the very decision records and prior trials; no independent user/gold is present.",
            "The 26 author pointers are not independently corroborated unique or complete relevant decision labels.",
            "The six unmatched questions are bounded author hypotheses about the examined ledger, not proof of repository-wide or real-world absence.",
            "All four retrieval mechanisms are lexical, character-lexical or their rank fusion; no semantic vector embeddings were tested.",
            "All cases reuse previously exposed historical source decision sections, even though the no-ID phrasings are new.",
            "The selective answer is explicitly a provisional sourced hypothesis with no independently verified referent; wrong hypotheses are counted, not repaired.",
            "Recorded status alone cannot prove actual current operative authority or whether a selected successor has been activated.",
            "RRF incurs additional indexes and query operations; no actual human metadata-authoring cost comparison or production latency certification was performed.",
            "The original formal Research 513/559/576 R0-P03 scored B0-B4 comparison remains incomplete and physical architecture unselected.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    out = run()
    raw = json.dumps(out, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(raw)
    print(json.dumps({
        "identifier": out["identifier"],
        "source_size": out["source_blob_identifiers"],
        "metrics": out["metrics"],
        "output_saved": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
