"""Targeted tooling spike for the accepted V1 persistence architecture.

This is experimental architecture-validation code, not production V1 code.
It tests whether SQLAlchemy Core plus Alembic can implement Specification 001
cleanly on SQLite while preserving a credible PostgreSQL path.
"""

from __future__ import annotations

import os
import tempfile
import uuid
from pathlib import Path

from alembic.migration import MigrationContext
from alembic.operations import Operations
from sqlalchemy import (
    CheckConstraint,
    Column,
    DDL,
    ForeignKey,
    Integer,
    MetaData,
    Table,
    Text,
    UniqueConstraint,
    create_engine,
    event,
    inspect,
    select,
    text,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.types import TypeDecorator

NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class DomainUUID(TypeDecorator):
    """Portable UUID preserving Specification 001 storage semantics.

    SQLite stores canonical hyphenated lowercase UUID text, while PostgreSQL
    uses its native UUID type. The Python-facing value remains a string so the
    domain contract is independent of a specific DBAPI UUID return type.
    """

    impl = Text
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(PG_UUID(as_uuid=False))
        return dialect.type_descriptor(Text())

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return str(uuid.UUID(str(value))).lower()

    def process_result_value(self, value, dialect):
        if value is None:
            return None
        return str(value).lower()


def new_id() -> str:
    return str(uuid.uuid4())


def build_metadata() -> MetaData:
    metadata = MetaData(naming_convention=NAMING_CONVENTION)

    node_type_check = CheckConstraint(
        "node_type IN ('ASSET','COMPONENT')",
        name="node_type_allowed",
    )

    kg_node = Table(
        "kg_node",
        metadata,
        Column("node_id", DomainUUID(), primary_key=True),
        Column("node_type", Text, nullable=False),
        node_type_check,
        sqlite_strict=True,
    )

    kg_asset = Table(
        "kg_asset",
        metadata,
        Column(
            "asset_id",
            DomainUUID(),
            ForeignKey("kg_node.node_id", ondelete="CASCADE"),
            primary_key=True,
        ),
        Column("stable_key", Text, nullable=False),
        UniqueConstraint("stable_key", name="stable_key"),
        sqlite_strict=True,
    )

    kg_content_revision = Table(
        "kg_content_revision",
        metadata,
        Column("revision_id", DomainUUID(), primary_key=True),
        Column(
            "node_id",
            DomainUUID(),
            ForeignKey("kg_node.node_id", ondelete="CASCADE"),
            nullable=False,
        ),
        Column("revision_no", Integer, nullable=False),
        Column("payload_json", Text, nullable=False),
        UniqueConstraint("node_id", "revision_no", name="node_revision_no"),
        sqlite_strict=True,
    )

    # json_valid() is an SQLite adapter strengthening, not a cross-database
    # domain assumption. Application validation remains mandatory.
    json_check = CheckConstraint(
        "json_valid(payload_json)",
        name="payload_json_valid",
    ).ddl_if(dialect="sqlite")
    kg_content_revision.append_constraint(json_check)

    prj_project = Table(
        "prj_project",
        metadata,
        Column("project_id", DomainUUID(), primary_key=True),
        Column("name", Text, nullable=False),
        sqlite_strict=True,
    )

    Table(
        "prj_knowledge_reference",
        metadata,
        Column(
            "project_id",
            DomainUUID(),
            ForeignKey("prj_project.project_id", ondelete="CASCADE"),
            primary_key=True,
        ),
        Column(
            "revision_id",
            DomainUUID(),
            ForeignKey("kg_content_revision.revision_id"),
            primary_key=True,
        ),
        Column("influence_type", Text, nullable=False, primary_key=True),
        sqlite_strict=True,
    )

    Table(
        "tooling_migration_probe",
        metadata,
        Column("probe_id", DomainUUID(), primary_key=True),
        Column("payload", Text, nullable=False),
        CheckConstraint("length(payload) > 0", name="payload_nonempty"),
        sqlite_strict=True,
    )

    # FTS5 remains explicitly SQLite-adapter DDL. PostgreSQL receives no such
    # object and is expected to use another LexicalIndex implementation.
    event.listen(
        metadata,
        "after_create",
        DDL(
            "CREATE VIRTUAL TABLE idx_knowledge_fts "
            "USING fts5(asset_id UNINDEXED, title, body)"
        ).execute_if(dialect="sqlite"),
    )

    return metadata


def configure_engine(url: str) -> Engine:
    engine = create_engine(url)

    if engine.dialect.name == "sqlite":

        @event.listens_for(engine, "connect")
        def set_sqlite_connection_contract(dbapi_connection, _connection_record):
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("PRAGMA busy_timeout = 5000")
            cursor.close()

        with engine.connect() as connection:
            connection.exec_driver_sql("PRAGMA journal_mode = WAL")
            connection.exec_driver_sql("PRAGMA synchronous = FULL")

    return engine


def assert_sqlite_contract(engine: Engine) -> None:
    with engine.connect() as connection:
        assert connection.exec_driver_sql("PRAGMA foreign_keys").scalar_one() == 1
        sql = connection.exec_driver_sql(
            "SELECT sql FROM sqlite_master WHERE type='table' AND name='kg_node'"
        ).scalar_one()
        assert "STRICT" in sql.upper()

        migration_sql = connection.exec_driver_sql(
            "SELECT sql FROM sqlite_master "
            "WHERE type='table' AND name='tooling_migration_probe'"
        ).scalar_one()
        assert "STRICT" in migration_sql.upper()
        assert "payload_nonempty" in migration_sql

        fts_exists = connection.exec_driver_sql(
            "SELECT COUNT(*) FROM sqlite_master "
            "WHERE type='table' AND name='idx_knowledge_fts'"
        ).scalar_one()
        assert fts_exists == 1


def exercise_core(engine: Engine, metadata: MetaData) -> None:
    kg_node = metadata.tables["kg_node"]
    kg_asset = metadata.tables["kg_asset"]
    kg_revision = metadata.tables["kg_content_revision"]
    project = metadata.tables["prj_project"]
    knowledge_ref = metadata.tables["prj_knowledge_reference"]
    probe = metadata.tables["tooling_migration_probe"]

    asset_id = new_id()
    revision_id = new_id()
    project_id = new_id()
    probe_id = new_id()

    with engine.begin() as connection:
        connection.execute(
            kg_node.insert().values(node_id=asset_id, node_type="ASSET")
        )
        connection.execute(
            kg_asset.insert().values(asset_id=asset_id, stable_key="random-forest")
        )
        connection.execute(
            kg_revision.insert().values(
                revision_id=revision_id,
                node_id=asset_id,
                revision_no=1,
                payload_json='{"title":"Random Forest"}',
            )
        )
        connection.execute(
            project.insert().values(project_id=project_id, name="Tooling spike")
        )
        connection.execute(
            knowledge_ref.insert().values(
                project_id=project_id,
                revision_id=revision_id,
                influence_type="INFORMED",
            )
        )
        connection.execute(
            probe.insert().values(probe_id=probe_id, payload="preserve-me")
        )

    with engine.connect() as connection:
        row = connection.execute(
            select(kg_asset.c.asset_id, kg_asset.c.stable_key)
        ).one()
        assert row.asset_id == asset_id
        assert row.stable_key == "random-forest"

        if engine.dialect.name == "sqlite":
            raw_id = connection.exec_driver_sql(
                "SELECT asset_id FROM kg_asset WHERE stable_key='random-forest'"
            ).scalar_one()
            assert raw_id == asset_id
            assert len(raw_id) == 36 and raw_id.count("-") == 4

            connection.exec_driver_sql(
                "INSERT INTO idx_knowledge_fts(asset_id,title,body) VALUES (?,?,?)",
                (asset_id, "Random Forest", "tree ensemble bagging variance"),
            )
            hit = connection.exec_driver_sql(
                "SELECT asset_id FROM idx_knowledge_fts "
                "WHERE idx_knowledge_fts MATCH 'bagging'"
            ).scalar_one()
            assert hit == asset_id

    try:
        with engine.begin() as connection:
            connection.execute(
                knowledge_ref.insert().values(
                    project_id=project_id,
                    revision_id=new_id(),
                    influence_type="INVALID",
                )
            )
    except IntegrityError:
        pass
    else:
        raise AssertionError("Foreign-key enforcement did not reject invalid revision")

    rollback_key = "must-rollback"
    try:
        with engine.begin() as connection:
            rollback_id = new_id()
            connection.execute(
                kg_node.insert().values(node_id=rollback_id, node_type="ASSET")
            )
            connection.execute(
                kg_asset.insert().values(
                    asset_id=rollback_id,
                    stable_key=rollback_key,
                )
            )
            raise RuntimeError("injected failure")
    except RuntimeError:
        pass

    with engine.connect() as connection:
        count = connection.execute(
            select(kg_asset.c.asset_id).where(kg_asset.c.stable_key == rollback_key)
        ).all()
        assert count == []


def run_alembic_migration(engine: Engine) -> None:
    with engine.begin() as connection:
        context = MigrationContext.configure(connection)
        op = Operations(context)

        if connection.dialect.name == "sqlite":
            with op.batch_alter_table(
                "tooling_migration_probe",
                recreate="always",
                naming_convention=NAMING_CONVENTION,
                table_kwargs={"sqlite_strict": True},
            ) as batch_op:
                batch_op.add_column(Column("note", Text, nullable=True))
        else:
            with op.batch_alter_table(
                "tooling_migration_probe",
                naming_convention=NAMING_CONVENTION,
            ) as batch_op:
                batch_op.add_column(Column("note", Text, nullable=True))

    inspector = inspect(engine)
    column_names = {column["name"] for column in inspector.get_columns("tooling_migration_probe")}
    assert "note" in column_names

    with engine.connect() as connection:
        preserved = connection.exec_driver_sql(
            "SELECT payload FROM tooling_migration_probe"
        ).scalar_one()
        assert preserved == "preserve-me"

        if engine.dialect.name == "sqlite":
            sql = connection.exec_driver_sql(
                "SELECT sql FROM sqlite_master "
                "WHERE type='table' AND name='tooling_migration_probe'"
            ).scalar_one()
            assert "STRICT" in sql.upper()
            assert "payload_nonempty" in sql

    try:
        with engine.begin() as connection:
            connection.exec_driver_sql(
                "INSERT INTO tooling_migration_probe(probe_id,payload,note) "
                "VALUES (:id,'','bad')",
                {"id": new_id()},
            )
    except Exception:
        pass
    else:
        raise AssertionError("Named CHECK constraint was lost during migration")


def assert_postgres_contract(engine: Engine) -> None:
    inspector = inspect(engine)
    assert not inspector.has_table("idx_knowledge_fts")

    with engine.connect() as connection:
        data_type = connection.execute(
            text(
                "SELECT data_type FROM information_schema.columns "
                "WHERE table_schema=current_schema() "
                "AND table_name='kg_node' AND column_name='node_id'"
            )
        ).scalar_one()
        assert data_type == "uuid"


def run(url: str) -> None:
    metadata = build_metadata()
    engine = configure_engine(url)

    try:
        metadata.drop_all(engine, checkfirst=True)
        if engine.dialect.name == "sqlite":
            with engine.begin() as connection:
                connection.exec_driver_sql("DROP TABLE IF EXISTS idx_knowledge_fts")

        metadata.create_all(engine)
        if engine.dialect.name == "sqlite":
            assert_sqlite_contract(engine)
        else:
            assert_postgres_contract(engine)

        exercise_core(engine, metadata)
        run_alembic_migration(engine)

        print(f"TOOLING_BACKEND={engine.dialect.name}")
        print("SQLALCHEMY_CORE=PASS")
        print("ALEMBIC_MIGRATION=PASS")
        print("PORTABLE_UUID=PASS")
        print("TRANSACTION_BOUNDARY=PASS")
        print("DIALECT_SPECIFIC_DDL_ISOLATION=PASS")
        print("TOOLING_SPIKE_RESULT=PASS")
    finally:
        if engine.dialect.name == "sqlite":
            with engine.begin() as connection:
                connection.exec_driver_sql("DROP TABLE IF EXISTS idx_knowledge_fts")
        metadata.drop_all(engine, checkfirst=True)
        engine.dispose()


def main() -> None:
    configured_url = os.environ.get("ADS_TOOLING_DB_URL")
    if configured_url:
        run(configured_url)
        return

    with tempfile.TemporaryDirectory(prefix="ads-tooling-spike-") as tmp:
        db_path = Path(tmp) / "tooling.db"
        run(f"sqlite:///{db_path.as_posix()}")


if __name__ == "__main__":
    main()
