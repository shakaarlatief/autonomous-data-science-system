"""R0-P03 J2 original-source evidence and natural-owner declaration preflight.

Read actual Git-observable facts, preserve a contemporaneous source attestation
as an assertion, and reject promotion to source-owner RELATIONAL COVERS without
a separately sourced declaration. Research 512 section 9 owns the distinction.
The new P03 J1 effects were accepted at Checkpoint 937; J2/J3 were not.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
from typing import Any

from experiments.r0_p03_navigation_probe import (
    v03_d1_accepted_semantic_projection_v01 as accepted,
)

ROOT = Path(__file__).resolve().parents[2]
RESULT = Path(__file__).with_name("v03_j2_natural_owner_evidence_result_v01.json")
E01 = "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT"
CORRECTION = "73f54c6a96b7a9172376b4c88deb9a5a400506d0"
ACTION = "cd0cf087a4d0ddb30920a8c753e478da8f92295c"
ORIGINAL_PIN = accepted.original.PIN
CLAUDE_MESSAGE = accepted.original.MESSAGE_018
CLAUDE_AUTHOR_ROLE = "CLAUDE_MESSAGE018_AUTHOR_IN_ORIGINAL_SOURCE"
CLAUDE_AUTHOR_LINE = "Author / collaborator           Claude"
CLAUDE_TRANSPORT_LINE = "Transport                       Claude-side GitHub connector (Research 485)"
REQUIRED = (
    "TRANSPORT_ATTESTED_GITHUB_CONNECTOR",
    "AUTHORIZED_PATH_ONLY",
    "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD",
)
EVIDENCE_IDS = frozenset({"J2OBS-D1-GIT-PATH", "J2ASSERT-D1-CLAUDE-TRANSPORT"})
PROVIDER_CLAIMS = frozenset({
    "ATTESTED_OWN_GITHUB_CONNECTOR",
    "CANNOT_CONFIRM_TRANSPORT",
    "CONTRADICTS_PREVIOUS_TRANSPORT_ASSERTION",
})
DECLARATION_FIELDS = frozenset({
    "schema_version", "declaration_kind", "natural_owner_role",
    "owner_source_carrier", "owner_source_commit", "owner_source_sha256",
    "target_effect_id", "accepted_packet_sha256", "relation",
    "covered_components", "coverage_extent", "source_evidence_ids",
    "provider_transport_claim", "remaining_uncertainties",
})


def canonical_digest(value: Any) -> str:
    """Content digest for a declared candidate, not an owner's signature."""
    return sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
    ).encode("utf8")).hexdigest()


def git(*args: str) -> bytes:
    """Read original immutable Git source, with explicit command result check."""
    result = subprocess.run(["git", *args], cwd=ROOT, capture_output=True)
    if result.returncode != 0:
        raise ValueError("REQUIRED_ORIGINAL_GIT_EVIDENCE_UNAVAILABLE")
    return result.stdout


def original_message_exact() -> dict:
    """Verify original author/transport text and independently observed Git facts."""
    data = git("show", f"{ORIGINAL_PIN}:{CLAUDE_MESSAGE}")
    text = data.decode("utf8")
    for required in (CLAUDE_AUTHOR_LINE, CLAUDE_TRANSPORT_LINE):
        if text.count(required) != 1:
            raise ValueError("ORIGINAL_SOURCE_AUTHOR_OR_TRANSPORT_ATTESTATION_DRIFT")
    parent = git("show", "-s", "--format=%P", ACTION).decode("ascii").strip()
    paths = git("diff-tree", "--no-commit-id", "--name-only", "-r", ACTION).decode("utf8").splitlines()
    if parent != CORRECTION or paths != [CLAUDE_MESSAGE]:
        raise ValueError("ACTUAL_GIT_PARENT_OR_CHANGED_PATH_CONFLICT")
    original = git("show", f"{ACTION}:{CLAUDE_MESSAGE}")
    if original != data:
        raise ValueError("SOURCE_MESSAGE_CHANGED_FROM_INITIAL_ACTION")
    packet = accepted.pinned_owner_packet()
    source = {s["source_path"]: s for s in packet["source_manifest"]}[CLAUDE_MESSAGE]
    oid = git("rev-parse", f"{ACTION}:{CLAUDE_MESSAGE}").decode("ascii").strip()
    if (
        len(data) != source["byte_count"]
        or sha256(data).hexdigest() != source["sha256"]
        or oid != source["git_blob_oid"]
    ):
        raise ValueError("ORIGINAL_OWNER_MESSAGE_BLOB_NOT_FROZEN")
    lines = text.splitlines()
    return {
        "source_path": CLAUDE_MESSAGE,
        "source_commit": ORIGINAL_PIN,
        "action_commit": ACTION,
        "action_parent": parent,
        "changed_paths": paths,
        "git_blob_oid": oid,
        "source_sha256": sha256(data).hexdigest(),
        "author_claim_line": next(i for i, s in enumerate(lines, 1) if CLAUDE_AUTHOR_LINE in s),
        "transport_attestation_line": next(i for i, s in enumerate(lines, 1) if CLAUDE_TRANSPORT_LINE in s),
        "natural_owner_role_claim": CLAUDE_AUTHOR_ROLE,
        "role_assurance": "SOURCE_REPORTED_AUTHOR_NOT_INDEPENDENTLY_AUTHENTICATED",
        "transport_assurance": "SOURCE_REPORTED_CLAUDE_CONNECTOR_NOT_PROVIDER_VERIFIED",
    }


