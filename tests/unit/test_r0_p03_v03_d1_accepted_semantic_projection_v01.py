"""Negative and source-integrity tests for explicit P03-only J1 acceptance.

Tests deliberately distinguish a human-reported chat owner decision from
independently authenticated governing authority, and J1 input acceptance from
unqualified J2 coverage and J3 completion. These are development tests, not
formal Research 513 scorers.
"""
from copy import deepcopy
from hashlib import sha256
import json
import subprocess

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_d1_accepted_semantic_projection_v01 as admit,
)


@pytest.fixture(scope="module")
def packet():
    return admit.pinned_owner_packet()


@pytest.fixture(scope="module")
def binding():
    return admit.owner_binding()


@pytest.fixture(scope="module")
def projection():
    return admit.build_accepted_projection()


def test_exact_published_original_owner_packet_immutable_and_bound(packet):
    assert packet["proposal_id"] == "R0_P03_V2_D1_REAL_EVENT_REUSE_CANDIDATE_001"
    assert packet["proposed_world_id"] == "P03V2_DEVELOPMENT_WORLD_CLAUDE_COLLABORATION_V01"
    assert admit.digest(packet) == admit.REVIEW_CANONICAL_SHA256
    assert len(packet["requested_experiment_only_j1_effects"]) == 4
    assert packet["new_p03_owner_decision"] is None
    assert not packet["new_p03_accepted_j1_effect_ids"]
    assert not packet["new_p03_qualified_j2_relations"]


def test_new_decision_binds_exact_packet_commit_and_owner_reply(binding, packet):
    admit.validate_acceptance_binding(binding, packet)
    assert binding["decision"] == "ACCEPT"
    assert binding["verbatim_owner_reply"] == "I ACCEPT."
    assert binding["source_proposal_commit"] == admit.REVIEW_COMMIT
    assert binding["source_proposal_canonical_json_sha256"] == admit.REVIEW_CANONICAL_SHA256
    assert binding["source_proposal_git_bytes_sha256"] == admit.REVIEW_GIT_SHA256
    assert binding["accepted_scope"] == (
        "REUSE_EXACT_FOUR_D1_EFFECT_STATEMENTS_AS_P03_EXPERIMENT_ONLY_J1_INPUTS"
    )
    assert binding["decision_provenance_class"].endswith("NOT_INDEPENDENTLY_AUTHENTICATED")


def test_exact_bindings_reject_edited_decision_or_scope(binding, packet):
    for field, falsification in [
        ("verbatim_owner_reply", "ACCEPT if later convenient"),
        ("decision", "REJECT"),
        ("decision_date", "2026-11-13"),
        ("source_proposal_commit", "0" * 40),
        ("source_proposal_canonical_json_sha256", "0" * 64),
        ("accepted_scope", "PRODUCTION_J1_UNLIMITED"),
        ("experimental_world_id", "UNRELATED_WORLD"),
        ("historical_d1_raw_outcome", "D1_PASS"),
        ("formal_r0_p03_status", "PASS"),
    ]:
        altered = deepcopy(binding)
        altered[field] = falsification
        with pytest.raises(ValueError, match="BINDING"):
            admit.validate_acceptance_binding(altered, packet)


def test_binding_does_not_admit_j2_even_if_hand_written(binding, packet):
    altered = deepcopy(binding)
    altered["accepted_j2_relations"].append({
        "source_owner": "FAKE", "target": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
        "qualified": True,
    })
    with pytest.raises(ValueError, match="BINDING"):
        admit.validate_acceptance_binding(altered, packet)


def test_exact_owner_reply_not_a_cryptographic_signature(binding):
    assert binding["decision_provenance_class"] == (
        "CHAT_CONVERSATION_EXPLICIT_OWNER_REPLY_NOT_INDEPENDENTLY_AUTHENTICATED"
    )
    assert "EXTERNAL_OWNER_IDENTITY_OR_CRYPTOGRAPHIC_AUTHENTICATION" in (
        binding["excluded_authorizations"]
    )


def test_projection_accepts_exact_four_j1_effects_and_no_more(projection, packet):
    assert projection["accepted_j1"]["count"] == 4
    assert projection["accepted_j1"]["effects"] == (
        packet["requested_experiment_only_j1_effects"]
    )
    assert tuple(
        e["accepted_effect_id"] for e in projection["accepted_j1"]["effects"]
    ) == admit.EXPECTED_EFFECT_IDS
    assert projection["accepted_j1"]["closed_accounting"] == {
        "NO_REALIZATION_REQUIRED": 3,
        "REALIZATION_TRACKED": 1,
    }


