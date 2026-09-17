"""Exact-Git infrastructure worker; restricted units are never imported.

Trust CPython, stdlib, jsonschema and referencing in the supported environment.
The fixed repository TCB has a checked declaration-only initialization grammar.
This is not a security sandbox or a mutable runtime object graph attestation.
"""

import ast
import __future__
import importlib.abc
import importlib.util
import inspect
import json
from pathlib import Path
import subprocess
import sys
import sysconfig

BOOTSTRAP_PATH = "tools/project_knowledge/adapters/execution.py"
TCB_FILES = (
    "tools/project_knowledge/__init__.py", "tools/project_knowledge/model.py",
    "tools/project_knowledge/views.py", "tools/project_knowledge/declaration.py",
    "tools/project_knowledge/references.py", "tools/project_knowledge/adapters/__init__.py",
    "tools/project_knowledge/adapters/execution.py", "tools/project_knowledge/adapters/pure.py",
    "tools/project_knowledge/adapters/gitio.py", "tools/project_knowledge/adapters/fsio.py",
    "tools/project_knowledge/adapters/schema.py", "tools/project_knowledge/services/__init__.py",
    "tools/project_knowledge/services/generation.py", "tools/project_knowledge/services/validation.py",
    "tools/project_knowledge/services/discovery.py",
)
RUNTIME_IMPORTS = (
    "__future__", "ast", "dataclasses", "datetime", "enum", "hashlib", "importlib.abc",
    "importlib.util", "inspect", "json", "jsonschema", "math", "pathlib", "re",
    "referencing", "subprocess", "sys", "sysconfig", "types", "typing",
)


def check_tcb_source(path, content):
    """No project calls or mutations at import time; annotations are postponed.

    Function bodies are trusted infrastructure. Initialization allows literal
    data, enum-member references, literal regexes/frozensets, inert definitions,
    and reviewed class constructors. Extension code uses the pure grammar.
    """
    if path not in TCB_FILES:
        raise ValueError("UNDECLARED_TCB_IMPLEMENTATION: " + path)
    tree = ast.parse(content, filename=path)
    module = path[:-3].replace("/", ".").removesuffix(".__init__")
    package = module if path.endswith("/__init__.py") else module.rpartition(".")[0]
    enums = set()
    protected = {"dataclass", "staticmethod", "property", "frozenset", "re", "StrEnum", "ValueError", "importlib"}
    import_identities = {"dataclass": ("dataclasses", "dataclass"), "StrEnum": ("enum", "StrEnum"),
                         "SubstrateError": ("tools.project_knowledge.model", "SubstrateError"),
                         "DiscoveryPolicy": ("tools.project_knowledge.services.discovery", "DiscoveryPolicy")}

    def value(node):
        if isinstance(node, ast.Constant):
            return
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            for element in node.elts:
                value(element)
            return
        if isinstance(node, ast.Dict):
            for element in (*node.keys, *node.values):
                value(element)
            return
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)) and isinstance(node.operand, ast.Constant):
            return
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            if node.value.id in enums or node.value.id == "re" and node.attr in {"I", "M", "S", "X", "ASCII"}:
                return
        if isinstance(node, ast.Call) and not node.keywords:
            if isinstance(node.func, ast.Name) and node.func.id == "frozenset" and len(node.args) <= 1:
                for argument in node.args:
                    value(argument)
                return
            if ast.unparse(node.func) == "re.compile" and 1 <= len(node.args) <= 2:
                if not isinstance(node.args[0], ast.Constant) or not isinstance(node.args[0].value, str):
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: regex must be literal")
                for argument in node.args:
                    value(argument)
                return
        raise ValueError("TCB_INITIALIZATION_FORBIDDEN: " + path + ":" + str(getattr(node, "lineno", 0)))

    def declarations(body, *, class_body=False, enum_body=False):
        bound = set()
        for node in body:
            if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
                continue
            if isinstance(node, ast.Pass):
                continue
            names = []
            if isinstance(node, (ast.Import, ast.ImportFrom)) and not class_body:
                if any(alias.asname for alias in node.names):
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: import aliases are outside the initialization contract")
                if isinstance(node, ast.Import):
                    modules = [alias.name for alias in node.names]
                    names = [alias.asname or alias.name.split(".")[0] for alias in node.names]
                else:
                    target = importlib.util.resolve_name("." * node.level + (node.module or ""), package) if node.level else node.module
                    modules = [target]
                    names = [alias.asname or alias.name for alias in node.names]
                    for alias in node.names:
                        local = alias.asname or alias.name
                        if local in import_identities and (target, alias.name) != import_identities[local]:
                            raise ValueError("TCB_INITIALIZATION_FORBIDDEN: constructor import substitution")
                        if local in {"property", "staticmethod", "frozenset", "re", "ValueError"}:
                            raise ValueError("TCB_INITIALIZATION_FORBIDDEN: builtin/module substitution")
                for target in modules:
                    source = target.replace(".", "/") + ".py"
                    if target not in RUNTIME_IMPORTS and source not in TCB_FILES:
                        raise ValueError("UNDECLARED_TCB_IMPORT: " + str(target))
                if "*" in names:
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: wildcard import")
                # Two importlib submodules share their package name.
                if isinstance(node, ast.Import) and all(alias.name.startswith("importlib.") and alias.asname is None for alias in node.names):
                    names = [name for name in names if name not in bound]
            elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                targets = node.targets if isinstance(node, ast.Assign) else [node.target]
                if any(not isinstance(target, ast.Name) for target in targets):
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: attribute/subscript assignment")
                names = [target.id for target in targets]
                if node.value is not None:
                    value(node.value)
            elif isinstance(node, ast.FunctionDef) and not enum_body:
                names = [node.name]
                if node.name in {"__init_subclass__", "__set_name__"}:
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: import-time hooks")
                for decorator in node.decorator_list:
                    if not class_body or not isinstance(decorator, ast.Name) or decorator.id not in {"staticmethod", "property"}:
                        raise ValueError("TCB_INITIALIZATION_FORBIDDEN: executable decorator")
                if node.type_params:
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: type parameters")
                for default in (*node.args.defaults, *(d for d in node.args.kw_defaults if d is not None)):
                    value(default)
            elif isinstance(node, ast.ClassDef) and not class_body:
                names = [node.name]
                bases = [ast.unparse(base) for base in node.bases]
                if node.keywords or node.type_params or any(base not in (
                    "StrEnum", "ValueError", "SubstrateError", "DiscoveryPolicy",
                    "importlib.abc.MetaPathFinder", "importlib.abc.Loader") for base in bases):
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: unqualified class base/metaclass")
                if node.decorator_list and [ast.unparse(d) for d in node.decorator_list] != ["dataclass(frozen=True)"]:
                    raise ValueError("TCB_INITIALIZATION_FORBIDDEN: unqualified class decorator")
                declarations(node.body, class_body=True, enum_body=bases == ["StrEnum"])
                if bases == ["StrEnum"]:
                    enums.add(node.name)
            else:
                raise ValueError("TCB_INITIALIZATION_FORBIDDEN: executable module/class statement")
            if not isinstance(node, (ast.Import, ast.ImportFrom)) and any(name in protected for name in names):
                raise ValueError("TCB_INITIALIZATION_FORBIDDEN: trusted constructor rebinding")
            if any(name in bound for name in names):
                raise ValueError("TCB_INITIALIZATION_FORBIDDEN: declaration rebinding")
            bound.update(names)
    declarations(tree.body)
    return tree


