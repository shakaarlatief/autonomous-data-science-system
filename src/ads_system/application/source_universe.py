"""Application services for the provider-free Specification 023 source substrate."""

from __future__ import annotations

import hashlib
import json
import mimetypes
import os
import shutil
from dataclasses import dataclass
from pathlib import Path
import re
from collections.abc import Mapping
from typing import Any, BinaryIO, Protocol
from uuid import uuid4

from sqlalchemy import Engine

from ads_system.domain.source_universe import IntegrityResult, SourceArtifact, SourceCollection, SourceRecord
from ads_system.infrastructure.persistence.types import new_id, utc_now_text
from ads_system.infrastructure.persistence.source_repository import (
    SourceRegistryConflict,
    SqlAlchemySourceRegistryRepository,
)

_STABLE_KEY = re.compile(r"^(?:[a-z0-9]|[a-z0-9][a-z0-9._/-]{0,126}[a-z0-9])$")


class SourceArtifactStore(Protocol):
    """ADS-owned storage port for exact immutable source artifacts."""

    def stage_from_path(self, source_path: str | Path): ...
    def commit(self, staged): ...
    def open(self, sha256: str) -> BinaryIO: ...
    def exists(self, sha256: str) -> bool: ...
    def verify(self, sha256: str, expected_size: int) -> bool: ...
    def iter_objects(self): ...


class LogicalSourceConflict(SourceRegistryConflict):
    """Exact bytes were already attached to a different logical source."""


class DirtySourceStore(RuntimeError):
    """Backup requires a fully clean source store."""


@dataclass(frozen=True, slots=True)
class IngestRequest:
    input_path: Path
    stable_key: str
    title: str
    source_type: str
    canonical_locator: str | None = None
    external_identifier_type: str | None = None
    external_identifier_value: str | None = None
    access_class: str = "PRIVATE_USER_SUPPLIED"
    redistribution_status: str = "UNKNOWN"
    rights_note: str | None = None
    metadata_visibility: str = "PRIVATE"
    media_type: str | None = None
    collection_stable_key: str | None = None
    collection_title: str | None = None
    collection_type: str = "COURSE"
    collection_canonical_locator: str | None = None
    collection_metadata: Mapping[str, Any] | None = None
    membership_role: str = "UNKNOWN"
    association_status: str = "UNVERIFIED"
    membership_note: str | None = None
    observed_name: str | None = None


@dataclass(frozen=True, slots=True)
class IngestOutcome:
    source: SourceRecord
    artifact: SourceArtifact
    collection: SourceCollection | None
    result: str


