"""Application-facing persistence contracts for the first V1 vertical slice."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol, Self

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
    projects: ProjectRepository

    def __enter__(self) -> Self: ...

    def __exit__(self, exc_type, exc, tb) -> None: ...

    def commit(self) -> None: ...

    def rollback(self) -> None: ...
