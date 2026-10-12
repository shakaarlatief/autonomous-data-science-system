"""Measured synthetic R0-P01 run rehearsal and descriptive evidence assessment.

This is NOT the F1 scientific outcome scorer. It connects the synthetic
governed issuer to actual monotonic technical-operation timing, and reads a
cryptographically reverified journal without treating operational observations
as governing authorization.

Time is measured using perf_counter_ns around one scripted signing operation
and its admission verification. It excludes run issuance, human deliberation,
passphrase prompts, Windows Hello ceremonies, and other owner work.
Interactions are scripted signer-call counts, not measured human gestures.

No real owner credential, consent or Attempt 002 may use this module.
"""

from __future__ import annotations

import copy
import time
from typing import Any

from experiments.r0_p01_successor_synthetic.trusted_claim_store import SyntheticClaimStore

MODES = frozenset({"VALID", "INTERRUPTED", "INVALID_PROOF"})
NOTES = {
    "VALID": "Synthetic signature and admission operation completed",
    "INTERRUPTED": "Synthetic interruption before signature request",
    "INVALID_PROOF": "Synthetic signature did not authorize changed statement",
}
KINDS = {"VALID": "COMPLETED", "INTERRUPTED": "INTERRUPTED", "INVALID_PROOF": "ERROR"}


def run_measured_synthetic_case(
    store: SyntheticClaimStore,
    node: Any,
    *,
    authorization: dict,
    signer_method: str,
    signer_label: str,
    mode: str,
) -> dict:
    """Issue a synthetic claim and measure one script-driven signer operation.

    Governed issuance precedes the measured interval. Admission and the
    observation use separate commits. A crash between them can leave a
    valid admission without a measurement: this is an open experiment
    evidence-atomicity issue, not something this prototype hides.
    """
    if mode not in MODES:
        raise ValueError("unsupported synthetic case")
    if signer_method not in {"sign_ssh", "sign_es256"}:
        raise ValueError("only synthetic signing methods supported")
    if not isinstance(signer_label, str) or not signer_label.startswith(
        "SYNTHETIC-NON-OWNER-"
    ):
        raise ValueError("non-owner signer label required")
    if not store.require_governed_issuance:
        raise ValueError("rehearsal requires synthetic governed issuer")

    statement = store.issue_governed(node, authorization)
    nonce = statement["claim_nonce"]
    start_ns = time.perf_counter_ns()
    calls = 0
    admitted = False
    atomically_observed = False
    kind = KINDS[mode]
    note = NOTES[mode]

    if mode != "INTERRUPTED":
        calls = 1
        try:
            material = node.call(signer_method, label=signer_label, statement=statement)
            if material["credential"] == store.context["trusted_credential"]:
                presented = copy.deepcopy(statement)
                if mode == "INVALID_PROOF":
                    presented["decision"] = (
                        "REJECT" if statement["decision"] != "REJECT" else "ACCEPT"
                    )
                result = store.admit(
                    node=node, claim_nonce=nonce, presented=presented,
                    proof=material["proof"], credential=material["credential"],
                    measurement_started_ns=(start_ns if mode == "VALID" else None),
                )
                admitted = result["admitted"] is True
                if admitted and mode == "VALID":
                    atomically_observed = True
                    measured_ms = result["measured_elapsed_ms"]
            else:
                kind = "ERROR"
                note = "Synthetic signature used a nonenrolled public credential"
            if mode == "VALID" and not admitted:
                kind = "ERROR"
                note = "Synthetic valid proof was not admitted"
        except Exception:
            # Raw error messages must not enter durable evidence.
            kind = "ERROR"
            note = "Synthetic signing or verification operation failed"

    elapsed_ns = time.perf_counter_ns() - start_ns
    if elapsed_ns < 0:
        raise RuntimeError("nonmonotonic measurement clock")
    elapsed_ms = measured_ms if atomically_observed else elapsed_ns // 1_000_000
    if not atomically_observed:
        recorded = store.record_observation(
            node=node, claim_nonce=nonce, kind=kind, elapsed_ms=elapsed_ms,
            interactions=calls, note=note,
        )
        if recorded["recorded"] is not True:
            raise RuntimeError("synthetic measurement could not be preserved")
    return {
        "claim_nonce": nonce,
        "mode": mode,
        "cryptographic_admitted": admitted,
        "observation_kind": kind,
        "measured_elapsed_ms": elapsed_ms,
        "scripted_signer_calls": calls,
    }


def assess_verified_journal(store: SyntheticClaimStore, node: Any) -> dict:
    """Produce descriptive outcomes from actual reverified durable status.

    A caller-supplied COMPLETED observation never creates a cryptographic
    acceptance. Categories are descriptive, not the full R0-P01 scorer.
    """
    view = store.snapshot(node)
    events: dict[str, list[dict]] = {}
    for observation in view["observations"]:
        events.setdefault(observation["claim_nonce"], []).append(observation)

    assessed = []
    for claim in view["claims"]:
        notes = events.get(claim["nonce"], [])
        labels = {entry["kind"] for entry in notes}
        status = claim["status"]
        if status == "ADMITTED":
            outcome = "VERIFIED_CRYPTOGRAPHIC_ADMISSION"
        elif status == "SUPERSEDED":
            outcome = "SUPERSEDED_WITHOUT_ADMISSION"
        elif "INTERRUPTED" in labels:
            outcome = "INTERRUPTED_WITHOUT_ADMISSION"
        elif "ERROR" in labels:
            outcome = "ERROR_WITHOUT_ADMISSION"
        else:
            outcome = "UNRESOLVED_WITHOUT_ADMISSION"
        assessed.append({
            "claim_nonce": claim["nonce"],
            "authorization_ref": claim["authorization_ref"],
            "admission_status": status,
            "descriptive_outcome": outcome,
            "observed_kinds": sorted(labels),
            "observed_elapsed_ms": sum(x["elapsed_ms"] for x in notes),
            "recorded_signer_calls": sum(x["interactions"] for x in notes),
            "observation_count": len(notes),
            # A cryptographically committed acceptance need not have a
            # separately committed timing/effort observation after a crash.
            # Do not silently treat missing evidence as completed measurement.
            "observation_coverage": (
                "PRESENT" if notes else "MISSING"
            ),
        })
    return {
        "issuer_id": view["issuer_id"],
        "claim_count": len(assessed),
        "claims": assessed,
        "total_recorded_elapsed_ms": sum(x["observed_elapsed_ms"] for x in assessed),
        "total_recorded_signer_calls": sum(x["recorded_signer_calls"] for x in assessed),
        "scope": "SYNTHETIC_DESCRIPTIVE_NOT_OWNER_OUTCOME_SCORER",
    }
