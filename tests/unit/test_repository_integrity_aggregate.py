from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_script_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


MODULE = load_script_module(
    "check_repository_integrity_test",
    SCRIPTS_DIR / "check_repository_integrity.py",
)
CHECKPOINT_MODULE = load_script_module(
    "check_checkpoint_metadata_test",
    SCRIPTS_DIR / "check_checkpoint_metadata.py",
)
KNOWLEDGE_MAP_MODULE = load_script_module(
    "check_knowledge_map_test",
    SCRIPTS_DIR / "check_knowledge_map.py",
)


def test_validator_command_preserves_focused_validator_cli_contracts(tmp_path: Path) -> None:
    rooted = MODULE.validator_command(
        tmp_path,
        "check_checkpoint_metadata.py",
        accepts_root_argument=True,
    )
    unrooted = MODULE.validator_command(
        tmp_path,
        "check_model_collaboration_state.py",
        accepts_root_argument=False,
    )

    assert rooted[-2:] == ["--root", str(tmp_path)]
    assert "--root" not in unrooted


def test_model_collaboration_validator_is_configured_without_root_argument() -> None:
    validators = {validator.name: validator for validator in MODULE.FOCUSED_VALIDATORS}

    assert validators["model collaboration state"].accepts_root_argument is False
    assert validators["checkpoint metadata"].accepts_root_argument is True
    assert validators["Knowledge Map"].accepts_root_argument is True


def test_run_validator_uses_compatible_command(monkeypatch, tmp_path: Path) -> None:
    observed: list[str] = []

    def fake_run(command, **kwargs):
        observed.extend(command)
        assert kwargs["cwd"] == tmp_path
        return subprocess.CompletedProcess(command, 0, stdout="ok\n", stderr="")

    monkeypatch.setattr(MODULE.subprocess, "run", fake_run)

    result = MODULE.run_validator(
        tmp_path,
        "model collaboration state",
        "check_model_collaboration_state.py",
        accepts_root_argument=False,
    )

    assert result.returncode == 0
    assert result.output == "ok"
    assert "--root" not in observed


def valid_intermediate_text(*, identity_disposition: bool = True) -> str:
    disposition = (
        "**Identity disposition:** Numbered identity retired after provenance audit.\n"
        if identity_disposition
        else ""
    )
    return (
        "# Historical Intermediate Milestone: Test milestone\n\n"
        "**Date:** 2026-08-28  \n"
        "**Status:** HISTORICAL INTERMEDIATE MILESTONE / NUMBERED IDENTITY RETIRED  \n"
        "**Checkpoint class:** CONTINUITY  \n"
        "**Project stage:** TEST  \n"
        "**Scope:** Preserve a test milestone.  \n"
        "**Authority:** Historical provenance only.  \n"
        "**Interaction environment:** ChatGPT  \n"
        "**Project / workspace:** Autonomous Data Science System  \n"
        "**Interaction session:** chatgpt-13  \n"
        "**Conversation title:** Test conversation  \n"
        "**Primary collaborator:** ChatGPT  \n"
        "**Original recorded identity:** `Checkpoint 252`  \n"
        f"{disposition}"
        "\n## Body\n"
    )


def test_historical_intermediate_checkpoint_metadata_is_strict(tmp_path: Path) -> None:
    path = (
        tmp_path
        / "docs/checkpoints/intermediate_2026-08-28_test_milestone.md"
    )
    path.parent.mkdir(parents=True)
    path.write_text(valid_intermediate_text(), encoding="utf-8")

    assert CHECKPOINT_MODULE.validate_intermediate_checkpoint(path) == []

    path.write_text(
        valid_intermediate_text(identity_disposition=False), encoding="utf-8"
    )
    errors = CHECKPOINT_MODULE.validate_intermediate_checkpoint(path)
    assert any("Identity disposition" in error for error in errors)


def test_historical_intermediate_checkpoint_filename_is_governed(tmp_path: Path) -> None:
    path = tmp_path / "docs/checkpoints/intermediate_bad.md"
    path.parent.mkdir(parents=True)
    path.write_text(valid_intermediate_text(), encoding="utf-8")

    errors = CHECKPOINT_MODULE.validate_intermediate_checkpoint(path)
    assert any("malformed historical-intermediate filename" in error for error in errors)


def test_historical_intermediate_checkpoint_requires_direct_knowledge_map_route(
    tmp_path: Path,
) -> None:
    relative = "docs/checkpoints/intermediate_2026-08-28_test_milestone.md"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_text(valid_intermediate_text(), encoding="utf-8")

    errors = KNOWLEDGE_MAP_MODULE.validate_intermediate_checkpoint_routes(
        tmp_path, set()
    )
    assert any(relative in error for error in errors)

    assert (
        KNOWLEDGE_MAP_MODULE.validate_intermediate_checkpoint_routes(
            tmp_path, {relative}
        )
        == []
    )


def test_checkpoint_support_file_is_not_misclassified_as_intermediate(
    tmp_path: Path,
) -> None:
    path = tmp_path / "docs/checkpoints/README.md"
    path.parent.mkdir(parents=True)
    path.write_text("# Checkpoint contract\n", encoding="utf-8")

    paths, errors = KNOWLEDGE_MAP_MODULE.intermediate_checkpoint_paths(tmp_path)
    assert paths == set()
    assert errors == []
