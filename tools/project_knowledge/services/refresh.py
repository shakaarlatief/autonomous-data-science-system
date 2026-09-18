"""G013 read-only impact selection; G009 remains the only generation path.

Both refs are opened as complete immutable Git snapshots. A supplied previous
specification set identifies the comparison contract, not saved generated state.
Without it there is no safe baseline and all current views are selected.

Plans are transient selection results, not durable freshness attestations. This
does not inspect/repair saved outputs, publish artifacts, or implement a CLI.
"""

from pathlib import Path

from ..adapters.gitio import commit_snapshot
from ..model import SubstrateError, ViewRefreshPlan, ViewRefreshResult
from ..views import fail, validate_specifications
from .generation import _execute_bound, generate_views


def _definitions(specifications):
    specs = validate_specifications(specifications)
    if any(type(s.compute) is not str or type(s.serialize) is not str for s in specs):
        fail("UNQUALIFIED_DURABLE_CALLBACK", "Refresh definitions require data-only execution identities")
    return specs


def _plan(previous, current, specifications, previous_specifications):
    specs = _definitions(specifications)
    old_specs = None if previous_specifications is None else _definitions(previous_specifications)
    current_ids = tuple(s.view_id for s in specs)
    old = {} if old_specs is None else {s.view_id: s for s in old_specs}
    removed = tuple(sorted(old.keys() - set(current_ids)))

    def result(reasons, fallback=False):
        return ViewRefreshPlan(previous.source_commit, current.source_commit, tuple(sorted(reasons)),
                               fallback, tuple(sorted(reasons.items())), removed)

    def full(reason):
        return result({identity: reason for identity in current_ids}, True)

    if old_specs is None:
        return full("BASELINE_SPECIFICATIONS_UNAVAILABLE")
    before = {entry.path: (entry.blob_id, entry.git_mode) for entry in previous.entries}
    after = {entry.path: (entry.blob_id, entry.git_mode) for entry in current.entries}
    reasons = {}
    comparable = []
    for spec in specs:
        if spec.view_id not in old:
            reasons[spec.view_id] = "NEW_VIEW"
            continue
        # Compare exact declared closure entries before trying to execute the
        # previous version. An old implementation need not match this checkout.
        paths = set(spec.generator.implementation_files) | set(old[spec.view_id].generator.implementation_files)
        if any(path not in before or path not in after or before[path] != after[path] for path in paths):
            reasons[spec.view_id] = "IMPLEMENTATION_CLOSURE_CHANGED"
        else:
            comparable.append(spec)
    if comparable:
        try:
            ids = tuple(s.view_id for s in comparable)
            prior = _execute_bound(previous, tuple(old[s.view_id] for s in comparable), ids, "dependencies")
            now = _execute_bound(current, tuple(comparable), ids, "dependencies")
        except SubstrateError:
            # Global admission, duplicate identities, missing dependencies,
            # old worker incompatibility, or unbound execution cannot prove
            # non-impact. Normal full generation must succeed or fail visibly.
            return full("DEPENDENCY_ANALYSIS_UNAVAILABLE")
        # Compare the complete dependency/output envelopes produced by the
        # shared binding pass. They include both the G009 manifest binding and
        # its output carrier path, which is not a field of that manifest.
        prior_bindings = {item["view_id"]: item for item in prior["bindings"]}
        now_bindings = {item["view_id"]: item for item in now["bindings"]}
        for identity in ids:
            if prior_bindings[identity] != now_bindings[identity]:
                reasons[identity] = "DEPENDENCY_BINDING_CHANGED"
    return result(reasons)


def plan_view_refresh(root: Path, previous_ref: str, current_ref: str, specifications, *, previous_specifications=None):
    """Compare complete commits; selectors/roles are interpreted only by G009.

    Moves change path bindings even when semantic IDs remain equal. G006
    transition records are ordinary canonical inputs when selected; this seam
    never infers identity continuity from Git rename heuristics or paths.
    """
    previous = commit_snapshot(root, previous_ref)
    current = commit_snapshot(root, current_ref)
    return _plan(previous, current, specifications, previous_specifications)


def refresh_views(root: Path, previous_ref: str, current_ref: str, specifications, *,
                  previous_specifications=None, known_private_values=()):
    """Select affected IDs, then rebuild them from the complete current snapshot.

    Refs are resolved once, so a moving branch cannot change the state between
    analysis and build. Known-private probes remain host-only validation inputs;
    without a prior validation-context receipt they require rechecking all views.
    """
    specs = _definitions(specifications)
    previous = commit_snapshot(root, previous_ref)
    current = commit_snapshot(root, current_ref)
    plan = _plan(previous, current, specs, previous_specifications)
    private_values = ((known_private_values,) if isinstance(known_private_values, (str, bytes))
                      else tuple(known_private_values))
    if private_values:
        ids = tuple(s.view_id for s in specs)
        plan = ViewRefreshPlan(previous.source_commit, current.source_commit, ids, True,
                               tuple((identity, "PUBLIC_VALIDATION_CONTEXT_REQUIRED") for identity in ids),
                               plan.removed_view_ids)
    builds = generate_views(current, specs, selected_view_ids=plan.affected_view_ids,
                            known_private_values=private_values)
    return ViewRefreshResult(plan, builds)
