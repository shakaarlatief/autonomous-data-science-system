"""Execute materially distinct B1, B2, and B3 additions on the frozen B0.

This is an exposed, non-formal engineering comparison. B1 and B3 use
per-carrier experimental source-adjacent editorial metadata, NOT source
accepted/governing metadata. B2 uses only three actual source-written
nonfenced candidate references beyond existing native typed headers.
None of these treatments asserts authority or replaces B4 embeddings.
"""
from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
import json
import math
from pathlib import Path
from typing import Any

from experiments.r0_p03_navigation_probe.exploratory_t2_no_id_retrieval_and_selective_evidence_v04 import tokens
from experiments.r0_p03_navigation_probe.route_b_primary_b0_baseline_execution_v01 import (
    ROOT, PIN, original_contents,
)

BASE = ROOT / "experiments/r0_p03_navigation_probe"
B0_RESULT = BASE / "route_b_primary_b0_baseline_result_v01.json"
B0_BYTES = 122682
B0_SHA256 = "59ab36aef96046f71e2ccacbcc2105918ab19ed4bbc1f013e9bb78539a9bd4ab"
AUTHORED = BASE / "route_b_primary_b1_b3_exposed_source_metadata_v01.json"
AUTHORED_BYTES = 76595
AUTHORED_SHA256 = "37d406b0dfce96e12e6ac6b5885445dc1b2e34e25c1f9cee2dccfb9791e5bcb4"
B2 = BASE / "route_b_primary_b2_source_editorial_link_witnesses_v01.json"
B2_BYTES = 10196
B2_SHA256 = "4ee5f25596ac538f7bc4c7fceadebad6bda0ae89ebdb0a6ac6a8dc8121e014b1"
CATALOG = ROOT / "experiments/project_knowledge_subject_navigation_t1_v02/subject_catalog_candidate_v02.json"
CATALOG_SHA256 = "53c5cb65caccd1a9123f5d6da2e5738f618b383339c5bcfcf1d58fb9f5399495"
RESULT = BASE / "route_b_distinct_b1_b2_b3_navigation_comparison_result_v01.json"
CONTRACT = "ROUTE_B_B1_B2_B3_ARM_EXECUTION_CONTRACT_V01.md"
RRF_DAMPING = 60
TOP_K = 10
LINK_OUTGOING = 0.6
LINK_INCOMING = 0.2
ARMS = (
    "B0_SOURCE_LEXICAL_UNCHANGED",
    "B1_SOURCE_SUBJECT_CHANNEL",
    "B1_SUBJECT_NAVIGATION_EXPOSED",
    "B2_EDITORIAL_LINK_NAVIGATION",
    "B3_SELECTIVE_CONCERN_CHANNEL",
    "B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED",
)


def frozen_json(path: Path, size: int, sha: str) -> dict[str, Any]:
    original = path.read_bytes()
    if len(original) != size or sha256(original).hexdigest() != sha:
        raise ValueError(f"Original frozen fixture changed: {path.name}")
    return json.loads(original)


def cosine_tokens(a: str, b: str) -> float:
    """Fixed term-frequency cosine on the pre-existing V04 token vocabulary.

    No corpus fitting, task/source gold, metadata target path or embedding
    affects the similarity calculation. All labels are authored separately.
    """
    x, y = Counter(tokens(a)), Counter(tokens(b))
    if not x or not y:
        return 0.0
    num = sum(n * y.get(k, 0) for k, n in x.items())
    den = math.sqrt(sum(n * n for n in x.values()) * sum(n * n for n in y.values()))
    return num / den if den else 0.0


def ranked_annotation_channel(
    query: str,
    authored: dict[str, dict[str, Any]],
    definition_text: dict[str, str],
    assignment_field: str,
) -> list[str]:
    """Source score is MAX one relevant membership, not sum of all tags."""
    result = []
    for path, carrier in authored.items():
        score = max(
            (cosine_tokens(query, definition_text[tag]) for tag in carrier[assignment_field]),
            default=0.0,
        )
        if score > 0:
            result.append((path, score))
    return [p for p, _ in sorted(result, key=lambda t: (-t[1], t[0]))[:TOP_K]]


