"""G010 production qualification through G009; fixtures never become authority."""

from copy import deepcopy
from dataclasses import replace
import hashlib
import json
from pathlib import Path
import random
import re

import pytest
from jsonschema import Draft202012Validator

from tools.project_knowledge.adapters.gitio import commit_snapshot, worktree_snapshot
from tools.project_knowledge.adapters.pure import resolve_unit
from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.model import RawDeclaration, SnapshotMode, ViewFreshnessStatus, ViewInput
from tools.project_knowledge.services.generation import generate_views, check_view_freshness, _capabilities
from tools.project_knowledge.services.validation import validate_repository, validate_declaration
from tools.project_knowledge.view_definitions import (
    PURE_UNIT_REGISTRY, current_state_core_specification, production_view_specifications,
    source_inventory_specification,
)
from tools.project_knowledge.views import build_views, deterministic_json, ViewValidationError
from tools.project_knowledge.workstreams import workstream_from_source
from tests.unit.test_project_knowledge_views import git, write, commit


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures/project_knowledge_g010"
HISTORICAL = ROOT / "docs/research/project_knowledge_candidate_01_current_state_core_v01"
ACTIVE = "docs/work/active.json"
PAUSED = "docs/work/paused.json"
BOUNDARY = "docs/boundary.json"
SPECIFICATION = "docs/specification.json"
EXPERIMENT = "docs/experiment.json"
COMPATIBILITY = ("docs/CURRENT_STATE.md", "docs/current_routing.json", "docs/CONTINUITY.md", "docs/KNOWLEDGE_MAP.md")


def corpus():
    return json.loads((FIXTURES / "corpus.json").read_bytes())


@pytest.fixture
def core_repo(tmp_path):
    git(tmp_path, "init", "--quiet")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    git(tmp_path, "config", "user.name", "G010 isolated fixture")
    git(tmp_path, "config", "core.autocrlf", "false")
    implementation_files = {
        path
        for specification in (*production_view_specifications(), source_inventory_specification())
        for path in specification.generator.implementation_files
    }
    for path in sorted(implementation_files):
        write(tmp_path, path, (ROOT / path).read_bytes())
    for path, declaration in corpus().items():
        write(tmp_path, path, deterministic_json(declaration))
    commit(tmp_path)
    return tmp_path


def build(root, selected=None, specs=None):
    return generate_views(commit_snapshot(root, "HEAD"), specs or (current_state_core_specification(),),
                          selected_view_ids=selected)


def change(root, path, action):
    declaration = json.loads((root / path).read_bytes())
    action(declaration)
    write(root, path, deterministic_json(declaration))
    return commit(root)


def reject_build_and_freshness(root, old, code):
    with pytest.raises(ViewValidationError) as error:
        build(root)
    assert code in {d.code for d in error.value.diagnostics}
    status = check_view_freshness(commit_snapshot(root, "HEAD"), (current_state_core_specification(),),
                                 "current_state_core", old.manifest, existing_view_bytes=old.view_bytes)
    assert status.status == ViewFreshnessStatus.INVALID
    assert code in {d.code for d in status.diagnostics}


def pointer(value, path):
    for key in path.split("."):
        value = value[int(key)] if isinstance(value, list) else value[key]
    return value


def test_production_fixture_strict_admission_and_legacy_anchor_projection(core_repo):
    snapshot = commit_snapshot(core_repo, "HEAD")
    validation = validate_repository(snapshot)
    assert validation.ok and len(validation.sources) == 8
    active = next(s for s in validation.sources if s.carrier_path == ACTIVE)
    route = workstream_from_source(active)
    assert route.current_anchor == corpus()[ACTIVE]["execution_anchor"]["current_boundary"]
    assert "current_anchor" not in active.declaration.fields
    assert active.declaration.fields["stage"]["stage_id"] == "RESEARCH:124"
    for path, value in corpus().items():
        encoded = deterministic_json(value)
        assert validate_declaration(encoded, path, SchemaValidator())[1] == ()
        markdown = b"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\n" + encoded + b"<!-- PKA-STRUCTURED-DECLARATION-END -->\n"
        raw, diagnostics = validate_declaration(markdown, "docs/carrier.md", SchemaValidator())
        assert not diagnostics and raw == RawDeclaration(value)


