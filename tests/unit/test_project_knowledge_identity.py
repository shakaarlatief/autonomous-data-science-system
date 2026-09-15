"""G006 qualification translations and explicitly contract-derived fixtures.

Q3-R03/R04 below translate real accepted evidence. Shadow V01 is qualified
synthetic evidence, including the time-bounded reversal of a merge. All other
examples are Specification-028 contract fixtures, not historical project facts.
Research Python orchestration is never imported or executed.
"""

from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError, replace
from datetime import datetime, timezone
import json
from pathlib import Path
import random

import pytest

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.identity import (
    IdentityValidationError, build_identity_index, historical_lookup,
    identity_index_data, resolve_identity, serialize_identity_index, transition_from_source,
)
from tools.project_knowledge.model import (
    AuthorityClass, GovernedSource, IdentityDisposition, LifecycleState, Profile,
    RawDeclaration, SemanticId, SnapshotMode, TransitionClass,
)


ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = SchemaValidator()
LOCAL = SnapshotMode.WORKTREE_SNAPSHOT


def source(sid, path=None, *, authority="canonical", profile=Profile.SEMANTIC_SOURCE, **fields):
    """Schema-valid, explicitly authored contract fixture."""
    data = {"schema_version": "1", "profile": profile.value,
            "kind": "contract-derived-fixture", "authority_class": authority, **fields}
    if sid is not None:
        data["semantic_id"] = sid
    raw = RawDeclaration(data)
    assert not VALIDATOR.validate(raw), VALIDATOR.validate(raw)
    return GovernedSource(
        path or f"docs/{sid or 'undeclared-identity'}.md", profile,
        AuthorityClass(authority), data["kind"], raw, LOCAL,
        SemanticId(sid) if sid is not None else None,
        state=LifecycleState(data["state"]) if "state" in data else None,
    )


def transition(name, kind, predecessors, successors=(), *, semantic_id=None, **fields):
    """Project exactly the accepted schema; no production fixture shortcuts."""
    data = {"transition_class": kind, "predecessors": list(predecessors),
            "resolution_behavior": f"Contract fixture for {kind}",
            "provenance": [f"docs/evidence/{name}.md"], **fields}
    if successors:
        data["successors"] = list(successors)
    return transition_from_source(source(semantic_id, f"docs/transitions/{name}.md",
                                         profile=Profile.IDENTITY_TRANSITION, **data))


def build(sources, transitions=(), **kwargs):
    return build_identity_index(sources, transitions, snapshot_mode=LOCAL, **kwargs)


def resolve(index, sid):
    return resolve_identity(index, SemanticId(sid))


def targets(index, sid):
    return tuple(value.value for value in resolve(index, sid).current_targets)


def errors(sources, transitions=(), **kwargs):
    with pytest.raises(IdentityValidationError) as failure:
        build(sources, transitions, **kwargs)
    assert failure.value.disposition == IdentityDisposition.UNRESOLVED
    assert all(d.severity == "ERROR" for d in failure.value.diagnostics)
    return {d.code for d in failure.value.diagnostics}


def test_current_selective_and_unknown_identity():
    index = build([source("A"), source(None), source("UNREVIEWED", authority="candidate")])
    assert targets(index, "A") == ("A",)
    assert resolve(index, "A").disposition == IdentityDisposition.CURRENT
    assert set(index.current) == {SemanticId("A")}
    assert resolve(index, "MISSING").disposition == IdentityDisposition.UNKNOWN
    assert not historical_lookup(index, SemanticId("MISSING")).known
    assert historical_lookup(index, SemanticId("A")).known


