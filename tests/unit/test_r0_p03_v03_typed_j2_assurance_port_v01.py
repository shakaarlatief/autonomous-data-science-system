"""Tests for the source-verified, fail-closed experimental typed J2 port.

This suite tests source-truth and security boundaries. It does not authenticate
model actors, invent external provider receipts, run the production J3
predicate, originate formal tasks or score B0-B4 navigation arms.
"""
from dataclasses import replace
from copy import deepcopy
from hashlib import sha256
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_typed_j2_assurance_port_v01 as port,
)


@pytest.fixture(scope="module")
def context():
    return port.actual_source_context()


@pytest.fixture(scope="module")
def result():
    return port.build()


def lookup(kind, event, component, target, assurance, family):
    return port.SourceClaim(kind, event, component, target, assurance, family)


def test_source_context_exact_git_objects_and_original_accepted_effect_set(context):
    assert context.accepted_effects == port.accepted.EXPECTED_EFFECT_IDS
    assert context.observations == port.EXPECTED_SOURCE_OBSERVATIONS
    assert context.natural_owner_authenticator_available is False
    assert context.provider_native_receipt_verifier_available is False
    assert len(context.observations) == 4
    assert len({(x.source_commit, x.component_id) for x in context.observations}) == 4


def test_seven_actual_bound_inquiries_have_expected_dispositions(context):
    inquiries = port.original_claims()
    assert len(inquiries) == 7
    assert [port.qualify_claim(c, context) for c in inquiries] == [
        port.Disposition.VERIFIED_GIT_OBSERVABLE,
        port.Disposition.VERIFIED_GIT_OBSERVABLE,
        port.Disposition.HOLD_PROVIDER_RECEIPT_UNAVAILABLE,
        port.Disposition.HOLD_NO_ACCEPTED_TARGET,
        port.Disposition.HOLD_NO_ACCEPTED_TARGET,
        port.Disposition.HOLD_NO_ACCEPTED_TARGET,
        port.Disposition.HOLD_NO_ACCEPTED_TARGET,
    ]


@pytest.mark.parametrize("idx", [0, 1])
def test_historical_git_source_fact_verified_not_full_j3(context, idx, result):
    assert port.qualify_claim(port.original_claims()[idx], context) == (
        port.Disposition.VERIFIED_GIT_OBSERVABLE
    )
    assert result["accepted_e01_evidence_readiness"]["direct_git_observables_verified"] == 2
    assert result["accepted_e01_evidence_readiness"]["j3_not_evaluated_by_this_port"] is True


def test_historical_transport_claim_is_not_provider_proof(context, result):
    assert port.qualify_claim(port.original_claims()[2], context) == (
        port.Disposition.HOLD_PROVIDER_RECEIPT_UNAVAILABLE
    )
    assert result["historical_d1_source_attestations"]["textual_source_carriers"] == 2
    assert result["historical_d1_source_attestations"]["authoritative_provider_receipts"] == 0
    assert result["historical_d1_source_attestations"]["deduplicated_claim_family_count"] == 1
    assert result["historical_d1_source_attestations"]["natural_owner_covers_response"] == "CANNOT_ATTEST"


def test_real_forward_covers_has_no_accepted_target(context, result):
    claim = port.original_claims()[3]
    assert claim.kind == "RELATIONAL" and claim.target_effect == port.FORWARD_TARGET
    assert port.qualify_claim(claim, context) == port.Disposition.HOLD_NO_ACCEPTED_TARGET
    assert result["forward_probe_relational_status"]["source_claim_co_committed"] is True
    assert result["forward_probe_relational_status"]["governing_effect_accepted"] is False
    assert result["forward_probe_relational_status"]["qualified_j2_relational"] is False


@pytest.mark.parametrize("index", [4, 5, 6])
def test_forward_git_and_tool_claims_cannot_qualify_new_j1(context, index):
    claim = port.original_claims()[index]
    assert claim.target_effect == port.FORWARD_TARGET
    assert port.qualify_claim(claim, context) == port.Disposition.HOLD_NO_ACCEPTED_TARGET


def test_exact_completion_composition_preserved_without_j3_self_certification(result):
    j1 = result["accepted_e01_evidence_readiness"]
    assert j1["completion_rule"] == "ALL_REQUIRED"
    assert j1["required_components"] == list(port.REQUIRED)
    assert j1["underlying_provider_use_qualified"] is False
    assert j1["attestation_sufficiency_interpretation"] == "UNRESOLVED_NO_SILENT_J1_AMENDMENT"
    assert j1["orientation"] == "HOLD_UNQUALIFIED_COMPONENT_AND_ASSURANCE"


