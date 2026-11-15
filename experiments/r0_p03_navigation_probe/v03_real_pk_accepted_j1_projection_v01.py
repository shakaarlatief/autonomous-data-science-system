"""Exact owner-accepted P03-V2 G006/G013 experimental J1 projection.

This reader binds the explicitly observed conversational ACCEPT to a frozen
Git-published effect packet. It creates one J1-only experimental semantic state,
not a production amendment or an independently authenticated owner identity.

An accepted successor effect and an accepted lifecycle *rule* are not a
performed source revision. At initial state S0, S1 is DORMANT and any prospective
REPLACE/OPEN_RESET transition is NOT_ACTIVATED. Neither source existence nor
successful test definitions are a natural-owner J2 COVERS declaration. J3 stays
HOLD for both tracked requirements until adequate source-owner and executed
evidence exists. This separation is necessary before meaningful navigation
comparisons can legitimately share one semantic substrate.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PROPOSAL = HERE / "v03_real_pk_semantic_j1_owner_proposal_v01.json"
BINDING = HERE / "v03_real_pk_experiment_owner_acceptance_binding_v01.json"
OUTPUT = HERE / "v03_real_pk_accepted_j1_projection_result_v01.json"
PROPOSAL_COMMIT = "ed1c379f31fadc47a62189363720e0cfb9390afa"
PROPOSAL_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_semantic_j1_owner_proposal_v01.json"
PROPOSAL_GIT_SHA256 = "340ec577f6bbe2fca7f8739cc33788e878bff659cf6ef554745d60af7d3088b0"
PROPOSAL_CANONICAL_SHA256 = "0fa8ecc09f4745b514697d206356ce2f529fa66e15380a9bd0d43f1c6a00a6df"
BINDING_FILE_SHA256 = "2916a31085adef8dc21b598cd4d26f44f97c25ab264ae20c12f412782ee1e84f"
AUDIT_FILE_SHA256 = "59de22c2709d380189d60cab305902bff7033f9453cd5687223abe58805f56ac"
EXPERIMENT_ID = "P03V2_PKA_IDENTITY_AND_DERIVED_REFRESH_REAL_SOURCES_V01"
PROPOSAL_ID = "P03V2_PKA_REAL_SOURCE_TWO_STATE_EXPERIMENT_J1_001"

EXPECTED_IDS = (
    "P03PKA-E01-S0-IDENTITY-CONTINUITY",
    "P03PKA-E02-S1-IDENTITY-REFRESH",
    "P03PKA-E03-S1-REPLACE-OPEN-RESET",
    "P03PKA-E04-NO-PATH-OR-DERIVED-AUTHORITY",
)
EXPECTED_ACTIVE = (EXPECTED_IDS[0], EXPECTED_IDS[3])


def canonical_bytes(value: Any) -> bytes:
    """Encode an unordered JSON document using the frozen review convention."""
    return json.dumps(
        value, sort_keys=True, ensure_ascii=False, separators=(",", ":")
    ).encode("utf8")


def canonical_sha(value: Any) -> str:
    return sha256(canonical_bytes(value)).hexdigest()


def original_proposal() -> dict[str, Any]:
    """Verify frozen original Git blob, its payload hash and mutable-copy parity.

    Git integrity establishes exact packet contents, not the human reply.
    """
    result = subprocess.run(
        ["git", "show", f"{PROPOSAL_COMMIT}:{PROPOSAL_PATH}"],
        cwd=ROOT, capture_output=True, check=False,
    )
    if result.returncode or sha256(result.stdout).hexdigest() != PROPOSAL_GIT_SHA256:
        raise ValueError("EXACT_PKA_OWNER_PROPOSAL_GIT_BYTES_UNVERIFIED")
    if result.stdout != PROPOSAL.read_bytes():
        raise ValueError("EXACT_PKA_OWNER_PROPOSAL_WORKTREE_DRIFT")
    proposal = json.loads(result.stdout.decode("utf8"))
    content = {
        key: value for key, value in proposal.items()
        if key not in {"canonicalization", "canonical_payload_sha256"}
    }
    if (
        proposal["canonical_payload_sha256"] != PROPOSAL_CANONICAL_SHA256
        or canonical_sha(content) != PROPOSAL_CANONICAL_SHA256
        or proposal["proposal_id"] != PROPOSAL_ID
        or proposal["decision_state"] != "PROPOSED_NOT_OWNER_ACCEPTED"
        or proposal["world_candidate"] != EXPERIMENT_ID
        or tuple(x["id"] for x in proposal["new_effects"]) != EXPECTED_IDS
        or proposal["proposed_new_effect_count"] != 4
        or proposal["next_execution_boundaries"]["separate_exact_owner_acceptance_required"] is not True
    ):
        raise ValueError("EXACT_PKA_OWNER_PROPOSAL_EFFECT_OR_HASH_DRIFT")
    return proposal


def accepted_binding() -> dict[str, Any]:
    """Read the explicit chat-reported decision; no external identity proof."""
    data = BINDING.read_bytes()
    if sha256(data).hexdigest() != BINDING_FILE_SHA256:
        raise ValueError("P03_PKA_OWNER_REPLY_BINDING_BYTES_DRIFT")
    result = json.loads(data)
    if set(result) != {
        "schema_version", "binding_id", "proposal_id", "decision",
        "verbatim_owner_reply", "decision_date", "decision_provenance_class",
        "decision_context", "accepted_scope", "experimental_world_id",
        "source_proposal_commit", "source_proposal_path",
        "source_proposal_git_bytes_sha256", "source_proposal_canonical_payload_sha256",
        "source_audit_sha256", "accepted_effect_ids", "initial_active_effect_ids",
        "successor_activation", "accepted_j2_relations", "provenance_boundary",
        "excluded_authorizations",
    }:
        raise ValueError("P03_PKA_ACCEPTANCE_BINDING_SCHEMA_DRIFT")
    if (
        result["schema_version"] != 1
        or result["proposal_id"] != PROPOSAL_ID
        or result["experimental_world_id"] != EXPERIMENT_ID
        or result["decision"] != "ACCEPT"
        or result["verbatim_owner_reply"] != "I ACCEPT. Proceed."
        or result["decision_date"] != "2026-11-15"
        or result["decision_provenance_class"] !=
            "CHAT_CONVERSATION_EXPLICIT_OWNER_REPLY_NOT_INDEPENDENTLY_AUTHENTICATED"
        or result["source_proposal_commit"] != PROPOSAL_COMMIT
        or result["source_proposal_path"] != PROPOSAL_PATH
        or result["source_proposal_git_bytes_sha256"] != PROPOSAL_GIT_SHA256
        or result["source_proposal_canonical_payload_sha256"] != PROPOSAL_CANONICAL_SHA256
        or result["source_audit_sha256"] != AUDIT_FILE_SHA256
        or tuple(result["accepted_effect_ids"]) != EXPECTED_IDS
        or tuple(result["initial_active_effect_ids"]) != EXPECTED_ACTIVE
        or result["successor_activation"] !=
            "PENDING_ACTUAL_QUALIFIED_PROSPECTIVE_SOURCE_REVISION"
        or result["accepted_j2_relations"] != []
        or result["accepted_scope"] !=
            "FOUR_EXACT_PROSPECTIVE_EXPERIMENT_ONLY_PKA_EFFECTS_WITH_S1_DORMANT_UNTIL_REAL_SOURCE_REVISION"
    ):
        raise ValueError("P03_PKA_ACCEPTANCE_BINDING_AUTHORITY_OR_EFFECT_DRIFT")
    required_exclusions = {
        "PRODUCTION_J1_J2_ADMISSION", "NATURAL_OWNER_RELATIONAL_J2_QUALIFICATION",
        "SOURCE_OWNER_AUTHENTICATION_BY_OWNER_ACCEPTANCE",
        "S1_ACTIVATION_WITHOUT_REAL_SOURCE_REVISION",
        "RETROACTIVE_HISTORICAL_G006_G013_ACCEPTANCE_REWRITE",
        "J3_REQUIREMENT_SATISFACTION_INFERENCE", "FORMAL_P03_PRIMARY_TASK_OR_GOLD_CREATION",
        "FORMAL_B0_B4_COMPARATOR_SCORING", "PHYSICAL_ARCHITECTURE_SELECTION",
        "MIGRATION_OR_CUTOVER", "PRODUCTION_SOURCE_MODIFICATION",
    }
    if set(result["excluded_authorizations"]) != required_exclusions:
        raise ValueError("P03_PKA_ACCEPTANCE_EXCLUSION_DRIFT")
    return result


def build() -> dict[str, Any]:
    """Materialize J1-only common semantic inputs with explicit S0 currentness."""
    packet = original_proposal()
    binding = accepted_binding()
    effects = packet["new_effects"]
    if (
        [effect["type"] for effect in effects] !=
        ["REQUIRE", "REQUIRE", "LIFECYCLE", "PROHIBIT"]
        or [effect["accounting"] for effect in effects] !=
        ["REALIZATION_TRACKED", "REALIZATION_TRACKED",
         "NO_REALIZATION_REQUIRED", "NO_REALIZATION_REQUIRED"]
        or effects[2]["lineage"] != {
            "predecessor_id": EXPECTED_IDS[0],
            "successor_id": EXPECTED_IDS[1],
            "relation": "REPLACE",
            "realization_succession": "OPEN_RESET",
            "transition_not_activated_by_this_proposal": True,
        }
    ):
        raise ValueError("P03_PKA_ACCEPTED_EFFECT_TYPES_OR_LINEAGE_CHANGED")
    return {
        "schema_version": 1,
        "world_id": EXPERIMENT_ID,
        "scope": "EXPERIMENT_ONLY_NON_OPERATIONAL",
        "world_status": "J1_ACCEPTED_S0_ACTIVE_S1_DORMANT_J2_AND_J3_UNQUALIFIED",
        "exact_accepted_proposal": {
            "commit": PROPOSAL_COMMIT,
            "source_path": PROPOSAL_PATH,
            "git_bytes_sha256": PROPOSAL_GIT_SHA256,
            "canonical_payload_sha256": PROPOSAL_CANONICAL_SHA256,
        },
        "owner_decision": {
            "verdict": binding["decision"],
            "verbatim_reply": binding["verbatim_owner_reply"],
            "provenance": binding["decision_provenance_class"],
            "binding_file_sha256": BINDING_FILE_SHA256,
            "independently_cryptographically_authenticated": False,
        },
        "accepted_j1": {
            "effects": effects,
            "count": 4,
            "current_effect_ids": list(EXPECTED_ACTIVE),
            "dormant_until_source_revision": [EXPECTED_IDS[1]],
            "lifecycle_effect_id": EXPECTED_IDS[2],
            "accounting_tracked_requirements": [EXPECTED_IDS[0], EXPECTED_IDS[1]],
        },
        "currentness": {
            "current_state": "S0_INITIAL",
            "successor_state": "S1_SUCCESSOR_AFTER_REAL_SOURCE_REVISION",
            "activation_status": "NOT_ACTIVATED",
            "accepted_transition_rule": effects[2]["lineage"],
            "on_future_qualified_activation": {
                "retired_current_requirement": EXPECTED_IDS[0],
                "new_current_requirement": EXPECTED_IDS[1],
                "realization_successor_initialization": "OPEN_RESET",
                "evidence_carryover_allowed": False,
            },
            "actual_source_revision_qualified": False,
        },
        "j2": {
            "qualified_relational": [],
            "qualified_count": 0,
            "candidate_source_owner_statements": [],
            "source_observations_do_not_imply_covers": True,
        },
        "j3": {
            "S0": "HOLD_J2_OWNER_RELATION_AND_EXECUTION_EVIDENCE",
            "S1": "NOT_ACTIVATED",
            "satisfaction_certified": False,
        },
        "preexisting_d1_experiment": {
            "accepted_effect_count": packet["existing_d1_experiment_effect_count"],
            "source_world": "SEPARATE_HISTORICAL_D1_HOLD",
            "not_merged_into_new_world": True,
        },
        "formal_primary_tasks": None,
        "formal_b0_b4_scores": None,
        "physical_architecture_selected": False,
        "production_migration_authorized": False,
    }


def main() -> None:
    result = build()
    content = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("P03_PKA_ACCEPTED_J1_PROJECTION_IMMUTABILITY_VIOLATION")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(content)
    print(json.dumps({
        "status": result["world_status"],
        "accepted_j1": result["accepted_j1"]["count"],
        "active_j1": result["accepted_j1"]["current_effect_ids"],
        "accepted_j2": result["j2"]["qualified_count"],
        "new_j3_certified": result["j3"]["satisfaction_certified"],
        "formal_p03_score": result["formal_b0_b4_scores"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
