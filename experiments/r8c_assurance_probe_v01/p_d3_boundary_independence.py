from __future__ import annotations

import argparse
import ast
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HARNESS_PATHS = [
    "experiments/r8c_assurance_probe_v01/README.md",
    "experiments/r8c_assurance_probe_v01/p_d3_boundary_independence.py",
]
PRODUCT_PREFIX = "src/ads_system/"
JW1_PREFIX = "tools/project_knowledge/"
PRODUCT_FORBIDDEN = ("tools", "project", "ads_project_system")
JW1_FORBIDDEN = ("ads_system", "project.engineering", "tests", "scripts")


class ProbeFailure(RuntimeError):
    pass


def git_bytes(*args: str) -> bytes:
    cp = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, check=False)
    if cp.returncode:
        raise ProbeFailure(
            "git failed: " + " ".join(args) + "\n"
            + cp.stderr.decode("utf-8", errors="replace")
        )
    return cp.stdout


def blob(commit: str, path: str) -> bytes:
    return git_bytes("show", f"{commit}:{path}")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def harness_binding(commit: str) -> dict[str, object]:
    return {
        "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT",
        "commit": commit,
        "files": {path: sha256(blob(commit, path)) for path in HARNESS_PATHS},
    }


def py_paths(commit: str, prefix: str) -> list[str]:
    raw = git_bytes("ls-tree", "-r", "--name-only", commit, "--", prefix)
    return [line for line in raw.decode().splitlines() if line.endswith(".py")]


def absolute_imports(source: bytes, path: str) -> list[str]:
    tree = ast.parse(source.decode("utf-8"), filename=path)
    result: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            result.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            result.append(node.module)
    return result


def forbidden(name: str, prefixes: tuple[str, ...]) -> bool:
    return any(name == p or name.startswith(p + ".") for p in prefixes)


def scan(commit: str, prefix: str, prefixes: tuple[str, ...]) -> dict[str, object]:
    paths = py_paths(commit, prefix)
    violations: list[dict[str, str]] = []
    for path in paths:
        for name in absolute_imports(blob(commit, path), path):
            if forbidden(name, prefixes):
                violations.append({"path": path, "import": name})
    return {
        "prefix": prefix,
        "file_count": len(paths),
        "forbidden_prefixes": list(prefixes),
        "violations": violations,
    }


