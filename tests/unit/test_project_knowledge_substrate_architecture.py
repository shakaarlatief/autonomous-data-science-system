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
from tools.project_knowledge.views import (
    PURE_UNIT_REGISTRY, source_inventory_specification,
)


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
    if module == prefix + ".__main__":
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
        set(TCB_FILES) | set(SCHEMA_FILES) | {"tools/project_knowledge/pure_units.py"})
    for path in TCB_FILES:
        check_tcb_source(path, (ROOT / path).read_bytes())
    assert PURE_UNIT_REGISTRY == (
        ("source_inventory.v1", "tools/project_knowledge/pure_units.py", "source_inventory",
         (("entry", "inventory_entry.v1"),), ()),
        ("inventory_entry.v1", "tools/project_knowledge/pure_units.py", "inventory_entry", (), ()),
        ("current_state_core.v1", "tools/project_knowledge/pure_units.py", "current_state_core",
         (("single", "core_single.v1"), ("fields", "core_fields.v1"),
          ("reference", "core_reference.v1"), ("paused", "core_paused.v1")), ("sorted_values",)),
        ("core_single.v1", "tools/project_knowledge/pure_units.py", "core_single", (), ("length", "fail_view")),
        ("core_fields.v1", "tools/project_knowledge/pure_units.py", "core_fields", (), ("fail_view",)),
        ("core_reference.v1", "tools/project_knowledge/pure_units.py", "core_reference",
         (("single", "core_single.v1"),), ()),
        ("core_procedure.v1", "tools/project_knowledge/pure_units.py", "core_procedure", (), ("length", "fail_view")),
        ("core_paused.v1", "tools/project_knowledge/pure_units.py", "core_paused",
         (("fields", "core_fields.v1"), ("reference", "core_reference.v1"), ("procedure", "core_procedure.v1")),
         ("sorted_values",)),
    )
    blobs = {"tools/project_knowledge/pure_units.py": (PACKAGE / "pure_units.py").read_bytes()}
    compute = resolve_unit(specification.compute, PURE_UNIT_REGISTRY, blobs, {})
    assert compute(()) == {"schema_version": "1", "authority_class": "derived", "sources": []}


def test_g010_uses_same_closed_framework_and_no_research_runtime():
    from tools.project_knowledge.views import current_state_core_specification
    from tools.project_knowledge.adapters.pure import resolve_unit
    from tools.project_knowledge.services.generation import _capabilities
    core = current_state_core_specification()
    assert core.generator.implementation_files == source_inventory_specification().generator.implementation_files
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
