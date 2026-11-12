"""Exact provenance tests for the source-path occurrence audit.

Source syntax and lexical wording are diagnostics, not source-owned semantic
authority, independent answer gold, or the formal R0-P03 architecture result.
"""
from __future__ import annotations

from hashlib import sha256
import json

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import source_at_revision
from experiments.r0_p03_navigation_probe.exploratory_reference_provenance_audit_v01 import (
    CONTEXTS, IDENTIFIER, PIN, PRIOR_RESULT, PRIOR_RESULT_SHA256,
    PROJECTIONS, RESULT, SOURCE_SHA256, extract_occurrences,
    git_blob_sha1, inline_code_spans, run,
)

RESULT_BYTES = 177638
RESULT_SHA256 = "e935edf01c6298b2c55950236c18eab6a9d4f712cfeca1ce3c7c48f69376d299"


def test_git_blob_sha1_is_canonical() -> None:
    assert git_blob_sha1(b"") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"


def test_inline_code_and_unmatched_delimiters() -> None:
    tick = chr(96)
    text = "a " + tick + "docs/a.md" + tick + " b " + 2*tick + "docs/b.md" + 2*tick
    spans = inline_code_spans(text)
    assert [text[a:b] for a, b in spans] == ["docs/a.md", "docs/b.md"]
    assert inline_code_spans(tick + "docs/a.md with no closer") == []


def test_synthetic_mixed_context_and_distinct_witnesses() -> None:
    tick = chr(96)
    source = "docs/source.md"
    universe = {"docs/source.md", "docs/child.md", "docs/second.md"}
    lines = [
        "# Example",
        "Governed by " + tick + "docs/child.md" + tick + " in this illustrative sentence.",
        "A source [link](docs/child.md) and docs/second.md",
        4 * tick + "text",
        "docs/child.md and docs/second.md",
        3 * tick,
        "docs/child.md",
        4 * tick,
        '"path:docs/second.md#anchor"',
        tick + "unclosed docs/child.md",
        "docs/source.md",
        "docs/not-in-corpus.md",
        "docs/child.md docs/child.md",
    ]
    text = "\n".join(lines) + "\n"
    entries = extract_occurrences(source, text.encode(), text, universe)
    assert len(entries) == 10
    assert [e["syntax_context"] for e in entries] == [
        "INLINE_CODE", "OTHER_TEXT", "OTHER_TEXT",
        "FENCED_CODE", "FENCED_CODE", "FENCED_CODE",
        "OTHER_TEXT", "OTHER_TEXT", "OTHER_TEXT", "OTHER_TEXT",
    ]
    assert entries[5]["line_number"] == 7
    assert "GOVERNANCE_WORDING" in entries[0]["indicators"]
    assert "MARKDOWN_INLINE_LINK" in entries[1]["indicators"]
    assert "MARKDOWN_INLINE_LINK" not in entries[0]["indicators"]
    # V01 is intentionally immutable: its known path-selector flag misses
    # an adjacent token. The corrected field is separately preserved in V02.
    assert "PATH_SELECTOR" not in entries[6]["indicators"]
    assert entries[7]["line_number"] == 10
    assert all(e["semantic_authority_disposition"] == "NOT_ADJUDICATED" for e in entries)
    assert all(e["target"] != source for e in entries)
    assert all(e["target"] in universe for e in entries)
    assert len({(e["source"], e["target"]) for e in entries}) == 2


def test_existing_legacy_path_matcher_has_trailing_period_limitation() -> None:
    # This is an observed limitation, not a retroactive fix to the original
    # parser or the immutable historical 110-edge output. An independent exact
    # corpus-membership scan found no additional pair on the pinned corpus.
    from experiments.r0_p03_navigation_probe.exploratory_reference_provenance_audit_v01 import PATH_TOKEN
    assert [m.group() for m in PATH_TOKEN.finditer("See docs/b.md.")] == []
    assert [m.group() for m in PATH_TOKEN.finditer("See docs/b.md")] == ["docs/b.md"]


