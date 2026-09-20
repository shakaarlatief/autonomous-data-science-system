"""G009 adversarial domain and exact-Git service regressions; no live outputs."""

import ast
from dataclasses import FrozenInstanceError, replace
import hashlib
import json
import os
from pathlib import Path
import random
import subprocess

import pytest

from tools.project_knowledge.adapters.gitio import commit_snapshot, read_blobs, worktree_snapshot
from tools.project_knowledge.adapters.schema import SchemaValidator
from tools.project_knowledge.model import (
    AuthorityClass, RawDeclaration, RebuildabilityClass, SemanticId, SnapshotMode,
    ViewGenerator, ViewInput, ViewInputSelector, ViewSpecification, ViewFreshnessStatus,
)
from tools.project_knowledge.services.generation import generate_views, check_view_freshness
from tools.project_knowledge.services.validation import validate_repository
from tools.project_knowledge.view_definitions import PURE_UNIT_REGISTRY, source_inventory_specification
from tools.project_knowledge.views import (
    ViewValidationError, build_views as domain_build_views, deterministic_json, implementation_digest,
    manifest_freshness,
)

ROOT = Path(__file__).resolve().parents[2]
MODE = SnapshotMode.COMMIT_SNAPSHOT
IMPL = source_inventory_specification().generator.implementation_files


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def write(root, path, content):
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(content)


def declaration(sid=None, authority="canonical"):
    value = {"schema_version": "1", "profile": "semantic_source.v1", "kind": "note", "authority_class": authority}
    if sid:
        value["semantic_id"] = sid
    return deterministic_json(value)


def commit(root):
    git(root, "add", ".")
    git(root, "commit", "--quiet", "-m", "G009 isolated fixture")
    return commit_snapshot(root, "HEAD")


@pytest.fixture
def repo(tmp_path):
    git(tmp_path, "init", "--quiet")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    git(tmp_path, "config", "user.name", "G009 fixture")
    git(tmp_path, "config", "core.autocrlf", "false")
    write(tmp_path, "docs/a.json", declaration("A"))
    write(tmp_path, "docs/z.json", declaration())  # Ordinary sources need no minted ID.
    write(tmp_path, "docs/candidate.json", declaration("CANDIDATE", "candidate"))
    for path in IMPL:
        write(tmp_path, path, (ROOT / path).read_bytes())
    commit(tmp_path)
    return tmp_path


def spec(name="inventory", **changes):
    values = dict(view_id=name, view_path=f"docs/project_knowledge/generated/{name}.json",
                  manifest_path=f"docs/project_knowledge/generated/manifests/{name}.json", view_schema_version="1",
                  rebuildability_class=RebuildabilityClass.DETERMINISTIC_BYTE_REBUILD,
                  selector=ViewInputSelector(), generator=ViewGenerator("fixture_generator", "1", IMPL),
                  compute="source_inventory.v1", serialize="canonical_json.v1")
    values.update(changes)
    if callable(values["compute"]) and "compute_identity" not in changes:
        values["compute_identity"] = "test_compute.v1"
    if callable(values["serialize"]) and "serialize_identity" not in changes:
        values["serialize_identity"] = "test_serializer.v1"
    return ViewSpecification(**values)


def build_views(specifications, corpus, implementation_blobs, **options):
    # Internal builder tests resolve the same committed pure source; this is
    # dependency construction, not another compute/serialization implementation.
    from tools.project_knowledge.adapters.pure import resolve_unit
    resolved = []
    for s in specifications:
        compute_path = next((path for identity, path, *_ in PURE_UNIT_REGISTRY if identity == s.compute), None)
        if type(s.compute) is str and compute_path in implementation_blobs:
            s = replace(s, compute=resolve_unit(s.compute, PURE_UNIT_REGISTRY, implementation_blobs, {}))
        if s.serialize == "canonical_json.v1":
            s = replace(s, serialize=deterministic_json)
        resolved.append(s)
    return domain_build_views(resolved, corpus, implementation_blobs, **options)


def build(repo, specs=None, selected=None):
    return generate_views(commit_snapshot(repo, "HEAD"), specs or (spec(),), selected_view_ids=selected)


