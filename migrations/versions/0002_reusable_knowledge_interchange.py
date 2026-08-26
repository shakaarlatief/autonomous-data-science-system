"""Add reusable-knowledge interchange persistence support.

Revision ID: 0002_knowledge_interchange
Revises: 0001_v1_persistence_core
Create Date: 2026-08-20
"""

from __future__ import annotations

import hashlib
import json
import uuid

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0002_knowledge_interchange"
down_revision = "0001_v1_persistence_core"
branch_labels = None
depends_on = None


def _uuid_type() -> sa.TypeEngine:
    if op.get_bind().dialect.name == "postgresql":
        return postgresql.UUID(as_uuid=False)
    return sa.Text()


def _strict_kwargs() -> dict[str, object]:
    return {"sqlite_strict": True}


def _json_constraints(*pairs: tuple[str, str]) -> list[sa.CheckConstraint]:
    if op.get_bind().dialect.name != "sqlite":
        return []
    return [sa.CheckConstraint(expression, name=name) for expression, name in pairs]


def _relation_digest(row: sa.RowMapping) -> str:
    semantic = {
        "relation_type": row["relation_type"],
        "source_node_id": str(row["source_node_id"]),
        "target_node_id": str(row["target_node_id"]),
        "scope": row["scope_text"],
        "rationale": row["rationale_text"],
    }
    canonical = json.dumps(
        semantic,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _backfill_relation_governance() -> None:
    """Preserve the implicit accepted-current meaning of migration 0001 relations."""

    bind = op.get_bind()
    rows = bind.execute(
        sa.text(
            """
            SELECT
                rr.relation_revision_id,
                rr.relation_id,
                rr.scope_text,
                rr.rationale_text,
                rr.created_at,
                r.source_node_id,
                r.target_node_id,
                r.relation_type,
                rc.relation_revision_id AS current_revision_id
            FROM kg_relation_revision AS rr
            JOIN kg_relation AS r
              ON r.relation_id = rr.relation_id
            LEFT JOIN kg_relation_current AS rc
              ON rc.relation_id = rr.relation_id
            """
        )
    ).mappings().all()

    for row in rows:
        relation_revision_id = str(row["relation_revision_id"])
        current_revision_id = (
            str(row["current_revision_id"])
            if row["current_revision_id"] is not None
            else None
        )
        status = (
            "ACCEPTED"
            if current_revision_id == relation_revision_id
            else "SUPERSEDED"
        )
        bind.execute(
            sa.text(
                """
                INSERT INTO kg_relation_revision_state
                    (relation_revision_id, governance_status, semantic_content_hash, updated_at)
                VALUES
                    (:relation_revision_id, :status, :semantic_hash, :updated_at)
                """
            ),
            {
                "relation_revision_id": relation_revision_id,
                "status": status,
                "semantic_hash": _relation_digest(row),
                "updated_at": row["created_at"],
            },
        )
        bind.execute(
            sa.text(
                """
                INSERT INTO kg_relation_governance_event
                    (event_id, relation_revision_id, from_status, to_status, actor, occurred_at, note_text)
                VALUES
                    (:event_id, :relation_revision_id, NULL, :status, :actor, :occurred_at, :note_text)
                """
            ),
            {
                "event_id": str(uuid.uuid4()),
                "relation_revision_id": relation_revision_id,
                "status": status,
                "actor": "migration-0002",
                "occurred_at": row["created_at"],
                "note_text": "Backfilled governance from migration 0001 current-relation semantics",
            },
        )


def upgrade() -> None:
    uuid_type = _uuid_type()

    op.create_table(
        "kg_content_revision_extension",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("schema_version", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("structured_json", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["revision_id"],
            ["kg_content_revision.revision_id"],
            name="fk_kg_rev_ext_revision",
            ondelete="CASCADE",
        ),
        sa.CheckConstraint(
            "schema_version >= 1",
            name="ck_kg_rev_ext_schema_version",
        ),
        *_json_constraints(
            (
                "json_valid(structured_json)",
                "ck_kg_rev_ext_json_valid",
            )
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_provenance_source",
        sa.Column("source_id", sa.Text(), primary_key=True),
        sa.Column("source_type", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("locator", sa.Text(), nullable=False),
        sa.Column("version_or_fingerprint", sa.Text(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_content_revision_provenance",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("source_id", sa.Text(), primary_key=True),
        sa.ForeignKeyConstraint(
            ["revision_id"],
            ["kg_content_revision.revision_id"],
            name="fk_kg_rev_prov_revision",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["kg_provenance_source.source_id"],
            name="fk_kg_rev_prov_source",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_rule_provenance",
        sa.Column("rule_spec_id", uuid_type, primary_key=True),
        sa.Column("source_id", sa.Text(), primary_key=True),
        sa.ForeignKeyConstraint(
            ["rule_spec_id"],
            ["kg_rule_spec.rule_spec_id"],
            name="fk_kg_rule_prov_rule",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["kg_provenance_source.source_id"],
            name="fk_kg_rule_prov_source",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_relation_revision_state",
        sa.Column("relation_revision_id", uuid_type, primary_key=True),
        sa.Column("governance_status", sa.Text(), nullable=False),
        sa.Column("semantic_content_hash", sa.Text(), nullable=False),
        sa.Column("updated_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["relation_revision_id"],
            ["kg_relation_revision.relation_revision_id"],
            name="fk_kg_rel_state_revision",
            ondelete="CASCADE",
        ),
        sa.CheckConstraint(
            "governance_status IN ('CANDIDATE','REVIEWED','ACCEPTED','SUPERSEDED','REJECTED')",
            name="ck_kg_rel_state_status",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_relation_governance_event",
        sa.Column("event_id", uuid_type, primary_key=True),
        sa.Column("relation_revision_id", uuid_type, nullable=False),
        sa.Column("from_status", sa.Text(), nullable=True),
        sa.Column("to_status", sa.Text(), nullable=False),
        sa.Column("actor", sa.Text(), nullable=False),
        sa.Column("occurred_at", sa.Text(), nullable=False),
        sa.Column("note_text", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["relation_revision_id"],
            ["kg_relation_revision.relation_revision_id"],
            name="fk_kg_rel_event_revision",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_relation_revision_provenance",
        sa.Column("relation_revision_id", uuid_type, primary_key=True),
        sa.Column("source_id", sa.Text(), primary_key=True),
        sa.ForeignKeyConstraint(
            ["relation_revision_id"],
            ["kg_relation_revision.relation_revision_id"],
            name="fk_kg_rel_prov_revision",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["source_id"],
            ["kg_provenance_source.source_id"],
            name="fk_kg_rel_prov_source",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_collection",
        sa.Column("collection_key", sa.Text(), primary_key=True),
        sa.Column("title", sa.Text(), nullable=False),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_collection_member",
        sa.Column("collection_key", sa.Text(), primary_key=True),
        sa.Column("node_id", uuid_type, primary_key=True),
        sa.ForeignKeyConstraint(
            ["collection_key"],
            ["kg_collection.collection_key"],
            name="fk_kg_coll_member_collection",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["node_id"],
            ["kg_node.node_id"],
            name="fk_kg_coll_member_node",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    _backfill_relation_governance()


def downgrade() -> None:
    op.drop_table("kg_collection_member")
    op.drop_table("kg_collection")
    op.drop_table("kg_relation_revision_provenance")
    op.drop_table("kg_relation_governance_event")
    op.drop_table("kg_relation_revision_state")
    op.drop_table("kg_rule_provenance")
    op.drop_table("kg_content_revision_provenance")
    op.drop_table("kg_provenance_source")
    op.drop_table("kg_content_revision_extension")