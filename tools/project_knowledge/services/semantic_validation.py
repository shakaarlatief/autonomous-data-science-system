"""L3 query-independent semantic validation over an already bounded repository snapshot.

The base validator owns discovery, parsing, schema/revision checks and public
projection safety. This layer composes only semantics that can be checked
without inventing an authority query, wall-clock time or retrieval context.
"""

from dataclasses import dataclass
from datetime import datetime, timezone
from itertools import combinations

from ..adapters.gitio import read_blobs
from ..adapters.schema import SCHEMA_FILES, SchemaValidator
from ..identity import IdentityValidationError, build_identity_index, transition_from_source
from ..model import (
    AuthorityClass, Diagnostic, DiagnosticSeverity, LifecycleState, Profile, SnapshotMode, SubstrateError,
)
from ..workstreams import WorkstreamValidationError, build_workstream_graph, workstream_from_source
from .validation import ValidationResult, validate_repository


_TEMPORAL_FIELDS = ("effective_from", "effective_to", "authority_from", "authority_to")


def _has_temporal_control(source) -> bool:
    return any(field in source.declaration.fields for field in _TEMPORAL_FIELDS)


def _time_value(source, field):
    value = source.declaration.fields.get(field)
    if value is None:
        return None
    return datetime.fromisoformat(value.upper().replace("Z", "+00:00")).astimezone(timezone.utc)


def _source_window(source):
    """Return the intersection of effective/authority half-open intervals."""
    starts, ends, invalid = [], [], False
    for start_field, end_field in (("effective_from", "effective_to"), ("authority_from", "authority_to")):
        start = _time_value(source, start_field)
        end = _time_value(source, end_field)
        if start is not None:
            starts.append(start)
        if end is not None:
            ends.append(end)
        if start is not None and end is not None and start >= end:
            invalid = True
    return (max(starts) if starts else None, min(ends) if ends else None, invalid)


def _windows_overlap(left, right):
    left_start, left_end, _ = left
    right_start, right_end, _ = right
    start_values = [value for value in (left_start, right_start) if value is not None]
    end_values = [value for value in (left_end, right_end) if value is not None]
    start = max(start_values) if start_values else None
    end = min(end_values) if end_values else None
    return end is None or start is None or start < end


def _scopes_overlap(left, right) -> bool:
    left_facets = left.scope.facets if left.scope is not None else {}
    right_facets = right.scope.facets if right.scope is not None else {}
    for key in set(left_facets) & set(right_facets):
        left_values = left_facets[key]
        right_values = right_facets[key]
        left_set = {left_values} if isinstance(left_values, str) else set(left_values)
        right_set = {right_values} if isinstance(right_values, str) else set(right_values)
        if left_set.isdisjoint(right_set):
            return False
    return True


def _actions_overlap(left, right) -> bool:
    left_actions = set(left.declaration.fields.get("governed_action_classes", ()))
    right_actions = set(right.declaration.fields.get("governed_action_classes", ()))
    return bool(left_actions & right_actions)


@dataclass(frozen=True)
class ProjectValidationResult:
    repository: ValidationResult
    diagnostics: tuple[Diagnostic, ...]

    @property
    def ok(self) -> bool:
        return not any(item.severity == DiagnosticSeverity.ERROR for item in self.diagnostics)


def _diagnostic(code, path, message, semantic_id=None, related=(), severity=DiagnosticSeverity.ERROR):
    return Diagnostic(
        code,
        severity,
        path,
        message,
        semantic_id,
        tuple(sorted(set(related))),
    )


def _ordered_diagnostics(diagnostics):
    unique = {}
    for item in diagnostics:
        key = (
            item.severity.value,
            item.code,
            item.carrier_path,
            item.semantic_id.value if item.semantic_id else "",
            item.message,
            item.related_sources,
            item.remediation,
        )
        unique[key] = item
    return tuple(sorted(
        unique.values(),
        key=lambda item: (
            item.severity.value,
            item.code,
            item.carrier_path,
            item.semantic_id.value if item.semantic_id else "",
            item.message,
            item.related_sources,
            item.remediation or "",
        ),
    ))


