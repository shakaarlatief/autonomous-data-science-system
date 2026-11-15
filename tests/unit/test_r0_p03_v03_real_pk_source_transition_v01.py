"""Actual Git-backed experimental carrier move through the production G006 engine.

The source role is OBSERVABLE exact Git plus a source-authored experiment-local
representation relation. No test asserts that Git proves natural-owner J2,
that the S1 REQUIRE is activated, or that B0-B4 scored navigation has run.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_source_transition_v01 as probe,
)


@pytest.fixture(scope="module")
def observation():
    return probe.build()


@pytest.fixture(scope="module")
def originals():
    return probe.committed_carriers()


def test_real_history_exact_parent_and_only_source_paths(observation):
    g = observation["git"]
    assert g["initial_commit"] == probe.INITIAL_COMMIT
    assert g["replacement_commit"] == probe.REPLACEMENT_COMMIT
    assert g["initial_parent"] == probe.INITIAL_PARENT
    assert g["git_changed_paths"] == sorted([probe.INITIAL_PATH, probe.REPLACEMENT_PATH])
    assert g["both_exact_source_revisions_verified"] is True


def test_original_git_blob_recoverable_after_old_carrier_removed(originals):
    initial, current, meta = originals
    assert sha256(probe.git("show", f"{probe.INITIAL_COMMIT}:{probe.INITIAL_PATH}")).hexdigest() == probe.INITIAL_SHA256
    assert sha256(probe.git("show", f"{probe.REPLACEMENT_COMMIT}:{probe.REPLACEMENT_PATH}")).hexdigest() == probe.REPLACEMENT_SHA256
    assert initial["lifecycle_stage"] == "S0_PREMOVE_ACTUAL_GIT_SOURCE_BASELINE"
    assert current["lifecycle_stage"] == "S0_EXPERIMENTAL_CARRIER_REPRESENTATION_REPLACEMENT_NOT_S1_ACTIVATION"


def test_same_explicit_semantic_id_despite_different_git_paths_and_content(originals):
    a, b, _ = originals
    assert a["governed_source"]["semantic_id"] == b["governed_source"]["semantic_id"] == probe.AUTHORED_ID
    assert probe.INITIAL_PATH != probe.REPLACEMENT_PATH
    assert probe.INITIAL_SHA256 != probe.REPLACEMENT_SHA256
    assert a["governed_source"]["authority_class"] == b["governed_source"]["authority_class"] == "canonical"


def test_original_pka_g006_real_git_source_witness_retained(originals):
    a, b, _ = originals
    assert a["real_ads_source"] == b["real_ads_source"]
    assert a["real_ads_source"]["original_sha256"] == (
        "c267136871d0349c5920edc47cae88fed07b097902f154d689b25d06d9d481df"
    )


def test_g013_expansion_is_source_grounded_not_attested_j2(originals):
    _, current, _ = originals
    witnesses = current["expanded_real_ads_source_witnesses"]
    assert len(witnesses) == 5
    assert {w["witness_id"] for w in witnesses} == {
        "G013_REFRESH_IMPLEMENTATION", "G013_VIEW_IMPLEMENTATION",
        "G013_EQUIVALENCE_TEST", "G013_CROSS_SEMANTIC_TEST",
        "G013_DECISION_RECORD",
    }
    assert all(w["qualified_fact"] == (
        "ORIGINAL_GIT_SOURCE_TEXT_EXISTS_NOT_A_NEW_J2_RELATIONAL_DECLARATION"
    ) for w in witnesses)
    assert current["revision_provenance"]["natural_owner_j2_coverage"] == "UNQUALIFIED"


def test_source_carrier_explicitly_declares_predecessor_successor_and_identity(originals):
    _, current, _ = originals
    p = current["revision_provenance"]
    assert p["previous_source_path"] == probe.INITIAL_PATH
    assert p["current_source_path"] == probe.REPLACEMENT_PATH
    assert p["semantic_id_invariant"] == probe.AUTHORED_ID
    assert p["prior_git_commit"] == probe.INITIAL_COMMIT
    assert p["git_successor_commit"] == "UNAVAILABLE_UNTIL_COMMIT"
    assert p["successor_j1_activation"] == "NOT_ACTIVATED"


def test_real_production_identity_engine_recovers_current_identity(observation):
    result = observation["actual_g006_replay"]
    assert result["identity_current_targets"] == [probe.AUTHORED_ID]
    assert result["current_source_path"] == probe.REPLACEMENT_PATH
    assert result["continuity_preserved"] is True
    assert result["order_independent_serialization"] is True


def test_real_production_identity_engine_recovers_both_historical_carriers(observation):
    result = observation["actual_g006_replay"]
    assert result["history_known"] is True
    assert result["historical_carrier_paths"] == sorted([probe.INITIAL_PATH, probe.REPLACEMENT_PATH])


def test_source_transformation_uses_historical_projected_role_only(originals):
    original, current, _ = originals
    old = probe._source(original, path=probe.INITIAL_PATH,
                        commit=probe.INITIAL_COMMIT, digest=probe.INITIAL_SHA256,
                        historical=True)
    new = probe._source(current, path=probe.REPLACEMENT_PATH,
                        commit=probe.REPLACEMENT_COMMIT, digest=probe.REPLACEMENT_SHA256,
                        historical=False)
    assert old.authority_class.value == "historical"
    assert new.authority_class.value == "canonical"
    assert old.revision.source_commit == probe.INITIAL_COMMIT
    assert new.revision.source_commit == probe.REPLACEMENT_COMMIT
    assert old.semantic_id == new.semantic_id


def test_transition_uses_source_local_claim_not_git_filename_inference(originals):
    _, current, _ = originals
    t = probe._transition(current)
    assert t.transition_class.value == "REPRESENTATION_REPLACEMENT"
    assert tuple(s.value for s in t.predecessors) == (probe.AUTHORED_ID,)
    assert tuple(s.value for s in t.successors) == (probe.AUTHORED_ID,)
    assert t.provenance == (probe.INITIAL_PATH, probe.REPLACEMENT_PATH)


def test_missing_explicit_source_claim_rejected_even_with_real_move(originals):
    _, current, _ = originals
    altered = deepcopy(current)
    altered["revision_provenance"]["semantic_id_invariant"] = "FORGED"
    with pytest.raises(ValueError, match="SOURCE_CARRIER_DOES_NOT_DECLARE"):
        probe._transition(altered)


def test_wrong_source_path_rejected_by_explicit_transition_contract(originals):
    _, current, _ = originals
    altered = deepcopy(current)
    altered["revision_provenance"]["current_source_path"] = probe.INITIAL_PATH
    with pytest.raises(ValueError, match="SOURCE_CARRIER_DOES_NOT_DECLARE"):
        probe._transition(altered)


def test_not_even_actual_git_commit_proves_model_writer_identity(observation):
    owner = observation["owner_relation"]
    assert owner["at_action_author_claim_exposed"] is True
    assert owner["author_claim_independently_verified"] is False
    assert owner["g006_historical_implementation_owner_covers_authenticated"] is False
    assert owner["qualified_relational_j2_count"] == 0


def test_acceptance_does_not_automatically_activate_s1_or_certify_j3(observation):
    assert observation["accepted_j1"]["effect_count"] == 4
    assert observation["accepted_j1"]["active_effect_ids"] == list(probe.accepted.EXPECTED_ACTIVE)
    assert observation["accepted_j1"]["successor_effect_dormant"] == probe.accepted.EXPECTED_IDS[1]
    assert observation["j3"]["S1"] == "NOT_ACTIVATED"
    assert observation["j3"]["completion_certified"] is False
    assert observation["j3"]["source_revision_observed_but_not_qualified_j1_activation"] is True


def test_absent_original_blob_cannot_generate_positive_world(monkeypatch):
    raw = probe.git
    def broken(*args):
        if args[0] == "show" and args[1] == f"{probe.INITIAL_COMMIT}:{probe.INITIAL_PATH}":
            return b"fabricated"
        return raw(*args)
    monkeypatch.setattr(probe, "git", broken)
    with pytest.raises(ValueError, match="P03_REAL_SOURCE_BYTE_EVIDENCE_CHANGED"):
        probe.committed_carriers()


def test_stale_worktree_current_carrier_not_mistaken_for_git_original(monkeypatch):
    from pathlib import Path
    target = probe.BASE / "real_pk_world/current/identity_carrier_v01.json"
    original_exists = Path.exists
    original_read_bytes = Path.read_bytes

    def with_stale_carrier_present(self):
        return True if self == target else original_exists(self)

    def with_stale_carrier_bytes(self):
        return b"changed or stale" if self == target else original_read_bytes(self)

    monkeypatch.setattr(Path, "exists", with_stale_carrier_present)
    monkeypatch.setattr(Path, "read_bytes", with_stale_carrier_bytes)
    with pytest.raises(ValueError, match="P03_CURRENT_CARRIER_WORKTREE_DRIFT"):
        probe.committed_carriers()


def test_historical_git_replay_survives_subsequent_carrier_removal(originals):
    historical_path = probe.BASE / "real_pk_world/current/identity_carrier_v01.json"
    assert not historical_path.exists()
    _, earlier_current, git_facts = originals
    assert earlier_current["governed_source"]["semantic_id"] == probe.AUTHORED_ID
    assert git_facts["replacement_commit"] == probe.REPLACEMENT_COMMIT


def test_wrong_source_parent_fails_before_semantic_success(monkeypatch):
    raw = probe.git
    def broken(*args):
        if args[:3] == ("show", "-s", "--format=%P") and args[3] == probe.REPLACEMENT_COMMIT:
            return b"not-the-parent\n"
        return raw(*args)
    monkeypatch.setattr(probe, "git", broken)
    with pytest.raises(ValueError, match="P03_REAL_SOURCE_PARENT_DRIFT"):
        probe.committed_carriers()


def test_derived_receipt_immutable_when_source_replay_matches(observation):
    assert json.loads(probe.OUTPUT.read_text("utf8")) == observation


def test_world_has_no_formal_navigation_result_or_physical_preselection(observation):
    assert observation["formal_primary_tasks"] is None
    assert observation["formal_b0_b4_scores"] is None
    assert observation["physical_architecture_selected"] is False
    assert observation["production_code_changed"] is False
