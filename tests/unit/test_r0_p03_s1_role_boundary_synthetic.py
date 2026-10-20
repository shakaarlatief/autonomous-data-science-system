"""Bounded adversarial S1 actor and disclosure tests using invented identifiers.

All test subjects are hardcoded synthetics. Results are evidence for pure
policy behavior, not proof of a distinct human, model context, Windows token,
ACL, authenticated application gateway or protected journal.
"""
from __future__ import annotations

from dataclasses import replace

import pytest

from experiments.r0_p03_navigation_probe.s1_role_boundary_synthetic import (
    FAKE_MARKER,
    FakeRoleDirectory,
    ReleaseWitness,
    observe_route_capabilities,
    screen_public_receipt,
    simulate_release_witness,
)


def _roles() -> FakeRoleDirectory:
    d = FakeRoleDirectory()
    for role, principal, session in [
        ("REVIEWER", "s1_fake_person_review", "s1_fake_session_review"),
        ("CHALLENGER", "s1_fake_person_challenge", "s1_fake_session_challenge"),
        ("AUTHORIZER", "s1_fake_person_authorize", "s1_fake_session_authorize"),
        ("BLIND_AUTHOR", "s1_fake_person_author", "s1_fake_session_author"),
        ("PUBLIC_COORDINATOR", "s1_fake_person_public", "s1_fake_session_public"),
    ]:
        d.enroll(principal=principal, session=session, role=role)
    return d


def test_exact_role_to_operation_matrix_not_claimed_roles():
    d = _roles()
    allowed = {
        "s1_fake_session_review": {"READ_REVIEW_BATCH", "WRITE_REVIEW_PROPOSAL"},
        "s1_fake_session_challenge": {"READ_REVIEW_LEDGER", "WRITE_CHALLENGE"},
        "s1_fake_session_authorize": {"READ_CHALLENGED_PACKET", "SIMULATE_AUTHORIZATION"},
        "s1_fake_session_author": {"READ_SIMULATED_AUTHOR_PACKET"},
        "s1_fake_session_public": {"READ_NONANSWER_RECEIPT"},
    }
    all_actions = set().union(*allowed.values())
    for session, permitted in allowed.items():
        for action in all_actions:
            result = d.decide(session=session, action=action, claimed_role="AUTHORIZER")
            assert result.permitted is (action in permitted)
            assert result.marker == FAKE_MARKER


def test_unregistered_session_cannot_self_assert_reviewer_status():
    d = _roles()
    result = d.decide(
        session="s1_fake_unknown_session",
        action="READ_REVIEW_LEDGER",
        claimed_role="CHALLENGER",
    )
    assert not result.permitted
    assert result.reason == "SESSION_UNREGISTERED"


def test_public_coordinator_cannot_read_restricted_reviewer_ledger():
    d = _roles()
    result = d.decide(
        session="s1_fake_session_public", action="READ_REVIEW_LEDGER",
        claimed_role="CHALLENGER"
    )
    assert not result.permitted
    assert result.reason == "ROLE_ACTION_DENIED"


def test_new_session_cannot_escape_existing_role_or_private_exposure():
    d = _roles()
    d.mark_private_exposure(session="s1_fake_session_review")
    with pytest.raises(ValueError, match="cannot change role"):
        d.enroll(
            principal="s1_fake_person_review",
            session="s1_fake_new_session",
            role="BLIND_AUTHOR",
        )
    d.enroll(
        principal="s1_fake_person_review",
        session="s1_fake_new_session",
        role="REVIEWER",
    )
    assert d.decide(
        session="s1_fake_new_session", action="READ_REVIEW_BATCH"
    ).permitted
    assert not d.decide(
        session="s1_fake_new_session", action="READ_SIMULATED_AUTHOR_PACKET",
        claimed_role="BLIND_AUTHOR",
    ).permitted


def test_caller_cannot_reassign_session_or_invent_real_identity():
    d = _roles()
    with pytest.raises(ValueError, match="reassign"):
        d.enroll(
            principal="s1_fake_person_different",
            session="s1_fake_session_review",
            role="BLIND_AUTHOR",
        )
    with pytest.raises(ValueError, match="fictional"):
        d.enroll(
            principal="actual-windows-account",
            session="s1_fake_session_new",
            role="REVIEWER",
        )


def test_unlinked_fake_principal_can_defeat_simulated_role_continuity():
    """A negative control, not a successful independent-role guarantee.

    Two attacker-chosen fake principal IDs may denote the same real person.
    With no external, attestable identity binding, the directory cannot
    connect them and therefore *permits* the second registration. This
    intentionally demonstrates the method's inability to enforce actual
    reviewer-versus-blind-author separation.
    """
    d = _roles()
    d.mark_private_exposure(session="s1_fake_session_review")
    fake_alias = d.enroll(
        principal="s1_fake_person_review_alias",
        session="s1_fake_new_blind_session",
        role="BLIND_AUTHOR",
    )
    assert fake_alias.role == "BLIND_AUTHOR"
    assert d.decide(
        session="s1_fake_new_blind_session", action="READ_SIMULATED_AUTHOR_PACKET"
    ).permitted  # A known limitation, NOT safe for real identities.


def test_blind_author_and_public_coordinator_cannot_claim_private_exposure():
    d = _roles()
    with pytest.raises(ValueError, match="known mock privileged"):
        d.mark_private_exposure(session="s1_fake_session_author")
    with pytest.raises(ValueError, match="known mock privileged"):
        d.mark_private_exposure(session="s1_fake_session_public")


