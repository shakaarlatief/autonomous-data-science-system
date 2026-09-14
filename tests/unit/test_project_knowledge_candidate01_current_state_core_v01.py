from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_current_state_core_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_current_state_core_v01/CURRENT_STATE_CORE_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_current_state_core_v01/CURRENT_STATE_CORE_ORACLE_V01.json"
EXPECTED_FIXTURE_SHA256 = "4b7ac27801e7d89c0cd782c895d6d0db47693916e4aae7696eb3fc4d6081ad38"
EXPECTED_ORACLE_SHA256 = "f7ceee34aa68d79dea8df4043bf5b1711f3a31078cf86d48bfc3b3f0b008af35"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_current_state_core_v01", SCRIPT)
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
    assert "CURRENT_STATE_CORE_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_all_source_hashes_and_shadow_source_kinds_match():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["all_source_hashes_match"] is expected["all_source_hashes_match"]
    assert result["generation"]["shadow_source_kinds"] == expected["shadow_source_kinds"]


def test_source_vault_successor_state_aligns_with_real_evidence():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["source_vault_evidence_alignment"]["all_aligned"] is expected["source_vault_state_evidence_alignment"]
    assert all(result["source_vault_evidence_alignment"]["checks"].values())
    assert result["source_vault_pause_state"] == expected["source_vault_pause_state"]


def test_compact_current_state_core_matches_frozen_oracle():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["current_state_core"] == expected["current_state_core"]


def test_routing_subset_and_live_current_state_markers_match_real_targets():
    result = run_result()["comparison"]
    expected = load_inputs()[1]["expectations"]
    assert result["routing_subset_exact_parity"] is expected["routing_subset_exact_parity"]
    assert result["current_state_live_marker_parity"] == expected["current_state_live_marker_parity"]


def test_all_must_preserve_items_remain_recoverable_without_core_duplication():
    result = run_result()["generation"]
    expected = load_inputs()[1]["expectations"]
    assert result["must_preserve_items_recoverable"] == expected["must_preserve_items_recoverable"]
    assert result["must_preserve_items_missing"] == expected["must_preserve_items_missing"]
    assert len(result["recoverable_semantics"]) == 23


def test_generation_reads_no_global_targets_and_uses_no_global_target_facts():
    result = run_result()
    fixture, expected_doc = load_inputs()
    expected = expected_doc["expectations"]
    forbidden = set(fixture["protocol"]["forbidden_generation_paths"])
    assert result["generation"]["forbidden_generation_path_reads"] == expected["generation_forbidden_path_reads"]
    assert set(result["generation"]["source_reads"]).isdisjoint(forbidden)
    assert result["generation"]["global_target_generation_fact_count"] == expected["global_target_generation_fact_count"]
    assert result["metrics"]["generation_forbidden_path_read_count"] == 0


def test_old_research113_return_condition_is_detected_as_stale_not_propagated():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["comparison"]["source_vault_old_pause_reason_detected_stale"] is expected["source_vault_old_pause_reason_detected_stale"]
    core_rendered = json.dumps(result["generation"]["current_state_core"], sort_keys=True)
    recoverable_rendered = json.dumps(result["generation"]["recoverable_semantics"], sort_keys=True)
    assert "Research 113" not in core_rendered
    assert "Research 113" not in recoverable_rendered


def test_core_is_small_projection_but_target_history_remains_comparison_only():
    result = run_result()
    assert result["metrics"]["current_state_core_bytes"] == 871
    assert result["metrics"]["current_state_target_bytes"] == 283023
    assert result["metrics"]["core_to_target_byte_ratio"] == 0.003077
    assert result["comparison"]["comparison_reads"] == [
        "docs/current_routing.json",
        "docs/CURRENT_STATE.md",
    ]


def test_shadow_boundary_and_migration_accounting_are_explicit():
    result = run_result()
    assert result["shadow_only"] is True
    assert result["implementation_reads_oracle"] is False
    assert result["metrics"]["successor_shadow_source_count"] == 3
    assert result["metrics"]["new_source_vault_workstream_source_count"] == 1
    assert result["metrics"]["must_preserve_item_count"] == 23
    assert result["metrics"]["must_preserve_recoverable_count"] == 23
