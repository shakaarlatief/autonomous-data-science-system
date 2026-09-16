"""G007 contract fixtures plus read-only translations of qualified evidence.

Research shapes are translated explicitly to the accepted production schema;
no research orchestration is imported and no evidence/oracle is rewritten.
"""

import ast
from dataclasses import FrozenInstanceError, replace
from datetime import datetime, timezone
import json
from pathlib import Path
import random

import pytest

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.authority import (
    authority_result_data, match_scope, resolve_authority, serialize_authority_result,
)
from tools.project_knowledge.model import (
    AuthorityClass, AuthorityEvidence, AuthorityQuery, AuthorityStatus, Freshness,
    GovernedSource, LifecycleState, PrivateStateEvidence, Profile, RawDeclaration,
    Relation, Scope, ScopeDisposition, SemanticId, SnapshotMode, SourceRevision,
)


ROOT = Path(__file__).resolve().parents[2]
LOCAL = SnapshotMode.WORKTREE_SNAPSHOT
COMMIT = SnapshotMode.COMMIT_SNAPSHOT
VALIDATOR = SchemaValidator()


def source(sid, *, path=None, scope=None, relations=(), authority="canonical", profile=Profile.SEMANTIC_SOURCE,
           mode=LOCAL, **fields):
    data = {"schema_version": "1", "profile": profile.value, "kind": "contract-fixture",
            "authority_class": authority, **fields}
    if sid is not None:
        data["semantic_id"] = sid
    if scope is not None:
        data["scope"] = scope
    if relations:
        data["relations"] = [{"mode": r[0], "target": r[1], **({"scope": r[2]} if len(r) > 2 else {})} for r in relations]
    raw = RawDeclaration(data)
    assert not VALIDATOR.validate(raw), VALIDATOR.validate(raw)
    carrier = path or f"docs/{sid or 'unidentified'}.md"
    revision = SourceRevision(carrier, "a" * 40, "sha256", "GIT_BLOB_BYTES_AT_COMMIT", "0" * 64) if mode == COMMIT else None
    return GovernedSource(carrier, profile, AuthorityClass(authority), data["kind"], raw, mode,
                          SemanticId(sid) if sid else None, Scope(scope) if scope is not None else None,
                          tuple(Relation(r[0], SemanticId(r[1]), Scope(r[2]) if len(r) > 2 else None) for r in relations),
                          revision, LifecycleState(data["state"]) if "state" in data else None)


def procedure(sid, ids=("C1", "C2"), **kwargs):
    data = dict(state="ACTIVE", governed_action_classes=["act"], preconditions=["preflight"],
                mandatory_constraints=[{"constraint_id": c, "requirement": f"Perform {c}"} for c in ids],
                prohibitions=["no bypass"], required_postconditions=["verify"], fail_closed_conditions=["unknown state"])
    data.update(kwargs)
    return source(sid, profile=Profile.GOVERNING_PROCEDURE, **data)


def joint(sid, members, **kwargs):
    admission = {key: True for key in ("overlapping_current_canonical_sources", "ordinary_relations_insufficient",
                                      "irreducible_set_fact", "independently_activated", "duplicate_ownership_rejected")}
    admission["review_evidence"] = ["docs/review.md"]
    data = dict(scope={}, members=members, combination_semantics="All peer members required, without precedence",
                governed_action_classes=["act"], admission=admission, provenance=["docs/evidence.md"])
    data.update(kwargs)
    return source(sid, profile=Profile.JOINT_AUTHORITY, **data)


def query(scope=None, **kwargs):
    return AuthorityQuery("act", "subject", Scope(scope or {}), kwargs.pop("consequence", "consequential"), **kwargs)


def attest(sources):
    return [AuthorityEvidence(s.carrier_path, True, Freshness.FRESH, s.revision) for s in sources]


def resolve(sources, q=None, joints=(), **kwargs):
    kwargs.setdefault("snapshot_mode", LOCAL)
    kwargs.setdefault("evidence", attest([*sources, *joints]))
    return resolve_authority(q or query(), sources, joint_authorities=joints, **kwargs)


def ids(result):
    assert result.status == AuthorityStatus.RESOLVED, result
    return {s.semantic_id.value if s.semantic_id else None for s in result.receipt.governing_sources}


def codes(result):
    assert result.receipt is None
    return {d.code for d in result.diagnostics}


@pytest.mark.parametrize("scope,facets,expected", [
    ({}, {}, "MATCH"), ({"region": "eu"}, {}, "UNDERSPECIFIED"),
    ({"region": "eu"}, {"region": "us"}, "NO_MATCH"),
    ({"region": ["eu", "us"]}, {"region": "us"}, "MATCH"),
    ({"region": "eu", "actor": "owner"}, {"region": "us"}, "NO_MATCH"),
    ({"region": "global"}, {"region": "eu"}, "NO_MATCH"),
    ({"region": "*"}, {"region": "eu"}, "NO_MATCH"),
])
def test_scope_exact_match_truth_table(scope, facets, expected):
    assert match_scope(Scope(scope), facets) == ScopeDisposition(expected)


