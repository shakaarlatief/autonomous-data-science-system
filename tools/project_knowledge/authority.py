"""G007: deterministic authority over an explicit, closed candidate corpus.

The caller supplies schema-validated sources selected for the action/target and
explicit verification attestations. Generic semantic sources need no universal
ID or invented action metadata. Declared action classes further restrict them.
No retrieval result expands or orders this corpus. No I/O, clock, or persistence.
"""

from dataclasses import fields, is_dataclass
from datetime import datetime, timezone
from itertools import product
import json
from typing import Iterable, Mapping

from .model import (
    ActionConstraint, ActionContract, AppliedAuthorityRelation, AuthorityClass,
    AuthorityEvidence, AuthorityQuery, AuthorityReceipt, AuthorityRemoval,
    AuthorityResult, AuthoritySource, AuthorityStatus, ConstraintActivation, ConstraintPrecedence,
    Diagnostic, DiagnosticSeverity, Freshness, GovernedSource, LifecycleState,
    PrivateStateEvidence, Profile, RelationMode, Scope, ScopeAssessment,
    ScopeDisposition, SemanticId, SnapshotMode,
)


def _facets(scope: Scope | None) -> dict[str, frozenset[str]]:
    return {key: frozenset((v,) if isinstance(v, str) else v)
            for key, v in (scope.facets.items() if scope else ())}


def match_scope(scope: Scope | None, query: Mapping[str, str | None]) -> ScopeDisposition:
    """None is an internal representative for all other exact literal values."""
    missing = False
    for key, values in _facets(scope).items():
        if key not in query:
            missing = True
        elif query[key] not in values:
            return ScopeDisposition.NO_MATCH
    return ScopeDisposition.UNDERSPECIFIED if missing else ScopeDisposition.MATCH


def _intersection(*scopes: Scope | None) -> dict[str, frozenset[str]]:
    result = {}
    for scope in scopes:
        for key, values in _facets(scope).items():
            result[key] = result.get(key, values) & values
    return result


def _narrower(owner: Scope | None, relation: Scope, base: Scope | None) -> bool:
    child, parent = _intersection(owner, relation), _facets(base)
    return (all(child.values()) and all(key in child and child[key] <= values for key, values in parent.items())
            and child != parent)


class _Failure(Exception):
    def __init__(self, status: AuthorityStatus, code: str, message: str, path: str = ""):
        self.result = AuthorityResult(status, diagnostics=(Diagnostic(code, DiagnosticSeverity.ERROR, path, message),))


def _conflict(code: str, message: str, path: str = "") -> None:
    raise _Failure(AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT, code, message, path)


def _temporal(source: GovernedSource, at_time: datetime | None) -> bool:
    pairs = []
    for start, end in (("effective_from", "effective_to"), ("authority_from", "authority_to")):
        parsed = []
        for name in (start, end):
            value = source.declaration.fields.get(name)
            if value is None:
                parsed.append(None)
                continue
            try:
                instant = datetime.fromisoformat(value.upper().replace("Z", "+00:00"))
                if instant.tzinfo is None or instant.utcoffset() is None:
                    raise ValueError("Timezone required")
                parsed.append(instant.astimezone(timezone.utc))
            except (ValueError, TypeError, AttributeError):
                _conflict("INVALID_AUTHORITY_TIME", f"Invalid {name}", source.carrier_path)
        low, high = parsed
        if low is not None and high is not None and low >= high:
            _conflict("INVALID_AUTHORITY_TIME", "Time interval must be nonempty", source.carrier_path)
        pairs.append((low, high))
    if at_time is None and any(v is not None for pair in pairs for v in pair):
        raise _Failure(AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED, "AUTHORITY_TIME_REQUIRED",
                       "Explicit at_time is required for temporal authority", source.carrier_path)
    return at_time is None or all((lo is None or lo <= at_time) and (hi is None or at_time < hi) for lo, hi in pairs)


