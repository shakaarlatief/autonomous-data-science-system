"""Storage-neutral models for task-specific methodological context selection.

The types in this module separate two different products of context selection:

* ``ContextSelectionResult`` is system-facing and keeps explicit inclusion and
  omission decisions for observability, debugging, and UI explanation.
* ``MethodologicalContextPack`` is model-facing and contains only the selected
  exact knowledge revisions needed for the current reasoning task.

Keeping those representations separate prevents omission/audit metadata from
being reintroduced into every LLM call merely because the wider system retains
it.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any

from ads_system.application.horizon_models import KnowledgeContextRequirement


@dataclass(frozen=True, slots=True)
class ContextNarrativeFacet:
    """Reasoning-relevant narrative facet from one accepted asset revision."""

    facet_kind: str
    body: str
    position: int


@dataclass(frozen=True, slots=True)
class ContextKnowledgeComponent:
    """Accepted component belonging to the exact selected asset revision."""

    component_key: str
    revision_id: str
    component_kind: str
    body: str | None
    reasoning_functions: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ContextKnowledgeRule:
    """Conditional methodological rule owned by the exact selected revision."""

    rule_spec_id: str
    rule_key: str
    condition: Mapping[str, Any]
    consequence_type: str
    consequence_payload: Mapping[str, Any] | None
    force: str
    unknown_behavior: str
    rationale: str | None


@dataclass(frozen=True, slots=True)
class ContextKnowledgeAsset:
    """Compact reasoning projection for one exact accepted knowledge revision."""

    stable_key: str
    revision_id: str
    title: str
    intrinsic_kind: str
    purpose: str
    scope: str | None
    reasoning_functions: tuple[str, ...]
    context_requirements: tuple[KnowledgeContextRequirement, ...]
    semantic_checks: tuple[str, ...]
    limitations: tuple[str, ...]
    narrative_facets: tuple[ContextNarrativeFacet, ...]
    components: tuple[ContextKnowledgeComponent, ...]
    rules: tuple[ContextKnowledgeRule, ...]


@dataclass(frozen=True, slots=True)
class MethodologicalContextRequest:
    """Explicit task profile consumed by the first deterministic selector."""

    task_id: str
    requested_reasoning_functions: tuple[str, ...]
    max_assets: int


@dataclass(frozen=True, slots=True)
class ContextSelectionDecision:
    """System-facing selection/omission decision for one Horizon candidate."""

    stable_key: str
    revision_id: str
    selected: bool
    reason: str
    origin: str
    applicability_state: str
    missing_context_keys: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class SelectedContextKnowledge:
    """One selected knowledge revision plus Horizon/relevance provenance."""

    asset: ContextKnowledgeAsset
    selection_reason: str
    origin: str
    applicability_state: str
    missing_context_keys: tuple[str, ...]
    relation_source_key: str | None
    relation_type: str | None
    relation_revision_id: str | None


@dataclass(frozen=True, slots=True)
class MethodologicalContextPack:
    """Model-facing methodological knowledge for one bounded reasoning task."""

    schema_version: int
    task_id: str
    requested_reasoning_functions: tuple[str, ...]
    knowledge: tuple[SelectedContextKnowledge, ...]
    missing_context_keys: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class ContextSelectionResult:
    """System-facing result retaining both pack and explicit candidate decisions."""

    request: MethodologicalContextRequest
    pack: MethodologicalContextPack
    decisions: tuple[ContextSelectionDecision, ...]


@dataclass(frozen=True, slots=True)
class SerializedMethodologicalContextPack:
    """Canonical model-facing serialization and deterministic size identity."""

    text: str
    utf8_bytes: int
    character_count: int
    sha256: str
