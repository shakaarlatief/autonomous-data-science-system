"""G013 complete-result equivalence over the frozen G010 production corpus.

The extra views use the accepted inventory unit with ordinary G009 selectors;
there is no toy compute implementation or new canonical fixture authority.
"""

from dataclasses import asdict, replace
import json
from pathlib import Path
import subprocess
import sys

import pytest

from tests.unit.test_project_knowledge_current_state_core import (
    ACTIVE, PAUSED, ROOT, FIXTURES, core_repo, corpus,
)
from tests.unit.test_project_knowledge_views import git, write, commit
from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.identity import build_identity_index, transition_from_source
from tools.project_knowledge.model import AuthorityClass, Profile, SnapshotMode, ViewInputSelector, ViewSpecification
from tools.project_knowledge.services import refresh
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge.view_definitions import current_state_core_specification, source_inventory_specification
from tools.project_knowledge.views import ViewValidationError, deterministic_json


@pytest.fixture
def refresh_repo(core_repo):
    # Subprocess provenance regressions import this actual fixture tree.
    path = "tools/project_knowledge/services/refresh.py"
    write(core_repo, path, (ROOT / path).read_bytes())
    commit(core_repo)
    return core_repo


def specifications():
    inventory = source_inventory_specification()
    def subset(name, selector):
        return replace(inventory, view_id=name, selector=selector,
                       view_path=f"docs/project_knowledge/generated/{name}.json",
                       manifest_path=f"docs/project_knowledge/generated/manifests/{name}.json")
    return (current_state_core_specification(),
            subset("work_inventory", ViewInputSelector(profiles=(Profile.WORKSTREAM,), prefixes=("docs/work",))),
            subset("semantic_inventory", ViewInputSelector(profiles=(Profile.SEMANTIC_SOURCE,))))


def head(root):
    return git(root, "rev-parse", "HEAD").decode().strip()


def update(root, path, action):
    value = json.loads((root / path).read_bytes())
    action(value)
    write(root, path, deterministic_json(value))


def note(sid="NOTE:EXTRA", authority="canonical"):
    return {"schema_version": "1", "profile": "semantic_source.v1", "kind": "NOTE",
            "authority_class": authority, "semantic_id": sid}


def assert_equivalent(root, previous, specs, expected, *, old_specs=None, prior_builds=None, fallback=False):
    old_specs = specs if old_specs is None else old_specs
    current = head(root)
    result = refresh.refresh_views(root, previous, current, specs, previous_specifications=old_specs)
    full = generate_views(commit_snapshot(root, current), specs)
    assert result.plan.affected_view_ids == tuple(sorted(expected))
    assert result.plan.previous_commit == previous and result.plan.current_commit == current
    assert result.plan.full_fallback is fallback
    # Dataclass equality covers every field: view ID/path, manifest path,
    # bytes, complete manifest (including binding/boundary), and manifest bytes.
    assert result.builds == tuple(b for b in full if b.view_id in expected)
    if prior_builds is not None:
        old = {b.view_id: b for b in prior_builds}
        for build in full:
            if build.view_id not in expected:
                assert build == old[build.view_id]
    return result, full