def two_channel_rrf(base: list[str], metadata: list[str]) -> list[str]:
    scores = defaultdict(float)
    for ranking in (base, metadata):
        for rank, path in enumerate(ranking[:TOP_K], 1):
            scores[path] += 1.0 / (RRF_DAMPING + rank)
    return [p for p, _ in sorted(scores.items(), key=lambda t: (-t[1], t[0]))[:TOP_K]]


def editorial_link_rank(
    base: list[str],
    edges: list[dict[str, Any]],
    valid_paths: set[str],
) -> tuple[list[str], list[dict[str, Any]]]:
    """One-hop source-written citation navigation; never governing semantics."""
    scores = defaultdict(float)
    for rank, path in enumerate(base[:TOP_K], 1):
        scores[path] += 1.0 / (RRF_DAMPING + rank)
    traversals = []
    for edge in edges:
        s = edge["source_path"]
        t = edge["target_path"]
        if s not in valid_paths or t not in valid_paths:
            raise ValueError("B2 reference would leave frozen original 60-source world")
        if s in base[:TOP_K]:
            weight = LINK_OUTGOING * (1 / (RRF_DAMPING + base.index(s) + 1))
            scores[t] += weight
            traversals.append({
                "edge_source": s, "edge_target": t, "propagation": "OUTGOING",
                "seed_source_rank": base.index(s) + 1, "added_weight": weight,
                "source_witness_line": edge["source_line"],
            })
        if t in base[:TOP_K]:
            weight = LINK_INCOMING * (1 / (RRF_DAMPING + base.index(t) + 1))
            scores[s] += weight
            traversals.append({
                "edge_source": s, "edge_target": t, "propagation": "INCOMING",
                "seed_target_rank": base.index(t) + 1, "added_weight": weight,
                "source_witness_line": edge["source_line"],
            })
    return [
        p for p, _ in sorted(scores.items(), key=lambda x: (-x[1], x[0]))[:TOP_K]
    ], traversals


def validate_subject_catalog(catalog: dict[str, Any]) -> dict[str, str]:
    subjects = catalog["subjects"]
    definitions = {s["id"]: s for s in subjects}
    if len(definitions) != 24 or len(subjects) != 24:
        raise ValueError("Historical Research217 canonical catalog unexpectedly changed")
    assigned = {k for k, v in definitions.items() if v["assignable"]}
    if len(assigned) != 18:
        raise ValueError("Historical Research217 18 assignable subjects changed")
    for name, node in definitions.items():
        for p in node["broader"]:
            if p not in definitions or p == name:
                raise ValueError("Invalid parent in frozen historical subject catalog")
        if node["preferred_parent"] is not None and node["preferred_parent"] not in node["broader"]:
            raise ValueError("Preferred route not one of broader subjects")
    # No cycles are tolerated, including non-assignable parent rollups.
    def visit(node: str, stack: set[str]) -> None:
        if node in stack:
            raise ValueError("Historical navigation subject polyhierarchy cycle")
        for parent in definitions[node]["broader"]:
            visit(parent, stack | {node})
    for subject in definitions:
        visit(subject, set())
    return {
        k: " ".join([v["label"], v["description"], v.get("include_when", "")])
        for k, v in definitions.items() if v["assignable"]
    }


def original_evidence_check(
    source: dict[str, bytes],
    metadata: list[dict[str, Any]],
    edges: list[dict[str, Any]],
) -> None:
    for item in metadata:
        p = item["path"]
        b = source[p]
        if item["source_sha256"] != sha256(b).hexdigest():
            raise ValueError("B1/B3 source-adjacent annotation no longer binds original bytes")
        evidence = item["primary_semantic_evidence"]
        original = b.decode("utf8").splitlines()[evidence["line"] - 1]
        if original != evidence["verbatim_original_line"]:
            raise ValueError("B1/B3 source witness line drift")
        if sha256(original.encode()).hexdigest() != evidence["line_sha256"]:
            raise ValueError("B1/B3 source line hash drift")
    for edge in edges:
        p, t = edge["source_path"], edge["target_path"]
        if edge["source_sha256"] != sha256(source[p]).hexdigest():
            raise ValueError("B2 source SHA drift")
        if edge["target_sha256"] != sha256(source[t]).hexdigest():
            raise ValueError("B2 target SHA drift")
        original = source[p].decode("utf8").splitlines()[edge["source_line"] - 1]
        if original != edge["verbatim_original_source_line"]:
            raise ValueError("B2 exact source-written original witness drift")
        if sha256(original.encode()).hexdigest() != edge["source_line_sha256"]:
            raise ValueError("B2 original line digest drift")
        if t not in original:
            raise ValueError("B2 path identity missing from original source text")


