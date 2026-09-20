from __future__ import annotations

import ast
from dataclasses import FrozenInstanceError
import importlib.util
from pathlib import Path
import sys

import pytest

from tools.project_knowledge.model import (
    AuthorityClass, GovernedSource, Profile, RawDeclaration, Relation, RelationMode,
    Scope, SemanticId, SnapshotMode, SourceRevision, thaw_json,
)
from tools.project_knowledge.view_definitions import PURE_UNIT_REGISTRY, source_inventory_specification


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "tools/project_knowledge"


def imports(source: str, module: str):
    package = module.rpartition(".")[0]
    for node in ast.walk(ast.parse(source)):
        if isinstance(node, ast.Import):
            yield from (alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            base = importlib.util.resolve_name("." * node.level + (node.module or ""), package) if node.level else node.module or ""
            yield base
            yield from (base + "." + alias.name for alias in node.names)


def allowed_dependency(module: str, dependency: str) -> bool:
    if dependency.split(".")[0] in sys.stdlib_module_names or dependency == "__future__":
        return True
    prefix = "tools.project_knowledge"
    if module == prefix + ".model":
        return False
    if ".adapters." in module:
        return dependency.startswith(prefix + ".model") or dependency.split(".")[0] in {"jsonschema", "referencing"}
    if ".services." in module:
        return dependency.startswith(prefix)
    if ".view_definitions." in module:
        # Declaration data: model types and sibling declarations only.
        return dependency.startswith((prefix + ".model", prefix + ".view_definitions"))
    if module == prefix + ".__main__":
        return dependency.startswith(prefix + ".cli")
    if module == prefix + ".cli":
        return dependency.startswith((prefix + ".model", prefix + ".services"))
    # All other top-level modules are L2. Parent import statements yield the
    # package itself too; aliases below are checked separately.
    return dependency == prefix or dependency.startswith(prefix + ".model")


def test_g001_package_boundary_and_all_layer_directions():
    assert PACKAGE.is_dir() and not (ROOT / "src/ads_system/project_knowledge").exists()
    for path in PACKAGE.rglob("*.py"):
        if path.name == "__init__.py":
            continue
        module = ".".join(path.relative_to(ROOT).with_suffix("").parts)
        for dependency in imports(path.read_text(encoding="utf-8"), module):
            assert allowed_dependency(module, dependency), (module, dependency)


def test_g009_production_units_and_tcb_have_explicit_source_contracts():
    from tools.project_knowledge.adapters.execution import TCB_FILES, check_tcb_source
    from tools.project_knowledge.adapters.pure import resolve_unit
    from tools.project_knowledge.adapters.schema import SCHEMA_FILES
    specification = source_inventory_specification()
    assert type(specification.compute) is type(specification.serialize) is str
    assert len(TCB_FILES) == 15 and len(SCHEMA_FILES) == 9
    assert set(specification.generator.implementation_files) == (
        set(TCB_FILES) | set(SCHEMA_FILES) | {
            "tools/project_knowledge/view_definitions/common.py",
            "tools/project_knowledge/view_definitions/source_inventory.py",
            "tools/project_knowledge/pure_source_inventory.py"})
    for path in TCB_FILES:
        check_tcb_source(path, (ROOT / path).read_bytes())
    accepted_prefix = (
        ("source_inventory.v1", "tools/project_knowledge/pure_source_inventory.py", "source_inventory",
         (("entry", "inventory_entry.v1"),), ()),
        ("inventory_entry.v1", "tools/project_knowledge/pure_source_inventory.py", "inventory_entry", (), ()),
        ("current_state_core.v1", "tools/project_knowledge/pure_current_state_core.py", "current_state_core",
         (("single", "core_single.v1"), ("fields", "core_fields.v1"),
          ("reference", "core_reference.v1"), ("paused", "core_paused.v1")), ("sorted_values",)),
        ("core_single.v1", "tools/project_knowledge/pure_current_state_core.py", "core_single", (), ("length", "fail_view")),
        ("core_fields.v1", "tools/project_knowledge/pure_current_state_core.py", "core_fields", (), ("fail_view",)),
        ("core_reference.v1", "tools/project_knowledge/pure_current_state_core.py", "core_reference",
         (("single", "core_single.v1"),), ()),
        ("core_procedure.v1", "tools/project_knowledge/pure_current_state_core.py", "core_procedure", (), ("length", "fail_view")),
        ("core_paused.v1", "tools/project_knowledge/pure_current_state_core.py", "core_paused",
         (("fields", "core_fields.v1"), ("reference", "core_reference.v1"), ("procedure", "core_procedure.v1")),
         ("sorted_values",)),
    )
    # Registry order is now per declaration module; the accepted records are unchanged data.
    assert set(accepted_prefix) <= set(PURE_UNIT_REGISTRY) and len(PURE_UNIT_REGISTRY) == 31
    identities = tuple(record[0] for record in PURE_UNIT_REGISTRY)
    assert len(identities) == len(set(identities))
    assert set(identities) == {
        "source_inventory.v1", "inventory_entry.v1",
        "current_state_core.v1", "core_single.v1", "core_fields.v1",
        "core_reference.v1", "core_procedure.v1", "core_paused.v1",
        "unique_values.v1", "normalized_scope.v1", "scope_token.v1",
        "normalized_relations.v1", "catalog_entry.v1", "source_catalog.v1",
        "has_temporal_control.v1", "identity_transition_record.v1",
        "identity_source_record.v1", "any_temporal.v1",
        "identity_static_resolution.v1", "identity_index.v1",
        "authority_candidate.v1", "authority_index.v1",
        "workstream_dependency_closure.v1", "workstream_parent_chain.v1",
        "workstream_node.v1", "workstream_graph.v1",
        "subject_memberships.v1", "subject_index.v1",
        "obligation_rows.v1", "risk_obligation_index.v1",
        "current_state_core_markdown.v1",
    }
    assert {record[1] for record in PURE_UNIT_REGISTRY} == {
        "tools/project_knowledge/pure_authority_index.py",
        "tools/project_knowledge/pure_current_state_core.py",
        "tools/project_knowledge/pure_current_state_core_markdown.py",
        "tools/project_knowledge/pure_identity_index.py",
        "tools/project_knowledge/pure_normalized_scope.py",
        "tools/project_knowledge/pure_risk_obligation_index.py",
        "tools/project_knowledge/pure_source_catalog.py",
        "tools/project_knowledge/pure_source_inventory.py",
        "tools/project_knowledge/pure_subject_index.py",
        "tools/project_knowledge/pure_temporal.py",
        "tools/project_knowledge/pure_unique_values.py",
        "tools/project_knowledge/pure_workstream_graph.py",
    }
    assert all(
        dependency in set(identities)
        for _, _, _, helpers, _ in PURE_UNIT_REGISTRY
        for _, dependency in helpers
    )
    blobs = {"tools/project_knowledge/pure_source_inventory.py":
             (PACKAGE / "pure_source_inventory.py").read_bytes()}
    compute = resolve_unit(specification.compute, PURE_UNIT_REGISTRY, blobs, {})
    assert compute(()) == {"schema_version": "1", "authority_class": "derived", "sources": []}


def test_g010_uses_same_closed_framework_and_no_research_runtime():
    from tools.project_knowledge.view_definitions import current_state_core_specification
    from tools.project_knowledge.adapters.pure import resolve_unit
    from tools.project_knowledge.services.generation import _capabilities
    core = current_state_core_specification()
    shared = source_inventory_specification().generator.implementation_files[:25]
    assert core.generator.implementation_files[:25] == shared
    assert core.generator.implementation_files[25:] == (
        "tools/project_knowledge/view_definitions/current_state_core.py",
        "tools/project_knowledge/view_definitions/units_current_state_core.py",
        "tools/project_knowledge/pure_current_state_core.py",
    )
    blobs = {p: (ROOT / p).read_bytes() for p in core.generator.implementation_files}
    compute = resolve_unit(core.compute, PURE_UNIT_REGISTRY, blobs, _capabilities())
    with pytest.raises(Exception, match="exactly one canonical owner"):
        compute(())
    assert core.compute_identity == "current_state_core.v1"
    assert core.serialize_identity == "canonical_json.v1"
    assert not any(p.startswith(("scripts/research/", "tests/", "docs/")) for p in blobs)


def test_g011_capture_planning_is_structurally_separate_from_authority():
    from tools.project_knowledge.model import HISTORICAL_CAPTURE_ROOT, OPEN_CAPTURE_ROOT
    from tools.project_knowledge.services.discovery import DiscoveryPolicy

    policy = DiscoveryPolicy()
    assert policy.open_capture_root == OPEN_CAPTURE_ROOT
    assert policy.historical_capture_root == HISTORICAL_CAPTURE_ROOT

    capture_module = "tools.project_knowledge.capture"
    capture_source = (PACKAGE / "capture.py").read_text(encoding="utf-8")
    capture_dependencies = tuple(imports(capture_source, capture_module))
    assert not any(dep.startswith((
        "tools.project_knowledge.authority",
        "tools.project_knowledge.services",
        "tools.project_knowledge.adapters",
    )) for dep in capture_dependencies)

    authority_module = "tools.project_knowledge.authority"
    authority_source = (PACKAGE / "authority.py").read_text(encoding="utf-8")
    assert not any(dep.startswith("tools.project_knowledge.capture") for dep in imports(authority_source, authority_module))


def test_g012_public_generation_and_repository_validation_have_nonleakage_gates():
    generation_tree = ast.parse((PACKAGE / "services/generation.py").read_text(encoding="utf-8"))
    generation_functions = {node.name: node for node in generation_tree.body if isinstance(node, ast.FunctionDef)}
    for name in ("_generate_verified", "generate_views"):
        calls = [node for node in ast.walk(generation_functions[name]) if isinstance(node, ast.Call)]
        assert any(isinstance(call.func, ast.Name) and call.func.id == "validate_public_projection" for call in calls)
    assert not any(
        isinstance(node, ast.Name) and node.id == "known_private_values"
        for node in ast.walk(generation_functions["_execute_bound"])
    )

    validation_tree = ast.parse((PACKAGE / "services/validation.py").read_text(encoding="utf-8"))
    validation_functions = {node.name: node for node in validation_tree.body if isinstance(node, ast.FunctionDef)}
    calls = [node for node in ast.walk(validation_functions["validate_repository"]) if isinstance(node, ast.Call)]
    assert any(isinstance(call.func, ast.Name) and call.func.id == "validate_public_projection" for call in calls)


def test_g013_impact_reuses_binding_admission_and_generation_without_compute_or_writes():
    generation = ast.parse((PACKAGE / "services/generation.py").read_text(encoding="utf-8"))
    functions = {n.name: n for n in generation.body if isinstance(n, ast.FunctionDef)}
    def calls(node):
        return {n.func.id for n in ast.walk(node) if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)}
    assert {"_generation_inputs", "bind_view_inputs", "validate_public_projection"} <= calls(functions["_dependencies_verified"])
    assert not {"build_views", "_generate_verified", "resolve_unit"} & calls(functions["_dependencies_verified"])
    assert {"_generation_inputs", "build_views", "validate_public_projection"} <= calls(functions["_generate_verified"])
    assert "validate_repository" in calls(functions["_generation_inputs"])
    views = ast.parse((PACKAGE / "views.py").read_text(encoding="utf-8"))
    builder = next(n for n in views.body if isinstance(n, ast.FunctionDef) and n.name == "build_views")
    assert "bind_view_inputs" in calls(builder)
    refresh = ast.parse((PACKAGE / "services/refresh.py").read_text(encoding="utf-8"))
    functions = {n.name: n for n in refresh.body if isinstance(n, ast.FunctionDef)}
    assert {"commit_snapshot", "_plan", "generate_views"} <= calls(functions["refresh_views"])
    assert "build_views" not in calls(refresh)
    assert not any(isinstance(n, ast.Attribute) and n.attr in {"write_bytes", "write_text", "unlink", "rename"}
                   for n in ast.walk(refresh))


