"""Real original-Git source closure and synthetic shared-projection parity controls.

The original 80-file archive remains locally restricted, unmodified and
unreleased. All model-visible results are aggregate only. No source semantics
or owner acceptance can be inferred from file families or Git provenance.

Test cases include original byte verification, exact corpus frontier evidence,
negative invalid-source/role/authority and arm interface injection controls.
They are NOT the official Research 513 B0-B4 arms or scored source task gold.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256

import pytest

from experiments.r0_p03_navigation_probe import (
    source_closure_common_projection_probe_v01 as probe,
)


@pytest.fixture(scope="module")
def actual_world() -> tuple:
    records, content, tree, receipt = probe.checked_corpus(probe.ROOT)
    return records, content, tree, receipt


def test_actual_original_zip_and_source_tree_identical(actual_world: tuple) -> None:
    records, contents, tree, receipt = actual_world
    assert len(records) == 80
    assert len(contents) == 80
    assert len(tree) >= 2500
    assert receipt["candidate_original_source_count"] == 80
    assert all(tree[row["path"]] == row["git_blob_oid"] for row in records)
    assert all(
        sha256(contents[row["path"]]).hexdigest() == row["sha256"]
        for row in records
    )
    assert all(row["current_authority"] == "UNKNOWN_NOT_PROVEN" for row in records)
    assert all(row["family_qualification"] == "NOT_INDEPENDENTLY_REVIEWED" for row in records)
    assert all(row["implementation_validation"] == "UNKNOWN_NOT_PROVEN" for row in records)


def test_real_literal_citation_frontier_is_source_unknown(actual_world: tuple) -> None:
    records, _, tree, _ = actual_world
    _, public = probe.source_reference_frontier(records, tree)
    counts = public["reference_totals"]
    assert counts == {
        "inside_reference_occurrences": 42,
        "outside_reference_occurrences": 258,
        "sources_with_inside_reference": 16,
        "sources_with_outside_reference": 33,
    }
    assert public["distinct_outside_reference_target_count"] == 199
    assert public["all_literal_external_targets_exist_at_exact_original_pin"] is True
    assert public["task_answerability_closure"] == "NOT_ADJUDICATED"
    assert public["non_literal_dependency_closure"] == "NOT_ADJUDICATED"


def test_exact_original_provenance_is_not_semantic_identity(actual_world: tuple) -> None:
    records, content, _, _ = actual_world
    common = probe.shared_source_projection(records, content)
    assert len(common["carrier"]) == 80
    assert len(common["literal_citation_candidates"]) == 300
    assert not common["accepted_governing_effects"]
    assert not common["accepted_j2_realization_edges"]
    assert not common["accepted_receipt_verification_edges"]
    assert all(
        car["source_authority"]["authority_currentness"] == "UNKNOWN_NOT_PROVEN"
        and car["source_authority"]["j2_realization_coverage"] == "UNPROVEN"
        and car["source_authority"]["actual_test_execution"] == "UNPROVEN"
        for car in common["carrier"]
    )
    assert all(
        link["relation_class"] == "LEXICAL_CITATION_ONLY_UNADJUDICATED"
        for link in common["literal_citation_candidates"]
    )


def test_full_text_actual_common_input_in_memory_works(actual_world: tuple) -> None:
    _, content, _, _ = actual_world
    assert probe.lexical_capability_check(content) == {
        "authority": 49,
        "validation": 43,
        "source": 57,
    }


def test_five_empty_interface_slots_keep_identical_source_projection(actual_world: tuple) -> None:
    records, content, _, _ = actual_world
    shared = probe.shared_source_projection(records, content)
    observed = probe.verify_common_interface_parity(shared)
    assert observed["all_empty_augmentations_have_byte_identical_common_view"]
    assert observed["simulated_interface_slot_count"] == 5
    assert observed["arm_implementations_actually_tested"] == 0
    assert observed["real_b0_b4_common_parity_qualification"] == "NOT_PERFORMED"
    digest = sha256(probe.canonical(shared)).hexdigest()
    assert observed["shared_projection_sha256"] == digest
    assert len({probe.arm_interface(shared, a)["shared_original_source_sha256"]
                for a in probe.ARMS}) == 1


def test_non_authoritative_extra_navigation_never_changes_common_model() -> None:
    common = {
        "carrier": [{"source_authority": {"authority_currentness": "UNKNOWN_NOT_PROVEN"}}],
        "accepted_governing_effects": [],
        "derived_orientation": {"authoritative": False},
    }
    baseline = sha256(probe.canonical(common)).hexdigest()
    permissible = probe.arm_interface(
        common, "B1", {"controlled_subject_memberships": [
            {"note": "Synthetic-topic-example-only"}
        ]},
    )
    assert permissible["shared_original_source_sha256"] == baseline
    assert permissible["shared_common_projection"] == common
    assert permissible["new_authority_from_extra_navigation"] is False
    with pytest.raises(ValueError):
        probe.arm_interface(common, "B0", {"controlled_subject_memberships": []})
    with pytest.raises(ValueError):
        probe.arm_interface(common, "B2", {"carrier": []})
    with pytest.raises(ValueError):
        probe.arm_interface(common, "B3", {"accepted_governing_effects": []})
    with pytest.raises(ValueError):
        probe.arm_interface(common, "B4", {"semantic_candidate_rankings": {"rank": 1}})
    with pytest.raises(ValueError):
        probe.arm_interface(
            common, "B1", {"controlled_subject_memberships": [
                {"nested": {"source_authority": "ACCEPTED"}}
            ]},
        )
    with pytest.raises(ValueError):
        probe.arm_interface(
            common, "B2", {"editorial_about_links": [
                {"governing_status": "ACCEPTED", "note": "illegal escalation"}
            ]},
        )
    assert common["derived_orientation"]["authoritative"] is False


@pytest.mark.parametrize(
    "path",
    ["", "../escape", "source/../../bad", "/absolute", "a\\windows",
     "a//double", "a/./normalized", "a\x00nul"],
)
def test_archive_path_escape_and_normalization_are_rejected(path: str) -> None:
    assert not probe.safe_path(path)


def test_one_cross_world_literal_ref_is_not_promoted_to_dependency(actual_world: tuple) -> None:
    records, _, tree, _ = actual_world
    bad = deepcopy(records)
    target = next(iter(bad[0]["literal_refs_outside_selected_world"]), None)
    if target is None:
        for row in bad:
            if row["literal_refs_outside_selected_world"]:
                bad[0]["literal_refs_in_selected_original"] = [row["literal_refs_outside_selected_world"][0]]
                break
    else:
        bad[0]["literal_refs_in_selected_original"] = [target]
    with pytest.raises(ValueError, match="frontier"):
        probe.source_reference_frontier(bad, tree)


def test_exclusive_output_bytes_match_source_free_replay() -> None:
    public, local = probe.build(probe.ROOT)
    expected_local = probe.canonical(local)
    assert sha256(probe.LOCAL_DETAIL.read_bytes()).hexdigest() == sha256(expected_local).hexdigest()
    assert public["source_admissions"] == 0
    assert public["formal_12_plus_9_tasks"] == "NONE"
    assert public["real_arm_scoring"] == "NONE"
    assert public["physical_architecture_selected"] is False
    data = dict(public)
    data["private_report_sha256_receipt_only"] = sha256(expected_local).hexdigest()
    data["private_report_bytes_receipt_only"] = len(expected_local)
    assert probe.PUBLIC_OUTPUT.read_bytes() == probe.canonical(data)
