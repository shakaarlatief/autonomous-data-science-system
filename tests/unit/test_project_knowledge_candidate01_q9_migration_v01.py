from __future__ import annotations

import hashlib
import importlib.util
import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_q9_migration_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_q9_migration_v01/Q9_MIGRATION_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_q9_migration_v01/Q9_MIGRATION_ORACLE_V01.json"
FIRST_RUN = ROOT / "docs/research/project_knowledge_candidate_01_q9_migration_v01/FIRST_RUN_RESULTS_V01.json"
FINAL_RESULT = ROOT / "docs/research/project_knowledge_candidate_01_q9_migration_v01/RESULTS_V01.json"
EXPECTED_FIXTURE_SHA256 = "5f6fec6c812692f8b085dde8f15ddc8c1f80a2695bf75933a80d736eeb83dfcc"
EXPECTED_ORACLE_SHA256 = "8994b9be935480aec58f9b1e25ba386a8ad979ac8f45c06665ac7d596d1c3015"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_q9_migration_v01", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_expected():
    return json.loads(ORACLE.read_text(encoding="utf-8"))["expectations"]


@lru_cache(maxsize=1)
def run_result():
    module = load_module()
    fixture, digest = module.load_fixture(FIXTURE)
    return module.run_probe(fixture, digest)


def test_frozen_fixture_and_oracle_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA256
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA256


def test_implementation_is_oracle_blind_and_switch_forbidden():
    source = SCRIPT.read_text(encoding="utf-8")
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert "Q9_MIGRATION_ORACLE" not in source
    assert "ORACLE_V01" not in source
    assert fixture["protocol"]["implementation_may_read_oracle"] is False
    assert fixture["protocol"]["authority_switch_forbidden"] is True
    assert fixture["protocol"]["rollback_export_must_not_overwrite_live_paths"] is True


def test_all_frozen_sources_match_and_policy_markers_are_grounded():
    result = run_result()
    assert result["all_source_hashes_match"] is True
    assert result["policy_grounding"] == {"P01": True, "P02": True, "P03": True, "P04": True}


def test_all_ten_migration_units_match_the_frozen_oracle():
    result = run_result()
    expected = load_expected()
    assert result["migration_unit_parity"] == expected["migration_unit_parity"]
    assert len(result["migration_unit_parity"]) == expected["migration_unit_count"] == 10
    assert all(result["migration_unit_parity"].values())


def test_semantic_identity_is_path_independent_and_provenance_is_bound_to_real_base():
    result = run_result()["identity_and_provenance"]
    expected = load_expected()["identity_and_provenance"]
    for key, value in expected.items():
        assert result[key] == value
    assert result["all_sources_shadow_only"] is True
    assert result["migration_provenance_bound_to_real_base"] is True


def test_reverse_reference_baseline_is_preserved_by_compatibility_paths():
    result = run_result()
    expected = load_expected()
    assert result["reverse_reference_counts"] == expected["reverse_reference_counts"]
    assert result["broken_reverse_reference_target_count"] == 0


def test_rollback_export_round_trips_routing_and_passes_legacy_validator():
    result = run_result()["rollback_export"]
    expected = load_expected()["rollback_export"]
    for key, value in expected.items():
        assert result[key] == value
    assert "Current routing consistency: PASS" in result["legacy_validator_output"]
    assert result["exported_routing"]["current_checkpoint"] == 508
    assert result["exported_routing"]["current_boundary"] == "project-knowledge-migration-rollback-shadow-next"


def test_rollback_export_does_not_mutate_live_authority_or_leave_export_tree():
    result = run_result()["rollback_export"]
    assert result["live_authority_mutation_detected"] is False
    assert not (ROOT / ".tmp/pka-c01-q9-migration-export").exists()


def test_authority_switch_stays_fail_closed_despite_rollback_and_integrity_pass():
    result = run_result()["authority_switch"]
    expected = load_expected()["authority_switch"]
    for key, value in expected.items():
        assert result[key] == value
    assert result["rollback_proof"] is True
    assert result["public_repository_integrity_pass"] is True
    assert result["experiment_forbids_switch"] is True
    assert result["allowed"] is False


def test_self_hosting_migration_state_matches_oracle():
    result = run_result()["self_hosting"]
    expected = load_expected()["self_hosting"]
    for key, value in expected.items():
        assert result[key] == value
    assert result["complete"] is True


def test_q9_subsystem_support_passes_without_final_qualification_or_selection():
    result = run_result()
    assert result["q9_shadow_subsystem_support"] is load_expected()["q9_shadow_subsystem_support"] is True
    interpretation = result["interpretation"]
    assert interpretation["q9_final_qualification_claimed"] is False
    assert interpretation["production_authority_migrated"] is False
    assert interpretation["rollback_executed_against_live_authority"] is False
    assert interpretation["target_architecture_selected"] is False


def test_first_run_is_byte_identical_to_final_result():
    assert FIRST_RUN.read_bytes() == FINAL_RESULT.read_bytes()