def test_frozen_historical_hashes():
    for name, digest in (
        ("CURRENT_STATE_CORE_FIXTURE_V01.json", "4b7ac27801e7d89c0cd782c895d6d0db47693916e4aae7696eb3fc4d6081ad38"),
        ("CURRENT_STATE_CORE_ORACLE_V01.json", "f7ceee34aa68d79dea8df4043bf5b1711f3a31078cf86d48bfc3b3f0b008af35"),
    ):
        assert hashlib.sha256((HISTORICAL / name).read_bytes()).hexdigest() == digest


def test_exact_crosswalk_all_23_and_frozen_output_contract(core_repo):
    result, = build(core_repo)
    assert result.view_bytes == (FIXTURES / "expected_core.json").read_bytes()
    core = json.loads(result.view_bytes)
    schema = json.loads((FIXTURES / "current_state_core.v1.schema.json").read_bytes())
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(core)
    crosswalk = json.loads((FIXTURES / "crosswalk.json").read_bytes())
    original = json.loads((HISTORICAL / "CURRENT_STATE_CORE_FIXTURE_V01.json").read_bytes())
    assert crosswalk["qualification_only"] is True
    assert [r["id"] for r in crosswalk["items"]] == [r["id"] for r in original["must_preserve_manifest"]]
    assert len(crosswalk["items"]) == 23
    core_rows = [r for r in crosswalk["items"] if "core_pointer" in r]
    assert len(core_rows) == 15
    assert {r["id"] for r in core_rows} == {r["id"] for r in original["must_preserve_manifest"] if r["required_in_core"]}
    bindings = {r["source_key"]: r for r in original["shadow_sources"] + original["real_sources"]}
    raw_cache = {}
    for row in crosswalk["items"]:
        owner = row["source_binding"]
        assert owner == bindings[owner["source_key"]]
        for binding in [owner, *row.get("evidence_bindings", [])]:
            assert binding == bindings[binding["source_key"]]
            key = binding["source_key"]
            if key not in raw_cache:
                raw_cache[key] = ((ROOT / binding["path"]).read_bytes() if binding in original["shadow_sources"]
                                  else git(ROOT, "show", crosswalk["real_base_commit"] + ":" + binding["path"]))
            raw = raw_cache[key]
            assert hashlib.sha256(raw).hexdigest() == binding["sha256"] and len(raw) == binding["bytes"]
        raw = raw_cache[owner["source_key"]]
        if owner in original["shadow_sources"]:
            declaration = json.loads(re.search(rb"<!-- PKA-STRUCTURED-DECLARATION-BEGIN -->\s*(.*?)\s*<!-- PKA-STRUCTURED-DECLARATION-END -->", raw, re.S)[1])
            historical = ({key: pointer(declaration, path) for key, path in row["historical_members"].items()}
                          if "historical_members" in row else pointer(declaration, row["historical_pointer"]))
            assert historical == row["historical_value"]
        else:
            assert row["evidence_text"].encode() in raw
        if "core_pointer" in row:
            assert pointer(core, row["core_pointer"]) == row.get("production_identity", row["historical_value"])
            if "milestone_id" in row:
                assert pointer(core, row["core_pointer"].rsplit(".", 1)[0])["milestone_id"] == row["milestone_id"]
        else:
            assert len(row["evidence_bindings"]) == 4
            # Compare semantic fields, not a scalar search: PENDING may occur in
            # a legitimate milestone without duplicating an audit/backup fact.
            shadow_key = row["historical_pointer"].split(".")[-1] if row["historical_pointer"] else "prospective_compare_total"
            assert shadow_key.encode() not in result.view_bytes
            assert json.dumps(row["historical_value"]).encode() not in result.view_bytes
    assert len(result.view_bytes) <= 2048
    assert b"Research 113" not in result.view_bytes
    assert core["active_workstream"]["objective"] == corpus()[ACTIVE]["objective"]
    assert core["active_workstream"]["semantic_id"] == corpus()[ACTIVE]["semantic_id"]
    assert core["integration_boundary"]["semantic_id"] == corpus()[BOUNDARY]["semantic_id"]
    assert core["current_experiment"]["semantic_id"] == corpus()[EXPERIMENT]["semantic_id"]
    assert core["paused_workstreams"][0]["semantic_id"] == corpus()[PAUSED]["semantic_id"]
    assert result.manifest.fields["authority_class"] == "derived"
    assert result.manifest.fields["generator"]["implementation_basis"] == "GIT_BLOB_BYTES_AT_COMMIT"


