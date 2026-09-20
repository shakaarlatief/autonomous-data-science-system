"""G009 executable boundary regressions. Every service probe imports its fixture.

General repository callbacks/package plugins are intentionally no longer a
durable execution API. Tests below preserve their attack classes through the
stronger data-only definition and restricted-source contract.
"""
import ast
from dataclasses import replace
import json
import os
import shutil
import sysconfig
import venv
from pathlib import Path
import subprocess
import sys

import pytest

from tests.unit.test_project_knowledge_views import repo, git, commit
from tools.project_knowledge.adapters.pure import resolve_unit
from tools.project_knowledge.model import SubstrateError

PURE_PATH = "tools/project_knowledge/pure_source_inventory.py"

PROBE = r'''
import json, sys
from dataclasses import replace
from pathlib import Path
request = json.load(sys.stdin)
root = Path.cwd()
views_path = root / "tools/project_knowledge/views.py"
original = views_path.read_bytes()
if request.get("cached_code"):
    views_path.write_bytes(original.replace(b"ensure_ascii=False", b"ensure_ascii=True"))
from tools.project_knowledge import views, model
from tools.project_knowledge.view_definitions.source_inventory import source_inventory_specification
from tools.project_knowledge.adapters.gitio import commit_snapshot
from tools.project_knowledge.services.generation import generate_views, check_view_freshness
if request.get("cached_code"):
    views_path.write_bytes(original)
if request.get("cached_binding"):
    from types import SimpleNamespace
    views.json = SimpleNamespace(dumps=lambda *a, **k: '{"ambient":"HOST"}')
base = source_inventory_specification()
files = tuple(p for p in base.generator.implementation_files if p not in request.get("exclude", ()))
files += tuple(request.get("extra", ()))
spec = replace(base, view_path=request.get("view_path", base.view_path), compute=request.get("unit", base.compute),
               serialize=request.get("serializer", base.serialize),
               generator=replace(base.generator, implementation_files=files))
if request.get("callable"):
    spec = replace(spec, **{request["callable"]: lambda value: value})
specs = (spec,)
if request.get("second_extra"):
    second = replace(base, view_id="second",
        view_path="docs/project_knowledge/generated/second.json",
        manifest_path="docs/project_knowledge/generated/manifests/second.json",
        compute=request.get("unit", base.compute),
        generator=replace(base.generator, implementation_files=base.generator.implementation_files + tuple(request["second_extra"])))
    specs += (second,)
snapshot = commit_snapshot(root, request["commit"])
host_observations = {}
if request.get("observe"):
    from tools.project_knowledge.adapters.schema import SchemaValidator
    host_observations = {
        "json_string_hex": json.encoder.encode_basestring("sources").encode().hex(),
        "profile": model.Profile.SEMANTIC_SOURCE.value,
        "serializer_hex": views.deterministic_json({"value": "ÃƒÆ’Ã‚Â©"}).hex(),
        "schema_required": SchemaValidator().validators[model.Profile.SEMANTIC_SOURCE].schema["required"],
    }
if request.get("editable_name"):
    import importlib.util
    host_observations["editable_origin"] = importlib.util.find_spec(request["editable_name"]).origin
result = {"host_observations": host_observations, "loaded_from": str(Path(views.__file__).resolve()),
          "pure_module_imported": any(name.startswith("tools.project_knowledge.pure_") for name in sys.modules)}
try:
    builds = generate_views(snapshot, specs, selected_view_ids=request.get("selected"))
    built = next(item for item in builds if item.view_id == spec.view_id)
    result.update(status="BUILT", view_bytes=built.view_bytes.hex(),
                  manifest_bytes=built.manifest_bytes.hex(), output=json.loads(built.view_bytes) if built.view_path.endswith(".json") else built.view_bytes.decode("utf-8"),
                  manifest=json.loads(built.manifest_bytes))
except views.ViewValidationError as error:
    result.update(status="REJECTED", codes=[d.code for d in error.diagnostics])
manifest = request.get("manifest", result.get("manifest"))
if manifest is not None:
    freshness = check_view_freshness(snapshot, specs, spec.view_id, model.RawDeclaration(manifest),
        existing_view_bytes=bytes.fromhex(request["existing"]) if "existing" in request else None)
    result.update(freshness=freshness.status, diagnostics=[d.code for d in freshness.diagnostics])
print(json.dumps(result))
'''


