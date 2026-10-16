"""Non-scored provenance and guard tests; no tasks, answers or arm execution."""

import copy
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

import pytest

from experiments.r0_p03_navigation_probe import role_frame_candidate as frame

REPO = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def report():
    return frame.build_capacity_parity_diagnostic(REPO)


def test_receipt_reproducible_from_published_sources(report):
    saved = json.loads((REPO / "experiments/r0_p03_navigation_probe/"
                       "task_capacity_parity_diagnostic_candidate.json").read_text("utf-8"))
    assert report == saved == frame.build_capacity_parity_diagnostic(REPO)
    assert report["source_ref"] == frame.SOURCE_REF
    assert report["engineering_design_ref"] == frame.DIAGNOSTIC_DESIGN_REF
    assert len(report["engineering_design_input_blobs"]) == 3
    assert report["event_count"] == 36
    assert {e["event_id"] for e in report["events"]} == {f"D-{i:03}" for i in range(1, 37)}
    assert report["classification"] == "EXPOSED_ENGINEERING_DIAGNOSTIC_NOT_TASKS_GOLD_OR_FIXTURE"
    assert not {"selected_tasks", "gold_answers", "selected_build", "heldout_paths", "scores"}.intersection(report)


@pytest.mark.parametrize("ref", ["HEAD", frame.DIAGNOSTIC_DESIGN_REF])
def test_diagnostic_rejects_changed_source_pin(ref):
    with pytest.raises(ValueError, match="historical role-frame pin"):
        frame.build_capacity_parity_diagnostic(REPO, ref)


def test_capacity_is_cited_signal_ceiling_not_twelve_answers(report):
    expected = [(21, 14), (7, 6), (12, 8), (17, 12)]
    for value, (hinted, cited) in zip(report["category_capacity"].values(), expected):
        assert value["lexical_hint_events"] == hinted
        assert value["hint_with_resolved_citation_events"] == cited
        assert value["independently_answerable_task_count"] is None
        assert value["qualification"].startswith("NOT_ESTABLISHED")
    assert report["distinct_event_signal_capacity_upper_bound"] == 12
    assert sum(any(r["status"] == "RESOLVED_FILE" for r in e["references"])
               for e in report["events"]) == 21
    assert frame.distinct_event_capacity({c: ["A", "B", "C"] for c in frame.TASK_SIGNALS}) == 3
    assert frame.distinct_event_capacity({c: [] for c in frame.TASK_SIGNALS}) == 0


def test_lexical_owner_or_accepted_status_does_not_prove_task():
    lines = ["## D-001. Current product evolution authority", "**Status:** Accepted",
             "**Date:** 2000-01-01", "Owner selected this."]
    event, = frame.decision_events(lines)
    assert all(event["lexical_signal_lines"].values())
    assert event["owner_mentioned"]
    assert frame.source_references(lines, "docs/DECISIONS.md", {}, {}) == []
    assert "answerable" not in event


def test_source_headers_and_lifecycle_are_literal_not_authority(report):
    observations = report["source_header_observations"]
    assert len(observations) == 74
    assert sum(bool(x["literal_metadata_first_forty_lines"]) for x in observations.values()) == 62
    assert all(not x["authority_or_task_eligibility_certified"] for x in observations.values())
    spec = observations["docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md"]
    assert any("does not switch operational authority" in r["text"]
               for r in spec["literal_metadata_first_forty_lines"])
    assert frame.source_metadata(["**Status:** Proposed", "# Accepted somewhere else"]) == [
        {"line": 1, "text": "**Status:** Proposed"}]
    assert frame.source_metadata([""] * 40 + ["**Status:** Accepted"]) == []
    statuses = report["raw_status_counts"]
    assert statuses["Accepted"] == 20
    assert sum(statuses.values()) == 36
    assert len(statuses) > 5  # Scoped supersession and selection are not flattened.


