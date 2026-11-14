"""P03-V2 exact new J1 effects packet is a proposal, never an admission."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_semantic_j1_owner_proposal_v01 as packet,
)


@pytest.fixture(scope="module")
def proposal():
    return packet.build()


def test_review_scope_is_exact_and_not_owner_accepted(proposal):
    assert proposal["proposal_id"] == packet.PROPOSAL_ID
    assert proposal["decision_state"] == "PROPOSED_NOT_OWNER_ACCEPTED"
    assert proposal["decision_kind"] == "EXPERIMENT_ONLY_SEMANTIC_EFFECT_SCOPE"
    assert proposal["source_role"] == "EXPOSED_PROPOSAL_NOT_GOVERNING_SOURCE"


def test_source_packet_is_bound_to_real_source_audit(proposal):
    assert proposal["source_audit_sha256"] == packet.SOURCE_SHA256
    assert sha256(packet.SOURCE.read_bytes()).hexdigest() == packet.SOURCE_SHA256
    assert proposal["source_pin"] == packet.audit.PIN
    assert proposal["world_candidate"] == packet.audit.CANDIDATE_ID


def test_four_exact_new_effect_ids_and_accounting(proposal):
    effects = proposal["new_effects"]
    assert len(effects) == proposal["proposed_new_effect_count"] == 4
    assert [e["id"] for e in effects] == [
        packet.S0, packet.S1, packet.LIFECYCLE, packet.PROHIBIT
    ]
    assert [e["type"] for e in effects] == [
        "REQUIRE", "REQUIRE", "LIFECYCLE", "PROHIBIT"
    ]
    assert [e["accounting"] for e in effects] == [
        "REALIZATION_TRACKED", "REALIZATION_TRACKED",
        "NO_REALIZATION_REQUIRED", "NO_REALIZATION_REQUIRED",
    ]


def test_genuine_implementation_owner_relations_required_not_assumed(proposal):
    for effect in proposal["new_effects"][:2]:
        contract = effect["completion_contract"]
        assert contract["composition"] == "ALL_REQUIRED"
        assert contract["actual_natural_owner_covers_required"] is True
        assert contract["exact_source_revision_and_executed_evidence_required"] is True
        assert len(contract["required_components"]) >= 2


def test_s0_and_s1_requirements_do_not_retroactively_reclassify_git_history(proposal):
    states = proposal["effect_timeline"]
    assert states["S0"] == [packet.S0, packet.PROHIBIT]
    assert states["S1"] == [packet.S1, packet.PROHIBIT]
    assert states["historical_g006_g013_git_chronology_is_not_new_effect_lineage"] is True
    assert states["transition_requires_real_prospective_source_revision"] is True


def test_s1_explicitly_replaces_s0_with_open_reset_not_carried_evidence(proposal):
    lineage = proposal["new_effects"][2]["lineage"]
    assert lineage == {
        "predecessor_id": packet.S0,
        "successor_id": packet.S1,
        "relation": "REPLACE",
        "realization_succession": "OPEN_RESET",
        "transition_not_activated_by_this_proposal": True,
    }


def test_derived_index_or_path_cannot_become_semantic_authority(proposal):
    text = proposal["new_effects"][3]["statement"]
    assert "carrier path" in text
    assert "generated navigation/index/manifest" in text
    assert "governing semantic identity" in text
    assert proposal["new_effects"][3]["standing_check"] == "DETECTIVE_ONLY_FALSE_AUTHORITY_REJECTION"


def test_four_original_d1_effects_remain_separate_not_new_j1(proposal):
    assert proposal["existing_d1_experiment_effect_count"] == 4
    assert proposal["proposed_new_effect_count"] == 4
    assert proposal["decision_state"] != "ACCEPTED"


@pytest.mark.parametrize("key", [
    "separate_exact_owner_acceptance_required",
    "actual_source_owner_j2_declaration_required",
    "j2_declaration_not_provided_by_owner_acceptance",
    "no_model_identity_or_connector_proof_assumed",
    "qualified_executed_test_evidence_required",
    "j3_predicate_must_be_evaluated_not_author_reported",
    "preexisting_d1_cannot_attest_kept_as_unknown_periphery",
    "formal_sixty_twenty_or_three_to_one_corpus_not_frozen",
    "formal_twelve_tasks_and_legacy_nine_unoriginated",
    "production_specification_028_unchanged",
])
def test_all_necessary_admission_and_method_boundaries_explicit(proposal, key):
    assert proposal["next_execution_boundaries"][key] is True


def test_no_production_authority_or_migration_approved(proposal):
    assert proposal["next_execution_boundaries"]["physical_architecture_selection_authorized"] is False
    assert proposal["next_execution_boundaries"]["migration_authorized"] is False


def test_canonical_payload_sha_is_exact_source_bound_and_stable(proposal):
    data = {k: v for k, v in proposal.items()
            if k not in ("canonical_payload_sha256", "canonicalization")}
    assert packet.canonical_sha(data) == proposal["canonical_payload_sha256"]
    assert proposal["canonical_payload_sha256"] == (
        "0fa8ecc09f4745b514697d206356ce2f529fa66e15380a9bd0d43f1c6a00a6df"
    )


def test_absent_owner_confirmation_fails_closed(proposal):
    with pytest.raises(ValueError, match="PKA_EXPERIMENT_J1_NOT_EXPLICITLY_OWNER_ACCEPTED"):
        packet.require_admission(proposal)


def test_forged_owner_acceptance_dictionary_fails_closed(proposal):
    with pytest.raises(ValueError, match="PKA_EXPERIMENT_J1_OWNER_BINDING_NOT_IMPLEMENTED"):
        packet.require_admission(
            proposal, claim={"owner_reply": "I ACCEPT", "governing": True}
        )


@pytest.mark.parametrize("mutation", [
    ("decision_state", "ACCEPTED"),
    ("source_pin", "f" * 40),
    ("source_role", "PRODUCTION_J1"),
    ("proposed_new_effect_count", 5),
])
def test_mutated_payload_cannot_be_self_admitted(proposal, mutation):
    copy = deepcopy(proposal)
    copy[mutation[0]] = mutation[1]
    with pytest.raises(ValueError, match="PKA_PROPOSAL_NOT_EXACT_PINNED_PACKET"):
        packet.require_admission(copy, claim={"owner_reply": "I ACCEPT"})


def test_extra_fabricated_effect_cannot_be_self_admitted(proposal):
    copy = deepcopy(proposal)
    copy["new_effects"].append({"id": "FAKE", "type": "REQUIRE"})
    with pytest.raises(ValueError, match="PKA_PROPOSAL_NOT_EXACT_PINNED_PACKET"):
        packet.require_admission(copy)


def test_immutable_proposal_output_matches_verified_source(proposal):
    assert json.loads(packet.OUTPUT.read_text("utf8")) == proposal


def test_source_audit_and_proposed_packet_exact_lf_checkout_contract(proposal):
    """Exact source-pinned bytes must not change through Windows CRLF checkout."""
    import subprocess

    for p in (packet.SOURCE, packet.OUTPUT):
        relative = p.relative_to(packet.ROOT).as_posix()
        attr = subprocess.check_output(
            ["git", "check-attr", "text", "--", relative],
            cwd=packet.ROOT, text=True, encoding="utf8",
        ).strip()
        assert attr == f"{relative}: text: unset"
        assert b"\r\n" not in p.read_bytes()
    assert sha256(packet.SOURCE.read_bytes()).hexdigest() == packet.SOURCE_SHA256
