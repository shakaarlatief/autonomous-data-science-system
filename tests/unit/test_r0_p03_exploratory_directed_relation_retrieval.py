"""Reproduce actual historical 130-query directed-reference retrieval results.

These are source-derived structural tests of an explicit path-mention operator,
not independent graded historical claims or authoritative J2/B2 editorial links.
The same raw mention graph constructs both reference sets and relation-index
candidates, which intentionally limits external validity of high scores.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_directed_relation_retrieval_v01 import (
    ADDITIONAL, ARMS, CONTRACT, FORWARD_PREFIX, FORWARD_SUFFIX, IDENTIFIER,
    LIMIT, PRIOR_RESULT, PRIOR_SHA256, RESULT, REVERSE_PREFIX, REVERSE_SUFFIX,
    aggregate, graph_score, parse_relation_question, rank_neighbors,
    relation_question, reverse_edges, run,
)

EXACT_BYTES = 1692786
EXACT_SHA256 = "99206720df7dfa6deb788f4abd8428137a55f5ee68962e83f08da79a7775c399"


def test_forward_reverse_title_resolver_is_exact_and_does_not_use_gold() -> None:
    idx = {"the test source": "docs/subject.md"}
    forward = relation_question("forward", "The Test Source")
    reverse = relation_question("reverse", "The Test Source")
    assert forward == FORWARD_PREFIX + "The Test Source" + FORWARD_SUFFIX
    assert reverse == REVERSE_PREFIX + "The Test Source" + REVERSE_SUFFIX
    assert parse_relation_question(forward, idx) == ("forward", "docs/subject.md")
    assert parse_relation_question(reverse, idx) == ("reverse", "docs/subject.md")
    assert parse_relation_question("List documents about The Test Source", idx) is None
    assert parse_relation_question(relation_question("forward", "Unknown"), idx) is None


def test_directed_inverse_and_deterministic_graph_rank_are_grounded() -> None:
    src = {
        "docs/a.md": {"docs/b.md", "docs/c.md"},
        "docs/b.md": {"docs/c.md"},
        "docs/c.md": set(),
    }
    assert reverse_edges(src) == {
        "docs/a.md": set(),
        "docs/b.md": {"docs/a.md"},
        "docs/c.md": {"docs/a.md", "docs/b.md"},
    }
    assert rank_neighbors({"docs/c.md", "docs/b.md"}, ["docs/a.md", "docs/b.md"]) == [
        "docs/b.md", "docs/c.md",
    ]
    assert rank_neighbors(set(), ["docs/a.md"]) == []


def test_empty_result_is_not_vacuous_perfect_recall() -> None:
    assert graph_score([], set()) == {
        "required_count": 0,
        "retrieved_required_count": 0,
        "irrelevant_to_raw_graph_count": 0,
        "returned_count": 0,
        "positive_recall_at_10": None,
        "exact_set": True,
        "empty_target_correct_abstention": True,
    }
    assert graph_score(["docs/a.md"], set())["exact_set"] is False
    assert graph_score([], {"docs/a.md"})["positive_recall_at_10"] == 0.0
    assert graph_score(["docs/a.md"], {"docs/a.md", "docs/b.md"})["positive_recall_at_10"] == 0.5


def test_exact_saved_real_source_result_reexecutes_identically() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXACT_BYTES
    assert sha256(raw).hexdigest() == EXACT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    stored = json.loads(raw)
    assert run() == stored
    assert stored["identifier"] == IDENTIFIER
    assert stored["experimental_contract"] == CONTRACT
    assert stored["source_documents"] == 65
    assert stored["questions"] == 130
    assert stored["zero_target_questions"] == 60
    assert stored["outbound_reference_edges"] == stored["inbound_reference_edges"] == 110
    assert stored["required_directed_relation_instances"] == 220
    assert stored["maximum_achievable_required_hits_at_k10"] == 208
    assert stored["over_budget_relation_questions"] == 2
    assert stored["return_limit"] == LIMIT
    assert tuple(stored["arm_names"]) == ARMS
    assert sha256(PRIOR_RESULT.read_bytes()).hexdigest() == PRIOR_SHA256


def test_observed_mechanisms_include_unfavorable_fusion_and_empty_controls() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    outcomes = report["aggregate"]["all_130_relation_questions"]
    for arm, hits, empty, exact, empty_slots in (
        ("b0", 110, 0, 0, 600),
        ("b1", 104, 0, 0, 600),
        ("b2", 132, 0, 0, 600),
        ("fusion_all", 126, 0, 0, 600),
        ("relation_b0_naive_rrf", 186, 0, 0, 600),
        ("relation_b0_gated_rrf", 186, 60, 60, 0),
        ("relation_index", 208, 60, 128, 0),
        ("typed_intent_router", 208, 60, 128, 0),
    ):
        score = outcomes[arm]
        assert score["required_link_instances"] == 220
        assert score["positive_questions"] == 70
        assert score["empty_questions"] == 60
        assert score["required_instances_found_at_10"] == hits
        assert score["correct_empty_abstentions"] == empty
        assert score["exact_set_questions"] == exact
        assert score["false_positive_slots_on_empty_questions"] == empty_slots
    assert outcomes["relation_index"]["irrelevant_to_graph_slots_all_questions"] == 0
    assert outcomes["relation_b0_gated_rrf"]["irrelevant_to_graph_slots_all_questions"] == 514
    assert outcomes["relation_b0_naive_rrf"]["irrelevant_to_graph_slots_all_questions"] == 1114
    assert outcomes["relation_index"]["upstream_candidate_union_instances"] == 208
    assert outcomes["relation_b0_gated_rrf"]["upstream_candidate_union_instances"] == 798
    assert set(ADDITIONAL) == {
        "relation_index", "relation_b0_naive_rrf",
        "relation_b0_gated_rrf", "typed_intent_router",
    }


def test_exhaustive_65_per_direction_no_post_result_task_exclusion() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = report["observations"]
    assert len(rows) == 130
    names = {"forward": set(), "reverse": set()}
    for row in rows:
        direction = row["direction"]
        names[direction].add(row["source_historical_path"])
        assert row["query"].startswith(FORWARD_PREFIX if direction == "forward" else REVERSE_PREFIX)
        expected = set(row["expected_literal_relation_targets"])
        assert len(expected) == len(row["expected_literal_relation_targets"])
        assert len(row["ranked"]) == len(ARMS)
        assert tuple(sorted(row["ranked"])) == tuple(sorted(ARMS))
        for arm in ARMS:
            ranked = row["ranked"][arm]
            assert len(ranked) <= 10 and len(ranked) == len(set(ranked))
            assert row["scores"][arm] == graph_score(ranked, expected)
        if not expected:
            assert row["ranked"]["relation_index"] == []
            assert row["ranked"]["relation_b0_gated_rrf"] == []
            assert row["ranked"]["typed_intent_router"] == []
            assert len(row["ranked"]["relation_b0_naive_rrf"]) == 10
    assert len(names["forward"]) == len(names["reverse"]) == 65
    assert names["forward"] == names["reverse"]
    assert report["nonrelation_router_regression"] == {
        "old_nine_subject_queries": 9,
        "all_65_heading_locator_queries": 65,
    }
    assert report["formal_r0_p03_scored"] is False