def test_reference_gaps_outside_frame_and_large_neighborhoods_retained(report):
    events = {e["event_id"]: e for e in report["events"]}
    assert "pyproject.toml" in events["D-030"]["observed_reference_neighborhood"]["direct_outside_role_frame"]
    assert any(p.startswith("prototype_v0/") for p in events["D-026"]["observed_reference_neighborhood"]["direct_outside_role_frame"])
    assert any(r["status"] == "MISSING" for r in events["D-033"]["references"])
    assert sum(e["observed_reference_neighborhood"]["two_hop_exceeds_sixty"] for e in events.values()) == 5
    assert all(not e["observed_reference_neighborhood"]["complete_task_closure"] for e in events.values())
    assert all(e["source_provenance"]["git_commit"] == frame.SOURCE_REF for e in events.values())


def test_missing_ambiguous_and_directory_links_not_silently_resolved():
    roster = {"docs/research/001_a.md": "a", "docs/research/001_b.md": "b",
              "tools/a.py": "c"}
    refs = frame.source_references(["Research 001 `tools/` `docs/missing.md`"],
                                   "docs/DECISIONS.md", roster, frame.reference_index(roster))
    assert {r["status"] for r in refs} == {"AMBIGUOUS_ID", "DIRECTORY_UNEXPANDED", "MISSING"}


def test_exact_citations_and_incomplete_carriers_not_conflated(report):
    audit = report["substrate_audit"]
    assert len(audit["source_citation_witnesses"]) == 11
    assert all(w["citation_exact"] for w in audit["source_citation_witnesses"])
    assert audit["shared_capabilities_complete"]
    assert audit["carrier_required_fields_absent_in_specimen"]["git_commit"] == 10
    assert audit["carrier_required_fields_absent_in_specimen"]["natural_owner"] == 10
    assert audit["synthetic_j2_analogues"] == 1
    assert not audit["accepted_j2_coverage_demonstrated_by_specimen"]
    assert audit["independent_semantics_and_runtime_parity"] == "NOT_QUALIFIED"
    assert audit["derived_checkpoint_status"] == "STALE_CHECKPOINT_MISMATCH"
    assert (audit["derived_checkpoint"], audit["source_routing_checkpoint"]) == (564, 895)


def test_tampered_source_citation_rejected(monkeypatch):
    original = frame.pinned_texts

    def altered(repo, roster, paths):
        result = original(repo, roster, paths)
        path = "docs/current_routing.json"
        if path in result:
            result[path][2] = '    "current_checkpoint": 0,'
        return result

    monkeypatch.setattr(frame, "pinned_texts", altered)
    with pytest.raises(ValueError, match="citation differs"):
        frame.build_capacity_parity_diagnostic(REPO)


@pytest.mark.parametrize("damage", ["body", "kind", "trailer", "truncated"])
def test_git_batch_integrity_errors_fail_closed(monkeypatch, damage):
    body = b"hello\n"
    oid = hashlib.sha1(b"blob 6\0" + body).hexdigest()
    raw = f"{oid} blob 6\n".encode() + body + b"\n"
    if damage == "body":
        raw = raw.replace(b"hello", b"jello")
    elif damage == "kind":
        raw = raw.replace(b"blob", b"tree")
    elif damage == "trailer":
        raw += b"unexpected"
    else:
        raw = raw[:-2]
    monkeypatch.setattr(frame.subprocess, "run", lambda *a, **kw: SimpleNamespace(stdout=raw))
    with pytest.raises(ValueError):
        frame.pinned_texts(REPO, {"a.md": oid}, {"a.md"})


def views():
    view = {"source_ref": frame.SOURCE_REF, "capabilities": list(frame.CAPABILITIES),
            "records": [{"id": "synthetic", "governing": False}], "common_relations": []}
    return {arm: copy.deepcopy(view) for arm in ("B0", "B1", "B2", "B3", "B4")}


def test_identical_neutral_views_and_optional_b4():
    shared = views()
    assert frame.shared_view_issues(shared) == []
    shared.pop("B4")
    assert frame.shared_view_issues(shared) == []
    shared.pop("B0")
    assert "ARM_SET_MISMATCH" in frame.shared_view_issues(shared)


@pytest.mark.parametrize("capability", frame.CAPABILITIES)
def test_b0_actual_capabilities_cannot_be_removed(capability):
    shared = views()
    shared["B0"]["capabilities"].remove(capability)
    assert frame.shared_view_issues(shared) == ["COMMON_CAPABILITY_MISMATCH", "UNEQUAL_SHARED_VIEWS"]


