"""Qualification of the complete Specification 028 persistent W0 view set."""

from dataclasses import replace
import json

from jsonschema import Draft202012Validator

from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.identity import (
    build_identity_index, identity_index_data, transition_from_source,
)
from tools.project_knowledge.model import AuthorityClass, Profile, SnapshotMode
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge.views import (
    deterministic_json, identity_index_specification, production_view_specifications,
)
from tools.project_knowledge.workstreams import build_workstream_graph, workstream_result_data
from tests.unit.test_project_knowledge_current_state_core import (
    ACTIVE, FIXTURES, core_repo,
)
from tests.unit.test_project_knowledge_views import commit, write


PERSISTENT_PATHS = {
    "docs/project_knowledge/generated/source_catalog.json",
    "docs/project_knowledge/generated/identity_index.json",
    "docs/project_knowledge/generated/authority_index.json",
    "docs/project_knowledge/generated/workstream_graph.json",
    "docs/project_knowledge/generated/subject_index.json",
    "docs/project_knowledge/generated/risk_obligation_index.json",
    "docs/project_knowledge/generated/current_state_core.json",
    "docs/project_knowledge/generated/CURRENT_STATE_CORE.md",
}


TEXT = {"type": "string"}
NULLABLE_TEXT = {"type": ["string", "null"]}
SEMANTIC = {"type": "string", "pattern": r"^[A-Za-z][A-Za-z0-9_.:-]*$"}
NULLABLE_SEMANTIC = {"anyOf": [SEMANTIC, {"type": "null"}]}
PATH = {"type": "string", "minLength": 1}
DIGEST = {"type": "string", "pattern": r"^[0-9a-f]{64}$"}
STRING_ARRAY = {"type": "array", "items": TEXT, "uniqueItems": True}
SEMANTIC_ARRAY = {"type": "array", "items": SEMANTIC, "uniqueItems": True}
PATH_ARRAY = {"type": "array", "items": PATH, "uniqueItems": True}


def object_schema(properties, required=None):
    return {
        "type": "object",
        "properties": properties,
        "required": list(properties if required is None else required),
        "additionalProperties": False,
    }


SCOPE = {
    "type": "object",
    "additionalProperties": {
        "oneOf": [TEXT, {"type": "array", "items": TEXT, "uniqueItems": True}],
    },
}

SOURCE_CATALOG_ROW = object_schema({
    "source_path": PATH,
    "semantic_id": NULLABLE_SEMANTIC,
    "profile": TEXT,
    "kind": TEXT,
    "state": NULLABLE_TEXT,
    "scope": SCOPE,
    "content_digest": DIGEST,
})

IDENTITY_ROW = object_schema({
    "semantic_id": SEMANTIC,
    "disposition": {
        "enum": [
            "CURRENT", "HISTORICAL", "MERGED", "SPLIT", "SUPERSEDED",
            "RETIRED", "REDIRECTED", "TEMPORAL_CONTEXT_REQUIRED",
        ],
    },
    "static_terminal_ids": SEMANTIC_ARRAY,
    "static_retired_ids": SEMANTIC_ARRAY,
    "static_current_carriers": PATH_ARRAY,
    "transition_paths": PATH_ARRAY,
    "history_carriers": PATH_ARRAY,
    "continuity_preserved": {"type": "boolean"},
    "temporal_resolution_required": {"type": "boolean"},
})

IDENTITY_SOURCE = object_schema({
    "source_path": PATH,
    "semantic_id": SEMANTIC,
    "authority_class": {"enum": ["canonical", "historical"]},
    "profile": TEXT,
    "state": NULLABLE_TEXT,
    "content_digest": DIGEST,
    "temporal": {"type": "boolean"},
    "effective_from": NULLABLE_TEXT,
    "effective_to": NULLABLE_TEXT,
    "authority_from": NULLABLE_TEXT,
    "authority_to": NULLABLE_TEXT,
})

IDENTITY_TRANSITION = object_schema({
    "source_path": PATH,
    "semantic_id": NULLABLE_SEMANTIC,
    "authority_class": {"enum": ["canonical", "historical"]},
    "state": NULLABLE_TEXT,
    "content_digest": DIGEST,
    "transition_class": {
        "enum": [
            "MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT", "MERGE", "SPLIT",
            "SUPERSEDE", "RETIRE", "REDIRECT",
        ],
    },
    "predecessors": SEMANTIC_ARRAY,
    "successors": SEMANTIC_ARRAY,
    "resolution_behavior": TEXT,
    "provenance": STRING_ARRAY,
    "temporal": {"type": "boolean"},
    "effective_from": NULLABLE_TEXT,
    "effective_to": NULLABLE_TEXT,
    "authority_from": NULLABLE_TEXT,
    "authority_to": NULLABLE_TEXT,
})

