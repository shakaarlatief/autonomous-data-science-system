"""Database-engine factories implementing Specification 001's connection contract."""

from __future__ import annotations

from pathlib import Path

from sqlalchemy import Engine, create_engine, event


def create_operational_engine(database_url: str, *, echo: bool = False) -> Engine:
    """Create an operational SQLAlchemy engine behind the V1 persistence ports.

    SQLite-specific operational policy is installed here so domain/application
    code never needs to know about PRAGMAs. PostgreSQL and later adapters pass
    through the same factory contract without receiving SQLite behavior.
    """

    engine = create_engine(database_url, echo=echo)

    if engine.dialect.name == "sqlite":

        @event.listens_for(engine, "connect")
        def _configure_sqlite_connection(dbapi_connection, _connection_record) -> None:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute("PRAGMA busy_timeout = 5000")
            cursor.close()

        with engine.connect() as connection:
            connection.exec_driver_sql("PRAGMA journal_mode = WAL")
            connection.exec_driver_sql("PRAGMA synchronous = FULL")

    return engine


def sqlite_database_url(path: str | Path) -> str:
    """Return a portable SQLAlchemy SQLite URL for a filesystem database."""

    resolved = Path(path).resolve().as_posix()
    return f"sqlite+pysqlite:///{resolved}"
