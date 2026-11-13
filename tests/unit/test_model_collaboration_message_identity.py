"""Prospective message identity collision guard with one immutable historical exception.

A numeric message identity is thread-local. The historical MC-0030/063
collision remains immutable and is disambiguated by exact path and hash,
not by retroactively renaming messages or broad exemption.
"""
from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/check_model_collaboration_state.py"
SPEC = importlib.util.spec_from_file_location("mc_identity_guard", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def messages(tmp_path: Path, thread: str = "MC-9999") -> Path:
    parent = tmp_path / "docs/model_collaboration/threads" / thread / "messages"
    parent.mkdir(parents=True)
    return parent


def test_repository_historical_collision_is_byte_pinned_and_only_exception() -> None:
    assert MODULE.validate_message_identities(ROOT) == []
    parent = ROOT / "docs/model_collaboration/threads/MC-0030/messages"
    actual = {
        name: hashlib.sha256((parent / name).read_bytes()).hexdigest()
        for name in MODULE.LEGACY_MESSAGE_COLLISION_063
    }
    assert actual == MODULE.LEGACY_MESSAGE_COLLISION_063
    assert len(actual) == 2


def test_unrelated_collision_is_rejected(tmp_path: Path) -> None:
    p = messages(tmp_path)
    (p / "001_first.md").write_text("one", encoding="utf-8")
    (p / "001_second.md").write_text("two", encoding="utf-8")
    errors = MODULE.validate_message_identities(tmp_path)
    assert len(errors) == 1
    assert "duplicate durable message identity" in errors[0]
    assert "MC-9999 Message 001" in errors[0]


def test_third_claimant_at_original_number_cannot_be_whitelisted(tmp_path: Path) -> None:
    p = messages(tmp_path, "MC-0030")
    for name in MODULE.LEGACY_MESSAGE_COLLISION_063:
        (p / name).write_bytes(
            (ROOT / "docs/model_collaboration/threads/MC-0030/messages" / name).read_bytes()
        )
    assert MODULE.validate_message_identities(tmp_path) == []
    (p / "063_third_claimant.md").write_text("third", encoding="utf-8")
    assert len(MODULE.validate_message_identities(tmp_path)) == 1


def test_modified_original_collision_is_rejected(tmp_path: Path) -> None:
    p = messages(tmp_path, "MC-0030")
    for name in MODULE.LEGACY_MESSAGE_COLLISION_063:
        (p / name).write_bytes(
            (ROOT / "docs/model_collaboration/threads/MC-0030/messages" / name).read_bytes()
        )
    first = next(iter(MODULE.LEGACY_MESSAGE_COLLISION_063))
    with (p / first).open("ab") as f:
        f.write(b"\nunauthorized change")
    assert len(MODULE.validate_message_identities(tmp_path)) == 1


def test_nonmessage_auxiliary_docs_and_distinct_numbers_are_valid(tmp_path: Path) -> None:
    p = messages(tmp_path)
    (p / "001_first.md").write_text("one", encoding="utf-8")
    (p / "002_second.md").write_text("two", encoding="utf-8")
    (p / "README.md").write_text("auxiliary", encoding="utf-8")
    assert MODULE.validate_message_identities(tmp_path) == []


def test_cross_thread_identical_numbers_are_valid(tmp_path: Path) -> None:
    for thread in ("MC-0001", "MC-0002"):
        (messages(tmp_path, thread) / "001_first.md").write_text("first", encoding="utf-8")
    assert MODULE.validate_message_identities(tmp_path) == []
