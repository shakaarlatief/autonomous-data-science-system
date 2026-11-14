"""Exact original-source and fail-closed tests for proposed P03-V2 D1 reuse.

The D1 owner acceptance is documentary and applies to the ORIGINAL development
replay. An agent-created owner_confirmation does not admit the effects in
the new P03 world. Real Git parent/path and D1 historical documentary claims
are examined at their original Git bytes. Nothing produces formal P03 gold.
"""
from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import v03_d1_real_event_admission_contract_v01 as p03


@pytest.fixture(scope="module")
def proposal():
    return p03.build_owner_packet()


@pytest.fixture(scope="module")
def original():
    raw = {path: p03.original_git_file(path)[0] for path in p03.FILES}
    j1 = json.loads(raw[p03.D1 + "accepted_j1.json"])
    facts = json.loads(raw[p03.D1 + "source_facts.json"])
    old_packet = json.loads(raw[p03.D1 + "owner_review_packet.json"])
    return raw, j1, facts, old_packet


def test_all_original_git_sources_are_exact_and_identity_bound(proposal):
    assert proposal["source_commit"] == p03.PIN
    assert len(proposal["source_manifest"]) == 12
    assert len({x["source_path"] for x in proposal["source_manifest"]}) == 12
    for record in proposal["source_manifest"]:
        raw, known = p03.original_git_file(record["source_path"])
        assert record == known
        assert record["sha256"] == sha256(raw).hexdigest()
        assert len(record["git_blob_oid"]) == 40


def test_original_owner_packet_mixed_byte_basis_is_explicit_and_exact(proposal):
    facts = proposal["original_d1_provenance"]
    assert facts["original_d1_recorded_sha256_basis"] == "WORKTREE_BYTES_CRLF"
    assert facts["original_d1_recorded_owner_packet_sha256"] == (
        "2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4"
    )
    assert facts["same_content_git_blob_sha256"] == (
        "af7037517174dda8e80a34f4c3cc3608afacf498ed798a3fb91242dfe4765e79"
    )
    assert facts["original_d1_packet_git_blob_length"] == 5107
    assert facts["original_d1_packet_crlf_length"] == 5193


def test_original_owner_review_effects_are_byte_reconstructed_not_inferred(original, proposal):
    _, accepted, _, packet = original
    assert packet["proposed_j1_effects"] == accepted["effects"]
    assert proposal["requested_experiment_only_j1_effects"] == accepted["effects"]
    assert len(proposal["requested_experiment_only_j1_effects"]) == 4
    accounting = proposal["requested_effect_accounting"]
    assert accounting == {
        "REALIZATION_TRACKED": 1, "NO_REALIZATION_REQUIRED": 3,
    }


def test_real_git_action_parent_path_and_connector_attestation_are_not_equated(proposal):
    evidence = proposal["original_d1_provenance"]
    assert evidence["actual_git_action_parent"] == p03.CORRECTION
    assert evidence["actual_git_changed_paths"] == [p03.MESSAGE_018]
    assert evidence["original_git_action_commit"] == p03.ACTION
    assert evidence["transport_proof_class"] == (
        "CLAUDE_SOURCE_ATTESTATION_NOT_INDEPENDENT_PROVIDER_PROOF"
    )
    fact_classes = {x["evidence_id"]: x for x in proposal["j2_evidence_ladder_candidate"]}
    assert fact_classes["J2OBS-D1-GIT-PATH"]["verification"] == "GIT_OBJECT_VERIFIED"
    assert fact_classes["J2ASSERT-D1-CLAUDE-TRANSPORT"]["verification"] != "GIT_OBJECT_VERIFIED"
    assert fact_classes["J2REL-D1-E01-COVERAGE"]["verification"] == (
        "NOT_ADMITTED_AS_P03_NATURAL_OWNER_RELATION"
    )


def test_lifecycle_preserves_exact_predecessor_successor_and_open_reset(proposal):
    assert proposal["proposed_lineage"] == {
        "relation": "REPLACE",
        "predecessor_id": "R484-S5-CLAUDE-RUNTIME-BRIDGE-REQUIREMENT",
        "successor_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
        "realization_succession": "OPEN_RESET",
    }


