"""Audit raw historical source-path mentions with exact evidence provenance.

This tool intentionally does NOT infer governing authority, true dependencies,
editorial source ownership, working hyperlinks, normative historical status,
or architectural superiority from text formatting. It measures information
lost by materializing all literal references as one unqualified edge type.

Source world: 65 immutable historical Git originals already used in public
exploratory W5/R0-P03 navigation tests. Previous output identities are checked.
Results are exposed source-level diagnostics, not independent reference gold.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha1, sha256
import json
from pathlib import Path
import re
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_legacy_b0_b1_live_comparison import (
    ANNOTATIONS, ROOT, load, source_at_revision,
)
from experiments.r0_p03_navigation_probe.exploratory_legacy_b2_source_link_proxy import references
from experiments.r0_p03_navigation_probe.exploratory_hybrid_fusion_and_routing_v01 import (
    PIN, SOURCE_SHA256,
)
from experiments.r0_p03_navigation_probe.exploratory_paraphrase_scope_and_abstention_v01 import (
    RESULT as PRIOR_RESULT,
)

IDENTIFIER = "R0_P03_EXPLORATORY_EXACT_SOURCE_REFERENCE_PROVENANCE_AUDIT_V01"
RESULT = ROOT / "experiments/r0_p03_navigation_probe/exploratory_reference_provenance_audit_result_v01.json"
CONTRACT = "EXPLORATORY_REFERENCE_PROVENANCE_AUDIT_CONTRACT_V01.md"
PRIOR_RESULT_SHA256 = "b1e4291b673d16e45ac96c6785b92884efc327276a9a898f7d83b6b95138a26e"
PATH_TOKEN = re.compile(
    r"(?<![A-Za-z0-9_])docs/[A-Za-z0-9_./-]+\.(?:md|json)(?![A-Za-z0-9_./-])"
)
MARKDOWN_LINK = re.compile(
    r"(?<!!)\[[^\]\r\n]{1,160}\]\(\s*<?"
    r"(docs/[A-Za-z0-9_./-]+\.(?:md|json))"
    r"(?:#[^)\s>]*)?>?\s*(?:\"[^\"]*\")?\s*\)", re.I
)
FENCE = re.compile(r"^\s*(" + chr(96) + r"{3,}|~{3,})(.*)$")
BACKTICKS = re.compile(chr(96) + r"+")
GOVERNANCE = re.compile(
    r"\b(?:govern(?:ed|ing|ance)?|authoritative|canonical|must|required"
    r"|source\s+of\s+truth|supersed\w*)\b", re.I,
)
NAVIGATION = re.compile(
    r"\b(?:see|read|refer(?:red|ence|ences|encing|s)?|mentioned"
    r"|source|context|cit(?:ation|ations|ed|ing))\b", re.I,
)
CONTEXTS = ("FENCED_CODE", "INLINE_CODE", "OTHER_TEXT")
PROJECTIONS = ("RAW_PATH_MENTIONS", "OUTSIDE_FENCE", "OTHER_TEXT_ONLY", "MARKDOWN_LINKS_ONLY")


def git_blob_sha1(data: bytes) -> str:
    """Compute the canonical Git loose-blob object ID, independent of worktree."""
    return sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def inline_code_spans(line: str) -> list[tuple[int, int]]:
    """Pair equal-width Markdown backtick runs; unmatched runs remain literal.

    This is a deliberately bounded single-line classification rather than a
    full Markdown parser. It records occurrences, not formatting authority.
    """
    runs = list(BACKTICKS.finditer(line))
    spans = []
    i = 0
    while i < len(runs):
        first = runs[i]
        matching = next(
            (j for j in range(i + 1, len(runs))
             if len(runs[j].group()) == len(first.group())),
            None,
        )
        if matching is None:
            i += 1
            continue
        spans.append((first.end(), runs[matching].start()))
        i = matching + 1
    return spans


def extract_occurrences(
    source: str,
    raw: bytes,
    text: str,
    eligible: set[str],
) -> list[dict[str, Any]]:
    """Return every original path occurrence with exact source-line evidence.

    The line-level fence/inline distinction is a context measure only. An
    inline-code path embedded in a normative sentence may still be meaningful.
    A path in a source code block may be a true example or a genuine document
    declaration; none is promoted or suppressed at extraction time.
    """
    path_hash = sha256(raw).hexdigest()
    blob_hash = git_blob_sha1(raw)
    fence: tuple[str, int] | None = None
    result: list[dict[str, Any]] = []
    for line_no, original_line in enumerate(text.splitlines(), start=1):
        line = original_line.rstrip("\r")
        m = FENCE.match(line)
        if m is not None:
            marker, trailing = m.groups()
            if fence is None:
                fence = (marker[0], len(marker))
                continue
            if marker[0] == fence[0] and len(marker) >= fence[1] and not trailing.strip():
                fence = None
                continue
        spans = inline_code_spans(line) if fence is None else []
        explicit_links = set()
        if fence is None:
            for link in MARKDOWN_LINK.finditer(line):
                explicit_links.add((link.start(1), link.end(1)))
        for match in PATH_TOKEN.finditer(line):
            target = match.group()
            if target not in eligible or target == source:
                continue
            inside_inline = any(
                left <= match.start() and match.end() <= right
                for left, right in spans
            ) if fence is None else False
            context = (
                "FENCED_CODE" if fence is not None else
                "INLINE_CODE" if inside_inline else "OTHER_TEXT"
            )
            flags = []
            if "path:docs/" in line[:match.start() + 1].lower():
                flags.append("PATH_SELECTOR")
            if GOVERNANCE.search(line):
                flags.append("GOVERNANCE_WORDING")
            if NAVIGATION.search(line):
                flags.append("NAVIGATION_WORDING")
            if (match.start(), match.end()) in explicit_links and not inside_inline:
                flags.append("MARKDOWN_INLINE_LINK")
            flags.sort()
            result.append({
                "source": source,
                "target": target,
                "line_number": line_no,
                "char_start": match.start(),
                "char_end": match.end(),
                "raw_original_line": line,
                "source_line_sha256": sha256(line.encode("utf-8")).hexdigest(),
                "source_blob_sha1": blob_hash,
                "source_sha256": path_hash,
                "syntax_context": context,
                "indicators": flags,
                "semantic_authority_disposition": "NOT_ADJUDICATED",
            })
    return result


def aggregate(
    occurrences: list[dict[str, Any]],
    eligible: set[str],
    legacy_edges: set[tuple[str, str]],
) -> dict[str, Any]:
    witnesses: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for entry in occurrences:
        witnesses[entry["source"], entry["target"]].append(entry)
    if set(witnesses) != legacy_edges:
        raise ValueError("Audited original occurrence graph differs from frozen 110-edge parser")
    if len(legacy_edges) != 110 or len(eligible) != 65:
        raise ValueError("Original historic source universe drift")

    raw = set(legacy_edges)
    outside_fence = {
        edge for edge, items in witnesses.items()
        if any(i["syntax_context"] != "FENCED_CODE" for i in items)
    }
    other_text = {
        edge for edge, items in witnesses.items()
        if any(i["syntax_context"] == "OTHER_TEXT" for i in items)
    }
    markdown_links = {
        edge for edge, items in witnesses.items()
        if any("MARKDOWN_INLINE_LINK" in i["indicators"] for i in items)
    }
    graphs = {
        "RAW_PATH_MENTIONS": raw,
        "OUTSIDE_FENCE": outside_fence,
        "OTHER_TEXT_ONLY": other_text,
        "MARKDOWN_LINKS_ONLY": markdown_links,
    }
    if tuple(graphs) != PROJECTIONS:
        raise AssertionError("Unexpected graph audit projections")
    if not (markdown_links <= other_text <= outside_fence <= raw):
        raise AssertionError("Syntactic graph projections are not nested")

    projections = {}
    for name, pairs in graphs.items():
        projections[name] = {
            "distinct_directed_edges": len(pairs),
            "distinct_sources_with_outgoing": len({a for a, _ in pairs}),
            "distinct_targets_with_incoming": len({b for _, b in pairs}),
            "dropped_raw_edges": len(raw - pairs),
            "edges": [[a, b] for a, b in sorted(pairs)],
        }
    kinds = Counter(e["syntax_context"] for e in occurrences)
    cues = Counter(f for e in occurrences for f in e["indicators"])
    mixed = sum(
        len({entry["syntax_context"] for entry in items}) > 1
        for items in witnesses.values()
    )
    exclusive = {
        k: sum(
            {entry["syntax_context"] for entry in items} == {k}
            for items in witnesses.values()
        )
        for k in CONTEXTS
    }
    return {
        "occurrences_total": len(occurrences),
        "directed_pairs_total": len(witnesses),
        "occurrences_by_context": {k: kinds[k] for k in CONTEXTS},
        "occurrences_with_indicator": {
            k: cues[k]
            for k in ("PATH_SELECTOR", "GOVERNANCE_WORDING",
                      "NAVIGATION_WORDING", "MARKDOWN_INLINE_LINK")
        },
        "edge_pairs_with_mixed_contexts": mixed,
        "edge_pairs_exclusive_to_context": exclusive,
        "source_coverage_by_projection": projections,
        "nested_differences": {
            "raw_not_outside_fence": len(raw - outside_fence),
            "outside_fence_not_other_text": len(outside_fence - other_text),
            "other_text_not_markdown_link": len(other_text - markdown_links),
        },
        "edge_evidence_inventory": [
            {
                "source": a,
                "target": b,
                "occurrence_indices": [
                    occurrences.index(entry) for entry in items
                ],
                "observed_contexts": sorted({
                    entry["syntax_context"] for entry in items
                }),
                "authority_qualified": False,
            }
            for (a, b), items in sorted(witnesses.items())
        ],
    }


def run() -> dict[str, Any]:
    if sha256(PRIOR_RESULT.read_bytes()).hexdigest() != PRIOR_RESULT_SHA256:
        raise ValueError("Checkpoint 910 immutable source-grounded result hash changed")
    original = load(ANNOTATIONS)
    if original["source_boundary"] != PIN:
        raise ValueError("Pinned source revision changed")
    paths = sorted(x["path"] for x in original["annotations"])
    if len(paths) != 65 or len(set(paths)) != 65:
        raise ValueError("Historical 65 source population changed")
    eligible = set(paths)
    sources = {p: source_at_revision(PIN, p) for p in paths}
    sha = sha256(json.dumps([
        [p, sha256(sources[p]).hexdigest()] for p in paths
    ], separators=(",", ":"), ensure_ascii=True).encode("ascii")).hexdigest()
    if sha != SOURCE_SHA256:
        raise ValueError("Exact original Git source byte fingerprint changed")
    legacy_edges = {
        (p, target)
        for p in paths
        for target in references(sources[p].decode("utf-8"), p, eligible)
    }
    all_occurrences: list[dict[str, Any]] = []
    for p in paths:
        all_occurrences.extend(extract_occurrences(
            p, sources[p], sources[p].decode("utf-8"), eligible
        ))
    metrics = aggregate(all_occurrences, eligible, legacy_edges)
    return {
        "identifier": IDENTIFIER,
        "contract": CONTRACT,
        "classification": "EXPLORATORY_REAL_ORIGINAL_SOURCE_PATH_OCCURRENCE_PROVENANCE_AUDIT",
        "scope": "SYNTAX_AND_SOURCE_EVIDENCE_ONLY",
        "not": [
            "NOT independent gold",
            "NOT source-owned governed or editorial B2 declaration adjudication",
            "NOT actual J2 relation validity, real-world dependency, governance or hyperlink verification",
            "NOT B3 concerns, B4 learned semantic retrieval or original R0-P03 scored experiment",
            "NOT a direction to delete inline-code or fenced-source references from future architecture",
        ],
        "historical_git_pin": PIN,
        "historical_source_fingerprint_sha256": sha,
        "prior_checkpoint_910_result_sha256": PRIOR_RESULT_SHA256,
        "eligible_sources": paths,
        "occurrences": all_occurrences,
        "summary": metrics,
        "formal_r0_p03_scored": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    output = run()
    serialized = json.dumps(output, ensure_ascii=True, sort_keys=True, indent=2) + "\n"
    if args.output:
        with RESULT.open("x", encoding="utf-8", newline="\n") as stream:
            stream.write(serialized)
    summary = output["summary"]
    print(json.dumps({
        "id": output["identifier"],
        "original_sources": len(output["eligible_sources"]),
        "occurrences": summary["occurrences_total"],
        "directed_pairs": summary["directed_pairs_total"],
        "by_context": summary["occurrences_by_context"],
        "by_indicator": summary["occurrences_with_indicator"],
        "exclusive": summary["edge_pairs_exclusive_to_context"],
        "mixed_context_edges": summary["edge_pairs_with_mixed_contexts"],
        "projected_graph_size": {
            k: v["distinct_directed_edges"]
            for k, v in summary["source_coverage_by_projection"].items()
        },
        "written": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
