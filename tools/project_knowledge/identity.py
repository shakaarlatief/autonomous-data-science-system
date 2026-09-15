"""G006: pure identity continuity, transition validation and in-memory indexing.

No authority/scope resolver, repository discovery, history scan, or persistence.
Sources are already schema-validated. Transition records are projected explicitly
by transition_from_source(); their authored IDs never come from carrier paths.
"""

from collections import deque
from datetime import datetime, timezone
import json
from typing import Iterable

from .model import (
    AuthorityClass, Diagnostic, DiagnosticSeverity, GovernedSource,
    IdentityDisposition, IdentityHistory, IdentityIndex, IdentityResolution,
    IdentityTransition, LifecycleState, Profile, SemanticId, SnapshotMode,
    SubstrateError, TransitionClass, thaw_json,
)


_CONTINUITY = {TransitionClass.MOVE_OR_RENAME, TransitionClass.REPRESENTATION_REPLACEMENT}
_TIMES = ("effective_from", "effective_to", "authority_from", "authority_to")


class IdentityValidationError(SubstrateError):
    """Invalid construction has an explicit unresolved disposition, never an index."""
    disposition = IdentityDisposition.UNRESOLVED

    def __init__(self, diagnostics: Iterable[Diagnostic]):
        self.diagnostics = tuple(sorted(diagnostics, key=lambda d: (
            d.code, d.carrier_path, d.semantic_id.value if d.semantic_id else "", d.message,
        )))
        super().__init__("INVALID_IDENTITY_INDEX", "; ".join(d.message for d in self.diagnostics))


def transition_from_source(source: GovernedSource) -> IdentityTransition:
    """Project schema-validated fields; resolution_behavior remains explanatory text.

    It is retained verbatim, never interpreted as an executable instruction or
    used to guess precedence. Cardinality/conflict checks happen during build.
    """
    if source.profile != Profile.IDENTITY_TRANSITION:
        raise ValueError("Expected identity_transition.v1")
    fields = source.declaration.fields
    return IdentityTransition(
        source, TransitionClass(fields["transition_class"]),
        tuple(SemanticId(value) for value in fields["predecessors"]),
        tuple(SemanticId(value) for value in fields.get("successors", ())),
        fields["resolution_behavior"], tuple(fields["provenance"]),
    )


def _ids(values: Iterable[SemanticId]) -> tuple[SemanticId, ...]:
    return tuple(sorted(set(values), key=lambda sid: sid.value))


def _source_key(source: GovernedSource) -> str:
    # A serialization order only; never used to select an owner/target.
    return json.dumps(_source_data(source), sort_keys=True, ensure_ascii=False)


def _source_data(source: GovernedSource) -> dict:
    revision = source.revision
    return {
        "carrier_path": source.carrier_path,
        "semantic_id": source.semantic_id.value if source.semantic_id else None,
        "authority_class": source.authority_class,
        "profile": source.profile,
        "state": source.state,
        "snapshot_mode": source.snapshot_mode,
        "revision": None if revision is None else {
            "source_path": revision.source_path, "source_commit": revision.source_commit,
            "hash_algorithm": revision.hash_algorithm, "hash_basis": revision.hash_basis,
            "content_digest": revision.content_digest, "snapshot_mode": revision.snapshot_mode,
        },
        "metadata": {key: thaw_json(source.declaration.fields[key]) for key in
                     (*_TIMES, "provenance", "references") if key in source.declaration.fields},
    }


