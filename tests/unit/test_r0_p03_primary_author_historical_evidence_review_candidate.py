"""Independent non-scored review inventory, no scored tasks or source admission."""
from pathlib import Path
import hashlib
import json
import subprocess
import tempfile

import pytest

from experiments.r0_p03_navigation_probe import (
    primary_author_historical_evidence_review_candidate as scan,
)


def git(repo, *args):
    return subprocess.check_output(["git", *args], cwd=repo).decode().strip()


def seed(tmp: Path):
    repo=tmp/"repo";repo.mkdir()
    git(repo,"init","-q")
    git(repo,"config","user.name","Synthetic")
    git(repo,"config","user.email","synthetic@example.invalid")
    content={
        "README.md":"# README\n",
        "docs/README.md":"# orientation\n",
        "docs/CONTINUITY.md":"# continuity\n",
        "docs/DECISIONS.md":"# policy\n",
        "docs/current_routing.json":"{}\n",
        "docs/specifications/028_v1_project_knowledge_architecture_implementation_and_migration_contract.md":"# spec\n",
        "docs/checkpoints/001_test.md":"One historic event\n",
        "docs/checkpoints/900_r0_p03_design.md":"R0-P03 arm design\n",
        "docs/research/001_history.md":"Lineage of a historical choice\n",
        "docs/research/999_golden.md":"Research 217 and must_retrieve reference\n",
        "docs/local_execution/validation/001_result.md":"test verification\n",
        "scripts/tool.py":"print('hello')\n",
        "tests/unit/test_thing.py":"def test_it(): pass\n",
        "schemas/example.json":"{}\n",
        "frontend/README.md":"# product\n",
        "frontend/index.html":"<div>product</div>\n",
        "frontend/e2e/snapshots/visual.png":"not really a PNG but unsupported\n",
        "src/ads_system/use.py":"sample = True\n",
    }
    for name,body in content.items():
        p=repo/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body)
    git(repo,"add",".")
    git(repo,"commit","-qm","Historical world")
    return repo,git(repo,"rev-parse","HEAD")


def test_review_only_for_every_missing_source_and_contamination_flags():
    with tempfile.TemporaryDirectory() as d:
        root=Path(d);repo,pin=seed(root)
        result=scan.audit(repo,pin=pin)
        by={r["path"]:r for r in result["review_records"]}
        assert len(by)==8
        assert result["admission_decision"] == "NONE_ADMITTED_BY_LEXICAL_OR_PATH_CENSUS"
        assert by["docs/checkpoints/001_test.md"]["status"] == "REVIEW_ONLY_NOT_ADMITTED"
        assert by["docs/checkpoints/001_test.md"]["review_flags"] == []
        assert "R0_P03_DESIGN" in by["docs/checkpoints/900_r0_p03_design.md"]["review_flags"]
        assert "PATH_INDICATES_DESIGN_OR_LEGACY" in by["docs/checkpoints/900_r0_p03_design.md"]["review_flags"]
        assert "LEGACY_W5_REFERENCE" in by["docs/research/999_golden.md"]["review_flags"]
        assert "docs/DECISIONS.md" not in by
        assert all("content" not in row and "full_text" not in row for row in by.values())
        assert all(row["status"] != "ADMITTED" for row in by.values())


def test_reproducible_manifest_and_tamper_detection():
    with tempfile.TemporaryDirectory() as d:
        root=Path(d);repo,pin=seed(root)
        out=root/"review"
        a=scan.emit(repo,pin=pin,root_override=out)
        scan.emit(repo,pin=pin,root_override=out,verify_only=True)
        payload=(out/scan.FILENAME).read_bytes()
        assert hashlib.sha256(payload).hexdigest()==a["manifest_sha256"]
        parsed=json.loads(payload)
        assert parsed["review_record_count"]==a["review_record_count"]
        (repo/"docs/checkpoints/001_test.md").write_text("UNPINNED STATE")
        scan.emit(repo,pin=pin,root_override=out,verify_only=True)
        with pytest.raises(FileExistsError):
            scan.emit(repo,pin=pin,root_override=out)
        (out/scan.FILENAME).write_bytes(b"TAMPER")
        with pytest.raises(ValueError):
            scan.emit(repo,pin=pin,root_override=out,verify_only=True)


def test_output_override_is_outside_repository():
    with tempfile.TemporaryDirectory() as d:
        repo,pin=seed(Path(d))
        with pytest.raises(ValueError):
            scan.emit(repo,pin=pin,root_override=repo/"in-repository")