def test_original_d1_replay_j3_remains_historical_and_not_formal_p03(proposal):
    preview = proposal["original_d1_non_governing_j3_preview"]
    d1 = preview["non_governing_d1_evaluator_projection"]
    assert preview["historical_d1_disposition"] == "D1_AMEND_NOT_FORMAL_P03_PASS"
    assert preview["d1_raw_v01_initialization_shape"] == "SINGLE_OBJECT"
    assert preview["research_499_reconciled_initialization_shape"] == (
        "ORDERED_LIST_BY_EFFECT_ID"
    )
    assert d1["realization_initialization"] == [{
        "effect_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
        "mode": "OPEN_RESET",
    }]
    assert d1["requirement_satisfied"] is True
    assert d1["current_effect_ids"] == [
        "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT", "D1-E02-NO-CLAUDE-RUNTIME-BRIDGE",
    ]


def test_new_world_still_has_no_accepted_j1_or_qualified_j2(proposal):
    assert proposal["new_p03_owner_decision"] is None
    assert proposal["new_p03_accepted_j1_effect_ids"] == []
    assert proposal["new_p03_qualified_j2_relations"] == []
    assert proposal["new_p03_formal_tasks"] == []
    assert proposal["new_p03_formal_scores"] is None
    assert proposal["original_d1_historical_replay_evidence"][
        "original_owner_acceptance_applies_to_new_p03_world"
    ] is False


def test_new_owner_confirmation_is_not_synthesized_by_coordinator(proposal):
    with pytest.raises(ValueError, match="P03_EXACT_OWNER_REUSE_APPROVAL_MISSING"):
        p03.admission_check(proposal)
    with pytest.raises(ValueError, match="P03_EXPERIMENT_OWNER_ADMISSION_NOT_YET_QUALIFIED"):
        p03.admission_check(
            proposal, owner_confirmation={
                "owner": "unknown-agent", "decision": "ACCEPT",
                "claimed_digest": p03.sha(p03.canonical_bytes(proposal)),
            },
        )


@pytest.mark.parametrize("field,value", [
    ("new_p03_owner_decision", "ACCEPT"),
    ("new_p03_accepted_j1_effect_ids", ["D1-E01-D2-CLAUDE-WRITE-REQUIREMENT"]),
    ("new_p03_qualified_j2_relations", [{"forged": True}]),
    ("new_p03_formal_scores", {"B0": "PASS"}),
    ("proposal_status", "APPROVED"),
])
def test_forged_new_world_status_is_rejected(proposal, field, value):
    altered = deepcopy(proposal)
    altered[field] = value
    with pytest.raises(ValueError, match="OWNER_VISIBLE_EXPERIMENT_PACKET_CHANGED"):
        p03.admission_check(altered, owner_confirmation={"decision": "ACCEPT"})


def test_altered_proposed_effect_meaning_is_rejected(proposal):
    altered = deepcopy(proposal)
    altered["requested_experiment_only_j1_effects"][0]["accepted_effect_statement"] += (
        " Additional unapproved owner obligation."
    )
    with pytest.raises(ValueError, match="OWNER_VISIBLE_EXPERIMENT_PACKET_CHANGED"):
        p03.admission_check(altered)


def test_original_acceptance_cannot_be_derived_from_modified_effect(original):
    sources, j1, facts, old_packet = original
    invalid = deepcopy(j1)
    invalid["effects"][0]["accepted_effect_statement"] += " forged suffix"
    with pytest.raises(ValueError, match="D1_ACCEPTED_EFFECTS_DO_NOT_EQUAL_OWNER_PACKET"):
        p03.assert_original_event_and_owner(invalid, facts, old_packet, sources)