def actual_component_evidence() -> dict:
    """Compute three source-relative components against owner-accepted J1."""
    world = accepted.build_accepted_projection()
    effects = [e for e in world["accepted_j1"]["effects"] if e["accepted_effect_id"] == E01]
    if len(effects) != 1 or effects[0]["type"] != "REQUIRE":
        raise ValueError("ACCEPTED_E01_EFFECT_ID_OR_TYPE_CHANGED")
    contract = effects[0]["completion_contract"]
    if (
        tuple(contract["required_components"]) != REQUIRED
        or contract["composition_rule"] != "ALL_REQUIRED"
        or contract["qualification_required"] is not True
        or contract["evidence_required"] is not True
        or contract["activation_required"] is not False
    ):
        raise ValueError("ACCEPTED_E01_COMPLETION_CONTRACT_CHANGED")
    source = original_message_exact()
    return {
        "effect_id": E01,
        "source_owner": source,
        "accepted_packet_sha256": accepted.REVIEW_CANONICAL_SHA256,
        "required_components": list(REQUIRED),
        "component_evidence": {
            REQUIRED[0]: {
                "source_class": "SOURCE_REPORTED_EPHEMERAL_ACTION_ATTESTATION",
                "evidence_id": "J2ASSERT-D1-CLAUDE-TRANSPORT",
                "status": "ATTESTED_BY_SOURCE",
                "provider_transport_proof": "UNKNOWN_NOT_IN_GIT",
                "natural_owner_relational_coverage": "NOT_DECLARED_FOR_P03",
                "source": CLAUDE_MESSAGE,
                "source_sha256": source["source_sha256"],
            },
            REQUIRED[1]: {
                "source_class": "OBSERVABLE_GIT_CHANGESET",
                "evidence_id": "J2OBS-D1-GIT-PATH",
                "status": "VERIFIED_GIT",
                "natural_owner_relational_coverage": "NOT_DECLARED_FOR_P03",
                "source": ACTION,
                "value": [CLAUDE_MESSAGE],
            },
            REQUIRED[2]: {
                "source_class": "OBSERVABLE_GIT_PARENT",
                "evidence_id": "J2OBS-D1-GIT-PATH",
                "status": "VERIFIED_GIT",
                "natural_owner_relational_coverage": "NOT_DECLARED_FOR_P03",
                "source": ACTION,
                "value": CORRECTION,
            },
        },
    }


def validate_candidate_declaration(candidate: dict, facts: dict) -> str:
    """Validate proposed COVERS scope, without authentication or J2 admission.

    No candidate exists yet. This prepares a strictly typed contract for an
    actual later natural-owner declaration, rather than inventing the claim.
    """
    if not isinstance(candidate, dict) or set(candidate) != DECLARATION_FIELDS:
        raise ValueError("SOURCE_OWNER_DECLARATION_SCHEMA_OR_AUTHORITY_INJECTION")
    if candidate["schema_version"] != 1 or candidate["declaration_kind"] != "EXPLICIT_NATURAL_OWNER_RELATIONAL_CLAIM":
        raise ValueError("NOT_AN_EXPLICIT_SOURCE_OWNER_RELATIONAL_CLAIM")
    if candidate["natural_owner_role"] != CLAUDE_AUTHOR_ROLE:
        raise ValueError("CLAIMED_SOURCE_OWNER_ROLE_INCORRECT")
    if candidate["owner_source_carrier"] != CLAUDE_MESSAGE or candidate["owner_source_commit"] != ORIGINAL_PIN:
        raise ValueError("DECLARATION_ORIGINAL_SOURCE_CARRIER_OR_COMMIT_CHANGED")
    if candidate["owner_source_sha256"] != facts["source_owner"]["source_sha256"]:
        raise ValueError("DECLARATION_SOURCE_DIGEST_CHANGED")
    if candidate["accepted_packet_sha256"] != accepted.REVIEW_CANONICAL_SHA256:
        raise ValueError("DECLARATION_ACCEPTED_J1_PACKET_CHANGED")
    if candidate["target_effect_id"] != E01 or candidate["relation"] != "COVERS":
        raise ValueError("UNAUTHORIZED_EFFECT_OR_RELATION")
    components = candidate["covered_components"]
    if (
        not isinstance(components, list) or not components
        or not all(isinstance(c, str) for c in components)
        or len(set(components)) != len(components)
        or not set(components) <= set(REQUIRED)
    ):
        raise ValueError("DECLARATION_COMPONENTS_UNKNOWN_DUPLICATE_OR_EMPTY")
    extent = "FULL" if set(components) == set(REQUIRED) else "PARTIAL"
    if candidate["coverage_extent"] != extent:
        raise ValueError("DECLARATION_COVERAGE_EXTENT_INCORRECT")
    refs = candidate["source_evidence_ids"]
    if (
        not isinstance(refs, list) or not refs
        or not all(isinstance(r, str) for r in refs)
        or len(set(refs)) != len(refs)
        or not set(refs) <= EVIDENCE_IDS
    ):
        raise ValueError("DECLARATION_EVIDENCE_IDS_UNKNOWN_OR_DUPLICATE")
    if candidate["provider_transport_claim"] not in PROVIDER_CLAIMS:
        raise ValueError("UNRECOGNIZED_PROVIDER_TRANSPORT_CLAIM")
    unknowns = candidate["remaining_uncertainties"]
    if (
        not isinstance(unknowns, list)
        or not all(isinstance(x, str) and 0 < len(x) <= 512 for x in unknowns)
        or len(set(unknowns)) != len(unknowns)
    ):
        raise ValueError("DECLARATION_UNCERTAINTIES_INVALID")
    return "STRUCTURALLY_VALID_SOURCE_OWNER_CLAIM_NOT_YET_AUTHENTICATED_OR_J2_QUALIFIED"