def test_selective_identity_and_receipt_completeness():
    unit = source(None)
    result = resolve([unit])
    assert ids(result) == {None}
    data = authority_result_data(result)["receipt"]
    assert data["snapshot_mode"] == LOCAL
    assert data["governing_sources"][0] == {
        "semantic_id": None, "carrier_path": unit.carrier_path, "revision": None,
        "applicability_reason": "CURRENT_CANONICAL_SCOPE_TIME_RELATION_CLOSURE",
        "evidence": {"carrier_path": unit.carrier_path, "available": True, "freshness": "FRESH",
                     "verified_revision": None, "expected_revision": None},
    }
    assert data["scope_dispositions"] == [{"carrier_path": unit.carrier_path, "disposition": "MATCH"}]
    assert data["removed_sources"] == data["relations"] == data["activated_constraints"] == []
    assert data["query"]["action"] == "act" and data["query"]["target"] == "subject"


@pytest.mark.parametrize("authority", ["candidate", "historical", "derived", "evidence", "capture"])
def test_noncanonical_sources_never_govern(authority):
    result = resolve([source("A"), source("B", authority=authority)])
    assert ids(result) == {"A"}
    assert result.receipt.removed_sources[0].reason == "NON_CANONICAL"


@pytest.mark.parametrize("mode", ["REPLACE", "CORRECT", "SPECIALIZE"])
def test_scoped_relations_and_residual_base(mode):
    base = source("BASE")
    successor = source("NEW", scope={"region": "eu"}, relations=[(mode, "BASE", {"region": "eu"})])
    result = resolve([base, successor], query({"region": "eu"}))
    assert ids(result) == {"NEW"}
    removal = result.receipt.removed_sources[0]
    assert (removal.carrier_path, removal.reason, removal.by_source) == (base.carrier_path, mode, successor.carrier_path)
    assert ids(resolve([base, successor], query({"region": "us"}))) == {"BASE"}
    assert resolve([base, successor]).status == AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED


def test_scope_discrimination_uses_final_closure_not_just_missing_facets():
    # The scoped obsolete candidate cannot change the resulting governing set.
    base = source("OLD", scope={"region": "eu"})
    new = source("NEW", relations=[("REPLACE", "OLD")])
    result = resolve([base, new])
    assert ids(result) == {"NEW"}
    assert next(d for d in result.receipt.scope_dispositions if d.carrier_path == base.carrier_path).disposition == ScopeDisposition.UNDERSPECIFIED
    assert ids(resolve([source("ONLY", scope={"region": "eu"})])) == {"ONLY"}


@pytest.mark.parametrize("consequence", ["low", "exploratory", "consequential", "critical"])
def test_consequence_never_breaks_scope_ties(consequence):
    result = resolve([source("A", scope={"region": "eu"}), source("B", scope={"region": "us"})], query(consequence=consequence))
    assert result.status == AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED
    assert "DISCRIMINATING_SCOPE_REQUIRED" in codes(result)


def test_relation_scope_can_discriminate_even_with_unscoped_candidates():
    units = [source("A"), source("B", relations=[("REPLACE", "A", {"region": "eu"})])]
    assert resolve(units).status == AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED
    assert ids(resolve(units, query({"region": "eu"}))) == {"B"}
    assert resolve(units, query({"region": "us"})).status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT


def test_query_target_actor_workstream_and_finite_scope_values():
    units = [source("A", scope={"target": "subject", "actor": "owner", "workstream": "WS", "region": ["eu", "us"]})]
    assert ids(resolve(units, query({"region": ["us", "eu"]}, actor="owner", workstream="WS"))) == {"A"}
    assert resolve(units, replace(query(), target="other")).status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    assert resolve(units, query(actor="guest")).status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY


@pytest.mark.parametrize("case", ["same", "different", "uncovered", "all_missing"])
@pytest.mark.parametrize("omitted_facet", [False, True])
def test_explicit_finite_cells_are_all_required_and_permutation_stable(case, omitted_facet):
    extra = {"environment": "prod"} if omitted_facet else {}
    units = ([source("A", scope={"region": ["eu", "us"], **extra})] if case == "same" else
             [source("A", scope={"region": "eu", **extra}), source("B", scope={"region": "us", **extra})] if case == "different" else
             [source("A", scope={"region": "eu" if case == "uncovered" else "apac", **extra})])
    expected_status = (AuthorityStatus.RESOLVED if case == "same" else AuthorityStatus.UNRESOLVED_SCOPE_REQUIRED
                       if case == "different" else AuthorityStatus.MISSING_REQUIRED_AUTHORITY)
    results = [resolve(order, query({"region": values}))
               for order in (units, units[::-1]) for values in (["eu", "us"], ["us", "eu"])]
    for result in results:
        assert result.status == expected_status
        if case == "same":
            assert ids(result) == {"A"}
            assert result.receipt.scope_dispositions[0].disposition == (ScopeDisposition.UNDERSPECIFIED if omitted_facet else ScopeDisposition.MATCH)
        else:
            assert result.receipt is None
            assert codes(result) == ({"DISCRIMINATING_SCOPE_REQUIRED"} if case == "different" else {"NO_APPLICABLE_AUTHORITY"})
        assert result == results[0]
        assert serialize_authority_result(result) == serialize_authority_result(results[0])


