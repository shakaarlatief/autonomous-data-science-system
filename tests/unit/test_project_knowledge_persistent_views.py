"""Qualification of the complete Specification 028 persistent W0 view set."""

import ast
from dataclasses import replace
import json
from pathlib import Path

import pytest

from jsonschema import Draft202012Validator

from tools.project_knowledge.adapters.gitio import commit_snapshot, read_blobs
from tools.project_knowledge.adapters.pure import declared_units, resolve_unit
from tools.project_knowledge.identity import (
    build_identity_index, identity_index_data, transition_from_source,
)
from tools.project_knowledge.model import (
    AuthorityClass, Profile, SnapshotMode, SubstrateError, ViewFreshnessStatus, ViewInput,
)
from tools.project_knowledge.services.generation import generate_views
from tools.project_knowledge.services.generation import _capabilities
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge import view_definitions
from tools.project_knowledge.view_definitions import (
    DECLARATION_MODULES, identity_index_specification, production_view_specifications, PURE_UNIT_REGISTRY,
)
from tools.project_knowledge.view_definitions.common import SHARED_IMPLEMENTATION_FILES
from tools.project_knowledge.views import (
    build_views as domain_build_views, deterministic_json, manifest_freshness,
)
from tools.project_knowledge.workstreams import build_workstream_graph, workstream_result_data
from tests.unit.test_project_knowledge_current_state_core import (
    ACTIVE, FIXTURES, core_repo,
)
from tests.unit.test_project_knowledge_views import commit, write


ROOT = Path(__file__).resolve().parents[2]
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


def c1_material(root):
    """Exact fixture Git blobs and complete corpus, without checkout-code attestation."""
    specifications = production_view_specifications()
    snapshot = commit_snapshot(root, "HEAD")
    validation = validate_repository(snapshot)
    assert validation.ok
    entries = {entry.path: entry for entry in snapshot.entries}
    paths = {source.carrier_path for source in validation.sources}
    paths.update(path for specification in specifications for path in specification.generator.implementation_files)
    raw = read_blobs(root, tuple(entries[path] for path in sorted(paths)))
    content = {path: raw[entries[path].blob_id] for path in paths}
    corpus = tuple(ViewInput(source, content[source.carrier_path]) for source in validation.sources)
    return specifications, corpus, content


def blob_builds(material, overrides=None):
    """Build every view from ONLY its own declared closure blobs, like the bound worker."""
    specifications, corpus, content = material
    content = {**content, **(overrides or {})}
    capabilities = _capabilities()
    results = []
    for specification in specifications:
        closure = {path: content[path] for path in specification.generator.implementation_files}
        registry = declared_units(closure)
        compute = resolve_unit(specification.compute, registry, closure, capabilities)
        serialize = (deterministic_json if specification.serialize == "canonical_json.v1"
                     else resolve_unit(specification.serialize, registry, closure, capabilities))
        resolved = replace(specification, compute=compute, serialize=serialize)
        result, = domain_build_views(
            (resolved,), corpus, closure, snapshot_mode=SnapshotMode.COMMIT_SNAPSHOT,
        )
        results.append(result)
    return by_id(results)


PACKAGE_ROOT = "tools/project_knowledge/"
DEFINITIONS = PACKAGE_ROOT + "view_definitions/"
ALL_VIEWS = frozenset({
    "source_catalog", "identity_index", "authority_index", "workstream_graph", "subject_index",
    "risk_obligation_index", "current_state_core", "current_state_core_markdown",
})
NOT_CORE = ALL_VIEWS - {"current_state_core", "current_state_core_markdown"}

