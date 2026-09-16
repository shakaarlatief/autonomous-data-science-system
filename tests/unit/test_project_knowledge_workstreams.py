"""G008 contract fixtures and explicitly translated, immutable Q4 evidence.

Mutation-seam tests use a verified real Git seed and separate exact-byte
transient versions. Changed copies never claim newly created Git commits.
"""

import ast
from dataclasses import FrozenInstanceError, asdict, replace
import hashlib
import json
from pathlib import Path
import random

import pytest

from tools.project_knowledge.adapters.gitio import read_committed_path
from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.model import (
    AuthorityClass, ConditionalMutationResult, DurableStepReceipt, GovernedSource, LifecycleState,
    PrimaryRouteDisposition, Profile, RawDeclaration, TransientContent, TransientContentVersion,
    SemanticId, SnapshotMode, SourceRevision, WorkflowStep, WorkstreamReadiness,
    WorkstreamUpdateStatus, WorkstreamWorkflow,
)
from tools.project_knowledge.services.workstream_ops import apply_expected_revision_update
from tools.project_knowledge.workstreams import (
    WorkstreamValidationError, build_workstream_graph, recover_workstream,
    serialize_workstream_result, workstream_from_source, workstream_result_data,
)


ROOT = Path(__file__).resolve().parents[2]
Q4 = ROOT / "docs/research/project_knowledge_candidate_01_q4_real_v01"
LOCAL = SnapshotMode.WORKTREE_SNAPSHOT
COMMIT = SnapshotMode.COMMIT_SNAPSHOT
VALIDATOR = SchemaValidator()


def revision(path="docs/workflow.json", content=b"definition", commit="a"):
    return SourceRevision(path, commit * 40, "sha256", "GIT_BLOB_BYTES_AT_COMMIT", hashlib.sha256(content).hexdigest())


def ws(sid, state="ACTIVE", *, dependencies=(), parent=None, authority="canonical", path=None, mode=LOCAL, **controls):
    data = {"schema_version": "1", "profile": "workstream.v1", "kind": "contract-fixture",
            "authority_class": authority, "semantic_id": sid, "state": state, "objective": f"Complete {sid}", **controls}
    if dependencies:
        data["depends_on"] = list(dependencies)
    if parent:
        data["parent"] = parent
    if state == "PAUSED" and data.get("expected_to_resume", True):
        data.setdefault("pause_reason", "Explicit routing pause")
        data.setdefault("return_condition", "Owner explicitly returns")
        data.setdefault("resume_target", sid)
    raw = RawDeclaration(data)
    assert not VALIDATOR.validate(raw), VALIDATOR.validate(raw)
    carrier = path or f"docs/workstreams/{sid}.md"
    return GovernedSource(carrier, Profile.WORKSTREAM, AuthorityClass(authority), data["kind"], raw, mode,
                          SemanticId(sid), revision=revision(carrier) if mode == COMMIT else None, state=LifecycleState(state))


def context(sid, **kwargs):
    unit = ws(sid, **kwargs)
    data = {"schema_version": "1", "profile": "project_boundary.v1", "kind": "explicit-project-context",
            "semantic_id": sid, "authority_class": unit.authority_class.value}
    raw = RawDeclaration(data)
    assert not VALIDATOR.validate(raw)
    return replace(unit, profile=Profile.PROJECT_BOUNDARY, kind=data["kind"], declaration=raw, state=None)


def malformed(unit, **fields):
    return replace(unit, declaration=RawDeclaration({**unit.declaration.fields, **fields}))


def build(units, **kwargs):
    kwargs.setdefault("snapshot_mode", LOCAL)
    return build_workstream_graph(units, **kwargs)


def sid(value):
    return SemanticId(value)


def names(values):
    return {value.value for value in values}


def errors(units, **kwargs):
    with pytest.raises(WorkstreamValidationError) as failure:
        build(units, **kwargs)
    assert all(d.severity == "ERROR" for d in failure.value.diagnostics)
    return {d.code for d in failure.value.diagnostics}


def workflow():
    return WorkstreamWorkflow("TR-1", sid("W"), revision(),
                              tuple(WorkflowStep(f"S{i}", f"operation{i}", f"target{i}") for i in range(1, 6)))


def receipt(flow, step_id, **kwargs):
    data = dict(workflow_id=flow.workflow_id, workstream_id=flow.workstream_id,
                definition_revision=flow.definition_revision, step_id=step_id, status="COMPLETED",
                evidence_refs=(f"docs/evidence/{step_id}.md",), receipt_revision=revision(f"docs/receipts/{step_id}.json"))
    data.update(kwargs)
    return DurableStepReceipt(**data)


def recovery_errors(flow, receipts):
    with pytest.raises(WorkstreamValidationError) as failure:
        recover_workstream(flow, receipts)
    return {d.code for d in failure.value.diagnostics}


def test_projection_preserves_authored_controls_and_exact_revision():
    expected = revision("docs/workstreams/W.md")
    unit = ws("W", "PAUSED", parent="P", dependencies=["D"], current_anchor="checkpoint:529",
              expected_revision=asdict(expected), risk_or_reopen_triggers=["review:changed-scope"])
    result = workstream_from_source(unit)
    assert result.semantic_id is unit.semantic_id
    assert result.parent == sid("P") and result.depends_on == (sid("D"),)
    assert result.expected_to_resume and result.resume_target == sid("W")
    assert result.return_condition == "Owner explicitly returns"
    assert result.current_anchor == "checkpoint:529" and result.expected_revision == expected
    assert result.risk_or_reopen_triggers == ("review:changed-scope",)
    assert result.source is unit


