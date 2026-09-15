from __future__ import annotations

import hashlib
from dataclasses import replace
import json
from pathlib import Path
import subprocess
import sys

import pytest

from tools.project_knowledge.adapters.fsio import read_worktree_bytes
from tools.project_knowledge.adapters import gitio
from tools.project_knowledge.adapters.gitio import commit_snapshot, read_blob, read_blobs, worktree_snapshot
from tools.project_knowledge.declaration import BEGIN, END, parse_markdown
from tools.project_knowledge.model import DiagnosticSeverity, SnapshotEntry, SnapshotMode, SubstrateError
from tools.project_knowledge.services.discovery import DiscoveryPolicy, PathRole, open_snapshot
from tools.project_knowledge.services.validation import validate_repository, validate_revision_descriptor


ROOT = Path(__file__).resolve().parents[2]
VALUE = {"schema_version": "1", "profile": "semantic_source.v1", "kind": "note", "authority_class": "canonical"}


def carrier(value=VALUE, newline="\n"):
    return (BEGIN + newline + json.dumps(value) + newline + END + newline).encode()


def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True).stdout


def write(root, path, content):
    destination = root / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(content)


@pytest.fixture()
def repo(tmp_path):
    git(tmp_path, "init", "--quiet")
    git(tmp_path, "config", "user.email", "fixture@example.invalid")
    git(tmp_path, "config", "user.name", "Substrate fixture")
    git(tmp_path, "config", "core.autocrlf", "false")
    write(tmp_path, "docs/source.md", carrier())
    write(tmp_path, ".gitignore", b"ignored/\n")
    git(tmp_path, "add", ".")
    git(tmp_path, "commit", "--quiet", "-m", "Fixture source")
    return tmp_path


def descriptor(repo, path="docs/source.md", content=None):
    commit = git(repo, "rev-parse", "HEAD").decode().strip()
    blob = git(repo, "show", f"{commit}:{path}") if content is None else content
    return {"source_path": path, "source_commit": commit, "hash_algorithm": "sha256", "hash_basis": "GIT_BLOB_BYTES_AT_COMMIT", "content_digest": hashlib.sha256(blob).hexdigest()}


def test_g005_exact_git_blobs_survive_checkout_changes(repo):
    revision = descriptor(repo)
    write(repo, "docs/source.md", carrier(newline="\r\n"))
    assert not validate_revision_descriptor(repo, revision)
    assert validate_revision_descriptor(repo, descriptor(repo, content=carrier(newline="\r\n")))[0].code == "SOURCE_DIGEST_MISMATCH"
    snapshot = commit_snapshot(repo, "HEAD")
    source = next(e for e in snapshot.entries if e.path == "docs/source.md")
    assert read_blob(repo, source) == carrier()
    assert read_worktree_bytes(repo, source.path) == carrier(newline="\r\n")
    (repo / source.path).unlink()
    assert not validate_revision_descriptor(repo, revision)
    assert any(d.code == "SOURCE_UNAVAILABLE" for d in validate_repository(worktree_snapshot(repo)).diagnostics)


@pytest.mark.parametrize("blob", [b"a\r\nb\r\n", b"a\nb\n", b"\xef\xbb\xbfnon-normalized", b"\xff\x00\xfe"])
def test_revision_hashes_every_byte_without_decoding(repo, blob):
    write(repo, "docs/raw.bin", blob)
    git(repo, "add", "docs/raw.bin")
    git(repo, "commit", "--quiet", "-m", "Exact bytes")
    assert not validate_revision_descriptor(repo, descriptor(repo, "docs/raw.bin"))
    snapshot = commit_snapshot(repo, "HEAD")
    entry = next(e for e in snapshot.entries if e.path == "docs/raw.bin")
    assert read_blobs(repo, (entry,))[entry.blob_id] == blob