@pytest.mark.parametrize("case,expected", [
    ("unchanged", ()),
    ("modify", ("current_state_core", "work_inventory")),
    ("create", ("current_state_core", "semantic_inventory")),
    ("delete", ("current_state_core", "work_inventory")),
    ("enter_prefix", ("current_state_core", "work_inventory")),
    ("leave_prefix", ("current_state_core", "work_inventory")),
    ("rename", ("current_state_core", "work_inventory")),
    ("profile", ("current_state_core", "semantic_inventory")),
    ("promote_candidate", ("current_state_core", "semantic_inventory")),
    ("demote_canonical", ("current_state_core", "semantic_inventory")),
    ("multiple", ("current_state_core", "work_inventory", "semantic_inventory")),
    ("unrelated", ()),
    ("undeclared", ()),
    ("capture", ()),
    ("generated", ()),
    ("compatibility", ()),
])
def test_frozen_w0_change_matrix(refresh_repo, case, expected):
    root = refresh_repo
    specs = specifications()
    if case == "enter_prefix":
        (root / ACTIVE).rename(root / "docs/active.json")
        commit(root)
    if case in {"promote_candidate", "demote_canonical"}:
        write(root, "docs/extra.json", deterministic_json(note(authority="candidate" if case == "promote_candidate" else "canonical")))
        commit(root)
    previous = head(root)
    before = generate_views(commit_snapshot(root, previous), specs)
    if case in {"modify", "multiple"}:
        update(root, ACTIVE, lambda d: d["execution_anchor"].update(checkpoint=502))
    if case in {"create", "multiple"}:
        write(root, "docs/extra.json", deterministic_json(note()))
    if case == "delete":
        (root / PAUSED).unlink()
    if case == "enter_prefix":
        (root / "docs/active.json").rename(root / ACTIVE)
    if case == "leave_prefix":
        (root / ACTIVE).rename(root / "docs/active.json")
    if case == "rename":
        (root / ACTIVE).rename(root / "docs/work/zzz-carrier.json")
    if case == "profile":
        update(root, "docs/research-stage.json", lambda d: d.update(profile="project_boundary.v1"))
    if case in {"promote_candidate", "demote_canonical"}:
        update(root, "docs/extra.json", lambda d: d.update(authority_class="canonical" if case == "promote_candidate" else "candidate"))
    if case == "unrelated":
        write(root, "assets/unrelated.txt", b"unrelated change\n")
    if case == "undeclared":
        write(root, "docs/ordinary.md", b"Ordinary undeclared prose\n")
    if case == "capture":
        write(root, "docs/project_knowledge/captures/open/capture.json", deterministic_json({
            "schema_version": "1", "profile": "capture.v1", "kind": "observation",
            "authority_class": "capture", "summary": "Unreviewed capture is never input authority",
        }))
    if case == "generated":
        write(root, "docs/project_knowledge/generated/current_state_core.json", b"\xffpoisoned old state")
        # Generated files are intentionally ignored by the root fixture policy.
        git(root, "add", "-f", "docs/project_knowledge/generated/current_state_core.json")
    if case == "compatibility":
        write(root, "docs/CURRENT_STATE.md", b"\xffnot an input")
    if case != "unchanged":
        commit(root)
    result, full = assert_equivalent(root, previous, specs, expected, prior_builds=before)
    if case == "modify":
        core = json.loads(next(b for b in result.builds if b.view_id == "current_state_core").view_bytes)
        assert core["active_workstream"]["execution_anchor"]["checkpoint"] == 502
        assert core["integration_boundary"]["promoted_commit"] == corpus()["docs/boundary.json"]["promoted_commit"]
        assert core["paused_workstreams"]  # unchanged inputs still present
    if case in {"rename", "enter_prefix", "leave_prefix"}:
        assert next(b for b in full if b.view_id == "current_state_core").view_bytes == before[0].view_bytes
    if case == "unchanged":
        assert before[0].view_bytes == (FIXTURES / "expected_core.json").read_bytes()


