"""Direct regression coverage for MC-0007 F1-F4 recovery-hardening findings."""

from __future__ import annotations

from pathlib import Path

import pytest
from sqlalchemy import create_engine

from ads_system.application import source_universe
from ads_system.application.source_universe import IngestRequest, SourceUniverseService
from ads_system.infrastructure.persistence.schema import metadata
import ads_system.infrastructure.persistence.source_schema  # noqa: F401
from ads_system.infrastructure.source_store import (
    LocalSourceArtifactStore,
    SourceArtifactIntegrityError,
)


def _service(tmp_path: Path, name: str = "recovery") -> SourceUniverseService:
    database = tmp_path / f"{name}.db"
    engine = create_engine(f"sqlite+pysqlite:///{database}")
    metadata.create_all(engine)
    return SourceUniverseService(engine, LocalSourceArtifactStore(tmp_path / f"{name}-vault"))


def _request(path: Path, stable_key: str) -> IngestRequest:
    return IngestRequest(
        input_path=path,
        stable_key=stable_key,
        title=stable_key,
        source_type="BOOK",
    )


def test_f1_existing_corrupt_object_cleans_staging_and_preserves_corruption(
    tmp_path: Path,
) -> None:
    store = LocalSourceArtifactStore(tmp_path / "vault")
    original = tmp_path / "original.bin"
    original.write_bytes(b"hello-bytes")
    stored = store.commit(store.stage_from_path(original))
    final_path = store.object_path(stored.sha256)
    final_path.write_bytes(b"corrupted-on-disk")

    duplicate = tmp_path / "duplicate.bin"
    duplicate.write_bytes(b"hello-bytes")
    staged = store.stage_from_path(duplicate)

    with pytest.raises(SourceArtifactIntegrityError):
        store.commit(staged)

    assert not staged.staging_path.exists()
    assert list(store.staging_root.iterdir()) == []
    assert final_path.read_bytes() == b"corrupted-on-disk"


def test_f2_new_object_post_replace_integrity_failure_removes_bad_final_object(
    tmp_path: Path,
) -> None:
    store = LocalSourceArtifactStore(tmp_path / "vault")
    original = tmp_path / "original.bin"
    original.write_bytes(b"good-bytes-for-digest")
    staged = store.stage_from_path(original)
    # Tamper the staged file after hashing so os.replace still succeeds but
    # the explicit post-replace digest/size verification of the object this
    # call just placed fails.
    staged.staging_path.write_bytes(b"tampered")

    with pytest.raises(SourceArtifactIntegrityError):
        store.commit(staged)

    final_path = store.object_path(staged.sha256)
    assert not final_path.exists()
    assert not staged.staging_path.exists()

    # A legitimate retry with the correct bytes is not blocked afterward.
    retry = tmp_path / "retry.bin"
    retry.write_bytes(b"good-bytes-for-digest")
    stored = store.commit(store.stage_from_path(retry))
    assert stored.sha256 == staged.sha256
    assert store.object_path(stored.sha256).read_bytes() == b"good-bytes-for-digest"


def test_f2_unrelated_fsync_failure_does_not_remove_final_object(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    store = LocalSourceArtifactStore(tmp_path / "vault")

    def _raise(_path: Path) -> None:
        raise OSError("simulated unrelated fsync failure")

    monkeypatch.setattr(store, "_fsync_directory", _raise)
    original = tmp_path / "original.bin"
    original.write_bytes(b"fsync-failure-bytes")
    staged = store.stage_from_path(original)

    with pytest.raises(OSError):
        store.commit(staged)

    final_path = store.object_path(staged.sha256)
    assert final_path.exists()
    assert final_path.read_bytes() == b"fsync-failure-bytes"


def test_f4_mid_backup_failure_leaves_retryable_target_and_subsequent_backup_succeeds(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    service = _service(tmp_path)
    first = tmp_path / "first.bin"
    first.write_bytes(b"alpha-object-bytes")
    second = tmp_path / "second.bin"
    second.write_bytes(b"beta-object-bytes")
    service.ingest_file(_request(first, "backup.alpha"))
    service.ingest_file(_request(second, "backup.beta"))

    target = tmp_path / "backup"
    original_copy_and_hash = source_universe._copy_and_hash
    call_count = {"n": 0}

    def _flaky_copy_and_hash(source, destination):
        call_count["n"] += 1
        if call_count["n"] == 2:
            raise OSError("simulated mid-backup disk failure")
        return original_copy_and_hash(source, destination)

    monkeypatch.setattr(source_universe, "_copy_and_hash", _flaky_copy_and_hash)
    with pytest.raises(OSError):
        service.create_backup(target)

    # The failed backup must never be reported as complete and must not
    # occupy or block a straightforward retry to the same target.
    assert not target.exists() or not any(target.iterdir())
    assert list(target.parent.glob(f".{target.name}.partial-*")) == []

    monkeypatch.setattr(source_universe, "_copy_and_hash", original_copy_and_hash)
    result = service.create_backup(target)
    manifest = service.verify_backup(result)
    assert manifest["object_count"] == 2


def test_f4_pre_existing_empty_target_is_restored_after_failure_and_then_succeeds(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    service = _service(tmp_path)
    only = tmp_path / "only.bin"
    only.write_bytes(b"only-object-bytes")
    service.ingest_file(_request(only, "backup.only"))

    target = tmp_path / "backup"
    target.mkdir()

    original_copy_and_hash = source_universe._copy_and_hash

    def _always_fail(source, destination):
        raise OSError("simulated disk failure")

    monkeypatch.setattr(source_universe, "_copy_and_hash", _always_fail)
    with pytest.raises(OSError):
        service.create_backup(target)

    assert target.is_dir()
    assert not any(target.iterdir())

    monkeypatch.setattr(source_universe, "_copy_and_hash", original_copy_and_hash)
    result = service.create_backup(target)
    manifest = service.verify_backup(result)
    assert manifest["object_count"] == 1


def test_f4_genuinely_non_empty_target_is_still_rejected(tmp_path: Path) -> None:
    service = _service(tmp_path)
    only = tmp_path / "only.bin"
    only.write_bytes(b"non-empty-target-bytes")
    service.ingest_file(_request(only, "backup.nonempty"))

    target = tmp_path / "backup"
    target.mkdir()
    (target / "unexpected.txt").write_text("pre-existing content", encoding="utf-8")

    with pytest.raises(FileExistsError):
        service.create_backup(target)
    assert (target / "unexpected.txt").exists()