def _validator_for_snapshot(snapshot):
    """Bind COMMIT validation to that commit's schema closure, never checkout drift."""
    if snapshot.mode != SnapshotMode.COMMIT_SNAPSHOT:
        return SchemaValidator()
    entries = {entry.path: entry for entry in snapshot.entries}
    present = set(SCHEMA_FILES) & entries.keys()
    if not present:
        # Preserve the pre-G014 contract for bounded synthetic/minimal
        # repositories that do not vendor the project schema set at all.
        # Once a repository carries any project-knowledge schema, however,
        # commit-bound validation must use one complete exact closure.
        return SchemaValidator()
    missing = set(SCHEMA_FILES) - entries.keys()
    if missing:
        raise SubstrateError(
            "MISSING_SCHEMA_DEPENDENCY",
            "Committed project-knowledge schema closure is incomplete.",
        )
    raw = read_blobs(
        snapshot.root,
        tuple(entries[path] for path in sorted(SCHEMA_FILES)),
    )
    return SchemaValidator(
        schema_blobs={path: raw[entries[path].blob_id] for path in SCHEMA_FILES}
    )


def validate_project_knowledge(snapshot, *, durable_evidence=False, known_private_values=()):
    """Validate query-independent G001-G012 repository semantics deterministically.

    Authority selection itself is deliberately absent: no synthetic task/action,
    scope, actor, time or private-state evidence is invented merely to make a
    broad validation command return a result.
    """
    base = validate_repository(
        snapshot,
        validator=_validator_for_snapshot(snapshot),
        durable_evidence=durable_evidence,
        known_private_values=known_private_values,
    )
    if not base.ok:
        return ProjectValidationResult(base, _ordered_diagnostics(base.diagnostics))

    sources = tuple(base.sources)
    diagnostics = list(base.diagnostics)
    current = tuple(
        source for source in sources
        if source.authority_class == AuthorityClass.CANONICAL
        and source.state != LifecycleState.SUPERSEDED
    )
    known = tuple(
        source for source in sources
        if source.authority_class in {AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL}
    )

    windows = {source.carrier_path: _source_window(source) for source in known}
    invalid_temporal_paths = {
        source.carrier_path for source in known if windows[source.carrier_path][2]
    }
    for source in sorted(known, key=lambda item: item.carrier_path):
        if source.carrier_path in invalid_temporal_paths:
            diagnostics.append(_diagnostic(
                "INVALID_IDENTITY_TIME",
                source.carrier_path,
                "Temporal interval must have start before end",
                source.semantic_id,
            ))

    # Current semantic identity must never be selected by carrier ordering.
    owners = {}
    for source in current:
        if source.semantic_id is not None:
            owners.setdefault(source.semantic_id, []).append(source)
    duplicate_ids = set()
    for sid, claimed in owners.items():
        if len(claimed) <= 1:
            continue
        if any(source.carrier_path in invalid_temporal_paths for source in claimed):
            continue
        overlaps = any(
            _windows_overlap(windows[left.carrier_path], windows[right.carrier_path])
            for left, right in combinations(claimed, 2)
        )
        if overlaps:
            duplicate_ids.add(sid)

    known_ids = {source.semantic_id for source in known if source.semantic_id is not None}
    owners_by_value = {sid.value: claimed for sid, claimed in owners.items()}
    for source in sorted(current, key=lambda item: item.carrier_path):
        for relation in source.relations:
            if relation.target not in known_ids:
                diagnostics.append(_diagnostic(
                    "DANGLING_RELATION_TARGET",
                    source.carrier_path,
                    f"A current canonical relation targets missing authored identity: {relation.target.value}.",
                    source.semantic_id,
                ))

    # Governing-procedure constraints carry authored IDs whose order is
    # meaningful. Duplicate IDs would make cross-source activation ambiguous.
    for source in sorted(known, key=lambda item: item.carrier_path):
        if source.profile != Profile.GOVERNING_PROCEDURE:
            continue
        constraints = tuple(source.declaration.fields.get("mandatory_constraints", ()))
        ids = tuple(item["constraint_id"] for item in constraints)
        duplicates = sorted({identity for identity in ids if ids.count(identity) > 1})
        if duplicates:
            diagnostics.append(_diagnostic(
                "DUPLICATE_CONSTRAINT_ID",
                source.carrier_path,
                "Constraint identifiers must be unique within their owning procedure: "
                + ", ".join(duplicates) + ".",
                source.semantic_id,
            ))

    # Joint declarations are special only when all named current members exist.
    joint_sets = {}
    for source in sorted(current, key=lambda item: item.carrier_path):
        if source.profile != Profile.JOINT_AUTHORITY:
            continue
        members = tuple(source.declaration.fields["members"])
        missing = tuple(member for member in members if member not in owners_by_value)
        if missing:
            diagnostics.append(_diagnostic(
                "DANGLING_JOINT_AUTHORITY_MEMBER",
                source.carrier_path,
                "Joint authority names missing current canonical member identities: "
                + ", ".join(missing) + ".",
                source.semantic_id,
            ))
        temporal_membership = _has_temporal_control(source) or any(
            _has_temporal_control(owner)
            for member in members
            for owner in owners_by_value.get(member, ())
        )
        if temporal_membership:
            diagnostics.append(_diagnostic(
                "TEMPORAL_JOINT_MEMBERSHIP_DEFERRED",
                source.carrier_path,
                "Joint-authority applicability requires an explicit time and is deferred to task-scoped resolution.",
                source.semantic_id,
                severity=DiagnosticSeverity.INFO,
            ))
        if source.state not in {LifecycleState.PAUSED, LifecycleState.BLOCKED}:
            key = tuple(sorted(members))
            joint_sets.setdefault(key, []).append(source)
    for members, declarations in sorted(joint_sets.items()):
        if len(declarations) <= 1:
            continue
        conflicting_pairs = tuple(
            (left, right)
            for left, right in combinations(declarations, 2)
            if left.carrier_path not in invalid_temporal_paths
            and right.carrier_path not in invalid_temporal_paths
            and _windows_overlap(windows[left.carrier_path], windows[right.carrier_path])
            and _scopes_overlap(left, right)
            and _actions_overlap(left, right)
        )
        if conflicting_pairs:
            conflicting_paths = {
                source.carrier_path
                for pair in conflicting_pairs
                for source in pair
            }
            diagnostics.append(_diagnostic(
                "DUPLICATE_JOINT_AUTHORITY_SET",
                min(conflicting_paths),
                "Multiple simultaneously applicable joint declarations claim the same member set.",
                related=conflicting_paths,
            ))

    # The workstream engine validates dependency/parent/resume closure without
    # inventing a route priority. Supply only explicitly referenced non-workstream
    # context identities; unrelated canonical knowledge is not graph context.
    workstream_sources = tuple(source for source in sources
                               if source.profile == Profile.WORKSTREAM
                               and source.authority_class == AuthorityClass.CANONICAL
                               and source.state != LifecycleState.SUPERSEDED)
    referenced_context = set()
    workstream_ids = {
        source.semantic_id.value for source in workstream_sources if source.semantic_id is not None
    }
    for source in workstream_sources:
        data = source.declaration.fields
        for field in ("parent", "resume_target"):
            if field in data:
                referenced_context.add(data[field])
    context_ids = referenced_context - workstream_ids
    contexts = tuple(
        source for source in sources
        if source.authority_class == AuthorityClass.CANONICAL
        and source.profile != Profile.WORKSTREAM
        and source.semantic_id is not None
        and source.semantic_id.value in context_ids
    )
    graph_sources = (*workstream_sources, *contexts)
    graph_ids = {source.semantic_id for source in graph_sources if source.semantic_id is not None}
    if workstream_sources:
        if any(_has_temporal_control(source) for source in graph_sources):
            typed_workstreams = []
            for source in workstream_sources:
                try:
                    typed_workstreams.append(workstream_from_source(source))
                except WorkstreamValidationError as error:
                    diagnostics.extend(error.diagnostics)
            binding_values = {
                source.semantic_id.value: source
                for source in graph_sources
                if source.semantic_id is not None
            }
            for context in contexts:
                if context.state == LifecycleState.SUPERSEDED:
                    diagnostics.append(_diagnostic(
                        "INVALID_WORKSTREAM_CONTEXT",
                        context.carrier_path,
                        "Workstream context must be a current non-superseded canonical source.",
                        context.semantic_id,
                    ))
            for workstream in typed_workstreams:
                source = workstream.source
                sid = workstream.semantic_id.value
                for dependency in workstream.depends_on:
                    if dependency.value == sid:
                        diagnostics.append(_diagnostic(
                            "WORKSTREAM_SELF_DEPENDENCY",
                            source.carrier_path,
                            "A workstream cannot require itself.",
                            workstream.semantic_id,
                        ))
                    elif dependency.value not in workstream_ids:
                        diagnostics.append(_diagnostic(
                            "DANGLING_WORKSTREAM_DEPENDENCY",
                            source.carrier_path,
                            "A workstream dependency has no current canonical workstream owner.",
                            workstream.semantic_id,
                        ))
                if workstream.parent is not None:
                    if workstream.parent.value == sid:
                        diagnostics.append(_diagnostic(
                            "WORKSTREAM_SELF_PARENT",
                            source.carrier_path,
                            "A workstream cannot parent itself.",
                            workstream.semantic_id,
                        ))
                    elif workstream.parent.value not in binding_values:
                        diagnostics.append(_diagnostic(
                            "DANGLING_WORKSTREAM_PARENT",
                            source.carrier_path,
                            "A workstream parent has no supplied current canonical owner.",
                            workstream.semantic_id,
                        ))
                if workstream.resume_target is not None:
                    target = binding_values.get(workstream.resume_target.value)
                    if target is None:
                        diagnostics.append(_diagnostic(
                            "DANGLING_WORKSTREAM_RESUME_TARGET",
                            source.carrier_path,
                            "A workstream resume target has no supplied current canonical owner.",
                            workstream.semantic_id,
                        ))
                    elif (workstream.expected_to_resume
                          and target.state in {LifecycleState.COMPLETED, LifecycleState.SUPERSEDED}):
                        diagnostics.append(_diagnostic(
                            "INVALID_WORKSTREAM_RESUME_TARGET",
                            source.carrier_path,
                            "Expected resume target is already completed or superseded.",
                            workstream.semantic_id,
                        ))
            diagnostics.append(_diagnostic(
                "TEMPORAL_WORKSTREAM_GRAPH_DEFERRED",
                "",
                "Workstream cycle/readiness validation requiring an explicit time is deferred to task-scoped validation.",
                severity=DiagnosticSeverity.INFO,
            ))
        elif not (duplicate_ids & graph_ids):
            try:
                build_workstream_graph(
                    workstream_sources,
                    snapshot_mode=snapshot.mode,
                    context_sources=contexts,
                )
            except WorkstreamValidationError as error:
                diagnostics.extend(error.diagnostics)

    # G006 owns identity-transition semantics. Temporal applicability changes
    # only at authored half-open interval boundaries, so validating one state
    # before the first boundary plus every boundary covers every distinct
    # representable temporal state without inventing a wall-clock "now".
    identity_sources = tuple(
        source for source in known
        if source.profile != Profile.IDENTITY_TRANSITION and source.semantic_id is not None
    )
    transition_sources = tuple(
        source for source in known if source.profile == Profile.IDENTITY_TRANSITION
    )
    if identity_sources or transition_sources:
        transitions = tuple(transition_from_source(source) for source in transition_sources)
        boundaries = {
            _time_value(source, field)
            for source in (*identity_sources, *transition_sources)
            for field in _TEMPORAL_FIELDS
            if field in source.declaration.fields
        }
        evaluation_times = (
            (None,)
            if not boundaries
            else (datetime.min.replace(tzinfo=timezone.utc), *sorted(boundaries))
        )
        for at_time in evaluation_times:
            try:
                build_identity_index(
                    identity_sources,
                    transitions,
                    snapshot_mode=snapshot.mode,
                    at_time=at_time,
                )
            except IdentityValidationError as error:
                diagnostics.extend(error.diagnostics)

    return ProjectValidationResult(base, _ordered_diagnostics(diagnostics))
