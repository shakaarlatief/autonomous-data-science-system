from __future__ import annotations

import copy
import json
import os
import uuid
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config

from ads_system.application.knowledge_interchange import (
    accept_candidate_bundle,
    export_current_accepted_snapshot,
    import_candidate_bundle,
)
from ads_system.infrastructure.interchange.knowledge_bundle import (
    dumps_bundle,
    load_bundle,
    semantic_digest,
    validate_bundle,
    validate_import_safety,
)
from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.persistence.interchange_repository import (
    KnowledgePersistenceConflict,
)
from ads_system.infrastructure.persistence.uow import SqlAlchemyUnitOfWork

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"


def _upgrade(database_url: str, target: str = "head") -> None:
    config = Config(str(ROOT / "alembic.ini"))
    config.set_main_option("script_location", str(ROOT / "migrations"))
    config.set_main_option("sqlalchemy.url", database_url)
    os.environ["ADS_DATABASE_URL"] = database_url
    try:
        command.upgrade(config, target)
    finally:
        os.environ.pop("ADS_DATABASE_URL", None)


def _candidate_bundle() -> dict:
    bundle = load_bundle(FIXTURE)
    bundle = copy.deepcopy(bundle)
    bundle["bundle_kind"] = "CANDIDATE_SET"
    validate_bundle(bundle)
    validate_import_safety(bundle)
    return bundle


def _updated_random_forest_bundle(original: dict) -> dict:
    random_forest = copy.deepcopy(
        next(asset for asset in original["assets"] if asset["stable_key"] == "random-forest")
    )
    random_forest["revision_id"] = str(uuid.uuid4())
    random_forest["revision_no"] = 2
    random_forest["governance_status"] = "CANDIDATE"
    random_forest["purpose"] = (
        "Flexible supervised prediction by aggregating randomized decision trees "
        "with explicit variance-reduction semantics."
    )
    for component in random_forest["components"]:
        component["revision_id"] = str(uuid.uuid4())
        component["revision_no"] = 2
        component["governance_status"] = "CANDIDATE"
    for rule in random_forest["rules"]:
        rule["rule_spec_id"] = str(uuid.uuid4())

    referenced = set(random_forest["provenance_source_ids"])
    for component in random_forest["components"]:
        referenced.update(component["provenance_source_ids"])
    for rule in random_forest["rules"]:
        referenced.update(rule["provenance_source_ids"])

    bundle = {
        "format": "ads-reusable-knowledge-bundle",
        "schema_version": 1,
        "bundle_kind": "CANDIDATE_SET",
        "assets": [random_forest],
        "relations": [],
        "provenance_sources": [
            copy.deepcopy(source)
            for source in original["provenance_sources"]
            if source["source_id"] in referenced
        ],
        "collections": [],
    }
    validate_bundle(bundle)
    validate_import_safety(bundle)
    return bundle


