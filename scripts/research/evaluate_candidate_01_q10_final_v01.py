#!/usr/bin/env python3
"""Evaluate the preserved Candidate 01 Q10 first run against the frozen oracle."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path("docs/research/project_knowledge_candidate_01_q10_final_v01")
RESULT = ROOT / "RESULTS_V01.json"
FIRST_RESULT = ROOT / "FIRST_RUN_RESULTS_V01.json"
ORACLE = ROOT / "Q10_FINAL_ORACLE_V01.json"
OUTPUT = ROOT / "EVALUATION_V01.json"
Q10_IDS = {"KA-R30", "KA-R40", "KA-R41"}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate() -> dict[str, Any]:
    result = load(RESULT)
    expected = load(ORACLE)["expectations"]
    budgets = {item["budget_id"]: item for item in result["budgets"]}
    final_items = {item["id"]: item for item in result["final_items"]}
    boundary = result["final_boundary"]
    behavioral = result["behavioral_gate"]

    checks = {
        "source_hashes_match": len(result["source_verification"]) == 17 and all(item.get("verified") is True for item in result["source_verification"]),
        "budget_B01": budgets["B01_BROAD_CURRENT_CORE"]["disposition"] == "PASS",
        "budget_B02": budgets["B02_NARROW_CONSEQUENTIAL_TASK"]["disposition"] == "PASS",
        "budget_B03": budgets["B03_CROSS_PROVIDER_AUTHORITY_TASK"]["disposition"] == "PASS",
        "budget_B04": budgets["B04_REAL_WORKSTREAM_STRESS"]["disposition"] == "PASS",
        "budget_pass_count": sum(item["disposition"] == "PASS" for item in result["budgets"]) == expected["budget_pass_count"],
        "dimension_count": len(behavioral["dimension_coverage"]["distinct_dimensions"]) == expected["dimension_count"],
        "scenario_count": behavioral["scenario_count"] == expected["scenario_count"],
        "all_relevant_dimensions_pass": behavioral["dimension_coverage"]["counts"].get("PASS") == behavioral["dimension_coverage"]["required"] and not behavioral["failed_dimensions"],
        "structural_gate_pass": result["structural_gate"]["disposition"] == "PASS",
        "behavioral_gate_pass": behavioral["disposition"] == "PASS",
        "non_q10_final_passes": sum(item["final_disposition"] == "PASS" and item["id"] not in Q10_IDS for item in result["final_items"]) == expected["non_q10_final_passes"],
        "q10_KA_R30": final_items["KA-R30"]["final_disposition"] == "PASS" and expected["q10_item_passes"]["KA-R30"] is True,
        "q10_KA_R40": final_items["KA-R40"]["final_disposition"] == "PASS" and expected["q10_item_passes"]["KA-R40"] is True,
        "q10_KA_R41": final_items["KA-R41"]["final_disposition"] == "PASS" and expected["q10_item_passes"]["KA-R41"] is True,
        "final_qualified_passes": boundary["final_qualified_pass_count"] == expected["final_qualified_passes"],
        "final_qualified_failures": boundary["final_qualified_failure_count"] == expected["final_qualified_failures"],
        "target_selection_allowed": boundary["target_selection_allowed"] is expected["target_selection_allowed"],
        "target_selected": boundary["target_selected"] is expected["target_selected"],
        "authority_switch_allowed": boundary["authority_switch_allowed"] is expected["authority_switch_allowed"],
        "h3_reopen": boundary["h3_object_primary_reopening_evidence_triggered"] is expected["h3_reopen"],
        "first_run_preserved_exactly": RESULT.read_bytes() == FIRST_RESULT.read_bytes(),
        "oracle_blind_first_run": result["provenance"]["oracle_read"] is False and result["provenance"]["q10_oracle_reads"] == 0,
        "no_post_result_semantic_repair": result["provenance"]["post_result_semantic_repair_occurred"] is False,
    }

    return {
        "schema_version": 1,
        "evaluation_id": "PKA-C01-Q10-FINAL-EVAL-V01",
        "fixture_id": result["fixture_id"],
        "result_sha256": sha(RESULT),
        "first_run_result_sha256": sha(FIRST_RESULT),
        "checks": checks,
        "passed": sum(checks.values()),
        "failed": sum(not value for value in checks.values()),
        "failed_checks": [name for name, value in checks.items() if not value],
        "q10_final_support": all(checks.values()),
        "implementation_repairs_before_first_successful_result": result["provenance"]["implementation_repairs_before_first_successful_result"],
        "pre_execution_repair": result["provenance"]["pre_execution_repair"],
        "final_qualified_passes": boundary["final_qualified_pass_count"],
        "final_qualified_failures": boundary["final_qualified_failure_count"],
        "target_selection_allowed": boundary["target_selection_allowed"],
        "target_selected": boundary["target_selected"],
        "authority_switch_allowed": boundary["authority_switch_allowed"],
    }


def main() -> int:
    output = evaluate()
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    return 0 if output["failed"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
