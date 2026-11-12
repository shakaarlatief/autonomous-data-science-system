"""Reproduce exact 719-query wording, evidence-scope, and abstention stress.

The new query families are synthetic, authored before execution, and grounded
in the old 65-document source-path mention graph. The scorer and relation
operator share that raw graph, so correct extraction is not independent semantic
or historical authority validation. Tests preserve both successful recognition
and the 130 intentionally uncorrected held-out inbound/outbound failures.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import inspect
import json

from experiments.r0_p03_navigation_probe.exploratory_paraphrase_scope_and_abstention_v01 import (
    FAMILIES, IDENTIFIER, LIMIT, PREVIOUS, PREVIOUS_SHA256,
    RESULT, UNSUPPORTED_FAMILIES, classify_intent, unique_task_population, run,
)

EXACT_BYTES = 1276498
EXACT_SHA = "b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e"


def test_guarded_parser_distinguishes_actual_evidence_scope_from_absence() -> None:
    lookup = {"evidence source": "docs/source.md"}
    examples = (
        ('In "Evidence Source", which other documents are referenced by repository path?',
         "recognized_forward", ("forward", "docs/source.md")),
        ('Find files that mention "Evidence Source" via a docs/ path.',
         "recognized_reverse", ("reverse", "docs/source.md")),
        ('Which file paths are explicitly cited within "Evidence Source"?',
         "recognized_forward", ("forward", "docs/source.md")),
        ('Give outbound docs/ path citations for "Evidence Source".',
         "unparsed_in_scope", None),
        ('Which documents actually depend on "Evidence Source" in practice?',
         "unsupported_scope", None),
        ('Which documents does "Evidence Source" govern authoritatively?',
         "unsupported_scope", None),
        ('Which documents contain working hyperlinks to "Evidence Source"?',
         "unsupported_scope", None),
        ('Which documents reference "Missing Title" by repository path?',
         "unknown_title", None),
        ('Which documents reference "Evidence Source" and "Another" by repository path?',
         "ambiguous_title", None),
        ('Which documents reference Evidence Source by repository path?',
         "malformed_unquoted_title", None),
    )
    for question, state, parsed in examples:
        assert classify_intent(question, lookup) == (state, parsed)


def test_parser_cannot_accept_gold_or_target_neighbors() -> None:
    assert set(inspect.signature(classify_intent).parameters) == {"query", "titles"}
    assert set(inspect.signature(unique_task_population).parameters) == {"titles"}
    assert len(FAMILIES) == 4
    assert len(UNSUPPORTED_FAMILIES) == 3
    assert LIMIT == 10


def test_complete_finite_population_exact_cardinalities_and_unique_queries() -> None:
    titles = {f"docs/{i}.md": f"Source title {i}" for i in range(65)}
    tasks = unique_task_population(titles)
    assert len(tasks) == len({r["query"] for r in tasks}) == 719
    assert sum(r["scope"] == "literal_path_mention" for r in tasks) == 520
    assert sum(r["scope"] == "unqualified_real_world_claim" for r in tasks) == 195
    assert sum(r["scope"] in ("unresolved_identity", "ambiguous_identity") for r in tasks) == 4
    for family in FAMILIES:
        assert sum(r["family"] == family for r in tasks) == 130


def test_real_719_source_based_query_run_reproduces_exact_saved_bytes() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXACT_BYTES
    assert sha256(raw).hexdigest() == EXACT_SHA
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    d = json.loads(raw)
    assert run() == d
    assert d["identifier"] == IDENTIFIER
    assert d["new_queries"] == 719
    assert d["source_documents"] == 65
    assert d["directed_literal_reference_edges"] == 110
    assert d["top10_limit"] == 10
    assert not d["formal_r0_p03_scored"]
    assert sha256(PREVIOUS.read_bytes()).hexdigest() == PREVIOUS_SHA256


def test_success_and_heldout_failure_are_not_averaged_into_misleading_scores() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    stats = d["families"]
    for family in ("S1", "S2", "H1"):
        v = stats[family]
        assert v["questions"] == 130
        assert v["required_reference_instances"] == 220
        assert v["top10_ceiling"] == 208
        assert v["found_reference_instances"] == 208
        assert v["direction_recognized"] == 130
        assert v["positive_questions"] == 70
        assert v["structurally_empty_questions"] == 60
        assert v["correct_no_edge_states"] == 60
        assert v["exact_structural_sets"] == 128
        assert v["old_exact_parser_recognized"] == 0
    heldout = stats["H2"]
    assert heldout["questions"] == 130
    assert heldout["required_reference_instances"] == 220
    assert heldout["found_reference_instances"] == 0
    assert heldout["direction_recognized"] == 0
    assert heldout["unparsed_in_scope"] == 130
    assert heldout["correct_no_edge_states"] == 0
    # Sixty empty-target exact-set matches are vacuous parser rejections,
    # not correct structural no-reference determinations.
    assert heldout["exact_structural_sets"] == 60


def test_unsupported_real_world_claims_and_bad_identities_are_separately_abstained() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    for family in UNSUPPORTED_FAMILIES:
        stats = d["families"][family]
        assert stats["safe_abstentions"] == 65
        assert stats["unsupported_relational_assertions"] == 0
        assert stats["lexical_candidate_slots"] == 650
    for family in ("X_unknown_forward", "X_unknown_reverse",
                   "X_ambiguous_forward", "X_ambiguous_reverse"):
        stats = d["families"][family]
        assert stats["safe_abstentions"] == 1
        assert stats["unsupported_relational_assertions"] == 0


def test_all_719_queries_accounted_for_without_label_leak_or_false_abstention() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = d["observations"]
    assert len(rows) == 719
    by_family = Counter(r["family"] for r in rows)
    assert all(by_family[key] == 130 for key in FAMILIES)
    assert all(by_family[key] == 65 for key in UNSUPPORTED_FAMILIES)
    assert sum(len(r["lexical_candidate_paths"]) for r in rows) == 7190
    for row in rows:
        asserted = row["asserted_literal_relation_paths"]
        assert len(asserted) <= 10 and len(asserted) == len(set(asserted))
        if row["scope"] != "literal_path_mention":
            assert asserted == []
            assert row["reference_targets_for_structural_audit"] is None
        elif row["family"] == "H2":
            assert asserted == []
            assert row["guarded_state"] == "unparsed_in_scope"
            assert not row["evaluation"]["direction_recognized"]
        else:
            expected = set(row["reference_targets_for_structural_audit"])
            assert row["evaluation"]["found"] == len(expected & set(asserted))
            assert row["evaluation"]["irrelevant_relation_assertions"] == len(set(asserted) - expected)
    assert sum(d["families"][k]["required_reference_instances"] for k in FAMILIES) == 880
    assert sum(d["families"][k]["top10_ceiling"] for k in FAMILIES) == 832