def test_role_report_never_lists_mock_private_principals_or_exposures():
    d = _roles()
    d.mark_private_exposure(session="s1_fake_session_review")
    summary = d.public_summary()
    assert summary == {
        "marker": FAKE_MARKER,
        "qualification": "S1_REAL_ROLE_ISOLATION_NOT_VERIFIED",
    }
    text = repr(summary)
    assert "s1_fake_person_review" not in text
    assert "s1_fake_session_review" not in text


def test_semantic_candidate_does_not_grant_release_without_all_other_witnesses():
    base = ReleaseWitness(proposed=True, manifest_exact=True, material_objection=False)
    result = simulate_release_witness(base)
    assert not result.permitted
    assert result.reason == "RELEASE_HOLD_UNQUALIFIED_WITNESS"


@pytest.mark.parametrize(
    "missing",
    [
        "manifest_exact",
        "proposed",
        "independently_challenged",
        "custody_readback",
        "author_render_verified",
        "cumulative_receipt_safe",
    ],
)
def test_each_missing_simulated_witness_holds_release(missing):
    complete = ReleaseWitness(
        manifest_exact=True,
        proposed=True,
        independently_challenged=True,
        custody_readback=True,
        author_render_verified=True,
        cumulative_receipt_safe=True,
        material_objection=False,
    )
    result = simulate_release_witness(replace(complete, **{missing: False}))
    assert not result.permitted
    assert result.reason == "RELEASE_HOLD_UNQUALIFIED_WITNESS"


def test_all_synthetic_witnesses_only_produce_simulated_readiness():
    complete = ReleaseWitness(
        manifest_exact=True,
        proposed=True,
        independently_challenged=True,
        custody_readback=True,
        author_render_verified=True,
        cumulative_receipt_safe=True,
        material_objection=False,
    )
    result = simulate_release_witness(complete)
    assert result.permitted
    assert result.reason == "SIMULATED_READY_ONLY_NO_RELEASE_CAPABILITY"
    assert result.marker == FAKE_MARKER
    assert not simulate_release_witness(replace(complete, material_objection=True)).permitted


@pytest.mark.parametrize(
    "unsafe",
    [
        {"marker": FAKE_MARKER, "qualified": False, "held": 1},
        {"marker": FAKE_MARKER, "qualified": False, "excluded_paths": ["secret_case"]},
        {"marker": FAKE_MARKER, "qualified": True},
        {"marker": "different", "qualified": False},
        {"marker": FAKE_MARKER},
    ],
)
def test_variable_public_receipts_refused_including_singleton_counts(unsafe):
    assert screen_public_receipt(fields=unsafe).reason == "VARIABLE_OR_PRIVATE_PUBLIC_METADATA"


def test_constant_public_receipt_requires_consistently_safe_history():
    safe = {"marker": FAKE_MARKER, "qualified": False}
    assert screen_public_receipt(fields=safe).permitted
    assert screen_public_receipt(fields=safe, previous_receipts=(safe, safe)).permitted
    result = screen_public_receipt(
        fields=safe, previous_receipts=(safe, {**safe, "count": 1})
    )
    assert not result.permitted
    assert result.reason == "UNVERIFIED_PUBLIC_HISTORY"


def test_truthy_strings_must_not_be_accepted_as_release_evidence():
    invalid = ReleaseWitness(
        manifest_exact="true",  # type: ignore[arg-type]
        proposed=True,
        independently_challenged=True,
        custody_readback=True,
        author_render_verified=True,
        cumulative_receipt_safe=True,
        material_objection=False,
    )
    with pytest.raises(TypeError, match="exact boolean"):
        simulate_release_witness(invalid)


def test_zero_must_not_masquerade_as_false_public_qualification():
    invalid = {"marker": FAKE_MARKER, "qualified": 0}
    result = screen_public_receipt(fields=invalid)
    assert not result.permitted
    assert result.reason == "VARIABLE_OR_PRIVATE_PUBLIC_METADATA"
    safe = {"marker": FAKE_MARKER, "qualified": False}
    assert not screen_public_receipt(fields=safe, previous_receipts=(invalid,)).permitted


def test_truthy_string_synthetic_route_claim_is_rejected():
    with pytest.raises(TypeError, match="exact booleans"):
        observe_route_capabilities(
            environment_has_separate_identities="yes",  # type: ignore[arg-type]
            actual_deny_test_observed=True,
            durable_confidential_readback_observed=True,
            separate_anchor_custody_observed=True,
        )


def test_supplied_environment_flags_never_prove_real_isolation():
    unknown = observe_route_capabilities(
        environment_has_separate_identities=False,
        actual_deny_test_observed=False,
        durable_confidential_readback_observed=False,
        separate_anchor_custody_observed=False,
    )
    assert unknown["simulated_gate_inputs_complete"] is False
    optimistic = observe_route_capabilities(
        environment_has_separate_identities=True,
        actual_deny_test_observed=True,
        durable_confidential_readback_observed=True,
        separate_anchor_custody_observed=True,
    )
    assert optimistic["simulated_gate_inputs_complete"] is True
    assert optimistic["actual_s1_security_qualified"] is False
    assert optimistic["real_content_authorized"] is False
