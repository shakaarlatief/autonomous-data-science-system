"""Regression and exact-original evidence for the versioned V02 selector repair.

Declared references are source-authored metadata only. These tests do not
establish authoritative governance, natural-owner J2 or editorial B2 links.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_reference_provenance_audit_v01 import RESULT as V01
from experiments.r0_p03_navigation_probe.exploratory_reference_declaration_correction_v02 import (
    RESULT, V01_SHA256, corrected_flags, independent_eligible_path_occurrences,
    is_adjacent_path_selector, run,
)

EXPECTED_BYTES = 175032
EXPECTED_SHA256 = "25b26e66e3bb03232d4ee7931e66aceb6bd6eaf28d2f5ae0ff207713c333831d"


def test_path_selector_scope_is_exactly_adjacent_to_each_current_token() -> None:
    line = "path:docs/a.md docs/b.md path:docs/c.md"
    assert is_adjacent_path_selector(line, line.index("docs/a.md"))
    assert not is_adjacent_path_selector(line, line.index("docs/b.md"))
    assert is_adjacent_path_selector(line, line.index("docs/c.md"))
    assert not is_adjacent_path_selector("docs/a.md", 0)


def test_declared_references_indicators_are_source_authored_not_semantic_trust() -> None:
    line = "**Declared references:** " + chr(96) + "path:docs/a.md" + chr(96) + " docs/b.md"
    at = line.index("docs/a.md")
    entry = {"raw_original_line": line, "char_start": at,
             "indicators": ["GOVERNANCE_WORDING", "PATH_SELECTOR"]}
    assert corrected_flags(entry) == [
        "DECLARED_REFERENCES_FIELD", "GOVERNANCE_WORDING", "PATH_SELECTOR"
    ]
    entry["char_start"] = line.index("docs/b.md")
    assert corrected_flags(entry) == ["GOVERNANCE_WORDING"]
    entry["raw_original_line"] = '"path:docs/a.md"'
    entry["char_start"] = entry["raw_original_line"].index("docs/a.md")
    assert corrected_flags(entry) == ["GOVERNANCE_WORDING", "PATH_SELECTOR"]


def test_exact_eligible_path_scanner_reports_known_terminal_punctuation_limit() -> None:
    sources = {
        "docs/a.md": b"See docs/b.md. Link docs/b.md#section. "
                     b"Not docs/b.md.backup. Not docs/missing.md.",
        "docs/b.md": b"Nothing here.",
    }
    found = independent_eligible_path_occurrences(sources, set(sources))
    assert sum(found.values()) == 2
    assert set(k[:2] for k in found) == {("docs/a.md", "docs/b.md")}


def test_actual_v02_result_exact_replay_with_immutable_v01_and_no_silent_rewrite() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXPECTED_BYTES
    assert sha256(raw).hexdigest() == EXPECTED_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    assert sha256(V01.read_bytes()).hexdigest() == V01_SHA256
    current = json.loads(raw)
    assert run() == current
    v01 = json.loads(V01.read_text(encoding="utf-8"))
    assert current["v01_exact_sha256"] == V01_SHA256
    assert current["source_line_identity_unchanged"]
    assert current["changed_occurrence_flag_records"] == 18
    assert current["alternate_exact_path_enumeration"] == {
        "matching_original_occurrences": 146,
        "matching_original_directed_pairs": 110,
        "new_occurrences_in_this_pinned_corpus": 0,
        "known_legacy_regex_terminal_period_blind_spot": True,
    }
    assert len(v01["occurrences"]) == len(current["occurrences"]) == 146
    for old, new in zip(v01["occurrences"], current["occurrences"]):
        assert {
            k: v for k, v in old.items() if k != "indicators"
        } == {
            k: v for k, v in new.items() if k != "indicators"
        }
        assert (set(old["indicators"]) - {"PATH_SELECTOR"}) <= set(new["indicators"])


def test_real_source_declared_reference_fields_are_not_qualified_governed_edges() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    meta = report["metadata"]
    adjacent = meta["adjacent_path_selector"]
    declared = meta["source_declared_references_field"]
    assert adjacent["occurrence_count"] == adjacent["distinct_directed_pairs"] == 18
    assert adjacent["source_count"] == 12
    assert declared["occurrence_count"] == declared["distinct_directed_pairs"] == 11
    assert declared["source_count"] == 6
    assert declared["target_count"] == 7
    assert not adjacent["semantic_authority_accepted"]
    assert not declared["semantic_authority_accepted"]
    for i in declared["occurrence_indices"]:
        row = report["occurrences"][i]
        assert "DECLARED_REFERENCES_FIELD" in row["indicators"]
        assert "PATH_SELECTOR" in row["indicators"]
        assert "**Declared references:**" in row["raw_original_line"]
        assert row["semantic_authority_disposition"] == "NOT_ADJUDICATED"
    summary = report["summary"]
    assert summary["occurrences_with_indicator"]["PATH_SELECTOR"] == 18
    sizes = {k: v["distinct_directed_edges"] for k, v in summary["source_coverage_by_projection"].items()}
    assert sizes == {
        "RAW_PATH_MENTIONS": 110,
        "OUTSIDE_FENCE": 40,
        "OTHER_TEXT_ONLY": 7,
        "MARKDOWN_LINKS_ONLY": 0,
    }
    assert report["formal_r0_p03_scored"] is False