def test_objective_reference_can_replace_inline_objective():
    unit = ws("W", objective_reference="docs/objective.md")
    fields = dict(unit.declaration.fields)
    del fields["objective"]
    result = workstream_from_source(replace(unit, declaration=RawDeclaration(fields)))
    assert result.objective is None and result.objective_reference == "docs/objective.md"


@pytest.mark.parametrize("authority", ["candidate", "historical", "evidence", "capture", "derived"])
def test_noncanonical_inputs_never_enter_current_workstream_graph(authority):
    graph = build([ws("A"), ws("B", authority=authority)])
    assert names(graph.nodes) == {"A"} and names(graph.active_ready_set) == {"A"}
    assert graph.excluded_sources == ("docs/workstreams/B.md",)
    assert "DANGLING_WORKSTREAM_DEPENDENCY" in errors([ws("A", dependencies=["B"]), ws("B", authority=authority)])


def test_duplicate_identity_fails_instead_of_choosing_a_carrier():
    units = [ws("A", path="docs/a.md"), ws("A", path="docs/z.md")]
    diagnostics = []
    for order in (units, units[::-1]):
        with pytest.raises(WorkstreamValidationError) as failure:
            build(order)
        diagnostics.append(failure.value.diagnostics)
    assert diagnostics[0] == diagnostics[1]
    assert diagnostics[0][0].code == "DUPLICATE_WORKSTREAM_IDENTITY"


@pytest.mark.parametrize("kind,expected", [("missing", "DANGLING_WORKSTREAM_DEPENDENCY"),
                                         ("self", "WORKSTREAM_SELF_DEPENDENCY"),
                                         ("cycle", "WORKSTREAM_DEPENDENCY_CYCLE")])
def test_invalid_dependency_edges_fail(kind, expected):
    units = [ws("A", dependencies=["MISSING"])] if kind == "missing" else [ws("A", dependencies=["A"])] if kind == "self" else [
        ws("A", dependencies=["B"]), ws("B", dependencies=["C"]), ws("C", dependencies=["A"])]
    assert expected in errors(units)


@pytest.mark.parametrize("kind,expected", [("missing", "DANGLING_WORKSTREAM_PARENT"),
                                         ("self", "WORKSTREAM_SELF_PARENT"), ("cycle", "WORKSTREAM_PARENT_CYCLE")])
def test_parent_edges_are_validated_separately(kind, expected):
    units = [ws("A", parent="MISSING")] if kind == "missing" else [ws("A", parent="A")] if kind == "self" else [
        ws("A", parent="B"), ws("B", parent="C"), ws("C", parent="A")]
    assert expected in errors(units)


def test_multi_dependency_closure_and_direct_vs_transitive_blockers():
    units = [ws("A", "COMPLETED"), ws("B", "ACTIVE", dependencies=["A"]),
             ws("C", "COMPLETED"), ws("D", dependencies=["B", "C"])]
    graph = build(units)
    assert names(graph.nodes[sid("D")].dependency_closure) == {"A", "B", "C"}
    assert graph.nodes[sid("D")].readiness == WorkstreamReadiness.DEPENDENCY_BLOCKED
    assert [(b.semantic_id.value, b.state, b.direct) for b in graph.nodes[sid("D")].dependency_blockers] == [("B", LifecycleState.ACTIVE, True)]
    assert names(graph.active_ready_set) == {"B"}
    # A completed intermediate does not erase an explicitly incomplete ancestor.
    graph = build([ws("A"), ws("B", "COMPLETED", dependencies=["A"]), ws("C", dependencies=["B"])])
    assert graph.nodes[sid("C")].dependency_blockers[0].direct is False
    assert graph.nodes[sid("C")].readiness == WorkstreamReadiness.DEPENDENCY_BLOCKED


@pytest.mark.parametrize("state,expected", [("ACTIVE", "RUNNABLE"), ("BLOCKED", "BLOCKED"), ("PAUSED", "PAUSED"),
                                         ("COMPLETED", "COMPLETED"), ("SUPERSEDED", "SUPERSEDED")])
def test_lifecycle_is_never_overridden_by_completed_dependencies(state, expected):
    graph = build([ws("D", "COMPLETED"), ws("W", state, dependencies=["D"])])
    assert graph.nodes[sid("W")].readiness == WorkstreamReadiness(expected)
    assert (sid("W") in graph.active_ready_set) == (state == "ACTIVE")
    assert graph.nodes[sid("W")].declared_block == (state == "BLOCKED")


def test_declared_block_and_dependency_block_remain_distinct():
    graph = build([ws("D"), ws("W", "BLOCKED", dependencies=["D"])])
    node = graph.nodes[sid("W")]
    assert node.declared_block and node.readiness == WorkstreamReadiness.BLOCKED
    assert names(b.semantic_id for b in node.dependency_blockers) == {"D"}
    assert build([ws("W", "BLOCKED")]).nodes[sid("W")].dependency_blockers == ()


