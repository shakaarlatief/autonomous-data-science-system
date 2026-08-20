"""Deterministic V1 reusable-knowledge interchange utilities.

This module implements Specification 004's storage-neutral interchange boundary.
It deliberately does not perform database writes. Structural validation, semantic
integrity checks, deterministic normalization, relation/reference resolution,
and import-governance safety happen before persistence adapters are invoked.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator, FormatChecker


class KnowledgeBundleValidationError(ValueError):
    """Raised when a reusable-knowledge bundle violates the interchange contract."""


def default_schema_path() -> Path:
    """Return the repository schema path used by the source-layout V1 application.

    Callers may always supply an explicit schema path. The environment override
    supports packaging/integration contexts without making repository layout part
    of the domain contract.
    """

    configured = os.environ.get("ADS_KNOWLEDGE_BUNDLE_SCHEMA")
    if configured:
        return Path(configured)

    source_file = Path(__file__).resolve()
    for parent in source_file.parents:
        candidate = parent / "schemas" / "reusable_knowledge_bundle_v1.schema.json"
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(
        "Reusable-knowledge JSON Schema was not found. "
        "Set ADS_KNOWLEDGE_BUNDLE_SCHEMA or pass schema_path explicitly."
    )


def load_schema(schema_path: str | Path | None = None) -> dict[str, Any]:
    """Load and self-check the Draft 2020-12 interchange schema."""

    path = Path(schema_path) if schema_path is not None else default_schema_path()
    schema = json.loads(path.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    return schema


def load_bundle(
    path: str | Path,
    *,
    schema_path: str | Path | None = None,
) -> dict[str, Any]:
    """Load a JSON bundle and validate both structural and semantic integrity."""

    bundle = json.loads(Path(path).read_text(encoding="utf-8"))
    validate_bundle(bundle, schema_path=schema_path)
    return bundle


def validate_bundle(
    bundle: Mapping[str, Any],
    *,
    schema_path: str | Path | None = None,
    schema: Mapping[str, Any] | None = None,
) -> None:
    """Validate the bundle against JSON Schema and application-level invariants."""

    schema_document = dict(schema) if schema is not None else load_schema(schema_path)
    validator = Draft202012Validator(
        schema_document,
        format_checker=FormatChecker(),
    )
    errors = sorted(
        validator.iter_errors(bundle),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        first = errors[0]
        location = "/".join(str(part) for part in first.absolute_path) or "<root>"
        raise KnowledgeBundleValidationError(
            f"JSON Schema validation failed at {location}: {first.message}"
        )

    _validate_semantic_integrity(bundle)


def validate_import_safety(
    bundle: Mapping[str, Any],
    *,
    trusted_accepted_snapshot: bool = False,
) -> None:
    """Enforce governance safety for a prospective authoritative import.

    Structural/semantic bundle validation is intentionally separate from import
    authorization. An ACCEPTED_SNAPSHOT can be parsed and inspected normally,
    but using it to restore/bootstrap accepted authority requires an explicit
    trusted path.
    """

    kind = bundle["bundle_kind"]
    statuses = list(_iter_governance_statuses(bundle))

    if kind == "BENCHMARK_FIXTURE":
        if any(status != "CANDIDATE" for status in statuses):
            raise KnowledgeBundleValidationError(
                "BENCHMARK_FIXTURE content must remain CANDIDATE and cannot "
                "masquerade as accepted operational knowledge."
            )
        return

    if kind == "CANDIDATE_SET":
        forbidden = {"ACCEPTED", "SUPERSEDED"}
        if any(status in forbidden for status in statuses):
            raise KnowledgeBundleValidationError(
                "CANDIDATE_SET import cannot contain ACCEPTED or SUPERSEDED "
                "knowledge revisions."
            )
        return

    if kind == "ACCEPTED_SNAPSHOT":
        if not trusted_accepted_snapshot:
            raise KnowledgeBundleValidationError(
                "ACCEPTED_SNAPSHOT import requires an explicit trusted "
                "restore/bootstrap path."
            )
        if any(status != "ACCEPTED" for status in statuses):
            raise KnowledgeBundleValidationError(
                "CURRENT accepted snapshot content must contain only ACCEPTED "
                "asset/component/relation revisions."
            )
        return

    raise KnowledgeBundleValidationError(f"Unsupported bundle kind: {kind}")


def resolve_node_ref(
    bundle: Mapping[str, Any],
    node_ref: Mapping[str, str],
) -> tuple[str, str | None]:
    """Resolve a human-readable asset/component reference to durable IDs."""

    asset_key = node_ref["asset_key"]
    matching_assets = [
        asset for asset in bundle["assets"] if asset["stable_key"] == asset_key
    ]
    if len(matching_assets) != 1:
        raise KnowledgeBundleValidationError(
            f"Node reference asset_key={asset_key!r} resolved to "
            f"{len(matching_assets)} assets."
        )

    asset = matching_assets[0]
    component_key = node_ref.get("component_key")
    if component_key is None:
        return asset["asset_id"], None

    matching_components = [
        component
        for component in asset["components"]
        if component["component_key"] == component_key
    ]
    if len(matching_components) != 1:
        raise KnowledgeBundleValidationError(
            f"Node reference {asset_key!r}/{component_key!r} resolved to "
            f"{len(matching_components)} components."
        )
    return asset["asset_id"], matching_components[0]["component_id"]


def normalize_bundle(bundle: Mapping[str, Any]) -> dict[str, Any]:
    """Return the deterministic logical ordering used for export and hashing."""

    normalized: dict[str, Any] = copy.deepcopy(dict(bundle))

    normalized["assets"] = sorted(
        normalized["assets"], key=lambda asset: asset["stable_key"]
    )
    for asset in normalized["assets"]:
        _sort_string_list_fields(
            asset,
            "limitations",
            "reasoning_functions",
            "semantic_checks",
            "provenance_source_ids",
        )
        profile = asset["retrieval_profile"]
        _sort_string_list_fields(
            profile,
            "aliases",
            "lexical_terms",
            "semantic_cues",
            "negative_cues",
        )
        asset["context_requirements"] = sorted(
            asset["context_requirements"], key=lambda item: item["key"]
        )
        for requirement in asset["context_requirements"]:
            _sort_string_list_fields(requirement, "required_for")

        asset["narrative_facets"] = sorted(
            asset["narrative_facets"],
            key=lambda facet: (facet["position"], facet["facet_kind"], facet["body"]),
        )
        asset["components"] = sorted(
            asset["components"], key=lambda component: component["component_key"]
        )
        for component in asset["components"]:
            _sort_string_list_fields(
                component,
                "reasoning_functions",
                "provenance_source_ids",
            )
        asset["rules"] = sorted(asset["rules"], key=lambda rule: rule["rule_key"])
        for rule in asset["rules"]:
            _sort_string_list_fields(rule, "provenance_source_ids")

    normalized["relations"] = sorted(
        normalized["relations"],
        key=lambda relation: (
            _node_ref_sort_key(relation["source_ref"]),
            relation["relation_type"],
            _node_ref_sort_key(relation["target_ref"]),
            relation["relation_id"],
        ),
    )
    for relation in normalized["relations"]:
        _sort_string_list_fields(relation, "provenance_source_ids")

    normalized["provenance_sources"] = sorted(
        normalized["provenance_sources"], key=lambda source: source["source_id"]
    )
    normalized["collections"] = sorted(
        normalized["collections"], key=lambda collection: collection["collection_key"]
    )
    for collection in normalized["collections"]:
        collection["members"] = sorted(
            collection["members"],
            key=lambda member: _node_ref_sort_key(member["ref"]),
        )

    return normalized


def dumps_bundle(bundle: Mapping[str, Any]) -> str:
    """Serialize a validated logical bundle deterministically for review/diff."""

    validate_bundle(bundle)
    normalized = normalize_bundle(bundle)
    return json.dumps(
        normalized,
        ensure_ascii=False,
        indent=2,
        sort_keys=True,
    ) + "\n"


def dump_bundle(bundle: Mapping[str, Any], path: str | Path) -> None:
    """Write a deterministic validated bundle using UTF-8 and LF newlines."""

    Path(path).write_text(dumps_bundle(bundle), encoding="utf-8", newline="\n")


def semantic_digest(bundle: Mapping[str, Any]) -> str:
    """Return a formatting-independent SHA-256 digest of the logical bundle."""

    validate_bundle(bundle)
    normalized = normalize_bundle(bundle)
    canonical = json.dumps(
        normalized,
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _validate_semantic_integrity(bundle: Mapping[str, Any]) -> None:
    asset_keys: set[str] = set()
    node_ids: set[str] = set()
    revision_ids: set[str] = set()
    rule_ids: set[str] = set()

    source_ids = _require_unique(
        (source["source_id"] for source in bundle["provenance_sources"]),
        "provenance source_id",
    )
    _require_unique(
        (collection["collection_key"] for collection in bundle["collections"]),
        "collection_key",
    )

    for asset in bundle["assets"]:
        _add_unique(asset_keys, asset["stable_key"], "asset stable_key")
        _add_unique(node_ids, asset["asset_id"], "knowledge node_id")
        _add_unique(revision_ids, asset["revision_id"], "knowledge revision_id")
        _validate_source_refs(
            asset["provenance_source_ids"], source_ids, asset["stable_key"]
        )

        component_keys: set[str] = set()
        for component in asset["components"]:
            _add_unique(
                component_keys,
                component["component_key"],
                f"component_key within asset {asset['stable_key']}",
            )
            _add_unique(node_ids, component["component_id"], "knowledge node_id")
            _add_unique(
                revision_ids,
                component["revision_id"],
                "knowledge revision_id",
            )
            _validate_source_refs(
                component["provenance_source_ids"],
                source_ids,
                f"{asset['stable_key']}/{component['component_key']}",
            )

        rule_keys: set[str] = set()
        for rule in asset["rules"]:
            _add_unique(
                rule_keys,
                rule["rule_key"],
                f"rule_key within asset {asset['stable_key']}",
            )
            _add_unique(rule_ids, rule["rule_spec_id"], "rule_spec_id")
            _validate_source_refs(
                rule["provenance_source_ids"],
                source_ids,
                f"{asset['stable_key']} rule {rule['rule_key']}",
            )

    relation_ids: set[str] = set()
    relation_revision_ids: set[str] = set()
    for relation in bundle["relations"]:
        _add_unique(relation_ids, relation["relation_id"], "relation_id")
        _add_unique(
            relation_revision_ids,
            relation["relation_revision_id"],
            "relation_revision_id",
        )
        resolve_node_ref(bundle, relation["source_ref"])
        resolve_node_ref(bundle, relation["target_ref"])
        _validate_source_refs(
            relation["provenance_source_ids"],
            source_ids,
            f"relation {relation['relation_id']}",
        )

    for collection in bundle["collections"]:
        seen_members: set[tuple[str, str | None]] = set()
        for member in collection["members"]:
            resolved = resolve_node_ref(bundle, member["ref"])
            if resolved in seen_members:
                raise KnowledgeBundleValidationError(
                    f"Duplicate member in collection {collection['collection_key']!r}: "
                    f"{member['ref']!r}"
                )
            seen_members.add(resolved)


def _iter_governance_statuses(bundle: Mapping[str, Any]):
    for asset in bundle["assets"]:
        yield asset["governance_status"]
        for component in asset["components"]:
            yield component["governance_status"]
    for relation in bundle["relations"]:
        yield relation["governance_status"]


def _validate_source_refs(
    references: list[str],
    source_ids: set[str],
    owner: str,
) -> None:
    unknown = sorted(set(references) - source_ids)
    if unknown:
        raise KnowledgeBundleValidationError(
            f"{owner} references unknown provenance source IDs: {unknown}"
        )


def _require_unique(values, label: str) -> set[str]:
    observed: set[str] = set()
    for value in values:
        _add_unique(observed, value, label)
    return observed


def _add_unique(observed: set[str], value: str, label: str) -> None:
    if value in observed:
        raise KnowledgeBundleValidationError(f"Duplicate {label}: {value}")
    observed.add(value)


def _sort_string_list_fields(mapping: dict[str, Any], *field_names: str) -> None:
    for field_name in field_names:
        mapping[field_name] = sorted(set(mapping[field_name]))


def _node_ref_sort_key(node_ref: Mapping[str, str]) -> tuple[str, str]:
    return (node_ref["asset_key"], node_ref.get("component_key", ""))
