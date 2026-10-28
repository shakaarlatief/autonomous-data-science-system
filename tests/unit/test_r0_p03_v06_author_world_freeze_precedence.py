"""Source-free method-text guards for the V0.6 world-freeze precedence amendment.

The external focused V0.5 critique demonstrated a textual ambiguity between
component/bundle authorization and the complete assembled author-world freeze.
These tests protect the newly stated ordering, pre-freeze restricted testing
exception, and the earlier M1/M2 semantic proposal protections. They are not
a formal proof of correct semantic source judgments, a credential/identity
test, an author-interface leak test, or independent acceptance of V0.6.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments" / "r0_p03_navigation_probe"
V05 = BASE / "NON_ARM_SOURCE_STATUS_REVIEWER_CONTRACT_CANDIDATE_V05.md"
V06 = BASE / "NON_ARM_SOURCE_STATUS_REVIEWER_CONTRACT_CANDIDATE_V06.md"
REVIEW = (
    BASE / "reviewer_intake_evidence"
    / "20261028_v05_focused_independent_method_review_report.txt"
)


def section(text: str, section_number: int) -> str:
    """Return one numbered method section, without borrowing later clauses."""
    start = text.index(f"## {section_number}. ")
    end = text.find(f"\n## {section_number + 1}. ", start + 4)
    return text[start:end if end >= 0 else None]


def test_exact_reviewed_v05_is_immutable() -> None:
    data = V05.read_bytes()
    assert len(data) == 28270
    assert hashlib.sha256(data).hexdigest() == (
        "1c787fe7daa1222b2923c06891b4db72717a0d9c32126ebaac846d31c27ae79a"
    )
    assert "V05_NOT_INDEPENDENTLY_ACCEPTED" in data.decode("utf-8")


def test_complete_owner_relayed_external_report_is_preserved() -> None:
    data = REVIEW.read_bytes()
    assert len(data) == 25656
    assert hashlib.sha256(data).hexdigest() == (
        "1d007c27b539bfe09ea5ce800f1632a07eca0794a23258e1a15e5409584496c1"
    )
    assert b"\r" not in data
    assert not data.endswith(b"\n")
    assert len(data.splitlines()) == 336
    content = data.decode("utf-8")
    for marker in (
        "M1-A: Valid",
        "M2-A: Valid",
        "AMEND_MATERIAL_STAGE_DEFECT",
        "Atomic-bundle authorization versus complete author-world freeze",
        "WORLD_UNFROZEN",
        "WORLD_FROZEN",
    ):
        assert marker in content


def test_new_version_is_prospective_not_independently_accepted() -> None:
    text = V06.read_text(encoding="utf-8")
    assert text.startswith(
        "# R0-P03 non-arm source-status reviewer contract candidate V0.6"
    )
    assert "V06_NOT_INDEPENDENTLY_ACCEPTED" in text
    assert "V05_EXTERNAL_FOCUSED_CHALLENGE=AMEND_MATERIAL_STAGE_DEFECT" in text
    assert (
        "V06_WORLD_FREEZE_BEFORE_PRIMARY_AUTHOR_DISCLOSURE="
        "PROPOSED_NOT_INDEPENDENTLY_CHECKED"
    ) in text


def test_component_authorization_does_not_release_to_primary_author() -> None:
    text = V06.read_text(encoding="utf-8")
    rule = section(text, 1)
    assert "normative precedence" in rule
    assert "eligible for inclusion in a prospective assembled author-world packet only" in rule
    assert "even `AUTHORIZATION_GRANTED` at component or packet-screen scope" in rule
    assert "does **not** itself permit revealing" in rule
    assert "`WORLD_UNFROZEN`" in rule
    assert "Primary task-author disclosure is prohibited until" in rule
    assert "reached `WORLD_FROZEN`" in rule


def test_reviewer_only_prefreeze_witness_has_distinct_authority() -> None:
    rule = section(V06.read_text(encoding="utf-8"), 1)
    assert "only **separately authorized protected-access reviewer" in rule
    assert "expressly disqualified from acting as the neutral primary task author" in rule
    assert "author-view witness needed for freeze" in rule
    assert "not** primary task-author disclosure" in rule
    assert "cannot import reviewer-only evidence into the final packet" in rule


def test_bundle_authorization_is_inclusion_and_world_gate_is_additional() -> None:
    text = V06.read_text(encoding="utf-8")
    bundle = section(text, 7)
    world = section(text, 8)
    assert "for **prospective packet inclusion**" in bundle
    assert "Primary task-author disclosure still requires separate acceptance" in bundle
    assert "does not by itself unlock the neutral task-author interface" in bundle
    assert "cannot be disclosed to the neutral primary task author" in world
    assert "even if no particular missing family has been proven" in world
    assert "not a fabricated semantic content deficiency" in world


@pytest.mark.parametrize(
    "token", [
        "`CANDIDATE_FULL`",
        "`CANDIDATE_EXCERPT`",
        "`AUXILIARY_EVIDENCE_ONLY`",
        "`PROHIBIT_DESIGN_OR_GOLD`",
        "`HOLD_FOR_SOURCE_REVIEW`",
        "`UNSUPPORTED_REPRESENTATION`",
    ]
)
def test_all_six_source_content_dispositions_still_defined(token: str) -> None:
    text = section(V06.read_text(encoding="utf-8"), 3)
    assert f"- {token}:" in text


def test_independent_challenge_and_author_world_transitions_remain_distinct() -> None:
    release = section(V06.read_text(encoding="utf-8"), 9)
    assert "Component/bundle release authorization" in release
    assert "whole-world acceptance and `WORLD_FROZEN`" in release
    assert "Whole author-world freeze and task-author disclosure" in release
    assert "protected prefreeze author-view witness" in release
    assert "only then** may the neutral primary task author" in release


def test_m1_m2_semantic_proposal_paths_are_not_regressed() -> None:
    text = V06.read_text(encoding="utf-8")
    one = section(text, 1)
    seven = section(text, 7)
    assert "a typed dependency-closure attribute" in one
    assert "A substantively adequate but not yet independently challenged" in one
    assert "`CHALLENGE_PENDING`" in one
    assert "do **not** relabel the semantic source as HOLD" in seven
    assert "material gap, plausible controlling exception" in seven
    assert "uninspected placeholders" in seven


def test_original_science_and_no_premature_authorship() -> None:
    text = V06.read_text(encoding="utf-8")
    eleven = section(text, 11)
    assert "AUTHOR_SOURCE_ADMISSIONS=0" in eleven
    assert "AUTHOR_WORLD=UNFROZEN" in eleven
    assert "PRIMARY_TASKS=NOT_AUTHORED" in eleven
    assert "GOLD=NONE" in eleven
    assert "B0_B4_SCORING=NOT_STARTED" in eleven
    assert "CHECKPOINT=898_UNCHANGED" in eleven
    assert "SPECIFICATION_028=UNCHANGED" in eleven
    assert "No coordinator self-certification" in section(text, 10)