@pytest.mark.parametrize("override", [
    {"target_effect": port.E01},
    {"source_commit": port.D1_EVENT},
    {"claim_family": "D1_GIT_PATH"},
    {"component_id": "AUTHORIZED_PATH_ONLY"},
    {"claimed_assurance": "DIRECT_GIT"},
])
def test_forward_relation_cannot_be_transplanted_onto_original_e01(context, override):
    fake = replace(port.original_claims()[3], **override)
    assert port.qualify_claim(fake, context) != port.Disposition.VERIFIED_GIT_OBSERVABLE
    assert port.qualify_claim(fake, context) != port.Disposition.HOLD_NO_NATURAL_OWNER_AUTHENTICATION


@pytest.mark.parametrize("override", [
    {"target_effect": "D1-E02-NO-CLAUDE-RUNTIME-BRIDGE"},
    {"target_effect": port.FORWARD_TARGET},
    {"source_commit": port.FORWARD_EVENT},
    {"claim_family": "FORWARD_GIT_PATH"},
    {"component_id": "FORWARD_COMMIT_PATH_EXACT"},
    {"kind": "RELATIONAL"},
])
def test_genuine_d1_git_observation_cannot_be_relabelled(context, override):
    fake = replace(port.original_claims()[0], **override)
    assert port.qualify_claim(fake, context) == port.Disposition.REJECT_SOURCE_IDENTITY


def test_forged_provider_verified_claim_rejected_even_for_original_effect(context):
    fake = replace(port.original_claims()[2], claimed_assurance="INDEPENDENT_PROVIDER_VERIFIED")
    assert port.qualify_claim(fake, context) == port.Disposition.REJECT_UNSUPPORTED_ASSURANCE


@pytest.mark.parametrize("claim", [
    {"kind": "RELATIONAL", "source_commit": port.FORWARD_EVENT,
     "component_id": "ACTOR_INTENT_PRESENT", "target_effect": port.E01,
     "claimed_assurance": "ACTOR_AUTHORED", "claim_family": "FORWARD_COCOMMITTED_PROBE_ONLY_COVERS"},
    {"kind": "OBSERVABLE", "source_commit": port.D1_EVENT,
     "component_id": "TRANSPORT_ATTESTED_GITHUB_CONNECTOR",
     "target_effect": port.E01, "claimed_assurance": "DIRECT_GIT",
     "claim_family": "D1_ACTION_CONNECTOR_USE_SOURCE_ASSERTION"},
])
def test_changing_claim_kind_or_target_never_qualifies(context, claim):
    assert port.qualify_claim(port.SourceClaim(**claim), context) == (
        port.Disposition.REJECT_SOURCE_IDENTITY
    )


def test_caller_cannot_insert_fake_git_observable_anchor(context):
    fake_obs = port.VerifiedGitObservation(
        port.FORWARD_EVENT, "FAKE_E01_RECEIPT", "GIT_OBJECT_STORE",
        "the provider action happened", "f" * 64,
    )
    forged = replace(context, observations=context.observations + (fake_obs,))
    assert port.qualify_claim(port.original_claims()[0], forged) == (
        port.Disposition.REJECT_SOURCE_IDENTITY
    )


def test_caller_cannot_extend_accepted_effects_with_probe_only_target(context):
    forged = replace(context, accepted_effects=context.accepted_effects + (port.FORWARD_TARGET,))
    assert port.qualify_claim(port.original_claims()[3], forged) == (
        port.Disposition.REJECT_SOURCE_IDENTITY
    )


@pytest.mark.parametrize("attribute", [
    "natural_owner_authenticator_available", "provider_native_receipt_verifier_available",
])
def test_invented_backend_capability_flag_does_not_create_assurance(context, attribute):
    forged = replace(context, **{attribute: True})
    assert port.qualify_claim(port.original_claims()[0], forged) == (
        port.Disposition.REJECT_SOURCE_IDENTITY
    )


def test_changed_observable_values_or_source_digest_fail_closed(context):
    first = context.observations[0]
    for alternate in (
        replace(first, value="FORGED_SOURCE_PATH"),
        replace(first, source_digest="0" * 64),
        replace(first, source_owner="CHATGPT_ACTOR"),
    ):
        forged = replace(context, observations=(alternate, *context.observations[1:]))
        assert port.qualify_claim(port.original_claims()[0], forged) == (
            port.Disposition.REJECT_SOURCE_IDENTITY
        )


def test_normalize_declared_source_claim_is_closed_schema():
    raw = port.original_claims()[0].__dict__
    assert port.normalize_claim(raw) == port.original_claims()[0]
    with pytest.raises(ValueError, match="SCHEMA_OR_AUTHORITY_SMUGGLING"):
        port.normalize_claim({**raw, "independently_verified": True})
    with pytest.raises(ValueError, match="SCHEMA_OR_AUTHORITY_SMUGGLING"):
        port.normalize_claim({"wrong": 1})


