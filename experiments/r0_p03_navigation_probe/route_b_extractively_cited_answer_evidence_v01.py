"""Fixed, deterministic and source-exact extractive responses for R0-P03.

Gold source labels and expected reference excerpts are evaluator-only.
These are quotation-based evidence drafts, not complete independently
adjudicated natural-language answers or formal R0-P03 task PASS scores.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_t2_no_id_retrieval_and_selective_evidence_v04 import tokens
from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    ROOT, PIN, original_contents,
)

BASE = ROOT / "experiments/r0_p03_navigation_probe"
RESULT = BASE / "route_b_extractively_cited_answer_evidence_result_v01.json"
CONTRACT = "ROUTE_B_PRIMARY_EXTRACTIVE_ANSWER_EVIDENCE_CONTRACT_V01.md"
MANIFEST = "ROUTE_B_PRIMARY_12_SOURCE_ANSWER_MANIFEST_V01.json"
B0 = "route_b_primary_b0_baseline_result_v01.json"
B123 = "route_b_distinct_b1_b2_b3_navigation_comparison_result_v01.json"
B4 = "route_b_b4_local_lsa_embedding_comparison_result_v01.json"
FROZEN = {
    MANIFEST: (9784, "c628555ef02f87499007ead3420a513cf43080262c7288cd347dc2479b4b0330"),
    B0: (122682, "59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab"),
    B123: (92547, "6a2b656432a5b8fbb963b0e8c14220411ed57bbad6127b8a550c05cf93ee0fa2"),
    B4: (154662, "59fd12cc78892bf6f97cde88e44fc692729582560011bf81a55f1fc62af0b00f"),
}
BUDGET = 12000
TOP_SOURCES = 3
SCAN = 35
EXTRA = 4
LINE_CAP = 550
METHODS = (
    "B0_ORIGINAL", "B1_EXPOSED_SUBJECT_B0",
    "B2_SOURCE_WRITTEN_LINK_B0", "B3_EXPOSED_CONCERN_B0",
    "B4_CLASSICAL_LSA_DENSE_ONLY", "B4_CLASSICAL_LSA_B0_FUSION",
    "B4_CLASSICAL_LSA_B2_FUSION",
)


def frozen(name: str) -> dict[str, Any]:
    size, digest = FROZEN[name]
    blob = (BASE / name).read_bytes()
    if len(blob) != size or sha256(blob).hexdigest() != digest:
        raise ValueError("Frozen original fixture changed: " + name)
    return json.loads(blob)


def accessible_lines(text: str, maximum: int = BUDGET) -> list[str]:
    if maximum < 1:
        raise ValueError("Invalid source context budget")
    prefix = text[:maximum]
    if len(text) > maximum and not prefix.endswith(("\r", "\n")):
        if "\n" not in prefix:
            return []
        prefix = prefix[:prefix.rfind("\n") + 1]
    return prefix.splitlines()


def evidence(question: str, text: str) -> list[dict]:
    """Select only original quoted lines from the original context budget."""
    query_terms = set(tokens(question))
    title = None
    possible = []
    seen = 0
    in_fence = False
    for i, line in enumerate(accessible_lines(text), 1):
        trimmed = line.strip()
        if trimmed.startswith((chr(96) * 3, "~~~")):
            in_fence = not in_fence
            continue
        if in_fence or not trimmed or len(line) > LINE_CAP:
            continue
        if title is None and line.startswith("# "):
            title = (i, line)
            continue
        if seen >= SCAN:
            break
        seen += 1
        if trimmed.startswith(("<!--", "{", "}", '"', "## ", "### ")):
            continue
        score = len(query_terms.intersection(tokens(line)))
        if trimmed.startswith("**Status:**"):
            score += 2
        if trimmed.startswith(("**Scope:**", "**Authority:**")):
            score += 1
        if trimmed.startswith(("**Checkpoint:**", "**Active development branch:**")):
            score += 1
        possible.append((score, i, line))
    chosen = sorted(possible, key=lambda v: (-v[0], v[1]))[:EXTRA]
    quote_rows = ([title] if title else []) + [(i, line) for _, i, line in chosen]
    quote_rows.sort(key=lambda v: v[0])
    return [
        {
            "line": i,
            "original_source_line": text_line,
            "sha256_of_original_line": sha256(text_line.encode("utf8")).hexdigest(),
            "is_H1": text_line.startswith("# "),
        }
        for i, text_line in quote_rows
    ]


def draft(citations: list[dict]) -> str:
    """Conservative source-reporting, never silently operative-authoritative."""
    if not citations:
        return "No retrieved source; source evidence is insufficient to answer."
    lines = ["Archived original sources report the following evidence:"]
    for index, source in enumerate(citations, 1):
        lines.append(
            f"Source {index}: {source['path']}@sha256:{source['sha256']}."
        )
        for quote in source["quotes"]:
            lines.append(
                f"  Original line {quote['line']}: "
                + json.dumps(quote["original_source_line"], ensure_ascii=True)
            )
    lines.append(
        "These attributed historical source reports are not an independently adjudicated "
        "complete answer or proof of current operative governing authority."
    )
    return "\n".join(lines)


def ranker_inputs(b0: dict, b123: dict, b4: dict) -> list[dict]:
    """Extract question text and candidate ranks, dropping all gold fields."""
    result = []
    a = b0["comparative_retrieval_trace"]
    b = b123["retrieval_trace"]
    c = b4["cases"]
    if len(a) != len(b) or len(b) != len(c) or len(a) != 12:
        raise ValueError("Frozen original twelve-case comparison count drift")
    for old, struct, semantic in zip(a, b, c):
        if not (
            old["id"] == struct["id"] == semantic["question_id"]
            and old["question"] == struct["question"] == semantic["original_question"]
        ):
            raise ValueError("Frozen source-side question identity drift")
        ordinary = old["common_source_candidate_rankings"]
        organized = struct["arm_rankings_before_expected_source_lookup"]
        dense = semantic["rankings_before_exposed_source_lookup"]
        rankings = {
            "B0_ORIGINAL": ordinary["B0_SUBSTRATE_LEXICAL_BASELINE"],
            "B1_EXPOSED_SUBJECT_B0": organized["B1_SUBJECT_NAVIGATION_EXPOSED"],
            "B2_SOURCE_WRITTEN_LINK_B0": organized["B2_EDITORIAL_LINK_NAVIGATION"],
            "B3_EXPOSED_CONCERN_B0": organized["B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED"],
            "B4_CLASSICAL_LSA_DENSE_ONLY": dense["B4_LSA16_DENSE_ONLY_EXPLORATORY"],
            "B4_CLASSICAL_LSA_B0_FUSION": dense["B4_LSA16_B0_RRF_EXPLORATORY"],
            "B4_CLASSICAL_LSA_B2_FUSION": dense["B4_LSA16_B2_RRF_EXPLORATORY"],
        }
        result.append({
            "id": old["id"], "question": old["question"],
            "ranks": {name: list(rankings[name]) for name in METHODS},
        })
    return result


def generate_all(
    inputs: list[dict], original: dict[str, bytes],
) -> list[dict]:
    """Complete all 84 drafts without reading the answer/reference manifest."""
    digest = {path: sha256(blob).hexdigest() for path, blob in original.items()}
    output = []
    for question in inputs:
        variants = []
        for name in METHODS:
            ranks = question["ranks"][name]
            if len(ranks) > 10 or len(set(ranks)) != len(ranks) or not set(ranks) <= set(original):
                raise ValueError("Retriever left fixed source world or repeated a source")
            citations = []
            for path in ranks[:TOP_SOURCES]:
                selected = evidence(question["question"], original[path].decode("utf8"))
                citations.append({
                    "path": path, "sha256": digest[path], "quotes": selected,
                })
            variants.append({
                "arm": name,
                "top_10_unchanged_source_ranking": ranks,
                "consumed_source_paths": ranks[:TOP_SOURCES],
                "cited_source_records": citations,
                "extractive_answer_draft": draft(citations),
                "gold_source_or_answer_used_in_draft": False,
                "operative_authority_asserted": False,
            })
        output.append({
            "id": question["id"], "question": question["question"],
            "arm_drafts": variants,
        })
    return output


def verify_quoted_lines(outputs: list[dict], original: dict[str, bytes]) -> dict:
    sources = 0
    quotes = 0
    chars = 0
    for row in outputs:
        for variant in row["arm_drafts"]:
            response = variant["extractive_answer_draft"]
            chars += len(response)
            assert not variant["gold_source_or_answer_used_in_draft"]
            assert not variant["operative_authority_asserted"]
            for cited in variant["cited_source_records"]:
                src = original[cited["path"]]
                if cited["sha256"] != sha256(src).hexdigest():
                    raise ValueError("Cited original Git source SHA invalid")
                lines = accessible_lines(src.decode("utf8"))
                sources += 1
                if len(cited["quotes"]) > EXTRA + 1:
                    raise ValueError("Exceeded fixed per-source quote limit")
                for quote in cited["quotes"]:
                    position = quote["line"]
                    if not 1 <= position <= len(lines):
                        raise ValueError("Quoted line beyond source budget")
                    if quote["original_source_line"] != lines[position - 1]:
                        raise ValueError("Cited quote differs from actual original Git line")
                    if sha256(lines[position - 1].encode("utf8")).hexdigest() != quote["sha256_of_original_line"]:
                        raise ValueError("Cited original line SHA invalid")
                    if len(lines[position - 1]) > LINE_CAP:
                        raise ValueError("Overlong cited source line")
                    quotes += 1
    return {
        "drafts": sum(len(x["arm_drafts"]) for x in outputs),
        "source_records_cited": sources,
        "verbatim_original_lines_verified": quotes,
        "draft_characters": chars,
        "all_citations_genuine_original_Git_lines": True,
    }


def evaluate_after_generation(
    outputs: list[dict], manifest: dict, original: dict[str, bytes],
) -> tuple[list[dict], dict]:
    """Reference source identity/excerpts are accessible only to evaluator."""
    tasks = {t["id"]: t for t in manifest["tasks"]}
    if len(tasks) != 12:
        raise ValueError("Original reference case identities incomplete")
    reviewed = []
    for attempt in outputs:
        task = tasks[attempt["id"]]
        if attempt["question"] != task["question"]:
            raise ValueError("Reference task and generated source question drift")
        target = task["required_source_for_evaluation_only"]
        if target not in original:
            raise ValueError("Expected source not in original frozen build")
        refs = task["required_source_witness_lines"]
        original_lines = accessible_lines(original[target].decode("utf8"))
        within = all(
            any(fragment.strip() in line.strip() for line in original_lines)
            for fragment in refs
        )
        per_arm = []
        for candidate in attempt["arm_drafts"]:
            retrieved = target in candidate["consumed_source_paths"]
            source_records = [
                value for value in candidate["cited_source_records"] if value["path"] == target
            ]
            if len(source_records) != int(retrieved):
                raise ValueError("Reference source citation mismatch")
            quoted = [
                quote["original_source_line"] for r in source_records for quote in r["quotes"]
            ]
            visible = within and retrieved
            emitted = visible and all(
                any(fragment.strip() in line.strip() for line in quoted)
                for fragment in refs
            )
            status = (
                "ALL_REFERENCES_QUOTED" if emitted else
                "REFERENCES_ACCESSIBLE_NOT_ALL_QUOTED" if visible else
                "REFERENCE_CONTEXT_NOT_AVAILABLE" if retrieved else
                "REQUIRED_SOURCE_NOT_RETRIEVED"
            )
            per_arm.append({
                "arm": candidate["arm"],
                "required_source_consumed_top_3": retrieved,
                "all_frozen_source_excerpts_available_in_original_12000_chars": visible,
                "all_frozen_source_excerpts_emitted_in_citations": emitted,
                "source_evidence_status": status,
                "full_answer_truth_independently_judged": False,
            })
        reviewed.append({
            "id": attempt["id"],
            "task_category": task["category"],
            "required_source_evaluation_only": target,
            "frozen_reference_draft_evaluation_only": task["reference_answer_for_evaluation_only"],
            "reference_excerpt_count": len(refs),
            "method_evidence": per_arm,
        })
    summary = {}
    for method in METHODS:
        items = [
            next(m for m in question["method_evidence"] if m["arm"] == method)
            for question in reviewed
        ]
        summary[method] = {
            "required_source_in_cited_top3": sum(x["required_source_consumed_top_3"] for x in items),
            "all_required_excerpt_content_available_in_source_context": sum(x["all_frozen_source_excerpts_available_in_original_12000_chars"] for x in items),
            "all_reference_excerpts_actually_cited": sum(x["all_frozen_source_excerpts_emitted_in_citations"] for x in items),
            "counts_by_grade": dict(sorted(Counter(x["source_evidence_status"] for x in items).items())),
            "cases_missing_complete_cited_reference_evidence": [
                question["id"] for question, item in zip(reviewed, items)
                if not item["all_frozen_source_excerpts_emitted_in_citations"]
            ],
            "semantic_answer_correctness_score": None,
            "semantic_answer_correctness_unqualified": True,
        }
    return reviewed, summary


def run() -> dict[str, Any]:
    b0, b123, b4 = frozen(B0), frozen(B123), frozen(B4)
    build = b0["build_sources"]
    if not (
        b0["source_git_pin"] == b123["original_git_pin"] == b4["original_git_pin"] == PIN
        and b123["build_carriers"] == b4["training_source_paths"] == build
        and len(build) == 60 and len(b0["heldout_sources"]) == 20
    ):
        raise ValueError("Original 60/20 source budget or original Git revision changed")
    original = original_contents(build)
    expected_sha = {
        r["path"]: r["original_source_sha256"]
        for r in b0["source_roster"] if r["is_build"]
    }
    if set(expected_sha) != set(original) or any(
        sha256(value).hexdigest() != expected_sha[path] for path, value in original.items()
    ):
        raise ValueError("Original Git content binding mismatch")

    # Source/arm-driven phase: no reference-answer manifest loaded.
    arm_inputs = ranker_inputs(b0, b123, b4)
    outputs = generate_all(arm_inputs, original)
    validation = verify_quoted_lines(outputs, original)
    # Evaluator phase: only now read exposed frozen historical reference draft.
    manifest = frozen(MANIFEST)
    graded, metrics = evaluate_after_generation(outputs, manifest, original)
    return {
        "id": "R0_P03_ROUTE_B_EXTRACTIVE_ANSWER_AND_CITATION_EVIDENCE_V01",
        "contract": CONTRACT,
        "original_source_git_pin": PIN,
        "frozen_input_sha256": {name: value[1] for name, value in FROZEN.items()},
        "build_carriers": build,
        "heldout_carrier_count_excluded": 20,
        "methods": list(METHODS),
        "renderer": {
            "source_char_budget": BUDGET,
            "retrieved_top_source_budget": TOP_SOURCES,
            "maximum_source_nonfenced_nonempty_lines_scanned": SCAN,
            "additional_lines_per_source_max": EXTRA,
            "original_heading_lines_per_source_max": 1,
            "max_characters_per_quote_line": LINE_CAP,
            "source_status_as_current_governing_authority": False,
            "model_free_extract_only": True,
            "gold_in_renderer": False,
        },
        "generated_source_only_answer_drafts": outputs,
        "exact_original_citation_verification": validation,
        "retrospective_reference_evidence_audit": graded,
        "metrics": metrics,
        "limits": [
            "This is an actual extractive source-cited draft reconstruction, not free-form LLM answer semantics or independent answer entailing.",
            "The twelve questions and gold reference drafts were exposed and coordinator-authored. The source-only draft engine does not use gold until evaluation.",
            "All methods reuse frozen original Git source world and ranking paths; one required citation is not exhaustive relevance gold.",
            "Only the top three ranked original sources and original first 12000 source characters are accessible to every arm.",
            "Citation/excerpt coverage is stronger than retrieval@3 but not a complete full-answer PASS or independently established truth.",
            "Original file Status remains an attributed archived source claim, never current owner-authorized operative governance.",
            "Claude Code no-tool reviewer readiness attempt timed out under the 30-second bound; no Claude independent review is claimed.",
            "Private C01/C02 reference and historical nine-case legacy gold remain uninspected and unchanged.",
            "Formal Research513/559/576 R0-P03 independent role controls, 65-source legacy, full native V03 substrate, heldout F1 and currentness authority gates remain unsatisfied.",
            "No formal scientific PASS, physical architecture winner or production migration can be inferred.",
        ],
        "independent_source_answer_gold": False,
        "formal_R0_P03_scored": False,
        "physical_architecture_selected": False,
    }


def main() -> None:
    import argparse
    arg = argparse.ArgumentParser(description=__doc__)
    arg.add_argument("--output", action="store_true")
    args = arg.parse_args()
    value = run()
    b = (json.dumps(value, ensure_ascii=True, sort_keys=True, indent=2) + "\n").encode()
    if args.output:
        with RESULT.open("xb") as result:
            result.write(b)
    print(json.dumps({
        "summary": value["metrics"],
        "citation_evidence": value["exact_original_citation_verification"],
        "result_bytes": len(b),
        "result_sha256": sha256(b).hexdigest(),
        "written": args.output,
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
