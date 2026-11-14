"""Experimental typed J2 source-owner and assurance port over two real events.

Research 512 section 9 owns the fact-kind distinction. Research 676 owns the
four accepted experiment-only D1 effects. Research 678 records a historical
source-owner CANNOT_ATTEST result and Research 679 records a real co-committed
ChatGPT actor claim with NO accepted governing target.

The module compiles *verified original Git objects* into a bounded input
world. An API caller cannot supply an "independently verified" Boolean and
thereby promote a source claim. The only implemented verifying backend is
the Git object verifier for two known historical event identities. No
natural-owner authentication or provider-native receipt verifier exists in
this experimental prototype. RELATIONAL and EPHEMERAL claims consequently
remain unqualified. This is NOT the production V03 predicate evaluator,
a replacement for its J3 grammar, or a formal B0-B4 scorer.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from hashlib import sha256
import json
from pathlib import Path
from typing import Any, Mapping

from experiments.r0_p03_navigation_probe import (
    v03_d1_accepted_semantic_projection_v01 as accepted,
    v03_j2_natural_owner_evidence_contract_v01 as historical_j2,
    v03_j2_091_response_reconciliation_v01 as historical,
    v03_forward_j2_at_action_evidence_probe_v01 as forward,
)

OUTPUT = Path(__file__).with_name("v03_typed_j2_assurance_port_result_v01.json")
EXPERIMENT_ONLY = "P03_V2_EXPOSED_UNSCORED_J2_PORT"
D1_EVENT = historical_j2.ACTION
FORWARD_EVENT = forward.ACTION_COMMIT
E01 = historical_j2.E01
REQUIRED = tuple(historical_j2.REQUIRED)
FORWARD_TARGET = forward.PROBE_ONLY_TARGET


class FactKind(str, Enum):
    OBSERVABLE = "OBSERVABLE"
    RELATIONAL = "RELATIONAL"
    EPHEMERAL = "EPHEMERAL"


class Disposition(str, Enum):
    VERIFIED_GIT_OBSERVABLE = "VERIFIED_GIT_OBSERVABLE"
    REJECT_SOURCE_IDENTITY = "REJECT_SOURCE_IDENTITY"
    REJECT_UNSUPPORTED_FACT_KIND = "REJECT_UNSUPPORTED_FACT_KIND"
    REJECT_UNSUPPORTED_ASSURANCE = "REJECT_UNSUPPORTED_ASSURANCE"
    HOLD_NO_ACCEPTED_TARGET = "HOLD_NO_ACCEPTED_TARGET"
    HOLD_NO_NATURAL_OWNER_AUTHENTICATION = "HOLD_NO_NATURAL_OWNER_AUTHENTICATION"
    HOLD_PROVIDER_RECEIPT_UNAVAILABLE = "HOLD_PROVIDER_RECEIPT_UNAVAILABLE"
    HOLD_SOURCE_ONLY_ATTESTATION = "HOLD_SOURCE_ONLY_ATTESTATION"


@dataclass(frozen=True)
class VerifiedGitObservation:
    """Source fact manufactured exclusively by rechecking original Git objects.

    Do not expose an API that constructs these from JSON-provided verification
    labels. A valid commit ID and exact original changed-path or parent
    observation can be independently reconstructed; provider usage cannot.
    """

    source_commit: str
    component_id: str
    source_owner: str
    value: str
    source_digest: str


@dataclass(frozen=True)
class SourceClaim:
    """Untrusted caller-supplied claim; every assurance label is only a claim."""

    kind: str
    source_commit: str
    component_id: str
    target_effect: str
    claimed_assurance: str
    claim_family: str


@dataclass(frozen=True)
class ProbeContext:
    """Only source-verified observations and exact accepted experiment target."""

    observations: tuple[VerifiedGitObservation, ...]
    accepted_effects: tuple[str, ...]
    natural_owner_authenticator_available: bool
    provider_native_receipt_verifier_available: bool


CLAIM_FIELDS = frozenset(
    {"kind", "source_commit", "component_id", "target_effect",
     "claimed_assurance", "claim_family"}
)
ALLOWED_ASSURANCE_CLAIMS = frozenset(
    {"DIRECT_GIT", "SOURCE_REPORTED", "ACTOR_AUTHORED", "UNVERIFIED"}
)

# These are *only* the exact real-source development inquiries already
# inspected in Research 677-679, not an extensible governing admission
# registry. An observed fact may not be relabeled as another effect's
# completion, even when both events are genuinely present in Git.
EXPECTED_INQUIRIES = {
    ("OBSERVABLE", D1_EVENT, "AUTHORIZED_PATH_ONLY"):
        (E01, "D1_GIT_PATH"),
    ("OBSERVABLE", D1_EVENT, "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD"):
        (E01, "D1_GIT_PARENT"),
    ("EPHEMERAL", D1_EVENT, "TRANSPORT_ATTESTED_GITHUB_CONNECTOR"):
        (E01, "D1_ACTION_CONNECTOR_USE_SOURCE_ASSERTION"),
    ("RELATIONAL", FORWARD_EVENT, "ACTOR_INTENT_PRESENT"):
        (FORWARD_TARGET, "FORWARD_COCOMMITTED_PROBE_ONLY_COVERS"),
    ("OBSERVABLE", FORWARD_EVENT, "FORWARD_COMMIT_PATH_EXACT"):
        (FORWARD_TARGET, "FORWARD_GIT_PATH"),
    ("OBSERVABLE", FORWARD_EVENT, "FORWARD_COMMIT_PARENT_EXACT"):
        (FORWARD_TARGET, "FORWARD_GIT_PARENT"),
    ("EPHEMERAL", FORWARD_EVENT, "PROVIDER_EXECUTED_CODEXLESS_COMMIT"):
        (FORWARD_TARGET, "FORWARD_RUNTIME_BRIDGE_TOOL_REPORT"),
}
EXPECTED_SOURCE_OBSERVATIONS = (
    VerifiedGitObservation(
        D1_EVENT, "AUTHORIZED_PATH_ONLY", "GIT_OBJECT_STORE",
        historical_j2.CLAUDE_MESSAGE,
        "890ea35d0e6ea99143e0918cb41ee93a8c28add9981d57add9f20dcc707cadaa",
    ),
    VerifiedGitObservation(
        D1_EVENT, "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD",
        "GIT_OBJECT_STORE", historical_j2.CORRECTION,
        "890ea35d0e6ea99143e0918cb41ee93a8c28add9981d57add9f20dcc707cadaa",
    ),
    VerifiedGitObservation(
        FORWARD_EVENT, "FORWARD_COMMIT_PATH_EXACT",
        "GIT_OBJECT_STORE", forward.ACTION_PATH, forward.ACTION_BLOB_SHA256,
    ),
    VerifiedGitObservation(
        FORWARD_EVENT, "FORWARD_COMMIT_PARENT_EXACT",
        "GIT_OBJECT_STORE", forward.ACTION_PARENT, forward.ACTION_BLOB_SHA256,
    ),
)


def canonical_sha(obj: Any) -> str:
    return sha256(
        json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf8")
    ).hexdigest()


def actual_source_context() -> ProbeContext:
    """Construct a context from immutable, re-verified evidence, never a blob label."""
    # Each function reopens the source from its exact original Git tree and
    # checks parent, path, source bytes, and the frozen owner-review digest.
    accepted_world = accepted.build_accepted_projection()
    old = historical_j2.original_message_exact()
    response_text, _ = historical.published_reply()
    disposition = historical.parse_disposition(response_text)
    record, live_git = forward.original_commit_data()

    if disposition["DISPOSITION"] != "CANNOT_ATTEST":
        raise ValueError("HISTORICAL_SOURCE_OWNER_STATUS_CHANGED")
    if (
        disposition["J2_QUALIFIED"] != "0"
        or disposition["J3_CERTIFIED"] != "false"
        or accepted_world["j2_evidence"]["qualified_relational_count"] != 0
        or accepted_world["j3"]["new_experimental_completion_certified"]
    ):
        raise ValueError("HISTORICAL_UNQUALIFIED_J2_WAS_PROMOTED")
    if record["governing_authority"] != "NONE_EXPERIMENT_ONLY_UNSCORED":
        raise ValueError("LIVE_SOURCE_FALSELY_GAINED_J1_AUTHORITY")
    if record["actor_statement"]["relational_claim"]["target"] != FORWARD_TARGET:
        raise ValueError("LIVE_ACTOR_CLAIM_TARGET_SCOPE_CHANGED")
    if live_git["event_commit"] != FORWARD_EVENT:
        raise ValueError("LIVE_GIT_ACTION_ID_CHANGED")

    effects = accepted_world["accepted_j1"]["effects"]
    effect_ids = tuple(effect["accepted_effect_id"] for effect in effects)
    if len(effect_ids) != 4 or E01 not in effect_ids:
        raise ValueError("EXACT_ACCEPTED_EXPERIMENT_EFFECT_SET_CHANGED")
    require = next(e for e in effects if e["accepted_effect_id"] == E01)
    contract = require["completion_contract"]
    if (
        tuple(contract["required_components"]) != REQUIRED
        or contract["composition_rule"] != "ALL_REQUIRED"
        or contract["qualification_required"] is not True
    ):
        raise ValueError("ACCEPTED_E01_REQUIREMENT_BOUNDARY_CHANGED")

    if old["changed_paths"] != [historical_j2.CLAUDE_MESSAGE]:
        raise ValueError("HISTORICAL_GIT_PATH_NOT_ACTUALLY_VERIFIED")
    if old["action_parent"] != historical_j2.CORRECTION:
        raise ValueError("HISTORICAL_GIT_PARENT_NOT_ACTUALLY_VERIFIED")
    if old["transport_assurance"] != "SOURCE_REPORTED_CLAUDE_CONNECTOR_NOT_PROVIDER_VERIFIED":
        raise ValueError("HISTORICAL_TRANSPORT_TEXT_EVIDENCE_CHANGED")

    source_digest = old["source_sha256"]
    observations = (
        VerifiedGitObservation(
            D1_EVENT, "AUTHORIZED_PATH_ONLY", "GIT_OBJECT_STORE",
            historical_j2.CLAUDE_MESSAGE, source_digest,
        ),
        VerifiedGitObservation(
            D1_EVENT, "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD",
            "GIT_OBJECT_STORE", historical_j2.CORRECTION, source_digest,
        ),
        VerifiedGitObservation(
            FORWARD_EVENT, "FORWARD_COMMIT_PATH_EXACT", "GIT_OBJECT_STORE",
            forward.ACTION_PATH, live_git["git_blob_sha256"],
        ),
        VerifiedGitObservation(
            FORWARD_EVENT, "FORWARD_COMMIT_PARENT_EXACT", "GIT_OBJECT_STORE",
            forward.ACTION_PARENT, live_git["git_blob_sha256"],
        ),
    )
    if len({(v.source_commit, v.component_id) for v in observations}) != len(observations):
        raise ValueError("CONFLICTING_DUPLICATE_VERIFIED_SOURCE_FACT")
    # The real accepted effects belong to the P03 development world only.
    # No source-author or provider verifier has been installed or run.
    return ProbeContext(
        observations=observations,
        accepted_effects=effect_ids,
        natural_owner_authenticator_available=False,
        provider_native_receipt_verifier_available=False,
    )


def normalize_claim(raw: Mapping[str, Any]) -> SourceClaim:
    """Validate exactly a claim; extra authoritative proof fields fail closed."""
    if not isinstance(raw, Mapping) or set(raw) != CLAIM_FIELDS:
        raise ValueError("TYPED_J2_CLAIM_SCHEMA_OR_AUTHORITY_SMUGGLING")
    if raw["kind"] not in {v.value for v in FactKind}:
        raise ValueError("TYPED_J2_CLAIM_KIND_UNKNOWN")
    if raw["claimed_assurance"] not in ALLOWED_ASSURANCE_CLAIMS:
        raise ValueError("TYPED_J2_UNSUPPORTED_CLAIMED_ASSURANCE")
    if any(
        not isinstance(raw[k], str) or not raw[k] or len(raw[k]) > 256
        for k in CLAIM_FIELDS
    ):
        raise ValueError("TYPED_J2_CLAIM_FIELD_VALUE_INVALID")
    if len(raw["source_commit"]) != 40 or any(
        c not in "0123456789abcdef" for c in raw["source_commit"]
    ):
        raise ValueError("TYPED_J2_SOURCE_COMMIT_ID_INVALID")
    return SourceClaim(**{k: raw[k] for k in (
        "kind", "source_commit", "component_id", "target_effect",
        "claimed_assurance", "claim_family",
    )})


def qualify_claim(claim: SourceClaim, context: ProbeContext) -> Disposition:
    """Conservative fact-class qualification, not the governing J3 predicate.

    A claimed assurance never grants trust. OBSERVABLE uses a constrained
    exact-source lookup; RELATIONAL cannot be qualified without a real
    accepted target *and* a separate natural-owner authenticator; EPHEMERAL
    cannot be qualified without a provider-native verification backend.
    Even if caller constructs a ProbeContext claiming capabilities, this
    prototype never implements the missing backends.
    """
    if claim.kind not in {v.value for v in FactKind}:
        return Disposition.REJECT_UNSUPPORTED_FACT_KIND
    if claim.claimed_assurance not in ALLOWED_ASSURANCE_CLAIMS:
        return Disposition.REJECT_UNSUPPORTED_ASSURANCE

    # In a production port these anchors would be resolved through a
    # qualified source adapter with a verifier-owned trust boundary. Here the
    # source scope is deliberately frozen to the two actual Git events. Caller
    # supplied context cannot extend the accepted effect or observation set.
    if (
        not isinstance(context, ProbeContext)
        or context.accepted_effects != accepted.EXPECTED_EFFECT_IDS
        or context.observations != EXPECTED_SOURCE_OBSERVATIONS
        or context.natural_owner_authenticator_available
        or context.provider_native_receipt_verifier_available
    ):
        return Disposition.REJECT_SOURCE_IDENTITY

    key = (claim.kind, claim.source_commit, claim.component_id)
    binding = EXPECTED_INQUIRIES.get(key)
    if binding is None or binding != (claim.target_effect, claim.claim_family):
        return Disposition.REJECT_SOURCE_IDENTITY

    if claim.kind == FactKind.OBSERVABLE.value:
        if claim.claimed_assurance != "DIRECT_GIT":
            return Disposition.REJECT_UNSUPPORTED_ASSURANCE
        if claim.target_effect not in context.accepted_effects:
            return Disposition.HOLD_NO_ACCEPTED_TARGET
        # The original-source compiler verified actual Git objects. A
        # forward event cannot be mapped to a different E01 effect.
        return Disposition.VERIFIED_GIT_OBSERVABLE

    if claim.kind == FactKind.RELATIONAL.value:
        if claim.claimed_assurance not in ("ACTOR_AUTHORED", "UNVERIFIED"):
            return Disposition.REJECT_UNSUPPORTED_ASSURANCE
        if claim.target_effect not in context.accepted_effects:
            return Disposition.HOLD_NO_ACCEPTED_TARGET
        return Disposition.HOLD_NO_NATURAL_OWNER_AUTHENTICATION

    if claim.claimed_assurance != "SOURCE_REPORTED":
        return Disposition.REJECT_UNSUPPORTED_ASSURANCE
    if claim.target_effect not in context.accepted_effects:
        return Disposition.HOLD_NO_ACCEPTED_TARGET
    return Disposition.HOLD_PROVIDER_RECEIPT_UNAVAILABLE


def original_claims() -> list[SourceClaim]:
    """Construct named diagnostic inquiries, not a new natural fact registry."""
    return [
        SourceClaim(
            FactKind.OBSERVABLE.value, D1_EVENT, "AUTHORIZED_PATH_ONLY",
            E01, "DIRECT_GIT", "D1_GIT_PATH",
        ),
        SourceClaim(
            FactKind.OBSERVABLE.value, D1_EVENT,
            "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD", E01,
            "DIRECT_GIT", "D1_GIT_PARENT",
        ),
        SourceClaim(
            FactKind.EPHEMERAL.value, D1_EVENT,
            "TRANSPORT_ATTESTED_GITHUB_CONNECTOR", E01,
            "SOURCE_REPORTED", "D1_ACTION_CONNECTOR_USE_SOURCE_ASSERTION",
        ),
        SourceClaim(
            FactKind.RELATIONAL.value, FORWARD_EVENT,
            "ACTOR_INTENT_PRESENT", FORWARD_TARGET,
            "ACTOR_AUTHORED", "FORWARD_COCOMMITTED_PROBE_ONLY_COVERS",
        ),
        SourceClaim(
            FactKind.OBSERVABLE.value, FORWARD_EVENT,
            "FORWARD_COMMIT_PATH_EXACT", FORWARD_TARGET,
            "DIRECT_GIT", "FORWARD_GIT_PATH",
        ),
        SourceClaim(
            FactKind.OBSERVABLE.value, FORWARD_EVENT,
            "FORWARD_COMMIT_PARENT_EXACT", FORWARD_TARGET,
            "DIRECT_GIT", "FORWARD_GIT_PARENT",
        ),
        SourceClaim(
            FactKind.EPHEMERAL.value, FORWARD_EVENT,
            "PROVIDER_EXECUTED_CODEXLESS_COMMIT", FORWARD_TARGET,
            "SOURCE_REPORTED", "FORWARD_RUNTIME_BRIDGE_TOOL_REPORT",
        ),
    ]


def build() -> dict[str, Any]:
    context = actual_source_context()
    assertions = historical.check_repeated_transport_claim()
    if assertions["number_of_textual_attestation_carriers"] != 2:
        raise ValueError("D1_TWO_SOURCE_ATTESTATIONS_CHANGED")
    if assertions["number_of_independent_provider_records"] != 0:
        raise ValueError("FALSE_NEW_PROVIDER_PROOF_IN_HISTORICAL_INPUT")
    actual_record, _ = forward.original_commit_data()
    if actual_record["governing_authority"] != "NONE_EXPERIMENT_ONLY_UNSCORED":
        raise ValueError("PROBE_ONLY_RELATION_WAS_PROMOTED")

    claims = original_claims()
    dispositions = [qualify_claim(claim, context) for claim in claims]
    result_rows = [
        {
            "fact_kind": claim.kind,
            "event_commit": claim.source_commit,
            "component_id": claim.component_id,
            "target_effect": claim.target_effect,
            "claim_family": claim.claim_family,
            "qualification": outcome.value,
            "is_governing_j2_relational_admission": False,
        }
        for claim, outcome in zip(claims, dispositions)
    ]
    assert [d.value for d in dispositions] == [
        "VERIFIED_GIT_OBSERVABLE",
        "VERIFIED_GIT_OBSERVABLE",
        "HOLD_PROVIDER_RECEIPT_UNAVAILABLE",
        "HOLD_NO_ACCEPTED_TARGET",
        "HOLD_NO_ACCEPTED_TARGET",
        "HOLD_NO_ACCEPTED_TARGET",
        "HOLD_NO_ACCEPTED_TARGET",
    ]
    return {
        "schema_version": 1,
        "world_class": EXPERIMENT_ONLY,
        "status": "SOURCE_VERIFIED_OBSERVABLES_WITH_UNQUALIFIED_RELATIONAL_AND_EPHEMERAL",
        "original_accepted_j1_effect_ids": list(context.accepted_effects),
        "accepted_j1_count": len(context.accepted_effects),
        "actual_git_events": [D1_EVENT, FORWARD_EVENT],
        "source_verified_git_observations": [
            {
                "source_commit": v.source_commit,
                "component": v.component_id,
                "fact_owner": v.source_owner,
                "value": v.value,
                "source_digest": v.source_digest,
            }
            for v in context.observations
        ],
        "capabilities_actually_implemented": {
            "exact_git_original_object_verification": True,
            "natural_owner_identity_authentication": False,
            "provider_native_receipt_verification": False,
            "production_j1_authentication": False,
            "governing_j3_predicate_evaluation": False,
        },
        "inquiries": result_rows,
        "historical_d1_source_attestations": {
            "claim_family": "D1_ACTION_CONNECTOR_USE_SOURCE_ASSERTION",
            "textual_source_carriers": 2,
            "authoritative_provider_receipts": 0,
            "natural_owner_covers_response": "CANNOT_ATTEST",
            "deduplicated_claim_family_count": 1,
            "underlying_connector_use": "UNKNOWN",
        },
        "forward_probe_relational_status": {
            "source_claim_co_committed": True,
            "target": FORWARD_TARGET,
            "governing_effect_accepted": False,
            "actor_identity_authenticated": False,
            "qualified_j2_relational": False,
        },
        "accepted_e01_evidence_readiness": {
            "completion_rule": "ALL_REQUIRED",
            "required_components": list(REQUIRED),
            "direct_git_observables_verified": 2,
            "ephemeral_connector_source_attested": True,
            "underlying_provider_use_qualified": False,
            "additional_genuine_relational_coverage_qualified": False,
            "attestation_sufficiency_interpretation": "UNRESOLVED_NO_SILENT_J1_AMENDMENT",
            "j3_not_evaluated_by_this_port": True,
            "orientation": "HOLD_UNQUALIFIED_COMPONENT_AND_ASSURANCE",
        },
        "invariants": {
            "new_accepted_j1_effects": 0,
            "new_qualified_j2_relational_facts": 0,
            "new_provider_verified_ephemeral_facts": 0,
            "historical_e01_j3": "HOLD",
            "historical_d1_raw_outcome": "D1_AMEND_UNCHANGED",
            "formal_p03_score": None,
            "physical_architecture_selected": False,
        },
        "candidate_next_architecture_tests": [
            "Owner-source-authentication verifier with real trust root, no caller-provided assurance bit",
            "Provider-native receipt adapter with independent platform observation and recovery guarantees",
            "Acceptance-scoped RELATIONAL verification for an actually accepted new experiment effect",
            "Metamorphic evidence removal, duplicate claim and stale source-currentness checks",
        ],
    }


def main() -> None:
    result = build()
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if OUTPUT.exists():
        if OUTPUT.read_text("utf8") != text:
            raise RuntimeError("TYPED_J2_ASSURANCE_RECEIPT_IMMUTABLE_CONFLICT")
    else:
        with OUTPUT.open("x", encoding="utf8", newline="\n") as out:
            out.write(text)
    print(json.dumps({
        "status": result["status"],
        "git_observables": result["accepted_e01_evidence_readiness"]["direct_git_observables_verified"],
        "accepted_j1": result["accepted_j1_count"],
        "new_qualified_j2": result["invariants"]["new_qualified_j2_relational_facts"],
        "provider_verified": result["invariants"]["new_provider_verified_ephemeral_facts"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
