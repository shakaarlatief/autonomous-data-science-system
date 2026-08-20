"""SQLAlchemy Core repository adapters for the first V1 persistence slice."""

from __future__ import annotations

from collections.abc import Mapping

from sqlalchemy import Connection, func, insert, select, update

from ads_system.domain.models import (
    Finding,
    KnowledgeAssetRevision,
    KnowledgeRelationRevision,
    Project,
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
    prj_entity,
    prj_finding,
    prj_knowledge_ref,
    prj_project,
)
from ads_system.infrastructure.persistence.types import (
    canonical_json,
    new_id,
    semantic_hash,
    utc_now_text,
)


class SqlAlchemyKnowledgeRepository:
    """Persist reusable methodological knowledge without leaking SQL upstream."""

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def publish_asset_revision(
        self,
        *,
        stable_key: str,
        intrinsic_kind: str,
        title: str,
        purpose: str,
        scope: str | None = None,
        limitations: str | None = None,
        actor: str = "system",
    ) -> KnowledgeAssetRevision:
        now = utc_now_text()
        existing = self._connection.execute(
            select(
                kg_asset.c.asset_id,
                kg_asset.c.current_accepted_revision_id,
            ).where(kg_asset.c.stable_key == stable_key)
        ).mappings().first()

        if existing is None:
            asset_id = new_id()
            previous_revision_id = None
            revision_no = 1
            self._connection.execute(
                insert(kg_node).values(
                    node_id=asset_id,
                    node_type="ASSET",
                    created_at=now,
                )
            )
            self._connection.execute(
                insert(kg_asset).values(
                    asset_id=asset_id,
                    stable_key=stable_key,
                    current_accepted_revision_id=None,
                    created_at=now,
                )
            )
        else:
            asset_id = existing["asset_id"]
            previous_revision_id = existing["current_accepted_revision_id"]
            max_revision = self._connection.execute(
                select(func.max(kg_content_revision.c.revision_no)).where(
                    kg_content_revision.c.node_id == asset_id
                )
            ).scalar_one()
            revision_no = int(max_revision or 0) + 1

        revision_id = new_id()
        semantic_content = {
            "intrinsic_kind": intrinsic_kind,
            "title": title,
            "purpose": purpose,
            "scope": scope,
            "limitations": limitations,
        }

        self._connection.execute(
            insert(kg_content_revision).values(
                revision_id=revision_id,
                node_id=asset_id,
                revision_no=revision_no,
                created_at=now,
                semantic_content_hash=semantic_hash(semantic_content),
            )
        )
        self._connection.execute(
            insert(kg_asset_revision).values(
                revision_id=revision_id,
                asset_id=asset_id,
                intrinsic_kind=intrinsic_kind,
                title=title,
                purpose=purpose,
                scope_text=scope,
                limitations_text=limitations,
            )
        )
        self._connection.execute(
            insert(kg_revision_governance).values(
                revision_id=revision_id,
                current_status="ACCEPTED",
                updated_at=now,
            )
        )
        self._connection.execute(
            insert(kg_governance_event).values(
                event_id=new_id(),
                revision_id=revision_id,
                from_status=None,
                to_status="ACCEPTED",
                actor=actor,
                occurred_at=now,
                note_text="Published through V1 knowledge repository",
            )
        )

        if previous_revision_id is not None:
            self._connection.execute(
                update(kg_revision_governance)
                .where(kg_revision_governance.c.revision_id == previous_revision_id)
                .values(current_status="SUPERSEDED", updated_at=now)
            )
            self._connection.execute(
                insert(kg_governance_event).values(
                    event_id=new_id(),
                    revision_id=previous_revision_id,
                    from_status="ACCEPTED",
                    to_status="SUPERSEDED",
                    actor=actor,
                    occurred_at=now,
                    note_text=f"Superseded by revision {revision_id}",
                )
            )

        self._connection.execute(
            update(kg_asset)
            .where(kg_asset.c.asset_id == asset_id)
            .values(current_accepted_revision_id=revision_id)
        )

        return KnowledgeAssetRevision(
            asset_id=asset_id,
            revision_id=revision_id,
            stable_key=stable_key,
            revision_no=revision_no,
            intrinsic_kind=intrinsic_kind,
            title=title,
            purpose=purpose,
        )

    def get_current_asset_revision(self, stable_key: str) -> KnowledgeAssetRevision | None:
        row = self._connection.execute(
            select(
                kg_asset.c.asset_id,
                kg_asset.c.stable_key,
                kg_content_revision.c.revision_id,
                kg_content_revision.c.revision_no,
                kg_asset_revision.c.intrinsic_kind,
                kg_asset_revision.c.title,
                kg_asset_revision.c.purpose,
            )
            .join(
                kg_content_revision,
                kg_content_revision.c.revision_id
                == kg_asset.c.current_accepted_revision_id,
            )
            .join(
                kg_asset_revision,
                kg_asset_revision.c.revision_id == kg_content_revision.c.revision_id,
            )
            .where(kg_asset.c.stable_key == stable_key)
        ).mappings().first()
        return self._asset_revision_from_row(row)

    def get_asset_revision(self, revision_id: str) -> KnowledgeAssetRevision | None:
        row = self._connection.execute(
            select(
                kg_asset.c.asset_id,
                kg_asset.c.stable_key,
                kg_content_revision.c.revision_id,
                kg_content_revision.c.revision_no,
                kg_asset_revision.c.intrinsic_kind,
                kg_asset_revision.c.title,
                kg_asset_revision.c.purpose,
            )
            .join(kg_asset, kg_asset.c.asset_id == kg_asset_revision.c.asset_id)
            .join(
                kg_content_revision,
                kg_content_revision.c.revision_id == kg_asset_revision.c.revision_id,
            )
            .where(kg_content_revision.c.revision_id == revision_id)
        ).mappings().first()
        return self._asset_revision_from_row(row)

    def add_component_revision(
        self,
        *,
        parent_asset_revision_id: str,
        component_key: str,
        component_kind: str,
        body: str | None = None,
        payload: Mapping[str, object] | None = None,
    ) -> str:
        parent = self._connection.execute(
            select(kg_asset_revision.c.asset_id).where(
                kg_asset_revision.c.revision_id == parent_asset_revision_id
            )
        ).scalar_one()

        existing = self._connection.execute(
            select(kg_component.c.component_id).where(
                kg_component.c.parent_asset_id == parent,
                kg_component.c.component_key == component_key,
            )
        ).scalar_one_or_none()

        now = utc_now_text()
        if existing is None:
            component_id = new_id()
            self._connection.execute(
                insert(kg_node).values(
                    node_id=component_id,
                    node_type="COMPONENT",
                    created_at=now,
                )
            )
            self._connection.execute(
                insert(kg_component).values(
                    component_id=component_id,
                    parent_asset_id=parent,
                    component_key=component_key,
                    component_kind=component_kind,
                    created_at=now,
                )
            )
            revision_no = 1
        else:
            component_id = existing
            max_revision = self._connection.execute(
                select(func.max(kg_content_revision.c.revision_no)).where(
                    kg_content_revision.c.node_id == component_id
                )
            ).scalar_one()
            revision_no = int(max_revision or 0) + 1

        revision_id = new_id()
        payload_json = canonical_json(payload) if payload is not None else None
        self._connection.execute(
            insert(kg_content_revision).values(
                revision_id=revision_id,
                node_id=component_id,
                revision_no=revision_no,
                created_at=now,
                semantic_content_hash=semantic_hash(
                    {
                        "component_kind": component_kind,
                        "body": body,
                        "payload": payload,
                        "parent_asset_revision_id": parent_asset_revision_id,
                    }
                ),
            )
        )
        self._connection.execute(
            insert(kg_component_revision).values(
                revision_id=revision_id,
                component_id=component_id,
                parent_asset_id=parent,
                parent_asset_revision_id=parent_asset_revision_id,
                body_text=body,
                payload_json=payload_json,
                position=0,
            )
        )
        self._connection.execute(
            insert(kg_revision_governance).values(
                revision_id=revision_id,
                current_status="ACCEPTED",
                updated_at=now,
            )
        )
        return revision_id

    def create_relation(
        self,
        *,
        source_node_id: str,
        target_node_id: str,
        relation_type: str,
        rationale: str | None = None,
        scope: str | None = None,
    ) -> KnowledgeRelationRevision:
        now = utc_now_text()
        relation_id = new_id()
        relation_revision_id = new_id()
        self._connection.execute(
            insert(kg_relation).values(
                relation_id=relation_id,
                source_node_id=source_node_id,
                target_node_id=target_node_id,
                relation_type=relation_type,
                created_at=now,
            )
        )
        self._connection.execute(
            insert(kg_relation_revision).values(
                relation_revision_id=relation_revision_id,
                relation_id=relation_id,
                revision_no=1,
                scope_text=scope,
                rationale_text=rationale,
                created_at=now,
            )
        )
        self._connection.execute(
            insert(kg_relation_current).values(
                relation_id=relation_id,
                relation_revision_id=relation_revision_id,
            )
        )
        return KnowledgeRelationRevision(
            relation_id=relation_id,
            relation_revision_id=relation_revision_id,
            source_node_id=source_node_id,
            target_node_id=target_node_id,
            relation_type=relation_type,
        )

    def add_rule(
        self,
        *,
        owner_content_revision_id: str,
        rule_key: str,
        condition: Mapping[str, object],
        consequence_type: str,
        consequence_payload: Mapping[str, object] | None,
        force: str,
        unknown_behavior: str,
        rationale: str | None = None,
    ) -> str:
        rule_spec_id = new_id()
        self._connection.execute(
            insert(kg_rule_spec).values(
                rule_spec_id=rule_spec_id,
                owner_content_revision_id=owner_content_revision_id,
                rule_key=rule_key,
                condition_json=canonical_json(condition),
                consequence_type=consequence_type,
                consequence_payload_json=(
                    canonical_json(consequence_payload)
                    if consequence_payload is not None
                    else None
                ),
                force=force,
                unknown_behavior=unknown_behavior,
                rationale_text=rationale,
            )
        )
        return rule_spec_id

    @staticmethod
    def _asset_revision_from_row(row) -> KnowledgeAssetRevision | None:
        if row is None:
            return None
        return KnowledgeAssetRevision(
            asset_id=row["asset_id"],
            revision_id=row["revision_id"],
            stable_key=row["stable_key"],
            revision_no=row["revision_no"],
            intrinsic_kind=row["intrinsic_kind"],
            title=row["title"],
            purpose=row["purpose"],
        )


