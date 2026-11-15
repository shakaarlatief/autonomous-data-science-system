"""Separately adjudicate one source-authored P03 RELATIONAL COVERS fact.

The source declaration is not allowed to qualify itself. This consumer reads
the declaration and its exact publication commit from Git, checks the owner-
accepted experiment-only policy, the prior frozen composite executable,
the one postfreeze source event, and the distinct execution-evidence commit.

Actual G006/G013/G009 results are replayed before experimental J2 admission.
All conclusions are SOURCE-RELATIVE with explicitly weaker exposed-model
provenance. No independent model identity, production J2, S1 activation,
J3 satisfaction, formal P03 score, or architecture choice is established.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as j1,
    v03_real_pk_j2_experiment_assurance_accepted_policy_rev01 as policy,
    v03_real_pk_delegated_s1_composite_realizer_v01 as runner,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
CLAIM_PATH = "experiments/r0_p03_navigation_probe/real_pk_world/delegated_s1/source_author_postexecution_covers_v01.json"
OUTPUT = HERE / "v03_real_pk_delegated_s1_j2_admission_result_v01.json"
CLAIM_COMMIT = "d4ef4d3ec259c2d578ad412f197dd49211225bc7"
CLAIM_PARENT = "338e591c3ba08bc1ca87af44df678086164a3f4b"
CLAIM_SHA256 = "a1fd016deb19d1468bfbbe2810fccd1bb5c0487711adc4d9dc17bb77901c2d6f"
EVIDENCE_COMMIT = CLAIM_PARENT
EVIDENCE_SHA256 = "47e41bb4c0fde09b9d245751ab7d727e81a9b7d78ec557053828cebad34e42f2"
EVENT = "ca91cbc27dc47f6efa383a788d4c9c02689bb9bd"
FREEZE = "c523340a20dd7628bc2a470594e28b48929a29dc"
EXECUTABLE_SHA256 = "2f6799ffa3c3be784853630f29d5e147c5552ff80234c22567f3eaa100d1978d"
INTENT_SHA256 = "eb6401ea2fa267b35fc1decb09506a7e78c74aebcc9d746c5174436ad58afdcf"
AFTER_SHA256 = "10df00847933203fb836a6b8f7c8d56732ab108fedc60ea2679e6197aaf3a331"
CLAIM_ID = "P03V2_S1_DELEGATED_COMPOSITE_POSTEXECUTION_COVERS_001"
ASSURANCE = "EXPERIMENT_ONLY_SOURCE_RELATIVE_RELATIONAL_J2_WITH_DECLARED_WEAK_ACTOR_ASSURANCE"
SOURCE_TREE = "experiments/r0_p03_navigation_probe/real_pk_world"
COMPONENT_MAP = (
    ("EXPLICIT_IDENTITY_PRESERVING_MOVE", "g006.identity_preserved",
     "NEW_EVENT_G006_IDENTITY_CONTINUITY"),
    ("AFFECTED_VIEW_REFRESH_SELECTED", "g013.affected_view",
     "NEW_EVENT_G013_SELECTED_EXPECTED_VIEW"),
    ("INCREMENTAL_EQUALS_CURRENT_FULL_BUILD", "g013.selected_equals_full",
     "NEW_EVENT_G013_G009_EXACT_EQUIVALENCE"),
    ("STALE_DERIVED_RESULT_NOT_GOVERNING", "g013.previous_manifest",
     "OLD_STALE_AND_NEW_FRESH"),
)
FALSE = {
    "formal_b0_b4_scored": False,
    "historical_s0_evidence_carryover": False,
    "j3_satisfied": False,
    "physical_target_selected": False,
    "production_j2_accepted": False,
    "qualified_relational_j2": False,
    "s1_activated": False,
}


def git(*args: str) -> bytes:
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if result.returncode:
        raise ValueError("P03_J2_SOURCE_GIT_OBJECT_MISSING")
    return result.stdout


def file_at(commit: str, path: str) -> bytes:
    return git("show", f"{commit}:{path}")


def direct_parent(commit: str) -> str:
    return git("show", "-s", "--format=%P", commit).decode("ascii").strip()


def changed_paths(commit: str) -> list[tuple[str, str]]:
    raw = git("diff-tree", "--no-commit-id", "--name-status",
              "--no-renames", "-r", commit).decode("utf8").strip()
    return [tuple(line.split("\t", 1)) for line in raw.splitlines()]


def source_claim() -> dict[str, Any]:
    """Read the declaration's original Git object and reject worktree drift."""
    if direct_parent(CLAIM_COMMIT) != EVIDENCE_COMMIT:
        raise ValueError("P03_J2_COVERS_CLAIM_NOT_AFTER_EXECUTION_EVIDENCE")
    if changed_paths(CLAIM_COMMIT) != [("A", CLAIM_PATH)]:
        raise ValueError("P03_J2_COVERS_CLAIM_NOT_DISTINCT_SINGLE_SOURCE_COMMIT")
    raw = file_at(CLAIM_COMMIT, CLAIM_PATH)
    if sha256(raw).hexdigest() != CLAIM_SHA256:
        raise ValueError("P03_J2_COVERS_GIT_BLOB_CHANGED")
    if (ROOT / CLAIM_PATH).read_bytes() != raw:
        raise ValueError("P03_J2_COVERS_WORKTREE_CONFLICT")
    return json.loads(raw.decode("utf8"))


