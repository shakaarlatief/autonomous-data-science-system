"""G012 public/private non-leakage and consequence-sensitive degraded-mode qualification."""

from dataclasses import fields
import hashlib
import json
from pathlib import Path

import pytest

from tests.unit.test_project_knowledge_authority import query, resolve, source
from tests.unit.test_project_knowledge_views import commit, declaration, repo, write
from tools.project_knowledge.authority import serialize_authority_result
from tools.project_knowledge.model import AuthorityStatus, PrivateStateEvidence
from tools.project_knowledge.services import generation
from tools.project_knowledge.adapters.gitio import worktree_snapshot
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.services.validation import validate_public_projection, validate_repository
from tools.project_knowledge.view_definitions import source_inventory_specification
from tools.project_knowledge.views import ViewValidationError


ROOT = Path(__file__).resolve().parents[2]
Q7_FOLDER = ROOT / "docs/research/project_knowledge_candidate_01_q7_real_v01"
Q7_FIXTURE = Q7_FOLDER / "Q7_REAL_FIXTURE_V01.json"
Q7_ORACLE = Q7_FOLDER / "Q7_REAL_ORACLE_V01.json"
Q7_FIXTURE_SHA256 = "a8e0872aa8c1ffab421d86924185c48642a075f872aa64847ebac7df34037bef"
Q7_ORACLE_SHA256 = "f85ec95c45b31c4ab9d643737f23bb55c9c269a0fc9915b0c009252aac7b82f4"


def test_g012_preserves_frozen_q7_fixture_and_oracle_evidence():
    assert hashlib.sha256(Q7_FIXTURE.read_bytes()).hexdigest() == Q7_FIXTURE_SHA256
    assert hashlib.sha256(Q7_ORACLE.read_bytes()).hexdigest() == Q7_ORACLE_SHA256


def test_g012_production_semantics_cover_frozen_q7_degraded_mode_scenarios():
    fixture = json.loads(Q7_FIXTURE.read_text(encoding="utf-8"))
    oracle = json.loads(Q7_ORACLE.read_text(encoding="utf-8"))["expectations"]["scenarios"]
    scenario_ids = {item["scenario_id"] for item in fixture["scenarios"]}
    assert scenario_ids == {"Q7-S01", "Q7-S02", "Q7-S03", "Q7-S04", "Q7-S05"}

    public = [source("PUBLIC")]
    s01 = resolve(
        public, query(consequence="public-only"),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", False, "UNKNOWN"),),
    )
    assert s01.status == AuthorityStatus.RESOLVED
    assert oracle["Q7-S01"]["public_resolved_private_preserved"] is True

    s02 = resolve(
        public, query(consequence="consequential", required_private_dependencies=("PRIVATE:CONTINUITY",)),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", False, "UNKNOWN"),),
    )
    assert s02.status == AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE
    assert oracle["Q7-S02"]["public_resolved_private_preserved"] is True

    s03 = resolve(
        public, query(consequence="consequential", required_private_dependencies=("PRIVATE:CONTINUITY",)),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", True, "STALE"),),
    )
    assert s03.status == AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE
    assert oracle["Q7-S03"]["public_resolved_private_preserved"] is True

    class UnavailableRetrieval:
        def __iter__(self):
            raise AssertionError("optional retrieval must not be consumed as authority")

    s05 = resolve(public, query(consequence="public-only"), retrieval_nominations=UnavailableRetrieval())
    assert s05.status == AuthorityStatus.RESOLVED
    assert oracle["Q7-S05"]["optional_retrieval_authority_bypass"] is False


@pytest.mark.parametrize("value", [
    r"C:\\Users\\alice\\private\\state.json",
    r"\\\\server\\private-share\\state.json",
    "/home/alice/private/state.json",
    "/Users/alice/private/state.json",
    "file:///home/alice/private/state.json",
    "../private/state.json",
    "C:private-state",
    "private dependency with spaces",
    "https://private.example/state",
])
def test_private_dependency_tokens_must_be_abstract_public_safe_identifiers(value):
    with pytest.raises(ValueError, match="public-safe abstract identifier"):
        query(required_private_dependencies=(value,))
    with pytest.raises(ValueError, match="public-safe abstract identifier"):
        PrivateStateEvidence(value, True, "FRESH")


