"""Execute Specification 011's lexical+dense Reciprocal Rank Fusion comparator.

This experiment intentionally combines the production SQLite FTS5 retriever with
the unchanged Specification 010 dense candidate. FastEmbed remains experiment
infrastructure and is not part of the locked production dependency set.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.metadata
import json
import os
import platform
import tempfile
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import Any

import numpy as np
from alembic import command
from alembic.config import Config
from fastembed import TextEmbedding

from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
from ads_system.infrastructure.interchange.knowledge_bundle import (
    load_bundle,
    semantic_digest,
    validate_bundle,
    validate_import_safety,
)
from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.persistence.uow import SqlAlchemyUnitOfWork
from ads_system.infrastructure.retrieval.sqlite_fts import SqliteFtsKnowledgeRetrieval

ROOT = Path(__file__).resolve().parents[2]
KNOWLEDGE_FIXTURE = (
    ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"
)
BENCHMARK_FIXTURE = (
    ROOT / "tests" / "fixtures" / "retrieval" / "methodological_horizon_v1.json"
)

FASTEMBED_VERSION = "0.8.0"
MODEL_NAME = "BAAI/bge-small-en-v1.5"
EXPECTED_DIMENSION = 384
CHANNEL_DEPTH = 3
FINAL_TOP_K = 3
RRF_K = 60


def _upgrade(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


def _candidate_bundle() -> dict[str, Any]:
    bundle = copy.deepcopy(load_bundle(KNOWLEDGE_FIXTURE))
    bundle["bundle_kind"] = "CANDIDATE_SET"
    validate_bundle(bundle)
    validate_import_safety(bundle)
    return bundle


def _canonical_digest(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


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
    """Build the unchanged Specification 010 semantic passage projection."""

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
        raise AssertionError("Hybrid comparator received a zero-length embedding vector")
    return matrix / norms


def _dense_rank(
    *,
    query: str,
    model: TextEmbedding,
    document_matrix: np.ndarray,
    stable_keys: list[str],
    revision_ids: Mapping[str, str],
) -> list[dict[str, object]]:
    query_vector = _normalize(np.asarray(list(model.query_embed(query))))[0]
    scores = document_matrix @ query_vector
    ordered = sorted(
        zip(stable_keys, scores, strict=True),
        key=lambda item: (-float(item[1]), item[0]),
    )[:CHANNEL_DEPTH]
    return [
        {
            "stable_key": stable_key,
            "revision_id": revision_ids[stable_key],
            "rank": rank,
            "score": round(float(score), 8),
        }
        for rank, (stable_key, score) in enumerate(ordered, start=1)
    ]


def _lexical_rank(
    retriever: SqliteFtsKnowledgeRetrieval,
    query: str,
) -> list[dict[str, object]]:
    return [
        {
            "stable_key": hit.stable_key,
            "revision_id": hit.revision_id,
            "rank": rank,
            "score": round(hit.score, 8),
        }
        for rank, hit in enumerate(
            retriever.search(query, limit=CHANNEL_DEPTH), start=1
        )
    ]


def _rrf(
    lexical: list[dict[str, object]],
    dense: list[dict[str, object]],
) -> tuple[list[dict[str, object]], int]:
    scores: dict[str, float] = {}
    revision_ids: dict[str, str] = {}

    for channel in (lexical, dense):
        for item in channel:
            stable_key = str(item["stable_key"])
            rank = int(item["rank"])
            revision_id = str(item["revision_id"])
            if stable_key in revision_ids and revision_ids[stable_key] != revision_id:
                raise AssertionError(
                    f"Channel revision mismatch for {stable_key}: "
                    f"{revision_ids[stable_key]} != {revision_id}"
                )
            revision_ids[stable_key] = revision_id
            scores[stable_key] = scores.get(stable_key, 0.0) + 1.0 / (RRF_K + rank)

    ordered = sorted(scores, key=lambda key: (-scores[key], key))
    fused = [
        {
            "stable_key": stable_key,
            "revision_id": revision_ids[stable_key],
            "rank": rank,
            "rrf_score": round(scores[stable_key], 10),
        }
        for rank, stable_key in enumerate(ordered[:FINAL_TOP_K], start=1)
    ]
    return fused, len(scores)


def _target_source(
    target_keys: list[str],
    lexical: list[dict[str, object]],
    dense: list[dict[str, object]],
) -> str:
    lexical_keys = {str(item["stable_key"]) for item in lexical}
    dense_keys = {str(item["stable_key"]) for item in dense}
    in_lexical = any(key in lexical_keys for key in target_keys)
    in_dense = any(key in dense_keys for key in target_keys)
    if in_lexical and in_dense:
        return "BOTH"
    if in_lexical:
        return "LEXICAL_ONLY"
    if in_dense:
        return "DENSE_ONLY"
    return "ABSENT"


def _evaluate_cases(
    *,
    cases: list[dict[str, Any]],
    target_field: str,
    retriever: SqliteFtsKnowledgeRetrieval,
    model: TextEmbedding,
    document_matrix: np.ndarray,
    stable_keys: list[str],
    revision_ids: Mapping[str, str],
) -> tuple[dict[str, dict[str, object]], float, float]:
    results: dict[str, dict[str, object]] = {}
    reciprocal_ranks: list[float] = []

    for case in cases:
        target_keys = [str(key) for key in case[target_field]]
        lexical = _lexical_rank(retriever, case["query"])
        dense = _dense_rank(
            query=case["query"],
            model=model,
            document_matrix=document_matrix,
            stable_keys=stable_keys,
            revision_ids=revision_ids,
        )
        fused, union_size = _rrf(lexical, dense)
        fused_keys = [str(item["stable_key"]) for item in fused]
        target_ranks = [
            fused_keys.index(target) + 1 for target in target_keys if target in fused_keys
        ]
        reciprocal_ranks.append(1.0 / min(target_ranks) if target_ranks else 0.0)

        results[case["case_id"]] = {
            "query": case["query"],
            "target_keys": target_keys,
            "target_source": _target_source(target_keys, lexical, dense),
            "lexical": lexical,
            "dense": dense,
            "candidate_union_size": union_size,
            "fused": fused,
        }

    recall_at_3 = sum(rank > 0 for rank in reciprocal_ranks) / len(reciprocal_ranks)
    mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
    return results, recall_at_3, mrr


def main() -> None:
    installed_version = importlib.metadata.version("fastembed")
    assert installed_version == FASTEMBED_VERSION, (
        f"Expected fastembed {FASTEMBED_VERSION}, found {installed_version}"
    )

    parsed_knowledge = json.loads(KNOWLEDGE_FIXTURE.read_text(encoding="utf-8"))
    benchmark = json.loads(BENCHMARK_FIXTURE.read_text(encoding="utf-8"))
    knowledge_digest = _canonical_digest(parsed_knowledge)
    benchmark_digest = _canonical_digest(benchmark)

    with tempfile.TemporaryDirectory(prefix="ads-rrf-") as temp_dir:
        database_url = sqlite_database_url(Path(temp_dir) / "fusion.sqlite3")
        _upgrade(database_url)
        engine = create_operational_engine(database_url)
        uow_factory = lambda: SqlAlchemyUnitOfWork(engine)
        retriever = SqliteFtsKnowledgeRetrieval(engine)

        try:
            candidate = _candidate_bundle()
            import_candidate_bundle(candidate, uow_factory=uow_factory)
            assert retriever.rebuild() == 0
            accept_candidate_bundle(candidate, uow_factory=uow_factory)

            snapshot_before = export_current_accepted_snapshot(uow_factory=uow_factory)
            authoritative_digest_before = semantic_digest(snapshot_before)

            indexed_count = retriever.rebuild()
            assert indexed_count == 10
            assert retriever.indexed_document_count() == 10

            accepted_assets = sorted(
                snapshot_before["assets"], key=lambda item: item["stable_key"]
            )
            stable_keys = [str(asset["stable_key"]) for asset in accepted_assets]
            revision_ids = {
                str(asset["stable_key"]): str(asset["revision_id"])
                for asset in accepted_assets
            }
            assert stable_keys == sorted(
                str(asset["stable_key"]) for asset in parsed_knowledge["assets"]
            )

            passages = [_asset_passage(asset) for asset in accepted_assets]
            assert len(passages) == 10
            assert all(passages)

            model = TextEmbedding(
                model_name=MODEL_NAME,
                providers=["CPUExecutionProvider"],
                threads=1,
            )
            document_vectors = np.asarray(list(model.passage_embed(passages)))
            assert document_vectors.shape == (10, EXPECTED_DIMENSION)
            document_matrix = _normalize(document_vectors)

            rh_s_results, rh_s_recall, rh_s_mrr = _evaluate_cases(
                cases=benchmark["semantic_diagnostic_cases"],
                target_field="target_keys",
                retriever=retriever,
                model=model,
                document_matrix=document_matrix,
                stable_keys=stable_keys,
                revision_ids=revision_ids,
            )
            rh_l_results, rh_l_recall, rh_l_mrr = _evaluate_cases(
                cases=benchmark["lexical_cases"],
                target_field="required_keys",
                retriever=retriever,
                model=model,
                document_matrix=document_matrix,
                stable_keys=stable_keys,
                revision_ids=revision_ids,
            )

            snapshot_after = export_current_accepted_snapshot(uow_factory=uow_factory)
            authoritative_digest_after = semantic_digest(snapshot_after)

            result = {
                "specification": "011-v0.1",
                "benchmark_id": benchmark["benchmark_id"],
                "fastembed_version": installed_version,
                "model_name": MODEL_NAME,
                "embedding_dimension": EXPECTED_DIMENSION,
                "python_version": platform.python_version(),
                "platform": platform.platform(),
                "knowledge_fixture_canonical_sha256": knowledge_digest,
                "benchmark_fixture_canonical_sha256": benchmark_digest,
                "indexed_lexical_documents": indexed_count,
                "dense_documents": len(passages),
                "channel_depth": CHANNEL_DEPTH,
                "final_top_k": FINAL_TOP_K,
                "rrf_k": RRF_K,
                "rh_s_recall_at_3": rh_s_recall,
                "rh_s_mrr": round(rh_s_mrr, 8),
                "rh_s_critical_omissions": int(
                    (1.0 - rh_s_recall)
                    * len(benchmark["semantic_diagnostic_cases"])
                ),
                "rh_s_results": rh_s_results,
                "rh_l_recall_at_3": rh_l_recall,
                "rh_l_mrr": round(rh_l_mrr, 8),
                "rh_l_results": rh_l_results,
                "authoritative_knowledge_unchanged": (
                    authoritative_digest_after == authoritative_digest_before
                    and snapshot_after == snapshot_before
                ),
            }

            # Emit complete evidence before the frozen assertions so a failure
            # remains diagnostically useful and cannot be hidden by assertion order.
            print("V1_RRF_RETRIEVAL_JSON=" + json.dumps(result, sort_keys=True))

            # Specification 011 primary semantic gate.
            assert rh_s_recall == 1.0, rh_s_results
            assert rh_s_mrr > 0.75, rh_s_results
            assert result["rh_s_critical_omissions"] == 0

            s01 = {
                str(item["stable_key"])
                for item in rh_s_results["RH-S01"]["fused"]
            }
            s04 = {
                str(item["stable_key"])
                for item in rh_s_results["RH-S04"]["fused"]
            }
            assert "class-imbalance" in s01, rh_s_results["RH-S01"]
            assert "ecdf" in s04, rh_s_results["RH-S04"]

            # Specification 011 lexical no-regression gate.
            assert rh_l_recall == 1.0, rh_l_results
            assert rh_l_mrr == 1.0, rh_l_results

            for case in benchmark["lexical_cases"]:
                fused_keys = [
                    str(item["stable_key"])
                    for item in rh_l_results[case["case_id"]]["fused"]
                ]
                for required_key in case["required_keys"]:
                    assert fused_keys.index(required_key) == 0, (
                        case["case_id"],
                        required_key,
                        fused_keys,
                    )

            # Bounded output and authority invariants.
            assert all(
                len(case_result["fused"]) <= FINAL_TOP_K
                for case_result in [*rh_s_results.values(), *rh_l_results.values()]
            )
            assert result["authoritative_knowledge_unchanged"] is True
        finally:
            engine.dispose()


if __name__ == "__main__":
    main()