RELATION = object_schema({
    "mode": {"enum": ["REPLACE", "SUPPLEMENT", "SPECIALIZE", "CORRECT"]},
    "target": SEMANTIC,
    "scope": SCOPE,
})

AUTHORITY_CANDIDATE = object_schema({
    "source_path": PATH,
    "semantic_id": NULLABLE_SEMANTIC,
    "profile": TEXT,
    "kind": TEXT,
    "state": NULLABLE_TEXT,
    "scope": SCOPE,
    "relations": {"type": "array", "items": RELATION},
    "governed_action_classes": STRING_ARRAY,
    "members": SEMANTIC_ARRAY,
    "combination_semantics": NULLABLE_TEXT,
    "effective_from": NULLABLE_TEXT,
    "effective_to": NULLABLE_TEXT,
    "authority_from": NULLABLE_TEXT,
    "authority_to": NULLABLE_TEXT,
    "content_digest": DIGEST,
    "declaration": {"type": "object"},
})

WORKSTREAM_NODE = object_schema({
    "semantic_id": SEMANTIC,
    "source_path": PATH,
    "state": TEXT,
    "readiness": TEXT,
    "objective": NULLABLE_TEXT,
    "parent": NULLABLE_SEMANTIC,
    "parent_chain": SEMANTIC_ARRAY,
    "depends_on": SEMANTIC_ARRAY,
    "dependency_closure": SEMANTIC_ARRAY,
    "dependency_blockers": SEMANTIC_ARRAY,
    "expected_to_resume": {"type": "boolean"},
    "pause_reason": NULLABLE_TEXT,
    "return_condition": NULLABLE_TEXT,
    "resume_target": NULLABLE_SEMANTIC,
    "current_anchor": NULLABLE_TEXT,
    "risk_or_reopen_triggers": STRING_ARRAY,
    "temporal": {"type": "boolean"},
})

SUBJECT_ROW = object_schema({
    "axis": TEXT,
    "value": TEXT,
    "semantic_id": NULLABLE_SEMANTIC,
    "source_path": PATH,
})

RISK_ROW = object_schema({
    "source_path": PATH,
    "semantic_id": NULLABLE_SEMANTIC,
    "trigger": TEXT,
})

OBLIGATION_ROW = object_schema({
    "source_path": PATH,
    "semantic_id": NULLABLE_SEMANTIC,
    "category": {
        "enum": [
            "PRECONDITION", "PROHIBITION", "POSTCONDITION", "FAIL_CLOSED",
            "MANDATORY_CONSTRAINT", "RETURN_CONDITION",
        ],
    },
    "ordinal": {"type": "integer", "minimum": 0},
    "constraint_id": NULLABLE_TEXT,
    "requirement": TEXT,
})


VIEW_SCHEMAS = {
    "source_catalog": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "sources": {"type": "array", "items": SOURCE_CATALOG_ROW},
    }),
    "identity_index": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "resolution_basis": {"const": "STATIC_PLUS_EXPLICIT_TEMPORAL_DEFER"},
        "identities": {"type": "array", "items": IDENTITY_ROW},
        "sources": {"type": "array", "items": IDENTITY_SOURCE},
        "transitions": {"type": "array", "items": IDENTITY_TRANSITION},
    }),
    "authority_index": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "resolution_note": {
            "const": "Candidate/index inputs only; task-scoped authority remains resolver-owned",
        },
        "candidates": {"type": "array", "items": AUTHORITY_CANDIDATE},
    }),
    "workstream_graph": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "nodes": {"type": "array", "items": WORKSTREAM_NODE},
        "active_ready_set": SEMANTIC_ARRAY,
        "route": object_schema({
            "disposition": {
                "enum": [
                    "UNIQUE_PRIMARY_ROUTE", "NO_UNIQUE_PRIMARY_ROUTE",
                    "NO_READY_WORKSTREAM", "TEMPORAL_CONTEXT_REQUIRED",
                ],
            },
            "primary": NULLABLE_SEMANTIC,
            "branches": SEMANTIC_ARRAY,
        }),
        "temporal_context_required": {"type": "boolean"},
    }),
    "subject_index": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "memberships": {"type": "array", "items": SUBJECT_ROW},
    }),
    "risk_obligation_index": object_schema({
        "schema_version": {"const": "1"},
        "authority_class": {"const": "derived"},
        "risks": {"type": "array", "items": RISK_ROW},
        "obligations": {"type": "array", "items": OBLIGATION_ROW},
    }),
}


