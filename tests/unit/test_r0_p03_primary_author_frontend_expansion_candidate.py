"""Historical frontend source admission is mechanical and non-scored."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile
import zipfile

import pytest

from experiments.r0_p03_navigation_probe import primary_author_frontend_expansion_candidate as expansion


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo).decode().strip()


def make_repo(root: Path, *, contaminated: bool = False) -> tuple[Path, str]:
    repo = root / "repo"
    repo.mkdir()
    git(repo, "init", "-q")
    git(repo, "config", "user.name", "Synthetic")
    git(repo, "config", "user.email", "synthetic@example.invalid")
    paths = {
        "README.md": "# orientation\n",
        "docs/README.md": "# docs\n",
        "docs/CONTINUITY.md": "# continuity\n",
        "docs/DECISIONS.md": "# decisions\n",
        "docs/current_routing.json": "{}\n",
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md": "# contract\n",
        "frontend/README.md": "# product frontend\n",
        "frontend/src/main.tsx": ("R0-P03 GOLD" if contaminated else "export const product = 'source';\n"),
        "frontend/design-lab/cockpit.css": ".cockpit { display: block; }\n",
        "frontend/e2e/visual.spec.ts-snapshots/sample.png": "BINARY_IGNORED\n",
        "src/ads_system/application/module.py": "x = 1\n",
    }
    for name, content in paths.items():
        p=repo/name;p.parent.mkdir(parents=True, exist_ok=True);p.write_text(content)
    git(repo, "add", ".")
    git(repo, "commit", "-qm", "Historical source world")
    return repo, git(repo, "rev-parse", "HEAD")


def test_exact_frontend_family_and_reproducible_archive():
    with tempfile.TemporaryDirectory() as d:
        root=Path(d)
        repo,pin=make_repo(root)
        out=root/"packet"
        receipt=expansion.build(repo,pin=pin,root_override=out)
        assert receipt["frontend_text_count"] == 3
        assert receipt["frontend_unsupported_media_count"] == 1
        assert receipt["status"] == "NON_SCORED_CANDIDATE_ONLY"
        expansion.build(repo,pin=pin,root_override=out,verify_only=True)
        with zipfile.ZipFile(out/expansion.OUT_NAME) as z:
            names=z.namelist()
            assert "sources/frontend/src/main.tsx" in names
            assert "sources/frontend/design-lab/cockpit.css" in names
            assert not any(name.endswith(".png") for name in names)
            m=json.loads(z.read("SOURCE_MANIFEST.json"))
            assert m["readiness"].startswith("CANDIDATE")
            assert m["frontend_media_excluded"] == [
                "frontend/e2e/visual.spec.ts-snapshots/sample.png"
            ]
            for entry in m["files"]:
                assert hashlib.sha256(z.read("sources/"+entry["path"])).hexdigest()==entry["sha256"]
        # A later worktree change does not silently alter the pinned archive.
        (repo/"frontend/src/main.tsx").write_text("UNPINNED MUTATION")
        expansion.build(repo,pin=pin,root_override=out,verify_only=True)
        with pytest.raises(FileExistsError):
            expansion.build(repo,pin=pin,root_override=out)
        (out/expansion.OUT_NAME).write_bytes(b"TAMPER")
        with pytest.raises(ValueError):
            expansion.build(repo,pin=pin,root_override=out,verify_only=True)


def test_text_only_frontend_family_is_also_valid():
    with tempfile.TemporaryDirectory() as d:
        repo, pin = make_repo(Path(d))
        git(repo, "rm", "-q", "frontend/e2e/visual.spec.ts-snapshots/sample.png")
        git(repo, "commit", "-qm", "Text-only supported frontend")
        pin = git(repo, "rev-parse", "HEAD")
        text_sources, excluded = expansion._frontend(repo, pin)
        assert len(text_sources) == 3
        assert excluded == []


def test_explicit_design_leakage_fails_closed():
    with tempfile.TemporaryDirectory() as d:
        repo,pin=make_repo(Path(d),contaminated=True)
        with pytest.raises(ValueError,match="design/scoring leakage"):
            expansion._frontend(repo,pin)


def test_unqualified_scored_boundary_and_output_location():
    with tempfile.TemporaryDirectory() as d:
        repo,pin=make_repo(Path(d))
        with pytest.raises(ValueError,match="inside the repository"):
            expansion.build(repo,pin=pin,root_override=repo/"not-allowed")