def _decoded_source(path, content):
    if path.endswith(".py"):
        return importlib.util.decode_source(content)
    if path.endswith(".schema.json"):
        return content.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    return content


def verify_checkout_implementation(blobs):
    """Check the actual importing tree, with Python/Git CRLF equivalence only."""
    from ..model import SubstrateError
    root = Path(__file__).resolve().parents[3]
    for path, blob in sorted(blobs.items()):
        try:
            matches = _decoded_source(path, (root / path).read_bytes()) == _decoded_source(path, blob)
        except (OSError, UnicodeError, SyntaxError) as error:
            raise SubstrateError("EXECUTION_IMPLEMENTATION_UNVERIFIED", path) from error
        if not matches:
            raise SubstrateError("EXECUTION_IMPLEMENTATION_MISMATCH", path)
        if path not in TCB_FILES:
            continue
        module = sys.modules.get(path[:-3].replace("/", ".").removesuffix(".__init__"))
        if module is None:
            continue
        if Path(module.__file__).resolve() != (root / path).resolve():
            raise SubstrateError("EXECUTION_IMPLEMENTATION_UNVERIFIED", path)
        compiled = compile(blob, str(root / path), "exec", dont_inherit=True)
        codes = {code.co_name: code for code in compiled.co_consts if inspect.iscode(code)}
        for name, code in codes.items():
            current = vars(module).get(name)
            if inspect.isfunction(current) and current.__code__ != code:
                raise SubstrateError("EXECUTION_IMPLEMENTATION_MISMATCH", path + ":" + name)


