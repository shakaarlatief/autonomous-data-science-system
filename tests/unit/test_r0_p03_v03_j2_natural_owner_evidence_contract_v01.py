"""Regression and failure tests for Research 512 J2 fact-kind separation.

The source owner has NOT authored a new P03 COVERS relationship in this code.
Synthetic claims exist inside tests only to validate the strict declaration
contract; they must never be interpreted as received natural-owner testimony.
"""
from copy import deepcopy
import hashlib
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_j2_natural_owner_evidence_contract_v01 as j2,
)


@pytest.fixture(scope="module")
def facts():
    return j2.actual_component_evidence()


@pytest.fixture(scope="module")
def result():
    return j2.build()


def synthetic_test_claim(facts, components=None):
    """A hypothetical, non-authoritative fixture, not a Claude declaration."""
    if components is None:
        components = list(j2.REQUIRED)
    return {
        "schema_version": 1,
        "declaration_kind": "EXPLICIT_NATURAL_OWNER_RELATIONAL_CLAIM",
        "natural_owner_role": j2.CLAUDE_AUTHOR_ROLE,
        "owner_source_carrier": j2.CLAUDE_MESSAGE,
        "owner_source_commit": j2.ORIGINAL_PIN,
        "owner_source_sha256": facts["source_owner"]["source_sha256"],
        "target_effect_id": j2.E01,
        "accepted_packet_sha256": j2.accepted.REVIEW_CANONICAL_SHA256,
        "relation": "COVERS",
        "covered_components": components,
        "coverage_extent": "FULL" if len(components) == 3 else "PARTIAL",
        "source_evidence_ids": sorted(j2.EVIDENCE_IDS),
        "provider_transport_claim": "ATTESTED_OWN_GITHUB_CONNECTOR",
        "remaining_uncertainties": ["No independent provider API execution receipt located"],
    }


def test_original_git_message_exact_sha_parent_and_only_action_path(facts):
    source = facts["source_owner"]
    assert source["action_commit"] == j2.ACTION
    assert source["action_parent"] == j2.CORRECTION
    assert source["changed_paths"] == [j2.CLAUDE_MESSAGE]
    assert source["source_commit"] == j2.ORIGINAL_PIN
    assert source["source_path"] == j2.CLAUDE_MESSAGE
    assert source["git_blob_oid"] == (
        "2d8fdf1a50dba34427f72d4c01949504003d7037"
    )
    assert source["source_sha256"] == (
        "890ea35d0e6ea99143e0918cb41ee93a8c28add9981d57add9f20dcc707cadaa"
    )
    assert source["author_claim_line"] > 0
    assert source["transport_attestation_line"] > 0


def test_three_exact_original_j1_components_with_no_semantic_redefinition(facts):
    assert tuple(facts["required_components"]) == j2.REQUIRED
    assert facts["effect_id"] == "D1-E01-D2-CLAUDE-WRITE-REQUIREMENT"
    assert facts["accepted_packet_sha256"] == (
        "186c70ff487104f8ee5baee8d21b50ffd466e812c6b97debb20296c8bbf9451f"
    )


@pytest.mark.parametrize("component", [
    "AUTHORIZED_PATH_ONLY",
    "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD",
])
def test_exact_git_observable_component_is_verified_but_not_new_cover(facts, component):
    row = facts["component_evidence"][component]
    assert row["source_class"].startswith("OBSERVABLE_GIT")
    assert row["status"] == "VERIFIED_GIT"
    assert row["natural_owner_relational_coverage"] == "NOT_DECLARED_FOR_P03"
    assert row["source"] == j2.ACTION
    assert row["evidence_id"] == "J2OBS-D1-GIT-PATH"


def test_transport_is_source_reported_not_observed_provider_proof(facts):
    row = facts["component_evidence"]["TRANSPORT_ATTESTED_GITHUB_CONNECTOR"]
    assert row["status"] == "ATTESTED_BY_SOURCE"
    assert row["source_class"] == "SOURCE_REPORTED_EPHEMERAL_ACTION_ATTESTATION"
    assert row["provider_transport_proof"] == "UNKNOWN_NOT_IN_GIT"
    assert row["natural_owner_relational_coverage"] == "NOT_DECLARED_FOR_P03"
    assert row["evidence_id"] == "J2ASSERT-D1-CLAUDE-TRANSPORT"


