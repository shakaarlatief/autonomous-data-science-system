"""Restricted pure-unit compiler, not a security sandbox for arbitrary Python.

Only declared functions are compiled, never their containing module. The source
language has local control flow and JSON data expressions, direct declared
helper/capability calls, and no attribute access, imports or reflection. Inputs
and outputs cross an exact-type data boundary. CPython and the installed stdlib
are trusted; arbitrary repository initialization is not a capability.
"""

import ast
import math
from types import FunctionType, MappingProxyType

from ..model import SubstrateError


def reject(code, message):
    raise SubstrateError(code, message)


def plain(value, *, freeze=False):
    """No domain instances, subclasses, descriptors or executable data cross."""
    if value is None or type(value) in (str, bool, int, bytes):
        return value
    if type(value) is float and math.isfinite(value):
        return value
    if type(value) in (dict, MappingProxyType):
        if any(type(key) is not str for key in value):
            reject("INVALID_PURE_DATA", "Pure mappings require string keys")
        copied = {key: plain(item, freeze=freeze) for key, item in value.items()}
        return MappingProxyType(copied) if freeze else copied
    if type(value) in (list, tuple):
        copied = [plain(item, freeze=freeze) for item in value]
        return tuple(copied) if freeze else copied
    reject("INVALID_PURE_DATA", "Pure values must be finite plain data, never repository/runtime objects")


def plain_text(value):
    """Never stringify runtime objects, whose repr can contain memory addresses."""
    return str(plain(value))


def source_functions(content, path):
    try:
        tree = ast.parse(content, filename=path)
    except (SyntaxError, ValueError) as error:
        reject("INVALID_PURE_SOURCE", str(error))
    functions = {}
    for node in tree.body:
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and isinstance(node.value.value, str):
            continue
        if not isinstance(node, ast.FunctionDef) or node.name in functions:
            reject("PURE_MODULE_INITIALIZATION_FORBIDDEN", "Pure modules contain only unique function declarations and docstrings")
        functions[node.name] = node
    return functions


def check_function(node, dependencies):
    args = node.args
    if args.defaults:
        reject("PURE_DEFAULTS_FORBIDDEN", "Pure units have no positional defaults")
    if any(value is not None for value in args.kw_defaults):
        reject("PURE_KWDEFAULTS_FORBIDDEN", "Pure units have no keyword defaults")
    if (node.decorator_list or node.returns or node.type_params
            or any(arg.annotation for arg in (*args.posonlyargs, *args.args, *args.kwonlyargs))
            or args.vararg or args.kwarg):
        reject("PURE_FUNCTION_STATE_FORBIDDEN", "Pure units have no decorators, annotations, type parameters or variadic arguments")
    allowed = (ast.FunctionDef, ast.arguments, ast.arg, ast.Return, ast.Assign, ast.If,
               ast.For, ast.While, ast.Break, ast.Continue, ast.Pass, ast.Expr,
               ast.Name, ast.Constant, ast.List, ast.Tuple, ast.Dict, ast.Subscript,
               ast.Slice, ast.ListComp, ast.DictComp, ast.comprehension,
               ast.IfExp, ast.UnaryOp, ast.BinOp, ast.BoolOp, ast.Compare, ast.Call,
               ast.keyword, ast.Load, ast.Store, ast.Add, ast.Sub, ast.Mult, ast.Div,
               ast.FloorDiv, ast.Mod, ast.USub, ast.UAdd, ast.Not, ast.And, ast.Or,
               ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.In, ast.NotIn)
    locals_used = {arg.arg for arg in (*args.posonlyargs, *args.args, *args.kwonlyargs)}
    locals_used.update(n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store))
    if locals_used & set(dependencies):
        reject("PURE_BINDING_SUBSTITUTION", "Local bindings cannot replace a helper or capability")
    parents = {child: parent for parent in ast.walk(node) for child in ast.iter_child_nodes(parent)}
    reached = set()
    for part in ast.walk(node):
        if not isinstance(part, allowed) or isinstance(part, ast.FunctionDef) and part is not node:
            reject("PURE_SYNTAX_FORBIDDEN", "Pure units forbid imports, attributes, closures/generators, object identity, global/nonlocal and dynamic execution")
        if isinstance(part, ast.Subscript) and not isinstance(part.ctx, ast.Load):
            reject("PURE_MUTATION_FORBIDDEN", "Pure units cannot mutate supplied data or capabilities")
        if isinstance(part, ast.comprehension) and part.is_async:
            reject("PURE_SYNTAX_FORBIDDEN", "Async execution is outside the pure contract")
        if isinstance(part, ast.Name):
            if part.id.startswith("_"):
                reject("PURE_REFLECTION_FORBIDDEN", "Private/runtime names are outside the pure contract")
            if isinstance(part.ctx, ast.Load) and part.id not in locals_used:
                parent = parents.get(part)
                if part.id not in dependencies or not isinstance(parent, ast.Call) or parent.func is not part:
                    reject("UNQUALIFIED_PURE_BINDING", "Nonlocal names may only directly call declared helpers/capabilities")
                reached.add(part.id)
        if isinstance(part, ast.Call) and (not isinstance(part.func, ast.Name) or part.func.id not in dependencies):
            reject("PURE_CALL_FORBIDDEN", "Only direct declared helper/capability calls are permitted")
    if reached != set(dependencies):
        reject("PURE_DEPENDENCY_MISMATCH", "Pure helper/capability declarations must match source calls exactly")