def _exercise_roundtrip(database_url: str) -> None:
    # IR-01: prove migration 0001 data remains reconstructable after 0002.
    _upgrade(database_url, "0001_v1_persistence_core")
    engine = create_operational_engine(database_url)
    try:
        with SqlAlchemyUnitOfWork(engine) as uow:
            legacy_a = uow.knowledge.publish_asset_revision(
                stable_key="legacy-a",
                intrinsic_kind="CONCEPT",
                title="Legacy A",
                purpose="Migration compatibility sentinel A.",
            )
            legacy_b = uow.knowledge.publish_asset_revision(
                stable_key="legacy-b",
                intrinsic_kind="CONCEPT",
                title="Legacy B",
                purpose="Migration compatibility sentinel B.",
            )
            legacy_relation = uow.knowledge.create_relation(
                source_node_id=legacy_a.asset_id,
                target_node_id=legacy_b.asset_id,
                relation_type="COMPLEMENTS",
                rationale="Migration 0001 relation-state compatibility sentinel.",
            )
            uow.commit()
    finally:
        engine.dispose()

    _upgrade(database_url, "head")
    engine = create_operational_engine(database_url)
    uow_factory = lambda: SqlAlchemyUnitOfWork(engine)
    try:
        migrated_snapshot = export_current_accepted_snapshot(uow_factory=uow_factory)
        assert {asset["stable_key"] for asset in migrated_snapshot["assets"]} == {
            "legacy-a",
            "legacy-b",
        }
        assert [relation["relation_id"] for relation in migrated_snapshot["relations"]] == [
            legacy_relation.relation_id
        ]

        candidate = _candidate_bundle()

        # IR-02: candidate import is idempotent and leaves accepted authority unchanged.
        import_candidate_bundle(candidate, uow_factory=uow_factory)
        import_candidate_bundle(candidate, uow_factory=uow_factory)
        with SqlAlchemyUnitOfWork(engine) as uow:
            assert uow.knowledge.get_current_asset_revision("random-forest") is None

        # IR-03: same durable revision identity with different content is rejected.
        conflict = copy.deepcopy(candidate)
        next(
            asset for asset in conflict["assets"] if asset["stable_key"] == "random-forest"
        )["title"] = "Conflicting Random Forest title"
        with pytest.raises(KnowledgePersistenceConflict):
            import_candidate_bundle(conflict, uow_factory=uow_factory)

        # IR-04: explicit acceptance advances current pointers only after review action.
        accept_candidate_bundle(candidate, uow_factory=uow_factory)
        with SqlAlchemyUnitOfWork(engine) as uow:
            random_forest_r1 = uow.knowledge.get_current_asset_revision("random-forest")
            assert random_forest_r1 is not None
            assert random_forest_r1.revision_no == 1

            project = uow.projects.create_project(title="Knowledge roundtrip pin test")
            finding = uow.projects.add_finding(
                project_id=project.project_id,
                finding_type="METHODOLOGICAL",
                statement="Random Forest is a candidate nonlinear benchmark.",
            )
            uow.projects.link_finding_to_knowledge(
                finding_id=finding.finding_id,
                project_id=project.project_id,
                knowledge_revision_id=random_forest_r1.revision_id,
                reference_type="INFORMED_BY",
            )
            uow.commit()

        # IR-05: accepted snapshot is valid, trusted-only, deterministic, and reloadable.
        snapshot_r1 = export_current_accepted_snapshot(uow_factory=uow_factory)
        validate_bundle(snapshot_r1)
        validate_import_safety(snapshot_r1, trusted_accepted_snapshot=True)
        text_r1 = dumps_bundle(snapshot_r1)
        assert dumps_bundle(json.loads(text_r1)) == text_r1
        assert semantic_digest(json.loads(text_r1)) == semantic_digest(snapshot_r1)
        exported_keys = {asset["stable_key"] for asset in snapshot_r1["assets"]}
        assert set(asset["stable_key"] for asset in candidate["assets"]).issubset(
            exported_keys
        )

        # IR-06: later candidate revision does not alter the accepted current revision.
        update_bundle = _updated_random_forest_bundle(candidate)
        random_forest_r2_doc = update_bundle["assets"][0]
        import_candidate_bundle(update_bundle, uow_factory=uow_factory)
        with SqlAlchemyUnitOfWork(engine) as uow:
            current_before_accept = uow.knowledge.get_current_asset_revision(
                "random-forest"
            )
            assert current_before_accept is not None
            assert current_before_accept.revision_id == random_forest_r1.revision_id

        # IR-07: explicit acceptance supersedes R1 while historical project pin remains R1.
        accept_candidate_bundle(update_bundle, uow_factory=uow_factory)
        with SqlAlchemyUnitOfWork(engine) as uow:
            random_forest_r2 = uow.knowledge.get_current_asset_revision("random-forest")
            assert random_forest_r2 is not None
            assert random_forest_r2.revision_id == random_forest_r2_doc["revision_id"]
            assert random_forest_r2.revision_no == 2
            assert uow.projects.knowledge_references_for_finding(finding.finding_id) == (
                random_forest_r1.revision_id,
            )

        # IR-08: export reflects R2 as current but keeps the database history separate.
        snapshot_r2 = export_current_accepted_snapshot(uow_factory=uow_factory)
        exported_rf = next(
            asset for asset in snapshot_r2["assets"] if asset["stable_key"] == "random-forest"
        )
        assert exported_rf["revision_id"] == random_forest_r2_doc["revision_id"]
        assert exported_rf["revision_no"] == 2
        assert exported_rf["governance_status"] == "ACCEPTED"
        assert exported_rf["purpose"] == random_forest_r2_doc["purpose"]
        assert all(
            component["governance_status"] == "ACCEPTED"
            for component in exported_rf["components"]
        )
        validate_import_safety(snapshot_r2, trusted_accepted_snapshot=True)
    finally:
        engine.dispose()


def test_sqlite_knowledge_interchange_roundtrip(tmp_path: Path) -> None:
    _exercise_roundtrip(sqlite_database_url(tmp_path / "knowledge-roundtrip.db"))


def test_postgres_knowledge_interchange_roundtrip_when_configured() -> None:
    database_url = os.environ.get("ADS_TEST_POSTGRES_URL")
    if not database_url:
        pytest.skip("ADS_TEST_POSTGRES_URL is not configured")
    _exercise_roundtrip(database_url)