def test_markdown_link_in_fence_is_not_rendered() -> None:
    corpus = {"docs/a.md", "docs/b.md"}
    body = "~~~markdown\n[see](docs/b.md)\n~~~\n[see](docs/b.md)\n"
    obs = extract_occurrences("docs/a.md", body.encode(), body, corpus)
    assert len(obs) == 2
    assert obs[0]["syntax_context"] == "FENCED_CODE"
    assert "MARKDOWN_INLINE_LINK" not in obs[0]["indicators"]
    assert obs[1]["syntax_context"] == "OTHER_TEXT"
    assert "MARKDOWN_INLINE_LINK" in obs[1]["indicators"]


def test_actual_result_matches_original_git_sources_bit_for_bit() -> None:
    raw = RESULT.read_bytes()
    assert len(raw) == RESULT_BYTES
    assert sha256(raw).hexdigest() == RESULT_SHA256
    assert raw.endswith(b"\n") and b"\r\n" not in raw
    original = json.loads(raw)
    assert run() == original
    assert original["identifier"] == IDENTIFIER
    assert original["historical_git_pin"] == PIN
    assert original["historical_source_fingerprint_sha256"] == SOURCE_SHA256
    assert len(original["eligible_sources"]) == 65
    assert sha256(PRIOR_RESULT.read_bytes()).hexdigest() == PRIOR_RESULT_SHA256

    git_bytes = {p: source_at_revision(PIN, p) for p in original["eligible_sources"]}
    for row in original["occurrences"]:
        contents = git_bytes[row["source"]]
        line = contents.decode("utf-8").splitlines()[row["line_number"] - 1].rstrip("\r")
        assert line == row["raw_original_line"]
        assert line[row["char_start"]:row["char_end"]] == row["target"]
        assert sha256(line.encode("utf-8")).hexdigest() == row["source_line_sha256"]
        assert sha256(contents).hexdigest() == row["source_sha256"]
        assert git_blob_sha1(contents) == row["source_blob_sha1"]
        assert row["syntax_context"] in CONTEXTS
        assert row["semantic_authority_disposition"] == "NOT_ADJUDICATED"


def test_original_graph_parity_contexts_and_projections() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    result = data["summary"]
    assert result["occurrences_total"] == 146
    assert result["directed_pairs_total"] == 110
    assert result["occurrences_by_context"] == {
        "FENCED_CODE": 93, "INLINE_CODE": 46, "OTHER_TEXT": 7,
    }
    assert result["occurrences_with_indicator"] == {
        "PATH_SELECTOR": 7, "GOVERNANCE_WORDING": 14,
        "NAVIGATION_WORDING": 23, "MARKDOWN_INLINE_LINK": 0,
    }
    assert result["edge_pairs_with_mixed_contexts"] == 11
    assert result["edge_pairs_exclusive_to_context"] == {
        "FENCED_CODE": 70, "INLINE_CODE": 26, "OTHER_TEXT": 3,
    }
    projections = result["source_coverage_by_projection"]
    assert set(projections) == set(PROJECTIONS)
    assert {key: v["distinct_directed_edges"] for key, v in projections.items()} == {
        "RAW_PATH_MENTIONS": 110,
        "OUTSIDE_FENCE": 40,
        "OTHER_TEXT_ONLY": 7,
        "MARKDOWN_LINKS_ONLY": 0,
    }
    assert result["nested_differences"] == {
        "raw_not_outside_fence": 70,
        "outside_fence_not_other_text": 33,
        "other_text_not_markdown_link": 7,
    }
    assert len(projections["RAW_PATH_MENTIONS"]["edges"]) == 110
    assert {tuple(pair) for pair in projections["RAW_PATH_MENTIONS"]["edges"]} == {
        (r["source"], r["target"]) for r in data["occurrences"]
    }
    assert all(v["authority_qualified"] is False for v in result["edge_evidence_inventory"])
    assert any("NOT source-owned" in note for note in data["not"])


def test_lossless_inventory_maps_every_original_occurrence() -> None:
    data = json.loads(RESULT.read_text(encoding="utf-8"))
    seen = []
    for edge in data["summary"]["edge_evidence_inventory"]:
        assert edge["occurrence_indices"]
        for i in edge["occurrence_indices"]:
            seen.append(i)
            item = data["occurrences"][i]
            assert (item["source"], item["target"]) == (edge["source"], edge["target"])
    assert sorted(seen) == list(range(len(data["occurrences"])))
