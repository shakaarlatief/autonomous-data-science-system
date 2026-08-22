"""Execute Specification 010's exact dense semantic retrieval comparator.

This file is intentionally experiment-local. ``fastembed`` is not a production
ADS dependency unless later evidence earns that promotion.
"""

from __future__ import annotations

import hashlib
import importlib.metadata
import json
import platform
import sys
import time
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import numpy as np
from fastembed import TextEmbedding

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_FIXTURE = (
    ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"
)
BENCHMARK_FIXTURE = (
    ROOT / "tests" / "fixtures" / "retrieval" / "methodological_horizon_v1.json"
)

PACKAGE_VERSION = "0.8.0"
MODEL_NAME = "BAAI/bge-small-en-v1.5"
EXPECTED_DIMENSION = 384
TOP_K = 3


def _strings(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, Mapping):
        result: list[str] = []
        for key in sorted(value):
            result.extend(_strings(value[key]))
        return result
    if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        result = []
        for item in value:
            result.extend(_strings(item))
        return result
    return []


def _asset_passage(asset: Mapping[str, Any]) -> str:
    """Build the frozen Specification 010 semantic passage projection."""

    parts: list[str] = []
    for key in ("stable_key", "title", "purpose", "scope"):
        parts.extend(_strings(asset.get(key)))

    parts.extend(_strings(asset.get("limitations")))

    profile = asset.get("retrieval_profile") or {}
    if isinstance(profile, Mapping):
        for key in ("lexical_terms", "aliases", "semantic_cues"):
            parts.extend(_strings(profile.get(key)))

    parts.extend(_strings(asset.get("reasoning_functions")))

    for requirement in asset.get("context_requirements") or []:
        if isinstance(requirement, Mapping):
            for key in ("key", "description", "required_for"):
                parts.extend(_strings(requirement.get(key)))

    parts.extend(_strings(asset.get("semantic_checks")))

    for facet in asset.get("narrative_facets") or []:
        if isinstance(facet, Mapping):
            for key in ("facet_kind", "body"):
                parts.extend(_strings(facet.get(key)))

    for component in asset.get("components") or []:
        if isinstance(component, Mapping):
            for key in (
                "component_key",
                "component_kind",
                "body",
                "reasoning_functions",
            ):
                parts.extend(_strings(component.get(key)))

    return "\n".join(part for part in parts if part)


def _normalize(matrix: np.ndarray) -> np.ndarray:
    matrix = np.asarray(matrix, dtype=np.float32)
    if matrix.ndim == 1:
        matrix = matrix.reshape(1, -1)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise AssertionError("Semantic comparator received a zero-length embedding vector")
    return matrix / norms


def _rank(
    query_vector: np.ndarray,
    document_matrix: np.ndarray,
    stable_keys: list[str],
) -> list[dict[str, object]]:
    scores = document_matrix @ query_vector
    ordered = sorted(
        zip(stable_keys, scores, strict=True),
        key=lambda item: (-float(item[1]), item[0]),
    )[:TOP_K]
    return [
        {"stable_key": stable_key, "score": round(float(score), 8)}
        for stable_key, score in ordered
    ]


def _evaluate_cases(
    *,
    cases: list[dict[str, Any]],
    target_field: str,
    model: TextEmbedding,
    document_matrix: np.ndarray,
    stable_keys: list[str],
) -> tuple[dict[str, list[dict[str, object]]], float, float, float]:
    results: dict[str, list[dict[str, object]]] = {}
    reciprocal_ranks: list[float] = []

    started = time.perf_counter()
    for case in cases:
        query_vector = _normalize(np.asarray(list(model.query_embed(case["query"]))))[0]
        ranked = _rank(query_vector, document_matrix, stable_keys)
        results[case["case_id"]] = ranked
        keys = [str(item["stable_key"]) for item in ranked]

        target_keys = case[target_field]
        target_ranks = [keys.index(target) + 1 for target in target_keys if target in keys]
        reciprocal_ranks.append(1.0 / min(target_ranks) if target_ranks else 0.0)

    elapsed = time.perf_counter() - started
    recall_at_3 = sum(rank > 0 for rank in reciprocal_ranks) / len(reciprocal_ranks)
    mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
    return results, recall_at_3, mrr, elapsed