def test_forged_original_git_parent_or_changed_paths_are_detected(original):
    sources, j1, facts, old_packet = original
    altered = deepcopy(facts)
    altered["action"]["parent"] = "f" * 40
    with pytest.raises(ValueError, match="D1_FACT_PARENT_CONFLICTS_WITH_GIT"):
        p03.assert_original_event_and_owner(j1, altered, old_packet, sources)
    altered = deepcopy(facts)
    altered["action"]["changed_paths"] = ["docs/research/485.md"]
    with pytest.raises(ValueError, match="D1_FACT_CHANGED_PATHS_CONFLICT_WITH_GIT"):
        p03.assert_original_event_and_owner(j1, altered, old_packet, sources)


def test_forged_lineage_is_detected(original):
    sources, j1, facts, old_packet = original
    bad = deepcopy(j1)
    bad_lineage = next(x["lineage"] for x in bad["effects"] if x["type"] == "LIFECYCLE")
    bad_lineage["realization_succession"] = "CARRY_SUCCESSOR_UNDER_NO_REVIEW"
    # Moving the same corruption to the old packet is not allowed either.
    modified_original_packet = deepcopy(old_packet)
    modified_original_packet["proposed_j1_effects"] = deepcopy(bad["effects"])
    with pytest.raises(ValueError, match="D1_LINEAGE_NOT_SUPPORTED_BY_ACCEPTED_REPLAY"):
        p03.assert_original_event_and_owner(bad, facts, modified_original_packet, sources)


def test_forged_recorded_hash_basis_detected(original):
    sources, j1, facts, old_packet = original
    corrupted = deepcopy(j1)
    corrupted["owner_packet_sha256"] = "0" * 64
    with pytest.raises(ValueError, match="ORIGINAL_OWNER_PACKET_RECORDED_HASH_BASIS_MISMATCH"):
        p03.assert_original_event_and_owner(corrupted, facts, old_packet, sources)


def test_missing_original_owner_acceptance_record_detected(original):
    sources, j1, facts, old_packet = original
    altered = dict(sources)
    altered["docs/research/491_d1_owner_acceptance_and_j1_binding.md"] = (
        b"Owner response not given"
    )
    with pytest.raises(ValueError, match="ORIGINAL_D1_OWNER_DECISION_NOT_SOURCE_ATTESTED"):
        p03.assert_original_event_and_owner(j1, facts, old_packet, altered)


def test_unrecognized_source_path_and_worktree_are_not_evidence():
    with pytest.raises(ValueError, match="SOURCE_FILE_OUTSIDE_FROZEN_EVIDENCE_SET"):
        p03.original_git_file("docs/anything_unreviewed.md")
    with pytest.raises(ValueError, match="ORIGINAL_GIT_EVIDENCE_UNAVAILABLE"):
        p03.git("cat-file", "-t", "0" * 40)


def test_current_python_evaluator_source_must_match_pinned_git(monkeypatch):
    # Source-byte pinning matters because the replay evaluator is imported
    # from the worktree instead of executed as historical Git source code.
    original_reader = p03.Path.read_bytes

    def altered_read_bytes(self):
        if self.name == "evaluator_chatgpt_a.py":
            return b"# forged evaluator with different semantics"
        return original_reader(self)

    with monkeypatch.context() as isolated:
        isolated.setattr(p03.Path, "read_bytes", altered_read_bytes)
        with pytest.raises(ValueError, match="EXECUTED_D1_EVALUATOR_DIFFERS_FROM_PINNED_SOURCE"):
            p03.build_owner_packet()


def test_immutable_packet_and_receipt_match_replay_and_canonical_digest(proposal):
    packet = json.loads(p03.PACKAGE_PATH.read_text("utf8"))
    receipt = json.loads(p03.RECEIPT_PATH.read_text("utf8"))
    assert packet == proposal
    assert receipt == p03.build_receipt(proposal)
    assert receipt["owner_packet_canonical_sha256"] == (
        "186c70ff487104f8ee5baee8d21b50ffd466e812c6b97debb20296c8bbf9451f"
    )
    assert receipt["new_p03_accepted_effects"] == 0
    assert receipt["formal_v03_experiment_world"] == "HOLD"
    assert receipt["formal_r0_p03_scores"] is None