def test_private_state_evidence_surface_cannot_carry_private_content_or_paths():
    assert tuple(field.name for field in fields(PrivateStateEvidence)) == ("dependency", "available", "freshness")
    assert PrivateStateEvidence("PRIVATE:CONTINUITY", True, "FRESH").dependency == "PRIVATE:CONTINUITY"
    with pytest.raises(ValueError, match="bool or None"):
        PrivateStateEvidence("PRIVATE:CONTINUITY", "yes", "FRESH")


@pytest.mark.parametrize("available,freshness", [
    (False, "FRESH"), (None, "UNKNOWN"), (True, "STALE"), (True, "UNKNOWN"),
])
def test_consequential_required_private_state_fails_visibly_when_not_fresh_and_available(available, freshness):
    result = resolve(
        [source("PUBLIC")],
        query(consequence="consequential", required_private_dependencies=("PRIVATE:CONTINUITY",)),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", available, freshness),),
    )
    assert result.status == AuthorityStatus.REQUIRED_PRIVATE_STATE_UNAVAILABLE
    assert {item.code for item in result.diagnostics} == {"REQUIRED_PRIVATE_STATE_UNAVAILABLE"}


def test_public_resolved_private_fact_survives_unavailable_optional_private_inspection():
    result = resolve(
        [source("PUBLIC")],
        query(consequence="public-only"),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", False, "UNKNOWN"),),
    )
    assert result.status == AuthorityStatus.RESOLVED
    rendered = serialize_authority_result(result)
    assert b"PRIVATE:CONTINUITY" not in rendered
    assert result.receipt.private_evidence == ()


def test_fresh_required_private_state_is_recorded_only_as_public_safe_verification_metadata():
    result = resolve(
        [source("PUBLIC")],
        query(consequence="consequential", required_private_dependencies=("PRIVATE:CONTINUITY",)),
        private_evidence=(PrivateStateEvidence("PRIVATE:CONTINUITY", True, "FRESH"),),
    )
    assert result.status == AuthorityStatus.RESOLVED
    rendered = serialize_authority_result(result)
    assert b"PRIVATE:CONTINUITY" in rendered
    assert b"FRESH" in rendered
    assert b"private_root" not in rendered and b"private_path" not in rendered and b"private_content" not in rendered


@pytest.mark.parametrize("leak", [
    r"C:\\Users\\alice\\private\\state.json",
    r"\\\\server\\private-share\\state.json",
    "/home/alice/private/state.json",
    "/Users/alice/private/state.json",
    "file:///home/alice/private/state.json",
])
def test_rendered_byte_defense_in_depth_rejects_private_filesystem_locators(leak):
    rendered = (json.dumps({"value": leak}, ensure_ascii=False) + "\n").encode("utf-8")
    findings = validate_public_projection(rendered, "docs/project_knowledge/generated/test.json")
    assert {item.code for item in findings} == {"PUBLIC_PRIVATE_PATH_LEAK"}
    assert all(leak not in item.message for item in findings)


def test_known_private_fixture_value_is_rejected_even_when_json_escaped_without_echoing_secret():
    secret = 'opaque-private-value-7f3a"with\\escaping'
    rendered = (json.dumps({"value": secret}, ensure_ascii=False) + "\n").encode("utf-8")
    findings = validate_public_projection(
        rendered, "docs/project_knowledge/generated/test.json", known_private_values=(secret,),
    )
    assert {item.code for item in findings} == {"PUBLIC_PRIVATE_VALUE_LEAK"}
    assert all(secret not in item.message for item in findings)


def test_known_private_unicode_fixture_value_is_rejected_when_ascii_escaped():
    secret = "privé-秘密-value"
    rendered = (json.dumps({"value": secret}, ensure_ascii=True) + "\n").encode("ascii")
    findings = validate_public_projection(
        rendered, "docs/project_knowledge/generated/test.json", known_private_values=(secret,),
    )
    assert {item.code for item in findings} == {"PUBLIC_PRIVATE_VALUE_LEAK"}
    assert all(secret not in item.message for item in findings)


def test_public_safe_relative_paths_tokens_and_urls_are_not_overclassified_as_private():
    rendered = (json.dumps({
        "path": "docs/private_companion/README.md",
        "dependency": "PRIVATE:CONTINUITY",
        "schema": "https://schemas.ads.local/project-knowledge/test",
    }, ensure_ascii=False) + "\n").encode("utf-8")
    assert validate_public_projection(rendered, "docs/project_knowledge/generated/test.json") == ()