def build_identity_index(
    sources: Iterable[GovernedSource], transitions: Iterable[IdentityTransition] = (), *,
    snapshot_mode: SnapshotMode, at_time: datetime | None = None,
) -> IdentityIndex:
    """Build a complete accepted record set and a flattened current graph.

    Canonical/historical sources form the supplied identity corpus. Candidate,
    evidence, capture and derived sources do not establish identity ownership.
    Canonical transitions apply within explicit half-open time windows; inactive
    records remain in history. Temporal input requires an aware explicit at_time.

    A same-ID move/replacement is a continuity annotation, not a self-loop. Its
    current carrier comes from an unambiguous current source, never from path
    order. Moves/replacements must preserve the same authored endpoint ID.
    Historic carriers stay in history. An explicitly identified transition source
    also owns an ordinary identity, independently of its relation endpoints.

    Multiple simultaneously current owners are rejected unless source state or
    explicit applicability distinguishes them. A self-transition alone cannot
    tell two current owners apart. No opaque provenance text is used to guess.
    """
    snapshot_mode = SnapshotMode(snapshot_mode)
    problems: list[Diagnostic] = []

    def error(code: str, message: str, source: GovernedSource | None = None,
              sid: SemanticId | None = None, related: Iterable[str] = ()) -> None:
        problems.append(Diagnostic(code, DiagnosticSeverity.ERROR,
                                   source.carrier_path if source else "", message, sid,
                                   tuple(sorted(set(related)))))

    def fail() -> None:
        if problems:
            raise IdentityValidationError(problems)

    if at_time is not None:
        if at_time.tzinfo is None or at_time.utcoffset() is None:
            error("IDENTITY_TIME_REQUIRED", "at_time must have an explicit timezone")
            fail()
        at_time = at_time.astimezone(timezone.utc)

    def applies(source: GovernedSource) -> bool:
        if source.snapshot_mode != snapshot_mode:
            error("IDENTITY_SNAPSHOT_MISMATCH", "All identity inputs must belong to the requested snapshot mode", source)
        times = []
        for field in _TIMES:
            value = source.declaration.fields.get(field)
            if value is None:
                times.append(None)
                continue
            try:
                parsed = datetime.fromisoformat(value.upper().replace("Z", "+00:00"))
                if parsed.tzinfo is None or parsed.utcoffset() is None:
                    raise ValueError("timezone required")
                times.append(parsed.astimezone(timezone.utc))
            except (ValueError, TypeError, AttributeError):
                error("INVALID_IDENTITY_TIME", f"Invalid {field}", source)
                times.append(None)
        if any(value is not None for value in times) and at_time is None:
            error("IDENTITY_TIME_REQUIRED", "Temporal identity controls require explicit at_time", source)
        for start, end in ((times[0], times[1]), (times[2], times[3])):
            if start is not None and end is not None and start >= end:
                error("INVALID_IDENTITY_TIME", "Temporal interval must have start before end", source)
        return at_time is None or all(
            (start is None or start <= at_time) and (end is None or at_time < end)
            for start, end in ((times[0], times[1]), (times[2], times[3]))
        )

    corpus: dict[SemanticId, list[GovernedSource]] = {}
    owners: dict[SemanticId, list[GovernedSource]] = {}

    def register_identity(source: GovernedSource, applicable: bool) -> None:
        if source.semantic_id is None:
            return
        corpus.setdefault(source.semantic_id, []).append(source)
        if applicable and source.authority_class == AuthorityClass.CANONICAL and source.state != LifecycleState.SUPERSEDED:
            owners.setdefault(source.semantic_id, []).append(source)

    for source in sources:
        if source.authority_class not in {AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL}:
            continue
        if source.profile == Profile.IDENTITY_TRANSITION:
            error("IDENTITY_TRANSITION_INPUT", "Pass transition records through the typed transitions input", source)
            continue
        if source.semantic_id is None:
            continue
        register_identity(source, applies(source))

    # Admit authored transition-unit identities before checking any endpoints.
    # Retain applicability once, including for single-pass transition iterables.
    accepted_transitions = []
    for transition in transitions:
        source = transition.source
        if source.authority_class not in {AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL}:
            continue
        applicable = applies(source)
        register_identity(source, applicable)
        accepted_transitions.append((transition, applicable))
    for sid, claimed in owners.items():
        if len(claimed) > 1:
            error("DUPLICATE_CURRENT_IDENTITY", "Multiple current sources claim the same semantic identity",
                  sid=sid, related=(s.carrier_path for s in claimed))

    records: dict[str, IdentityTransition] = {}
    active: dict[SemanticId, list[IdentityTransition]] = {sid: [] for sid in corpus}
    annotations: dict[SemanticId, list[IdentityTransition]] = {sid: [] for sid in corpus}
    history_paths: dict[SemanticId, set[str]] = {sid: set() for sid in corpus}
    for transition, applicable in accepted_transitions:
        source = transition.source
        if source.profile != Profile.IDENTITY_TRANSITION:
            error("IDENTITY_TRANSITION_INPUT", "Transition source must use identity_transition.v1", source)
        path = source.carrier_path
        if path in records:
            error("DUPLICATE_TRANSITION_SOURCE", "One carrier cannot declare multiple identity transitions", source)
        records[path] = transition
        pred, succ = transition.predecessors, transition.successors
        kind = transition.transition_class
        if kind == TransitionClass.MERGE:
            valid = len(pred) >= 2 and len(succ) == 1
        elif kind == TransitionClass.SPLIT:
            valid = len(pred) == 1 and len(succ) >= 2
        elif kind == TransitionClass.RETIRE:
            valid = len(pred) >= 1 and not succ
        else:
            valid = len(pred) == len(succ) == 1
        if not valid or len(set(pred)) != len(pred) or len(set(succ)) != len(succ):
            error("INVALID_TRANSITION_MULTIPLICITY", f"Invalid endpoint cardinality for {kind}", source)
        if kind in _CONTINUITY and valid and pred != succ:
            error("CONTINUITY_IDENTITY_CHANGED", "Move/replacement must preserve the same semantic identity", source)
        if not transition.provenance or not transition.resolution_behavior.strip():
            error("MISSING_TRANSITION_PROVENANCE", "Transition needs provenance and explicit resolution behavior", source)
        if source.declaration.fields.get("scope"):
            error("SCOPED_IDENTITY_TRANSITION", "A global identity index cannot apply a scoped transition without an explicit scoped identity contract", source)
        for sid in set((*pred, *succ)):
            if sid not in corpus:
                error("DANGLING_IDENTITY_REFERENCE", "Transition endpoint is absent from the supplied identity corpus", source, sid)
            else:
                history_paths[sid].add(path)
        if not (applicable and source.authority_class == AuthorityClass.CANONICAL
                and source.state not in {LifecycleState.PAUSED, LifecycleState.BLOCKED, LifecycleState.SUPERSEDED}):
            continue
        annotation = kind in _CONTINUITY and len(pred) == len(succ) == 1 and pred == succ
        for sid in pred:
            if sid in corpus:
                (annotations if annotation else active)[sid].append(transition)
    for sid, outgoing in active.items():
        if len(outgoing) > 1:
            error("CONFLICTING_IDENTITY_TRANSITIONS", "Identity has incompatible simultaneous outgoing transitions",
                  sid=sid, related=(t.source.carrier_path for t in outgoing))
    fail()

    # Topological construction is iterative; deep chains do not require a Python
    # recursion stack. Lexical order affects serialization only, never priority.
    edges = {sid: set(active[sid][0].successors) if active[sid] else set() for sid in corpus}
    parents = {sid: set() for sid in corpus}
    for sid, successors in edges.items():
        for target in successors:
            parents[target].add(sid)
    indegree = {sid: len(incoming) for sid, incoming in parents.items()}
    ready = deque(_ids(sid for sid, degree in indegree.items() if degree == 0))
    ordered = []
    lineage = {sid: set() for sid in corpus}
    while ready:
        sid = ready.popleft()
        ordered.append(sid)
        for target in _ids(edges[sid]):
            lineage[target].update(lineage[sid] | {sid})
            indegree[target] -= 1
            if indegree[target] == 0:
                ready.append(target)
    if len(ordered) != len(corpus):
        error("IDENTITY_TRANSITION_CYCLE", "Active identity transitions contain a cycle; current lookup cannot be flattened",
              related=(t.source.carrier_path for sid in corpus if indegree[sid] for t in active[sid]))
        fail()

    current = {}
    dispositions = {
        TransitionClass.MERGE: IdentityDisposition.MERGED,
        TransitionClass.SPLIT: IdentityDisposition.SPLIT,
        TransitionClass.SUPERSEDE: IdentityDisposition.SUPERSEDED,
        TransitionClass.RETIRE: IdentityDisposition.RETIRED,
        TransitionClass.REDIRECT: IdentityDisposition.REDIRECTED,
    }
    for sid in reversed(ordered):
        direct = (*annotations[sid], *active[sid])
        trace = {t.source.carrier_path for t in direct}
        targets, retired = set(), set()
        if active[sid]:
            transition = active[sid][0]
            disposition = dispositions[transition.transition_class]
            if transition.transition_class == TransitionClass.RETIRE:
                retired.add(sid)
            for target in edges[sid]:
                row = current[target]
                targets.update(row.current_targets)
                retired.update(row.retired_targets)
                trace.update(row.transition_paths)
                if not row.current_targets and not row.retired_targets:
                    error("NO_CURRENT_IDENTITY_TARGET", "Transition ends at a historical identity without a current successor or retirement",
                          transition.source, target)
        else:
            disposition = IdentityDisposition.CURRENT if owners.get(sid) else IdentityDisposition.HISTORICAL
            if owners.get(sid):
                targets.add(sid)
        current[sid] = IdentityResolution(
            sid, disposition, _ids(targets), _ids(retired),
            tuple(sorted(t.source.carrier_path for t in direct)), tuple(sorted(trace)),
            _ids(lineage[sid]), any(t.transition_class in _CONTINUITY for t in direct),
            tuple(owners[target][0] for target in _ids(targets)),
        )
    fail()
    history = {sid: IdentityHistory(sid, True, tuple(sorted(corpus[sid], key=_source_key)),
                                    tuple(sorted(history_paths[sid]))) for sid in corpus}
    return IdentityIndex(snapshot_mode, at_time, records, current, history)


