"""Admit the explicit conversational owner decision for P03 experiment-only J2 policy.

The owner has accepted the exact *policy*, not a J2 fact or any source event.
This decoder checks the immutable original Git proposal, the new decision
binding and historical negative J2 evidence without changing the frozen
predecision proposal/preflight. Recorded-chat context is not a cryptographic
proof of human identity, and cannot grant past or future realization coverage
automatically. The source-realizer/event freeze must happen after this
acceptance is durably published.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_j2_experiment_assurance_preflight_rev01 as preflight,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
BINDING = HERE / "v03_real_pk_j2_experiment_assurance_owner_acceptance_binding_rev01.json"
OUTPUT = HERE / "v03_real_pk_j2_experiment_assurance_accepted_policy_result_rev01.json"
POLICY_COMMIT = "3dc76841973e75af201c4036007e95f06d10545d"
POLICY_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_j2_experiment_assurance_owner_proposal_rev01.json"
BINDING_SHA256 = "beabc995359f79fe8d4f659efa76ff912b8ec02de74397d3656c29438215672d"
EXPECTED_EXCLUSIONS = (
    "INDEPENDENT_MODEL_ACTOR_AUTHENTICATION",
    "PRODUCTION_NATURAL_OWNER_COVERS",
    "HISTORICAL_G006_G013_CODE_AUTHORSHIP",
    "RETROSPECTIVE_CHECKPOINT_948_J2",
    "AUTOMATIC_FUTURE_J2_FROM_OWNER_ACCEPTANCE",
    "AUTOMATIC_S1_ACTIVATION",
    "AUTOMATIC_J3_SATISFIED",
    "NEW_EXPERIMENT_J1_EFFECT",
    "FORMAL_B0_B4_SCORES",
    "PHYSICAL_ARCHITECTURE_SELECTION",
    "PRODUCTION_CHANGE_MIGRATION_OR_CUTOVER",
)


def validate_binding(b: dict[str, Any]) -> None:
    """Validate the full exact decision envelope, refusing stronger authority."""
    if not isinstance(b, dict) or set(b) != {
        "schema_version", "binding_id", "decision", "verbatim_owner_reply",
        "decision_date", "decision_context", "decision_provenance_class",
        "policy_proposal_id", "policy_proposal_source_path",
        "policy_proposal_git_commit", "policy_proposal_sha256",
        "accepted_scope", "effect_id", "world_id", "agreed_actor_assurance",
        "prospective_event_count", "requires_separate_source_realizer_scope_freeze",
        "requires_new_git_event_after_acceptance",
        "requires_actual_new_revision_g006_g013",
        "requires_postexecution_source_author_covers",
        "requires_independent_j3_evaluation",
        "previous_event", "previous_event_qualifying_j2_count",
        "previous_s1_activated", "previous_j3",
        "accepted_policy_not_an_admission", "excluded_authorizations",
    }:
        raise ValueError("P03_J2_POLICY_ACCEPTANCE_CLOSED_SCHEMA")
    expected = {
        "schema_version": 1,
        "binding_id": "P03V2_EXPERIMENT_ONLY_J2_POLICY_REV01_OWNER_ACCEPTANCE_BINDING_V01",
        "decision": "ACCEPT",
        "verbatim_owner_reply": "ACCEPT",
        "decision_date": "2026-11-15",
        "decision_provenance_class": "CHAT_CONVERSATION_EXPLICIT_OWNER_REPLY_NOT_INDEPENDENTLY_AUTHENTICATED",
        "policy_proposal_id": preflight.PROPOSAL,
        "policy_proposal_source_path": POLICY_PATH,
        "policy_proposal_git_commit": POLICY_COMMIT,
        "policy_proposal_sha256": preflight.SOURCE_SHA256,
        "accepted_scope": "ONE_FORWARD_ONLY_PROSPECTIVE_EXPERIMENT_SOURCE_OWNER_J2_ASSURANCE_POLICY_FOR_BOUND_S1_REALIZER",
        "effect_id": preflight.EXPECTED_SOURCE_CONTEXT["accepted_j1_effect_id"],
        "world_id": preflight.EXPECTED_SOURCE_CONTEXT["world_id"],
        "agreed_actor_assurance": "RECORDED_CHAT_DELEGATION_WITH_EXPOSED_MODEL_SOURCE_AUTHOR_NOT_INDEPENDENTLY_AUTHENTICATED",
        "prospective_event_count": 1,
        "requires_separate_source_realizer_scope_freeze": True,
        "requires_new_git_event_after_acceptance": True,
        "requires_actual_new_revision_g006_g013": True,
        "requires_postexecution_source_author_covers": True,
        "requires_independent_j3_evaluation": True,
        "previous_event": preflight.EVENT_SHA,
        "previous_event_qualifying_j2_count": 0,
        "previous_s1_activated": False,
        "previous_j3": "HOLD",
        "accepted_policy_not_an_admission": True,
        "excluded_authorizations": list(EXPECTED_EXCLUSIONS),
    }
    if any(b[key] != value for key, value in expected.items()):
        raise ValueError("P03_J2_POLICY_ACCEPTANCE_SCOPE_OR_AUTHORITY_DRIFT")
    if b["decision_context"] != (
        "Direct owner reply immediately following ChatGPT's exact REV01 proposal ID, SHA-256, ACCEPT/AMEND/REJECT presentation after Checkpoint 949 publication."
    ):
        raise ValueError("P03_J2_POLICY_ACCEPTANCE_PROVENANCE_DRIFT")


def verify_original_git() -> dict:
    """Read the exact original published proposal, not a mutable replacement."""
    result = subprocess.run(
        ["git", "show", f"{POLICY_COMMIT}:{POLICY_PATH}"],
        cwd=ROOT, check=False, capture_output=True,
    )
    if result.returncode or sha256(result.stdout).hexdigest() != preflight.SOURCE_SHA256:
        raise ValueError("P03_J2_POLICY_ORIGINAL_GIT_SOURCE_DRIFT")
    if result.stdout != preflight.SOURCE.read_bytes():
        raise ValueError("P03_J2_POLICY_WORKTREE_CONFLICTS_WITH_GIT")
    return preflight.load_source()


def build() -> dict[str, Any]:
    """Return policy accepted, while J2/S1/J3 remain unqualified."""
    proposal = verify_original_git()
    raw = BINDING.read_bytes()
    if sha256(raw).hexdigest() != BINDING_SHA256:
        raise ValueError("P03_J2_POLICY_ACCEPTANCE_BINDING_BYTES_CHANGED")
    binding = json.loads(raw.decode("utf8"))
    validate_binding(binding)
    prior = preflight.build()
    if (
        proposal["proposal_id"] != binding["policy_proposal_id"]
        or proposal["decision_state"] != "PROPOSED_NOT_OWNER_ACCEPTED"
        or prior["prior_event_j2"] != "HOLD"
        or prior["prior_event_s1"] != "NOT_ACTIVATED"
        or prior["prior_event_j3"] != "HOLD"
        or prior["owner_decision"] != "NOT_RECEIVED"
        or prior["proposal_state"] != "PROPOSED_NOT_OWNER_ACCEPTED"
    ):
        raise ValueError("P03_J2_POLICY_PRIOR_EVIDENCE_WRONGFULLY_PROMOTED")
    return {
        "schema_version": 1,
        "policy": {
            "proposal_id": preflight.PROPOSAL,
            "proposal_sha256": preflight.SOURCE_SHA256,
            "original_proposal_git_commit": POLICY_COMMIT,
            "owner_decision": "ACCEPT",
            "owner_decision_source": "EXPLICIT_CHAT_REPLY_REPORTED_IN_THIS_INTERACTION",
            "owner_independent_authentication": False,
            "binding_file_sha256": BINDING_SHA256,
            "scope": "ONE_FUTURE_EXPERIMENT_ONLY_EVENT",
            "status": "OWNER_ACCEPTED_PROSPECTIVE_EXPERIMENT_ONLY_POLICY",
            "usable_before_binding_publication": False,
        },
        "preexisting_event": {
            "git": preflight.EVENT_SHA,
            "natural_owner_j2_qualified": False,
            "s1_activated": False,
            "j3": "HOLD",
        },
        "next_gates": {
            "one_source_realizer_scope_freeze": "REQUIRED_BEFORE_NEW_EVENT",
            "new_exact_git_event": "NOT_YET_PERFORMED",
            "g006_and_g013_execution_for_new_event": "NOT_YET_PERFORMED",
            "postexecution_covers": "NOT_YET_RECEIVED",
            "independent_j3": "NOT_EVALUATED",
        },
        "qualified_experimental_relational_j2": 0,
        "s1_activated": False,
        "j3_satisfied": False,
        "formal_r0_p03_complete": False,
        "production_authority_changed": False,
        "physical_target_selected": False,
    }


def main() -> None:
    result = build()
    data = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != data:
            raise RuntimeError("P03_J2_POLICY_ACCEPTED_RECEIPT_IMMUTABILITY_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as f:
            f.write(data)
    print(json.dumps({
        "policy": result["policy"]["status"],
        "existing_J2": result["qualified_experimental_relational_j2"],
        "S1_activated": result["s1_activated"],
        "J3_satisfied": result["j3_satisfied"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
