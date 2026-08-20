"""Create the first production V1 persistence core.

Revision ID: 0001_v1_persistence_core
Revises: None
Create Date: 2026-08-20
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0001_v1_persistence_core"
down_revision = None
branch_labels = None
depends_on = None


def _uuid_type() -> sa.TypeEngine:
    if op.get_bind().dialect.name == "postgresql":
        return postgresql.UUID(as_uuid=False)
    return sa.Text()


def _strict_kwargs() -> dict[str, object]:
    return {"sqlite_strict": True}


def upgrade() -> None:
    uuid_type = _uuid_type()

    op.create_table(
        "kg_node",
        sa.Column("node_id", uuid_type, primary_key=True),
        sa.Column("node_type", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.CheckConstraint(
            "node_type IN ('ASSET','COMPONENT')",
            name="ck_kg_node_node_type_allowed",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_content_revision",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("node_id", uuid_type, nullable=False),
        sa.Column("revision_no", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.Column("semantic_content_hash", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["node_id"], ["kg_node.node_id"],
            name="fk_kg_content_revision_node_id_kg_node",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "revision_no >= 1",
            name="ck_kg_content_revision_revision_no_positive",
        ),
        sa.UniqueConstraint(
            "node_id", "revision_no",
            name="uq_kg_content_revision_node_revision_no",
        ),
        sa.UniqueConstraint(
            "node_id", "revision_id",
            name="uq_kg_content_revision_node_revision_identity",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_asset",
        sa.Column("asset_id", uuid_type, primary_key=True),
        sa.Column("stable_key", sa.Text(), nullable=False),
        sa.Column("current_accepted_revision_id", uuid_type, nullable=True),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["asset_id"], ["kg_node.node_id"],
            name="fk_kg_asset_asset_id_kg_node",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id", "current_accepted_revision_id"],
            ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
            name="fk_kg_asset_asset_current_revision",
            deferrable=True,
            initially="DEFERRED",
        ),
        sa.UniqueConstraint("stable_key", name="uq_kg_asset_stable_key"),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_revision_governance",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("current_status", sa.Text(), nullable=False),
        sa.Column("updated_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["revision_id"], ["kg_content_revision.revision_id"],
            name="fk_kg_revision_governance_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "current_status IN ('CANDIDATE','REVIEWED','ACCEPTED','SUPERSEDED','REJECTED')",
            name="ck_kg_revision_governance_governance_status_allowed",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_governance_event",
        sa.Column("event_id", uuid_type, primary_key=True),
        sa.Column("revision_id", uuid_type, nullable=False),
        sa.Column("from_status", sa.Text(), nullable=True),
        sa.Column("to_status", sa.Text(), nullable=False),
        sa.Column("actor", sa.Text(), nullable=False),
        sa.Column("occurred_at", sa.Text(), nullable=False),
        sa.Column("note_text", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["revision_id"], ["kg_content_revision.revision_id"],
            name="fk_kg_governance_event_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_asset_revision",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("asset_id", uuid_type, nullable=False),
        sa.Column("intrinsic_kind", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("purpose", sa.Text(), nullable=False),
        sa.Column("scope_text", sa.Text(), nullable=True),
        sa.Column("limitations_text", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["revision_id"], ["kg_content_revision.revision_id"],
            name="fk_kg_asset_revision_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id"], ["kg_asset.asset_id"],
            name="fk_kg_asset_revision_asset_id_kg_asset",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["asset_id", "revision_id"],
            ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
            name="fk_kg_asset_revision_asset_revision_envelope",
        ),
        sa.UniqueConstraint(
            "revision_id", "asset_id",
            name="uq_kg_asset_revision_revision_asset_identity",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_component",
        sa.Column("component_id", uuid_type, primary_key=True),
        sa.Column("parent_asset_id", uuid_type, nullable=False),
        sa.Column("component_key", sa.Text(), nullable=False),
        sa.Column("component_kind", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["component_id"], ["kg_node.node_id"],
            name="fk_kg_component_component_id_kg_node",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["parent_asset_id"], ["kg_asset.asset_id"],
            name="fk_kg_component_parent_asset_id_kg_asset",
            ondelete="RESTRICT",
        ),
        sa.UniqueConstraint(
            "parent_asset_id", "component_key",
            name="uq_kg_component_parent_component_key",
        ),
        sa.UniqueConstraint(
            "component_id", "parent_asset_id",
            name="uq_kg_component_component_parent_identity",
        ),
        **_strict_kwargs(),
    )

    component_constraints: list[sa.SchemaItem] = [
        sa.ForeignKeyConstraint(
            ["revision_id"], ["kg_content_revision.revision_id"],
            name="fk_kg_component_revision_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["component_id", "revision_id"],
            ["kg_content_revision.node_id", "kg_content_revision.revision_id"],
            name="fk_kg_component_revision_component_revision_envelope",
        ),
        sa.ForeignKeyConstraint(
            ["component_id", "parent_asset_id"],
            ["kg_component.component_id", "kg_component.parent_asset_id"],
            name="fk_kg_component_revision_component_parent",
        ),
        sa.ForeignKeyConstraint(
            ["parent_asset_revision_id", "parent_asset_id"],
            ["kg_asset_revision.revision_id", "kg_asset_revision.asset_id"],
            name="fk_kg_component_revision_parent_asset_revision",
        ),
    ]
    if op.get_bind().dialect.name == "sqlite":
        component_constraints.append(
            sa.CheckConstraint(
                "payload_json IS NULL OR json_valid(payload_json)",
                name="ck_kg_component_revision_component_payload_json_valid",
            )
        )
    op.create_table(
        "kg_component_revision",
        sa.Column("revision_id", uuid_type, primary_key=True),
        sa.Column("component_id", uuid_type, nullable=False),
        sa.Column("parent_asset_id", uuid_type, nullable=False),
        sa.Column("parent_asset_revision_id", uuid_type, nullable=False),
        sa.Column("body_text", sa.Text(), nullable=True),
        sa.Column("payload_json", sa.Text(), nullable=True),
        sa.Column("position", sa.Integer(), nullable=False, server_default="0"),
        *component_constraints,
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_relation",
        sa.Column("relation_id", uuid_type, primary_key=True),
        sa.Column("source_node_id", uuid_type, nullable=False),
        sa.Column("target_node_id", uuid_type, nullable=False),
        sa.Column("relation_type", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["source_node_id"], ["kg_node.node_id"],
            name="fk_kg_relation_source_node_id_kg_node",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["target_node_id"], ["kg_node.node_id"],
            name="fk_kg_relation_target_node_id_kg_node",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )
    op.create_index(
        "ix_kg_relation_source_type",
        "kg_relation",
        ["source_node_id", "relation_type"],
    )
    op.create_index(
        "ix_kg_relation_target_type",
        "kg_relation",
        ["target_node_id", "relation_type"],
    )

    op.create_table(
        "kg_relation_revision",
        sa.Column("relation_revision_id", uuid_type, primary_key=True),
        sa.Column("relation_id", uuid_type, nullable=False),
        sa.Column("revision_no", sa.Integer(), nullable=False),
        sa.Column("scope_text", sa.Text(), nullable=True),
        sa.Column("rationale_text", sa.Text(), nullable=True),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["relation_id"], ["kg_relation.relation_id"],
            name="fk_kg_relation_revision_relation_id_kg_relation",
            ondelete="RESTRICT",
        ),
        sa.CheckConstraint(
            "revision_no >= 1",
            name="ck_kg_relation_revision_relation_revision_no_positive",
        ),
        sa.UniqueConstraint(
            "relation_id", "revision_no",
            name="uq_kg_relation_revision_relation_revision_no",
        ),
        sa.UniqueConstraint(
            "relation_id", "relation_revision_id",
            name="uq_kg_relation_revision_relation_revision_identity",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "kg_relation_current",
        sa.Column("relation_id", uuid_type, primary_key=True),
        sa.Column("relation_revision_id", uuid_type, nullable=False),
        sa.ForeignKeyConstraint(
            ["relation_id"], ["kg_relation.relation_id"],
            name="fk_kg_relation_current_relation_id_kg_relation",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["relation_id", "relation_revision_id"],
            ["kg_relation_revision.relation_id", "kg_relation_revision.relation_revision_id"],
            name="fk_kg_relation_current_relation_current_revision",
            deferrable=True,
            initially="DEFERRED",
        ),
        **_strict_kwargs(),
    )

    rule_constraints: list[sa.SchemaItem] = [
        sa.ForeignKeyConstraint(
            ["owner_content_revision_id"], ["kg_content_revision.revision_id"],
            name="fk_kg_rule_spec_owner_content_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        sa.UniqueConstraint(
            "owner_content_revision_id", "rule_key",
            name="uq_kg_rule_spec_owner_rule_key",
        ),
        sa.CheckConstraint(
            "force IN ('HARD','STRONG','HEURISTIC','INFORMATIONAL')",
            name="ck_kg_rule_spec_rule_force_allowed",
        ),
        sa.CheckConstraint(
            "unknown_behavior IN ('ASK','DEFER','BLOCK_DEPENDENT','NO_INFERENCE')",
            name="ck_kg_rule_spec_rule_unknown_behavior_allowed",
        ),
    ]
    if op.get_bind().dialect.name == "sqlite":
        rule_constraints.extend(
            [
                sa.CheckConstraint(
                    "json_valid(condition_json)",
                    name="ck_kg_rule_spec_rule_condition_json_valid",
                ),
                sa.CheckConstraint(
                    "consequence_payload_json IS NULL OR json_valid(consequence_payload_json)",
                    name="ck_kg_rule_spec_rule_consequence_json_valid",
                ),
            ]
        )
    op.create_table(
        "kg_rule_spec",
        sa.Column("rule_spec_id", uuid_type, primary_key=True),
        sa.Column("owner_content_revision_id", uuid_type, nullable=False),
        sa.Column("rule_key", sa.Text(), nullable=False),
        sa.Column("condition_json", sa.Text(), nullable=False),
        sa.Column("consequence_type", sa.Text(), nullable=False),
        sa.Column("consequence_payload_json", sa.Text(), nullable=True),
        sa.Column("force", sa.Text(), nullable=False),
        sa.Column("unknown_behavior", sa.Text(), nullable=False),
        sa.Column("rationale_text", sa.Text(), nullable=True),
        *rule_constraints,
        **_strict_kwargs(),
    )

    op.create_table(
        "prj_project",
        sa.Column("project_id", uuid_type, primary_key=True),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        **_strict_kwargs(),
    )

    op.create_table(
        "prj_entity",
        sa.Column("entity_id", uuid_type, primary_key=True),
        sa.Column("project_id", uuid_type, nullable=False),
        sa.Column("entity_type", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"], ["prj_project.project_id"],
            name="fk_prj_entity_project_id_prj_project",
            ondelete="CASCADE",
        ),
        sa.UniqueConstraint(
            "entity_id", "project_id",
            name="uq_prj_entity_entity_project_identity",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "prj_finding",
        sa.Column("finding_id", uuid_type, primary_key=True),
        sa.Column("project_id", uuid_type, nullable=False),
        sa.Column("finding_type", sa.Text(), nullable=False),
        sa.Column("statement_text", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["finding_id", "project_id"],
            ["prj_entity.entity_id", "prj_entity.project_id"],
            name="fk_prj_finding_finding_entity",
            ondelete="RESTRICT",
        ),
        **_strict_kwargs(),
    )

    op.create_table(
        "prj_knowledge_ref",
        sa.Column("ref_id", uuid_type, primary_key=True),
        sa.Column("project_entity_id", uuid_type, nullable=False),
        sa.Column("project_id", uuid_type, nullable=False),
        sa.Column("knowledge_revision_id", uuid_type, nullable=False),
        sa.Column("reference_type", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_entity_id", "project_id"],
            ["prj_entity.entity_id", "prj_entity.project_id"],
            name="fk_prj_knowledge_ref_project_entity",
            ondelete="RESTRICT",
        ),
        sa.ForeignKeyConstraint(
            ["knowledge_revision_id"], ["kg_content_revision.revision_id"],
            name="fk_prj_knowledge_ref_knowledge_revision_id_kg_content_revision",
            ondelete="RESTRICT",
        ),
        sa.UniqueConstraint(
            "project_entity_id", "knowledge_revision_id", "reference_type",
            name="uq_prj_knowledge_ref_entity_revision_reference",
        ),
        **_strict_kwargs(),
    )


def downgrade() -> None:
    op.drop_table("prj_knowledge_ref")
    op.drop_table("prj_finding")
    op.drop_table("prj_entity")
    op.drop_table("prj_project")
    op.drop_table("kg_rule_spec")
    op.drop_table("kg_relation_current")
    op.drop_table("kg_relation_revision")
    op.drop_index("ix_kg_relation_target_type", table_name="kg_relation")
    op.drop_index("ix_kg_relation_source_type", table_name="kg_relation")
    op.drop_table("kg_relation")
    op.drop_table("kg_component_revision")
    op.drop_table("kg_component")
    op.drop_table("kg_asset_revision")
    op.drop_table("kg_governance_event")
    op.drop_table("kg_revision_governance")
    op.drop_table("kg_asset")
    op.drop_table("kg_content_revision")
    op.drop_table("kg_node")
