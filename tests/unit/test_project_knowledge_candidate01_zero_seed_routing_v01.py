from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_zero_seed_routing_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_zero_seed_routing_v01/ZERO_SEED_ROUTING_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_zero_seed_routing_v01/ZERO_SEED_ROUTING_ORACLE_V01.json"
EXPECTED_FIXTURE_SHA256 = "25d302e1fd46afdc1f7e1d363cd8eeedc5881c055aeb2ab79655bae756364594"
EXPECTED_ORACLE_SHA256 = "9687bfe08c32a4bab7718f7f7ace3fb60f6a3d015ff468cbd7431d39c2b38e64"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_zero_seed_routing_v01", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_inputs():
    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    oracle = json.loads(ORACLE.read_text(encoding="utf-8"))
    return fixture, oracle


def run_result():
    module = load_module()
    fixture, digest = module.load_fixture(FIXTURE)
    return module.run_probe(fixture, digest)


def test_frozen_fixture_and_oracle_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA256
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA256


def test_implementation_does_not_read_or_name_oracle():
    source = SCRIPT.read_text(encoding="utf-8")
    assert "ZERO_SEED_ROUTING_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_shadow_sources_and_all_source_hashes_match():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["all_source_hashes_match"] is expected["all_source_hashes_match"]
    assert result["generation"]["shadow_source_kinds"] == expected["shadow_source_kinds"]


def test_generation_reads_no_global_live_state_targets():
    result = run_result()
    fixture, expected_doc = load_inputs()
    expected = expected_doc["expectations"]
    assert result["generation"]["forbidden_generation_path_reads"] == expected["generation_forbidden_path_reads"]
    assert result["generation"]["global_live_state_generation_fact_count"] == expected["generation_global_live_state_fact_count"]
    forbidden = set(fixture["protocol"]["forbidden_generation_paths"])
    assert set(result["generation"]["generation_reads"]).isdisjoint(forbidden)
    assert result["metrics"]["generation_forbidden_path_read_count"] == 0


def test_zero_seed_routing_projection_matches_oracle_and_real_target_exactly():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["generation"]["routing_projection"] == expected["routing_projection"]
    assert result["comparison"]["routing_exact_parity"] is expected["routing_exact_parity"]


def test_semantic_ownership_matches_amended_candidate_model():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["semantic_ownership"] == expected["semantic_ownership"]
    assert result["manual_shadow_source_touch_count"] == expected["manual_shadow_source_touch_count"]
    assert result["global_live_state_generation_fact_count"] == 0


def test_no_broad_project_control_source_is_needed():
    result = run_result()
    assert result["metrics"]["successor_shadow_source_count"] == 2
    assert result["metrics"]["broad_project_control_source_count"] == 0
    assert result["generation"]["shadow_source_kinds"] == {
        "active_workstream": "WORKSTREAM",
        "integration_boundary": "PROJECT_INTEGRATION_BOUNDARY",
    }


def test_comparison_target_is_read_only_after_generation_surface_exists():
    result = run_result()
    assert result["comparison"]["comparison_reads"] == ["docs/current_routing.json"]
    assert result["generation"]["routing_projection"]["current_checkpoint"] == 498
    assert result["generation"]["routing_projection"]["current_boundary"] == "project-knowledge-zero-seed-routing-shadow-next"
