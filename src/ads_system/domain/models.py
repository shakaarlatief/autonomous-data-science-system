"""Storage-neutral domain values used by the first V1 persistence slice."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KnowledgeAssetRevision:
    asset_id: str
    revision_id: str
    stable_key: str
    revision_no: int
    intrinsic_kind: str
    title: str
    purpose: str


@dataclass(frozen=True, slots=True)
class KnowledgeRelationRevision:
    relation_id: str
    relation_revision_id: str
    source_node_id: str
    target_node_id: str
    relation_type: str


@dataclass(frozen=True, slots=True)
class Project:
    project_id: str
    title: str


@dataclass(frozen=True, slots=True)
class Finding:
    finding_id: str
    project_id: str
    finding_type: str
    statement: str