def test_explicit_cartesian_cells_cannot_disappear_between_facets():
    units = [source("A", scope={"region": "eu", "environment": "prod"}),
             source("B", scope={"region": "us", "environment": "dev"})]
    # Every value occurs somewhere, but two explicitly requested conjunctions
    # (eu/dev and us/prod) have no authority.
    first = resolve(units, query({"region": ["eu", "us"], "environment": ["dev", "prod"]}))
    second = resolve(units[::-1], query({"environment": ["prod", "dev"], "region": ["us", "eu"]}))
    assert first.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    assert codes(first) == {"NO_APPLICABLE_AUTHORITY"}
    assert serialize_authority_result(first) == serialize_authority_result(second)


def test_finite_cells_agree_after_closure_with_three_valued_source_assessments():
    units = [source("OLD", scope={"region": "eu"}), source("NEW", relations=[("REPLACE", "OLD")]),
             source("EVIDENCE", scope={"region": "apac"}, authority="evidence")]
    result = resolve(units, query({"region": ["eu", "us"]}))
    assert ids(result) == {"NEW"}
    assert {a.carrier_path: a.disposition for a in result.receipt.scope_dispositions} == {
        units[0].carrier_path: ScopeDisposition.UNDERSPECIFIED,
        units[1].carrier_path: ScopeDisposition.MATCH,
        units[2].carrier_path: ScopeDisposition.NO_MATCH,
    }
    assert serialize_authority_result(result) == serialize_authority_result(resolve(units[::-1], query({"region": ["us", "eu"]})))


def test_omitted_hypothetical_other_is_not_an_explicit_literal_other():
    units = [source("A", scope={"region": "eu", "environment": "prod"})]
    assert ids(resolve(units)) == {"A"}  # Only candidate-compatible omitted completions matter.
    assert ids(resolve(units, query({"region": "eu"}))) == {"A"}
    missing = resolve(units, query({"region": ["eu", "OTHER"]}))
    assert missing.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    assert codes(missing) == {"NO_APPLICABLE_AUTHORITY"}
    units = [source("A", scope={"region": ["eu", "OTHER"]})]
    assert ids(resolve(units, query({"region": ["OTHER", "eu"]}))) == {"A"}