def resolve_identity(index: IdentityIndex, semantic_id: SemanticId) -> IdentityResolution:
    """One precomputed mapping lookup; no graph traversal or repository access."""
    return index.current.get(semantic_id, IdentityResolution(semantic_id, IdentityDisposition.UNKNOWN))


def historical_lookup(index: IdentityIndex, semantic_id: SemanticId) -> IdentityHistory:
    return index.history.get(semantic_id, IdentityHistory(semantic_id, False))


def identity_index_data(index: IdentityIndex) -> dict:
    """Purpose-specific value projection for a future derived-view writer."""
    def values(ids):
        return [sid.value for sid in ids]

    return {
        "schema_version": "1", "snapshot_mode": index.snapshot_mode,
        "at_time": index.at_time.isoformat() if index.at_time else None,
        "transitions": [{
            "source": _source_data(t.source), "transition_class": t.transition_class,
            "predecessors": values(_ids(t.predecessors)), "successors": values(_ids(t.successors)),
            "resolution_behavior": t.resolution_behavior, "provenance": list(t.provenance),
        } for _, t in sorted(index.transitions.items())],
        "identities": [{
            "semantic_id": sid.value, "disposition": row.disposition,
            "current_targets": values(row.current_targets), "retired_targets": values(row.retired_targets),
            "direct_transition_paths": list(row.direct_transition_paths),
            "transition_paths": list(row.transition_paths),
            "predecessor_lineage": values(row.predecessor_lineage),
            "continuity_preserved": row.continuity_preserved,
            "current_sources": [_source_data(s) for s in row.current_sources],
            "history": {"sources": [_source_data(s) for s in index.history[sid].sources],
                        "transition_paths": list(index.history[sid].transition_paths)},
        } for sid, row in sorted(index.current.items(), key=lambda item: item[0].value)],
    }


def serialize_identity_index(index: IdentityIndex) -> bytes:
    return (json.dumps(identity_index_data(index), ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
