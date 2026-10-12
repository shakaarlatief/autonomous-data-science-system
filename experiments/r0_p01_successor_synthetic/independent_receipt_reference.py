"""Bounded, synthetic-only raw-event to B01 derived-state reference.

Tests event receipt completeness and a small set of independently checkable
fault sources. This is NOT evidence of real SSH/WebAuthn producer authenticity,
a frozen F1 oracle, a capability-verification implementation, or consent to
perform an owner ceremony. Raw receipts require independently qualified
producers before a full experiment can score them.

In particular, unsupported browser capability, unvisited setup, owner
refusal, and post-Ctrl+C interruption MUST NOT produce NOT_REALIZABLE.
"""
from __future__ import annotations
import hashlib
import re
from typing import Any

EVENTS = ("P0", "S01", "S02", "S03")
OUTCOMES = frozenset({
    "VALID", "INVALID", "P0_NON_ACCEPT_DECISION",
    "OWNER_S_EVENT_STOP", "SSH_UNLOCK_BUDGET_EXHAUSTED",
    "PARTIAL_OR_INCONSISTENT_OUTPUT", "WEBAUTHN_ASSERTION_NOT_COMPLETED",
})
RECEIPT_KEYS = frozenset({
    "attempt_id", "arm", "event", "acceptance_id", "event_terminal",
    "terminal_outcome", "verification_result", "assertion",
})
ASSERTION_KEYS = frozenset({
    "rp_issued", "rp_delivered", "browser_get_invoked", "rp_consumed",
    "rp_acceptance_id", "browser_acceptance_id", "browser_result",
})


def _validate_receipt(receipt: Any, attempt_id: str, arm: str) -> None:
    if type(receipt) is not dict or set(receipt) != RECEIPT_KEYS:
        raise ValueError("invalid receipt field set")
    event = receipt["event"]
    if type(event) is not str or event not in EVENTS:
        raise ValueError("unknown event")
    if (
        receipt["attempt_id"] != attempt_id or receipt["arm"] != arm
        or receipt["acceptance_id"] != f"{attempt_id}-{arm}-{event}"
    ):
        raise ValueError("wrong claim, arm or acceptance identity")
    if type(receipt["event_terminal"]) is not bool:
        raise ValueError("invalid terminal flag")
    verification = receipt["verification_result"]
    if type(verification) is not str or verification not in {
        "VALID","INVALID","ERROR","NOT_RUN"
    }:
        raise ValueError("invalid verification result")
    outcome = receipt["terminal_outcome"]
    if outcome is not None and (type(outcome) is not str or outcome not in OUTCOMES):
        raise ValueError("unknown outcome")
    if receipt["event_terminal"] != (outcome is not None):
        raise ValueError("terminal flag and outcome conflict")
    if outcome == "P0_NON_ACCEPT_DECISION" and event != "P0":
        raise ValueError("non-ACCEPT decision only meaningful at P0")
    if outcome == "WEBAUTHN_ASSERTION_NOT_COMPLETED" and arm != "B":
        raise ValueError("WebAuthn terminal outcome on SSH arm")
    if outcome in {"OWNER_S_EVENT_STOP", "SSH_UNLOCK_BUDGET_EXHAUSTED"} and arm != "A":
        raise ValueError("native SSH stop/budget terminal on WebAuthn proof event")
    if outcome in {"VALID", "INVALID"}:
        if outcome != verification:
            raise ValueError("proof outcome inconsistent with verifier")
    elif verification != "NOT_RUN" and not (
        outcome is None and verification == "ERROR"
    ):
        raise ValueError("no-proof event cannot claim cryptographic proof")
    if receipt["assertion"] is not None and outcome != "WEBAUTHN_ASSERTION_NOT_COMPLETED":
        raise ValueError("irrelevant RP/browser assertion receipt")


def _cancel_correlated(receipt: dict) -> bool:
    a=receipt["assertion"]
    if a is None:
        return False
    if type(a) is not dict or set(a) != ASSERTION_KEYS:
        raise ValueError("malformed RP/browser receipt")
    fields=("rp_issued","rp_delivered","browser_get_invoked","rp_consumed")
    if any(type(a[k]) is not bool for k in fields):
        raise ValueError("invalid RP/browser receipt boolean")
    if (type(a["rp_acceptance_id"]) is not str
        or type(a["browser_acceptance_id"]) is not str
        or a["rp_acceptance_id"] != receipt["acceptance_id"]
        or a["browser_acceptance_id"] != receipt["acceptance_id"]):
        raise ValueError("RP and browser identities disagree")
    if (type(a["browser_result"]) is not str
        or a["browser_result"] not in {"NotAllowedError","OWNER_CANCEL","TIMEOUT"}):
        raise ValueError("unknown browser result")
    return all(a[k] for k in fields)


