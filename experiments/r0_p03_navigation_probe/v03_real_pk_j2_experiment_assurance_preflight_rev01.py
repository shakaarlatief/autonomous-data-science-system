"""Bounded predecision admission analysis for R0-P03 experiment-only J2.

This is a source-bound, adversarial policy PROPOSAL check. The only owner
decision in the known record is acceptance of the earlier exact four J1
effects. A future source-owner J2 assurance policy is neither accepted nor
activated by this implementation or a matching proposal hash.

The preflight replays accepted J1 and the actual Checkpoint-948 source event,
then verifies that the proposed weak actor-provenance boundary cannot be
promoted into independent model authentication, governing J2 or J3.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as j1,
    v03_real_pk_prospective_j2_source_assay_v01 as event,
)

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "v03_real_pk_j2_experiment_assurance_owner_proposal_rev01.json"
OUTPUT = HERE / "v03_real_pk_j2_experiment_assurance_preflight_result_rev01.json"
SOURCE_SHA256 = "f0217d8c24aba8aa5a5d493d6c816f9e439de4e32f32c00d56665b075ead798f"
EVENT_SHA = "faf8ff2686c6b09f53d3569470cf2057c11e5971"
EVENT_RECEIPT_SHA256 = "b64569b802f5d9d6de2e6d975ba8a3e462698ba696752afe0392c4abd0f565ac"
PROPOSAL = "P03V2_EXPERIMENT_SOURCE_OWNER_RELATIONAL_J2_ASSURANCE_POLICY_REV01"
EXPECTED_AUTHORITY = {
    "accepted_by_owner": False,
    "eligible_to_admit_j2_now": False,
    "qualified_relational_j2": 0,
    "s1_activated": False,
    "j3_certified": False,
    "formal_r0_p03_completed": False,
    "physical_architecture_selected": False,
    "production_authority_changed": False,
}
EXPECTED_SOURCE_CONTEXT = {
    "world_id": j1.EXPERIMENT_ID,
    "accepted_j1_effect_id": j1.EXPECTED_IDS[1],
    "accepted_j1_proposal_id": "P03V2_PKA_REAL_SOURCE_TWO_STATE_EXPERIMENT_J1_001",
    "accepted_j1_proposal_digest": "0fa8ecc09f4745b514697d206356ce2f529fa66e15380a9bd0d43f1c6a00a6df",
    "required_components": [
        "EXPLICIT_IDENTITY_PRESERVING_MOVE",
        "AFFECTED_VIEW_REFRESH_SELECTED",
        "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
        "STALE_DERIVED_RESULT_NOT_GOVERNING",
    ],
    "original_948_source_event": EVENT_SHA,
    "original_948_result_digest": EVENT_RECEIPT_SHA256,
    "original_948_qualified_relational_j2": 0,
    "original_948_s1_activated": False,
    "original_948_j3": "HOLD",
}

REQUIRED_CONTROLS = (
    "FUTURE_EVENT_PUBLISHED_AFTER_POLICY_ACCEPTANCE_AND_SOURCE_SCOPE_FREEZE",
    "EXACT_GIT_PARENT_SOURCE_REVISIONS_AND_CHANGED_PATHS_INDEPENDENTLY_VERIFIED",
    "SINGLE_NATURAL_OWNER_CARRIER_FOR_EACH_FACT_TUPLE_NO_CONTRADICTORY_DUPLICATES",
    "SOURCE_AUTHOR_REALIZER_SCOPE_NAMED_PRIOR_TO_EVENT_AND_NOT_INFERRED_FROM_GIT_AUTHOR",
    "SCOPED_AUTHOR_CONTROLS_EXACT_EXECUTABLE_EXPERIMENT_REALIZER_NOT_JUST_NARRATIVE_SOURCE",
    "COVERAGE_BOUND_TO_COMPOSITE_REALIZER_NOT_HISTORICAL_G006_G013_IMPLEMENTATION_AUTHORSHIP",
    "CONTEMPORANEOUS_AUTHOR_DECLARES_REALIZER_INTENT_AND_EXACT_ACCEPTED_J1_COMPONENT_BINDING",
    "POSTEXECUTION_COVERS_DECLARATION_BY_SAME_SCOPED_SOURCE_AUTHOR_NOT_BACKDATED",
    "ACTUAL_PRODUCTION_G006_AND_G013_G009_ON_EXACT_NEW_SOURCE_REVISION",
    "PARTIAL_COVERAGE_ALLOWED_AS_EVIDENCE_BUT_ALL_REQUIRED_FOR_J3_COMPLETION",
    "EXECUTION_EVIDENCE_SOURCE_REVISION_PINNED_AND_SEPARATE_FROM_RELATIONAL_DECLARATION",
    "NO_PREDECESSOR_S0_EVIDENCE_CARRIED_AS_S1_J3_PASS",
    "FALSE_AUTHORITY_AND_UNKNOWN_CASES_MECHANICALLY_REJECTED",
    "INDEPENDENT_SEPARATE_J3_EVALUATOR_WITH_EXACT_ADMITTED_J1_AND_J2",
    "SOURCE_RELATIVE_REFERENCE_TRUTH_EXPOSES_WEAK_ASSURANCE_TO_ALL_B0_B4_ARMS",
)
FORBIDDEN = (
    "INDEPENDENT_MODEL_SESSION_ACTOR_AUTHENTICATION",
    "PRODUCTION_NATURAL_OWNER_COVERS",
    "HISTORICAL_G006_G013_IMPLEMENTATION_AUTHORSHIP",
    "CRYPTOGRAPHIC_GOVERNING_J1_ACCEPTANCE",
    "RETROACTIVE_948_J2_CERTIFICATION",
    "PROVIDER_NATIVE_EPHEMERAL_RECEIPT_AUTHENTICATION",
    "NEW_EFFECT_OR_CHANGE_TO_ACCEPTED_J1_COMPONENTS",
    "S1_ACTIVATION_FROM_SOURCE_CLAIM_ALONE",
    "J3_SATISFIED_FROM_SOURCE_CLAIM_ALONE",
    "FORMAL_B0_B4_SCORING_OR_ARCHITECTURE_SELECTION",
    "MIGRATION_OR_PRODUCTION_AUTHORITY_CHANGE",
)
EXPECTED_DECISION_CHOICES = {"ACCEPT", "AMEND", "REJECT"}
EXPECTED_QUALIFIERS = {
    "author_self_claim_cannot_self_admit": True,
    "source_hash_is_not_independent_actor_authentication": True,
    "structurally_valid_claim_can_still_fail_owner_assurance": True,
    "prior_source_result_stays_hold": True,
    "no_registered_authenticated_source_adapter_in_this_proposal": True,
    "formal_primary_and_legacy_reference_guards_unchanged": True,
}


def load_source() -> dict[str, Any]:
    """Return only the original frozen candidate, never a caller-supplied rule."""
    raw = SOURCE.read_bytes()
    if sha256(raw).hexdigest() != SOURCE_SHA256:
        raise ValueError("P03_J2_OWNER_POLICY_PROPOSAL_SOURCE_DRIFT")
    data = json.loads(raw.decode("utf8"))
    validate_candidate(data)
    return data


def validate_candidate(data: dict[str, Any]) -> None:
    """Reject authority promotion, retrospective effect and missing controls."""
    if not isinstance(data, dict) or set(data) != {
        "schema_version", "proposal_id", "decision_state", "decision_kind",
        "source_head_preparation", "source_context", "candidate_policy",
        "decision_choices", "independence_and_falsification", "authority",
    }:
        raise ValueError("P03_J2_POLICY_CLOSED_OUTER_SCHEMA")
    if (
        data["schema_version"] != 1
        or data["proposal_id"] != PROPOSAL
        or data["decision_state"] != "PROPOSED_NOT_OWNER_ACCEPTED"
        or data["decision_kind"] != "EXPERIMENT_ONLY_NATURAL_SOURCE_OWNER_ASSURANCE_INTERPRETATION"
        or data["source_head_preparation"] != "488a437fa2a8957a01a8c6fa053109a15bd13046"
        or data["source_context"] != EXPECTED_SOURCE_CONTEXT
        or data["authority"] != EXPECTED_AUTHORITY
    ):
        raise ValueError("P03_J2_POLICY_ACCEPTANCE_OR_SOURCE_AUTHORITY_FALSIFIED")
    p = data["candidate_policy"]
    if not isinstance(p, dict) or set(p) != {
        "policy_state", "duration", "effective_rule", "source_author_scope",
        "owner_delegation_method", "owner_authenticity_class",
        "source_author_authenticity_class", "relationship_class_if_qualified",
        "independent_strong_natural_owner_authentication_claimed",
        "technical_requirements", "non_delegable_claims",
        "automatic_qualification_if_owner_accepts",
        "new_source_event_required_after_owner_acceptance",
        "j3_re_evaluation_required", "full_r0_p03_method_unchanged",
    }:
        raise ValueError("P03_J2_POLICY_CLOSED_INNER_SCHEMA")
    if (
        p["policy_state"] != "INACTIVE_UNTIL_SEPARATE_EXACT_OWNER_DECISION"
        or p["duration"] != "ONE_PROSPECTIVE_BOUNDED_EXPERIMENTAL_SOURCE_EVENT"
        or p["effective_rule"] != "FORWARD_ONLY_FROM_ACCEPTED_POLICY_NO_RETROSPECTIVE_J2_PROMOTION"
        or p["source_author_scope"] !=
            "EXPOSED_EXPERIMENT_CARRIER_AUTHOR_ONLY_NOT_HISTORICAL_G006_G013_CODE_OWNER"
        or p["owner_delegation_method"] != "EXACT_RECORDED_CHAT_OWNER_ACCEPTANCE_OF_FROZEN_PACKET"
        or p["owner_authenticity_class"] !=
            "RECORDED_CHAT_OWNER_CONFIRMATION_NOT_INDEPENDENTLY_VERIFIABLE"
        or p["source_author_authenticity_class"] !=
            "EXPOSED_SESSION_AND_GIT_PROVENANCE_NOT_INDEPENDENTLY_AUTHENTICATED"
        or p["relationship_class_if_qualified"] !=
            "EXPERIMENT_ONLY_SOURCE_RELATIVE_RELATIONAL_J2_WITH_DECLARED_WEAK_ACTOR_ASSURANCE"
        or p["independent_strong_natural_owner_authentication_claimed"] is not False
        or p["automatic_qualification_if_owner_accepts"] is not False
        or p["new_source_event_required_after_owner_acceptance"] is not True
        or p["j3_re_evaluation_required"] is not True
        or p["full_r0_p03_method_unchanged"] is not True
        or tuple(p["technical_requirements"]) != REQUIRED_CONTROLS
        or tuple(p["non_delegable_claims"]) != FORBIDDEN
    ):
        raise ValueError("P03_J2_POLICY_ASSURANCE_OR_TEMPORAL_GATE_FALSIFIED")
    decisions = data["decision_choices"]
    if (
        not isinstance(decisions, dict)
        or set(decisions) != EXPECTED_DECISION_CHOICES
        or any(not isinstance(v, str) or len(v) < 40 for v in decisions.values())
        or "prospective" not in decisions["ACCEPT"]
        or "new" not in decisions["AMEND"]
        or "HOLD" not in decisions["REJECT"]
        or data["independence_and_falsification"] != EXPECTED_QUALIFIERS
    ):
        raise ValueError("P03_J2_POLICY_DECISION_AND_FALSIFIER_GATE_INVALID")


def build() -> dict[str, Any]:
    """Compare the proposed policy with immutable accepted J1 and a real HOLD."""
    proposal = load_source()
    accepted = j1.build()
    earlier = event.evaluate(EVENT_SHA)
    receipt_raw = event.OUTPUT.read_bytes()
    if sha256(receipt_raw).hexdigest() != EVENT_RECEIPT_SHA256:
        raise ValueError("P03_J2_POLICY_PREDECESSOR_EVIDENCE_DIGEST_DRIFT")
    if json.loads(receipt_raw.decode("utf8")) != earlier:
        raise ValueError("P03_J2_POLICY_PREDECESSOR_EVIDENCE_REPLAY_DRIFT")
    if (
        accepted["accepted_j1"]["effects"][1]["id"] != EXPECTED_SOURCE_CONTEXT["accepted_j1_effect_id"]
        or accepted["accepted_j1"]["effects"][1]["completion_contract"]["required_components"]
            != EXPECTED_SOURCE_CONTEXT["required_components"]
        or accepted["currentness"]["activation_status"] != "NOT_ACTIVATED"
        or accepted["j2"]["qualified_count"] != 0
        or earlier["claimed_relational_J2_qualified"] is not False
        or earlier["S1_activated"] is not False
        or earlier["component_execution_verified_for_this_transition"] is not False
        or not earlier["J3"].startswith("HOLD_")
    ):
        raise ValueError("P03_J2_POLICY_SOURCE_WORLD_ALREADY_PROMOTED")
    return {
        "schema_version": 1,
        "proposal_id": proposal["proposal_id"],
        "proposal_sha256": SOURCE_SHA256,
        "proposal_state": "PROPOSED_NOT_OWNER_ACCEPTED",
        "proposal_scope": "ONE_FUTURE_SOURCE_EVENT_EXPERIMENT_ONLY",
        "prior_event_commit": EVENT_SHA,
        "prior_event_git_structural_result": "PASS",
        "prior_event_nat_owner_authentication": "NOT_INDEPENDENTLY_VERIFIED",
        "prior_event_j2": "HOLD",
        "prior_event_s1": "NOT_ACTIVATED",
        "prior_event_j3": "HOLD",
        "eligible_to_admit_existing_j2": False,
        "auto_qualify_future_j2_if_policy_accepted": False,
        "strong_actor_authentication_satisfied": False,
        "future_policy_decision_required": True,
        "future_source_revision_and_real_execution_required": True,
        "owner_decision": "NOT_RECEIVED",
        "formal_r0_p03": "INCOMPLETE",
        "physical_architecture_selected": False,
        "production_authority_changed": False,
    }


def main() -> None:
    result = build()
    rendered = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != rendered:
            raise RuntimeError("P03_J2_POLICY_PREFLIGHT_IMMUTABLE_RESULT_MISMATCH")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as f:
            f.write(rendered)
    print(json.dumps({
        "proposal": result["proposal_state"],
        "previous_J2": result["prior_event_j2"],
        "owner_decision": result["owner_decision"],
        "S1": result["prior_event_s1"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