def builds(root):
    return generate_views(commit_snapshot(root, "HEAD"), production_view_specifications())


def by_id(results):
    return {result.view_id: result for result in results}


def test_eight_persistent_paths_exact_schemas_and_deterministic_bytes(core_repo):
    first = builds(core_repo)
    second = builds(core_repo)
    assert first == second
    assert len(first) == 8
    assert {result.view_path for result in first} == PERSISTENT_PATHS
    assert {result.manifest_path for result in first} == {
        "docs/project_knowledge/generated/manifests/" + result.view_id + ".json"
        for result in first
    }

    rows = by_id(first)
    assert set(rows) == {
        "source_catalog", "identity_index", "authority_index", "workstream_graph",
        "subject_index", "risk_obligation_index", "current_state_core",
        "current_state_core_markdown",
    }
    for view_id, schema in VIEW_SCHEMAS.items():
        Draft202012Validator.check_schema(schema)
        Draft202012Validator(schema).validate(json.loads(rows[view_id].view_bytes))

    assert rows["current_state_core"].view_bytes == (FIXTURES / "expected_core.json").read_bytes()
    markdown = rows["current_state_core_markdown"].view_bytes
    assert markdown.decode("utf-8").startswith("# Current State Core\n\n")
    assert b"\r" not in markdown and markdown.endswith(b"\n")
    assert b"WS-PKA-CURRENT" in markdown
    assert b"PROJECT-INTEGRATION-BOUNDARY" in markdown

    for result in first:
        assert result.manifest.fields["view_id"] == result.view_id
        assert result.manifest.fields["view_path"] == result.view_path
        assert result.manifest.fields["authority_class"] == "derived"
        assert result.manifest.fields["rebuildability_class"] == "DETERMINISTIC_BYTE_REBUILD"


def test_source_catalog_subject_and_risk_views_are_source_owned_projections(core_repo):
    rows = {view_id: json.loads(result.view_bytes)
            for view_id, result in by_id(builds(core_repo)).items()
            if view_id in {"source_catalog", "subject_index", "risk_obligation_index"}}

    catalog_paths = {source["source_path"] for source in rows["source_catalog"]["sources"]}
    assert ACTIVE in catalog_paths
    assert "docs/procedure.json" in catalog_paths

    memberships = rows["subject_index"]["memberships"]
    assert {
        (row["axis"], row["value"], row["source_path"]) for row in memberships
    } >= {
        ("profile", "workstream.v1", ACTIVE),
        ("kind", "PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM", ACTIVE),
    }

    authority = json.loads(by_id(builds(core_repo))["authority_index"].view_bytes)
    procedure = next(
        row for row in authority["candidates"]
        if row["semantic_id"] == "PROCEDURE:PERMANENT-SOURCE-VAULT-BOOTSTRAP"
    )
    assert procedure["declaration"]["mandatory_constraints"][0]["constraint_id"] == "RECOVERY"

    obligations = rows["risk_obligation_index"]["obligations"]
    assert {
        (row["category"], row["requirement"]) for row in obligations
    } >= {
        ("MANDATORY_CONSTRAINT", "Require accepted recovery proof before Course 2"),
        ("RETURN_CONDITION", "Resume when project routing explicitly returns to the Source Vault bootstrap workstream"),
    }


def test_identity_view_alone_binds_accepted_historical_sources(core_repo):
    historical_path = "docs/history/research-124-old.json"
    write(core_repo, historical_path, deterministic_json({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "RESEARCH_STAGE_HISTORY",
        "authority_class": "historical",
        "semantic_id": "RESEARCH:124",
        "state": "SUPERSEDED",
    }))
    commit(core_repo)

    results = by_id(builds(core_repo))
    identity = json.loads(results["identity_index"].view_bytes)
    row = next(item for item in identity["identities"] if item["semantic_id"] == "RESEARCH:124")
    assert historical_path in row["history_carriers"]
    assert historical_path not in row["static_current_carriers"]

    identity_inputs = {
        binding["source_path"] for binding in results["identity_index"].manifest.fields["input_bindings"]
    }
    assert historical_path in identity_inputs
    for view_id, result in results.items():
        if view_id != "identity_index":
            assert historical_path not in {
                binding["source_path"] for binding in result.manifest.fields["input_bindings"]
            }


