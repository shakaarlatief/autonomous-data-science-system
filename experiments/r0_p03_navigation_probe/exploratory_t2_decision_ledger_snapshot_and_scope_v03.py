"""Actual Git decision-section status across two recorded source snapshots.

Compares deliberately weak lexical/latest/accepted shortcuts against typed
source-snapshot and exact decision-identity checking. All results concern what
original repository documentation records, not external operative authority,
independent natural-question correctness or a B0-B4 physical architecture.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import ROOT

IDENTIFIER = "R0_P03_T2_EXPLORATORY_REAL_DECISION_SNAPSHOT_AND_SCOPE_V03"
CONTRACT = "EXPLORATORY_T2_DECISION_LEDGER_SNAPSHOT_AND_SCOPE_CONTRACT_V03.md"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_t2_decision_ledger_snapshot_and_scope_result_v03.json"
REVISIONS = {
    "S0": "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef",
    "S1": "6d484dd5d35884f55a9bb15dd1adf8b1e3afc3d3",
}
SOURCE_PATH = "docs/DECISIONS.md"
HEADING = re.compile(r"^## (D-\d{3})\.\s+(.+?)\s*$")
FIELD = re.compile(r"^\*\*(Status|Date|Superseded in scope):\*\*\s*(.*?)\s*$")
SUPERS = re.compile(r"^Superseded\b", re.I)
NOT_OPERATIONAL = re.compile(r"\bnot yet operational authority\b", re.I)
ACCEPTED = re.compile(r"^Accepted\b", re.I)
TOKEN = re.compile(r"[a-z0-9]+", re.I)
K = 5


def original_git_blob(revision: str) -> bytes:
    """Read an exact public original Git blob; never source mutable worktree."""
    r = subprocess.run(
        ["git", "show", f"{revision}:{SOURCE_PATH}"],
        cwd=ROOT, capture_output=True, check=True,
    )
    return r.stdout


def git_blob_id(raw: bytes) -> str:
    """Compute Git's content-addressed loose-blob SHA-1 from original bytes."""
    return sha1(b"blob " + str(len(raw)).encode("ascii") + b"\0" + raw).hexdigest()


def witness(line_number: int, text: str) -> dict[str, Any]:
    return {
        "line": line_number,
        "source_line": text,
        "line_sha256": sha256(text.encode("utf-8")).hexdigest(),
    }


def parse_sections(raw: bytes, snapshot: str) -> dict[str, dict[str, Any]]:
    """Parse section and status as source text, with honest scoped evidence.

    A section is bounded by the next D-NNN level-two heading. Other Markdown
    headings are part of the current decision section and cannot silently
    alter its state. The parser refuses duplicate IDs and multiple Status
    declarations rather than guessing which represents the operative fact.
    """
    lines = raw.decode("utf-8").splitlines(keepends=True)
    positions = [(i, m) for i, line in enumerate(lines)
                 if (m := HEADING.fullmatch(line.rstrip("\r\n")))]
    records = {}
    for i, (start, match) in enumerate(positions):
        end = positions[i + 1][0] if i + 1 < len(positions) else len(lines)
        did, title = match.group(1), match.group(2).strip()
        if did in records:
            raise ValueError(f"duplicate decision ID {did} in {snapshot}")
        fields = {}
        for line_index in range(start + 1, end):
            original = lines[line_index].rstrip("\r\n")
            m = FIELD.fullmatch(original)
            if m is not None:
                name, value = m.groups()
                if name in fields:
                    raise ValueError(f"duplicate {name} field for {did}")
                fields[name] = {
                    "normalized_value": value.strip(),
                    "witness": witness(line_index + 1, original),
                }
        if "Status" not in fields:
            raise ValueError(f"missing explicit Status for {did}")
        status = fields["Status"]["normalized_value"]
        category = (
            "RECORDED_SUPERSESSION_WITH_SCOPE" if SUPERS.search(status)
            else "RECORDED_SELECTED_NOT_OPERATIVE" if NOT_OPERATIONAL.search(status)
            else "OTHER_RECORDED_DECISION"
        )
        section_text = "".join(lines[start:end])
        records[did] = {
            "snapshot": snapshot,
            "source_document": SOURCE_PATH,
            "id": did,
            "title": title,
            "heading_fragment": did,
            "heading_witness": witness(start + 1, lines[start].rstrip("\r\n")),
            "source_status": status,
            "source_status_category": category,
            "status_witness": fields["Status"]["witness"],
            "date": fields.get("Date"),
            "superseded_in_scope": fields.get("Superseded in scope"),
            "section_start_line": start + 1,
            "section_end_line": end,
            "section_sha256": sha256(section_text.encode("utf-8")).hexdigest(),
            "original_section_text": section_text,
            "operative_authority_proven": False,
        }
    if len(records) != (35 if snapshot == "S0" else 36):
        raise ValueError(f"Unexpected actual {snapshot} decision population: {len(records)}")
    return dict(sorted(records.items()))