def test_j2_absence_does_not_inherit_prior_d1_pass(result):
    assert result["accepted_j1_count"] == 4
    assert result["git_verified_components"] == 2
    assert result["source_attested_transport_components"] == 1
    assert result["provider_verified_transport_components"] == 0
    assert result["new_natural_owner_declarations_observed"] == 0
    assert result["qualified_relational_components"] == []
    assert result["j3_satisfaction"] == "HOLD_J2_NATURAL_OWNER_QUALIFICATION"
    assert result["j3_completion_certified"] is False
    assert result["formal_p03_score"] is None


def test_lineage_open_reset_does_not_auto_carry_old_realization(result):
    assert result["lineage_relation"] == "REPLACE"
    assert result["lineage_realization_succession"] == "OPEN_RESET"
    assert result["predecessor_realization_autocarried"] is False
    assert result["standing_prohibition_compliance"] == "NOT_INDEPENDENTLY_DEMONSTRATED"


def test_hypothetical_full_owner_claim_is_only_structurally_valid(facts):
    candidate = synthetic_test_claim(facts)
    assert j2.validate_candidate_declaration(candidate, facts) == (
        "STRUCTURALLY_VALID_SOURCE_OWNER_CLAIM_NOT_YET_AUTHENTICATED_OR_J2_QUALIFIED"
    )
    assert j2.assess_claims([candidate], facts) == (
        "NO_SOURCE_OWNER_RELATIONAL_ADMISSION_PERFORMED"
    )


def test_hypothetical_partial_owner_claim_allowed_without_full_assertion(facts):
    claim = synthetic_test_claim(facts, [j2.REQUIRED[1]])
    assert claim["coverage_extent"] == "PARTIAL"
    assert "NOT_YET_AUTHENTICATED" in j2.validate_candidate_declaration(claim, facts)


@pytest.mark.parametrize("field,replacement,reason", [
    ("schema_version", 2, "NOT_AN_EXPLICIT"),
    ("declaration_kind", "ACCEPTED_J1", "NOT_AN_EXPLICIT"),
    ("natural_owner_role", "CHATGPT_MODEL", "SOURCE_OWNER_ROLE"),
    ("owner_source_carrier", "some/other.md", "SOURCE_CARRIER"),
    ("owner_source_commit", "0" * 40, "SOURCE_CARRIER"),
    ("owner_source_sha256", "0" * 64, "SOURCE_DIGEST"),
    ("target_effect_id", "D1-E02-NO-CLAUDE-RUNTIME-BRIDGE", "EFFECT_OR_RELATION"),
    ("relation", "ACCEPTED", "EFFECT_OR_RELATION"),
    ("accepted_packet_sha256", "0" * 64, "ACCEPTED_J1_PACKET"),
    ("coverage_extent", "FULLER", "COVERAGE_EXTENT"),
    ("provider_transport_claim", "PROVEN_BY_GIT", "PROVIDER_TRANSPORT"),
])
def test_unsafe_hypothetical_declarations_rejected(facts, field, replacement, reason):
    candidate = synthetic_test_claim(facts)
    candidate[field] = replacement
    with pytest.raises(ValueError, match=reason):
        j2.validate_candidate_declaration(candidate, facts)


@pytest.mark.parametrize("components", [
    [],
    ["NOT_A_COMPONENT"],
    ["AUTHORIZED_PATH_ONLY", "AUTHORIZED_PATH_ONLY"],
])
def test_empty_duplicate_or_unknown_component_claim_rejected(facts, components):
    candidate = synthetic_test_claim(facts, components)
    with pytest.raises(ValueError, match="COMPONENTS_UNKNOWN"):
        j2.validate_candidate_declaration(candidate, facts)


def test_extra_governing_status_smuggling_rejected(facts):
    candidate = synthetic_test_claim(facts)
    candidate["j3_satisfied"] = True
    with pytest.raises(ValueError, match="SCHEMA_OR_AUTHORITY_INJECTION"):
        j2.validate_candidate_declaration(candidate, facts)


