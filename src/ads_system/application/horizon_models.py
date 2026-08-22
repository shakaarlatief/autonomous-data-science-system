"""Storage-neutral read models for MethodologicalHorizon construction.

These models deliberately represent methodological navigation semantics rather
than retrieval-engine or persistence details. Later context-selection layers may
consume the exact stable/revision identities preserved here without depending on
how a candidate originally entered the Horizon.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class KnowledgeContextRequirement:
    """Context explicitly required by a reusable knowledge revision."""

    key: str
    description: str
    required_for: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class NavigableKnowledgeAsset:
    """Accepted-current knowledge projection used for methodological navigation."""

    stable_key: str
    revision_id: str
    title: str
    applicability: Mapping[str, Any] | None
    context_requirements: tuple[KnowledgeContextRequirement, ...]
    reasoning_functions: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class RelatedKnowledgeAsset:
    """One accepted-current relation edge and its accepted-current target asset."""

    relation_revision_id: str
    relation_type: str
    stable_key: str
    revision_id: str
    title: str


@dataclass(frozen=True, slots=True)
class ApplicabilityAssessment:
    """Deterministic applicability/context assessment for one knowledge revision."""

    state: str
    missing_context_keys: tuple[str, ...]
    unknown_predicate_keys: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class HorizonSeed:
    """Revision-transparent direct candidate supplied to the Horizon builder."""

    stable_key: str
    revision_id: str
    title: str


@dataclass(frozen=True, slots=True)
class HorizonCandidate:
    """Explained candidate retained or excluded by the bounded Horizon builder.

    ``reasoning_functions`` is accepted-current methodological metadata used by
    the next task-specific context-selection slice. ``relation_source_key``
    preserves which direct seed introduced a relation candidate. Both fields are
    storage-neutral extensions and do not change the one-hop traversal semantics
    validated by Specification 012.
    """

    stable_key: str
    revision_id: str
    title: str
    origin: str
    relation_type: str | None
    relation_revision_id: str | None
    applicability_state: str
    missing_context_keys: tuple[str, ...]
    relation_source_key: str | None = None
    reasoning_functions: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class MethodologicalHorizon:
    """Bounded applicability-aware methodological horizon."""

    included: tuple[HorizonCandidate, ...]
    excluded: tuple[HorizonCandidate, ...]
