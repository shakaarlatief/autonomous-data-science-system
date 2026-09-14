#!/usr/bin/env python3
"""Finalize the integrated Q1+Q2+Q5 qualification after explicit promotion review."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path("docs/research/project_knowledge_candidate_01_q1_q2_q5_integrated_v01")
DECLARATION_RE = re.compile(
    r"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\r?\n(.*?)\r?\n<!-- PKA-STRUCTURED-DECLARATION-END -->",
    re.DOTALL,
)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def declaration(path: Path) -> dict[str, Any]:
    match = DECLARATION_RE.search(path.read_text(encoding="utf-8"))
    if not match:
        raise RuntimeError(f"structured declaration missing: {path}")
    return json.loads(match.group(1))


def authority_unchanged() -> bool:
    completed = subprocess.run(
        ["git", "diff", "--quiet", "HEAD", "--", "docs/CURRENT_STATE.md", "docs/current_routing.json"],
        check=False,
    )
    return completed.returncode == 0


def finalize() -> dict[str, Any]:
    collaborator_path = ROOT / "FRESH_COLLABORATOR_RESULT_V01.json"
    first_collaborator_path = ROOT / "FIRST_RUN_FRESH_COLLABORATOR_RESULT_V01.json"
    evaluation_path = ROOT / "FRESH_COLLABORATOR_EVALUATION_V01.json"
    first_eval_path = ROOT / "FIRST_RUN_EVALUATION_V01.json"
    second_eval_path = ROOT / "SECOND_RUN_EVALUATION_V01.json"
    review_path = ROOT / "PROMOTION_REVIEW_V01.json"
    promoted_path = ROOT / "SHADOW_PROMOTED_KNOWLEDGE_V01.md"

    collaborator = load(collaborator_path)
    evaluation = load(evaluation_path)
    review = load(review_path)
    promoted = declaration(promoted_path)

    capture = collaborator["capture_candidate"]
    review_checks = review["checks"]
    exact_engine_recorded = any(
        token in collaborator["collaborator"].lower()
        for token in ("gpt-", "claude", "gemini", "astra", "engine=")
    )
    checks = {
        "fresh_collaborator_result_preserved_exactly": collaborator_path.read_bytes() == first_collaborator_path.read_bytes(),
        "fresh_collaborator_oracle_evaluation_pass": evaluation["oracle_result"] == "PASS" and evaluation["failed"] == 0,
        "fresh_collaborator_budget_pass": evaluation["budget"]["evidence_read_count"] <= evaluation["budget"]["max_allowed_read_count"] and evaluation["budget"]["legacy_bootstrap_read_count"] == 0,
        "explicit_promotion_review_all_checks_pass": bool(review_checks) and all(review_checks.values()),
        "explicit_promotion_review_accepts": review["decision"] == "ACCEPT_FOR_SHADOW_PROMOTION",
        "promoted_statement_matches_capture": promoted["statement"] == capture["statement"],
        "promoted_source_basis_matches_capture": promoted["source_basis"] == capture["source_basis"],
        "promoted_source_is_shadow_only": promoted["shadow_only"] is True and promoted["current_project_authority"] is False,
        "promotion_transition_was_not_automatic": capture["state"] == "CAPTURED_NON_AUTHORITATIVE" and review["decision"] == "ACCEPT_FOR_SHADOW_PROMOTION",
        "current_authority_unchanged": authority_unchanged(),
        "source_revision_basis_ambiguity_preserved": evaluation["source_revision_diagnostic"]["finding"] == "SOURCE_REVISION_BASIS_AMBIGUOUS",
    }

    return {
        "schema_version": 1,
        "result_id": "PKA-C01-Q1-Q2-Q5-INTEGRATED-FINAL-V01",
        "collaborator_result_sha256": sha(collaborator_path),
        "first_collaborator_result_sha256": sha(first_collaborator_path),
        "evaluation_sha256": sha(evaluation_path),
        "first_evaluator_run_sha256": sha(first_eval_path),
        "second_evaluator_run_sha256": sha(second_eval_path),
        "promotion_review_sha256": sha(review_path),
        "promoted_knowledge_sha256": sha(promoted_path),
        "collaborator_repairs": 0,
        "evaluator_repairs": 2,
        "evaluator_repair_summary": [
            "First evaluator implementation compared Windows checkout raw bytes directly with an earlier Git-blob base, conflating line-ending transformation and checkpoint progression with collaborator mutation.",
            "Second evaluator implementation used Git diff semantics but still compared against the pre-fixture real base rather than the committed fixture-freeze HEAD. Final evaluator checks working-tree mutation against frozen HEAD.",
        ],
        "checks": checks,
        "passed": sum(checks.values()),
        "failed": sum(not value for value in checks.values()),
        "failed_checks": [key for key, value in checks.items() if not value],
        "budget": evaluation["budget"],
        "capture_transition": [
            "EMPTY_BEFORE_COLLABORATOR_RUN",
            "CAPTURED_NON_AUTHORITATIVE",
            "PROMOTED_WITHIN_CANDIDATE_01_SHADOW_AFTER_EXPLICIT_REVIEW",
        ],
        "promoted_semantic_id": promoted["semantic_id"],
        "source_revision_binding_finding": evaluation["source_revision_diagnostic"],
        "architecture_amendment_required": "EXPLICIT_SOURCE_REVISION_BASIS_DESCRIPTOR",
        "collaborator_exact_engine_provenance_recorded": exact_engine_recorded,
        "collaborator_provenance_limitation": (
            "The result establishes a fresh manual Codex collaborator session but does not preserve an exact engine/thread identifier. "
            "This is sufficient for conversation-independence evidence but not for a provider/engine-portability claim."
        ),
        "integrated_q1_q2_q5_shadow_support": all(checks.values()),
        "final_qualification_claimed": False,
        "target_architecture_selected": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "FINAL_INTEGRATED_RESULT_V01.json")
    args = parser.parse_args()
    result = finalize()
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