class SqlAlchemyProjectRepository:
    """Persist the minimum project epistemic state needed by this slice."""

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def create_project(self, *, title: str) -> Project:
        project_id = new_id()
        self._connection.execute(
            insert(prj_project).values(
                project_id=project_id,
                title=title,
                created_at=utc_now_text(),
            )
        )
        return Project(project_id=project_id, title=title)

    def add_finding(
        self,
        *,
        project_id: str,
        finding_type: str,
        statement: str,
    ) -> Finding:
        finding_id = new_id()
        now = utc_now_text()
        self._connection.execute(
            insert(prj_entity).values(
                entity_id=finding_id,
                project_id=project_id,
                entity_type="FINDING",
                created_at=now,
            )
        )
        self._connection.execute(
            insert(prj_finding).values(
                finding_id=finding_id,
                project_id=project_id,
                finding_type=finding_type,
                statement_text=statement,
                created_at=now,
            )
        )
        return Finding(
            finding_id=finding_id,
            project_id=project_id,
            finding_type=finding_type,
            statement=statement,
        )

    def link_finding_to_knowledge(
        self,
        *,
        finding_id: str,
        project_id: str,
        knowledge_revision_id: str,
        reference_type: str,
    ) -> str:
        ref_id = new_id()
        self._connection.execute(
            insert(prj_knowledge_ref).values(
                ref_id=ref_id,
                project_entity_id=finding_id,
                project_id=project_id,
                knowledge_revision_id=knowledge_revision_id,
                reference_type=reference_type,
                created_at=utc_now_text(),
            )
        )
        return ref_id

    def knowledge_references_for_finding(self, finding_id: str) -> tuple[str, ...]:
        rows = self._connection.execute(
            select(prj_knowledge_ref.c.knowledge_revision_id)
            .where(prj_knowledge_ref.c.project_entity_id == finding_id)
            .order_by(prj_knowledge_ref.c.created_at)
        ).scalars()
        return tuple(rows)
