"""SQLAlchemy Core adapter for Specification 004 knowledge interchange.

The adapter deliberately keeps candidate import, explicit acceptance, and
accepted-snapshot export separate. Interchange parsing and schema validation
happen outside database transactions in the application service.
"""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from typing import Any

from sqlalchemy import Connection, delete, insert, select, update

from ads_system.infrastructure.persistence.interchange_schema import (
    kg_collection,
    kg_collection_member,
    kg_content_revision_extension,
    kg_content_revision_provenance,
    kg_provenance_source,
    kg_relation_governance_event,
    kg_relation_revision_provenance,
    kg_relation_revision_state,
    kg_rule_provenance,
)
from ads_system.infrastructure.persistence.schema import (
    kg_asset,
    kg_asset_revision,
    kg_component,
    kg_component_revision,
    kg_content_revision,
    kg_governance_event,
    kg_node,
    kg_relation,
    kg_relation_current,
    kg_relation_revision,
    kg_revision_governance,
    kg_rule_spec,
)
from ads_system.infrastructure.persistence.types import (
    canonical_json,
    new_id,
    semantic_hash,
    utc_now_text,
)


class KnowledgePersistenceConflict(ValueError):
    """Raised when imported knowledge conflicts with durable identity/history."""


class SqlAlchemyKnowledgeInterchangeRepository:
    """Persist validated reusable-knowledge bundles behind application ports."""

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    # ------------------------------------------------------------------
    # Candidate import
    # ------------------------------------------------------------------

    def import_provenance_source(self, source: Mapping[str, Any]) -> None:
        existing = self._connection.execute(
            select(kg_provenance_source).where(
                kg_provenance_source.c.source_id == source["source_id"]
            )
        ).mappings().first()
        values = {
            "source_id": source["source_id"],
            "source_type": source["source_type"],
            "title": source["title"],
            "locator": source["locator"],
            "version_or_fingerprint": source["version_or_fingerprint"],
            "notes": source["notes"],
        }
        if existing is None:
            self._connection.execute(insert(kg_provenance_source).values(**values))
            return
        if dict(existing) != values:
            raise KnowledgePersistenceConflict(
                f"Provenance source {source['source_id']!r} already exists with different content."
            )

    def import_asset_revision(self, asset: Mapping[str, Any], *, actor: str) -> None:
        self._ensure_asset_identity(asset)
        extension = {
            "limitations": asset["limitations"],
            "reasoning_functions": asset["reasoning_functions"],
            "retrieval_profile": asset["retrieval_profile"],
            "context_requirements": asset["context_requirements"],
            "applicability": asset["applicability"],
            "semantic_checks": asset["semantic_checks"],
            "narrative_facets": asset["narrative_facets"],
        }
        digest = semantic_hash(
            {
                "intrinsic_kind": asset["intrinsic_kind"],
                "title": asset["title"],
                "purpose": asset["purpose"],
                "scope": asset["scope"],
                "extension": extension,
            }
        )

        existing = self._existing_content_revision(asset["revision_id"])
        if existing is not None:
            self._assert_existing_content_revision(
                existing,
                node_id=asset["asset_id"],
                revision_no=asset["revision_no"],
                semantic_content_hash=digest,
                governance_status=asset["governance_status"],
            )
            return

        self._assert_revision_number_available(
            asset["asset_id"], asset["revision_no"], asset["revision_id"]
        )
        now = utc_now_text()
        self._connection.execute(
            insert(kg_content_revision).values(
                revision_id=asset["revision_id"],
                node_id=asset["asset_id"],
                revision_no=asset["revision_no"],
                created_at=now,
                semantic_content_hash=digest,
            )
        )
        self._connection.execute(
            insert(kg_asset_revision).values(
                revision_id=asset["revision_id"],
                asset_id=asset["asset_id"],
                intrinsic_kind=asset["intrinsic_kind"],
                title=asset["title"],
                purpose=asset["purpose"],
                scope_text=asset["scope"],
                limitations_text=None,
            )
        )
        self._connection.execute(
            insert(kg_content_revision_extension).values(
                revision_id=asset["revision_id"],
                schema_version=1,
                structured_json=canonical_json(extension),
            )
        )
        self._insert_content_governance(
            revision_id=asset["revision_id"],
            status=asset["governance_status"],
            actor=actor,
            note="Imported reusable-knowledge asset revision",
            now=now,
        )
        self._sync_content_provenance(
            asset["revision_id"], asset["provenance_source_ids"]
        )

    def import_component_revision(
        self,
        *,
        parent_asset_revision_id: str,
        component: Mapping[str, Any],
        actor: str,
    ) -> None:
        parent_asset_id = self._connection.execute(
            select(kg_asset_revision.c.asset_id).where(
                kg_asset_revision.c.revision_id == parent_asset_revision_id
            )
        ).scalar_one()
        self._ensure_component_identity(parent_asset_id, component)

        extension = {"reasoning_functions": component["reasoning_functions"]}
        digest = semantic_hash(
            {
                "component_kind": component["component_kind"],
                "body": component["body"],
                "payload": component["payload"],
                "parent_asset_revision_id": parent_asset_revision_id,
                "extension": extension,
            }
        )
        existing = self._existing_content_revision(component["revision_id"])
        if existing is not None:
            self._assert_existing_content_revision(
                existing,
                node_id=component["component_id"],
                revision_no=component["revision_no"],
                semantic_content_hash=digest,
                governance_status=component["governance_status"],
            )
            return

        self._assert_revision_number_available(
            component["component_id"],
            component["revision_no"],
            component["revision_id"],
        )
        now = utc_now_text()
        self._connection.execute(
            insert(kg_content_revision).values(
                revision_id=component["revision_id"],
                node_id=component["component_id"],
                revision_no=component["revision_no"],
                created_at=now,
                semantic_content_hash=digest,
            )
        )
        self._connection.execute(
            insert(kg_component_revision).values(
                revision_id=component["revision_id"],
                component_id=component["component_id"],
                parent_asset_id=parent_asset_id,
                parent_asset_revision_id=parent_asset_revision_id,
                body_text=component["body"],
                payload_json=(
                    canonical_json(component["payload"])
                    if component["payload"] is not None
                    else None
                ),
                position=0,
            )
        )
        self._connection.execute(
            insert(kg_content_revision_extension).values(
                revision_id=component["revision_id"],
                schema_version=1,
                structured_json=canonical_json(extension),
            )
        )
        self._insert_content_governance(
            revision_id=component["revision_id"],
            status=component["governance_status"],
            actor=actor,
            note="Imported reusable-knowledge component revision",
            now=now,
        )
        self._sync_content_provenance(
            component["revision_id"], component["provenance_source_ids"]
        )

    def import_rule(
        self,
        *,
        owner_content_revision_id: str,
        rule: Mapping[str, Any],
    ) -> None:
        values = {
            "rule_spec_id": rule["rule_spec_id"],
            "owner_content_revision_id": owner_content_revision_id,
            "rule_key": rule["rule_key"],
            "condition_json": canonical_json(rule["condition"]),
            "consequence_type": rule["consequence_type"],
            "consequence_payload_json": (
                canonical_json(rule["consequence_payload"])
                if rule["consequence_payload"] is not None
                else None
            ),
            "force": rule["force"],
            "unknown_behavior": rule["unknown_behavior"],
            "rationale_text": rule["rationale"],
        }
        existing = self._connection.execute(
            select(kg_rule_spec).where(
                kg_rule_spec.c.rule_spec_id == rule["rule_spec_id"]
            )
        ).mappings().first()
        existing_key = self._connection.execute(
            select(kg_rule_spec.c.rule_spec_id).where(
                kg_rule_spec.c.owner_content_revision_id == owner_content_revision_id,
                kg_rule_spec.c.rule_key == rule["rule_key"],
            )
        ).scalar_one_or_none()
        if existing is not None:
            if dict(existing) != values:
                raise KnowledgePersistenceConflict(
                    f"Rule {rule['rule_spec_id']} already exists with different content."
                )
        else:
            if existing_key is not None and existing_key != rule["rule_spec_id"]:
                raise KnowledgePersistenceConflict(
                    f"Rule key {rule['rule_key']!r} already has a different durable identity."
                )
            self._connection.execute(insert(kg_rule_spec).values(**values))
        self._sync_rule_provenance(
            rule["rule_spec_id"], rule["provenance_source_ids"]
        )

    def import_relation_revision(
        self,
        relation: Mapping[str, Any],
        *,
        source_node_id: str,
        target_node_id: str,
        actor: str,
    ) -> None:
        relation_identity = self._connection.execute(
            select(kg_relation).where(
                kg_relation.c.relation_id == relation["relation_id"]
            )
        ).mappings().first()
        if relation_identity is None:
            self._connection.execute(
                insert(kg_relation).values(
                    relation_id=relation["relation_id"],
                    source_node_id=source_node_id,
                    target_node_id=target_node_id,
                    relation_type=relation["relation_type"],
                    created_at=utc_now_text(),
                )
            )
        else:
            expected = {
                "relation_id": relation["relation_id"],
                "source_node_id": source_node_id,
                "target_node_id": target_node_id,
                "relation_type": relation["relation_type"],
                "created_at": relation_identity["created_at"],
            }
            if dict(relation_identity) != expected:
                raise KnowledgePersistenceConflict(
                    f"Relation {relation['relation_id']} identity conflicts with existing endpoints/type."
                )

        digest = semantic_hash(
            {
                "relation_type": relation["relation_type"],
                "source_node_id": source_node_id,
                "target_node_id": target_node_id,
                "scope": relation["scope"],
                "rationale": relation["rationale"],
            }
        )
        existing_revision = self._connection.execute(
            select(kg_relation_revision).where(
                kg_relation_revision.c.relation_revision_id
                == relation["relation_revision_id"]
            )
        ).mappings().first()
        if existing_revision is not None:
            state = self._connection.execute(
                select(kg_relation_revision_state).where(
                    kg_relation_revision_state.c.relation_revision_id
                    == relation["relation_revision_id"]
                )
            ).mappings().one()
            if (
                existing_revision["relation_id"] != relation["relation_id"]
                or existing_revision["revision_no"] != relation["revision_no"]
                or existing_revision["scope_text"] != relation["scope"]
                or existing_revision["rationale_text"] != relation["rationale"]
                or state["semantic_content_hash"] != digest
                or state["governance_status"] != relation["governance_status"]
            ):
                raise KnowledgePersistenceConflict(
                    f"Relation revision {relation['relation_revision_id']} conflicts with existing content."
                )
            return

        number_collision = self._connection.execute(
            select(kg_relation_revision.c.relation_revision_id).where(
                kg_relation_revision.c.relation_id == relation["relation_id"],
                kg_relation_revision.c.revision_no == relation["revision_no"],
            )
        ).scalar_one_or_none()
        if number_collision is not None:
            raise KnowledgePersistenceConflict(
                f"Relation {relation['relation_id']} revision number {relation['revision_no']} is already used."
            )

        now = utc_now_text()
        self._connection.execute(
            insert(kg_relation_revision).values(
                relation_revision_id=relation["relation_revision_id"],
                relation_id=relation["relation_id"],
                revision_no=relation["revision_no"],
                scope_text=relation["scope"],
                rationale_text=relation["rationale"],
                created_at=now,
            )
        )
        self._connection.execute(
            insert(kg_relation_revision_state).values(
                relation_revision_id=relation["relation_revision_id"],
                governance_status=relation["governance_status"],
                semantic_content_hash=digest,
                updated_at=now,
            )
        )
        self._connection.execute(
            insert(kg_relation_governance_event).values(
                event_id=new_id(),
                relation_revision_id=relation["relation_revision_id"],
                from_status=None,
                to_status=relation["governance_status"],
                actor=actor,
                occurred_at=now,
                note_text="Imported reusable-knowledge relation revision",
            )
        )
        self._sync_relation_provenance(
            relation["relation_revision_id"], relation["provenance_source_ids"]
        )

    # ------------------------------------------------------------------
    # Explicit acceptance
    # ------------------------------------------------------------------

    def accept_content_revision(self, revision_id: str, *, actor: str) -> None:
        row = self._connection.execute(
            select(
                kg_content_revision.c.node_id,
                kg_revision_governance.c.current_status,
                kg_node.c.node_type,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_content_revision.c.revision_id,
            )
            .join(kg_node, kg_node.c.node_id == kg_content_revision.c.node_id)
            .where(kg_content_revision.c.revision_id == revision_id)
        ).mappings().one()
        if row["current_status"] == "ACCEPTED":
            if row["node_type"] == "ASSET":
                self._set_asset_current(row["node_id"], revision_id)
            return
        if row["current_status"] not in {"CANDIDATE", "REVIEWED"}:
            raise KnowledgePersistenceConflict(
                f"Revision {revision_id} cannot be accepted from status {row['current_status']}."
            )

        now = utc_now_text()
        previous = self._connection.execute(
            select(kg_revision_governance.c.revision_id)
            .join(
                kg_content_revision,
                kg_content_revision.c.revision_id
                == kg_revision_governance.c.revision_id,
            )
            .where(
                kg_content_revision.c.node_id == row["node_id"],
                kg_revision_governance.c.current_status == "ACCEPTED",
                kg_revision_governance.c.revision_id != revision_id,
            )
        ).scalars().all()
        for previous_revision_id in previous:
            self._transition_content_status(
                previous_revision_id,
                from_status="ACCEPTED",
                to_status="SUPERSEDED",
                actor=actor,
                note=f"Superseded by revision {revision_id}",
                now=now,
            )
        self._transition_content_status(
            revision_id,
            from_status=row["current_status"],
            to_status="ACCEPTED",
            actor=actor,
            note="Explicitly accepted reusable-knowledge revision",
            now=now,
        )
        if row["node_type"] == "ASSET":
            self._set_asset_current(row["node_id"], revision_id)

    def accept_relation_revision(self, relation_revision_id: str, *, actor: str) -> None:
        row = self._connection.execute(
            select(
                kg_relation_revision.c.relation_id,
                kg_relation_revision_state.c.governance_status,
            )
            .join(
                kg_relation_revision_state,
                kg_relation_revision_state.c.relation_revision_id
                == kg_relation_revision.c.relation_revision_id,
            )
            .where(
                kg_relation_revision.c.relation_revision_id == relation_revision_id
            )
        ).mappings().one()
        if row["governance_status"] == "ACCEPTED":
            self._set_relation_current(row["relation_id"], relation_revision_id)
            return
        if row["governance_status"] not in {"CANDIDATE", "REVIEWED"}:
            raise KnowledgePersistenceConflict(
                f"Relation revision {relation_revision_id} cannot be accepted from status {row['governance_status']}."
            )

        now = utc_now_text()
        current = self._connection.execute(
            select(kg_relation_current.c.relation_revision_id).where(
                kg_relation_current.c.relation_id == row["relation_id"]
            )
        ).scalar_one_or_none()
        if current is not None and current != relation_revision_id:
            current_status = self._connection.execute(
                select(kg_relation_revision_state.c.governance_status).where(
                    kg_relation_revision_state.c.relation_revision_id == current
                )
            ).scalar_one()
            self._transition_relation_status(
                current,
                from_status=current_status,
                to_status="SUPERSEDED",
                actor=actor,
                note=f"Superseded by relation revision {relation_revision_id}",
                now=now,
            )
        self._transition_relation_status(
            relation_revision_id,
            from_status=row["governance_status"],
            to_status="ACCEPTED",
            actor=actor,
            note="Explicitly accepted reusable-knowledge relation revision",
            now=now,
        )
        self._set_relation_current(row["relation_id"], relation_revision_id)

    def sync_collection(
        self,
        *,
        collection_key: str,
        title: str,
        node_ids: Sequence[str],
    ) -> None:
        existing = self._connection.execute(
            select(kg_collection.c.collection_key).where(
                kg_collection.c.collection_key == collection_key
            )
        ).scalar_one_or_none()
        if existing is None:
            self._connection.execute(
                insert(kg_collection).values(
                    collection_key=collection_key,
                    title=title,
                )
            )
        else:
            self._connection.execute(
                update(kg_collection)
                .where(kg_collection.c.collection_key == collection_key)
                .values(title=title)
            )
        self._connection.execute(
            delete(kg_collection_member).where(
                kg_collection_member.c.collection_key == collection_key
            )
        )
        for node_id in sorted(set(node_ids)):
            self._connection.execute(
                insert(kg_collection_member).values(
                    collection_key=collection_key,
                    node_id=node_id,
                )
            )

    # ------------------------------------------------------------------
    # Accepted snapshot export
    # ------------------------------------------------------------------

    def export_current_accepted_snapshot(self) -> dict[str, Any]:
        assets: list[dict[str, Any]] = []
        included_nodes: set[str] = set()
        referenced_sources: set[str] = set()

        asset_rows = self._connection.execute(
            select(
                kg_asset.c.asset_id,
                kg_asset.c.stable_key,
                kg_asset.c.current_accepted_revision_id,
                kg_content_revision.c.revision_no,
                kg_asset_revision.c.intrinsic_kind,
                kg_asset_revision.c.title,
                kg_asset_revision.c.purpose,
                kg_asset_revision.c.scope_text,
                kg_asset_revision.c.limitations_text,
            )
            .join(
                kg_content_revision,
                kg_content_revision.c.revision_id
                == kg_asset.c.current_accepted_revision_id,
            )
            .join(
                kg_asset_revision,
                kg_asset_revision.c.revision_id
                == kg_content_revision.c.revision_id,
            )
            .order_by(kg_asset.c.stable_key)
        ).mappings().all()

        for row in asset_rows:
            revision_id = row["current_accepted_revision_id"]
            extension = self._content_extension(revision_id, node_type="ASSET")
            provenance = self._content_provenance(revision_id)
            referenced_sources.update(provenance)
            components = self._accepted_components_for_asset_revision(revision_id)
            for component in components:
                included_nodes.add(component["component_id"])
                referenced_sources.update(component["provenance_source_ids"])
            rules = self._rules_for_revision(revision_id)
            for rule in rules:
                referenced_sources.update(rule["provenance_source_ids"])

            included_nodes.add(row["asset_id"])
            assets.append(
                {
                    "asset_id": row["asset_id"],
                    "stable_key": row["stable_key"],
                    "revision_id": revision_id,
                    "revision_no": row["revision_no"],
                    "governance_status": "ACCEPTED",
                    "intrinsic_kind": row["intrinsic_kind"],
                    "title": row["title"],
                    "purpose": row["purpose"],
                    "scope": row["scope_text"],
                    "limitations": extension.get(
                        "limitations",
                        [row["limitations_text"]] if row["limitations_text"] else [],
                    ),
                    "reasoning_functions": extension.get("reasoning_functions", []),
                    "retrieval_profile": extension.get(
                        "retrieval_profile",
                        {
                            "aliases": [],
                            "lexical_terms": [],
                            "semantic_cues": [],
                            "negative_cues": [],
                        },
                    ),
                    "context_requirements": extension.get(
                        "context_requirements", []
                    ),
                    "applicability": extension.get("applicability"),
                    "semantic_checks": extension.get("semantic_checks", []),
                    "narrative_facets": extension.get("narrative_facets", []),
                    "components": components,
                    "rules": rules,
                    "provenance_source_ids": provenance,
                }
            )

        relations = self._accepted_relations(included_nodes)
        for relation in relations:
            referenced_sources.update(relation["provenance_source_ids"])
        collections = self._collections_for_nodes(included_nodes)
        sources = self._provenance_sources(referenced_sources)

        return {
            "format": "ads-reusable-knowledge-bundle",
            "schema_version": 1,
            "bundle_kind": "ACCEPTED_SNAPSHOT",
            "assets": assets,
            "relations": relations,
            "provenance_sources": sources,
            "collections": collections,
        }

    # ------------------------------------------------------------------
    # Identity and conflict helpers
    # ------------------------------------------------------------------

    def _ensure_asset_identity(self, asset: Mapping[str, Any]) -> None:
        by_key = self._connection.execute(
            select(kg_asset.c.asset_id).where(
                kg_asset.c.stable_key == asset["stable_key"]
            )
        ).scalar_one_or_none()
        by_id = self._connection.execute(
            select(kg_asset.c.stable_key).where(
                kg_asset.c.asset_id == asset["asset_id"]
            )
        ).scalar_one_or_none()
        if by_key is not None and by_key != asset["asset_id"]:
            raise KnowledgePersistenceConflict(
                f"Stable key {asset['stable_key']!r} already belongs to a different asset_id."
            )
        if by_id is not None and by_id != asset["stable_key"]:
            raise KnowledgePersistenceConflict(
                f"Asset ID {asset['asset_id']} already belongs to stable key {by_id!r}."
            )
        if by_key is None and by_id is None:
            now = utc_now_text()
            self._connection.execute(
                insert(kg_node).values(
                    node_id=asset["asset_id"],
                    node_type="ASSET",
                    created_at=now,
                )
            )
            self._connection.execute(
                insert(kg_asset).values(
                    asset_id=asset["asset_id"],
                    stable_key=asset["stable_key"],
                    current_accepted_revision_id=None,
                    created_at=now,
                )
            )

    def _ensure_component_identity(
        self,
        parent_asset_id: str,
        component: Mapping[str, Any],
    ) -> None:
        by_key = self._connection.execute(
            select(kg_component).where(
                kg_component.c.parent_asset_id == parent_asset_id,
                kg_component.c.component_key == component["component_key"],
            )
        ).mappings().first()
        by_id = self._connection.execute(
            select(kg_component).where(
                kg_component.c.component_id == component["component_id"]
            )
        ).mappings().first()
        for existing in (by_key, by_id):
            if existing is not None and (
                existing["component_id"] != component["component_id"]
                or existing["parent_asset_id"] != parent_asset_id
                or existing["component_key"] != component["component_key"]
                or existing["component_kind"] != component["component_kind"]
            ):
                raise KnowledgePersistenceConflict(
                    f"Component {component['component_key']!r} conflicts with existing durable identity."
                )
        if by_key is None and by_id is None:
            now = utc_now_text()
            self._connection.execute(
                insert(kg_node).values(
                    node_id=component["component_id"],
                    node_type="COMPONENT",
                    created_at=now,
                )
            )
            self._connection.execute(
                insert(kg_component).values(
                    component_id=component["component_id"],
                    parent_asset_id=parent_asset_id,
                    component_key=component["component_key"],
                    component_kind=component["component_kind"],
                    created_at=now,
                )
            )

    def _existing_content_revision(self, revision_id: str):
        return self._connection.execute(
            select(
                kg_content_revision.c.revision_id,
                kg_content_revision.c.node_id,
                kg_content_revision.c.revision_no,
                kg_content_revision.c.semantic_content_hash,
                kg_revision_governance.c.current_status,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_content_revision.c.revision_id,
            )
            .where(kg_content_revision.c.revision_id == revision_id)
        ).mappings().first()

    def _assert_existing_content_revision(
        self,
        existing,
        *,
        node_id: str,
        revision_no: int,
        semantic_content_hash: str,
        governance_status: str,
    ) -> None:
        if (
            existing["node_id"] != node_id
            or existing["revision_no"] != revision_no
            or existing["semantic_content_hash"] != semantic_content_hash
            or existing["current_status"] != governance_status
        ):
            raise KnowledgePersistenceConflict(
                f"Revision {existing['revision_id']} already exists with conflicting identity, content, or governance."
            )

    def _assert_revision_number_available(
        self, node_id: str, revision_no: int, revision_id: str
    ) -> None:
        existing = self._connection.execute(
            select(kg_content_revision.c.revision_id).where(
                kg_content_revision.c.node_id == node_id,
                kg_content_revision.c.revision_no == revision_no,
            )
        ).scalar_one_or_none()
        if existing is not None and existing != revision_id:
            raise KnowledgePersistenceConflict(
                f"Node {node_id} revision number {revision_no} is already used by {existing}."
            )

    # ------------------------------------------------------------------
    # Governance helpers
    # ------------------------------------------------------------------

    def _insert_content_governance(
        self,
        *,
        revision_id: str,
        status: str,
        actor: str,
        note: str,
        now: str,
    ) -> None:
        self._connection.execute(
            insert(kg_revision_governance).values(
                revision_id=revision_id,
                current_status=status,
                updated_at=now,
            )
        )
        self._connection.execute(
            insert(kg_governance_event).values(
                event_id=new_id(),
                revision_id=revision_id,
                from_status=None,
                to_status=status,
                actor=actor,
                occurred_at=now,
                note_text=note,
            )
        )

    def _transition_content_status(
        self,
        revision_id: str,
        *,
        from_status: str,
        to_status: str,
        actor: str,
        note: str,
        now: str,
    ) -> None:
        self._connection.execute(
            update(kg_revision_governance)
            .where(kg_revision_governance.c.revision_id == revision_id)
            .values(current_status=to_status, updated_at=now)
        )
        self._connection.execute(
            insert(kg_governance_event).values(
                event_id=new_id(),
                revision_id=revision_id,
                from_status=from_status,
                to_status=to_status,
                actor=actor,
                occurred_at=now,
                note_text=note,
            )
        )

    def _transition_relation_status(
        self,
        relation_revision_id: str,
        *,
        from_status: str,
        to_status: str,
        actor: str,
        note: str,
        now: str,
    ) -> None:
        self._connection.execute(
            update(kg_relation_revision_state)
            .where(
                kg_relation_revision_state.c.relation_revision_id
                == relation_revision_id
            )
            .values(governance_status=to_status, updated_at=now)
        )
        self._connection.execute(
            insert(kg_relation_governance_event).values(
                event_id=new_id(),
                relation_revision_id=relation_revision_id,
                from_status=from_status,
                to_status=to_status,
                actor=actor,
                occurred_at=now,
                note_text=note,
            )
        )

    def _set_asset_current(self, asset_id: str, revision_id: str) -> None:
        self._connection.execute(
            update(kg_asset)
            .where(kg_asset.c.asset_id == asset_id)
            .values(current_accepted_revision_id=revision_id)
        )

    def _set_relation_current(
        self, relation_id: str, relation_revision_id: str
    ) -> None:
        existing = self._connection.execute(
            select(kg_relation_current.c.relation_id).where(
                kg_relation_current.c.relation_id == relation_id
            )
        ).scalar_one_or_none()
        if existing is None:
            self._connection.execute(
                insert(kg_relation_current).values(
                    relation_id=relation_id,
                    relation_revision_id=relation_revision_id,
                )
            )
        else:
            self._connection.execute(
                update(kg_relation_current)
                .where(kg_relation_current.c.relation_id == relation_id)
                .values(relation_revision_id=relation_revision_id)
            )

    # ------------------------------------------------------------------
    # Provenance helpers
    # ------------------------------------------------------------------

    def _sync_content_provenance(
        self, revision_id: str, source_ids: Sequence[str]
    ) -> None:
        self._sync_link_rows(
            table=kg_content_revision_provenance,
            owner_column=kg_content_revision_provenance.c.revision_id,
            owner_value=revision_id,
            source_column=kg_content_revision_provenance.c.source_id,
            source_ids=source_ids,
        )

    def _sync_rule_provenance(self, rule_spec_id: str, source_ids: Sequence[str]) -> None:
        self._sync_link_rows(
            table=kg_rule_provenance,
            owner_column=kg_rule_provenance.c.rule_spec_id,
            owner_value=rule_spec_id,
            source_column=kg_rule_provenance.c.source_id,
            source_ids=source_ids,
        )

    def _sync_relation_provenance(
        self, relation_revision_id: str, source_ids: Sequence[str]
    ) -> None:
        self._sync_link_rows(
            table=kg_relation_revision_provenance,
            owner_column=kg_relation_revision_provenance.c.relation_revision_id,
            owner_value=relation_revision_id,
            source_column=kg_relation_revision_provenance.c.source_id,
            source_ids=source_ids,
        )

    def _sync_link_rows(
        self,
        *,
        table,
        owner_column,
        owner_value: str,
        source_column,
        source_ids: Sequence[str],
    ) -> None:
        existing = set(
            self._connection.execute(
                select(source_column).where(owner_column == owner_value)
            ).scalars()
        )
        expected = set(source_ids)
        if existing - expected:
            raise KnowledgePersistenceConflict(
                f"Existing provenance links for {owner_value} conflict with imported revision."
            )
        for source_id in sorted(expected - existing):
            self._connection.execute(
                insert(table).values(
                    **{
                        owner_column.name: owner_value,
                        source_column.name: source_id,
                    }
                )
            )

    # ------------------------------------------------------------------
    # Snapshot helpers
    # ------------------------------------------------------------------

    def _content_extension(self, revision_id: str, *, node_type: str) -> dict[str, Any]:
        raw = self._connection.execute(
            select(kg_content_revision_extension.c.structured_json).where(
                kg_content_revision_extension.c.revision_id == revision_id
            )
        ).scalar_one_or_none()
        if raw is not None:
            return json.loads(raw)
        if node_type == "ASSET":
            return {
                "limitations": [],
                "reasoning_functions": [],
                "retrieval_profile": {
                    "aliases": [],
                    "lexical_terms": [],
                    "semantic_cues": [],
                    "negative_cues": [],
                },
                "context_requirements": [],
                "applicability": None,
                "semantic_checks": [],
                "narrative_facets": [],
            }
        return {"reasoning_functions": []}

    def _content_provenance(self, revision_id: str) -> list[str]:
        return list(
            self._connection.execute(
                select(kg_content_revision_provenance.c.source_id)
                .where(kg_content_revision_provenance.c.revision_id == revision_id)
                .order_by(kg_content_revision_provenance.c.source_id)
            ).scalars()
        )

    def _accepted_components_for_asset_revision(
        self, parent_asset_revision_id: str
    ) -> list[dict[str, Any]]:
        rows = self._connection.execute(
            select(
                kg_component.c.component_id,
                kg_component.c.component_key,
                kg_component.c.component_kind,
                kg_component_revision.c.revision_id,
                kg_content_revision.c.revision_no,
                kg_component_revision.c.body_text,
                kg_component_revision.c.payload_json,
            )
            .join(
                kg_component_revision,
                kg_component_revision.c.component_id == kg_component.c.component_id,
            )
            .join(
                kg_content_revision,
                kg_content_revision.c.revision_id
                == kg_component_revision.c.revision_id,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_component_revision.c.revision_id,
            )
            .where(
                kg_component_revision.c.parent_asset_revision_id
                == parent_asset_revision_id,
                kg_revision_governance.c.current_status == "ACCEPTED",
            )
            .order_by(kg_component.c.component_key)
        ).mappings().all()
        result: list[dict[str, Any]] = []
        for row in rows:
            extension = self._content_extension(row["revision_id"], node_type="COMPONENT")
            result.append(
                {
                    "component_id": row["component_id"],
                    "component_key": row["component_key"],
                    "component_kind": row["component_kind"],
                    "revision_id": row["revision_id"],
                    "revision_no": row["revision_no"],
                    "governance_status": "ACCEPTED",
                    "body": row["body_text"],
                    "payload": (
                        json.loads(row["payload_json"])
                        if row["payload_json"] is not None
                        else None
                    ),
                    "reasoning_functions": extension.get("reasoning_functions", []),
                    "provenance_source_ids": self._content_provenance(
                        row["revision_id"]
                    ),
                }
            )
        return result

    def _rules_for_revision(self, revision_id: str) -> list[dict[str, Any]]:
        rows = self._connection.execute(
            select(kg_rule_spec)
            .where(kg_rule_spec.c.owner_content_revision_id == revision_id)
            .order_by(kg_rule_spec.c.rule_key)
        ).mappings().all()
        result: list[dict[str, Any]] = []
        for row in rows:
            provenance = list(
                self._connection.execute(
                    select(kg_rule_provenance.c.source_id)
                    .where(kg_rule_provenance.c.rule_spec_id == row["rule_spec_id"])
                    .order_by(kg_rule_provenance.c.source_id)
                ).scalars()
            )
            result.append(
                {
                    "rule_spec_id": row["rule_spec_id"],
                    "rule_key": row["rule_key"],
                    "condition": json.loads(row["condition_json"]),
                    "consequence_type": row["consequence_type"],
                    "consequence_payload": (
                        json.loads(row["consequence_payload_json"])
                        if row["consequence_payload_json"] is not None
                        else None
                    ),
                    "force": row["force"],
                    "unknown_behavior": row["unknown_behavior"],
                    "rationale": row["rationale_text"],
                    "provenance_source_ids": provenance,
                }
            )
        return result

    def _accepted_relations(self, included_nodes: set[str]) -> list[dict[str, Any]]:
        rows = self._connection.execute(
            select(
                kg_relation.c.relation_id,
                kg_relation.c.source_node_id,
                kg_relation.c.target_node_id,
                kg_relation.c.relation_type,
                kg_relation_revision.c.relation_revision_id,
                kg_relation_revision.c.revision_no,
                kg_relation_revision.c.scope_text,
                kg_relation_revision.c.rationale_text,
            )
            .join(
                kg_relation_current,
                kg_relation_current.c.relation_id == kg_relation.c.relation_id,
            )
            .join(
                kg_relation_revision,
                kg_relation_revision.c.relation_revision_id
                == kg_relation_current.c.relation_revision_id,
            )
            .join(
                kg_relation_revision_state,
                kg_relation_revision_state.c.relation_revision_id
                == kg_relation_revision.c.relation_revision_id,
            )
            .where(kg_relation_revision_state.c.governance_status == "ACCEPTED")
        ).mappings().all()
        result: list[dict[str, Any]] = []
        for row in rows:
            if (
                row["source_node_id"] not in included_nodes
                or row["target_node_id"] not in included_nodes
            ):
                continue
            provenance = list(
                self._connection.execute(
                    select(kg_relation_revision_provenance.c.source_id)
                    .where(
                        kg_relation_revision_provenance.c.relation_revision_id
                        == row["relation_revision_id"]
                    )
                    .order_by(kg_relation_revision_provenance.c.source_id)
                ).scalars()
            )
            result.append(
                {
                    "relation_id": row["relation_id"],
                    "relation_revision_id": row["relation_revision_id"],
                    "revision_no": row["revision_no"],
                    "governance_status": "ACCEPTED",
                    "source_ref": self._node_ref(row["source_node_id"]),
                    "target_ref": self._node_ref(row["target_node_id"]),
                    "relation_type": row["relation_type"],
                    "scope": row["scope_text"],
                    "rationale": row["rationale_text"],
                    "provenance_source_ids": provenance,
                }
            )
        return result

    def _node_ref(self, node_id: str) -> dict[str, str]:
        asset_key = self._connection.execute(
            select(kg_asset.c.stable_key).where(kg_asset.c.asset_id == node_id)
        ).scalar_one_or_none()
        if asset_key is not None:
            return {"asset_key": asset_key}
        row = self._connection.execute(
            select(
                kg_asset.c.stable_key,
                kg_component.c.component_key,
            )
            .join(
                kg_component,
                kg_component.c.parent_asset_id == kg_asset.c.asset_id,
            )
            .where(kg_component.c.component_id == node_id)
        ).mappings().one()
        return {
            "asset_key": row["stable_key"],
            "component_key": row["component_key"],
        }

    def _collections_for_nodes(self, included_nodes: set[str]) -> list[dict[str, Any]]:
        collections = self._connection.execute(
            select(kg_collection).order_by(kg_collection.c.collection_key)
        ).mappings().all()
        result: list[dict[str, Any]] = []
        for collection in collections:
            members = self._connection.execute(
                select(kg_collection_member.c.node_id)
                .where(
                    kg_collection_member.c.collection_key
                    == collection["collection_key"]
                )
                .order_by(kg_collection_member.c.node_id)
            ).scalars().all()
            refs = [
                {"ref": self._node_ref(node_id)}
                for node_id in members
                if node_id in included_nodes
            ]
            result.append(
                {
                    "collection_key": collection["collection_key"],
                    "title": collection["title"],
                    "members": refs,
                }
            )
        return result

    def _provenance_sources(self, source_ids: set[str]) -> list[dict[str, Any]]:
        if not source_ids:
            return []
        rows = self._connection.execute(
            select(kg_provenance_source)
            .where(kg_provenance_source.c.source_id.in_(sorted(source_ids)))
            .order_by(kg_provenance_source.c.source_id)
        ).mappings().all()
        if len(rows) != len(source_ids):
            present = {row["source_id"] for row in rows}
            missing = sorted(source_ids - present)
            raise KnowledgePersistenceConflict(
                f"Accepted knowledge references missing provenance sources: {missing}"
            )
        return [dict(row) for row in rows]