def test_unknown_or_duplicate_evidence_id_rejected(facts):
    for refs in [["FORGED_OWNER_VERIFICATION"], ["J2OBS-D1-GIT-PATH"] * 2]:
        candidate = synthetic_test_claim(facts)
        candidate["source_evidence_ids"] = refs
        with pytest.raises(ValueError, match="EVIDENCE_IDS_UNKNOWN"):
            j2.validate_candidate_declaration(candidate, facts)


def test_duplicate_or_conflicting_owner_fact_tuple_rejected(facts):
    one = synthetic_test_claim(facts, [j2.REQUIRED[0]])
    two = synthetic_test_claim(facts, [j2.REQUIRED[0], j2.REQUIRED[1]])
    with pytest.raises(ValueError, match="DUPLICATE_NATURAL_OWNER"):
        j2.assess_claims([one, two], facts)


def test_non_overlapping_hypothetical_claims_never_auto_admitted(facts):
    one = synthetic_test_claim(facts, [j2.REQUIRED[0]])
    two = synthetic_test_claim(facts, [j2.REQUIRED[1], j2.REQUIRED[2]])
    assert j2.assess_claims([one, two], facts) == (
        "NO_SOURCE_OWNER_RELATIONAL_ADMISSION_PERFORMED"
    )


def test_false_source_attestation_detected(monkeypatch):
    original_git = j2.git

    def changed_source(*args):
        result = original_git(*args)
        if args[:1] == ("show",) and len(args) == 2 and args[1].endswith(
            ":" + j2.CLAUDE_MESSAGE
        ):
            return result.replace(
                j2.CLAUDE_TRANSPORT_LINE.encode("utf8"),
                b"Transport                       NOT A GITHUB CONNECTOR",
            )
        return result

    with monkeypatch.context() as context:
        context.setattr(j2, "git", changed_source)
        with pytest.raises(ValueError, match="AUTHOR_OR_TRANSPORT_ATTESTATION_DRIFT"):
            j2.original_message_exact()


def test_false_git_parent_detected(monkeypatch):
    original_git = j2.git

    def forged_git(*args):
        if args == ("show", "-s", "--format=%P", j2.ACTION):
            return ("f" * 40 + "\n").encode("ascii")
        return original_git(*args)

    with monkeypatch.context() as context:
        context.setattr(j2, "git", forged_git)
        with pytest.raises(ValueError, match="GIT_PARENT_OR_CHANGED_PATH_CONFLICT"):
            j2.original_message_exact()


def test_false_git_changed_path_detected(monkeypatch):
    original_git = j2.git

    def forged_git(*args):
        if args == ("diff-tree", "--no-commit-id", "--name-only", "-r", j2.ACTION):
            return b"another/unauthorized/file.md\n"
        return original_git(*args)

    with monkeypatch.context() as context:
        context.setattr(j2, "git", forged_git)
        with pytest.raises(ValueError, match="GIT_PARENT_OR_CHANGED_PATH_CONFLICT"):
            j2.original_message_exact()


def test_first_run_result_is_immutable_and_deterministic():
    actual = json.loads(j2.RESULT.read_text("utf8"))
    assert actual == j2.build()
    assert actual["physical_target_selected"] is False
    assert actual["natural_owner_relation_assessment"] == (
        "NO_SOURCE_OWNER_RELATIONAL_ADMISSION_PERFORMED"
    )
    assert hashlib.sha256(j2.RESULT.read_bytes()).hexdigest() == (
        "f45cd1b709c87d54bc99f5808e52b7685aa63646e8204c9827bab1d1b81f6c0b"
    )


def test_no_actual_declared_new_owner_claim_present(result):
    assert result["new_natural_owner_declarations_observed"] == 0
    assert result["qualified_relational_components"] == []
    assert result["next_required_source"].startswith("Original Claude Message018 author")


def test_invalid_candidate_set_fails_closed(facts):
    with pytest.raises(ValueError, match="INVALID_SOURCE_OWNER_DECLARATION_SET"):
        j2.assess_claims({"not": "a list"}, facts)