def probe(repo, ambient="ONE", *, interpreter=None, **request):
    request.setdefault("commit", git(repo, "rev-parse", "HEAD").decode().strip())
    process = subprocess.run([str(interpreter or sys.executable), "-B", "-c", PROBE], cwd=repo,
        input=json.dumps(request).encode(), capture_output=True,
        env=dict(os.environ, G009_AMBIENT=ambient))
    assert process.returncode == 0, process.stderr.decode(errors="replace")
    result = json.loads(process.stdout)
    assert Path(result["loaded_from"]) == (repo / "tools/project_knowledge/views.py").resolve()
    assert result["pure_module_imported"] is False
    return result


def rejected(result, code=None):
    assert result["status"] == "REJECTED"
    assert not {"view_bytes", "manifest", "manifest_bytes", "output"} & result.keys()
    assert result["freshness"] == "INVALID"
    if code:
        assert code in result["codes"] and code in result["diagnostics"]


def register(repo, *entries):
    """Amend committed fixture DATA, never register a live Python object."""
    path = repo / "tools/project_knowledge/view_definitions/source_inventory.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    node, = [node for node in tree.body if isinstance(node, ast.Assign)
             and any(isinstance(target, ast.Name) and target.id == "PURE_UNITS" for target in node.targets)]
    node.value = ast.parse(repr(ast.literal_eval(node.value) + entries), mode="eval").body
    path.write_text(ast.unparse(ast.fix_missing_locations(tree)) + "\n", encoding="utf-8")


def custom(repo, source, *, helpers=(), capabilities=(), path="tools/project_knowledge/custom_pure.py", identity="fixture.v1"):
    target = repo / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source, encoding="utf-8")
    register(repo, (identity, path, "compute", helpers, capabilities))
    return path


def test_environment_independence_and_positive_production(repo):
    one, two = probe(repo, "ONE"), probe(repo, "TWO")
    assert one["status"] == two["status"] == "BUILT"
    assert one["view_bytes"] == two["view_bytes"]
    assert one["manifest_bytes"] == two["manifest_bytes"]
    assert one["freshness"] == two["freshness"] == "FRESH"
    assert one["diagnostics"] == two["diagnostics"] == []
    assert probe(repo, existing=one["view_bytes"], manifest=one["manifest"])["freshness"] == "FRESH"


@pytest.mark.parametrize("change", ["python", "schema", "cached_code", "pure_source"])
def test_actual_executing_drift_rejects_build_and_freshness(repo, change):
    before = probe(repo, observe=True)
    head = git(repo, "rev-parse", "HEAD")
    if change == "schema":
        path = repo / "schemas/project_knowledge/semantic_source.v1.schema.json"
        schema = json.loads(path.read_bytes())
        schema["required"].append("uncommitted_control")
        path.write_text(json.dumps(schema), encoding="utf-8")
    elif change in {"python", "pure_source"}:
        path = repo / ("tools/project_knowledge/views.py" if change == "python" else PURE_PATH)
        original = path.read_bytes()
        changed = (original.replace(b"ensure_ascii=False", b"ensure_ascii=True") if change == "python"
                   else original.replace(b'"schema_version": "1"', b'"schema_version": "X"'))
        assert changed != original
        path.write_bytes(changed)
        if change == "pure_source":
            namespace = {}
            exec(compile(changed, str(path), "exec"), namespace)
            assert namespace["source_inventory"](()) == {"schema_version": "X", "authority_class": "derived", "sources": []}
    result = probe(repo, manifest=before["manifest"], cached_code=change == "cached_code", observe=True)
    rejected(result, "EXECUTION_IMPLEMENTATION_MISMATCH")
    if change in {"python", "cached_code"}:
        assert result["host_observations"]["serializer_hex"] != before["host_observations"]["serializer_hex"]
    if change == "schema":
        assert "uncommitted_control" in result["host_observations"]["schema_required"]
        assert "uncommitted_control" not in before["host_observations"]["schema_required"]
    assert git(repo, "rev-parse", "HEAD") == head


