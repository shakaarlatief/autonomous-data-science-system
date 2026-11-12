"""Guard independently received public C02 Phase A counts without private task exposure.

A cryptographic match proves only exact public aggregate identity. It cannot
prove adjudicator semantic correctness, source answerability, or architecture
performance. Protected case-level reports are deliberately never read here.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
AGGREGATE = ROOT / "experiments/r0_p03_navigation_probe/C02_CROSS_COHORT_EQUIVALENCE_AGGREGATE_VERIFIED_V01.md"
FULL_SHA = "7d5b979b48596b09e990166bcb5b3bbe43cfb564941a343e3631d7a7ee2d85de"
BODY_SHA = "6c617b747b83a78951d4539aa788fa1afd032cf218348ffc7bfe51f5eb4a8756"


def test_exact_uploaded_bytes_and_independent_content_body_digest() -> None:
    raw = AGGREGATE.read_bytes()
    assert len(raw) == 2899
    assert sha256(raw).hexdigest() == FULL_SHA
    assert len(raw[:2660]) == 2660
    assert sha256(raw[:2660]).hexdigest() == BODY_SHA
    assert b"\r\n" not in raw and raw.endswith(b"\n")
    raw.decode("utf-8")


def test_twelve_case_equivalence_counts_without_gold_claim() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    for label, count in (
        ("DISTINCT", "8"),
        ("SUBSTANTIVE_DUPLICATE", "2"),
        ("EQUIVALENCE_UNCERTAIN", "2"),
    ):
        assert f"| {label} | {count} |" in s
    assert "| **All classifications** | **12** |" in s
    assert "This report does not constitute Phase B" in s
    assert "No question was answered or modified" in s
    assert "Twelve C02 needs compared against twelve C01 needs" in s


def test_original_actor_scope_and_reported_protected_output_only() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    assert "40,615 bytes" in s
    assert "9e554e9ef0471a648c604f13f7e0370e0ca5e5f91d473254b88a3c920f8d1d07" in s
    assert "No web search" in s
    assert "No protected project questions outside these authorized inputs" in s
    assert "cannot independently verify absence of invisible prior/model-training exposure" in s


def test_public_aggregate_has_no_visible_case_wording_or_source_paths() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    assert not re.search(
        r"(?im)^(?:question|candidate|need)\s*#?\s*(?:[1-9]|1[0-2])\s*[:.)-]",
        s,
    )
    assert not re.search(
        r"\b(?:docs|frontend|src|tests|tools|scripts|schemas)/[A-Za-z0-9_./-]+",
        s,
    )
    assert "must_retrieve" not in s
    assert "expected_answer" not in s
    assert "per-category" not in s.lower()


def test_scientific_capacity_hold_and_exact_attribute() -> None:
    s = (ROOT / "docs/research/639_r0_p03_c02_phase_a_verified_equivalence_capacity_and_phase_b_boundary.md").read_text(encoding="utf-8")
    assert "at most **10/12 C02 candidates**" in s
    assert "C02_ACCEPTED_SCORED_REFERENCE_CASES=0" in s
    assert "SOURCE_ADMISSIONS=0" in s
    assert "B0_B4_RESULTS=NONE" in s
    assert (
        "experiments/r0_p03_navigation_probe/"
        "C02_CROSS_COHORT_EQUIVALENCE_AGGREGATE_VERIFIED_V01.md -text"
    ) in (ROOT / ".gitattributes").read_text(encoding="utf-8")