def normalized_title(text: str) -> str:
    return " ".join(TOKEN.findall(text.lower()))


def create_questions(
    snapshots: dict[str, dict[str, dict[str, Any]]]
) -> list[dict[str, Any]]:
    """Generate all 94 case fields before any retrieval index is built."""
    current_ids = sorted(snapshots["S1"])
    if current_ids != [f"D-{i:03d}" for i in range(1, 37)]:
        raise ValueError("Current decision ledger IDs drift")
    tasks = []
    pairs = [
        ("D-003", "D-011"), ("D-015", "D-024"),
        ("D-028", "D-035"), ("D-033", "D-036"),
        ("D-035", "D-036"),
    ]
    for snapshot in ("S0", "S1"):
        for did in current_ids:
            tasks.append({
                "family": "RECORDED_STATUS",
                "snapshot": snapshot,
                "requested_decision_id": did,
                "requested_title": None,
                "intent": "RECORDED_STATUS",
                "question": f"In recorded Git source snapshot {snapshot}, what Status and supersession scope, if any, are explicitly recorded for decision {did}?",
            })
        for did in ("D-900", "D-901", "D-902", "D-903"):
            tasks.append({
                "family": "UNKNOWN_ID",
                "snapshot": snapshot,
                "requested_decision_id": did,
                "requested_title": None,
                "intent": "RECORDED_STATUS",
                "question": f"Does this exact source snapshot {snapshot} record decision {did}? If no section is found, report only that bounded absence.",
            })
        for did, other in pairs:
            other_title = snapshots["S1"][other]["title"]
            tasks.append({
                "family": "CONFLICTING_ID_TITLE",
                "snapshot": snapshot,
                "requested_decision_id": did,
                "requested_title": other_title,
                "intent": "RECORDED_STATUS",
                "question": f"For snapshot {snapshot}, give the recorded Status of decision {did} under title '{other_title}'. Refuse if ID and title are inconsistent.",
            })
        for did in ("D-035", "D-036"):
            tasks.append({
                "family": "OPERATIVE_GOVERNANCE",
                "snapshot": snapshot,
                "requested_decision_id": did,
                "requested_title": None,
                "intent": "OPERATIVE_GOVERNANCE",
                "question": f"Does decision {did} currently have operative governing authority according to the explicit record at snapshot {snapshot}? Do not infer from 'Accepted'.",
            })
    counts = Counter(q["family"] for q in tasks)
    if counts != {
        "RECORDED_STATUS": 72,
        "UNKNOWN_ID": 8,
        "CONFLICTING_ID_TITLE": 10,
        "OPERATIVE_GOVERNANCE": 4,
    }:
        raise ValueError("Wrong frozen question family count")
    for i, q in enumerate(tasks):
        q["id"] = f"T2-V03-{i+1:03d}"
    return tasks


def lexical_query(did: str, title: str | None) -> str:
    tokens = TOKEN.findall(did)
    if title:
        tokens.extend(TOKEN.findall(title))
    return " OR ".join('"' + t + '"' for t in tokens)


def index_sections(records: dict[str, dict[str, Any]]) -> sqlite3.Connection:
    db = sqlite3.connect(":memory:")
    db.execute("CREATE VIRTUAL TABLE sections_fts USING fts5(id UNINDEXED, body, tokenize='unicode61')")
    for did, row in sorted(records.items()):
        db.execute("INSERT INTO sections_fts (id, body) VALUES (?,?)", (did, row["original_section_text"]))
    db.commit()
    db.execute("PRAGMA query_only=ON")
    return db


def search_sections(db: sqlite3.Connection, did: str, title: str | None) -> list[str]:
    return [
        r[0] for r in db.execute(
            "SELECT id FROM sections_fts WHERE sections_fts MATCH ? "
            "ORDER BY bm25(sections_fts) ASC, id ASC LIMIT ?",
            (lexical_query(did, title), K),
        )
    ]


def source_evidence(row: dict[str, Any], git_sha: str, blob_sha: str) -> dict[str, Any]:
    return {
        "revision": git_sha,
        "source_document": SOURCE_PATH,
        "git_blob_sha1": blob_sha,
        "decision_id": row["id"],
        "decision_fragment": row["heading_fragment"],
        "decision_title": row["title"],
        "section_sha256": row["section_sha256"],
        "source_status": row["source_status"],
        "source_status_category": row["source_status_category"],
        "status_witness": row["status_witness"],
        "superseded_in_scope": row["superseded_in_scope"],
        "date_witness": row["date"],
        "not_independent_operational_governance": True,
    }


