"""Targeted SQLAlchemy reads for methodological navigation and context assembly.

The repository exposes only accepted-current reusable-knowledge projections. It
deliberately does not use interchange snapshot export as the operational
navigation/context API and does not expose SQLAlchemy or persistence-table
details to the application layer.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any

from sqlalchemy import Connection, select

from ads_system.application.context_models import (
    ContextKnowledgeAsset,
    ContextKnowledgeComponent,
    ContextKnowledgeRule,
    ContextNarrativeFacet,
)
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
    kg_component,
    kg_component_revision,
    kg_relation,
    kg_relation_current,
    kg_relation_revision,
    kg_revision_governance,
    kg_rule_spec,
)


class SqlAlchemyKnowledgeNavigationRepository:
    """Read accepted-current knowledge, governed relations, and compact context."""

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
            reasoning_functions=self._string_tuple(
                stable_key=stable_key,
                field="reasoning_functions",
                value=extension.get("reasoning_functions"),
            ),
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

    def get_context_asset(
        self, stable_key: str, revision_id: str
    ) -> ContextKnowledgeAsset | None:
        """Return compact reasoning content for one exact current accepted revision.

        The method intentionally fails closed by returning ``None`` when the
        requested revision is historical/stale even if the stable asset has a
        newer accepted revision. Callers can then surface an explicit stale
        context error instead of silently changing the methodological basis of a
        reasoning call.
        """

        row = self._connection.execute(
            select(
                kg_asset.c.stable_key,
                kg_asset.c.current_accepted_revision_id.label("revision_id"),
                kg_asset_revision.c.title,
                kg_asset_revision.c.intrinsic_kind,
                kg_asset_revision.c.purpose,
                kg_asset_revision.c.scope_text,
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
                kg_asset.c.current_accepted_revision_id == revision_id,
                kg_revision_governance.c.current_status == "ACCEPTED",
            )
        ).mappings().first()

        if row is None:
            return None

        extension = self._load_extension(row["structured_json"])
        return ContextKnowledgeAsset(
            stable_key=str(row["stable_key"]),
            revision_id=str(row["revision_id"]),
            title=str(row["title"]),
            intrinsic_kind=str(row["intrinsic_kind"]),
            purpose=str(row["purpose"]),
            scope=(str(row["scope_text"]) if row["scope_text"] is not None else None),
            reasoning_functions=self._string_tuple(
                stable_key=stable_key,
                field="reasoning_functions",
                value=extension.get("reasoning_functions"),
            ),
            context_requirements=self._context_requirements(
                stable_key=stable_key,
                value=extension.get("context_requirements"),
            ),
            semantic_checks=self._string_tuple(
                stable_key=stable_key,
                field="semantic_checks",
                value=extension.get("semantic_checks"),
            ),
            limitations=self._string_tuple(
                stable_key=stable_key,
                field="limitations",
                value=extension.get("limitations"),
            ),
            narrative_facets=self._narrative_facets(
                stable_key=stable_key,
                value=extension.get("narrative_facets"),
            ),
            components=self._accepted_context_components(revision_id),
            rules=self._context_rules(revision_id),
        )

    def _accepted_context_components(
        self, parent_revision_id: str
    ) -> tuple[ContextKnowledgeComponent, ...]:
        extension = kg_content_revision_extension.alias("context_component_extension")
        rows = self._connection.execute(
            select(
                kg_component.c.component_key,
                kg_component_revision.c.revision_id,
                kg_component.c.component_kind,
                kg_component_revision.c.body_text,
                extension.c.structured_json,
            )
            .join(
                kg_component_revision,
                kg_component_revision.c.component_id == kg_component.c.component_id,
            )
            .join(
                kg_revision_governance,
                kg_revision_governance.c.revision_id
                == kg_component_revision.c.revision_id,
            )
            .outerjoin(
                extension,
                extension.c.revision_id == kg_component_revision.c.revision_id,
            )
            .where(
                kg_component_revision.c.parent_asset_revision_id == parent_revision_id,
                kg_revision_governance.c.current_status == "ACCEPTED",
            )
            .order_by(
                kg_component_revision.c.position,
                kg_component.c.component_key,
                kg_component_revision.c.revision_id,
            )
        ).mappings().all()

        result: list[ContextKnowledgeComponent] = []
        for row in rows:
            component_extension = self._load_extension(row["structured_json"])
            result.append(
                ContextKnowledgeComponent(
                    component_key=str(row["component_key"]),
                    revision_id=str(row["revision_id"]),
                    component_kind=str(row["component_kind"]),
                    body=(
                        str(row["body_text"])
                        if row["body_text"] is not None
                        else None
                    ),
                    reasoning_functions=self._string_tuple(
                        stable_key=str(row["component_key"]),
                        field="component.reasoning_functions",
                        value=component_extension.get("reasoning_functions"),
                    ),
                )
            )
        return tuple(result)

    def _context_rules(self, revision_id: str) -> tuple[ContextKnowledgeRule, ...]:
        rows = self._connection.execute(
            select(
                kg_rule_spec.c.rule_spec_id,
                kg_rule_spec.c.rule_key,
                kg_rule_spec.c.condition_json,
                kg_rule_spec.c.consequence_type,
                kg_rule_spec.c.consequence_payload_json,
                kg_rule_spec.c.force,
                kg_rule_spec.c.unknown_behavior,
                kg_rule_spec.c.rationale_text,
            )
            .where(kg_rule_spec.c.owner_content_revision_id == revision_id)
            .order_by(kg_rule_spec.c.rule_key, kg_rule_spec.c.rule_spec_id)
        ).mappings().all()

        result: list[ContextKnowledgeRule] = []
        for row in rows:
            condition = json.loads(row["condition_json"])
            if not isinstance(condition, Mapping):
                raise ValueError(
                    f"Rule {row['rule_key']!r} condition must decode to an object"
                )
            consequence_payload = (
                json.loads(row["consequence_payload_json"])
                if row["consequence_payload_json"] is not None
                else None
            )
            if consequence_payload is not None and not isinstance(
                consequence_payload, Mapping
            ):
                raise ValueError(
                    f"Rule {row['rule_key']!r} consequence payload must decode to an object or null"
                )
            result.append(
                ContextKnowledgeRule(
                    rule_spec_id=str(row["rule_spec_id"]),
                    rule_key=str(row["rule_key"]),
                    condition=condition,
                    consequence_type=str(row["consequence_type"]),
                    consequence_payload=consequence_payload,
                    force=str(row["force"]),
                    unknown_behavior=str(row["unknown_behavior"]),
                    rationale=(
                        str(row["rationale_text"])
                        if row["rationale_text"] is not None
                        else None
                    ),
                )
            )
        return tuple(result)

    @staticmethod
    def _load_extension(value: str | None) -> dict[str, Any]:
        if value is None:
            return {}
        loaded = json.loads(value)
        if not isinstance(loaded, dict):
            raise ValueError("Knowledge revision extension must decode to a JSON object")
        return loaded

    @staticmethod
    def _string_tuple(
        *,
        stable_key: str,
        field: str,
        value: Any,
    ) -> tuple[str, ...]:
        if value is None:
            return ()
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise ValueError(f"{field} for {stable_key!r} must be a JSON string array")
        return tuple(value)

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

    @staticmethod
    def _narrative_facets(
        *,
        stable_key: str,
        value: Any,
    ) -> tuple[ContextNarrativeFacet, ...]:
        if value is None:
            return ()
        if not isinstance(value, list):
            raise ValueError(f"Narrative facets for {stable_key!r} must be a JSON array")

        facets: list[ContextNarrativeFacet] = []
        for item in value:
            if not isinstance(item, Mapping):
                raise ValueError(f"Narrative facet for {stable_key!r} must be an object")
            facet_kind = item.get("facet_kind")
            body = item.get("body")
            position = item.get("position")
            if not isinstance(facet_kind, str) or not isinstance(body, str):
                raise ValueError(
                    f"Narrative facet for {stable_key!r} has invalid kind/body"
                )
            if not isinstance(position, int) or isinstance(position, bool):
                raise ValueError(
                    f"Narrative facet for {stable_key!r} has invalid position"
                )
            facets.append(
                ContextNarrativeFacet(
                    facet_kind=facet_kind,
                    body=body,
                    position=position,
                )
            )
        return tuple(sorted(facets, key=lambda item: (item.position, item.facet_kind)))