class SourceUniverseService:
    def __init__(self, engine: Engine, store: SourceArtifactStore) -> None:
        self.engine = engine
        self.store = store

    def ingest_file(self, request: IngestRequest) -> IngestOutcome:
        self._validate_stable_key(request.stable_key)
        if request.collection_stable_key is not None:
            self._validate_stable_key(request.collection_stable_key)
        staged = self.store.stage_from_path(request.input_path)
        stored = self.store.commit(staged)
        now = utc_now_text()
        with self.engine.begin() as connection:
            repo = SqlAlchemySourceRegistryRepository(connection)
            source = repo.get_source_by_stable_key(request.stable_key)
            if source is None:
                source = repo.create_source(
                    {
                        "source_id": new_id(),
                        "stable_key": request.stable_key,
                        "title": request.title,
                        "source_type": request.source_type,
                        "canonical_locator": request.canonical_locator,
                        "external_identifier_type": request.external_identifier_type,
                        "external_identifier_value": request.external_identifier_value,
                        "access_class": request.access_class,
                        "redistribution_status": request.redistribution_status,
                        "rights_note": request.rights_note,
                        "metadata_visibility": request.metadata_visibility,
                        "created_at": now,
                        "updated_at": now,
                    }
                )
            else:
                expected = (request.title, request.source_type)
                if (source.title, source.source_type) != expected:
                    raise SourceRegistryConflict(
                        f"stable source {request.stable_key!r} conflicts with existing title/type"
                    )

            existing_artifact = repo.get_artifact_by_sha256(stored.sha256)
            if existing_artifact is not None and existing_artifact.source_id != source.source_id:
                raise LogicalSourceConflict(
                    f"artifact {stored.sha256} already belongs to logical source {existing_artifact.source_id}"
                )
            if existing_artifact is None:
                artifact = repo.create_artifact(
                    {
                        "artifact_id": new_id(),
                        "source_id": source.source_id,
                        "sha256": stored.sha256,
                        "byte_size": stored.byte_size,
                        "media_type": request.media_type
                        or mimetypes.guess_type(request.input_path.name)[0]
                        or "application/octet-stream",
                        "artifact_state": "PRESERVED",
                        "first_seen_at": now,
                        "last_verified_at": now,
                    }
                )
                event_result = "NEW_ARTIFACT"
            else:
                artifact = existing_artifact
                event_result = "EXACT_DUPLICATE"

            collection: SourceCollection | None = None
            if request.collection_stable_key is not None:
                collection = repo.get_collection_by_stable_key(request.collection_stable_key)
                if collection is None:
                    if not request.collection_title:
                        raise ValueError("collection_title is required when creating a collection")
                    collection = repo.create_collection(
                        {
                            "collection_id": new_id(),
                            "stable_key": request.collection_stable_key,
                            "title": request.collection_title,
                            "collection_type": request.collection_type,
                            "canonical_locator": request.collection_canonical_locator,
                            "metadata_json": dict(request.collection_metadata or {}),
                            "created_at": now,
                            "updated_at": now,
                        }
                    )
                repo.upsert_membership(
                    collection_id=collection.collection_id,
                    source_id=source.source_id,
                    membership_role=request.membership_role,
                    association_status=request.association_status,
                    note=request.membership_note,
                )

            observed_path = str(request.input_path.resolve())
            repo.add_locator(
                {
                    "locator_id": new_id(),
                    "source_id": source.source_id,
                    "artifact_id": artifact.artifact_id,
                    "locator_type": "OBSERVED_PATH",
                    "locator": observed_path,
                    "is_canonical": 0,
                    "visibility": "PRIVATE",
                    "created_at": now,
                }
            )
            if request.canonical_locator:
                repo.add_locator(
                    {
                        "locator_id": new_id(),
                        "source_id": source.source_id,
                        "artifact_id": None,
                        "locator_type": "CANONICAL_URL",
                        "locator": request.canonical_locator,
                        "is_canonical": 1,
                        "visibility": (
                            "PUBLIC_SAFE"
                            if request.metadata_visibility == "PUBLIC_SAFE"
                            else "PRIVATE"
                        ),
                        "created_at": now,
                    }
                )
            repo.add_ingestion_event(
                {
                    "ingestion_event_id": new_id(),
                    "source_id": source.source_id,
                    "artifact_id": artifact.artifact_id,
                    "collection_id": collection.collection_id if collection else None,
                    "occurred_at": now,
                    "intake_channel": "FILESYSTEM",
                    "observed_name": request.observed_name or request.input_path.name,
                    "observed_locator": observed_path,
                    "result": event_result,
                    "note": None,
                }
            )
        return IngestOutcome(source, artifact, collection, event_result)

    def add_derived_artifact(
        self,
        *,
        parent_artifact_id: str,
        kind: str,
        pipeline_key: str,
        pipeline_version: str,
        configuration_sha256: str,
        output_sha256: str,
        byte_size: int,
        media_type: str,
        storage_key: str,
    ) -> str:
        derived_id = new_id()
        with self.engine.begin() as connection:
            SqlAlchemySourceRegistryRepository(connection).add_derived_artifact(
                {
                    "derived_artifact_id": derived_id,
                    "parent_source_artifact_id": parent_artifact_id,
                    "kind": kind,
                    "pipeline_key": pipeline_key,
                    "pipeline_version": pipeline_version,
                    "configuration_sha256": configuration_sha256,
                    "output_sha256": output_sha256,
                    "byte_size": byte_size,
                    "media_type": media_type,
                    "storage_key": storage_key,
                    "created_at": utc_now_text(),
                }
            )
        return derived_id

    def audit(self, *, update_verified_at: bool = False) -> tuple[IntegrityResult, ...]:
        with self.engine.connect() as connection:
            registered = SqlAlchemySourceRegistryRepository(connection).list_preserved_artifacts()
        registered_by_digest = {row["sha256"]: row for row in registered}
        results: list[IntegrityResult] = []
        verified_ids: list[str] = []
        for digest, row in sorted(registered_by_digest.items()):
            expected_size = int(row["byte_size"])
            if not self.store.exists(digest):
                results.append(IntegrityResult(digest, "MISSING_OBJECT", expected_size, None))
                continue
            with self.store.open(digest) as handle:
                observed_digest, observed_size = _hash_stream(handle)
            if observed_size != expected_size:
                results.append(
                    IntegrityResult(digest, "SIZE_MISMATCH", expected_size, observed_size)
                )
                continue
            if observed_digest != digest:
                results.append(
                    IntegrityResult(
                        digest,
                        "DIGEST_MISMATCH",
                        expected_size,
                        observed_size,
                        observed_digest,
                    )
                )
                continue
            results.append(IntegrityResult(digest, "OK", expected_size, observed_size))
            verified_ids.append(row["artifact_id"])
        for digest, observed_size in self.store.iter_objects():
            if digest not in registered_by_digest:
                results.append(IntegrityResult(digest, "ORPHAN_OBJECT", None, observed_size))
        results.sort(key=lambda item: (item.sha256, item.status))
        if update_verified_at and verified_ids:
            now = utc_now_text()
            with self.engine.begin() as connection:
                repo = SqlAlchemySourceRegistryRepository(connection)
                for artifact_id in verified_ids:
                    repo.touch_artifact_verified(artifact_id, now)
        return tuple(results)

    def export_snapshot(self, profile: str = "PRIVATE_SNAPSHOT") -> bytes:
        if profile not in {"PRIVATE_SNAPSHOT", "PUBLIC_SAFE_CATALOG"}:
            raise ValueError(f"unsupported export profile: {profile}")
        with self.engine.connect() as connection:
            rows = SqlAlchemySourceRegistryRepository(connection).export_rows()
        document = _snapshot_document(rows, profile)
        return _canonical_json_bytes(document)

    def import_private_snapshot(self, payload: bytes) -> None:
        document = json.loads(payload.decode("utf-8"))
        if document.get("format") != "ADS_SOURCE_REGISTRY" or document.get("schema_version") != 1:
            raise SourceRegistryConflict("unsupported source registry snapshot format")
        if document.get("export_profile") != "PRIVATE_SNAPSHOT":
            raise SourceRegistryConflict("only PRIVATE_SNAPSHOT may be imported")
        with self.engine.begin() as connection:
            SqlAlchemySourceRegistryRepository(connection).import_rows(document)

    def create_backup(self, backup_root: str | Path) -> Path:
        audit = self.audit()
        if any(item.status != "OK" for item in audit):
            raise DirtySourceStore(f"source store is not clean: {audit}")
        target = Path(backup_root)
        if target.exists() and any(target.iterdir()):
            raise FileExistsError(f"backup target is not empty: {target}")
        target_pre_existed = target.exists()
        target.parent.mkdir(parents=True, exist_ok=True)
        # Build the backup in a temporary sibling and publish it into `target`
        # only after full verification succeeds, so a mid-copy or
        # verification failure never leaves a partial, retry-blocking target.
        staging_target = target.parent / f".{target.name}.partial-{uuid4().hex}"
        shutil.rmtree(staging_target, ignore_errors=True)
        staging_target.mkdir(parents=True)
        try:
            registry_dir = staging_target / "registry"
            registry_dir.mkdir(parents=True, exist_ok=True)
            snapshot = self.export_snapshot("PRIVATE_SNAPSHOT")
            snapshot_path = registry_dir / "source_registry_snapshot.json"
            snapshot_path.write_bytes(snapshot)
            snapshot_digest = hashlib.sha256(snapshot).hexdigest()
            with self.engine.connect() as connection:
                artifacts = SqlAlchemySourceRegistryRepository(connection).list_preserved_artifacts()
            manifest_objects: list[dict[str, Any]] = []
            total_bytes = 0
            for artifact in sorted(artifacts, key=lambda row: row["sha256"]):
                digest = artifact["sha256"]
                size = int(artifact["byte_size"])
                destination = staging_target / "objects" / "sha256" / digest[:2] / digest[2:]
                destination.parent.mkdir(parents=True, exist_ok=True)
                with self.store.open(digest) as source_handle, destination.open("wb") as destination_handle:
                    copied_digest, copied_size = _copy_and_hash(source_handle, destination_handle)
                if copied_digest != digest or copied_size != size:
                    raise SourceRegistryConflict(
                        f"backup object copy verification failed: {digest}"
                    )
                manifest_objects.append({"sha256": digest, "byte_size": size})
                total_bytes += size
            manifest = {
                "format": "ADS_SOURCE_BACKUP",
                "schema_version": 1,
                "created_at": utc_now_text(),
                "registry_snapshot_sha256": snapshot_digest,
                "object_count": len(manifest_objects),
                "object_total_bytes": total_bytes,
                "objects": manifest_objects,
            }
            manifest_path = staging_target / "backup_manifest.json"
            manifest_path.write_bytes(_canonical_json_bytes(manifest))
            self.verify_backup(staging_target)
            if target_pre_existed:
                target.rmdir()
            os.replace(staging_target, target)
        except BaseException:
            shutil.rmtree(staging_target, ignore_errors=True)
            if target_pre_existed and not target.exists():
                target.mkdir(parents=True, exist_ok=True)
            raise
        return target

    @staticmethod
    def verify_backup(backup_root: str | Path) -> dict[str, Any]:
        root = Path(backup_root)
        manifest_path = root / "backup_manifest.json"
        snapshot_path = root / "registry" / "source_registry_snapshot.json"
        if not manifest_path.is_file() or not snapshot_path.is_file():
            raise SourceRegistryConflict("incomplete source backup")
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("format") != "ADS_SOURCE_BACKUP" or manifest.get("schema_version") != 1:
            raise SourceRegistryConflict("unsupported source backup format")
        snapshot = snapshot_path.read_bytes()
        if hashlib.sha256(snapshot).hexdigest() != manifest["registry_snapshot_sha256"]:
            raise SourceRegistryConflict("registry snapshot digest mismatch")
        total = 0
        for item in manifest["objects"]:
            digest = item["sha256"]
            expected_size = int(item["byte_size"])
            path = root / "objects" / "sha256" / digest[:2] / digest[2:]
            observed_digest, observed_size = _hash_path(path)
            if observed_digest != digest or observed_size != expected_size:
                raise SourceRegistryConflict(f"backup object integrity mismatch: {digest}")
            total += observed_size
        if (
            len(manifest["objects"]) != int(manifest["object_count"])
            or total != int(manifest["object_total_bytes"])
        ):
            raise SourceRegistryConflict("backup manifest aggregate mismatch")
        return manifest

    @classmethod
    def restore_backup(
        cls,
        backup_root: str | Path,
        *,
        target_engine: Engine,
        target_store: SourceArtifactStore,
    ) -> "SourceUniverseService":
        root = Path(backup_root)
        manifest = cls.verify_backup(root)
        if any(True for _ in target_store.iter_objects()):
            raise FileExistsError("target source artifact store is not empty")
        with target_engine.connect() as connection:
            if any(SqlAlchemySourceRegistryRepository(connection).counts().values()):
                raise SourceRegistryConflict("target source registry is not empty")
        for item in manifest["objects"]:
            digest = item["sha256"]
            path = root / "objects" / "sha256" / digest[:2] / digest[2:]
            stored = target_store.commit(target_store.stage_from_path(path))
            if stored.sha256 != digest or stored.byte_size != int(item["byte_size"]):
                raise SourceRegistryConflict("restored object does not match backup manifest")
        service = cls(target_engine, target_store)
        snapshot = (root / "registry" / "source_registry_snapshot.json").read_bytes()
        service.import_private_snapshot(snapshot)
        restored_audit = service.audit()
        if any(item.status != "OK" for item in restored_audit):
            raise SourceRegistryConflict(
                f"restored source store audit failed: {restored_audit}"
            )
        return service

    @staticmethod
    def _validate_stable_key(stable_key: str) -> None:
        if not _STABLE_KEY.fullmatch(stable_key):
            raise ValueError(f"invalid stable_key: {stable_key!r}")