def test_parent_is_context_and_never_an_implicit_dependency():
    graph = build([ws("P", "PAUSED"), ws("CHILD", parent="P")])
    assert names(graph.active_ready_set) == {"CHILD"}
    assert graph.nodes[sid("CHILD")].dependency_closure == frozenset()
    assert graph.nodes[sid("CHILD")].parent_chain == (sid("P"),)
    # Opposite parent/dependency directions are not a combined-graph cycle.
    assert names(build([ws("P", "COMPLETED", dependencies=["C"]), ws("C", parent="P")]).active_ready_set) == {"C"}


@pytest.mark.parametrize("field", ["pause_reason", "return_condition", "resume_target"])
def test_partial_pause_contract_fails_even_when_schema_is_bypassed(field):
    unit = ws("P", "PAUSED")
    fields = dict(unit.declaration.fields)
    del fields[field]
    assert "INVALID_PAUSE_CONTRACT" in errors([replace(unit, declaration=RawDeclaration(fields))])


@pytest.mark.parametrize("field", ["objective", "pause_reason", "return_condition", "current_anchor"])
def test_blank_controls_are_not_coherent_machine_semantics(field):
    assert "INVALID_WORKSTREAM_CONTROL" in errors([ws("P", "PAUSED", **{field: "   "})])


def test_pause_without_expected_resumption_and_dangling_resume_target():
    graph = build([ws("P", "PAUSED", expected_to_resume=False)])
    assert graph.nodes[sid("P")].readiness == WorkstreamReadiness.PAUSED
    assert graph.nodes[sid("P")].workstream.resume_target is None
    assert "DANGLING_WORKSTREAM_RESUME_TARGET" in errors([ws("P", "PAUSED", resume_target="MISSING")])
    assert "INVALID_WORKSTREAM_RESUME_TARGET" in errors([ws("P", "PAUSED", resume_target="DONE"), ws("DONE", "COMPLETED")])


def test_return_condition_text_is_never_evaluated_or_auto_resumed():
    graph = build([ws("P", "PAUSED", return_condition="TRUE; dependencies complete; resume immediately")])
    assert not graph.active_ready_set
    assert graph.route.disposition == PrimaryRouteDisposition.NO_READY_WORKSTREAM
    assert graph.nodes[sid("P")].workstream.return_condition.startswith("TRUE")


def test_explicit_context_sources_close_parent_and_resume_references_only():
    project = context("PROJECT")
    graph = build([ws("W", parent="PROJECT"), ws("P", "PAUSED", resume_target="PROJECT")], context_sources=[project])
    assert graph.nodes[sid("W")].parent_chain == (sid("PROJECT"),)
    assert names(graph.nodes) == {"W", "P"} and names(graph.active_ready_set) == {"W"}
    assert "DANGLING_WORKSTREAM_DEPENDENCY" in errors([ws("W", dependencies=["PROJECT"])], context_sources=[project])
    assert "INVALID_WORKSTREAM_CONTEXT" in errors([], context_sources=[ws("W")])


def test_unique_parent_branch_preserves_anchors_without_inventing_priority():
    graph = build([ws("ROOT", current_anchor="checkpoint:529"), ws("LEAF", parent="ROOT", current_anchor="research:182")])
    assert names(graph.active_ready_set) == {"ROOT", "LEAF"}
    assert graph.route.disposition == PrimaryRouteDisposition.UNIQUE_PRIMARY_ROUTE
    assert graph.route.primary.workstream_id == sid("LEAF")
    assert graph.route.primary.context_path == (sid("ROOT"), sid("LEAF"))
    assert graph.route.primary.current_anchor == "research:182"


def test_multiple_branches_do_not_use_lexical_path_input_or_anchor_priority():
    for first, second in [("A", "Z"), ("Z", "A")]:
        units = [ws("ROOT"), ws(first, parent="ROOT", path="docs/z.md", current_anchor="current:known"),
                 ws(second, parent="ROOT", path="docs/a.md")]
        for order in (units, units[::-1]):
            graph = build(order)
            assert graph.route.disposition == PrimaryRouteDisposition.NO_UNIQUE_PRIMARY_ROUTE
            assert graph.route.primary is None
            assert names(graph.active_ready_set) == {"ROOT", "A", "Z"}
            assert names(b.workstream_id for b in graph.route.branches) == {"A", "Z"}


def test_paused_resume_metadata_is_retained_when_other_work_has_unique_route():
    graph = build([ws("CURRENT", current_anchor="checkpoint:529"), ws("PAUSED", "PAUSED", resume_target="CURRENT")])
    assert graph.route.primary.workstream_id == sid("CURRENT")
    assert graph.nodes[sid("PAUSED")].workstream.resume_target == sid("CURRENT")
    assert names(graph.active_ready_set) == {"CURRENT"}


