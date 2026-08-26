"""Storage-neutral source-universe domain values for Specification 023."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal


AuditStatus = Literal["OK", "MISSING_OBJECT", "SIZE_MISMATCH", "DIGEST_MISMATCH", "ORPHAN_OBJECT"]
ComparisonStatus = Literal["MATCH", "DIFFERENT_ARTIFACT", "MISSING_LOCAL_SOURCE", "ADDITIONAL_LOCAL_SOURCE"]


@dataclass(frozen=True, slots=True)
class SourceRecord:
    source_id: str
    stable_key: str
    title: str
    source_type: str
    canonical_locator: str | None
    access_class: str
    redistribution_status: str
    metadata_visibility: str


@dataclass(frozen=True, slots=True)
class SourceArtifact:
    artifact_id: str
    source_id: str
    sha256: str
    byte_size: int
    media_type: str
    artifact_state: str


@dataclass(frozen=True, slots=True)
class SourceCollection:
    collection_id: str
    stable_key: str
    title: str
    collection_type: str


@dataclass(frozen=True, slots=True)
class StagedSourceArtifact:
    staging_path: Path
    sha256: str
    byte_size: int


@dataclass(frozen=True, slots=True)
class StoredSourceArtifact:
    sha256: str
    byte_size: int
    already_existed: bool


@dataclass(frozen=True, slots=True)
class IntegrityResult:
    sha256: str
    status: AuditStatus
    expected_size: int | None = None
    observed_size: int | None = None
    detail: str | None = None


@dataclass(frozen=True, slots=True)
class IntakeComparison:
    observed_name: str
    status: ComparisonStatus
    local_name: str | None
    expected_sha256: str | None
    observed_sha256: str | None
    expected_size: int | None
    observed_size: int | None
