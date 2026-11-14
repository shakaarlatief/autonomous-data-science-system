"""Synthetic and pinned-need contract tests for unscored four-need retrieval.

No source-answer gold, private report, case-to-source map, or expected
source-ranking labels are accessed. Tests establish protocol and deterministic
mechanical properties rather than a navigation method's scientific validity.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
import sqlite3

from experiments.r0_p03_navigation_probe import four_need_gold_free_original_source_navigation_v01 as nav


def test_original_needs_and_predeclared_contract_identity() -> None:
    assert sha256(nav.NEEDS.read_bytes()).hexdigest() == nav.NEEDS_SHA256
    assert sha256(nav.CONTRACT.read_bytes()).hexdigest() == nav.CONTRACT_SHA256
    assert nav.SOURCE_PIN == "47ed6344a9153dcf366769e95722840fbf1a8f8b"
    questions = nav.questions_from_original()
    assert len(questions) == 4
    assert [r["question_id"] for r in questions] == [
        "R0P03-PILOT-N01", "R0P03-PILOT-N02",
        "R0P03-PILOT-N03", "R0P03-PILOT-N04",
    ]
    assert tuple(r["category"] for r in questions) == nav.CATEGORIES
    assert all(len(q["question"]) > 150 for q in questions)
    assert all("47ed6344a9153dcf366769e95722840fbf1a8f8b" in q["question"] for q in questions)


def test_path_only_source_admission_no_reference_closure() -> None:
    assert nav.source_kind("docs/CURRENT_STATE.md") == "ORIENTATION"
    assert nav.source_kind("docs/DECISIONS.md") == "ORIENTATION"
    assert nav.source_kind("docs/foundations/historical/021_source.md") == "FOUNDATION"
    assert nav.source_kind("docs/research/640_source.md") == "RESEARCH"
    assert nav.source_kind("docs/local_execution/validation/320.md") == "VALIDATION"
    assert nav.source_kind("tests/unit/test_something.py") == "TEST_PY"
    assert nav.source_kind("tools/project_knowledge/identity.py") == "TOOL_PY"
    assert nav.source_kind("scripts/checks.py") == "SCRIPT_PY"
    assert nav.source_kind("docs/other_file.md") is None
    assert nav.source_kind("secrets/file.txt") is None
    assert nav.source_kind("docs/research/scores.json") is None


def test_query_removes_shared_git_pin_without_rewriting_full_need() -> None:
    question = "Which document explains X at " + nav.SOURCE_PIN + "?"
    assert nav.SOURCE_PIN not in nav.retrieval_query(question)
    assert "document" in nav.retrieval_query(question)


def test_heading_fts_and_fusion_are_distinct_source_derived_diagnostics() -> None:
    synthetic = {
        "docs/a.md": {"text": "# Persistence specification\nA stores durable state.", "was_truncated": False, "blob_oid": "a" * 40},
        "docs/b.md": {"text": "# Source evidence\nA historical source.", "was_truncated": False, "blob_oid": "b" * 40},
        "docs/c.md": {"text": "# Orientation and history\nProject continuation.", "was_truncated": False, "blob_oid": "c" * 40},
    }
    db = nav.build_db(synthetic)
    try:
        heading = nav.rank(db, "heading_fts", "persistence")
        body = nav.rank(db, "body_fts", "persistence")
        assert heading and body
        assert heading[0] == "docs/a.md" and body[0] == "docs/a.md"
    finally:
        db.close()
    assert nav.rrf(["a", "b"], ["c", "a"]) == ["a", "c", "b"]
    assert nav.headings_from_text("# Alpha\nbody line\n## Beta\n### Gamma\n") == "Alpha\nBeta\nGamma"


def test_citation_windows_are_bounded_and_preserve_ordinal_source_lines() -> None:
    text = "\n".join(
        f"line {i}: " + ("persistence durability" if i in (13, 14) else "other content")
        for i in range(1, 50)
    )
    windows = nav.citation_windows(text, "What persistence durability does this establish?")
    assert 1 <= len(windows) <= nav.MAX_WINDOWS
    total_characters = 0
    seen = set()
    for window in windows:
        for line in window["lines"]:
            assert 1 <= line["original_line"] <= 49
            assert line["original_line"] not in seen
            seen.add(line["original_line"])
            assert isinstance(line["line_clipped"], bool)
            total_characters += len(line["text"])
    assert total_characters <= nav.SOURCE_EXCERPT_CHARS


def test_source_only_packet_no_gold_and_equal_fixed_topk() -> None:
    q = [
        {"question_id": f"R0P03-PILOT-N{i:02d}", "question": "What is the orientation?", "category": nav.CATEGORIES[i-1]}
        for i in range(1, 5)
    ]
    p = {
        f"docs/{i}.md": {"text": f"# Source {i}\nOriginal claim {i}", "blob_oid": f"{i}" * 40, "was_truncated": False}
        for i in range(1, 5)
    }
    packet = nav.source_only_packet(q, {item["question_id"]: list(p) for item in q}, p)
    assert packet["case_count"] == len(packet["cases"]) == 4
    assert packet["original_reference_answers_in_packet"] is False
    assert packet["expected_source_gold_in_packet"] is False
    assert packet["treatment_identity_in_packet"] is False
    assert len(packet["cases"][0]["source_excerpts"]) == 4
    assert all("original_git_blob_sha1" in d for d in packet["cases"][0]["source_excerpts"])
    assert "reference_answer_for_evaluation_only" not in json.dumps(packet)