def test_deterministic_sources_dependencies_and_serialization():
    units = [ws("ROOT"), ws("A", "COMPLETED", parent="ROOT"), ws("B", "COMPLETED", parent="ROOT"),
             ws("W", parent="ROOT", dependencies=["A", "B"])]
    expected = serialize_workstream_result(build(units))
    for seed in range(15):
        shuffled = units[:]
        random.Random(seed).shuffle(shuffled)
        permuted = [malformed(s, depends_on=list(reversed(s.declaration.fields["depends_on"]))) if "depends_on" in s.declaration.fields else s for s in shuffled]
        assert serialize_workstream_result(build(permuted)) == expected
    assert expected.endswith(b"\n") and b"\r\n" not in expected


def test_unordered_workstream_metadata_and_receipt_evidence_serialize_canonically():
    controls_a = {
        "scope": {"region": ["eu", "us"]},
        "risk_or_reopen_triggers": ["risk:b", "risk:a"],
        "provenance": ["research:2", "research:1"],
        "references": ["path:z", "path:a"],
        "relations": [
            {"mode": "SUPPLEMENT", "target": "BASE-B", "scope": {"region": ["us", "eu"]}},
            {"mode": "REPLACE", "target": "BASE-A"},
        ],
    }
    controls_b = {
        "scope": {"region": ["us", "eu"]},
        "risk_or_reopen_triggers": ["risk:a", "risk:b"],
        "provenance": ["research:1", "research:2"],
        "references": ["path:a", "path:z"],
        "relations": [
            {"mode": "REPLACE", "target": "BASE-A"},
            {"mode": "SUPPLEMENT", "target": "BASE-B", "scope": {"region": ["eu", "us"]}},
        ],
    }
    left = serialize_workstream_result(build([ws("W", **controls_a)]))
    right = serialize_workstream_result(build([ws("W", **controls_b)]))
    assert left == right

    flow = workflow()
    first = receipt(flow, "S1", evidence_refs=("evidence:b", "evidence:a"))
    second = receipt(flow, "S1", evidence_refs=("evidence:a", "evidence:b"))
    assert serialize_workstream_result(recover_workstream(flow, [first])) == serialize_workstream_result(
        recover_workstream(flow, [second])
    )


def test_ordered_workflow_steps_remain_semantically_ordered():
    flow = workflow()
    reordered = replace(flow, steps=(flow.steps[1], flow.steps[0], *flow.steps[2:]))
    original = recover_workstream(flow, [])
    changed = recover_workstream(reordered, [])
    assert [step.step_id for step in original.pending] == ["S1", "S2", "S3", "S4", "S5"]
    assert [step.step_id for step in changed.pending] == ["S2", "S1", "S3", "S4", "S5"]
    assert serialize_workstream_result(original) != serialize_workstream_result(changed)


def test_deep_dependency_and_parent_graphs_are_iterative():
    units = [ws(f"W{i}", "COMPLETED" if i < 1099 else "ACTIVE",
                dependencies=[f"W{i-1}"] if i else (), parent=f"W{i-1}" if i else None) for i in range(1100)]
    graph = build(units[::-1])
    assert len(graph.nodes[sid("W1099")].dependency_closure) == 1099
    assert len(graph.nodes[sid("W1099")].parent_chain) == 1099
    assert names(graph.active_ready_set) == {"W1099"}


def test_immutable_graph_and_empty_graph():
    graph = build([ws("W")])
    with pytest.raises(TypeError):
        graph.nodes[sid("NEW")] = graph.nodes[sid("W")]
    with pytest.raises(FrozenInstanceError):
        graph.nodes[sid("W")].workstream.state = LifecycleState.COMPLETED
    assert build([]).route.disposition == PrimaryRouteDisposition.NO_READY_WORKSTREAM


def test_snapshot_and_expected_revision_semantics_fail_visibly():
    assert "WORKSTREAM_SNAPSHOT_MISMATCH" in errors([ws("W", mode=COMMIT)])
    assert "INVALID_EXPECTED_REVISION" in errors([ws("W", expected_revision=asdict(revision("docs/wrong.md")))])
    bad = malformed(ws("W"), expected_revision={"source_path": "docs/workstreams/W.md"})
    assert "INVALID_WORKSTREAM_CONTROL" in errors([bad])


def test_completed_prefix_recovery_never_returns_completed_work_as_next_step():
    flow = workflow()
    receipts = [receipt(flow, "S2"), receipt(flow, "S1")]
    result = recover_workstream(flow, receipts)
    assert [s.step_id for s in result.completed] == ["S1", "S2"]
    assert [s.step_id for s in result.pending] == ["S3", "S4", "S5"]
    assert result.next_resume_step.step_id == "S3" and not result.blind_replay_required
    assert not set(result.completed) & set(result.pending)
    assert serialize_workstream_result(result) == serialize_workstream_result(recover_workstream(flow, receipts[::-1]))


def test_empty_receipts_and_fully_completed_workflow():
    flow = workflow()
    assert recover_workstream(flow, []).next_resume_step == flow.steps[0]
    result = recover_workstream(flow, [receipt(flow, s.step_id) for s in flow.steps])
    assert result.pending == () and result.next_resume_step is None


@pytest.mark.parametrize("steps", [["S2"], ["S1", "S3"], ["S1", "S2", "S5"]])
def test_skipped_prefix_steps_cannot_be_inferred_complete(steps):
    flow = workflow()
    assert "NON_PREFIX_WORKFLOW_RECEIPTS" in recovery_errors(flow, [receipt(flow, s) for s in steps])


