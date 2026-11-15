"""Exact R0-P03-V2 owner-accepted J1 and initial source-role audit.

All checks concern the explicitly accepted experimental effect packet and
the still-unrealized initial world. They cannot authenticate the human's
account or the implementation source owner.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as p,
)


@pytest.fixture(scope="module")
def projection():
    return p.build()


def test_exact_git_published_proposal_is_proposal_not_retroactive_owner_decision():
    data = p.original_proposal()
    assert data["proposal_id"] == p.PROPOSAL_ID
    assert data["decision_state"] == "PROPOSED_NOT_OWNER_ACCEPTED"
    assert tuple(x["id"] for x in data["new_effects"]) == p.EXPECTED_IDS


def test_original_packet_byte_and_canonical_hash_bound():
    assert sha256(p.PROPOSAL.read_bytes()).hexdigest() == p.PROPOSAL_GIT_SHA256
    original = p.original_proposal()
    payload = {
        k: v for k, v in original.items()
        if k not in {"canonicalization", "canonical_payload_sha256"}
    }
    assert p.canonical_sha(payload) == p.PROPOSAL_CANONICAL_SHA256


def test_owner_reply_exactly_bound_with_experiment_only_scope():
    data = p.accepted_binding()
    assert data["decision"] == "ACCEPT"
    assert data["verbatim_owner_reply"] == "I ACCEPT. Proceed."
    assert data["decision_date"] == "2026-11-15"
    assert data["experimental_world_id"] == p.EXPERIMENT_ID
    assert data["source_proposal_commit"] == p.PROPOSAL_COMMIT
    assert data["source_proposal_canonical_payload_sha256"] == p.PROPOSAL_CANONICAL_SHA256


def test_binding_is_pinned_to_exact_bytes_and_no_detached_owner_signer():
    assert sha256(p.BINDING.read_bytes()).hexdigest() == p.BINDING_FILE_SHA256
    assert "NOT_INDEPENDENTLY_AUTHENTICATED" in p.accepted_binding()["decision_provenance_class"]


def test_no_j2_attested_by_owner_acceptance():
    data = p.accepted_binding()
    assert data["accepted_j2_relations"] == []
    assert "NATURAL_OWNER_RELATIONAL_J2_QUALIFICATION" in data["excluded_authorizations"]
    assert "SOURCE_OWNER_AUTHENTICATION_BY_OWNER_ACCEPTANCE" in data["excluded_authorizations"]


def test_four_effects_are_exact_and_all_effect_classes_preserved(projection):
    effects = projection["accepted_j1"]["effects"]
    assert tuple(x["id"] for x in effects) == p.EXPECTED_IDS
    assert [x["type"] for x in effects] == [
        "REQUIRE", "REQUIRE", "LIFECYCLE", "PROHIBIT"
    ]
    assert [x["accounting"] for x in effects] == [
        "REALIZATION_TRACKED", "REALIZATION_TRACKED",
        "NO_REALIZATION_REQUIRED", "NO_REALIZATION_REQUIRED",
    ]


def test_s0_active_s1_dormant_and_rule_not_activated(projection):
    assert projection["accepted_j1"]["current_effect_ids"] == list(p.EXPECTED_ACTIVE)
    assert projection["accepted_j1"]["dormant_until_source_revision"] == [p.EXPECTED_IDS[1]]
    assert projection["currentness"]["current_state"] == "S0_INITIAL"
    assert projection["currentness"]["activation_status"] == "NOT_ACTIVATED"
    assert projection["currentness"]["actual_source_revision_qualified"] is False


def test_open_reset_lifecycle_rule_does_not_carry_legacy_s0_evidence(projection):
    rule = projection["currentness"]["accepted_transition_rule"]
    assert rule["relation"] == "REPLACE"
    assert rule["realization_succession"] == "OPEN_RESET"
    assert rule["predecessor_id"] == p.EXPECTED_IDS[0]
    assert rule["successor_id"] == p.EXPECTED_IDS[1]
    assert projection["currentness"]["on_future_qualified_activation"][
        "evidence_carryover_allowed"
    ] is False


def test_j2_and_j3_hold_not_conflated_with_j1_acceptance(projection):
    assert projection["j2"]["qualified_relational"] == []
    assert projection["j2"]["qualified_count"] == 0
    assert projection["j3"]["S0"] == "HOLD_J2_OWNER_RELATION_AND_EXECUTION_EVIDENCE"
    assert projection["j3"]["S1"] == "NOT_ACTIVATED"
    assert projection["j3"]["satisfaction_certified"] is False


def test_old_d1_effects_remain_separate_bounded_unknown(projection):
    old = projection["preexisting_d1_experiment"]
    assert old["accepted_effect_count"] == 4
    assert old["not_merged_into_new_world"] is True


def test_no_scored_nav_task_no_physical_or_production_authority(projection):
    assert projection["formal_primary_tasks"] is None
    assert projection["formal_b0_b4_scores"] is None
    assert projection["physical_architecture_selected"] is False
    assert projection["production_migration_authorized"] is False


def test_exact_owner_packet_drift_is_detected(monkeypatch):
    original = p.PROPOSAL.read_bytes()
    class Alternate:
        def read_bytes(self):
            return original + b"\\n"
    monkeypatch.setattr(p, "PROPOSAL", Alternate())
    with pytest.raises(ValueError, match="WORKTREE_DRIFT"):
        p.original_proposal()


def test_acceptance_binding_forgery_is_rejected_by_fixed_hash(monkeypatch):
    original = p.BINDING.read_bytes()
    class Alternate:
        def read_bytes(self):
            return original.replace(b"I ACCEPT. Proceed.", b"I REJECT. Proceed.")
    monkeypatch.setattr(p, "BINDING", Alternate())
    with pytest.raises(ValueError, match="BINDING_BYTES_DRIFT"):
        p.accepted_binding()


def test_activation_not_made_true_by_mutating_derived_projection(projection):
    tampered = deepcopy(projection)
    tampered["currentness"]["activation_status"] = "ACTIVATED"
    tampered["j3"]["satisfaction_certified"] = True
    assert tampered != p.build()
    assert p.build()["j3"]["satisfaction_certified"] is False


def test_existing_j1_projection_result_is_byte_stable(projection):
    expected = json.dumps(projection, sort_keys=True, ensure_ascii=False, indent=2) + "\n"
    assert p.OUTPUT.read_text("utf8") == expected


def test_initial_carrier_is_recovered_at_exact_git_commit_after_real_replacement():
    """An actual later source move does not erase original Git source evidence."""
    from tools.project_knowledge.adapters.schema import SchemaValidator
    from tools.project_knowledge.model import RawDeclaration
    from experiments.r0_p03_navigation_probe import (
        v03_real_pk_source_transition_v01 as transition,
    )

    original, current, source = transition.committed_carriers()
    assert source["initial_commit"] == transition.INITIAL_COMMIT
    assert source["replacement_commit"] == transition.REPLACEMENT_COMMIT
    assert original["world_id"] == current["world_id"] == p.EXPERIMENT_ID
    assert original["production_authority"] is current["production_authority"] is False
    assert original["source_owner_claim"]["natural_owner_relational_j2_qualified"] is False
    assert current["source_owner_claim"]["natural_owner_relational_j2_qualified"] is False
    assert original["governed_source"]["semantic_id"] == current["governed_source"]["semantic_id"]
    assert all(not SchemaValidator().validate(RawDeclaration(x["governed_source"]))
               for x in (original, current))
    assert original["real_ads_source"]["original_git_pin"] == (
        "5463b2ad2e6799339746637f38340fa2a9dc00f6"
    )
