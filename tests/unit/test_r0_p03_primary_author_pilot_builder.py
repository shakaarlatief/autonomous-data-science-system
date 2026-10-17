"""Focused synthetic regression for exact-source non-scored author pilot."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

PATH = Path(__file__).parents[2] / "experiments/r0_p03_navigation_probe/primary_author_pilot_builder_candidate.py"
spec = importlib.util.spec_from_file_location("author_pilot", PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


def git(repo, *argv):
    return subprocess.check_output(["git", *argv], cwd=repo, stderr=subprocess.STDOUT).decode().strip()


def test_source_bound_unscored_rehearsal():
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        repo = root / "repo"
        repo.mkdir()
        git(repo, "init", "-q")
        git(repo, "config", "user.name", "Synthetic Pilot")
        git(repo, "config", "user.email", "pilot@example.invalid")
        files = {
            "docs/DECISIONS.md": "# decisions\n",
            "docs/current_routing.json": '{"current_checkpoint":895}\n',
            "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md": "# contract\n",
            "docs/foundations/001_foundation.md": "# foundation\n",
            "src/ads_system/component.py": "x = 1\n",
            "tools/project_knowledge/authority.py": "y = 1\n",
            "tests/unit/test_project_knowledge_authority.py": "def test_example(): pass\n",
            "docs/research/513_protocol.md": "HIDDEN DESIGN\n",
            "experiments/r0_p03_navigation_probe/gold.json": "HIDDEN GOLD\n",
            "docs/model_collaboration/threads/MC-0030/THREAD.md": "HIDDEN THREAD\n",
            "docs/local_execution/validation/262_p03.md": "HIDDEN VALIDATION\n",
        }
        for path, value in files.items():
            target = repo / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(value, encoding="utf-8")
        git(repo, "add", ".")
        git(repo, "commit", "-qm", "synthetic source")
        pin = git(repo, "rev-parse", "HEAD")
        output = root / "artifacts"
        try:
            mod.build(repo, pin=pin, root_override=repo / ".git")
            raise AssertionError("Unsafe output override was not rejected")
        except ValueError as error:
            assert "cannot target ADS" in str(error)
        receipt = mod.build(repo, pin=pin, root_override=output)
        assert receipt["source_ref"] == pin
        mod.build(repo, pin=pin, verify_only=True, root_override=output)
        with zipfile.ZipFile(output / "R0_P03_FRESH_AUTHOR_PILOT.zip") as archive:
            names = archive.namelist()
            assert len(names) == receipt["file_count"] + 2
            assert "sources/docs/DECISIONS.md" in names
            assert not any(k in name for name in names for k in ("HIDDEN", "/research/", "/validation/", "MC-0030", "gold.json"))
            manifest = json.loads(archive.read("SOURCE_MANIFEST.json"))
            for entry in manifest["files"]:
                data = archive.read("sources/" + entry["path"])
                assert hashlib.sha256(data).hexdigest() == entry["sha256"]
                assert hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest() == entry["git_blob_oid"]
        assert not mod.admissible("docs/research/513_protocol.md")
        assert not mod.admissible("docs/specifications/../research/513.md")
        (repo / "docs/DECISIONS.md").write_text("CHANGED WORKTREE\n", encoding="utf-8")
        mod.build(repo, pin=pin, verify_only=True, root_override=output)
        packet = output / "R0_P03_FRESH_AUTHOR_PILOT.zip"
        packet.write_bytes(packet.read_bytes() + b"tamper")
        try:
            mod.build(repo, pin=pin, verify_only=True, root_override=output)
            raise AssertionError("Tampered packet was not rejected")
        except ValueError:
            pass