def write_blob(commit: str, source: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(blob(commit, source))


def run_child(
    sys_path: Path,
    code: str,
    *,
    should_pass: bool,
    error_token: str | None = None,
) -> dict[str, object]:
    wrapped = f"import sys\nsys.path.insert(0, {str(sys_path)!r})\n" + code
    cp = subprocess.run(
        [sys.executable, "-I", "-S", "-c", wrapped],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    passed = cp.returncode == 0
    if passed != should_pass:
        raise ProbeFailure(
            f"child passed={passed}, expected={should_pass}; "
            f"stdout={cp.stdout!r}; stderr={cp.stderr!r}"
        )
    if error_token is not None and error_token not in cp.stderr:
        raise ProbeFailure(
            f"negative control did not fail on {error_token!r}; stderr={cp.stderr!r}"
        )
    return {
        "returncode": cp.returncode,
        "stdout": cp.stdout.strip(),
        "stderr": cp.stderr.strip(),
    }


PRODUCT_CODE = r'''
from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningModelConfiguration,
    ReasoningRequest,
)
request = ReasoningRequest(
    run_id="p-d3",
    run_nonce="nonce",
    system_instruction="Use supplied evidence.",
    user_task="Check boundary independence.",
    project_evidence={"x": 1},
    methodological_context_payload={"schema_version": 1},
    methodological_context_sha256="a" * 64,
    knowledge_revisions=(KnowledgeRevisionPointer("k", "r1"),),
    model_configuration=ReasoningModelConfiguration(
        requested_model="fixture",
        reasoning_effort="medium",
        verbosity="low",
        max_output_tokens=100,
    ),
)
assert len(request.semantic_digest()) == 64
assert request.canonical_model_input()
print("PRODUCT_BEHAVIOR=PASS")
'''

CURRENT_JW1_CODE = r'''
from tools.project_knowledge.identity import build_identity_index, resolve_identity
from tools.project_knowledge.model import (
    AuthorityClass, GovernedSource, Profile, RawDeclaration,
    SemanticId, SnapshotMode,
)
source = GovernedSource(
    carrier_path="project/knowledge/evidence/example.md",
    profile=Profile.SEMANTIC_SOURCE,
    authority_class=AuthorityClass.CANONICAL,
    kind="fixture",
    declaration=RawDeclaration({
        "schema_version": "1",
        "profile": "semantic_source.v1",
        "kind": "fixture",
        "authority_class": "canonical",
        "semantic_id": "Fixture",
    }),
    snapshot_mode=SnapshotMode.WORKTREE_SNAPSHOT,
    semantic_id=SemanticId("Fixture"),
)
index = build_identity_index([source], snapshot_mode=SnapshotMode.WORKTREE_SNAPSHOT)
row = resolve_identity(index, SemanticId("Fixture"))
assert tuple(item.value for item in row.current_targets) == ("Fixture",)
print("JW1_BEHAVIOR=PASS")
'''
TARGET_JW1_CODE = CURRENT_JW1_CODE.replace(
    "tools.project_knowledge", "ads_project_system"
)


def current_product(commit: str, root: Path) -> Path:
    src = root / "src"
    write_blob(commit, "src/ads_system/__init__.py", src / "ads_system/__init__.py")
    app = src / "ads_system/application"
    app.mkdir(parents=True, exist_ok=True)
    (app / "__init__.py").write_text("", encoding="utf-8")
    write_blob(
        commit,
        "src/ads_system/application/reasoning.py",
        app / "reasoning.py",
    )
    return src


def current_jw1(commit: str, root: Path) -> Path:
    tools = root / "tools"
    tools.mkdir(parents=True, exist_ok=True)
    (tools / "__init__.py").write_text("", encoding="utf-8")
    write_blob(
        commit,
        "tools/project_knowledge/__init__.py",
        root / "tools/project_knowledge/__init__.py",
    )
    write_blob(
        commit,
        "tools/project_knowledge/model.py",
        root / "tools/project_knowledge/model.py",
    )
    write_blob(
        commit,
        "tools/project_knowledge/identity.py",
        root / "tools/project_knowledge/identity.py",
    )
    return root


def target_product(commit: str, root: Path) -> Path:
    src = root / "product/runtime/src"
    write_blob(commit, "src/ads_system/__init__.py", src / "ads_system/__init__.py")
    app = src / "ads_system/application"
    app.mkdir(parents=True, exist_ok=True)
    (app / "__init__.py").write_text("", encoding="utf-8")
    write_blob(
        commit,
        "src/ads_system/application/reasoning.py",
        app / "reasoning.py",
    )
    return src


def target_jw1(commit: str, root: Path) -> Path:
    src = root / "project/system/src"
    pkg = src / "ads_project_system"
    pkg.mkdir(parents=True, exist_ok=True)
    (pkg / "__init__.py").write_text(
        '"""P-D3 target-shaped JW1 fixture."""\n',
        encoding="utf-8",
    )
    write_blob(commit, "tools/project_knowledge/model.py", pkg / "model.py")
    write_blob(commit, "tools/project_knowledge/identity.py", pkg / "identity.py")
    return src


def inject(path: Path, module: str) -> None:
    path.write_text(
        path.read_text(encoding="utf-8") + f"\nimport {module}\n",
        encoding="utf-8",
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--harness-commit", required=True)
    ap.add_argument("--source-commit", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    output = Path(args.output)
    if not output.is_absolute():
        output = ROOT / output
    output.parent.mkdir(parents=True, exist_ok=True)

    product_scan = scan(args.source_commit, PRODUCT_PREFIX, PRODUCT_FORBIDDEN)
    jw1_scan = scan(args.source_commit, JW1_PREFIX, JW1_FORBIDDEN)

    current_runtime: dict[str, object] = {}
    target_runtime: dict[str, object] = {}
    controls: dict[str, object] = {}

    with tempfile.TemporaryDirectory(prefix="p-d3-current-product-") as d:
        current_runtime["product_without_project"] = run_child(
            current_product(args.source_commit, Path(d)),
            PRODUCT_CODE,
            should_pass=True,
        )

    with tempfile.TemporaryDirectory(prefix="p-d3-current-jw1-") as d:
        current_runtime["jw1_without_engineering"] = run_child(
            current_jw1(args.source_commit, Path(d)),
            CURRENT_JW1_CODE,
            should_pass=True,
        )

    with tempfile.TemporaryDirectory(prefix="p-d3-target-product-") as d:
        path = target_product(args.source_commit, Path(d))
        target_runtime["product_runtime"] = run_child(
            path, PRODUCT_CODE, should_pass=True
        )
        inject(path / "ads_system/application/reasoning.py", "ads_project_system")
        controls["product_forbidden_dependency"] = run_child(
            path,
            PRODUCT_CODE,
            should_pass=False,
            error_token="ads_project_system",
        )

    with tempfile.TemporaryDirectory(prefix="p-d3-target-jw1-") as d:
        path = target_jw1(args.source_commit, Path(d))
        target_runtime["jw1_system"] = run_child(
            path, TARGET_JW1_CODE, should_pass=True
        )
        inject(path / "ads_project_system/identity.py", "ads_system")
        controls["jw1_forbidden_dependency"] = run_child(
            path,
            TARGET_JW1_CODE,
            should_pass=False,
            error_token="ads_system",
        )

    current_clean = not product_scan["violations"] and not jw1_scan["violations"]
    target_ok = all(item["returncode"] == 0 for item in target_runtime.values())
    controls_ok = all(item["returncode"] != 0 for item in controls.values())

    if not target_ok or not controls_ok:
        result = "HARNESS_INVALID"
    elif current_clean:
        result = "PASS"
    else:
        result = "CURRENT_DEBT_ONLY"

    payload = {
        "probe": "P-D3",
        "protocol": "Research 277",
        "candidate": "WARRANT-F V0.2",
        "result": result,
        "harness_binding": harness_binding(args.harness_commit),
        "source_binding": {
            "commit": args.source_commit,
            "product_prefix": PRODUCT_PREFIX,
            "jw1_prefix": JW1_PREFIX,
        },
        "layer_a_current_observation": {
            "static_product": product_scan,
            "static_jw1": jw1_scan,
            "runtime": current_runtime,
        },
        "layer_b_target_shaped_fixture": {
            "runtime": target_runtime,
            "forbidden_dependency_controls": controls,
        },
        "assertions": {
            "current_static_import_boundaries_clean": current_clean,
            "target_shaped_runtime_succeeds": target_ok,
            "forbidden_dependency_injections_detected": controls_ok,
        },
        "scope_limits": [
            "Representative Product behavior is the provider-neutral reasoning request contract.",
            "Representative JW1 behavior is identity-index construction and resolution.",
            "Static scan covers explicit absolute Python imports at the frozen source commit.",
            "The probe establishes boundary realizability, not exhaustive production readiness.",
        ],
        "interpretation": {
            "target_architecture_amendment_required": False,
            "current_layout_debt_observed": result == "CURRENT_DEBT_ONLY",
            "physical_migration_authorized": False,
        },
    }
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "probe": "P-D3",
        "result": result,
        "product_files_scanned": product_scan["file_count"],
        "jw1_files_scanned": jw1_scan["file_count"],
        "product_import_violations": len(product_scan["violations"]),
        "jw1_import_violations": len(jw1_scan["violations"]),
    }, indent=2))
    return 0 if result in {"PASS", "CURRENT_DEBT_ONLY"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
