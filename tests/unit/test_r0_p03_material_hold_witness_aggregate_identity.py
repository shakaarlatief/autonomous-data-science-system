"""Verify exact public witness-aggregate bytes, scientific limits and custody boundary.

The independent aggregate is a non-scored source-free artifact. Its reported
restricted witness ledger and the fourteen newly identified original-source
locators are neither copied nor opened by this public regression.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/r0_p03_navigation_probe"
REPORT = EXPERIMENT / "NEED_MATERIAL_HOLD_WITNESS_AGGREGATE_VERIFIED_V01.md"
EARLIER = EXPERIMENT / "NEED_SOURCE_ADJUDICATION_AGGREGATE_VERIFIED_V02.md"
EXPECTED = "29b5049eb9d502f819099b9c56bc8c5b76f88cf41816d627ae35776c1b8d5b5c"


def test_independent_witness_aggregate_preserves_original_bytes() -> None:
    raw = REPORT.read_bytes()
    assert len(raw) == 5224
    assert sha256(raw).hexdigest() == EXPECTED
    assert raw.startswith("# Material HOLD witness aggregate".encode("utf-8"))
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert len(EARLIER.read_bytes()) == 6243
    assert sha256(EARLIER.read_bytes()).hexdigest() == (
        "29bda10bc26c19bdaa1328dc0e378a35f48cddaef7dc7595f254dd532057ffd0"
    )


def test_six_material_holds_unresolved_and_categories_unchanged() -> None:
    s = REPORT.read_text(encoding="utf-8")
    expected_rows = (
        ("Orientation and situation reconstruction", 2),
        ("Project/Product relationships", 0),
        ("Impact and evolution", 2),
        ("Exact evidence, authority and recovery", 2),
    )
    for name, holds in expected_rows:
        assert re.search(
            rf"^\| {re.escape(name)} \| 3 \| {holds} \| {holds} \| 0 \|$",
            s, re.MULTILINE,
        )
    assert "| **Total** | **12** | **6** | **6** | **0** |" in s
    assert "other six needs retain their preexisting provisional" in s
    assert "zero new source-admission, reference-gold or experimental-scoring" in s


def test_overlapping_evidence_existence_and_gap_counts_not_additive() -> None:
    s = REPORT.read_text(encoding="utf-8")
    for part, n in (
        ("Additional indexed original **plausibly** relevant", 5),
        ("No identifiable indexed **indispensable event-instance** source", 1),
        ("Off-index authority original referenced", 3),
        ("Other possible off-index evidence", 3),
        ("Required execution, validation or authoritative event", 6),
        ("Full historical-scope closure currently unjustified", 6),
        ("Existence of indispensable remaining original evidence unresolved", 6),
        ("Endpoint operative/effective authority", 4),
        ("Cross-track / effective-time crosswalk", 3),
        ("Real integrated or first-project witness", 3),
        ("Matched replay or empirical consequence", 2),
        ("Event/project provenance", 5),
        ("Negative, validation or rollback receipts", 6),
    ):
        assert re.search(rf"^\| {re.escape(part)}[^\n]* \| {n} \|", s, re.MULTILINE)
    assert "Counts overlap by design" in s
    assert "**14 distinct indexed locator identities**" in s
    assert "**0** lead original plaintexts fetched or verified" in s


def test_review_exposes_no_specific_originals_or_case_mappings() -> None:
    s = REPORT.read_text(encoding="utf-8")
    forbidden = (
        r"(?:docs|src|frontend|experiments|tests|scripts|tools)/[A-Za-z0-9_.\-/]+",
        r"(?i)\b(?:Question|Need|Case)\s+(?:0?[1-9]|1[0-2])\s*:",
        r"(?i)\b(?:B0|B1|B2|B3|B4)\s+(?:wins|outperforms)",
    )
    assert all(re.search(p, s) is None for p in forbidden)
    assert "46,473" in s
    assert "ad94559a82b57fd1908143f4285d9c689ebc5aad9ffaf56b2ac3f330ace42a5f" in s
    assert "zero independent remote Git provenance checks" in s


def test_raw_file_checkout_does_not_rewrite_utf8_line_endings() -> None:
    attrs = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "NEED_MATERIAL_HOLD_WITNESS_AGGREGATE_VERIFIED_V01.md -text"
    ) in attrs
