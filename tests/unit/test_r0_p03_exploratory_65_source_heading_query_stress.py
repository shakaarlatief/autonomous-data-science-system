"""Test actual fresh mechanically generated heading locator comparison.

The query family uses complete first-H1 headings and exact historical
self-document targets rather than B1-authored old nine-scenario relevance
sets. This is still a source-contained document lookup probe, not true
independent user questions or authoritative historical answer scoring.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_65_source_heading_query_stress import (
    IDENTIFIER, RESULT, citation_route, first_h1, infer_subject, run,
    subject_route, target_score,
)

EXPECTED_SHA256 = "497cdfc559f7d2d56c97b12afb33de1210f5f8bf1945ca9978bd7b73b6ad58b4"
EXPECTED_BYTES = 195216
REV = "4b94ffe183ff7af72cef6ee7492b4ba2f30c11ef"


def test_first_heading_is_literal_not_rewritten_or_selected_by_answer() -> None:
    assert first_h1("preamble\n# First Title\n## Second\n# Third") == "First Title"
    try:
        first_h1("## No top level\ntext")
    except ValueError as exc:
        assert "first H1" in str(exc)
    else:
        raise AssertionError("Missing H1 must fail")


def test_subject_inference_is_fixed_from_words_not_gold_or_target() -> None:
    subjects = [
        {
            "id": "one", "assignable": True, "label": "Evidence and Authority",
            "description": "Governance and documentary source provenance",
        },
        {
            "id": "two", "assignable": True, "label": "Navigation and Retrieval",
            "description": "Relevance, search and discovery",
        },
    ]
    assert infer_subject("Authority, evidence and source provenance", subjects) == "one"
    assert infer_subject("Completely different words", subjects) is None
    annotated = {
        "docs/a.md": {"subjects": ["one"], "preferred_subject": "one"},
        "docs/b.md": {"subjects": ["two"], "preferred_subject": "two"},
    }
    returned, label = subject_route(
        "Authority evidence source provenance", ["docs/b.md", "docs/a.md"],
        annotated, subjects,
    )
    assert label == "one" and returned == ["docs/a.md", "docs/b.md"]


def test_citation_route_behaves_on_short_literal_results() -> None:
    found, added = citation_route(
        ["docs/a.md"],
        {"docs/a.md": {"docs/b.md"}, "docs/b.md": set()},
    )
    assert found == ["docs/a.md", "docs/b.md"]
    assert added == 1
    assert target_score(found, "docs/b.md")["target_rank"] == 2
    assert target_score(found, "docs/z.md")["rr_at_10"] == 0.0


def test_actual_sixty_five_source_queries_reproduce_saved_trace() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXPECTED_BYTES
    assert sha256(raw).hexdigest() == EXPECTED_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    prior = json.loads(raw)
    rerun = run()
    assert rerun == prior
    assert prior["identifier"] == IDENTIFIER
    assert prior["source_revision"] == REV
    assert prior["source_count"] == 65
    assert prior["heading_count"] == 65
    assert prior["unique_heading_count"] == 65
    assert prior["retrieval_limit"] == 10
    assert prior["literal_directed_citation_edges"] == 110
    assert prior["b1_inferred_topic_count"] == 54
    assert prior["b1_fallback_query_count"] == 11
    assert prior["b2_citation_added_after_seeds"] == 306


def test_mechanisms_and_exact_document_gold_measured_without_old_scenario_keys() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    targets = set()
    titles = set()
    for row in report["query_observations"]:
        targets.add(row["target_historical_path"])
        titles.add(row["query_from_h1"])
        for arm in ("b0", "b1", "b2"):
            ranked = row[f"{arm}_ranked_paths"]
            assert len(ranked) <= 10
            assert len(ranked) == len(set(ranked))
            assert row[arm] == target_score(ranked, row["target_historical_path"])
    assert len(targets) == len(titles) == 65
    for arm, at1, at10, mrr in (
        ("b0", 45, 64, 0.80359),
        ("b1", 33, 63, 0.65359),
        ("b2", 45, 64, 0.802949),
    ):
        observed = report["aggregate"][arm]
        assert observed["queries"] == 65
        assert observed["hit_at_1"] == at1
        assert observed["hit_at_10"] == at10
        assert observed["mrr_at_10"] == mrr
        assert observed["total_returned_slots"] == 650
    assert "KNOWN" not in report["classification"]
    assert not any("must_retrieve" in row or "must_not_retrieve" in row for row in report["query_observations"])
