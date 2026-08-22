from __future__ import annotations

import copy
import json
import os
from pathlib import Path

from alembic import command
from alembic.config import Config

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


def _upgrade(database_url: str) -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, "head")
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


def _candidate_bundle() -> dict:
    bundle = copy.deepcopy(load_bundle(KNOWLEDGE_FIXTURE))
    bundle["bundle_kind"] = "CANDIDATE_SET"
    validate_bundle(bundle)
    validate_import_safety(bundle)
    return bundle


def _benchmark() -> dict:
    return json.loads(BENCHMARK_FIXTURE.read_text(encoding="utf-8"))


def _ordered_identity(hits) -> tuple[tuple[str, str], ...]:
    return tuple((hit.stable_key, hit.revision_id) for hit in hits)


def test_sqlite_fts_retrieval_frozen_benchmark(tmp_path: Path) -> None:
    database_url = sqlite_database_url(tmp_path / "retrieval.sqlite3")
    _upgrade(database_url)
    engine = create_operational_engine(database_url)
    uow_factory = lambda: SqlAlchemyUnitOfWork(engine)
    retriever = SqliteFtsKnowledgeRetrieval(engine)

    try:
        candidate = _candidate_bundle()
        benchmark = _benchmark()

        # RL-01: importing candidate material must not make it retrievable.
        import_candidate_bundle(candidate, uow_factory=uow_factory)
        assert retriever.rebuild() == 0
        assert retriever.indexed_document_count() == 0
        assert retriever.search("random forest", limit=3) == ()

        # Test-only benchmark acceptance goes through the normal explicit path.
        accept_candidate_bundle(candidate, uow_factory=uow_factory)
        snapshot_before = export_current_accepted_snapshot(uow_factory=uow_factory)
        digest_before = semantic_digest(snapshot_before)

        assert retriever.rebuild() == 10
        assert retriever.indexed_document_count() == 10

        reciprocal_ranks: list[float] = []
        lexical_identities: dict[str, tuple[tuple[str, str], ...]] = {}

        for case in benchmark["lexical_cases"]:
            hits = retriever.search(case["query"], limit=3)
            keys = [hit.stable_key for hit in hits]
            lexical_identities[case["case_id"]] = _ordered_identity(hits)
            for required_key in case["required_keys"]:
                assert required_key in keys, (
                    f"{case['case_id']} omitted {required_key!r}; got {keys!r}"
                )
                reciprocal_ranks.append(1.0 / (keys.index(required_key) + 1))
            assert all(hit.channel == "LEXICAL" for hit in hits)

        # Frozen RH-L gate: all ten required keys are present inside top three.
        assert len(reciprocal_ranks) == 10
        assert sum(rank > 0 for rank in reciprocal_ranks) / 10 == 1.0

        # RL-10: execute semantic diagnostics without making them lexical gates.
        semantic_results: dict[str, tuple[str, ...]] = {}
        for case in benchmark["semantic_diagnostic_cases"]:
            hits = retriever.search(case["query"], limit=3)
            semantic_results[case["case_id"]] = tuple(hit.stable_key for hit in hits)
        assert set(semantic_results) == {"RH-S01", "RH-S02", "RH-S03", "RH-S04"}

        # RL-02: hits identify the exact current accepted revision.
        with SqlAlchemyUnitOfWork(engine) as uow:
            for case in benchmark["lexical_cases"]:
                for required_key in case["required_keys"]:
                    current = uow.knowledge.get_current_asset_revision(required_key)
                    assert current is not None
                    hit = next(
                        item
                        for item in retriever.search(case["query"], limit=3)
                        if item.stable_key == required_key
                    )
                    assert hit.revision_id == current.revision_id

        # RL-03: unchanged authoritative knowledge rebuilds identically.
        assert retriever.rebuild() == 10
        for case in benchmark["lexical_cases"]:
            assert _ordered_identity(retriever.search(case["query"], limit=3)) == (
                lexical_identities[case["case_id"]]
            )

        # RL-04/RL-05: bounded output and query safety.
        assert len(retriever.search("distribution", limit=1)) <= 1
        assert retriever.search("distribution", limit=0) == ()
        assert retriever.search("distribution", limit=-1) == ()
        assert retriever.search("", limit=3) == ()
        assert retriever.search("   ", limit=3) == ()
        assert retriever.search("!!! ... --", limit=3) == ()

        # RL-06: rebuild/search cannot mutate authoritative semantic state.
        snapshot_after = export_current_accepted_snapshot(uow_factory=uow_factory)
        assert semantic_digest(snapshot_after) == digest_before
        assert snapshot_after == snapshot_before

        # RL-01/RL-02 supersession: historical accepted revision remains durable
        # but disappears from the current retrieval projection after a new
        # accepted revision advances the current pointer.
        with SqlAlchemyUnitOfWork(engine) as uow:
            old_random_forest = uow.knowledge.get_current_asset_revision("random-forest")
            assert old_random_forest is not None
            new_random_forest = uow.knowledge.publish_asset_revision(
                stable_key="random-forest",
                intrinsic_kind="METHOD",
                title="Random Forest Revised",
                purpose="Current accepted Random Forest retrieval supersession sentinel.",
                actor="retrieval-test",
            )
            uow.commit()

        assert new_random_forest.revision_id != old_random_forest.revision_id
        assert retriever.rebuild() == 10
        hits = retriever.search("random forest", limit=3)
        random_forest_hit = next(hit for hit in hits if hit.stable_key == "random-forest")
        assert random_forest_hit.revision_id == new_random_forest.revision_id
        assert all(hit.revision_id != old_random_forest.revision_id for hit in hits)
    finally:
        engine.dispose()
