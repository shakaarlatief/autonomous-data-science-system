from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "scripts" / "research" / "project_knowledge_architecture_probe_v02.py"
SPEC = importlib.util.spec_from_file_location("project_knowledge_architecture_probe_v02", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def fixture() -> dict:
    data, digest = MODULE.load_fixture()
    assert digest == MODULE.EXPECTED_FIXTURE_SHA256
    return data


def test_frozen_fixture_hash_and_identity() -> None:
    data, digest = MODULE.load_fixture()
    assert data["fixture_id"] == "PKA-RL-V02"
    assert digest == "ece094762e3fe4f064640004da3f2293aa39168268af183df6f1347ba7f4b4c0"


def test_both_candidates_pass_same_frozen_relation_lifecycle_oracles() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        result = MODULE.run_candidate(cls, data)
        assert result["all_semantic_checks_pass"] is True


def test_h1_uses_deterministic_but_arbitrary_endpoint_ownership() -> None:
    probe = MODULE.H1Probe(fixture())
    probe.run_lifecycle()
    observation = probe.owner_observation()
    assert observation["arbitrary_endpoint_owner_count"] == 2
    assert observation["dedicated_relation_authority_locations"] == 0
    assert observation["independent_relation_authority_location_count"] == 1
    assert observation["independent_relations"]["R-ABC-1"]["owner"] == "sidecar:S-A:relations"
    assert observation["source_sidecar_write_revisions"]["S-A"] == 5
    assert observation["independent_relations"]["R-ABC-1"]["semantically_natural"] is False


def test_h2_admits_only_first_class_relations() -> None:
    probe = MODULE.H2Probe(fixture())
    probe.run_lifecycle()
    admission = probe.h2_admission_observation()
    assert admission["admitted_relation_ids"] == ["R-ABC-1", "R-ABC-2"]
    assert admission["nonqualifying_control_in_spine"] is False
    assert admission["false_positive_admissions"] == 0
    assert admission["false_negative_admissions"] == 0


def test_relation_only_changes_do_not_change_endpoint_semantics() -> None:
    data = fixture()
    h1 = MODULE.H1Probe(data)
    h2 = MODULE.H2Probe(data)
    h1.run_lifecycle()
    h2.run_lifecycle()
    expected = data["expected_final"]["endpoint_semantic_revisions"]
    assert h1.endpoint_semantic_revisions() == expected
    assert h2.endpoint_semantic_revisions() == expected
    assert h1.endpoint_container_write_revisions() == {"S-A": 1, "S-B": 1, "S-C": 1, "S-D": 1}
    assert h1.owner_observation()["source_sidecar_write_revisions"]["S-A"] == 5
    assert h2.endpoint_container_write_revisions() == {"S-A": 1, "S-B": 1, "S-C": 1, "S-D": 1}


def test_stale_relation_update_is_rejected_without_mutation() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        transitions = data["independent_relation"]["transitions"]
        for transition in transitions[:3]:
            probe.apply_transition(transition)
        before = copy.deepcopy(probe._get_relation("R-ABC-1"))
        result = probe.apply_transition(transitions[3])
        after = probe._get_relation("R-ABC-1")
        assert result["error"] == "STALE_RELATION_REVISION"
        assert result["authoritative_mutation"] is False
        assert after == before


def test_missing_relation_evidence_fails_visible() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        probe.run_lifecycle()
        result = probe.missing_evidence_challenge()
        assert result["status"] == "unresolved_missing_relation_evidence"
        assert result["missing_evidence_ids"] == ["E3"]


def test_minimal_h2_spine_does_not_absorb_scaled_ordinary_relations() -> None:
    data = fixture()
    probe = MODULE.H2Probe(data)
    probe.run_lifecycle()
    observations = [probe.scale_observation(count) for count in (10, 50, 100)]
    assert [item["relation_spine_records"] for item in observations] == [2, 2, 2]
    assert [item["false_positive_spine_admissions"] for item in observations] == [0, 0, 0]
    assert [item["source_local_relation_count"] for item in observations] == [11, 51, 101]


def test_derived_relation_views_rebuild_with_freshness_binding() -> None:
    data = fixture()
    for cls in (MODULE.H1Probe, MODULE.H2Probe):
        probe = cls(data)
        probe.run_lifecycle()
        digest = probe.source_digest()
        probe.build_views()
        payloads = {key: value["payload"] for key, value in probe.derived.items()}
        probe.delete_views()
        try:
            probe.require_view("current_relation_view")
        except MODULE.ProbeError as exc:
            assert str(exc) == "DERIVED_VIEW_UNAVAILABLE:current_relation_view"
        else:
            raise AssertionError("missing derived relation view did not fail visibly")
        probe.build_views()
        assert {key: value["payload"] for key, value in probe.derived.items()} == payloads
        assert all(value["source_digest"] == digest for value in probe.derived.values())


def test_physical_touch_accounting_does_not_hide_h2_supersession_fanout() -> None:
    data = fixture()
    h1 = MODULE.run_candidate(MODULE.H1Probe, data)
    h2 = MODULE.run_candidate(MODULE.H2Probe, data)
    assert h1["representation"]["authoritative_location_touch_total"] == 4
    assert h2["representation"]["authoritative_location_touch_total"] == 5
    assert h1["representation"]["owner_observation"]["independent_relation_authority_location_count"] == 1
    assert h2["representation"]["owner_observation"]["independent_relation_authority_location_count"] == 2


def test_full_probe_has_no_winner_score_or_target_selection() -> None:
    result = MODULE.run(None)
    comparison = result["comparison"]
    assert comparison["semantic_correctness"] == {"H1": True, "H2": True}
    assert "winner" not in comparison
    assert "score" not in comparison
    assert "No aggregate score" in comparison["interpretation_guard"]