def test_batch_blob_framing_and_one_git_process(repo, monkeypatch):
    content = b"\x00\xff\r\n" + b"a" * 40 + b" blob 999\ntrailing\x00"
    write(repo, "docs/one.bin", content)
    write(repo, "docs/two.bin", content)
    write(repo, "docs/empty.bin", b"")
    git(repo, "add", ".")
    git(repo, "commit", "--quiet", "-m", "Binary batch fixtures")
    snapshot = commit_snapshot(repo, "HEAD")
    calls = []
    original = gitio._git

    def counted(root, *args, **kwargs):
        calls.append(args)
        return original(root, *args, **kwargs)

    monkeypatch.setattr(gitio, "_git", counted)
    blobs = read_blobs(repo, snapshot.entries)
    assert calls == [("cat-file", "--batch")]
    assert len(blobs) == len(snapshot.entries) - 1
    for entry in snapshot.entries:
        assert blobs[entry.blob_id] == (repo / entry.path).read_bytes()


@pytest.mark.parametrize("response", [b"missing\n", b"a" * 40 + b" blob 5\nab\n", b"a" * 40 + b" blob 0\n\ntrailing"])
def test_invalid_batch_output_fails_without_fallback(repo, monkeypatch, response):
    monkeypatch.setattr(gitio, "_git", lambda *args, **kwargs: response)
    with pytest.raises(SubstrateError) as error:
        read_blobs(repo, (SnapshotEntry("docs/file.md", "a" * 40, "100644"),))
    assert error.value.code == "GIT_READ_FAILED"


def test_modes_have_distinct_source_universes(repo):
    write(repo, "docs/new.md", carrier())
    write(repo, "ignored/hidden.md", carrier())
    committed = commit_snapshot(repo, "HEAD")
    local = worktree_snapshot(repo)
    assert "docs/new.md" not in {e.path for e in committed.entries}
    assert "docs/new.md" in {e.path for e in local.entries}
    assert "ignored/hidden.md" not in {e.path for e in local.entries}
    assert local.source_commit is None and local.status == "NON_COMMITTED"
    assert committed.source_commit and committed.status == "COMMITTED"
    result = validate_repository(local)
    assert result.ok and len(result.sources) == 2
    assert all(s.revision is None and s.semantic_id is None for s in result.sources)
    bound = validate_repository(committed, durable_evidence=True)
    assert bound.ok and bound.sources[0].revision.snapshot_mode == SnapshotMode.COMMIT_SNAPSHOT
    git(repo, "add", "docs/new.md")
    assert len([e for e in worktree_snapshot(repo).entries if e.path == "docs/new.md"]) == 1


def test_commit_snapshot_stays_at_resolved_tree_after_head_moves(repo):
    snapshot = commit_snapshot(repo, "HEAD")
    write(repo, "docs/source.md", carrier({**VALUE, "kind": "changed"}))
    git(repo, "add", "docs/source.md")
    git(repo, "commit", "--quiet", "-m", "New head")
    assert validate_repository(snapshot).sources[0].kind == "note"


@pytest.mark.parametrize("manifest_path", ["docs/local-manifest.json", "docs/project_knowledge/generated/manifests/local.json"])
def test_durable_worktree_descriptor_and_artifact_hard_fail(repo, manifest_path):
    result = validate_repository(worktree_snapshot(repo), durable_evidence=True)
    assert not result.ok and result.diagnostics[0].code == "NON_COMMITTED_EVIDENCE"
    value = descriptor(repo)
    value["snapshot_mode"] = "WORKTREE_SNAPSHOT"
    assert validate_revision_descriptor(repo, value)[0].code == "NON_COMMITTED_EVIDENCE"
    manifest = json.loads((ROOT / "tests/fixtures/project_knowledge/derived_view_manifest.valid.json").read_text())
    manifest["snapshot_mode"] = "WORKTREE_SNAPSHOT"
    manifest["snapshot_status"] = "NON_COMMITTED"
    manifest["input_bindings"] = []
    write(repo, manifest_path, json.dumps(manifest).encode())
    git(repo, "add", manifest_path)
    git(repo, "commit", "--quiet", "-m", "Worktree artifact does not become durable when committed")
    snapshot = commit_snapshot(repo, "HEAD")
    assert validate_repository(snapshot).ok
    result = validate_repository(snapshot, durable_evidence=True)
    assert not result.ok
    assert any(d.code == "NON_COMMITTED_EVIDENCE" and d.carrier_path == manifest_path for d in result.diagnostics)


