"""Source-verified G013 facts over identical common V03 preadmission semantics.

These tests validate evidence integration, not protected R0-P03 navigation gold,
not a new J2 source-owner acceptance, and not an S1 transition.
"""
from __future__ import annotations

from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_common_world_g013_overlay_v01 as p,
)


@pytest.fixture(scope="module")
def world():
    return p.build()


def test_common_world_has_same_nineteen_original_ads_sources(world):
    root = world["source_of_truth"]
    assert root["source_roles_and_revisions"]["distinct_original_git_paths"] == 19
    assert root["source_roles_and_revisions"]["source_pin"] == p.base.original.PIN
    assert root["root_common_world_sha256"] == p.BASE_SHA256


def test_actual_pka_accepted_effects_not_adapted_by_g013(world):
    effects = world["source_of_truth"]["accepted_j1"]["accepted_effects"]
    assert len(effects) == 4
    assert [x["id"] for x in effects] == list(p.owner.EXPECTED_IDS)


def test_single_semantic_identity_and_two_original_git_source_versions(world):
    src = world["source_of_truth"]
    assert src["identity"]["authored_id"] == p.refresh.transition.AUTHORED_ID
    assert src["source_versions"]["initial_git_commit"] == p.refresh.transition.INITIAL_COMMIT
    assert src["source_versions"]["replacement_git_commit"] == p.refresh.transition.REPLACEMENT_COMMIT


def test_g013_real_source_projection_changes_path_not_identity(world):
    rows = world["G013_executed_observations"]["source_identity_transition"]
    assert rows["before"]["semantic_id"] == rows["after"]["semantic_id"] == p.refresh.transition.AUTHORED_ID
    assert rows["before"]["content_digest"] == rows["after"]["content_digest"]
    assert rows["before"]["source_path"] == p.refresh.OLD
    assert rows["after"]["source_path"] == p.refresh.NEW
    assert rows["previous_carrier_absent_from_current_view"] is True


def test_g013_actual_rebuild_freshness_and_components_reconciled(world):
    facts = world["G013_executed_observations"]
    assert facts["view_id"] == p.refresh.VIEW
    assert facts["affected_view_ids"] == [p.refresh.VIEW]
    assert facts["incremental_full_build_equal"] is True
    assert facts["old_manifest_stale"] is True
    assert facts["current_manifest_fresh"] is True
    components = facts["component_evidence_without_J2_qualification"]
    assert [x["component"] for x in components] == [
        "EXPLICIT_IDENTITY_PRESERVING_MOVE", "AFFECTED_VIEW_REFRESH_SELECTED",
        "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD", "STALE_DERIVED_RESULT_NOT_GOVERNING"
    ]
    assert all(x["qualified_governing_j2"] is False for x in components)


def test_g010_fixture_remains_support_not_formal_p03_corpus(world):
    facts = world["G013_executed_observations"]
    assert facts["fixture_is_experiment_support_not_primary_navigation_corpus"] is True
    assert "SEPARATE_ISOLATED_G010_SUPPORT_ROOT" in facts["source_role"]


def test_acceptance_not_activation_and_no_j3_inference(world):
    q = world["qualification"]
    assert q["new_PKA_experiment_only_J1_accepted"] == 4
    assert q["S0_current"] is True
    assert q["S1_accepted_but_dormant"] is True
    assert q["S1_lineage_activated"] is False
    assert q["qualified_natural_owner_RELATIONAL_J2"] == 0
    assert q["J3_certified"] is False


def test_formal_method_frozen_scoring_not_started(world):
    q = world["qualification"]
    for key in (
        "all_19_original_ADS_sources_admitted_as_one_G013_root",
        "B0_B4_navigation_arms_frozen",
        "protected_primary_tasks_originated",
        "neutral_legacy_nine_rejudged_under_current_method",
        "formal_P03_comparison_scored", "physical_architecture_selected",
    ):
        assert q[key] is False


def test_duplicate_or_self_promoted_j2_not_emitted(world):
    assert world["source_of_truth"]["J2"]["qualified_relational_count"] == 0
    assert world["source_of_truth"]["J3"]["completion_certified"] is False
    assert "NATURAL_OWNER_COVERS" in world["next_critical_path"][0]


def test_receipts_are_exact_source_bound(world):
    assert sha256(p.base.OUTPUT.read_bytes()).hexdigest() == p.BASE_SHA256
    assert sha256(p.refresh.OUTPUT.read_bytes()).hexdigest() == p.REFRESH_SHA256
    assert json.loads(p.OUTPUT.read_text("utf8")) == world