def test_no_p03_source_owner_relational_qualification_or_j3_autocertification(projection):
    assert len(projection["j2_evidence"]["git_observable"]) == 1
    assert len(projection["j2_evidence"]["source_reported_attestations"]) == 1
    assert len(projection["j2_evidence"]["natural_owner_relational_proposals_unadmitted"]) == 1
    assert projection["j2_evidence"]["qualified_relational"] == []
    assert projection["j2_evidence"]["qualified_relational_count"] == 0
    assert projection["j3"]["new_experimental_requirement_satisfaction"] == (
        "HOLD_J2_NATURAL_OWNER_QUALIFICATION"
    )
    assert projection["j3"]["new_experimental_completion_certified"] is False
    assert projection["j3"]["derived_orientation"] == "REVIEW_REQUIRED"
    assert projection["world_status"] == "J1_EXPERIMENT_ACCEPTED_J2_RELATIONAL_AND_J3_QUALIFICATION_HOLD"


def test_original_d1_amend_is_not_reclassified_or_rescored(projection):
    assert projection["original_d1_raw_outcome"] == "D1_AMEND"
    assert projection["historical_d1_rescored"] is False
    prior = projection["j3"]["historical_non_governing_d1_preview"]
    assert prior["historical_d1_disposition"] == "D1_AMEND_NOT_FORMAL_P03_PASS"
    assert prior["non_governing_d1_evaluator_projection"]["requirement_satisfied"] is True
    assert projection["j3"]["new_experimental_completion_certified"] is False


def test_original_lineage_is_exact_and_accepted_only_in_experiment(projection):
    line = projection["lineage"]
    assert line["accepted_experiment_semantics"] == {
        "predecessor_id": "R484-S5-CLAUDE-RUNTIME-BRIDGE-REQUIREMENT",
        "realization_succession": "OPEN_RESET",
        "relation": "REPLACE",
        "successor_id": "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
    }
    assert line["historical_d1_predicate_not_reexecuted_as_new_j3"] is True


def test_transport_attestation_must_not_be_called_independent_provider_proof(projection):
    observed = projection["j2_evidence"]["git_observable"][0]
    attested = projection["j2_evidence"]["source_reported_attestations"][0]
    assert observed["verification"] == "GIT_OBJECT_VERIFIED"
    assert attested["verification"] == (
        "MESSAGE_CONTENT_VERIFIED_PROVIDER_TRANSPORT_NOT_INDEPENDENTLY_OBSERVED"
    )
    assert attested["governing_completion_consequence"] is False


def test_no_formal_b0_b4_or_new_gold_is_invented(projection):
    assert projection["primary_tasks_originated"] is False
    assert projection["historical_legacy_nine_gold_rejudged"] is False
    assert projection["formal_b0_b4_scores"] is None
    assert projection["physical_architecture_selected"] is False
    assert projection["migration_authorized"] is False


def test_historical_owner_review_source_blob_remains_unchanged():
    source = subprocess.check_output(
        ["git", "show", f"{admit.REVIEW_COMMIT}:{admit.REVIEW_FILE}"],
        cwd=admit.ROOT,
    )
    assert sha256(source).hexdigest() == admit.REVIEW_GIT_SHA256
    assert json.loads(source)["new_p03_owner_decision"] is None


def test_acceptance_binding_is_restricted_to_one_literal_reuse_event(binding):
    assert len(binding["accepted_effect_ids"]) == 4
    assert tuple(binding["accepted_effect_ids"]) == admit.EXPECTED_EFFECT_IDS
    assert tuple(binding["excluded_authorizations"]) == admit.EXPECTED_EXCLUSIONS


def test_result_immutable_and_reproducible_after_accepted_reply(projection):
    on_disk = json.loads(admit.PROJECTION_PATH.read_text(encoding="utf8"))
    assert on_disk == projection
    assert on_disk["owner_decision"]["binding_record_canonical_sha256"] == (
        admit.BINDING_CANONICAL_SHA256
    )


def test_unknown_or_extra_binding_fields_are_rejected(binding, packet):
    mutated = deepcopy(binding)
    mutated["independent_owner_signature"] = "FORGED"
    with pytest.raises(ValueError, match="BINDING"):
        admit.validate_acceptance_binding(mutated, packet)


def test_published_packet_cannot_be_replaced_by_worktree_mock(monkeypatch, packet):
    original_run = admit.subprocess.run

    def forbidden_substitute(argv, **kwargs):
        if argv[:2] == ["git", "show"] and str(argv[2]).startswith(admit.REVIEW_COMMIT):
            fake = json.dumps({**packet, "proposal_id": "FORGED"}).encode("utf8")
            return subprocess.CompletedProcess(argv, 0, stdout=fake, stderr=b"")
        return original_run(argv, **kwargs)

    with monkeypatch.context() as isolated:
        isolated.setattr(admit.subprocess, "run", forbidden_substitute)
        with pytest.raises(ValueError, match="GIT_BLOB_CHANGED"):
            admit.pinned_owner_packet()
