from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest
from sqlalchemy import create_engine

from ads_system.application.source_manifest import (
    compare_intake_manifest,
    load_intake_manifest,
)
from ads_system.application.source_universe import (
    DirtySourceStore,
    IngestRequest,
    LogicalSourceConflict,
    SourceUniverseService,
)
from ads_system.infrastructure.persistence.schema import metadata
import ads_system.infrastructure.persistence.source_schema  # noqa: F401
from ads_system.infrastructure.persistence.source_repository import (
    SqlAlchemySourceRegistryRepository,
)
from ads_system.infrastructure.source_store import LocalSourceArtifactStore


def _service(tmp_path: Path, name: str = "a") -> SourceUniverseService:
    database = tmp_path / f"{name}.db"
    engine = create_engine(f"sqlite+pysqlite:///{database}")
    metadata.create_all(engine)
    return SourceUniverseService(
        engine,
        LocalSourceArtifactStore(tmp_path / f"{name}-vault"),
    )


def _request(path: Path, stable_key: str = "vu.ml.lecture") -> IngestRequest:
    return IngestRequest(
        input_path=path,
        stable_key=stable_key,
        title="Test Lecture",
        source_type="LECTURE_MATERIAL",
        collection_stable_key="vu.ml",
        collection_title="VU Machine Learning",
        membership_role="LECTURE",
        association_status="POSSIBLE",
        observed_name=path.name,
    )


def test_ingest_duplicate_uncertainty_public_export_and_derived_lineage(
    tmp_path: Path,
) -> None:
    source_file = tmp_path / "lecture.pdf"
    source_file.write_bytes(b"same exact bytes")
    service = _service(tmp_path)
    first = service.ingest_file(_request(source_file))
    duplicate = tmp_path / "renamed.pdf"
    duplicate.write_bytes(source_file.read_bytes())
    second = service.ingest_file(_request(duplicate))

    assert first.result == "NEW_ARTIFACT"
    assert second.result == "EXACT_DUPLICATE"
    assert first.artifact.artifact_id == second.artifact.artifact_id
    assert sum(1 for _ in service.store.iter_objects()) == 1

    with service.engine.connect() as connection:
        rows = SqlAlchemySourceRegistryRepository(connection).export_rows()
    assert len(rows["artifacts"]) == 1
    assert len(rows["ingestion_events"]) == 2
    assert rows["memberships"][0]["association_status"] == "POSSIBLE"

    public = service.export_snapshot("PUBLIC_SAFE_CATALOG").decode()
    assert str(source_file.resolve()) not in public
    assert str(duplicate.resolve()) not in public
    assert service.export_snapshot() == service.export_snapshot()

    service.add_derived_artifact(
        parent_artifact_id=first.artifact.artifact_id,
        kind="EXTRACTED_TEXT",
        pipeline_key="test.extract",
        pipeline_version="1",
        configuration_sha256="0" * 64,
        output_sha256="1" * 64,
        byte_size=4,
        media_type="text/plain",
        storage_key="derived/private.txt",
    )
    assert len(json.loads(service.export_snapshot())["derived_artifacts"]) == 1


def test_distinct_bytes_remain_distinct_and_audit_detects_corruption_orphans(
    tmp_path: Path,
) -> None:
    service = _service(tmp_path)
    a = tmp_path / "a.pdf"
    a.write_bytes(b"A")
    b = tmp_path / "b.pdf"
    b.write_bytes(b"B")
    first = service.ingest_file(_request(a, "source.a"))
    second = service.ingest_file(
        IngestRequest(
            input_path=b,
            stable_key="source.b",
            title="B",
            source_type="BOOK",
        )
    )
    assert first.artifact.sha256 != second.artifact.sha256
    assert all(item.status == "OK" for item in service.audit())

    service.store.object_path(first.artifact.sha256).write_bytes(b"corrupt")
    assert any(
        item.status in {"SIZE_MISMATCH", "DIGEST_MISMATCH"}
        for item in service.audit()
    )
    service.store.object_path(first.artifact.sha256).write_bytes(b"A")

    orphan = tmp_path / "orphan.bin"
    orphan.write_bytes(b"orphan")
    service.store.put_path(orphan)
    assert any(item.status == "ORPHAN_OBJECT" for item in service.audit())


