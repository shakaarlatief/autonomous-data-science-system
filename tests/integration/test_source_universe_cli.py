"""Direct regression coverage for MC-0007 F3: structured partial ingest progress."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from sqlalchemy import create_engine

from ads_system import source_cli
from ads_system.infrastructure.persistence.schema import metadata
import ads_system.infrastructure.persistence.source_schema  # noqa: F401


def _prepare_database(database: Path) -> None:
    engine = create_engine(f"sqlite+pysqlite:///{database}")
    metadata.create_all(engine)
    engine.dispose()


def _write_manifest(path: Path) -> None:
    manifest = {
        "format": "ADS_SOURCE_INTAKE_MANIFEST",
        "schema_version": 1,
        "collection": {"stable_key": "cli.course", "title": "CLI Course"},
        "entries": [
            {
                "observed_name": "first.pdf",
                "stable_key": "cli.first",
                "title": "First",
                "source_type": "BOOK",
            },
            {
                "observed_name": "second.pdf",
                "stable_key": "cli.second",
                "title": "Second",
                "source_type": "BOOK",
            },
        ],
    }
    path.write_text(json.dumps(manifest), encoding="utf-8")


def test_ingest_preserves_partial_progress_on_reachable_conflict(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root = tmp_path / "course"
    root.mkdir()
    # Both files carry identical bytes but distinct stable_key values, which
    # reaches the same reachable LogicalSourceConflict as the application-layer
    # regression, but exercised through the CLI's batch-ingest loop.
    (root / "first.pdf").write_bytes(b"identical-bytes")
    (root / "second.pdf").write_bytes(b"identical-bytes")

    manifest_path = tmp_path / "manifest.json"
    _write_manifest(manifest_path)
    database = tmp_path / "registry.db"
    _prepare_database(database)
    vault = tmp_path / "vault"

    exit_code = source_cli.main(
        [
            "ingest",
            "--manifest",
            str(manifest_path),
            "--root",
            str(root),
            "--database",
            str(database),
            "--vault",
            str(vault),
        ]
    )

    captured = capsys.readouterr()
    records = json.loads(captured.out)

    assert exit_code == 1
    assert len(records) == 2
    by_key = {record["stable_key"]: record for record in records}
    assert by_key["cli.first"]["status"] == "OK"
    assert by_key["cli.first"]["sha256"]
    assert by_key["cli.first"]["result"] == "NEW_ARTIFACT"
    assert by_key["cli.second"]["status"] == "FAILED"
    assert by_key["cli.second"]["error_type"] == "LogicalSourceConflict"
    assert "error_detail" in by_key["cli.second"]


def test_ingest_returns_zero_and_all_ok_when_every_request_succeeds(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    root = tmp_path / "course"
    root.mkdir()
    (root / "first.pdf").write_bytes(b"first-bytes")
    (root / "second.pdf").write_bytes(b"second-bytes")

    manifest_path = tmp_path / "manifest.json"
    _write_manifest(manifest_path)
    database = tmp_path / "registry.db"
    _prepare_database(database)
    vault = tmp_path / "vault"

    exit_code = source_cli.main(
        [
            "ingest",
            "--manifest",
            str(manifest_path),
            "--root",
            str(root),
            "--database",
            str(database),
            "--vault",
            str(vault),
        ]
    )

    captured = capsys.readouterr()
    records = json.loads(captured.out)

    assert exit_code == 0
    assert len(records) == 2
    assert all(record["status"] == "OK" for record in records)
