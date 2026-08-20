from __future__ import annotations

import os
from pathlib import Path

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from ads_system.infrastructure.persistence.engine import (
    create_operational_engine,
    sqlite_database_url,
)
from ads_system.infrastructure.persistence.schema import (
    kg_relation,
    kg_revision_governance,
    kg_rule_spec,
)
from ads_system.infrastructure.persistence.uow import SqlAlchemyUnitOfWork

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


def _exercise_vertical_slice(database_url: str) -> None:
    _upgrade(database_url)
    engine = create_operational_engine(database_url)
    try:
        with SqlAlchemyUnitOfWork(engine) as uow:
            histogram = uow.knowledge.publish_asset_revision(
                stable_key="histogram",
                intrinsic_kind="METHOD",
                title="Histogram",
                purpose="Characterize a quantitative empirical distribution.",
            )
            random_forest_r1 = uow.knowledge.publish_asset_revision(
                stable_key="random-forest",
                intrinsic_kind="METHOD",
                title="Random Forest",
                purpose="Flexible tree-ensemble prediction through randomized bagging.",
            )
            component_revision_id = uow.knowledge.add_component_revision(
                parent_asset_revision_id=random_forest_r1.revision_id,
                component_key="variance-reduction-mechanism",
                component_kind="MECHANISM",
                body="Aggregate randomized trees to reduce variance relative to one unstable tree.",
            )
            relation = uow.knowledge.create_relation(
                source_node_id=random_forest_r1.asset_id,
                target_node_id=histogram.asset_id,
                relation_type="COMPLEMENTS",
                rationale="A predictive model and a distribution diagnostic serve different project questions.",
            )
            rule_id = uow.knowledge.add_rule(
                owner_content_revision_id=random_forest_r1.revision_id,
                rule_key="consider-for-supervised-tabular-nonlinearity",
                condition={
                    "all": [
                        {"predicate": "project.is_supervised"},
                        {"predicate": "data.is_tabular"},
                    ]
                },
                consequence_type="RECOMMEND_OPTION",
                consequence_payload={"asset_key": "random-forest"},
                force="HEURISTIC",
                unknown_behavior="DEFER",
                rationale="Applicability does not imply automatic selection.",
            )

            project = uow.projects.create_project(title="Persistence vertical slice")
            finding = uow.projects.add_finding(
                project_id=project.project_id,
                finding_type="METHODOLOGICAL",
                statement="A nonlinear tabular benchmark is worth evaluating.",
            )
            uow.projects.link_finding_to_knowledge(
                finding_id=finding.finding_id,
                project_id=project.project_id,
                knowledge_revision_id=random_forest_r1.revision_id,
                reference_type="INFORMED_BY",
            )
            uow.commit()

        with SqlAlchemyUnitOfWork(engine) as uow:
            random_forest_r2 = uow.knowledge.publish_asset_revision(
                stable_key="random-forest",
                intrinsic_kind="METHOD",
                title="Random Forest",
                purpose="Flexible randomized tree-ensemble prediction with explicit variance-reduction semantics.",
            )
            uow.commit()

        with SqlAlchemyUnitOfWork(engine) as uow:
            current = uow.knowledge.get_current_asset_revision("random-forest")
            historical = uow.knowledge.get_asset_revision(random_forest_r1.revision_id)
            pinned = uow.projects.knowledge_references_for_finding(finding.finding_id)

            assert current is not None
            assert historical is not None
            assert current.revision_id == random_forest_r2.revision_id
            assert current.revision_no == 2
            assert historical.revision_id == random_forest_r1.revision_id
            assert historical.revision_no == 1
            assert pinned == (random_forest_r1.revision_id,)

        with engine.connect() as connection:
            relation_count = connection.execute(
                select(kg_relation.c.relation_id).where(
                    kg_relation.c.relation_id == relation.relation_id
                )
            ).all()
            rule_count = connection.execute(
                select(kg_rule_spec.c.rule_spec_id).where(
                    kg_rule_spec.c.rule_spec_id == rule_id
                )
            ).all()
            statuses = dict(
                connection.execute(
                    select(
                        kg_revision_governance.c.revision_id,
                        kg_revision_governance.c.current_status,
                    ).where(
                        kg_revision_governance.c.revision_id.in_(
                            [
                                component_revision_id,
                                random_forest_r1.revision_id,
                                random_forest_r2.revision_id,
                            ]
                        )
                    )
                ).all()
            )

            assert len(relation_count) == 1
            assert len(rule_count) == 1
            assert statuses[component_revision_id] == "ACCEPTED"
            assert statuses[random_forest_r1.revision_id] == "SUPERSEDED"
            assert statuses[random_forest_r2.revision_id] == "ACCEPTED"

        with pytest.raises(IntegrityError):
            with SqlAlchemyUnitOfWork(engine) as uow:
                other_project = uow.projects.create_project(title="Other project")
                uow.projects.link_finding_to_knowledge(
                    finding_id=finding.finding_id,
                    project_id=other_project.project_id,
                    knowledge_revision_id=random_forest_r1.revision_id,
                    reference_type="INVALID_CROSS_PROJECT_REFERENCE",
                )
                uow.commit()
    finally:
        engine.dispose()


def test_sqlite_vertical_slice(tmp_path: Path) -> None:
    _exercise_vertical_slice(sqlite_database_url(tmp_path / "ads-v1.db"))


def test_postgres_vertical_slice_when_configured() -> None:
    database_url = os.environ.get("ADS_TEST_POSTGRES_URL")
    if not database_url:
        pytest.skip("ADS_TEST_POSTGRES_URL is not configured")
    _exercise_vertical_slice(database_url)
