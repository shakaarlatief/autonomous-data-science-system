#!/usr/bin/env python3
"""Evaluate Candidate 01's integrated Q1+Q2+Q5 fresh-collaborator result.

This evaluator intentionally runs only after the independent collaborator has
finished. Unlike the collaborator, the evaluator may read the separately frozen
oracle. It preserves the collaborator output unchanged, checks bounded reads,
authority/risk resolution, stale-view failure, receipt binding, capture state,
and current-authority non-mutation. It also reports a representation-level
source-revision-basis ambiguity exposed by Windows checkout line-ending
normalization without silently changing the frozen experiment.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path("docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01")
DEFAULT_FIXTURE = ROOT / "Q1_Q2_Q5_FIXTURE_V01.json"
DEFAULT_ORACLE = ROOT / "Q1_Q2_Q5_ORACLE_V01.json"
DEFAULT_COLLABORATOR = ROOT / "FRESH_COLLABORATOR_RESULT_V01.json"
DEFAULT_OUTPUT = ROOT / "FRESH_COLLABORATOR_EVALUATION_V01.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob(base: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{base}:{path}"])


def text_contains_all(texts: list[str], tokens: list[str]) -> bool:
    joined = "\n".join(texts).upper()
    return all(token.upper() in joined for token in tokens)


def blocker_concepts(blockers: list[str]) -> dict[str, bool]:
    joined = "\n".join(blockers).upper()
    return {
        "SOURCE_INGESTION_NOT_STARTED": "INGESTION" in joined and "NOT_STARTED" in joined,
        "WORKING_STORE_AUDIT_PENDING": "WORKING-STORE" in joined and "PENDING" in joined,
        "INDEPENDENT_BACKUP_ROUND_TRIP_PENDING": (
            "BACKUP ROUND TRIP" in joined or "BACKUP ROUND-TRIP" in joined
        ) and "PENDING" in joined,
        "CLEAN_RESTORE_PENDING": "CLEAN RESTORE" in joined and "PENDING" in joined,
        "RESTORED_INTEGRITY_AUDIT_PENDING": (
            "RESTORED INTEGRITY AUDIT" in joined or "RESTORED AUDIT" in joined
        ) and "PENDING" in joined,
    }


def current_authority_unchanged(fixture: dict[str, Any]) -> bool:
    # The fixture's real_base_commit predates the committed fixture-freeze checkpoint,
    # which legitimately advanced CURRENT_STATE/current_routing. The collaborator run
    # must therefore be checked for *working-tree mutation relative to the frozen HEAD*,
    # not equality to the earlier real evidence base.
    completed = subprocess.run(
        [
            "git",
            "diff",
            "--quiet",
            "HEAD",
            "--",
            "docs/CURRENT_STATE.md",
            "docs/current_routing.json",
        ],
        check=False,
    )
    return completed.returncode == 0


def source_revision_diagnostic(fixture: dict[str, Any], collaborator: dict[str, Any]) -> dict[str, Any]:
    index_path = Path(
        "docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01/SHADOW_AUTHORITY_RISK_INDEX.json"
    )
    index = load(index_path)
    route = index["task_routes"]["AUTHORITY-ROUTE-SOURCE-VAULT-COURSE2"]
    indexed_sha = route["governing_sources"][0]["sha256"]
    governing_path = Path(route["governing_sources"][0]["path"])
    working_raw = governing_path.read_bytes()
    git_raw = git_blob(fixture["real_base_commit"], governing_path.as_posix())
    working_sha = sha256_bytes(working_raw)
    git_sha = sha256_bytes(git_raw)
    lf_normalized_sha = sha256_bytes(working_raw.replace(b"\r\n", b"\n"))
    receipt_sha = collaborator["authority_receipt"]["source_revision"]
    return {
        "indexed_sha256": indexed_sha,
        "receipt_sha256": receipt_sha,
        "git_blob_sha256": git_sha,
        "working_tree_raw_sha256": working_sha,
        "working_tree_lf_normalized_sha256": lf_normalized_sha,
        "indexed_matches_git_blob": indexed_sha == git_sha,
        "indexed_matches_working_tree_raw": indexed_sha == working_sha,
        "indexed_matches_working_tree_lf_normalized": indexed_sha == lf_normalized_sha,
        "receipt_follows_frozen_index": receipt_sha == indexed_sha,
        "finding": (
            "SOURCE_REVISION_BASIS_AMBIGUOUS"
            if indexed_sha == git_sha and indexed_sha != working_sha
            else "NO_BASIS_AMBIGUITY_OBSERVED"
        ),
        "interpretation": (
            "The frozen index binds canonical Git-blob bytes at the exact base, while the Windows "
            "working tree exposes CRLF-transformed bytes. The receipt obeys the frozen request, but a "
            "bare sha256 field is insufficiently explicit about revision/hash basis. Future successor "
            "receipts/index entries should bind commit + path + hash basis (for example GIT_BLOB_BYTES) "
            "or an equally explicit canonicalization contract."
        ),
    }


def evaluate(fixture: dict[str, Any], oracle: dict[str, Any], collaborator: dict[str, Any]) -> dict[str, Any]:
    exp = oracle["expectations"]
    reads = collaborator["reads"]
    allowed = fixture["allowed_collaborator_reads"]
    size_by_path = {
        item["path"]: item["bytes"]
        for item in fixture["real_sources"] + fixture["shadow_sources"]
    }
    read_bytes = sum(size_by_path[path] for path in reads)
    forbidden = set(fixture["protocol"]["forbidden_legacy_bootstrap_paths"])

    task_a = collaborator["task_a"]
    task_b = collaborator["task_b"]
    receipt = collaborator["authority_receipt"]
    capture = collaborator["capture_candidate"]
    concepts = blocker_concepts(task_a["blockers"])

    checks = {
        "result_schema_top_level": all(
            key in collaborator
            for key in ("collaborator", "reads", "task_a", "task_b", "authority_receipt", "capture_candidate")
        ),
        "read_paths_unique": len(reads) == len(set(reads)),
        "reads_within_allowlist": set(reads).issubset(set(allowed)),
        "read_budget_count": len(reads) <= exp["budget"]["max_allowed_read_count"],
        "forbidden_legacy_bootstrap_reads_zero": len(set(reads) & forbidden) == exp["budget"]["forbidden_legacy_bootstrap_read_count"],
        "course2_blocked": "BLOCK" in task_a["decision"].upper() and "NOT" in task_a["decision"].upper(),
        "governing_source_exact": exp["task_a"]["required_governing_source"] in task_a["governing_sources"],
        "required_evidence_sources": set(exp["task_a"]["required_evidence_sources"]).issubset(set(task_a["evidence_sources"])),
        "historical_distractor_rejected": exp["task_a"]["required_distractor_rejection"] in task_a["distractors_rejected"],
        "required_risks_activated": set(exp["task_a"]["required_risk_ids"]) == set(task_a["activated_risks"]),
        "required_blocker_concepts": all(concepts.get(key, False) for key in exp["task_a"]["required_blocker_concepts"]),
        "required_workstream": receipt["workstream"] == exp["task_a"]["required_workstream"],
        "stale_view_rejected": "FAIL" in task_b["decision"].upper() and "AUTHORIZE" in task_b["decision"].upper(),
        "stale_view_id_exact": task_b["stale_view_id"] == exp["task_b"]["required_view_id"],
        "stale_failure_concept": "SOURCE_BINDING_MISMATCH" in task_b["reason"],
        "receipt_task_exact": receipt["task"] == "COURSE2_ADMISSION_DECISION",
        "receipt_governing_source_exact": receipt["governing_source"] == exp["task_a"]["required_governing_source"],
        "receipt_revision_binding": receipt["source_revision"] == exp["receipt"]["must_bind_governing_source_sha256"],
        "receipt_risks_present": bool(receipt["activated_risks"]) and set(exp["task_a"]["required_risk_ids"]).issubset(set(receipt["activated_risks"])),
        "receipt_blockers_present": bool(receipt["blockers"]),
        "capture_non_authoritative": capture["state"] == "CAPTURED_NON_AUTHORITATIVE",
        "capture_has_source_basis": bool(capture["source_basis"]) and set(capture["source_basis"]).issubset(set(allowed)),
        "capture_not_auto_promoted": not (ROOT / "SHADOW_PROMOTED_KNOWLEDGE_V01.md").exists(),
        "capture_requests_review_not_self_promotion": capture["promotion_recommendation"] in {"REVIEW_FOR_PROMOTION", "DO_NOT_PROMOTE"},
        "current_authority_unchanged": current_authority_unchanged(fixture),
    }
    return {
        "schema_version": 1,
        "evaluation_id": "PKA-C01-Q1-Q2-Q5-FRESH-COLLABORATOR-EVAL-V01",
        "fixture_id": fixture["fixture_id"],
        "collaborator_result_sha256": sha256_bytes(DEFAULT_COLLABORATOR.read_bytes()),
        "checks": checks,
        "passed": sum(checks.values()),
        "failed": sum(not value for value in checks.values()),
        "failed_checks": [key for key, value in checks.items() if not value],
        "blocker_concept_coverage": concepts,
        "budget": {
            "evidence_read_count": len(reads),
            "evidence_read_bytes_from_frozen_manifest": read_bytes,
            "max_allowed_read_count": exp["budget"]["max_allowed_read_count"],
            "legacy_bootstrap_read_count": len(set(reads) & forbidden),
            "all_allowed_reads_used": set(reads) == set(allowed),
        },
        "source_revision_diagnostic": source_revision_diagnostic(fixture, collaborator),
        "promotion_eligible_for_review": (
            all(checks.values())
            and capture["promotion_recommendation"] == "REVIEW_FOR_PROMOTION"
            and bool(capture["statement"].strip())
        ),
        "oracle_result": "PASS" if all(checks.values()) else "FAIL",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, default=DEFAULT_FIXTURE)
    parser.add_argument("--oracle", type=Path, default=DEFAULT_ORACLE)
    parser.add_argument("--collaborator", type=Path, default=DEFAULT_COLLABORATOR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    fixture = load(args.fixture)
    oracle = load(args.oracle)
    collaborator = load(args.collaborator)
    result = evaluate(fixture, oracle, collaborator)
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["oracle_result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
