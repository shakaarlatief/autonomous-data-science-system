"""Synthetic-only exact-source-capsule checks for the private owner handoff.

No confidential need file or real 76-kB adjudication report is read.
Only test-created fake request path lists (not scored tasks) are exercised.
The owner alone runs the real request exporter in their ordinary PowerShell.
"""
from __future__ import annotations

from hashlib import sha256
from functools import lru_cache
from io import BytesIO
import json
from pathlib import Path
from zipfile import ZipFile

import pytest

from experiments.r0_p03_navigation_probe import (
    need_adjudication_exact_source_bytes as capsule,
    primary_need_adjudication_discovery_packet as discovery,
    source_world_coverage_gate as world,
)

ROOT = Path(__file__).resolve().parents[2]
_UNPATCHED_CENSUS = world.compute


@lru_cache(maxsize=1)
def _immutable_actual_census():
    return _UNPATCHED_CENSUS(ROOT)


@pytest.fixture(autouse=True)
def _reuse_unchanged_real_git_census(monkeypatch: pytest.MonkeyPatch) -> None:
    # Costly full 2,539-file census must not be repeated for every intentionally
    # malformed input. Production exporter still computes the real census.
    def cached(repo: Path):
        if Path(repo).resolve() == ROOT.resolve():
            return _immutable_actual_census()
        return _UNPATCHED_CENSUS(repo)

    monkeypatch.setattr(world, "compute", cached)


def fake_request(paths: list[str]) -> bytes:
    return capsule.canonical({
        "format": capsule.REQUEST_FORMAT,
        "source_ref": world.PIN,
        "paths": paths,
    })


def test_two_real_pinned_public_originals_export_authentic_bytes_without_tasks() -> None:
    names = sorted(["README.md", "docs/DEVELOPMENT_METHOD.md"])
    output, receipt = capsule.exact_capsule(ROOT, fake_request(names))
    assert receipt["original_file_count"] == 2
    assert receipt["origin"] == world.PIN
    assert receipt["source_admissions"] == 0
    assert receipt["protected_task_wording_accessed"] is False
    assert receipt["owner_transfer_to_independent_reviewer"] == "NOT_AUTOMATIC"
    assert receipt["archive_sha256"] == sha256(output).hexdigest()
    with ZipFile(BytesIO(output)) as z:
        assert z.testzip() is None
        assert z.namelist() == [
            "SOURCE_MANIFEST.json",
            "originals/README.md",
            "originals/docs/DEVELOPMENT_METHOD.md",
        ]
        manifest = json.loads(z.read("SOURCE_MANIFEST.json"))
        assert manifest["original_file_count"] == 2
        assert manifest["source_admissions"] == 0
        assert len(manifest["records"]) == 2
        ledger, _ = world.compute(ROOT)
        rows = {r["path"]: r for r in discovery.indexed(ledger)}
        for row in manifest["records"]:
            name = row["source_path"]
            assert name in names
            raw = z.read("originals/" + name)
            assert len(raw) == rows[name]["bytes"] == row["bytes"]
            assert sha256(raw).hexdigest() == rows[name]["sha256"] == row["sha256"]
            assert capsule.git_blob(raw) == rows[name]["git_blob_oid"] == row["git_blob_oid"]
    assert b"NEED_PROPOSALS_RESTRICTED" not in output
    assert b"NEED_SOURCE_ADJUDICATION_RESTRICTED" not in output


def test_deterministic_exact_original_byte_capsule() -> None:
    req = fake_request(["README.md"])
    first, a = capsule.exact_capsule(ROOT, req)
    second, b = capsule.exact_capsule(ROOT, req)
    assert first == second
    assert a == b
    assert len(first) < 100_000