@pytest.mark.parametrize("path", [ACTIVE, BOUNDARY, SPECIFICATION, EXPERIMENT])
@pytest.mark.parametrize("mutation", ["missing", "duplicate", "noncanonical"])
def test_required_roles_fail_without_tiebreak(core_repo, path, mutation):
    old, = build(core_repo)
    if mutation == "missing":
        (core_repo / path).unlink()
    else:
        value = json.loads((core_repo / path).read_bytes())
        if mutation == "duplicate":
            value["semantic_id"] = "AAA:DIFFERENT-OWNER"
            write(core_repo, "docs/000-arbitrary-first.json", deterministic_json(value))
        else:
            value["authority_class"] = "candidate"
            write(core_repo, path, deterministic_json(value))
    commit(core_repo)
    reject_build_and_freshness(core_repo, old, "CURRENT_STATE_ROLE_CARDINALITY")


@pytest.mark.parametrize("path", ["docs/research-stage.json", "docs/ingestion.json", "docs/procedure.json"])
@pytest.mark.parametrize("mutation", ["missing", "ambiguous", "candidate"])
def test_semantic_references_resolve_exactly(core_repo, path, mutation):
    old, = build(core_repo)
    if mutation == "missing":
        (core_repo / path).unlink()
    elif mutation == "ambiguous":
        write(core_repo, "docs/duplicate-reference.json", (core_repo / path).read_bytes())
    else:
        change(core_repo, path, lambda value: value.update(authority_class="candidate"))
    commit(core_repo) if mutation != "candidate" else None
    reject_build_and_freshness(core_repo, old, "DUPLICATE_VIEW_INPUT_IDENTITY" if mutation == "ambiguous" else "CURRENT_STATE_ROLE_CARDINALITY")


# Present malformed declarations must fail at schema admission before compute.
BAD_CONTROLS = [
    (ACTIVE, "execution_anchor", {}),
    (ACTIVE, "execution_anchor.checkpoint", -1),
    (ACTIVE, "execution_anchor.checkpoint", True),
    (ACTIVE, "execution_anchor.development_branch", "  "),
    (ACTIVE, "execution_anchor.pull_request", 0),
    (ACTIVE, "execution_anchor.pull_request", False),
    (ACTIVE, "execution_anchor.current_boundary", "docs/path.md"),
    (ACTIVE, "execution_anchor.payload", {}),
    (ACTIVE, "current_anchor", "second authority"),
    (ACTIVE, "stage", {}),
    (ACTIVE, "stage.stage_id", "bad identity"),
    (ACTIVE, "stage.stage_state", {}),
    (ACTIVE, "stage.payload", "extra"),
    (PAUSED, "governing_procedure", "docs/procedure.md"),
    (PAUSED, "orientation_milestones", [{"milestone_id": "M", "state": "ACTIVE"}, {"milestone_id": "M", "state": "PAUSED"}]),
    (PAUSED, "orientation_milestones", [{"milestone_id": "M", "state": "ACTIVE"}] * 2),
    (PAUSED, "orientation_milestones", [{"milestone_id": "M", "state": "INVALID"}]),
    (PAUSED, "orientation_milestones", [{"milestone_id": "M", "state": "ACTIVE", "value": 42}]),
    (PAUSED, "orientation_milestones", [{"milestone_id": "M", "state": "ACTIVE", "metadata": {}}]),
    (PAUSED, "orientation_milestones", [{"milestone_id": "docs/path", "state": "ACTIVE"}]),
    (BOUNDARY, "promoted_branch", " "),
    (BOUNDARY, "promoted_commit", "A" * 40),
    (BOUNDARY, "promoted_commit", "a" * 39),
    (BOUNDARY, "promoted_commit", "a" * 40 + "\n"),
    (BOUNDARY, "facts", {"value": 1}),
    (EXPERIMENT, "outcome", {}),
    (EXPERIMENT, "outcome", "not valid"),
    (EXPERIMENT, "value", "arbitrary"),
    (SPECIFICATION, "outcome", "INCOMPLETE"),
]


def assign(value, path, new):
    keys = path.split(".")
    for key in keys[:-1]:
        value = value[key]
    value[keys[-1]] = new


@pytest.mark.parametrize("path,control,new", BAD_CONTROLS)
def test_refined_schema_strictness(path, control, new):
    value = corpus()[path]
    assign(value, control, new)
    findings = SchemaValidator().validate(RawDeclaration(value))
    assert findings and all(d.code == "PROFILE_SCHEMA_VIOLATION" for d in findings)


@pytest.mark.parametrize("path,control", [(EXPERIMENT, "outcome"), (BOUNDARY, "promoted_branch"), (BOUNDARY, "promoted_commit")])
def test_required_typed_controls_fail_durable_admission(core_repo, path, control):
    old, = build(core_repo)
    change(core_repo, path, lambda value: value.pop(control))
    reject_build_and_freshness(core_repo, old, "PROFILE_SCHEMA_VIOLATION")


