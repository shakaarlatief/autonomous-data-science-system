"""Regression guards for prospective source-status V0.5 method text.

These checks verify exact source-free text invariants after an externally
authored V0.4 adversarial critique. They deliberately do NOT claim machine
verification of historical-source semantics, independent review, restricted
output custody, release authority or experimental quality. The bounded
textual assertions simply prevent accidental reintroduction of the two
documented prechallenge stage-precedence contradictions or weakening of
existing disqualification requirements.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
METHOD_BASE = PROJECT_ROOT / "experiments" / "r0_p03_navigation_probe"
V04 = METHOD_BASE / "NON_ARM_SOURCE_STATUS_REVIEWER_CONTRACT_CANDIDATE_V04.md"
V05 = METHOD_BASE / "NON_ARM_SOURCE_STATUS_REVIEWER_CONTRACT_CANDIDATE_V05.md"
REVIEW = (METHOD_BASE / "reviewer_intake_evidence" /
          "20261028_v04_independent_method_review_report.txt")


def _text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _section(source: str, number: int) -> str:
    start = source.index(f"## {number}. ")
    end = source.find(f"\n## {number + 1}. ", start + 4)
    return source[start:end if end >= 0 else None]


def test_exact_external_target_is_unchanged() -> None:
    original = V04.read_bytes()
    assert len(original) == 23276
    assert hashlib.sha256(original).hexdigest() == (
        "b9945bd4fb36a7da1b4573b3ccc8c54cc92add02b1c4d0c412ffdbafd108f39d"
    )
    assert "SOURCE_STATUS_CONTRACT=V04_PROSPECTIVE_UNACCEPTED" in original.decode()


def test_external_review_normalized_complete_and_not_misrepresented() -> None:
    original = REVIEW.read_bytes()
    assert len(original) == 48885
    assert hashlib.sha256(original).hexdigest() == (
        "449e411a1c55e3ba7b6dc62f414a7f98579f29eb451f6bdade06e7ee11e461bf"
    )
    assert b"\r" not in original
    assert not original.endswith(b"\n")
    assert len(original.splitlines()) == 634
    text = original.decode("utf-8")
    for required in (
        "Finding M1", "Finding M2", "AMEND_MATERIAL_CONTRADICTION",
        "AUTHORIZED_FALSE_ADMISSION_PATHWAY=NOT_DEMONSTRATED",
        "REAL_SOURCE_RECORDS_INSPECTED=0",
        "SOURCE_ADMISSION_AUTHORIZATION=NOT_REQUESTED",
    ):
        assert required in text


def test_v05_is_distinct_prospective_unaccepted_version() -> None:
    source = _text(V05)
    assert source.startswith(
        "# R0-P03 non-arm source-status reviewer contract candidate V0.5"
    )
    assert "V05_NOT_INDEPENDENTLY_ACCEPTED" in source
    assert "M1_M2_STAGE_PRECEDENCE_REPAIRED" in source
    assert "V04_EXTERNAL_METHOD_TEXT_CHALLENGE=AMEND_MATERIAL_CONTRADICTION" in source
    assert "V05_M1_M2_STAGE_PRECEDENCE_REPAIR=PROPOSED_NOT_INDEPENDENTLY_CHECKED" in source


def test_m1_positive_context_conditional_proposals_not_preaccepted() -> None:
    source = _text(V05)
    opening = _section(source, 1)
    context = _section(source, 5)
    bundle = _section(source, 7)
    assert "A complete, substantively inspected dependency bundle" in opening
    assert "only as a typed dependency-closure attribute" in opening
    assert "At **semantic proposal stage**" in context
    assert "independent acceptance is not required **to record**" in context
    assert "At **author disclosure stage**" in context
    assert "independently accepted and released" in context
    assert "not refer to uninspected placeholders" in bundle
    assert "No bundle member is individually or atomically released" in bundle


def test_m1_missing_or_prohibited_context_still_blocks_substantively() -> None:
    source = _text(V05)
    context = _section(source, 5)
    bundle = _section(source, 7)
    assert "context is absent, uninspected, prohibited or materially inadequate" in context
    assert "assign the appropriate scoped substantive HOLD/veto" in context
    assert "one component is prohibited, missing or unqualified" in bundle
    assert "the bundle stays held" in bundle
    assert "reviewer-private explanation" in context


def test_m2_adequate_unchallenged_coverage_not_semantically_held() -> None:
    coverage = _section(_text(V05), 7)
    assert "**Typed coverage precedence:**" in coverage
    assert "substantively adequate" in coverage
    assert "If substantive negative-search adequacy is established" in coverage
    assert "record `CHALLENGE_PENDING`" in coverage
    assert "hold the **exposure** at `RELEASE_HOLD`" in coverage
    assert "do **not** relabel the semantic source as HOLD" in coverage


def test_m2_real_coverage_gaps_and_world_deficits_still_block() -> None:
    coverage = _section(_text(V05), 7)
    assert "material gap, plausible controlling exception" in coverage
    assert "receives `HOLD_FOR_SOURCE_REVIEW`" in coverage
    assert "required **before release**" in coverage
    assert "`HOLD_SOURCE_WORLD_INCOMPLETE`" in coverage
    assert "not a seventh source disposition" in coverage


@pytest.mark.parametrize("key", [
    "`CANDIDATE_FULL`",
    "`CANDIDATE_EXCERPT`",
    "`AUXILIARY_EVIDENCE_ONLY`",
    "`PROHIBIT_DESIGN_OR_GOLD`",
    "`HOLD_FOR_SOURCE_REVIEW`",
    "`UNSUPPORTED_REPRESENTATION`",
])
def test_all_six_source_content_dispositions_remain_defined(key: str) -> None:
    definitions = _section(_text(V05), 3)
    assert f"- {key}:" in definitions


def test_release_and_actor_science_gates_survive() -> None:
    source = _text(V05)
    release = _section(source, 9)
    boundaries = _section(source, 11)
    assert "`AUTHORIZATION_GRANTED`" in release
    assert "`CHALLENGED_DISPUTED`" in release
    assert "separately approved authority" in release
    assert "No unassigned party can mark" in release
    assert "S1" in boundaries and "S2" in boundaries and "S3" in boundaries
    assert "AUTHOR_SOURCE_ADMISSIONS=0" in boundaries
    assert "GOLD=NONE" in boundaries
    assert "B0_B4_SCORING=NOT_STARTED" in boundaries
    assert "CHECKPOINT=898_UNCHANGED" in boundaries
    assert "SPECIFICATION_028=UNCHANGED" in boundaries


def test_next_independent_review_is_not_simulated_as_complete() -> None:
    text = _section(_text(V05), 10)
    assert "not yet independently tested **V0.5**" in text
    assert "test exactly two invented situations" in text
    assert "not a claim those tests have been independently run" in text
    assert "independently qualified downstream" in text