@pytest.mark.parametrize("bad,expected", [
    ({"step_id": "UNKNOWN"}, "UNKNOWN_WORKFLOW_RECEIPT"),
    ({"workflow_id": "OTHER"}, "RECEIPT_WORKFLOW_MISMATCH"),
    ({"workstream_id": SemanticId("OTHER")}, "RECEIPT_WORKFLOW_MISMATCH"),
    ({"status": "FAILED"}, "UNSUPPORTED_WORKFLOW_RECEIPT"),
    ({"status": "PENDING"}, "UNSUPPORTED_WORKFLOW_RECEIPT"),
    ({"evidence_refs": ()}, "NON_DURABLE_WORKFLOW_RECEIPT"),
    ({"evidence_refs": (" ",)}, "NON_DURABLE_WORKFLOW_RECEIPT"),
    ({"receipt_revision": None}, "NON_DURABLE_WORKFLOW_RECEIPT"),
])
def test_malformed_receipts_fail(bad, expected):
    flow = workflow()
    base = receipt(flow, "S1")
    assert expected in recovery_errors(flow, [replace(base, **bad)])


def test_duplicate_contradictory_receipts_and_changed_definition_fail():
    flow = workflow()
    done = receipt(flow, "S1")
    assert "DUPLICATE_WORKFLOW_RECEIPT" in recovery_errors(flow, [done, done])
    assert {"DUPLICATE_WORKFLOW_RECEIPT", "UNSUPPORTED_WORKFLOW_RECEIPT"} <= recovery_errors(flow, [done, replace(done, status="FAILED")])
    changed = replace(flow, definition_revision=replace(flow.definition_revision, source_commit="b" * 40))
    assert "RECEIPT_WORKFLOW_MISMATCH" in recovery_errors(changed, [done])
    assert "DUPLICATE_WORKFLOW_STEP" in recovery_errors(replace(flow, steps=(flow.steps[0], flow.steps[0])), [])


@pytest.mark.parametrize("bad_id", [[], None, " "])
def test_invalid_step_and_receipt_identities_fail_with_diagnostics(bad_id):
    flow = workflow()
    invalid_step = replace(flow.steps[0], step_id=bad_id)
    assert "INVALID_WORKFLOW_STEP" in recovery_errors(replace(flow, steps=(invalid_step,)), [])
    assert "INVALID_WORKFLOW_RECEIPT" in recovery_errors(flow, [replace(receipt(flow, "S1"), step_id=bad_id)])


def test_untyped_recovery_inputs_fail_with_diagnostics():
    flow = workflow()
    assert "INVALID_WORKSTREAM_WORKFLOW" in recovery_errors(None, [])
    assert "INVALID_WORKFLOW_STEP" in recovery_errors(replace(flow, steps=(None,)), [])
    assert "INVALID_WORKFLOW_RECEIPT" in recovery_errors(flow, [None])


def test_receipt_diagnostics_are_order_independent_and_interruption_is_isolated():
    flow = workflow()
    invalid = [receipt(flow, "S2"), receipt(flow, "S2", status="FAILED"), receipt(flow, "UNKNOWN")]
    failures = []
    for receipts in (invalid, invalid[::-1]):
        with pytest.raises(WorkstreamValidationError) as failure:
            recover_workstream(flow, receipts)
        failures.append(failure.value.diagnostics)
    assert failures[0] == failures[1]
    receipts = (receipt(flow, "S1"), receipt(flow, "S2"))
    graph = build([ws("W"), ws("COCKPIT", "PAUSED")])
    before = serialize_workstream_result(graph), serialize_workstream_result(recover_workstream(flow, receipts))
    assert graph.nodes[sid("COCKPIT")].workstream.resume_target == sid("COCKPIT")
    after = serialize_workstream_result(graph), serialize_workstream_result(recover_workstream(flow, receipts))
    assert before == after


@pytest.fixture(scope="module")
def committed_seed():
    fixture = json.loads((Q4 / "Q4_REAL_FIXTURE_V01.json").read_text())
    case = next(c for c in fixture["stress_cases"] if c["case_id"] == "Q4-R03")
    base = SourceRevision(**dict(case["base_revision"], hash_algorithm="sha256"))
    blob = read_committed_path(ROOT, base.source_commit, base.source_path)
    assert hashlib.sha256(blob).hexdigest() == base.content_digest
    return TransientContent(TransientContentVersion(base, base.content_digest), blob)


def changed_copy(seed, content):
    return TransientContent(TransientContentVersion(seed.version.base_revision, hashlib.sha256(content).hexdigest()), content)


class ConditionalStore:
    """Single-threaded test store; races are scheduled before its indivisible CAS.

    A real concurrent store must implement this contract with its own atomic
    conditional-write primitive. This fixture is not a multithreaded adapter.
    """
    def __init__(self, current):
        self.current = current
        self.events = []
        self.mutations = 0

    def compare_and_swap(self, expected, replacement):
        before = self.current
        self.events.append("compare")
        if before.version != expected:
            return ConditionalMutationResult(WorkstreamUpdateStatus.REJECTED_STALE_REVISION, before, before)
        self.events.append("mutate")
        self.current = replacement
        self.mutations += 1
        return ConditionalMutationResult(WorkstreamUpdateStatus.APPLIED, before, self.current)