def test_g014_cli_is_thin_and_generated_writes_are_structurally_bounded():
    main_tree = ast.parse((PACKAGE / "__main__.py").read_text(encoding="utf-8"))
    main_imports = tuple(imports((PACKAGE / "__main__.py").read_text(encoding="utf-8"),
                                 "tools.project_knowledge.__main__"))
    assert main_imports == ("tools.project_knowledge.cli", "tools.project_knowledge.cli.main")
    assert not any(isinstance(node, ast.FunctionDef) for node in main_tree.body)

    cli_tree = ast.parse((PACKAGE / "cli.py").read_text(encoding="utf-8"))
    cli_imports = tuple(imports((PACKAGE / "cli.py").read_text(encoding="utf-8"),
                                "tools.project_knowledge.cli"))
    assert all(allowed_dependency("tools.project_knowledge.cli", dependency) for dependency in cli_imports)
    assert not any(
        isinstance(node, ast.Attribute) and node.attr in {"write_bytes", "write_text", "unlink", "rename"}
        for node in ast.walk(cli_tree)
    )

    operations = ast.parse((PACKAGE / "services/cli_ops.py").read_text(encoding="utf-8"))
    functions = {node.name: node for node in operations.body if isinstance(node, ast.FunctionDef)}
    def named_calls(node):
        return {item.func.id for item in ast.walk(node)
                if isinstance(item, ast.Call) and isinstance(item.func, ast.Name)}
    assert {"validate_project_knowledge"} <= named_calls(functions["validate_operation"])
    assert {"validate_project_knowledge"} <= named_calls(functions["_require_semantic_validity"])
    assert "generate_views" in named_calls(functions["rebuild_operation"])
    assert "refresh_views" in named_calls(functions["refresh_operation"])
    assert "check_view_freshness" in named_calls(functions["check_freshness_operation"])

    semantic_validation = ast.parse(
        (PACKAGE / "services/semantic_validation.py").read_text(encoding="utf-8")
    )
    semantic_calls = {item.func.id for item in ast.walk(semantic_validation)
                      if isinstance(item, ast.Call) and isinstance(item.func, ast.Name)}
    assert {"validate_repository", "build_identity_index", "build_workstream_graph"} <= semantic_calls

    generated_io = (PACKAGE / "adapters/generated_io.py").read_text(encoding="utf-8")
    generated_tree = ast.parse(generated_io)
    assert 'GENERATED_ROOT = "docs/project_knowledge/generated/"' in generated_io
    assert any(
        isinstance(node, ast.Raise)
        and isinstance(node.exc, ast.Call)
        and isinstance(node.exc.func, ast.Name)
        and node.exc.func.id == "SubstrateError"
        for node in ast.walk(generated_tree)
    )
    from tools.project_knowledge.adapters.execution import TCB_FILES
    assert "tools/project_knowledge/adapters/generated_io.py" not in TCB_FILES
    assert "tools/project_knowledge/services/cli_ops.py" not in TCB_FILES
    assert "tools/project_knowledge/services/semantic_validation.py" not in TCB_FILES
    assert "tools/project_knowledge/cli.py" not in TCB_FILES

    from tools.project_knowledge.view_definitions import production_view_specifications
    persistent = production_view_specifications()
    assert len(persistent) == 8
    assert {spec.view_path for spec in persistent} == {
        "docs/project_knowledge/generated/source_catalog.json",
        "docs/project_knowledge/generated/identity_index.json",
        "docs/project_knowledge/generated/authority_index.json",
        "docs/project_knowledge/generated/workstream_graph.json",
        "docs/project_knowledge/generated/subject_index.json",
        "docs/project_knowledge/generated/risk_obligation_index.json",
        "docs/project_knowledge/generated/current_state_core.json",
        "docs/project_knowledge/generated/CURRENT_STATE_CORE.md",
    }
    assert {spec.view_id for spec in persistent} == {
        "source_catalog", "identity_index", "authority_index", "workstream_graph",
        "subject_index", "risk_obligation_index", "current_state_core",
        "current_state_core_markdown",
    }
    assert source_inventory_specification().view_id not in {spec.view_id for spec in persistent}


