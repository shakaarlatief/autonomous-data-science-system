"""L0: immutable substrate values. Identity is always explicitly authored."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path
import re
from types import MappingProxyType
from typing import Mapping, TypeAlias


class AuthorityClass(StrEnum):
    CANONICAL = "canonical"
    CANDIDATE = "candidate"
    HISTORICAL = "historical"
    DERIVED = "derived"
    EVIDENCE = "evidence"
    CAPTURE = "capture"


class Profile(StrEnum):
    SEMANTIC_SOURCE = "semantic_source.v1"
    WORKSTREAM = "workstream.v1"
    GOVERNING_PROCEDURE = "governing_procedure.v1"
    PROJECT_BOUNDARY = "project_boundary.v1"
    IDENTITY_TRANSITION = "identity_transition.v1"
    JOINT_AUTHORITY = "joint_authority.v1"
    CAPTURE = "capture.v1"
    DERIVED_VIEW_MANIFEST = "derived_view_manifest.v1"


class LifecycleState(StrEnum):
    ACTIVE = "ACTIVE"
    PAUSED = "PAUSED"
    BLOCKED = "BLOCKED"
    COMPLETED = "COMPLETED"
    SUPERSEDED = "SUPERSEDED"


class RelationMode(StrEnum):
    REPLACE = "REPLACE"
    SUPPLEMENT = "SUPPLEMENT"
    SPECIALIZE = "SPECIALIZE"
    CORRECT = "CORRECT"


class SnapshotMode(StrEnum):
    COMMIT_SNAPSHOT = "COMMIT_SNAPSHOT"
    WORKTREE_SNAPSHOT = "WORKTREE_SNAPSHOT"


class HashBasis(StrEnum):
    GIT_BLOB_BYTES_AT_COMMIT = "GIT_BLOB_BYTES_AT_COMMIT"


class DiagnosticSeverity(StrEnum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass(frozen=True)
class SemanticId:
    value: str

    def __post_init__(self) -> None:
        if not isinstance(self.value, str) or not re.fullmatch(
            r"[A-Za-z][A-Za-z0-9_.:-]*", self.value
        ):
            raise ValueError("semantic_id must be an authored nonempty identifier")


def validate_source_path(value: str) -> None:
    """Require a normalized repository-relative POSIX path, never a filesystem escape."""
    if (not isinstance(value, str) or not value or "\\" in value or ":" in value
            or any(ord(c) < 32 for c in value)
            or any(part in ("", ".", "..") for part in value.split("/"))):
        raise ValueError("source_path must be a normalized repository-relative path")


@dataclass(frozen=True)
class Scope:
    """Finite exact-match facet conjunction; no action/time or predicate language."""
    facets: Mapping[str, str | tuple[str, ...]]

    def __post_init__(self) -> None:
        copied = {}
        for key, value in self.facets.items():
            if not isinstance(key, str) or not isinstance(value, (str, tuple, list)):
                raise ValueError("scope requires string keys and string/finite-list values")
            values = (value,) if isinstance(value, str) else tuple(value)
            if (not key or key in {"action", "time", "at_time"} or not values
                    or any(not isinstance(v, str) or not v for v in values)
                    or len(set(values)) != len(values)):
                raise ValueError("scope requires named nonempty exact-match facets")
            copied[key] = value if isinstance(value, str) else values
        object.__setattr__(self, "facets", MappingProxyType(copied))


@dataclass(frozen=True)
class Relation:
    mode: RelationMode
    target: SemanticId
    scope: Scope | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "mode", RelationMode(self.mode))
        if self.mode == RelationMode.SPECIALIZE and (self.scope is None or not self.scope.facets):
            raise ValueError("SPECIALIZE requires an explicit narrower scope")


JsonValue: TypeAlias = "None | bool | int | float | str | tuple[JsonValue, ...] | Mapping[str, JsonValue]"


def freeze_json(value):
    """Detach and recursively freeze decoded JSON; no carrier-derived identity."""
    if isinstance(value, Mapping):
        return MappingProxyType({key: freeze_json(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(freeze_json(item) for item in value)
    return value


def thaw_json(value):
    """Produce ordinary JSON containers for schema validation/serialization."""
    if isinstance(value, Mapping):
        return {key: thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [thaw_json(item) for item in value]
    return value


@dataclass(frozen=True)
class RawDeclaration:
    fields: Mapping[str, JsonValue]

    def __post_init__(self) -> None:
        object.__setattr__(self, "fields", freeze_json(self.fields))


@dataclass(frozen=True)
class SourceRevision:
    source_path: str
    source_commit: str
    hash_algorithm: str
    hash_basis: HashBasis
    content_digest: str
    snapshot_mode: SnapshotMode = SnapshotMode.COMMIT_SNAPSHOT

    def __post_init__(self) -> None:
        validate_source_path(self.source_path)
        object.__setattr__(self, "snapshot_mode", SnapshotMode(self.snapshot_mode))
        object.__setattr__(self, "hash_basis", HashBasis(self.hash_basis))
        if self.snapshot_mode != SnapshotMode.COMMIT_SNAPSHOT:
            raise ValueError("WORKTREE_SNAPSHOT is NON_COMMITTED, not a source revision")
        if not re.fullmatch(r"[0-9a-f]{40}", self.source_commit):
            raise ValueError("source_commit must be an exact 40-character commit")
        if self.hash_algorithm != "sha256":
            raise ValueError("hash_algorithm must be sha256")
        if not re.fullmatch(r"[0-9a-f]{64}", self.content_digest):
            raise ValueError("content_digest must be lowercase SHA-256")


@dataclass(frozen=True)
class SnapshotEntry:
    path: str
    blob_id: str | None = None
    git_mode: str | None = None


@dataclass(frozen=True)
class RepositorySnapshot:
    root: Path
    mode: SnapshotMode
    entries: tuple[SnapshotEntry, ...]
    source_commit: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "mode", SnapshotMode(self.mode))
        object.__setattr__(self, "entries", tuple(self.entries))
        if self.mode == SnapshotMode.COMMIT_SNAPSHOT:
            if not self.source_commit or not re.fullmatch(r"[0-9a-f]{40}", self.source_commit):
                raise ValueError("commit snapshot requires an exact commit")
            if any(e.blob_id is None for e in self.entries):
                raise ValueError("commit snapshot entries require Git object IDs")
        elif self.source_commit is not None:
            raise ValueError("worktree snapshot cannot claim a source commit")

    @property
    def status(self) -> str:
        return "COMMITTED" if self.mode == SnapshotMode.COMMIT_SNAPSHOT else "NON_COMMITTED"


@dataclass(frozen=True)
class GovernedSource:
    carrier_path: str
    profile: Profile
    authority_class: AuthorityClass
    kind: str
    declaration: RawDeclaration
    snapshot_mode: SnapshotMode
    semantic_id: SemanticId | None = None
    scope: Scope | None = None
    relations: tuple[Relation, ...] = ()
    revision: SourceRevision | None = None
    state: LifecycleState | None = None

    def __post_init__(self) -> None:
        validate_source_path(self.carrier_path)
        object.__setattr__(self, "profile", Profile(self.profile))
        object.__setattr__(self, "authority_class", AuthorityClass(self.authority_class))
        object.__setattr__(self, "snapshot_mode", SnapshotMode(self.snapshot_mode))
        object.__setattr__(self, "relations", tuple(self.relations))
        if self.state is not None:
            object.__setattr__(self, "state", LifecycleState(self.state))
        if self.snapshot_mode == SnapshotMode.WORKTREE_SNAPSHOT and self.revision is not None:
            raise ValueError("Worktree materialization cannot carry a persistent source revision")
        if self.profile == Profile.CAPTURE and self.authority_class != AuthorityClass.CAPTURE:
            raise ValueError("A capture cannot claim canonical authority")
        if self.profile == Profile.DERIVED_VIEW_MANIFEST and self.authority_class != AuthorityClass.DERIVED:
            raise ValueError("A view manifest must have derived authority class")


@dataclass(frozen=True)
class Diagnostic:
    code: str
    severity: DiagnosticSeverity
    carrier_path: str
    message: str
    semantic_id: SemanticId | None = None
    related_sources: tuple[str, ...] = ()
    remediation: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "severity", DiagnosticSeverity(self.severity))
        object.__setattr__(self, "related_sources", tuple(self.related_sources))


class SubstrateError(ValueError):
    """A deterministic, user-actionable substrate failure."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
