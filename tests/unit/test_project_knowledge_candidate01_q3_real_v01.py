from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_q3_real_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/Q3_REAL_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/Q3_REAL_ORACLE_V01.json"
FIRST_RUN = ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/FIRST_RUN_RESULTS_V01.json"
FINAL_RESULT = ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/RESULTS_V01.json"
EXPECTED_FIXTURE_SHA256 = "d30a3968e901b6f273a25ddef8d1ebbe093e1040e74f3ab80ba68ce523760ab6"
EXPECTED_ORACLE_SHA256 = "74c0684ec341311f0f91241f8f79bbe02c83d699784406b0d886bca34994f8a8"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_q3_real_v01", SCRIPT)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_inputs():
    return (
        json.loads(FIXTURE.read_text(encoding="utf-8")),
        json.loads(ORACLE.read_text(encoding="utf-8")),
    )


def run_result():
    module = load_module()
    fixture, digest = module.load_fixture(FIXTURE)
    return module.run_probe(fixture, digest)


def test_frozen_fixture_and_oracle_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA256
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA256


def test_implementation_is_oracle_blind():
    source = SCRIPT.read_text(encoding="utf-8")
    assert "Q3_REAL_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_all_frozen_sources_match_exact_hashes():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["all_source_hashes_match"] is expected["all_source_hashes_match"]


def test_all_five_real_semantic_cases_match_frozen_oracle():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["real_semantics_alignment"] == expected["real_semantics_alignment"]
    assert result["real_semantic_query_failures"] == []


def test_scoped_supersession_stays_source_local_and_does_not_invent_dates():
    result = run_result()["real_semantics_alignment"]
    assert result["Q3-R01"]["successor_for_external_source_architecture_uncertainty"] == "D-033"
    assert result["Q3-R01"]["retained_outcomes"] == ["public_git_source_binary_exclusion"]
    assert result["Q3-R02"]["invented_per_successor_effective_dates"] is False
    assert len(result["Q3-R02"]["scope_successors"]) == 6


def test_real_carrier_identity_repair_preserves_semantic_identity_without_collision():
    result = run_result()["real_semantics_alignment"]["Q3-R03"]
    assert result["semantic_id"] == "MILESTONE-SOURCE-FAITHFUL-REINTEGRATION"
    assert result["original_recorded_identity"] == "Checkpoint 252"
    assert result["original_identity_disposition"] == "RETIRED_PROVENANCE_ONLY"
    assert result["rename_commit"] == "b79d6ae0187b61e73c3b08312e4c7ec9d8f7f61d"
    assert result["identity_collision"] is False


def test_paused_workstream_and_epistemic_transition_are_selectively_structured():
    result = run_result()["real_semantics_alignment"]
    assert result["Q3-R04"]["state"] == "PAUSED"
    assert result["Q3-R04"]["semantic_identity_preserved_while_paused"] is True
    assert result["Q3-R05"]["message001_role"] == "INDEPENDENT_CANDIDATE_DESIGN"
    assert result["Q3-R05"]["current_thread_state"] == "COMPARATIVE_ONLY"
    assert result["Q3-R05"]["message003_and_later_role"] == "COMPARATIVE_REVIEW"


def test_complexity_measurements_match_frozen_bounds():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    for key, value in expected["complexity_bounds"].items():
        assert result["complexity"][key] == value
    assert result["complexity"]["source_local_relation_count"] == 7
    assert result["complexity"]["selective_temporal_field_count"] == 5


def test_no_h3_reopen_trigger_fires_on_final_implementation():
    result = run_result()
    expected = load_inputs()[1]["expectations"]
    assert result["h3_reopen"] is expected["h3_reopen"]
    assert result["h3_reopen"] is False
    assert not any(result["h3_reopen_triggers"].values())


def test_first_run_failure_is_preserved_and_final_result_repairs_only_evidence_location_check():
    first = json.loads(FIRST_RUN.read_text(encoding="utf-8"))
    final = json.loads(FINAL_RESULT.read_text(encoding="utf-8"))
    assert len(first["real_semantic_query_failures"]) == 1
    assert first["real_semantic_query_failures"][0].startswith("Q3-R03:")
    assert first["h3_reopen"] is True
    assert final["real_semantic_query_failures"] == []
    assert final["h3_reopen"] is False
    assert final["real_semantics_alignment"]["Q3-R01"] == first["real_semantics_alignment"]["Q3-R01"]
    assert final["real_semantics_alignment"]["Q3-R02"] == first["real_semantics_alignment"]["Q3-R02"]
    assert final["real_semantics_alignment"]["Q3-R04"] == first["real_semantics_alignment"]["Q3-R04"]
    assert final["real_semantics_alignment"]["Q3-R05"] == first["real_semantics_alignment"]["Q3-R05"]


def test_probe_does_not_overclaim_q3_or_architecture_selection():
    interpretation = run_result()["interpretation"]
    assert interpretation["candidate01_real_q3_support"] is True
    assert interpretation["q3_final_qualification_claimed"] is False
    assert interpretation["architecture_family_selection_claimed"] is False
    assert interpretation["unproven_real_transition_classes"] == ["MERGE", "SPLIT", "TOMBSTONE"]
