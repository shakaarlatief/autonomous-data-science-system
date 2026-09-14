from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_q7_real_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01/Q7_REAL_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01/Q7_REAL_ORACLE_V01.json"
RECEIPT = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01/PRIVATE_EVIDENCE_RECEIPT_V01.json"
FIRST_RUN = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01/FIRST_RUN_RESULTS_V01.json"
FINAL_RESULT = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01/RESULTS_V01.json"
EXPECTED_FIXTURE_SHA256 = "a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef"
EXPECTED_ORACLE_SHA256 = "f85ec95c45b31c4ab9d643737f23bb55c9c269a0fc9915b0c009252aac7b82f4"
EXPECTED_RECEIPT_SHA256 = "d9c5648e0a62cb2b6fa6b96c4615e1513cff8d48fc5ff3179c8f5aa4abdf0a66"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_q7_real_v01", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_result():
    module = load_module()
    fixture, digest = module.load_fixture(FIXTURE)
    receipt = module.load_receipt(RECEIPT, fixture)
    return module.run_probe(fixture, digest, receipt)


def expected():
    return json.loads(ORACLE.read_text(encoding="utf-8"))["expectations"]


def test_frozen_fixture_oracle_and_private_receipt_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA256
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA256
    assert hashlib.sha256(RECEIPT.read_bytes()).hexdigest() == EXPECTED_RECEIPT_SHA256


def test_implementation_is_oracle_blind():
    source = SCRIPT.read_text(encoding="utf-8")
    assert "Q7_REAL_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_real_public_sources_and_private_receipt_bindings_match():
    result = run_result()
    exp = expected()
    assert result["all_public_source_hashes_match"] is exp["all_public_source_hashes_match"]
    assert result["private_evidence_binding_match"] is exp["private_evidence_binding_match"]
    assert result["observed_private_anchor"] == exp["observed_private_anchor"]


def test_public_contract_evidence_is_complete():
    checks = run_result()["public_contract_checks"]
    assert checks
    assert all(checks.values())


def test_public_only_continuation_preserves_resolved_private_when_private_unavailable():
    scenario = run_result()["scenarios"]["Q7-S01"]
    assert scenario == expected()["scenarios"]["Q7-S01"]
    assert scenario["private_continuity_status"] == "NOT_VERIFIED"
    assert scenario["public_resolved_private_preserved"] is True


def test_private_required_work_fails_visibly_when_unverified_or_stale():
    scenarios = run_result()["scenarios"]
    assert scenarios["Q7-S02"] == expected()["scenarios"]["Q7-S02"]
    assert scenarios["Q7-S03"] == expected()["scenarios"]["Q7-S03"]
    assert scenarios["Q7-S02"]["task_disposition"] == "BLOCK_REQUIRED_PRIVATE_UNVERIFIED"
    assert scenarios["Q7-S03"]["task_disposition"] == "BLOCK_PRIVATE_CONTINUITY_FAIL"


def test_public_safe_projection_leaks_no_private_values_or_paths():
    result = run_result()
    scenario = result["scenarios"]["Q7-S04"]
    exp = expected()["scenarios"]["Q7-S04"]
    for key, value in exp.items():
        assert scenario[key] == value
    assert result["global_private_value_leak_count"] == 0
    assert result["global_private_paths_serialized_count"] == 0
    rendered = json.dumps(result, sort_keys=True)
    assert re.search(r"[A-Za-z]:\\", rendered) is None
    assert re.search(r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", rendered) is None
    assert "http://" not in rendered
    assert "https://" not in rendered


def test_optional_retrieval_unavailability_does_not_bypass_authority():
    scenario = run_result()["scenarios"]["Q7-S05"]
    assert scenario == expected()["scenarios"]["Q7-S05"]
    assert scenario["optional_retrieval_authority_bypass"] is False


def test_q7_real_subsystem_support_matches_oracle_without_overclaiming():
    result = run_result()
    assert result["q7_real_subsystem_support"] is expected()["q7_real_subsystem_support"]
    assert result["q7_real_subsystem_support"] is True
    assert result["interpretation"]["q7_final_qualification_claimed"] is False
    assert result["interpretation"]["architecture_selection_claimed"] is False
    assert result["interpretation"]["public_repository_integrity_reclassified_by_private_status"] is False


def test_first_run_is_byte_identical_to_final_result():
    assert FIRST_RUN.read_bytes() == FINAL_RESULT.read_bytes()
