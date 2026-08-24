from __future__ import annotations

import copy
import os
from pathlib import Path

from alembic import command
from alembic.config import Config

from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
from ads_system.application.retrieval import KnowledgeRetrievalHit
from ads_system.infrastructure.interchange.knowledge_bundle import (
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
from experiments.methodological_navigation_coverage.contract import (
    load_frozen_contract,
    snapshot_by_id,
)
from experiments.methodological_navigation_coverage.navigation import (
    CHANNEL_DEPTH,
    HORIZON_LIMIT,
    build_ads_horizon_context,
)

ROOT = Path(__file__).resolve().parents[2]


def _upgrade(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


class FixedDenseRetriever:
    """Provider-free deterministic dense-channel test double.

    The production experiment later supplies the frozen FastEmbed implementation.
    This double exists only to validate RRF, revision identity, Horizon expansion,
    applicability, ordering, capping, and model-facing serialization without a
    network/model download in ordinary CI.

    ``revalidation-after-data-change`` is intentionally ranked first because its
    frozen outbound relation targets are not ordinary E1 retrieval seeds. This
    guarantees that the integration test exercises relation-added candidates
    rather than accidentally deduplicating every relation target as a direct
    seed.
    """

    def __init__(self, accepted_assets: dict[str, dict]) -> None:
        self._accepted_assets = accepted_assets
        self._keys = (
            "revalidation-after-data-change",
            "prediction-moment",
            "prediction-time-feature-eligibility",
            "temporal-validation",
            "class-imbalance",
            "data-leakage",
        )

    def search(self, query: str, *, limit: int = 10) -> tuple[KnowledgeRetrievalHit, ...]:
        assert query
        hits = []
        for index, stable_key in enumerate(self._keys, start=1):
            asset = self._accepted_assets[stable_key]
            hits.append(
                KnowledgeRetrievalHit(
                    stable_key=stable_key,
                    revision_id=str(asset["revision_id"]),
                    title=str(asset["title"]),
                    score=1.0 / index,
                    channel="DENSE_TEST_DOUBLE",
                )
            )
        return tuple(hits[:limit])


def test_spec022_fixed_database_navigation_is_deterministic_and_read_only(
    tmp_path: Path,
) -> None:
    contract = load_frozen_contract()
    database_url = sqlite_database_url(tmp_path / "spec022.sqlite3")
    _upgrade(database_url)
    engine = create_operational_engine(database_url)
    uow_factory = lambda: SqlAlchemyUnitOfWork(engine)
    lexical = SqliteFtsKnowledgeRetrieval(engine)

    try:
        candidate = copy.deepcopy(dict(contract.universe))
        candidate["bundle_kind"] = "CANDIDATE_SET"
        validate_bundle(candidate)
        validate_import_safety(candidate)
        import_candidate_bundle(candidate, uow_factory=uow_factory)
        assert lexical.rebuild() == 0
        accept_candidate_bundle(candidate, uow_factory=uow_factory)
        assert lexical.rebuild() == 28
        assert lexical.indexed_document_count() == 28

        accepted_before = export_current_accepted_snapshot(uow_factory=uow_factory)
        digest_before = semantic_digest(accepted_before)
        accepted_assets = {
            str(item["stable_key"]): item for item in accepted_before["assets"]
        }
        dense = FixedDenseRetriever(accepted_assets)
        snapshot = snapshot_by_id(contract, "E1", "E1-S1")

        first = build_ads_horizon_context(
            episode_id="E1",
            snapshot=snapshot,
            lexical_retriever=lexical,
            dense_retriever=dense,
            uow_factory=uow_factory,
        )
        second = build_ads_horizon_context(
            episode_id="E1",
            snapshot=snapshot,
            lexical_retriever=lexical,
            dense_retriever=dense,
            uow_factory=uow_factory,
        )

        assert first == second
        assert len(first.lexical_hits) <= CHANNEL_DEPTH
        assert len(first.dense_hits) <= CHANNEL_DEPTH
        assert len(first.fused_hits) <= 8
        assert len(first.included) <= HORIZON_LIMIT
        assert first.methodological_context_sha256 == second.methodological_context_sha256
        assert first.methodological_context_payload == second.methodological_context_payload
        assert len(first.knowledge_revisions) == len(first.included)
        assert [item.stable_key for item in first.knowledge_revisions] == [
            item.stable_key for item in first.included
        ]

        model_payload = first.methodological_context_payload["methodological_horizon"]
        assert model_payload
        for item in model_payload:
            assert set(item) == {
                "title",
                "purpose",
                "applicability_state",
                "missing_context_keys",
            }
            assert "stable_key" not in item
            assert "revision_id" not in item

        included_keys = {item.stable_key for item in first.included}
        assert "prediction-moment" in included_keys
        assert "prediction-time-feature-eligibility" in included_keys
        assert any(
            item.origin == "RELATION"
            for item in (*first.included, *first.excluded, *first.truncated)
        )

        accepted_after = export_current_accepted_snapshot(uow_factory=uow_factory)
        assert accepted_after == accepted_before
        assert semantic_digest(accepted_after) == digest_before
    finally:
        engine.dispose()