def test_repository_validation_rejects_private_path_in_governed_public_declaration(repo):
    leaked_path = r"C:\\Users\\alice\\private\\state.json"
    value = {
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "note",
        "authority_class": "canonical", "semantic_id": "A", "provenance": [leaked_path],
    }
    write(repo, "docs/a.json", json.dumps(value).encode("utf-8"))
    result = validate_repository(worktree_snapshot(repo))
    assert not result.ok
    assert {item.code for item in result.diagnostics} == {"PUBLIC_PRIVATE_PATH_LEAK"}
    assert all(leaked_path not in item.message for item in result.diagnostics)


def test_repository_validation_rejects_known_private_value_in_governed_public_declaration(repo):
    secret = "OPAQUE_SYNTHETIC_PRIVATE_VALUE_7F3A"
    value = {
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "note",
        "authority_class": "canonical", "semantic_id": "A", "provenance": [secret],
    }
    write(repo, "docs/a.json", json.dumps(value).encode("utf-8"))
    result = validate_repository(worktree_snapshot(repo), known_private_values=(secret,))
    assert not result.ok
    assert {item.code for item in result.diagnostics} == {"PUBLIC_PRIVATE_VALUE_LEAK"}
    assert all(secret not in item.message for item in result.diagnostics)


def test_repository_validation_accepts_public_safe_abstract_private_reference(repo):
    value = {
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "note",
        "authority_class": "canonical", "semantic_id": "A",
        "provenance": ["PRIVATE:CONTINUITY", "docs/private_companion/README.md"],
    }
    write(repo, "docs/a.json", json.dumps(value).encode("utf-8"))
    result = validate_repository(worktree_snapshot(repo))
    assert result.ok, result.diagnostics


def test_public_projection_probe_contract_rejects_empty_or_untyped_private_fixture_values():
    with pytest.raises(ValueError, match="nonempty"):
        validate_public_projection(b"{}\n", known_private_values=("",))
    with pytest.raises(ValueError, match="str or bytes"):
        validate_public_projection(b"{}\n", known_private_values=(object(),))


def test_generation_ignores_non_authoritative_capture_payload_even_when_probe_knows_it(repo):
    secret = "SYNTHETIC_PRIVATE_CAPTURE_VALUE_7F3A"
    capture = {
        "schema_version": "1", "profile": "capture.v1", "kind": "observation",
        "authority_class": "capture", "summary": secret,
    }
    write(repo, "docs/project_knowledge/captures/open/private-observation.json", json.dumps(capture).encode("utf-8"))
    snapshot = commit(repo)
    result, = generate_views(snapshot, (source_inventory_specification(),), known_private_values=(secret,))
    assert secret.encode() not in result.view_bytes
    assert secret.encode() not in result.manifest_bytes


def test_generation_rejects_known_private_value_if_it_reaches_public_rendered_bytes(repo):
    secret = "SYNTHETIC:PRIVATE:VALUE:7F3A"
    write(repo, "docs/a.json", declaration(secret))
    snapshot = commit(repo)
    with pytest.raises(ViewValidationError) as error:
        generate_views(snapshot, (source_inventory_specification(),), known_private_values=(secret,))
    assert {item.code for item in error.value.diagnostics} == {"PUBLIC_PRIVATE_VALUE_LEAK"}
    assert secret not in str(error.value)


def test_known_private_probes_are_host_side_validation_only(monkeypatch):
    observed = {}

    def fake_execute(snapshot, specifications, selected, operation, **extra):
        observed.update(extra)
        return {"builds": []}

    monkeypatch.setattr(generation, "_execute_bound", fake_execute)
    assert generate_views(object(), (), known_private_values=("SYNTHETIC_PRIVATE_VALUE",)) == ()
    assert observed == {}


def test_public_profile_schemas_do_not_offer_raw_private_storage_fields():
    forbidden = {
        "private_root", "private_path", "private_state_path", "private_source_store_root",
        "private_content", "private_payload", "private_exact_values", "secret", "secrets",
    }
    for path in sorted((ROOT / "schemas/project_knowledge").glob("*.schema.json")):
        schema = json.loads(path.read_text(encoding="utf-8"))
        pending = [schema]
        property_names = set()
        while pending:
            value = pending.pop()
            if isinstance(value, dict):
                property_names.update(value.get("properties", ()))
                pending.extend(value.values())
            elif isinstance(value, list):
                pending.extend(value)
        assert not (forbidden & property_names), (path.name, forbidden & property_names)
