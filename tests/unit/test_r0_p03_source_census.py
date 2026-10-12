"""Non-scored verification of the R0-P03 candidate source-frame census.

These tests check Git provenance, source-pool partition properties, quota
feasibility and that no actual held-out sample or answer keys are emitted.
They are not navigation quality tests, semantic authority oracles, or evidence
that the proposed corpus has been independently approved.
"""

import importlib.util
import re
from pathlib import Path

import pytest


REPO = Path(__file__).resolve().parents[2]
MODULE = REPO / "experiments/r0_p03_navigation_probe/source_census.py"
SOURCE_REF = "22a63604e382f73b7fe661937ed4852ecf7da672"

_spec = importlib.util.spec_from_file_location("r0_p03_source_census", MODULE)
assert _spec is not None and _spec.loader is not None
census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(census)


@pytest.fixture(scope="module")
def result():
    return census.build_census(REPO, SOURCE_REF)


def test_source_ref_must_be_explicit_full_revision():
    with pytest.raises(ValueError):
        census.committed_markdown_sources(REPO, "HEAD")
    with pytest.raises(ValueError):
        census.committed_markdown_sources(REPO, "../untrusted")


def test_frozen_ref_and_deterministic_reconstruction(result):
    assert result["source_ref"] == SOURCE_REF
    assert result == census.build_census(REPO, SOURCE_REF)


def test_candidate_pool_quota_feasibility(result):
    assert result["classification"] == "UNFROZEN_SOURCE_FRAME_FEASIBILITY_ONLY"
    assert result["sample_plan"]["total"] == 80
    assert result["sample_plan"]["build"] == 60
    assert result["sample_plan"]["heldout"] == 20
    assert len(result["strata"]) == 10
    for stratum in result["strata"]:
        assert stratum["candidate_source_count"] >= 8
        assert stratum["target_build"] == 6
        assert stratum["target_heldout"] == 2


def test_source_strata_are_disjoint_and_git_bound(result):
    sources = census.committed_markdown_sources(REPO, SOURCE_REF)
    member_sets = [
        {path for path in sources if census.belongs_to_stratum(name, path)}
        for name in census.STRATUM_ORDER
    ]
    union = set()
    for member_set in member_sets:
        assert not (union & member_set)
        union |= member_set
    assert result["source_pool_size_unique_paths"] == len(union)
    assert all(
        re.fullmatch(r"[0-9a-f]{64}", record["candidate_pool_digest_sha256"])
        for record in result["strata"]
    )


def test_prospective_build_anchors_exist_in_correct_strata(result):
    sources = census.committed_markdown_sources(REPO, SOURCE_REF)
    for record in result["strata"]:
        assert 1 <= len(record["prospective_build_anchors"]) <= 6
        assert len(set(record["prospective_build_anchors"])) == len(record["prospective_build_anchors"])
        for path in record["prospective_build_anchors"]:
            assert path in sources
            assert census.belongs_to_stratum(record["name"], path)


def test_no_split_seeds_heldout_identities_or_gold_answers_exported(result):
    assert "heldout_paths" not in result
    assert "selection_seed" not in result
    assert "gold_answers" not in result
    assert "scoring" not in result
    assert "scenario_questions" not in result
    for record in result["strata"]:
        assert "selected_build" not in record
        assert "selected_heldout" not in record
        assert "members" not in record


def test_historical_subject_baseline_is_build_candidate_not_auto_winner(result):
    prior = next(s for s in result["strata"] if s["name"] == "semantic_prior_research")
    assert any("/217_" in x for x in prior["prospective_build_anchors"])
    assert "winner" not in result


def test_no_wildcard_or_untracked_path_is_implicitly_selected():
    assert not census.belongs_to_stratum("current_orientation", "docs/generated/CURRENT_STATE.md")
    assert not census.belongs_to_stratum("historical_checkpoints", "docs/checkpoints/foo.md")
    assert not census.belongs_to_stratum("semantic_prior_research", "docs/research/900_unknown.md")


def test_shared_contract_has_provenance_and_unknown_status_visibility():
    import json

    contract_path = REPO / "experiments/r0_p03_navigation_probe/common_substrate_contract_candidate.json"
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    assert contract["state"] == "UNFROZEN_NONEXECUTING"
    assert contract["source_ref"] == SOURCE_REF
    required = set(contract["exact_record_contract"]["carrier"]["required"])
    assert {"source_path", "git_commit", "git_blob_oid", "authority_currentness_basis"} <= required
    shared = set(contract["shared_capabilities"]["all_arms"])
    assert {"lineage_and_currentness", "j2_coverage", "lexical_full_text",
            "connector_readable_derived_orientation"} <= shared


def test_B0_B2_B3_distinctions_do_not_duplicate_semantic_authority():
    import json

    contract = json.loads((
        REPO / "experiments/r0_p03_navigation_probe/common_substrate_contract_candidate.json"
    ).read_text(encoding="utf-8"))
    additions = contract["comparison_augmentations"]
    assert additions["B0"]["additional_signals"] == []
    assert "editorial_carrier_to_governing_about_links" in additions["B2"]["additional_signals"]
    assert "bounded_cross_cutting_concern_vocabulary" in additions["B3"]["additional_signals"]
    assert "collapse" in additions["B2"]["collapse_rule"].lower() or "non-distinct" in additions["B2"]["collapse_rule"]
    assert additions["B4"]["conditional"] is True
    for arm in additions.values():
        assert not (set(arm["additional_signals"]) & set(contract["shared_capabilities"]["all_arms"]))


def test_contract_does_not_publish_scores_or_sample_members():
    import json

    contract = json.loads((
        REPO / "experiments/r0_p03_navigation_probe/common_substrate_contract_candidate.json"
    ).read_text(encoding="utf-8"))
    assert "scores" not in contract
    assert "selected_heldout" not in contract
    assert "gold_answers" not in contract
    assert "accepted_results" not in contract