def inputs(repo):
    snapshot = commit_snapshot(repo, "HEAD")
    validation = validate_repository(snapshot)
    assert validation.ok
    entries = {e.path: e for e in snapshot.entries}
    paths = {s.carrier_path for s in validation.sources} | set(IMPL)
    blobs = read_blobs(repo, tuple(entries[p] for p in sorted(paths)))
    contents = {p: blobs[entries[p].blob_id] for p in paths}
    return tuple(ViewInput(s, contents[s.carrier_path]) for s in validation.sources), contents


def altered_manifest(result, **changes):
    return RawDeclaration({**result.manifest.fields, **changes})


def codes(result):
    return {d.code for d in result.diagnostics}


def test_repeated_full_and_selected_builds_are_identical(repo):
    specs = (spec("all"), spec("a", selector=ViewInputSelector(ordered_paths=("docs/a.json",))))
    first = build(repo, specs)
    assert build(repo, specs) == first
    assert build(repo, specs[::-1], ("all",)) == (first[1],)
    for result in first:
        assert not SchemaValidator().validate(result.manifest)
        assert result.manifest_bytes == deterministic_json(result.manifest.fields)
        assert result.manifest.fields["authority_class"] == "derived"
        assert result.manifest.fields["snapshot_status"] == "COMMITTED"
        assert b"source_commit" not in result.manifest_bytes
        assert result.view_bytes.endswith(b"\n") and b"\r\n" not in result.view_bytes
    data = json.loads(first[1].view_bytes)
    assert data["schema_version"] == "1" and data["authority_class"] == "derived"
    assert [s["source_path"] for s in data["sources"]] == ["docs/a.json", "docs/z.json"]
    assert data["sources"][1]["semantic_id"] is None


def test_irrelevant_input_and_selector_permutations_are_identical(repo):
    corpus, blobs = inputs(repo)
    original = spec(selector=ViewInputSelector(prefixes=("docs/a.json", "docs/z.json")))
    expected = build_views((original,), corpus, blobs, snapshot_mode=MODE)
    for seed in range(8):
        reordered = list(corpus)
        random.Random(seed).shuffle(reordered)
        s = replace(original, selector=replace(original.selector, prefixes=original.selector.prefixes[::-1]))
        assert build_views((s,), reordered, blobs, snapshot_mode=MODE) == expected


def test_explicit_meaningful_input_order_is_preserved(repo):
    s = spec(selector=ViewInputSelector(ordered_paths=("docs/z.json", "docs/a.json")))
    first, = build(repo, (s,))
    second, = build(repo, (replace(s, selector=ViewInputSelector(ordered_paths=("docs/a.json", "docs/z.json"))),))
    assert first.view_bytes != second.view_bytes and first.manifest_bytes != second.manifest_bytes
    assert [b["source_path"] for b in first.manifest.fields["input_bindings"]] == ["docs/z.json", "docs/a.json"]
    assert manifest_freshness(first.manifest, second).status == ViewFreshnessStatus.STALE


@pytest.mark.parametrize("change", ["bytes", "delete", "add", "identity", "authority"])
def test_changed_complete_input_bindings_are_stale(repo, change):
    before, = build(repo)
    if change == "bytes":
        write(repo, "docs/a.json", declaration("A") + b" \n")
    elif change == "delete":
        (repo / "docs/a.json").unlink()
    elif change == "add":
        write(repo, "docs/new.json", declaration("NEW"))
    elif change == "identity":
        write(repo, "docs/a.json", declaration("NEW-A"))
    else:
        write(repo, "docs/a.json", declaration("A", "candidate"))
    snapshot = commit(repo)
    result = check_view_freshness(snapshot, (spec(),), "inventory", before.manifest)
    assert result.status == ViewFreshnessStatus.STALE and "STALE_VIEW_INPUTS" in codes(result)


def test_selected_view_receives_unchanged_and_new_inputs_not_a_delta(repo):
    specs = (spec("all"), spec("other", selector=ViewInputSelector(prefixes=("elsewhere",))))
    build(repo, specs)
    write(repo, "docs/new.json", declaration("NEW"))
    commit(repo)
    selected, = build(repo, specs, ("all",))
    full = build(repo, specs)
    assert selected == next(r for r in full if r.view_id == "all")
    assert len(json.loads(selected.view_bytes)["sources"]) == 3
    assert build(repo, specs, ()) == ()


