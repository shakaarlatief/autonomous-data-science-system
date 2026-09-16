"""G008: pure workstream graphs and receipt-based recovery over explicit inputs.

The caller supplies the canonical corpus qualified for its scope/time (G007).
This module never discovers sources, selects authority, evaluates return-condition
prose, resumes work, reads a clock, executes workflow steps, or performs writes.
"""

from collections import deque
from dataclasses import fields, is_dataclass
import json
from typing import Iterable, Mapping

from .model import (
    AuthorityClass, Diagnostic, DiagnosticSeverity, DurableStepReceipt,
    GovernedSource, LifecycleState, PrimaryRouteDisposition, Profile,
    SemanticId, SnapshotMode, SourceRevision, SubstrateError, Workstream,
    WorkstreamBlocker, WorkstreamBranch, WorkstreamGraph, WorkstreamNode,
    WorkflowStep, WorkstreamReadiness, WorkstreamRecovery, WorkstreamRoute, WorkstreamWorkflow,
)


class WorkstreamValidationError(SubstrateError):
    def __init__(self, diagnostics: Iterable[Diagnostic]):
        self.diagnostics = tuple(sorted(diagnostics, key=lambda d: (
            d.code, d.carrier_path, d.semantic_id.value if d.semantic_id else "", d.message,
        )))
        super().__init__("INVALID_WORKSTREAM_INPUT", "; ".join(d.message for d in self.diagnostics))


def _diagnostic(code, message, source=None, sid=None, related=()):
    return Diagnostic(code, DiagnosticSeverity.ERROR, source.carrier_path if source else "", message,
                      sid or (source.semantic_id if source else None), tuple(sorted(set(related))))


def _fail(code, message, source=None):
    raise WorkstreamValidationError((_diagnostic(code, message, source),))


def _ids(values):
    return tuple(sorted(values, key=lambda s: s.value))


def workstream_from_source(source: GovernedSource) -> Workstream:
    """Project authored workstream fields; IDs only come from declared controls."""
    data = source.declaration.fields
    if (source.profile != Profile.WORKSTREAM or source.semantic_id is None or source.state is None
            or data.get("semantic_id") != source.semantic_id.value or data.get("state") != source.state.value):
        _fail("INVALID_WORKSTREAM_SOURCE", "Expected an identified workstream with consistent declared lifecycle", source)
    try:
        parent = SemanticId(data["parent"]) if "parent" in data else None
        dependencies = tuple(SemanticId(value) for value in data.get("depends_on", ()))
        resume = SemanticId(data["resume_target"]) if "resume_target" in data else None
        revision = SourceRevision(**data["expected_revision"]) if "expected_revision" in data else None
    except (ValueError, TypeError) as error:
        _fail("INVALID_WORKSTREAM_CONTROL", str(error), source)
    if len(set(dependencies)) != len(dependencies):
        _fail("DUPLICATE_WORKSTREAM_DEPENDENCY", "Dependency identities must be unique", source)
    for name in ("objective", "objective_reference", "pause_reason", "return_condition", "current_anchor"):
        if name in data and (not isinstance(data[name], str) or not data[name].strip()):
            _fail("INVALID_WORKSTREAM_CONTROL", f"{name} must be nonblank authored text", source)
    if not (data.get("objective") or data.get("objective_reference")):
        _fail("MISSING_WORKSTREAM_OBJECTIVE", "Workstream needs an objective or objective reference", source)
    expected_resume = data.get("expected_to_resume", source.state == LifecycleState.PAUSED)
    if not isinstance(expected_resume, bool):
        _fail("INVALID_PAUSE_CONTRACT", "expected_to_resume must be a boolean", source)
    pause_fields = [data.get("pause_reason"), data.get("return_condition"), resume]
    if ((source.state == LifecycleState.PAUSED and expected_resume) or any(pause_fields)) and not all(pause_fields):
        _fail("INVALID_PAUSE_CONTRACT", "Pause reason, return condition and resume target must form a complete contract", source)
    if revision is not None and revision.source_path != source.carrier_path:
        _fail("INVALID_EXPECTED_REVISION", "Expected revision must identify this workstream carrier", source)
    if source.revision is not None and source.revision.source_path != source.carrier_path:
        _fail("INVALID_WORKSTREAM_REVISION", "Source revision must identify this workstream carrier", source)
    return Workstream(source, source.semantic_id, source.state, data.get("objective"), data.get("objective_reference"),
                      parent, _ids(dependencies), expected_resume, data.get("pause_reason"), data.get("return_condition"),
                      resume, data.get("current_anchor"), revision, data.get("risk_or_reopen_triggers", ()))


