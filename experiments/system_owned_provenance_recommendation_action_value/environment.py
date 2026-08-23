"""Isolated accepted-current knowledge environment for Specification 019.

Specification 019 deliberately reuses the same governed ten-asset knowledge
state and explained MethodologicalHorizon already exercised by Specifications
014 and 015. The experiment changes only the downstream recommendation/action
contract and the prospective relation-backed benchmark states.
"""

from __future__ import annotations

from pathlib import Path

from experiments.reasoning_context_value.environment import (
    PreparedReasoningEnvironment,
    prepare_reasoning_environment,
)


PreparedSystemOwnedProvenanceRecommendationEnvironment = PreparedReasoningEnvironment


def prepare_system_owned_provenance_recommendation_environment(
    database_path: Path,
) -> PreparedSystemOwnedProvenanceRecommendationEnvironment:
    """Prepare the unchanged accepted-current ten-asset benchmark environment."""

    return prepare_reasoning_environment(database_path)