def test_fresh_stale_then_fresh_updates_guard_at_mutation(committed_seed):
    base = committed_seed
    next_value = changed_copy(base, b"next")
    final = changed_copy(base, b"final")
    store = ConditionalStore(base)
    fresh = apply_expected_revision_update(base.version, next_value, compare_and_swap=store.compare_and_swap)
    assert fresh.status == WorkstreamUpdateStatus.APPLIED and fresh.mutation_applied
    assert store.events == ["compare", "mutate"] and store.mutations == 1
    store.events.clear()
    before = store.current
    stale = apply_expected_revision_update(base.version, final, compare_and_swap=store.compare_and_swap)
    assert stale.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION and not stale.mutation_applied
    assert store.events == ["compare"] and store.mutations == 1 and store.current == before
    assert stale.before_version == stale.after_version == next_value.version
    store.events.clear()
    fresh_again = apply_expected_revision_update(next_value.version, final, compare_and_swap=store.compare_and_swap)
    assert fresh_again.status == WorkstreamUpdateStatus.APPLIED and fresh_again.mutation_applied
    assert store.events == ["compare", "mutate"] and store.mutations == 2
    assert store.current == final
    # Both updates retain the real immutable Git seed; neither invents a commit.
    assert fresh.after_version.base_revision is base.version.base_revision
    assert fresh_again.after_version.base_revision is base.version.base_revision
    assert fresh_again.after_version.content_digest != base.version.base_revision.content_digest
    assert not isinstance(fresh_again.after_version, SourceRevision)
    assert not hasattr(fresh_again.after_version, "source_commit")


@pytest.mark.parametrize("race_at", ["observation_return", "cas_entry"])
def test_concurrent_writer_between_observation_and_mutation_is_preserved(committed_seed, race_at):
    base = committed_seed
    store = ConditionalStore(base)
    concurrent = changed_copy(base, b"concurrent writer")
    replacement = changed_copy(base, b"stale writer")

    def concurrent_writer():
        applied = apply_expected_revision_update(base.version, concurrent, compare_and_swap=store.compare_and_swap)
        assert applied.status == WorkstreamUpdateStatus.APPLIED

    def preflight_observation():
        observed = store.current.version
        if race_at == "observation_return":
            concurrent_writer()  # The observation becomes stale before returning.
        return observed

    def mutation_boundary(expected, value):
        if race_at == "cas_entry":
            concurrent_writer()  # Advances AFTER the service's request validation.
        previous_mutations = store.mutations
        result = store.compare_and_swap(expected, value)
        assert store.mutations == previous_mutations  # Zero mutation by stale writer.
        return result

    expected = preflight_observation()
    assert expected == base.version
    result = apply_expected_revision_update(expected, replacement, compare_and_swap=mutation_boundary)
    assert result.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION
    assert not result.mutation_applied and store.mutations == 1
    assert store.current == concurrent and store.current.content == b"concurrent writer"
    assert store.events == ["compare", "mutate", "compare"]


@pytest.mark.parametrize("field", ["source_commit", "source_path", "content_digest", "transient_digest"])
def test_complete_expected_version_comparison(committed_seed, field):
    base = committed_seed
    if field == "transient_digest":
        expected = changed_copy(base, b"different observation").version
    else:
        # Deliberately tampered request descriptors, never installed store state
        # or asserted durable evidence.
        # Even the alternate commit is a real accepted commit, not a version counter.
        changes = {"source_commit": "7cb32f2725fb43617c325b5c450ca68854cdac41",
                   "source_path": "docs/CURRENT_STATE.md", "content_digest": "0" * 64}
        altered_seed = replace(base.version.base_revision, **{field: changes[field]})
        expected = replace(base.version, base_revision=altered_seed)
    assert expected != base.version
    replacement = TransientContent(replace(expected, content_digest=hashlib.sha256(b"next").hexdigest()), b"next")
    store = ConditionalStore(base)
    result = apply_expected_revision_update(expected, replacement, compare_and_swap=store.compare_and_swap)
    assert result.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION
    assert not result.mutation_applied and store.mutations == 0 and store.current == base


@pytest.mark.parametrize("field,value", [("hash_algorithm", "sha1"), ("hash_basis", "WORKTREE_BYTES"),
                                         ("snapshot_mode", LOCAL)])
def test_fixed_git_revision_fields_cannot_be_repurposed(committed_seed, field, value):
    with pytest.raises(ValueError):
        replace(committed_seed.version.base_revision, **{field: value})


def test_exact_bytes_are_distinct_and_invalid_materialization_never_reaches_cas(committed_seed):
    crlf = changed_copy(committed_seed, b"a\r\nb")
    lf = changed_copy(committed_seed, b"a\nb")
    assert crlf.version != lf.version
    store = ConditionalStore(crlf)
    stale = apply_expected_revision_update(lf.version, changed_copy(lf, b"next"), compare_and_swap=store.compare_and_swap)
    assert stale.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION and store.mutations == 0
    store.events.clear()
    with pytest.raises(WorkstreamValidationError):
        apply_expected_revision_update(crlf.version, replace(lf, content=crlf.content), compare_and_swap=store.compare_and_swap)
    assert not store.events