def run() -> dict[str, Any]:
    base = frozen_json(B0_RESULT, B0_BYTES, B0_SHA256)
    authored = frozen_json(AUTHORED, AUTHORED_BYTES, AUTHORED_SHA256)
    links = frozen_json(B2, B2_BYTES, B2_SHA256)
    catalog = frozen_json(CATALOG, CATALOG.stat().st_size, CATALOG_SHA256)
    subjects = validate_subject_catalog(catalog)
    concerns = authored["concern_vocabulary"]["definitions"]
    if len(concerns) != 5:
        raise ValueError("Prospective five-concern source metadata changed")
    build = base["build_sources"]
    if len(build) != 60 or len(base["comparative_retrieval_trace"]) != 12:
        raise ValueError("Prospective source and question boundary drift")
    indexed = {r["path"]: r for r in authored["sampled_60_metadata_entries"]}
    if len(indexed) != 60 or set(indexed) != set(build):
        raise ValueError("B1/B3 authoring metadata missing frozen build carriers")
    edges = links["original_source_written_candidate_edges"]
    if links["build_paths"] != build or len(edges) != 3:
        raise ValueError("B2 pre-score source link freeze mismatch")
    if base["source_git_pin"] != PIN or authored["source_git_pin"] != PIN or links["source_git_pin"] != PIN:
        raise ValueError("Original Git-source revision mismatch")
    for row in indexed.values():
        if not row["subjects"] or row["preferred_subject"] not in row["subjects"]:
            raise ValueError("Invalid author-proposed preferred route")
        if any(x not in subjects for x in row["subjects"]):
            raise ValueError("Unknown B1 assignable subject")
        if any(x not in concerns for x in row["concerns"]):
            raise ValueError("Unknown B3 proposed concern")
    full_original = original_contents(build)
    original_evidence_check(full_original, list(indexed.values()), edges)
    original_sha_by_path = {row["path"]: row["original_source_sha256"] for row in base["source_roster"]}

    observed = []
    for case in base["comparative_retrieval_trace"]:
        question = case["question"]
        b0 = case["common_source_candidate_rankings"]["B0_SUBSTRATE_LEXICAL_BASELINE"]
        b1_topics = ranked_annotation_channel(question, indexed, subjects, "subjects")
        b3_concerns = ranked_annotation_channel(question, indexed, {
            k: k.replace("-", " ") + " " + v for k, v in concerns.items()
        }, "concerns")
        b2_ranked, traversed = editorial_link_rank(b0, edges, set(build))
        ranked = {
            "B0_SOURCE_LEXICAL_UNCHANGED": list(b0),
            "B1_SOURCE_SUBJECT_CHANNEL": b1_topics,
            "B1_SUBJECT_NAVIGATION_EXPOSED": two_channel_rrf(b0, b1_topics),
            "B2_EDITORIAL_LINK_NAVIGATION": b2_ranked,
            "B3_SELECTIVE_CONCERN_CHANNEL": b3_concerns,
            "B3_SELECTIVE_CONCERN_NAVIGATION_EXPOSED": two_channel_rrf(b0, b3_concerns),
        }
        # Evaluator-only source read AFTER all arm rankings have been returned.
        source = case["intended_source_for_evaluation_only"]
        ranks = {
            name: (ids.index(source) + 1 if source in ids else None)
            for name, ids in ranked.items()
        }
        observed.append({
            "id": case["id"],
            "question": question,
            "original_category": case["category"],
            "source_identity_for_exposed_evaluation_only": source,
            "source_original_sha256": original_sha_by_path[source],
            "arm_rankings_before_expected_source_lookup": ranked,
            "required_source_rank_after_outputs_frozen": ranks,
            "B2_actual_source_line_edge_traversals": traversed,
            "source_specific_authority_assertions": [],
            "source_citations_are_navigation_only": True,
        })
    summary = {}
    for name in ARMS:
        ranks = [case["required_source_rank_after_outputs_frozen"][name] for case in observed]
        summary[name] = {
            f"required_source_at_{n}": sum(r is not None and r <= n for r in ranks)
            for n in (1, 3, 5, 10)
        } | {
            "mrr_at_10": sum(1 / rank if rank else 0 for rank in ranks) / 12,
            "missed_required_source_within_top_10": [
                c["id"] for c in observed if c["required_source_rank_after_outputs_frozen"][name] is None
            ],
        }
    return {
        "id": "R0_P03_ROUTE_B_DISTINCT_B1_B2_B3_SOURCE_NAVIGATION_EXPOSURE_TEST_V01",
        "contract": CONTRACT,
        "exact_baseline_output_hash": B0_SHA256,
        "exact_source_adjacent_authoring_hash": AUTHORED_SHA256,
        "exact_original_editorial_link_hash": B2_SHA256,
        "catalog_hash": CATALOG_SHA256,
        "original_git_pin": PIN,
        "build_carriers": build,
        "same_12_exposed_questions": True,
        "arms": list(ARMS),
        "source_metadata_cost": {
            "B1_source_adjacent_memberships": authored["cost"]["new_source_adjoining_subject_memberships"],
            "B1_source_adjoining_carriers": len(indexed),
            "B1_preexisting_history_same_path": authored["cost"]["historically_annotated_carrier_overlap_at_prior_revision"],
            "B3_source_adjacent_concern_memberships": authored["cost"]["new_source_adjoining_concern_memberships"],
            "B3_concerns": len(concerns),
            "B2_extra_literal_editorial_path_witnesses": len(edges),
            "B2_extra_unique_directed_pairs": links["observed_unique_directed_candidate_pairs"],
            "B2_fenced_links_rejected": links["fenced_source_mentions_not_in_B2"],
            "B2_native_header_refs_excluded_as_common": links["native_header_matches_not_in_B2"],
            "B1_B3_metadata_bytes": AUTHORED_BYTES,
            "B2_original_witness_bytes": B2_BYTES,
            "combined_additional_metadata_bytes": AUTHORED_BYTES + B2_BYTES,
            "metadata_is_not_source_authored_or_governing": True,
            "human_authoring_time_not_measured": True,
        },
        "retrieval_trace": observed,
        "metrics": summary,
        "scientific_limits": [
            "Both B1 subject memberships and B3 concern memberships were authored by the exposed coordinator after seeing all twelve questions and the B0 outputs.",
            "B1 includes the authentic eighteen-subject Research217 vocabulary and source-adjacent membership/navigation hierarchy; it does not prove source-owner authorship at this historical Git revision.",
            "B2 uses exactly original source-written nonfenced references, not newly accepted carrier-to-governing editorial relationships; authoring sparsity may prevent any benefit.",
            "B3 concern vocabulary and carrier assignments are proposed experimental navigational obligations, not actually owner-governed.",
            "All derived indexes and editorial annotations are navigation hints and cannot change original Git source authority or current operative effects.",
            "The common substrate remains the Checkpoint918 lexical proxy, not a qualified complete equal V03-native relation/effect/lineage/coverage substrate.",
            "One coordinator-selected required source per question is not independent or exhaustive relevance gold, and hit@k is not a full answer PASS.",
            "No independent role qualification, legacy nine-case neutral reference, held-out maintenance gold, human runtime cost, B4 real semantic embeddings, or formal R0-P03 architecture comparison.",
            "No post-output metadata or query tuning permitted. Negative results count; no owner physical target or source migration selected.",
        ],
        "formal_R0_P03_scored": False,
        "owner_selected_physical_architecture": False,
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", action="store_true")
    args = parser.parse_args()
    d = run()
    raw = (json.dumps(d, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode()
    if args.output:
        with RESULT.open("xb") as f:
            f.write(raw)
    print(json.dumps({
        "metrics": d["metrics"],
        "source_metadata_cost": d["source_metadata_cost"],
        "byte_count": len(raw),
        "sha256": sha256(raw).hexdigest(),
        "output_saved": bool(args.output),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