def guarded_answer(
    question: dict[str, Any],
    record: dict[str, dict[str, Any]],
    revision: str,
    blob_sha: str,
) -> dict[str, Any]:
    did = question["requested_decision_id"]
    row = record.get(did)
    if row is None:
        return {
            "state": "NOT_RECORDED_IN_THIS_SNAPSHOT",
            "asserted_decision_id": None,
            "status_category": None,
            "evidence": None,
            "coverage": f"Only {SOURCE_PATH} at exact snapshot {revision}",
            "operative_governance_claimed": False,
        }
    title = question["requested_title"]
    if title is not None and normalized_title(title) != normalized_title(row["title"]):
        return {
            "state": "CONFLICTING_IDENTITY",
            "asserted_decision_id": None,
            "status_category": None,
            "evidence": None,
            "coverage": f"Decision {did} exists but the supplied full title conflicts with its own section heading",
            "operative_governance_claimed": False,
        }
    evidence = source_evidence(row, revision, blob_sha)
    if question["intent"] == "OPERATIVE_GOVERNANCE":
        state = (
            "RECORDED_NOT_YET_OPERATIONAL"
            if row["source_status_category"] == "RECORDED_SELECTED_NOT_OPERATIVE"
            else "UNSUPPORTED_OPERATIVE_GOVERNANCE"
        )
    elif question["intent"] == "RECORDED_STATUS":
        state = "ASSERTED_RECORDED_DECISION_STATUS"
    else:
        raise ValueError("Unknown request intent")
    return {
        "state": state,
        "asserted_decision_id": row["id"] if state in (
            "ASSERTED_RECORDED_DECISION_STATUS", "RECORDED_NOT_YET_OPERATIONAL"
        ) else None,
        "status_category": row["source_status_category"] if state != "UNSUPPORTED_OPERATIVE_GOVERNANCE" else None,
        "evidence": evidence if state != "UNSUPPORTED_OPERATIVE_GOVERNANCE" else None,
        "coverage": f"Only {SOURCE_PATH} at exact snapshot {revision}",
        "operative_governance_claimed": False,
    }


