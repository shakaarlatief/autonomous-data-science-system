"""Read-only first-slice validation, without identity/authority resolution."""

from dataclasses import dataclass
import hashlib
from pathlib import Path, PurePosixPath
from typing import Mapping

from ..adapters.gitio import read_committed_path
from ..adapters.schema import SchemaValidator
from ..declaration import parse_markdown, parse_native_json
from ..model import (
    AuthorityClass, Diagnostic, DiagnosticSeverity, GovernedSource, HashBasis, LifecycleState,
    Profile, RawDeclaration, Relation, RelationMode, RepositorySnapshot, Scope,
    SemanticId, SnapshotMode, SourceRevision, SubstrateError,
)
from ..references import validate_durable_evidence, verify_blob_digest
from .discovery import DiscoveryPolicy, PathRole, read_entry, read_snapshot_blobs


@dataclass(frozen=True)
class ValidationResult:
    sources: tuple[GovernedSource, ...]
    diagnostics: tuple[Diagnostic, ...]
    candidate_count: int
    excluded_count: int
    undeclared_by_root: tuple[tuple[str, int], ...]
    path_role_counts: tuple[tuple[str, int], ...]
    noncanonical_declaration_count: int

    @property
    def ok(self) -> bool:
        return not any(d.severity == DiagnosticSeverity.ERROR for d in self.diagnostics)

    @property
    def excluded_but_declared_count(self) -> int:
        return sum(d.code == "EXCLUDED_BUT_DECLARED" for d in self.diagnostics)


def validate_revision_descriptor(root: Path, descriptor: Mapping) -> tuple[Diagnostic, ...]:
    path = descriptor.get("source_path", "")
    try:
        mode = SnapshotMode(descriptor.get("snapshot_mode", SnapshotMode.COMMIT_SNAPSHOT))
        boundary = validate_durable_evidence(mode, path)
        if boundary:
            return boundary
        revision = SourceRevision(**descriptor)
    except (TypeError, ValueError) as error:
        return (Diagnostic("INVALID_SOURCE_REVISION", DiagnosticSeverity.ERROR, path, str(error)),)
    try:
        blob = read_committed_path(root, revision.source_commit, revision.source_path)
    except SubstrateError as error:
        return (Diagnostic(error.code, DiagnosticSeverity.ERROR, path, str(error)),)
    return verify_blob_digest(revision, blob)


def validate_declaration(content: bytes, carrier_path: str, validator: SchemaValidator) -> tuple[RawDeclaration | None, tuple[Diagnostic, ...]]:
    try:
        raw = parse_markdown(content) if PurePosixPath(carrier_path).suffix.lower() == ".md" else parse_native_json(content)
    except SubstrateError as error:
        return None, (Diagnostic(error.code, DiagnosticSeverity.ERROR, carrier_path, str(error)),)
    return raw, validator.validate(raw, carrier_path) if raw is not None else ()


def validate_repository(
    snapshot: RepositorySnapshot, *, validator: SchemaValidator | None = None,
    policy: DiscoveryPolicy = DiscoveryPolicy(), durable_evidence: bool = False,
) -> ValidationResult:
    validator = validator or SchemaValidator()
    diagnostics = list(validate_durable_evidence(snapshot.mode)) if durable_evidence else []
    sources = []
    candidates = excluded_count = 0
    undeclared = {}
    role_counts = {}
    noncanonical_count = 0
    blobs = read_snapshot_blobs(snapshot, policy)
    for entry in sorted(snapshot.entries, key=lambda item: item.path):
        if not policy.supports(entry.path):
            continue
        candidates += 1
        role = policy.classify(entry.path)
        role_counts[role.value] = role_counts.get(role.value, 0) + 1
        excluded = role != PathRole.ELIGIBLE_SOURCE
        excluded_count += int(excluded)
        if role == PathRole.EVIDENCE_FIXTURE:
            # Fixture validity belongs to its tests, never to production discovery.
            continue
        try:
            content = read_entry(snapshot, entry, blobs)
        except SubstrateError as error:
            diagnostics.append(Diagnostic(error.code, DiagnosticSeverity.ERROR, entry.path, str(error)))
            continue
        raw, findings = validate_declaration(content, entry.path, validator)
        diagnostics.extend(findings)
        misplaced = raw is not None and not policy.admits_profile(entry.path, Profile(raw.fields["profile"]))
        forbidden_attempt = role == PathRole.DISALLOWED and any(d.code != "INVALID_UTF8" for d in findings)
        if misplaced or forbidden_attempt:
            diagnostics.append(Diagnostic(
                "EXCLUDED_BUT_DECLARED", DiagnosticSeverity.ERROR, entry.path,
                f"A production declaration is not permitted in this path role: {role.value}.",
                remediation="Use the natural eligible source or the designated area for this artifact profile.",
            ))
        if raw is None:
            if not findings:
                root = policy.bounded_root(entry.path)
                undeclared[root] = undeclared.get(root, 0) + 1
            continue
        if findings or misplaced:
            continue
        fields = raw.fields
        if fields["profile"] == Profile.DERIVED_VIEW_MANIFEST:
            if durable_evidence:
                diagnostics.extend(validate_durable_evidence(SnapshotMode(fields["snapshot_mode"]), entry.path))
            for binding in fields["input_bindings"]:
                if "source_commit" in binding or snapshot.mode == SnapshotMode.COMMIT_SNAPSHOT:
                    descriptor = {key: value for key, value in binding.items() if key != "semantic_id"}
                    # Same-commit manifests bind exact input digests without a
                    # self-referential SHA. The checked commit supplies context.
                    descriptor.setdefault("source_commit", snapshot.source_commit)
                    diagnostics.extend(validate_revision_descriptor(snapshot.root, descriptor))
                elif durable_evidence:
                    diagnostics.append(Diagnostic(
                        "UNBOUND_SOURCE_REVISION", DiagnosticSeverity.ERROR, entry.path,
                        "Durable evidence requires an exact commit for every input binding.",
                    ))
        if "expected_revision" in fields:
            diagnostics.extend(validate_revision_descriptor(snapshot.root, fields["expected_revision"]))
        if excluded:
            # Validate admitted capture/manifest declarations, including revision
            # and durability checks, without exposing them as canonical sources.
            noncanonical_count += 1
            continue
        revision = None
        if snapshot.mode == SnapshotMode.COMMIT_SNAPSHOT:
            revision = SourceRevision(entry.path, snapshot.source_commit, "sha256", HashBasis.GIT_BLOB_BYTES_AT_COMMIT, hashlib.sha256(content).hexdigest())
        sources.append(GovernedSource(
            carrier_path=entry.path, profile=Profile(fields["profile"]),
            authority_class=AuthorityClass(fields["authority_class"]), kind=fields["kind"],
            declaration=raw, snapshot_mode=snapshot.mode,
            semantic_id=SemanticId(fields["semantic_id"]) if "semantic_id" in fields else None,
            scope=Scope(fields["scope"]) if "scope" in fields else None,
            relations=tuple(Relation(RelationMode(r["mode"]), SemanticId(r["target"]), Scope(r["scope"]) if "scope" in r else None) for r in fields.get("relations", ())),
            revision=revision,
            state=LifecycleState(fields["state"]) if "state" in fields else None,
        ))
    return ValidationResult(
        tuple(sources), tuple(diagnostics), candidates, excluded_count,
        tuple(sorted(undeclared.items())), tuple(sorted(role_counts.items())), noncanonical_count,
    )
