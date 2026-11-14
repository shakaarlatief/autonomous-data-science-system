"""Reconcile the published masked source-support review without private gold.

Inputs are the ORIGINAL Git-committed source-free Claude reviewer report and
the previous exact-byte public boundary audit. All treatment mapping is
derived from the prospectively fixed, content-independent mask assignment
algorithm. No historical source files, source-only answer bodies, reviewer
private reasoning, hidden source associations, or per-claim gold are read.

This is a retrospective evidence accounting diagnostic, not a performance
score or an official R0-P03 B0-B4 architecture comparison. Individual claim
units were chosen by an interpretive reviewer; an accurate abstention or a
citation disclaimer can count as 'supported'. Counts cannot be interpreted
as accuracy rates, treatment effect estimates, or PASS thresholds.

The output is source-free. It is exact-byte original publication by
exclusive create; subsequent checks compare a model-free replay of bytes.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "experiments" / "r0_p03_navigation_probe"
REVIEW = ROOT / "docs/model_collaboration/threads/MC-0030/messages/082_claude_r0_p03_masked_four_need_claim_support_review_result.md"
REVIEW_SHA = "2227b5c172291951d5e874bf1d0cdcd4638c8f5b91c5aebdd3f3df47cb1f1fd5"
SOURCE_BOUNDARY = BASE / "four_need_source_only_answer_case_boundary_audit_v01.json"
BOUNDARY_SHA = "975cba9fddbfcf74925fe33853955264ce358ba62467344af0c9e688d00352ad"
REVIEW_FIXTURE = BASE / "four_need_masked_source_excerpt_claim_review_packet_v01.json"
REVIEW_FIXTURE_SHA = "e53544ac31eacaf6fd64e74b67c920d9a2b0ec96bafb1a0951c5fdc43c3453a2"
MANIFEST = BASE / "four_need_masked_source_excerpt_claim_review_manifest_v01.json"
MANIFEST_SHA = "afd02851a2795be8442b1d8e859fbcf7456c3038256ebb67bddd3306f9fbda62"
OUTPUT = BASE / "four_need_public_claim_support_reconciliation_v01.json"
COUNTS = (
    "items", "supported", "partial_or_overbroad", "unsupported_or_out_of_case",
    "contradicted", "insufficient",
)
LINE = re.compile(
    r"^\|\s*(N0[1-4]-[PQ])\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|"
    r"\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|$",
    re.M,
)
LABEL = re.compile(
    r"^\|\s*(N0[1-4])\s*\|\s*"
    r"\x60(P_MORE_SUPPORTED_COVERAGE|Q_MORE_SUPPORTED_COVERAGE|SIMILAR_OR_INCOMPARABLE|UNRESOLVED)\x60\s*\|",
    re.M,
)
# The identical data-independent P/Q masking procedure from the already-
# frozen review-fixture creation contract. Do NOT inspect private sources.
def p_method(question_ids: list[str]) -> dict[str, str]:
    if len(question_ids) != 4 or len(set(question_ids)) != 4:
        raise ValueError("Expected four fixed unique question IDs")
    first_two = {
        q for _, q in sorted(
            (sha256(("R0P03_PAIR_MASK_V01|" + q).encode("ascii")).hexdigest(), q)
            for q in question_ids
        )[:2]
    }
    return {q: ("A" if q in first_two else "B") for q in question_ids}


def exact(path: Path, digest: str) -> bytes:
    data = path.read_bytes()
    if sha256(data).hexdigest() != digest:
        raise ValueError(f"Frozen public input drift: {path.name}")
    return data


def parse_review(text: str) -> tuple[dict[str, dict[str, int]], dict[str, str]]:
    """Consume only the two public Markdown tables, with no answer material."""
    table = {}
    for row in LINE.finditer(text):
        key = row[1]
        if key in table:
            raise ValueError("Duplicate answer review row")
        fields = [int(row[k]) for k in range(2, 8)]
        value = dict(zip(COUNTS, fields))
        if sum(fields[1:]) != value["items"]:
            raise ValueError("Claim categories do not sum to total items")
        table[key] = value
    if set(table) != {f"N{i:02d}-{name}" for i in range(1, 5) for name in ("P", "Q")}:
        raise ValueError("Review must contain exactly eight candidate rows")
    compare = {}
    for match in LABEL.finditer(text):
        if match[1] in compare:
            raise ValueError("Duplicate masked comparison row")
        compare[match[1]] = match[2]
    if set(compare) != {f"N{i:02d}" for i in range(1, 5)}:
        raise ValueError("Exactly four pairwise comparison outcomes required")
    return table, compare


def build() -> dict:
    review = exact(REVIEW, REVIEW_SHA).decode("utf8")
    boundary = json.loads(exact(SOURCE_BOUNDARY, BOUNDARY_SHA))
    manifest = json.loads(exact(MANIFEST, MANIFEST_SHA))
    # Fixture content has original answer and source excerpts. Read its exact
    # digest only, not its bodies or source-specific associations.
    if sha256(REVIEW_FIXTURE.read_bytes()).hexdigest() != REVIEW_FIXTURE_SHA:
        raise ValueError("Masked review input drift")
    if manifest["fixture_sha256"] != REVIEW_FIXTURE_SHA or manifest["masked_candidate_count"] != 8:
        raise ValueError("Original masked reviewer fixture mismatch")
    table, compare = parse_review(review)
    sums = Counter()
    for row in table.values():
        sums.update(row)
    expected = {
        "items": 192,
        "supported": 170,
        "partial_or_overbroad": 11,
        "unsupported_or_out_of_case": 9,
        "contradicted": 0,
        "insufficient": 2,
    }
    if any(sums[k] != expected[k] for k in COUNTS):
        raise ValueError("Published claim verdict totals differ from source-free receipt")
    if (
        boundary["treatments"]["A"]["aggregate_reference_counts"].get("cross_case_full_source_reference_occurrences", 0) != 0
        or boundary["treatments"]["B"]["aggregate_reference_counts"].get("cross_case_full_source_reference_occurrences", 0) != 1
    ):
        raise ValueError("Original source-only case boundary aggregate changed")
    question_ids = [f"R0P03-PILOT-N{i:02d}" for i in range(1, 5)]
    map_ = p_method(question_ids)
    observations = []
    for i, question_id in enumerate(question_ids, 1):
        need = f"N{i:02d}"
        p, q = table[need + "-P"], table[need + "-Q"]
        method_p = map_[question_id]
        method_q = "B" if method_p == "A" else "A"
        label = compare[need]
        winner = (
            method_p if label == "P_MORE_SUPPORTED_COVERAGE" else
            method_q if label == "Q_MORE_SUPPORTED_COVERAGE" else None
        )
        observations.append({
            "original_need": need,
            "mask_candidate_P_original_method": "BODY_BM25" if method_p == "A" else "BODY_PLUS_HEADING_RRF_DIAGNOSTIC",
            "mask_candidate_Q_original_method": "BODY_BM25" if method_q == "A" else "BODY_PLUS_HEADING_RRF_DIAGNOSTIC",
            "masked_comparison_label": label,
            "source_conditioned_supported_coverage_favored_method": (
                "BODY_BM25" if winner == "A" else
                "BODY_PLUS_HEADING_RRF_DIAGNOSTIC" if winner == "B" else
                "NONE_OR_INCOMPARABLE"
            ),
            "candidate_P_claim_units": p["items"],
            "candidate_Q_claim_units": q["items"],
            "candidate_P_supported_item_units": p["supported"],
            "candidate_Q_supported_item_units": q["supported"],
            "candidate_P_out_of_case_or_unsupported": p["unsupported_or_out_of_case"],
            "candidate_Q_out_of_case_or_unsupported": q["unsupported_or_out_of_case"],
            "fully_covered_question": False,
        })
    return {
        "id": "R0_P03_FOUR_NEED_POST_REVIEW_PUBLIC_RECONCILIATION_V01",
        "source_free_reviewer_report_sha256": REVIEW_SHA,
        "review_packet_sha256": REVIEW_FIXTURE_SHA,
        "original_case_source_audit_sha256": BOUNDARY_SHA,
        "source_free_claim_items_by_reviewer": dict((k,sums[k]) for k in COUNTS),
        "eight_answers_reviewed": True,
        "four_original_questions": True,
        "source_conditioned_observations": observations,
        "reviewer_abstention_quality_appropriate_across_eight_answers": True,
        "original_question_fully_covered_count": 0,
        "source_boundary_issue": "BODY_PLUS_HEADING_RRF_DIAGNOSTIC_N03_ONE_OUT_OF_CASE_SOURCE_NINE_ASSESSED_ITEMS",
        "claim_units_include_correct_abstentions_and_qualifications": True,
        "support_claims_are_interpretive_not_independent_gold": True,
        "source_packet_answer_author_confounding_not_separated": True,
        "candidate_masking_not_os_verified": True,
        "formal_R0_P03_scored": False,
        "physical_architecture_selected": False,
        "next_scientific_focus": (
            "STOP_AD_HOC_FOUR_NEED_RETRIEVAL_LOOP;"
            "QUALIFY_SOURCE_ROLE_AUTHORITY_CLOSURE_AND_COMMON_V03_SUBSTRATE_PARITY;"
            "REASSESS_FORMAL_RESEARCH_513_559_576_ADMISSION"
        ),
        "scientific_limits": [
            "The reviewer saw only selected case-local excerpts; neither full historical source nor private original-reference gold was used.",
            "Claim units include supported source-attribution qualifiers, proper abstentions and other accurate limitations; supported proportion is NOT answer accuracy.",
            "One B N03 answer used a source that belonged only to N04; nine assessed items depended on that out-of-case source.",
            "The same Claude model family authored and interpreted the evidence, across separate sessions but without OS-level separation.",
            "Question coverage, expected-source recall, owner/authority correctness and original context are not exhaustively established.",
            "Body BM25 and body-plus-heading RRF are diagnostics; B is not original Research 513 B1 controlled subject architecture.",
            "No original 12+9 formal tasks, 60/20 role-representative qualified parity cohort, neutral protected gold, real B0-B4 full arms, or scored independent evaluator agreement.",
        ],
    }


def canonical(data: dict) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2, ensure_ascii=True) + "\n").encode("utf8")


def main() -> None:
    if OUTPUT.exists():
        raise FileExistsError("Original source-free reconciliation already exists")
    report = build()
    bytes_ = canonical(report)
    with OUTPUT.open("xb") as f:
        f.write(bytes_)
    print(json.dumps({
        "status": report["id"],
        "public_output_bytes": len(bytes_),
        "public_output_sha256": sha256(bytes_).hexdigest(),
        "claim_counts": report["source_free_claim_items_by_reviewer"],
        "need_coverage_favors": [
            (row["original_need"], row["source_conditioned_supported_coverage_favored_method"])
            for row in report["source_conditioned_observations"]
        ],
        "answer_accuracy_percentage_claimed": False,
        "formal_scoring_claimed": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
