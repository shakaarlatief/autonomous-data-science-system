"""Synthetic V02 packet clipping correction and preservation controls.

The test deliberately contains no original historical source text, private
reference answer or expected-source mapping.
"""
from __future__ import annotations
from copy import deepcopy

import pytest
from experiments.r0_p03_navigation_probe import (
    four_need_gold_free_packet_clipping_correction_v02 as correction,
)


def fake_packet() -> dict:
    return {
        "packet_type": "synthetic",
        "original_reference_answers_in_packet": False,
        "cases": [{
            "question_id": "FAKE",
            "exact_original_question": "What is the test?",
            "source_excerpts": [{
                "original_git_path": "docs/synthetic.md",
                "original_git_blob_sha1": "a" * 40,
                "rank": 1,
                "excerpts": [{
                    "lines": [
                        {"original_line": 1, "text": "first", "line_clipped": False},
                        {"original_line": 2, "text": "second", "line_clipped": False},
                    ]
                }],
            }],
        }],
    }


def test_correction_only_flips_clipping_flag(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(correction, "pinned_lines", lambda path, oid, cache: [
        "first line is longer", "second"
    ])
    original = fake_packet()
    copied = deepcopy(original)
    updated, count = correction.corrected_packet(original, {})
    assert count == 1
    assert original == copied
    assert updated["cases"][0]["source_excerpts"][0]["excerpts"][0]["lines"] == [
        {"original_line": 1, "text": "first", "line_clipped": True},
        {"original_line": 2, "text": "second", "line_clipped": False},
    ]
    assert updated["cases"][0]["exact_original_question"] == original["cases"][0]["exact_original_question"]


def test_correction_rejects_excerpt_not_at_original_location(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(correction, "pinned_lines", lambda path, oid, cache: ["different", "second"])
    with pytest.raises(ValueError, match="Source excerpt text"):
        correction.corrected_packet(fake_packet(), {})


def test_no_correction_when_original_line_is_exact(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(correction, "pinned_lines", lambda path, oid, cache: ["first", "second"])
    updated, count = correction.corrected_packet(fake_packet(), {})
    assert count == 0
    assert updated == fake_packet()


def test_original_packet_sha_guards_and_distinct_v02_paths() -> None:
    assert correction.V01_SHA["A"] != correction.V01_SHA["B"]
    assert len(correction.V01_AGG_SHA) == 64
    assert correction.OUTPUT_A != correction.nav.PACKET_A
    assert correction.OUTPUT_B != correction.nav.PACKET_B
    assert correction.AGGREGATE != correction.nav.AGGREGATE