@pytest.mark.parametrize("key", sorted(frame.NAVIGATION_KEYS))
def test_arm_navigation_contamination_rejected_even_when_equal(key):
    shared = views()
    for view in shared.values():
        view["records"][0][key] = ["synthetic"]
    assert frame.shared_view_issues(shared) == ["ARM_NAVIGATION_IN_SHARED_VIEW"]


def test_equal_bytes_do_not_excuse_wrong_source_pin():
    shared = views()
    for view in shared.values():
        view["source_ref"] = frame.DIAGNOSTIC_DESIGN_REF
    assert frame.shared_view_issues(shared) == ["COMMON_SOURCE_REF_MISMATCH"]


@pytest.mark.parametrize("role", ["unaccepted_physical_tree_research_proposal", "realizer_source_candidate",
                                  "realization_schema_candidate", "test_implementation_source",
                                  "incumbent_generated_identity_projection", "incumbent_generated_current_state_projection"])
def test_false_governing_claims_cannot_be_laundered_by_status(role):
    assert "NON_GOVERNING_SOURCE_ROLE" in frame.authority_claim_issues({
        "governing": True, "role": role, "status": "SOURCE_REVIEWED_ACCEPTED_GOVERNING",
        "accepted_effect_reference": "synthetic"})
    assert "UNSUPPORTED_GOVERNING_PROMOTION" in frame.authority_claim_issues({"governing": True})


@pytest.mark.parametrize("record", [{"status": "SYNTHETIC_V03_ANALOGUE_NOT_GOVERNING_J2"},
                                   {"status": "IMPLEMENTATION_SOURCE_NOT_ACCEPTANCE_PROOF"},
                                   {"status": "SOURCE_REVIEWED_ACCEPTED_J2"}])
def test_inferred_j2_coverage_rejected(record):
    assert frame.authority_claim_issues(dict(record, accepted_j2_coverage=True)) == ["INFERRED_J2_COVERAGE"]


def test_scoped_positive_claim_guards_are_not_acceptance_oracles():
    assert frame.authority_claim_issues({"governing": True, "status": "SOURCE_REVIEWED_ACCEPTED_GOVERNING",
                                        "accepted_effect_reference": "synthetic"}) == []
    assert frame.authority_claim_issues({"accepted_j2_coverage": True, "status": "SOURCE_REVIEWED_ACCEPTED_J2",
                                        "source_owned_coverage_reference": "synthetic"}) == []
    assert frame.derived_checkpoint_status({}, {}) == "FRESHNESS_UNVERIFIED"
    core = {"active_workstream": {"execution_anchor": {"checkpoint": 1}}}
    assert frame.derived_checkpoint_status(core, {"current_checkpoint": 2}) == "STALE_CHECKPOINT_MISMATCH"
    assert frame.derived_checkpoint_status(core, {"current_checkpoint": 1}) == "CHECKPOINT_MATCH_DIGEST_FRESHNESS_UNVERIFIED"


def test_b2_duplicate_reverse_and_different_meaning_distinguished():
    common = [{"source_reference": "A", "target_reference": "B", "scope": "synthetic",
               "semantic_relation_family": "lineage"}]
    extra = dict(common[0])
    assert frame.b2_link_diagnostic(common, extra) == "DUPLICATE_OR_REVERSE_COMMON_RELATION"
    extra.update(source_reference="B", target_reference="A")
    assert frame.b2_link_diagnostic(common, extra) == "DUPLICATE_OR_REVERSE_COMMON_RELATION"
    extra["semantic_relation_family"] = "about"
    assert frame.b2_link_diagnostic(common, extra) == "COMMON_ENDPOINT_COLLISION_SEMANTICS_UNQUALIFIED"
    extra["target_reference"] = "C"
    assert frame.b2_link_diagnostic(common, extra) == "NON_DUPLICATE_ENDPOINTS_SEMANTICS_UNQUALIFIED"
    extra["governing"] = True
    assert frame.b2_link_diagnostic(common, extra) == "INVALID_AUTHORITY_OR_COVERAGE"
