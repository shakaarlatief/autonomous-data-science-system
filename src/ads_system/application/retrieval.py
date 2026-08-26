"""Application-level values for reusable-knowledge retrieval.

Retrieval results are derived application projections over governed reusable
knowledge. They are intentionally not persisted domain objects: the
methodological source of truth remains the revisioned knowledge store, while a
retrieval adapter may be rebuilt or replaced without changing knowledge
identity, governance, or project history.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KnowledgeRetrievalHit:
    """One bounded retrieval candidate with exact knowledge-revision identity.

    ``score`` is channel-local and is only meaningful for ordering results from
    the same retrieval implementation/query. Application code must not treat it
    as a calibrated probability or cross-channel relevance measure.
    """

    stable_key: str
    revision_id: str
    title: str
    score: float
    channel: str
