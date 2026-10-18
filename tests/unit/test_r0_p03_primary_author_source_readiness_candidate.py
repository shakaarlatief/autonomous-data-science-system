"""Synthetic source-readiness window: independent of real scored source/gold."""
from __future__ import annotations

import hashlib
from pathlib import Path
import subprocess
import tempfile
import zipfile

from experiments.r0_p03_navigation_probe import primary_author_source_readiness_candidate as readiness


def git(repo, *argv):
    return subprocess.check_output(["git", *argv], cwd=repo, stderr=subprocess.STDOUT).decode().strip()


def test_primary_source_window_exact_pin_and_exclusions():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        repo = root / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "config", "user.name", "Synthetic Source")
        git(repo, "config", "user.email", "synthetic@example.invalid")
        content = {
            "README.md": "# root orientation\n",
            "docs/README.md": "# documents\n",
            "docs/CONTINUITY.md": "# operational reconstruction\n",
            "docs/CURRENT_STATE.md": "R0-P03 comparison: hidden design\n",
            "docs/KNOWLEDGE_MAP.md": "Research 513: hidden design\n",
            "docs/DECISIONS.md": "# evidence\n",
            "docs/current_routing.json": '{"current_checkpoint": 895}\n',
            "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md": "# governing\n",
            "src/ads_system/feature.py": "state = 'source'\n",
            "docs/research/513_r0_p03.md": "SCORED DESIGN\n",
        }
        for path, value in content.items():
            p = repo / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(value, encoding="utf-8")
        git(repo, "add", ".")
        git(repo, "commit", "-qm", "source world")
        pin = git(repo, "rev-parse", "HEAD")
        output = root / "packet"
        receipt = readiness.build(repo, pin=pin, root_override=output)
        assert receipt["source_count"] == 7
        readiness.build(repo, pin=pin, root_override=output, verify_only=True)
        packet = output / readiness.NAME
        with zipfile.ZipFile(packet) as z:
            names = z.namelist()
            assert len(names) == 9
            assert z.testzip() is None
            for name in readiness.ADDITIONS:
                assert "sources/" + name in names
            for name in readiness.WITHHELD:
                assert "sources/" + name not in names
            assert not any("/research/" in name for name in names)
        (repo / "docs/CONTINUITY.md").write_text("MUTATED\n")
        readiness.build(repo, pin=pin, root_override=output, verify_only=True)
        tampered = packet.read_bytes()
        packet.write_bytes(tampered+b"tamper")
        try:
            readiness.build(repo, pin=pin, root_override=output, verify_only=True)
            raise AssertionError("Tamper not detected")
        except ValueError:
            pass


def test_explicit_design_leak_in_addition_fails_closed():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        repo = root / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "config", "user.name", "Synthetic Source")
        git(repo, "config", "user.email", "synthetic@example.invalid")
        content = {
            "README.md": "R0-P03 comparator leakage",
            "docs/README.md": "# docs",
            "docs/CONTINUITY.md": "# continuity",
            "docs/DECISIONS.md": "# decisions",
            "docs/current_routing.json": "{}",
            "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md": "# spec",
        }
        for path, value in content.items():
            p=repo/path;p.parent.mkdir(parents=True, exist_ok=True);p.write_text(value)
        git(repo, "add", ".")
        git(repo, "commit", "-qm", "leaky source")
        pin=git(repo, "rev-parse", "HEAD")
        try:
            readiness.source_window(repo, pin=pin)
            raise AssertionError("Leaking source admitted")
        except ValueError as error:
            assert "Unsafe added source" in str(error)