def admissible_source_relations() -> list[tuple[str, dict[str, Any]]]:
    """Enumerate every JSON in the exact bounded experimental source world.

    A complete source-tree enumeration prevents a duplicate RELATIONAL COVERS
    tuple from being hidden behind another filename in the same world. It
    does not purport to audit unrelated or private source-owner registries.
    """
    paths = git("ls-tree", "-r", "--name-only", CLAIM_COMMIT, "--", SOURCE_TREE
                ).decode("utf8").splitlines()
    relations = []
    for path in paths:
        if not path.endswith(".json"):
            continue
        value = json.loads(file_at(CLAIM_COMMIT, path))
        if isinstance(value, dict) and value.get("relation") == "COVERS":
            relations.append((path, value))
        elif isinstance(value, dict) and isinstance(value.get("relational_claim"), dict):
            nested = value["relational_claim"]
            if nested.get("relation") == "COVERS":
                relations.append((path, nested))
    return relations


def validate_claim(claim: dict, scope: dict, intent: dict,
                   receipt: dict) -> None:
    """Reject false authority and test each exact source-author component.

    The authorial string FULL is a requested coverage class, not proof. The
    executed result is inspected independently of the source-authored flag.
    """
    if not isinstance(claim, dict) or set(claim) != {
        "accepted_effect_id", "accepted_policy", "all_required_component_claims",
        "authorial_coverage_summary", "authority", "declaration_id",
        "declaration_status", "execution_evidence", "fact_class",
        "natural_owner", "postexecution_timing", "realizer", "relation",
        "relation_scope", "schema_version", "source_event", "world_id",
    }:
        raise ValueError("P03_J2_COVERS_CLOSED_SCHEMA")
    if any((
        claim["schema_version"] != 1,
        claim["declaration_id"] != CLAIM_ID,
        claim["declaration_status"] !=
            "SOURCE_AUTHOR_COVERS_CLAIM_AWAITING_SEPARATE_J2_ADMISSION",
        claim["fact_class"] != "RELATIONAL",
        claim["relation"] != "COVERS",
        claim["relation_scope"] != "EXACT_ONE_EVENT_SOURCE_RELATIVE_EXPERIMENT_ONLY",
        claim["world_id"] != scope["world_id"],
        claim["accepted_effect_id"] != scope["accepted_s1_effect_id"],
        claim["authorial_coverage_summary"] != "CLAIMED_FULL_NOT_SELF_CERTIFIED",
        claim["authority"] != FALSE,
    )):
        raise ValueError("P03_J2_COVERS_SCOPE_OR_FALSE_AUTHORITY")
    if claim["accepted_policy"] != {
        "owner_acceptance_binding_sha256": policy.BINDING_SHA256,
        "owner_acceptance_commit": scope["policy"]["acceptance_commit"],
        "proposal_id": scope["policy"]["proposal_id"],
        "proposal_sha256": scope["policy"]["proposal_sha256"],
        "scope_freeze_commit": FREEZE,
        "scope_id": scope["scope_id"],
    }:
        raise ValueError("P03_J2_COVERS_WRONG_ACCEPTED_POLICY")
    owner = claim["natural_owner"]
    if owner != {
        "independently_authenticated": False,
        "natural_owner_scope": "AUTHOR_OF_EXPERIMENT_ORCHESTRATION_ONLY",
        "production_implementation_author": False,
        "provenance": scope["realizer"]["actor_assurance"],
        "role": intent["author_role"],
        "self_declared_same_source_author_as_at_action_intent": True,
    }:
        raise ValueError("P03_J2_COVERS_OWNER_OR_AUTHENTICATION_UNQUALIFIED")
    if claim["realizer"] != {
        "executable_path": runner.RUNNER_PATH,
        "executable_sha256": EXECUTABLE_SHA256,
        "historical_g006_g013_library_ownership_asserted": False,
        "id": runner.REALIZER,
    }:
        raise ValueError("P03_J2_COVERS_NOT_OWNED_COMPOSITE_REALIZER")
    if claim["source_event"] != {
        "after_path": runner.AFTER,
        "at_action_intent_path": runner.INTENT,
        "at_action_relationship": "PROSPECTIVE_EXECUTION_INTENT_NOT_J2_COVERS",
        "before_path": runner.BEFORE,
        "commit": EVENT,
        "parent": FREEZE,
    }:
        raise ValueError("P03_J2_COVERS_WRONG_SOURCE_EVENT")
    if claim["execution_evidence"] != {
        "formal_ads_corpus_rebuild": False,
        "independent_model_or_provider_actor_attestation": False,
        "published_evidence_commit": EVIDENCE_COMMIT,
        "receipt_path": str(runner.OUTPUT.relative_to(ROOT)).replace("\\", "/"),
        "receipt_sha256": EVIDENCE_SHA256,
        "reproduced_at_least_twice": True,
        "source_role": "OBSERVABLE_PRODUCTION_CODE_EXECUTED_IN_ISOLATED_SCHEMA_VALID_GIT_ROOT",
    }:
        raise ValueError("P03_J2_COVERS_EVIDENCE_SOURCE_WRONG")
    if claim["postexecution_timing"] != {
        "execution_receipt_precedes_declaration": True,
        "new_source_event_already_committed": True,
        "not_backdated_as_at_action_covers": True,
    }:
        raise ValueError("P03_J2_COVERS_TIMING_CLAIM_WRONG")
    claims = claim["all_required_component_claims"]
    if not isinstance(claims, list) or len(claims) != len(COMPONENT_MAP):
        raise ValueError("P03_J2_COVERS_ALL_REQUIRED_INCOMPLETE")
    expected = [
        {
            "component_id": component,
            "coverage_assertion": "FULL_AS_SOURCE_AUTHOR_CLAIM_PENDING_EVIDENCE_ADMISSION",
            "evidence_field": field,
            "observation_kind": kind,
        } for component, field, kind in COMPONENT_MAP
    ]
    if claims != expected:
        raise ValueError("P03_J2_COVERS_COMPONENT_CLAIM_CHANGED")
    if (
        receipt["event"]["source_event_commit"] != EVENT
        or receipt["event"]["freeze_commit"] != FREEZE
        or receipt["realizer_id"] != runner.REALIZER
        or receipt["component_ids"] != [entry[0] for entry in COMPONENT_MAP]
        or receipt["g006"]["production_g006_executed"] is not True
        or receipt["g006"]["identity_preserved"] is not True
        or receipt["g006"]["serialization_order_independent"] is not True
        or receipt["g006"]["current_carrier"] != runner.AFTER
        or set(receipt["g006"]["historical_carriers"]) != {runner.BEFORE, runner.AFTER}
        or receipt["g013"]["production_g013_g009_executed"] is not True
        or receipt["g013"]["affected_view"] != runner.VIEW_ID
        or receipt["g013"]["selection_reason"] !=
           [[runner.VIEW_ID, "DEPENDENCY_BINDING_CHANGED"]]
        or receipt["g013"]["selected_equals_full"] is not True
        or receipt["g013"]["previous_manifest"] != "STALE"
        or receipt["g013"]["current_manifest"] != "FRESH"
        or receipt["g013"]["G010_fixture_used_only_as_execution_prerequisite"] is not True
        or receipt["g013"]["whole_ADS_corpus_G013_claimed"] is not False
        or receipt["qualified_relational_j2"] is not False
        or receipt["s1_activated"] is not False
        or receipt["postexecution_covers_admitted"] is not False
        or not receipt["j3"].startswith("HOLD_")
    ):
        raise ValueError("P03_J2_COVERS_NEW_EVENT_EXECUTION_COMPONENTS_NOT_PROVEN")


