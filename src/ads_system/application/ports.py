"""Application-facing persistence contracts for the first V1 vertical slices."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Protocol, Self

from ads_system.domain.models import (
    Finding,
    KnowledgeAssetRevision,
    KnowledgeRelationRevision,
    Project,
)


class KnowledgeRepository(Protocol):
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
    ) -> KnowledgeAssetRevision: ...

    def get_current_asset_revision(self, stable_key: str) -> KnowledgeAssetRevision | None: ...

    def get_asset_revision(self, revision_id: str) -> KnowledgeAssetRevision | None: ...

    def add_component_revision(
        self,
        *,
        parent_asset_revision_id: str,
        component_key: str,
        component_kind: str,
        body: str | None = None,
        payload: Mapping[str, object] | None = None,
    ) -> str: ...

    def create_relation(
        self,
        *,
        source_node_id: str,
        target_node_id: str,
        relation_type: str,
        rationale: str | None = None,
        scope: str | None = None,
    ) -> KnowledgeRelationRevision: ...

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
    ) -> str: ...


class KnowledgeInterchangeRepository(Protocol):
    """Persistence operations required by Specification 004 services."""

    def import_provenance_source(self, source: Mapping[str, Any]) -> None: ...

    def import_asset_revision(
        self, asset: Mapping[str, Any], *, actor: str
    ) -> None: ...

    def import_component_revision(
        self,
        *,
        parent_asset_revision_id: str,
        component: Mapping[str, Any],
        actor: str,
    ) -> None: ...

    def import_rule(
        self,
        *,
        owner_content_revision_id: str,
        rule: Mapping[str, Any],
    ) -> None: ...

    def import_relation_revision(
        self,
        relation: Mapping[str, Any],
        *,
        source_node_id: str,
        target_node_id: str,
        actor: str,
    ) -> None: ...

    def accept_content_revision(self, revision_id: str, *, actor: str) -> None: ...

    def accept_relation_revision(
        self, relation_revision_id: str, *, actor: str
    ) -> None: ...

    def sync_collection(
        self,
        *,
        collection_key: str,
        title: str,
        node_ids: Sequence[str],
    ) -> None: ...

    def export_current_accepted_snapshot(self) -> dict[str, Any]: ...


class ProjectRepository(Protocol):
    def create_project(self, *, title: str) -> Project: ...

    def add_finding(
        self,
        *,
        project_id: str,
        finding_type: str,
        statement: str,
    ) -> Finding: ...

    def link_finding_to_knowledge(
        self,
        *,
        finding_id: str,
        project_id: str,
        knowledge_revision_id: str,
        reference_type: str,
    ) -> str: ...

    def knowledge_references_for_finding(self, finding_id: str) -> tuple[str, ...]: ...


class UnitOfWork(Protocol):
    knowledge: KnowledgeRepository
    interchange: KnowledgeInterchangeRepository
    projects: ProjectRepository

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type, exc, tb) -> None: ...

    def commit(self) -> None: ...

    def rollback(self) -> None: ...
