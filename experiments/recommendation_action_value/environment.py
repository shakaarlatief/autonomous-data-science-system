"""Isolated accepted-current environment for Specification 015.

Specification 015 intentionally reuses the exact ten-asset governed knowledge
state and explained MethodologicalHorizon validated by the preceding reasoning
slice. The recommendation experiment changes the downstream task, not the
methodological catalog or Horizon construction.
"""

from __future__ import annotations

from pathlib import Path

from experiments.reasoning_context_value.environment import (
    PreparedReasoningEnvironment,
    prepare_reasoning_environment,
)


PreparedRecommendationEnvironment = PreparedReasoningEnvironment


def prepare_recommendation_environment(
    database_path: Path,
) -> PreparedRecommendationEnvironment:
    """Prepare the unchanged accepted-current ten-asset benchmark environment."""

    return prepare_reasoning_environment(database_path)
