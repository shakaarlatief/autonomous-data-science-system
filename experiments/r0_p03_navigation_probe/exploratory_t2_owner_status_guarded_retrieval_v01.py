"""Execute a fixed, nonblind T2 status-assertion and retrieval pilot on new sources.

This is a source-header-claim benchmark, not a current operative-governance
oracle, independent author study, or R0-P03 B0–B4 architecture decision.
The source cohort excludes all 65 already-exposed historical originals.
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
import sys
import tarfile
import tempfile
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import ANNOTATIONS, ROOT, load, tokenize_query
from scripts.repository_integrity import read_header_fields

IDENTIFIER = "R0_P03_T2_EXPLORATORY_NEW_SOURCE_OWNER_STATUS_GUARDED_RETRIEVAL_V01"
CONTRACT = "EXPLORATORY_T2_OWNER_STATUS_GUARDED_RETRIEVAL_CONTRACT_V01.md"
PIN = "e8ae867392f818f43dc8b76984f164e277d5cc87"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_t2_owner_status_guarded_retrieval_result_v01.json"
FAMILIES = ("docs/research", "docs/checkpoints", "docs/specifications")
CLASS_ORDER = (
    "OWNER_ACCEPTANCE_RECORDED",
    "OWNER_DECISION_REQUIRED_RECORDED",
    "CANDIDATE_RECORDED",
)
PREFIX = "T2-V01-NOV13-STATUS-FIXED"
DISTRACTOR_PREFIX = "T2-V01-DISTRACTOR-FIXED"
N_PER_CLASS = 8
N_DISTRACTORS = 96
K = 10

STATUS_PATTERN = re.compile(r"^\s*\*\*Status:\*\*\s*(.*?)\s*$")
OWNER_ACCEPTED = re.compile(r"\bOWNER[\s-]+ACCEPTED\b", re.I)
OWNER_REQUIRED = re.compile(r"\bOWNER DECISION REQUIRED\b", re.I)
CANDIDATE = re.compile(r"\bCANDIDATE\b", re.I)
REMOVE_LABEL_WORDS = re.compile(
    r"\b(?:owner|accepted|approved|decision|required|candidate|pending)\b",
    re.I,
)
HEADER_SCAN_LINES = 100


def source_archive() -> dict[str, bytes]:
    """Read only the exact Git objects at the frozen new-source commit."""
    git = subprocess.run(
        ["git", "archive", "--format=tar", PIN, *FAMILIES],
        cwd=ROOT, capture_output=True, check=True,
    )
    sources: dict[str, bytes] = {}
    with tarfile.open(fileobj=io.BytesIO(git.stdout), mode="r:") as bundle:
        for member in bundle.getmembers():
            if not member.isfile() or not member.name.endswith(".md"):
                continue
            if not member.name.startswith(tuple(x + "/" for x in FAMILIES)):
                continue
            content = bundle.extractfile(member)
            if content is None:
                raise ValueError("Cannot read original archived source member")
            if member.name in sources:
                raise ValueError("Duplicate source path within pinned original Git archive")
            sources[member.name] = content.read()
    if len(sources) < 200:
        raise ValueError("New original Git horizon unexpectedly small")
    return sources


def classified_status(status: str) -> str | None:
    """Classify claims about the document Status, NEVER operative authority."""
    if OWNER_REQUIRED.search(status):
        return CLASS_ORDER[1]
    if OWNER_ACCEPTED.search(status):
        return CLASS_ORDER[0]
    if CANDIDATE.search(status) and "ACCEPTED" not in status.upper() and "OWNER DECISION" not in status.upper():
        return CLASS_ORDER[2]
    return None


def status_witness(body: str, expected: str) -> dict[str, Any]:
    """Locate the exact original governed Status header line and content digest.

    Header value parsing is done exclusively through read_header_fields. This
    helper locates evidence already accepted by that same native parser.
    """
    matches = []
    for n, line in enumerate(body.splitlines()[:HEADER_SCAN_LINES], 1):
        if line.startswith("## "):
            break
        match = STATUS_PATTERN.match(line)
        if match and match.group(1).strip() == expected:
            matches.append((n, line))
    if len(matches) != 1:
        raise ValueError("Parsed native Status does not have one exact original header witness")
    n, original = matches[0]
    return {
        "line_number": n,
        "original_line": original,
        "line_sha256": sha256(original.encode("utf-8")).hexdigest(),
    }


def first_h1(body: str) -> str:
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("Selected original source lacks first H1")


def topic_from_heading(heading: str) -> str:
    candidate = REMOVE_LABEL_WORDS.sub(" ", heading)
    candidate = re.sub(r"\s+", " ", candidate).strip(" -:/.,")
    if len(re.findall(r"[a-z0-9]{2,}", candidate.casefold())) < 2:
        raise ValueError("Title-derived topic has fewer than two usable words")
    return candidate


def query_from_heading(heading: str) -> tuple[str, str]:
    topic = topic_from_heading(heading)
    return (
        topic,
        "What is the owner-decision status for " + topic +
        "? Was it actually accepted, still awaiting an owner decision, "
        "or only a candidate? Cite the status evidence and keep useful "
        "document suggestions separate.",
    )


def naive_body_status(body: str) -> str | None:
    """Deliberately fragile whole-body scanner, never a source-authority gate."""
    if OWNER_REQUIRED.search(body):
        return CLASS_ORDER[1]
    if OWNER_ACCEPTED.search(body):
        return CLASS_ORDER[0]
    if CANDIDATE.search(body):
        return CLASS_ORDER[2]
    return None


def source_records(
    originals: dict[str, bytes],
    previous_paths: set[str],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, str], dict[str, Any]]:
    """Freeze class-balanced 24 targets and 96 distractors BEFORE retrieval."""
    targets_by_class = {key: [] for key in CLASS_ORDER}
    headers = {}
    body_text = {}
    witness = {}
    with tempfile.TemporaryDirectory(dir=ROOT / ".venv") as temporary:
        scratch = Path(temporary) / "source.md"
        for path in sorted(originals):
            if path in previous_paths:
                continue
            b = originals[path]
            text = b.decode("utf-8")
            body_text[path] = text
            scratch.write_bytes(b)
            status = read_header_fields(scratch).get("Status")
            headers[path] = status
            if status:
                kind = classified_status(status)
                if kind is not None:
                    try:
                        heading = first_h1(text)
                        query_from_heading(heading)
                    except ValueError:
                        continue
                    targets_by_class[kind].append(path)
                    witness[path] = status_witness(text, status)

    selected = []
    available = {}
    for class_name in CLASS_ORDER:
        possible = sorted(
            targets_by_class[class_name],
            key=lambda p: (sha256((PREFIX + "|" + class_name + "|" + p).encode("utf-8")).hexdigest(), p),
        )
        available[class_name] = len(possible)
        if len(possible) < N_PER_CLASS:
            raise ValueError(f"Too few unexposed historical sources in {class_name}: {len(possible)}")
        selected.extend((p, class_name) for p in possible[:N_PER_CLASS])
    selected_paths = {p for p, _ in selected}
    distractors = sorted(
        (p for p in body_text if p not in selected_paths),
        key=lambda p: (sha256((DISTRACTOR_PREFIX + "|" + p).encode("utf-8")).hexdigest(), p),
    )[:N_DISTRACTORS]
    if len(distractors) != N_DISTRACTORS:
        raise ValueError("Too few archive distractors")
    corpus_paths = sorted(selected_paths | set(distractors))
    if len(corpus_paths) != 120 or set(corpus_paths) & previous_paths:
        raise ValueError("Selected new source cohort duplicates old exposed originals")
    cases = []
    for path, kind in sorted(selected, key=lambda z: (CLASS_ORDER.index(z[1]), z[0])):
        heading = first_h1(body_text[path])
        topic, query = query_from_heading(heading)
        cases.append({
            "id": "T2-" + str(len(cases) + 1).zfill(2),
            "expected_source": path,
            "expected_source_sha256": sha256(originals[path]).hexdigest(),
            "original_first_h1": heading,
            "topic": topic,
            "question": query,
            "expected_source_header_class": kind,
            "expected_source_header_status": headers[path],
            "expected_source_header_witness": witness[path],
            "independent_oracle": False,
        })
    roster = [
        {
            "path": p,
            "body_sha256": sha256(originals[p]).hexdigest(),
            "bytes": len(originals[p]),
            "is_target": p in selected_paths,
            "native_header_status": headers[p],
        }
        for p in corpus_paths
    ]
    snapshot = {
        "eligible_archive_markdown_count": len(originals),
        "excluded_historical_65_count": len(previous_paths),
        "eligible_class_available_counts": available,
        "sampled_source_count": len(corpus_paths),
        "sampled_target_count": len(cases),
        "sampled_distractors": N_DISTRACTORS,
        "sampled_source_sha256": sha256(
            json.dumps([[r["path"], r["body_sha256"]] for r in roster], sort_keys=True, separators=(",", ":")).encode("utf-8")
        ).hexdigest(),
    }
    return cases, roster, {p: body_text[p] for p in corpus_paths}, snapshot


def rank_query(connection: sqlite3.Connection, topic: str) -> list[str]:
    expression = tokenize_query([topic])
    return [
        row[0] for row in connection.execute(
            "SELECT path FROM docs_fts WHERE docs_fts MATCH ? "
            "ORDER BY bm25(docs_fts) ASC, path ASC LIMIT ?",
            (expression, K),
        )
    ]


def assertion(
    candidate: str | None,
    source_status: str | None,
    claimed_status: str | None,
    witness: dict[str, Any] | None,
    coverage: str,
) -> dict[str, Any]:
    if candidate is None or claimed_status is None:
        return {
            "state": "NOT_FOUND_IN_COVERED_SCOPE",
            "asserted_document": None,
            "asserted_source_header_class": None,
            "evidence": None,
            "coverage": coverage,
            "operative_governance_claim": False,
        }
    return {
        "state": "ASSERTED_SOURCE_STATUS_ONLY",
        "asserted_document": candidate,
        "asserted_source_header_class": claimed_status,
        "evidence": witness,
        "coverage": coverage,
        "source_header_status_as_parsed": source_status,
        "operative_governance_claim": False,
    }


def run() -> dict[str, Any]:
    if subprocess.run(["git", "cat-file", "-e", PIN + "^{commit}"], cwd=ROOT).returncode:
        raise ValueError("Pinned Git commit not available")
    originals = source_archive()
    history = {r["path"] for r in load(ANNOTATIONS)["annotations"]}
    if len(history) != 65:
        raise ValueError("Prior exposed 65-source population drift")
    cases, roster, bodies, world = source_records(originals, history)
    if len(cases) != 24 or Counter(c["expected_source_header_class"] for c in cases) != {k: 8 for k in CLASS_ORDER}:
        raise ValueError("Fixed task class balance drift")
    # All case selection and question strings are now fixed. No retrieval
    # outcome can affect which source or topic enters the experiment.
    status_by_path = {r["path"]: r["native_header_status"] for r in roster}
    witness_by_path = {
        c["expected_source"]: c["expected_source_header_witness"]
        for c in cases
    }
    # Status witness for other possible top candidates is located directly
    # from the parsed source header, not from expected task labels.
    for p, status in status_by_path.items():
        if status and classified_status(status) is not None and p not in witness_by_path:
            witness_by_path[p] = status_witness(bodies[p], status)

    db = sqlite3.connect(":memory:")
    outcomes = []
    try:
        db.execute("CREATE VIRTUAL TABLE docs_fts USING fts5(path UNINDEXED, body, tokenize='unicode61')")
        for p in sorted(bodies):
            db.execute("INSERT INTO docs_fts (path, body) VALUES (?, ?)", (p, bodies[p]))
        db.commit()
        db.execute("PRAGMA query_only=ON")
        for case in cases:
            ranked = rank_query(db, case["topic"])
            top = ranked[0] if ranked else None
            top_status = status_by_path.get(top) if top is not None else None
            header_claim = classified_status(top_status) if top_status else None
            naive = naive_body_status(bodies[top]) if top is not None else None
            header = assertion(
                top, top_status, header_claim,
                witness_by_path.get(top) if header_claim else None,
                "Native first-100-line Status of the top lexical document within the 120-source pinned Git corpus",
            )
            naive_answer = assertion(
                top, top_status, naive, None,
                "Unscoped regex over the entire top-ranked document body, not source-owner semantics",
            )
            if top is not None and naive is not None:
                naive_answer["evidence"] = {
                    "evidence_class": "UNSCOPED_BODY_KEYWORD_HEURISTIC",
                    "not_a_source_header_witness": True,
                }
            # Same evidence assertion, with independently retained lexical
            # suggestions. It never promotes a candidate to governing truth.
            two_channel = {
                "assertion": header,
                "candidate_documents_not_authoritative": ranked,
            }
            expected = case["expected_source"]
            cls = case["expected_source_header_class"]
            outcomes.append({
                **case,
                "candidate_ranking": ranked,
                "top_candidate": top,
                "target_rank": (ranked.index(expected) + 1) if expected in ranked else None,
                "top_candidate_status": top_status,
                "top_candidate_source_header_class": header_claim,
                "lexical_only": {
                    "candidate_documents": ranked,
                    "assertion_state": "NO_ASSERTION_BY_DESIGN",
                },
                "naive_body_keyword": naive_answer,
                "governed_header_assertion": header,
                "two_channel_guarded": two_channel,
                "exact_source_and_status_correct": top == expected and header_claim == cls,
                "naive_exact_source_and_status_correct": top == expected and naive == cls,
                "naive_false_owner_acceptance_for_nonaccepted_target": (
                    naive == CLASS_ORDER[0] and cls != CLASS_ORDER[0]
                ),
                "header_false_owner_acceptance_for_nonaccepted_target": (
                    header_claim == CLASS_ORDER[0] and cls != CLASS_ORDER[0]
                ),
                "naive_conflicts_with_top_source_native_status": (
                    naive is not None and naive != header_claim
                ),
                "wrong_source_with_nonempty_header_status": (
                    top is not None and top != expected and header_claim is not None
                ),
            })
    finally:
        db.close()
    ranked_recall = {
        str(n): sum(row["target_rank"] is not None and row["target_rank"] <= n for row in outcomes)
        for n in (1, 5, 10)
    }
    metrics = {
        "questions": len(outcomes),
        "status_classes": dict(sorted(Counter(x["expected_source_header_class"] for x in outcomes).items())),
        "lexical_target_hit_at": ranked_recall,
        "lexical_mrr_at_10": sum(
            1.0 / r["target_rank"] if r["target_rank"] else 0.0
            for r in outcomes
        ) / len(outcomes),
        "source_header_exact_status_correct_at_rank_1": sum(x["exact_source_and_status_correct"] for x in outcomes),
        "naive_body_exact_status_correct_at_rank_1": sum(x["naive_exact_source_and_status_correct"] for x in outcomes),
        "naive_false_owner_acceptance_nonaccepted_target": sum(x["naive_false_owner_acceptance_for_nonaccepted_target"] for x in outcomes),
        "governed_header_false_owner_acceptance_nonaccepted_target": sum(x["header_false_owner_acceptance_for_nonaccepted_target"] for x in outcomes),
        "naive_claim_disagrees_with_own_top_source_header": sum(x["naive_conflicts_with_top_source_native_status"] for x in outcomes),
        "wrong_source_with_nonempty_header_status": sum(x["wrong_source_with_nonempty_header_status"] for x in outcomes),
        "no_operative_governance_claims": all(
            not row["governed_header_assertion"]["operative_governance_claim"]
            and not row["two_channel_guarded"]["assertion"]["operative_governance_claim"]
            for row in outcomes
        ),
        "all_cases_return_nonassertive_candidates_separately": all(
            row["two_channel_guarded"]["candidate_documents_not_authoritative"] == row["candidate_ranking"]
            for row in outcomes
        ),
        "source_operational_governance_adjudicated": False,
    }
    return {
        "id": IDENTIFIER,
        "contract": CONTRACT,
        "source_commit": PIN,
        "classification": "NEW_SOURCE_EXPOSED_TITLE_DERIVED_STATUS_AND_CANDIDATE_RETRIEVAL_PILOT",
        "source_cohort": world,
        "sources": roster,
        "test_cases_and_results": outcomes,
        "metrics": metrics,
        "methods": {
            "retrieval": "Common 120-source SQLite FTS5 unicode61 BM25, OR topic words, K10",
            "lexical_only": "candidate retrieval only, no owner-status assertion",
            "naive_body_keyword": "whole-body keyword heuristic, intentionally unscoped diagnostic",
            "governed_header_assertion": "native first-100-line Status of top lexical candidate",
            "two_channel_guarded": "native scoped source-Status assertion plus separate nonassertive top-ten lexical candidates",
        },
        "software": {"python": sys.version.split()[0], "sqlite": sqlite3.sqlite_version},
        "limits": [
            "Owner acceptance in a historical source header is not current operative governance.",
            "Header status is source-authored task label; the source-header arm therefore shares its syntactic evidence basis with the answer key.",
            "Every query is coordinator-authored by fixed transformation of its target H1; no independent blind user queries or gold.",
            "The 120-source test population is narrow and partially synthetic by seed/hash sampling, not a neutral repository-wide currentness census.",
            "This runs no learned semantic retrieval model; only an FTS5 lexical candidate ranking and two evidence-handling variants.",
            "Naive body keyword heuristic is an explicitly weak hazard demonstration, not a fair B0-B4 architecture comparator.",
            "No ranking difference between guarded assertion and guarded two-channel variants; their distinction is output safety contract.",
            "No authoritative real-world zero-false-governance claim and no formal R0-P03 result.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--output", action="store_true")
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=True) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as f:
            f.write(text)
    print(json.dumps({
        "id": result["id"],
        "source_world": result["source_cohort"],
        "metrics": result["metrics"],
        "written": bool(args.output),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
