"""True production G013 refresh on real ADS source versions in isolated Git.

This test exercises the authentic production refresh API and full G009
generator. Only the *carrier* versions are original ADS Git objects; the
isolated execution root includes existing G010 test-fixture support and is
NOT the whole original ADS source world. No J2, S1, J3, architecture or scored
navigation facts follow automatically from the positive functional result.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_g013_isolated_source_refresh_v01 as p,
)


@pytest.fixture(scope="module")
def observed():
    return p.execute()


def test_production_g013_and_g009_executed_on_actual_snapshots(observed):
    assert observed["status"] == "ACTUAL_PRODUCTION_G013_REFRESH_ON_EXACT_REAL_SOURCE_PROJECTION_PASS"
    assert observed["execution"]["actual_production_G013_api_used"] is True
    assert observed["execution"]["actual_production_G009_full_generator_used"] is True
    assert observed["execution"]["previous_repository_admission"] == "PASS"
    assert observed["execution"]["current_repository_admission"] == "PASS"


def test_true_git_original_source_versions_not_historical_model_fiction(observed):
    source = observed["experimental_source"]
    assert source["original_git_before_commit"] == p.transition.INITIAL_COMMIT
    assert source["original_git_after_commit"] == p.transition.REPLACEMENT_COMMIT
    assert source["original_before_sha256"] == p.transition.INITIAL_SHA256
    assert source["original_after_sha256"] == p.transition.REPLACEMENT_SHA256
    assert source["original_exact_bytes_copied_to_isolated_root"] is True
    assert source["governed_source_field_values_unchanged_from_actual_carrier"] is True
    assert source["same_semantic_id"] == p.transition.AUTHORED_ID


def test_source_move_and_selected_binding_are_not_name_similarity(observed):
    e = observed["execution"]
    assert e["generated_view_id"] == p.VIEW
    assert e["G013_affected_view_ids"] == [p.VIEW]
    assert e["G013_reasons"] == [[p.VIEW, "DEPENDENCY_BINDING_CHANGED"]]
    assert e["G013_full_fallback"] is False


def test_actual_source_in_generated_views_has_same_id_and_new_path(observed):
    projection = observed["source_projection"]
    assert projection["before"]["semantic_id"] == projection["after"]["semantic_id"] == p.transition.AUTHORED_ID
    assert projection["before"]["source_path"] == p.OLD
    assert projection["after"]["source_path"] == p.NEW
    assert projection["before"]["content_digest"] == projection["after"]["content_digest"]
    assert projection["identity_unmodified_when_carrier_path_changes"] is True
    assert projection["previous_carrier_absent_from_current_view"] is True


def test_selected_incremental_is_byte_identical_to_full_current_build(observed):
    assert observed["execution"]["incremental_exactly_equals_full_build"] is True
    assert observed["execution"]["output_source_input_is_complete_current_snapshot"] is True
    assert observed["execution"]["old_view_bytes_differ_from_new"] is True
    assert observed["execution"]["old_view_sha256"] != observed["execution"]["current_view_sha256"]


def test_stale_old_manifest_and_fresh_current_manifest(observed):
    assert observed["execution"]["previous_manifest_currentness"] == "STALE"
    assert observed["execution"]["current_manifest_currentness"] == "FRESH"
    assert len(observed["execution"]["new_view_manifest_sha256"]) == 64


def test_g013_components_named_exactly_from_accepted_s1_not_from_guess(observed):
    facts = observed["component_observations_not_gov_j2"]
    assert [v["component"] for v in facts] == [
        "EXPLICIT_IDENTITY_PRESERVING_MOVE",
        "AFFECTED_VIEW_REFRESH_SELECTED",
        "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
        "STALE_DERIVED_RESULT_NOT_GOVERNING",
    ]
    assert all(v["accepted_effect"] == p.accepted_j1.EXPECTED_IDS[1] for v in facts)
    assert all(v["evidence_class"] == "OBSERVABLE_EXECUTED" for v in facts)
    assert all(v["qualified_governing_j2"] is False for v in facts)


def test_result_has_reproducible_sandbox_git_commit_identities(observed):
    a = observed["execution"]
    assert a["ephemeral_git_commit_before"] == "22ff8fdafdd0db4160eb1b4798cb4c6259ea4b82"
    assert a["ephemeral_git_commit_after"] == "df8423466976add577b128924a635bf1918ead0e"
    assert a["old_view_sha256"] == "67f52f6b20834550d5191e94d7582e8930f67bfb56cb4a8a0d6dd7fedf1c41f4"
    assert a["current_view_sha256"] == "b76999ded5f55ec552390e9a5a7286f7ca348ea4703a89ba7ab2a149b0df6404"


def test_underlying_generator_has_normal_production_closure():
    spec = p._specification()
    assert spec.view_id == p.VIEW
    assert spec.selector.profiles == (p.Profile.SEMANTIC_SOURCE,)
    assert spec.compute == "source_inventory.v1"
    assert spec.serialize == "canonical_json.v1"
    assert spec.generator.generator_id == "project_knowledge_source_inventory"
    assert set(p.TCB_FILES).issubset(set(spec.generator.implementation_files))


def test_supporting_g010_fixture_is_not_experiment_scoring_corpus(observed):
    a = observed["provenance"]
    assert a["supporting_fixture"] == "tests/fixtures/project_knowledge_g010/corpus.json"
    assert a["fixture_only_for_valid_production_execution_closure"] is True
    assert observed["execution"]["fixture_supporting_source_count"] == 8
    assert a["all_19_original_sources_executed_as_single_G013_CORPUS"] is False
    assert a["same_real_main_repository_full_validation_claimed"] is False
    assert a["temporary_sandbox_commits_not_original_ADS_Git_commits"] is True


def test_current_repository_digests_not_silently_cleared_by_sandbox(observed):
    assert observed["provenance"]["production_source_or_code_modified"] is False
    assert observed["authority"]["source_owner_relational_J2_qualified"] is False
    assert observed["authority"]["S1_accepted_transition_activated"] is False
    assert observed["authority"]["J3_satisfaction_certified"] is False
    assert observed["authority"]["formal_B0_B4_scoring_performed"] is False
    assert observed["authority"]["physical_architecture_selected"] is False


def test_repeatable_derived_receipt_matches_recomputed_source_and_g013(observed):
    assert json.loads(p.OUTPUT.read_text("utf8")) == observed
    assert sha256(p.OUTPUT.read_bytes()).hexdigest() == (
        "594eecaef1c770a3545ef2664dbe47df1c8fb74e069a7e2cd7f1a9cc230b50e2"
    )


def test_fabricated_initial_identity_is_refused_before_sandbox(monkeypatch):
    source = p.transition.committed_carriers
    def changed():
        old, current, info = source()
        old = deepcopy(old)
        old["governed_source"]["semantic_id"] = "FORGED.EXPERIMENT.ID"
        return old, current, info
    monkeypatch.setattr(p.transition, "committed_carriers", changed)
    with pytest.raises(RuntimeError, match="EXPERIMENT_SOURCE_SEMANTIC_ID_CHANGED"):
        p.execute()


def test_authority_cannot_be_promoted_by_fabricated_owner_reply(monkeypatch):
    actual = p.accepted_j1.build()
    fabricated = deepcopy(actual)
    fabricated["j2"]["qualified_count"] = 1
    monkeypatch.setattr(p.accepted_j1, "build", lambda: fabricated)
    with pytest.raises(RuntimeError, match="G013_EXPERIMENT_ACCEPTED_J1_OR_AUTHORITATIVE_STATUS_DRIFT"):
        p.execute()


def test_changed_s1_component_contract_cannot_be_silently_scored(monkeypatch):
    actual = p.accepted_j1.build()
    fabricated = deepcopy(actual)
    fabricated["accepted_j1"]["effects"][1]["completion_contract"]["required_components"][1] = "FABRICATED_COMPONENT"
    monkeypatch.setattr(p.accepted_j1, "build", lambda: fabricated)
    with pytest.raises(RuntimeError, match="G013_EXACT_ACCEPTED_S1_COMPONENTS_CHANGED"):
        p.execute()
