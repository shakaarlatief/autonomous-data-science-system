"""Fidelity and bounded source-free release guards for the real calibration rule.

This checks only the published prospective method, never hidden calibration
case evidence, the owner-private Wave0 register or the falsification sources.
Lexical leak checks are necessary but insufficient for a semantic clearance;
the separate independent method audit is documented in Research 628.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
RULE = (
    ROOT / "experiments/r0_p03_navigation_probe/"
    "R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md"
)
INTERPRETATION = (
    ROOT / "experiments/r0_p03_navigation_probe/"
    "R0_P03_SOURCE_FAMILY_FALSIFICATION_INTERPRETATION_V01.md"
)
RULE_SHA256 = "9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268"


def test_original_proposed_rule_is_the_exact_reviewer_file() -> None:
    original = RULE.read_bytes()
    assert len(original) == 18580
    assert sha256(original).hexdigest() == RULE_SHA256
    assert original.endswith(b"\n")
    assert b"\r\n" not in original
    decoded = original.decode("utf-8")
    assert len(decoded.splitlines()) == 121
    assert "RULE = PROPOSED_NOT_FROZEN" in decoded
    assert "SOURCE_ADMISSIONS = ZERO" in decoded
    assert "AUTHOR_WORLD = WORLD_UNFROZEN" in decoded


def test_rule_contains_core_falsification_and_nonadmission_boundaries() -> None:
    text = RULE.read_text(encoding="utf-8")
    required = [
        "CANDIDATE_CURRENT_BOUNDED",
        "CANDIDATE_HISTORICAL_BOUNDED",
        "CANDIDATE_SANITIZED_DERIVATIVE",
        "HOLD_MATERIAL",
        "EXCLUDE_FOR_INTENDED_WORLD",
        "RESTRICTED_REVIEW_ONLY",
        "Wrongful admission",
        "Wrongful exclusion",
        "Indeterminate",
        "Freeze criteria",
        "Release criteria",
    ]
    assert all(term.casefold() in text.casefold() for term in required)


def test_bounded_public_rule_lexical_exposure_screen_has_no_direct_case_ids() -> None:
    text = RULE.read_text(encoding="utf-8")
    forbidden = [
        r"\b[0-9a-f]{40}\b",
        r"\b[0-9a-f]{64}\b",
        r"(?:docs|src|frontend|tests|experiments|scripts|tools|schemas)/"
        r"[A-Za-z0-9_.\-/]+",
        r"\b(?:case|source)[-_ ]?(?:0[1-9]|1[0-6])\b",
        r"https?://\S+",
    ]
    assert all(re.search(term, text, re.I) is None for term in forbidden)


def test_interpretation_does_not_replace_rule_or_approve_release() -> None:
    companion = INTERPRETATION.read_text(encoding="utf-8")
    assert RULE_SHA256 in companion
    assert "NOT_OWNER_FROZEN" in companion
    assert "SOURCE_ADMISSIONS=ZERO" in companion
    assert "No challenge transfer is authorized" in companion
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md -text"
    ) in attributes