def _topological(prerequisites, code, sources):
    """Iterative Kahn traversal; traversal order never selects a route."""
    remaining = {sid: len(edges) for sid, edges in prerequisites.items()}
    children = {sid: [] for sid in prerequisites}
    for sid, edges in prerequisites.items():
        for predecessor in edges:
            children[predecessor].append(sid)
    ready = deque(sid for sid, count in remaining.items() if count == 0)
    ordered = []
    while ready:
        sid = ready.popleft()
        ordered.append(sid)
        for child in children[sid]:
            remaining[child] -= 1
            if remaining[child] == 0:
                ready.append(child)
    if len(ordered) != len(prerequisites):
        raise WorkstreamValidationError((_diagnostic(
            code, "Cycle prevents deterministic closure; remove cyclic edges",
            related=(sources[sid].carrier_path for sid, count in remaining.items() if count),
        ),))
    return ordered


def build_workstream_graph(
    sources: Iterable[GovernedSource], *, snapshot_mode: SnapshotMode,
    context_sources: Iterable[GovernedSource] = (),
) -> WorkstreamGraph:
    """Validate a closed graph and compute lifecycle, dependency and parent closure.

    Explicit non-workstream context sources can close project-parent/resume
    references (as in Q4); they never become dependencies or ready workstreams.
    Readiness requires ACTIVE plus completion of every declared prerequisite in
    dependency closure. Parent links express context only, never prerequisites.
    """
    mode = SnapshotMode(snapshot_mode)
    workstreams, contexts, bindings, excluded, problems = {}, {}, {}, [], []
    for context_input, values in ((False, sources), (True, context_sources)):
        for source in sorted(values, key=lambda s: s.carrier_path):
            if source.authority_class != AuthorityClass.CANONICAL:
                excluded.append(source.carrier_path)
                continue
            if source.snapshot_mode != mode:
                problems.append(_diagnostic("WORKSTREAM_SNAPSHOT_MISMATCH", "All admitted sources require one snapshot mode", source))
            if source.semantic_id is None:
                problems.append(_diagnostic("MISSING_WORKSTREAM_IDENTITY", "Workstream/context identity must be authored", source))
                continue
            if source.semantic_id in bindings:
                problems.append(_diagnostic("DUPLICATE_WORKSTREAM_IDENTITY", "Multiple canonical sources claim one identity",
                                            sid=source.semantic_id, related=(bindings[source.semantic_id].carrier_path, source.carrier_path)))
            bindings[source.semantic_id] = source
            if context_input:
                if source.profile == Profile.WORKSTREAM or source.state == LifecycleState.SUPERSEDED:
                    problems.append(_diagnostic("INVALID_WORKSTREAM_CONTEXT", "Context must be a current non-workstream semantic source", source))
                contexts[source.semantic_id] = source
            else:
                try:
                    workstreams[source.semantic_id] = workstream_from_source(source)
                except WorkstreamValidationError as error:
                    problems.extend(error.diagnostics)
    if problems:
        raise WorkstreamValidationError(problems)
    for sid, workstream in workstreams.items():
        source = workstream.source
        for dependency in workstream.depends_on:
            if dependency == sid:
                problems.append(_diagnostic("WORKSTREAM_SELF_DEPENDENCY", "A workstream cannot require itself", source))
            elif dependency not in workstreams:
                problems.append(_diagnostic("DANGLING_WORKSTREAM_DEPENDENCY", f"Missing canonical workstream dependency: {dependency.value}", source))
        if workstream.parent == sid:
            problems.append(_diagnostic("WORKSTREAM_SELF_PARENT", "A workstream cannot parent itself", source))
        elif workstream.parent is not None and workstream.parent not in bindings:
            problems.append(_diagnostic("DANGLING_WORKSTREAM_PARENT", "Supply the explicitly referenced parent source", source))
        target = workstream.resume_target
        if target is not None:
            if target not in bindings:
                problems.append(_diagnostic("DANGLING_WORKSTREAM_RESUME_TARGET", "Supply the explicitly referenced resume target", source))
            elif workstream.expected_to_resume and bindings[target].state in {LifecycleState.COMPLETED, LifecycleState.SUPERSEDED}:
                problems.append(_diagnostic("INVALID_WORKSTREAM_RESUME_TARGET", "Expected resume target is already completed or superseded", source))
    if problems:
        raise WorkstreamValidationError(problems)
    dependencies = {sid: set(w.depends_on) for sid, w in workstreams.items()}
    dependency_order = _topological(dependencies, "WORKSTREAM_DEPENDENCY_CYCLE", bindings)
    parents = {sid: ({w.parent} if w.parent else set()) for sid, w in workstreams.items()}
    parents.update({sid: set() for sid in contexts})
    parent_order = _topological(parents, "WORKSTREAM_PARENT_CYCLE", bindings)
    closure, parent_paths = {}, {}
    for sid in dependency_order:
        closure[sid] = set(dependencies[sid])
        for dependency in dependencies[sid]:
            closure[sid].update(closure[dependency])
    for sid in parent_order:
        parent = workstreams[sid].parent if sid in workstreams else None
        parent_paths[sid] = (*parent_paths[parent], parent) if parent is not None else ()
    nodes, ready = {}, set()
    for sid in _ids(workstreams):
        workstream = workstreams[sid]
        blockers = tuple(WorkstreamBlocker(dep, workstreams[dep].state, dep in dependencies[sid])
                         for dep in _ids(closure[sid]) if workstreams[dep].state != LifecycleState.COMPLETED)
        if workstream.state == LifecycleState.ACTIVE:
            readiness = WorkstreamReadiness.DEPENDENCY_BLOCKED if blockers else WorkstreamReadiness.RUNNABLE
            if not blockers:
                ready.add(sid)
        else:
            readiness = WorkstreamReadiness(workstream.state.value)
        nodes[sid] = WorkstreamNode(workstream, readiness, frozenset(closure[sid]), parent_paths[sid], blockers)
    # An ancestor is branch context when a ready descendant exists. Distinct
    # maximal ready branches remain peers, irrespective of names or anchors.
    ancestor_context = {ancestor for sid in ready for ancestor in parent_paths[sid]}
    leaves = ready - ancestor_context
    branches = tuple(WorkstreamBranch(sid, (*parent_paths[sid], sid), workstreams[sid].current_anchor,
                                     workstreams[sid].resume_target) for sid in _ids(leaves))
    disposition = (PrimaryRouteDisposition.NO_READY_WORKSTREAM if not ready else
                   PrimaryRouteDisposition.UNIQUE_PRIMARY_ROUTE if len(branches) == 1 else
                   PrimaryRouteDisposition.NO_UNIQUE_PRIMARY_ROUTE)
    route = WorkstreamRoute(disposition, branches[0] if len(branches) == 1 else None, branches)
    return WorkstreamGraph(mode, nodes, contexts, frozenset(ready), route, tuple(sorted(excluded)))


