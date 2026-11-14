"""Read-only, exact-binding projection of owner-accepted P03-V2 D1 replay effects.

The owner explicitly accepted the complete P03 experimental reuse packet in the
ChatGPT conversation. This module records that *chat-reported* decision using a
new bound record; it does not and cannot independently authenticate the human
account, produce a detached J1 signature or give that decision production force.

Critical evidence separation:
  J1: four previously reviewed D1 effect statements become EXPERIMENT-ONLY J1
      inputs for the new P03-V2 world, without changing any original source.
  J2 OBSERVABLE: a true Git parent and changed path are verified in original
      Git objects. This is real historical source evidence.
  J2 SOURCE-REPORTED: Claude's connector transport claim is not externally
      provider-verified by the Git object.
  J2 RELATIONAL: no new natural-owner coverage declaration is qualified.
  J3: old D1 results are a labelled non-governing preview only. New J3
      satisfaction is held pending a real J2 relational/qualification contract.

No primary questions, protected gold, B0-B4 scores, real J1 credentials,
physical target, migration or production authority are created here.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_d1_real_event_admission_contract_v01 as original,
)

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
ACCEPTANCE_PATH = BASE / "v03_d1_experiment_owner_acceptance_binding_v01.json"
PROJECTION_PATH = BASE / "v03_d1_experiment_accepted_j1_projection_v01.json"

REVIEW_COMMIT = "ff8bf4c4c504a17f5b26db630f83920d727ff51c"
REVIEW_FILE = "experiments/r0_p03_navigation_probe/v03_d1_real_event_owner_proposal_v01.json"
REVIEW_GIT_SHA256 = "d9220667ddb60d89d12259ee553c0c3666e0d37329723360e00be311299baddd"
REVIEW_CANONICAL_SHA256 = "186c70ff487104f8ee5baee8d21b50ffd466e812c6b97debb20296c8bbf9451f"
BINDING_CANONICAL_SHA256 = "95f99ba0f62f35408b4086d7ee0dd666be43b81a8d6ff69cad5d653b904cd9af"

EXPECTED_EFFECT_IDS = (
    "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT",
    "D1-E02-NO-CLAUDE-RUNTIME-BRIDGE",
    "D1-E03-MESSAGE018-AUTHORIZATION",
    "D1-E04-TRANSPORT-CORRECTION-LIFECYCLE",
)

EXPECTED_EXCLUSIONS = (
    "PRODUCTION_J1_J2_ADMISSION",
    "NATURAL_OWNER_RELATIONAL_J2_QUALIFICATION",
    "INDEPENDENT_PROVIDER_CONNECTOR_PROOF",
    "RETROACTIVE_D1_RESULT_CHANGE",
    "FORMAL_P03_PRIMARY_TASK_OR_GOLD_CREATION",
    "FORMAL_B0_B4_COMPARATOR_SCORING",
    "PHYSICAL_ARCHITECTURE_SELECTION",
    "MIGRATION_OR_CUTOVER",
    "EXTERNAL_OWNER_IDENTITY_OR_CRYPTOGRAPHIC_AUTHENTICATION",
)


def canonical_json(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf8")


def digest(obj: Any) -> str:
    return sha256(canonical_json(obj)).hexdigest()


def pinned_owner_packet() -> dict:
    """Read exact published Git blob, never a mutable packet in the worktree."""
    proc = subprocess.run(
        ["git", "show", f"{REVIEW_COMMIT}:{REVIEW_FILE}"],
        cwd=ROOT, capture_output=True, check=False,
    )
    if proc.returncode:
        raise ValueError("PUBLISHED_EXACT_OWNER_PACKET_GIT_BLOB_UNAVAILABLE")
    if sha256(proc.stdout).hexdigest() != REVIEW_GIT_SHA256:
        raise ValueError("PUBLISHED_EXACT_OWNER_PACKET_GIT_BLOB_CHANGED")
    packet = json.loads(proc.stdout.decode("utf8"))
    if digest(packet) != REVIEW_CANONICAL_SHA256:
        raise ValueError("PUBLISHED_EXACT_OWNER_PACKET_CANONICAL_HASH_CHANGED")
    # Recompute the original owner packet, Git facts and D1 replay from their
    # original frozen sources before reusing any accepted effect bytes.
    if original.build_owner_packet() != packet:
        raise ValueError("PUBLISHED_OWNER_PACKET_DIFFERS_FROM_VERIFIED_D1_SOURCES")
    if packet["new_p03_owner_decision"] is not None:
        raise ValueError("PREADMISSION_PACKET_WAS_RETROACTIVELY_MUTATED")
    if packet["new_p03_accepted_j1_effect_ids"] or packet["new_p03_qualified_j2_relations"]:
        raise ValueError("PREADMISSION_PACKET_WRONGLY_CONTAINS_ACCEPTED_EFFECTS")
    if tuple(e["accepted_effect_id"] for e in packet["requested_experiment_only_j1_effects"]) != EXPECTED_EFFECT_IDS:
        raise ValueError("PUBLISHED_EFFECT_SET_CHANGED")
    return packet


def validate_acceptance_binding(binding: dict, packet: dict) -> None:
    """Validate the frozen chat-reported acceptance and its exact scope.

    These checks prove that the on-disk record matches the exposed decision
    that ChatGPT was instructed to preserve. They cannot prove owner identity
    independently of this conversation. Never describe them as cryptographic
    evidence of who sent the original message.
    """
    if not isinstance(binding, dict) or digest(binding) != BINDING_CANONICAL_SHA256:
        raise ValueError("EXACT_OWNER_ACCEPTANCE_BINDING_DIGEST_MISMATCH")
    expected_fields = {
        "schema_version", "binding_id", "decision", "verbatim_owner_reply",
        "decision_date", "decision_provenance_class", "decision_context",
        "source_proposal_commit", "source_proposal_path",
        "source_proposal_git_bytes_sha256", "source_proposal_canonical_json_sha256",
        "proposal_id", "experimental_world_id", "accepted_scope",
        "accepted_effect_ids", "accepted_j2_relations", "excluded_authorizations",
        "historical_d1_raw_outcome", "formal_r0_p03_status",
    }
    if set(binding) != expected_fields:
        raise ValueError("EXACT_OWNER_ACCEPTANCE_BINDING_SCHEMA_DRIFT")
    expected = {
        "schema_version": 1,
        "binding_id": "P03V2_D1_EXPERIMENT_OWNER_ACCEPTANCE_BINDING_V01",
        "decision": "ACCEPT",
        "verbatim_owner_reply": "I ACCEPT.",
        "decision_date": "2026-11-14",
        "decision_provenance_class": "CHAT_CONVERSATION_EXPLICIT_OWNER_REPLY_NOT_INDEPENDENTLY_AUTHENTICATED",
        "decision_context": "Owner's immediate reply to the Checkpoint 936 question to ACCEPT, AMEND, or REJECT the exact experiment-only D1 reuse proposal; Research 675, Message 088",
        "source_proposal_commit": REVIEW_COMMIT,
        "source_proposal_path": REVIEW_FILE,
        "source_proposal_git_bytes_sha256": REVIEW_GIT_SHA256,
        "source_proposal_canonical_json_sha256": REVIEW_CANONICAL_SHA256,
        "proposal_id": packet["proposal_id"],
        "experimental_world_id": packet["proposed_world_id"],
        "accepted_scope": "REUSE_EXACT_FOUR_D1_EFFECT_STATEMENTS_AS_P03_EXPERIMENT_ONLY_J1_INPUTS",
        "accepted_effect_ids": list(EXPECTED_EFFECT_IDS),
        "accepted_j2_relations": [],
        "excluded_authorizations": list(EXPECTED_EXCLUSIONS),
        "historical_d1_raw_outcome": "D1_AMEND",
        "formal_r0_p03_status": "INCOMPLETE",
    }
    if binding != expected:
        raise ValueError("EXACT_OWNER_ACCEPTANCE_BINDING_SEMANTIC_DRIFT")


def owner_binding() -> dict:
    record = json.loads(ACCEPTANCE_PATH.read_text(encoding="utf8"))
    validate_acceptance_binding(record, pinned_owner_packet())
    return record


def build_accepted_projection() -> dict:
    """Build one derived, non-operational J1-only development-world snapshot."""
    packet = pinned_owner_packet()
    accepted = json.loads(ACCEPTANCE_PATH.read_text(encoding="utf8"))
    validate_acceptance_binding(accepted, packet)
    j1 = packet["requested_experiment_only_j1_effects"]
    evidence = packet["j2_evidence_ladder_candidate"]
    observable = [e for e in evidence if e["class"] == "OBSERVABLE"]
    assertions = [e for e in evidence if e["class"] == "SOURCE_REPORTED_ATTESTATION"]
    proposed_relations = [e for e in evidence if e["class"] == "RELATIONAL_PROPOSAL"]
    if len(observable) != 1 or len(assertions) != 1 or len(proposed_relations) != 1:
        raise ValueError("SOURCE_FACT_ROLE_LADDER_DRIFT")
    if observable[0]["verification"] != "GIT_OBJECT_VERIFIED":
        raise ValueError("GIT_OBSERVABLE_PROOF_NOT_QUALIFIED")
    if proposed_relations[0]["governing_completion_consequence"] is not False:
        raise ValueError("UNQUALIFIED_J2_PROPOSAL_ELEVATED")
    if assertions[0]["verification"] == "GIT_OBJECT_VERIFIED":
        raise ValueError("SOURCE_ATTESTATION_FALSELY_TREATED_AS_GIT_PROOF")
    lineage = packet["proposed_lineage"]
    if lineage["relation"] != "REPLACE" or lineage["realization_succession"] != "OPEN_RESET":
        raise ValueError("ACCEPTED_EXPERIMENT_LINEAGE_CHANGED")

    result = {
        "schema_version": 1,
        "world_id": accepted["experimental_world_id"],
        "world_status": "J1_EXPERIMENT_ACCEPTED_J2_RELATIONAL_AND_J3_QUALIFICATION_HOLD",
        "scope": "EXPERIMENT_ONLY_NON_OPERATIONAL",
        "owner_decision": {
            "verdict": "ACCEPT",
            "verbatim_reply": accepted["verbatim_owner_reply"],
            "assurance": accepted["decision_provenance_class"],
            "binding_record_canonical_sha256": digest(accepted),
            "accepted_packet_canonical_sha256": digest(packet),
            "source_commit": REVIEW_COMMIT,
        },
        "accepted_j1": {
            "source": "GIT_PINNED_OWNER_REVIEW_PACKET",
            "effects": j1,
            "count": len(j1),
            "closed_accounting": packet["requested_effect_accounting"],
            "currentness_scope": "D1_HISTORICAL_EVENT_REPLAY_ONLY",
        },
        "lineage": {
            "accepted_experiment_semantics": lineage,
            "source_role": "EXACT_OWNER_REVIEWED_EXPERIMENT_LINEAGE",
            "historical_d1_predicate_not_reexecuted_as_new_j3": True,
        },
        "j2_evidence": {
            "git_observable": observable,
            "source_reported_attestations": assertions,
            "natural_owner_relational_proposals_unadmitted": proposed_relations,
            "qualified_relational": [],
            "qualified_relational_count": 0,
        },
        "j3": {
            "new_experimental_requirement_satisfaction": "HOLD_J2_NATURAL_OWNER_QUALIFICATION",
            "new_experimental_completion_certified": False,
            "derived_orientation": "REVIEW_REQUIRED",
            "historical_non_governing_d1_preview": packet["original_d1_non_governing_j3_preview"],
        },
        "original_d1_raw_outcome": "D1_AMEND",
        "historical_d1_rescored": False,
        "primary_tasks_originated": False,
        "historical_legacy_nine_gold_rejudged": False,
        "formal_b0_b4_scores": None,
        "physical_architecture_selected": False,
        "migration_authorized": False,
        "next_qualification": [
            "Actual natural-owner J2 RELATIONAL coverage admission for the three E01 completion components",
            "Independent or explicitly bounded source-attestation qualification for claimed provider transport",
            "One integrated common J1/J2/lineage/J3 currentness executable world rather than historical D1 preview reuse",
            "Sufficient real-source breadth, independent gold roles and formal B0-B4 common-substrate parity",
        ],
    }
    if len(j1) != 4 or len({e["accepted_effect_id"] for e in j1}) != 4:
        raise ValueError("EXPERIMENT_ACCEPTED_EFFECT_COUNT_OR_IDENTITY_WRONG")
    if result["j3"]["new_experimental_completion_certified"] is not False:
        raise ValueError("J2_UNQUALIFIED_COMPLETION_WAS_SELF_CERTIFIED")
    return result


def persist_if_absent(record: dict) -> None:
    text = json.dumps(record, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if PROJECTION_PATH.exists():
        if PROJECTION_PATH.read_text(encoding="utf8") != text:
            raise RuntimeError("EXPERIMENT_ACCEPTED_J1_PROJECTION_IS_IMMUTABLE")
    else:
        with PROJECTION_PATH.open("x", encoding="utf8", newline="\n") as output:
            output.write(text)


def main() -> None:
    projection = build_accepted_projection()
    persist_if_absent(projection)
    print(json.dumps({
        "world_status": projection["world_status"],
        "j1_effects_accepted_experiment_only": projection["accepted_j1"]["count"],
        "qualified_j2_relations": projection["j2_evidence"]["qualified_relational_count"],
        "new_j3_satisfaction": projection["j3"]["new_experimental_requirement_satisfaction"],
        "formal_p03_score": projection["formal_b0_b4_scores"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
