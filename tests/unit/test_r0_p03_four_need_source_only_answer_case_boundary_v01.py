"""Case-local source-boundary tests for frozen A/B source-only answers.

Tests are synthetic or hash-grounded against already published source-only
inputs. They do not read independent private reference answers or historical
source bodies and do not promote self-grades to formal Research 513 gold.
"""
from __future__ import annotations

from hashlib import sha256

import pytest

from experiments.r0_p03_navigation_probe import (
    four_need_source_only_answer_case_boundary_audit_v01 as audit,
)


def test_original_immutable_inputs_and_frozen_four_need_shape() -> None:
    for key in ("A", "B"):
        answer_path, answer_sha = audit.ANSWERS[key]
        packet_path, packet_sha = audit.PACKETS[key]
        assert sha256(answer_path.read_bytes()).hexdigest() == answer_sha
        assert sha256(packet_path.read_bytes()).hexdigest() == packet_sha
        assert len(audit.case_sections(answer_path.read_text("utf8"))) == 4


def test_synthetic_cross_case_source_reference_rejected() -> None:
    first = ("docs/synthetic_a.md", "a" * 40)
    second = ("docs/synthetic_b.md", "b" * 40)
    third = ("docs/other.md", "c" * 40)
    allowed = [{first}, {second}, set(), set()]
    text = (
        "The first source is cited at "
        + first[0] + "@" + first[1] + ":L5. "
        + "But the second source is cross-case at "
        + second[0] + "@" + second[1] + ":L11. "
        + "And the unknown source is outside at "
        + third[0] + "@" + third[1] + ":L17."
    )
    result = audit.count_case_references(text, 1, allowed)
    assert result["explicit_source_reference_occurrences"] == 3
    assert result["case_local_full_source_reference_occurrences"] == 1
    assert result["cross_case_full_source_reference_occurrences"] == 1
    assert result["outside_packet_full_source_reference_occurrences"] == 1


def test_synthetic_case_local_reference_not_equivalent_to_claim_truth() -> None:
    a = ("docs/fake_source.md", "f" * 40)
    allowed = [{a}, set(), set(), set()]
    section = "A fully fabricated claim cited " + a[0] + "@" + a[1] + ":L5."
    result = audit.count_case_references(section, 1, allowed)
    assert result["case_local_full_source_reference_occurrences"] == 1
    # There is deliberately no entailment-verdict field in this parser.
    assert not any("support" in key or "truth" in key for key in result)


def test_case_section_parser_only_accepts_exact_four_ordered_anchors() -> None:
    valid = "## N01 A\none\n## N02 B\ntwo\n## N03 C\nthree\n## N04 D\nfour\n## Outcome summary\n"
    assert audit.case_sections(valid) == {1: "\none\n", 2: "\ntwo\n", 3: "\nthree\n", 4: "\nfour\n"}
    with pytest.raises(ValueError):
        audit.case_sections("## N01\n## N02\n## N04\n")
    with pytest.raises(ValueError):
        audit.case_sections("## N02 B\n## N01 A\n## N03 C\n## N04 D\n")


def test_frozen_answer_audit_is_not_a_formal_scored_result() -> None:
    output = audit.build()
    assert output["original_git_source_bodies_read"] is False
    assert output["private_original_reference_report_accessed"] is False
    assert output["full_citation_line_or_semantic_entailment_audited"] is False
    assert output["shorthand_references_completely_verified"] is False
    assert output["formal_r0_p03_score"] is None
    assert output["architecture_selection"] is None
    assert sum(
        x["aggregate_reference_counts"]["explicit_source_reference_occurrences"]
        for x in output["treatments"].values()
    ) >= 30