@pytest.mark.parametrize("kind", ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT"])
def test_same_id_carrier_continuity_and_historical_representation(kind):
    old = source("UNIT", "docs/z-old.md", authority="historical", provenance=["docs/origin.md"])
    new = source("UNIT", "docs/a-current.json")
    event = transition("continuity", kind, ["UNIT"], ["UNIT"], provenance=[old.carrier_path, new.carrier_path])
    index = build([old, new], [event])
    assert targets(index, "UNIT") == ("UNIT",)
    assert resolve(index, "UNIT").continuity_preserved
    assert resolve(index, "UNIT").current_sources == (new,)
    history = historical_lookup(index, SemanticId("UNIT"))
    assert {s.carrier_path for s in history.sources} == {old.carrier_path, new.carrier_path}
    assert history.transition_paths == (event.source.carrier_path,)
    assert index.transitions[event.source.carrier_path].provenance == event.provenance
    assert serialize_identity_index(index) == serialize_identity_index(build([new, old], [event]))


@pytest.mark.parametrize("kind", ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT"])
def test_continuity_cannot_change_durable_identity(kind):
    old = source("LEGACY-REFERENCE", authority="historical")
    new = source("CURRENT-REFERENCE")
    event = transition("representation-reference", kind, ["LEGACY-REFERENCE"], ["CURRENT-REFERENCE"])
    assert errors([old, new], [event]) == {"CONTINUITY_IDENTITY_CHANGED"}


def test_merge_retains_each_predecessor_and_successor_lineage():
    event = transition("merge", "MERGE", ["A", "B", "C"], ["MERGED"])
    index = build([source(s) for s in ["A", "B", "C", "MERGED"]], [event])
    for sid in ["A", "B", "C"]:
        assert targets(index, sid) == ("MERGED",)
        assert resolve(index, sid).disposition == IdentityDisposition.MERGED
        assert historical_lookup(index, SemanticId(sid)).sources[0].semantic_id == SemanticId(sid)
    assert resolve(index, "MERGED").predecessor_lineage == tuple(map(SemanticId, ["A", "B", "C"]))


def test_split_has_all_successors_without_a_primary():
    event = transition("split", "SPLIT", ["PARENT"], ["Z", "A"])
    units = [source("PARENT"), source("Z", "docs/a.md"), source("A", "docs/z.md")]
    index = build(units, [event])
    assert set(targets(index, "PARENT")) == {"A", "Z"}
    assert resolve(index, "PARENT").disposition == IdentityDisposition.SPLIT
    assert "primary" not in json.dumps(identity_index_data(index)).lower()
    assert historical_lookup(index, SemanticId("PARENT")).known
    assert serialize_identity_index(index) == serialize_identity_index(build(units[::-1], [replace(event, successors=event.successors[::-1])]))


def test_supersede_preserves_history_and_explicit_current_successor():
    index = build([source("OLD"), source("NEW")], [transition("supersede", "SUPERSEDE", ["OLD"], ["NEW"])])
    assert resolve(index, "OLD").disposition == IdentityDisposition.SUPERSEDED
    assert not resolve(index, "OLD").continuity_preserved
    assert targets(index, "OLD") == ("NEW",)
    assert resolve(index, "NEW").disposition == IdentityDisposition.CURRENT
    assert historical_lookup(index, SemanticId("OLD")).sources


def test_retirement_and_historical_only_are_not_unknown():
    index = build([source("RETIRED"), source("ARCHIVE", authority="historical")],
                  [transition("retire", "RETIRE", ["RETIRED"])])
    row = resolve(index, "RETIRED")
    assert row.disposition == IdentityDisposition.RETIRED
    assert row.current_targets == () and row.retired_targets == (SemanticId("RETIRED"),)
    assert historical_lookup(index, SemanticId("RETIRED")).known
    assert resolve(index, "ARCHIVE").disposition == IdentityDisposition.HISTORICAL
    assert resolve(index, "ARCHIVE").current_targets == ()


@pytest.mark.parametrize("first", ["REDIRECT", "SUPERSEDE"])
def test_chain_retains_complete_provenance(first):
    events = [transition("representation", "REPRESENTATION_REPLACEMENT", ["A"], ["A"]),
              transition("z-first", first, ["A"], ["B"]), transition("a-second", "REDIRECT", ["B"], ["C"])]
    index = build([source(s) for s in "ABC"], events)
    assert targets(index, "A") == ("C",)
    paths = resolve(index, "A").transition_paths
    assert set(paths) == {t.source.carrier_path for t in events}
    # Storage order does not claim path order: predecessor/successor edges do.
    first_record = index.transitions[events[1].source.carrier_path]
    assert first_record.successors == (SemanticId("B"),)
    assert resolve(index, "A").continuity_preserved
    assert resolve(index, "A").disposition == (IdentityDisposition.REDIRECTED if first == "REDIRECT" else IdentityDisposition.SUPERSEDED)
    assert resolve(index, "C").predecessor_lineage == (SemanticId("A"), SemanticId("B"))


def test_move_then_merge_then_supersession_then_split_and_retire():
    events = [transition("move", "MOVE_OR_RENAME", ["A"], ["A"]),
              transition("merge", "MERGE", ["A", "B"], ["M"]),
              transition("super", "SUPERSEDE", ["M"], ["N"]),
              transition("split", "SPLIT", ["N"], ["X", "Y"]),
              transition("retire", "RETIRE", ["Y"])]
    index = build([source(s) for s in "ABMNXY"], events)
    assert targets(index, "A") == ("X",)
    assert resolve(index, "A").retired_targets == (SemanticId("Y"),)
    assert len(resolve(index, "A").transition_paths) == 5


def test_duplicate_current_ownership_never_picks_by_path():
    units = [source("A", "docs/a.md"), source("A", "docs/z.md")]
    for ordering in [units, units[::-1]]:
        assert "DUPLICATE_CURRENT_IDENTITY" in errors(ordering)
        for kind in ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT"]:
            for provenance in [[s.carrier_path for s in units], [s.carrier_path for s in units[::-1]]]:
                assert "DUPLICATE_CURRENT_IDENTITY" in errors(ordering, [transition("ambiguous", kind, ["A"], ["A"], provenance=provenance)])
    explained = [source("A", units[0].carrier_path, state="SUPERSEDED"), units[1]]
    event = transition("handoff", "MOVE_OR_RENAME", ["A"], ["A"])
    index = build(explained, [event])
    assert resolve(index, "A").current_sources == (units[1],)
    assert serialize_identity_index(index) == serialize_identity_index(build(explained[::-1], [event]))


@pytest.mark.parametrize("predecessors,successors", [(["MISSING"], ["B"]), (["A"], ["MISSING"])])
def test_dangling_references_fail(predecessors, successors):
    assert "DANGLING_IDENTITY_REFERENCE" in errors([source("A"), source("B")],
                                                   [transition("dangling", "REDIRECT", predecessors, successors)])


@pytest.mark.parametrize("first,second", [("REDIRECT", "REDIRECT"), ("SUPERSEDE", "SUPERSEDE"),
                                         ("REDIRECT", "SUPERSEDE"), ("SUPERSEDE", "REDIRECT")])
def test_mixed_and_single_class_cycles_fail(first, second):
    events = [transition("one", first, ["A"], ["B"]), transition("two", second, ["B"], ["A"])]
    assert "IDENTITY_TRANSITION_CYCLE" in errors([source("A"), source("B")], events)


@pytest.mark.parametrize("kind", ["SUPERSEDE", "REDIRECT", "SPLIT", "MERGE"])
def test_self_reference_is_not_a_generic_cycle_exception(kind):
    pred = ["A", "B"] if kind == "MERGE" else ["A"]
    succ = ["A", "B"] if kind == "SPLIT" else ["A"]
    assert "IDENTITY_TRANSITION_CYCLE" in errors([source("A"), source("B")], [transition("self", kind, pred, succ)])


@pytest.mark.parametrize("second", ["RETIRE", "REDIRECT", "SUPERSEDE", "SPLIT"])
def test_conflicting_outcomes_fail(second):
    successors = [] if second == "RETIRE" else ["B", "C"] if second == "SPLIT" else ["C"]
    events = [transition("one", "SUPERSEDE", ["A"], ["B"]), transition("two", second, ["A"], successors)]
    assert "CONFLICTING_IDENTITY_TRANSITIONS" in errors([source(s) for s in "ABC"], events)


@pytest.mark.parametrize("kind", ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT", "SUPERSEDE", "REDIRECT"])
def test_schema_valid_single_successor_transition_cannot_claim_a_split(kind):
    event = transition("bad-multiplicity", kind, ["A"], ["B", "C"])
    assert "INVALID_TRANSITION_MULTIPLICITY" in errors([source(s) for s in "ABC"], [event])


def test_typed_input_cardinality_and_duplicate_endpoints_are_checked():
    merge = transition("merge", "MERGE", ["A", "B"], ["C"])
    for invalid in [replace(merge, predecessors=(SemanticId("A"),)),
                    replace(merge, predecessors=(SemanticId("A"), SemanticId("A")))]:
        assert "INVALID_TRANSITION_MULTIPLICITY" in errors([source(s) for s in "ABC"], [invalid])


def test_same_path_does_not_rescue_dangling_or_retired_identity():
    event = transition("same-path", "SUPERSEDE", ["A"], ["MISSING"])
    assert "DANGLING_IDENTITY_REFERENCE" in errors([source("A", "docs/shared.md"), source("B", "docs/shared.md")], [event])
    assert "NO_CURRENT_IDENTITY_TARGET" in errors([source("A"), source("B", authority="historical")],
                                                  [transition("inactive-target", "REDIRECT", ["A"], ["B"])])


def test_noncanonical_transitions_cannot_control_identity():
    event = transition("proposal", "RETIRE", ["A"], authority="candidate")
    index = build([source("A")], [event])
    assert targets(index, "A") == ("A",) and not index.transitions
    historical = transition("past", "RETIRE", ["A"], authority="historical")
    index = build([source("A")], [historical])
    assert targets(index, "A") == ("A",) and len(index.transitions) == 1


def test_unidentified_transition_does_not_mint_an_identity():
    event = transition("unidentified", "REDIRECT", ["A"], ["B"])
    index = build([source("A"), source("B")], [event])
    assert set(index.current) == set(map(SemanticId, ["A", "B"]))
    assert event.source.semantic_id is None
    assert identity_index_data(index)["transitions"][0]["source"]["semantic_id"] is None


@pytest.mark.parametrize("authority", ["canonical", "historical"])
def test_transition_source_authored_identity_is_separate_from_its_endpoints(authority):
    event = transition("identified", "REDIRECT", ["A"], ["B"], semantic_id="TR:1", authority=authority)
    index = build([source("A"), source("B")], iter([event]))
    row = resolve(index, "TR:1")
    assert row.disposition == (IdentityDisposition.CURRENT if authority == "canonical" else IdentityDisposition.HISTORICAL)
    assert row.current_sources == ((event.source,) if authority == "canonical" else ())
    assert targets(index, "TR:1") == (("TR:1",) if authority == "canonical" else ())
    assert not row.transition_paths and not row.predecessor_lineage
    history = historical_lookup(index, SemanticId("TR:1"))
    assert history.known and history.sources == (event.source,)
    assert history.sources[0].carrier_path == event.source.carrier_path
    assert history.sources[0].authority_class == AuthorityClass(authority)
    assert not history.transition_paths  # Its own relation does not implicitly reference TR:1.
    assert event.predecessors == (SemanticId("A"),) and event.successors == (SemanticId("B"),)
    assert targets(index, "A") == (("B",) if authority == "canonical" else ("A",))
    serialized = next(row for row in identity_index_data(index)["identities"] if row["semantic_id"] == "TR:1")
    assert serialized["history"]["sources"][0]["carrier_path"] == event.source.carrier_path


@pytest.mark.parametrize("authority", ["candidate", "evidence", "capture", "derived"])
def test_noncanonical_transition_source_does_not_establish_identity(authority):
    event = transition("noncanonical", "REDIRECT", ["A"], ["B"], semantic_id="TR:1", authority=authority)
    index = build([source("A"), source("B")], [event])
    assert resolve(index, "TR:1").disposition == IdentityDisposition.UNKNOWN
    assert not historical_lookup(index, SemanticId("TR:1")).known


@pytest.mark.parametrize("state", ["ACTIVE", "PAUSED", "BLOCKED", "COMPLETED", "SUPERSEDED"])
def test_transition_unit_identity_respects_lifecycle_independently_of_relation(state):
    event = transition("state", "REDIRECT", ["A"], ["B"], semantic_id="TR:1", state=state)
    index = build([source("A"), source("B")], [event])
    assert targets(index, "TR:1") == (() if state == "SUPERSEDED" else ("TR:1",))
    assert targets(index, "A") == (("B",) if state in {"ACTIVE", "COMPLETED"} else ("A",))
    assert historical_lookup(index, SemanticId("TR:1")).sources[0].state == LifecycleState(state)


@pytest.mark.parametrize("start,end", [("effective_from", "effective_to"), ("authority_from", "authority_to")])
def test_transition_unit_temporal_ownership_and_carrier_handoff(start, end):
    boundary = "2026-01-01T00:00:00Z"
    old = transition("z-old", "REDIRECT", ["A"], ["B"], semantic_id="TR:1", **{end: boundary})
    new = transition("a-new", "REDIRECT", ["A"], ["B"], semantic_id="TR:1", **{start: boundary})
    units = [source("A"), source("B")]
    assert "IDENTITY_TIME_REQUIRED" in errors(units, [old, new])
    for instant, owner in [(datetime(2025, 12, 31, tzinfo=timezone.utc), old),
                           (datetime(2026, 1, 1, tzinfo=timezone.utc), new)]:
        index = build(units, [old, new], at_time=instant)
        assert resolve(index, "TR:1").current_sources == (owner.source,)
        assert len(historical_lookup(index, SemanticId("TR:1")).sources) == 2
        assert serialize_identity_index(index) == serialize_identity_index(build(units[::-1], [new, old], at_time=instant))
    expired = build(units, [old], at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    assert resolve(expired, "TR:1").disposition == IdentityDisposition.HISTORICAL
    assert historical_lookup(expired, SemanticId("TR:1")).sources == (old.source,)


def test_transition_source_identity_collisions_fail_visibly():
    event = transition("identified", "REDIRECT", ["A"], ["B"], semantic_id="TR:1")
    units = [source("A"), source("B"), source("TR:1", "docs/colliding-unit.md")]
    assert errors(units, [event]) == {"DUPLICATE_CURRENT_IDENTITY"}
    other = transition("other", "RETIRE", ["B"], semantic_id="TR:1")
    assert errors(units[:2], [event, other]) == {"DUPLICATE_CURRENT_IDENTITY"}


def test_identified_transition_is_an_explicit_endpoint_of_another_transition():
    event = transition("identified", "REDIRECT", ["A"], ["B"], semantic_id="TR:1")
    handoff = transition("handoff", "SUPERSEDE", ["TR:1"], ["TR:2"])
    replacement = transition("replacement", "MOVE_OR_RENAME", ["B"], ["B"], semantic_id="TR:2")
    units, events = [source("A"), source("B")], [event, handoff, replacement]
    index = build(units, events)
    assert targets(index, "TR:1") == ("TR:2",)
    assert resolve(index, "TR:1").current_sources == (replacement.source,)
    assert resolve(index, "TR:1").transition_paths == (handoff.source.carrier_path,)
    assert historical_lookup(index, SemanticId("TR:1")).sources == (event.source,)
    assert targets(index, "A") == ("B",)
    expected_bytes = serialize_identity_index(index)
    for seed in range(20):
        rng = random.Random(seed)
        rng.shuffle(units)
        rng.shuffle(events)
        assert serialize_identity_index(build(iter(units), iter(events))) == expected_bytes
    cycle = transition("cycle", "REDIRECT", ["TR:2"], ["TR:1"])
    assert "IDENTITY_TRANSITION_CYCLE" in errors(units, [*events, cycle])


def test_identified_transition_source_cannot_mix_snapshot_modes():
    event = transition("identified", "REDIRECT", ["A"], ["B"], semantic_id="TR:1")
    event = replace(event, source=replace(event.source, snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT))
    assert errors([source("A"), source("B")], [event]) == {"IDENTITY_SNAPSHOT_MISMATCH"}


def test_explicit_half_open_temporal_windows_and_no_implicit_now():
    event = transition("timed", "SUPERSEDE", ["A"], ["B"], effective_from="2026-01-01T00:00:00Z", effective_to="2026-02-01T00:00:00Z")
    units = [source("A"), source("B")]
    assert "IDENTITY_TIME_REQUIRED" in errors(units, [event])
    assert "IDENTITY_TIME_REQUIRED" in errors(units, [event], at_time=datetime(2026, 1, 1))
    assert targets(build(units, [event], at_time=datetime(2026, 1, 1, tzinfo=timezone.utc)), "A") == ("B",)
    expired = build(units, [event], at_time=datetime(2026, 2, 1, tzinfo=timezone.utc))
    assert targets(expired, "A") == ("A",) and len(expired.transitions) == 1
    assert historical_lookup(expired, SemanticId("A")).transition_paths
    invalid = transition("inverted", "RETIRE", ["A"], effective_from="2026-02-01T00:00:00Z", effective_to="2026-01-01T00:00:00Z")
    assert "INVALID_IDENTITY_TIME" in errors(units, [invalid], at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))


def test_duplicate_owners_can_be_disambiguated_only_by_explicit_control():
    units = [source("A", "docs/old.md", authority_to="2026-01-01T00:00:00Z"),
             source("A", "docs/new.md", authority_from="2026-01-01T00:00:00Z")]
    index = build(units, at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    assert targets(index, "A") == ("A",)
    assert len(historical_lookup(index, SemanticId("A")).sources) == 2


def test_deterministic_rebuild_source_transition_and_endpoint_permutations():
    units = [source(s) for s in "ABCDE"]
    events = [transition("merge", "MERGE", ["B", "A"], ["C"]), transition("split", "SPLIT", ["C"], ["E", "D"])]
    expected = build(units, events)
    expected_bytes = serialize_identity_index(expected)
    for seed in range(20):
        rng = random.Random(seed)
        rng.shuffle(units)
        rng.shuffle(events)
        rebuilt = build(units, events)
        assert rebuilt == expected
        assert serialize_identity_index(rebuilt) == expected_bytes
    assert expected_bytes.endswith(b"\n") and b"\r\n" not in expected_bytes
    assert json.loads(expected_bytes)["snapshot_mode"] == "WORKTREE_SNAPSHOT"


def test_index_and_results_are_immutable():
    index = build([source("A")])
    with pytest.raises(TypeError):
        index.current[SemanticId("B")] = resolve(index, "A")
    with pytest.raises(FrozenInstanceError):
        resolve(index, "A").disposition = IdentityDisposition.RETIRED


def test_snapshot_mixing_fails():
    assert "IDENTITY_SNAPSHOT_MISMATCH" in errors([replace(source("A"), snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT)])


def test_empty_corpus_and_scoped_transition_boundary():
    assert not build([source(None)]).current
    assert "SCOPED_IDENTITY_TRANSITION" in errors([source("A"), source("B")],
        [transition("scoped", "SUPERSEDE", ["A"], ["B"], scope={"target": "one-domain"})])


def test_source_state_and_transition_times_preserve_current_carrier_explicitly():
    units = [source("A", "docs/z-before.md", effective_to="2026-01-01T00:00:00Z"),
             source("A", "docs/a-after.md", effective_from="2026-01-01T00:00:00Z")]
    event = transition("rename", "MOVE_OR_RENAME", ["A"], ["A"], authority_from="2026-01-01T00:00:00Z")
    index = build(units, [event], at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    assert resolve(index, "A").current_sources == (units[1],)
    assert resolve(index, "A").continuity_preserved
    assert serialize_identity_index(index) == serialize_identity_index(build(units[::-1], [event], at_time=datetime.fromisoformat("2026-01-01T01:00:00+01:00")))


def test_deep_chain_build_and_bounded_lookup_do_not_scan_history():
    units = [source(f"U{i}") for i in range(1050)]
    events = [transition(f"step{i}", "REDIRECT", [f"U{i}"], [f"U{i+1}"]) for i in range(1049)]
    index = build(units, events)
    assert targets(index, "U0") == ("U1049",)
    assert len(resolve(index, "U0").transition_paths) == 1049
    class NoScan(dict):
        def __iter__(self):
            raise AssertionError("lookup traversed index")
        def items(self):
            raise AssertionError("lookup traversed index")
    # Duck-typed access sentinel: normal lookup needs only current.get/history.get.
    class LookupOnly:
        current = NoScan(index.current)
        history = NoScan(index.history)
    assert resolve_identity(LookupOnly(), SemanticId("U0")) == resolve(index, "U0")
    assert historical_lookup(LookupOnly(), SemanticId("U0")).known


def test_identity_module_has_no_io_or_dynamic_import_capability():
    tree = ast.parse((ROOT / "tools/project_knowledge/identity.py").read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert {a.name.split('.')[0] for a in node.names} <= {"json"}
        elif isinstance(node, ast.ImportFrom):
            assert (node.level == 1 and node.module == "model") or node.module in {"collections", "datetime", "typing"}
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"open", "eval", "exec", "__import__"}


def shadow_json(path):
    """Read evidence as data in tests; never route legacy shadow shapes to production."""
    text = (ROOT / path).read_text(encoding="utf-8")
    return json.loads(text.split("<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->", 1)[1].split("<!-- PKA-STRUCTURED-DECLARATION-END -->", 1)[0])


def test_qualified_real_q3_r03_carrier_continuity_and_retired_label():
    base = "docs/research/project_knowledge_candidate_01_q3_real_v01/"
    evidence = shadow_json(base + "SHADOW_HISTORICAL_INTERMEDIATE.md")
    oracle = json.loads((ROOT / (base + "Q3_REAL_ORACLE_V01.json")).read_text())["expectations"]["real_semantics_alignment"]["Q3-R03"]
    sid = evidence["semantic_id"]
    # The real case needs no standalone transition source. Carrier/retired label
    # provenance stays source-owned, exactly as Q3 qualified it.
    unit = source(sid, evidence["current_carrier"], authority="historical", provenance=[
        evidence["carrier_history"]["original_carrier"],
        evidence["carrier_history"]["rename_commit"],
        evidence["original_recorded_identity"], evidence["original_identity_disposition"],
        evidence["canonical_numeric_identity_owner"],
    ])
    index = build([unit])
    history = historical_lookup(index, SemanticId(sid))
    assert history.sources[0].carrier_path == oracle["current_carrier"]
    assert resolve(index, sid).disposition == IdentityDisposition.HISTORICAL
    assert not index.transitions and len(index.current) == 1
    assert oracle["original_identity_disposition"] in history.sources[0].declaration.fields["provenance"]
    assert oracle["canonical_numeric_identity_owner"] != history.sources[0].carrier_path
    assert resolve(index, "Checkpoint252").disposition == IdentityDisposition.UNKNOWN  # No ID minted from an old label.


def test_qualified_real_q3_r04_paused_identity_is_preserved():
    base = "docs/research/project_knowledge_candidate_01_q3_real_v01/"
    evidence = shadow_json(base + "SHADOW_COCKPIT_WORKSTREAM.md")
    unit = source(evidence["semantic_id"], evidence["current_carrier"], state=evidence["state"],
                  references=[base + "SHADOW_COCKPIT_WORKSTREAM.md"])
    index = build([unit])
    assert targets(index, evidence["semantic_id"]) == (evidence["semantic_id"],)
    assert historical_lookup(index, unit.semantic_id).sources[0].state == LifecycleState.PAUSED


def test_qualified_synthetic_shadow_move_merge_reversal_and_split():
    base = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v01"
    fixture = json.loads((base / "SHADOW_FIXTURE_V01.json").read_text())
    oracle = json.loads((base / "SHADOW_ORACLE_V01.json").read_text())["expectations"]
    move, merge, reversal, split = fixture["identity_events"]
    carriers = {u["semantic_id"]: u["carrier"] for u in fixture["identity_initial"]}
    carriers[move["semantic_id"]] = move["to_carrier"]
    carriers[merge["output"]] = merge["output_carrier"]
    carriers.update(split["output_carriers"])
    units = [source(sid, path) for sid, path in carriers.items()]
    # REVERSE_MERGE is not an eighth production class. The qualified synthetic
    # sequence translates to an explicit end of MERGE applicability and a SPLIT
    # of its result. These timestamps express fixture order, not real history.
    events = [transition(move["event_id"], "MOVE_OR_RENAME", [move["semantic_id"]], [move["semantic_id"]], provenance=[move["from_carrier"], move["to_carrier"]]),
              transition(merge["event_id"], "MERGE", merge["inputs"], [merge["output"]], effective_to="2000-01-03T00:00:00Z"),
              transition(reversal["event_id"], "SPLIT", [reversal["input"]], reversal["outputs"], effective_from="2000-01-03T00:00:00Z"),
              transition(split["event_id"], "SPLIT", [split["input"]], split["outputs"], effective_from="2000-01-04T00:00:00Z")]
    index = build(units, events, at_time=datetime(2000, 1, 4, tzinfo=timezone.utc))
    assert {sid.value: list(targets(index, sid.value)) for sid in index.current} == oracle["identity_current_targets"]
    assert {s.semantic_id.value: s.carrier_path for row in index.current.values() for s in row.current_sources} == oracle["identity_current_carriers"]
    assert len(index.transitions) == 4  # The closed merge is preserved, not overwritten.
    assert events[1].source.carrier_path in historical_lookup(index, SemanticId(merge["output"])).transition_paths
