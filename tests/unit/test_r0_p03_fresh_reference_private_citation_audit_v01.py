"""Synthetic-only tests for unscored R0-P03 private citation provenance.

No private answer text or private source-to-question mappings appear here.
"""
from __future__ import annotations

import json
import pytest

from experiments.r0_p03_navigation_probe import fresh_reference_private_citation_audit_v01 as audit


def test_frozen_pin_and_private_storage_contract() -> None:
    assert audit.PIN == "47ed6344a9153dcf366769e95722840fbf1a8f8b"
    assert audit.EXPECTED_REPORT_BYTES == 84359
    assert len(audit.EXPECTED_REPORT_SHA256) == 64
    assert audit.REPORT.parts[0] == ".venv"
    assert audit.PRIVATE_AUDIT.parts[0] == ".venv"
    assert audit.PUBLIC_AGGREGATE.parts[0] == "experiments"


@pytest.mark.parametrize(
    ("spec", "line_count", "expected"),
    [
        ("1", 3, (1,)),
        ("1-2", 3, (1, 2)),
        ("2, 1-2, 3", 3, (1, 2, 3)),
        ("5, 7-9", 9, (5, 7, 8, 9)),
    ],
)
def test_line_parser_positive(spec: str, line_count: int, expected: tuple[int, ...]) -> None:
    assert audit.parse_line_spec(spec, line_count) == expected


@pytest.mark.parametrize(
    "spec",
    ["", "0", "4", "3-2", "1-L2", "1, x", "1-10", "-1", "1, ", "1;2", "1, ../../x"],
)
def test_line_parser_rejects_invalid(spec: str) -> None:
    with pytest.raises(ValueError):
        audit.parse_line_spec(spec, 3)


@pytest.mark.parametrize(
    ("quote", "selected", "whole", "expected"),
    [
        ('"fixed original witness"', "fixed original witness", "fixed original witness", "EXACT_CITED_LINE_MATCH"),
        (chr(96) + "original   claim" + chr(96), "original claim", "original claim", "WHITESPACE_ONLY_CITED_LINE_MATCH"),
        ('"different passage"', "given line", "given line\ndifferent passage", "LITERAL_MATCH_ELSEWHERE_IN_SAME_BLOB"),
        ('"invented sentence"', "given line", "given line", "NO_LITERAL_MATCH"),
        ('""', "text", "text", "NO_LITERAL_MATCH"),
    ],
)
def test_literal_quote_fidelity(quote: str, selected: str, whole: str, expected: str) -> None:
    assert audit.classify_literal_excerpt(quote, selected, whole) == expected


@pytest.mark.parametrize(
    "path",
    ["../secret.md", "docs/../../secret.md", "/tmp/source.md", "C:/secret.md", "docs\\bad.md", "secrets/file.md"],
)
def test_source_path_guards(path: str) -> None:
    with pytest.raises(ValueError):
        audit.validate_path(path)


def test_synthetic_reference_parser_and_unparsed_citation() -> None:
    report = (
        "| ID | Claim | Class | Witness | Lines | Excerpt |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        "| 01 | fake claim | synthetic | docs/synthetic_example.md@" + "a" * 40
        + ' | 1-2 | "fake source quotation" |\n'
        "| 02 | invalid citation | synthetic | docs/no_blob.md@bad | 1 | invalid |\n"
        "| 03 | no citation | synthetic | — | — | — |\n"
    )
    witnesses, unparsed = audit.extract_witnesses(report)
    assert len(witnesses) == 1
    assert witnesses[0].path == "docs/synthetic_example.md"
    assert witnesses[0].blob_oid == "a" * 40
    assert unparsed == 1


def test_synthetic_original_git_verification_and_negative_controls(monkeypatch: pytest.MonkeyPatch) -> None:
    path = "docs/synthetic_example.md"
    valid_oid = "c" * 40
    sources = {path: (valid_oid, ["first original line", "second original line"])}
    monkeypatch.setattr(audit, "historical_source", lambda reported, cache: sources[reported])
    cases = [
        audit.Witness(10, path, valid_oid, "1", '"first original line"'),
        audit.Witness(11, path, valid_oid, "2", '"first original line"'),
        audit.Witness(12, path, "d" * 40, "1", '"first original line"'),
        audit.Witness(13, path, valid_oid, "999", '"first original line"'),
        audit.Witness(14, path, valid_oid, "1", '"fabricated original line"'),
    ]
    counts, details = audit.evaluate(cases)
    assert counts["citation_rows"] == 5
    assert counts["historical_blob_ids_verified"] == 4
    assert counts["historical_line_ranges_valid"] == 3
    assert counts["EXACT_CITED_LINE_MATCH"] == 1
    assert counts["LITERAL_MATCH_ELSEWHERE_IN_SAME_BLOB"] == 1
    assert counts["BLOB_ID_MISMATCH"] == 1
    assert counts["LINE_RANGE_INVALID"] == 1
    assert counts["NO_LITERAL_MATCH"] == 1
    assert len(details) == 5


def test_public_summary_contains_no_fake_case_specific_text() -> None:
    public = {
        "audit_id": "FAKE",
        "verification_counts": {"citation_rows": 5, "historical_blob_ids_verified": 4},
        "detailed_source_paths_or_quotes_in_public_output": False,
        "semantic_claim_entailment_checked": False,
        "independent_gold_or_scored_R0_P03_qualified": False,
    }
    encoded = json.dumps(public)
    assert "docs/synthetic_example.md" not in encoded
    assert "fabricated original line" not in encoded
