"""Retrospective case-local source-use audit for frozen four-need source answers.

A source packet can contain four different question-specific evidence bundles.
Permitted access to a whole packet is NOT permission to use a source assigned
only to another case in an answer. This analyzer counts full historical
source@blob references per fixed case, verifies membership against that case's
published packet, and reports cross-case and extraneous source identities.

The result is structural, post-answer and unscored. A full citation membership
match does not prove an accurate claim, literal line support, complete answer
or valid operative authority. Author shorthand may not be parseable. Neither
private reference answers nor original Git source bodies are used.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments/r0_p03_navigation_probe"
MESSAGES = ROOT / "docs/model_collaboration/threads/MC-0030/messages"
PACKETS = {
    "A": (
        BASE / "four_need_gold_free_source_packet_A_v02.json",
        "3876a30dabc022c67483ea0de5c3ddfcbb75c43ed054f5e4668345df53fe9a37",
    ),
    "B": (
        BASE / "four_need_gold_free_source_packet_B_v02.json",
        "a7ec96918330aa75b2ead92fcf6ad60b4324abc9d5f90ed1f82d1422fc6499d0",
    ),
}
ANSWERS = {
    "A": (
        MESSAGES / "079_claude_r0_p03_fresh_need_packet_a_source_only_answers.md",
        "618767905efe5c3f4ff67088a45b579a41b7b420679e20b7ec5870e6cd501b05",
    ),
    "B": (
        MESSAGES / "080_claude_r0_p03_fresh_need_packet_b_source_only_answers.md",
        "171a000daa1bd569ecac3cc5227c9239d9b513684b5ce35b04edc2db39584905",
    ),
}
OUTPUT = BASE / "four_need_source_only_answer_case_boundary_audit_v01.json"
SOURCE_REF = re.compile(
    r"(?P<path>(?:docs|tools|tests|scripts)/[A-Za-z0-9_./-]+\.(?:md|py))"
    r"@(?P<oid>[0-9a-f]{40})"
)
SECTION_HEADING = re.compile(r"(?m)^## N(?P<n>0[1-4])\s+.*$")
TAIL_HEADING = re.compile(r"(?m)^## (?:[5-9]\.|Outcome summary|Exposure and procedural disclosures)")


def exact_text(path: Path, expected_sha: str) -> str:
    raw = path.read_bytes()
    if sha256(raw).hexdigest() != expected_sha:
        raise ValueError("Previously committed input identity changed")
    return raw.decode("utf-8")


def case_sections(answer: str) -> dict[int, str]:
    headings = list(SECTION_HEADING.finditer(answer))
    if len(headings) != 4 or [int(h["n"]) for h in headings] != [1, 2, 3, 4]:
        raise ValueError("Exactly four ordered original need sections are mandatory")
    tail = TAIL_HEADING.search(answer, headings[-1].end())
    result: dict[int, str] = {}
    for i, header in enumerate(headings):
        end = headings[i + 1].start() if i < 3 else (tail.start() if tail else len(answer))
        result[i + 1] = answer[header.end():end]
    return result


def count_case_references(
    answer_section: str,
    case_index: int,
    permitted_sources: list[set[tuple[str, str]]],
) -> dict[str, int]:
    stats: Counter[str] = Counter()
    for ref in SOURCE_REF.finditer(answer_section):
        stats["explicit_source_reference_occurrences"] += 1
        key = (ref["path"], ref["oid"])
        if key in permitted_sources[case_index - 1]:
            stats["case_local_full_source_reference_occurrences"] += 1
        elif any(key in other for other in permitted_sources):
            stats["cross_case_full_source_reference_occurrences"] += 1
        else:
            stats["outside_packet_full_source_reference_occurrences"] += 1
    # A separate syntactic observation; not a claim-fidelity measurement.
    stats["same_blob_shorthand_mentions"] = len(re.findall(r"same@blob", answer_section))
    return dict(stats)


def build() -> dict:
    records = {}
    for treatment in ("A", "B"):
        packet = json.loads(exact_text(*PACKETS[treatment]))
        answer = exact_text(*ANSWERS[treatment])
        if packet["case_count"] != 4 or len(packet["cases"]) != 4:
            raise ValueError("Frozen packet case structure changed")
        permitted = [
            {(s["original_git_path"], s["original_git_blob_sha1"])
             for s in c["source_excerpts"]}
            for c in packet["cases"]
        ]
        if any(len(s) != 4 for s in permitted):
            raise ValueError("Frozen packet must have four distinct source references per case")
        all_case_sources = set().union(*permitted)
        sections = case_sections(answer)
        stats_by_case = {
            f"N{i:02d}": count_case_references(sections[i], i, permitted)
            for i in range(1, 5)
        }
        # Aggregate each case without losing repeated metric names.
        totals = dict(sum((Counter(row) for row in stats_by_case.values()), Counter()))
        self_labels = {
            f"N{i:02d}": (
                re.findall(
                    r"(ANSWERED_FROM_SUPPLIED_EXCERPTS|PARTIAL_FROM_SUPPLIED_EXCERPTS|ABSTAIN_INSUFFICIENT_EXCERPTS)",
                    sections[i],
                )[:1] or ["LABEL_NOT_FOUND"]
            )[0]
            for i in range(1, 5)
        }
        records[treatment] = {
            "author_answer_sha256": ANSWERS[treatment][1],
            "gold_free_packet_sha256": PACKETS[treatment][1],
            "case_local_reference_counts": stats_by_case,
            "aggregate_reference_counts": totals,
            "self_described_unscored_outcomes": self_labels,
            "unique_source_references_available_across_packet": len(all_case_sources),
            "case_local_evidence_boundary_clean_for_explicit_full_references": (
                totals.get("cross_case_full_source_reference_occurrences", 0) == 0
                and totals.get("outside_packet_full_source_reference_occurrences", 0) == 0
            ),
        }
    return {
        "audit_id": "R0_P03_FOUR_NEED_SOURCE_ONLY_CASE_LOCAL_BOUNDARY_V01",
        "class": "RETROSPECTIVE_EXPLICIT_SOURCE_REFERENCE_BOUNDARY_CHECK_UNSCORED",
        "original_git_pin": "47ed6344a9153dcf366769e95722840fbf1a8f8b",
        "treatments": records,
        "private_original_reference_report_accessed": False,
        "original_git_source_bodies_read": False,
        "full_citation_line_or_semantic_entailment_audited": False,
        "shorthand_references_completely_verified": False,
        "author_answers_modified": False,
        "source_packets_modified": False,
        "formal_r0_p03_score": None,
        "architecture_selection": None,
        "limits": [
            "A cross-case reference means the author used an identity not assigned to the question under the frozen per-case packet rule.",
            "A valid case-local source reference does not independently verify its precise cited lines, claim truth or temporal authority.",
            "Abbreviated shorthand needs a separate contextual review and is not counted as a fully specified source identity.",
            "Self-described ANSWERED/PARTIAL/ABSTAIN labels are author judgments, not blind independent gold or architecture scores.",
        ],
    }


def main() -> None:
    result = build()
    raw = (json.dumps(result, sort_keys=True, indent=2) + "\n").encode("utf8")
    with OUTPUT.open("xb") as fp:
        fp.write(raw)
    print(json.dumps({
        "audit_id": result["audit_id"],
        "treatments": {
            k: {
                "aggregate_reference_counts": val["aggregate_reference_counts"],
                "case_local_evidence_boundary_clean": val["case_local_evidence_boundary_clean_for_explicit_full_references"],
            }
            for k, val in result["treatments"].items()
        },
        "public_output_bytes": len(raw),
        "public_output_sha256": sha256(raw).hexdigest(),
        "private_reference_accessed": False,
        "formal_scored": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
