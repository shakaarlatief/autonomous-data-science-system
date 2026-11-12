"""Exact identity and public scientific-boundary checks for the C02 original-byte review.

This test authenticates a source-free independent reviewer artifact and keeps
its explicit limitations visible in the public record. It does not inspect
protected original questions, ZIP source members, or any private case mapping;
therefore passing tests cannot establish full-scope source answerability.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / "experiments/r0_p03_navigation_probe/C02_DIRECT_ORIGINAL_EVIDENCE_REVIEW_AGGREGATE_VERIFIED_V01.md"
FULL_SHA256 = "cf182453adedaf7d5a1bf6a9434b3f145cbf2fbabcd725ecf9edd8352ad8ab86"
PREFIX_SHA256 = "75e9f8806d27e9fa7aa329e5d9a9627c676afc319ba19d64aacb6b08cc808d8b"
PRIVATE_SHA256 = "bfd3bad0e9436557f8389322d74eead08ca20d1f9616109a62710c1bf9741a63"


def test_uploaded_full_file_and_own_reported_prefix_authenticate() -> None:
    raw = REPORT.read_bytes()
    assert len(raw) == 3859
    assert sha256(raw).hexdigest() == FULL_SHA256
    split = raw.rfind(b"Aggregate pre-footer SHA-256:")
    assert split == 3762
    assert sha256(raw[:split]).hexdigest() == PREFIX_SHA256
    assert b"\r\n" not in raw
    assert raw.endswith(b"\n")
    raw.decode("utf-8")


def test_direct_original_checks_are_reported_with_provenance_limit() -> None:
    s = REPORT.read_text(encoding="utf-8")
    for marker in (
        "2 of 2",
        "37 of 37",
        "| Distinct originals, across both capsules | 37 |",
        "| Detected duplicate/missing/extra original members or hash discrepancies | 0 |",
        "| Independently authenticated upstream Git commit-tree memberships | 0",
        "| Original-source builds, application runs, CI jobs or human sessions re-executed | 0 |",
        "not authenticated ancestry or source membership in a Git commit",
    ):
        assert marker in s


def test_ten_full_scope_holds_preserve_prior_classification() -> None:
    s = REPORT.read_text(encoding="utf-8")
    for row in (
        "| DISTINCT | 8 | 0 | 8 | 0 |",
        "| SUBSTANTIVE_DUPLICATE | 2 | 0 | 0 | 2 |",
        "| EQUIVALENCE_UNCERTAIN | 2 | 0 | 2 | 0 |",
        "| **Total** | **12** | **0** | **10** | **2** |",
    ):
        assert row in s
    assert "C01's six provisional closures and six material HOLDs remain unchanged" in s
    assert PRIVATE_SHA256 in s
    assert "**63,733 bytes**" in s


def test_public_report_has_no_case_or_source_mapping_and_is_exact_checkouted() -> None:
    s = REPORT.read_text(encoding="utf-8")
    assert not re.search(
        r"(?im)^(?:question|candidate|need)\s*#?\s*(?:[1-9]|1[0-2])\s*[:.)-]",
        s,
    )
    assert not re.search(r"\b(?:docs|src|tools|tests|scripts)/[A-Za-z0-9_./-]+", s)
    rules = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    assert (
        "experiments/r0_p03_navigation_probe/"
        "C02_DIRECT_ORIGINAL_EVIDENCE_REVIEW_AGGREGATE_VERIFIED_V01.md -text"
    ) in rules


def test_research_separates_byte_identity_from_unearned_answers_or_scores() -> None:
    r = (ROOT / "docs/research/641_r0_p03_c02_direct_original_evidence_exhaustion_and_prospective_reference_decision.md").read_text(encoding="utf-8")
    for marker in (
        "C02_MEMBER_BYTES_REVIEWER_VERIFIED=37_OF_37",
        "C02_HISTORICAL_COMMIT_MEMBERSHIPS_VERIFIED_BY_REVIEWER=0",
        "C02_FULL_SCOPE_CLOSURES=0",
        "C02_NON_DUPLICATE_HOLDS=10",
        "C02_MINIMUM_DISTINCT_SLOT_SHORTFALL=2",
        "SOURCE_ADMISSIONS=0",
        "B0_B4_SCORING=NONE",
        "NEXT=OWNER_PROSPECTIVE_REFERENCE_METHOD_DECISION",
    ):
        assert marker in r
