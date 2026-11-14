"""Source-free postreview reconciliation contract tests.

These tests read only exact-identity public source-free reviewer and protocol
aggregate records. They do not use historical source bodies, the private
reference key, per-claim reviewer reasons, or model-facing source excerpts.
Self-reported or model-reviewed claim item counts are not scored accuracy.
"""
from __future__ import annotations

from hashlib import sha256

import pytest

from experiments.r0_p03_navigation_probe import (
    four_need_public_claim_support_reconciliation_v01 as recon,
)


def synthetic_tables(bad: bool = False) -> str:
    tick = chr(96)
    rows = "\n".join(
        f"| N{i:02d}-{t} | 2 | {2 if bad else 1} | 0 | 1 | 0 | 0 |"
        for i in range(1, 5)
        for t in ("P", "Q")
    )
    labels = "\n".join(
        f"| N{i:02d} | {tick}SIMILAR_OR_INCOMPARABLE{tick} | sample |"
        for i in range(1, 5)
    )
    return rows + "\n" + labels


def test_expected_frozen_source_free_inputs_are_verified() -> None:
    for path, expected in (
        (recon.REVIEW, recon.REVIEW_SHA),
        (recon.SOURCE_BOUNDARY, recon.BOUNDARY_SHA),
        (recon.MANIFEST, recon.MANIFEST_SHA),
        (recon.REVIEW_FIXTURE, recon.REVIEW_FIXTURE_SHA),
    ):
        assert sha256(path.read_bytes()).hexdigest() == expected


def test_synthetic_review_rows_totals_and_comparison_labels() -> None:
    table, compared = recon.parse_review(synthetic_tables())
    assert len(table) == 8
    assert len(compared) == 4
    assert sum(x["items"] for x in table.values()) == 16
    assert table["N01-P"]["unsupported_or_out_of_case"] == 1
    assert all(x == "SIMILAR_OR_INCOMPARABLE" for x in compared.values())


def test_synthetic_miscounted_review_rejected() -> None:
    with pytest.raises(ValueError, match="do not sum"):
        recon.parse_review(synthetic_tables(bad=True))


def test_mask_method_recovery_is_question_fixed_and_balanced() -> None:
    ids = [f"R0P03-PILOT-N{i:02d}" for i in range(1, 5)]
    result = recon.p_method(ids)
    assert result == recon.p_method(list(reversed(ids)))
    assert list(result.values()).count("A") == 2
    assert list(result.values()).count("B") == 2


def test_reconciliation_preserves_original_protocol_limits() -> None:
    report = recon.build()
    counts = report["source_free_claim_items_by_reviewer"]
    assert counts == {
        "items": 192,
        "supported": 170,
        "partial_or_overbroad": 11,
        "unsupported_or_out_of_case": 9,
        "contradicted": 0,
        "insufficient": 2,
    }
    assert report["original_question_fully_covered_count"] == 0
    assert report["formal_R0_P03_scored"] is False
    assert report["physical_architecture_selected"] is False
    assert report["claim_units_include_correct_abstentions_and_qualifications"] is True
    assert report["support_claims_are_interpretive_not_independent_gold"] is True
    assert [
        (row["original_need"], row["source_conditioned_supported_coverage_favored_method"])
        for row in report["source_conditioned_observations"]
    ] == [
        ("N01", "BODY_PLUS_HEADING_RRF_DIAGNOSTIC"),
        ("N02", "NONE_OR_INCOMPARABLE"),
        ("N03", "BODY_BM25"),
        ("N04", "BODY_PLUS_HEADING_RRF_DIAGNOSTIC"),
    ]


def test_exact_original_public_output_replay() -> None:
    expected = recon.canonical(recon.build())
    assert recon.OUTPUT.read_bytes() == expected
    assert sha256(expected).hexdigest() == "c0ea416a8efdeed70803f76603948e331e575673471ab1af03cb86358a1932c4"