def execute_snapshot(request, blobs):
    from ..model import SubstrateError
    try:
        for path in TCB_FILES:
            check_tcb_source(path, blobs[path])
    except (KeyError, ValueError, SyntaxError) as error:
        raise SubstrateError("TCB_ADMISSION_FAILED", str(error)) from error
    # -S disables site/.pth startup, including editable-install execution. Only
    # the current supported environment's dependency directories are added;
    # .pth files are not evaluated. No repository path is added to sys.path.
    runtime_paths = sorted({sysconfig.get_path("purelib"), sysconfig.get_path("platlib")})
    payload = {**request, "runtime_paths": runtime_paths,
               "implementation": {path: blob.hex() for path, blob in blobs.items()}}
    transport = ("import json,sys; r=json.load(sys.stdin); sys.path.extend(r['runtime_paths']); "
                 "exec(compile(bytes.fromhex(r['implementation']['" + BOOTSTRAP_PATH + "']), "
                 "'" + BOOTSTRAP_PATH + "', 'exec')); run_snapshot_worker(r)")
    process = subprocess.run([sys.executable, "-I", "-S", "-B", "-c", transport],
                             input=json.dumps(payload).encode("utf-8"), capture_output=True, check=False)
    if process.returncode:
        raise SubstrateError("BOUND_EXECUTION_FAILED", "Bound worker failed before returning evidence")
    try:
        return json.loads(process.stdout)
    except (ValueError, UnicodeError) as error:
        raise SubstrateError("BOUND_EXECUTION_FAILED", "Bound worker returned invalid evidence") from error


class _SnapshotModules(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    """Only the finite TCB may import repository code; no plugin fallback."""
    def __init__(self, blobs, roots, paths, runtime_paths):
        self.blobs, self.sources = blobs, {}
        self.roots = tuple(Path(root).resolve() for root in roots)
        self.paths = set(paths)
        self.runtime_paths = tuple(Path(root).resolve() for root in runtime_paths)

    def find_spec(self, fullname, path=None, target=None):
        if fullname == "tools":
            return importlib.util.spec_from_loader(fullname, self, is_package=True)
        if fullname.startswith("tools."):
            source = fullname.replace(".", "/")
            package = source + "/__init__.py" in TCB_FILES
            source += "/__init__.py" if package else ".py"
            if source not in TCB_FILES or source not in self.blobs:
                raise ImportError("UNDECLARED_TCB_IMPLEMENTATION: " + fullname)
            self.sources[fullname] = source
            return importlib.util.spec_from_loader(fullname, self, is_package=package)
        tail = fullname.replace(".", "/")
        if any(p == tail + suffix or p.endswith("/src/" + tail + suffix) or p == "src/" + tail + suffix
               for p in self.paths for suffix in (".py", "/__init__.py")):
            raise ImportError("Repository packages are not implicit TCB: " + fullname)
        for finder in sys.meta_path:
            if finder is self or not hasattr(finder, "find_spec"):
                continue
            spec = finder.find_spec(fullname, path, target)
            if spec is None:
                continue
            for location in (getattr(spec, "origin", None), *(spec.submodule_search_locations or ())):
                if location in (None, "built-in", "frozen"):
                    continue
                resolved = Path(location).resolve()
                if (any(resolved.is_relative_to(root) for root in self.roots)
                        and not any(resolved.is_relative_to(root) for root in self.runtime_paths)):
                    raise ImportError("External repository import is not admitted: " + fullname)
            return spec
        return None

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        if module.__name__ == "tools":
            return
        source = self.sources[module.__name__]
        tree = check_tcb_source(source, self.blobs[source])
        module.__file__ = source
        exec(compile(tree, source, "exec", flags=__future__.annotations.compiler_flag,
                     dont_inherit=True), module.__dict__)


def run_snapshot_worker(request):
    blobs = {path: bytes.fromhex(blob) for path, blob in request["implementation"].items()}
    try:
        for path in TCB_FILES:
            check_tcb_source(path, blobs[path])
        loader = _SnapshotModules(blobs, request["repository_roots"], [entry["path"] for entry in request["entries"]], request["runtime_paths"])
        if any(name == "tools" or name.startswith("tools.") for name in sys.modules):
            raise ImportError("Repository code loaded before bound infrastructure")
        sys.meta_path.insert(0, loader)
        module = __import__("tools.project_knowledge.services.generation", fromlist=["_worker_dispatch"])
        output = module._worker_dispatch(request, blobs)
    except Exception as error:
        output = {"error": True, "diagnostics": [{"code": "BOUND_EXECUTION_FAILED", "message": str(error), "carrier_path": ""}]}
    print(json.dumps(output, ensure_ascii=True, sort_keys=True))