@pytest.mark.parametrize("part", ["expected", "replacement", "replacement_version", "replacement_seed", "unchanged"])
def test_invalid_update_requests_do_not_reach_store(committed_seed, part):
    base = committed_seed
    expected, replacement = base.version, changed_copy(base, b"next")
    if part == "expected":
        expected = base.version.base_revision  # A Git seed alone is not a transient version.
    elif part == "replacement":
        replacement = None
    elif part == "replacement_version":
        replacement = replace(replacement, version=None)
    elif part == "replacement_seed":
        replacement = replace(replacement, version=replace(replacement.version,
            base_revision=replace(base.version.base_revision, source_commit="7cb32f2725fb43617c325b5c450ca68854cdac41")))
    else:
        replacement = base
    store = ConditionalStore(base)
    with pytest.raises(WorkstreamValidationError):
        apply_expected_revision_update(expected, replacement, compare_and_swap=store.compare_and_swap)
    assert not store.events and store.current == base


@pytest.mark.parametrize("outcome", ["silent_noop", "false", "applied_noop", "applied_wrong_after", "applied_stale_before",
                                      "stale_matching_before", "stale_mutated_after", "invalid_bytes"])
def test_invalid_or_noop_store_results_cannot_be_reported_applied(committed_seed, outcome):
    base = committed_seed
    replacement = changed_copy(base, b"next")
    other = changed_copy(base, b"other")
    results = {
        "silent_noop": None,
        "false": False,
        "applied_noop": ConditionalMutationResult(WorkstreamUpdateStatus.APPLIED, base, base),
        "applied_wrong_after": ConditionalMutationResult(WorkstreamUpdateStatus.APPLIED, base, other),
        "applied_stale_before": ConditionalMutationResult(WorkstreamUpdateStatus.APPLIED, other, replacement),
        "stale_matching_before": ConditionalMutationResult(WorkstreamUpdateStatus.REJECTED_STALE_REVISION, base, base),
        "stale_mutated_after": ConditionalMutationResult(WorkstreamUpdateStatus.REJECTED_STALE_REVISION, other, replacement),
        "invalid_bytes": ConditionalMutationResult(WorkstreamUpdateStatus.APPLIED, base, replace(replacement, content=b"corrupt")),
    }
    with pytest.raises(WorkstreamValidationError):
        apply_expected_revision_update(base.version, replacement, compare_and_swap=lambda *_: results[outcome])


def test_store_exceptions_propagate_without_claiming_applied(committed_seed):
    error = OSError("store failed conditional mutation")
    def fail(*_):
        raise error
    with pytest.raises(OSError) as failure:
        apply_expected_revision_update(committed_seed.version, changed_copy(committed_seed, b"next"), compare_and_swap=fail)
    assert failure.value is error