@pytest.mark.parametrize("failure_kind", ["temporal", "relation", "conflict"])
def test_failure_inside_one_requested_cell_cannot_be_hidden(failure_kind):
    units = [source("A", scope={"region": "eu"})]
    fields = {"effective_to": "2025-01-01T00:00:00Z"} if failure_kind == "temporal" else {}
    relations = [("SUPPLEMENT", "ABSENT")] if failure_kind == "relation" else []
    units.append(source("B", scope={"region": "us"}, relations=relations, **fields))
    if failure_kind == "conflict":
        units.append(source("C", scope={"region": "us"}))
    q = query({"region": ["eu", "us"]}, at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    result = resolve(units, q)
    assert result.status != AuthorityStatus.RESOLVED and result.receipt is None
    assert serialize_authority_result(result) == serialize_authority_result(resolve(units[::-1], replace(q, scope=Scope({"region": ["us", "eu"]}))))


def test_ambiguous_authority_and_retrieval_are_independent():
    class HostileRanking:
        def __iter__(self):
            raise AssertionError("retrieval was read")
    units = [source("A"), source("B")]
    result = resolve(units, retrieval_nominations=HostileRanking())
    assert result.status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT
    replacement = source("B", relations=[("REPLACE", "A")])
    assert ids(resolve([units[0], replacement], retrieval_nominations=[{"id": "A", "rank": 1}])) == {"B"}


def test_supplement_direction_and_order_are_not_lexical():
    base = procedure("Z-BASE", path="docs/z.md", ids=("Z9", "A1"))
    supplement = procedure("A-SUP", path="docs/a.md", ids=("S",), relations=[("SUPPLEMENT", "Z-BASE")])
    result = resolve([supplement, base])
    assert ids(result) == {"Z-BASE", "A-SUP"}
    order = {(e.before_source, e.before_constraint, e.after_source, e.after_constraint) for e in result.receipt.constraint_order}
    assert order == {(base.carrier_path, "Z9", base.carrier_path, "A1"), (base.carrier_path, "A1", supplement.carrier_path, "S")}
    assert result.receipt.action_contracts[0].preconditions == ("preflight",)
    assert result.receipt.action_contracts[0].prohibitions == ("no bypass",)
    assert result.receipt.action_contracts[0].required_postconditions == ("verify",)
    assert result.receipt.action_contracts[0].fail_closed_conditions == ("unknown state",)


@pytest.mark.parametrize("mode", ["REPLACE", "CORRECT", "SPECIALIZE"])
def test_replacement_retains_supplements_and_transitive_closure(mode):
    units = [procedure("BASE", ids=("B",)),
             procedure("MID", ids=("M",), scope={"region": "eu"}, relations=[(mode, "BASE", {"region": "eu"})]),
             procedure("NEW", ids=("N",), scope={"region": "eu"}, relations=[("CORRECT", "MID")]),
             procedure("SUP", ids=("S",), relations=[("SUPPLEMENT", "BASE")])]
    result = resolve(units, query({"region": "eu"}))
    assert ids(result) == {"NEW", "SUP"}
    assert {(e.before_constraint, e.after_constraint) for e in result.receipt.constraint_order} == {("N", "S")}
    assert {r.carrier_path for r in result.receipt.removed_sources} == {units[0].carrier_path, units[1].carrier_path}
    assert result.receipt.supporting_sources[0].carrier_path == units[1].carrier_path


def test_replacing_supplement_retains_base_dependency_and_its_provenance():
    units = [procedure("BASE", ids=("B",)), procedure("SUP", ids=("S",), relations=[("SUPPLEMENT", "BASE")]),
             procedure("NEW", ids=("N",), relations=[("REPLACE", "SUP")])]
    result = resolve(units)
    assert ids(result) == {"BASE", "NEW"}
    assert {(e.before_constraint, e.after_constraint) for e in result.receipt.constraint_order} == {("B", "N")}
    checks = attest(units)
    checks[1] = replace(checks[1], freshness=Freshness.STALE)
    assert resolve(units, evidence=checks).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY
    assert result.receipt.supporting_sources[0].carrier_path == units[1].carrier_path


def test_replacing_entire_supplement_bundle_and_contradictory_owner():
    units = [source("BASE"), source("SUP", relations=[("SUPPLEMENT", "BASE")]),
             source("NEW", relations=[("REPLACE", "BASE"), ("REPLACE", "SUP")])]
    assert ids(resolve(units)) == {"NEW"}
    assert "AUTHORITY_SUPPLEMENT_CYCLE" in codes(resolve([source("A"), source("B", relations=[("SUPPLEMENT", "A"), ("REPLACE", "A")])]))


def test_supplement_scope_and_filtered_base():
    units = [source("BASE"), source("SUP", scope={"region": "eu"}, relations=[("SUPPLEMENT", "BASE")])]
    assert ids(resolve(units, query({"region": "eu"}))) == {"BASE", "SUP"}
    assert ids(resolve(units, query({"region": "us"}))) == {"BASE"}
    units[0] = source("BASE", scope={"region": "us"})
    assert "INAPPLICABLE_SUPPLEMENT_BASE" in codes(resolve(units, query({"region": "eu"})))


def test_replacement_can_reference_explicitly_historical_or_superseded_predecessor():
    for old in [source("OLD", authority="historical"), source("OLD", state="SUPERSEDED")]:
        assert ids(resolve([old, source("NEW", relations=[("REPLACE", "OLD")])])) == {"NEW"}


def test_specialization_uses_partial_order_instead_of_facet_count():
    units = [source("BASE", scope={"region": ["eu", "us"]}),
             source("SPEC", relations=[("SPECIALIZE", "BASE", {"region": "eu"})])]
    assert ids(resolve(units, query({"region": "eu"}))) == {"SPEC"}
    # More facets do not make a scope a subset when one facet broadens the base.
    units = [source("BASE", scope={"region": "eu"}),
             source("SPEC", relations=[("SPECIALIZE", "BASE", {"region": ["eu", "us"], "environment": "prod"})])]
    assert "INVALID_SPECIALIZATION" in codes(resolve(units, query({"region": "eu", "environment": "prod"})))


@pytest.mark.parametrize("modes", [("REPLACE", "REPLACE"), ("CORRECT", "CORRECT"), ("REPLACE", "CORRECT"), ("SUPPLEMENT", "SUPPLEMENT")])
def test_cycles_fail_visibly(modes):
    result = resolve([source("A", relations=[(modes[0], "B")]), source("B", relations=[(modes[1], "A")])])
    assert result.status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT
    assert any("CYCLE" in code for code in codes(result))


def test_invalid_specialization_missing_base_and_conflicting_successors():
    result = resolve([source("A", scope={"region": "eu"}), source("B", scope={"region": "eu"}, relations=[("SPECIALIZE", "A", {"region": "eu"})])])
    assert "INVALID_SPECIALIZATION" in codes(result)
    assert resolve([source("B", relations=[("SUPPLEMENT", "ABSENT")])]).status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    units = [source("A"), source("B", relations=[("REPLACE", "A")]), source("C", relations=[("REPLACE", "A")])]
    assert resolve(units).status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT


def test_duplicate_current_carriers_fail_and_explicit_handoff_works():
    units = [source("A", path="docs/a.md"), source("A", path="docs/z.md")]
    assert "DUPLICATE_CURRENT_AUTHORITY" in codes(resolve(units))
    units[0] = source("A", path="docs/a.md", state="SUPERSEDED")
    assert resolve(units).receipt.governing_sources[0].carrier_path == "docs/z.md"


@pytest.mark.parametrize("prefix", ["effective", "authority"])
def test_temporal_half_open_boundaries_and_explicit_time(prefix):
    units = [source("A", **{f"{prefix}_to": "2026-01-01T00:00:00Z"}),
             source("B", **{f"{prefix}_from": "2026-01-01T00:00:00Z"})]
    assert "AUTHORITY_TIME_REQUIRED" in codes(resolve(units))
    assert ids(resolve(units, query(at_time=datetime(2025, 12, 31, tzinfo=timezone.utc)))) == {"A"}
    assert ids(resolve(units, query(at_time=datetime(2026, 1, 1, tzinfo=timezone.utc)))) == {"B"}
    assert "AUTHORITY_TIME_REQUIRED" in codes(resolve(units, query(at_time=datetime(2026, 1, 1))))


def test_invalid_interval_and_temporally_filtered_relation_owner():
    bad = source("A", effective_from="2026-02-01T00:00:00Z", effective_to="2026-01-01T00:00:00Z")
    assert "INVALID_AUTHORITY_TIME" in codes(resolve([bad], query(at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))))
    units = [source("A"), source("B", effective_from="2027-01-01T00:00:00Z", relations=[("REPLACE", "A")])]
    assert ids(resolve(units, query(at_time=datetime(2026, 1, 1, tzinfo=timezone.utc)))) == {"A"}


