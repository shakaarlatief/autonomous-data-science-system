"""SQLAlchemy Core source-universe schema for Specification 023."""

from __future__ import annotations

from sqlalchemy import CheckConstraint, Column, ForeignKey, Index, Integer, Table, Text, UniqueConstraint

from ads_system.infrastructure.persistence.schema import metadata
from ads_system.infrastructure.persistence.types import DomainUUID


def _json_check(expression: str, name: str) -> CheckConstraint:
    return CheckConstraint(expression, name=name).ddl_if(dialect="sqlite")


source_record = Table(
    "src_source",
    metadata,
    Column("source_id", DomainUUID(), primary_key=True),
    Column("stable_key", Text, nullable=False),
    Column("title", Text, nullable=False),
    Column("source_type", Text, nullable=False),
    Column("canonical_locator", Text, nullable=True),
    Column("external_identifier_type", Text, nullable=True),
    Column("external_identifier_value", Text, nullable=True),
    Column("access_class", Text, nullable=False),
    Column("redistribution_status", Text, nullable=False),
    Column("rights_note", Text, nullable=True),
    Column("metadata_visibility", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    Column("updated_at", Text, nullable=False),
    UniqueConstraint("stable_key", name="src_source_stable_key"),
    CheckConstraint("source_type IN ('LECTURE_MATERIAL','BOOK','PAPER','STANDARD','SOFTWARE_DOCUMENTATION','WEB_DOCUMENT','USER_NOTE','DATASET_DOCUMENTATION','OTHER')", name="src_source_type_allowed"),
    CheckConstraint("external_identifier_type IS NULL OR external_identifier_type IN ('DOI','ISBN','URL','STANDARD_ID','OTHER')", name="src_external_identifier_type_allowed"),
    CheckConstraint("access_class IN ('PUBLIC','PRIVATE_USER_SUPPLIED','ORGANIZATION_INTERNAL','UNKNOWN')", name="src_access_class_allowed"),
    CheckConstraint("redistribution_status IN ('PERMITTED','RESTRICTED','UNKNOWN')", name="src_redistribution_allowed"),
    CheckConstraint("metadata_visibility IN ('PUBLIC_SAFE','PRIVATE')", name="src_metadata_visibility_allowed"),
    sqlite_strict=True,
)

source_artifact = Table(
    "src_artifact",
    metadata,
    Column("artifact_id", DomainUUID(), primary_key=True),
    Column("source_id", DomainUUID(), ForeignKey("src_source.source_id", ondelete="RESTRICT"), nullable=False),
    Column("sha256", Text, nullable=False),
    Column("byte_size", Integer, nullable=False),
    Column("media_type", Text, nullable=False),
    Column("artifact_state", Text, nullable=False),
    Column("first_seen_at", Text, nullable=False),
    Column("last_verified_at", Text, nullable=True),
    UniqueConstraint("sha256", name="src_artifact_sha256"),
    CheckConstraint("length(sha256) = 64 AND sha256 = lower(sha256)", name="src_artifact_sha256_shape"),
    CheckConstraint("byte_size >= 0", name="src_artifact_byte_size_nonnegative"),
    CheckConstraint("artifact_state IN ('PRESERVED','MISSING','CORRUPT')", name="src_artifact_state_allowed"),
    sqlite_strict=True,
)
Index("ix_src_artifact_source", source_artifact.c.source_id)

source_collection = Table(
    "src_collection",
    metadata,
    Column("collection_id", DomainUUID(), primary_key=True),
    Column("stable_key", Text, nullable=False),
    Column("title", Text, nullable=False),
    Column("collection_type", Text, nullable=False),
    Column("canonical_locator", Text, nullable=True),
    Column("metadata_json", Text, nullable=False, server_default="{}"),
    Column("created_at", Text, nullable=False),
    Column("updated_at", Text, nullable=False),
    UniqueConstraint("stable_key", name="src_collection_stable_key"),
    CheckConstraint("collection_type IN ('COURSE','READING_LIST','SOURCE_BUNDLE','STANDARD_FAMILY','PROJECT_EVIDENCE_SET','OTHER')", name="src_collection_type_allowed"),
    _json_check("json_valid(metadata_json)", "src_collection_metadata_json_valid"),
    sqlite_strict=True,
)

source_membership = Table(
    "src_collection_membership",
    metadata,
    Column("collection_id", DomainUUID(), ForeignKey("src_collection.collection_id", ondelete="CASCADE"), primary_key=True),
    Column("source_id", DomainUUID(), ForeignKey("src_source.source_id", ondelete="CASCADE"), primary_key=True),
    Column("membership_role", Text, primary_key=True),
    Column("association_status", Text, nullable=False),
    Column("note", Text, nullable=True),
    CheckConstraint("membership_role IN ('LECTURE','REQUIRED_READING','SUPPLEMENTARY_READING','BOOK','PAPER','EXERCISE','SOLUTION','NOTES','REFERENCE','UNKNOWN')", name="src_membership_role_allowed"),
    CheckConstraint("association_status IN ('CONFIRMED','LIKELY','POSSIBLE','UNVERIFIED')", name="src_association_status_allowed"),
    sqlite_strict=True,
)

source_locator = Table(
    "src_locator",
    metadata,
    Column("locator_id", DomainUUID(), primary_key=True),
    Column("source_id", DomainUUID(), ForeignKey("src_source.source_id", ondelete="CASCADE"), nullable=False),
    Column("artifact_id", DomainUUID(), ForeignKey("src_artifact.artifact_id", ondelete="CASCADE"), nullable=True),
    Column("locator_type", Text, nullable=False),
    Column("locator", Text, nullable=False),
    Column("is_canonical", Integer, nullable=False, server_default="0"),
    Column("visibility", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    CheckConstraint("locator_type IN ('CANONICAL_URL','DOI','ISBN','STANDARD_ID','OBSERVED_PATH','OBSERVED_URL','OTHER')", name="src_locator_type_allowed"),
    CheckConstraint("visibility IN ('PUBLIC_SAFE','PRIVATE')", name="src_locator_visibility_allowed"),
    CheckConstraint("is_canonical IN (0,1)", name="src_locator_canonical_boolean"),
    UniqueConstraint("source_id", "artifact_id", "locator_type", "locator", name="src_locator_identity"),
    sqlite_strict=True,
)

source_ingestion_event = Table(
    "src_ingestion_event",
    metadata,
    Column("ingestion_event_id", DomainUUID(), primary_key=True),
    Column("source_id", DomainUUID(), ForeignKey("src_source.source_id", ondelete="RESTRICT"), nullable=False),
    Column("artifact_id", DomainUUID(), ForeignKey("src_artifact.artifact_id", ondelete="RESTRICT"), nullable=True),
    Column("collection_id", DomainUUID(), ForeignKey("src_collection.collection_id", ondelete="RESTRICT"), nullable=True),
    Column("occurred_at", Text, nullable=False),
    Column("intake_channel", Text, nullable=False),
    Column("observed_name", Text, nullable=True),
    Column("observed_locator", Text, nullable=True),
    Column("result", Text, nullable=False),
    Column("note", Text, nullable=True),
    CheckConstraint("intake_channel IN ('FILESYSTEM','CHATGPT_UPLOAD','WEB_DOWNLOAD','CONNECTOR','MANUAL_REFERENCE','OTHER')", name="src_intake_channel_allowed"),
    CheckConstraint("result IN ('NEW_ARTIFACT','EXACT_DUPLICATE','EXTERNAL_REFERENCE_ONLY','REJECTED','UNRESOLVED')", name="src_ingestion_result_allowed"),
    sqlite_strict=True,
)

source_derived_artifact = Table(
    "src_derived_artifact",
    metadata,
    Column("derived_artifact_id", DomainUUID(), primary_key=True),
    Column("parent_source_artifact_id", DomainUUID(), ForeignKey("src_artifact.artifact_id", ondelete="CASCADE"), nullable=False),
    Column("kind", Text, nullable=False),
    Column("pipeline_key", Text, nullable=False),
    Column("pipeline_version", Text, nullable=False),
    Column("configuration_sha256", Text, nullable=False),
    Column("output_sha256", Text, nullable=False),
    Column("byte_size", Integer, nullable=False),
    Column("media_type", Text, nullable=False),
    Column("storage_key", Text, nullable=False),
    Column("created_at", Text, nullable=False),
    CheckConstraint("kind IN ('EXTRACTED_TEXT','PAGE_RENDER_SET','DOCUMENT_STRUCTURE','OTHER')", name="src_derived_kind_allowed"),
    CheckConstraint("byte_size >= 0", name="src_derived_byte_size_nonnegative"),
    sqlite_strict=True,
)