def test_l2_workstreams_have_no_io_or_dynamic_imports():
    tree = ast.parse((ROOT / "tools/project_knowledge/workstreams.py").read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert {a.name for a in node.names} <= {"json"}
        if isinstance(node, ast.ImportFrom):
            assert (node.level == 1 and node.module == "model") or node.module in {"collections", "dataclasses", "typing"}
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ""
            assert name not in {"open", "read_text", "read_bytes", "write_text", "write_bytes", "eval", "exec", "__import__", "system", "popen"}


@pytest.fixture
def q4():
    return (json.loads((Q4 / "SHADOW_Q4_WORKSTREAM_DAG.json").read_text()),
            json.loads((Q4 / "Q4_REAL_FIXTURE_V01.json").read_text()),
            json.loads((Q4 / "Q4_REAL_ORACLE_V01.json").read_text())["expectations"])


def q4_graph(dag):
    units = []
    for node in dag["workstreams"]:
        controls = {key: node[key] for key in ("objective", "current_anchor", "pause_reason", "return_condition") if key in node}
        if node["state"] == "PAUSED":
            # Old Q4 used prose/branch text as resume_target. In workstream.v1,
            # the already-authored workstream ID identifies what resumes, while
            # current_anchor preserves that exact original continuation location.
            controls.update(resume_target=node["semantic_id"], current_anchor=node["resume_target"])
        units.append(ws(node["semantic_id"], node["state"], dependencies=node["depends_on"], parent=node["parent"], **controls))
    # Q4 names these project parents but does not declare workstream nodes for
    # them. Supply explicit contract-fixture context sources for those authored
    # IDs, without fabricating active parent workstreams or altering evidence.
    contexts = [context("PROJECT-SOURCE-UNIVERSE"), context("PROJECT-COCKPIT")]
    return build(units, context_sources=contexts)


def test_qualified_q4_r01_multi_dependency_and_real_paused_workstreams(q4):
    dag, _, oracle = q4
    graph = q4_graph(dag)
    expected = oracle["multi_dependency"]
    for name in ("WS-Q4-STRESS", "WS-Q10-FINAL"):
        assert names(graph.nodes[sid(name)].workstream.depends_on) == set(expected[name])
    assert sid("WS-Q4-STRESS") in graph.active_ready_set
    assert sid("WS-Q10-FINAL") not in graph.active_ready_set
    q10 = graph.nodes[sid("WS-Q10-FINAL")]
    assert q10.declared_block and len(q10.dependency_blockers) == 3
    assert {b.state for b in q10.dependency_blockers} == {LifecycleState.ACTIVE, LifecycleState.BLOCKED}
    assert sum(len(n.workstream.depends_on) >= 2 for n in graph.nodes.values()) == expected["multi_dependency_node_count"]
    assert sum(len(n.workstream.depends_on) for n in graph.nodes.values()) == 7
    for name in ("WS-SOURCE-VAULT-BOOTSTRAP", "WS-COCKPIT-DESIGN"):
        node = graph.nodes[sid(name)]
        original = next(w for w in dag["workstreams"] if w["semantic_id"] == name)
        assert node.readiness == WorkstreamReadiness.PAUSED
        assert node.workstream.current_anchor == original["resume_target"]
        assert node.workstream.return_condition == original["return_condition"]
    assert graph.route.primary.workstream_id == sid("WS-Q4-STRESS")


def test_qualified_q4_r02_recovery_and_read_only_cockpit_interruption(q4):
    dag, fixture, oracle = q4
    transition = dag["transition"]
    source = fixture["shadow_sources"][0]
    commit = "7cb32f2725fb43617c325b5c450ca68854cdac41"
    blob = read_committed_path(ROOT, commit, source["path"])
    # The old fixture hashes CRLF worktree bytes. A production revision binds
    # exact Git bytes (LF here), without relabeling that historical digest.
    assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]
    assert json.loads(blob) == dag
    definition = SourceRevision(source["path"], commit, "sha256", "GIT_BLOB_BYTES_AT_COMMIT",
                                hashlib.sha256(blob).hexdigest())
    flow = WorkstreamWorkflow(transition["transition_id"], sid(transition["workstream_id"]), definition,
                              tuple(WorkflowStep(**step) for step in transition["steps"]))
    receipts = tuple(DurableStepReceipt(flow.workflow_id, flow.workstream_id, definition, r["step_id"], r["status"],
                                       (r["evidence_ref"],), definition) for r in transition["durable_receipts"])
    graph = q4_graph(dag)
    before = serialize_workstream_result(graph)
    recovered = recover_workstream(flow, receipts)
    expected = oracle["interruption_recovery"]
    assert [s.step_id for s in recovered.completed] == expected["completed_steps"]
    assert [s.step_id for s in recovered.pending] == expected["pending_steps"]
    assert recovered.next_resume_step.step_id == expected["next_resume_step"]
    assert recovered.blind_replay_required == expected["blind_replay_required"]
    interrupted = graph.nodes[sid(transition["interruption"]["unrelated_workstream_id"])]
    assert interrupted.workstream.current_anchor
    assert serialize_workstream_result(graph) == before
    assert recover_workstream(flow, receipts) == recovered


def test_qualified_q4_r03_stale_update_on_in_memory_materialization(q4):
    _, fixture, oracle = q4
    case = next(c for c in fixture["stress_cases"] if c["case_id"] == "Q4-R03")
    descriptor = dict(case["base_revision"], hash_algorithm="sha256")  # Old evidence spells SHA-256; production fixes sha256.
    base_revision = SourceRevision(**descriptor)
    blob = read_committed_path(ROOT, base_revision.source_commit, base_revision.source_path)
    assert hashlib.sha256(blob).hexdigest() == base_revision.content_digest
    live_path = ROOT / case["target_path"]
    live_before = live_path.read_bytes()
    seed = TransientContent(TransientContentVersion(base_revision, base_revision.content_digest), blob)
    store = ConditionalStore(seed)
    frozen = next(c for c in json.loads((Q4 / "RESULTS_V01.json").read_text())["cases"] if c["case_id"] == "Q4-R03")
    after_b = None
    for i, attempt in enumerate(case["temp_updates"]):
        expected = seed.version if attempt["expected_revision"] == "BASE" else after_b
        marker = ("\n<!-- Q4 TEMP ONLY: " + attempt["attempt_id"] + " / " + attempt["patch_kind"] + " -->\n").encode()
        replacement = changed_copy(seed, store.current.content + marker)
        before, mutations = store.current, store.mutations
        result = apply_expected_revision_update(expected, replacement, compare_and_swap=store.compare_and_swap)
        expected_result = oracle["concurrency"][attempt["attempt_id"]]
        assert result.mutation_applied == expected_result["mutation_applied"]
        if expected_result["status"] == "STALE_REVISION":
            assert result.status == WorkstreamUpdateStatus.REJECTED_STALE_REVISION
            assert store.current == before and store.mutations == mutations
        else:
            assert result.status == WorkstreamUpdateStatus.APPLIED
            assert store.current == replacement and store.mutations == mutations + 1
        assert result.after_version.base_revision is base_revision
        assert not isinstance(result.after_version, SourceRevision)
        assert result.before_version.content_digest == frozen["attempts"][i]["sha256_before"]
        assert result.after_version.content_digest == frozen["attempts"][i]["sha256_after"]
        if i == 0:
            after_b = store.current.version
    assert store.mutations == 2
    assert base_revision.content_digest == hashlib.sha256(blob).hexdigest()
    assert store.current.version.content_digest == hashlib.sha256(store.current.content).hexdigest()
    assert store.current.version.content_digest != base_revision.content_digest
    assert live_path.read_bytes() == live_before
