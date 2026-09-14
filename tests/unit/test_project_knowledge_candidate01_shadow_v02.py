from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_shadow_v02.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_FIXTURE_V02.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v02/SHADOW_OPERATIONAL_ORACLE_V02.json"
EXPECTED_FIXTURE_SHA256 = "6daefddd448ead145281d56da8325925cb82c71fc57418283ef21c65418ec486"
EXPECTED_ORACLE_SHA256 = "a1af441f356fbd0e7cac65ba1f6c45589f96941139e669d99de4276acf8440b6"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_shadow_v02", SCRIPT)
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


def test_fixture_contains_no_answer_bearing_keys_and_implementation_does_not_read_oracle():
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
    assert "SHADOW_OPERATIONAL_ORACLE" not in source
    assert "ORACLE_V02" not in source


def test_workstream_route_pause_dag_and_signal_activation_match_oracle():
    result = run_result()["workstreams"]
    expected = load_inputs()[1]["expectations"]["workstreams"]
    baseline = result["baseline"]
    assert baseline["mandatory_route"] == expected["baseline_mandatory_route"]
    assert baseline["paused_visible"] == expected["baseline_paused_visible"]
    assert baseline["blocked_visible"] == expected["baseline_blocked_visible"]
    assert baseline["multiple_dependencies"] == expected["multiple_dependencies"]
    ready = result["private_ready"]
    assert ready["signal_activated_from_pause"] == expected["private_ready_activated"]
    assert ready["active_leaves"] == expected["private_ready_route_leaves"]


def test_interruption_recovery_uses_durable_receipts_without_blind_replay():
    got = run_result()["workstreams"]["interruption_recovery"]
    expected = load_inputs()[1]["expectations"]["workstreams"]["interruption_recovery"]
    for key, value in expected.items():
        assert got[key] == value
    assert got["receipt_evidence"] == ["research:149", "workstream:WS-OPS@rev4"]


def test_workstream_optimistic_concurrency_rejects_stale_and_accepts_fresh():
    got = run_result()["workstreams"]["updates"]
    expected = load_inputs()[1]["expectations"]["workstreams"]
    for attempt_id in ("STALE-WS-OPS", "FRESH-WS-OPS"):
        for key, value in expected[attempt_id].items():
            assert got[attempt_id].get(key) == value
    assert got["STALE-WS-OPS"]["state_after"]["revision"] == 4
    assert got["STALE-WS-OPS"]["state_after"]["current_anchor"] == "shadow-v02"


def test_consolidation_fidelity_blocks_bad_candidate_and_allows_good_candidate():
    result = run_result()["consolidation"]
    expected = load_inputs()[1]["expectations"]["consolidation"]
    assert result["candidates"]["SYN-BAD"] == expected["SYN-BAD"]
    assert result["candidates"]["SYN-GOOD"] == expected["SYN-GOOD"]
    assert result["promotions"]["PROMOTE-BAD"] == expected["PROMOTE-BAD"]
    assert result["promotions"]["PROMOTE-GOOD"] == expected["PROMOTE-GOOD"]


def test_capture_does_not_imply_authority_and_novel_narrative_claim_is_recaptured():
    result = run_result()["consolidation"]
    expected = load_inputs()[1]["expectations"]["consolidation"]
    assert result["capture_authority"]["CAP-2"] == expected["CAP-2-authority"]
    for capture_id in expected["accepted_view_excludes"]:
        assert capture_id in result["accepted_view_excludes"]
    assert result["novel_narrative_claim_capture_ids"] == expected["novel_narrative_claim_capture_ids"]


def test_derived_views_rebuild_exactly_and_match_expected_current_core_and_navigation():
    result = run_result()["derived_views"]
    expected = load_inputs()[1]["expectations"]["derived_views"]
    assert result["routing_rebuild_equal"] is expected["routing_rebuild_equal"]
    assert result["current_state_rebuild_equal"] is expected["current_state_rebuild_equal"]
    assert result["navigation_rebuild_equal"] is expected["navigation_rebuild_equal"]
    assert result["current_state_core"] == expected["current_state_core"]
    assert result["navigation_index"] == expected["navigation_index"]


def test_public_private_boundary_matches_oracle_and_leaks_no_private_values():
    result = run_result()["private_boundary"]
    expected = load_inputs()[1]["expectations"]["private_boundary"]
    for scenario_id, exp in expected.items():
        if scenario_id == "forbidden_public_leaks":
            continue
        got = result["scenarios"][scenario_id]
        for key, value in exp.items():
            assert got.get(key) == value
    assert result["public_leaked_private_values"] == []
    rendered = json.dumps(result, sort_keys=True)
    for forbidden in expected["forbidden_public_leaks"]:
        assert forbidden not in rendered


def test_authority_uncertainty_distinguishes_resolved_missing_conflict_and_optional_degraded():
    result = run_result()["authority_uncertainty"]
    expected = load_inputs()[1]["expectations"]["authority_uncertainty"]
    for scenario_id, exp in expected.items():
        got = result[scenario_id]
        for key, value in exp.items():
            assert got.get(key) == value


def test_operational_metrics_remain_bounded_and_shadow_only():
    result = run_result()
    assert result["shadow_only"] is True
    assert result["implementation_reads_oracle"] is False
    assert result["metrics"] == {
        "workstream_count": 8,
        "paused_count": 2,
        "multi_dependency_workstream_count": 2,
        "promoted_knowledge_count": 1,
        "candidate_capture_count": 2,
        "derived_view_count": 3,
        "public_leak_count": 0,
        "fail_visible_authority_cases": 2,
    }