@pytest.mark.parametrize("source", [
    "from .adapters import gitio", "from . import adapters", "from . import services",
    "from .services.validation import validate_repository",
    "import tools.project_knowledge.adapters.gitio as git",
    "from tools.project_knowledge import services",
])
def test_architecture_guard_detects_forbidden_l2_imports(source):
    module = "tools.project_knowledge.declaration"
    assert any(not allowed_dependency(module, dep) for dep in imports(source, module))


def test_no_automatic_semantic_id_minting_capability():
    """Every production construction site must consume an authored JSON field.

    This allowlist makes a new ID factory/construction site require review;
    unlike a function-name search it catches hash/path helpers with other names.
    """
    approved = {
        ("adapters/schema.py", 'value["semantic_id"]'),
        ("services/validation.py", 'fields["semantic_id"]'),
        ("services/validation.py", 'r["target"]'),
        ("identity.py", 'value'),  # Only authored predecessor/successor fields; checked below.
        ("workstreams.py", 'data["parent"]'),
        ("workstreams.py", 'data["resume_target"]'),
        ("workstreams.py", 'value'),  # Only the authored depends_on list; checked below.
    }
    observed = set()
    for path in PACKAGE.rglob("*.py"):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "SemanticId":
                argument = ast.unparse(node.args[0]).replace("'", '"')
                observed.add((path.relative_to(PACKAGE).as_posix(), argument))
                if path.name == "identity.py":
                    assert any(
                        isinstance(parent, ast.GeneratorExp) and node is parent.elt
                        and ast.unparse(parent.generators[0].iter) in {
                            "fields['predecessors']", "fields.get('successors', ())",
                        }
                        for parent in ast.walk(tree)
                    )
                if path.name == "workstreams.py" and argument == "value":
                    assert any(
                        isinstance(parent, ast.GeneratorExp) and node is parent.elt
                        and ast.unparse(parent.generators[0].iter) == "data.get('depends_on', ())"
                        for parent in ast.walk(tree)
                    )
    assert observed == approved
    assert SemanticId.__dataclass_fields__["value"].default_factory is __import__("dataclasses").MISSING