@pytest.mark.parametrize("change", ["version", "identity", "bytes", "path", "order", "list"])
def test_changed_generator_binding_is_stale(repo, change):
    original = spec()
    before, = build(repo, (original,))
    gen = original.generator
    if change == "version":
        gen = replace(gen, generator_version="2")
    elif change == "identity":
        gen = replace(gen, generator_id="different_generator")
    elif change == "bytes":
        write(repo, IMPL[1], (repo / IMPL[1]).read_bytes() + b"\n# changed implementation\n")
        commit(repo)
    elif change == "path":
        path = "tools/relocated.py"
        write(repo, path, (repo / IMPL[1]).read_bytes())
        commit(repo)
        gen = replace(gen, implementation_files=(IMPL[0], path, IMPL[2]))
    elif change == "order":
        gen = replace(gen, implementation_files=gen.implementation_files[::-1])
    else:
        gen = replace(gen, implementation_files=gen.implementation_files[:-1])
    result = check_view_freshness(commit_snapshot(repo, "HEAD"), (replace(original, generator=gen),), original.view_id, before.manifest)
    if change in {"bytes", "path", "list"}:
        assert result.status == ViewFreshnessStatus.INVALID
        assert codes(result) & {"EXECUTION_IMPLEMENTATION_MISMATCH", "INCOMPLETE_EXECUTION_BINDING",
                                "MISSING_PURE_IMPLEMENTATION"}
    else:
        assert result.status == ViewFreshnessStatus.STALE and "STALE_VIEW_GENERATOR" in codes(result)


def test_digest_uses_exact_declared_path_nul_blob_nul_framing():
    files = {"tools/\u00e9.py": b"a\r\n\x00\xff", "tools/b.py": b"b\n"}
    gen = ViewGenerator("g", "1", tuple(files))
    framed = b"tools/\xc3\xa9.py\0a\r\n\x00\xff\0tools/b.py\0b\n\0"
    assert implementation_digest(gen, files) == hashlib.sha256(framed).hexdigest()
    assert implementation_digest(replace(gen, implementation_files=tuple(reversed(files))), files) != implementation_digest(gen, files)
    normalized = {p: b.replace(b"\r\n", b"\n") for p, b in files.items()}
    assert implementation_digest(gen, normalized) != implementation_digest(gen, files)


@pytest.mark.parametrize("field,value", [
    ("authority_class", "canonical"), ("view_id", "wrong"), ("view_path", "docs/wrong.json"),
    ("view_schema_version", "2"), ("rebuildability_class", "REGENERABLE_NONAUTHORITATIVE"),
    ("freshness_basis", "mtime"), ("schema_version", "2"), ("extra_field", True),
])
def test_malformed_or_incompatible_metadata_fails_visibly(repo, field, value):
    before, = build(repo)
    result = check_view_freshness(commit_snapshot(repo, "HEAD"), (spec(),), "inventory", altered_manifest(before, **{field: value}))
    assert result.status == ViewFreshnessStatus.INVALID and result.diagnostics


@pytest.mark.parametrize("change", ["missing", "extra", "digest", "path", "identity", "order", "boundary"])
def test_tampered_manifest_bindings_and_boundary_are_stale(repo, change):
    before, = build(repo)
    bindings = [dict(b) for b in before.manifest.fields["input_bindings"]]
    if change == "missing":
        bindings.pop()
    elif change == "extra":
        bindings.append({**bindings[0], "source_path": "docs/not-selected.json"})
    elif change in {"digest", "path", "identity"}:
        field, value = {"digest": ("content_digest", "0" * 64), "path": ("source_path", "docs/wrong.json"), "identity": ("semantic_id", "WRONG")}[change]
        bindings[0][field] = value
    elif change == "order":
        bindings.reverse()
    changes = {"created_or_refreshed_boundary": "incorrect"} if change == "boundary" else {"input_bindings": bindings}
    result = check_view_freshness(commit_snapshot(repo, "HEAD"), (spec(),), "inventory", altered_manifest(before, **changes))
    assert result.status == ViewFreshnessStatus.STALE


