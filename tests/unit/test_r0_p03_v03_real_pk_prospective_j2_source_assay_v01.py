"""Adversarial source-authority boundary tests for prospective P03 S1 J2.

The test fixture is synthetic until the real event commit exists. The final
receipt test requires exact real Git objects and verifies that a source-owner
claim stays non-governing even when co-committed with the source transition.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_prospective_j2_source_assay_v01 as assay,
)


def sample_claim(parent: str = "a" * 40) -> dict:
    return {
        "schema_version": 1,
        "world_id": "P03V2_PKA_IDENTITY_AND_DERIVED_REFRESH_REAL_SOURCES_V01",
        "record_class": "AT_ACTION_EXPERIMENT_SOURCE_OWNER_COVERS_CANDIDATE",
        "fact_class": "RELATIONAL_SOURCE_AUTHOR_ASSERTION",
        "author_statement": {
            "claimed_role": "EXPOSED_CHATGPT_EXPERIMENT_SOURCE_AUTHOR",
            "natural_owner_scope": "THIS_P03_PROSPECTIVE_SOURCE_REVISION_ONLY",
            "claimant_identity_assurance": "MODEL_CONVERSATION_CLAIM_NOT_INDEPENDENTLY_AUTHENTICATED",
            "independently_authenticated_actor": False,
            "provider_receipt_verified": False,
            "claim_made_before_action": True,
        },
        "relational_claim": {
            "relation": "COVERS",
            "target_accepted_effect_id": assay.EFFECT,
            "realizer_id": assay.REALIZER,
            "component_ids": list(assay.COMPONENTS),
            "coverage_status": "PROPOSED_PENDING_ACTUAL_EXECUTION_AND_OWNER_QUALIFICATION",
        },
        "source_action": {
            "operation": "ACTUAL_REPRESENTATION_REPLACEMENT_WITH_COCOMMITTED_CLAIM",
            "expected_branch": assay.BRANCH,
            "expected_parent_sha": parent,
            "previous_source_commit": assay.previous.REPLACEMENT_COMMIT,
            "previous_path": assay.BEFORE,
            "new_path": assay.AFTER,
            "declaration_path": assay.CLAIM,
            "commit_sha_known_before_action": False,
            "expected_changed_paths": [
                {"status": status, "path": path} for status, path in assay.EXPECTED_CHANGES
            ],
        },
        "authority_exclusions": [
            "NO_INDEPENDENT_MODEL_ACTOR_PROOF",
            "NO_AUTHENTICATED_NATURAL_OWNER_RELATIONAL_J2",
            "NO_S1_ACTIVATION",
            "NO_J3_SATISFIED",
            "NO_PRODUCTION_OR_PHYSICAL_TARGET_AUTHORITY",
            "NO_FORMAL_B0_B4_SCORE",
        ],
        "s1_activation": "NOT_ACTIVATED",
        "j3_status": "HOLD_J2_OWNER_ASSURANCE",
    }


def sample_after(parent: str = "a" * 40) -> tuple[dict, dict]:
    before = json.loads(assay._git("show", f"{assay.previous.REPLACEMENT_COMMIT}:{assay.BEFORE}").decode("utf8"))
    after = deepcopy(before)
    after["accepted_effect_ref"] = assay.EFFECT
    after["lifecycle_stage"] = "S1_SOURCE_CANDIDATE_NOT_GOVERNING_ACTIVATION"
    after["revision_provenance"]["current_source_path"] = assay.AFTER
    after["revision_provenance"]["previous_source_path"] = assay.BEFORE
    after["revision_provenance"]["prior_git_commit"] = assay.previous.REPLACEMENT_COMMIT
    after["revision_provenance"]["expected_action_parent"] = parent
    return before, after


def test_exact_nongoverning_source_declaration_is_structurally_accepted():
    assay.validate_claim(sample_claim(), "a" * 40)
    assay.validate_carrier(*sample_after(), "a" * 40)


@pytest.mark.parametrize("section, field, value", [
    ("author_statement", "independently_authenticated_actor", True),
    ("author_statement", "provider_receipt_verified", True),
    ("author_statement", "natural_owner_scope", "HISTORICAL_G006_CODE_OWNER"),
    ("author_statement", "claimant_identity_assurance", "CRYPTOGRAPHIC_OWNER_PROVEN"),
    ("relational_claim", "target_accepted_effect_id", "P03PKA-E01-S0-IDENTITY-CONTINUITY"),
    ("relational_claim", "coverage_status", "FULL_QUALIFIED"),
    ("relational_claim", "component_ids", ["EXPLICIT_IDENTITY_PRESERVING_MOVE"]),
    ("source_action", "expected_parent_sha", "b" * 40),
    ("source_action", "commit_sha_known_before_action", True),
    ("source_action", "expected_branch", "main"),
    ("source_action", "previous_source_commit", "b" * 40),
])
def test_reject_misbound_or_self_certifying_source_claim(section, field, value):
    source = sample_claim()
    source[section][field] = value
    with pytest.raises(ValueError):
        assay.validate_claim(source, "a" * 40)


@pytest.mark.parametrize("field,value", [
    ("s1_activation", "ACTIVATED"),
    ("j3_status", "SATISFIED"),
    ("fact_class", "QUALIFIED_GOVERNING_RELATIONAL_J2"),
])
def test_reject_source_claim_authority_promotion(field, value):
    source = sample_claim()
    source[field] = value
    with pytest.raises(ValueError):
        assay.validate_claim(source, "a" * 40)


@pytest.mark.parametrize("tamper", [
    "identity", "effect", "coverage", "activation", "wrong_path", "unknown_commit", "wrong_parent", "actor_auth",
])
def test_reject_source_carrier_semantic_or_provenance_tampering(tamper):
    before, after = sample_after()
    if tamper == "identity":
        after["governed_source"]["semantic_id"] = "P03.FORGED"
    elif tamper == "effect":
        after["accepted_effect_ref"] = "P03PKA-E01-S0-IDENTITY-CONTINUITY"
    elif tamper == "coverage":
        after["asserted_implementation_coverage"] = "FULL"
    elif tamper == "activation":
        after["revision_provenance"]["successor_j1_activation"] = "ACTIVATED"
    elif tamper == "wrong_path":
        after["revision_provenance"]["current_source_path"] = "docs/pretend.md"
    elif tamper == "unknown_commit":
        after["revision_provenance"]["git_successor_commit"] = "a" * 40
    elif tamper == "wrong_parent":
        after["revision_provenance"]["expected_action_parent"] = "b" * 40
    elif tamper == "actor_auth":
        after["source_owner_claim"]["natural_owner_relational_j2_qualified"] = True
    with pytest.raises(ValueError):
        assay.validate_carrier(before, after, "a" * 40)


def test_reject_untrusted_commit_selector():
    with pytest.raises(ValueError, match="COMMIT_ID_REQUIRED"):
        assay.evaluate("HEAD")


def test_real_git_source_event_is_exact_and_no_authority_is_promoted():
    if not assay.OUTPUT.exists():
        pytest.skip("Prospective real Git source event has not yet been committed")
    actual = json.loads(assay.OUTPUT.read_text("utf8"))
    assert assay.evaluate(actual["commit"]) == actual
    assert actual["declaration_present_in_same_commit"]
    assert actual["git_observable_verified"]
    assert actual["claimed_relational_J2_qualified"] is False
    assert actual["source_owner_claim_independently_authenticated"] is False
    assert actual["S1_activated"] is False
    assert actual["J3"].startswith("HOLD_")
