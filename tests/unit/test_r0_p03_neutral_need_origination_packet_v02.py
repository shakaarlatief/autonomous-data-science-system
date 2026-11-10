"""Prospective author-role V02 correction without retrospective V01 mutation.

Checks operational ability vs actual forbidden exposure, practical download
custody vs unsupported host guarantees, and no change to the neutral context.
It does not generate, see or adjudicate protected task proposals.
"""
from __future__ import annotations

from hashlib import sha256
from pathlib import Path
from zipfile import ZipFile
import pytest

from experiments.r0_p03_navigation_probe import (
    neutral_need_origination_packet as v1,
    neutral_need_origination_packet_v02 as v2,
)

ROOT = Path(__file__).resolve().parents[2]
V1_PATH = ROOT / v1.LOCAL_FOLDER / v1.ARCHIVE_NAME
V2_PATH = ROOT / v2.FOLDER / v2.ARCHIVE_NAME


def test_exact_v01_aborted_packet_preserved() -> None:
    assert sha256(V1_PATH.read_bytes()).hexdigest() == v2.V01_ARCHIVE_SHA256
    with ZipFile(V1_PATH) as old:
        text = old.read("AUTHOR_BRIEF.md").decode("utf-8")
        assert "can read material beyond the supplied input" in text


def test_v02_changes_only_prospective_brief_and_preserves_neutral_input() -> None:
    with ZipFile(V1_PATH) as old, ZipFile(V2_PATH) as new:
        assert old.namelist() == new.namelist() == [
            "AUTHOR_BRIEF.md", "NEUTRAL_CONTEXT.md"
        ]
        assert old.read("NEUTRAL_CONTEXT.md") == new.read("NEUTRAL_CONTEXT.md")
        assert sha256(new.read("NEUTRAL_CONTEXT.md")).hexdigest() == (
            v2.V01_CONTEXT_SHA256
        )
        assert old.read("AUTHOR_BRIEF.md") != new.read("AUTHOR_BRIEF.md")
        assert new.testzip() is None
        texts = {name: new.read(name) for name in new.namelist()}
    v1.check_author_texts(texts)
    assert len(texts) == 2
    assert not any(n.startswith("sources/") for n in texts)


def test_v02_role_operational_contamination_and_output_contract() -> None:
    with ZipFile(V2_PATH) as z:
        text = z.read("AUTHOR_BRIEF.md").decode("utf-8")
    for required in (
        "available but unused general-purpose capability",
        "not by itself disqualifying",
        "Do not invoke it",
        "Stop without originating proposals",
        "actually accessed other project/evaluation evidence",
        "owner-private",
        "human owner must download",
        "cryptographically enforced owner-only access",
        "If you cannot create the two separate downloadable files",
        "NOT_YET_ADJUDICATED",
    ):
        assert required in text
    assert "owner-only permissions are guaranteed" not in text
    assert "Do not" in text


def test_real_v02_bytes_and_rebuild_fail_closed() -> None:
    receipt = v2.build(ROOT, verify_only=True)
    assert receipt["archive_bytes"] == 3818
    assert receipt["archive_sha256"] == (
        "f0685d22172faedd79d4becce56d36b3f6d38e4d7e320cb439918fa75a1a1880"
    )
    assert sha256(V2_PATH.read_bytes()).hexdigest() == receipt["archive_sha256"]
    assert receipt["owner_only_file_access"] == "NOT_CLAIMED"
    assert receipt["task_proposals"] == 0
    assert receipt["source_admissions"] == 0


def test_guard_rejects_answer_and_git_link_in_v02_text() -> None:
    with ZipFile(V2_PATH) as z:
        texts = {name: z.read(name) for name in z.namelist()}
    for injected in (b"\nResearch 217 had old answer labels\n",
                     b"\ndocs/research/513_expected_gold.md\n",
                     b"\nB2 is the best arm\n"):
        broken = dict(texts)
        broken["NEUTRAL_CONTEXT.md"] += injected
        with pytest.raises(ValueError, match="Recognized"):
            v1.check_author_texts(broken)
