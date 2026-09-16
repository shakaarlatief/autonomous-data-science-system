"""L0: immutable substrate values. Identity is always explicitly authored."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
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


class TransitionClass(StrEnum):
    MOVE_OR_RENAME = "MOVE_OR_RENAME"
    REPRESENTATION_REPLACEMENT = "REPRESENTATION_REPLACEMENT"
    MERGE = "MERGE"
    SPLIT = "SPLIT"
    SUPERSEDE = "SUPERSEDE"
    RETIRE = "RETIRE"
    REDIRECT = "REDIRECT"


class IdentityDisposition(StrEnum):
    CURRENT = "CURRENT"
    HISTORICAL = "HISTORICAL"
    CONTINUITY = "CONTINUITY"
    MERGED = "MERGED"
    SPLIT = "SPLIT"
    SUPERSEDED = "SUPERSEDED"
    RETIRED = "RETIRED"
    REDIRECTED = "REDIRECTED"
    UNKNOWN = "UNKNOWN"
    UNRESOLVED = "UNRESOLVED"


@dataclass(frozen=True)
class IdentityTransition:
    """Typed projection of an accepted identity_transition.v1 declaration.

    The declaring source retains provenance, optional times, references, and
    its own optional authored ID. Its carrier path identifies a record, not a
    semantic unit. No event ordering is inferred from that path.
    """
    source: GovernedSource
    transition_class: TransitionClass
    predecessors: tuple[SemanticId, ...]
    successors: tuple[SemanticId, ...]
    resolution_behavior: str
    provenance: tuple[str, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "transition_class", TransitionClass(self.transition_class))
        for field in ("predecessors", "successors", "provenance"):
            object.__setattr__(self, field, tuple(getattr(self, field)))
        if any(not isinstance(sid, SemanticId) for sid in (*self.predecessors, *self.successors)):
            raise ValueError("Transition endpoints must be explicitly authored SemanticId values")


@dataclass(frozen=True)
class IdentityResolution:
    semantic_id: SemanticId
    disposition: IdentityDisposition
    current_targets: tuple[SemanticId, ...] = ()
    retired_targets: tuple[SemanticId, ...] = ()
    direct_transition_paths: tuple[str, ...] = ()
    transition_paths: tuple[str, ...] = ()
    predecessor_lineage: tuple[SemanticId, ...] = ()
    continuity_preserved: bool = False
    current_sources: tuple[GovernedSource, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "disposition", IdentityDisposition(self.disposition))
        for field in ("current_targets", "retired_targets", "direct_transition_paths",
                      "transition_paths", "predecessor_lineage", "current_sources"):
            object.__setattr__(self, field, tuple(getattr(self, field)))


@dataclass(frozen=True)
class IdentityHistory:
    semantic_id: SemanticId
    known: bool
    sources: tuple[GovernedSource, ...] = ()
    transition_paths: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "sources", tuple(self.sources))
        object.__setattr__(self, "transition_paths", tuple(self.transition_paths))


@dataclass(frozen=True)
class IdentityIndex:
    snapshot_mode: SnapshotMode
    at_time: datetime | None
    transitions: Mapping[str, IdentityTransition]
    current: Mapping[SemanticId, IdentityResolution]
    history: Mapping[SemanticId, IdentityHistory]

    def __post_init__(self) -> None:
        object.__setattr__(self, "snapshot_mode", SnapshotMode(self.snapshot_mode))
        for field in ("transitions", "current", "history"):
            object.__setattr__(self, field, MappingProxyType(dict(getattr(self, field))))


class AuthorityStatus(StrEnum):
    RESOLVED = "RESOLVED"
    UNRESOLVED_SCOPE_REQUIRED = "UNRESOLVED_SCOPE_REQUIRED"
    UNRESOLVED_AUTHORITY_CONFLICT = "UNRESOLVED_AUTHORITY_CONFLICT"
    MISSING_REQUIRED_AUTHORITY = "MISSING_REQUIRED_AUTHORITY"
    STALE_REQUIRED_AUTHORITY = "STALE_REQUIRED_AUTHORITY"
    REQUIRED_PRIVATE_STATE_UNAVAILABLE = "REQUIRED_PRIVATE_STATE_UNAVAILABLE"


class ScopeDisposition(StrEnum):
    NO_MATCH = "NO_MATCH"
    UNDERSPECIFIED = "UNDERSPECIFIED"
    MATCH = "MATCH"


class Freshness(StrEnum):
    FRESH = "FRESH"
    STALE = "STALE"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class AuthorityQuery:
    action: str
    target: str
    scope: Scope
    consequence: str
    at_time: datetime | None = None
    workstream: str | None = None
    actor: str | None = None
    required_authorities: tuple[SemanticId, ...] = ()
    required_private_dependencies: tuple[str, ...] = ()
    require_revision: bool = False
    require_freshness: bool = True

    def __post_init__(self) -> None:
        if not all(isinstance(v, str) and v for v in (self.action, self.target, self.consequence)):
            raise ValueError("Authority query requires explicit action, target and consequence")
        if set(self.scope.facets) & {"target", "workstream", "actor"}:
            raise ValueError("Use the dedicated query target/workstream/actor fields")
        object.__setattr__(self, "scope", Scope({k: tuple(sorted((v,) if isinstance(v, str) else v))
                                               for k, v in self.scope.facets.items()}))
        for field in ("required_authorities", "required_private_dependencies"):
            object.__setattr__(self, field, tuple(getattr(self, field)))
        if any(not isinstance(sid, SemanticId) for sid in self.required_authorities):
            raise ValueError("Required authorities must be authored typed IDs")
        object.__setattr__(self, "required_authorities", tuple(sorted(set(self.required_authorities), key=lambda s: s.value)))
        object.__setattr__(self, "required_private_dependencies", tuple(sorted(set(self.required_private_dependencies))))
        if self.at_time is not None and self.at_time.utcoffset() is not None:
            object.__setattr__(self, "at_time", self.at_time.astimezone(timezone.utc))


@dataclass(frozen=True)
class AuthorityEvidence:
    """Explicit caller attestation, never an I/O check or a default freshness claim."""
    carrier_path: str
    available: bool | None = None
    freshness: Freshness = Freshness.UNKNOWN
    verified_revision: SourceRevision | None = None
    expected_revision: SourceRevision | None = None

    def __post_init__(self) -> None:
        validate_source_path(self.carrier_path)
        object.__setattr__(self, "freshness", Freshness(self.freshness))


@dataclass(frozen=True)
class PrivateStateEvidence:
    """Public-safe dependency token and verification state; no private contents."""
    dependency: str
    available: bool | None = None
    freshness: Freshness = Freshness.UNKNOWN

    def __post_init__(self) -> None:
        object.__setattr__(self, "freshness", Freshness(self.freshness))


@dataclass(frozen=True)
class ActionConstraint:
    constraint_id: str
    requirement: str


@dataclass(frozen=True)
class ActionContract:
    carrier_path: str
    preconditions: tuple[str, ...]
    mandatory_constraints: tuple[ActionConstraint, ...]
    prohibitions: tuple[str, ...]
    required_postconditions: tuple[str, ...]
    fail_closed_conditions: tuple[str, ...]

    def __post_init__(self) -> None:
        for field in ("preconditions", "mandatory_constraints", "prohibitions",
                      "required_postconditions", "fail_closed_conditions"):
            object.__setattr__(self, field, tuple(getattr(self, field)))


@dataclass(frozen=True)
class AuthoritySource:
    semantic_id: SemanticId | None
    carrier_path: str
    revision: SourceRevision | None
    applicability_reason: str
    evidence: AuthorityEvidence


@dataclass(frozen=True)
class ScopeAssessment:
    carrier_path: str
    disposition: ScopeDisposition


@dataclass(frozen=True)
class AuthorityRemoval:
    carrier_path: str
    reason: str
    by_source: str | None = None


@dataclass(frozen=True)
class AppliedAuthorityRelation:
    owner_path: str
    target_path: str
    mode: RelationMode
    scope: Scope | None = None


@dataclass(frozen=True)
class ConstraintActivation:
    carrier_path: str
    constraint_id: str
    requirement: str


@dataclass(frozen=True)
class ConstraintPrecedence:
    before_source: str
    before_constraint: str
    after_source: str
    after_constraint: str


@dataclass(frozen=True)
class AuthorityReceipt:
    query: AuthorityQuery
    snapshot_mode: SnapshotMode
    governing_sources: tuple[AuthoritySource, ...]
    joint_sources: tuple[AuthoritySource, ...]
    supporting_sources: tuple[AuthoritySource, ...]
    combination_semantics: tuple[tuple[str, str], ...]
    scope_dispositions: tuple[ScopeAssessment, ...]
    removed_sources: tuple[AuthorityRemoval, ...]
    relations: tuple[AppliedAuthorityRelation, ...]
    action_contracts: tuple[ActionContract, ...]
    # Array order is presentation only. Only explicit edges assert precedence.
    activated_constraints: tuple[ConstraintActivation, ...]
    constraint_order: tuple[ConstraintPrecedence, ...]
    private_evidence: tuple[PrivateStateEvidence, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "snapshot_mode", SnapshotMode(self.snapshot_mode))
        for field in ("governing_sources", "joint_sources", "supporting_sources", "scope_dispositions",
                      "removed_sources", "relations", "action_contracts", "private_evidence",
                      "activated_constraints", "constraint_order"):
            object.__setattr__(self, field, tuple(getattr(self, field)))
        for field in ("combination_semantics",):
            object.__setattr__(self, field, tuple(tuple(v) for v in getattr(self, field)))


@dataclass(frozen=True)
class AuthorityResult:
    status: AuthorityStatus
    receipt: AuthorityReceipt | None = None
    diagnostics: tuple[Diagnostic, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "status", AuthorityStatus(self.status))
        object.__setattr__(self, "diagnostics", tuple(self.diagnostics))
        if (self.status == AuthorityStatus.RESOLVED) != (self.receipt is not None):
            raise ValueError("Exactly RESOLVED results carry an authority receipt")


class WorkstreamReadiness(StrEnum):
    RUNNABLE = "RUNNABLE"
    DEPENDENCY_BLOCKED = "DEPENDENCY_BLOCKED"
    BLOCKED = "BLOCKED"
    PAUSED = "PAUSED"
    COMPLETED = "COMPLETED"
    SUPERSEDED = "SUPERSEDED"


class PrimaryRouteDisposition(StrEnum):
    UNIQUE_PRIMARY_ROUTE = "UNIQUE_PRIMARY_ROUTE"
    NO_UNIQUE_PRIMARY_ROUTE = "NO_UNIQUE_PRIMARY_ROUTE"
    NO_READY_WORKSTREAM = "NO_READY_WORKSTREAM"


@dataclass(frozen=True)
class Workstream:
    source: GovernedSource
    semantic_id: SemanticId
    state: LifecycleState
    objective: str | None
    objective_reference: str | None
    parent: SemanticId | None
    depends_on: tuple[SemanticId, ...]
    expected_to_resume: bool
    pause_reason: str | None
    return_condition: str | None
    resume_target: SemanticId | None
    current_anchor: str | None
    expected_revision: SourceRevision | None
    risk_or_reopen_triggers: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "state", LifecycleState(self.state))
        object.__setattr__(self, "depends_on", tuple(sorted(self.depends_on, key=lambda sid: sid.value)))
        object.__setattr__(self, "risk_or_reopen_triggers", tuple(sorted(self.risk_or_reopen_triggers)))


@dataclass(frozen=True)
class WorkstreamBlocker:
    semantic_id: SemanticId
    state: LifecycleState
    direct: bool


@dataclass(frozen=True)
class WorkstreamNode:
    workstream: Workstream
    readiness: WorkstreamReadiness
    dependency_closure: frozenset[SemanticId]
    parent_chain: tuple[SemanticId, ...]
    dependency_blockers: tuple[WorkstreamBlocker, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "dependency_closure", frozenset(self.dependency_closure))
        object.__setattr__(self, "parent_chain", tuple(self.parent_chain))
        object.__setattr__(self, "dependency_blockers", tuple(self.dependency_blockers))

    @property
    def declared_block(self) -> bool:
        return self.workstream.state == LifecycleState.BLOCKED


@dataclass(frozen=True)
class WorkstreamBranch:
    workstream_id: SemanticId
    context_path: tuple[SemanticId, ...]
    current_anchor: str | None
    resume_target: SemanticId | None

    def __post_init__(self) -> None:
        object.__setattr__(self, "context_path", tuple(self.context_path))


@dataclass(frozen=True)
class WorkstreamRoute:
    disposition: PrimaryRouteDisposition
    primary: WorkstreamBranch | None
    branches: tuple[WorkstreamBranch, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "disposition", PrimaryRouteDisposition(self.disposition))
        object.__setattr__(self, "branches", tuple(self.branches))


@dataclass(frozen=True)
class WorkstreamGraph:
    snapshot_mode: SnapshotMode
    nodes: Mapping[SemanticId, WorkstreamNode]
    context_sources: Mapping[SemanticId, GovernedSource]
    active_ready_set: frozenset[SemanticId]
    route: WorkstreamRoute
    excluded_sources: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "snapshot_mode", SnapshotMode(self.snapshot_mode))
        for field in ("nodes", "context_sources"):
            object.__setattr__(self, field, MappingProxyType(dict(getattr(self, field))))
        object.__setattr__(self, "active_ready_set", frozenset(self.active_ready_set))
        object.__setattr__(self, "excluded_sources", tuple(self.excluded_sources))


@dataclass(frozen=True)
class WorkflowStep:
    step_id: str
    operation: str
    target: str
    consequential: bool = True


@dataclass(frozen=True)
class WorkstreamWorkflow:
    workflow_id: str
    workstream_id: SemanticId
    definition_revision: SourceRevision
    steps: tuple[WorkflowStep, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "steps", tuple(self.steps))


@dataclass(frozen=True)
class DurableStepReceipt:
    workflow_id: str
    workstream_id: SemanticId
    definition_revision: SourceRevision
    step_id: str
    status: str
    evidence_refs: tuple[str, ...]
    receipt_revision: SourceRevision

    def __post_init__(self) -> None:
        object.__setattr__(self, "evidence_refs", tuple(sorted(self.evidence_refs)))


@dataclass(frozen=True)
class WorkstreamRecovery:
    workflow: WorkstreamWorkflow
    completed: tuple[WorkflowStep, ...]
    pending: tuple[WorkflowStep, ...]
    next_resume_step: WorkflowStep | None
    receipts: tuple[DurableStepReceipt, ...]

    def __post_init__(self) -> None:
        for field in ("completed", "pending", "receipts"):
            object.__setattr__(self, field, tuple(getattr(self, field)))

    @property
    def blind_replay_required(self) -> bool:
        return False


@dataclass(frozen=True)
class TransientContentVersion:
    """Immutable Git seed plus SHA-256 of exact transient bytes, not a commit.

    The base revision always describes the seed. The content digest describes
    the current copy, which may differ from that seed without any new commit.
    """
    base_revision: SourceRevision
    content_digest: str

    def __post_init__(self) -> None:
        if not isinstance(self.base_revision, SourceRevision):
            raise ValueError("Transient versions require an exact immutable Git seed revision")
        if not isinstance(self.content_digest, str) or not re.fullmatch(r"[0-9a-f]{64}", self.content_digest):
            raise ValueError("Transient content_digest must be lowercase SHA-256 of exact bytes")


@dataclass(frozen=True)
class TransientContent:
    version: TransientContentVersion
    content: bytes

    def __post_init__(self) -> None:
        if not isinstance(self.content, bytes):
            raise ValueError("Transient content requires immutable exact bytes")


class WorkstreamUpdateStatus(StrEnum):
    APPLIED = "APPLIED"
    REJECTED_STALE_REVISION = "REJECTED_STALE_REVISION"


@dataclass(frozen=True)
class ConditionalMutationResult:
    """Store attestation of before/after state at one conditional mutation.

    APPLIED attests a successful mutation, not just acceptance of a request.
    Rejection attests no mutation by this attempt. These are transient states.
    """
    status: WorkstreamUpdateStatus
    before: TransientContent
    after: TransientContent

    def __post_init__(self) -> None:
        object.__setattr__(self, "status", WorkstreamUpdateStatus(self.status))


@dataclass(frozen=True)
class WorkstreamUpdateResult:
    status: WorkstreamUpdateStatus
    expected_version: TransientContentVersion
    before_version: TransientContentVersion
    after_version: TransientContentVersion
    mutation_applied: bool
