from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ART = ROOT / "docs/research/project_knowledge_candidate_01_q4_real_v01"
FIXTURE = ART / "Q4_REAL_FIXTURE_V01.json"
ORACLE = ART / "Q4_REAL_ORACLE_V01.json"
DAG = ART / "SHADOW_Q4_WORKSTREAM_DAG.json"
RESULT = ART / "RESULTS_V01.json"
FIRST_RESULT = ART / "FIRST_RUN_RESULTS_V01.json"
EVAL = ART / "EVALUATION_V01.json"
EVAL_SCRIPT = ROOT / "scripts/research/evaluate_candidate_01_q4_real_v01.py"

EXPECTED = {
    "fixture": "5046c5cfa6672e8467ba91c30c8dd0212267df6cd7cfb316f875d11299ccca40",
    "oracle": "1aa4225794ec5eaf0085bc6c961270e4a178dba55443d24550ca729696386e79",
    "dag": "6f7e7bb4a387590320129da12bbde30d9e01ea1122489c48b2c13c1b226bfc35",
    "result": "85e9bf340c62ee9eeea860e53f4b40d3f753a5e0c83bb6c115678aa95532ac44",
    "evaluation": "f29a13fd1246aaa85714932b7b2faba0d97796b54cdf13b59ebdd27b6b707cff",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_frozen_hashes_and_first_run_preservation():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED["fixture"]
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED["oracle"]
    assert hashlib.sha256(DAG.read_bytes()).hexdigest() == EXPECTED["dag"]
    assert hashlib.sha256(RESULT.read_bytes()).hexdigest() == EXPECTED["result"]
    assert RESULT.read_bytes() == FIRST_RESULT.read_bytes()


def test_oracle_blind_first_run_provenance():
    result = load(RESULT)
    assert result["provenance"]["oracle_reads"] == 0
    assert result["provenance"]["evaluation_artifact_reads"] == 0
    assert result["provenance"]["run_ordinal"] == 1
    assert result["provenance"]["result_existed_at_start"] is False


def test_all_declared_sources_verified():
    result = load(RESULT)
    assert len(result["source_verification"]) == 10
    assert all(item["verified"] for item in result["source_verification"])


def test_multi_dependency_dag_and_runnable_states():
    result = load(RESULT)
    case = {x["case_id"]: x for x in result["cases"]}["Q4-R01"]
    q4 = case["nodes"]["WS-Q4-STRESS"]
    q10 = case["nodes"]["WS-Q10-FINAL"]
    assert q4["depends_on"] == ["WS-Q125-INTEGRATED", "WS-Q9-MIGRATION"]
    assert q4["runnable"] is True
    assert q10["depends_on"] == ["WS-Q4-STRESS", "WS-Q1-PORTABILITY", "WS-Q2-HARD-CASES"]
    assert q10["runnable"] is False
    assert result["metrics"]["multi_dependency_node_count"] == 2
    assert result["metrics"]["dependency_edge_count"] == 7


def test_interruption_recovery_uses_receipts_without_replay():
    result = load(RESULT)
    case = {x["case_id"]: x for x in result["cases"]}["Q4-R02"]
    assert case["completed_steps"] == ["S1", "S2"]
    assert case["pending_steps"] == ["S3", "S4", "S5"]
    assert case["next_resume_step"] == "S3"
    assert case["blind_replay_required"] is False
    assert case["recovery_replay_count"] == 0
    assert case["interruption"]["transition_mutated"] is False
    assert case["interruption"]["dag_mutated"] is False


def test_stale_update_is_rejected_without_mutation_and_fresh_updates_apply():
    result = load(RESULT)
    case = {x["case_id"]: x for x in result["cases"]}["Q4-R03"]
    attempts = {x["attempt_id"]: x for x in case["attempts"]}
    assert attempts["WRITER-B-FRESH"]["status"] == "APPLIED"
    assert attempts["WRITER-B-FRESH"]["mutated"] is True
    assert "STALE_REVISION" in attempts["WRITER-A-STALE"]["status"]
    assert attempts["WRITER-A-STALE"]["mutated"] is False
    assert attempts["WRITER-A-STALE"]["sha256_before"] == attempts["WRITER-A-STALE"]["sha256_after"]
    assert attempts["WRITER-C-FRESH"]["status"] == "APPLIED"
    assert attempts["WRITER-C-FRESH"]["mutated"] is True


def test_revision_basis_and_live_target_safety():
    result = load(RESULT)
    case = {x["case_id"]: x for x in result["cases"]}["Q4-R03"]
    assert case["base_revision"]["hash_basis"] == "GIT_BLOB_BYTES_AT_COMMIT"
    assert case["live_target"]["unchanged"] is True
    assert result["metrics"]["stale_attempt_mutation"] is False


def test_evaluation_passes_with_only_nonsemantic_label_variance():
    evaluation = load(EVAL)
    assert hashlib.sha256(EVAL.read_bytes()).hexdigest() == EXPECTED["evaluation"]
    assert evaluation["passed"] == 20
    assert evaluation["failed"] == 0
    assert evaluation["q4_real_source_stress_support"] is True
    variance = evaluation["oracle_label_variance"]
    assert variance["literal_match"] is False
    assert variance["semantic_match"] is True
    assert variance["disposition"] == "NON_SEMANTIC_LABEL_VARIANCE"


def test_evaluator_recomputes_exactly():
    spec = importlib.util.spec_from_file_location("q4_eval", EVAL_SCRIPT)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    assert mod.evaluate() == load(EVAL)
