"""Actual original-source packet identity and clipping metadata preservation.

These tests use only the original frozen questions, original Git objects and
gold-free retrieved excerpts. They NEVER read the local-only reference
report, expected evidence mapping, reviewer judgments or formal answer gold.
"""
from __future__ import annotations

from hashlib import sha256
import json
import subprocess
from copy import deepcopy

from experiments.r0_p03_navigation_probe import four_need_gold_free_original_source_navigation_v01 as nav
from experiments.r0_p03_navigation_probe import four_need_gold_free_packet_clipping_correction_v02 as corr


def test_original_v01_source_only_packets_remain_exactly_immutable() -> None:
    assert sha256(nav.PACKET_A.read_bytes()).hexdigest() == corr.V01_SHA["A"]
    assert sha256(nav.PACKET_B.read_bytes()).hexdigest() == corr.V01_SHA["B"]
    assert sha256(nav.AGGREGATE.read_bytes()).hexdigest() == corr.V01_AGG_SHA


def test_v02_packet_metadata_only_correction_and_byte_commitments() -> None:
    statement = json.loads(corr.AGGREGATE.read_bytes())
    original_summary = json.loads(nav.AGGREGATE.read_bytes())
    assert statement["corrected_clipping_flags_A"] == 1
    assert statement["corrected_clipping_flags_B"] == 1
    assert statement["original_source_files_checked"] == 23
    assert original_summary["question_count"] == 4
    assert original_summary["document_count"] == 2258
    assert original_summary["top_four_overlaps_by_fixed_question_order"] == [2, 2, 2, 3]
    for old_path, new_path, key in (
        (nav.PACKET_A, corr.OUTPUT_A, "A"),
        (nav.PACKET_B, corr.OUTPUT_B, "B"),
    ):
        old_raw, new_raw = old_path.read_bytes(), new_path.read_bytes()
        assert sha256(new_raw).hexdigest() == statement[f"v02_packet_{key}_sha256"]
        assert len(new_raw) == statement[f"v02_packet_{key}_bytes"]
        old, new = json.loads(old_raw), json.loads(new_raw)
        old_without_flags, new_without_flags = deepcopy(old), deepcopy(new)
        n = 0
        for original_case, revised_case in zip(old_without_flags["cases"], new_without_flags["cases"]):
            assert original_case["exact_original_question"] == revised_case["exact_original_question"]
            for original_source, revised_source in zip(original_case["source_excerpts"], revised_case["source_excerpts"]):
                assert original_source["original_git_path"] == revised_source["original_git_path"]
                for original_window, revised_window in zip(original_source["excerpts"], revised_source["excerpts"]):
                    for original_line, revised_line in zip(original_window["lines"], revised_window["lines"]):
                        if original_line["line_clipped"] != revised_line["line_clipped"]:
                            n += 1
                        original_line.pop("line_clipped")
                        revised_line.pop("line_clipped")
        assert n == 1
        assert old_without_flags == new_without_flags


def test_all_v02_published_excerpts_match_original_git_lines() -> None:
    source_cache: dict[str, list[str]] = {}
    question_truth = nav.questions_from_original()
    for packet_path in (corr.OUTPUT_A, corr.OUTPUT_B):
        packet = json.loads(packet_path.read_bytes())
        assert packet["original_reference_answers_in_packet"] is False
        assert packet["expected_source_gold_in_packet"] is False
        assert packet["treatment_identity_in_packet"] is False
        assert len(packet["cases"]) == len(question_truth) == 4
        for case, fixed in zip(packet["cases"], question_truth):
            assert case["exact_original_question"] == fixed["question"]
            assert case["question_id"] == fixed["question_id"]
            assert len(case["source_excerpts"]) == nav.TOP_K
            for record in case["source_excerpts"]:
                oid = record["original_git_blob_sha1"]
                path = record["original_git_path"]
                if path not in source_cache:
                    resolved = subprocess.check_output(
                        ["git", "rev-parse", nav.SOURCE_PIN + ":" + path],
                        cwd=nav.ROOT, timeout=12,
                    ).decode("ascii").strip()
                    assert resolved == oid
                    content = subprocess.check_output(
                        ["git", "cat-file", "blob", oid],
                        cwd=nav.ROOT, timeout=12,
                    ).decode("utf8")
                    source_cache[path] = content.splitlines()
                lines = source_cache[path]
                per_source_chars = 0
                line_ordinals: set[int] = set()
                for window in record["excerpts"]:
                    for witness in window["lines"]:
                        index = witness["original_line"] - 1
                        assert index not in line_ordinals
                        line_ordinals.add(index)
                        assert 0 <= index < len(lines)
                        assert lines[index].startswith(witness["text"])
                        assert witness["line_clipped"] == (len(witness["text"]) < len(lines[index]))
                        per_source_chars += len(witness["text"])
                assert per_source_chars <= nav.SOURCE_EXCERPT_CHARS
    assert len(source_cache) == 23
