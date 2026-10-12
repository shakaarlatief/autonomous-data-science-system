"""Independent candidate R0-P01 B01 outcome reference for bounded F1 review.

Test-only expected-case evaluator derived from accepted B01 precedence and
the original 10s/15s/B selection thresholds. It imports no historical
harness, candidate 288-row table, cryptographic verifier, or live scorer.

Only already-validated per-arm predicates and flags are consumed. This
cannot independently prove the underlying raw receipts or flags are valid.
It does not freeze F1 or confer any run authorization. The owner's 2026-10-11
procedural replacement approval is distinct from study-level scoring.
"""
from __future__ import annotations

from fractions import Fraction
import re
from typing import Any

_ARM_STATES = frozenset({"NOT_REALIZABLE", "INCOMPLETE", "COMPLETED"})
_KEYS = frozenset({"evidence_state", "proof_viable", "selection_eligible"})


def _arm(value: Any) -> None:
    if (
        type(value) is not dict or set(value) != _KEYS
        or type(value["evidence_state"]) is not str
        or value["evidence_state"] not in _ARM_STATES
        or type(value["proof_viable"]) is not bool
        or type(value["selection_eligible"]) is not bool
        or (value["selection_eligible"] and (
            not value["proof_viable"] or value["evidence_state"] != "COMPLETED"
        ))
        or (value["evidence_state"] == "NOT_REALIZABLE" and value["proof_viable"])
    ):
        raise ValueError("invalid or contradictory derived arm predicate")


def _duration(value: Any) -> Fraction:
    """Use exact nonnegative decimal strings, never machine binary floats."""
    if type(value) is not str or not value or len(value) > 40:
        raise ValueError("duration must be a bounded decimal string")
    if not re.fullmatch(r"(?:0|[1-9][0-9]{0,9})(?:\.[0-9]{1,9})?", value):
        raise ValueError("duration must be a plain decimal string")
    x = Fraction(value)
    if x < 0 or x > 86400:
        raise ValueError("duration outside reasonable range")
    return x


def select_arm_exact(
    a_small: str, a_large: str, b_small: str, b_large: str,
) -> str:
    """Frozen >=10 s small delta, then >=15 s large delta, else B."""
    a_s, a_l, b_s, b_l = map(
        _duration, (a_small, a_large, b_small, b_large)
    )
    if abs(a_s - b_s) >= 10:
        return "A" if a_s < b_s else "B"
    if abs(a_l - b_l) >= 15:
        return "A" if a_l < b_l else "B"
    return "B"


def projected_volume_gate(
    selected_small_seconds: str, projected_acceptances: int = 97,
) -> bool:
    """Check the original <=100 acceptances and <=90 total minutes gates.

    Exact rational multiplication avoids silently rounding the threshold.
    This remains a derived aggregate, not proof of the underlying measured
    owner workload or of arm eligibility.
    """
    if (
        type(projected_acceptances) is not int
        or not (1 <= projected_acceptances <= 1_000_000)
    ):
        raise ValueError("invalid projected acceptance count")
    small = _duration(selected_small_seconds)
    return projected_acceptances <= 100 and small * projected_acceptances <= 5400


def classify_b01(
    *,
    A: dict,
    B: dict,
    integrity_flag: bool,
    instrument_flag: bool,
    volume_gate_pass: bool,
    selected_arm: str | None = None,
) -> dict:
    """Evaluate already-derived B01 predicates without assuming raw evidence.

    Volume must refer to the selected arm. With two eligible arms, the
    numeric selection must be supplied before scoring PASS or AMEND.
    The caller cannot select an ineligible arm. Flags are prevalidated by
    an independent upstream evidence analysis, not by this function.
    """
    _arm(A)
    _arm(B)
    if any(type(x) is not bool for x in (
        integrity_flag, instrument_flag, volume_gate_pass
    )):
        raise ValueError("flags and volume predicate must be explicit booleans")
    if selected_arm is not None and selected_arm not in ("A", "B"):
        raise ValueError("selected arm must be A, B or omitted")

    eligible = [name for name, state in (("A", A), ("B", B))
                if state["selection_eligible"]]
    if selected_arm is not None and selected_arm not in eligible:
        raise ValueError("cannot select an ineligible arm")
    if integrity_flag:
        cls, reason = "INVALID", "INVALID_INTEGRITY"
    elif instrument_flag:
        cls, reason = "INVALID", "INVALID_INSTRUMENT"
    elif not A["proof_viable"] and not B["proof_viable"]:
        if "INCOMPLETE" in (A["evidence_state"], B["evidence_state"]):
            cls, reason = "INVALID", "INVALID_INCOMPLETE"
        else:
            cls, reason = (
                "REOPEN", "NO_VIABLE_CRYPTOGRAPHIC_ARM_AFTER_COMPLETE_EVIDENCE"
            )
    elif not eligible:
        cls, reason = "AMEND", "VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY"
    else:
        if len(eligible) == 2 and selected_arm is None:
            return {
                "status": "PENDING_NUMERIC_SELECTION", "class": None,
                "reason": None, "arm_selection": None,
                "G2_OTHER_ARM_INCOMPLETE": False,
            }
        winner = selected_arm or eligible[0]
        if len(eligible) == 1 and winner != eligible[0]:
            raise ValueError("selection conflicts with eligibility")
        g2 = (B if winner == "A" else A)["evidence_state"] == "INCOMPLETE"
        if volume_gate_pass:
            return {
                "status": "DETERMINED", "class": "PASS_WITH_SELECTION",
                "reason": "ELIGIBLE_SELECTED_WITHIN_VOLUME_GATES",
                "arm_selection": winner,
                "G2_OTHER_ARM_INCOMPLETE": g2,
            }
        return {
            "status": "DETERMINED", "class": "AMEND",
            "reason": "VOLUME_GATE", "arm_selection": "NONE",
            "G2_OTHER_ARM_INCOMPLETE": False,
        }

    return {
        "status": "DETERMINED", "class": cls,
        "reason": reason, "arm_selection": "NONE",
        "G2_OTHER_ARM_INCOMPLETE": False,
    }