@pytest.mark.parametrize("field,value,code", [
    ("source_commit", "HEAD", "INVALID_SOURCE_REVISION"),
    ("source_commit", "0" * 40, "GIT_READ_FAILED"),
    ("source_path", "docs/missing.md", "SOURCE_NOT_IN_COMMIT"),
    ("source_path", "../outside.md", "INVALID_SOURCE_REVISION"),
    ("hash_basis", "WORKTREE_BYTES", "INVALID_SOURCE_REVISION"),
    ("hash_algorithm", "sha1", "INVALID_SOURCE_REVISION"),
    ("content_digest", "A" * 64, "INVALID_SOURCE_REVISION"),
    ("snapshot_mode", "GUESS", "INVALID_SOURCE_REVISION"),
    ("extra", True, "INVALID_SOURCE_REVISION"),
])
def test_invalid_revisions_fail_visibly(repo, field, value, code):
    revision = descriptor(repo)
    revision[field] = value
    assert validate_revision_descriptor(repo, revision)[0].code == code


@pytest.mark.parametrize("path", [
    "scripts/source.md", "docs/project_knowledge/generated/view.json",
    "docs/project_knowledge/captures/open/capture.md", ".tmp/source.md",
    "docs/unexpected/fixtures/source.md", "experiments/source.md",
])
def test_excluded_but_declared_is_error(repo, path):
    write(repo, path, json.dumps(VALUE).encode() if path.endswith(".json") else carrier())
    result = validate_repository(worktree_snapshot(repo))
    assert not result.ok and result.excluded_but_declared_count == 1
    error = next(d for d in result.diagnostics if d.code == "EXCLUDED_BUT_DECLARED")
    assert error.severity == DiagnosticSeverity.ERROR and error.carrier_path == path
    assert path not in {s.carrier_path for s in result.sources}


def test_numbered_research_and_undeclared_observability(repo):
    write(repo, "docs/research/180_source.md", carrier())
    write(repo, "docs/research/181_plain.md", b"No declaration")
    write(repo, "docs/data.json", b'{"data":true}')
    write(repo, "tests/fixtures/plain.json", b'{"data":true}')
    result = validate_repository(worktree_snapshot(repo))
    assert result.ok and len(result.sources) == 2
    assert result.candidate_count == 5 and result.excluded_count == 1
    assert dict(result.undeclared_by_root) == {"docs/research": 1, "docs": 1}
    assert dict(result.path_role_counts)[PathRole.EVIDENCE_FIXTURE] == 1


def test_malformed_excluded_declaration_not_hidden(repo):
    write(repo, "experiments/bad.md", BEGIN.encode())
    result = validate_repository(worktree_snapshot(repo))
    assert {d.code for d in result.diagnostics} == {"MALFORMED_DECLARATION_MARKERS", "EXCLUDED_BUT_DECLARED"}


def test_expected_revision_orchestration(repo):
    write(repo, "docs/source.md", carrier({**VALUE, "profile": "workstream.v1", "semantic_id": "WS:1", "state": "ACTIVE", "objective": "Test", "expected_revision": {**descriptor(repo), "content_digest": "0" * 64}}))
    result = validate_repository(worktree_snapshot(repo))
    assert not result.ok and any(d.code == "SOURCE_DIGEST_MISMATCH" for d in result.diagnostics)


def test_same_commit_manifest_binds_inputs_without_self_referential_commit(repo):
    manifest = json.loads((ROOT / "tests/fixtures/project_knowledge/derived_view_manifest.valid.json").read_text())
    binding = descriptor(repo)
    del binding["source_commit"]
    manifest["input_bindings"] = [binding]
    write(repo, "docs/manifest.json", json.dumps(manifest).encode())
    git(repo, "add", "docs/manifest.json")
    git(repo, "commit", "--quiet", "-m", "Same-commit binding fixture")
    assert validate_repository(commit_snapshot(repo, "HEAD"), durable_evidence=True).ok
    write(repo, "docs/source.md", carrier({**VALUE, "kind": "changed"}))
    git(repo, "add", "docs/source.md")
    git(repo, "commit", "--quiet", "-m", "Stale input fixture")
    result = validate_repository(commit_snapshot(repo, "HEAD"), durable_evidence=True)
    assert not result.ok and any(d.code == "SOURCE_DIGEST_MISMATCH" for d in result.diagnostics)


