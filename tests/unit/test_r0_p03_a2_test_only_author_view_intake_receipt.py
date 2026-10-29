"""Integrity and nonpromotion checks for the owner-relayed A2-R07 source-free intake.

The test reads only the published test-only author-view brief and its complete
LF-normalized owner-relayed report. It never opens actual owner files, retrieves
private reviewer history, invokes a future author interface, or simulates an
access-denied result. The original owner-uploaded CRLF fingerprint is separately
recorded in Research 615 and Validation 285, not reconstructed here.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROBE = ROOT / "experiments" / "r0_p03_navigation_probe"
REPORT = (
    PROBE / "author_view_intake_evidence"
    / "20261029_a2_test_only_author_view_intake_report.txt"
)
BRIEF = PROBE / "S1_A2_FUTURE_AUTHOR_VIEW_ROUTE_INTAKE_V01.md"
REPORT_SHA256_LF = "2b47c5ffe8d0a3000f0a6175023b7e2e7df14aeafcc2bf355a9108a8025a3698"
BRIEF_SHA256_LF = "090ccfc8e6a78fa1bb841deb4e8c074ea65446312da20af75a8bcd5cbb49b67e"


def _normalize_checkout_line_endings(data: bytes) -> bytes:
    """Canonicalize only Git checkout CRLF for the known LF evidence copies.

    A Git checkout may represent text files with CRLF when core.autocrlf is
    enabled. The reference hashes cover LF-normalized bytes. This helper
    changes no other bytes and must not be applied to binary evidence.
    """
    return data.replace(b"\r\n", b"\n")


def test_full_owner_report_exact_lf_fingerprint_and_line_count() -> None:
    raw = _normalize_checkout_line_endings(REPORT.read_bytes())
    assert len(raw) == 10345
    assert sha256(raw).hexdigest() == REPORT_SHA256_LF
    assert len(raw.splitlines()) == 153
    assert not raw.endswith(b"\n")
    assert raw.startswith(b"# R0-P03 S1 A2")


def test_test_only_author_brief_precommitted_fingerprint() -> None:
    raw = _normalize_checkout_line_endings(BRIEF.read_bytes())
    assert len(raw) == 5684
    assert sha256(raw).hexdigest() == BRIEF_SHA256_LF
    assert b"ADS_A2_AUTHOR_VIEW_INTAKE_PUBLIC_V01" in raw
    assert b"A2_R07_DIRECT_AUTHOR_ACCESS_DENIAL=NOT_TESTED" in raw


def test_report_matches_prepared_brief_but_does_not_claim_denial() -> None:
    report = REPORT.read_text(encoding="utf-8")
    assert "Bytes read: 5,684" in report
    assert BRIEF_SHA256_LF in report
    assert "Marker present: YES" in report
    for marker in (
        "A2_R07_TEST_ACTOR=NON_AUTHOR_SOURCE_FREE",
        "A2_R07_PUBLIC_BRIEF_VISIBLE=YES",
        "A2_R07_AUTHOR_VIEW_INTAKE=INTAKE_REPORTED_ONLY",
        "A2_R07_OWNER_RESTRICTED_TARGET_REQUESTED=NO",
        "A2_R07_DIRECT_AUTHOR_ACCESS_DENIAL=NOT_TESTED",
        "A2_R07_ACTUAL_PRIMARY_AUTHOR_ADMITTED=NO",
        "A2_R07_HISTORICAL_SOURCES_DELIVERED=ZERO",
        "A2_R07_SCORING=NOT_STARTED",
        "NEGATIVE_ACCESS_TEST_NOT_INSTRUMENTABLE",
    ):
        assert marker in report
    assert "No access-denied response was observed" in report
    assert "Temporary Chat status" in report
    assert "UNKNOWN" in report