def _levels(nodes: Iterable, edges: Iterable[tuple], code: str) -> tuple[tuple, ...]:
    """Topological batches. Sorting within a batch is serialization, not priority."""
    remaining = set(nodes)
    parents = {node: set() for node in remaining}
    for before, after in edges:
        parents[after].add(before)
    levels = []
    while remaining:
        ready = tuple(sorted(node for node in remaining if not (parents[node] & remaining)))
        if not ready:
            _conflict(code, "Explicit authority/constraint dependencies contain a cycle")
        levels.append(ready)
        remaining.difference_update(ready)
    return tuple(levels)


def _components(nodes: Iterable[str], edges: Iterable[tuple[str, str]]) -> list[set[str]]:
    groups = [{node} for node in sorted(nodes)]
    for left, right in sorted(edges):
        matching = [g for g in groups if left in g or right in g]
        merged = set().union(*matching)
        groups = [g for g in groups if g not in matching] + [merged]
    return groups


def _case(candidates, joints, known, facets, at_time, required_ids):
    removed = []
    selected = {}
    for path, source in sorted({**candidates, **joints}.items()):
        if match_scope(source.scope, facets) == ScopeDisposition.NO_MATCH:
            removed.append(AuthorityRemoval(path, "SCOPE_NO_MATCH"))
        elif not _temporal(source, at_time):
            removed.append(AuthorityRemoval(path, "TEMPORALLY_INAPPLICABLE"))
        else:
            selected[path] = source
    ids = {}
    for path, source in selected.items():
        if source.semantic_id is not None:
            if source.semantic_id in ids:
                _conflict("DUPLICATE_CURRENT_AUTHORITY", "Multiple applicable carriers claim one identity", path)
            ids[source.semantic_id] = path
    for sid in sorted(required_ids, key=lambda s: s.value):
        if sid not in ids:
            raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "REQUIRED_AUTHORITY_INAPPLICABLE",
                           f"Required authority does not apply to this scope/time: {sid.value}")
    relations = []
    replacement_edges, supplement_edges = [], []
    for path, source in selected.items():
        for relation in source.relations:
            if match_scope(relation.scope, facets) == ScopeDisposition.NO_MATCH:
                continue
            targets = known.get(relation.target, ())
            if not targets:
                raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "MISSING_RELATION_TARGET",
                               "Supply the explicitly referenced canonical authority", path)
            target_path = ids.get(relation.target)
            if target_path is None:
                if relation.mode == RelationMode.SUPPLEMENT:
                    raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "INAPPLICABLE_SUPPLEMENT_BASE",
                                   "A supplement requires an applicable base", path)
                continue
            target = selected[target_path]
            if relation.mode == RelationMode.SPECIALIZE and not _narrower(source.scope, relation.scope, target.scope):
                _conflict("INVALID_SPECIALIZATION", "SPECIALIZE must declare a strictly narrower compatible scope", path)
            normalized_scope = Scope({k: tuple(sorted(v)) for k, v in _facets(relation.scope).items()}) if relation.scope else None
            relations.append(AppliedAuthorityRelation(path, target_path, relation.mode, normalized_scope))
            if relation.mode == RelationMode.SUPPLEMENT:
                supplement_edges.append((target_path, path))
            else:
                replacement_edges.append((target_path, path))
                removed.append(AuthorityRemoval(target_path, relation.mode.value, path))
    # The natural edge runs from predecessor to successor. All applicable edges
    # take part in closure even when an intermediate predecessor is replaced.
    levels = _levels(selected, replacement_edges, "AUTHORITY_REPLACEMENT_CYCLE")
    next_sources = {path: set() for path in selected}
    for old, new in replacement_edges:
        next_sources[old].add(new)
    final = {}
    for level in reversed(levels):
        for path in level:
            final[path] = set().union(*(final[n] for n in next_sources[path])) if next_sources[path] else {path}
    survivors = set(selected) - {old for old, _ in replacement_edges}
    order = set()
    for base, supplement in supplement_edges:
        # Replacing either endpoint preserves its position in the combination.
        # A successor replacing the entire old bundle collapses that old edge;
        # a surviving owner that both replaces and supplements its base conflicts.
        order.update((current_base, current_supplement)
                     for current_base in final[base] for current_supplement in final[supplement]
                     if current_base != current_supplement or supplement in survivors)
    _levels(survivors, order, "AUTHORITY_SUPPLEMENT_CYCLE")
    ordinary_groups = _components(survivors, order)
    joint_paths, combinations, occupied = [], [], set()
    joint_edges = set(order)
    for path, joint in joints.items():
        if path not in survivors:
            continue
        data = joint.declaration.fields
        member_values = set(data["members"])
        members = {p for p in survivors if p in candidates and selected[p].semantic_id is not None and selected[p].semantic_id.value in member_values}
        admission = data["admission"]
        qualified = (len(members) == len(member_values) >= 2
                     and all(admission.get(key) is True for key in (
                         "overlapping_current_canonical_sources", "ordinary_relations_insufficient",
                         "irreducible_set_fact", "independently_activated", "duplicate_ownership_rejected"))
                     and bool(admission.get("review_evidence")) and bool(data.get("provenance"))
                     and bool(data["combination_semantics"].strip()))
        if not qualified:
            _conflict("UNQUALIFIED_JOINT_AUTHORITY", "J1-J6 require reviewed facts and all members surviving filtering", path)
        if any(members <= group for group in ordinary_groups):
            _conflict("JOINT_ORDINARY_RELATIONS_SUFFICIENT", "Ordinary directional closure already represents this governing set", path)
        membership = frozenset(members)
        if membership in occupied:
            _conflict("DUPLICATE_JOINT_OWNERSHIP", "Multiple joint declarations claim the same member set", path)
        occupied.add(membership)
        # Connectivity is not procedure execution order; joint peers stay peers.
        joint_edges.update((left, right) for left in members for right in members if left != right)
        joint_edges.update((path, member) for member in members)
        joint_paths.append(path)
        combinations.append((path, data["combination_semantics"]))
    if not survivors:
        raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "NO_APPLICABLE_AUTHORITY", "No current canonical authority applies")
    if len(_components(survivors, joint_edges)) != 1:
        _conflict("UNRELATED_GOVERNING_SOURCES", "Multiple sources lack a qualified relation or joint governing set")
    return survivors - set(joint_paths), order, relations, removed, tuple(joint_paths), tuple(combinations), {ids[sid] for sid in required_ids}


