"""Non-scored source-only capsule checks for independent-reference readiness.

The capsule test establishes exact historical source bytes and absence of old W5
fixture/answer files in the staged contents. It does not certify that a later
reviewer cannot browse the original repository, access a model's other tools,
or know old annotations from prior exposure. Those are execution boundaries.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from contextlib import contextmanager
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe.source_only_capsule_candidate import (
    ALLOWED_TOP_LEVEL,
    _safe_relative_source_path,
    export_source_capsule,
)

ROOT = Path(__file__).resolve().parents[2]
PRIVATE_COMPANION_CONTRACT = ROOT / "docs/private_companion/README.md"


@pytest.fixture(scope="module")
def capsule(tmp_path_factory):
    root = tmp_path_factory.mktemp("source_capsule") / "review"
    proof = export_source_capsule(ROOT, root)
    return root, proof


def test_exact_historical_source_world_without_old_gold(capsule):
    root, proof = capsule
    manifest = json.loads((root / "reviewer_intake.json").read_text("utf-8"))
    assert proof["source_count"] == 65
    assert proof["theme_count"] == 9
    assert len(manifest["themes"]) == 9
    assert set(p.name for p in root.iterdir()) == ALLOWED_TOP_LEVEL
    assert not list(root.rglob(".git"))
    assert not any("project_knowledge_subject_navigation_t1_v02" in str(p)
                   for p in root.rglob("*"))
    for forbidden in ("must_retrieve", "must_not_retrieve", "candidate_subjects",
                      "preferred_subject", "gold_answers", "selected_heldout"):
        assert forbidden not in json.dumps(manifest)
    assert manifest["status"] == "SOURCE_ONLY_LEGACY_INTAKE_NOT_GOLD"


def test_byte_copies_are_from_exact_historical_commit(capsule):
    root, proof = capsule
    historical_ref = proof["historical_source_ref"]
    sources = [p for p in (root / "sources").rglob("*") if p.is_file()]
    assert len(sources) == 65
    assert all(p.is_relative_to(root / "sources") for p in sources)
    for src in sources:
        rel = src.relative_to(root / "sources").as_posix()
        expected = subprocess.run(
            ["git", "show", f"{historical_ref}:{rel}"],
            cwd=ROOT, capture_output=True, check=True,
        ).stdout
        assert src.read_bytes() == expected


def test_deterministic_source_content_commitment(tmp_path, capsule):
    root, original = capsule
    other = tmp_path / "second"
    again = export_source_capsule(ROOT, other)
    assert again == original
    assert again["source_bytes_sha256"] == original["source_bytes_sha256"]
    original_files = {p.relative_to(root): p.read_bytes()
                      for p in root.rglob("*") if p.is_file()}
    other_files = {p.relative_to(other): p.read_bytes()
                   for p in other.rglob("*") if p.is_file()}
    assert other_files == original_files


def test_content_commitment_recomputed_from_saved_bytes(capsule):
    root, proof = capsule
    sources = sorted((root / "sources").rglob("*.md"),
                     key=lambda p: p.relative_to(root / "sources").as_posix())
    assert len(sources) == 65
    packed = "".join(
        f"{p.relative_to(root / 'sources').as_posix()}\0"
        f"{hashlib.sha256(p.read_bytes()).hexdigest()}\n" for p in sources
    ).encode("utf-8")
    assert sum(p.stat().st_size for p in sources) == 1_725_920
    assert hashlib.sha256(packed).hexdigest() == proof["source_bytes_sha256"]
    assert proof["source_bytes_sha256"] == (
        "baf2b893435c1951b52814a3de897f7684890b1449bb437b46948cc868d304d3"
    )


@pytest.mark.parametrize("source_path", [
    "", ".", "docs//file.md", "docs/./file.md", "../outside",
    "C:outside", "docs/.GIT/config", "/absolute",
])
def test_noncanonical_source_paths_are_rejected(source_path):
    with pytest.raises(ValueError):
        _safe_relative_source_path(source_path)


def test_corrupted_saved_source_cannot_receive_integrity_receipt(tmp_path, monkeypatch):
    original_open = Path.open

    class CorruptWriter:
        def __init__(self, handle):
            self.handle = handle

        def write(self, content):
            return self.handle.write(content + b"\0")

    @contextmanager
    def corrupt_open(path, mode="r", *args, **kwargs):
        with original_open(path, mode, *args, **kwargs) as handle:
            yield CorruptWriter(handle) if mode == "xb" else handle

    monkeypatch.setattr(Path, "open", corrupt_open)
    destination = tmp_path / "corrupt"
    with pytest.raises(ValueError, match="Saved source byte mismatch"):
        export_source_capsule(ROOT, destination)
    assert not (destination / "capsule_integrity.json").exists()


def test_no_overwrite_existing_capsule(capsule):
    root, _ = capsule
    with pytest.raises(FileExistsError):
        export_source_capsule(ROOT, root)


def test_capsule_cannot_write_outside_gitignored_workspace(tmp_path):
    external = ROOT / "docs" / "_not_an_authorized_capsule"
    assert not external.exists()
    with pytest.raises(PermissionError):
        export_source_capsule(ROOT, external)
    assert not external.exists()


def test_scrubbed_intake_does_not_establish_evaluator_independence(capsule):
    _, proof = capsule
    assert proof["status"] == "UNFROZEN_SOURCE_CAPSULE_MECHANICS_ONLY"
    assert "not actual reviewer isolation" in " ".join(proof["limitations"])
    assert "No independent author" in " ".join(proof["limitations"])


def test_existing_private_companion_not_automatically_scoring_authority():
    contract = PRIVATE_COMPANION_CONTRACT.read_text("utf-8")
    assert "knowledge-preservation complement only" in contract
    assert "sole ADS project-development repository" in contract
    assert "not a private development fork" in contract