def recover_workstream(workflow: WorkstreamWorkflow, receipts: Iterable[DurableStepReceipt]) -> WorkstreamRecovery:
    """Recover an ordered workflow from a durable completed prefix only.

    Receipt iteration order has no meaning. Unknown, duplicate, stale-definition,
    non-completed or non-prefix receipts fail before any recovery plan is returned.
    The only next-step surface is the first pending step; completed steps are
    never nominated for execution. This function executes nothing.
    """
    problems = []
    if (not isinstance(workflow, WorkstreamWorkflow)
            or not isinstance(workflow.workflow_id, str) or not workflow.workflow_id.strip()
            or not isinstance(workflow.workstream_id, SemanticId) or not workflow.steps
            or not isinstance(workflow.definition_revision, SourceRevision)):
        _fail("INVALID_WORKSTREAM_WORKFLOW", "Workflow requires authored identity, ordered steps and exact definition revision")
    steps = {}
    for step in workflow.steps:
        if not isinstance(step, WorkflowStep) or not isinstance(step.step_id, str) or not step.step_id.strip():
            problems.append(_diagnostic("INVALID_WORKFLOW_STEP", "Every ordered step needs a nonblank authored step identity"))
            continue
        if any(not isinstance(v, str) or not v.strip() for v in (step.step_id, step.operation, step.target)) or not isinstance(step.consequential, bool):
            problems.append(_diagnostic("INVALID_WORKFLOW_STEP", "Step identity, operation and target must be explicit"))
        if step.step_id in steps:
            problems.append(_diagnostic("DUPLICATE_WORKFLOW_STEP", f"Duplicate step: {step.step_id}"))
        steps[step.step_id] = step
    by_step = {}
    for receipt in receipts:
        if not isinstance(receipt, DurableStepReceipt) or not isinstance(receipt.step_id, str) or not receipt.step_id.strip():
            problems.append(_diagnostic("INVALID_WORKFLOW_RECEIPT", "Every durable receipt needs a nonblank authored step identity"))
            continue
        if (receipt.workflow_id != workflow.workflow_id or receipt.workstream_id != workflow.workstream_id
                or receipt.definition_revision != workflow.definition_revision):
            problems.append(_diagnostic("RECEIPT_WORKFLOW_MISMATCH", "Receipt belongs to another workflow, workstream or exact definition revision"))
        if receipt.step_id not in steps:
            problems.append(_diagnostic("UNKNOWN_WORKFLOW_RECEIPT", f"Receipt names unknown step: {receipt.step_id}"))
        if receipt.step_id in by_step:
            problems.append(_diagnostic("DUPLICATE_WORKFLOW_RECEIPT", f"Multiple receipts claim step: {receipt.step_id}"))
        if receipt.status != "COMPLETED":
            problems.append(_diagnostic("UNSUPPORTED_WORKFLOW_RECEIPT", "Only explicit durable COMPLETED receipts establish completion"))
        if (not isinstance(receipt.receipt_revision, SourceRevision) or not receipt.evidence_refs
                or any(not isinstance(ref, str) or not ref.strip() for ref in receipt.evidence_refs)
                or len(set(receipt.evidence_refs)) != len(receipt.evidence_refs)):
            problems.append(_diagnostic("NON_DURABLE_WORKFLOW_RECEIPT", "Receipt needs an exact committed revision and nonempty unique evidence references"))
        by_step[receipt.step_id] = receipt
    if problems:
        raise WorkstreamValidationError(problems)
    count = len(by_step)
    if set(by_step) != {step.step_id for step in workflow.steps[:count]}:
        _fail("NON_PREFIX_WORKFLOW_RECEIPTS", "Completed steps must be a contiguous prefix; omitted earlier work cannot be inferred complete")
    completed, pending = workflow.steps[:count], workflow.steps[count:]
    ordered_receipts = tuple(by_step[step.step_id] for step in completed)
    return WorkstreamRecovery(workflow, completed, pending, pending[0] if pending else None, ordered_receipts)