def test_identity_projection_matches_g006_static_targets_for_supersession(core_repo):
    write(core_repo, "docs/history/old.json", deterministic_json({
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "OLD_IDENTITY",
        "authority_class": "historical", "semantic_id": "IDENTITY:OLD", "state": "SUPERSEDED",
    }))
    write(core_repo, "docs/new.json", deterministic_json({
        "schema_version": "1", "profile": "semantic_source.v1", "kind": "NEW_IDENTITY",
        "authority_class": "canonical", "semantic_id": "IDENTITY:NEW",
    }))
    write(core_repo, "docs/transition.json", deterministic_json({
        "schema_version": "1", "profile": "identity_transition.v1", "kind": "SUPERSESSION",
        "authority_class": "canonical", "semantic_id": "TRANSITION:ONE",
        "transition_class": "SUPERSEDE",
        "predecessors": ["IDENTITY:OLD"], "successors": ["IDENTITY:NEW"],
        "resolution_behavior": "Old identity is superseded by the reviewed successor",
        "provenance": ["docs/review.md"],
    }))
    commit(core_repo)

    snapshot = commit_snapshot(core_repo, "HEAD")
    validation = validate_repository(snapshot)
    assert validation.ok
    transitions = tuple(
        transition_from_source(source)
        for source in validation.sources
        if source.profile == Profile.IDENTITY_TRANSITION
    )
    domain = build_identity_index(
        tuple(source for source in validation.sources if source.profile != Profile.IDENTITY_TRANSITION),
        transitions,
        snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT,
    )
    domain_data = identity_index_data(domain)
    domain_old = next(row for row in domain_data["identities"] if row["semantic_id"] == "IDENTITY:OLD")

    derived, = generate_views(snapshot, (identity_index_specification(),))
    row = next(
        item for item in json.loads(derived.view_bytes)["identities"]
        if item["semantic_id"] == "IDENTITY:OLD"
    )
    assert row["static_terminal_ids"] == domain_old["current_targets"]
    assert row["static_retired_ids"] == domain_old["retired_targets"]
    assert row["transition_paths"] == domain_old["transition_paths"]
    assert row["continuity_preserved"] == domain_old["continuity_preserved"]
    assert row["disposition"] == domain_old["disposition"]
    transition_owner = next(
        item for item in json.loads(derived.view_bytes)["identities"]
        if item["semantic_id"] == "TRANSITION:ONE"
    )
    domain_transition = next(
        item for item in domain_data["identities"]
        if item["semantic_id"] == "TRANSITION:ONE"
    )
    assert transition_owner["disposition"] == domain_transition["disposition"]
    assert transition_owner["static_terminal_ids"] == domain_transition["current_targets"]


def test_workstream_projection_matches_g008_non_temporal_readiness_and_route(core_repo):
    snapshot = commit_snapshot(core_repo, "HEAD")
    validation = validate_repository(snapshot)
    assert validation.ok

    workstreams = tuple(
        source for source in validation.sources
        if source.profile == Profile.WORKSTREAM and source.authority_class == AuthorityClass.CANONICAL
    )
    referenced = {
        value
        for source in workstreams
        for field in ("parent", "resume_target")
        for value in [source.declaration.fields.get(field)]
        if value is not None
    }
    contexts = tuple(
        source for source in validation.sources
        if source.profile != Profile.WORKSTREAM
        and source.authority_class == AuthorityClass.CANONICAL
        and source.semantic_id is not None
        and source.semantic_id.value in referenced
    )
    domain = workstream_result_data(
        build_workstream_graph(
            workstreams,
            snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT,
            context_sources=contexts,
        )
    )

    result = by_id(builds(core_repo))["workstream_graph"]
    derived = json.loads(result.view_bytes)
    assert derived["active_ready_set"] == domain["active_ready_set"]
    assert derived["route"]["disposition"] == domain["route"]["disposition"]
    assert derived["route"]["primary"] == (
        None if domain["route"]["primary"] is None
        else domain["route"]["primary"]["workstream_id"]
    )
    domain_nodes = domain["nodes"]
    for node in derived["nodes"]:
        domain_node = domain_nodes[node["semantic_id"]]
        assert node["readiness"] == domain_node["readiness"]
        assert node["dependency_closure"] == domain_node["dependency_closure"]
