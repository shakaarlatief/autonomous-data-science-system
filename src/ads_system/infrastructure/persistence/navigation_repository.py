"""Targeted SQLAlchemy reads for MethodologicalHorizon knowledge navigation.

The repository exposes only accepted-current reusable-knowledge projections.
It deliberately does not use interchange snapshot export as the operational
navigation API and does not expose SQLAlchemy or persistence-table details to the
application layer.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from sqlalchemy import Connection, select

from ads_system.application.horizon_models import (
    KnowledgeContextRequirement,
    NavigableKnowledgeAsset,
    RelatedKnowledgeAsset,
)
from ads_system.infrastructure.persistence.interchange_schema import (
    kg_content_revision_extension,
    kg_relation_revision_state,
)
from ads_system.infrastructure.persistence.schema import (
    kg_asset,
    kg_asset_revision,
    kg_relation,
    kg_relation_current,
    kg_relation_revision,
    kg_revision_governance,
)


class SqlAlchemyKnowledgeNavigationRepository:
    """Read accepted-current knowledge and one-hop governed relations."""

    def __init__(self, connection: Connection) -> None:
        self._connection = connection

    def get_current_asset(self, stable_key: str) -> NavigableKnowledgeAsset | None:
        row = self._connection.execute(
            select(
                kg_asset.c.stable_key,
                kg_asset.c.current_accepted_revision_id.label("revision_id"),
                kg_asset_revision.c.title,
                kg_content_revision_extension.c.structured_json,
            )
            .join(
                kg_asset_revision,
                kg_asset_revision.c.revision_id
                == kg_asset.c.current_accepted_revision_id,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_asset.c.current_accepted_revision_id,
            )
            .outerjoin(
                kg_content_revision_extension,
                kg_content_revision_extension.c.revision_id
                == kg_asset.c.current_accepted_revision_id,
            )
            .where(
                kg_asset.c.stable_key == stable_key,
                kg_asset.c.current_accepted_revision_id.is_not(None),
                kg_revision_governance.c.current_status == "ACCEPTED",
            )
        ).mappings().first()

        if row is None:
            return None

        extension = self._load_extension(row["structured_json"])
        applicability = extension.get("applicability")
        if applicability is not None and not isinstance(applicability, Mapping):
            raise ValueError(
                f"Applicability for {stable_key!r} must be a JSON object or null"
            )

        requirements = self._context_requirements(
            stable_key=stable_key,
            value=extension.get("context_requirements"),
        )
        return NavigableKnowledgeAsset(
            stable_key=str(row["stable_key"]),
            revision_id=str(row["revision_id"]),
            title=str(row["title"]),
            applicability=applicability,
            context_requirements=requirements,
        )

    def get_outbound_related_assets(
        self, stable_key: str
    ) -> tuple[RelatedKnowledgeAsset, ...]:
        """Return one-hop outbound accepted relations to accepted-current assets.

        Component targets and relation revisions without explicit accepted
        governance are excluded by construction. Directionality is preserved.
        """

        source_asset = kg_asset.alias("source_asset")
        source_governance = kg_revision_governance.alias("source_governance")
        target_asset = kg_asset.alias("target_asset")
        target_revision = kg_asset_revision.alias("target_asset_revision")
        target_governance = kg_revision_governance.alias("target_governance")

        rows = self._connection.execute(
            select(
                kg_relation_current.c.relation_revision_id,
                kg_relation.c.relation_type,
                target_asset.c.stable_key,
                target_asset.c.current_accepted_revision_id.label("target_revision_id"),
                target_revision.c.title,
            )
            .select_from(source_asset)
            .join(
                source_governance,
                source_governance.c.revision_id
                == source_asset.c.current_accepted_revision_id,
            )
            .join(
                kg_relation,
                kg_relation.c.source_node_id == source_asset.c.asset_id,
            )
            .join(
                kg_relation_current,
                kg_relation_current.c.relation_id == kg_relation.c.relation_id,
            )
            .join(
                kg_relation_revision,
                (
                    kg_relation_revision.c.relation_id
                    == kg_relation_current.c.relation_id
                )
                & (
                    kg_relation_revision.c.relation_revision_id
                    == kg_relation_current.c.relation_revision_id
                ),
            )
            .join(
                kg_relation_revision_state,
                kg_relation_revision_state.c.relation_revision_id
                == kg_relation_current.c.relation_revision_id,
            )
            .join(
                target_asset,
                target_asset.c.asset_id == kg_relation.c.target_node_id,
            )
            .join(
                target_revision,
                target_revision.c.revision_id
                == target_asset.c.current_accepted_revision_id,
            )
            .join(
                target_governance,
                target_governance.c.revision_id
                == target_asset.c.current_accepted_revision_id,
            )
            .where(
                source_asset.c.stable_key == stable_key,
                source_asset.c.current_accepted_revision_id.is_not(None),
                source_governance.c.current_status == "ACCEPTED",
                kg_relation_revision_state.c.governance_status == "ACCEPTED",
                target_asset.c.current_accepted_revision_id.is_not(None),
                target_governance.c.current_status == "ACCEPTED",
            )
            .order_by(
                kg_relation.c.relation_type,
                target_asset.c.stable_key,
                kg_relation_current.c.relation_revision_id,
            )
        ).mappings().all()

        return tuple(
            RelatedKnowledgeAsset(
                relation_revision_id=str(row["relation_revision_id"]),
                relation_type=str(row["relation_type"]),
                stable_key=str(row["stable_key"]),
                revision_id=str(row["target_revision_id"]),
                title=str(row["title"]),
            )
            for row in rows
        )

    @staticmethod
    def _load_extension(value: str | None) -> dict[str, Any]:
        if value is None:
            return {}
        loaded = json.loads(value)
        if not isinstance(loaded, dict):
            raise ValueError("Knowledge revision extension must decode to a JSON object")
        return loaded

    @staticmethod
    def _context_requirements(
        *,
        stable_key: str,
        value: Any,
    ) -> tuple[KnowledgeContextRequirement, ...]:
        if value is None:
            return ()
        if not isinstance(value, list):
            raise ValueError(
                f"Context requirements for {stable_key!r} must be a JSON array"
            )

        requirements: list[KnowledgeContextRequirement] = []
        for item in value:
            if not isinstance(item, Mapping):
                raise ValueError(
                    f"Context requirement for {stable_key!r} must be an object"
                )
            key = item.get("key")
            description = item.get("description")
            required_for = item.get("required_for")
            if not isinstance(key, str) or not isinstance(description, str):
                raise ValueError(
                    f"Context requirement for {stable_key!r} has invalid key/description"
                )
            if not isinstance(required_for, list) or not all(
                isinstance(entry, str) for entry in required_for
            ):
                raise ValueError(
                    f"Context requirement for {stable_key!r} has invalid required_for"
                )
            requirements.append(
                KnowledgeContextRequirement(
                    key=key,
                    description=description,
                    required_for=tuple(required_for),
                )
            )

        return tuple(sorted(requirements, key=lambda item: item.key))
