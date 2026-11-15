"""Add an actually executed G013 observation to the common P03-V2 world.

The canonical 19-original-source context and accepted experimental J1 remain
bound to the existing Research 685 preflight. The new G013 receipt describes
real Git-pinned carrier bytes *projected into a separately qualified isolated
temporary Git source root*, using the actual G009/G013 implementation.

A generated view remains a disposable derivative. Neither the technical
S1 component observations nor a colocated experimental carrier author's
unqualified COVERS proposal create a governing RELATIONAL J2, execute the
accepted S0->S1 successor, certify J3 or freeze formal B0-B4 arms/gold.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_common_world_preflight_v01 as base,
    v03_real_pk_g013_isolated_source_refresh_v01 as refresh,
    v03_real_pk_accepted_j1_projection_v01 as owner,
)

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "v03_real_pk_common_world_g013_overlay_result_v01.json"
BASE_SHA256 = "db9ca1a2ac337710637fa2a9bb9beecb5c8da701168b5333ee09f195608be42e"
REFRESH_SHA256 = "594eecaef1c770a3545ef2664dbe47df1c8fb74e069a7e2cd7f1a9cc230b50e2"


def read_exact(path: Path, expected: str) -> dict[str, Any]:
    data = path.read_bytes()
    if sha256(data).hexdigest() != expected:
        raise ValueError("P03_COMMON_WORLD_G013_SOURCE_RECEIPT_DIGEST_DRIFT")
    return json.loads(data.decode("utf8"))


def build() -> dict[str, Any]:
    """Combine source-verified semantically compatible receipts, not authority."""
    shared = read_exact(base.OUTPUT, BASE_SHA256)
    if shared != base.build():
        raise ValueError("P03_COMMON_WORLD_ORIGINAL_SOURCE_REGENERATION_DRIFT")
    observed = read_exact(refresh.OUTPUT, REFRESH_SHA256)
    if (
        shared["world_id"] != owner.EXPERIMENT_ID
        or shared["accepted_j1"]["accepted_effects"][1]["id"] != owner.EXPECTED_IDS[1]
        or shared["semantic_identity"]["authored_id"] != refresh.transition.AUTHORED_ID
        or shared["source_versions"]["initial_git_commit"] != refresh.transition.INITIAL_COMMIT
        or shared["source_versions"]["replacement_git_commit"] != refresh.transition.REPLACEMENT_COMMIT
        or shared["j2"]["qualified_relational_count"] != 0
        or shared["accepted_lineage_currentness"]["S1_activation"] != "NOT_ACTIVATED"
    ):
        raise ValueError("P03_COMMON_WORLD_G013_SEMANTIC_BASE_MISMATCH")
    role = observed["experimental_source"]
    if (
        observed["status"] != "ACTUAL_PRODUCTION_G013_REFRESH_ON_EXACT_REAL_SOURCE_PROJECTION_PASS"
        or role["original_git_before_commit"] != refresh.transition.INITIAL_COMMIT
        or role["original_git_after_commit"] != refresh.transition.REPLACEMENT_COMMIT
        or role["original_before_sha256"] != refresh.transition.INITIAL_SHA256
        or role["original_after_sha256"] != refresh.transition.REPLACEMENT_SHA256
        or observed["execution"]["G013_affected_view_ids"] != [refresh.VIEW]
        or observed["execution"]["incremental_exactly_equals_full_build"] is not True
        or observed["execution"]["previous_manifest_currentness"] != "STALE"
        or observed["execution"]["current_manifest_currentness"] != "FRESH"
    ):
        raise ValueError("P03_G013_EXECUTED_SOURCE_RESULT_NOT_COMPATIBLE_WITH_COMMON_WORLD")
    requirements = shared["accepted_j1"]["accepted_effects"][1]["completion_contract"]["required_components"]
    actual = observed["component_observations_not_gov_j2"]
    if (
        requirements != [x["component"] for x in actual]
        or any(x["accepted_effect"] != owner.EXPECTED_IDS[1] for x in actual)
        or any(x["qualified_governing_j2"] is not False for x in actual)
    ):
        raise ValueError("P03_G013_COMPONENTS_NOT_BINDING_TO_ACCEPTED_S1")
    if (
        observed["authority"]["S1_accepted_transition_activated"] is not False
        or observed["authority"]["source_owner_relational_J2_qualified"] is not False
        or observed["authority"]["J3_satisfaction_certified"] is not False
    ):
        raise ValueError("P03_G013_UNQUALIFIED_AUTHORITY_PROMOTED")
    return {
        "schema_version": 1,
        "world_id": owner.EXPERIMENT_ID,
        "world_status": "REAL_COMMON_V03_SOURCE_WORLD_G006_G013_OBSERVATIONS_J2_J3_HOLD",
        "source_of_truth": {
            "accepted_j1": shared["accepted_j1"],
            "source_roles_and_revisions": shared["original_project_source_catalog"],
            "identity": shared["semantic_identity"],
            "source_versions": shared["source_versions"],
            "lineage_currentness": shared["accepted_lineage_currentness"],
            "J2": shared["j2"],
            "J3": shared["j3"],
            "root_common_world_sha256": BASE_SHA256,
        },
        "G013_executed_observations": {
            "receipt_sha256": REFRESH_SHA256,
            "source_role": "ACTUAL_REAL_GIT_CARRIER_PROJECTION_IN_SEPARATE_ISOLATED_G010_SUPPORT_ROOT",
            "source_identity_transition": observed["source_projection"],
            "view_id": refresh.VIEW,
            "affected_view_ids": observed["execution"]["G013_affected_view_ids"],
            "incremental_full_build_equal": True,
            "old_manifest_stale": True,
            "current_manifest_fresh": True,
            "component_evidence_without_J2_qualification": actual,
            "fixture_is_experiment_support_not_primary_navigation_corpus": True,
        },
        "qualification": {
            "new_PKA_experiment_only_J1_accepted": 4,
            "S0_current": True,
            "S1_accepted_but_dormant": True,
            "S1_lineage_activated": False,
            "qualified_natural_owner_RELATIONAL_J2": 0,
            "J3_certified": False,
            "all_19_original_ADS_sources_admitted_as_one_G013_root": False,
            "B0_B4_navigation_arms_frozen": False,
            "protected_primary_tasks_originated": False,
            "neutral_legacy_nine_rejudged_under_current_method": False,
            "formal_P03_comparison_scored": False,
            "physical_architecture_selected": False,
        },
        "next_critical_path": [
            "FINITE_QUALIFICATION_OF_EXPERIMENT_CARRIER_NATURAL_OWNER_COVERS_PROVENANCE",
            "GOVERNED_S1_SOURCE_STATE_ACTIVATION_ONLY_AFTER_QUALIFIED_TRANSITION",
            "J3_EVALUATION_AND_OPEN_RESET_NONCARRY_WITH_EXPLICIT_UNKNOWN_NEGATIVES",
            "NEUTRAL_REAL_ADS_CORPUS_SPLIT_AND_ARM_FREEZE",
            "INDEPENDENT_REFERENCE_ORIGINATION_LEGACY_NINE_AND_ONE_FORMAL_P03_RUN",
        ],
    }


def main() -> None:
    result = build()
    rendered = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != rendered:
            raise RuntimeError("P03_COMMON_G013_OVERLAY_IMMUTABILITY_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(rendered)
    print(json.dumps({
        "world_status": result["world_status"],
        "real_source_paths": result["source_of_truth"]["source_roles_and_revisions"]["distinct_original_git_paths"],
        "S1_component_observations": len(result["G013_executed_observations"]["component_evidence_without_J2_qualification"]),
        "qualified_J2": result["qualification"]["qualified_natural_owner_RELATIONAL_J2"],
        "J3": result["qualification"]["J3_certified"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
