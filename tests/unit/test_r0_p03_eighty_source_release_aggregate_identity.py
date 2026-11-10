"""Exact independent source-world capacity result and non-admission guards.

The 80-source source-free report is independent evidence about this candidate's
capacity, not a qualified author-source corpus or an R0-P03 architecture score.
The private 312,821-byte per-source report and old gold are intentionally not
opened by these tests.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/r0_p03_navigation_probe"
REPORT = EXPERIMENT / "R0_P03_EIGHTY_SOURCE_RELEASE_AGGREGATE.md"
EXPECTED = "92f735c6a880e53dec8f51b17435cfdc1adbdf837a3e0c794b3767dfb75b5ae1"
FROZEN_RULE = EXPERIMENT / "R0_P03_CALIBRATION_FAMILY_RULE_SOURCE_FREE.md"
FROZEN_INTERPRETATION = EXPERIMENT / "R0_P03_SOURCE_FAMILY_FALSIFICATION_INTERPRETATION_V01.md"


def test_external_source_free_aggregate_byte_for_byte_identity() -> None:
    raw = REPORT.read_bytes()
    assert len(raw) == 5481
    assert sha256(raw).hexdigest() == EXPECTED
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert raw.decode("utf-8").startswith("# R0-P03 80-source release review:")


def test_all_80_read_but_proposed_dispositions_not_admissions() -> None:
    text = REPORT.read_text(encoding="utf-8")
    assert "80/80" in text
    assert "**0** unreadable or uninspected originals" in text
    expected = {
        "AUTHOR_RELEASE_CANDIDATE": 20,
        "REVIEW_ONLY": 13,
        "EXCLUDE_AUTHOR": 23,
        "HOLD_MATERIAL": 24,
    }
    for disposition, n in expected.items():
        assert re.search(
            rf"^\| {chr(96)}{disposition}{chr(96)} \| \*\*{n}\*\* \|$",
            text, re.MULTILINE,
        )
    assert sum(expected.values()) == 80
    assert "not an admission" in text.lower()
    assert "SOURCE_ADMISSIONS = ZERO" in text
    assert "AUTHOR_WORLD = WORLD_UNFROZEN" in text


def test_all_four_author_ready_need_categories_report_zero_of_three() -> None:
    text = REPORT.read_text(encoding="utf-8")
    patterns = (
        r"Cold-start and current-at-pin orientation",
        r"Cross-plane Product and Project discovery",
        r"Impact analysis and architectural evolution",
        r"Exact source, authority and recovery",
    )
    for category in patterns:
        assert re.search(rf"^\| {category} \| \*\*0\*\* \| 3 \|",
                         text, re.MULTILINE)
    assert "INSUFFICIENT_VERIFIED_CAPACITY" in text
    assert "No omitted source was actually inspected" in text
    assert "199" in text
    assert "SCORED_TASKS = NONE" in text
    assert "B0_B4_RESULTS = NONE" in text


def test_source_free_summary_has_no_direct_identifiable_case_leakage() -> None:
    text = REPORT.read_text(encoding="utf-8")
    patterns = (
        r"\b[0-9a-f]{40}\b",
        r"\b[0-9a-f]{64}\b",
        r"(?:docs|src|frontend|tests|scripts|schemas|experiments)/[A-Za-z0-9_.\-/]+",
        r"https?://\S+",
        r"\b(?:case|source)[-_ ]?(?:0[1-9]|[1-7][0-9])\b",
    )
    assert all(re.search(pat, text, flags=re.I) is None for pat in patterns)


def test_original_rule_and_interpretation_unchanged_and_git_fidelity() -> None:
    assert sha256(FROZEN_RULE.read_bytes()).hexdigest() == (
        "9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268"
    )
    assert sha256(FROZEN_INTERPRETATION.read_bytes()).hexdigest() == (
        "7594b420f215c311c4075a98c2775857c0e359e712efbec397d3ac969d8862ff"
    )
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "R0_P03_EIGHTY_SOURCE_RELEASE_AGGREGATE.md -text"
    ) in attributes