def test_backup_refuses_dirty_then_round_trips_clean_state(tmp_path: Path) -> None:
    service = _service(tmp_path, "source")
    source_file = tmp_path / "lecture.pdf"
    source_file.write_bytes(b"recoverable")
    service.ingest_file(_request(source_file))

    orphan = tmp_path / "orphan.bin"
    orphan.write_bytes(b"orphan")
    orphan_stored = service.store.put_path(orphan)
    with pytest.raises(DirtySourceStore):
        service.create_backup(tmp_path / "bad-backup")
    service.store.object_path(orphan_stored.sha256).unlink()

    backup = service.create_backup(tmp_path / "backup")
    manifest = service.verify_backup(backup)
    assert manifest["object_count"] == 1

    restored = _service(tmp_path, "restored")
    SourceUniverseService.restore_backup(
        backup,
        target_engine=restored.engine,
        target_store=restored.store,
    )
    assert restored.export_snapshot() == service.export_snapshot()
    assert all(item.status == "OK" for item in restored.audit())


def test_manifest_comparison_preserves_all_mismatch_classes(tmp_path: Path) -> None:
    root = tmp_path / "course"
    root.mkdir()
    match = root / "local-match.pdf"
    match.write_bytes(b"match")
    different = root / "different.pdf"
    different.write_bytes(b"observed")
    extra = root / "extra.pdf"
    extra.write_bytes(b"extra")

    manifest = {
        "format": "ADS_SOURCE_INTAKE_MANIFEST",
        "schema_version": 1,
        "entries": [
            {
                "observed_name": "match.pdf",
                "local_name_aliases": ["local-match.pdf"],
                "expected_sha256": hashlib.sha256(b"match").hexdigest(),
                "expected_byte_size": 5,
            },
            {
                "observed_name": "different.pdf",
                "expected_sha256": hashlib.sha256(b"expected").hexdigest(),
                "expected_byte_size": 8,
            },
            {
                "observed_name": "missing.pdf",
                "expected_sha256": "0" * 64,
                "expected_byte_size": 1,
            },
        ],
    }
    statuses = {
        result.observed_name: result.status
        for result in compare_intake_manifest(manifest, root)
    }
    assert statuses == {
        "match.pdf": "MATCH",
        "different.pdf": "DIFFERENT_ARTIFACT",
        "missing.pdf": "MISSING_LOCAL_SOURCE",
        "extra.pdf": "ADDITIONAL_LOCAL_SOURCE",
    }


def test_logical_source_conflict_for_same_exact_bytes(tmp_path: Path) -> None:
    service = _service(tmp_path)
    first_path = tmp_path / "first.pdf"
    first_path.write_bytes(b"identity")
    second_path = tmp_path / "second.pdf"
    second_path.write_bytes(b"identity")
    service.ingest_file(
        IngestRequest(
            input_path=first_path,
            stable_key="logical.first",
            title="First",
            source_type="BOOK",
        )
    )
    with pytest.raises(LogicalSourceConflict):
        service.ingest_file(
            IngestRequest(
                input_path=second_path,
                stable_key="logical.second",
                title="Second",
                source_type="BOOK",
            )
        )
    with service.engine.connect() as connection:
        rows = SqlAlchemySourceRegistryRepository(connection).export_rows()
    assert len(rows["artifacts"]) == 1
    assert len(rows["sources"]) == 1


def test_audit_detects_missing_and_same_size_digest_mismatch(tmp_path: Path) -> None:
    service = _service(tmp_path)
    source_file = tmp_path / "x.pdf"
    source_file.write_bytes(b"abc")
    outcome = service.ingest_file(
        IngestRequest(
            input_path=source_file,
            stable_key="x",
            title="X",
            source_type="BOOK",
        )
    )
    object_path = service.store.object_path(outcome.artifact.sha256)
    object_path.unlink()
    assert service.audit()[0].status == "MISSING_OBJECT"
    object_path.parent.mkdir(parents=True, exist_ok=True)
    object_path.write_bytes(b"xyz")
    assert service.audit()[0].status == "DIGEST_MISMATCH"


def test_real_vu_manifest_is_metadata_only_and_preserves_uncertainty() -> None:
    manifest = load_intake_manifest(
        Path("docs/source_universe/manifests/001_vu_machine_learning.json")
    )
    assert len(manifest["entries"]) == 20
    assert all(
        "input_path" not in entry and "storage_key" not in entry
        for entry in manifest["entries"]
    )
    lecture9 = [
        entry
        for entry in manifest["entries"]
        if entry["observed_name"].startswith("Lecture9-")
    ]
    assert lecture9
    assert all(entry["association_status"] == "POSSIBLE" for entry in lecture9)
    duplicated_names = [
        entry
        for entry in manifest["entries"]
        if "(1).pdf" in entry["observed_name"]
    ]
    assert len(duplicated_names) == 14
    assert all(entry.get("local_name_aliases") for entry in duplicated_names)