def test_committed_inputs_ignore_checkout_mtime_and_checkout_deletion(repo):
    snapshot = commit_snapshot(repo, "HEAD")
    before, = generate_views(snapshot, (spec(),))
    write(repo, "docs/a.json", declaration("A").replace(b"\n", b"\r\n"))
    os.utime(repo / "docs/a.json", (1, 1))
    (repo / "docs/z.json").unlink()
    for path in IMPL:
        write(repo, path, b"uncommitted replacement")
    after, = generate_views(snapshot, (spec(),))
    assert before == after
    assert check_view_freshness(snapshot, (spec(),), "inventory", before.manifest).status == ViewFreshnessStatus.FRESH


def test_same_commit_binding_survives_final_commit_without_self_sha(repo):
    # A temporary preparation commit supplies exact Git blobs. The final commit
    # replaces it with changed inputs AND views together; its SHA is unknowable
    # during generation and is never an input to the manifest.
    original = git(repo, "rev-parse", "HEAD").decode().strip()
    write(repo, "docs/a.json", declaration("SAME-COMMIT"))
    commit(repo)
    before, = build(repo)
    write(repo, before.view_path, before.view_bytes)
    write(repo, before.manifest_path, before.manifest_bytes)
    git(repo, "reset", "--soft", original)
    snapshot = commit(repo)
    assert "docs/a.json" in git(repo, "diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").decode().splitlines()
    after, = generate_views(snapshot, (spec(),))
    assert before == after and snapshot.source_commit.encode() not in before.manifest_bytes
    assert check_view_freshness(snapshot, (spec(),), "inventory", before.manifest,
                                existing_view_bytes=before.view_bytes).status == ViewFreshnessStatus.FRESH
    # A stale persisted manifest must not prevent regeneration after inputs move.
    write(repo, "docs/a.json", declaration("CHANGED"))
    snapshot = commit(repo)
    assert check_view_freshness(snapshot, (spec(),), "inventory", before.manifest).status == ViewFreshnessStatus.STALE
    assert generate_views(snapshot, (spec(),))[0].view_bytes != before.view_bytes


def test_worktree_is_noncommitted_and_never_durable_freshness(repo):
    before, = build(repo)
    snapshot = worktree_snapshot(repo)
    assert snapshot.status == "NON_COMMITTED"
    with pytest.raises(ViewValidationError) as failure:
        generate_views(snapshot, (spec(),))
    assert "NON_COMMITTED_VIEW_INPUT" in codes(failure.value)
    assert check_view_freshness(snapshot, (spec(),), "inventory", before.manifest).status == ViewFreshnessStatus.UNSUPPORTED_SNAPSHOT
    local = altered_manifest(before, snapshot_mode="WORKTREE_SNAPSHOT", snapshot_status="NON_COMMITTED")
    assert check_view_freshness(commit_snapshot(repo, "HEAD"), (spec(),), "inventory", local).status == ViewFreshnessStatus.UNSUPPORTED_SNAPSHOT
    with pytest.raises(ViewValidationError):
        build_views((spec(),), (), {}, snapshot_mode=snapshot.mode)


def test_output_content_freshness_is_distinct_from_manifest_freshness(repo):
    before, = build(repo)
    assert manifest_freshness(before.manifest, before).status == ViewFreshnessStatus.FRESH
    result = manifest_freshness(before.manifest, before, existing_view_bytes=before.view_bytes + b" ")
    assert result.status == ViewFreshnessStatus.STALE and codes(result) == {"STALE_VIEW_CONTENT"}


@pytest.mark.parametrize("bad", ["own_output", "own_manifest", "other_output", "input_output", "duplicate_id", "duplicate_path", "duplicate_file", "missing_file", "protected_output"])
def test_circular_and_invalid_view_contracts_fail(repo, bad):
    a, b = spec("a"), spec("b")
    if bad in {"own_output", "own_manifest", "other_output"}:
        path = {"own_output": a.view_path, "own_manifest": a.manifest_path, "other_output": b.view_path}[bad]
        a = replace(a, generator=replace(a.generator, implementation_files=(path,)))
    elif bad == "input_output":
        a = replace(a, selector=ViewInputSelector(ordered_paths=(a.view_path,)))
    elif bad == "duplicate_id":
        b = replace(b, view_id=a.view_id)
    elif bad == "duplicate_path":
        b = replace(b, view_path=a.view_path)
    elif bad == "duplicate_file":
        a = replace(a, generator=replace(a.generator, implementation_files=(IMPL[0], IMPL[0])))
    elif bad == "missing_file":
        a = replace(a, generator=replace(a.generator, implementation_files=("tools/missing.py",)))
    else:
        a = replace(a, view_path="docs/CURRENT_STATE.md")
    with pytest.raises(ViewValidationError):
        build(repo, (a, b))


