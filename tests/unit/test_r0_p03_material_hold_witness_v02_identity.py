"""Guard exact V02 public witness result and no unearned experiment promotion.

Only the source-free uploaded report is inspected; the private source evidence,
ledger and source/need associations are deliberately out of scope. Matching
source payloads does not establish operative authority or executed workflows.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/r0_p03_navigation_probe"
V02 = EXPERIMENT / "NEED_MATERIAL_HOLD_WITNESS_AGGREGATE_VERIFIED_V02.md"
V01 = EXPERIMENT / "NEED_MATERIAL_HOLD_WITNESS_AGGREGATE_VERIFIED_V01.md"
V02_HASH = "8e74bc8f4f9cdeb8ebb36b38034b6f358e56cb5ab711db97482fcc09d880acc5"
V01_HASH = "29b5049eb9d502f819099b9c56bc8c5b76f88cf41816d627ae35776c1b8d5b5c"


def test_v02_exact_bytes_and_v01_nonmutation() -> None:
    raw = V02.read_bytes()
    assert len(raw) == 6033
    assert sha256(raw).hexdigest() == V02_HASH
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    previous = V01.read_bytes()
    assert len(previous) == 5224 and sha256(previous).hexdigest() == V01_HASH


def test_v02_six_of_six_authentication_with_explicit_provenance_limit() -> None:
    s = V02.read_text(encoding="utf-8")
    for phrase in (
        "6 original plaintext members and 1 manifest",
        "**6 / 6**; cumulative bytes: **75,451**",
        "SHA-256 comparisons: **6 / 6 PASS**",
        "Git blob SHA-1 comparisons: **6 / 6 PASS**",
        "**37 distinct** original identities",
        "not independently authenticated",
    ):
        assert phrase in s
    assert "not independently recomputed this turn" in s


def test_original_holds_preserved_and_no_scientific_promotion() -> None:
    s = V02.read_text(encoding="utf-8")
    for category, count in (
        ("Orientation and situation reconstruction", 2),
        ("Project/Product relationships", 0),
        ("Impact and evolution", 2),
        ("Exact evidence, authority and recovery", 2),
    ):
        assert re.search(
            rf"^\| {re.escape(category)} \| {count} \| {count} \| 0 \| 0 \|$",
            s, re.MULTILINE,
        )
    assert "| **Total** | **6** | **6** | **0** | **0** |" in s
    assert "Previous unreviewed provisional source closures: **6**, unchanged" in s
    assert "No source admission, reference-gold freeze, task substitution or B0–B4 scoring is authorized" in s


def test_limited_evidence_capacity_and_no_further_search() -> None:
    s = V02.read_text(encoding="utf-8")
    for phrase in (
        "No further indexed-original search was started or authorized",
        "8 uninspected among the prior set",
        "full unchanged question currently unjustified for **6**",
        "indispensable evidence existence/retention remains unknown for **6**",
        "original-byte hash consistency",
    ):
        assert phrase in s


def test_public_report_is_source_free_and_checkout_exactness() -> None:
    s = V02.read_text(encoding="utf-8")
    patterns = (
        r"(?:docs|src|frontend|tools|experiments|tests|scripts)/[A-Za-z0-9_.\-/]+",
        r"(?i)\b(?:question|case|need)\s+(?:0?[1-9]|1[0-2])\s*:",
        r"(?i)\b(?:B[0-4])\s+(?:wins|outperforms|failed)",
    )
    assert not any(re.search(x, s) for x in patterns)
    assert "87,376" in s
    assert "8a2c72c78e3550864489c73c5e65d9736116abefdb8198165a0a826a07bde01f" in s
    assert (
        "experiments/r0_p03_navigation_probe/"
        "NEED_MATERIAL_HOLD_WITNESS_AGGREGATE_VERIFIED_V02.md -text"
    ) in (ROOT / ".gitattributes").read_text(encoding="utf-8")
