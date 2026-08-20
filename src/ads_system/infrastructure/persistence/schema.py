"""SQLAlchemy Core schema for the first production V1 persistence slice."""

from __future__ import annotations

from sqlalchemy import (
    CheckConstraint,
    Column,
    ForeignKey,
    ForeignKeyConstraint,
    Index,
    Integer,
    MetaData,
    Table,
    Text,
    UniqueConstraint,
)

from ads_system.infrastructure.persistence.types import DomainUUID

NAMING_CONVENTION = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)


def _json_check(expression: str, name: str) -> CheckConstraint:
    """Return an SQLite-only JSON-validity strengthening constraint."""

    return CheckConstraint(expression, name=name).ddl_if(dialect="sqlite")


kg_node = Table(
    "kg_node",
    metadata,
    Column("node_id", DomainUUID(), primary_key=True),
    Column("node_type", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    CheckConstraint(
        "node_type IN ('ASSET','COMPONENT')",
        name="node_type_allowed",
    ),
    sqlite_strict=True,
)

kg_content_revision = Table(
    "kg_content_revision",
    metadata,
    Column("revision_id", DomainUUID(), primary_key=True),
    Column(
        "node_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("revision_no", Integer, nullable=False),
    Column("created_at", Text, nullable=False),
    Column("semantic_content_hash", Text, nullable=False),
    CheckConstraint("revision_no >= 1", name="revision_no_positive"),
    UniqueConstraint("node_id", "revision_no", name="node_revision_no"),
    UniqueConstraint("node_id", "revision_id", name="node_revision_identity"),
    sqlite_strict=True,
)

kg_asset = Table(
    "kg_asset",
    metadata,
    Column(
        "asset_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    Column("stable_key", Text, nullable=False),
    Column("current_accepted_revision_id", DomainUUID(), nullable=True),
    Column("created_at", Text, nullable=False),
    UniqueConstraint("stable_key", name="stable_key"),
    ForeignKeyConstraint(
        ["asset_id", "current_accepted_revision_id"],
        ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
        name="asset_current_revision",
        deferrable=True,
        initially="DEFERRED",
    ),
    sqlite_strict=True,
)

kg_revision_governance = Table(
    "kg_revision_governance",
    metadata,
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    Column("current_status", Text, nullable=False),
    Column("updated_at", Text, nullable=False),
    CheckConstraint(
        "current_status IN ('CANDIDATE','REVIEWED','ACCEPTED','SUPERSEDED','REJECTED')",
        name="governance_status_allowed",
    ),
    sqlite_strict=True,
)

kg_governance_event = Table(
    "kg_governance_event",
    metadata,
    Column("event_id", DomainUUID(), primary_key=True),
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("from_status", Text, nullable=True),
    Column("to_status", Text, nullable=False),
    Column("actor", Text, nullable=False),
    Column("occurred_at", Text, nullable=False),
    Column("note_text", Text, nullable=True),
    sqlite_strict=True,
)

kg_asset_revision = Table(
    "kg_asset_revision",
    metadata,
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    Column(
        "asset_id",
        DomainUUID(),
        ForeignKey("kg_asset.asset_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("intrinsic_kind", Text, nullable=False),
    Column("title", Text, nullable=False),
    Column("purpose", Text, nullable=False),
    Column("scope_text", Text, nullable=True),
    Column("limitations_text", Text, nullable=True),
    ForeignKeyConstraint(
        ["asset_id", "revision_id"],
        ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
        name="asset_revision_envelope",
    ),
    UniqueConstraint("revision_id", "asset_id", name="asset_revision_identity"),
    sqlite_strict=True,
)

kg_component = Table(
    "kg_component",
    metadata,
    Column(
        "component_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    Column(
        "parent_asset_id",
        DomainUUID(),
        ForeignKey("kg_asset.asset_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("component_key", Text, nullable=False),
    Column("component_kind", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    UniqueConstraint("parent_asset_id", "component_key", name="parent_component_key"),
    UniqueConstraint("component_id", "parent_asset_id", name="component_parent_identity"),
    sqlite_strict=True,
)

kg_component_revision = Table(
    "kg_component_revision",
    metadata,
    Column(
        "revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        primary_key=True,
    ),
    Column("component_id", DomainUUID(), nullable=False),
    Column("parent_asset_id", DomainUUID(), nullable=False),
    Column("parent_asset_revision_id", DomainUUID(), nullable=False),
    Column("body_text", Text, nullable=True),
    Column("payload_json", Text, nullable=True),
    Column("position", Integer, nullable=False, server_default="0"),
    ForeignKeyConstraint(
        ["component_id", "revision_id"],
        ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
        name="component_revision_envelope",
    ),
    ForeignKeyConstraint(
        ["component_id", "parent_asset_id"],
        ["kg_component.component_id", "kg_component.parent_asset_id"],
        name="component_parent",
    ),
    ForeignKeyConstraint(
        ["parent_asset_revision_id", "parent_asset_id"],
        ["kg_asset_revision.revision_id", "kg_asset_revision.asset_id"],
        name="component_parent_asset_revision",
    ),
    _json_check(
        "payload_json IS NULL OR json_valid(payload_json)",
        "component_payload_json_valid",
    ),
    sqlite_strict=True,
)

kg_relation = Table(
    "kg_relation",
    metadata,
    Column("relation_id", DomainUUID(), primary_key=True),
    Column(
        "source_node_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column(
        "target_node_id",
        DomainUUID(),
        ForeignKey("kg_node.node_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("relation_type", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    sqlite_strict=True,
)

Index("ix_kg_relation_source_type", kg_relation.c.source_node_id, kg_relation.c.relation_type)
Index("ix_kg_relation_target_type", kg_relation.c.target_node_id, kg_relation.c.relation_type)

kg_relation_revision = Table(
    "kg_relation_revision",
    metadata,
    Column("relation_revision_id", DomainUUID(), primary_key=True),
    Column(
        "relation_id",
        DomainUUID(),
        ForeignKey("kg_relation.relation_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("revision_no", Integer, nullable=False),
    Column("scope_text", Text, nullable=True),
    Column("rationale_text", Text, nullable=True),
    Column("created_at", Text, nullable=False),
    CheckConstraint("revision_no >= 1", name="relation_revision_no_positive"),
    UniqueConstraint("relation_id", "revision_no", name="relation_revision_no"),
    UniqueConstraint(
        "relation_id",
        "relation_revision_id",
        name="relation_revision_identity",
    ),
    sqlite_strict=True,
)

kg_relation_current = Table(
    "kg_relation_current",
    metadata,
    Column(
        "relation_id",
        DomainUUID(),
        ForeignKey("kg_relation.relation_id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column("relation_revision_id", DomainUUID(), nullable=False),
    ForeignKeyConstraint(
        ["relation_id", "relation_revision_id"],
        ["kg_relation_revision.relation_id", "kg_relation_revision.relation_revision_id"],
        name="relation_current_revision",
        deferrable=True,
        initially="DEFERRED",
    ),
    sqlite_strict=True,
)

kg_rule_spec = Table(
    "kg_rule_spec",
    metadata,
    Column("rule_spec_id", DomainUUID(), primary_key=True),
    Column(
        "owner_content_revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("rule_key", Text, nullable=False),
    Column("condition_json", Text, nullable=False),
    Column("consequence_type", Text, nullable=False),
    Column("consequence_payload_json", Text, nullable=True),
    Column("force", Text, nullable=False),
    Column("unknown_behavior", Text, nullable=False),
    Column("rationale_text", Text, nullable=True),
    UniqueConstraint("owner_content_revision_id", "rule_key", name="owner_rule_key"),
    CheckConstraint(
        "force IN ('HARD','STRONG','HEURISTIC','INFORMATIONAL')",
        name="rule_force_allowed",
    ),
    CheckConstraint(
        "unknown_behavior IN ('ASK','DEFER','BLOCK_DEPENDENT','NO_INFERENCE')",
        name="rule_unknown_behavior_allowed",
    ),
    _json_check("json_valid(condition_json)", "rule_condition_json_valid"),
    _json_check(
        "consequence_payload_json IS NULL OR json_valid(consequence_payload_json)",
        "rule_consequence_json_valid",
    ),
    sqlite_strict=True,
)

prj_project = Table(
    "prj_project",
    metadata,
    Column("project_id", DomainUUID(), primary_key=True),
    Column("title", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    sqlite_strict=True,
)

prj_entity = Table(
    "prj_entity",
    metadata,
    Column("entity_id", DomainUUID(), primary_key=True),
    Column(
        "project_id",
        DomainUUID(),
        ForeignKey("prj_project.project_id", ondelete="CASCADE"),
        nullable=False,
    ),
    Column("entity_type", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    UniqueConstraint("entity_id", "project_id", name="entity_project_identity"),
    sqlite_strict=True,
)

prj_finding = Table(
    "prj_finding",
    metadata,
    Column("finding_id", DomainUUID(), primary_key=True),
    Column("project_id", DomainUUID(), nullable=False),
    Column("finding_type", Text, nullable=False),
    Column("statement_text", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    ForeignKeyConstraint(
        ["finding_id", "project_id"],
        ["prj_entity.entity_id", "prj_entity.project_id"],
        name="finding_entity",
        ondelete="RESTRICT",
    ),
    sqlite_strict=True,
)

prj_knowledge_ref = Table(
    "prj_knowledge_ref",
    metadata,
    Column("ref_id", DomainUUID(), primary_key=True),
    Column("project_entity_id", DomainUUID(), nullable=False),
    Column("project_id", DomainUUID(), nullable=False),
    Column(
        "knowledge_revision_id",
        DomainUUID(),
        ForeignKey("kg_content_revision.revision_id", ondelete="RESTRICT"),
        nullable=False,
    ),
    Column("reference_type", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    ForeignKeyConstraint(
        ["project_entity_id", "project_id"],
        ["prj_entity.entity_id", "prj_entity.project_id"],
        name="knowledge_ref_project_entity",
        ondelete="RESTRICT",
    ),
    UniqueConstraint(
        "project_entity_id",
        "knowledge_revision_id",
        "reference_type",
        name="project_entity_knowledge_reference",
    ),
    sqlite_strict=True,
)
