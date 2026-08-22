"""SQLAlchemy UnitOfWork adapter for controlled V1 transactions."""

from __future__ import annotations

from types import TracebackType
from typing import Self

from sqlalchemy import Connection, Engine

from ads_system.infrastructure.persistence.interchange_repository import (
    SqlAlchemyKnowledgeInterchangeRepository,
)
from ads_system.infrastructure.persistence.navigation_repository import (
    SqlAlchemyKnowledgeNavigationRepository,
)
from ads_system.infrastructure.persistence.repositories import (
    SqlAlchemyKnowledgeRepository,
    SqlAlchemyProjectRepository,
)


class SqlAlchemyUnitOfWork:
    """Own one short application transaction and its repository adapters."""

    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._connection: Connection | None = None
        self._transaction = None
        self._committed = False
        self.knowledge: SqlAlchemyKnowledgeRepository
        self.navigation: SqlAlchemyKnowledgeNavigationRepository
        self.interchange: SqlAlchemyKnowledgeInterchangeRepository
        self.projects: SqlAlchemyProjectRepository

    def __enter__(self) -> Self:
        self._connection = self._engine.connect()
        self._transaction = self._connection.begin()
        self._committed = False
        self.knowledge = SqlAlchemyKnowledgeRepository(self._connection)
        self.navigation = SqlAlchemyKnowledgeNavigationRepository(self._connection)
        self.interchange = SqlAlchemyKnowledgeInterchangeRepository(self._connection)
        self.projects = SqlAlchemyProjectRepository(self._connection)
        return self

    def commit(self) -> None:
        if self._transaction is None:
            raise RuntimeError("UnitOfWork is not active")
        self._transaction.commit()
        self._committed = True

    def rollback(self) -> None:
        if self._transaction is not None and self._transaction.is_active:
            self._transaction.rollback()

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        try:
            if exc_type is not None or not self._committed:
                self.rollback()
        finally:
            if self._connection is not None:
                self._connection.close()
            self._connection = None
            self._transaction = None