def test_policy_has_no_blanket_research_exclusion():
    policy = DiscoveryPolicy()
    assert not policy.is_excluded("docs/research/179_mc0017_reconciled_w0_implementation_architecture.md")
    assert policy.is_excluded("docs/research/project_knowledge_baselines/results/fixture.md")
    assert policy.classify("docs/research/project_knowledge_new_domain/source.md") == PathRole.ELIGIBLE_SOURCE
    assert policy.classify("docs/research/project_knowledge_candidate_01_future/source.md") == PathRole.ELIGIBLE_SOURCE


@pytest.mark.parametrize("mode", list(SnapshotMode))
def test_evidence_fixtures_never_enter_production_discovery(repo, mode):
    write(repo, "tests/fixtures/project_knowledge/valid.json", json.dumps(VALUE).encode())
    write(repo, "tests/fixtures/project_knowledge/invalid.md", BEGIN.encode())
    write(repo, "docs/research/project_knowledge_candidate_01_shadow_v01/source.md", carrier())
    write(repo, "docs/research/project_knowledge_candidate_01_real_shadow_v01/legacy.json", b'{"profile":"old-research-format"}')
    git(repo, "add", ".")
    git(repo, "commit", "--quiet", "-m", "Non-production evidence fixtures")
    result = validate_repository(open_snapshot(repo, mode, "HEAD" if mode == SnapshotMode.COMMIT_SNAPSHOT else None))
    assert result.ok and result.diagnostics == ()
    assert [s.carrier_path for s in result.sources] == ["docs/source.md"]
    assert dict(result.path_role_counts)[PathRole.EVIDENCE_FIXTURE] == 4


@pytest.mark.parametrize("mode", list(SnapshotMode))
def test_legitimate_special_artifacts_validate_without_becoming_sources(repo, mode):
    capture = json.loads((ROOT / "tests/fixtures/project_knowledge/capture.valid.json").read_text())
    manifest = json.loads((ROOT / "tests/fixtures/project_knowledge/derived_view_manifest.valid.json").read_text())
    manifest["input_bindings"] = [descriptor(repo)]
    write(repo, "docs/project_knowledge/captures/open/observation.md", carrier(capture))
    write(repo, "docs/project_knowledge/captures/historical/observation.json", json.dumps(capture).encode())
    write(repo, "docs/project_knowledge/generated/manifests/catalog.json", json.dumps(manifest).encode())
    write(repo, "docs/project_knowledge/generated/catalog.json", b'{"sources":[]}')
    git(repo, "add", ".")
    git(repo, "commit", "--quiet", "-m", "Non-canonical governed artifacts")
    result = validate_repository(open_snapshot(repo, mode, "HEAD" if mode == SnapshotMode.COMMIT_SNAPSHOT else None))
    assert result.ok and result.excluded_but_declared_count == 0
    assert [s.carrier_path for s in result.sources] == ["docs/source.md"]
    assert result.noncanonical_declaration_count == 3
    assert dict(result.path_role_counts)[PathRole.CAPTURE_AREA] == 2
    assert dict(result.path_role_counts)[PathRole.GENERATED_AREA] == 2


def test_special_artifacts_do_not_bypass_schema_validation(repo):
    write(repo, "docs/project_knowledge/captures/open/invalid.json", json.dumps({**VALUE, "profile": "capture.v1"}).encode())
    result = validate_repository(worktree_snapshot(repo))
    assert not result.ok and any(d.code == "PROFILE_SCHEMA_VIOLATION" for d in result.diagnostics)
    assert len(result.sources) == 1 and result.noncanonical_declaration_count == 0


def test_misplaced_capture_and_manifest_profiles_fail(repo):
    capture = json.loads((ROOT / "tests/fixtures/project_knowledge/capture.valid.json").read_text())
    manifest = json.loads((ROOT / "tests/fixtures/project_knowledge/derived_view_manifest.valid.json").read_text())
    write(repo, "docs/project_knowledge/captures/open/manifest.json", json.dumps(manifest).encode())
    write(repo, "docs/project_knowledge/generated/manifests/capture.json", json.dumps(capture).encode())
    write(repo, "docs/project_knowledge/generated/misplaced-manifest.json", json.dumps(manifest).encode())
    result = validate_repository(worktree_snapshot(repo))
    assert not result.ok and result.excluded_but_declared_count == 3
    assert all(d.severity == DiagnosticSeverity.ERROR for d in result.diagnostics)


