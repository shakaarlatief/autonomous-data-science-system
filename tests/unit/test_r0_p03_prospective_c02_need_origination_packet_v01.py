"""Test exact fresh-author C02 handoff without viewing protected questions.

The original C01 source-free evidence and restricted case-level results are not
used as expected answers or opened. C02 remains an unscored, prospective cohort.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import (
    neutral_need_origination_packet as v1,
    neutral_need_origination_packet_v02 as v2,
    prospective_c02_need_origination_packet_v01 as c02,
)

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_BYTES = 3869
EXPECTED_SHA = "1bd83e8d689fd88524e883ec1537d1f51e3448af6026caac8ec285d165d3c7f6"


def test_exact_new_local_packet_and_one_file_upload_readback() -> None:
    r = c02.build(ROOT, verify_only=True)
    packet = ROOT / c02.FOLDER / c02.ARCHIVE_NAME
    upload = ROOT / c02.UPLOAD_DIR / c02.ARCHIVE_NAME
    assert packet.read_bytes() == upload.read_bytes()
    assert packet.stat().st_size == EXPECTED_BYTES
    assert r["archive_bytes"] == EXPECTED_BYTES
    assert r["archive_sha256"] == EXPECTED_SHA
    assert sha256(packet.read_bytes()).hexdigest() == EXPECTED_SHA
    assert set(x.name for x in (ROOT / c02.UPLOAD_DIR).iterdir()) == {c02.ARCHIVE_NAME}
    assert r["scored_tasks"] == "NONE"
    assert r["source_admissions"] == 0
    assert r["independent_actor"] == "NOT_STARTED"
    assert r["old_protected_questions"] == 0
    assert r["new_proposals"] == 0


def test_exact_neutral_zip_only_two_sources_without_comparator_or_gold() -> None:
    packet = ROOT / c02.FOLDER / c02.ARCHIVE_NAME
    prior = ROOT / v2.FOLDER / v2.ARCHIVE_NAME
    assert sha256(prior.read_bytes()).hexdigest() == (
        "f0685d22172faedd79d4becce56d36b3f6d38e4d7e320cb439918fa75a1a1880"
    )
    with ZipFile(packet) as current, ZipFile(prior) as previous:
        assert current.testzip() is None
        assert current.namelist() == ["AUTHOR_BRIEF.md", "NEUTRAL_CONTEXT.md"]
        assert current.read("NEUTRAL_CONTEXT.md") == previous.read("NEUTRAL_CONTEXT.md")
        assert current.read("AUTHOR_BRIEF.md") != previous.read("AUTHOR_BRIEF.md")
        assert sha256(current.read("NEUTRAL_CONTEXT.md")).hexdigest() == c02.HISTORICAL_CONTEXT_SHA256
        v1.check_author_texts({name: current.read(name) for name in current.namelist()})
        assert not any(name.startswith("sources/") for name in current.namelist())


def test_role_discipline_distinct_cohort_and_realistic_scope() -> None:
    with ZipFile(ROOT / c02.FOLDER / c02.ARCHIVE_NAME) as z:
        s = z.read("AUTHOR_BRIEF.md").decode("utf-8")
    for clause in (
        "fresh, independent contributor",
        "not convenient questions",
        "You cannot claim cross-cohort distinctness",
        "A different independent reviewer",
        "NOT_YET_ADJUDICATED",
        "Do not invoke web search",
        "human owner must download",
        "NEED_PROPOSALS_RESTRICTED.md",
        "NEED_ORIGINATION_SAFE_RECEIPT.md",
        "SCORING=NOT_STARTED",
    ):
        assert clause in s
    assert "No candidate is admitted or scored" in s


def test_cohort_manifest_source_horizon_and_no_task_promotion() -> None:
    texts, m = c02.content_and_manifest(ROOT)
    assert set(texts) == {"AUTHOR_BRIEF.md", "NEUTRAL_CONTEXT.md"}
    assert m["prospective_source_evidence_ceiling_before_any_new_question"] == (
        "47ed6344a9153dcf366769e95722840fbf1a8f8b"
    )
    assert m["old_historical_cohort"] == "PRESERVED_6_PROVISIONAL_6_MATERIAL_HOLD"
    assert m["cross_cohort_duplicate_adjudication"] == "PENDING_SEPARATE_PROTECTED_REVIEW"
    assert m["new_questions"] == "NOT_ORIGINATED"
    assert m["author_visible_sources"] == 0
    assert m["author_visible_question_or_answer_material"] == 0
    assert m["source_admissions"] == 0
    assert m["gold"] == "NONE"


def test_fails_closed_on_author_input_leakage(monkeypatch: pytest.MonkeyPatch) -> None:
    original = v1.check_author_texts

    def guarded(texts: dict[str, bytes]) -> None:
        leaked = dict(texts)
        leaked["AUTHOR_BRIEF.md"] += b"\nR0-P03 B1 has been selected\n"
        original(leaked)

    monkeypatch.setattr(c02.v1, "check_author_texts", guarded)
    with pytest.raises(ValueError, match="Recognized prior-design"):
        c02.content_and_manifest(ROOT)
