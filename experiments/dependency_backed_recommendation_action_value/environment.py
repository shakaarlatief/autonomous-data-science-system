"""Isolated accepted-current knowledge environment for Specification 021.

Specification 021 deliberately reuses the governed ten-asset knowledge state and
the deliberately wide MethodologicalHorizon already accepted by the selective-
context experiments. The experiment changes only the downstream project-relation
and recommendation/action contract.
"""

from __future__ import annotations

from pathlib import Path

from experiments.reasoning_context_value.environment import (
    PreparedReasoningEnvironment,
    prepare_reasoning_environment,
)


PreparedDependencyBackedRecommendationEnvironment = PreparedReasoningEnvironment


def prepare_dependency_backed_recommendation_environment(
    database_path: Path,
) -> PreparedDependencyBackedRecommendationEnvironment:
    """Prepare the unchanged accepted-current ten-asset benchmark environment."""

    return prepare_reasoning_environment(database_path)
