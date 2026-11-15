"""Preaction, non-scoring controls for the delegated S1 composite executable.

These tests intentionally do not create the future Git event, call G013 with
an invented future source, admit RELATIONAL J2, or certify S1/J3. They qualify
only the exact scope and authorial intent/carrier schema before publication.
The production G006/G013 execution must later use actual published event
commits and separate postexecution coverage.
"""
from __future__ import annotations

from copy import deepcopy
import json

import pytest

from experiments.r0_p03_navigation_probe import (
    v03_real_pk_delegated_s1_composite_realizer_v01 as realizer,
)


@pytest.fixture
def scope():
    return realizer.load_scope()


@pytest.fixture
def specimen(scope):
    return {
        "schema_version": 1,
        "scope_id": scope["scope_id"],
        "policy_proposal_id": scope["policy"]["proposal_id"],
        "policy_acceptance_commit": scope["policy"]["acceptance_commit"],
        "scope_freeze_commit": "a" * 40,
        "source_event_parent": "a" * 40,
        "realizer_id": realizer.REALIZER,
        "author_role": scope["realizer"]["natural_owner_scope"],
        "author_identity_assurance": scope["realizer"]["actor_assurance"],
        "source_before_path": realizer.BEFORE,
        "source_after_path": realizer.AFTER,
        "semantic_id": realizer.SEMANTIC_ID,
        "accepted_s1_effect_id": scope["accepted_s1_effect_id"],
        "target_components": list(realizer.COMPONENTS),
        "relationship": "PROSPECTIVE_EXECUTION_INTENT_NOT_J2_COVERS",
        "execution_status": "NOT_EXECUTED_AT_TIME_OF_GIT_EVENT",
        "qualified_relational_j2": False,
        "s1_activated": False,
        "j3": "HOLD",
        "production_authority": False,
        "formal_b0_b4_scored": False,
    }


@pytest.fixture
def source_pair(scope):
    before = json.loads(
        realizer.git("show", f"{realizer.BEFORE_COMMIT}:{realizer.BEFORE}")
    )
    after = deepcopy(before)
    after["lifecycle_stage"] = "S1_DELEGATED_PREEXECUTION_SOURCE_NOT_ACTIVATED"
    after["source_owner_claim"]["claim_class"] = (
        "SCOPED_COMPOSITE_REALIZER_AUTHOR_NOT_INDEPENDENTLY_AUTHENTICATED"
    )
    provenance = after["revision_provenance"]
    provenance.update({
        "previous_source_path": realizer.BEFORE,
        "current_source_path": realizer.AFTER,
        "prior_git_commit": realizer.BEFORE_COMMIT,
        "expected_action_parent": "a" * 40,
        "git_successor_commit": "UNAVAILABLE_UNTIL_COMMIT",
        "natural_owner_j2_coverage": "UNQUALIFIED_PENDING_REAL_EXECUTION",
        "semantic_id_invariant": realizer.SEMANTIC_ID,
        "successor_j1_activation": "NOT_ACTIVATED",
        "source_event_scope_id": scope["scope_id"],
        "composite_realizer_id": realizer.REALIZER,
    })
    return before, after


def test_frozen_scope_has_accepted_one_event_policy_not_j2(scope):
    assert scope["policy"]["max_new_events"] == 1
    assert scope["policy"]["owner_acceptance_class"] == "CHAT_RECORDED_NOT_INDEPENDENTLY_AUTHENTICATED"
    assert scope["realizer"]["historical_production_g006_g013_owner_claim"] is False
    assert scope["realizer"]["executable_path"] == realizer.RUNNER_PATH
    assert scope["postevent"]["independent_separate_j3_required"] is True


def test_prospective_intent_and_source_carrier_preflight(scope, specimen, source_pair):
    realizer.validate_intent(specimen, scope, "a" * 40)
    realizer.validate_carrier(*source_pair, scope, "a" * 40)


@pytest.mark.parametrize("field, value", [
    ("policy_acceptance_commit", "b" * 40),
    ("scope_freeze_commit", "b" * 40),
    ("source_event_parent", "b" * 40),
    ("realizer_id", "HISTORICAL_G013_OWNER"),
    ("author_identity_assurance", "CRYPTOGRAPHIC_PROOF"),
    ("semantic_id", "FORGED_ID"),
    ("accepted_s1_effect_id", "P03PKA-E01-S0-IDENTITY-CONTINUITY"),
    ("target_components", ["EXPLICIT_IDENTITY_PRESERVING_MOVE"]),
    ("relationship", "FULL_COVERS"),
    ("execution_status", "EXECUTED_BEFORE_GIT_ACTION"),
    ("qualified_relational_j2", True),
    ("s1_activated", True),
    ("j3", "SATISFIED"),
    ("production_authority", True),
    ("formal_b0_b4_scored", True),
])
def test_reject_forged_authority_or_temporal_intent(scope, specimen, field, value):
    specimen[field] = value
    with pytest.raises(ValueError, match="FALSE_AUTHORITY"):
        realizer.validate_intent(specimen, scope, "a" * 40)


@pytest.mark.parametrize("tamper", [
    "semantic_id", "coverage", "source_role", "j2", "activation",
    "previous_source", "wrong_parent", "missing_realizer",
])
def test_reject_source_author_coverage_self_certification(scope, source_pair, tamper):
    before, after = source_pair
    if tamper == "semantic_id":
        after["governed_source"]["semantic_id"] = "ALTERED"
    elif tamper == "coverage":
        after["asserted_implementation_coverage"] = "FULL"
    elif tamper == "source_role":
        after["lifecycle_stage"] = "S1_ACTIVATED"
    elif tamper == "j2":
        after["source_owner_claim"]["natural_owner_relational_j2_qualified"] = True
    elif tamper == "activation":
        after["revision_provenance"]["successor_j1_activation"] = "ACTIVATED"
    elif tamper == "previous_source":
        after["revision_provenance"]["previous_source_path"] = "wrong"
    elif tamper == "wrong_parent":
        after["revision_provenance"]["expected_action_parent"] = "b" * 40
    elif tamper == "missing_realizer":
        after["revision_provenance"]["composite_realizer_id"] = "other"
    with pytest.raises(ValueError, match="CHANGED|FORGERY|INVALID"):
        realizer.validate_carrier(before, after, scope, "a" * 40)


def test_production_g006_can_process_synthetic_projection_without_j2(scope, source_pair):
    before, after = source_pair
    facts = {
        "source_event_commit": "b" * 40,
        "before_sha256": realizer.BEFORE_SHA256,
        "after_sha256": "c" * 64,
    }
    result = realizer.run_g006(before, after, facts)
    assert result["production_g006_executed"] is True
    assert result["identity_preserved"] is True
    assert result["current_carrier"] == realizer.AFTER
    # This synthetic compatibility test is not the required real source event.


def test_missing_event_sha_rejects_without_execution():
    with pytest.raises(ValueError, match="COMMIT_SHA_REQUIRED"):
        realizer.observe_event("HEAD", "a" * 40)


def test_forged_future_commit_rejects_before_g006_g013():
    with pytest.raises(ValueError, match="GIT_OBJECT_UNAVAILABLE"):
        realizer.observe_event("b" * 40, "a" * 40)
