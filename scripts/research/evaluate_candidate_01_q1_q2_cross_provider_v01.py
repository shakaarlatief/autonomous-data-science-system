#!/usr/bin/env python3
"""Evaluate the frozen Candidate 01 cross-provider Q1+Q2 result."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path("docs/research/project_knowledge_candidate_01_q1_q2_cross_provider_v01")
RESULT = ROOT / "EXTERNAL_PROVIDER_RESULT_V01.json"
FIRST_RESULT = ROOT / "FIRST_RUN_EXTERNAL_PROVIDER_RESULT_V01.json"
ORACLE = ROOT / "Q1_Q2_CROSS_PROVIDER_ORACLE_V01.json"
OUTPUT = ROOT / "EVALUATION_V01.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate() -> dict[str, Any]:
    result = load(RESULT)
    expected = load(ORACLE)["expectations"]

    checks = {
        "provider_non_openai": result["provider"].strip().lower() not in {"openai", "chatgpt"},
        "exact_model_recorded": bool(result["model"].strip()),
        "fresh_session": result["fresh_session"] is True,
        "prior_ads_context_false": result["prior_ads_context"] is False,
        "packet_id_exact": result["packet_id"] == "PKA-C01-Q1-Q2-CROSS-PROVIDER-V01",
        "task_a_resolved_semantics": result["task_a"]["resolution_status"].startswith("RESOLVED"),
        "task_a_governing_ids": result["task_a"]["governing_ids"] == expected["task_a"]["governing_ids"],
        "task_a_retrieval_non_authoritative": result["task_a"]["retrieval_used_as_authority"] is False,
        "task_b_unresolved_semantics": result["task_b"]["resolution_status"].startswith("UNRESOLVED"),
        "task_b_governing_ids_empty": result["task_b"]["governing_ids"] == [],
        "task_b_retrieval_non_authoritative": result["task_b"]["retrieval_used_as_authority"] is False,
        "task_b_missing_scope_visible": bool(result["task_b"]["missing_scope_or_conflict"].strip()),
        "task_c_resolved_semantics": result["task_c"]["resolution_status"].startswith("RESOLVED"),
        "task_c_governing_architecture_ids": result["task_c"]["governing_architecture_ids"] == expected["task_c"]["governing_architecture_ids"],
        "task_c_retained_outcomes": result["task_c"]["retained_outcomes"] == expected["task_c"]["retained_outcomes"],
        "task_c_public_git_exclusion": result["task_c"]["public_git_source_binaries_allowed_merely_because_ads_consumes_them"] is False,
        "task_c_retrieval_non_authoritative": result["task_c"]["retrieval_used_as_authority"] is False,
        "receipt_base_commit": result["authority_receipt"]["source_base_commit"] == expected["authority_receipt"]["source_base_commit"],
        "receipt_retrieval_non_authoritative": result["authority_receipt"]["retrieval_is_non_authoritative"] is True,
        "first_run_preserved_exactly": RESULT.read_bytes() == FIRST_RESULT.read_bytes(),
    }

    variances = {
        "task_b_status": {
            "oracle": expected["task_b"]["resolution_status"],
            "observed": result["task_b"]["resolution_status"],
            "literal_match": result["task_b"]["resolution_status"] == expected["task_b"]["resolution_status"],
            "semantic_match": checks["task_b_unresolved_semantics"],
        },
        "task_c_status": {
            "oracle": expected["task_c"]["resolution_status"],
            "observed": result["task_c"]["resolution_status"],
            "literal_match": result["task_c"]["resolution_status"] == expected["task_c"]["resolution_status"],
            "semantic_match": checks["task_c_resolved_semantics"] and checks["task_c_retained_outcomes"],
        },
    }

    return {
        "schema_version": 1,
        "evaluation_id": "PKA-C01-Q1-Q2-CROSS-PROVIDER-EVAL-V01",
        "fixture_id": "PKA-C01-Q1-Q2-CROSS-PROVIDER-V01",
        "result_sha256": sha(RESULT),
        "first_run_result_sha256": sha(FIRST_RESULT),
        "checks": checks,
        "passed": sum(checks.values()),
        "failed": sum(not value for value in checks.values()),
        "failed_checks": [name for name, value in checks.items() if not value],
        "status_label_variances": variances,
        "cross_provider_q1_q2_support": all(checks.values()),
        "supported_mechanism_ids": expected["supported_mechanism_ids"],
        "final_qualification_claimed": False,
        "target_architecture_selected": False,
    }


def main() -> int:
    output = evaluate()
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0 if output["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