def action_contract(source: GovernedSource) -> ActionContract:
    """Project authored machine constraints; never infer constraints from prose."""
    data = source.declaration.fields
    constraints = tuple(ActionConstraint(c["constraint_id"], c["requirement"]) for c in data["mandatory_constraints"])
    if len({c.constraint_id for c in constraints}) != len(constraints):
        _conflict("DUPLICATE_CONSTRAINT_ID", "Constraint identifiers must be unique within their owning procedure", source.carrier_path)
    return ActionContract(source.carrier_path, data["preconditions"], constraints, data["prohibitions"],
                          data["required_postconditions"], data["fail_closed_conditions"])


def _activate(sources, survivors, order):
    contracts = tuple(action_contract(sources[p]) for p in sorted(survivors) if sources[p].profile == Profile.GOVERNING_PROCEDURE)
    nodes, edges, activations = set(), set(), {}
    # Source start/end vertices propagate ordering through non-procedure sources.
    for path in survivors:
        start, end = (path, -1), (path, 10**20)
        nodes.update((start, end))
        chain = [start]
        contract = next((c for c in contracts if c.carrier_path == path), None)
        for i, constraint in enumerate(contract.mandatory_constraints if contract else ()):
            node = (path, i)
            nodes.add(node)
            chain.append(node)
            activations[node] = ConstraintActivation(path, constraint.constraint_id, constraint.requirement)
        chain.append(end)
        edges.update(zip(chain, chain[1:]))
    for before, after in order:
        edges.add(((before, 10**20), (after, -1)))
    _levels(nodes, edges, "AUTHORITY_CONSTRAINT_CYCLE")
    parents = {n: set() for n in nodes}
    for before, after in edges:
        parents[after].add(before)
    precedence = set()
    for node, after in activations.items():
        pending, seen = list(parents[node]), set()
        while pending:
            previous = pending.pop()
            if previous in seen:
                continue
            seen.add(previous)
            if previous in activations:
                before = activations[previous]
                precedence.add((before.carrier_path, before.constraint_id, after.carrier_path, after.constraint_id))
            else:
                pending.extend(parents[previous])
    return (contracts, tuple(activations[n] for n in sorted(activations)),
            tuple(ConstraintPrecedence(*edge) for edge in sorted(precedence)))


