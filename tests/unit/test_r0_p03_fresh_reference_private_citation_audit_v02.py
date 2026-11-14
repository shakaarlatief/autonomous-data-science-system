"""Synthetic negative controls for the transparent V01-to-V02 audit correction.

V02 keeps V01's fixed report hash, Git pin and literal citation comparison.
Only the overly narrow source directory filter and incidental @ cell
classification change. No actual case-answer material is used in these tests.
"""
from __future__ import annotations

import pytest

from experiments.r0_p03_navigation_probe import (
    fresh_reference_private_citation_audit_v01 as old,
    fresh_reference_private_citation_audit_v02 as new,
)


def test_v02_preserves_original_input_and_literal_match_contract() -> None:
    assert new.PIN == old.PIN
    assert new.EXPECTED_REPORT_BYTES == old.EXPECTED_REPORT_BYTES
    assert new.EXPECTED_REPORT_SHA256 == old.EXPECTED_REPORT_SHA256
    assert new.LINE_SPEC_RE.pattern == old.LINE_SPEC_RE.pattern
    assert new.classify_literal_excerpt('"unmatched"', "other", "other") == "NO_LITERAL_MATCH"
    assert new.PRIVATE_AUDIT != old.PRIVATE_AUDIT
    assert new.PUBLIC_AGGREGATE != old.PUBLIC_AGGREGATE


@pytest.mark.parametrize("path", ["README.md", "pyproject.toml", ".github/workflows/test.yml", "docs/normal.md"])
def test_source_path_admission_is_entire_pinned_git_tree(path: str) -> None:
    new.validate_path(path)


@pytest.mark.parametrize("path", ["../x.md", "docs/../../x.md", "/tmp/x.md", "C:/private.md", "docs\\x.md", "docs//x.md"])
def test_source_path_still_rejects_unsafe_forms(path: str) -> None:
    with pytest.raises(ValueError):
        new.validate_path(path)


def test_incidental_at_field_does_not_count_as_broken_source_citation() -> None:
    report = (
        "| ID | Assertion | Class | Witness | Lines | Excerpt |\n"
        "| -- | -- | -- | -- | -- | -- |\n"
        "| 1 | fake | synthetic | owner@runtime | — | not a source reference |\n"
        "| 2 | fake | synthetic | README.md@" + "a" * 40 + ' | 1 | "fake original line" |\n'
        "| 3 | fake | synthetic | docs/invalid.md@bad | 1 | cannot parse |\n"
    )
    witnesses, invalid = new.extract_witnesses(report)
    assert len(witnesses) == 1
    assert witnesses[0].path == "README.md"
    assert invalid == 1


def test_no_stale_v01_prefix_filter_remains() -> None:
    import inspect
    body = inspect.getsource(new.validate_path)
    assert 'SOURCE_PATH_UNEXPECTED' not in body
    assert 'SOURCE_PATH_UNSAFE' in body