def validate_original_sources() -> tuple[dict, dict, dict, dict]:
    """Validate chronological commits and original exact evidence origins."""
    accepted = policy.build()
    original_j1 = j1.build()
    scope = runner.load_scope()
    if (
        accepted["policy"]["status"] != "OWNER_ACCEPTED_PROSPECTIVE_EXPERIMENT_ONLY_POLICY"
        or accepted["qualified_experimental_relational_j2"] != 0
        or original_j1["accepted_j1"]["effects"][1]["id"] !=
            scope["accepted_s1_effect_id"]
        or original_j1["accepted_j1"]["effects"][1]["completion_contract"] != {
            "actual_natural_owner_covers_required": True,
            "composition": "ALL_REQUIRED",
            "exact_source_revision_and_executed_evidence_required": True,
            "required_components": list(runner.COMPONENTS),
        }
        or original_j1["accepted_j1"]["effects"][2]["lineage"][
            "realization_succession"] != "OPEN_RESET"
        or original_j1["currentness"]["activation_status"] != "NOT_ACTIVATED"
    ):
        raise ValueError("P03_J2_COVERS_J1_OR_POLICY_INVALID")
    for child, parent in (
        (FREEZE, scope["policy"]["acceptance_commit"]),
        (EVENT, FREEZE),
        (EVIDENCE_COMMIT, EVENT),
        (CLAIM_COMMIT, EVIDENCE_COMMIT),
    ):
        if child == FREEZE:
            result = subprocess.run(
                ["git", "merge-base", "--is-ancestor", parent, child],
                cwd=ROOT, capture_output=True,
            )
            if result.returncode:
                raise ValueError("P03_J2_COVERS_PREACTION_ACCEPTANCE_NOT_ANCESTOR")
        elif direct_parent(child) != parent:
            raise ValueError("P03_J2_COVERS_GIT_CHRONOLOGY_FALSE")
    if sha256(file_at(FREEZE, runner.RUNNER_PATH)).hexdigest() != EXECUTABLE_SHA256:
        raise ValueError("P03_J2_FROZEN_REALIZER_BYTES_CHANGED")
    if sha256(file_at(EVENT, runner.INTENT)).hexdigest() != INTENT_SHA256:
        raise ValueError("P03_J2_AT_ACTION_INTENT_BYTES_CHANGED")
    if sha256(file_at(EVENT, runner.AFTER)).hexdigest() != AFTER_SHA256:
        raise ValueError("P03_J2_SOURCE_AFTER_BLOB_CHANGED")
    intent = json.loads(file_at(EVENT, runner.INTENT))
    runner.validate_intent(intent, scope, FREEZE)
    source_before = json.loads(file_at(FREEZE, runner.BEFORE))
    source_after = json.loads(file_at(EVENT, runner.AFTER))
    runner.validate_carrier(source_before, source_after, scope, FREEZE)
    raw_receipt = file_at(EVIDENCE_COMMIT, str(runner.OUTPUT.relative_to(ROOT)).replace("\\", "/"))
    if (
        sha256(raw_receipt).hexdigest() != EVIDENCE_SHA256
        or raw_receipt != runner.OUTPUT.read_bytes()
    ):
        raise ValueError("P03_J2_EXECUTION_RECEIPT_OR_WORKTREE_DRIFT")
    receipt = json.loads(raw_receipt)
    claim = source_claim()
    return claim, scope, intent, receipt