# Everything after the shared prefix: this view's specification module, the
# unit-declaration modules of its reachable units, then their pure sources.
EXPECTED_VIEW_SPECIFIC_FILES = {
    "source_catalog": (
        DEFINITIONS + "source_catalog.py", DEFINITIONS + "units_normalized_scope.py",
        DEFINITIONS + "units_unique_values.py", PACKAGE_ROOT + "pure_source_catalog.py",
        PACKAGE_ROOT + "pure_normalized_scope.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "identity_index": (
        DEFINITIONS + "identity_index.py", DEFINITIONS + "units_temporal.py",
        DEFINITIONS + "units_unique_values.py", PACKAGE_ROOT + "pure_identity_index.py",
        PACKAGE_ROOT + "pure_temporal.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "authority_index": (
        DEFINITIONS + "authority_index.py", DEFINITIONS + "units_normalized_scope.py",
        DEFINITIONS + "units_unique_values.py", PACKAGE_ROOT + "pure_authority_index.py",
        PACKAGE_ROOT + "pure_normalized_scope.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "workstream_graph": (
        DEFINITIONS + "workstream_graph.py", DEFINITIONS + "units_temporal.py",
        DEFINITIONS + "units_unique_values.py", PACKAGE_ROOT + "pure_workstream_graph.py",
        PACKAGE_ROOT + "pure_temporal.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "subject_index": (
        DEFINITIONS + "subject_index.py", DEFINITIONS + "units_unique_values.py",
        PACKAGE_ROOT + "pure_subject_index.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "risk_obligation_index": (
        DEFINITIONS + "risk_obligation_index.py", DEFINITIONS + "units_unique_values.py",
        PACKAGE_ROOT + "pure_risk_obligation_index.py", PACKAGE_ROOT + "pure_unique_values.py",
    ),
    "current_state_core": (
        DEFINITIONS + "current_state_core.py", DEFINITIONS + "units_current_state_core.py",
        PACKAGE_ROOT + "pure_current_state_core.py",
    ),
    "current_state_core_markdown": (
        DEFINITIONS + "current_state_core_markdown.py", DEFINITIONS + "units_current_state_core.py",
        PACKAGE_ROOT + "pure_current_state_core.py", PACKAGE_ROOT + "pure_current_state_core_markdown.py",
    ),
}
SHARED_PREFIX_LENGTH = 25


def shared_prefix_and_tail(specification):
    files = specification.generator.implementation_files
    return files[:SHARED_PREFIX_LENGTH], files[SHARED_PREFIX_LENGTH:]


def repository_path(module):
    return str(Path(module.__file__).resolve().relative_to(ROOT)).replace("\\", "/")


def derived_view_specific_files(specification):
    """Independent derivation from the unit graph, not from the declared lists."""
    records = {record[0]: record for record in PURE_UNIT_REGISTRY}
    assert len(records) == len(PURE_UNIT_REGISTRY)
    reachable, pending = set(), [specification.compute_identity]
    if specification.serialize_identity != "canonical_json.v1":
        pending.append(specification.serialize_identity)
    while pending:
        identity = pending.pop()
        if identity not in reachable:
            reachable.add(identity)
            pending.extend(dependency for _, dependency in records[identity][3])
    declared_in = {
        record[0]: repository_path(module) for module in DECLARATION_MODULES for record in module.PURE_UNITS
    }
    return (
        {repository_path(getattr(view_definitions, specification.view_id))}
        | {declared_in[identity] for identity in reachable}
        | {records[identity][1] for identity in reachable}
    )


def test_c1_implementation_closures_are_explicit_ordered_and_deterministic():
    from tools.project_knowledge.adapters.execution import TCB_FILES
    from tools.project_knowledge.adapters.schema import SCHEMA_FILES
    first, second = production_view_specifications(), production_view_specifications()
    assert first == second
    assert len(first) == 8 and {spec.view_id for spec in first} == ALL_VIEWS
    shared = first[0].generator.implementation_files[:SHARED_PREFIX_LENGTH]
    assert set(shared) == set(TCB_FILES) | set(SCHEMA_FILES) | {DEFINITIONS + "common.py"}
    assert shared == SHARED_IMPLEMENTATION_FILES
    for specification in first:
        prefix, tail = shared_prefix_and_tail(specification)
        assert prefix == shared
        assert tail == EXPECTED_VIEW_SPECIFIC_FILES[specification.view_id]
        files = specification.generator.implementation_files
        assert len(files) == len(set(files))
        assert not any(path.startswith("docs/") for path in files)


def test_c1_no_view_binds_another_views_specific_bytes():
    specifications = {spec.view_id: spec for spec in production_view_specifications()}
    private_modules = {DEFINITIONS + view_id + ".py" for view_id in specifications}
    for view_id, specification in specifications.items():
        tail = set(shared_prefix_and_tail(specification)[1])
        own = DEFINITIONS + view_id + ".py"
        assert own in tail
        assert not (tail & (private_modules - {own}))
        assert tail == derived_view_specific_files(specification)
    # Neither the host catalog nor the non-persistent inventory view is any persistent view's input.
    unbound = {DEFINITIONS + "__init__.py", DEFINITIONS + "source_inventory.py",
               PACKAGE_ROOT + "pure_source_inventory.py"}
    assert not any(unbound & set(spec.generator.implementation_files) for spec in specifications.values())


