"""Exact pinned Git-source regression for native Specification 025/028 extraction.

The V03 source-owned declarations are parseable claims, not independently
adjudicated governance or R0-P03 gold. Historical 65-source membership is
an explicitly exposed reference audit frame, not a fresh benchmark.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import source_at_revision
from experiments.r0_p03_navigation_probe.exploratory_governed_reference_audit_v03 import (
    PIN, RESULT, V01, V01_SHA, V02, V02_SHA, SOURCE_SHA256,
    numbered_index, resolve_token, header_witness, structured_witness, run,
)
from scripts.repository_integrity import read_header_fields, parse_declared_reference_field
from tools.project_knowledge.declaration import BEGIN, END, parse_markdown

EXACT_LENGTH = 138104
EXACT_SHA = "f6037c05a6d88e27dc22bb838db24d9e066619f19314dddc2a68ff766f4866cb"


def test_full_real_original_gov_parsers_reexecute_byte_for_byte() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == EXACT_LENGTH
    assert sha256(raw).hexdigest() == EXACT_SHA
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    report = json.loads(raw)
    assert run() == report
    assert report["formal_r0_p03_scored"] is False
    assert report["source_fingerprint_sha256"] == SOURCE_SHA256
    assert sha256(V01.read_bytes()).hexdigest() == V01_SHA
    assert sha256(V02.read_bytes()).hexdigest() == V02_SHA


def test_actual_65_source_slot_and_pair_accounting_is_complete() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    stats = report["summary"]
    assert stats["source_documents"] == 65
    assert stats["header_declaring_documents"] == 7
    assert stats["structured_declaring_documents"] == 9
    assert stats["source_owned_tokens"] == len(report["parsed_source_owned_entries"]) == 113
    assert stats["all_tokens_by_grammar_slot"] == {
        "SPEC025_DECLARED_REFERENCES": 59,
        "SPEC028_PROVENANCE": 34,
        "SPEC028_REFERENCES": 20,
    }
    assert stats["in_corpus_tokens_by_grammar_slot"] == {
        "SPEC025_DECLARED_REFERENCES": 21,
        "SPEC028_PROVENANCE": 4,
        "SPEC028_REFERENCES": 6,
    }
    assert stats["in_corpus_distinct_declared_pairs"] == 31
    assert stats["in_corpus_pairs_also_in_old_110_path_graph"] == 19
    assert stats["in_corpus_pairs_missing_from_old_path_graph"] == 12
    assert stats["old_path_graph_directed_pairs"] == 110
    assert stats["out_of_sample_or_unresolved_tokens"] == 81
    assert stats["tokens_with_preserved_fragments"] == 3
    assert stats["old_empty_forward_sources_with_declared_in_corpus_references"] == [
        "docs/research/126_knowledge_identity_and_multi_axis_organization_deep_dive.md"
    ]
    assert len(stats["old_empty_reverse_sources_with_declared_in_corpus_references"]) == 4


def test_reviewers_29_10_count_difference_is_source_identified_not_silent() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    add = d["summary"]["missing_from_old_path_graph"]
    s = {(x["source"], x["target"]) for x in add}
    spec028 = "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"
    assert ("docs/DECISIONS.md", spec028) in s
    assert ("docs/project_knowledge/selected_architecture_workstream.md", spec028) in s
    assert len(s) == 12
    # No new R0-P03 scored result is inferred from a 29 vs 31 difference.
    assert not d["formal_r0_p03_scored"]


def test_source_claim_witnesses_are_exact_pinned_git_original_lines() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    originals = {}
    for x in d["parsed_source_owned_entries"]:
        p = x["source_path"]
        if p not in originals:
            originals[p] = source_at_revision(PIN, p)
        raw = originals[p]
        assert sha256(raw).hexdigest() == x["source_sha256"]
        assert x["authority_qualified"] is False
        assert x["source_witnesses"]
        for w in x["source_witnesses"]:
            line = raw.decode("utf-8").splitlines()[w["line_number"] - 1]
            assert line == w["original_line"]
            assert sha256(line.encode("utf-8")).hexdigest() == w["line_sha256"]
            assert x["raw_typed_token"] in line


def test_fragment_targets_preserve_decision_and_backlog_selectors() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    fragments = {x["target_fragment"] for x in d["parsed_source_owned_entries"] if x["target_fragment"]}
    assert fragments == {"AB-032", "D-035", "13"}
    p = {
        "docs/DECISIONS.md", "docs/OPEN_ARCHITECTURE_BACKLOG.md",
        "docs/source_universe/PERMANENT_VAULT_BOOTSTRAP.md",
    }
    r = resolve_token(
        "path:docs/DECISIONS.md#D-035", "docs/some_other_source.md",
        p, numbered_index(p),
    )
    assert r["target_member_in_sample"] == "docs/DECISIONS.md"
    assert r["target_fragment"] == "D-035"
    assert r["resolution_state"] == "RESOLVED_IN_65"
    assert resolve_token(
        "research:124", "docs/other.md", p, numbered_index(p),
    )["resolution_state"] == "OUTSIDE_SAMPLED_65_OR_UNRESOLVED"


def test_research126_typed_reference_is_not_path_only_structural_absence() -> None:
    d = json.loads(RESULT.read_text(encoding="utf-8"))
    src = "docs/research/126_knowledge_identity_and_multi_axis_organization_deep_dive.md"
    matches = [x for x in d["parsed_source_owned_entries"] if x["source_path"] == src and x["raw_typed_token"] == "research:124"]
    assert len(matches) == 1
    assert matches[0]["target_member_in_sample"].startswith("docs/research/124_")
    assert matches[0]["grammar_slot"] == "SPEC025_DECLARED_REFERENCES"


def test_native_header_parser_ignores_body_fenced_declared_label(tmp_path: Path) -> None:
    p = tmp_path / "test.md"
    p.write_text(
        "# A\n\n**Status:** ACTIVE\n\n## Ordinary body\n\n"
        + 3 * chr(96) + "text\n"
        "**Declared references:** " + chr(96) + "research:124" + chr(96) + "\n"
        + 3 * chr(96) + "\n", encoding="utf-8",
    )
    assert "Declared references" not in read_header_fields(p)
    p.write_text(
        "# A\n\n**Declared references:** " + chr(96) + "research:124" + chr(96)
        + "\n\n## Body\n", encoding="utf-8",
    )
    h = read_header_fields(p)
    parsed, error = parse_declared_reference_field(h["Declared references"])
    assert error is None and parsed == ["research:124"]


def test_native_structured_parser_distinguishes_real_block_from_fenced_example() -> None:
    raw = (
        "# Example\n\n" + 3 * chr(96) + "markdown\n"
        + BEGIN + "\n"
        + '{"schema_version":"1","profile":"semantic_source.v1"}' + "\n"
        + END + "\n" + 3 * chr(96) + "\n"
    ).encode("utf-8")
    assert parse_markdown(raw) is None
    original = source_at_revision(
        PIN, "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"
    )
    d = parse_markdown(original)
    assert d is not None
    assert d.fields["profile"] == "semantic_source.v1"
    assert structured_witness(original.decode("utf-8"), "research:176")


def test_declared_provenance_is_not_refused_or_merged_into_ordinary_references() -> None:
    report = json.loads(RESULT.read_text(encoding="utf-8"))
    rows = report["parsed_source_owned_entries"]
    provenance = [x for x in rows if x["grammar_slot"] == "SPEC028_PROVENANCE"]
    refs = [x for x in rows if x["grammar_slot"] == "SPEC028_REFERENCES"]
    assert len(provenance) == 34 and len(refs) == 20
    assert all(row["authority_qualified"] is False for row in provenance + refs)
    assert len(report["structured_profile_claims"]) == 9
