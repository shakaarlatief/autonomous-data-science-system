"""Shared R0-P03-V2 real-source V03 semantic-world preflight, not formal arm freeze.

Composes the exact accepted experiment-only J1 scope, actual Git-backed
G006 identity continuity, explicit source-local J2 candidate, and original
Git-pinned Project Knowledge source catalog into ONE common non-scored world.

All B0-B4 arms must receive the same J1/evidence/source-role/identity/
lineage/currentness/J2/J3 base. The arms may add only navigation organization
or retrieval treatments, and may not promote generated rankings to authority.

The world remains pre-admission: no qualified RELATIONAL J2, no S1 activated
state, no complete J3; no 60/20 representative freeze, independent twelve
primary tasks, neutral nine or blinded scoring. An accurate HOLD is a useful
semantic result, never proof of experiment viability.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as j1,
    v03_real_pk_semantic_candidate_audit_v01 as audit,
    v03_real_pk_source_transition_v01 as movement,
    v03_real_pk_source_owner_coverage_preflight_v01 as j2,
    v03_real_content_source_frame_v01 as original,
)

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_real_pk_common_world_preflight_result_v01.json"
EXISTING_AUDIT = audit.OUTPUT
AUDIT_SHA256 = "59de22c2709d380189d60cab305902bff7033f9453cd5687223abe58805f56ac"
BASE = original.OUTPUT


def _original_source_records() -> list[dict[str, Any]]:
    """Preserve original Git source-revision and role, with no authority promotion."""
    if sha256(EXISTING_AUDIT.read_bytes()).hexdigest() != AUDIT_SHA256:
        raise ValueError("COMMON_WORLD_ORIGINAL_CANDIDATE_AUDIT_DRIFT")
    current = json.loads(EXISTING_AUDIT.read_text("utf8"))
    if current != audit.evaluate():
        raise ValueError("COMMON_WORLD_ORIGINAL_GIT_WITNESSES_NOT_REGENERABLE")
    baseline = original.build()
    if baseline != json.loads(BASE.read_text("utf8")):
        raise ValueError("COMMON_WORLD_OLD_BASE_SOURCE_WITNESSES_NOT_REGENERABLE")
    rows: dict[str, dict[str, Any]] = {}
    for item in baseline["witnesses"]:
        path = item["source_path"]
        role = item["source_role_classification"]
        entry = rows.setdefault(path, {
            "source_path": path,
            "exact_source_commit": item["source_commit"],
            "git_blob_oid": item["git_blob_oid"],
            "sha256": item["sha256"],
            "source_roles": [],
            "evidence_class": "ORIGINAL_SOURCE_OBSERVABLE_WITHOUT_NEW_J1_J2",
        })
        if (entry["sha256"], entry["git_blob_oid"]) != (
            item["sha256"], item["git_blob_oid"]
        ):
            raise ValueError("COMMON_WORLD_SAME_PATH_WITH_CONFLICTING_GIT_REVISION")
        entry["source_roles"].append(role)
    for item in current["additional_candidate_witnesses"]:
        path = item["source_path"]
        role = item["source_role"]
        entry = rows.setdefault(path, {
            "source_path": path,
            "exact_source_commit": item["source_commit"],
            "git_blob_oid": item["original_git_blob"],
            "sha256": item["original_sha256"],
            "source_roles": [],
            "evidence_class": "ORIGINAL_SOURCE_OBSERVABLE_WITHOUT_NEW_J1_J2",
        })
        if (entry["sha256"], entry["git_blob_oid"]) != (
            item["original_sha256"], item["original_git_blob"]
        ):
            raise ValueError("COMMON_WORLD_SAME_PATH_WITH_CONFLICTING_GIT_REVISION")
        entry["source_roles"].append(role)
    if len(rows) != 19:
        raise ValueError("COMMON_WORLD_ORIGINAL_SOURCE_COUNT_DRIFT")
    for entry in rows.values():
        entry["source_roles"] = sorted(set(entry["source_roles"]))
    return [rows[p] for p in sorted(rows)]


def build() -> dict[str, Any]:
    """Create one exact common-information contract, without scoring an arm."""
    accepted = j1.build()
    observed = movement.build()
    candidate = j2.build()
    original_sources = _original_source_records()
    if (
        accepted["accepted_j1"]["count"] != 4
        or candidate["accepted_new_experiment_only_j1_count"] != 4
        or candidate["qualified_relational_j2_count"] != 0
        or observed["owner_relation"]["qualified_relational_j2_count"] != 0
        or observed["actual_g006_replay"]["continuity_preserved"] is not True
        or accepted["currentness"]["activation_status"] != "NOT_ACTIVATED"
        or candidate["s1_activation"] != "NOT_ACTIVATED"
        or accepted["j3"]["satisfaction_certified"] is not False
    ):
        raise ValueError("COMMON_WORLD_SUBSTRATE_J1_J2_J3_ROLE_COLLISION")
    common = {
        "schema_version": 1,
        "world_id": j1.EXPERIMENT_ID,
        "scope": "R0_P03_V2_REAL_PROJECT_KNOWLEDGE_SOURCE_WORLD_EXPERIMENT_ONLY",
        "world_status": "ONE_REAL_SOURCE_COMMON_SEMANTIC_PREFLIGHT_J2_J3_HOLD_NOT_FROZEN",
        "original_project_source_catalog": {
            "source_pin": original.PIN,
            "distinct_original_git_paths": len(original_sources),
            "sources": original_sources,
            "all_original_source_roles_are_evidence_not_new_governing_effects": True,
        },
        "accepted_j1": {
            "accepted_effects": accepted["accepted_j1"]["effects"],
            "current_effect_ids": accepted["accepted_j1"]["current_effect_ids"],
            "dormant_successor_effect_ids": accepted["accepted_j1"]["dormant_until_source_revision"],
            "acceptance_class": accepted["owner_decision"]["provenance"],
            "original_review_commit": j1.PROPOSAL_COMMIT,
        },
        "semantic_identity": {
            "authored_id": movement.AUTHORED_ID,
            "current_source": movement.REPLACEMENT_PATH,
            "historical_sources": observed["actual_g006_replay"]["historical_carrier_paths"],
            "continuity_observed_by_g006": True,
            "current_lookup_does_not_derive_from_path": True,
        },
        "source_versions": {
            "initial_git_commit": movement.INITIAL_COMMIT,
            "replacement_git_commit": movement.REPLACEMENT_COMMIT,
            "original_source_sha256": movement.INITIAL_SHA256,
            "current_source_sha256": movement.REPLACEMENT_SHA256,
            "relation": movement.RELATION,
            "git_paths_exact_verified": True,
        },
        "accepted_lineage_currentness": {
            "accepted_rule": accepted["currentness"]["accepted_transition_rule"],
            "active_state": "S0_INITIAL",
            "S1_activation": "NOT_ACTIVATED",
            "successor_realization_evidence_carryover": "FORBIDDEN_BY_OPEN_RESET",
            "actual_git_revision_does_not_automatically_qualify_s1": True,
        },
        "j2": {
            "observable": {
                "git_source_history_verified": True,
                "identity_continuity_and_history_executed_in_g006": True,
            },
            "source_local_relational_candidates_not_admitted":
                candidate["source_local_relational_declarations"],
            "qualified_relational": [],
            "qualified_relational_count": 0,
        },
        "j3": {
            "S0": "HOLD_UNQUALIFIED_SOURCE_OWNER_RELATION",
            "S1": "NOT_ACTIVATED",
            "completion_certified": False,
        },
        "shared_arm_input": {
            "identical_mandatory_information_for_B0_B1_B2_B3_B4": True,
            "common_semantics": [
                "source_role_and_natural_owner_provenance",
                "exact_pinned_source_revision",
                "accepted_effect_ids_and_component_contracts",
                "lineage_and_currentness",
                "identity_and_historical_lookup",
                "J2_OBSERVABLE_RELATIONAL_EPHEMERAL_ASSURANCE",
                "J3_completion_or_explicit_HOLD",
                "lexical_full_text_and_derived_orientation_to_be_frozen",
            ],
            "no_arm_specific_index_authority": True,
            "arm_implementations_frozen": False,
        },
        "formality": {
            "sixty_build_twenty_heldout_or_fallback_frozen": False,
            "twelve_independent_primary_tasks_originated": False,
            "nine_neutral_legacy_reference_gold_frozen_under_current_method": False,
            "blinded_evaluators_assigned": False,
            "formal_B0_B4_scores": None,
            "physical_target_selected": False,
        },
        "remaining_qualification": [
            "SOURCE_OWNER_RELATIONAL_COVERS_ASSURANCE_FOR_EXPERIMENT_CARRIER",
            "SECOND_QUALIFIED_S1_SOURCE_REVISION_WITH_TRUE_G013_VIEW_REFRESH",
            "MECHANICAL_S0_S1_J3_AND_STALE_EVIDENCE_BEHAVIOR",
            "NEUTRAL_60_20_OR_DETERMINISTIC_3_1_SOURCE_FREEZE",
            "B0_B4_ARM_IMPLEMENTATION_PARITY_AND_LEGACY_INDEPENDENCE",
            "INDEPENDENT_TWELVE_PRIMARY_TASKS_PROTECTED_GOLD_TWO_EVALUATORS",
        ],
    }
    return common


def main() -> None:
    result = build()
    content = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("P03_REAL_COMMON_WORLD_IMMUTABILITY_VIOLATION")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as f:
            f.write(content)
    print(json.dumps({
        "status": result["world_status"],
        "original_sources": result["original_project_source_catalog"]["distinct_original_git_paths"],
        "accepted_effects": len(result["accepted_j1"]["accepted_effects"]),
        "qualified_relational_j2": result["j2"]["qualified_relational_count"],
        "formal": result["formality"]["formal_B0_B4_scores"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