def _canonical_scope_metadata(value):
    """Canonicalize exact-match scope facets without creating semantic priority."""
    if not isinstance(value, Mapping):
        return _value(value)
    result = {}
    for key, item in value.items():
        values = (item,) if isinstance(item, str) else tuple(item)
        result[key] = sorted(values)
    return result


def _canonical_relation_metadata(value):
    """Canonicalize one unordered relation record for deterministic presentation."""
    if not isinstance(value, Mapping):
        return _value(value)
    result = {}
    for key, item in value.items():
        result[key] = _canonical_scope_metadata(item) if key == "scope" else _value(item)
    return result


def _canonical_source_metadata(source: GovernedSource):
    fields = source.declaration.fields
    metadata = {}
    if "scope" in fields:
        metadata["scope"] = _canonical_scope_metadata(fields["scope"])
    if "relations" in fields:
        relations = [_canonical_relation_metadata(item) for item in fields["relations"]]
        metadata["relations"] = sorted(
            relations, key=lambda item: json.dumps(item, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        )
    for key in ("provenance", "references"):
        if key in fields:
            metadata[key] = sorted(_value(item) for item in fields[key])
    for key in ("effective_from", "effective_to", "authority_from", "authority_to"):
        if key in fields:
            metadata[key] = _value(fields[key])
    return metadata


def _value(value):
    if isinstance(value, SemanticId):
        return value.value
    if isinstance(value, GovernedSource):
        # Binding/provenance only. Machine controls are projected once on Workstream.
        return {"carrier_path": value.carrier_path, "semantic_id": _value(value.semantic_id),
                "authority_class": value.authority_class, "profile": value.profile,
                "state": value.state, "snapshot_mode": value.snapshot_mode, "revision": _value(value.revision),
                "metadata": _canonical_source_metadata(value)}
    if is_dataclass(value):
        return {field.name: _value(getattr(value, field.name)) for field in fields(value)}
    if isinstance(value, Mapping):
        return {_value(key): _value(item) for key, item in value.items()}
    if isinstance(value, (set, frozenset)):
        return [_value(item) for item in _ids(value)]
    if isinstance(value, (tuple, list)):
        return [_value(item) for item in value]
    return value


def workstream_result_data(result: WorkstreamGraph | WorkstreamRecovery) -> dict:
    return _value(result)


def serialize_workstream_result(result: WorkstreamGraph | WorkstreamRecovery) -> bytes:
    return (json.dumps(workstream_result_data(result), sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
