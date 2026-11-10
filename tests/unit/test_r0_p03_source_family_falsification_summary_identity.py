"""Exact non-arm falsification result custody and bounded source-free guards.

This test binds the independent source-free scientific report received from a
separate reviewer. It does not read any confidential case data, check hidden
reference answers or claim the challenged source-family rule is generally
correct or sources are independently qualified.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/r0_p03_navigation_probe"
SUMMARY = EXPERIMENT / "R0_P03_SOURCE_FAMILY_FALSIFICATION_SOURCE_FREE_SUMMARY.md"
ORIGINAL_RULE = EXPERIMENT / "R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md"
INTERPRETATION = EXPERIMENT / "R0_P03_SOURCE_FAMILY_FALSIFICATION_INTERPRETATION_V01.md"
EXPECTED = "4b9bcab8361a9bcec634503319cd178f37188a09b0db8456a438c27f6423e8ab"


def test_received_independent_summary_exact_original_bytes() -> None:
    raw = SUMMARY.read_bytes()
    assert len(raw) == 4194
    assert sha256(raw).hexdigest() == EXPECTED
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert raw.decode("utf-8").startswith("# R0-P03 source-family falsification")


def test_result_no_false_admission_exclusion_but_nine_unresolved() -> None:
    body = SUMMARY.read_text(encoding="utf-8")
    assert "0 confirmed material wrongful admissions" in body
    assert "0 confirmed material wrongful exclusions" in body
    assert "7 justified material HOLDs" in body
    assert "2 indeterminate/unavailable cases" in body
    assert "7 cases with no demonstrated counterexample" in body
    assert "14" in body and "16" in body
    assert "not general validation" in body
    assert "do **not** freeze the primary-author source world" in body


def test_summary_bounded_direct_source_leakage_screen() -> None:
    body = SUMMARY.read_text(encoding="utf-8")
    patterns = [
        r"\b[a-f0-9]{40}\b",
        r"\b[a-f0-9]{64}\b",
        r"(?:docs|src|frontend|tools|schemas|scripts|experiments)/"
        r"[A-Za-z0-9_.\-/]+",
        r"\b(?:case|source)[-_ ]?(?:0[1-9]|1[0-6])\b",
        r"https?://\S+",
    ]
    assert not any(re.search(pattern, body, re.I) for pattern in patterns)


def test_complete_source_free_result_is_not_scored_or_admitted() -> None:
    body = SUMMARY.read_text(encoding="utf-8")
    required = [
        "RULE_FROZEN_FOR_TEST=YES",
        "SOURCE_ADMISSIONS=ZERO",
        "AUTHOR_WORLD=WORLD_UNFROZEN",
        "ORIGINAL_CALIBRATION_PACKET=NOT_ACCESSED",
        "PRIVATE_CALIBRATION_ASSESSMENTS=NOT_ACCESSED",
        "SCORED_TASKS_OR_B0_B4_RESULTS=NONE",
    ]
    assert all(state in body for state in required)
    assert sha256(ORIGINAL_RULE.read_bytes()).hexdigest() == (
        "9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268"
    )
    assert sha256(INTERPRETATION.read_bytes()).hexdigest() == (
        "7594b420f215c311c4075a98c2775857c0e359e712efbec397d3ac969d8862ff"
    )


def test_git_line_ending_control_for_exact_review_document() -> None:
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "R0_P03_SOURCE_FAMILY_FALSIFICATION_SOURCE_FREE_SUMMARY.md -text"
    ) in attributes
