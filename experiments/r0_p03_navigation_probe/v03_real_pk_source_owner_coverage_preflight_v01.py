"""P03-V2 source-local prospective S0 COVERS declaration preflight.

The declaration is written by the exposed author of the experiment-local
carrier, not by the historical developer of G006 or G013 production code.
Exact source bytes, Git-bound realizer, exhaustive effect component naming,
and executed G006 identity behavior can be checked deterministically.

This is a mechanically valid RELATIONAL *candidate*. Qualification as
governing J2 requires a source-owner assurance rule and cannot be manufactured
from the model-authored validation code or the declaration's own flags. We
therefore do not certify J3, activate the S1 successor, score B0-B4, or change
the production Project Knowledge substrate.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_accepted_j1_projection_v01 as accepted,
    v03_real_pk_source_transition_v01 as transition,
)

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "real_pk_world/current/realizes_s0_v01.json"
OUTPUT = HERE / "v03_real_pk_source_owner_coverage_preflight_result_v01.json"
SOURCE_SHA256 = "4d0aa3cdcedc2f0c33ed81a8c11ecf743a3135c2c938205cb8d8a392bd265c2f"
EXPECTED_COMPONENTS = (
    "EXPLICIT_IDENTITY_PRESERVING_MOVE",
    "HISTORICAL_CARRIER_REMAINS_RESOLVABLE",
)
EXPECTED_REALIZER = "P03PKA.EXPERIMENT_SOURCE_CARRIER_TRANSITION_001"


def source_declaration() -> dict[str, Any]:
    """Verify the exact experimental source author's claim without accepting it."""
    if sha256(SOURCE.read_bytes()).hexdigest() != SOURCE_SHA256:
        raise ValueError("P03_SOURCE_OWNER_COVERS_SOURCE_DRIFT")
    data = json.loads(SOURCE.read_text("utf8"))
    if set(data) != {
        "schema_version", "world_id", "fact_class", "source_owner_claim",
        "source_owner_assurance", "natural_owner_carrier",
        "natural_owner_carrier_git_commit", "natural_owner_carrier_sha256",
        "realizer_id", "realizer_scope", "accepted_effect_id",
        "coverage_claim", "component_claims",
        "source_owner_declaration_status", "independently_authenticated_actor",
        "qualified_relational_j2", "j3_satisfaction_inferred",
        "predecessor_source_commit", "successor_j1_activation",
        "prohibited_inferences",
    }:
        raise ValueError("P03_COVERS_CLOSED_SOURCE_SHAPE_VIOLATED")
    if (
        data["schema_version"] != 1
        or data["world_id"] != accepted.EXPERIMENT_ID
        or data["fact_class"] != "RELATIONAL_SOURCE_LOCAL_COVERS_PROPOSAL_NOT_YET_QUALIFIED"
        or data["natural_owner_carrier"] != transition.REPLACEMENT_PATH
        or data["natural_owner_carrier_git_commit"] != transition.REPLACEMENT_COMMIT
        or data["natural_owner_carrier_sha256"] != transition.REPLACEMENT_SHA256
        or data["realizer_id"] != EXPECTED_REALIZER
        or data["realizer_scope"] != (
            "THIS_EXPERIMENT_SOURCE_REPRESENTATION_CHANGE_ONLY_NOT_HISTORICAL_G006_G013_CODE_OWNERSHIP"
        )
        or data["accepted_effect_id"] != accepted.EXPECTED_IDS[0]
        or data["coverage_claim"] != "FULL"
        or data["source_owner_claim"] != (
            "EXPOSED_CHATGPT_AUTHOR_OF_EXPERIMENT_SOURCE_CARRIER_AND_MOVE"
        )
        or data["source_owner_assurance"] != (
            "AT_ACTION_SOURCE_AUTHOR_ASSERTION_NOT_INDEPENDENTLY_AUTHENTICATED"
        )
        or data["source_owner_declaration_status"] != (
            "EXPLICIT_SOURCE_AUTHORED_PROPOSAL_PENDING_QUALIFICATION"
        )
        or data["independently_authenticated_actor"] is not False
        or data["qualified_relational_j2"] is not False
        or data["j3_satisfaction_inferred"] is not False
        or data["successor_j1_activation"] != "NOT_ACTIVATED"
        or data["predecessor_source_commit"] != transition.INITIAL_COMMIT
        or len(data["prohibited_inferences"]) != 7
    ):
        raise ValueError("P03_SOURCE_OWNER_RELATIONAL_SCOPE_OR_AUTHORITY_FALSIFIED")
    claims = data["component_claims"]
    if (
        not isinstance(claims, list)
        or tuple(x["id"] for x in claims) != EXPECTED_COMPONENTS
        or any(x["coverage"] != "FULL" for x in claims)
        or claims[0] != {
            "id": EXPECTED_COMPONENTS[0],
            "coverage": "FULL",
            "evidence_class": "OBSERVABLE_EXACT_GIT_AND_SOURCE_LOCAL_RELATION",
            "source_commit": transition.REPLACEMENT_COMMIT,
        }
        or claims[1] != {
            "id": EXPECTED_COMPONENTS[1],
            "coverage": "FULL",
            "evidence_class": "EXECUTED_PRODUCTION_G006_REPLAY",
            "source_result_sha256":
                "fc8a40c58fbacbd0be32f82ada6bbb1a92749f30e90d453f55dc961953b05d0d",
        }
    ):
        raise ValueError("P03_COVERS_COMPONENT_OR_SOURCE_EVIDENCE_MISMATCH")
    return data


