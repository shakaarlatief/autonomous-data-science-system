"""Signed-but-unauthorized admission regression for the historical R0-P01 ledger.

A cryptographically valid acceptance is not automatically a governingly
authorized acceptance. This suite tests that the historical ledger checks
*current* roles, dependencies, signer-set version and single-consumption
rules, while a rejection cannot change the ledger's trusted state.

Test keys are synthetic Ed25519/ES256 keys generated as in-memory Node
KeyObjects by the historical synthetic endpoints. The Python test receives
only public key material and signed proof bytes. It neither reads an owner
credential nor starts a claimed R0-P01 attempt. All SSH and WebAuthn positive
controls execute their real verifier paths on every signed test record.

This guards important behavior in the original implementation. It does not
approve, freeze or substitute for testing the future R0-P01 successor.
"""
from __future__ import annotations

import copy
import json
import shutil
from pathlib import Path

import pytest

from experiments.r0_p01_owner_acceptance_v01 import harness as h


@pytest.fixture(scope="module")
def environment():
    """Create only synthetic in-memory signers and the public fixture.

    The recovery key is an independent synthetic SSH Ed25519 key. For Arm B,
    the primary is an independent synthetic ES256 credential. The primary/
    recovery role definitions come from the historical signed trust ledger,
    not from trusting the proof's self-declared role.
    """
    if not shutil.which("node") or not shutil.which("ssh-keygen"):
        pytest.skip("Node and OpenSSH required for real synthetic proof verification")
    fixture = json.loads((Path(h.HERE) / "fixture.json").read_text(encoding="utf-8"))
    node = h.NodeBridge()
    try:
        identities = {
            "A_PRIMARY": (
                "synthetic_ssh",
                "SYNTHETIC-NON-OWNER-ADMISSION-A-PRIMARY",
            ),
            "B_PRIMARY": (
                "synthetic_webauthn",
                "SYNTHETIC-NON-OWNER-ADMISSION-B-PRIMARY",
            ),
            "RECOVERY": (
                "synthetic_ssh",
                "SYNTHETIC-NON-OWNER-ADMISSION-RECOVERY",
            ),
            "A_UNREGISTERED": (
                "synthetic_ssh",
                "SYNTHETIC-NON-OWNER-ADMISSION-A-UNREGISTERED",
            ),
            "B_UNREGISTERED": (
                "synthetic_webauthn",
                "SYNTHETIC-NON-OWNER-ADMISSION-B-UNREGISTERED",
            ),
        }
        reference_statement = json.loads(
            (Path(h.HERE) / "clarification_vectors_v02.json").read_text(
                encoding="utf-8"
            )
        )["statement"]
        credentials = {}
        for identity, (method, label) in identities.items():
            result = node.call(method, label=label, statement=reference_statement)
            credentials[identity] = result["credential"]
            assert result["proof"]["synthetic_non_owner"] is True
            assert h.verify(
                reference_statement, result["proof"], result["credential"], node
            )
        assert len({
            credential["public_id"] for credential in credentials.values()
        }) == len(credentials)
        yield fixture, node, identities, credentials
    finally:
        node.close()


def ledger_for(environment, arm: str, scenario: str = "BURDEN"):
    fixture, _, _, credentials = environment
    return h.Ledger(
        fixture,
        arm,
        credentials[f"{arm}_PRIMARY"],
        credentials["RECOVERY"],
        credentials["A_PRIMARY"],
        credentials["RECOVERY"],
        scenario,
    )


def signed(environment, ledger, arm: str, item: str, identity: str,
           decision: str = "ACCEPT"):
    """Build an expected record and obtain a *valid* independent signature."""
    fixture, node, identities, credentials = environment
    rec = h.record(
        fixture, arm, item, ledger, decision,
        None, credentials[identity],
    )
    method, label = identities[identity]
    output = node.call(method, label=label, statement=rec["statement"])
    assert output["credential"] == credentials[identity]
    assert output["proof"]["synthetic_non_owner"] is True
    rec["proof"] = output["proof"]
    rec["verifier_result"] = "VALID"
    assert h.verify(rec["statement"], rec["proof"], rec["credential"], node)
    return rec


def snapshot(ledger):
    """Capture all admission-authoritative mutable fields before an action.

    Comparing just the number of accepted entries or a consumed ID can miss
    an unauthorized trust-root rewrite or a changed dependency. We copy the
    entries, consumed-ID set, effects, member roster, signer-set version,
    current dependencies and target credentials in one snapshot.
    """
    return copy.deepcopy({
        "entries": ledger.entries,
        "consumed": ledger.consumed,
        "effects": ledger.effects,
        "members": ledger.members,
        "version": ledger.version,
        "dependencies": ledger.dependencies,
        "a_primary": ledger.a_primary,
        "a_recovery": ledger.a_recovery,
    })


def assert_rejected_unchanged(ledger, rec, node, expected_reason: str):
    before = snapshot(ledger)
    result = ledger.admit(rec, node)
    assert result == {"admitted": False, "reason": expected_reason}
    assert snapshot(ledger) == before
    return result


@pytest.mark.parametrize("arm", ["A", "B"])
def test_valid_signature_consumed_once_and_replay_has_zero_side_effects(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "P0", f"{arm}_PRIMARY")
    before = snapshot(ledger)
    outcome = ledger.admit(rec, node)
    assert outcome["admitted"] is True
    assert rec["statement"]["acceptance_id"] in ledger.consumed
    assert len(ledger.entries) == len(before["entries"]) + 1
    assert len(ledger.consumed) == len(before["consumed"]) + 1
    assert h.verify(rec["statement"], rec["proof"], rec["credential"], node)
    assert_rejected_unchanged(ledger, rec, node, "CONSUMED_ACCEPTANCE_ID")


