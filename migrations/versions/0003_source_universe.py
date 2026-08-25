"""Add governed source-universe registry tables.

Revision ID: 0003_source_universe
Revises: 0002_knowledge_interchange
Create Date: 2026-08-25
"""

from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "0003_source_universe"
down_revision = "0002_knowledge_interchange"
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


def upgrade() -> None:
    uuid_type = _uuid_type()
    op.create_table(
        "src_source",
        sa.Column("source_id", uuid_type, primary_key=True),
        sa.Column("stable_key", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("source_type", sa.Text(), nullable=False),
        sa.Column("canonical_locator", sa.Text(), nullable=True),
        sa.Column("external_identifier_type", sa.Text(), nullable=True),
        sa.Column("external_identifier_value", sa.Text(), nullable=True),
        sa.Column("access_class", sa.Text(), nullable=False),
        sa.Column("redistribution_status", sa.Text(), nullable=False),
        sa.Column("rights_note", sa.Text(), nullable=True),
        sa.Column("metadata_visibility", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.Column("updated_at", sa.Text(), nullable=False),
        sa.UniqueConstraint("stable_key", name="uq_src_source_stable_key"),
        sa.CheckConstraint("source_type IN ('LECTURE_MATERIAL','BOOK','PAPER','STANDARD','SOFTWARE_DOCUMENTATION','WEB_DOCUMENT','USER_NOTE','DATASET_DOCUMENTATION','OTHER')", name="ck_src_source_type_allowed"),
        sa.CheckConstraint("external_identifier_type IS NULL OR external_identifier_type IN ('DOI','ISBN','URL','STANDARD_ID','OTHER')", name="ck_src_external_identifier_type_allowed"),
        sa.CheckConstraint("access_class IN ('PUBLIC','PRIVATE_USER_SUPPLIED','ORGANIZATION_INTERNAL','UNKNOWN')", name="ck_src_access_class_allowed"),
        sa.CheckConstraint("redistribution_status IN ('PERMITTED','RESTRICTED','UNKNOWN')", name="ck_src_redistribution_allowed"),
        sa.CheckConstraint("metadata_visibility IN ('PUBLIC_SAFE','PRIVATE')", name="ck_src_metadata_visibility_allowed"),
        **_strict_kwargs(),
    )
    op.create_table(
        "src_artifact",
        sa.Column("artifact_id", uuid_type, primary_key=True),
        sa.Column("source_id", uuid_type, nullable=False),
        sa.Column("sha256", sa.Text(), nullable=False),
        sa.Column("byte_size", sa.Integer(), nullable=False),
        sa.Column("media_type", sa.Text(), nullable=False),
        sa.Column("artifact_state", sa.Text(), nullable=False),
        sa.Column("first_seen_at", sa.Text(), nullable=False),
        sa.Column("last_verified_at", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["source_id"], ["src_source.source_id"], name="fk_src_artifact_source", ondelete="RESTRICT"),
        sa.UniqueConstraint("sha256", name="uq_src_artifact_sha256"),
        sa.CheckConstraint("length(sha256) = 64 AND sha256 = lower(sha256)", name="ck_src_artifact_sha256_shape"),
        sa.CheckConstraint("byte_size >= 0", name="ck_src_artifact_byte_size_nonnegative"),
        sa.CheckConstraint("artifact_state IN ('PRESERVED','MISSING','CORRUPT')", name="ck_src_artifact_state_allowed"),
        **_strict_kwargs(),
    )
    op.create_index("ix_src_artifact_source", "src_artifact", ["source_id"])
    op.create_table(
        "src_collection",
        sa.Column("collection_id", uuid_type, primary_key=True),
        sa.Column("stable_key", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("collection_type", sa.Text(), nullable=False),
        sa.Column("canonical_locator", sa.Text(), nullable=True),
        sa.Column("metadata_json", sa.Text(), nullable=False, server_default="{}"),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.Column("updated_at", sa.Text(), nullable=False),
        sa.UniqueConstraint("stable_key", name="uq_src_collection_stable_key"),
        sa.CheckConstraint("collection_type IN ('COURSE','READING_LIST','SOURCE_BUNDLE','STANDARD_FAMILY','PROJECT_EVIDENCE_SET','OTHER')", name="ck_src_collection_type_allowed"),
        *_json_constraints(("json_valid(metadata_json)", "ck_src_collection_metadata_json_valid")),
        **_strict_kwargs(),
    )
    op.create_table(
        "src_collection_membership",
        sa.Column("collection_id", uuid_type, primary_key=True),
        sa.Column("source_id", uuid_type, primary_key=True),
        sa.Column("membership_role", sa.Text(), primary_key=True),
        sa.Column("association_status", sa.Text(), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["collection_id"], ["src_collection.collection_id"], name="fk_src_membership_collection", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["source_id"], ["src_source.source_id"], name="fk_src_membership_source", ondelete="CASCADE"),
        sa.CheckConstraint("membership_role IN ('LECTURE','REQUIRED_READING','SUPPLEMENTARY_READING','BOOK','PAPER','EXERCISE','SOLUTION','NOTES','REFERENCE','UNKNOWN')", name="ck_src_membership_role_allowed"),
        sa.CheckConstraint("association_status IN ('CONFIRMED','LIKELY','POSSIBLE','UNVERIFIED')", name="ck_src_association_status_allowed"),
        **_strict_kwargs(),
    )
    op.create_table(
        "src_locator",
        sa.Column("locator_id", uuid_type, primary_key=True),
        sa.Column("source_id", uuid_type, nullable=False),
        sa.Column("artifact_id", uuid_type, nullable=True),
        sa.Column("locator_type", sa.Text(), nullable=False),
        sa.Column("locator", sa.Text(), nullable=False),
        sa.Column("is_canonical", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("visibility", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(["source_id"], ["src_source.source_id"], name="fk_src_locator_source", ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["artifact_id"], ["src_artifact.artifact_id"], name="fk_src_locator_artifact", ondelete="CASCADE"),
        sa.UniqueConstraint("source_id", "artifact_id", "locator_type", "locator", name="uq_src_locator_identity"),
        sa.CheckConstraint("locator_type IN ('CANONICAL_URL','DOI','ISBN','STANDARD_ID','OBSERVED_PATH','OBSERVED_URL','OTHER')", name="ck_src_locator_type_allowed"),
        sa.CheckConstraint("visibility IN ('PUBLIC_SAFE','PRIVATE')", name="ck_src_locator_visibility_allowed"),
        sa.CheckConstraint("is_canonical IN (0,1)", name="ck_src_locator_canonical_boolean"),
        **_strict_kwargs(),
    )
    op.create_table(
        "src_ingestion_event",
        sa.Column("ingestion_event_id", uuid_type, primary_key=True),
        sa.Column("source_id", uuid_type, nullable=False),
        sa.Column("artifact_id", uuid_type, nullable=True),
        sa.Column("collection_id", uuid_type, nullable=True),
        sa.Column("occurred_at", sa.Text(), nullable=False),
        sa.Column("intake_channel", sa.Text(), nullable=False),
        sa.Column("observed_name", sa.Text(), nullable=True),
        sa.Column("observed_locator", sa.Text(), nullable=True),
        sa.Column("result", sa.Text(), nullable=False),
        sa.Column("note", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["source_id"], ["src_source.source_id"], name="fk_src_ingestion_source", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["artifact_id"], ["src_artifact.artifact_id"], name="fk_src_ingestion_artifact", ondelete="RESTRICT"),
        sa.ForeignKeyConstraint(["collection_id"], ["src_collection.collection_id"], name="fk_src_ingestion_collection", ondelete="RESTRICT"),
        sa.CheckConstraint("intake_channel IN ('FILESYSTEM','CHATGPT_UPLOAD','WEB_DOWNLOAD','CONNECTOR','MANUAL_REFERENCE','OTHER')", name="ck_src_intake_channel_allowed"),
        sa.CheckConstraint("result IN ('NEW_ARTIFACT','EXACT_DUPLICATE','EXTERNAL_REFERENCE_ONLY','REJECTED','UNRESOLVED')", name="ck_src_ingestion_result_allowed"),
        **_strict_kwargs(),
    )
    op.create_table(
        "src_derived_artifact",
        sa.Column("derived_artifact_id", uuid_type, primary_key=True),
        sa.Column("parent_source_artifact_id", uuid_type, nullable=False),
        sa.Column("kind", sa.Text(), nullable=False),
        sa.Column("pipeline_key", sa.Text(), nullable=False),
        sa.Column("pipeline_version", sa.Text(), nullable=False),
        sa.Column("configuration_sha256", sa.Text(), nullable=False),
        sa.Column("output_sha256", sa.Text(), nullable=False),
        sa.Column("byte_size", sa.Integer(), nullable=False),
        sa.Column("media_type", sa.Text(), nullable=False),
        sa.Column("storage_key", sa.Text(), nullable=False),
        sa.Column("created_at", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(["parent_source_artifact_id"], ["src_artifact.artifact_id"], name="fk_src_derived_parent", ondelete="CASCADE"),
        sa.CheckConstraint("kind IN ('EXTRACTED_TEXT','PAGE_RENDER_SET','DOCUMENT_STRUCTURE','OTHER')", name="ck_src_derived_kind_allowed"),
        sa.CheckConstraint("byte_size >= 0", name="ck_src_derived_byte_size_nonnegative"),
        **_strict_kwargs(),
    )


def downgrade() -> None:
    op.drop_table("src_derived_artifact")
    op.drop_table("src_ingestion_event")
    op.drop_table("src_locator")
    op.drop_table("src_collection_membership")
    op.drop_table("src_collection")
    op.drop_index("ix_src_artifact_source", table_name="src_artifact")
    op.drop_table("src_artifact")
    op.drop_table("src_source")