def test_crlf_checkout_conversion_preserves_git_attestation(repo):
    before = probe(repo)
    git(repo, "config", "core.autocrlf", "true")
    for path in [*repo.rglob("*.py"), *(repo / "schemas/project_knowledge").glob("*.json")]:
        path.write_bytes(git(repo, "cat-file", "--filters", "HEAD:" + path.relative_to(repo).as_posix()))
    assert b"\r\n" in (repo / PURE_PATH).read_bytes()
    after = probe(repo, manifest=before["manifest"])
    assert after["status"] == "BUILT" and after["freshness"] == "FRESH"
    assert after["view_bytes"] == before["view_bytes"]
    assert after["manifest_bytes"] == before["manifest_bytes"]


def test_cached_mutable_binding_has_no_worker_authority(repo):
    before = probe(repo)
    after = probe(repo, cached_binding=True, manifest=before["manifest"])
    assert after["status"] == "BUILT" and after["freshness"] == "FRESH"
    assert after["view_bytes"] == before["view_bytes"]


def test_committed_pure_change_changes_binding_and_stales_manifest(repo):
    before = probe(repo)
    path = repo / PURE_PATH
    path.write_bytes(path.read_bytes().replace(b'"schema_version": "1"', b'"schema_version": "X"'))
    commit(repo)
    after = probe(repo, manifest=before["manifest"])
    assert after["output"]["schema_version"] == "X"
    assert after["manifest"]["generator"]["implementation_digest"] != before["manifest"]["generator"]["implementation_digest"]
    assert after["freshness"] == "STALE"


DEEP_ATTACKS = {
    "json": r'''
import os
_g009_original_encode_basestring = json.encoder.encode_basestring
def _g009_ambient_encode_basestring(value):
    encoded = _g009_original_encode_basestring(value)
    if value == "sources" and os.environ.get("G009_AMBIENT") == "TWO":
        return '"\\u0073ources"'
    return encoded
json.encoder.encode_basestring = _g009_ambient_encode_basestring
''',
    "enum": r'''
import enum
def _g009_ambient_enum_value(self):
    result = self._value_
    if result == "semantic_source.v1" and __import__("os").environ.get("G009_AMBIENT") == "TWO":
        return "ambient_semantic_source.v1"
    return result
enum.Enum.__dict__["value"].fget.__code__ = _g009_ambient_enum_value.__code__
''',
}


@pytest.mark.parametrize("attack", ["json", "enum"])
def test_exact_deep_runtime_import_attacks_fail_closed(repo, attack):
    before = probe(repo)
    path = repo / "tools/project_knowledge/views.py"
    path.write_text(path.read_text(encoding="utf-8") + DEEP_ATTACKS[attack], encoding="utf-8")
    commit(repo)
    head = git(repo, "rev-parse", "HEAD")
    observations = []
    for ambient in ("ONE", "TWO"):
        result = probe(repo, ambient, manifest=before["manifest"], observe=True)
        rejected(result, "TCB_ADMISSION_FAILED")
        observations.append(result["host_observations"])
    key = "json_string_hex" if attack == "json" else "profile"
    assert observations[0][key] != observations[1][key]
    assert git(repo, "rev-parse", "HEAD") == head


