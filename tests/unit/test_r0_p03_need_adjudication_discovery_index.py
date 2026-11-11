"""Actual original-Git locator index for non-arm source adjudication.

The fixed roster is a discovery aid, not an independently accepted corpus.
No real candidate tasks, restricted assessments, old relevance labels or
historical gold are opened in these tests.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from zipfile import ZipFile
import pytest

from experiments.r0_p03_navigation_probe import (
    primary_need_adjudication_discovery_packet as packet,
    source_world_coverage_gate as world,
)

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / packet.FOLDER / packet.ARCHIVE_NAME
RECEIPT = ROOT / packet.FOLDER / packet.RECEIPT_NAME
ZIP_SHA = "8840aa1762f8e729fed056d8038928674b0edf82acfed4c92204cae1dd68cac8"
INDEX_SHA = "88b6a2677535cbc90e7aed8a1a8a2a6ecd8a6261abbb5a2307544545a7329881"


def test_archive_exact_original_census_and_no_source_content() -> None:
    receipt = packet.build(ROOT, verify_only=True)
    assert receipt["archive_bytes"] == 217929
    assert receipt["archive_sha256"] == ZIP_SHA
    assert receipt["index_sha256"] == INDEX_SHA
    assert receipt["indexed_source_paths"] == 2409
    assert receipt["excluded_or_unsupported_source_records"] == 130
    assert receipt["actual_original_source_bodies_delivered"] == 0
    assert receipt["private_questions_delivered"] == 0
    assert receipt["source_admissions"] == 0
    assert receipt["independent_reference_review"] == "NOT_STARTED"
    assert sha256(ARCHIVE.read_bytes()).hexdigest() == ZIP_SHA
    assert packet.canonical(receipt) == RECEIPT.read_bytes()
    with ZipFile(ARCHIVE) as z:
        assert z.namelist() == ["ADJUDICATOR_BRIEF.md", "INDEX.json"]
        assert z.testzip() is None
        index = json.loads(z.read("INDEX.json"))
        assert sha256(z.read("INDEX.json")).hexdigest() == INDEX_SHA
        assert index["index_record_count"] == 2409
        assert index["historical_git_revision"] == world.PIN
        assert index["exact_source_bytes_in_archive"] == 0
        assert index["private_candidate_questions_in_archive"] == 0
        paths = [r["path"] for r in index["files"]]
        assert paths == sorted(set(paths))
        assert len(paths) == 2409
        assert all(r["qualification"] == "NOT_ADMITTED_REVIEW_ONLY_LOCATOR"
                   for r in index["files"])
        assert not any(packet.PATH_EXCLUDE.search(p) for p in paths)
        assert not any("source content:" in p.lower() for p in paths)


def test_actual_review_brief_requires_exact_pinned_source_and_usable_evidence() -> None:
    with ZipFile(ARCHIVE) as z:
        brief = z.read("ADJUDICATOR_BRIEF.md").decode("utf-8")
    assert "NOT twelve preaccepted scored questions" in brief
    assert world.PIN in brief
    assert "raw.githubusercontent.com/shakaarlatief/autonomous-data-science-system" in brief
    for marker in (
        "read-only raw Git URL", "ONLY network", "exact paths from INDEX.json",
        "Verify actual fetched byte lengths", "original contents",
        "not automatically governing truth",
        "MISSING_EVIDENCE/HOLD", "UNANSWERABLE_AS_STATED",
        "NEED_SOURCE_ADJUDICATION_RESTRICTED.md",
        "NEED_SOURCE_ADJUDICATION_AGGREGATE.md",
        "three categories",  # intentional negative checked below
    ):
        if marker == "three categories":
            assert marker not in brief
        else:
            assert marker in brief
    assert "four categories" in brief
    assert "Do not act as a scored agent" in brief


def test_path_exclusion_explicit_old_answers_and_unknown_modalities() -> None:
    roster, _ = world.compute(ROOT)
    copied = deepcopy(roster)
    for row in copied["source_records"]:
        if row["path"].startswith("docs/research/"):
            row["path"] = "docs/research/217_w5_t1_old_reference.md"
            break
    copied["roster_sha256"] = world._fingerprint(copied["source_records"])
    indexed = packet.indexed(copied)
    assert "docs/research/217_w5_t1_old_reference.md" not in {
        r["path"] for r in indexed
    }
    copied = deepcopy(roster)
    for row in copied["source_records"]:
        if row["path"] == "README.md":
            row["flags"] = ["KNOWN_SCORING_DESIGN_RISK"]
            break
    copied["roster_sha256"] = world._fingerprint(copied["source_records"])
    indexed = packet.indexed(copied)
    assert "README.md" not in {r["path"] for r in indexed}


def test_inconsistent_census_or_fake_source_admissions_fail_closed() -> None:
    roster, _ = world.compute(ROOT)
    changed = deepcopy(roster)
    changed["source_ref"] = "a" * 40
    with pytest.raises(ValueError, match="identity"):
        packet.indexed(changed)
    changed = deepcopy(roster)
    changed["source_count"] = 1
    with pytest.raises(ValueError, match="identity"):
        packet.indexed(changed)
    changed = deepcopy(roster)
    changed["source_records"][0]["status"] = "ADMITTED"
    changed["roster_sha256"] = world._fingerprint(changed["source_records"])
    with pytest.raises(ValueError, match="Corrupt"):
        packet.indexed(changed)


def test_never_reads_private_local_question_paths() -> None:
    import inspect
    source = inspect.getsource(packet)
    assert "NEED_PROPOSALS_RESTRICTED.md" in source
    assert 'Path("NEED_PROPOSALS_RESTRICTED.md").read_bytes' not in source
    assert 'Path("NEED_PROPOSALS_RESTRICTED.md").read_text' not in source
    assert "source_world_coverage_gate" in source
    assert packet.FOLDER.is_relative_to(Path(".venv"))
