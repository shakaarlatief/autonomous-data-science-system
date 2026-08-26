from __future__ import annotations

import copy
import json
import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config

from ads_system.application.horizon import (
    ApplicabilityEvaluationError,
    StaleKnowledgeCandidateError,
    assess_applicability,
    build_methodological_horizon,
)
from ads_system.application.horizon_models import HorizonSeed
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


def _snapshot_asset_map(snapshot: dict) -> dict[str, dict]:
    return {asset["stable_key"]: asset for asset in snapshot["assets"]}


def _direct_snapshot_relations(snapshot: dict, source_key: str) -> list[dict]:
    return sorted(
        [
            relation
            for relation in snapshot["relations"]
            if relation["source_ref"].get("asset_key") == source_key
            and "asset_key" in relation["target_ref"]
        ],
        key=lambda relation: (
            relation["relation_type"],
            relation["target_ref"]["asset_key"],
            relation["relation_revision_id"],
        ),
    )


def test_first_methodological_horizon_frozen_benchmark(tmp_path: Path) -> None:
    database_url = sqlite_database_url(tmp_path / "horizon.sqlite3")
    _upgrade(database_url)
    engine = create_operational_engine(database_url)
    uow_factory = lambda: SqlAlchemyUnitOfWork(engine)

    try:
        benchmark = _benchmark()
        candidate = _candidate_bundle()

        # Candidate knowledge is not operational navigation authority.
        import_candidate_bundle(candidate, uow_factory=uow_factory)
        with SqlAlchemyUnitOfWork(engine) as uow:
            assert uow.navigation.get_current_asset("random-forest") is None
            assert uow.navigation.get_outbound_related_assets("random-forest") == ()

        accept_candidate_bundle(candidate, uow_factory=uow_factory)
        snapshot_before = export_current_accepted_snapshot(uow_factory=uow_factory)
        digest_before = semantic_digest(snapshot_before)
        snapshot_assets = _snapshot_asset_map(snapshot_before)

        relational_results: dict[str, dict] = {}
        for case in benchmark["relational_horizon_cases"]:
            with SqlAlchemyUnitOfWork(engine) as uow:
                seed_asset = uow.navigation.get_current_asset(case["seed_key"])
            assert seed_asset is not None

            horizon = build_methodological_horizon(
                [
                    HorizonSeed(
                        stable_key=seed_asset.stable_key,
                        revision_id=seed_asset.revision_id,
                        title=seed_asset.title,
                    )
                ],
                known_context={},
                uow_factory=uow_factory,
            )
            relation_candidates = [
                item for item in horizon.included if item.origin == "RELATION"
            ] + [item for item in horizon.excluded if item.origin == "RELATION"]
            relation_keys = {item.stable_key for item in relation_candidates}

            assert set(case["expected_related_keys"]).issubset(relation_keys), (
                case["case_id"],
                case["expected_related_keys"],
                sorted(relation_keys),
            )

            # The builder must equal the authoritative accepted-current one-hop
            # outbound relation set. This catches reverse or recursive expansion.
            snapshot_relations = _direct_snapshot_relations(
                snapshot_before, case["seed_key"]
            )
            expected_direct_keys = {
                relation["target_ref"]["asset_key"] for relation in snapshot_relations
            }
            assert relation_keys == expected_direct_keys

            relation_by_target = {
                relation["target_ref"]["asset_key"]: relation
                for relation in snapshot_relations
            }
            for item in relation_candidates:
                target_asset = snapshot_assets[item.stable_key]
                source_relation = relation_by_target[item.stable_key]
                assert item.revision_id == target_asset["revision_id"]
                assert item.relation_revision_id == source_relation["relation_revision_id"]
                assert item.relation_type == source_relation["relation_type"]

            direct_candidates = [
                item for item in horizon.included if item.origin == "DIRECT"
            ] + [item for item in horizon.excluded if item.origin == "DIRECT"]
            assert len(direct_candidates) == 1
            assert direct_candidates[0].stable_key == case["seed_key"]
            assert direct_candidates[0].revision_id == snapshot_assets[case["seed_key"]][
                "revision_id"
            ]

            relational_results[case["case_id"]] = {
                "seed_key": case["seed_key"],
                "direct_revision_id": direct_candidates[0].revision_id,
                "related": [
                    {
                        "stable_key": item.stable_key,
                        "revision_id": item.revision_id,
                        "relation_type": item.relation_type,
                        "relation_revision_id": item.relation_revision_id,
                        "applicability_state": item.applicability_state,
                    }
                    for item in sorted(
                        relation_candidates, key=lambda candidate: candidate.stable_key
                    )
                ],
            }

        applicability_results: dict[str, dict] = {}
        for case in benchmark["applicability_cases"]:
            with SqlAlchemyUnitOfWork(engine) as uow:
                asset = uow.navigation.get_current_asset(case["asset_key"])
            assert asset is not None
            assessment = assess_applicability(asset, case["known_context"])
            assert assessment.state == case["expected_state"], (
                case["case_id"],
                case["expected_state"],
                assessment,
            )
            if case["expected_state"] == "MISSING_CONTEXT":
                assert assessment.missing_context_keys
            if case["expected_state"] == "INAPPLICABLE":
                assert assessment.missing_context_keys == ()
                assert assessment.unknown_predicate_keys == ()

            applicability_results[case["case_id"]] = {
                "asset_key": case["asset_key"],
                "revision_id": asset.revision_id,
                "known_context": case["known_context"],
                "state": assessment.state,
                "missing_context_keys": assessment.missing_context_keys,
                "unknown_predicate_keys": assessment.unknown_predicate_keys,
            }

        # Known negative applicability must place the direct candidate in the
        # explicit excluded group rather than silently dropping it.
        random_forest = snapshot_assets["random-forest"]
        rejected_horizon = build_methodological_horizon(
            [
                HorizonSeed(
                    stable_key="random-forest",
                    revision_id=random_forest["revision_id"],
                    title=random_forest["title"],
                )
            ],
            known_context={
                "project.task.is_supervised": False,
                "data.representation.is_supported_tabular": True,
            },
            uow_factory=uow_factory,
        )
        assert any(
            item.stable_key == "random-forest"
            and item.applicability_state == "INAPPLICABLE"
            for item in rejected_horizon.excluded
        )
        assert all(
            item.stable_key != "random-forest" for item in rejected_horizon.included
        )

        # A direct seed owns candidate origin when a relation also reaches it.
        histogram = snapshot_assets["histogram"]
        ecdf = snapshot_assets["ecdf"]
        duplicate_horizon = build_methodological_horizon(
            [
                HorizonSeed(
                    stable_key="histogram",
                    revision_id=histogram["revision_id"],
                    title=histogram["title"],
                ),
                HorizonSeed(
                    stable_key="ecdf",
                    revision_id=ecdf["revision_id"],
                    title=ecdf["title"],
                ),
            ],
            known_context={},
            uow_factory=uow_factory,
        )
        all_duplicate_candidates = [
            *duplicate_horizon.included,
            *duplicate_horizon.excluded,
        ]
        ecdf_candidates = [
            item for item in all_duplicate_candidates if item.stable_key == "ecdf"
        ]
        assert len(ecdf_candidates) == 1
        assert ecdf_candidates[0].origin == "DIRECT"

        # Stale revision-transparent candidates are rejected explicitly.
        with pytest.raises(StaleKnowledgeCandidateError):
            build_methodological_horizon(
                [
                    HorizonSeed(
                        stable_key="random-forest",
                        revision_id="00000000-0000-0000-0000-000000000000",
                        title=random_forest["title"],
                    )
                ],
                known_context={},
                uow_factory=uow_factory,
            )

        # The frozen direct-predicate subset rejects ambiguous truthiness.
        with SqlAlchemyUnitOfWork(engine) as uow:
            rf_asset = uow.navigation.get_current_asset("random-forest")
        assert rf_asset is not None
        with pytest.raises(ApplicabilityEvaluationError):
            assess_applicability(
                rf_asset,
                {
                    "project.task.is_supervised": "yes",
                    "data.representation.is_supported_tabular": True,
                },
            )

        # Horizon construction is derived/read-only application behavior.
        snapshot_after = export_current_accepted_snapshot(uow_factory=uow_factory)
        assert snapshot_after == snapshot_before
        assert semantic_digest(snapshot_after) == digest_before

        result = {
            "specification": "012-v0.1",
            "relational_cases_passed": len(relational_results),
            "applicability_cases_passed": len(applicability_results),
            "relational_results": relational_results,
            "applicability_results": applicability_results,
            "authoritative_knowledge_unchanged": True,
        }
        print("V1_METHODOLOGICAL_HORIZON_JSON=" + json.dumps(result, sort_keys=True))
    finally:
        engine.dispose()