@pytest.mark.parametrize("effect", [
    'import os\n',
    'import json\njson.encoder.encode_basestring = lambda value: value\n',
    'from pathlib import Path\nPath("PURE_IMPORT_SENTINEL").write_text("executed")\n',
    'compute.ambient = "state"\n',
    'ambient = 1\n',
])
def test_pure_module_body_is_never_executed(repo, effect):
    before = probe(repo)
    path = custom(repo, 'def compute(inputs):\n    return {"value": "safe"}\n' + effect)
    commit(repo)
    result = probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"])
    rejected(result, "PURE_MODULE_INITIALIZATION_FORBIDDEN")
    assert not (repo / "PURE_IMPORT_SENTINEL").exists()


@pytest.mark.parametrize("statement", [
    "import os", "import importlib", "import json",
    'return __import__("os")', 'return eval("1")', 'return globals()',
    'return inputs.__class__', 'inputs[0] = "changed"', 'global ambient',
    'def nested():\n        return inputs\n    return nested()',
    'return canonical_json.__globals__',
    'canonical_json.ambient = inputs',
    'return [canonical_json][0](inputs)',
    'cap = canonical_json\n    return cap(inputs)',
])
def test_pure_unit_forbidden_runtime_mechanisms(repo, statement):
    before = probe(repo)
    caps = ("canonical_json",) if "canonical_json" in statement else ()
    path = custom(repo, "def compute(inputs):\n    " + statement + "\n", capabilities=caps)
    commit(repo)
    rejected(probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"]))


@pytest.mark.parametrize("state,source,code", [
    ("defaults", 'def compute(inputs, ambient="capture"):\n    return ambient\n', "PURE_DEFAULTS_FORBIDDEN"),
    ("kwdefaults", 'def compute(inputs, *, ambient="capture"):\n    return ambient\n', "PURE_KWDEFAULTS_FORBIDDEN"),
    ("decorator", '@ambient\ndef compute(inputs):\n    return inputs\n', "PURE_FUNCTION_STATE_FORBIDDEN"),
    ("annotation", 'def compute(inputs: ambient):\n    return inputs\n', "PURE_FUNCTION_STATE_FORBIDDEN"),
    ("closure", 'def compute(inputs):\n    def captured():\n        return inputs\n    return captured()\n', "PURE_SYNTAX_FORBIDDEN"),
])
def test_callable_state_is_rejected_from_source(repo, state, source, code):
    before = probe(repo)
    path = custom(repo, source)
    commit(repo)
    for ambient in ("ONE", "TWO"):
        rejected(probe(repo, ambient, unit="fixture.v1", extra=[path], manifest=before["manifest"]), code)


@pytest.mark.parametrize("state", ["defaults", "kwdefaults", "attributes", "closure", "trusted_object"])
def test_earlier_ambient_capture_examples_cannot_initialize_tcb(repo, state):
    before = probe(repo)
    additions = {
        "defaults": '\nimport os\ndef captured(value, ambient=os.environ.get("G009_AMBIENT")):\n    return value\n',
        "kwdefaults": '\nimport os\ndef captured(value, *, ambient=os.environ.get("G009_AMBIENT")):\n    return value\n',
        "attributes": '\nthaw_json.ambient = "captured"\n',
        "closure": '\ndef factory():\n    def captured(value):\n        return value\n    return captured\nthaw_json = factory()\n',
        "trusted_object": '\nMapping.ambient = "captured"\n',
    }
    path = repo / "tools/project_knowledge/model.py"
    path.write_text(path.read_text(encoding="utf-8") + additions[state], encoding="utf-8")
    commit(repo)
    for ambient in ("ONE", "TWO"):
        rejected(probe(repo, ambient, manifest=before["manifest"]),
                 "EXECUTION_IMPLEMENTATION_MISMATCH" if state == "closure" else "TCB_ADMISSION_FAILED")


@pytest.mark.parametrize("role", ["compute", "serialize"])
def test_live_callables_do_not_gain_durable_authority(repo, role):
    before = probe(repo)
    rejected(probe(repo, callable=role, manifest=before["manifest"]), "UNQUALIFIED_DURABLE_CALLBACK")


@pytest.mark.parametrize("identity,serializer", [("absent", False), ("absent", True)])
def test_unqualified_data_identity_fails(repo, identity, serializer):
    before = probe(repo)
    request = {"serializer" if serializer else "unit": identity}
    rejected(probe(repo, manifest=before["manifest"], **request), "UNQUALIFIED_PURE_UNIT")


def test_canonical_serializer_capability_positive(repo):
    before = probe(repo)
    path = custom(repo, "def compute(value):\n    return canonical_json(value)\n",
                  capabilities=("canonical_json",), identity="serializer.v1")
    commit(repo)
    after = probe(repo, serializer="serializer.v1", extra=[path])
    assert after["status"] == "BUILT" and after["freshness"] == "FRESH"
    assert after["view_bytes"] == before["view_bytes"]


def test_manifest_freshness_binds_compute_unit_identity(repo):
    path = "tools/project_knowledge/contract_units.py"
    (repo / path).write_text(
        'def compute_a(inputs):\n    return {"variant": "A"}\n'
        'def compute_b(inputs):\n    return {"variant": "B"}\n', encoding="utf-8")
    register(repo,
             ("compute_a.v1", path, "compute_a", (), ()),
             ("compute_b.v1", path, "compute_b", (), ()))
    commit(repo)
    first = probe(repo, unit="compute_a.v1", extra=[path])
    second = probe(repo, unit="compute_b.v1", extra=[path], manifest=first["manifest"])
    assert first["status"] == second["status"] == "BUILT"
    assert first["output"] == {"variant": "A"} and second["output"] == {"variant": "B"}
    assert first["view_bytes"] != second["view_bytes"]
    assert (first["manifest"]["generator"]["implementation_digest"]
            == second["manifest"]["generator"]["implementation_digest"])
    assert first["manifest_bytes"] != second["manifest_bytes"]
    assert second["freshness"] == "STALE"
    assert "STALE_VIEW_BOUNDARY" in second["diagnostics"]


def test_manifest_freshness_binds_serializer_identity(repo):
    path = "tools/project_knowledge/contract_serializers.py"
    (repo / path).write_text(
        'def compute(inputs):\n    return {"value": "same"}\n'
        'def serialize_a(value):\n    return utf8_text("A")\n'
        'def serialize_b(value):\n    return utf8_text("B")\n', encoding="utf-8")
    register(repo,
             ("contract_compute.v1", path, "compute", (), ()),
             ("serializer_a.v1", path, "serialize_a", (), ("utf8_text",)),
             ("serializer_b.v1", path, "serialize_b", (), ("utf8_text",)))
    commit(repo)
    options = dict(unit="contract_compute.v1", extra=[path],
                   view_path="docs/project_knowledge/generated/contract.md")
    first = probe(repo, serializer="serializer_a.v1", **options)
    second = probe(repo, serializer="serializer_b.v1", manifest=first["manifest"], **options)
    assert first["status"] == second["status"] == "BUILT"
    assert first["output"] == "A\n" and second["output"] == "B\n"
    assert first["view_bytes"] != second["view_bytes"]
    assert (first["manifest"]["generator"]["implementation_digest"]
            == second["manifest"]["generator"]["implementation_digest"])
    assert first["manifest_bytes"] != second["manifest_bytes"]
    assert second["freshness"] == "STALE"
    assert "STALE_VIEW_BOUNDARY" in second["diagnostics"]


@pytest.mark.parametrize("substitute", ["parameter", "local", "unknown_capability"])
def test_exact_capability_bindings_cannot_be_substituted(repo, substitute):
    before = probe(repo)
    source = {
        "parameter": "def compute(canonical_json):\n    return canonical_json({})\n",
        "local": "def compute(inputs):\n    canonical_json = inputs\n    return canonical_json({})\n",
        "unknown_capability": "def compute(inputs):\n    return environment(inputs)\n",
    }[substitute]
    caps = ("environment",) if substitute == "unknown_capability" else ("canonical_json",)
    path = custom(repo, source, capabilities=caps)
    commit(repo)
    rejected(probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"]),
             "INVALID_PURE_CAPABILITY" if substitute == "unknown_capability" else "PURE_BINDING_SUBSTITUTION")


def test_helpers_are_recursive_explicit_and_per_view(repo):
    before = probe(repo)
    helper = "tools/project_knowledge/other_pure.py"
    (repo / helper).write_text('def value(inputs):\n    return {"value": "ONE"}\n', encoding="utf-8")
    path = custom(repo, "def compute(inputs):\n    return helper(inputs)\n",
                  helpers=(("helper", "helper.v1"),))
    register(repo, ("helper.v1", helper, "value", (), ()))
    commit(repo)
    valid = probe(repo, unit="fixture.v1", extra=[path, helper])
    assert valid["status"] == "BUILT" and valid["output"] == {"value": "ONE"}
    for selected in (None, ["source_inventory"]):
        result = probe(repo, unit="fixture.v1", extra=[path],
            second_extra=[path, helper], selected=selected, manifest=valid["manifest"])
        rejected(result, "MISSING_PURE_IMPLEMENTATION")
    result = probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"])
    rejected(result, "MISSING_PURE_IMPLEMENTATION")


def test_missing_helper_qualification_and_dependency_drift(repo):
    before = probe(repo)
    path = custom(repo, "def compute(inputs):\n    return helper(inputs)\n",
                  helpers=(("helper", "absent.v1"),))
    commit(repo)
    rejected(probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"]), "UNQUALIFIED_PURE_UNIT")
    (repo / path).write_text("def compute(inputs):\n    return other(inputs)\n", encoding="utf-8")
    commit(repo)
    rejected(probe(repo, unit="fixture.v1", extra=[path], manifest=before["manifest"]), "PURE_CALL_FORBIDDEN")


def test_registered_helper_cycles_and_self_recursion(repo):
    path = custom(repo, """def compute(inputs):
    return {"value": a(True), "depth": count(3)}
def a(value):
    return b(False) if value else "A"
def b(value):
    return a(False) if value else "B"
def count(value):
    return 1 + count(value - 1) if value else 0
""", helpers=(("a", "a.v1"), ("count", "count.v1")))
    register(repo, ("a.v1", path, "a", (("b", "b.v1"),), ()),
             ("b.v1", path, "b", (("a", "a.v1"),), ()),
             ("count.v1", path, "count", (("count", "count.v1"),), ()))
    commit(repo)
    result = probe(repo, unit="fixture.v1", extra=[path])
    assert result["status"] == "BUILT" and result["output"] == {"value": "B", "depth": 3}
    assert result["freshness"] == "FRESH"


@pytest.mark.parametrize("kind", ["module", "package", "namespace", "editable"])
def test_repository_packages_cannot_become_implicit_tcb(repo, kind):
    before = probe(repo)
    dependency = {"module": "src/owned_module.py", "package": "src/owned_package/__init__.py",
                  "namespace": "src/owned_namespace/dependency.py", "editable": "src/owned_editable/__init__.py"}[kind]
    name = {"module": "owned_module", "package": "owned_package",
            "namespace": "owned_namespace.dependency", "editable": "owned_editable"}[kind]
    target = repo / dependency
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text('from pathlib import Path\nPath("PACKAGE_SENTINEL").write_text("escaped")\n', encoding="utf-8")
    # Probe a dynamic infrastructure import, including explicitly declared code:
    # the loader must not infer TCB membership from declaration or discovery.
    path = repo / "tools/project_knowledge/services/generation.py"
    source = path.read_text(encoding="utf-8")
    source = source.replace('def _worker_dispatch(request, blobs):',
        'def _worker_dispatch(request, blobs):\n    __import__(' + repr(name) + ')')
    path.write_text(source, encoding="utf-8")
    commit(repo)
    for extra in ([], [dependency]):
        rejected(probe(repo, extra=extra, manifest=before["manifest"]), "BOUND_EXECUTION_FAILED")
    assert not (repo / "PACKAGE_SENTINEL").exists()



def test_real_editable_install_cannot_escape_isolated_worker(repo):
    before = probe(repo)
    name = "editable_escape"
    dependency = repo / "untracked_editable" / name / "__init__.py"
    dependency.parent.mkdir(parents=True)
    dependency.write_text('raise AssertionError("editable repository module executed")\n', encoding="utf-8")
    environment = repo / ".runtime"
    venv.EnvBuilder(with_pip=False).create(environment)
    interpreter = environment / ("Scripts/python.exe" if os.name == "nt" else "bin/python")
    site = Path(subprocess.check_output([str(interpreter), "-c",
        'import sysconfig; print(sysconfig.get_path("purelib"))'], text=True).strip())
    dependencies = Path(sysconfig.get_path("purelib"))
    for package in ("attr", "attrs", "jsonschema", "jsonschema_specifications", "referencing", "rpds"):
        shutil.copytree(dependencies / package, site / package)
    shutil.copyfile(dependencies / "typing_extensions.py", site / "typing_extensions.py")
    finder = ("import importlib.abc, importlib.util, sys\n"
              "class EditableFinder(importlib.abc.MetaPathFinder):\n"
              "    def find_spec(self, fullname, path=None, target=None):\n"
              "        if fullname == 'editable_escape':\n"
              "            return importlib.util.spec_from_file_location(fullname, " + repr(str(dependency)) + ")\n"
              "sys.meta_path.insert(0, EditableFinder())\n")
    (site / "g009_editable_finder.py").write_text(finder, encoding="utf-8")
    (site / "g009_editable.pth").write_text("import g009_editable_finder\n", encoding="utf-8")
    baseline = probe(repo, interpreter=interpreter, editable_name=name)
    assert baseline["status"] == "BUILT" and baseline["freshness"] == "FRESH"
    assert baseline["view_bytes"] == before["view_bytes"]
    path = repo / "tools/project_knowledge/services/generation.py"
    path.write_text(path.read_text().replace("def _worker_dispatch(request, blobs):",
        'def _worker_dispatch(request, blobs):\n    __import__("editable_escape")'), encoding="utf-8")
    # Commit only the changed infrastructure; editable code stays outside the snapshot.
    git(repo, "add", "tools/project_knowledge/services/generation.py")
    git(repo, "commit", "--quiet", "-m", "G009 editable fixture")
    result = probe(repo, interpreter=interpreter, editable_name=name, manifest=before["manifest"])
    assert Path(result["host_observations"]["editable_origin"]) == dependency
    rejected(result, "BOUND_EXECUTION_FAILED")


def test_pure_helpers_can_live_in_declared_regular_package_paths_without_import(repo):
    path = "src/owned_package/__init__.py"
    custom(repo, 'def compute(inputs):\n    return {"value": "bound"}\n', path=path)
    commit(repo)
    result = probe(repo, unit="fixture.v1", extra=[path], exclude=[PURE_PATH])
    assert result["status"] == "BUILT" and result["output"] == {"value": "bound"}
    assert PURE_PATH not in result["manifest"]["generator"]["implementation_files"]
    assert path in result["manifest"]["generator"]["implementation_files"]


@pytest.mark.parametrize("initialization", [
    'json.encoder.encode_basestring = None',
    'class Evil:\n    json.encoder.encode_basestring = None',
    'def side_effect():\n    return 1\nambient = side_effect()',
    '@side_effect\ndef extra():\n    return 1',
    'class Extra(UnknownBase):\n    pass',
    'from .model import thaw_json as dataclass',
    'import json as re',
    'import dataclasses as dataclass',
    'def StrEnum():\n    pass',
    'class Extra:\n    def __init_subclass__(cls):\n        pass',
])
def test_tcb_initialization_contract_rejects_indirect_side_effects(initialization):
    from tools.project_knowledge.adapters.execution import check_tcb_source
    with pytest.raises(ValueError):
        check_tcb_source("tools/project_knowledge/views.py", initialization)


def test_plain_boundary_rejects_executable_domain_values():
    class Hostile:
        def __getitem__(self, key):
            raise AssertionError("must not invoke user hooks")
    registry = (("test", "pure.py", "compute", (), ()),)
    unit = resolve_unit("test", registry, {"pure.py": b"def compute(value):\n    return value\n"}, {})
    with pytest.raises(SubstrateError, match="plain data"):
        unit(Hostile())
    assert unit({"nested": [1, 2]}) == {"nested": [1, 2]}

def test_qualified_text_serializer_uses_same_full_and_selected_builder(repo):
    path = custom(repo, 'def compute(inputs):\n    return {"value": "cafÃƒÂ©"}\n'
                  'def serialize(value):\n    return utf8_text("# " + value["value"] + "\\r\\n")\n')
    register(repo, ("text_serializer.v1", path, "serialize", (), ("utf8_text",)))
    commit(repo)
    options = dict(unit="fixture.v1", serializer="text_serializer.v1", extra=[path],
                   view_path="docs/project_knowledge/generated/fixture.md")
    full = probe(repo, **options)
    selected = probe(repo, selected=["source_inventory"], **options)
    assert full["status"] == "BUILT" and full["freshness"] == "FRESH"
    assert full["output"] == "# cafÃƒÂ©\n"
    assert full["view_bytes"] == selected["view_bytes"]
    assert full["manifest_bytes"] == selected["manifest_bytes"]


@pytest.mark.parametrize("package", [False, True])
def test_loader_rejects_discovered_repository_namespace_or_package(tmp_path, monkeypatch, package):
    from tools.project_knowledge.adapters.execution import _SnapshotModules
    root = tmp_path / "src"
    directory = root / "unbound_package"
    directory.mkdir(parents=True)
    if package:
        (directory / "__init__.py").write_text('raise AssertionError("must not execute")\n')
    monkeypatch.syspath_prepend(str(root))
    loader = _SnapshotModules({}, (tmp_path,), (), ())
    with pytest.raises(ImportError, match="External repository import is not admitted"):
        loader.find_spec("unbound_package")


@pytest.mark.parametrize("expression,caps,code", [
    ("as_text(item for item in inputs)", ("as_text",), "PURE_SYNTAX_FORBIDDEN"),
    ("as_text(sequence_range(2))", ("as_text", "sequence_range"), "INVALID_PURE_DATA"),
    ("inputs is inputs", (), "PURE_SYNTAX_FORBIDDEN"),
])
def test_runtime_representations_and_identity_cannot_enter_persistent_data(repo, expression, caps, code):
    before = probe(repo)
    path = custom(repo, 'def compute(inputs):\n    return {"value": ' + expression + '}\n', capabilities=caps)
    commit(repo)
    for ambient in ("ONE", "TWO"):
        rejected(probe(repo, ambient, unit="fixture.v1", extra=[path], manifest=before["manifest"]), code)


def test_text_capability_accepts_only_plain_data():
    from tools.project_knowledge.adapters.pure import plain_text
    first, second = (x for x in (1,)), (x for x in (1,))
    assert str(first) != str(second)  # The raw builtin is not a deterministic capability.
    for value in (first, second, {"nested": first}):
        with pytest.raises(SubstrateError, match="plain data"):
            plain_text(value)
    assert plain_text(42) == "42"
    assert plain_text({"values": [1, 2]}) == "{'values': [1, 2]}"
