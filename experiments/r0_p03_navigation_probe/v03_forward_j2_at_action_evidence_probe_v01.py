"""A real at-action Git event: source owner, fact kind and evidence assurance.

This unscored probe was preceded by an actual single-path commit containing
an actor-authored, explicitly non-governing source claim. Git independently
records exact file content, changed path and parent. The actor's statement
is not authenticated by the Git object, and the tool/provider execution
details are not independently provable from the object.

Research 512 section 9 is the governing fact-kind distinction. Research 678
is the retrospective contrast. This is NOT an accepted J1 effect, a J2
source admission, a J3 evaluator or a formal Research 513 B0-B4 task.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_j2_091_response_reconciliation_v01 as historical,
)

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).with_name("v03_forward_j2_at_action_evidence_result_v01.json")
ACTION_COMMIT = "131c54a4aec9f8733af35b1c90e8b16a7c9919a5"
ACTION_PARENT = "fefa21bd57df9d40d71a53c5b8af8da0d81b667c"
ACTION_PATH = "experiments/r0_p03_navigation_probe/v03_forward_j2_at_action_event_001.json"
ACTION_BLOB_OID = "425b365c3a845e776babbccd8a6ecf7188c3a73b"
ACTION_BLOB_SHA256 = "ce7a6addb7c1b612c4e1ed5a65fa3baacf06c57f11fae06a512e213b41f923a2"
ACTION_COMMIT_MESSAGE = (
    "Exercise real at-action J2 source-carrier separation with one non-governing event"
)
EXPECTED_COMPONENTS = [
    "ACTOR_INTENT_PRESENT",
    "EXPECTED_PARENT_DECLARED",
    "INTENDED_PATH_DECLARED",
]
PROBE_ONLY_TARGET = "UNACCEPTED_PROBE_ONLY_ACTION_RECORDING_CRITERION"
EXPECTED_LIMITS = [
    "An identical file committed with a Git SHA proves tree membership, not authentic human or provider identity",
    "Commit tool execution has not yet occurred at authoring time",
    "Git author, commit body and actor JSON do not independently prove the executor provider API",
    "No new governing J1 was proposed or accepted for this probe-only target",
    "No existing E01 source-owner COVERS or historical connector proof is created",
    "No new J3 completion, formal R0-P03 score, physical target or migration is implied",
]


def git(*args: str) -> bytes:
    """Read actual Git object data, never directory-naming inference."""
    out = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if out.returncode:
        raise ValueError("REAL_FORWARD_GIT_OBJECT_UNAVAILABLE")
    return out.stdout


def verify_event_record(record: dict[str, Any]) -> None:
    """Reject any unreviewed widening of the non-governing actor claim."""
    if not isinstance(record, dict) or set(record) != {
        "schema_version", "event_id", "record_class", "governing_authority",
        "experimental_action", "actor_statement", "fact_owner_boundaries",
        "assurance_limits", "at_action_source_status",
    }:
        raise ValueError("PROSPECTIVE_SOURCE_RECORD_SCHEMA_OR_AUTHORITY_DRIFT")
    if record["schema_version"] != 1 or record["event_id"] != "R0_P03_V2_FORWARD_J2_ACTION_001":
        raise ValueError("PROSPECTIVE_SOURCE_RECORD_EVENT_ID_DRIFT")
    if record["record_class"] != "PRECOMMIT_CONTEMPORANEOUS_SOURCE_OWNER_CLAIM_AND_ACTION_INTENT":
        raise ValueError("PROSPECTIVE_SOURCE_RECORD_CLASS_DRIFT")
    if record["governing_authority"] != "NONE_EXPERIMENT_ONLY_UNSCORED":
        raise ValueError("PROSPECTIVE_ACTOR_ATTEMPTED_J1_AUTHORITY_ESCALATION")
    expected_action = {
        "operation": "ADD_EXACTLY_ONE_NEW_SOURCE_RECORD_IN_ACTUAL_GIT_COMMIT",
        "source_path": ACTION_PATH,
        "expected_parent_sha": ACTION_PARENT,
        "expected_branch": "v1-source-vault-bootstrap-resume",
        "requested_executor": "CODEXLESS_RUNTIME_BRIDGE_CODEX_GIT_COMMIT_PATHS",
        "commit_message": ACTION_COMMIT_MESSAGE,
        "commit_occurred_at_time_record_was_written": False,
        "commit_sha_known_before_action": False,
    }
    if record["experimental_action"] != expected_action:
        raise ValueError("PROSPECTIVE_ACTOR_ACTION_INTENT_OR_PARENT_CHANGED")
    expected_statement = {
        "claimant_role": "EXPOSED_CHATGPT_ARCHITECTURE_COORDINATOR",
        "claimant_identity_assurance": "CONVERSATION_ROLE_NOT_INDEPENDENTLY_AUTHENTICATED",
        "natural_owner_claim_scope": "AUTHOR_OF_THIS_RECORD_AND_COMMIT_INTENT_NOT_GIT_OR_PROVIDER_FACTS",
        "action_intent": "I intend to add this exact file through the approved single-path commit mechanism",
        "relational_claim": {
            "relation": "COVERS",
            "subject_source_path": ACTION_PATH,
            "target": PROBE_ONLY_TARGET,
            "component_ids": EXPECTED_COMPONENTS,
            "coverage_extent": "FULL_FOR_SELF_REPORTED_INTENT_CONTENT_ONLY",
            "source_status": "CLAIMED_BY_EXPOSED_ACTOR_NOT_J2_ADMITTED",
        },
    }
    if record["actor_statement"] != expected_statement:
        raise ValueError("PROSPECTIVE_RELATIONAL_CLAIM_NOT_EXACTLY_BOUNDED")
    expected_facts = {
        "git_parent_and_changed_path": {
            "fact_class": "OBSERVABLE",
            "natural_owner": "GIT_OBJECT_STORE",
            "status": "TO_BE_VERIFIED_AFTER_COMMIT",
        },
        "actual_bridge_invocation": {
            "fact_class": "EPHEMERAL",
            "natural_owner": "CODEXLESS_BRIDGE_EXECUTION_RESPONSE",
            "status": "UNOBSERVED_AT_RECORD_AUTHORING",
            "durability": "FOLLOWUP_NON_GOVERNING_RECEIPT_ONLY",
        },
        "actor_claim_relation": {
            "fact_class": "RELATIONAL",
            "natural_owner": "THIS_SOURCE_AUTHOR",
            "status": "RECORDED_CLAIM_NOT_AUTHENTICATED_OR_QUALIFIED",
        },
    }
    if record["fact_owner_boundaries"] != expected_facts:
        raise ValueError("PROSPECTIVE_SOURCE_FACT_CLASS_OR_OWNER_CHANGED")
    if record["assurance_limits"] != EXPECTED_LIMITS:
        raise ValueError("PROSPECTIVE_ASSURANCE_EXCLUSIONS_CHANGED")
    if record["at_action_source_status"] != "BEFORE_GIT_COMMIT_SOURCE_DECLARATION":
        raise ValueError("SOURCE_RECORD_FALSELY_CLAIMS_POSTCOMMIT_PROOF")


def original_commit_data() -> tuple[dict[str, Any], dict[str, Any]]:
    """Verify event and actor claim from the same *actual* immutable Git tree."""
    raw = git("show", f"{ACTION_COMMIT}:{ACTION_PATH}")
    if sha256(raw).hexdigest() != ACTION_BLOB_SHA256 or len(raw) != 2990:
        raise ValueError("REAL_ACTION_EVENT_RECORD_BYTES_CHANGED")
    oid = git("rev-parse", f"{ACTION_COMMIT}:{ACTION_PATH}").decode("ascii").strip()
    if oid != ACTION_BLOB_OID:
        raise ValueError("REAL_ACTION_EVENT_BLOB_OID_CHANGED")
    parent = git("show", "-s", "--format=%P", ACTION_COMMIT).decode("ascii").strip()
    diff = git("diff-tree", "--no-commit-id", "--name-status", "-r", ACTION_COMMIT).decode("utf8").splitlines()
    msg = git("show", "-s", "--format=%B", ACTION_COMMIT).decode("utf8").strip()
    if parent != ACTION_PARENT or diff != ["A\t" + ACTION_PATH]:
        raise ValueError("REAL_ACTION_CHANGED_PATH_OR_PARENT_CONTRADICTION")
    if msg != ACTION_COMMIT_MESSAGE:
        raise ValueError("REAL_ACTION_COMMIT_MESSAGE_DRIFT")
    record = json.loads(raw)
    verify_event_record(record)
    return record, {
        "event_commit": ACTION_COMMIT,
        "commit_parent": parent,
        "changed_paths": diff,
        "git_blob_oid": oid,
        "git_blob_sha256": sha256(raw).hexdigest(),
        "git_blob_size": len(raw),
        "exact_claim_present_in_same_commit_tree": True,
        "independent_observation_class": "GIT_OBJECT_VERIFIED",
        "independent_actor_identity": "NOT_VERIFIED",
        "independent_tool_provider_transport": "NOT_VERIFIED_FROM_GIT",
    }


def build() -> dict[str, Any]:
    record, git_observation = original_commit_data()
    old = historical.build()
    if (
        old["disposition"]["DISPOSITION"] != "CANNOT_ATTEST"
        or old["qualified_j2_relational_count"] != 0
        or old["new_j3_completion_certified"]
    ):
        raise ValueError("HISTORICAL_D1_J2_OR_J3_BOUNDARY_CHANGED")
    claim = record["actor_statement"]["relational_claim"]
    if claim["target"] != PROBE_ONLY_TARGET:
        raise ValueError("PROBE_ONLY_RELATION_WRONGLY_TARGETS_ACCEPTED_J1")
    return {
        "schema_version": 1,
        "status": "REAL_GIT_AT_ACTION_CLAIM_COCOMMITTED_WITH_INDEPENDENT_OBSERVABLES",
        "scope": "EXPOSED_NON_GOVERNING_UNSCORED_PHYSICAL_J2_CARRIER_PROBE",
        "source_event": git_observation,
        "actor_claim": {
            "source_carrier": ACTION_PATH,
            "source_commit": ACTION_COMMIT,
            "claimant_role": record["actor_statement"]["claimant_role"],
            "claimant_identity": "SELF_DESCRIBED_NOT_INDEPENDENTLY_AUTHENTICATED",
            "claim_type": "RELATIONAL_COVERS_PROBE_ONLY_RECORDING_CRITERION",
            "claimed_component_ids": claim["component_ids"],
            "claimed_coverage": claim["coverage_extent"],
            "claim_recorded_in_same_git_commit": True,
            "independent_owner_identity_proof": False,
            "qualified_j2_relational": False,
            "governing_j1_target_accepted": False,
        },
        "observable_git": {
            "fact_owner": "GIT_COMMIT_OBJECT",
            "changed_path_exact": True,
            "parent_exact": True,
            "file_blob_exact": True,
            "no_separate_covers_needed_for_direct_git_facts": True,
        },
        "ephemeral_executor": {
            "requested_executor_self_report": record["experimental_action"]["requested_executor"],
            "record_was_created_before_commit_claim": True,
            "provider_execution_report_in_current_conversation": "BRIDGE_COMMIT_PATHS_AND_PUSH_FF_SUCCESS_REPORTED",
            "durable_independent_provider_receipt": False,
            "underlying_provider_api_independently_authenticated": False,
            "status": "SOURCE_REPORTED_EXECUTION_WITH_GIT_OBSERVABLE_SIDE_EFFECT",
        },
        "comparison_to_historical": {
            "historical_event": "ORIGINAL_D1_MC0029_MESSAGE018",
            "historical_later_source_owner_response": "CANNOT_ATTEST",
            "historical_contemporaneous_covers_of_new_p03_j1": False,
            "new_event_has_contemporaneously_cocommitted_claim": True,
            "new_event_claim_is_qualified_j2": False,
            "new_event_has_owner_authenticated_identity": False,
            "new_event_is_more_traceable_as_claim": True,
            "new_event_proves_actual_requested_executor": False,
        },
        "candidate_design_discriminators": {
            "cocommitted_actor_claim": "CAUSAL_SOURCE_COHERENCE_GIT_VERIFIABLE_OWNER_IDENTITY_UNPROVEN",
            "direct_git_observables": "RECONSTRUCTIBLE_FROM_PLATFORM_OBJECTS",
            "external_ephemeral_action": "REQUIRES_PROVIDER_RECEIPT_WHEN_GOVERNING_ASSURANCE_DEMANDS_IT",
            "relational_j2": "REQUIRES_REAL_ACCEPTED_EFFECT_AND_QUALIFIED_SOURCE_OWNER_DECLARATION",
            "missing_evidence": "BOUNDED_UNKNOWN_NEVER_AUTOMATIC_SATISFIED",
            "architectural_candidate": "OPEN_NO_PHYSICAL_SELECTION",
        },
        "new_accepted_j1_effects": 0,
        "p03_preexisting_experiment_only_accepted_j1": 4,
        "new_qualified_natural_owner_j2": 0,
        "historical_j3_completion": "HOLD",
        "new_j3_completion": "NOT_APPLICABLE_NO_GOVERNING_PROBE_EFFECT",
        "formal_r0_p03_scores": None,
        "physical_target_selected": False,
        "next": (
            "QUALIFY_WHETHER_A_REAL_SOURCE_OWNER_AT_ACTION_COVERS_PORT_AND_PROVIDER_RECEIPT "
            "CAN_BE_SUPPORTED_WITHOUT_UNSAFE_IDENTITY_OR_AUTHORITATIVE_INDEX_ASSUMPTIONS"
        ),
    }


def main() -> None:
    result = build()
    data = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != data:
            raise RuntimeError("FORWARD_J2_PROBE_FIRST_RUN_RESULT_IMMUTABILITY_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as output:
            output.write(data)
    print(json.dumps({
        "status": result["status"],
        "git_verified": result["observable_git"]["changed_path_exact"],
        "actor_claim_cocommitted": result["actor_claim"]["claim_recorded_in_same_git_commit"],
        "qualified_j2": result["new_qualified_natural_owner_j2"],
        "provider_proof": result["ephemeral_executor"]["durable_independent_provider_receipt"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