def derive_arm_evidence(
    *, arm: str, attempt_id: str, setup: str, event_receipts: list[dict],
    capability_receipt: Any = None,
) -> dict:
    """Only compute P0/S01/S02/S03 completeness from typed *test* receipts.

    Capability verification requires a future independently qualified probe.
    A submitted fake receipt is rejected rather than declaring NOT_REALIZABLE.
    """
    if type(arm) is not str or arm not in ("A","B"):
        raise ValueError("synthetic arm must be A or B")
    if type(attempt_id) is not str or re.fullmatch(
        r"SYNTHETIC-[A-Z0-9-]{8,90}",attempt_id
    ) is None:
        raise ValueError("only synthetic claimed identity supported")
    if type(setup) is not str or setup not in {
        "REALIZABLE","OWNER_REFUSED","NOT_VISITED","CAPABILITY_CLAIMED",
    }:
        raise ValueError("invalid setup observation")
    if capability_receipt is not None:
        raise ValueError("independent capability receipt qualification pending")
    if type(event_receipts) is not list:
        raise ValueError("receipt list required")

    seen=set()
    terminal=set()
    for receipt in event_receipts:
        _validate_receipt(receipt,attempt_id,arm)
        event=receipt["event"]
        if event in seen:
            raise ValueError("duplicate receipt for a proof event")
        seen.add(event)
        valid_terminal=receipt["event_terminal"]
        if receipt["terminal_outcome"] == "WEBAUTHN_ASSERTION_NOT_COMPLETED":
            valid_terminal = valid_terminal and _cancel_correlated(receipt)
        if valid_terminal:
            terminal.add(event)
    return {
        "evidence_state": (
            "COMPLETED" if setup=="REALIZABLE" and len(terminal)==4
            else "INCOMPLETE"
        ),
        "terminal_events":[x for x in EVENTS if x in terminal],
        "missing_or_unqualified_events":[x for x in EVENTS if x not in terminal],
        "capability_qualification":(
            "PENDING_INDEPENDENT_PRODUCER"
            if setup=="CAPABILITY_CLAIMED" else "NOT_APPLICABLE"
        ),
    }


def derive_narrow_flags(
    *, verifier_result: str,
    unexpected_rp_exit_sequence: int | None,
    owner_abort_sequence: int | None,
    previous_snapshot_bytes: bytes | None,
    declared_previous_sha256: str | None,
    final_head_witness_present: bool,
) -> dict:
    """Derive only verifiable narrow flag inputs; never accept prose INVALID."""
    if type(verifier_result) is not str or verifier_result not in {
        "VALID","INVALID","ERROR","NOT_RUN"
    }:
        raise ValueError("invalid tri-state verifier result")
    for v in (unexpected_rp_exit_sequence,owner_abort_sequence):
        if v is not None and (type(v) is not int or v<1):
            raise ValueError("invalid receipt sequence")
    if type(final_head_witness_present) is not bool:
        raise ValueError("witness availability must be boolean")
    if (previous_snapshot_bytes is None)!=(declared_previous_sha256 is None):
        raise ValueError("missing required hash-link component")
    if previous_snapshot_bytes is not None and (
        type(previous_snapshot_bytes) is not bytes
        or type(declared_previous_sha256) is not str
        or re.fullmatch(r"[0-9a-f]{64}",declared_previous_sha256) is None
    ):
        raise ValueError("invalid exact snapshot hash evidence")
    if (unexpected_rp_exit_sequence is not None
        and unexpected_rp_exit_sequence==owner_abort_sequence):
        raise ValueError("ambiguous child-exit/owner-abort order")
    instrument_verifier=verifier_result=="ERROR"
    instrument_rp=(
        unexpected_rp_exit_sequence is not None and (
            owner_abort_sequence is None
            or unexpected_rp_exit_sequence < owner_abort_sequence
        )
    )
    broken_link=(
        previous_snapshot_bytes is not None and
        hashlib.sha256(previous_snapshot_bytes).hexdigest()!=declared_previous_sha256
    )
    return {
        "integrity.verifier_error":instrument_verifier,
        "integrity.node_rp_failure":instrument_rp,
        "integrity.evidence_chain_break":broken_link,
        "integrity.instrument_failure":instrument_verifier or instrument_rp,
        "evidence.final_head_witness_absent":not final_head_witness_present,
    }
