from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "docs/research/project_knowledge_candidate_01_q10_final_v01"
FIXTURE = ART / "Q10_FINAL_FIXTURE_V01.json"
ORACLE = ART / "Q10_FINAL_ORACLE_V01.json"
RESULT = ART / "RESULTS_V01.json"
FIRST_RESULT = ART / "FIRST_RUN_RESULTS_V01.json"
EVALUATION = ART / "EVALUATION_V01.json"
EVAL_SCRIPT = ROOT / "scripts/research/evaluate_candidate_01_q10_final_v01.py"

EXPECTED_FIXTURE_SHA = "c62b54e7cb9903a175449d89c5383ed8843b2a8da236688173201a0d429db57c"
EXPECTED_ORACLE_SHA = "02349331fe405630599eb5dbd08401892517cdc87bfbdfdfee38983b7c80a15c"
EXPECTED_RESULT_SHA = "7855357e68ba29414b82a39039f62abb62ec4ddc295070f2949b072583ba8663"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_frozen_fixture_oracle_and_first_run_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA
    assert hashlib.sha256(RESULT.read_bytes()).hexdigest() == EXPECTED_RESULT_SHA
    assert RESULT.read_bytes() == FIRST_RESULT.read_bytes()


def test_first_run_is_oracle_blind_and_unrepaired_after_result():
    provenance = load(RESULT)["provenance"]
    assert provenance["run_ordinal"] == 1
    assert provenance["oracle_read"] is False
    assert provenance["q10_oracle_reads"] == 0
    assert provenance["post_result_semantic_repair_occurred"] is False
    assert provenance["implementation_repairs_before_first_successful_result"] == 1
    assert "KA-R23" in provenance["pre_execution_repair"]


def test_all_frozen_sources_and_budgets_pass():
    result = load(RESULT)
    assert len(result["source_verification"]) == 17
    assert all(item["verified"] for item in result["source_verification"])
    assert len(result["budgets"]) == 4
    assert all(item["disposition"] == "PASS" for item in result["budgets"])


def test_structural_gate_and_complete_unit_suite_pass():
    gate = load(RESULT)["structural_gate"]
    assert gate["disposition"] == "PASS"
    assert all(gate["checks"].values())
    assert gate["real_item_count"] == 64
    coverage = gate["unit_partition_coverage"]
    assert coverage["exactly_once"] is True
    assert coverage["inventory_unchanged"] is True
    assert len(coverage["complete_current_file_set"]) == 30
    assert coverage["missing"] == []
    assert coverage["extra"] == []
    assert coverage["duplicates"] == []
    assert sum(part["counts"].get("PASS", 0) for part in gate["unit_partitions"]) == 300


def test_behavioral_multidimensional_gate_is_complete_without_aggregate_score():
    result = load(RESULT)
    gate = result["behavioral_gate"]
    assert gate["disposition"] == "PASS"
    assert gate["scenario_count"] == 9
    assert gate["dimension_coverage"]["required"] == 42
    assert gate["dimension_coverage"]["evaluated"] == 42
    assert gate["dimension_coverage"]["counts"] == {"PASS": 42}
    assert gate["aggregate_score_used"] is False
    assert len(result["scenarios"]) == 9


def test_preserved_limitations_are_visible_and_nonblocking():
    limitations = load(RESULT)["preserved_limitations"]
    assert len(limitations) == 12
    assert all(item["blocks_final_disposition"] is False for item in limitations)
    assert any(item["limitation_id"] == "L01_REAL_TRANSITIONS_UNEXERCISED" for item in limitations)
    assert any(item["limitation_id"] == "L02_SHADOW_MIGRATION_BOUNDARY" for item in limitations)
    assert any(item["limitation_id"] == "L03_AUTHORITY_REMAINS_CURRENT" for item in limitations)


def test_all_67_items_receive_explicit_pass_disposition():
    final_items = load(RESULT)["final_items"]
    assert len(final_items) == 67
    assert len({item["id"] for item in final_items}) == 67
    assert all(item["final_disposition"] == "PASS" for item in final_items)
    by_id = {item["id"]: item for item in final_items}
    assert by_id["KA-R30"]["final_disposition"] == "PASS"
    assert by_id["KA-R40"]["final_disposition"] == "PASS"
    assert by_id["KA-R41"]["final_disposition"] == "PASS"


def test_final_governance_boundary_stops_before_selection_and_authority_switch():
    boundary = load(RESULT)["final_boundary"]
    assert boundary["final_qualified_pass_count"] == 67
    assert boundary["final_qualified_failure_count"] == 0
    assert boundary["failed_item_ids"] == []
    assert boundary["target_selection_allowed"] is True
    assert boundary["target_selected"] is False
    assert boundary["authority_switch_allowed"] is False
    assert boundary["h3_object_primary_reopening_evidence_triggered"] is False


def test_frozen_oracle_comparison_and_evaluator_recompute_pass():
    evaluation = load(EVALUATION)
    assert evaluation["passed"] == 24
    assert evaluation["failed"] == 0
    assert evaluation["q10_final_support"] is True
    assert evaluation["final_qualified_passes"] == 67
    assert evaluation["target_selection_allowed"] is True
    assert evaluation["target_selected"] is False
    assert evaluation["authority_switch_allowed"] is False
    spec = importlib.util.spec_from_file_location("q10_eval", EVAL_SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert module.evaluate() == evaluation