def _snapshot_document(
    rows: Mapping[str, list[dict[str, Any]]], profile: str
) -> dict[str, Any]:
    sources = list(rows["sources"])
    artifacts = list(rows["artifacts"])
    collections = list(rows["collections"])
    memberships = list(rows["memberships"])
    locators = list(rows["locators"])
    events = list(rows["ingestion_events"])
    derived = list(rows["derived_artifacts"])
    if profile == "PUBLIC_SAFE_CATALOG":
        sources = [row for row in sources if row["metadata_visibility"] == "PUBLIC_SAFE"]
        source_ids = {row["source_id"] for row in sources}
        artifacts = [row for row in artifacts if row["source_id"] in source_ids]
        artifact_ids = {row["artifact_id"] for row in artifacts}
        memberships = [row for row in memberships if row["source_id"] in source_ids]
        collection_ids = {row["collection_id"] for row in memberships}
        collections = [
            {key: value for key, value in row.items() if key != "metadata_json"}
            for row in collections
            if row["collection_id"] in collection_ids
        ]
        locators = [
            row
            for row in locators
            if row["source_id"] in source_ids
            and row["visibility"] == "PUBLIC_SAFE"
            and row["locator_type"] != "OBSERVED_PATH"
        ]
        events = []
        derived = [
            {key: value for key, value in row.items() if key != "storage_key"}
            for row in derived
            if row["parent_source_artifact_id"] in artifact_ids
        ]
    source_key = {row["source_id"]: row["stable_key"] for row in sources}
    collection_key = {row["collection_id"]: row["stable_key"] for row in collections}
    artifact_digest = {row["artifact_id"]: row["sha256"] for row in artifacts}
    sources.sort(key=lambda row: (row["stable_key"], row["source_id"]))
    artifacts.sort(key=lambda row: (row["sha256"], row["artifact_id"]))
    collections.sort(key=lambda row: (row["stable_key"], row["collection_id"]))
    memberships.sort(
        key=lambda row: (
            collection_key.get(row["collection_id"], ""),
            source_key.get(row["source_id"], ""),
            row["membership_role"],
        )
    )
    locators.sort(
        key=lambda row: (
            source_key.get(row["source_id"], ""),
            row["locator_type"],
            row["locator"],
        )
    )
    events.sort(key=lambda row: (row["occurred_at"], row["ingestion_event_id"]))
    derived.sort(
        key=lambda row: (
            artifact_digest.get(row["parent_source_artifact_id"], ""),
            row["kind"],
            row["pipeline_key"],
            row["derived_artifact_id"],
        )
    )
    return {
        "format": "ADS_SOURCE_REGISTRY",
        "schema_version": 1,
        "export_profile": profile,
        "sources": sources,
        "artifacts": artifacts,
        "collections": collections,
        "memberships": memberships,
        "locators": locators,
        "ingestion_events": events,
        "derived_artifacts": derived,
    }


def _hash_stream(handle: BinaryIO) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    while True:
        block = handle.read(1024 * 1024)
        if not block:
            break
        digest.update(block)
        size += len(block)
    return digest.hexdigest(), size


def _hash_path(path: Path) -> tuple[str, int]:
    with path.open("rb") as handle:
        return _hash_stream(handle)


def _copy_and_hash(source: BinaryIO, destination: BinaryIO) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    while True:
        block = source.read(1024 * 1024)
        if not block:
            break
        destination.write(block)
        digest.update(block)
        size += len(block)
    destination.flush()
    return digest.hexdigest(), size


def _canonical_json_bytes(value: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