def qualify() -> dict[str, Any]:
    """Apply scoped policy and mechanical source/evidence checks independently."""
    claim, scope, intent, receipt = validate_original_sources()
    validate_claim(claim, scope, intent, receipt)
    # Full-tree uniqueness is defined per fact (world, event, effect, realizer).
    relations = admissible_source_relations()
    matches = []
    for path, declaration in relations:
        if (
            declaration.get("relation") == "COVERS"
            and declaration.get("accepted_effect_id",
                declaration.get("target_accepted_effect_id")) == scope["accepted_s1_effect_id"]
            and declaration.get("realizer", {}).get("id",
                declaration.get("realizer_id")) == runner.REALIZER
            and declaration.get("source_event", {}).get("commit", EVENT) == EVENT
        ):
            matches.append(path)
    if matches != [CLAIM_PATH]:
        raise ValueError("P03_J2_NATURAL_OWNER_RELATIONAL_FACT_TUPLE_NOT_UNIQUE")
    # Recompute actual production-backed engineering behavior on the exact
    # Git pair. Do not treat a convenient fixture, author FULL string or an
    # older transition as an already qualified component result.
    observed = runner.execute(EVENT, FREEZE)
    if observed != receipt:
        raise ValueError("P03_J2_PRODUCTION_REPLAY_DIFFERENT_FROM_PUBLISHED_EVIDENCE")
    return {
        "schema_version": 1,
        "status": "QUALIFIED_SOURCE_RELATIVE_EXPERIMENTAL_J2_WEAK_ACTOR_ASSURANCE",
        "world_id": scope["world_id"],
        "fact_class": "RELATIONAL",
        "relation": "COVERS",
        "accepted_effect_id": scope["accepted_s1_effect_id"],
        "realizer_id": runner.REALIZER,
        "source_event_commit": EVENT,
        "declaration_commit": CLAIM_COMMIT,
        "declaration_sha256": CLAIM_SHA256,
        "scope_commit": FREEZE,
        "published_execution_commit": EVIDENCE_COMMIT,
        "published_execution_sha256": EVIDENCE_SHA256,
        "assurance_class": ASSURANCE,
        "provenance_limit": "MODEL_ACTOR_NOT_INDEPENDENTLY_AUTHENTICATED",
        "scope_limit": "ONE_EXPERIMENTAL_COMPOSITE_REALIZER_NOT_PRODUCTION_G006_G013_OWNER",
        "qualified_experimental_relational_j2_count": 1,
        "all_required_component_ids": [v[0] for v in COMPONENT_MAP],
        "all_component_evidence_replayed": True,
        "one_fact_tuple_in_bounded_source_world": True,
        "previous_s0_execution_credited_to_s1": False,
        "prior_948_j2_upgraded": False,
        "independent_model_identity_proven": False,
        "production_j2_qualified": False,
        "s1_activated_by_this_j2_verifier": False,
        "j3_satisfied_by_this_j2_verifier": False,
        "formal_r0_p03_scored": False,
        "physical_target_selected": False,
    }


def main() -> None:
    result = qualify()
    raw = (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)
           + "\n").encode("utf8")
    if OUTPUT.exists():
        if OUTPUT.read_bytes() != raw:
            raise RuntimeError("P03_J2_ADMISSION_RECEIPT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("xb") as f:
            f.write(raw)
    print(json.dumps({
        "status": result["status"],
        "qualified_experimental_j2": result["qualified_experimental_relational_j2_count"],
        "strong_actor_authenticated": result["independent_model_identity_proven"],
        "S1": result["s1_activated_by_this_j2_verifier"],
        "J3": result["j3_satisfied_by_this_j2_verifier"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
