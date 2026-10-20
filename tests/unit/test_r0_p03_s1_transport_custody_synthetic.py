"""Adversarial fictional-only evidence for the S1 transport and custody model.

The assertions qualify deterministic simulation mechanics, not independence,
cryptographic authorization, Windows ACLs, encrypted storage, real source
semantics, a protected reviewer ledger or author-facing release.
"""
from __future__ import annotations

import json

import pytest

from experiments.r0_p03_navigation_probe.s1_transport_custody_synthetic import (
    ACTORS,
    FAKE_SOURCE_BYTES,
    JOURNAL_FILENAME,
    JournalError,
    SyntheticJournal,
    build_fixed_manifest,
    screen_fictional_author_view,
    screen_fictional_bundle,
    screen_fictional_scope,
    verify_delivery,
)


def _journal(tmp_path):
    return SyntheticJournal(tmp_path / JOURNAL_FILENAME)


def _proposal(journal, name="s1_fake_a", deps=()):
    journal.append(
        event_id="s1_fake_event_a", subject=name,
        actor="SIMULATED_REVIEWER", action="PROPOSE", dependencies=tuple(deps)
    )


def test_fixture_is_bounded_to_three_in_memory_fictional_sources():
    manifest = build_fixed_manifest()
    assert len(manifest.sources) == 3
    assert len(manifest.digest) == 64
    assert all(source.byte_count > 0 and len(source.git_blob_oid) == 40 for source in manifest.sources)
    result = verify_delivery(manifest, dict(FAKE_SOURCE_BYTES))
    assert result.status == "PASS"
    assert result.verified_count == 3
    assert not result.missing and not result.modified and not result.unexpected


def test_manifest_refuses_partial_modified_extra_and_nonbytes():
    from dataclasses import replace
    manifest = build_fixed_manifest()
    batch = dict(FAKE_SOURCE_BYTES)
    missing_path = "fictional_exception.txt"
    batch.pop(missing_path)
    assert verify_delivery(manifest, batch).missing == (missing_path,)
    assert verify_delivery(manifest, batch).status == "HOLD_DELIVERY"

    batch = dict(FAKE_SOURCE_BYTES)
    batch["fictional_rule.txt"] += b"unexpected appended content"
    result = verify_delivery(manifest, batch)
    assert result.modified == ("fictional_rule.txt",)
    assert result.status == "HOLD_DELIVERY"

    batch = dict(FAKE_SOURCE_BYTES)
    batch["unexpected_real_path.txt"] = b"not a permitted fixture"
    assert verify_delivery(manifest, batch).unexpected == ("unexpected_real_path.txt",)

    batch = dict(FAKE_SOURCE_BYTES)
    batch["fictional_rule.txt"] = "not bytes"
    assert verify_delivery(manifest, batch).modified == ("fictional_rule.txt",)

    with pytest.raises(ValueError, match="fixed fictional manifest"):
        verify_delivery(replace(manifest, ref="a-real-git-ref-is-not-a-trial"), FAKE_SOURCE_BYTES)


def test_source_candidate_stays_only_proposed_without_real_permission():
    result = screen_fictional_scope(
        delivery_complete=True,
        confirmed_protected_in_exposure=False,
        context_complete=True,
    )
    assert result.status == "ELIGIBLE_PROPOSED"
    assert result.blockers == ()


def test_confirmed_protected_content_veto_survives_missing_bytes():
    result = screen_fictional_scope(
        delivery_complete=False,
        confirmed_protected_in_exposure=True,
    )
    assert result.status == "PROHIBITED_EXPOSURE"
    assert result.blockers == ("CONFIRMED_PROTECTED_EXPOSURE", "MISSING_BYTES")
    recovered = screen_fictional_scope(
        delivery_complete=True,
        confirmed_protected_in_exposure=True,
    )
    assert recovered.status == "PROHIBITED_EXPOSURE"
    assert recovered.blockers == ("CONFIRMED_PROTECTED_EXPOSURE",)


def test_material_possible_spoiler_and_missing_context_hold_separately():
    result = screen_fictional_scope(
        delivery_complete=True,
        confirmed_protected_in_exposure=False,
        material_possible_leak=True,
        context_complete=False,
    )
    assert result.status == "RELEASE_HOLD"
    assert set(result.blockers) == {"MATERIAL_POSSIBLE_DISCLOSURE", "CONTEXT_DEPENDENCY_OPEN"}


@pytest.mark.parametrize(
    "risk,flag",
    [
        ({"dynamic_loaded_asset": True}, "DYNAMIC_LOADED_ASSET"),
        ({"navigable_unfrozen_link": True}, "NAVIGABLE_UNFROZEN_LINK"),
        ({"generated_metadata_leak": True}, "VIEWER_GENERATED_METADATA_LEAK"),
        ({"public_receipt_join_leak": True}, "PUBLIC_RECEIPT_JOIN_LEAK"),
    ],
)
def test_synthetic_author_view_holds_on_disclosed_asset_or_metadata_risk(risk, flag):
    result = screen_fictional_author_view(**risk)
    assert result.status == "RELEASE_HOLD"
    assert flag in result.blockers