@pytest.mark.parametrize("bad", [
    b"{}",
    b"not json",
    b'{"format":"a","format":"b","paths":["README.md"],"source_ref":"a"}',
    fake_request([]),
    fake_request(["README.md", "README.md"]),
    fake_request(["README.md", "docs/README.md"][::-1]),
    fake_request(["../secrets.md"]),
    fake_request(["README.md"] * 65),
])
def test_rejects_unqualified_request_format_duplicate_paths_and_leak_inputs(bad: bytes) -> None:
    with pytest.raises(ValueError):
        capsule.parse_request(bad)


def test_path_outside_risk_screened_index_rejected_without_fetch(monkeypatch: pytest.MonkeyPatch) -> None:
    forbidden = "docs/research/559_r0_p03_claude_critique_reconciliation_and_owner_accepted_legacy_gold_amendment.md"
    accessed = []

    def intercept(repo: Path, name: str) -> bytes:
        accessed.append(name)
        raise AssertionError("Must reject before source read")

    monkeypatch.setattr(capsule, "git_bytes", intercept)
    with pytest.raises(ValueError, match="NOT_IN_APPROVED_DISCOVERY_INDEX"):
        capsule.exact_capsule(ROOT, fake_request([forbidden]))
    assert not accessed


def test_corrupted_original_git_object_rejected_before_capsule(monkeypatch: pytest.MonkeyPatch) -> None:
    original = capsule.git_bytes

    def fake(repo: Path, name: str) -> bytes:
        return original(repo, name) + b"tamper"

    monkeypatch.setattr(capsule, "git_bytes", fake)
    with pytest.raises(ValueError, match="CONTENT_IDENTITY_FAILURE"):
        capsule.exact_capsule(ROOT, fake_request(["README.md"]))


def test_owner_request_loader_refuses_inside_public_worktree(tmp_path: Path) -> None:
    import inspect
    source = inspect.getsource(capsule)
    assert "safe_private_request_path" in source
    assert "RESTRICTED_SOURCE_REQUEST_IN_PUBLIC_REPO" in source
    assert "PRIVATE_SOURCE_CAPSULE_DESTINATION_IN_PUBLIC_REPO" in source
    assert "OWNER_SOURCE_EXACT_ORIGINAL_BYTES_EXPORT=PASS" in source
    assert "read_text()" not in source
    assert "NEED_PROPOSALS_RESTRICTED.md" not in source
    assert "NEED_SOURCE_ADJUDICATION_RESTRICTED.md" not in source
    public_fake = ROOT / ".venv" / "this-request-does-not-exist.json"
    with pytest.raises(FileNotFoundError):
        capsule.safe_private_request_path(ROOT, public_fake)
    private_fake = tmp_path / "NEED_SOURCE_BYTE_REQUEST.json"
    private_fake.write_bytes(fake_request(["README.md"]))
    # Pytest's synthetic temporary directory is inside the public worktree;
    # the real owner-only import must reject it just like any other repo path.
    with pytest.raises(ValueError, match="RESTRICTED_SOURCE_REQUEST_IN_PUBLIC_REPO"):
        capsule.safe_private_request_path(ROOT, private_fake)


def test_owner_powershell_wrapper_custody_guards() -> None:
    script = (ROOT / "scripts/r0_p03_owner_reviewed_source_bytes.ps1").read_text(encoding="utf-8")
    for marker in (
        "NON_ELEVATED_OWNER_POWERSHELL_REQUIRED",
        "REVIEWER_REQUEST_MUST_NOT_ENTER_PUBLIC_REPOSITORY",
        "OWNER_SOURCE_FOLDER_ACL_INHERITANCE_NOT_PROTECTED",
        "OWNER_SOURCE_FOLDER_UNEXPECTED_ACCESS_RULE",
        "NEED_SOURCE_BYTE_REQUEST.json",
        "NEED_SOURCE_EXACT_ORIGINAL_BYTES_RESTRICTED.zip",
        "OWNER_PRIVATE_EXACT_SOURCE_CAPSULE=PASS",
        "DO_NOT_PASTE_OWNER_PRIVATE_PATH_OR_SOURCE_REQUEST_IN_COORDINATING_CHAT=TRUE",
    ):
        assert marker in script
    assert "Remove-Item" not in script