def test_input_admission_exact_revision_and_deterministic_failures(repo):
    corpus, blobs = inputs(repo)
    canonical = next(i for i in corpus if i.source.semantic_id == SemanticId("A"))
    bad = replace(canonical, content=canonical.content.replace(b"\n", b"\r\n"))
    failures = []
    for order in ((bad, *corpus), (*reversed(corpus), bad)):
        with pytest.raises(ViewValidationError) as failure:
            build_views((spec(),), order, blobs, snapshot_mode=MODE)
        failures.append(failure.value.diagnostics)
    assert failures[0] == failures[1]
    with pytest.raises(ViewValidationError):
        build_views((spec(),), (replace(canonical, source=replace(canonical.source, carrier_path=spec().view_path)),), blobs, snapshot_mode=MODE)


@pytest.mark.parametrize("serializer", [lambda value: json.dumps(value).encode(), lambda value: b"{}\r\n", lambda value: "{}\n"])
def test_noncanonical_json_serializers_are_rejected(repo, serializer):
    corpus, blobs = inputs(repo)
    with pytest.raises(ViewValidationError):
        build_views((spec(serialize=serializer),), corpus, blobs, snapshot_mode=MODE)


def test_json_serialization_preserves_unicode_and_semantic_arrays():
    assert deterministic_json({"z": [2, 1], "a": "\u00e9"}) == b'{\n  "a": "\xc3\xa9",\n  "z": [\n    2,\n    1\n  ]\n}\n'
    with pytest.raises(ValueError):
        deterministic_json({"bad": float("nan")})


def test_uppercase_json_extension_cannot_bypass_canonical_serialization(repo):
    corpus, blobs = inputs(repo)
    with pytest.raises(ViewValidationError) as failure:
        build_views((spec(view_path="docs/project_knowledge/generated/inventory.JSON", serialize=lambda _: b"{}"),),
                    corpus, blobs, snapshot_mode=MODE)
    assert "INVALID_VIEW_SERIALIZATION" in codes(failure.value)


def test_unknown_selection_and_immutable_results(repo):
    with pytest.raises(ViewValidationError):
        build(repo, selected=("unknown",))
    result, = build(repo)
    with pytest.raises(FrozenInstanceError):
        result.view_bytes = b"changed"
    with pytest.raises(TypeError):
        result.manifest.fields["view_id"] = "changed"


def test_views_l2_has_no_io_clock_dynamic_imports_or_id_minting():
    tree = ast.parse((ROOT / "tools/project_knowledge/views.py").read_text())
    forbidden = {"open", "read_text", "read_bytes", "write_text", "write_bytes", "eval", "exec", "__import__", "system", "popen", "now", "utcnow", "time", "SemanticId"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            assert {a.name for a in node.names} <= {"hashlib", "json", "re"}
        elif isinstance(node, ast.ImportFrom):
            assert (node.level == 1 and node.module == "model") or (node.level == 0 and node.module == "typing")
        elif isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else node.func.attr if isinstance(node.func, ast.Attribute) else ""
            assert name not in forbidden


def test_builtin_structural_view_has_explicit_auditable_closure(repo):
    s = source_inventory_specification()
    result, = build(repo, (s,))
    assert result.view_id == "source_inventory"
    assert tuple(result.manifest.fields["generator"]["implementation_files"]) == IMPL
    assert len(IMPL) == 27 and len(set(IMPL)) == 27
    assert result.manifest.fields["rebuildability_class"] == "DETERMINISTIC_BYTE_REBUILD"
    assert result.manifest.fields["authority_class"] == "derived"
