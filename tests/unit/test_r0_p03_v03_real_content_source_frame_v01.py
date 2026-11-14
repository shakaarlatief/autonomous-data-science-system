"""Reproducible, explicitly non-scored real-content P03-V2 source preadmission.

The existing Research 672 method acceptance does not supply or admit new
individual owner-accepted experimental J1 consequences. These tests guard that
boundary while verifying pinned bytes, evidence roles and exact line anchors.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import v03_real_content_source_frame_v01 as seed


def test_original_git_pin_and_source_role_frame_are_reproducible():
    output = seed.build()
    assert output["source_commit"] == "5463b2ad2e6799339746637f38340fa2a9dc00f6"
    assert output["distinct_original_git_paths"] == 15
    assert output["source_witness_count"] == 16
    assert len(set(w["source_path"] for w in output["witnesses"])) == 15
    assert all(w["source_commit"] == seed.PIN for w in output["witnesses"])


@pytest.mark.parametrize("label,path,role,anchor", seed.ROWS)
def test_each_source_evidence_line_exists_exactly_in_pinned_git_blob(
    label, path, role, anchor,
):
    out = seed.witness_record(label, path, role, anchor)
    source, object_sha = seed.git_bytes(path)
    lines = source.decode("utf8").splitlines()
    assert out["git_blob_oid"] == object_sha
    assert out["sha256"] == hashlib.sha256(source).hexdigest()
    assert out["witness_line_sha256"] == hashlib.sha256(
        lines[out["anchor_line"] - 1].encode("utf8")
    ).hexdigest()
    assert anchor in lines[out["anchor_line"] - 1]
    assert out["authority_verification"] == (
        "SOURCE_FACT_ONLY_NOT_NEWLY_ACCEPTED_J1"
    )


def test_d035_and_d036_share_historical_source_but_not_semantic_authority():
    data = seed.build()
    by_id = {w["witness_id"]: w for w in data["witnesses"]}
    assert by_id["D035"]["source_path"] == by_id["D036"]["source_path"]
    assert by_id["D035"]["sha256"] == by_id["D036"]["sha256"]
    assert by_id["D035"]["anchor_line"] != by_id["D036"]["anchor_line"]
    assert data["accepted_experimental_j1_effects"] == []
    assert data["qualified_experimental_j2_relations"] == []


def test_test_definitions_and_workflow_definitions_are_not_runs():
    data = seed.build()
    by_id = {w["witness_id"]: w for w in data["witnesses"]}
    for label in ("TEST_ID", "TEST_AUTH", "TEST_CAPTURE"):
        assert by_id[label]["source_role_classification"] == (
            "TEST_DEFINITION_NOT_EXECUTION"
        )
    assert by_id["CI_DEFINITION"]["source_role_classification"] == (
        "WORKFLOW_DEFINITION_NOT_EXECUTION"
    )
    assert "TEST_EXECUTED_SUCCESSFULLY" not in data["roles"]


def test_derived_status_and_old_navigation_are_not_governing_acceptances():
    data = seed.build()
    by_id = {w["witness_id"]: w for w in data["witnesses"]}
    assert by_id["DERIVED_ROUTING"]["source_role_classification"] == (
        "DERIVED_ROUTING_STATUS_NOT_J1"
    )
    assert by_id["W5SUBJECT"]["source_role_classification"] == (
        "HISTORICAL_NAVIGATION_EVIDENCE"
    )
    assert data["formal_primary_tasks"] == []
    assert data["formal_arm_scores"] is None


@pytest.mark.parametrize("proposal", seed.EFFECT_PROPOSALS)
def test_all_proposed_effects_unadmitted_even_if_method_was_approved(proposal):
    assert proposal["status"] == "NOT_ADMITTED_EXPERIMENT_J1"
    with pytest.raises(ValueError, match="EXPERIMENT_EFFECT_NOT_OWNER_RATIFIED"):
        seed.require_experimental_effect_admission(proposal)
    with pytest.raises(ValueError, match="EXPERIMENTAL_J1_ADMISSION_CONTRACT_NOT_IMPLEMENTED"):
        seed.require_experimental_effect_admission(
            proposal, owner_confirmation_record={
                "claimed_owner": "unverified", "decision": "ACCEPT"
            },
        )


def test_unknown_or_fabricated_effect_cannot_be_admitted():
    bogus = {
        "candidate_id": "FAKE", "source_witness": "D036",
        "assertion": "Made up", "status": "NOT_ADMITTED_EXPERIMENT_J1",
    }
    with pytest.raises(ValueError, match="Unrecognized experimental governing"):
        seed.require_experimental_effect_admission(bogus)


def test_mutable_worktree_byte_reader_is_not_used_for_evidence(monkeypatch):
    sample = seed.ROWS[0]
    before = seed.witness_record(*sample)

    def forbidden_worktree_read(self):
        raise AssertionError("Mutable worktree file reading is forbidden here")

    # A corrupted or unavailable working-tree file must not substitute for
    # the Git-pinned bytes. Do not create any host-global temporary files.
    with monkeypatch.context() as isolated:
        isolated.setattr(Path, "read_bytes", forbidden_worktree_read)
        assert seed.witness_record(*sample) == before


def test_wrong_anchor_and_unknown_source_path_fail_closed():
    row = seed.ROWS[0]
    with pytest.raises(ValueError, match="Witness anchor must be unique"):
        seed.witness_record(row[0], row[1], row[2], "NOT_IN_SOURCE_XXXXXXXX")
    with pytest.raises(ValueError, match="not part of the approved seed inventory"):
        seed.git_bytes("not-a-source-in-frame.md")


def test_invalid_source_commit_pin_rejected():
    with pytest.raises(ValueError, match="full pinned hexadecimal"):
        seed.git_bytes(seed.ROWS[0][1], pin="not-a-commit")
    with pytest.raises(ValueError, match="Pinned source unavailable"):
        seed.git_bytes(seed.ROWS[0][1], pin="0" * 40)


def test_frozen_seed_receipt_has_exact_content_and_no_autonomous_rewrite():
    receipt = json.loads(seed.OUTPUT.read_text("utf8"))
    assert receipt == seed.build()
    assert receipt["scientific_admission"] == "HOLD"
    assert receipt["historical_legacy_gold"] is None
    assert receipt["formal_arm_scores"] is None
    assert len(receipt["effect_proposals"]) == 3
    raw = seed.OUTPUT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "3bfd99fd15dc9ab4d3b86d2cb0de7bd7c0480ccbe344704c44a38f16e03db5a4"
    )
