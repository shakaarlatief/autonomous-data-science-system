"""Separate deterministic J3 lifecycle/currentness predicate for P03 S1.

The authorial COVERS statement is not imported as a completion oracle. This
module consumes exact owner-accepted J1, a separately qualified source-relative
experimental J2 fact, and actual source-event execution observations. It
applies REQUIRE/ALL_REQUIRED and LIFECYCLE/REPLACE/OPEN_RESET as separate
operations, including the prohibition on path/generated-view authority.

This is a distinct semantic evaluation mechanism, not independently authored
blind scientific gold, a cryptographically authenticated model source owner,
production Project System activation, or R0-P03 B0-B4 scoring.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as accepted_j1,
    v03_real_pk_delegated_s1_j2_admission_v01 as j2_admission,
    v03_real_pk_delegated_s1_composite_realizer_v01 as runner,
)

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_real_pk_delegated_s1_j3_lifecycle_result_v01.json"

ACCEPTED_J2_COMMIT = "14f48760b1e23d50cb2d30820817239c1d1ee7f0"
ACCEPTED_J2_RESULT_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_j2_admission_result_v01.json"
ACCEPTED_J2_RESULT_SHA256 = "3e9e5c6ad65f381e50cd7605f0abdb1679d47d9fa59ec14311797554883fdbad"
EXECUTION_COMMIT = j2_admission.EVIDENCE_COMMIT
EXECUTION_PATH = "experiments/r0_p03_navigation_probe/v03_real_pk_delegated_s1_composite_realizer_result_v01.json"
EXECUTION_SHA256 = j2_admission.EVIDENCE_SHA256

SOURCE_EVIDENCE_ROLE = "GIT_PINNED_PRODUCTION_G006_G013_G009_EXECUTED_IN_ISOLATED_ADS_SCHEMA_VALID_ROOT"
J3_PASS = "SATISFIED_EXPERIMENT_ONLY_SOURCE_RELATIVE_WEAK_ACTOR_ASSURANCE"
J3_HOLD = "HOLD_MISSING_S1_ALL_REQUIRED_COMPONENT_EVIDENCE"
CURRENTNESS_STATUS = "ACTIVATED_IN_EXACT_BOUNDED_EXPERIMENTAL_S1_WORLD"
E01, E02, E03, E04 = accepted_j1.EXPECTED_IDS

def source_digest(value: Any) -> bool:
    """Accept only complete SHA-256 hex material, not a descriptive flag."""
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def check_component(name: str, execution: dict) -> bool:
    """Classify incomplete evidence as unavailable, not as a false PASS."""
    try:
        return bool(COMPONENT_TESTS[name](execution))
    except (KeyError, TypeError, ValueError, AttributeError):
        return False


COMPONENT_TESTS = {
    "EXPLICIT_IDENTITY_PRESERVING_MOVE": lambda ex: (
        ex["g006"]["production_g006_executed"] is True
        and ex["g006"]["identity_preserved"] is True
        and ex["g006"]["serialization_order_independent"] is True
        and ex["g006"]["authored_semantic_id"] == runner.SEMANTIC_ID
        and ex["g006"]["current_carrier"] == runner.AFTER
        and set(ex["g006"]["historical_carriers"]) == {runner.BEFORE, runner.AFTER}
    ),
    "AFFECTED_VIEW_REFRESH_SELECTED": lambda ex: (
        ex["g013"]["production_g013_g009_executed"] is True
        and ex["g013"]["affected_view"] == runner.VIEW_ID
        and ex["g013"]["selection_reason"] ==
            [[runner.VIEW_ID, "DEPENDENCY_BINDING_CHANGED"]]
    ),
    "INCREMENTAL_EQUALS_CURRENT_FULL_BUILD": lambda ex: (
        ex["g013"]["production_g013_g009_executed"] is True
        and ex["g013"]["selected_equals_full"] is True
        and source_digest(ex["g013"]["generated_current_view_sha256"])
        and source_digest(ex["g013"]["current_manifest_sha256"])
    ),
    "STALE_DERIVED_RESULT_NOT_GOVERNING": lambda ex: (
        ex["g013"]["previous_manifest"] == "STALE"
        and ex["g013"]["current_manifest"] == "FRESH"
        and ex["g013"]["G010_fixture_used_only_as_execution_prerequisite"] is True
        and ex["g013"]["whole_ADS_corpus_G013_claimed"] is False
    ),
}


def exact_git_file(commit: str, path: str, expected_digest: str) -> bytes:
    """Read exact source bytes from Git, rejecting substituted current files."""
    proc = subprocess.run(
        ["git", "show", f"{commit}:{path}"],
        cwd=ROOT, capture_output=True,
    )
    if proc.returncode or sha256(proc.stdout).hexdigest() != expected_digest:
        raise ValueError("P03_J3_EXACT_SOURCE_GIT_DIGEST_MISMATCH")
    return proc.stdout


def validate_j1(world: dict[str, Any]) -> tuple[list[str], dict[str, Any]]:
    """Prove owner-accepted S0, S1 and lifecycle predicates are unchanged."""
    if (
        world.get("schema_version") != 1
        or world.get("world_id") != accepted_j1.EXPERIMENT_ID
        or world.get("accepted_j1", {}).get("count") != 4
        or world.get("owner_decision", {}).get("verdict") != "ACCEPT"
        or world.get("scope") != "EXPERIMENT_ONLY_NON_OPERATIONAL"
        or world["accepted_j1"].get("current_effect_ids") != [E01, E04]
        or world.get("owner_decision", {}).get("binding_file_sha256") !=
            accepted_j1.BINDING_FILE_SHA256
        or world.get("owner_decision", {}).get("independently_cryptographically_authenticated") is not False
        or world["accepted_j1"].get("dormant_until_source_revision") != [E02]
        or world["currentness"]["activation_status"] != "NOT_ACTIVATED"
        or world["currentness"]["actual_source_revision_qualified"] is not False
        or world["j2"]["qualified_count"] != 0
        or world["j3"]["satisfaction_certified"] is not False
        or world["production_migration_authorized"] is not False
    ):
        raise ValueError("P03_J3_ORIGINAL_ACCEPTED_J1_OR_S0_TAMPERED")
    effects = world["accepted_j1"]["effects"]
    if (
        [e["id"] for e in effects] != list(accepted_j1.EXPECTED_IDS)
        or [e["type"] for e in effects] !=
            ["REQUIRE", "REQUIRE", "LIFECYCLE", "PROHIBIT"]
        or effects[0]["accounting"] != "REALIZATION_TRACKED"
        or effects[0]["completion_contract"] != {
            "actual_natural_owner_covers_required": True,
            "composition": "ALL_REQUIRED",
            "exact_source_revision_and_executed_evidence_required": True,
            "required_components": [
                "EXPLICIT_IDENTITY_PRESERVING_MOVE",
                "HISTORICAL_CARRIER_REMAINS_RESOLVABLE",
            ],
        }
        or effects[1]["accounting"] != "REALIZATION_TRACKED"
        or effects[1]["completion_contract"] != {
            "actual_natural_owner_covers_required": True,
            "composition": "ALL_REQUIRED",
            "exact_source_revision_and_executed_evidence_required": True,
            "required_components": list(runner.COMPONENTS),
        }
        or effects[2]["lineage"] != {
            "predecessor_id": E01,
            "successor_id": E02,
            "relation": "REPLACE",
            "realization_succession": "OPEN_RESET",
            "transition_not_activated_by_this_proposal": True,
        }
        or effects[2]["accounting"] != "NO_REALIZATION_REQUIRED"
        or effects[3]["accounting"] != "NO_REALIZATION_REQUIRED"
        or effects[3]["standing_check"] !=
           "DETECTIVE_ONLY_FALSE_AUTHORITY_REJECTION"
        or world["currentness"]["on_future_qualified_activation"] != {
            "retired_current_requirement": E01,
            "new_current_requirement": E02,
            "realization_successor_initialization": "OPEN_RESET",
            "evidence_carryover_allowed": False,
        }
    ):
        raise ValueError("P03_J3_EFFECT_OR_OPEN_RESET_SEMANTICS_CHANGED")
    return list(effects[1]["completion_contract"]["required_components"]), effects[2]["lineage"]


def validate_j2(admitted: dict[str, Any]) -> None:
    """Inspect independently admitted source-relative J2, not author FULL flags."""
    if not isinstance(admitted, dict) or set(admitted) != {
        "schema_version", "status", "world_id", "fact_class", "relation",
        "accepted_effect_id", "realizer_id", "source_event_commit",
        "declaration_commit", "declaration_sha256", "scope_commit",
        "published_execution_commit", "published_execution_sha256",
        "assurance_class", "provenance_limit", "scope_limit",
        "qualified_experimental_relational_j2_count", "all_required_component_ids",
        "all_component_evidence_replayed", "one_fact_tuple_in_bounded_source_world",
        "previous_s0_execution_credited_to_s1", "prior_948_j2_upgraded",
        "independent_model_identity_proven", "production_j2_qualified",
        "s1_activated_by_this_j2_verifier", "j3_satisfied_by_this_j2_verifier",
        "formal_r0_p03_scored", "physical_target_selected",
    }:
        raise ValueError("P03_J3_J2_UNRECOGNIZED_OR_FORGED_AUTHORITY_FIELDS")
    if (
        admitted.get("schema_version") != 1
        or admitted.get("status") !=
           "QUALIFIED_SOURCE_RELATIVE_EXPERIMENTAL_J2_WEAK_ACTOR_ASSURANCE"
        or admitted.get("world_id") != accepted_j1.EXPERIMENT_ID
        or admitted.get("fact_class") != "RELATIONAL"
        or admitted.get("relation") != "COVERS"
        or admitted.get("accepted_effect_id") != E02
        or admitted.get("realizer_id") != runner.REALIZER
        or admitted.get("source_event_commit") != j2_admission.EVENT
        or admitted.get("scope_commit") != j2_admission.FREEZE
        or admitted.get("declaration_commit") != j2_admission.CLAIM_COMMIT
        or admitted.get("declaration_sha256") != j2_admission.CLAIM_SHA256
        or admitted.get("published_execution_commit") != EXECUTION_COMMIT
        or admitted.get("published_execution_sha256") != EXECUTION_SHA256
        or admitted.get("assurance_class") != j2_admission.ASSURANCE
        or admitted.get("provenance_limit") != "MODEL_ACTOR_NOT_INDEPENDENTLY_AUTHENTICATED"
        or admitted.get("scope_limit") !=
           "ONE_EXPERIMENTAL_COMPOSITE_REALIZER_NOT_PRODUCTION_G006_G013_OWNER"
        or admitted.get("physical_target_selected") is not False
        or admitted.get("qualified_experimental_relational_j2_count") != 1
        or admitted.get("all_required_component_ids") != list(runner.COMPONENTS)
        or admitted.get("all_component_evidence_replayed") is not True
        or admitted.get("one_fact_tuple_in_bounded_source_world") is not True
        or admitted.get("previous_s0_execution_credited_to_s1") is not False
        or admitted.get("prior_948_j2_upgraded") is not False
        or admitted.get("independent_model_identity_proven") is not False
        or admitted.get("production_j2_qualified") is not False
        or admitted.get("s1_activated_by_this_j2_verifier") is not False
        or admitted.get("j3_satisfied_by_this_j2_verifier") is not False
        or admitted.get("formal_r0_p03_scored") is not False
    ):
        raise ValueError("P03_J3_J2_NOT_SEPARATELY_QUALIFIED_OR_FALSE_AUTHORITY")


def validate_execution(execution: dict[str, Any]) -> None:
    """Require new exact source event evidence, independent of author claims."""
    if not isinstance(execution, dict) or set(execution) != {
        "schema_version", "status", "event", "realizer_id", "component_ids",
        "g006", "g013", "source_author_independently_authenticated",
        "postexecution_covers_admitted", "qualified_relational_j2",
        "s1_activated", "j3", "formal_R0_P03", "production_modified",
        "physical_architecture_selected",
    }:
        raise ValueError("P03_J3_EXECUTION_UNRECOGNIZED_OR_FORGED_AUTHORITY_FIELDS")
    if (
        execution.get("schema_version") != 1
        or execution.get("status") != "NEW_SOURCE_RELATIVE_G006_G013_OBSERVED_NOT_J2_CERTIFIED"
        or not isinstance(execution.get("event"), dict)
        or execution.get("event", {}).get("source_event_commit") != j2_admission.EVENT
        or execution["event"].get("freeze_commit") != j2_admission.FREEZE
        or execution["event"].get("before_sha256") != runner.BEFORE_SHA256
        or execution["event"].get("after_sha256") != j2_admission.AFTER_SHA256
        or execution["event"].get("intent_sha256") != j2_admission.INTENT_SHA256
        or execution["event"].get("changes") != [
            {"path": runner.AFTER, "status": "A"},
            {"path": runner.INTENT, "status": "A"},
            {"path": runner.BEFORE, "status": "D"},
        ]
        or execution.get("realizer_id") != runner.REALIZER
        or execution.get("component_ids") != list(runner.COMPONENTS)
        or execution.get("source_author_independently_authenticated") is not False
        or execution.get("postexecution_covers_admitted") is not False
        or execution.get("qualified_relational_j2") is not False
        or execution.get("s1_activated") is not False
        or not execution.get("j3", "").startswith("HOLD_")
        or execution.get("production_modified") is not False
        or execution.get("formal_R0_P03") != "INCOMPLETE"
        or execution.get("physical_architecture_selected") is not False
    ):
        raise ValueError("P03_J3_SOURCE_EXECUTION_EVENT_OR_FALSE_AUTHORITY")


def evaluate_snapshot(world: dict, admitted_j2: dict,
                      execution: dict) -> dict[str, Any]:
    """Pure J3 predicate with separate activation and requirement completion.

    S1 currentness changes only when the accepted policy's exact source event,
    semantic identity continuity and qualified J2 identify a successor. Then
    realization starts OPEN with zero predecessor credit. Four current-event
    component observations are individually evaluated; missing evidence
    yields HOLD rather than allowing claimed FULL to count.
    """
    required, lineage = validate_j1(world)
    validate_j2(admitted_j2)
    validate_execution(execution)
    if not check_component(required[0], execution):
        return {
            "activation_status": "HOLD_SOURCE_REVISION_IDENTITY_UNQUALIFIED",
            "current_effect_ids": [E01, E04],
            "s1_j3": "NOT_ACTIVATED",
            "s1_components": {k: False for k in required},
            "s1_open_reset": False,
            "previous_s0_evidence_carried": False,
        }

    checks = {name: check_component(name, execution) for name in required}
    qualified = all(checks.values()) and len(checks) == len(required)
    return {
        "activation_status": CURRENTNESS_STATUS,
        "previous_state": "S0_INITIAL",
        "current_state": "S1_SUCCESSOR_AFTER_REAL_SOURCE_REVISION",
        "current_effect_ids": [E02, E04],
        "retired_current_requirement": E01,
        "new_current_requirement": E02,
        "lineage_relation": lineage["relation"],
        "realization_succession": lineage["realization_succession"],
        "s1_open_reset": True,
        "initial_successor_component_credit": 0,
        "previous_s0_evidence_carried": False,
        "previous_s0_j3_not_backfilled": True,
        "s1_components": checks,
        "s1_component_count": sum(checks.values()),
        "s1_required_count": len(required),
        "s1_composition": "ALL_REQUIRED",
        "s1_j3": J3_PASS if qualified else J3_HOLD,
        "s1_j3_satisfied": qualified,
        "s1_assurance": j2_admission.ASSURANCE,
        "e04_path_or_generated_index_as_authority": False,
        "j1_authority_source": "EXACT_EXPERIMENT_ONLY_OWNER_ACCEPTED_J1_GIT_BINDING",
        "j2_authority_source": "SEPARATELY_QUALIFIED_EXPERIMENT_ONLY_SOURCE_RELATIVE_COVERS",
        "execution_evidence_source": SOURCE_EVIDENCE_ROLE,
        "independently_authenticated_model_actor": False,
        "production_j3_satisfied": False,
        "formal_b0_b4_scored": False,
        "physical_target_selected": False,
        "production_migration_authorized": False,
    }


def build() -> dict[str, Any]:
    """Reverify exact published sources and independent mechanical J2 result."""
    old_world = accepted_j1.build()
    raw_j2 = exact_git_file(
        ACCEPTED_J2_COMMIT, ACCEPTED_J2_RESULT_PATH, ACCEPTED_J2_RESULT_SHA256
    )
    raw_execution = exact_git_file(
        EXECUTION_COMMIT, EXECUTION_PATH, EXECUTION_SHA256
    )
    if (
        raw_j2 != j2_admission.OUTPUT.read_bytes()
        or raw_execution != runner.OUTPUT.read_bytes()
    ):
        raise ValueError("P03_J3_ACCEPTED_J2_OR_EXECUTION_WORKTREE_DRIFT")

    # A stored J2 result is not a self-authenticating authority token.
    # Run the separate verifier anew to check current implementation and
    # source evidence before materializing lifecycle state.
    observed_j2 = j2_admission.qualify()
    admitted = json.loads(raw_j2)
    if admitted != observed_j2:
        raise ValueError("P03_J3_ACCEPTED_J2_NOT_REPRODUCIBLE")
    execution = json.loads(raw_execution)
    evaluated = evaluate_snapshot(old_world, admitted, execution)
    if evaluated.get("s1_j3") != J3_PASS:
        raise RuntimeError("P03_J3_S1_EXPERIMENTAL_ALL_REQUIRED_NOT_SATISFIED")
    return {
        "schema_version": 1,
        "status": "SEPARATE_EXPERIMENTAL_SOURCE_RELATIVE_J3_PREDICATE_PASS",
        "world_id": accepted_j1.EXPERIMENT_ID,
        "accepted_j1_commit": accepted_j1.PROPOSAL_COMMIT,
        "source_event_commit": j2_admission.EVENT,
        "relational_j2_source_commit": j2_admission.CLAIM_COMMIT,
        "relational_j2_admission_commit": ACCEPTED_J2_COMMIT,
        "relational_j2_admission_sha256": ACCEPTED_J2_RESULT_SHA256,
        "new_event_execution_commit": EXECUTION_COMMIT,
        "new_event_execution_sha256": EXECUTION_SHA256,
        "qualified_experiment_only_j2_count": 1,
        "source_relative_weak_assurance": True,
        "model_actor_independently_authenticated": False,
        "evaluator_mechanically_separate_from_source_claim": True,
        "evaluator_independently_authored_blind": False,
        "derived_semantics": evaluated,
        "formal_r0_p03": "INCOMPLETE",
        "physical_architecture_selected": False,
        "production_authority_activated": False,
    }


def main() -> None:
    result = build()
    raw = (json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False)
           + "\n").encode("utf8")
    if OUTPUT.exists():
        if OUTPUT.read_bytes() != raw:
            raise RuntimeError("P03_J3_IMMUTABLE_RESULT_CONFLICT")
    else:
        with OUTPUT.open("xb") as out:
            out.write(raw)
    print(json.dumps({
        "status": result["status"],
        "S1": result["derived_semantics"]["activation_status"],
        "J3": result["derived_semantics"]["s1_j3"],
        "production_J3": result["derived_semantics"]["production_j3_satisfied"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