def test_repeated_and_permuted_specifications_have_identical_plans_and_results(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    update(root, ACTIVE, lambda d: d["execution_anchor"].update(checkpoint=503))
    commit(root)
    first = refresh.refresh_views(root, previous, "HEAD", specs, previous_specifications=specs)
    assert refresh.refresh_views(root, previous, "HEAD", specs, previous_specifications=specs) == first
    assert refresh.refresh_views(root, previous, "HEAD", specs[::-1], previous_specifications=specs[::-1]) == first


def test_selector_and_execution_contract_changes_without_repository_change(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    changed = (specs[0], replace(specs[1], selector=ViewInputSelector(profiles=(Profile.WORKSTREAM,))), specs[2])
    # Even with equal membership, the declared selection boundary changes.
    assert_equivalent(root, previous, changed, ("work_inventory",), old_specs=specs)
    inventory_files = source_inventory_specification().generator.implementation_files
    changed_core = replace(
        specs[0], compute="source_inventory.v1",
        generator=replace(specs[0].generator, implementation_files=inventory_files),
    )
    changed = (changed_core, *specs[1:])
    assert_equivalent(root, previous, changed, ("current_state_core",), old_specs=specs)


def test_selector_authority_class_change_is_bound_even_when_membership_is_equal(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    original = specs[1]
    changed_selector = replace(
        original.selector,
        authority_classes=(AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL),
    )
    changed = (specs[0], replace(original, selector=changed_selector), specs[2])

    result, full = assert_equivalent(
        root, previous, changed, (original.view_id,), old_specs=specs
    )
    assert result.plan.full_fallback is False
    assert result.plan.reasons == ((original.view_id, "DEPENDENCY_BINDING_CHANGED"),)
    selected, = result.builds
    assert selected == next(build for build in full if build.view_id == original.view_id)


def test_historical_source_change_affects_only_view_that_declares_historical_inputs(refresh_repo):
    root = refresh_repo
    specs = specifications()
    historical_selector = replace(
        specs[1].selector,
        authority_classes=(AuthorityClass.CANONICAL, AuthorityClass.HISTORICAL),
    )
    scoped = (specs[0], replace(specs[1], selector=historical_selector), specs[2])
    previous = head(root)

    historical = corpus()[PAUSED].copy()
    historical.update(
        authority_class="historical",
        semantic_id="HISTORY:WORKSTREAM",
        state="SUPERSEDED",
        expected_to_resume=False,
    )
    historical.pop("pause_reason", None)
    historical.pop("return_condition", None)
    historical.pop("resume_target", None)
    historical.pop("governing_procedure", None)
    historical.pop("orientation_milestones", None)
    write(root, "docs/work/history.json", deterministic_json(historical))
    commit(root)

    result, _ = assert_equivalent(
        root, previous, scoped, (specs[1].view_id,), old_specs=scoped
    )
    assert result.plan.reasons == ((specs[1].view_id, "DEPENDENCY_BINDING_CHANGED"),)


def test_manifest_output_relocation_selects_only_that_view_and_matches_full_build(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    moved_path = "docs/project_knowledge/generated/manifests/work_inventory_moved.json"
    changed = (specs[0], replace(specs[1], manifest_path=moved_path), specs[2])

    result, full = assert_equivalent(root, previous, changed, ("work_inventory",), old_specs=specs)

    assert result.plan.full_fallback is False
    assert result.plan.reasons == (("work_inventory", "DEPENDENCY_BINDING_CHANGED"),)
    selected, = result.builds
    corresponding = next(build for build in full if build.view_id == "work_inventory")
    assert selected == corresponding
    assert selected.manifest_path == moved_path
    assert selected.view_path == corresponding.view_path
    assert selected.view_bytes == corresponding.view_bytes
    assert selected.manifest == corresponding.manifest
    assert selected.manifest_bytes == corresponding.manifest_bytes


def test_every_view_specification_field_is_covered_by_the_impact_contract():
    # Manifest fields include the selection/execution boundary. Durable unit
    # names are data aliases whose identities are set by ViewSpecification.
    manifest_bound = {
        "view_id", "view_path", "view_schema_version", "rebuildability_class",
        "selector", "generator", "compute_identity", "serialize_identity",
    }
    execution_aliases = {"compute", "serialize"}
    impact_envelope = {"manifest_path"}
    assert set(ViewSpecification.__dataclass_fields__) == (
        manifest_bound | execution_aliases | impact_envelope
    )
    for spec in specifications():
        assert type(spec.compute) is str and spec.compute_identity == spec.compute
        assert type(spec.serialize) is str and spec.serialize_identity == spec.serialize


def test_selector_filter_order_is_not_impact(refresh_repo):
    specs = specifications()
    selector = ViewInputSelector(profiles=(Profile.WORKSTREAM, Profile.SEMANTIC_SOURCE), prefixes=("docs/work", "docs"))
    before = (replace(specs[1], selector=selector),)
    after = (replace(before[0], selector=replace(selector, profiles=selector.profiles[::-1], prefixes=selector.prefixes[::-1])),)
    assert_equivalent(refresh_repo, head(refresh_repo), after, (), old_specs=before)


def test_ordered_paths_are_explicit_meaningful_contract(refresh_repo):
    original = specifications()[1]
    before = (replace(original, selector=ViewInputSelector(ordered_paths=(ACTIVE, PAUSED))),)
    after = (replace(original, selector=ViewInputSelector(ordered_paths=(PAUSED, ACTIVE))),)
    result, _ = assert_equivalent(refresh_repo, head(refresh_repo), after, (original.view_id,), old_specs=before)
    assert result.plan.reasons == ((original.view_id, "DEPENDENCY_BINDING_CHANGED"),)


@pytest.mark.parametrize("case", ["malformed", "duplicate_identity", "private_path", "capture_authority", "missing_required_owner"])
def test_global_admission_and_semantic_failures_remain_visible(refresh_repo, case):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    if case == "malformed":
        write(root, "docs/outside-all-narrow-selectors.json", b'{"profile":"semantic_source.v1"')
    elif case == "duplicate_identity":
        write(root, "docs/duplicate.json", deterministic_json(note(corpus()[ACTIVE]["semantic_id"])))
    elif case == "private_path":
        value = note()
        value["provenance"] = ["/home/private-user/secret/state"]
        write(root, "docs/private-leak.json", deterministic_json(value))
    elif case == "capture_authority":
        value = note()
        value["profile"] = "capture.v1"
        write(root, "docs/project_knowledge/captures/open/capture.json", deterministic_json(value))
    else:
        (root / ACTIVE).unlink()
    commit(root)
    plan = refresh.plan_view_refresh(root, previous, "HEAD", specs, previous_specifications=specs)
    if case != "missing_required_owner":
        assert plan.full_fallback and set(plan.affected_view_ids) == {s.view_id for s in specs}
    with pytest.raises(ViewValidationError) as incremental:
        refresh.refresh_views(root, previous, "HEAD", specs, previous_specifications=specs)
    with pytest.raises(ViewValidationError) as full:
        generate_views(commit_snapshot(root, "HEAD"), specs)
    assert {d.code for d in incremental.value.diagnostics} == {d.code for d in full.value.diagnostics}


def test_invalid_baseline_falls_back_to_full_current_state(refresh_repo):
    root = refresh_repo
    specs = specifications()
    write(root, "docs/broken.json", b'{"profile":')
    commit(root)
    previous = head(root)
    (root / "docs/broken.json").unlink()
    commit(root)
    result, _ = assert_equivalent(root, previous, specs, tuple(s.view_id for s in specs), fallback=True)
    assert {reason for _, reason in result.plan.reasons} == {"DEPENDENCY_ANALYSIS_UNAVAILABLE"}


def test_unknown_baseline_contract_falls_back_and_new_removed_views_are_explicit(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    result = refresh.refresh_views(root, previous, "HEAD", specs)
    assert result.plan.full_fallback and result.builds == generate_views(commit_snapshot(root, "HEAD"), specs)
    old = (specs[0], specs[1])
    current = (specs[0], specs[2])
    result, _ = assert_equivalent(root, previous, current, (specs[2].view_id,), old_specs=old)
    assert result.plan.removed_view_ids == (specs[1].view_id,)


def test_g006_same_identity_move_and_authored_transition_are_not_rename_heuristics(refresh_repo):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    identity = corpus()[ACTIVE]["semantic_id"]
    (root / ACTIVE).rename(root / "docs/work/moved.json")
    write(root, "docs/transition.json", deterministic_json({
        "schema_version": "1", "profile": "identity_transition.v1", "kind": "continuity",
        "authority_class": "canonical", "transition_class": "MOVE_OR_RENAME",
        "predecessors": [identity], "successors": [identity],
        "resolution_behavior": "Same authored identity, new carrier", "provenance": ["Reviewed move"],
    }))
    commit(root)
    validation = validate_repository(commit_snapshot(root, "HEAD"))
    assert validation.ok
    transitions = tuple(transition_from_source(s) for s in validation.sources if s.profile == Profile.IDENTITY_TRANSITION)
    build_identity_index(tuple(s for s in validation.sources if s.profile != Profile.IDENTITY_TRANSITION), transitions,
                         snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT)
    assert_equivalent(root, previous, specs, ("current_state_core", "work_inventory"))


def test_private_probes_force_revalidation_at_host_boundary(refresh_repo, monkeypatch):
    root = refresh_repo
    specs = specifications()
    original = refresh.generate_views
    calls = []
    def observe(*args, **kwargs):
        calls.append(kwargs)
        return original(*args, **kwargs)
    # Spy only on the new caller seam. Mutating the attested G009 TCB would
    # correctly fail execution verification before testing the privacy gate.
    monkeypatch.setattr(refresh, "generate_views", observe)
    with pytest.raises(ViewValidationError) as error:
        refresh.refresh_views(root, head(root), "HEAD", specs, previous_specifications=specs,
                              known_private_values=("TARGET_ARCHITECTURE_NOT_SELECTED",))
    assert {d.code for d in error.value.diagnostics} == {"PUBLIC_PRIVATE_VALUE_LEAK"}
    assert len(calls) == 1 and calls[0]["selected_view_ids"] == tuple(sorted(s.view_id for s in specs))


def test_selected_generation_receives_complete_fixed_current_snapshot(refresh_repo, monkeypatch):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    update(root, ACTIVE, lambda d: d["execution_anchor"].update(checkpoint=505))
    current = commit(root)
    original = refresh.generate_views
    calls = []
    def observe(snapshot, definitions, **kwargs):
        calls.append((snapshot, definitions, kwargs))
        # Moving HEAD cannot change the already captured final state.
        write(root, "unrelated.txt", b"later commit")
        commit(root)
        return original(snapshot, definitions, **kwargs)
    monkeypatch.setattr(refresh, "generate_views", observe)
    result = refresh.refresh_views(root, previous, "HEAD", specs, previous_specifications=specs)
    assert len(calls) == 1 and calls[0][0] == current
    assert set(corpus()) <= {e.path for e in calls[0][0].entries}
    assert calls[0][2]["selected_view_ids"] == result.plan.affected_view_ids
    assert result.builds == tuple(b for b in generate_views(current, specs) if b.view_id in result.plan.affected_view_ids)


PROBE = r'''
import json, sys
from pathlib import Path
from tools.project_knowledge.model import ViewSpecification, ViewGenerator, ViewInputSelector
from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.services import refresh
from tools.project_knowledge.services.generation import generate_views
request = json.load(sys.stdin)
def definitions(records):
    return tuple(ViewSpecification(**{**r, 'generator': ViewGenerator(**r['generator']),
                'selector': ViewInputSelector(**r['selector'])}) for r in records)
specs = definitions(request['specs'])
old = definitions(request['old_specs'])
result = {'loaded_from': str(Path(refresh.__file__).resolve())}
try:
    refreshed = refresh.refresh_views(Path.cwd(), request['previous'], 'HEAD', specs, previous_specifications=old)
    full = generate_views(commit_snapshot(Path.cwd(), 'HEAD'), specs)
    result.update(ids=refreshed.plan.affected_view_ids, fallback=refreshed.plan.full_fallback,
                  reasons=refreshed.plan.reasons,
                  versions={b.view_id: json.loads(b.view_bytes)['schema_version'] for b in full},
                  equal=refreshed.builds == tuple(b for b in full if b.view_id in refreshed.plan.affected_view_ids))
except Exception as error:
    result['codes'] = [d.code for d in getattr(error, 'diagnostics', ())]
    if not result['codes']: raise
print(json.dumps(result))
'''


def probe(root, previous, specs, old_specs=None):
    process = subprocess.run([sys.executable, "-B", "-c", PROBE], cwd=root, capture_output=True,
        input=json.dumps({"previous": previous, "specs": [asdict(s) for s in specs],
                          "old_specs": [asdict(s) for s in (old_specs or specs)]}).encode())
    assert process.returncode == 0, process.stderr.decode(errors="replace")
    result = json.loads(process.stdout)
    assert Path(result["loaded_from"]) == (root / "tools/project_knowledge/services/refresh.py").resolve()
    return result


@pytest.mark.parametrize("path", ["tools/project_knowledge/pure_source_inventory.py", "tools/project_knowledge/services/validation.py",
                                 "schemas/project_knowledge/workstream.v1.schema.json"])
def test_committed_implementation_changes_select_exact_consumers_from_executing_fixture(refresh_repo, path):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    # Actual executing schema/TCB/pure bytes come from this changed fixture,
    # never modules accidentally imported from the main checkout.
    if path.endswith(".json"):
        update(root, path, lambda d: d.update(title="G013 exact schema revision"))
    elif path.endswith("pure_source_inventory.py"):
        original = (root / path).read_bytes()
        target = (
            b'return {"schema_version": "1", "authority_class": "derived",\n'
            b'            "sources": [entry(item) for item in inputs]}'
        )
        replacement = (
            b'return {"schema_version": "2", "authority_class": "derived",\n'
            b'            "sources": [entry(item) for item in inputs]}'
        )
        assert original.count(target) == 1
        write(root, path, original.replace(target, replacement))
    else:
        write(root, path, (root / path).read_bytes() + b"\n# G013 exact implementation revision\n")
    commit(root)
    result = probe(root, previous, specs)
    expected = (["semantic_inventory", "work_inventory"]
                if path.endswith("pure_source_inventory.py") else sorted(s.view_id for s in specs))
    assert result["equal"] and result["ids"] == expected
    assert {reason for _, reason in result["reasons"]} == {"IMPLEMENTATION_CLOSURE_CHANGED"}
    if path.endswith("pure_source_inventory.py"):
        assert result["versions"] == {"current_state_core": "1", "semantic_inventory": "2", "work_inventory": "2"}


def test_view_local_implementation_change_does_not_rebuild_other_views(refresh_repo):
    root = refresh_repo
    specs = specifications()
    extra = "tools/project_knowledge/inventory_contract.txt"
    write(root, extra, b"explicit local implementation dependency v1\n")
    specs = (specs[0], replace(specs[1], generator=replace(specs[1].generator,
             implementation_files=specs[1].generator.implementation_files + (extra,))), specs[2])
    commit(root)
    previous = head(root)
    write(root, extra, b"explicit local implementation dependency v2\n")
    commit(root)
    result = probe(root, previous, specs)
    assert result["equal"] and result["ids"] == ["work_inventory"]


def test_uncommitted_executing_drift_cannot_be_misreported_as_no_impact(refresh_repo):
    root = refresh_repo
    previous = head(root)
    path = "tools/project_knowledge/pure_source_inventory.py"
    write(root, path, (root / path).read_bytes().replace(b'"schema_version": "1"', b'"schema_version": "X"'))
    result = probe(root, previous, specifications())
    assert "EXECUTION_IMPLEMENTATION_MISMATCH" in result["codes"]
    assert not {"equal", "ids"} & result.keys()


def test_refresh_is_read_only_and_empty_selection_never_calls_compute(refresh_repo, monkeypatch):
    root = refresh_repo
    specs = specifications()
    previous = head(root)
    captured = {p: (root / p).read_bytes() for p in git(root, "ls-files").decode().splitlines()}
    original = refresh.generate_views
    selections = []
    def observe(snapshot, definitions, **kwargs):
        selections.append(kwargs["selected_view_ids"])
        return original(snapshot, definitions, **kwargs)
    monkeypatch.setattr(refresh, "generate_views", observe)
    result = refresh.refresh_views(root, previous, "HEAD", specs, previous_specifications=specs)
    assert result.builds == () and selections == [()]
    assert all((root / p).read_bytes() == content for p, content in captured.items())
    assert head(root) == previous and git(root, "status", "--porcelain") == b""
    assert not (root / "docs/project_knowledge/generated").exists()
