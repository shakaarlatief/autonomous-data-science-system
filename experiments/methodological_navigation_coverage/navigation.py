"""Deterministic navigation treatment for Specification 022.

The practical ADS path composes the already accepted retrieval identities,
Specification-012 one-hop Horizon builder, and the frozen Specification-022
ordering/capping rules. Dense retrieval remains an injected provider-free port
here so ordinary CI does not need the experiment-only FastEmbed runtime. A later
live-capable source may supply the frozen dense adapter without changing this
contract logic.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Mapping, Protocol, Sequence

from ads_system.application.horizon import (
    assess_applicability,
    build_methodological_horizon,
)
from ads_system.application.horizon_models import (
    HorizonCandidate,
    HorizonSeed,
)
from ads_system.application.ports import UnitOfWork
from ads_system.application.reasoning import KnowledgeRevisionPointer
from ads_system.application.retrieval import KnowledgeRetrievalHit

from experiments.methodological_navigation_coverage.contract import (
    FrozenContract,
    EvaluatorState,
    canonical_json_bytes,
    canonical_sha256,
    oracle_items_for_snapshot,
    project_state_to_retrieval_text,
)

CHANNEL_DEPTH = 6
DIRECT_SEED_LIMIT = 8
RRF_K = 60
HORIZON_LIMIT = 12


class RetrievalPort(Protocol):
    def search(
        self,
        query: str,
        *,
        limit: int = 10,
    ) -> tuple[KnowledgeRetrievalHit, ...]: ...


@dataclass(frozen=True, slots=True)
class FusedRetrievalHit:
    stable_key: str
    revision_id: str
    title: str
    rank: int
    rrf_score: float
    lexical_rank: int | None
    dense_rank: int | None


@dataclass(frozen=True, slots=True)
class MethodologicalHorizonContext:
    condition: str
    retrieval_query: str | None
    lexical_hits: tuple[KnowledgeRetrievalHit, ...]
    dense_hits: tuple[KnowledgeRetrievalHit, ...]
    fused_hits: tuple[FusedRetrievalHit, ...]
    included: tuple[HorizonCandidate, ...]
    excluded: tuple[HorizonCandidate, ...]
    truncated: tuple[HorizonCandidate, ...]
    methodological_context_payload: Mapping[str, object]
    methodological_context_sha256: str
    knowledge_revisions: tuple[KnowledgeRevisionPointer, ...]
    system_trace: Mapping[str, object]


def _validate_channel(
    hits: Sequence[KnowledgeRetrievalHit],
    channel_name: str,
) -> tuple[KnowledgeRetrievalHit, ...]:
    bounded = tuple(hits[:CHANNEL_DEPTH])
    keys = [item.stable_key for item in bounded]
    if len(keys) != len(set(keys)):
        raise ValueError(f"{channel_name} retrieval contains duplicate stable keys")
    for item in bounded:
        if not item.stable_key.strip() or not item.revision_id.strip():
            raise ValueError(f"{channel_name} retrieval identity must be non-empty")
    return bounded


def fuse_retrieval_hits(
    lexical_hits: Sequence[KnowledgeRetrievalHit],
    dense_hits: Sequence[KnowledgeRetrievalHit],
) -> tuple[FusedRetrievalHit, ...]:
    """Apply the frozen equal-weight RRF rule and return the top eight seeds."""

    lexical = _validate_channel(lexical_hits, "lexical")
    dense = _validate_channel(dense_hits, "dense")
    scores: dict[str, float] = {}
    revisions: dict[str, str] = {}
    titles: dict[str, str] = {}
    lexical_ranks: dict[str, int] = {}
    dense_ranks: dict[str, int] = {}

    for channel_name, hits, rank_store in (
        ("lexical", lexical, lexical_ranks),
        ("dense", dense, dense_ranks),
    ):
        for rank, hit in enumerate(hits, start=1):
            existing = revisions.get(hit.stable_key)
            if existing is not None and existing != hit.revision_id:
                raise ValueError(
                    f"retrieval revision mismatch for {hit.stable_key}: "
                    f"{existing} != {hit.revision_id}"
                )
            revisions[hit.stable_key] = hit.revision_id
            titles.setdefault(hit.stable_key, hit.title)
            rank_store[hit.stable_key] = rank
            scores[hit.stable_key] = scores.get(hit.stable_key, 0.0) + 1.0 / (
                RRF_K + rank
            )

    ordered = sorted(scores, key=lambda key: (-scores[key], key))[
        :DIRECT_SEED_LIMIT
    ]
    return tuple(
        FusedRetrievalHit(
            stable_key=stable_key,
            revision_id=revisions[stable_key],
            title=titles[stable_key],
            rank=rank,
            rrf_score=scores[stable_key],
            lexical_rank=lexical_ranks.get(stable_key),
            dense_rank=dense_ranks.get(stable_key),
        )
        for rank, stable_key in enumerate(ordered, start=1)
    )


def _candidate_sort_key(
    candidate: HorizonCandidate,
    direct_rank: Mapping[str, int],
) -> tuple[int, int, str, str]:
    if candidate.origin == "DIRECT":
        return (
            0,
            direct_rank[candidate.stable_key],
            "",
            candidate.stable_key,
        )
    source = candidate.relation_source_key
    if source is None or source not in direct_rank:
        raise ValueError(
            f"relation candidate {candidate.stable_key} lacks ranked source"
        )
    return (
        1,
        direct_rank[source],
        candidate.relation_type or "",
        candidate.stable_key,
    )


def _context_payload_and_revisions(
    candidates: Sequence[HorizonCandidate],
    *,
    uow_factory,
) -> tuple[dict[str, object], tuple[KnowledgeRevisionPointer, ...]]:
    knowledge: list[dict[str, object]] = []
    revisions: list[KnowledgeRevisionPointer] = []
    with uow_factory() as uow:
        for candidate in candidates:
            asset = uow.navigation.get_context_asset(
                candidate.stable_key,
                candidate.revision_id,
            )
            if asset is None:
                raise ValueError(
                    "included Horizon candidate has no exact accepted-current "
                    f"context projection: {candidate.stable_key}@{candidate.revision_id}"
                )
            knowledge.append(
                {
                    "title": asset.title,
                    "purpose": asset.purpose,
                    "applicability_state": candidate.applicability_state,
                    "missing_context_keys": list(candidate.missing_context_keys),
                }
            )
            revisions.append(
                KnowledgeRevisionPointer(
                    stable_key=candidate.stable_key,
                    revision_id=candidate.revision_id,
                )
            )
    payload: dict[str, object] = {"methodological_horizon": knowledge}
    return payload, tuple(revisions)


def build_ads_horizon_context(
    *,
    episode_id: str,
    snapshot: Mapping[str, object],
    lexical_retriever: RetrievalPort,
    dense_retriever: RetrievalPort,
    uow_factory,
) -> MethodologicalHorizonContext:
    """Build the frozen ADS_HORIZON treatment without evaluator knowledge."""

    query = project_state_to_retrieval_text(episode_id, snapshot)
    lexical = _validate_channel(
        lexical_retriever.search(query, limit=CHANNEL_DEPTH),
        "lexical",
    )
    dense = _validate_channel(
        dense_retriever.search(query, limit=CHANNEL_DEPTH),
        "dense",
    )
    fused = fuse_retrieval_hits(lexical, dense)
    seeds = tuple(
        HorizonSeed(
            stable_key=item.stable_key,
            revision_id=item.revision_id,
            title=item.title,
        )
        for item in fused
    )
    direct_rank = {item.stable_key: item.rank for item in fused}
    horizon = build_methodological_horizon(
        seeds,
        known_context=dict(snapshot["project_facts"]),
        uow_factory=uow_factory,
    )

    ordered_included = tuple(
        sorted(
            horizon.included,
            key=lambda item: _candidate_sort_key(item, direct_rank),
        )
    )
    included = ordered_included[:HORIZON_LIMIT]
    truncated = ordered_included[HORIZON_LIMIT:]
    excluded = tuple(
        sorted(
            horizon.excluded,
            key=lambda item: _candidate_sort_key(item, direct_rank),
        )
    )
    payload, revisions = _context_payload_and_revisions(
        included,
        uow_factory=uow_factory,
    )
    trace = {
        "query": query,
        "lexical": [
            {
                "stable_key": hit.stable_key,
                "revision_id": hit.revision_id,
                "rank": rank,
                "score": hit.score,
            }
            for rank, hit in enumerate(lexical, start=1)
        ],
        "dense": [
            {
                "stable_key": hit.stable_key,
                "revision_id": hit.revision_id,
                "rank": rank,
                "score": hit.score,
            }
            for rank, hit in enumerate(dense, start=1)
        ],
        "fused": [asdict(item) for item in fused],
        "included": [asdict(item) for item in included],
        "excluded": [asdict(item) for item in excluded],
        "truncated": [
            {
                **asdict(item),
                "pre_truncation_position": HORIZON_LIMIT + offset,
            }
            for offset, item in enumerate(truncated, start=1)
        ],
    }
    return MethodologicalHorizonContext(
        condition="ADS_HORIZON",
        retrieval_query=query,
        lexical_hits=lexical,
        dense_hits=dense,
        fused_hits=fused,
        included=included,
        excluded=excluded,
        truncated=truncated,
        methodological_context_payload=payload,
        methodological_context_sha256=canonical_sha256(payload),
        knowledge_revisions=revisions,
        system_trace=trace,
    )


def _representation_by_oracle_id(
    contract: FrozenContract,
) -> dict[str, tuple[str, ...]]:
    return {
        str(item["oracle_id"]): tuple(map(str, item["stable_keys"]))
        for item in contract.representation_map["mappings"]
    }


def build_oracle_horizon_context(
    *,
    contract: FrozenContract,
    episode_id: str,
    snapshot: Mapping[str, object],
    uow_factory,
) -> MethodologicalHorizonContext:
    """Build the evaluator-only ORACLE_HORIZON diagnostic upper bound.

    Only stable keys explicitly mapped to oracle items that are ACTIVE or
    MISSING_CONTEXT at this snapshot may enter the model-facing context. No
    relation-added asset is introduced in this diagnostic condition.
    """

    mapping = _representation_by_oracle_id(contract)
    relevant_keys: set[str] = set()
    for item in oracle_items_for_snapshot(
        contract,
        episode_id,
        str(snapshot["snapshot_id"]),
    ):
        state = EvaluatorState(str(item["expected_state"]))
        if state in {EvaluatorState.ACTIVE, EvaluatorState.MISSING_CONTEXT}:
            relevant_keys.update(mapping[str(item["oracle_id"])])

    included: list[HorizonCandidate] = []
    excluded: list[HorizonCandidate] = []
    with uow_factory() as uow:
        for stable_key in sorted(relevant_keys):
            asset = uow.navigation.get_current_asset(stable_key)
            if asset is None:
                raise ValueError(
                    f"oracle-mapped asset is not accepted-current: {stable_key}"
                )
            assessment = assess_applicability(
                asset,
                dict(snapshot["project_facts"]),
            )
            candidate = HorizonCandidate(
                stable_key=asset.stable_key,
                revision_id=asset.revision_id,
                title=asset.title,
                origin="DIRECT",
                relation_type=None,
                relation_revision_id=None,
                applicability_state=assessment.state,
                missing_context_keys=assessment.missing_context_keys,
                relation_source_key=None,
                reasoning_functions=asset.reasoning_functions,
            )
            if candidate.applicability_state == "INAPPLICABLE":
                excluded.append(candidate)
            else:
                included.append(candidate)

    payload, revisions = _context_payload_and_revisions(
        included,
        uow_factory=uow_factory,
    )
    trace = {
        "included": [asdict(item) for item in included],
        "excluded": [asdict(item) for item in excluded],
        "oracle_mapping_used_system_side": True,
    }
    return MethodologicalHorizonContext(
        condition="ORACLE_HORIZON",
        retrieval_query=None,
        lexical_hits=(),
        dense_hits=(),
        fused_hits=(),
        included=tuple(included),
        excluded=tuple(excluded),
        truncated=(),
        methodological_context_payload=payload,
        methodological_context_sha256=canonical_sha256(payload),
        knowledge_revisions=revisions,
        system_trace=trace,
    )


def empty_generic_context() -> MethodologicalHorizonContext:
    payload: dict[str, object] = {}
    return MethodologicalHorizonContext(
        condition="GENERIC",
        retrieval_query=None,
        lexical_hits=(),
        dense_hits=(),
        fused_hits=(),
        included=(),
        excluded=(),
        truncated=(),
        methodological_context_payload=payload,
        methodological_context_sha256=canonical_sha256(payload),
        knowledge_revisions=(),
        system_trace={},
    )
