"""Relational sidecar schema for reusable-knowledge interchange semantics.

The first production persistence slice intentionally kept the authoritative core
small. Specification 004 adds richer reusable-knowledge interchange fields. This
module extends the same SQLAlchemy ``MetaData`` with tables for structured
revision metadata, provenance, relation governance, and navigation collections
without duplicating stable identity or core revision columns.
"""

from __future__ import annotations

from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    Integer,
    Table,
    Text,
)

from ads_system.infrastructure.persistence.schema import metadata
from ads_system.infrastructure.persistence.types import DomainUUID


def _json_check(expression: str, name: str) -> CheckConstraint:
    """Return an SQLite-only JSON validity constraint."""

    return CheckConstraint(expression, name=name).ddl_if(dialect="sqlite")


kg_content_revision_extension = Table(
    "kg_content_revision_extension",
    metadata,
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("schema_version", Integer, nullable=False, server_default="1"),
    Column("structured_json", Text, nullable=False),
    CheckConstraint("schema_version >= 1", name="schema_version_positive"),
    _json_check("json_valid(structured_json)", "structured_json_valid"),
    sqlite_strict=True,
)

kg_provenance_source = Table(
    "kg_provenance_source",
    metadata,
    Column("source_id", Text, primary_key=True),
    Column("source_type", Text, nullable=False),
    Column("title", Text, nullable=False),
    Column("locator", Text, nullable=False),
    Column("version_or_fingerprint", Text, nullable=True),
    Column("notes", Text, nullable=True),
    sqlite_strict=True,
)

kg_content_revision_provenance = Table(
    "kg_content_revision_provenance",
    metadata,
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "source_id",
        Text,
        ForeignKey("kg_provenance_source.source_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sqlite_strict=True,
)

kg_rule_provenance = Table(
    "kg_rule_provenance",
    metadata,
    Column(
        "rule_spec_id",
        DomainUUID(),
        ForeignKey("kg_rule_spec.rule_spec_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "source_id",
        Text,
        ForeignKey("kg_provenance_source.source_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sqlite_strict=True,
)

kg_relation_revision_state = Table(
    "kg_relation_revision_state",
    metadata,
    Column(
        "relation_revision_id",
        DomainUUID(),
        ForeignKey("kg_relation_revision.relation_revision_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("governance_status", Text, nullable=False),
    Column("semantic_content_hash", Text, nullable=False),
    Column("updated_at", Text, nullable=False),
    CheckConstraint(
        "governance_status IN ('CANDIDATE','REVIEWED','ACCEPTED','SUPERSEDED','REJECTED')",
        name="relation_governance_status_allowed",
    ),
    sqlite_strict=True,
)

kg_relation_governance_event = Table(
    "kg_relation_governance_event",
    metadata,
    Column("event_id", DomainUUID(), primary_key=True),
    Column(
        "relation_revision_id",
        DomainUUID(),
        ForeignKey("kg_relation_revision.relation_revision_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("from_status", Text, nullable=True),
    Column("to_status", Text, nullable=False),
    Column("actor", Text, nullable=False),
    Column("occurred_at", Text, nullable=False),
    Column("note_text", Text, nullable=True),
    sqlite_strict=True,
)

kg_relation_revision_provenance = Table(
    "kg_relation_revision_provenance",
    metadata,
    Column(
        "relation_revision_id",
        DomainUUID(),
        ForeignKey("kg_relation_revision.relation_revision_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "source_id",
        Text,
        ForeignKey("kg_provenance_source.source_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sqlite_strict=True,
)

kg_collection = Table(
    "kg_collection",
    metadata,
    Column("collection_key", Text, primary_key=True),
    Column("title", Text, nullable=False),
    sqlite_strict=True,
)

kg_collection_member = Table(
    "kg_collection_member",
    metadata,
    Column(
        "collection_key",
        Text,
        ForeignKey("kg_collection.collection_key", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "node_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    sqlite_strict=True,
)