UNIT_DECLARATION_PREFIX = "tools/project_knowledge/view_definitions/"


def declared_units(blobs):
    """Data-only unit records from this view's own explicit implementation blobs.

    Declaration modules are parsed, never imported or executed: each may bind one
    top-level PURE_UNITS literal. Only blobs the caller already bound are read, so
    another view's declarations cannot qualify a unit here.
    """
    records = []
    for path in sorted(blobs):
        if not (path.startswith(UNIT_DECLARATION_PREFIX) and path.endswith(".py")):
            continue
        try:
            tree = ast.parse(blobs[path], filename=path)
        except (SyntaxError, ValueError) as error:
            reject("INVALID_PURE_REGISTRY", str(error))
        nodes = [node for node in tree.body if isinstance(node, ast.Assign)
                 and any(isinstance(target, ast.Name) and target.id == "PURE_UNITS" for target in node.targets)]
        if len(nodes) > 1:
            reject("INVALID_PURE_REGISTRY", "A declaration module binds PURE_UNITS at most once")
        for node in nodes:
            try:
                declared = ast.literal_eval(node.value)
            except ValueError as error:
                reject("INVALID_PURE_REGISTRY", "PURE_UNITS must be a data literal: " + str(error))
            if type(declared) is not tuple:
                reject("INVALID_PURE_REGISTRY", "PURE_UNITS must be a tuple of unit records")
            records.extend(declared)
    return tuple(records)


def resolve_unit(unit_id, registry, blobs, capabilities):
    """Construct a closed function graph; cycles need no module initialization."""
    records = {}
    for identity, path, name, helpers, required_caps in registry:
        if identity in records:
            reject("INVALID_PURE_REGISTRY", "Pure unit identities must be unique")
        records[identity] = (path, name, helpers, required_caps)
    functions = {}

    def load(identity):
        if identity in functions:
            return functions[identity]
        if identity not in records:
            reject("UNQUALIFIED_PURE_UNIT", "Pure unit identity has no committed qualification")
        path, name, helpers, required_caps = records[identity]
        if path not in blobs:
            reject("MISSING_PURE_IMPLEMENTATION", "Pure unit source must be in this view's explicit implementation files")
        nodes = source_functions(blobs[path], path)
        if name not in nodes:
            reject("MISSING_PURE_FUNCTION", "Qualified function is absent from committed pure source")
        names = [alias for alias, _ in helpers] + list(required_caps)
        if len(names) != len(set(names)) or any(cap not in capabilities for cap in required_caps):
            reject("INVALID_PURE_CAPABILITY", "Pure dependencies must be unique explicit deterministic capabilities")
        node = nodes[name]
        check_function(node, names)
        code = compile(ast.Module(body=[node], type_ignores=[]), path, "exec", dont_inherit=True)
        function_code, = (item for item in code.co_consts if hasattr(item, "co_code"))
        environment = {"__builtins__": {}}
        function = FunctionType(function_code, environment, name)
        functions[identity] = function
        environment.update({cap: capabilities[cap] for cap in required_caps})
        for alias, dependency in helpers:
            environment[alias] = load(dependency)
        return function

    function = load(unit_id)

    def execute(value):
        try:
            return plain(function(plain(value, freeze=True)))
        except SubstrateError:
            raise
        except Exception as error:
            reject("PURE_EXECUTION_FAILED", str(error))

    return execute