def build() -> dict[str, Any]:
    """Cross-check accepted J1, real source revision and proposed owner claims."""
    owner = source_declaration()
    j1 = accepted.build()
    git_effect = transition.build()
    required = j1["accepted_j1"]["effects"][0]["completion_contract"]["required_components"]
    claimed = [x["id"] for x in owner["component_claims"]]
    if required != claimed:
        raise ValueError("P03_SOURCE_OWNER_COMPONENTS_NOT_ACCEPTED_J1")
    if not (
        git_effect["observed_source_revision"]["actual_source_replacement"]
        and git_effect["actual_g006_replay"]["continuity_preserved"]
        and len(git_effect["actual_g006_replay"]["historical_carrier_paths"]) == 2
        and git_effect["owner_relation"]["qualified_relational_j2_count"] == 0
    ):
        raise ValueError("P03_SOURCE_OWNER_COVERAGE_NO_REAL_OBSERVATION")
    return {
        "schema_version": 1,
        "world_id": accepted.EXPERIMENT_ID,
        "scope": "REAL_ADS_SOURCE_EXPERIMENT_NOT_PRODUCTION",
        "accepted_new_experiment_only_j1_count": 4,
        "required_component_ids": required,
        "observed_git_transition": {
            "initial_commit": transition.INITIAL_COMMIT,
            "replacement_commit": transition.REPLACEMENT_COMMIT,
            "semantic_identity": transition.AUTHORED_ID,
            "original_and_new_sources_verified": True,
        },
        "source_local_relational_declarations": [{
            "fact_class": owner["fact_class"],
            "realizer_id": owner["realizer_id"],
            "target_effect_id": owner["accepted_effect_id"],
            "component_ids": claimed,
            "reported_coverage": owner["coverage_claim"],
            "source_exact_sha256": SOURCE_SHA256,
            "source_owner": owner["source_owner_claim"],
            "source_owner_independently_authenticated": False,
            "qualified_as_governing_relational_j2": False,
        }],
        "source_observable_component_test_passed": True,
        "natural_owner_relational_declaration_source_exists": True,
        "qualified_relational_j2_count": 0,
        "j3": "HOLD_OWNER_RELATIONAL_QUALIFICATION",
        "s1_activation": "NOT_ACTIVATED",
        "formal_r0_p03": "INCOMPLETE",
        "physical_architecture_selected": False,
        "next": "QUALIFY_EXPERIMENT_SOURCE_OWNER_AUTHORITY_FOR_EXACT_COVERS_THEN_RUN_TRUE_G013_CURRENT_SOURCE_REFRESH",
    }


def main() -> None:
    result = build()
    content = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != content:
            raise RuntimeError("P03_SOURCE_OWNER_COVERS_PREFLIGHT_IMMUTABILITY_VIOLATION")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as f:
            f.write(content)
    print(json.dumps({
        "source_owner_claim_observed": result["natural_owner_relational_declaration_source_exists"],
        "source_observed": result["source_observable_component_test_passed"],
        "qualified_j2": result["qualified_relational_j2_count"],
        "j3": result["j3"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
