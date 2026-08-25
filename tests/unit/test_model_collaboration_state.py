from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_PATH = ROOT / "scripts" / "check_model_collaboration_state.py"
SPEC = importlib.util.spec_from_file_location("check_model_collaboration_state", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def valid_state() -> dict:
    return {
        "schema_version": 1,
        "thread_id": "MC-0002",
        "review_mode": "REVIEWED",
        "lifecycle_state": "ACTIVE",
        "phase": "IMPLEMENTATION_ACTIVE",
        "target": {
            "branch": "v1-multimodel-development-collaboration",
            "base_ref": "9da382d4011ff112b75dec9c456143d798336336",
            "description": "Implement Specification 024 collaboration-state guard.",
            "write_paths": [
                "schemas/model_collaboration_thread_state_v1.schema.json",
                "scripts/check_model_collaboration_state.py",
                "tests/unit/test_model_collaboration_state.py",
            ],
        },
        "task_owner": "chatgpt",
        "target_write_owner": "chatgpt",
        "participants": [
            {
                "collaborator_id": "chatgpt",
                "interaction_environment": "ChatGPT",
                "interaction_session": "chatgpt-06",
                "roles": ["TASK_OWNER", "IMPLEMENTER"],
            },
            {
                "collaborator_id": "claude",
                "interaction_environment": "Claude",
                "interaction_session": "claude-01",
                "roles": ["REVIEWER"],
            },
        ],
        "allowed_secondary_write_surfaces": [
            {
                "collaborator_id": "claude",
                "paths": ["docs/model_collaboration/threads/MC-0002/messages/**"],
            }
        ],
        "next_expected_actor": "chatgpt",
        "independence": {
            "status": "NOT_APPLICABLE",
            "review_base_ref": None,
            "known_exposures": [],
            "notes": "Direct review under a frozen implementation contract.",
        },
        "last_transition": {
            "transition_id": "mc0002-open",
            "from_state": "OPEN",
            "to_state": "ACTIVE",
            "actor": "chatgpt",
            "reason": "Begin implementation from frozen Specification 024.",
            "repository_head": "9da382d4011ff112b75dec9c456143d798336336",
        },
    }


def write_case(tmp_path: Path, state: dict, directory: str = "MC-0002") -> Path:
    thread_dir = tmp_path / directory
    thread_dir.mkdir(parents=True)
    (thread_dir / "THREAD.md").write_text("# Thread\n", encoding="utf-8")
    state_path = thread_dir / "STATE.json"
    state_path.write_text(json.dumps(state), encoding="utf-8")
    return state_path


def errors_for(tmp_path: Path, state: dict, directory: str = "MC-0002") -> list[str]:
    return MODULE.validate_state_file(write_case(tmp_path, state, directory))


def test_valid_state_passes(tmp_path: Path) -> None:
    assert errors_for(tmp_path, valid_state()) == []


def test_thread_id_must_match_directory(tmp_path: Path) -> None:
    assert any("does not match containing directory" in error for error in errors_for(tmp_path, valid_state(), "MC-9999"))

@pytest.mark.parametrize("field", ["task_owner", "target_write_owner", "next_expected_actor"])
def test_primary_actor_references_must_be_declared(tmp_path: Path, field: str) -> None:
    state = valid_state()
    state[field] = "ghost"
    assert any("undeclared participant" in error for error in errors_for(tmp_path, state))


def test_transition_actor_must_be_declared(tmp_path: Path) -> None:
    state = valid_state()
    state["last_transition"]["actor"] = "ghost"
    assert any("last_transition.actor references undeclared" in error for error in errors_for(tmp_path, state))


def test_duplicate_participant_ids_fail(tmp_path: Path) -> None:
    state = valid_state()
    state["participants"].append(copy.deepcopy(state["participants"][0]))
    assert any("duplicate participant IDs" in error for error in errors_for(tmp_path, state))


def test_unknown_role_fails_schema(tmp_path: Path) -> None:
    state = valid_state()
    state["participants"][0]["roles"] = ["SUPREME_ARCHITECT"]
    assert any("schema" in error for error in errors_for(tmp_path, state))

@pytest.mark.parametrize(
    "bad_path",
    ["/absolute/path", "C:/drive/path", "a\\b", "a//b", "a/../b", "a/./b", "trailing/"],
)
def test_invalid_repository_paths_fail(tmp_path: Path, bad_path: str) -> None:
    state = valid_state()
    state["target"]["write_paths"] = [bad_path]
    assert any("invalid target write path" in error for error in errors_for(tmp_path, state))


def test_secondary_path_overlap_is_rejected(tmp_path: Path) -> None:
    state = valid_state()
    state["target"]["write_paths"] = ["docs/model_collaboration/threads/MC-0002/**"]
    assert any("may overlap target write path" in error for error in errors_for(tmp_path, state))


def test_disjoint_secondary_path_is_allowed(tmp_path: Path) -> None:
    state = valid_state()
    state["target"]["write_paths"] = ["docs/model_collaboration/threads/MC-0002/STATE.json"]
    assert errors_for(tmp_path, state) == []

@pytest.mark.parametrize("lifecycle", ["OPEN", "ACTIVE", "WAITING"])
def test_active_state_with_target_paths_requires_write_owner(tmp_path: Path, lifecycle: str) -> None:
    state = valid_state()
    state["lifecycle_state"] = lifecycle
    state["last_transition"]["to_state"] = lifecycle
    state["target_write_owner"] = None
    assert any("requires target_write_owner" in error for error in errors_for(tmp_path, state))


def test_closed_state_releases_writer_and_next_actor(tmp_path: Path) -> None:
    state = valid_state()
    state["lifecycle_state"] = "CLOSED"
    state["last_transition"]["to_state"] = "CLOSED"
    assert any("CLOSED state requires target_write_owner = null" in error for error in errors_for(tmp_path, state))
    assert any("CLOSED state requires next_expected_actor = null" in error for error in errors_for(tmp_path, state))


def test_transition_state_must_match_current_state(tmp_path: Path) -> None:
    state = valid_state()
    state["last_transition"]["to_state"] = "WAITING"
    assert any("must equal lifecycle_state" in error for error in errors_for(tmp_path, state))


def test_bad_transition_sha_fails_schema(tmp_path: Path) -> None:
    state = valid_state()
    state["last_transition"]["repository_head"] = "ABC123"
    assert any("schema" in error for error in errors_for(tmp_path, state))


def test_guarded_state_requires_thread_file(tmp_path: Path) -> None:
    thread_dir = tmp_path / "MC-0002"
    thread_dir.mkdir()
    state_path = thread_dir / "STATE.json"
    state_path.write_text(json.dumps(valid_state()), encoding="utf-8")
    assert any("adjacent THREAD.md is required" in error for error in MODULE.validate_state_file(state_path))


def test_extra_fields_fail_closed(tmp_path: Path) -> None:
    state = valid_state()
    state["unexpected"] = True
    assert any("schema" in error for error in errors_for(tmp_path, state))


def test_secondary_collaborator_must_be_declared(tmp_path: Path) -> None:
    state = valid_state()
    state["allowed_secondary_write_surfaces"][0]["collaborator_id"] = "ghost"
    assert any("allowed_secondary_write_surfaces" in error and "undeclared participant" in error for error in errors_for(tmp_path, state))