def main() -> None:
    installed_version = importlib.metadata.version("fastembed")
    assert installed_version == PACKAGE_VERSION, (
        f"Expected fastembed {PACKAGE_VERSION}, found {installed_version}"
    )

    knowledge_bytes = KNOWLEDGE_FIXTURE.read_bytes()
    benchmark_bytes = BENCHMARK_FIXTURE.read_bytes()
    knowledge = json.loads(knowledge_bytes)
    benchmark = json.loads(benchmark_bytes)

    assets = sorted(knowledge["assets"], key=lambda item: item["stable_key"])
    stable_keys = [asset["stable_key"] for asset in assets]
    passages = [_asset_passage(asset) for asset in assets]
    assert len(stable_keys) == 10
    assert len(set(stable_keys)) == 10
    assert all(passages)

    model_started = time.perf_counter()
    model = TextEmbedding(
        model_name=MODEL_NAME,
        providers=["CPUExecutionProvider"],
        threads=1,
    )
    model_initialization_seconds = time.perf_counter() - model_started

    corpus_started = time.perf_counter()
    document_vectors = np.asarray(list(model.passage_embed(passages)))
    corpus_embedding_seconds = time.perf_counter() - corpus_started
    assert document_vectors.shape == (10, EXPECTED_DIMENSION), document_vectors.shape
    document_matrix = _normalize(document_vectors)

    rh_s_results, rh_s_recall, rh_s_mrr, rh_s_seconds = _evaluate_cases(
        cases=benchmark["semantic_diagnostic_cases"],
        target_field="target_keys",
        model=model,
        document_matrix=document_matrix,
        stable_keys=stable_keys,
    )
    rh_l_results, rh_l_recall, rh_l_mrr, rh_l_seconds = _evaluate_cases(
        cases=benchmark["lexical_cases"],
        target_field="required_keys",
        model=model,
        document_matrix=document_matrix,
        stable_keys=stable_keys,
    )

    # Specification 010 primary semantic gate.
    assert rh_s_recall == 1.0, rh_s_results
    assert rh_s_mrr > 0.75, rh_s_results
    assert "class-imbalance" in {
        item["stable_key"] for item in rh_s_results["RH-S01"]
    }, rh_s_results["RH-S01"]

    # Diagnostic weakness threshold from Specification 010.
    assert rh_l_recall >= 0.80, rh_l_results

    result = {
        "specification": "010-v0.1",
        "benchmark_id": benchmark["benchmark_id"],
        "fastembed_version": installed_version,
        "model_name": MODEL_NAME,
        "embedding_dimension": EXPECTED_DIMENSION,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "knowledge_fixture_sha256": hashlib.sha256(knowledge_bytes).hexdigest(),
        "benchmark_fixture_sha256": hashlib.sha256(benchmark_bytes).hexdigest(),
        "document_count": len(passages),
        "top_k": TOP_K,
        "rh_s_recall_at_3": rh_s_recall,
        "rh_s_mrr": round(rh_s_mrr, 8),
        "rh_s_critical_omissions": int((1.0 - rh_s_recall) * len(benchmark["semantic_diagnostic_cases"])),
        "rh_s_results": rh_s_results,
        "rh_l_semantic_recall_at_3": rh_l_recall,
        "rh_l_semantic_mrr": round(rh_l_mrr, 8),
        "rh_l_results": rh_l_results,
        "model_initialization_seconds": round(model_initialization_seconds, 4),
        "corpus_embedding_seconds": round(corpus_embedding_seconds, 4),
        "rh_s_query_seconds": round(rh_s_seconds, 4),
        "rh_l_query_seconds": round(rh_l_seconds, 4),
    }

    print("V1_SEMANTIC_RETRIEVAL_JSON=" + json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"V1 semantic comparator failed: {exc}", file=sys.stderr)
        raise