@pytest.mark.parametrize("controls", [{}, {"promoted_branch": "branch"}, {"promoted_commit": "a" * 40}, {"promoted_branch": "branch", "promoted_commit": "a" * 40}])
def test_nonintegration_boundary_pair_contract(controls):
    value = corpus()[BOUNDARY]
    value.pop("promoted_branch")
    value.pop("promoted_commit")
    value.update(kind="OTHER_BOUNDARY", **controls)
    assert bool(SchemaValidator().validate(RawDeclaration(value))) == (len(controls) == 1)


@pytest.mark.parametrize("path,control", [(ACTIVE, "execution_anchor"), (ACTIVE, "stage"), (SPECIFICATION, "semantic_id")])
def test_schema_optional_but_core_required_controls_fail_visibly(core_repo, path, control):
    old, = build(core_repo)
    change(core_repo, path, lambda value: value.pop(control))
    reject_build_and_freshness(core_repo, old, "CURRENT_STATE_MISSING_CONTROL")


def test_deterministic_full_selected_and_permuted_inputs(core_repo):
    spec = current_state_core_specification()
    specs = (spec, source_inventory_specification())
    first, = build(core_repo)
    assert build(core_repo) == (first,)
    assert build(core_repo, (spec.view_id,), specs) == (first,)
    assert next(r for r in build(core_repo, specs=specs[::-1]) if r.view_id == spec.view_id) == first
    validation = validate_repository(commit_snapshot(core_repo, "HEAD"))
    inputs = [ViewInput(s, (core_repo / s.carrier_path).read_bytes()) for s in validation.sources]
    blobs = {p: (core_repo / p).read_bytes() for p in spec.generator.implementation_files}
    resolved = replace(spec, compute=resolve_unit(spec.compute, PURE_UNIT_REGISTRY, blobs, _capabilities()), serialize=deterministic_json)
    for seed in range(6):
        random.Random(seed).shuffle(inputs)
        assert build_views((resolved,), inputs, blobs, snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT) == (first,)
    change(core_repo, PAUSED, lambda value: value["orientation_milestones"].reverse())
    reordered, = build(core_repo)
    assert reordered.view_bytes == first.view_bytes
    assert reordered.manifest_bytes != first.manifest_bytes  # exact source bytes changed


def test_all_paused_owners_sorted_for_presentation_only(core_repo):
    value = corpus()[PAUSED]
    value["semantic_id"] = "AAA:SECOND-PAUSED"
    write(core_repo, "docs/zzz-second-paused.json", deterministic_json(value))
    other = deepcopy(value)
    other.update(semantic_id="AAA:NOT-RESUMABLE", expected_to_resume=False)
    write(core_repo, "docs/000-inactive-paused.json", deterministic_json(other))
    commit(core_repo)
    result, = build(core_repo)
    assert [w["semantic_id"] for w in json.loads(result.view_bytes)["paused_workstreams"]] == ["AAA:SECOND-PAUSED", corpus()[PAUSED]["semantic_id"]]


def test_paused_projection_accepts_spec028_minimal_resumable_workstream(core_repo):
    write(core_repo, "docs/cockpit-target.json", deterministic_json({
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "RESUME_TARGET",
        "authority_class": "canonical", "semantic_id": "COCKPIT:RESUME",
    }))
    write(core_repo, "docs/work/cockpit.json", deterministic_json({
        "schema_version": "1", "profile": "workstream.v1", "kind": "COCKPIT_WORKSTREAM",
        "authority_class": "canonical", "semantic_id": "AAA:COCKPIT", "state": "PAUSED",
        "objective": "Resume Cockpit design", "expected_to_resume": True,
        "pause_reason": "Other work is active", "return_condition": "Owner explicitly returns",
        "resume_target": "COCKPIT:RESUME",
    }))
    commit(core_repo)
    result, = build(core_repo)
    paused = json.loads(result.view_bytes)["paused_workstreams"]
    assert paused[0] == {"semantic_id": "AAA:COCKPIT", "state": "PAUSED", "resume_target": "COCKPIT:RESUME"}
    assert paused[1]["semantic_id"] == corpus()[PAUSED]["semantic_id"]


