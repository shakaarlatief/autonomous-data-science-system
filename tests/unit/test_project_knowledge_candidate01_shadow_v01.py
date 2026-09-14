from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/research/project_knowledge_candidate01_shadow_v01.py"
FIXTURE = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_FIXTURE_V01.json"
ORACLE = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v01/SHADOW_ORACLE_V01.json"
EXPECTED_FIXTURE_SHA256 = "77ffecc278995ef03130d962f863d46ccebac41d446de7099cc666750e8b66f7"
EXPECTED_ORACLE_SHA256 = "3ced74eb18f4d792c9a43eaf2b3d6956c497bc7b85c71bfc6b5e226f840fc38b"


def load_module():
    spec = importlib.util.spec_from_file_location("candidate01_shadow_v01", SCRIPT)
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
    fixture, _ = module.load_fixture(FIXTURE)
    return module.run_probe(fixture, EXPECTED_FIXTURE_SHA256)


def test_frozen_fixture_and_oracle_hashes():
    assert hashlib.sha256(FIXTURE.read_bytes()).hexdigest() == EXPECTED_FIXTURE_SHA256
    assert hashlib.sha256(ORACLE.read_bytes()).hexdigest() == EXPECTED_ORACLE_SHA256


def test_fixture_contains_no_answer_bearing_joint_authority_flags():
    fixture, _ = load_inputs()
    forbidden = set(fixture["protocol"]["admission_answer_flags_forbidden"])

    def walk(value):
        if isinstance(value, dict):
            for key, item in value.items():
                assert key not in forbidden
                walk(item)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    walk(fixture)


def test_implementation_does_not_read_or_name_oracle():
    source = SCRIPT.read_text(encoding="utf-8")
    assert "SHADOW_ORACLE" not in source
    assert "ORACLE_V01" not in source


def test_contract_drift_matches_frozen_oracle():
    result = run_result()
    _, oracle = load_inputs()
    assert result["contract_drift"] == oracle["expectations"]["contract_drift"]


def test_authority_admission_preserves_natural_direction_and_admits_symmetric_case():
    result = run_result()["authority_admission"]
    expected = load_inputs()[1]["expectations"]["authority_admission"]

    publish = result["publish_release"]
    assert publish["governing_sources"] == expected["publish_release"]["governing_sources"]
    assert publish["joint_authority_objects_created"] == 0
    assert publish["natural_direction_owner"] == expected["publish_release"]["natural_direction_owner"]
    assert publish["gate"]["J2"] is False

    near_miss = result["deploy_service_eu"]
    assert near_miss["governing_sources"] == expected["deploy_service_eu"]["governing_sources"]
    assert near_miss["joint_authority_objects_created"] == 0
    assert near_miss["admission_status"] == expected["deploy_service_eu"]["admission_status"]
    assert near_miss["gate"]["J2"] is False

    positive = result["approve_joint_release_jx"]
    assert positive["joint_authority_objects_created"] == 1
    assert positive["members"] == expected["approve_joint_release_jx"]["members"]
    assert positive["admission_status"] == expected["approve_joint_release_jx"]["admission_status"]
    assert all(positive["gate"][key] for key in ("J1", "J2", "J3", "J4", "J5", "J6"))


def test_action_contract_good_and_bad_attempts_match_oracle():
    result = run_result()["action_contract"]
    expected = load_inputs()[1]["expectations"]["action_contract"]
    assert result["activated_constraint_ids"] == expected["activated_constraint_ids"]
    for attempt in ("BL1-GOOD", "BL1-BAD"):
        assert result[attempt]["status"] == expected[attempt]["status"]
        assert result[attempt]["omitted"] == expected[attempt]["omitted"]
        assert result[attempt]["order_violations"] == expected[attempt]["order_violations"]


def test_incremental_refresh_is_dependency_local():
    result = run_result()["refresh_and_rebuild"]["incremental"]
    expected = load_inputs()[1]["expectations"]["refresh_and_rebuild"]["CHANGE-P2-CONTRACT"]
    assert result["incremental_source_scans"] == expected["incremental_source_scans"]
    assert result["refreshed_views"] == expected["refreshed_views"]
    assert result["authoritative_source_locations_touched"] == ["P2"]


def test_full_rebuild_scales_with_history_while_current_view_and_lookup_stay_bounded():
    result = run_result()["refresh_and_rebuild"]
    expected = load_inputs()[1]["expectations"]["refresh_and_rebuild"]
    assert result["current_view_digest_equal_across_scales"] is expected["current_view_digest_equal_across_scales"]
    digests = set()
    for scale, exp in expected["scales"].items():
        got = result["scales"][scale]
        assert got["full_rebuild_source_records"] == exp["full_rebuild_source_records"]
        assert got["identity_event_records"] == exp["identity_event_records"]
        assert got["normal_identity_lookup_steps"] == exp["normal_identity_lookup_steps"]
        assert got["identity_index_entries"] == 6
        digests.add(got["current_view_digest"])
    assert len(digests) == 1


def test_identity_current_targets_and_carriers_match_oracle():
    result = run_result()["identity"]
    expected = load_inputs()[1]["expectations"]
    assert result["current_targets"] == expected["identity_current_targets"]
    assert result["current_carriers"] == expected["identity_current_carriers"]
    assert result["normal_lookup_model"] == "precomputed_current_target_index"


def test_shadow_boundary_and_profile_surface_are_bounded():
    result = run_result()
    assert result["shadow_only"] is True
    assert result["implementation_reads_oracle"] is False
    assert result["profile_surface"] == [
        "GOVERNING_PROCEDURE",
        "JOINT_AUTHORITY_DECLARATION",
        "IDENTITY_TRANSITION",
        "DERIVED_VIEW_MANIFEST",
    ]
    assert result["metrics"]["implementation_profile_types"] == 4
    assert result["metrics"]["joint_authority_objects_created"] == 1
