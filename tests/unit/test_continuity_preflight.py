from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load_script(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


PRIVATE = load_script("check_private_continuity_test", "check_private_continuity.py")
PREFLIGHT = load_script(
    "check_chat_rotation_preflight_test", "check_chat_rotation_preflight.py"
)


def write_private_state(path: Path, checkpoint: str, commit: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# Current Private State\n\n"
        f"**Public continuity checkpoint:** {checkpoint}  \n"
        f"**Public continuity commit:** {commit}\n\n"
        "## Private content\n",
        encoding="utf-8",
    )


def test_private_anchor_passes_when_both_public_safe_values_match(tmp_path: Path) -> None:
    path = tmp_path / "CURRENT_PRIVATE_STATE.md"
    expected_commit = "a" * 40
    write_private_state(path, "269", expected_commit)

    status, errors = PRIVATE.evaluate_private_continuity(path, 269, expected_commit)

    assert status == "PASS"
    assert errors == []


def test_private_anchor_fails_when_accessible_values_mismatch(tmp_path: Path) -> None:
    path = tmp_path / "CURRENT_PRIVATE_STATE.md"
    write_private_state(path, "268", "b" * 40)

    status, errors = PRIVATE.evaluate_private_continuity(path, 269, "a" * 40)

    assert status == "FAIL"
    assert any("checkpoint" in error.lower() and "mismatch" in error for error in errors)
    assert any("commit" in error.lower() and "mismatch" in error for error in errors)


def test_private_anchor_is_not_verified_when_private_surface_is_inaccessible(tmp_path: Path) -> None:
    status, errors = PRIVATE.evaluate_private_continuity(
        tmp_path / "missing.md", 269, "a" * 40
    )

    assert status == "NOT_VERIFIED"
    assert errors == []


def test_private_anchor_rejects_malformed_accessible_values(tmp_path: Path) -> None:
    path = tmp_path / "CURRENT_PRIVATE_STATE.md"
    write_private_state(path, "zero", "NOT_A_SHA")

    status, errors = PRIVATE.evaluate_private_continuity(path, 269, "a" * 40)

    assert status == "FAIL"
    assert len(errors) == 2


def test_public_failure_makes_rotation_fail() -> None:
    status, reasons = PREFLIGHT.evaluate_chat_rotation(
        "FAIL", "NOT_VERIFIED", private_required=True
    )
    assert status == "FAIL"
    assert reasons


def test_required_private_not_verified_holds_rotation() -> None:
    status, reasons = PREFLIGHT.evaluate_chat_rotation(
        "PASS", "NOT_VERIFIED", private_required=True
    )
    assert status == "HOLD"
    assert any("not verified" in reason for reason in reasons)


def test_required_private_failure_makes_rotation_fail() -> None:
    status, reasons = PREFLIGHT.evaluate_chat_rotation(
        "PASS", "FAIL", private_required=True
    )
    assert status == "FAIL"
    assert reasons


def test_open_transition_obligation_holds_otherwise_green_rotation() -> None:
    status, reasons = PREFLIGHT.evaluate_chat_rotation(
        "PASS",
        "PASS",
        private_required=True,
        open_transition_obligations=("canonical reconciliation",),
    )
    assert status == "HOLD"
    assert reasons == ["open transition obligation: canonical reconciliation"]


def test_green_public_private_and_no_obligations_allows_rotation_pass() -> None:
    status, reasons = PREFLIGHT.evaluate_chat_rotation(
        "PASS", "PASS", private_required=True
    )
    assert status == "PASS"
    assert reasons == []
