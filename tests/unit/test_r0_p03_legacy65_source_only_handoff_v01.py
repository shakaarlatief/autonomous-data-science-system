"""Verify the independent, gold-free historical legacy author input.

The tests validate complete original Git source bytes and exact identity,
the complete nine topical slots, the capsule's absence of historical
Research 217 subject assignments and answer lists, and deterministic
serialization. They make no independent legacy reference judgments.
"""
from __future__ import annotations

from hashlib import sha256
from io import BytesIO
import json
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import legacy_65_source_only_handoff_v01 as h


@pytest.fixture(scope="module")
def capsule():
    raw, manifest = h.build_zip()
    return raw, manifest


def test_historical_source_ref_and_exact_size(capsule):
    raw,manifest=capsule
    assert manifest["historical_git_ref"]=="4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"
    assert manifest["source_count"]==65
    assert len(manifest["source_records"])==65
    assert len({r["source_path"] for r in manifest["source_records"]})==65
    assert len({r["original_git_blob_oid"] for r in manifest["source_records"]})>=60
    assert len(raw)==622066
    assert sha256(raw).hexdigest()==(
        "db2eb5fc66105918166db54de225b0625ce6d7faf9cb9270bfd98ba3842ffc7b"
    )


def test_zip_crc_all_members_and_pinned_original_sources(capsule):
    raw,manifest=capsule
    h.verify_archive(raw,manifest)
    historical_tree=h.original_git_tree()
    with ZipFile(BytesIO(raw)) as archive:
        assert len(archive.namelist())==68
        assert archive.testzip() is None
        assert all(name in archive.namelist() for name in (
            "MANIFEST.json","AUTHOR_BRIEF.md","THEMES.md",
        ))
        for item in manifest["source_records"]:
            path=item["source_path"]
            payload=archive.read("SOURCES/"+path)
            assert len(payload)==item["source_bytes"]
            assert sha256(payload).hexdigest()==item["source_sha256"]
            assert historical_tree[path]==item["original_git_blob_oid"]


def test_no_original_subject_catalog_results_or_gold_in_archive(capsule):
    raw,manifest=capsule
    with ZipFile(BytesIO(raw)) as archive:
        filenames=set(archive.namelist())
        for prohibited in (
            "navigation_scenarios_v02.json","corpus_annotations_v02.json",
            "result_v02.json","subject_catalog_candidate_v02.json",
            "w1_c_arm_authored_navigation_metadata.json",
            "EXPOSED_DIAGNOSTIC_QUERIES",
        ):
            assert not any(name.endswith(prohibited) for name in filenames)
        intake=archive.read("THEMES.md").decode("utf8")
        assert "must_retrieve" not in intake
        assert "must_not_retrieve" not in intake
        assert "B1" not in intake
    assert manifest["old_W5_reference_answers_included"] is False
    assert manifest["old_W5_subject_assignments_included"] is False
    assert manifest["no_adjudicated_reference_gold_in_this_archive"] is True


def test_nine_separate_natural_information_domains_not_old_gold(capsule):
    raw,manifest=capsule
    assert len(h.THEMES)==9
    assert [name for name,_ in h.THEMES]==[
        f"legacy-{i:02}" for i in range(1,10)
    ]
    assert len({text for _,text in h.THEMES})==9
    with ZipFile(BytesIO(raw)) as archive:
        themes=archive.read("THEMES.md").decode("utf8")
        for key,description in h.THEMES:
            assert themes.count(key+":")==1
            assert description in themes
        instructions=archive.read("AUTHOR_BRIEF.md").decode("utf8")
        assert "MATERIAL_HOLD" in instructions
        assert "source relative" in instructions.lower() or "source-relative" in instructions
        assert "No private backup folder" in instructions
        assert "owner-held" in instructions


def test_deterministic_rebuild_and_existing_local_receipt(capsule):
    raw,manifest=capsule
    again,again_manifest=h.build_zip()
    assert again==raw
    assert again_manifest==manifest
    assert h.OUTPUT.is_file()
    assert h.OUTPUT.read_bytes()==raw


def test_tamper_detection_refuses_revised_source_bytes(capsule):
    raw,manifest=capsule
    broken=bytearray(raw)
    broken[len(broken)//2]^=0x01
    with pytest.raises((ValueError,Exception)):
        h.verify_archive(bytes(broken),manifest)


def test_no_real_answers_and_no_formal_attempt_consumed():
    info=h.create()
    assert info["source_count"]==65
    assert info["themes"]==9
    assert info["legacy_reference_created"] is False
    assert info["includes_old_b1_answers"] is False
    assert info["formal_m6_attempts_consumed"]==0
    assert str(h.OUTPUT).startswith(str(h.REPO/".ads-private"))
