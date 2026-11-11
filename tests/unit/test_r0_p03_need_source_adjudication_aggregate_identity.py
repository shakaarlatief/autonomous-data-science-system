"""Exact source-free independent 12-need adjudication result, no task promotion."""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
AGGREGATE = (
    ROOT / "experiments/r0_p03_navigation_probe"
    / "NEED_SOURCE_ADJUDICATION_AGGREGATE.md"
)
EXPECTED_HASH = "78f7d428372c9d51ea8c44fd63ff37740306d27de729642eca6daa5d751d09b7"


def test_uploaded_independent_aggregate_retained_exact_original_bytes() -> None:
    raw = AGGREGATE.read_bytes()
    assert len(raw) == 6168
    assert sha256(raw).hexdigest() == EXPECTED_HASH
    assert raw.startswith(b"# Information-need adjudication")
    assert raw.endswith(b"\n\n")
    assert b"\r\n" not in raw
    assert "aggregate, source-free receipt" in raw.decode("utf-8")


def test_category_counts_are_six_provisional_six_material_hold_not_three_each() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    table = [
        ("Orientation and situation reconstruction", 1, 2),
        ("Project/Product relationships", 3, 0),
        ("Impact and evolution", 1, 2),
        ("Exact evidence, authority and recovery", 1, 2),
    ]
    for name, provisional, holds in table:
        pattern = (
            r"^\| " + re.escape(name) + r" \| 3 \| "
            + str(provisional) + r" \| " + str(holds) + r" \| 0 \| 0 \|$"
        )
        assert re.search(pattern, s, re.MULTILINE)
    assert sum(x[1] for x in table) == 6
    assert sum(x[2] for x in table) == 6
    assert "**31** unique" in s
    assert "verified: **0**" in s
    assert "**0 of 4 categories**" in s
    assert "No historical source qualified/admitted" in s


def test_six_holds_have_nonexclusive_material_evidence_classes() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    classes = (
        ("Endpoint operative-state / authority witnesses", 4),
        ("Validated real first-project or integration/runtime witness", 5),
        ("Longitudinal cross-track lineage or measured effect", 3),
        ("Original executed analytical provenance and rollback/replay", 3),
        ("Snapshot capability or supersession/status crosswalk", 2),
    )
    for label, count in classes:
        assert re.search(
            rf"^\| {re.escape(label)} \| {count} \|", s, re.MULTILINE
        )
    assert "Family counts overlap" in s
    assert "No evidence source was admitted" in s


def test_source_free_summary_carries_no_specific_original_or_question_mapping() -> None:
    s = AGGREGATE.read_text(encoding="utf-8")
    forbidden = (
        r"(?:docs|src|frontend|tests|experiments|tools|scripts)/[A-Za-z0-9_.\-/]+",
        r"(?i)\b(?:Question|Need|Case)\s+(?:0?[1-9]|1[0-2])\s*:",
        r"(?i)\b(?:B0|B1|B2|B3|B4)\s+(?:wins|outperforms)",
    )
    for pattern in forbidden:
        assert re.search(pattern, s) is None


def test_win_checkout_cannot_normalize_uploaded_aggregate_bytes() -> None:
    text = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "NEED_SOURCE_ADJUDICATION_AGGREGATE.md -text"
    ) in text
