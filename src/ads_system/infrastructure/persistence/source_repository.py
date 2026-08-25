"""SQLAlchemy Core repository for the Specification 023 Source Registry."""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from sqlalchemy import Connection, delete, insert, select, update

from ads_system.domain.source_universe import SourceArtifact, SourceCollection, SourceRecord
from ads_system.infrastructure.persistence.source_schema import (
    source_artifact,
    source_collection,
    source_derived_artifact,
    source_ingestion_event,
    source_locator,
    source_membership,
    source_record,
)


class SourceRegistryConflict(RuntimeError):
    """Raised when stable source identity conflicts with existing registry state."""


class SqlAlchemySourceRegistryRepository:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def get_source_by_stable_key(self, stable_key: str) -> SourceRecord | None:
        row = self.connection.execute(
            select(source_record).where(source_record.c.stable_key == stable_key)
        ).mappings().first()
        return None if row is None else self._source_value(row)

    def get_source(self, source_id: str) -> SourceRecord | None:
        row = self.connection.execute(
            select(source_record).where(source_record.c.source_id == source_id)
        ).mappings().first()
        return None if row is None else self._source_value(row)

    def create_source(self, values: Mapping[str, Any]) -> SourceRecord:
        self.connection.execute(insert(source_record).values(**dict(values)))
        result = self.get_source(str(values["source_id"]))
        assert result is not None
        return result

    def get_collection_by_stable_key(self, stable_key: str) -> SourceCollection | None:
        row = self.connection.execute(
            select(source_collection).where(source_collection.c.stable_key == stable_key)
        ).mappings().first()
        return None if row is None else self._collection_value(row)

    def get_collection(self, collection_id: str) -> SourceCollection | None:
        row = self.connection.execute(
            select(source_collection).where(source_collection.c.collection_id == collection_id)
        ).mappings().first()
        return None if row is None else self._collection_value(row)

    def create_collection(self, values: Mapping[str, Any]) -> SourceCollection:
        payload = dict(values)
        metadata = payload.get("metadata_json", {})
        if not isinstance(metadata, str):
            payload["metadata_json"] = json.dumps(
                metadata,
                sort_keys=True,
                separators=(",", ":"),
                ensure_ascii=False,
            )
        self.connection.execute(insert(source_collection).values(**payload))
        result = self.get_collection(str(values["collection_id"]))
        assert result is not None
        return result

    def get_artifact_by_sha256(self, sha256: str) -> SourceArtifact | None:
        row = self.connection.execute(
            select(source_artifact).where(source_artifact.c.sha256 == sha256)
        ).mappings().first()
        return None if row is None else self._artifact_value(row)

    def get_artifact(self, artifact_id: str) -> SourceArtifact | None:
        row = self.connection.execute(
            select(source_artifact).where(source_artifact.c.artifact_id == artifact_id)
        ).mappings().first()
        return None if row is None else self._artifact_value(row)

    def create_artifact(self, values: Mapping[str, Any]) -> SourceArtifact:
        self.connection.execute(insert(source_artifact).values(**dict(values)))
        result = self.get_artifact(str(values["artifact_id"]))
        assert result is not None
        return result

    def touch_artifact_verified(self, artifact_id: str, verified_at: str) -> None:
        self.connection.execute(
            update(source_artifact)
            .where(source_artifact.c.artifact_id == artifact_id)
            .values(last_verified_at=verified_at)
        )

    def upsert_membership(
        self,
        *,
        collection_id: str,
        source_id: str,
        membership_role: str,
        association_status: str,
        note: str | None,
    ) -> None:
        existing = self.connection.execute(
            select(source_membership).where(
                source_membership.c.collection_id == collection_id,
                source_membership.c.source_id == source_id,
                source_membership.c.membership_role == membership_role,
            )
        ).mappings().first()
        if existing is None:
            self.connection.execute(
                insert(source_membership).values(
                    collection_id=collection_id,
                    source_id=source_id,
                    membership_role=membership_role,
                    association_status=association_status,
                    note=note,
                )
            )
            return
        if existing["association_status"] != association_status or existing["note"] != note:
            self.connection.execute(
                update(source_membership)
                .where(
                    source_membership.c.collection_id == collection_id,
                    source_membership.c.source_id == source_id,
                    source_membership.c.membership_role == membership_role,
                )
                .values(association_status=association_status, note=note)
            )

    def add_locator(self, values: Mapping[str, Any]) -> None:
        duplicate = self.connection.execute(
            select(source_locator.c.locator_id).where(
                source_locator.c.source_id == values["source_id"],
                source_locator.c.artifact_id == values.get("artifact_id"),
                source_locator.c.locator_type == values["locator_type"],
                source_locator.c.locator == values["locator"],
            )
        ).first()
        if duplicate is None:
            self.connection.execute(insert(source_locator).values(**dict(values)))

    def add_ingestion_event(self, values: Mapping[str, Any]) -> None:
        self.connection.execute(insert(source_ingestion_event).values(**dict(values)))

    def add_derived_artifact(self, values: Mapping[str, Any]) -> None:
        self.connection.execute(insert(source_derived_artifact).values(**dict(values)))

    def list_preserved_artifacts(self) -> list[dict[str, Any]]:
        return [
            dict(row)
            for row in self.connection.execute(
                select(source_artifact).where(source_artifact.c.artifact_state == "PRESERVED")
            ).mappings().all()
        ]

    def counts(self) -> dict[str, int]:
        return {
            "sources": len(self.connection.execute(select(source_record.c.source_id)).all()),
            "artifacts": len(self.connection.execute(select(source_artifact.c.artifact_id)).all()),
            "collections": len(self.connection.execute(select(source_collection.c.collection_id)).all()),
            "memberships": len(self.connection.execute(select(source_membership.c.source_id)).all()),
            "locators": len(self.connection.execute(select(source_locator.c.locator_id)).all()),
            "ingestion_events": len(
                self.connection.execute(select(source_ingestion_event.c.ingestion_event_id)).all()
            ),
            "derived_artifacts": len(
                self.connection.execute(select(source_derived_artifact.c.derived_artifact_id)).all()
            ),
        }

    def export_rows(self) -> dict[str, list[dict[str, Any]]]:
        return {
            "sources": [dict(r) for r in self.connection.execute(select(source_record)).mappings().all()],
            "artifacts": [dict(r) for r in self.connection.execute(select(source_artifact)).mappings().all()],
            "collections": [dict(r) for r in self.connection.execute(select(source_collection)).mappings().all()],
            "memberships": [dict(r) for r in self.connection.execute(select(source_membership)).mappings().all()],
            "locators": [dict(r) for r in self.connection.execute(select(source_locator)).mappings().all()],
            "ingestion_events": [
                dict(r)
                for r in self.connection.execute(select(source_ingestion_event)).mappings().all()
            ],
            "derived_artifacts": [
                dict(r)
                for r in self.connection.execute(select(source_derived_artifact)).mappings().all()
            ],
        }

    def import_rows(self, snapshot: Mapping[str, Any]) -> None:
        self._validate_snapshot_references(snapshot)
        table_order = (
            (source_record, "sources"),
            (source_artifact, "artifacts"),
            (source_collection, "collections"),
            (source_membership, "memberships"),
            (source_locator, "locators"),
            (source_ingestion_event, "ingestion_events"),
            (source_derived_artifact, "derived_artifacts"),
        )
        for table, key in table_order:
            for row in snapshot.get(key, []):
                pk_columns = list(table.primary_key.columns)
                predicate = [column == row[column.name] for column in pk_columns]
                existing = self.connection.execute(select(table).where(*predicate)).mappings().first()
                if existing is None:
                    self.connection.execute(insert(table).values(**dict(row)))
                    continue
                existing_semantic = dict(existing)
                incoming = dict(row)
                if existing_semantic != incoming:
                    raise SourceRegistryConflict(
                        f"conflicting snapshot row for {table.name}: {incoming}"
                    )

    def clear_all(self) -> None:
        for table in (
            source_derived_artifact,
            source_ingestion_event,
            source_locator,
            source_membership,
            source_collection,
            source_artifact,
            source_record,
        ):
            self.connection.execute(delete(table))

    @staticmethod
    def _validate_snapshot_references(snapshot: Mapping[str, Any]) -> None:
        source_ids = {row["source_id"] for row in snapshot.get("sources", [])}
        artifact_ids = {row["artifact_id"] for row in snapshot.get("artifacts", [])}
        collection_ids = {row["collection_id"] for row in snapshot.get("collections", [])}
        source_keys: dict[str, str] = {}
        artifact_digests: dict[str, int] = {}
        for row in snapshot.get("sources", []):
            key = row["stable_key"]
            if key in source_keys and source_keys[key] != row["source_id"]:
                raise SourceRegistryConflict(f"stable_key identity conflict: {key}")
            source_keys[key] = row["source_id"]
        for row in snapshot.get("artifacts", []):
            if row["source_id"] not in source_ids:
                raise SourceRegistryConflict("artifact references missing source")
            digest = row["sha256"]
            size = int(row["byte_size"])
            if digest in artifact_digests and artifact_digests[digest] != size:
                raise SourceRegistryConflict("same digest has conflicting byte size")
            artifact_digests[digest] = size
        for row in snapshot.get("memberships", []):
            if row["source_id"] not in source_ids or row["collection_id"] not in collection_ids:
                raise SourceRegistryConflict("membership references missing identity")
        for row in snapshot.get("locators", []):
            if row["source_id"] not in source_ids:
                raise SourceRegistryConflict("locator references missing source")
            if row.get("artifact_id") is not None and row["artifact_id"] not in artifact_ids:
                raise SourceRegistryConflict("locator references missing artifact")
        for row in snapshot.get("ingestion_events", []):
            if row["source_id"] not in source_ids:
                raise SourceRegistryConflict("ingestion event references missing source")
            if row.get("artifact_id") is not None and row["artifact_id"] not in artifact_ids:
                raise SourceRegistryConflict("ingestion event references missing artifact")
            if row.get("collection_id") is not None and row["collection_id"] not in collection_ids:
                raise SourceRegistryConflict("ingestion event references missing collection")
        for row in snapshot.get("derived_artifacts", []):
            if row["parent_source_artifact_id"] not in artifact_ids:
                raise SourceRegistryConflict("derived artifact references missing source artifact")

    @staticmethod
    def _source_value(row: Mapping[str, Any]) -> SourceRecord:
        return SourceRecord(
            source_id=str(row["source_id"]),
            stable_key=row["stable_key"],
            title=row["title"],
            source_type=row["source_type"],
            canonical_locator=row["canonical_locator"],
            access_class=row["access_class"],
            redistribution_status=row["redistribution_status"],
            metadata_visibility=row["metadata_visibility"],
        )

    @staticmethod
    def _artifact_value(row: Mapping[str, Any]) -> SourceArtifact:
        return SourceArtifact(
            artifact_id=str(row["artifact_id"]),
            source_id=str(row["source_id"]),
            sha256=row["sha256"],
            byte_size=int(row["byte_size"]),
            media_type=row["media_type"],
            artifact_state=row["artifact_state"],
        )

    @staticmethod
    def _collection_value(row: Mapping[str, Any]) -> SourceCollection:
        return SourceCollection(
            collection_id=str(row["collection_id"]),
            stable_key=row["stable_key"],
            title=row["title"],
            collection_type=row["collection_type"],
        )