@pytest.mark.parametrize("arm", ["A", "B"])
def test_recovery_key_valid_signature_cannot_authorize_normal_trial(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", "RECOVERY")
    assert not ledger.authorized(rec["credential"], "PRIMARY")
    assert_rejected_unchanged(ledger, rec, node, "CURRENT_ROLE_DENIED")


@pytest.mark.parametrize("arm", ["A", "B"])
def test_fully_valid_unregistered_signer_signature_cannot_enter_trust(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", f"{arm}_UNREGISTERED")
    assert not ledger.authorized(rec["credential"], "PRIMARY")
    assert_rejected_unchanged(ledger, rec, node, "CURRENT_ROLE_DENIED")


@pytest.mark.parametrize("arm", ["A", "B"])
def test_old_governed_dependency_with_valid_signature_cannot_enter_trust(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", f"{arm}_PRIMARY")
    assert h.verify(rec["statement"], rec["proof"], rec["credential"], node)
    ledger.dependencies[0]["lineage_head"] += "-PROSPECTIVE-SYNTHETIC-UPDATE"
    assert h.digest(ledger.base(rec["envelope"])) != (
        rec["statement"]["semantic_base_digest"]
    )
    assert_rejected_unchanged(ledger, rec, node, "IDENTITY_OR_BASE_MISMATCH")


@pytest.mark.parametrize("arm", ["A", "B"])
def test_valid_signature_with_wrong_presented_owner_view_cannot_enter_trust(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", f"{arm}_PRIMARY")
    rec["owner_view"] = rec["owner_view"] + "UNSIGNED-ADDED-TEXT"
    assert h.verify(rec["statement"], rec["proof"], rec["credential"], node)
    assert_rejected_unchanged(ledger, rec, node, "IDENTITY_OR_BASE_MISMATCH")


@pytest.mark.parametrize("arm", ["A", "B"])
def test_signed_current_statement_not_authoritative_for_different_event(
    environment, arm
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", f"{arm}_PRIMARY")
    rec["item"] = "S02"
    assert h.verify(rec["statement"], rec["proof"], rec["credential"], node)
    assert_rejected_unchanged(ledger, rec, node, "IDENTITY_OR_BASE_MISMATCH")


def test_old_signer_set_signature_rejected_after_actual_authorized_rotation(
    environment,
):
    _, node, _, credentials = environment
    ledger = ledger_for(environment, "A", "ROTATION")
    baseline = signed(environment, ledger, "A", "P0", "A_PRIMARY")
    assert ledger.admit(baseline, node)["admitted"]
    old_statement = signed(environment, ledger, "A", "S01", "A_PRIMARY")

    rotation = signed(environment, ledger, "A", "P5", "A_PRIMARY")
    assert ledger.admit(rotation, node)["admitted"]
    assert ledger.version == h.V2
    assert ledger.authorized(credentials["RECOVERY"], "PRIMARY")
    assert not ledger.authorized(credentials["A_PRIMARY"], "PRIMARY")
    assert h.verify(
        old_statement["statement"], old_statement["proof"],
        old_statement["credential"], node,
    )
    assert_rejected_unchanged(
        ledger, old_statement, node, "IDENTITY_OR_BASE_MISMATCH"
    )

    # Even a *freshly signed* postrotation statement from the old primary
    # has an acceptable signature but lacks the current PRIMARY role.
    fresh_old_primary = signed(
        environment, ledger, "A", "S01", "A_PRIMARY"
    )
    assert_rejected_unchanged(
        ledger, fresh_old_primary, node, "CURRENT_ROLE_DENIED"
    )
    # The new primary (former recovery) can actually sign and be admitted.
    new_primary = signed(
        environment, ledger, "A", "S01", "RECOVERY"
    )
    result = ledger.admit(new_primary, node)
    assert result["admitted"]
    assert len(ledger.consumed) == 3


@pytest.mark.parametrize("arm", ["A", "B"])
def test_recovery_role_permitted_only_for_explicit_recovery_transition(
    environment, arm,
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm, "RECOVERY")
    baseline = signed(environment, ledger, arm, "P0", f"{arm}_PRIMARY")
    assert ledger.admit(baseline, node)["admitted"]
    normal = signed(environment, ledger, arm, "S01", "RECOVERY")
    assert_rejected_unchanged(ledger, normal, node, "CURRENT_ROLE_DENIED")
    special = signed(environment, ledger, arm, "P6", "RECOVERY")
    outcome = ledger.admit(special, node)
    assert outcome["admitted"]
    assert ledger.version == h.V2R
    assert ledger.historical(2, node)


@pytest.mark.parametrize("arm", ["A", "B"])
@pytest.mark.parametrize("decision", ["REJECT", "AMEND"])
def test_signed_nonaccept_decisions_consume_once_but_never_apply_effects(
    environment, arm, decision
):
    _, node, _, _ = environment
    ledger = ledger_for(environment, arm)
    rec = signed(environment, ledger, arm, "S01", f"{arm}_PRIMARY", decision)
    previous = snapshot(ledger)
    result = ledger.admit(rec, node)
    assert result["admitted"] is True
    assert len(ledger.entries) == len(previous["entries"]) + 1
    assert ledger.effects == previous["effects"]
    assert ledger.members == previous["members"]
    assert ledger.version == previous["version"]
    assert_rejected_unchanged(ledger, rec, node, "CONSUMED_ACCEPTANCE_ID")