def test_c1_views_module_holds_only_shared_builder_infrastructure():
    """views.py is shared by every view, so it carries no view-specific declaration."""
    source = (ROOT / "tools/project_knowledge/views.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    names = {node.name for node in tree.body if isinstance(node, ast.FunctionDef)}
    assigned = {target.id for node in tree.body if isinstance(node, ast.Assign)
                for target in node.targets if isinstance(target, ast.Name)}
    assert not {name for name in names if name.endswith("_specification")}
    assert "production_view_specifications" not in names and "PURE_UNIT_REGISTRY" not in assigned
    assert "pure_" not in source and "view_definitions" not in source
    assert [path for path in SHARED_IMPLEMENTATION_FILES if "pure_" in path] == []
    assert [path for path in SHARED_IMPLEMENTATION_FILES
            if path.startswith(DEFINITIONS) and path != DEFINITIONS + "common.py"] == []


def test_c1_every_declared_view_specific_file_is_required_by_generation(core_repo):
    specifications, _, content = c1_material(core_repo)
    capabilities = _capabilities()
    for specification in specifications:
        closure = {path: content[path] for path in specification.generator.implementation_files}
        identities = [specification.compute]
        if specification.serialize != "canonical_json.v1":
            identities.append(specification.serialize)
        # Sufficient: the view's own closure alone resolves every unit it executes.
        for identity in identities:
            resolve_unit(identity, declared_units(closure), closure, capabilities)
        # Necessary: dropping any one view-specific file breaks resolution. The
        # specification module is the file that declares the closure itself.
        own = repository_path(getattr(view_definitions, specification.view_id))
        for path in shared_prefix_and_tail(specification)[1]:
            if path == own:
                continue
            reduced = {name: blob for name, blob in closure.items() if name != path}
            with pytest.raises(SubstrateError) as failure:
                for identity in identities:
                    resolve_unit(identity, declared_units(reduced), reduced, capabilities)
            assert failure.value.code in {"UNQUALIFIED_PURE_UNIT", "MISSING_PURE_IMPLEMENTATION"}, (
                specification.view_id, path)


def test_c1_declaration_loader_is_data_only_and_closure_scoped():
    good = b"PURE_UNITS = (('a.v1', 'tools/project_knowledge/pure_x.py', 'a', (), ()),)\n"
    path = DEFINITIONS + "x.py"
    assert declared_units({path: good}) == (("a.v1", "tools/project_knowledge/pure_x.py", "a", (), ()),)
    assert declared_units({PACKAGE_ROOT + "other.py": good, DEFINITIONS + "x.txt": good}) == ()
    assert declared_units({path: b"import os\nvalue = os.getcwd()\n"}) == ()
    for bad in (b"PURE_UNITS = [1]\n", b"PURE_UNITS = (open('x'),)\n", b"PURE_UNITS = ()\nPURE_UNITS = ()\n",
                b"PURE_UNITS = (\n"):
        with pytest.raises(SubstrateError) as failure:
            declared_units({path: bad})
        assert failure.value.code == "INVALID_PURE_REGISTRY"
    # A view's own blobs cannot qualify another view's private unit.
    specifications = {spec.view_id: spec for spec in production_view_specifications()}
    blobs = {p: (ROOT / p).read_bytes() for p in specifications["subject_index"].generator.implementation_files}
    with pytest.raises(SubstrateError) as failure:
        resolve_unit("identity_index.v1", declared_units(blobs), blobs, _capabilities())
    assert failure.value.code == "UNQUALIFIED_PURE_UNIT"


# path -> the exact set of views whose generation semantics depend on it
C1_INVALIDATION_CASES = {
    # view-specific specification / private unit-declaration modules
    DEFINITIONS + "subject_index.py": {"subject_index"},
    DEFINITIONS + "identity_index.py": {"identity_index"},
    DEFINITIONS + "authority_index.py": {"authority_index"},
    DEFINITIONS + "current_state_core.py": {"current_state_core"},
    DEFINITIONS + "current_state_core_markdown.py": {"current_state_core_markdown"},
    # unit declarations consumed by several views
    DEFINITIONS + "units_unique_values.py": NOT_CORE,
    DEFINITIONS + "units_temporal.py": {"identity_index", "workstream_graph"},
    DEFINITIONS + "units_normalized_scope.py": {"source_catalog", "authority_index"},
    DEFINITIONS + "units_current_state_core.py": {"current_state_core", "current_state_core_markdown"},
    # view-specific pure sources
    PACKAGE_ROOT + "pure_authority_index.py": {"authority_index"},
    PACKAGE_ROOT + "pure_risk_obligation_index.py": {"risk_obligation_index"},
    PACKAGE_ROOT + "pure_current_state_core_markdown.py": {"current_state_core_markdown"},
    # shared pure sources
    PACKAGE_ROOT + "pure_unique_values.py": NOT_CORE,
    PACKAGE_ROOT + "pure_temporal.py": {"identity_index", "workstream_graph"},
    PACKAGE_ROOT + "pure_normalized_scope.py": {"source_catalog", "authority_index"},
    PACKAGE_ROOT + "pure_current_state_core.py": {"current_state_core", "current_state_core_markdown"},
    # genuinely shared builder / admission / execution infrastructure and schemas
    PACKAGE_ROOT + "views.py": ALL_VIEWS,
    PACKAGE_ROOT + "model.py": ALL_VIEWS,
    PACKAGE_ROOT + "adapters/pure.py": ALL_VIEWS,
    PACKAGE_ROOT + "adapters/execution.py": ALL_VIEWS,
    PACKAGE_ROOT + "services/generation.py": ALL_VIEWS,
    DEFINITIONS + "common.py": ALL_VIEWS,
    "schemas/project_knowledge/defs.v1.schema.json": ALL_VIEWS,
}


def test_c1_declared_consumers_match_every_closure_membership():
    specifications = production_view_specifications()
    for path, expected in C1_INVALIDATION_CASES.items():
        assert {spec.view_id for spec in specifications if path in spec.generator.implementation_files} == expected, path


def test_c1_byte_change_invalidates_exactly_the_actual_consumers(core_repo):
    material = c1_material(core_repo)
    before = blob_builds(material)
    assert set(before) == ALL_VIEWS
    for path, expected in C1_INVALIDATION_CASES.items():
        after = blob_builds(material, {path: material[2][path] + b"\n# c1 fixture-only byte change\n"})
        stale = set()
        for view_id, previous in before.items():
            freshness = manifest_freshness(previous.manifest, after[view_id], existing_view_bytes=previous.view_bytes)
            if freshness.status == ViewFreshnessStatus.STALE:
                stale.add(view_id)
                assert {d.code for d in freshness.diagnostics} == {"STALE_VIEW_GENERATOR", "STALE_VIEW_BOUNDARY"}, (path, view_id)
            else:
                assert freshness.status == ViewFreshnessStatus.FRESH, (path, view_id)
                assert after[view_id].manifest_bytes == previous.manifest_bytes, (path, view_id)
            # Comment-only structure changes never change generated view bytes.
            assert after[view_id].view_bytes == previous.view_bytes, (path, view_id)
        assert stale == expected, path


def test_c1_full_and_each_selected_build_are_exactly_equivalent(core_repo):
    specifications = production_view_specifications()
    snapshot = commit_snapshot(core_repo, "HEAD")
    full = by_id(generate_views(snapshot, specifications))
    for view_id in full:
        selected, = generate_views(snapshot, specifications, selected_view_ids=(view_id,))
        assert selected == full[view_id]


def test_c1_bound_worker_build_matches_in_process_closure_build(core_repo):
    """The bound worker reads declarations from blobs and yields the same exact bytes."""
    snapshot = commit_snapshot(core_repo, "HEAD")
    worker = by_id(generate_views(snapshot, production_view_specifications()))
    local = blob_builds(c1_material(core_repo))
    assert {k: (v.view_bytes, v.manifest_bytes) for k, v in worker.items()} == {
        k: (v.view_bytes, v.manifest_bytes) for k, v in local.items()}


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
        assert node["current_anchor"] == domain_node["workstream"]["current_anchor"]
