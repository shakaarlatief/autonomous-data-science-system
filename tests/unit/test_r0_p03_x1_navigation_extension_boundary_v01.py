"""Reproducible contract tests for the explicitly unscored X1 interface pilot.

These tests do not qualify the future V02 kernel, operational authority,
source-owned metadata, full B0–B4 implementations, or Research 513 scoring.
"""
import json

import pytest

from experiments.r0_p03_navigation_probe import x1_navigation_extension_boundary_v01 as x1


def _effect_ids():
    j1, _, _ = x1.load_development_replays()
    return {e["accepted_effect_id"] for e in j1["effects"]}


def test_real_d1_d2_replay_inputs_and_results_are_exercised():
    report = x1.run()
    assert report["d1_effect_count"] == 4
    assert report["d2_case_count"] == 14
    assert report["d1_d2_results_unchanged"] is True
    assert report["research_513_formal_outcome"] is None
    assert report["physical_target_selected"] is False


def test_all_five_unscored_adapter_paths_rebuild_and_relocate():
    report = x1.run()
    assert set(report["arms"]) == {"B0", "B1", "B2", "B3", "B4"}
    for arm, observation in report["arms"].items():
        assert observation["rebuild_digest_preserved"] is True, arm
        assert observation["metadata_survives_path_rename"] is True, arm
        assert observation["ranking_ids"], arm
        assert set(observation["ranking_ids"]) <= set(x1.CARRIERS)


def test_authority_and_identity_negative_controls_rejected():
    rejected = x1.negative_controls(_effect_ids())
    assert set(rejected) == {
        "authority_field_injection", "path_as_identity", "invented_effect",
        "authority_class_promotion", "vector_path_as_identity",
    }


@pytest.mark.parametrize("arm,metadata", [
    ("B1", {"definitions": {"topic:a": "a"}, "assignments": {"carrier:decision": ["topic:unknown"]}}),
    ("B2", {"links": [{"source_id": "carrier:code", "target_id": "carrier:decision",
                       "effect_id": x1.EFFECT_ID, "source_line": 1,
                       "evidence": "ACCEPTED_J1"}]}),
    ("B4", {"vectors": {"carrier:decision": [1.0, float("nan"), 0.0]}}),
    ("FAKE", {}),
])
def test_invalid_extension_metadata_rejected(arm, metadata):
    with pytest.raises(ValueError):
        x1.derived_index(arm, metadata, x1.CARRIERS, _effect_ids())


def test_d2_real_replacement_does_not_silently_carry_link():
    _, _, cases = x1.load_development_replays()
    case = next(c for c in cases if c["fixture_id"] == "F08_REPLACE_DEFAULT_OPEN_RESET")
    evaluation = x1.d2_evaluate(case)
    predecessor = case["predecessors"][0]["effect_id"]
    assert evaluation["relation_valid"] is True
    assert predecessor not in evaluation["current_effect_ids"]
    assert x1.evidence_status_after_lineage(
        [{"effect_id": predecessor}], set(evaluation["current_effect_ids"])
    ) == "REVIEW_REQUIRED"


def test_determinism_and_original_experiment_inputs_are_unchanged():
    original = {
        f: f.read_bytes()
        for d in (x1.ROOT / "experiments/ao10_hybrid_d1_replay_v01",
                  x1.ROOT / "experiments/ao10_hybrid_d2_lineage_v01")
        for f in d.glob("*.json")
    }
    a, b = x1.run(), x1.run()
    assert a == b
    assert all(f.read_bytes() == value for f, value in original.items())


def test_receipt_is_exact_replay_result_without_rewrite():
    frozen = json.loads(x1.RESULT.read_text("utf8"))
    assert frozen == x1.run()
    assert frozen["status"] == "LIMITED_UNSCORED_INTERFACE_PILOT_NOT_X1_PASS"
    assert frozen["authored_metadata_rewritten_count"] == 0
    assert frozen["synthetic_growth_carriers_added"] == 10