def run() -> dict[str, Any]:
    blobs = {k: original_git_blob(v) for k, v in REVISIONS.items()}
    sections = {k: parse_sections(blobs[k], k) for k in REVISIONS}
    tasks = create_questions(sections)
    # No source text, source ID, source title or question set changes after
    # looking at any lexical rankings. All top K share identical snapshot
    # scope with the guarded source-ID lookup.
    dbs = {k: index_sections(rows) for k, rows in sections.items()}
    original_blob_ids = {k: git_blob_id(raw) for k, raw in blobs.items()}
    findings = []
    try:
        for q in tasks:
            snapshot = q["snapshot"]
            revision = REVISIONS[snapshot]
            candidates = search_sections(dbs[snapshot], q["requested_decision_id"], q["requested_title"])
            first = sections[snapshot].get(candidates[0]) if candidates else None
            status_of_first = first["source_status"] if first else None
            latest = sections["S1"].get(q["requested_decision_id"])
            naive_latest_status = latest["source_status"] if latest is not None else None
            naive_operative = bool(
                first and ACCEPTED.match(first["source_status"])
            )
            guarded = guarded_answer(q, sections[snapshot], revision, original_blob_ids[snapshot])
            two_channel = {
                "evidence_assertion": guarded,
                "lexical_candidate_decision_ids_not_authority": candidates,
            }
            expected = sections[snapshot].get(q["requested_decision_id"])
            # Evaluation sees documented original sections only; it does not
            # certify the real world, operational activation or owner identity.
            expected_status = expected["source_status"] if expected else None
            findings.append({
                **q,
                "expected_record_from_this_git_snapshot_for_evaluation_only": (
                    source_evidence(expected, revision, original_blob_ids[snapshot])
                    if expected is not None else None
                ),
                "lexical_top_k_decision_sections": candidates,
                "lexical_top_1_decision_id": first["id"] if first else None,
                "lexical_top_1_recorded_status": status_of_first,
                "lexical_top_1_false_decision_identity": (
                    first is not None and first["id"] != q["requested_decision_id"]
                ),
                "naive_latest_only_recorded_status": naive_latest_status,
                "naive_latest_snapshot_leakage": (
                    q["family"] == "RECORDED_STATUS"
                    and naive_latest_status != expected_status
                ),
                "naive_accepted_is_operative": naive_operative,
                "naive_false_positive_operative_against_explicit_not_yet": (
                    q["family"] == "OPERATIVE_GOVERNANCE"
                    and expected is not None
                    and expected["source_status_category"] == "RECORDED_SELECTED_NOT_OPERATIVE"
                    and naive_operative
                ),
                "guarded_id_and_snapshot": guarded,
                "two_channel_guarded": two_channel,
                "correct_source_status_for_evaluation_only": (
                    q["family"] == "RECORDED_STATUS"
                    and guarded["state"] == "ASSERTED_RECORDED_DECISION_STATUS"
                    and guarded["asserted_decision_id"] == q["requested_decision_id"]
                    and expected is not None
                    and guarded["evidence"]["source_status"] == expected_status
                ),
                "false_guarded_recorded_status_claim_for_evaluation_only": (
                    guarded["state"] == "ASSERTED_RECORDED_DECISION_STATUS"
                    and (expected is None or guarded["evidence"]["source_status"] != expected_status)
                ),
            })
    finally:
        for db in dbs.values():
            db.close()

    totals = Counter(row["family"] for row in findings)
    states = {
        kind: dict(sorted(Counter(
            f["guarded_id_and_snapshot"]["state"] for f in findings
            if f["family"] == kind
        ).items()))
        for kind in ("RECORDED_STATUS", "UNKNOWN_ID", "CONFLICTING_ID_TITLE", "OPERATIVE_GOVERNANCE")
    }
    metrics = {
        "requests": len(findings),
        "family_counts": dict(sorted(totals.items())),
        "states_by_family": states,
        "documented_source_status_correct_for_existing_ledger_sections": sum(
            r["correct_source_status_for_evaluation_only"] for r in findings
        ),
        "original_recorded_status_requests": 72,
        "missing_at_s0_D_036_is_scoped_absence": any(
            r["requested_decision_id"] == "D-036" and r["snapshot"] == "S0"
            and r["guarded_id_and_snapshot"]["state"] == "NOT_RECORDED_IN_THIS_SNAPSHOT"
            for r in findings
        ),
        "naive_latest_snapshot_leakage": sum(r["naive_latest_snapshot_leakage"] for r in findings),
        "lexical_top1_false_decision_identity_all_requests": sum(r["lexical_top_1_false_decision_identity"] for r in findings),
        "naive_accepted_operative_false_positive_against_explicit_source_statement": sum(
            r["naive_false_positive_operative_against_explicit_not_yet"] for r in findings
        ),
        "guarded_false_recorded_status_claims": sum(r["false_guarded_recorded_status_claim_for_evaluation_only"] for r in findings),
        "guarded_positive_operative_authority_claims": sum(r["guarded_id_and_snapshot"]["operative_governance_claimed"] for r in findings),
        "nonassertive_candidates_preserved_for_every_request": all(
            r["two_channel_guarded"]["lexical_candidate_decision_ids_not_authority"] == r["lexical_top_k_decision_sections"]
            for r in findings
        ),
        "scope_preserved_supersession_sections": sum(
            r["guarded_id_and_snapshot"]["evidence"] is not None
            and r["guarded_id_and_snapshot"]["evidence"]["superseded_in_scope"] is not None
            for r in findings if r["family"] == "RECORDED_STATUS"
            and r["requested_decision_id"] in ("D-003", "D-011", "D-015")
        ),
        "independent_currentness_gold": False,
        "operative_activation_verified": False,
    }
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "source_revisions": REVISIONS,
        "source_document": SOURCE_PATH,
        "original_git_blobs": {
            k: {"revision": REVISIONS[k], "bytes": len(blobs[k]),
                "sha256": sha256(blobs[k]).hexdigest(), "git_blob_sha1": original_blob_ids[k]}
            for k in REVISIONS
        },
        "actual_source_sections": sections,
        "requests_and_results": findings,
        "metrics": metrics,
        "scientific_limits": [
            "Direct status retrieval is only self-consistency with the same document sections used for reference; no independent owner/source authority gold.",
            "Exact decision IDs are parsed request fields, not natural-language resolved referents.",
            "The two Git commits are recorded source snapshots, not timestamps of real owner decisions.",
            "Some supersessions are explicitly scope-limited, not global invalidation of an entire historical decision.",
            "Selected successor target is not yet operational authority according to source status, but real deployment was not independently inspected.",
            "Naive latest and accepted shortcuts are deliberately unsound negative controls, not equally capable B0-B4 retrieval arms.",
            "The decision ledger and prior 65/120 source sets have already been exposed; counts are regression results, not arm-neutral architecture scoring.",
            "No B2/B3/B4 distinctive mechanism, independent author, formal R0-P03 score or physical target choice.",
        ],
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    result = run()
    raw = json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as file:
            file.write(raw)
    print(json.dumps({
        "identifier": result["identifier"],
        "source_sections": {k: len(x) for k, x in result["actual_source_sections"].items()},
        "metrics": result["metrics"],
        "output_saved": args.output,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
