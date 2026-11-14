"""Exact, non-operational R0-P03-V2 candidate J1 packet for human review.

An accepted *method* (Research 673) and accepted historical D1 experiment
effects (Research 676) do not accept any new requirements for the G006/G013
Project Knowledge source candidate. The four effects proposed here are new,
prospective experiment-only semantics. They are not retroactive descriptions
of G006/G013 gate acceptance or a production Specification 028 amendment.

Even if a future user explicitly accepts this packet, a separate owner-decision
binding and actual source-owner J2 qualification are required. Neither this
module nor arbitrary JSON claiming "accepted" can create authority.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_semantic_candidate_audit_v01 as audit,
)

ROOT = Path(__file__).resolve().parents[2]
SOURCE = audit.OUTPUT
SOURCE_SHA256 = "59de22c2709d380189d60cab305902bff7033f9453cd5687223abe58805f56ac"
OUTPUT = Path(__file__).with_name("v03_real_pk_semantic_j1_owner_proposal_v01.json")
PROPOSAL_ID = "P03V2_PKA_REAL_SOURCE_TWO_STATE_EXPERIMENT_J1_001"
S0 = "P03PKA-E01-S0-IDENTITY-CONTINUITY"
S1 = "P03PKA-E02-S1-IDENTITY-REFRESH"
LIFECYCLE = "P03PKA-E03-S1-REPLACE-OPEN-RESET"
PROHIBIT = "P03PKA-E04-NO-PATH-OR-DERIVED-AUTHORITY"


def canonical_sha(value: Any) -> str:
    return sha256(
        json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf8")
    ).hexdigest()


def build() -> dict[str, Any]:
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError("PKA_PROPOSAL_SOURCE_AUDIT_BYTES_DRIFT")
    original = audit.evaluate()
    if original != json.loads(SOURCE.read_text("utf8")):
        raise ValueError("PKA_PROPOSAL_AUDIT_NOT_REGENERABLE")
    if (
        original["combined_unique_source_paths"] != 19
        or original["new_experiment_only_j1_effects_accepted"] != 0
        or original["new_qualified_j2_relations"] != 0
    ):
        raise ValueError("PKA_PROPOSAL_SOURCE_AND_AUTHORITY_SCOPE_DRIFT")

    effects = [
        {
            "id": S0,
            "state": "S0_INITIAL",
            "type": "REQUIRE",
            "accounting": "REALIZATION_TRACKED",
            "statement": (
                "In the bounded P03 experimental source world, a move or representation "
                "replacement of an authored canonical source carrier must preserve its "
                "semantic identity and retain its historical carrier in lookup."
            ),
            "completion_contract": {
                "composition": "ALL_REQUIRED",
                "required_components": [
                    "EXPLICIT_IDENTITY_PRESERVING_MOVE",
                    "HISTORICAL_CARRIER_REMAINS_RESOLVABLE",
                ],
                "actual_natural_owner_covers_required": True,
                "exact_source_revision_and_executed_evidence_required": True,
            },
        },
        {
            "id": S1,
            "state": "S1_SUCCESSOR_AFTER_REAL_SOURCE_REVISION",
            "type": "REQUIRE",
            "accounting": "REALIZATION_TRACKED",
            "statement": (
                "In the bounded P03 successor experimental state, the same authored "
                "semantic identity must survive a real source carrier move; affected "
                "derived views must be rebuilt from the complete current source snapshot "
                "and any incremental refresh must be equivalent to the full current build. "
                "A stale prior generated manifest must never govern current semantics."
            ),
            "completion_contract": {
                "composition": "ALL_REQUIRED",
                "required_components": [
                    "EXPLICIT_IDENTITY_PRESERVING_MOVE",
                    "AFFECTED_VIEW_REFRESH_SELECTED",
                    "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD",
                    "STALE_DERIVED_RESULT_NOT_GOVERNING",
                ],
                "actual_natural_owner_covers_required": True,
                "exact_source_revision_and_executed_evidence_required": True,
            },
        },
        {
            "id": LIFECYCLE,
            "state": "S1_SUCCESSOR_AFTER_REAL_SOURCE_REVISION",
            "type": "LIFECYCLE",
            "accounting": "NO_REALIZATION_REQUIRED",
            "statement": (
                "When the separately qualified prospective P03 source-revision transition "
                "activates S1, S1 REPLACES S0 as the current experimental requirement, "
                "with OPEN_RESET realization succession; S0 implementation evidence "
                "cannot be carried forward as sufficient for S1 without requalification."
            ),
            "lineage": {
                "predecessor_id": S0,
                "successor_id": S1,
                "relation": "REPLACE",
                "realization_succession": "OPEN_RESET",
                "transition_not_activated_by_this_proposal": True,
            },
        },
        {
            "id": PROHIBIT,
            "state": "BOTH",
            "type": "PROHIBIT",
            "accounting": "NO_REALIZATION_REQUIRED",
            "statement": (
                "Neither a carrier path nor a generated navigation/index/manifest output "
                "may be treated as governing semantic identity or acceptance authority."
            ),
            "standing_check": "DETECTIVE_ONLY_FALSE_AUTHORITY_REJECTION",
        },
    ]
    payload = {
        "schema_version": 1,
        "proposal_id": PROPOSAL_ID,
        "world_candidate": audit.CANDIDATE_ID,
        "decision_kind": "EXPERIMENT_ONLY_SEMANTIC_EFFECT_SCOPE",
        "decision_state": "PROPOSED_NOT_OWNER_ACCEPTED",
        "source_audit_sha256": SOURCE_SHA256,
        "source_pin": audit.PIN,
        "new_effects": effects,
        "proposed_new_effect_count": 4,
        "existing_d1_experiment_effect_count": 4,
        "source_role": "EXPOSED_PROPOSAL_NOT_GOVERNING_SOURCE",
        "effect_timeline": {
            "S0": [S0, PROHIBIT],
            "S1": [S1, PROHIBIT],
            "transition_requires_real_prospective_source_revision": True,
            "historical_g006_g013_git_chronology_is_not_new_effect_lineage": True,
        },
        "next_execution_boundaries": {
            "separate_exact_owner_acceptance_required": True,
            "actual_source_owner_j2_declaration_required": True,
            "j2_declaration_not_provided_by_owner_acceptance": True,
            "no_model_identity_or_connector_proof_assumed": True,
            "qualified_executed_test_evidence_required": True,
            "j3_predicate_must_be_evaluated_not_author_reported": True,
            "preexisting_d1_cannot_attest_kept_as_unknown_periphery": True,
            "formal_sixty_twenty_or_three_to_one_corpus_not_frozen": True,
            "formal_twelve_tasks_and_legacy_nine_unoriginated": True,
            "production_specification_028_unchanged": True,
            "physical_architecture_selection_authorized": False,
            "migration_authorized": False,
        },
    }
    packet = {
        **payload,
        "canonicalization": "UTF8_JSON_SORTED_KEYS_COMPACT_NO_EXTRA_WHITESPACE",
        "canonical_payload_sha256": canonical_sha(payload),
    }
    return packet


def require_admission(candidate: dict, *, claim: dict | None = None) -> None:
    """No self-authentication, even if caller writes a fabricated owner reply."""
    # Admission is deliberately unavailable. Compare an incoming claim with
    # the staged exact review packet before rejecting it, but do not rebuild
    # the expensive original Git source frame for every negative inquiry.
    # Full original-Git regeneration happens separately in build()/tests.
    if candidate != json.loads(OUTPUT.read_text("utf8")):
        raise ValueError("PKA_PROPOSAL_NOT_EXACT_PINNED_PACKET")
    if claim is None:
        raise ValueError("PKA_EXPERIMENT_J1_NOT_EXPLICITLY_OWNER_ACCEPTED")
    raise ValueError("PKA_EXPERIMENT_J1_OWNER_BINDING_NOT_IMPLEMENTED")


def main() -> None:
    packet = build()
    text = json.dumps(packet, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != text:
            raise RuntimeError("PKA_OWNER_PROPOSAL_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as handle:
            handle.write(text)
    print(json.dumps({
        "proposal_id": PROPOSAL_ID,
        "canonical_payload_sha256": packet["canonical_payload_sha256"],
        "proposed_new_j1": len(packet["new_effects"]),
        "actually_accepted_new_j1": 0,
        "actual_j2": 0,
        "status": packet["decision_state"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