def test_inert_irrelevant_citation_does_not_force_infinite_closure():
    result = screen_fictional_author_view(inert_nonmaterial_citation=True)
    assert result.status == "ELIGIBLE_PROPOSED"
    assert not result.blockers


def test_atomic_fictional_bundle_breaks_context_cycle_without_real_release():
    required = frozenset({"s1_fake_rule", "s1_fake_exception"})
    assert screen_fictional_bundle(members=required, required_members=required).status == "CONDITIONALLY_ELIGIBLE"
    held = screen_fictional_bundle(
        members=frozenset({"s1_fake_rule"}), required_members=required
    )
    assert held.status == "RELEASE_HOLD"
    assert held.blockers == ("MISSING_REQUIRED_CONTEXT",)
    forbidden = screen_fictional_bundle(
        members=required, required_members=required,
        prohibited_members=frozenset({"s1_fake_exception"})
    )
    assert forbidden.status == "PROHIBITED_EXPOSURE"
    with pytest.raises(ValueError, match="fictional"):
        screen_fictional_bundle(members=frozenset({"docs/real-source.md"}), required_members=required)


def test_journal_fsynced_roundtrip_uses_only_mock_actor_labels(tmp_path):
    journal = _journal(tmp_path)
    assert journal.inspect_restricted_events("SIMULATED_REVIEWER") == ()
    _proposal(journal)
    assert not journal.simulated_release_ready("s1_fake_a")
    with pytest.raises(PermissionError, match="Mock author"):
        journal.inspect_restricted_events("SIMULATED_AUTHOR")

    journal.append(
        event_id="s1_fake_event_b", subject="s1_fake_a",
        actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT"
    )
    assert not journal.simulated_release_ready("s1_fake_a")
    journal.append(
        event_id="s1_fake_event_c", subject="s1_fake_a",
        actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY"
    )
    assert journal.simulated_release_ready("s1_fake_a")
    recovered = SyntheticJournal(tmp_path / JOURNAL_FILENAME)
    assert len(recovered.inspect_restricted_events("SIMULATED_CHALLENGER")) == 3
    assert recovered.simulated_release_ready("s1_fake_a")
    assert recovered.events[-1]["action"] == "SIMULATED_READY"
    assert ACTORS == {
        "SIMULATED_REVIEWER", "SIMULATED_CHALLENGER", "SIMULATED_AUTHORIZER"
    }


def test_wrong_actor_unknown_action_and_replayed_event_fail_closed(tmp_path):
    journal = _journal(tmp_path)
    with pytest.raises(JournalError, match="Unrecognized"):
        journal.append(
            event_id="s1_fake_one", subject="s1_fake_a",
            actor="SIMULATED_AUTHOR", action="PROPOSE"
        )
    with pytest.raises(JournalError, match="Unrecognized"):
        journal.append(
            event_id="s1_fake_one", subject="s1_fake_a",
            actor="SIMULATED_REVIEWER", action="REAL_AUTHORIZE"
        )
    _proposal(journal)
    with pytest.raises(JournalError, match="Duplicate"):
        _proposal(journal)
    with pytest.raises(JournalError, match="challenger"):
        journal.append(
            event_id="s1_fake_event_b", subject="s1_fake_a",
            actor="SIMULATED_REVIEWER", action="CHALLENGE_ACCEPT"
        )
    with pytest.raises(JournalError, match="mock accepted challenge"):
        journal.append(
            event_id="s1_fake_event_c", subject="s1_fake_a",
            actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY"
        )


def test_challenge_disagreement_prevents_simulated_release(tmp_path):
    journal = _journal(tmp_path)
    _proposal(journal)
    journal.append(
        event_id="s1_fake_dispute", subject="s1_fake_a",
        actor="SIMULATED_CHALLENGER", action="CHALLENGE_DISPUTE"
    )
    assert not journal.simulated_release_ready("s1_fake_a")
    with pytest.raises(JournalError):
        journal.append(
            event_id="s1_fake_ready", subject="s1_fake_a",
            actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY"
        )


def test_upstream_invalidation_deactivates_downstream_fake_release(tmp_path):
    journal = _journal(tmp_path)
    for i, name, dependencies in [
        ("a", "s1_fake_exception", ()),
        ("b", "s1_fake_rule", ("s1_fake_exception",)),
    ]:
        journal.append(event_id=f"s1_fake_proposal_{i}", subject=name, actor="SIMULATED_REVIEWER",
                       action="PROPOSE", dependencies=dependencies)
        journal.append(event_id=f"s1_fake_challenge_{i}", subject=name, actor="SIMULATED_CHALLENGER",
                       action="CHALLENGE_ACCEPT")
        journal.append(event_id=f"s1_fake_ready_{i}", subject=name, actor="SIMULATED_AUTHORIZER",
                       action="SIMULATED_READY")
    assert journal.simulated_release_ready("s1_fake_rule")
    journal.append(event_id="s1_fake_invalidate_a", subject="s1_fake_exception",
                   actor="SIMULATED_CHALLENGER", action="INVALIDATE")
    assert not journal.simulated_release_ready("s1_fake_exception")
    assert not journal.simulated_release_ready("s1_fake_rule")
    assert not SyntheticJournal(tmp_path / JOURNAL_FILENAME).simulated_release_ready("s1_fake_rule")


