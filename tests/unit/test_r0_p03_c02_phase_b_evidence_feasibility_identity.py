"""Protect independently uploaded source-free C02 Phase B aggregate identity.

The exact evidence report is public source-free data. Matching bytes and
reviewer counts neither authenticates protected original historical sources
nor qualifies any scored reference question or benchmark.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PATH = ROOT / "experiments/r0_p03_navigation_probe/C02_EVIDENCE_FEASIBILITY_AGGREGATE_VERIFIED_V01.md"
EXACT_SHA256 = "7f7b9304507d1f44693e434b646598934567d394776e3588760e8b9241cc9a40"
PAYLOAD_SHA256 = "54de32794adab4cc04f2575cdc7566112e27344d93cfc3ad0f4d83e2816f1dae"
PRIVATE_REVIEW_SHA256 = "78b29d82dcc07bfd1c57e7b8ace58bd50d8649161fa5087d610c3f209972ff94"


def test_actual_phase_b_exact_full_bytes_and_checksum_section_prefix() -> None:
    raw = PATH.read_bytes()
    assert len(raw) == 3616
    assert sha256(raw).hexdigest() == EXACT_SHA256
    prefix, marker, _ = raw.partition(b"## Output checksums and self-reference limit")
    assert marker
    assert len(prefix) == 2785
    assert sha256(prefix).hexdigest() == PAYLOAD_SHA256
    raw.decode("utf-8")
    assert raw.endswith(b"\n") and b"\r\n" not in raw


def test_frozen_phase_a_categories_and_preliminary_holds() -> None:
    text = PATH.read_text(encoding="utf-8")
    expected = (
        ("Category 1", 2, 1, 0, 2, 0, 1, 0),
        ("Category 2", 2, 1, 0, 2, 0, 1, 0),
        ("Category 3", 1, 0, 2, 1, 2, 0, 0),
        ("Category 4", 3, 0, 0, 3, 0, 0, 0),
    )
    for row in expected:
        assert "| " + " | ".join(map(str, row)) + " |" in text
    assert "| **TOTAL** | **8** | **2** | **2** | **8** | **2** | **2** | **0** |" in text
    assert "10 assessed; 10 `HOLD`; 0 sufficient; 0 admitted" in text


def test_ledger_only_no_unearned_source_authentication() -> None:
    text = PATH.read_text(encoding="utf-8")
    for marker in (
        "`LEDGER_ONLY_PRELIMINARY`",
        "Historical original-source bodies directly authenticated or read: **0**",
        "Authenticated historical original-source ZIPs in this phase: **0**",
        "Independent execution/replay receipts: **0**",
        "No replacement or supplemental need origination",
    ):
        assert marker in text
    assert PRIVATE_REVIEW_SHA256 in text
    assert "51228" in text


def test_no_original_case_wording_paths_or_unsafe_gold_claim() -> None:
    text = PATH.read_text(encoding="utf-8")
    assert not re.search(
        r"(?im)^(?:question|candidate|need)\s*#?\s*(?:[1-9]|1[0-2])\s*[:.)-]",
        text,
    )
    assert not re.search(
        r"\b(?:docs|src|frontend|tools|tests|scripts|schemas)/[a-zA-Z0-9_./-]+",
        text,
    )
    assert not re.search(r"\b(?:answer_text|expected_answer|case_to_source)\b", text)


def test_scientific_capacity_boundary_and_git_exactness() -> None:
    research = (ROOT / "docs/research/640_r0_p03_c02_phase_b_ledger_only_evidence_capacity_and_next_scientific_gate.md").read_text(encoding="utf-8")
    for item in (
        "C02_EVIDENCE_HOLD=10",
        "C02_EVIDENCE_SUFFICIENT=0",
        "C02_MINIMUM_UNAVOIDABLE_DISTINCT_DEFICIT=2",
        "C02_CURRENTLY_UNCONFIRMED_DISTINCT_DEFICIT=4",
        "C01_MATERIAL_HOLDS=6_UNCHANGED",
        "B0_B4_SCORING=NONE",
    ):
        assert item in research
    rules = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert "experiments/r0_p03_navigation_probe/C02_EVIDENCE_FEASIBILITY_AGGREGATE_VERIFIED_V01.md -text" in rules