def test_g004_selective_identity_and_immutable_scope_relations():
    fields = {"scope": {"target": ["one", "two"]}}
    raw = RawDeclaration(fields)
    fields["scope"]["target"].append("three")
    assert raw.fields["scope"]["target"] == ("one", "two")
    source = GovernedSource("docs/source.md", Profile.SEMANTIC_SOURCE, AuthorityClass.CANONICAL, "note", raw, SnapshotMode.WORKTREE_SNAPSHOT)
    assert source.semantic_id is None
    with pytest.raises(FrozenInstanceError):
        source.semantic_id = SemanticId("EXPLICIT:1")
    with pytest.raises(TypeError):
        raw.fields["new"] = True
    scope = Scope({"target": ["one", "two"]})
    assert scope.facets["target"] == ("one", "two")
    relation = Relation(RelationMode.SPECIALIZE, SemanticId("EXPLICIT:1"), scope)
    assert relation.target.value == "EXPLICIT:1"
    with pytest.raises(ValueError):
        Relation(RelationMode.SPECIALIZE, SemanticId("EXPLICIT:1"))


@pytest.mark.parametrize("value", ["", "contains spaces", "docs/file.md", "1starts-number", None])
def test_semantic_id_runtime_validation(value):
    with pytest.raises(ValueError):
        SemanticId(value)


def test_source_revision_cannot_construct_worktree_authority():
    with pytest.raises(ValueError, match="NON_COMMITTED"):
        SourceRevision("docs/source.md", "a" * 40, "sha256", "GIT_BLOB_BYTES_AT_COMMIT", "0" * 64, SnapshotMode.WORKTREE_SNAPSHOT)


def test_governed_source_cannot_mislabel_worktree_revision_or_capture():
    revision = SourceRevision("docs/source.md", "a" * 40, "sha256", "GIT_BLOB_BYTES_AT_COMMIT", "0" * 64)
    with pytest.raises(ValueError, match="Worktree"):
        GovernedSource("docs/source.md", Profile.SEMANTIC_SOURCE, AuthorityClass.CANONICAL, "note", RawDeclaration({}), SnapshotMode.WORKTREE_SNAPSHOT, revision=revision)
    with pytest.raises(ValueError, match="capture"):
        GovernedSource("docs/source.md", Profile.CAPTURE, AuthorityClass.CANONICAL, "note", RawDeclaration({}), SnapshotMode.COMMIT_SNAPSHOT)


def test_scope_value_object_rejects_predicate_mappings():
    with pytest.raises(ValueError):
        Scope({"target": {"regex": ".*"}})
