"""Real original-Git source and experimental-authoring regression for B1/B2/B3.

These source-adjacent labels are exposed coordinator judgments, not historical
source-authority, independent scoring gold or a qualified Research513 result.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
import subprocess
import sys

import pytest

from experiments.r0_p03_navigation_probe.route_b_distinct_b1_b2_b3_navigation_comparison_v01 import (
    ARMS, AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256, B0_BYTES, B0_RESULT, B0_SHA256,
    B2, B2_BYTES, B2_SHA256, CATALOG, CATALOG_SHA256, PIN, RESULT, ROOT,
    cosine_tokens, editorial_link_rank, frozen_json, original_evidence_check,
    ranked_annotation_channel, run, two_channel_rrf, validate_subject_catalog,
)
from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    original_contents,
)
from experiments.r0_p03_navigation_probe.route_b_b2_source_editorial_link_extraction_v01 import original_edges

RESULT_BYTES = 92547
RESULT_SHA256 = "6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2"


def test_original_frozen_B0_and_authoring_bytes_are_exact() -> None:
    docs = [
        (B0_RESULT, B0_BYTES, B0_SHA256),
        (AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256),
        (B2, B2_BYTES, B2_SHA256),
        (RESULT, RESULT_BYTES, RESULT_SHA256),
    ]
    for path, n, digest in docs:
        original = path.read_bytes()
        assert len(original) == n
        assert sha256(original).hexdigest() == digest
        assert original.endswith(b"\n") and b"\r\n" not in original


def test_B1_uses_real_18_subject_hierarchy_and_60_carrier_local_overlays() -> None:
    catalog = json.loads(CATALOG.read_text(encoding="utf8"))
    assert sha256(CATALOG.read_bytes()).hexdigest() == CATALOG_SHA256
    defs = validate_subject_catalog(catalog)
    assert len(defs) == 18
    assert len(catalog["subjects"]) == 24
    annotated = frozen_json(AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256)
    items = annotated["sampled_60_metadata_entries"]
    baseline = frozen_json(B0_RESULT, B0_BYTES, B0_SHA256)
    assert [x["path"] for x in items] == baseline["build_sources"]
    assert len(items) == 60
    assert sum(len(x["subjects"]) for x in items) == 94
    assert all(x["preferred_subject"] in x["subjects"] for x in items)
    assert all(set(x["subjects"]) <= set(defs) for x in items)
    assert not any(x["ownership"] == "SOURCE_AUTHORED" for x in items)
    assert "EXPOSED" in annotated["author_exposure"]
    assert sum(bool(x["historical_w5_same_path_annotation"]) for x in items) == 6
    assert all(not x["historical_w5_same_path_annotation"]
               or x["historical_w5_same_path_annotation"]["not_original_current_revision"]
               for x in items)


def test_B3_five_distinct_concerns_are_not_B1_subject_labels_or_governance() -> None:
    d = frozen_json(AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256)
    concerns = d["concern_vocabulary"]
    assert concerns["status"] == "EXPERIMENTAL_PROPOSED_CROSS_CUTTING_NON_GOVERNING"
    assert len(concerns["definitions"]) == 5
    items = d["sampled_60_metadata_entries"]
    assert sum(len(x["concerns"]) for x in items) == 78
    assert set(concerns["definitions"]) & set(validate_subject_catalog(
        json.loads(CATALOG.read_text(encoding="utf8"))
    )) == set()
    assert all(set(x["concerns"]) <= set(concerns["definitions"]) for x in items)


def test_all_original_carrier_metadata_and_B2_link_witnesses_match_git_bytes() -> None:
    a = frozen_json(AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256)
    b = frozen_json(B2, B2_BYTES, B2_SHA256)
    src = original_contents([x["path"] for x in a["sampled_60_metadata_entries"]])
    original_evidence_check(src, a["sampled_60_metadata_entries"],
                            b["original_source_written_candidate_edges"])
    assert len(src) == 60
    assert all(x["source_git_revision"] == PIN for x in a["sampled_60_metadata_entries"])


def test_B2_is_only_actual_written_nonfenced_edges_not_native_or_outside() -> None:
    d = frozen_json(B2, B2_BYTES, B2_SHA256)
    actual = original_edges()
    assert d == actual
    assert d["observed_editorial_candidate_link_count"] == 3
    assert d["observed_unique_directed_candidate_pairs"] == 3
    assert d["fenced_source_mentions_not_in_B2"] == 585
    assert d["native_header_matches_not_in_B2"] == 16
    assert d["nonbuild_or_self_mentions_not_in_B2"] == 46
    assert not any(x["owner_governing_effect_asserted"] for x in d["original_source_written_candidate_edges"])
    assert d["none_of_these_edges_proves_operative_authority"]
    pairs = {
        (x["source_path"], x["target_path"])
        for x in d["original_source_written_candidate_edges"]
    }
    assert pairs == {
        ("docs/CURRENT_STATE.md", "docs/DECISIONS.md"),
        ("docs/DECISIONS.md", "docs/CURRENT_STATE.md"),
        ("docs/research/156_real_current_state_decomposition_and_source_ownership_audit.md",
         "docs/CURRENT_STATE.md"),
    }


def test_frozen_coordinator_authored_annotation_script_reproduces_original_bytes() -> None:
    # Reconstruct all 60 metadata entries from embedded explicit, author-
    # selected subject/concern labels and original source Git bytes.
    p = subprocess.run(
        [sys.executable, "-B", "-m",
         "experiments.r0_p03_navigation_probe.route_b_source_annotation_preparation_v01"],
        cwd=ROOT, capture_output=True, text=True, check=True, timeout=25,
    )
    assert "FROZEN_B1_B3_METADATA 76595" in p.stdout


def test_B1_similarity_and_B2_graph_have_real_distinct_mechanisms() -> None:
    assert cosine_tokens("source integrity provenance", "source identity and provenance") > 0
    assert cosine_tokens("completely unrelated", "source integrity provenance") == 0
    assert two_channel_rrf(["docs/a.md"], ["docs/b.md"]) == ["docs/a.md", "docs/b.md"]
    assert ranked_annotation_channel(
        "author approval required",
        {"a": {"subjects": ["x"]}, "b": {"subjects": ["y"]}},
        {"x": "reusable knowledge", "y": "approval required"},
        "subjects",
    ) == ["b"]
    fake_edge = {
        "source_path": "source", "target_path": "target", "source_line": 2
    }
    out, traversals = editorial_link_rank(["source", "third"], [fake_edge],
                                           {"source", "target", "third"})
    assert out[0] == "source"
    assert "target" in out
    assert traversals[0]["propagation"] == "OUTGOING"
    assert traversals[0]["source_witness_line"] == 2
    # Zero links and empty topical channels cannot invent an authority.
    assert editorial_link_rank([], [], set()) == ([], [])
    assert two_channel_rrf([], []) == []


def test_full_reexecution_is_exact_and_preserves_all_postlabel_evaluation() -> None:
    original = json.loads(RESULT.read_text(encoding="utf8"))
    assert original == run()
    assert original["original_git_pin"] == PIN
    assert original["same_12_exposed_questions"]
    assert len(original["retrieval_trace"]) == 12
    assert set(original["arms"]) == set(ARMS)
    baseline = frozen_json(B0_RESULT, B0_BYTES, B0_SHA256)
    for before, after in zip(
        baseline["comparative_retrieval_trace"], original["retrieval_trace"]
    ):
        assert before["id"] == after["id"]
        assert before["question"] == after["question"]
        assert before["common_source_candidate_rankings"]["B0_SUBSTRATE_LEXICAL_BASELINE"] == (
            after["arm_rankings_before_expected_source_lookup"]["B0_SOURCE_LEXICAL_UNCHANGED"]
        )
        assert after["source_specific_authority_assertions"] == []
        assert after["source_citations_are_navigation_only"]


def test_negative_and_positive_arm_effects_are_recorded_not_tuned_away() -> None:
    d = frozen_json(RESULT, RESULT_BYTES, RESULT_SHA256)
    m = d["metrics"]
    assert m["B0_SOURCE_LEXICAL_UNCHANGED"]["required_source_at_1"] == 8
    assert m["B0_SOURCE_LEXICAL_UNCHANGED"]["required_source_at_10"] == 11
    assert m["B1_SOURCE_SUBJECT_CHANNEL"]["required_source_at_1"] == 2
    assert m["B1_SOURCE_SUBJECT_CHANNEL"]["required_source_at_10"] == 6
    assert m["B1_SUBJECT_NAVIGATION_EXPOSED"]["required_source_at_1"] == 4
    assert m["B1_SUBJECT_NAVIGATION_EXPOSED"]["required_source_at_10"] == 11
    assert m["B2_EDITORIAL_LINK_NAVIGATION"]["required_source_at_1"] == 8
    assert m["B2_EDITORIAL_LINK_NAVIGATION"]["required_source_at_10"] == 11
    assert m["B3_SELECTIVE_CONCERN_CHANNEL"]["required_source_at_1"] == 0
    assert m["B3_SELECTIVE_CONCERN_CHANNEL"]["required_source_at_10"] == 6
    assert m["B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED"]["required_source_at_1"] == 7
    assert m["B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED"]["required_source_at_10"] == 11
    cases = {x["id"]: x for x in d["retrieval_trace"]}
    assert cases["P01"]["required_source_rank_after_outputs_frozen"]["B0_SOURCE_LEXICAL_UNCHANGED"] is None
    assert cases["P01"]["required_source_rank_after_outputs_frozen"]["B1_SUBJECT_NAVIGATION_EXPOSED"] == 3
    assert cases["P03"]["required_source_rank_after_outputs_frozen"]["B1_SUBJECT_NAVIGATION_EXPOSED"] is None
    assert cases["P03"]["required_source_rank_after_outputs_frozen"]["B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED"] == 1


def test_metadata_burden_and_formal_scientific_stopping_boundaries_are_explicit() -> None:
    d = frozen_json(RESULT, RESULT_BYTES, RESULT_SHA256)
    cost = d["source_metadata_cost"]
    assert cost["B1_source_adjacent_memberships"] == 94
    assert cost["B3_source_adjacent_concern_memberships"] == 78
    assert cost["B2_extra_literal_editorial_path_witnesses"] == 3
    assert cost["combined_additional_metadata_bytes"] == 86791
    assert cost["metadata_is_not_source_authored_or_governing"]
    assert cost["human_authoring_time_not_measured"]
    assert not d["formal_R0_P03_scored"]
    assert not d["owner_selected_physical_architecture"]
    assert any("nine-case" in x for x in d["scientific_limits"])
    assert any("embeddings" in x for x in d["scientific_limits"])
    assert any("source-owner" in x for x in d["scientific_limits"])