def test_qualified_joint_authority_and_unordered_peer_constraints():
    units = [procedure("A", ids=("A1", "A2")), procedure("B", ids=("B1",))]
    declaration = joint("J", ["B", "A"])
    result = resolve(units, joints=[declaration])
    assert ids(result) == {"A", "B"}
    assert {j.semantic_id.value for j in result.receipt.joint_sources} == {"J"}
    assert result.receipt.combination_semantics == ((declaration.carrier_path, declaration.declaration.fields["combination_semantics"]),)
    # No cross-peer precedence is invented, even though one peer has more steps.
    assert {(e.before_constraint, e.after_constraint) for e in result.receipt.constraint_order} == {("A1", "A2")}


@pytest.mark.parametrize("filter_kind", ["scope", "time", "replace"])
def test_joint_cannot_resurrect_filtered_member(filter_kind):
    a = source("A")
    b = source("B", scope={"region": "us"}) if filter_kind == "scope" else source("B", effective_to="2025-01-01T00:00:00Z") if filter_kind == "time" else source("B", relations=[("REPLACE", "A")])
    result = resolve([a, b], query({"region": "eu"}, at_time=datetime(2026, 1, 1, tzinfo=timezone.utc)), [joint("J", ["A", "B"])])
    assert "UNQUALIFIED_JOINT_AUTHORITY" in codes(result)


def test_joint_near_miss_ordinary_relations_and_duplicate_ownership():
    units = [source("A"), source("B", relations=[("SUPPLEMENT", "A")])]
    assert "JOINT_ORDINARY_RELATIONS_SUFFICIENT" in codes(resolve(units, joints=[joint("J", ["A", "B"])]))
    units[1] = source("B")
    assert "DUPLICATE_JOINT_OWNERSHIP" in codes(resolve(units, joints=[joint("J", ["A", "B"]), joint("K", ["A", "B"])]))


def test_joint_source_identity_collision_and_extra_unrelated_authority():
    units = [source("A"), source("B")]
    assert "DUPLICATE_CURRENT_AUTHORITY" in codes(resolve(units, joints=[joint("A", ["A", "B"], path="docs/joint.md")]))
    assert resolve([*units, source("C")], joints=[joint("J", ["A", "B"])]).status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT


def test_distinct_reviewed_joint_sets_can_share_a_member_without_copying_it():
    units = [procedure("A"), procedure("B"), procedure("C")]
    result = resolve(units, joints=[joint("AB", ["A", "B"]), joint("BC", ["B", "C"])])
    assert ids(result) == {"A", "B", "C"}
    assert len(result.receipt.action_contracts) == 3
    assert len(result.receipt.activated_constraints) == 6
    assert all(edge.before_source == edge.after_source for edge in result.receipt.constraint_order)


@pytest.mark.parametrize("kwargs", [{"state": "PAUSED"}, {"state": "SUPERSEDED"}, {"authority": "candidate"},
                                   {"governed_action_classes": ["other"]}])
def test_inactive_joint_does_not_authorize_peers(kwargs):
    assert resolve([source("A"), source("B")], joints=[joint("J", ["A", "B"], **kwargs)]).status == AuthorityStatus.UNRESOLVED_AUTHORITY_CONFLICT