@pytest.mark.parametrize("field,new,error", [
    ("kind", "SIGNED_GOVERNING_J2", "KIND_UNKNOWN"),
    ("claimed_assurance", "PROVIDER_VERIFIED", "UNSUPPORTED_CLAIMED_ASSURANCE"),
    ("target_effect", "", "FIELD_VALUE_INVALID"),
    ("claim_family", "x" * 300, "FIELD_VALUE_INVALID"),
    ("source_commit", "nothex", "SOURCE_COMMIT_ID_INVALID"),
])
def test_normalize_rejects_injection_and_bad_fields(field, new, error):
    raw = dict(port.original_claims()[0].__dict__)
    raw[field] = new
    with pytest.raises(ValueError, match=error):
        port.normalize_claim(raw)


def test_no_qualified_j2_or_provider_proof_or_physical_target(result):
    invariants = result["invariants"]
    assert invariants["new_accepted_j1_effects"] == 0
    assert invariants["new_qualified_j2_relational_facts"] == 0
    assert invariants["new_provider_verified_ephemeral_facts"] == 0
    assert invariants["historical_e01_j3"] == "HOLD"
    assert invariants["historical_d1_raw_outcome"] == "D1_AMEND_UNCHANGED"
    assert invariants["formal_p03_score"] is None
    assert invariants["physical_architecture_selected"] is False


def test_no_genuinely_accepted_forward_effect_added(result):
    assert len(result["original_accepted_j1_effect_ids"]) == 4
    assert port.FORWARD_TARGET not in result["original_accepted_j1_effect_ids"]
    assert result["accepted_j1_count"] == 4
    assert result["actual_git_events"] == [port.D1_EVENT, port.FORWARD_EVENT]


def test_fact_claims_inquiry_matrix_does_not_admit_relational_or_ephemeral(result):
    for item in result["inquiries"]:
        assert item["is_governing_j2_relational_admission"] is False
        if item["fact_kind"] != "OBSERVABLE":
            assert item["qualification"] != "VERIFIED_GIT_OBSERVABLE"


def test_no_untrusted_actor_or_provider_proof_backend_installed(result):
    caps = result["capabilities_actually_implemented"]
    assert caps["exact_git_original_object_verification"] is True
    assert caps["natural_owner_identity_authentication"] is False
    assert caps["provider_native_receipt_verification"] is False
    assert caps["production_j1_authentication"] is False
    assert caps["governing_j3_predicate_evaluation"] is False


def test_immutable_receipt_equals_recomputed_source_derived_projection(result):
    raw = port.OUTPUT.read_bytes()
    assert json.loads(raw) == result
    assert result["world_class"] == port.EXPERIMENT_ONLY
    assert result["status"] == (
        "SOURCE_VERIFIED_OBSERVABLES_WITH_UNQUALIFIED_RELATIONAL_AND_EPHEMERAL"
    )


def test_claim_kind_enum_and_invalid_direct_constructed_claim_rejected(context):
    assert {k.value for k in port.FactKind} == {"OBSERVABLE", "RELATIONAL", "EPHEMERAL"}
    fake = replace(port.original_claims()[0], kind="INFERRED_FROM_FILENAME")
    assert port.qualify_claim(fake, context) == port.Disposition.REJECT_UNSUPPORTED_FACT_KIND


def test_fake_source_commit_and_fake_actor_assurance_fail(context):
    fake = replace(port.original_claims()[0], source_commit="f" * 40)
    assert port.qualify_claim(fake, context) == port.Disposition.REJECT_SOURCE_IDENTITY
    fake = replace(port.original_claims()[0], claimed_assurance="UNVERIFIED")
    assert port.qualify_claim(fake, context) == port.Disposition.REJECT_UNSUPPORTED_ASSURANCE


def test_source_inquiry_matrix_exact_cardinality_and_no_duplicate_keys(result):
    data = result["inquiries"]
    assert len(data) == 7
    assert len({(x["fact_kind"], x["event_commit"], x["component_id"]) for x in data}) == 7


def test_no_new_g3_or_regression_of_historical_cannot_attest(result):
    assert result["historical_d1_source_attestations"]["underlying_connector_use"] == "UNKNOWN"
    assert result["historical_d1_source_attestations"]["natural_owner_covers_response"] == "CANNOT_ATTEST"
    assert result["accepted_e01_evidence_readiness"]["j3_not_evaluated_by_this_port"] is True
