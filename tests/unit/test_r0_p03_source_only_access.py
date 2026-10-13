"""API-boundary tests only: no model, OS/network isolation or gold custody claim."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

from experiments.r0_p03_navigation_probe.source_only_access_candidate import (
    CONTENT_DIGEST, HISTORICAL_REF, MAX_RESULTS, MAX_TEXT,
    SourceAccessError, SourceOnlyAccess,
)
import experiments.r0_p03_navigation_probe.source_only_access_candidate as access_module
from experiments.r0_p03_navigation_probe.source_only_capsule_candidate import export_source_capsule

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def verified(tmp_path_factory):
    capsule = tmp_path_factory.mktemp("access") / "capsule"
    export_source_capsule(ROOT, capsule)
    return capsule, SourceOnlyAccess(capsule)


def all_sources(access):
    result, offset = [], 0
    while offset is not None:
        page = access.request("list", offset=offset)
        assert page["ok"]
        result.extend(page["sources"])
        offset = page["next_offset"]
    return result


def test_exact_identity_and_paged_read_reconstruct_all_git_bytes(verified):
    capsule, access = verified
    sources = all_sources(access)
    assert len(sources) == 65
    assert [r["path"] for r in sources] == sorted(r["path"] for r in sources)
    commitments, total = [], 0
    for source in sources:
        name = source["path"]
        expected = subprocess.run(["git", "show", f"{HISTORICAL_REF}:{name}"],
                                  cwd=ROOT, check=True, capture_output=True).stdout
        chunks, start = [], 1
        while True:
            page = access.request("read", path=name, start_line=start, max_lines=1)
            assert page["ok"]
            assert page["source_blob_oid"] == source["source_blob_oid"]
            chunks.append(page["text"])
            if page["end_line"] >= page["total_lines"]:
                break
            start = page["end_line"] + 1
        saved = "".join(chunks).encode("utf-8")
        assert saved == expected == (capsule / "sources" / name).read_bytes()
        digest = hashlib.sha256(saved).hexdigest()
        assert digest == source["sha256"]
        commitments.append(f"{name}\0{digest}\n")
        total += len(saved)
    assert total == 1_725_920
    assert hashlib.sha256("".join(commitments).encode()).hexdigest() == CONTENT_DIGEST


@pytest.mark.parametrize("path", [
    "../reviewer_intake.json", "/etc/passwd", "C:/Windows/win.ini", "C:outside",
    "docs//CURRENT_STATE.md", "docs/./CURRENT_STATE.md", "docs\\CURRENT_STATE.md",
    ".git/HEAD", "docs/.GIT/config", "reviewer_intake.json", "capsule_integrity.json",
    "experiments/project_knowledge_subject_navigation_t1_v02/corpus_annotations_v02.json",
    "experiments/project_knowledge_subject_navigation_t1_v02/navigation_scenarios_v02.json",
    "docs/research/562_r0_p03_source_only_capsule_and_reviewer_execution_readiness.md",
    "docs/research/559_r0_p03_claude_critique_reconciliation_and_owner_accepted_legacy_gold_amendment.md",
    "docs/model_collaboration/threads/MC-0030/STATE.json", "https://example.com", None,
])
def test_unauthorized_paths_are_uniformly_denied(verified, path):
    _, access = verified
    assert access.request("read", path=path) == {"ok": False, "error": "SOURCE_NOT_ALLOWED"}


@pytest.mark.parametrize("operation,params", [
    ("shell", {"command": "git show HEAD"}), ("write", {"path": "answer.json"}),
    ("read", {"path": "docs/DECISIONS.md", "repository": str(ROOT)}),
    ("list", {"root": str(ROOT)}), ("search", {"query": "x", "regex": True}),
    ("__getattribute__", {"name": "_sources"}),
])
def test_no_ambient_capabilities_or_extra_parameters(verified, operation, params):
    _, access = verified
    assert access.request(operation, **params) == {
        "ok": False, "error": "OPERATION_OR_PARAMETERS_NOT_ALLOWED"}


@pytest.mark.parametrize("operation,params,code", [
    ("list", {"limit": 21}, "INVALID_RANGE"), ("list", {"offset": -1}, "INVALID_RANGE"),
    ("list", {"limit": True}, "INVALID_RANGE"), ("list", {"offset": 66}, "INVALID_RANGE"),
    ("search", {"query": ""}, "INVALID_QUERY"),
    ("search", {"query": " "}, "INVALID_QUERY"),
    ("search", {"query": "x" * 129}, "INVALID_QUERY"),
    ("search", {"query": "x", "limit": 0}, "INVALID_RANGE"),
])
def test_request_budgets_fail_deterministically(verified, operation, params, code):
    _, access = verified
    assert access.request(operation, **params) == {"ok": False, "error": code}


def test_literal_search_is_bounded_source_cited_and_repeatable(verified):
    _, access = verified
    result = access.request("search", query="the", limit=3)
    assert result == access.request("search", query="the", limit=3)
    assert result["ok"] and len(result["hits"]) == 3 and result["truncated"]
    for hit in result["hits"]:
        line = access.request("read", path=hit["path"], start_line=hit["line"], max_lines=1)
        assert hit["snippet"] in line["text"] and len(hit["snippet"]) <= 160
        assert hit["historical_source_ref"] == HISTORICAL_REF
    assert access.request("search", query="[.*]")["hits"] == []
    assert len(access.request("list")["sources"]) <= MAX_RESULTS
    assert access.request("list")["scope"] == "SOURCE_API_ONLY_NOT_EXECUTION_ISOLATION"


def test_reads_are_bounded_and_returned_objects_cannot_mutate_snapshot(verified):
    _, access = verified
    source = access.request("list")["sources"][0]
    original = access.request("read", path=source["path"], max_lines=1)
    assert len(original["text"]) <= MAX_TEXT
    original["text"] = "changed"
    source["path"] = "../outside"
    assert access.request("list")["sources"][0]["path"] != "../outside"
    name = access.request("list")["sources"][0]["path"]
    assert access.request("read", path=name, max_lines=1)["text"] != "changed"
    assert access.request("read", path=name, max_lines=101)["error"] == "INVALID_RANGE"
    assert access.request("read", path=name, start_line=0)["error"] == "INVALID_RANGE"


def copy_capsule(verified, tmp_path):
    capsule, _ = verified
    target = tmp_path / "copy"
    shutil.copytree(capsule, target)
    return target


@pytest.mark.parametrize("mutation", ["changed", "missing", "extra", "git", "receipt"])
def test_corrupt_or_extended_capsules_fail_closed(verified, tmp_path, mutation):
    target = copy_capsule(verified, tmp_path)
    name = all_sources(verified[1])[0]["path"]
    source = target / "sources" / name
    if mutation == "changed":
        source.write_bytes(source.read_bytes() + b"x")
    elif mutation == "missing":
        source.unlink()
    elif mutation == "extra":
        (target / "sources" / "unauthorized.md").write_text("forbidden")
    elif mutation == "git":
        (target / ".git").mkdir()
    else:
        (target / "capsule_integrity.json").unlink()
    with pytest.raises(SourceAccessError):
        SourceOnlyAccess(target)


def test_symlink_or_junction_source_is_rejected(verified, tmp_path):
    original, _ = verified
    target = tmp_path / "linked"
    target.mkdir()
    for name in ("reviewer_intake.json", "capsule_integrity.json"):
        shutil.copy2(original / name, target / name)
    (target / "sources").mkdir()
    docs = target / "sources" / "docs"
    if os.name == "nt":
        subprocess.run(["cmd.exe", "/d", "/c", "mklink", "/J", str(docs),
                        str(original / "sources" / "docs")],
                       check=True, capture_output=True)
    else:
        docs.symlink_to(original / "sources" / "docs", target_is_directory=True)
    with pytest.raises(SourceAccessError, match="LINK_FORBIDDEN"):
        SourceOnlyAccess(target)


def test_post_initialization_disk_mutation_cannot_expand_or_change_api(verified, tmp_path):
    target = copy_capsule(verified, tmp_path)
    access = SourceOnlyAccess(target)
    name = all_sources(access)[0]["path"]
    before = access.request("read", path=name, max_lines=1)
    (target / "sources" / name).write_bytes(b"replacement")
    (target / "sources" / "gold.json").write_text("not an answer")
    assert access.request("read", path=name, max_lines=1) == before
    assert access.request("read", path="gold.json")["error"] == "SOURCE_NOT_ALLOWED"


def test_manifest_replacement_cannot_change_trusted_roster(verified, tmp_path, monkeypatch):
    changed = json.loads(access_module.MANIFEST.read_bytes())
    changed["corpus"][0]["source_path"] = "../outside"
    manifest = tmp_path / "manifest.json"
    manifest.write_text(json.dumps(changed), encoding="utf-8")
    monkeypatch.setattr(access_module, "MANIFEST", manifest)
    with pytest.raises(SourceAccessError, match="TRUSTED_MANIFEST_MISMATCH"):
        SourceOnlyAccess(verified[0])


def test_actual_large_excerpt_hits_text_budget(verified):
    capsule, access = verified
    for source in all_sources(access):
        lines = (capsule / "sources" / source["path"]).read_text("utf-8").splitlines(keepends=True)
        for start in range(0, len(lines), 100):
            if len("".join(lines[start:start + 100])) > MAX_TEXT:
                assert access.request("read", path=source["path"], start_line=start + 1,
                                      max_lines=100) == {"ok": False, "error": "READ_OUTPUT_LIMIT"}
                return
    pytest.fail("Historical corpus no longer exercises the large-excerpt output budget")
