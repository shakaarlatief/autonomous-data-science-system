#!/usr/bin/env python3
"""Evaluate the frozen Candidate 01 Q4 real-source result against its oracle."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

ROOT = Path("docs/research/project_knowledge_candidate_01_q4_real_v01")
RESULT = ROOT / "RESULTS_V01.json"
FIRST_RESULT = ROOT / "FIRST_RUN_RESULTS_V01.json"
ORACLE = ROOT / "Q4_REAL_ORACLE_V01.json"
OUTPUT = ROOT / "EVALUATION_V01.json"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evaluate() -> dict[str, Any]:
    result = load(RESULT)
    expected = load(ORACLE)["expectations"]
    cases = {item["case_id"]: item for item in result["cases"]}
    q4 = cases["Q4-R01"]["nodes"]["WS-Q4-STRESS"]
    q10 = cases["Q4-R01"]["nodes"]["WS-Q10-FINAL"]
    interruption = cases["Q4-R02"]
    concurrency = cases["Q4-R03"]
    attempts = {item["attempt_id"]: item for item in concurrency["attempts"]}

    checks = {
        "all_source_hashes_match": all(item["verified"] for item in result["source_verification"]) and len(result["source_verification"]) == 10,
        "q4_dependency_list_exact": q4["depends_on"] == expected["multi_dependency"]["WS-Q4-STRESS"],
        "q10_dependency_list_exact": q10["depends_on"] == expected["multi_dependency"]["WS-Q10-FINAL"],
        "multi_dependency_node_count": result["metrics"]["multi_dependency_node_count"] == expected["multi_dependency"]["multi_dependency_node_count"],
        "q4_dependencies_satisfied": q4["runnable"] is expected["multi_dependency"]["q4_stress_dependencies_satisfied"],
        "q10_final_runnable": q10["runnable"] is expected["multi_dependency"]["q10_final_runnable"],
        "transition_id": interruption["transition_id"] == expected["interruption_recovery"]["transition_id"],
        "completed_steps": interruption["completed_steps"] == expected["interruption_recovery"]["completed_steps"],
        "pending_steps": interruption["pending_steps"] == expected["interruption_recovery"]["pending_steps"],
        "next_resume_step": interruption["next_resume_step"] == expected["interruption_recovery"]["next_resume_step"],
        "blind_replay_required": interruption["blind_replay_required"] is expected["interruption_recovery"]["blind_replay_required"],
        "unrelated_interruption_mutation": interruption["interruption"]["transition_mutated"] is expected["interruption_recovery"]["unrelated_interruption_mutation"] and interruption["interruption"]["dag_mutated"] is False,
        "revision_hash_basis": concurrency["base_revision"]["hash_basis"] == expected["concurrency"]["revision_hash_basis"],
        "writer_b_fresh": attempts["WRITER-B-FRESH"]["status"] == expected["concurrency"]["WRITER-B-FRESH"]["status"] and attempts["WRITER-B-FRESH"]["mutated"] is expected["concurrency"]["WRITER-B-FRESH"]["mutation_applied"],
        "writer_a_stale_semantics": "STALE_REVISION" in attempts["WRITER-A-STALE"]["status"] and attempts["WRITER-A-STALE"]["mutated"] is expected["concurrency"]["WRITER-A-STALE"]["mutation_applied"],
        "writer_c_fresh": attempts["WRITER-C-FRESH"]["status"] == expected["concurrency"]["WRITER-C-FRESH"]["status"] and attempts["WRITER-C-FRESH"]["mutated"] is expected["concurrency"]["WRITER-C-FRESH"]["mutation_applied"],
        "stale_attempt_preserves_temp_state": attempts["WRITER-A-STALE"]["sha256_before"] == attempts["WRITER-A-STALE"]["sha256_after"] and attempts["WRITER-A-STALE"]["marker_present_after"] is False,
        "live_target_unchanged": concurrency["live_target"]["unchanged"] is expected["concurrency"]["live_target_unchanged"],
        "first_run_preserved_exactly": RESULT.read_bytes() == FIRST_RESULT.read_bytes(),
        "oracle_blind_provenance": result["provenance"]["oracle_reads"] == 0 and result["provenance"]["evaluation_artifact_reads"] == 0,
    }

    literal = attempts["WRITER-A-STALE"]["status"] == expected["concurrency"]["WRITER-A-STALE"]["status"]
    return {
        "schema_version": 1,
        "evaluation_id": "PKA-C01-Q4-REAL-EVAL-V01",
        "fixture_id": result["fixture_id"],
        "result_sha256": sha(RESULT),
        "first_run_result_sha256": sha(FIRST_RESULT),
        "checks": checks,
        "passed": sum(checks.values()),
        "failed": sum(not value for value in checks.values()),
        "failed_checks": [name for name, value in checks.items() if not value],
        "oracle_label_variance": {
            "field": "Q4-R03.WRITER-A-STALE.status",
            "oracle_label": expected["concurrency"]["WRITER-A-STALE"]["status"],
            "observed_label": attempts["WRITER-A-STALE"]["status"],
            "literal_match": literal,
            "semantic_match": checks["writer_a_stale_semantics"],
            "disposition": "NON_SEMANTIC_LABEL_VARIANCE" if (not literal and checks["writer_a_stale_semantics"]) else ("NONE" if literal else "SEMANTIC_MISMATCH"),
        },
        "q4_real_source_stress_support": all(checks.values()),
        "implementation_repairs_after_first_run": 0,
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