@pytest.mark.parametrize("mode", list(SnapshotMode))
def test_actual_ads_documentation_and_fixture_discovery_integration(mode):
    """Bounded real carriers, not synthetic copies or filename exceptions in production."""
    policy = DiscoveryPolicy()
    documents = {
        "docs/research/177_selected_candidate_physical_architecture_and_repository_contract_v01.md",
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md",
    }
    snapshot = open_snapshot(ROOT, mode, "HEAD" if mode == SnapshotMode.COMMIT_SNAPSHOT else None)
    selected = tuple(e for e in snapshot.entries if e.path in documents or
                     e.path.startswith("tests/fixtures/project_knowledge/") or
                     e.path.startswith("docs/research/project_knowledge_candidate_01_shadow_v01/"))
    assert documents <= {e.path for e in selected}
    assert any(e.path.startswith("docs/research/project_knowledge_candidate_01_shadow_v01/") for e in selected)
    if mode == SnapshotMode.WORKTREE_SNAPSHOT:
        assert any(e.path.startswith("tests/fixtures/project_knowledge/") for e in selected)
    result = validate_repository(replace(snapshot, entries=selected))
    assert result.ok, result.diagnostics
    assert result.sources == () and result.excluded_but_declared_count == 0
    assert dict(result.path_role_counts)[PathRole.EVIDENCE_FIXTURE] > 0
    for path in documents:
        assert policy.classify(path) == PathRole.ELIGIBLE_SOURCE
        assert parse_markdown((ROOT / path).read_bytes()) is None


def test_snapshot_ref_is_explicit(repo):
    with pytest.raises(ValueError):
        open_snapshot(repo, SnapshotMode.COMMIT_SNAPSHOT)
    with pytest.raises(ValueError):
        open_snapshot(repo, SnapshotMode.WORKTREE_SNAPSHOT, "HEAD")


def test_cli_is_read_only_deterministic_and_fail_nonzero(repo):
    command = [sys.executable, "-m", "tools.project_knowledge", "validate", "--root", str(repo), "--snapshot-mode", "COMMIT_SNAPSHOT", "--ref", "HEAD"]
    before = git(repo, "status", "--porcelain")
    first = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    second = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    assert first.returncode == 0, first.stderr + first.stdout
    assert first.stdout == second.stdout and json.loads(first.stdout)["ok"]
    assert git(repo, "status", "--porcelain") == before
    write(repo, "docs/bad.md", BEGIN.encode())
    local = command[:-4] + ["--snapshot-mode", "WORKTREE_SNAPSHOT"]
    failed = subprocess.run(local, cwd=ROOT, capture_output=True, text=True)
    assert failed.returncode == 1 and not json.loads(failed.stdout)["ok"]
    invalid = subprocess.run(command[:-4], cwd=ROOT, capture_output=True)
    assert invalid.returncode == 2


def test_symlink_blob_never_followed(repo):
    # Index plumbing is portable even where Windows denies symlink creation.
    oid = subprocess.run(["git", "-C", str(repo), "hash-object", "-w", "--stdin"], input=b"../../outside.md", check=True, capture_output=True).stdout.decode().strip()
    git(repo, "update-index", "--add", "--cacheinfo", f"120000,{oid},docs/link.md")
    git(repo, "commit", "--quiet", "-m", "Symlink fixture")
    result = validate_repository(commit_snapshot(repo, "HEAD"))
    assert not result.ok and any(d.code == "UNSUPPORTED_SOURCE_MODE" for d in result.diagnostics)


@pytest.mark.parametrize("path", ["../escape", "/absolute", "docs/../escape", "C:/escape", "docs\\escape"])
def test_worktree_path_escape_rejected(repo, path):
    with pytest.raises(ValueError):
        read_worktree_bytes(repo, path)