def resolve_authority(
    query: AuthorityQuery, candidates: Iterable[GovernedSource], *, snapshot_mode: SnapshotMode,
    joint_authorities: Iterable[GovernedSource] = (), evidence: Iterable[AuthorityEvidence] = (),
    private_evidence: Iterable[PrivateStateEvidence] = (), retrieval_nominations: object = None,
) -> AuthorityResult:
    """Resolve explicit authority. Retrieval is deliberately unread, even if hostile.

    Missing scope facets are partitioned into finite exact-value cells, including
    an OTHER cell. Every explicitly requested cell must have candidate coverage.
    Only hypothetical omitted-facet completions inconsistent with every candidate
    are excluded. A universal candidate keeps OTHER in play. No wildcard meaning
    is assigned to literals such as 'global', 'OTHER' or '*'.

    Joint admission fields attest reviewed J2-J5 facts: this function checks their
    structure and cross-source contradictions; it does not perform semantic review.
    """
    try:
        return _resolve(query, candidates, SnapshotMode(snapshot_mode), joint_authorities, evidence, private_evidence)
    except _Failure as failure:
        return failure.result


def _resolve(query, candidates, mode, joint_authorities, evidence, private_evidence):
    at_time = query.at_time
    if at_time is not None:
        if at_time.tzinfo is None or at_time.utcoffset() is None:
            raise _Failure(AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED, "AUTHORITY_TIME_REQUIRED", "at_time requires an explicit timezone")
        at_time = at_time.astimezone(timezone.utc)
    sources, joints, removed, known, seen_paths, supplied_sources = {}, {}, [], {}, set(), {}
    for joint_input, items in ((False, candidates), (True, joint_authorities)):
        for source in sorted(items, key=lambda s: s.carrier_path):
            path = source.carrier_path
            if path in seen_paths:
                _conflict("DUPLICATE_AUTHORITY_CARRIER", "Supply each authority carrier once", path)
            seen_paths.add(path)
            supplied_sources[path] = source
            if source.authority_class in {AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL} and source.semantic_id is not None:
                known.setdefault(source.semantic_id, []).append(path)
            if source.authority_class != AuthorityClass.CANONICAL:
                removed.append(AuthorityRemoval(path, "NON_CANONICAL"))
                continue
            if source.snapshot_mode != mode:
                _conflict("AUTHORITY_SNAPSHOT_MISMATCH", "All canonical inputs must have one snapshot mode", path)
            if joint_input != (source.profile == Profile.JOINT_AUTHORITY):
                _conflict("AUTHORITY_INPUT_ROLE", "Pass joint declarations through joint_authorities", path)
            if (source.state == LifecycleState.SUPERSEDED
                    or (source.profile == Profile.GOVERNING_PROCEDURE and source.state != LifecycleState.ACTIVE)
                    or (joint_input and source.state in {LifecycleState.PAUSED, LifecycleState.BLOCKED})):
                removed.append(AuthorityRemoval(path, "INACTIVE_LIFECYCLE"))
                continue
            actions = source.declaration.fields.get("governed_action_classes")
            if actions is not None and query.action not in actions:
                removed.append(AuthorityRemoval(path, "ACTION_NO_MATCH"))
                continue
            (joints if joint_input else sources)[path] = source
    current_ids = {source.semantic_id for source in (*sources.values(), *joints.values())}
    for sid in sorted(query.required_authorities, key=lambda s: s.value):
        if sid not in current_ids:
            raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "MISSING_REQUIRED_AUTHORITY", f"Required canonical identity absent: {sid.value}")
    if not sources:
        raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "NO_CANONICAL_CANDIDATES", "Supply current canonical authority candidates")
    supplied = dict(query.scope.facets)
    supplied["target"] = query.target
    for name in ("workstream", "actor"):
        if getattr(query, name) is not None:
            supplied[name] = getattr(query, name)
    # Query scopes may name a finite set; every requested cell must agree too.
    domains = {k: set((v,) if isinstance(v, str) else v) for k, v in supplied.items()}
    requested_keys = sorted(domains)
    requested_cells = tuple(dict(zip(requested_keys, values))
                            for values in product(*(sorted(domains[k]) for k in requested_keys)))
    # Do not treat explicit cells as hypothetical completions. UNDERSPECIFIED
    # here still admits a candidate whose omitted facets can be completed later.
    uncovered = tuple(Diagnostic(
        "NO_APPLICABLE_AUTHORITY", DiagnosticSeverity.ERROR, "",
        "No authority matches explicitly requested scope cell: " + json.dumps(cell, sort_keys=True),
    ) for cell in requested_cells if all(
        match_scope(s.scope, cell) == ScopeDisposition.NO_MATCH for s in sources.values()
    ))
    if uncovered:
        return AuthorityResult(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, diagnostics=uncovered)
    assessments = []
    for path, source in sorted(supplied_sources.items()):
        dispositions = {match_scope(source.scope, cell) for cell in requested_cells}
        disposition = next(iter(dispositions)) if len(dispositions) == 1 else ScopeDisposition.UNDERSPECIFIED
        assessments.append(ScopeAssessment(path, disposition))
    for source in (*sources.values(), *joints.values()):
        for scope in (source.scope, *(r.scope for r in source.relations)):
            for key, values in _facets(scope).items():
                if key not in supplied:
                    domains.setdefault(key, {None}).update(values)
    keys = sorted(domains)
    cases, failures = [], []
    for values in product(*(sorted(domains[k], key=lambda v: (v is None, v or "")) for k in keys)):
        facets = dict(zip(keys, values))
        if not any(match_scope(s.scope, facets) == ScopeDisposition.MATCH for s in sources.values()):
            # Explicit coverage was checked above. This can only discard an
            # incompatible hypothetical completion of omitted facets.
            continue
        try:
            cases.append(_case(sources, joints, known, facets, at_time, query.required_authorities))
        except _Failure as failure:
            failures.append(failure.result)
    signatures = {(frozenset(c[0]), frozenset(c[1]), c[4], c[5]) for c in cases}
    failure_statuses = {f.status for f in failures}
    if len(signatures) > 1 or (cases and failures) or len(failure_statuses) > 1:
        raise _Failure(AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED, "DISCRIMINATING_SCOPE_REQUIRED", "Explicit scope/workstream/actor facets discriminate authority outcomes")
    if failures:
        diagnostics = {(d.code, d.carrier_path, d.message): d for f in failures for d in f.diagnostics}
        return AuthorityResult(failures[0].status, diagnostics=tuple(diagnostics[k] for k in sorted(diagnostics)))
    if not cases:
        raise _Failure(AuthorityStatus.MISSING_REQUIRED_AUTHORITY, "NO_APPLICABLE_AUTHORITY", "No authority matches the explicit target/scope")
    survivors, order, _, _, joint_paths, combinations, _ = cases[0]
    all_relations = {}
    all_removed = {(r.carrier_path, r.reason, r.by_source or ""): r for r in removed}
    for case in cases:
        for relation in case[2]:
            all_relations[json.dumps(_data(relation), sort_keys=True)] = relation
        for removal in case[3]:
            all_removed[(removal.carrier_path, removal.reason, removal.by_source or "")] = removal
    relation_values = tuple(all_relations[k] for k in sorted(all_relations))
    proof_paths = (survivors | set(joint_paths) | {r.owner_path for r in relation_values}
                   | set().union(*(case[6] for case in cases)))
    health = {}
    for item in sorted(evidence, key=lambda e: e.carrier_path):
        if item.carrier_path in health:
            _conflict("DUPLICATE_AUTHORITY_EVIDENCE", "Verification evidence must be unambiguous", item.carrier_path)
        health[item.carrier_path] = item
    all_sources = {**sources, **joints}
    verified = {}
    unavailable, stale = [], []
    for path in sorted(proof_paths):
        source = all_sources[path]
        check = health.get(path, AuthorityEvidence(path))
        if check.available is not True:
            unavailable.append(Diagnostic("AUTHORITY_UNAVAILABLE", DiagnosticSeverity.ERROR, path,
                                          "Required authority availability is not verified"))
        revision_required = query.require_revision or mode == SnapshotMode.COMMIT_SNAPSHOT
        if ((query.require_freshness and check.freshness != Freshness.FRESH)
                or check.freshness == Freshness.STALE
                or (revision_required and source.revision is None)
                or (source.revision is not None and (source.revision.source_path != path or check.verified_revision != source.revision))
                or (check.expected_revision is not None and check.expected_revision != source.revision)
                or (mode == SnapshotMode.WORKTREE_SNAPSHOT and check.verified_revision is not None)):
            stale.append(Diagnostic("AUTHORITY_REVISION_OR_FRESHNESS_UNVERIFIED", DiagnosticSeverity.ERROR, path,
                                    "Required freshness/exact revision binding is stale or unverified"))
        verified[path] = AuthoritySource(source.semantic_id, path, source.revision,
                                         "CURRENT_CANONICAL_SCOPE_TIME_RELATION_CLOSURE", check)
    # Availability failure precedes freshness failure independently of source
    # spelling/order. Report all findings, never select the first sorted failure.
    if unavailable or stale:
        return AuthorityResult(AuthorityStatus.MISSING_REQUIRED_AUTHORITY if unavailable else AuthorityStatus.STALE_REQUIRED_AUTHORITY,
                               diagnostics=tuple(sorted(unavailable + stale, key=lambda d: (d.code, d.carrier_path))))
    private = {}
    for item in private_evidence:
        if item.dependency not in query.required_private_dependencies:
            continue  # Public RESOLVED_PRIVATE facts require no private reinspection.
        if item.dependency in private:
            _conflict("DUPLICATE_PRIVATE_EVIDENCE", "Private verification must be unambiguous")
        private[item.dependency] = item
    for dependency in sorted(query.required_private_dependencies):
        item = private.get(dependency)
        if item is None or item.available is not True or item.freshness != Freshness.FRESH:
            raise _Failure(AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE, "REQUIRED_PRIVATE_STATE_UNAVAILABLE",
                           "Required delegated private state is unavailable, stale or unverified")
    contracts, activations, constraint_order = _activate(all_sources, survivors | set(joint_paths), order)
    receipt = AuthorityReceipt(query, mode, tuple(verified[p] for p in sorted(survivors)),
                               tuple(verified[p] for p in joint_paths),
                               tuple(verified[p] for p in sorted(proof_paths - survivors - set(joint_paths))), combinations, assessments,
                               tuple(all_removed[k] for k in sorted(all_removed)), relation_values,
                               contracts, activations, constraint_order, tuple(private[k] for k in sorted(private)))
    return AuthorityResult(AuthorityStatus.RESOLVED, receipt)


def _data(value):
    if isinstance(value, SemanticId):
        return value.value
    if isinstance(value, Scope):
        return {k: sorted(v) for k, v in sorted(_facets(value).items())}
    if isinstance(value, datetime):
        return value.astimezone(timezone.utc).isoformat()
    if is_dataclass(value):
        return {f.name: _data(getattr(value, f.name)) for f in fields(value)}
    if isinstance(value, (tuple, list)):
        return [_data(v) for v in value]
    return value


def authority_result_data(result: AuthorityResult) -> dict:
    return _data(result)


def serialize_authority_result(result: AuthorityResult) -> bytes:
    return (json.dumps(authority_result_data(result), ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
