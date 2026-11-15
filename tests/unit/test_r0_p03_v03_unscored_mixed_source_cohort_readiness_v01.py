"""Negative and parity checks for the unscored P03 mixed-role corpus probe.

This suite can verify source existence, blob hashes, documented role *hints*,
literal lexical access and a common interface contract. It intentionally does
not qualify a 60/20 source sample, score B0-B4, create hidden gold or infer J1
authority from source paths, test code or generated/current views.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_r0_p03_unscored_mixed_source_cohort_readiness_v01 as candidate,
)


@pytest.fixture(scope="module")
def result():
    return candidate.build()


@pytest.fixture(scope="module")
def seed():
    return candidate.load_seed()


@pytest.fixture(scope="module")
def witnesses(seed):
    return candidate.witness_records(seed)


@pytest.fixture(scope="module")
def core(witnesses):
    return candidate.common_projection(witnesses, candidate.source_relative_semantics())


def test_exact_pinned_mixed_role_counts_not_qualified_eligibility(result):
    frame = result["candidate_evidence"]
    assert result["source_git_revision"] == candidate.REF
    assert frame["markdown_path_count_not_semantically_eligible"] == 1586
    assert frame["multi_modality_reviewable_text_paths_not_semantically_eligible"] == 2897
    assert frame["tracked_paths_in_role_census"] == 4090
    assert frame["role_seed_path_count"] == 24
    assert frame["eligible_formal_carrier_count_established"] == 0
    assert frame["every_role_eligibility"] == "UNREVIEWED_CANDIDATE"


def test_sample_still_has_no_build_or_heldout_members(result):
    split = result["proposed_formal_sampling"]
    assert split["target_build"] == 60
    assert split["target_heldout"] == 20
    assert split["eligibility_adjudicated"] is False
    assert split["sampling_selected"] is False
    assert split["heldout_paths_salt_or_keys_published"] is False
    assert split["historical_65_source_legacy_world_independent"] is True
    assert result["formal_r0_p03"] == "INCOMPLETE"


def test_seed_is_not_an_accepted_authority_or_scored_source(seed):
    assert len(seed["sources"]) == 24
    assert all(x["eligibility"] == "UNREVIEWED_SOURCE_ROLE_CANDIDATE" for x in seed["sources"])
    assert all(x["role_is_not_accepted_authority"] is True for x in seed["sources"])
    assert not any(x["path"].startswith("experiments/r0_p03_") for x in seed["sources"])
    assert any("TASK_OR_GOLD" in x for x in seed["prohibited"])
    assert any("HELDOUT" in x for x in seed["prohibited"])


def test_source_records_are_exact_git_blobs_not_current_filename_guesses(witnesses):
    roster = candidate.source_roster()
    assert len(witnesses) == 24
    assert len({x["source_path"] for x in witnesses}) == 24
    for source in witnesses:
        body = candidate.git_blob(source["source_path"], roster[source["source_path"]])
        assert sha256(body).hexdigest() == source["source_sha256"]
        assert source["git_blob_oid"] == roster[source["source_path"]]
        assert source["source_ref"] == candidate.REF
        assert source["witness_line"] == 1
        assert sha256(body.decode("utf8").splitlines()[0].encode("utf8")).hexdigest() == source["witness_line_sha256"]
        assert source["governing_authority_or_semantic_relevance_verified"] is False


@pytest.mark.parametrize("path", [
    "tools/project_knowledge/identity.py",
    "tools/project_knowledge/services/refresh.py",
    "src/ads_system/application/source_universe.py",
    "src/ads_system/infrastructure/retrieval/sqlite_fts.py",
    "frontend/src/components/CockpitProjectMap.tsx",
    "schemas/project_knowledge/semantic_source.v1.schema.json",
    "tests/unit/test_project_knowledge_refresh.py",
    ".github/workflows/repository-integrity.yml",
])
def test_cross_plane_code_and_test_sources_not_absent_from_seed(witnesses, path):
    source = next(w for w in witnesses if w["source_path"] == path)
    assert source["byte_count"] > 0
    assert source["role_hypothesis"] != "CURRENT_DECISION_CONTEXT"


def test_24_seed_is_not_markdown_only(witnesses):
    assert any(x["source_path"].endswith(".tsx") for x in witnesses)
    assert any(x["source_path"].endswith(".py") for x in witnesses)
    assert any(x["source_path"].endswith(".json") for x in witnesses)
    assert any(x["source_path"].endswith(".yml") for x in witnesses)
    assert any(x["source_path"].endswith(".md") for x in witnesses)


def test_b0_b4_share_exact_common_substrate_bytes(core, result):
    outputs = [candidate.project_arm_common(arm, core) for arm in candidate.ARMS]
    assert len(set(outputs)) == 1
    assert len({sha256(b).hexdigest() for b in outputs}) == 1
    assert result["arm_neutral_interface_probe"]["common_core_sha256"] == sha256(outputs[0]).hexdigest()
    assert result["arm_neutral_interface_probe"]["arm_runtimes_implemented"] is False
    assert result["arm_neutral_interface_probe"]["b1_b2_b3_b4_additions_implemented"] is False
    assert result["arm_neutral_interface_probe"]["common_core_runtime_parity_qualified"] is False


@pytest.mark.parametrize("arm,extension", [
    ("B1", {"research217_topical_memberships": []}),
    ("B2", {"extra_editorial_about_links": []}),
    ("B3", {"prospective_governed_navigation_concerns": []}),
    ("B4", {"semantic_similarity_rankings": []}),
])
def test_allowlisted_potential_arm_additions_cannot_change_core(core, arm, extension):
    assert candidate.project_arm_common(arm, core, extension) == candidate.project_arm_common("B0", core)


@pytest.mark.parametrize("arm,extension", [
    ("B0", {"extra_editorial_about_links": []}),
    ("B1", {"experimental_semantics": {"j3": "FULL"}}),
    ("B2", {"source_witnesses": []}),
    ("B3", {"derived_orientation": {"governing": True}}),
    ("B4", {"accepted_effects": ["FAKE"]}),
])
def test_injected_authority_or_core_overrides_rejected(core, arm, extension):
    with pytest.raises(ValueError, match="COMMON_AUTHORITY|ZERO_ADDITIONS"):
        candidate.project_arm_common(arm, core, extension)


def test_unknown_arm_or_extra_common_core_key_rejected(core):
    with pytest.raises(ValueError, match="CORE_SCHEMA_OR_NAME"):
        candidate.project_arm_common("B9", core)
    mutated = deepcopy(core)
    mutated["hidden_gold"] = ["leak"]
    with pytest.raises(ValueError, match="CORE_SCHEMA_OR_NAME"):
        candidate.project_arm_common("B0", mutated)


def test_source_relative_j1_j2_j3_are_shared_but_only_experimental(core):
    s = core["experimental_semantics"]
    assert s["qualifying_j2_count"] == 1
    assert s["current_effects"] == [candidate.j3.E02, candidate.j3.E04]
    assert s["inherited_component_credit"] == 0
    assert s["j3_status"] == candidate.j3.J3_PASS
    assert s["production_j2_j3_qualified"] is False
    assert s["independent_model_actor_authentication"] is False
    assert s["nonsemantic_source_carriers_not_inferred_as_j1_j2"] is True
    assert len(s["accepted_j1_effects"]) == 4


def test_core_has_no_navigation_arm_advantage_or_hidden_gold(core):
    assert set(core) == candidate.CORE_FIELDS
    assert set(core["shared_capabilities"]) == set(candidate.EXPECTED_SHARED)
    assert set(core).isdisjoint(candidate.NONCOMMON)
    assert core["derived_orientation"]["status"] == "EXPERIMENT_ONLY_DERIVED_NON_GOVERNING"
    assert core["authority_boundary"]["not_a_formal_scored_or_gold_packet"] is True
    assert core["lexical_adapter"]["same_callable_for_all_arms"] is True


def test_literal_lexical_access_returns_exact_source_line_location(witnesses):
    hits = candidate.exact_lexical_hits("continuity", witnesses, max_hits=8)
    assert 0 < len(hits) <= 8
    assert hits == candidate.exact_lexical_hits("CONTINUITY", witnesses, max_hits=8)
    for hit in hits:
        assert hit["source_ref"] == candidate.REF
        assert hit["match_class"] == "LITERAL_CASEFOLD_UNRANKED_NOT_AUTHORITY"
        assert hit["line"] >= 1
        oid = candidate.source_roster()[hit["source_path"]]
        line = candidate.git_blob(hit["source_path"], oid).decode("utf8").splitlines()[hit["line"]-1]
        assert "continuity" in line.casefold()
        assert sha256(line.encode("utf8")).hexdigest() == hit["line_sha256"]


@pytest.mark.parametrize("query,max_hits", [
    ("", 5), (" ", 5), ("a"*81, 5), ("identity", 0),
    ("identity", 101), ("identity", True),
])
def test_invalid_lexical_query_or_budget_rejected(witnesses, query, max_hits):
    with pytest.raises(ValueError, match="LEXICAL_QUERY_CONTRACT"):
        candidate.exact_lexical_hits(query, witnesses, max_hits=max_hits)


def test_lexical_source_hash_tampering_rejected(witnesses):
    changed = deepcopy(witnesses)
    changed[0]["source_sha256"] = "0"*64
    with pytest.raises(ValueError, match="LEXICAL_SOURCE_HASH_CONFLICT"):
        candidate.exact_lexical_hits("continuity", [changed[0]])


def test_git_oid_tampering_rejected(witnesses):
    source = witnesses[0]
    with pytest.raises(ValueError, match="SOURCE_BLOB_IDENTITY_CONFLICT"):
        candidate.git_blob(source["source_path"], "0"*40)


def test_unsupported_source_missing_from_git_rejected():
    with pytest.raises(ValueError, match="PINNED_GIT_SOURCE_NOT_AVAILABLE"):
        candidate.git_blob("docs/not-real-source.md", "0"*40)


def test_seed_file_bytes_are_frozen_and_source_only(monkeypatch):
    # Use an existing repository-local artifact as invalid input; no
    # out-of-workspace temp location or file mutation is needed.
    monkeypatch.setattr(candidate, "SEED", candidate.OUTPUT)
    with pytest.raises(ValueError, match="COORDINATOR_SEED_MUTATED"):
        candidate.load_seed()


def test_candidate_report_is_immutable_replay(result):
    assert json.loads(candidate.OUTPUT.read_text("utf8")) == result