def test_parent_reapproval_does_not_silently_reactivate_older_child(tmp_path):
    journal = _journal(tmp_path)
    for label, subject, dependencies in [
        ("parent", "s1_fake_parent", ()),
        ("child", "s1_fake_child", ("s1_fake_parent",)),
    ]:
        journal.append(event_id=f"s1_fake_initial_proposal_{label}", subject=subject,
                       actor="SIMULATED_REVIEWER", action="PROPOSE",
                       dependencies=dependencies)
        journal.append(event_id=f"s1_fake_initial_challenge_{label}", subject=subject,
                       actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT")
        journal.append(event_id=f"s1_fake_initial_ready_{label}", subject=subject,
                       actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY")
    assert journal.simulated_release_ready("s1_fake_child")

    journal.append(event_id="s1_fake_parent_invalidated", subject="s1_fake_parent",
                   actor="SIMULATED_CHALLENGER", action="INVALIDATE")
    assert not journal.simulated_release_ready("s1_fake_child")

    journal.append(event_id="s1_fake_parent_reproposal", subject="s1_fake_parent",
                   actor="SIMULATED_REVIEWER", action="PROPOSE")
    journal.append(event_id="s1_fake_parent_rechallenge", subject="s1_fake_parent",
                   actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT")
    journal.append(event_id="s1_fake_parent_reready", subject="s1_fake_parent",
                   actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY")
    assert journal.simulated_release_ready("s1_fake_parent")
    assert not journal.simulated_release_ready("s1_fake_child")
    assert not SyntheticJournal(tmp_path / JOURNAL_FILENAME).simulated_release_ready(
        "s1_fake_child"
    )

    # Only a fresh dependent review can make the child usable again.
    journal.append(event_id="s1_fake_child_invalidated", subject="s1_fake_child",
                   actor="SIMULATED_CHALLENGER", action="INVALIDATE")
    journal.append(event_id="s1_fake_child_reproposal", subject="s1_fake_child",
                   actor="SIMULATED_REVIEWER", action="PROPOSE",
                   dependencies=("s1_fake_parent",))
    journal.append(event_id="s1_fake_child_rechallenge", subject="s1_fake_child",
                   actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT")
    journal.append(event_id="s1_fake_child_reready", subject="s1_fake_child",
                   actor="SIMULATED_AUTHORIZER", action="SIMULATED_READY")
    assert journal.simulated_release_ready("s1_fake_child")


def test_torn_or_modified_journal_recovery_does_not_silently_accept(tmp_path):
    journal = _journal(tmp_path)
    _proposal(journal)
    path = tmp_path / JOURNAL_FILENAME
    original = path.read_bytes()
    assert original.endswith(b"\n")
    path.write_bytes(original[:-3])
    with pytest.raises(JournalError, match="Torn final"):
        SyntheticJournal(path)
    path.write_bytes(original.replace(b"SIMULATED_REVIEWER", b"SIMULATED_AUTHORXX"))
    with pytest.raises(JournalError, match="Hash-chain|Invalid"):
        SyntheticJournal(path)
    path.write_bytes(original)
    assert len(SyntheticJournal(path).inspect_restricted_events("SIMULATED_REVIEWER")) == 1


def test_hash_chain_detects_record_reordering_or_truncation(tmp_path):
    journal = _journal(tmp_path)
    _proposal(journal)
    journal.append(event_id="s1_fake_event_b", subject="s1_fake_a",
                   actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT")
    p = tmp_path / JOURNAL_FILENAME
    lines = p.read_bytes().splitlines(keepends=True)
    p.write_bytes(lines[1] + lines[0])
    with pytest.raises(JournalError):
        SyntheticJournal(p)
    p.write_bytes(lines[0])
    # Important limitation: a valid prefix alone does not prove journal
    # completeness. An externally held last digest/sequence is necessary.
    assert len(SyntheticJournal(p).inspect_restricted_events("SIMULATED_REVIEWER")) == 1


def test_external_expected_anchor_detects_valid_looking_shorter_prefix(tmp_path):
    journal = _journal(tmp_path)
    _proposal(journal)
    last_digest = journal.append(
        event_id="s1_fake_event_b", subject="s1_fake_a",
        actor="SIMULATED_CHALLENGER", action="CHALLENGE_ACCEPT"
    )
    assert SyntheticJournal(tmp_path / JOURNAL_FILENAME).verify_external_anchor(
        expected_digest=last_digest, expected_event_count=2
    )
    p = tmp_path / JOURNAL_FILENAME
    lines = p.read_bytes().splitlines(keepends=True)
    p.write_bytes(lines[0])
    short = SyntheticJournal(p)
    assert len(short.events) == 1
    with pytest.raises(JournalError, match="anchor mismatch"):
        short.verify_external_anchor(expected_digest=last_digest, expected_event_count=2)
