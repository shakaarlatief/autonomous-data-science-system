from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "scripts" / "research" / "project_knowledge_architecture_probe_v01.py"
SPEC = importlib.util.spec_from_file_location("project_knowledge_architecture_probe_v01", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def fixture() -> dict:
    data, digest = MODULE.load_fixture()
    assert digest == MODULE.EXPECTED_FIXTURE_SHA256
    return data


def test_frozen_fixture_hash_and_id() -> None:
    data, digest = MODULE.load_fixture()
    assert digest == "c8ed1873014b7a69016eb6fb259791d1c34b9cd14219547f1ebc0e755b836fe8"
    assert data["fixture_id"] == "PKA-CF-V01"


def test_h1_and_h2_pass_same_semantic_fixture() -> None:
    data = fixture()
    h1 = MODULE.run_candidate(MODULE.H1Probe, data)
    h2 = MODULE.run_candidate(MODULE.H2Probe, data)
    assert h1["all_semantic_checks_pass"] is True
    assert h2["all_semantic_checks_pass"] is True


def test_semantic_inventory_is_identical_but_ownership_differs() -> None:
    data = fixture()
    h1 = MODULE.run_candidate(MODULE.H1Probe, data)
    h2 = MODULE.run_candidate(MODULE.H2Probe, data)
    expected = MODULE.expected_semantic_fact_ids(data)
    assert set(h1["representation"]["semantic_ownership"]) == expected
    assert set(h2["representation"]["semantic_ownership"]) == expected
    assert h1["representation"]["semantic_fact_ownership_count"] == {
        "source_local": 30,
        "spine": 0,
        "derived_only": 2,
    }
    assert h2["representation"]["semantic_fact_ownership_count"] == {
        "source_local": 5,
        "spine": 27,
        "derived_only": 0,
    }
    assert h1["representation"]["duplicate_authoritative_fact_owners"] == {}
    assert h2["representation"]["duplicate_authoritative_fact_owners"] == {}


def test_missing_cross_source_authority_relation_fails_visible_in_both() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        result = probe.challenge_missing_authority_relation()
        assert result["governing_sources"] == []
        assert result["status"] in {"ambiguous", "unresolved"}


def test_h2_spine_stays_constant_when_only_history_grows() -> None:
    data = fixture()
    h2 = MODULE.H2Probe(data)
    h2.run_identity_transitions()
    observations = [h2.scale_observation(count) for count in (20, 100, 200)]
    assert [item["spine_records"] for item in observations] == [7, 7, 7]
    assert len({item["active_view_bytes"] for item in observations}) == 1
    assert len({item["active_count"] for item in observations}) == 1


def test_h1_needs_no_separate_spine_for_fixture_v01() -> None:
    data = fixture()
    h1 = MODULE.H1Probe(data)
    h1.run_identity_transitions()
    h1.run_capture_lifecycle()
    assert h1.spine_record_count() == 0
    ownership = h1.semantic_ownership()
    assert not any(owner.startswith("spine:") for owners in ownership.values() for owner in owners)


def test_derived_views_are_rebuildable_and_freshness_bound() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        probe.run_identity_transitions()
        before_digest = probe.source_digest()
        probe.build_views()
        payloads = {name: value["payload"] for name, value in probe.derived.items()}
        probe.delete_derived()
        try:
            probe.require_view("authority_closure")
        except MODULE.ProbeError as exc:
            assert str(exc) == "DERIVED_VIEW_UNAVAILABLE:authority_closure"
        else:
            raise AssertionError("missing derived view did not fail visibly")
        probe.build_views()
        assert {name: value["payload"] for name, value in probe.derived.items()} == payloads
        assert all(value["source_digest"] == before_digest for value in probe.derived.values())


def test_contract_fidelity_detects_missing_and_contradictory_constraints() -> None:
    data = fixture()
    expected_order = data["F7_contract"]["expected"]["after_2026-04-01_order"]
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        assert probe.bind_contract("2026-04-15")["constraint_order"] == expected_order
        assert probe.challenge_missing_constraint().startswith("MISSING_REQUIRED_CONSTRAINT:C04")
        assert probe.challenge_contradictory_constraint().startswith("CONTRACT_CONFLICT:")


def test_full_probe_has_no_aggregate_winner_score() -> None:
    result = MODULE.run(None)
    comparison = result["comparison"]
    assert comparison["semantic_correctness"] == {"H1": True, "H2": True}
    assert "winner" not in comparison
    assert "score" not in comparison
    assert "No aggregate winner score" in comparison["interpretation_guard"]