def test_joint_revision_is_required_and_peer_order_is_byte_stable():
    units = [procedure("A", mode=COMMIT), procedure("B", mode=COMMIT)]
    declaration = joint("J", ["B", "A"], mode=COMMIT)
    checks = attest([*units, declaration])
    result = resolve(units, joints=[declaration], snapshot_mode=COMMIT, evidence=checks)
    assert ids(result) == {"A", "B"}
    assert result.receipt.joint_sources[0].revision == declaration.revision
    rebuilt = resolve(units[::-1], joints=[joint("J", ["A", "B"], mode=COMMIT)], snapshot_mode=COMMIT, evidence=checks[::-1])
    assert rebuilt == result
    assert serialize_authority_result(rebuilt) == serialize_authority_result(result)
    checks[-1] = replace(checks[-1], verified_revision=None)
    assert resolve(units, joints=[declaration], snapshot_mode=COMMIT, evidence=checks).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY


@pytest.mark.parametrize("mode", ["REPLACE", "CORRECT", "SPECIALIZE"])
def test_joint_declarations_are_filtered_by_their_own_authored_relations(mode):
    units = [source("A"), source("B")]
    old = joint("OLD", ["A", "B"])
    new = joint("NEW", ["A", "B"], scope={"region": "eu"}, relations=[(mode, "OLD", {"region": "eu"})])
    result = resolve(units, query({"region": "eu"}), joints=[old, new])
    assert ids(result) == {"A", "B"}
    assert {s.semantic_id.value for s in result.receipt.joint_sources} == {"NEW"}
    assert any(r.carrier_path == old.carrier_path and r.reason == mode for r in result.receipt.removed_sources)
    outside = resolve(units, query({"region": "us"}), joints=[new, old])
    assert {s.semantic_id.value for s in outside.receipt.joint_sources} == {"OLD"}


def test_joint_declaration_replacement_cycles_cannot_be_hidden_by_admission():
    joints = [joint("J", ["A", "B"], relations=[("REPLACE", "K")]),
              joint("K", ["A", "B"], relations=[("CORRECT", "J")])]
    assert "AUTHORITY_REPLACEMENT_CYCLE" in codes(resolve([source("A"), source("B")], joints=joints))


@pytest.mark.parametrize("key", ["overlapping_current_canonical_sources", "ordinary_relations_insufficient", "irreducible_set_fact",
                                "independently_activated", "duplicate_ownership_rejected", "review_evidence"])
def test_unclear_joint_admission_is_not_inferred(key):
    declaration = joint("J", ["A", "B"])
    fields = dict(declaration.declaration.fields)
    admission = dict(fields["admission"])
    admission[key] = [] if key == "review_evidence" else False
    fields["admission"] = admission
    declaration = replace(declaration, declaration=RawDeclaration(fields))  # Deliberately invalid typed input.
    assert "UNQUALIFIED_JOINT_AUTHORITY" in codes(resolve([source("A"), source("B")], joints=[declaration]))


@pytest.mark.parametrize("available,freshness,status", [(None, "UNKNOWN", "MISSING_REQUIRED_AUTHORITY"),
    (False, "FRESH", "MISSING_REQUIRED_AUTHORITY"), (True, "UNKNOWN", "STALE_REQUIRED_AUTHORITY"),
    (True, "STALE", "STALE_REQUIRED_AUTHORITY"), (True, "FRESH", "RESOLVED")])
def test_explicit_availability_and_freshness(available, freshness, status):
    unit = source("A")
    result = resolve([unit], evidence=[AuthorityEvidence(unit.carrier_path, available, freshness)])
    assert result.status == AuthorityStatus(status)


def test_missing_required_authority_is_not_hidden_by_available_subset():
    result = resolve([source("A")], query(required_authorities=(SemanticId("B"),)))
    assert result.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    assert resolve([source("A")], evidence=[]).status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY


@pytest.mark.parametrize("scope,temporal", [(True, False), (False, True)])
def test_required_authority_filtered_by_scope_or_time_fails(scope, temporal):
    units = [source("A"), source("B", scope={"region": "us"} if scope else {},
                                 **({"authority_to": "2025-01-01T00:00:00Z"} if temporal else {}))]
    q = query({"region": "eu"}, required_authorities=(SemanticId("B"),), at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    result = resolve(units, q)
    assert "REQUIRED_AUTHORITY_INAPPLICABLE" in codes(result)
    assert result.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY


def test_temporal_same_id_carrier_handoff_is_order_independent():
    units = [source("A", path="docs/old.md", authority_to="2026-01-01T00:00:00Z"),
             source("A", path="docs/new.md", authority_from="2026-01-01T00:00:00Z")]
    q = query(at_time=datetime(2026, 1, 1, tzinfo=timezone.utc))
    result = resolve(units, q)
    assert result.receipt.governing_sources[0].carrier_path == units[1].carrier_path
    assert result == resolve(units[::-1], replace(q, at_time=datetime.fromisoformat("2026-01-01T01:00:00+01:00")))
    required = replace(q, required_authorities=(SemanticId("A"),))
    assert ids(resolve(units, required, evidence=attest([units[1]]))) == {"A"}


def test_revision_path_mismatch_and_worktree_attestation_cannot_be_durable():
    unit = source("A", mode=COMMIT)
    wrong = replace(unit, revision=replace(unit.revision, source_path="docs/wrong.md"))
    assert resolve([wrong], snapshot_mode=COMMIT).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY
    assert resolve([source("A")], evidence=attest([unit])).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY


def test_commit_receipt_exact_revision_and_mismatch_failure():
    unit = source("A", mode=COMMIT)
    result = resolve([unit], snapshot_mode=COMMIT)
    assert result.receipt.governing_sources[0].revision == unit.revision
    for check in [AuthorityEvidence(unit.carrier_path, True, "FRESH"),
                  AuthorityEvidence(unit.carrier_path, True, "FRESH", replace(unit.revision, content_digest="1" * 64)),
                  AuthorityEvidence(unit.carrier_path, True, "FRESH", unit.revision, replace(unit.revision, source_commit="b" * 40))]:
        assert resolve([unit], snapshot_mode=COMMIT, evidence=[check]).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY
    assert resolve([replace(unit, revision=None)], snapshot_mode=COMMIT).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY
    assert resolve([source("A")], query(require_revision=True)).status == AuthorityStatus.STALE_REQUIRED_AUTHORITY


def test_snapshot_and_evidence_collisions_fail():
    assert "AUTHORITY_SNAPSHOT_MISMATCH" in codes(resolve([source("A", mode=COMMIT)]))
    unit = source("A")
    assert "DUPLICATE_AUTHORITY_EVIDENCE" in codes(resolve([unit], evidence=attest([unit, unit])))
    assert "DUPLICATE_AUTHORITY_CARRIER" in codes(resolve([unit, unit]))


@pytest.mark.parametrize("available,freshness", [(False, "FRESH"), (None, "UNKNOWN"), (True, "STALE"), (True, "UNKNOWN")])
def test_required_private_state_fails_when_unavailable_or_stale(available, freshness):
    result = resolve([source("A")], query(required_private_dependencies=("PD",)), private_evidence=[PrivateStateEvidence("PD", available, freshness)])
    assert result.status == AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE


def test_verified_private_and_public_resolved_private_are_distinct_requirements():
    units = [source("PUBLIC")]
    private = [PrivateStateEvidence("PD", True, "FRESH")]
    assert ids(resolve(units, query(required_private_dependencies=("PD",)), private_evidence=private)) == {"PUBLIC"}
    assert ids(resolve(units, private_evidence=[PrivateStateEvidence("PD", False)])) == {"PUBLIC"}
    assert resolve(units, query(required_private_dependencies=("PD",))).status == AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE


def test_inactive_or_wrong_action_procedure_does_not_activate():
    for kwargs in [{"state": "PAUSED"}, {"state": "COMPLETED"}, {"governed_action_classes": ["other"]}]:
        result = resolve([procedure("P", **kwargs), source("A")])
        assert ids(result) == {"A"} and not result.receipt.activated_constraints


def test_duplicate_constraint_ids_fail_without_global_constraint_ids():
    duplicate = procedure("A", mandatory_constraints=[{"constraint_id": "C", "requirement": "first"},
                                                     {"constraint_id": "C", "requirement": "different"}])
    assert "DUPLICATE_CONSTRAINT_ID" in codes(resolve([duplicate]))
    result = resolve([procedure("A"), procedure("B", relations=[("SUPPLEMENT", "A")])])
    assert len(result.receipt.activated_constraints) == 4  # IDs are source-local.


def test_immutable_values_deterministic_input_and_relation_order():
    units = [source("BASE"), source("MID", relations=[("REPLACE", "BASE")]),
             procedure("NEW", relations=[("CORRECT", "MID"), ("REPLACE", "BASE")]),
             procedure("SUP", relations=[("SUPPLEMENT", "BASE")])]
    expected = resolve(units)
    assert ids(expected) == {"NEW", "SUP"}
    for seed in range(15):
        rng = random.Random(seed)
        rng.shuffle(units)
        checks = attest(units)
        rng.shuffle(checks)
        result = resolve([replace(s, relations=s.relations[::-1]) for s in units], evidence=checks)
        assert result == expected
        assert serialize_authority_result(result) == serialize_authority_result(expected)
    with pytest.raises(FrozenInstanceError):
        expected.status = AuthorityStatus.MISSING_REQUIRED_AUTHORITY
    blob = serialize_authority_result(expected)
    assert blob.endswith(b"\n") and b"\r\n" not in blob


def test_facet_set_order_and_query_requirement_order_do_not_change_receipt():
    unit = source("A", scope={"region": ["eu", "us"]})
    first = resolve([unit], query({"region": ["us", "eu"]}))
    second = resolve([replace(unit, scope=Scope({"region": ["us", "eu"]}))], query({"region": ["eu", "us"]}))
    assert first == second
    assert serialize_authority_result(first) == serialize_authority_result(second)
    assert query(required_private_dependencies=("B", "A")) == query(required_private_dependencies=("A", "B"))


def test_unavailable_and_stale_disposition_never_uses_path_priority():
    for paths in [("docs/a.md", "docs/z.md"), ("docs/z.md", "docs/a.md")]:
        units = [source("BASE", path=paths[0]), source("SUP", path=paths[1], relations=[("SUPPLEMENT", "BASE")])]
        checks = [AuthorityEvidence(paths[0], True, "STALE"), AuthorityEvidence(paths[1], False, "FRESH")]
        result = resolve(units, evidence=checks)
        assert result.status == AuthorityStatus.MISSING_REQUIRED_AUTHORITY
        assert codes(result) == {"AUTHORITY_UNAVAILABLE", "AUTHORITY_REVISION_OR_FRESHNESS_UNVERIFIED"}


def test_authority_is_pure_l2_without_io_or_dynamic_imports():
    tree = ast.parse((ROOT / "tools/project_knowledge/authority.py").read_text())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert {a.name for a in node.names} <= {"json"}
        if isinstance(node, ast.ImportFrom):
            assert (node.level == 1 and node.module == "model") or node.module in {"dataclasses", "datetime", "itertools", "typing"}
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"open", "eval", "exec", "__import__", "SemanticId"}


