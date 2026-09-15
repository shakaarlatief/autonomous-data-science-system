from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.model import Profile, RawDeclaration


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests/fixtures/project_knowledge"


def fixture(profile: Profile) -> dict:
    return json.loads((FIXTURES / f"{profile.value.removesuffix('.v1')}.valid.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def validator():
    return SchemaValidator()


@pytest.mark.parametrize("profile", list(Profile))
def test_g002_positive_and_unknown_property_through_running_validator(profile, validator):
    value = fixture(profile)
    assert validator.validate(RawDeclaration(value)) == ()
    value["unrecognized_property"] = True
    errors = validator.validate(RawDeclaration(value))
    assert errors and all(e.code == "PROFILE_SCHEMA_VIOLATION" for e in errors)
    assert any("unrecognized_property" in e.message for e in errors)


@pytest.mark.parametrize("profile", list(Profile))
@pytest.mark.parametrize("field", ["schema_version", "profile", "kind", "authority_class"])
def test_required_envelope_fields(profile, field, validator):
    value = fixture(profile)
    del value[field]
    assert validator.validate(RawDeclaration(value))


@pytest.mark.parametrize("profile", list(Profile))
def test_leaf_complete_strict_schema_and_profile_specific_requirements(profile, validator):
    schema = validator.validators[profile].schema
    assert schema["additionalProperties"] is False
    assert set(schema["required"]) <= set(schema["properties"])
    for field in schema["required"]:
        value = fixture(profile)
        del value[field]
        assert validator.validate(RawDeclaration(value)), (profile, field)


@pytest.mark.parametrize("profile", [Profile.SEMANTIC_SOURCE, Profile.CAPTURE, Profile.IDENTITY_TRANSITION, Profile.DERIVED_VIEW_MANIFEST])
def test_selective_identity(profile, validator):
    value = fixture(profile)
    assert "semantic_id" not in value
    assert not validator.validate(RawDeclaration(value))


@pytest.mark.parametrize("authority", ["canonical", "candidate", "historical", "derived", "evidence"])
def test_capture_cannot_claim_other_authority(authority, validator):
    value = fixture(Profile.CAPTURE)
    value["authority_class"] = authority
    assert validator.validate(RawDeclaration(value))


def test_project_boundary_has_no_generic_facts(validator):
    value = fixture(Profile.PROJECT_BOUNDARY)
    value["facts"] = {"anything": "goes"}
    assert validator.validate(RawDeclaration(value))


@pytest.mark.parametrize("field", ["pause_reason", "return_condition", "resume_target"])
def test_resumable_paused_workstream_controls(field, validator):
    value = fixture(Profile.WORKSTREAM)
    del value[field]
    assert validator.validate(RawDeclaration(value))
    value["expected_to_resume"] = False
    assert not validator.validate(RawDeclaration(value))


def test_objective_alternative_and_nested_constraint_strictness(validator):
    value = fixture(Profile.WORKSTREAM)
    del value["objective"]
    assert validator.validate(RawDeclaration(value))
    value["objective_reference"] = "docs/objective.md"
    assert not validator.validate(RawDeclaration(value))
    procedure = fixture(Profile.GOVERNING_PROCEDURE)
    procedure["mandatory_constraints"][0]["surprise"] = True
    assert validator.validate(RawDeclaration(procedure))


@pytest.mark.parametrize("relation", [
    {"mode": "SPECIALIZE", "target": "ID:1"},
    {"mode": "SPECIALIZE", "target": "ID:1", "scope": {}},
    {"mode": "GUESS", "target": "ID:1"},
    {"mode": "REPLACE"},
])
def test_relation_shape_rejected(relation, validator):
    value = fixture(Profile.SEMANTIC_SOURCE)
    value["relations"] = [relation]
    assert validator.validate(RawDeclaration(value))


@pytest.mark.parametrize("scope", [{"time": "now"}, {"action": "run"}, {"target": []}, {"target": {"regex": ".*"}}])
def test_scope_is_exact_finite_facets(scope, validator):
    value = fixture(Profile.SEMANTIC_SOURCE)
    value["scope"] = scope
    assert validator.validate(RawDeclaration(value))


def test_transition_and_joint_required_controls(validator):
    value = fixture(Profile.IDENTITY_TRANSITION)
    value["transition_class"] = "SPLIT"
    assert validator.validate(RawDeclaration(value))
    value["successors"] = ["NEW:1", "NEW:2"]
    assert not validator.validate(RawDeclaration(value))
    joint = fixture(Profile.JOINT_AUTHORITY)
    joint["admission"]["ordinary_relations_insufficient"] = False
    assert validator.validate(RawDeclaration(joint))


def test_manifest_snapshot_boundary_and_structural_rebuildability(validator):
    value = fixture(Profile.DERIVED_VIEW_MANIFEST)
    value["snapshot_mode"] = "WORKTREE_SNAPSHOT"
    assert validator.validate(RawDeclaration(value))
    value["snapshot_status"] = "NON_COMMITTED"
    assert not validator.validate(RawDeclaration(value))
    value["rebuildability_class"] = "REGENERABLE_NONAUTHORITATIVE"
    assert validator.validate(RawDeclaration(value))


@pytest.mark.parametrize("field,value", [
    ("source_path", "../outside.md"), ("source_path", "/absolute.md"),
    ("source_path", "docs/../outside.md"), ("source_path", "docs\\file.md"),
    ("source_commit", "HEAD"), ("content_digest", "A" * 64),
    ("hash_basis", "WORKTREE_BYTES"), ("hash_algorithm", "sha1"),
    ("snapshot_mode", "WORKTREE_SNAPSHOT"), ("unknown", "value"),
    ("source_commit", "a" * 40 + "\n"), ("content_digest", "a" * 64 + "\n"),
])
def test_persistent_revision_schema_rejects_ambiguity(field, value, validator):
    source = fixture(Profile.WORKSTREAM)
    source["expected_revision"] = {
        "source_path": "docs/example.md", "source_commit": "a" * 40,
        "hash_algorithm": "sha256", "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT", "content_digest": "0" * 64,
    }
    source["expected_revision"][field] = value
    assert validator.validate(RawDeclaration(source))


def test_schema_version_identity_and_temporal_format(validator):
    for field, invalid in [("schema_version", "2"), ("semantic_id", "path with spaces.md"), ("semantic_id", "ID:1\n"), ("effective_from", "yesterday"), ("effective_from", "2026-02-30T12:00:00Z")]:
        value = copy.deepcopy(fixture(Profile.SEMANTIC_SOURCE))
        value[field] = invalid
        assert validator.validate(RawDeclaration(value))


def test_valid_optional_control_fields(validator):
    value = fixture(Profile.SEMANTIC_SOURCE)
    value.update({"semantic_id": "CONTROL:1", "scope": {"target": ["one", "two"]}, "relations": [{"mode": "SPECIALIZE", "target": "CONTROL:2", "scope": {"target": "one"}}], "effective_from": "2026-09-15T12:00:00Z"})
    assert not validator.validate(RawDeclaration(value))
