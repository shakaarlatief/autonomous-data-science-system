from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from ads_system.infrastructure.interchange.knowledge_bundle import (
    KnowledgeBundleValidationError,
    dumps_bundle,
    load_bundle,
    load_schema,
    resolve_node_ref,
    semantic_digest,
    validate_bundle,
    validate_import_safety,
)

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "schemas" / "reusable_knowledge_bundle_v1.schema.json"
FIXTURE_PATH = (
    ROOT / "tests" / "fixtures" / "knowledge" / "reusable_knowledge_stress_v1.json"
)


@pytest.fixture()
def bundle() -> dict:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def test_ki_01_schema_self_validates() -> None:
    schema = load_schema(SCHEMA_PATH)
    Draft202012Validator.check_schema(schema)


def test_ki_02_representative_heterogeneous_bundle_validates(bundle: dict) -> None:
    validate_bundle(bundle, schema_path=SCHEMA_PATH)
    assert len(bundle["assets"]) == 10
    assert {
        "histogram",
        "missing-data",
        "temporal-validation",
        "random-forest",
        "prediction-time-feature-eligibility",
        "class-imbalance",
    }.issubset({asset["stable_key"] for asset in bundle["assets"]})


def test_ki_03_unknown_typed_property_is_rejected(bundle: dict) -> None:
    invalid = copy.deepcopy(bundle)
    invalid["assets"][0]["surprise_field"] = "not allowed"

    with pytest.raises(KnowledgeBundleValidationError, match="surprise_field"):
        validate_bundle(invalid, schema_path=SCHEMA_PATH)


@pytest.mark.parametrize(
    ("mutator", "expected_fragment"),
    [
        (
            lambda candidate: candidate["assets"][0].__setitem__(
                "asset_id", "not-a-uuid"
            ),
            "uuid",
        ),
        (
            lambda candidate: candidate["assets"][0].__setitem__(
                "stable_key", "Not A Stable Key"
            ),
            "does not match",
        ),
    ],
)
def test_ki_04_malformed_identity_fields_are_rejected(
    bundle: dict,
    mutator,
    expected_fragment: str,
) -> None:
    invalid = copy.deepcopy(bundle)
    mutator(invalid)

    with pytest.raises(KnowledgeBundleValidationError) as error:
        validate_bundle(invalid, schema_path=SCHEMA_PATH)

    assert expected_fragment.lower() in str(error.value).lower()


@pytest.mark.parametrize(
    "bad_condition",
    [
        {"all": []},
        {"predicate": "project.task.is_supervised", "arguments": {}, "all": []},
        {"predicate": "invalidpredicate", "arguments": {}},
        {"not": {"any": []}},
    ],
)
def test_ki_05_malformed_recursive_rule_conditions_are_rejected(
    bundle: dict,
    bad_condition: dict,
) -> None:
    invalid = copy.deepcopy(bundle)
    random_forest = next(
        asset for asset in invalid["assets"] if asset["stable_key"] == "random-forest"
    )
    random_forest["rules"][0]["condition"] = bad_condition

    with pytest.raises(KnowledgeBundleValidationError):
        validate_bundle(invalid, schema_path=SCHEMA_PATH)


def test_ki_06_deterministic_dump_load_dump_is_byte_identical(
    bundle: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ADS_KNOWLEDGE_BUNDLE_SCHEMA", str(SCHEMA_PATH))

    first = dumps_bundle(bundle)
    second = dumps_bundle(json.loads(first))

    assert first == second
    assert first.endswith("\n")


def test_ki_07_semantic_digest_ignores_insignificant_json_formatting(
    bundle: dict,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ADS_KNOWLEDGE_BUNDLE_SCHEMA", str(SCHEMA_PATH))

    pretty = json.dumps(bundle, ensure_ascii=False, indent=4)
    compact = json.dumps(bundle, ensure_ascii=False, separators=(",", ":"))

    assert semantic_digest(json.loads(pretty)) == semantic_digest(json.loads(compact))


def test_ki_08_relation_references_resolve_uniquely(bundle: dict) -> None:
    validate_bundle(bundle, schema_path=SCHEMA_PATH)

    relation = next(
        relation
        for relation in bundle["relations"]
        if relation["relation_type"] == "USES_CONCEPT"
    )
    source_asset_id, source_component_id = resolve_node_ref(
        bundle, relation["source_ref"]
    )
    target_asset_id, target_component_id = resolve_node_ref(
        bundle, relation["target_ref"]
    )

    assert source_asset_id == "65f10694-eb0e-40ab-aa82-ac45317b5714"
    assert source_component_id is None
    assert target_asset_id == "38dbf459-97e1-41a0-b99f-bb2c7a7e62ca"
    assert target_component_id is None


@pytest.mark.parametrize("duplicate_kind", ["stable_key", "component_key", "rule_key"])
def test_ki_09_semantic_duplicate_keys_are_rejected(
    bundle: dict,
    duplicate_kind: str,
) -> None:
    invalid = copy.deepcopy(bundle)

    if duplicate_kind == "stable_key":
        invalid["assets"][1]["stable_key"] = invalid["assets"][0]["stable_key"]
    elif duplicate_kind == "component_key":
        asset = next(
            asset for asset in invalid["assets"] if asset["stable_key"] == "random-forest"
        )
        duplicate = copy.deepcopy(asset["components"][0])
        duplicate["component_id"] = "fa94f4e0-5b57-40cc-a15f-e350565b8799"
        duplicate["revision_id"] = "e9eb9fb2-a73d-472f-97b0-2ed6feb08252"
        asset["components"].append(duplicate)
    else:
        asset = next(
            asset for asset in invalid["assets"] if asset["stable_key"] == "random-forest"
        )
        duplicate = copy.deepcopy(asset["rules"][0])
        duplicate["rule_spec_id"] = "2477071d-bb9a-427c-9e38-d526c72d21fa"
        asset["rules"].append(duplicate)

    with pytest.raises(KnowledgeBundleValidationError, match="Duplicate"):
        validate_bundle(invalid, schema_path=SCHEMA_PATH)


def test_ki_10_bundle_kind_and_governance_import_safety(
    bundle: dict,
) -> None:
    validate_bundle(bundle, schema_path=SCHEMA_PATH)
    validate_import_safety(bundle)

    masquerading = copy.deepcopy(bundle)
    masquerading["assets"][0]["governance_status"] = "ACCEPTED"
    with pytest.raises(KnowledgeBundleValidationError, match="BENCHMARK_FIXTURE"):
        validate_import_safety(masquerading)

    trusted_snapshot = copy.deepcopy(bundle)
    trusted_snapshot["bundle_kind"] = "ACCEPTED_SNAPSHOT"
    for asset in trusted_snapshot["assets"]:
        asset["governance_status"] = "ACCEPTED"
        for component in asset["components"]:
            component["governance_status"] = "ACCEPTED"
    for relation in trusted_snapshot["relations"]:
        relation["governance_status"] = "ACCEPTED"

    with pytest.raises(KnowledgeBundleValidationError, match="trusted"):
        validate_import_safety(trusted_snapshot)

    validate_import_safety(
        trusted_snapshot,
        trusted_accepted_snapshot=True,
    )


def test_load_bundle_uses_same_validation_contract(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("ADS_KNOWLEDGE_BUNDLE_SCHEMA", str(SCHEMA_PATH))
    loaded = load_bundle(FIXTURE_PATH)
    assert loaded["format"] == "ads-reusable-knowledge-bundle"