def test_qualified_cross_provider_scoped_supersession_and_retrieval():
    folder = ROOT / "docs/research/project_knowledge_candidate_01_q1_q2_cross_provider_v01"
    nominations = json.loads((folder / "RETRIEVAL_NOMINATIONS_V01.json").read_text())["queries"]
    oracle = json.loads((folder / "Q1_Q2_CROSS_PROVIDER_ORACLE_V01.json").read_text())["expectations"]
    shadow = (ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/SHADOW_DECISION_D011.md").read_text()
    declaration = json.loads(shadow.split("<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->")[1].split("<!-- PKA-STRUCTURED-DECLARATION-END -->")[0])
    # This old evidence encodes outgoing 'superseded by' links on D-011.
    # Production natural ownership puts REPLACE on each successor, targeting D-011.
    units = [source(declaration["semantic_id"])]
    for relation in declaration["relations"]:
        units.append(source(relation["target"], scope={"domain": relation["scope"]},
                            relations=[(relation["mode"], declaration["semantic_id"], {"domain": relation["scope"]})]))
    a = resolve(units, query({"domain": "v1_persistence_retrieval_architecture"}), retrieval_nominations=nominations["TASK_A"])
    assert a.status.value == oracle["task_a"]["resolution_status"]
    assert ids(a) == set(oracle["task_a"]["governing_ids"])
    b = resolve(units, retrieval_nominations=nominations["TASK_B"])
    assert b.status.value == oracle["task_b"]["resolution_status"]
    assert ids(resolve(units, query({"domain": declaration["residual_applicability"]}))) == {"D-011"}

    shadow = (ROOT / "docs/research/project_knowledge_candidate_01_q3_real_v01/SHADOW_DECISION_D015.md").read_text()
    declaration = json.loads(shadow.split("<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->")[1].split("<!-- PKA-STRUCTURED-DECLARATION-END -->")[0])
    relation = declaration["relations"][0]
    units = [source(declaration["semantic_id"]), source(relation["target"], scope={"domain": relation["scope"]},
                relations=[("REPLACE", declaration["semantic_id"], {"domain": relation["scope"]})])]
    assert ids(resolve(units, query({"domain": relation["scope"]}), retrieval_nominations=nominations["TASK_C"])) == set(oracle["task_c"]["governing_architecture_ids"])
    for outcome in oracle["task_c"]["retained_outcomes"]:
        assert outcome in declaration["retained_outcomes"]
        assert ids(resolve(units, query({"domain": outcome}))) == {"D-015"}


def test_qualified_shadow_supplement_and_private_cases():
    folder = ROOT / "docs/research/project_knowledge_candidate_01_shadow_v02"
    fixture = json.loads((folder / "SHADOW_OPERATIONAL_FIXTURE_V02.json").read_text())
    oracle = json.loads((folder / "SHADOW_OPERATIONAL_ORACLE_V02.json").read_text())["expectations"]
    units = [source(s["source_id"], scope={k: v for k, v in s["scope"].items() if k != "action"},
                    relations=[(r["relation"], r["target"]) for r in s["relations"]])
             for s in fixture["authority_sources"] if s["scope"]["action"] == "safe_deploy"]
    result = resolve(units, replace(query({"environment": "prod"}), action="safe_deploy"))
    assert ids(result) == set(oracle["authority_uncertainty"]["AUTH-COMPLETE"]["governing_sources"])
    for scenario in fixture["private_scenarios"]:
        record = next(r for r in fixture["public_records"] if r["public_id"] == scenario["public_record_id"])
        required = (record["private_dependency_id"],) if scenario["action"] in record["private_required_for"] else ()
        result = resolve([source(record["public_id"])], replace(query(required_private_dependencies=required), action=scenario["action"]),
                         private_evidence=[PrivateStateEvidence("PD-1", scenario["private_available"], "FRESH" if scenario["private_available"] else "UNKNOWN")])
        expected = oracle["private_boundary"][scenario["scenario_id"]]["status"]
        assert (result.status == AuthorityStatus.RESOLVED) == expected.startswith("PASS_")
        blob = serialize_authority_result(result)
        assert all(leak.encode() not in blob for leak in oracle["private_boundary"]["forbidden_public_leaks"])
