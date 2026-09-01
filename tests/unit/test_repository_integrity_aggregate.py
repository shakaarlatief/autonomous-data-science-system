from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = ROOT / "scripts"
SCRIPT_PATH = SCRIPTS_DIR / "check_repository_integrity.py"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
SPEC = importlib.util.spec_from_file_location("check_repository_integrity_test", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


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
