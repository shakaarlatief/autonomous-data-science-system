"""Protect the exact owner-uploaded, source-free C02 origination receipt.

These tests assert byte identity, absence of case-level claims, and the
reported/verified distinction for protected outputs. Neither the original
C01 questions nor C02 restricted proposal contents enter this repository.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
SAFE = ROOT / "experiments/r0_p03_navigation_probe/NEED_ORIGINATION_C02_SAFE_RECEIPT_VERIFIED_V01.md"
EXPECTED_SHA256 = "3cf0861affb77ee45e0bfa9248416cecd401970a136e2ec4ed92e04d78e08e29"
PRIVATE_C02_SHA256 = "e62566b852ea59408ec69d1c210a2d68d5cf63b3cd5cfbe39909a3e534a38965"
PREFREEZE_INPUT_SHA256 = "1bd83e8d689fd88524e883ec1537d1f51e3448af6026caac8ec285d165d3c7f6"


def test_exact_safe_receipt_bytes() -> None:
    raw = SAFE.read_bytes()
    assert len(raw) == 2870
    assert sha256(raw).hexdigest() == EXPECTED_SHA256
    assert raw.decode("utf-8").startswith("# Need origination")
    assert raw.endswith(b"\n")
    assert b"\r\n" not in raw
    assert b"\x00" not in raw


def test_safe_receipt_claims_all_four_three_case_slots_without_admission() -> None:
    s = SAFE.read_text(encoding="utf-8")
    for label in (
        "Orientation and situation reconstruction",
        "Project/Product relationships",
        "Impact and evolution",
        "Exact evidence, authority and recovery",
    ):
        assert re.search(rf"^\| {re.escape(label)} \| 3 \| 0 \|$", s, re.M)
    assert "| **Total** | **12** | **0** |" in s
    assert "**Status:** `NOT_YET_ADJUDICATED`" in s
    assert "**SCORING=NOT_STARTED**" in s
    assert "none of the candidates' answerability" in s


def test_private_output_only_receipt_reported_not_content_included() -> None:
    s = SAFE.read_text(encoding="utf-8")
    assert PRIVATE_C02_SHA256 in s
    assert PREFREEZE_INPUT_SHA256 in s
    assert "15567" in s
    assert "2870" in s
    assert "Separate downloads are provided" in s
    assert "platform-enforced owner-only access is not claimed" in s
    assert "full technical isolation cannot be independently certified" in s


def test_no_case_level_or_original_source_material_in_safe_receipt() -> None:
    s = SAFE.read_text(encoding="utf-8")
    assert not re.search(
        r"(?im)^(?:question|candidate|need)\s*#?\s*(?:[1-9]|1[012])\s*[:.)-]",
        s,
    )
    assert not re.search(
        r"\b(?:docs|src|frontend|tools|tests|scripts|schemas)/[a-zA-Z0-9_./-]+", s
    )
    assert not re.search(r"\b[a-f0-9]{40}\b", s)
    assert "must_retrieve" not in s
    assert "must_not_retrieve" not in s


def test_exact_checkout_rule_and_scientific_status_routing() -> None:
    rule = "experiments/r0_p03_navigation_probe/NEED_ORIGINATION_C02_SAFE_RECEIPT_VERIFIED_V01.md -text whitespace=-blank-at-eol"
    assert rule in (ROOT / ".gitattributes").read_text(encoding="utf-8")
    research = (ROOT / "docs/research/638_r0_p03_c02_independent_origination_received_and_protected_adjudication_transition.md").read_text(encoding="utf-8")
    assert "C02_CROSS_COHORT_DISTINCTNESS=UNADJUDICATED" in research
    assert "SOURCE_ADMISSIONS=0" in research
    assert "B0_B4_SCORING=NONE" in research
