from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_real_shadow_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_real_shadow_v01/REAL_SHADOW_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_real_shadow_v01/REAL_SHADOW_ORACLE_V01.json"
EXPECTED_FIXTURE_SHA256 = "9e8cd2ce0be7ced69eabc246414bd9aa0f21b305e03efeffd81db86c222d42bc"
EXPECTED_ORACLE_SHA256 = "7e42889a65ac181feb9bcdc9fdacdab2d6d7e295aa2ed1a71583bd5beb4cf32b"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_real_shadow_v01", SCRIPT)
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


def test_fixture_has_no_answer_keys_and_implementation_does_not_read_oracle():
    fixture, _ = load_inputs()
    forbidden = set(fixture["protocol"]["forbidden_answer_keys"])

    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                assert key not in forbidden
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(fixture)
    source = SCRIPT.read_text(encoding="utf-8")
    assert "REAL_SHADOW_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_all_real_source_hashes_match_exact_base():
    result = run_result()["manifest_verification"]
    assert result["all_match"] is True
    assert all(item["bytes_match"] and item["sha256_match"] for item in result["sources"].values())


def test_generation_never_reads_comparison_targets():
    result = run_result()
    fixture, oracle = load_inputs()
    expected = oracle["expectations"]
    comparison_targets = set(fixture["protocol"]["comparison_targets"])
    assert result["generation"]["generation_reads_comparison_targets"] is expected["generation_reads_comparison_targets"]
    assert set(result["generation"]["source_reads"]).isdisjoint(comparison_targets)
    assert result["metrics"]["generation_comparison_target_read_count"] == 0


def test_real_workstream_route_and_migration_seed_burden_match_oracle():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["workstreams"]["route"] == expected["workstream_route"]
    assert result["workstreams"]["migration_seed_workstreams"] == expected["migration_seed_workstreams"]
    assert result["migration_seed_project_control"]["fact_count"] == expected["project_control_global_fact_count"]
    assert result["migration_seed_project_control"]["facts"] == [
        "active_pr",
        "promoted_integration_branch",
        "promoted_integration_sha",
    ]


def test_generated_routing_matches_oracle_and_real_target_exactly():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["generation"]["routing_projection"] == expected["routing_projection"]
    assert result["comparison"]["routing_exact_parity"] is expected["routing_exact_parity"]


def test_current_state_semantic_markers_match_real_target():
    result = run_result()["comparison"]["current_state_semantic_parity"]
    expected = load_inputs()[1]["expectations"]["current_state_semantic_parity"]
    assert result == expected


def test_real_continuity_contract_aligns_and_bad_plan_fails_visible():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["continuity_contract"]["aligned"] is expected["continuity_contract_alignment"]
    for attempt_id, exp in expected["continuity_action_attempts"].items():
        assert result["continuity_action_attempts"][attempt_id] == exp


def test_generated_navigation_and_real_knowledge_map_membership_match():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["generation"]["navigation_projection"] == expected["generated_navigation"]
    assert result["comparison"]["knowledge_map_membership"] == expected["knowledge_map_membership"]


def test_real_capture_remains_candidate_and_does_not_auto_promote():
    result = run_result()["generation"]["real_capture"]
    expected = load_inputs()[1]["expectations"]
    assert result["authority_class"] == expected["real_capture_authority"]
    assert result["authority_class"] == "candidate"


def test_comparison_reads_happen_only_after_generation_surface_is_complete():
    result = run_result()
    assert result["comparison"]["comparison_reads"] == [
        "routing_target",
        "current_state_target",
        "knowledge_map_target",
    ]
    assert result["generation"]["routing_projection"]["current_checkpoint"] == 496
    assert result["metrics"]["migration_seed_workstream_count"] == 1
    assert result["metrics"]["migration_seed_project_control_fact_count"] == 3