def test_governing_procedure_reference_must_resolve_to_procedure_profile(core_repo):
    old, = build(core_repo)
    write(core_repo, "docs/procedure.json", deterministic_json({
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "NOTE",
        "authority_class": "canonical", "semantic_id": corpus()[PAUSED]["governing_procedure"],
    }))
    commit(core_repo)
    reject_build_and_freshness(core_repo, old, "CURRENT_STATE_REFERENCE_TYPE")


@pytest.mark.parametrize("mutation", ["anchor", "outcome", "milestone"])
def test_meaningful_change_stales_exact_bindings(core_repo, mutation):
    old, = build(core_repo)
    if mutation == "anchor":
        change(core_repo, ACTIVE, lambda value: value["execution_anchor"].update(checkpoint=502))
    elif mutation == "outcome":
        change(core_repo, EXPERIMENT, lambda value: value.update(outcome="COMPLETED"))
    else:
        change(core_repo, PAUSED, lambda value: value["orientation_milestones"][0].update(state="ACTIVE"))
    new, = build(core_repo)
    assert new.view_bytes != old.view_bytes and new.manifest_bytes != old.manifest_bytes
    status = check_view_freshness(commit_snapshot(core_repo, "HEAD"), (current_state_core_specification(),),
                                 "current_state_core", old.manifest, existing_view_bytes=old.view_bytes)
    assert status.status == ViewFreshnessStatus.STALE
    assert {"STALE_VIEW_INPUTS", "STALE_VIEW_BOUNDARY", "STALE_VIEW_CONTENT"} <= {d.code for d in status.diagnostics}


def test_carrier_movement_and_unrelated_source_do_not_select_semantics(core_repo):
    old, = build(core_repo)
    for index, path in enumerate(corpus()):
        (core_repo / path).rename(core_repo / ("docs/moved-" + str(index) + ".json"))
    unrelated = {"schema_version": "1", "profile": "semantic_source.v1", "kind": "NOTE", "authority_class": "canonical"}
    write(core_repo, "docs/000-unrelated.json", deterministic_json(unrelated))
    commit(core_repo)
    new, = build(core_repo)
    assert new.view_bytes == old.view_bytes and new.manifest_bytes != old.manifest_bytes
    assert len(new.manifest.fields["input_bindings"]) == 9  # declared all-canonical selector


def test_no_oracle_compatibility_writes_or_migration(core_repo):
    before, = build(core_repo)
    # Invalid UTF-8 would fail discovery if any target were read. Even a
    # canonical declaration at a compatibility path cannot become an input.
    for path in COMPATIBILITY:
        write(core_repo, path, b"\xffMUST NOT READ\x00")
    write(core_repo, COMPATIBILITY[0], deterministic_json(corpus()[ACTIVE]))
    oracle = "docs/research/project_knowledge_candidate_01_current_state_core_v01/CURRENT_STATE_CORE_ORACLE_V01.json"
    write(core_repo, oracle, b"\xffPOISONED ORACLE")
    write(core_repo, "docs/project_knowledge/generated/current_state_core.json", b"\xffold artifact")
    commit(core_repo)
    all_paths = [p for p in core_repo.rglob("*") if p.is_file() and ".git" not in p.parts]
    captured = {p: p.read_bytes() for p in all_paths}
    after, = build(core_repo)
    assert after == before
    assert all(p.read_bytes() == value for p, value in captured.items())
    assert set(captured) == {p for p in core_repo.rglob("*") if p.is_file() and ".git" not in p.parts}
    assert not git(core_repo, "status", "--porcelain")
    assert not set(COMPATIBILITY) & {b["source_path"] for b in after.manifest.fields["input_bindings"]}
    spec = current_state_core_specification()
    assert spec.compute_identity == "current_state_core.v1" and spec.serialize_identity == "canonical_json.v1"
    for path in spec.generator.implementation_files:
        content = (ROOT / path).read_text(encoding="utf-8")
        assert "ORACLE_V01" not in content and "scripts.research" not in content
        assert "4b7ac278" not in content and "2480109fadeee" not in content


def test_worktree_remains_noncommitted(core_repo):
    with pytest.raises(ViewValidationError, match="WORKTREE"):
        generate_views(worktree_snapshot(core_repo), (current_state_core_specification(),))


@pytest.mark.parametrize("path,control,new", [BAD_CONTROLS[0], BAD_CONTROLS[8], BAD_CONTROLS[14]])
def test_adversarial_workstream_controls_reject_durable_build(core_repo, path, control, new):
    old, = build(core_repo)
    change(core_repo, path, lambda value: assign(value, control, new))
    reject_build_and_freshness(core_repo, old, "PROFILE_SCHEMA_VIOLATION")