def assess_claims(candidates: list[dict], facts: dict) -> str:
    """Reject competing natural-owner tuples; do not install a governing fact."""
    if not isinstance(candidates, list):
        raise ValueError("INVALID_SOURCE_OWNER_DECLARATION_SET")
    seen = set()
    for candidate in candidates:
        validate_candidate_declaration(candidate, facts)
        for component in candidate["covered_components"]:
            key = (candidate["target_effect_id"], component)
            if key in seen:
                raise ValueError("CONFLICTING_DUPLICATE_NATURAL_OWNER_FACT_TUPLE")
            seen.add(key)
    return "NO_SOURCE_OWNER_RELATIONAL_ADMISSION_PERFORMED"


def build() -> dict:
    facts = actual_component_evidence()
    accepted_world = accepted.build_accepted_projection()
    if accepted_world["j2_evidence"]["qualified_relational_count"] != 0:
        raise ValueError("UNEXPECTED_ALREADY_ADMITTED_J2")
    assessment = assess_claims([], facts)
    return {
        "schema_version": 1,
        "status": "J2_SOURCE_FACTS_VERIFIED_RELATIONAL_OWNER_DECLARATION_PENDING",
        "scope": "EXPERIMENT_ONLY_UNSCORED",
        "source_commit": ORIGINAL_PIN,
        "target_effect_id": E01,
        "accepted_j1_count": accepted_world["accepted_j1"]["count"],
        "accepted_packet_sha256": facts["accepted_packet_sha256"],
        "natural_owner_source": facts["source_owner"],
        "required_components": facts["required_components"],
        "component_evidence": facts["component_evidence"],
        "git_verified_components": 2,
        "source_attested_transport_components": 1,
        "provider_verified_transport_components": 0,
        "qualified_relational_components": [],
        "new_natural_owner_declarations_observed": 0,
        "natural_owner_relation_assessment": assessment,
        "j3_satisfaction": "HOLD_J2_NATURAL_OWNER_QUALIFICATION",
        "j3_completion_certified": False,
        "lineage_relation": "REPLACE",
        "lineage_realization_succession": "OPEN_RESET",
        "predecessor_realization_autocarried": False,
        "standing_prohibition_compliance": "NOT_INDEPENDENTLY_DEMONSTRATED",
        "authorization_exercise": "GIT_SCOPED_ACTION_OBSERVED_PROVIDER_TRANSPORT_ATTESTED_ONLY",
        "next_required_source": (
            "Original Claude Message018 author must independently declare any "
            "P03-E01 COVERS relationship, with named components and uncertainty; "
            "a separately qualified source-provenance process must verify it"
        ),
        "formal_p03_score": None,
        "physical_target_selected": False,
    }


def main() -> None:
    result = build()
    raw = json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    if RESULT.exists():
        if RESULT.read_text("utf8") != raw:
            raise RuntimeError("J2_RECEIPT_IMMUTABILITY_CONFLICT")
    else:
        with RESULT.open("x", encoding="utf8", newline="\n") as file:
            file.write(raw)
    print(json.dumps({
        "status": result["status"],
        "git_verified": result["git_verified_components"],
        "transport_attested": result["source_attested_transport_components"],
        "qualified_relational": len(result["qualified_relational_components"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
