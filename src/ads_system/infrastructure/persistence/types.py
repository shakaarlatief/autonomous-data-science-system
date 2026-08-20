"""Portable SQLAlchemy types and serialization helpers for V1 persistence."""

from __future__ import annotations

import hashlib
import json
import uuid
from datetime import UTC, datetime
from typing import Any

from sqlalchemy import Text
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.types import TypeDecorator


class DomainUUID(TypeDecorator[str]):
    """Persist UUIDs according to Specification 001's portability contract.

    SQLite stores canonical lowercase hyphenated UUID text. PostgreSQL uses its
    native UUID type. The application-facing representation remains ``str`` so
    storage-driver return types do not escape the persistence adapter.
    """

    impl = Text
    cache_ok = True

    def load_dialect_impl(self, dialect):
        if dialect.name == "postgresql":
            return dialect.type_descriptor(PostgreSQLUUID(as_uuid=False))
        return dialect.type_descriptor(Text())

    def process_bind_param(self, value: str | uuid.UUID | None, dialect) -> str | None:
        if value is None:
            return None
        return str(uuid.UUID(str(value))).lower()

    def process_result_value(self, value: Any, dialect) -> str | None:
        if value is None:
            return None
        return str(value).lower()


def new_id() -> str:
    """Return a storage-neutral durable ID.

    UUIDv7 remains preferred by Specification 001, but the physical schema and
    application contracts intentionally accept any RFC 9562 UUID. The first V1
    slice uses UUIDv4 until a UUIDv7 generator is selected independently.
    """

    return str(uuid.uuid4())


def utc_now_text() -> str:
    """Return a fixed-format UTC timestamp suitable for SQLite TEXT storage."""

    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def canonical_json(value: Any) -> str:
    """Serialize JSON deterministically for hashing and persisted rule payloads."""

    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def semantic_hash(value: Any) -> str:
    """Return a SHA-256 hash over deterministic semantic JSON."""

    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
