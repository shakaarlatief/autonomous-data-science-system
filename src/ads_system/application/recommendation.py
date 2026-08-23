"""ADS-owned recommendation and bounded action-classification models.

The first recommendation/action vertical slice deliberately separates the
reasoner's structured recommendation result from authoritative project-state
mutation. These types describe what the reasoning layer concluded about a
frozen candidate action menu. They do not create Proposal, Question,
Investigation, Decision, or execution objects by themselves.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class RecommendationDisposition(str, Enum):
    """Bounded recommendation disposition used by Specification 015.

    The enum is intentionally experimental rather than a final production
    project-state taxonomy. In particular, ``BLOCKING_REQUIRED`` represents a
    validity/dependency relationship to a named downstream scope; it is not
    modeled as merely a stronger ordinal recommendation than ``RECOMMENDED``.
    """

    BLOCKING_REQUIRED = "BLOCKING_REQUIRED"
    RECOMMENDED = "RECOMMENDED"
    DEFER = "DEFER"
    NOT_NOW = "NOT_NOW"


@dataclass(frozen=True, slots=True)
class RecommendationActionDecision:
    """One reasoned disposition for one supplied candidate action."""

    action_id: str
    disposition: RecommendationDisposition
    rationale: str

    def __post_init__(self) -> None:
        if not self.action_id.strip():
            raise ValueError("action_id must be non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")
        if not isinstance(self.disposition, RecommendationDisposition):
            try:
                normalized = RecommendationDisposition(self.disposition)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"unsupported recommendation disposition: {self.disposition!r}"
                ) from exc
            object.__setattr__(self, "disposition", normalized)

    def to_payload(self) -> dict[str, str]:
        return {
            "action_id": self.action_id,
            "disposition": self.disposition.value,
            "rationale": self.rationale,
        }


@dataclass(frozen=True, slots=True)
class RecommendationActionResult:
    """Structured result for the bounded recommendation/action experiment."""

    summary: str
    action_decisions: tuple[RecommendationActionDecision, ...]
    blocked_scopes: tuple[str, ...]
    required_clarification_ids: tuple[str, ...]
    warnings: tuple[str, ...]
    methodological_basis: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("summary must be non-empty")

        action_ids = [decision.action_id for decision in self.action_decisions]
        if len(action_ids) != len(set(action_ids)):
            raise ValueError("action_decisions must contain unique action IDs")

        for field_name in (
            "blocked_scopes",
            "required_clarification_ids",
            "warnings",
            "methodological_basis",
        ):
            values = getattr(self, field_name)
            if any(not value.strip() for value in values):
                raise ValueError(f"{field_name} cannot contain empty strings")
            if len(values) != len(set(values)):
                raise ValueError(f"{field_name} must not contain duplicates")

    def to_payload(self) -> dict[str, object]:
        return {
            "summary": self.summary,
            "action_decisions": [
                decision.to_payload() for decision in self.action_decisions
            ],
            "blocked_scopes": list(self.blocked_scopes),
            "required_clarification_ids": list(self.required_clarification_ids),
            "warnings": list(self.warnings),
            "methodological_basis": list(self.methodological_basis),
        }


def validate_recommendation_action_result(
    result: RecommendationActionResult,
    *,
    candidate_action_ids: tuple[str, ...],
    allowed_blocked_scopes: tuple[str, ...],
    allowed_clarification_ids: tuple[str, ...],
) -> None:
    """Validate exact bounded-menu coverage for one recommendation result.

    This validation is deterministic application logic. It does not judge
    whether a disposition or rationale is methodologically correct; the frozen
    evaluator and semantic rubric handle those separate questions.
    """

    if len(candidate_action_ids) != len(set(candidate_action_ids)):
        raise ValueError("candidate_action_ids must be unique")
    if len(allowed_blocked_scopes) != len(set(allowed_blocked_scopes)):
        raise ValueError("allowed_blocked_scopes must be unique")
    if len(allowed_clarification_ids) != len(set(allowed_clarification_ids)):
        raise ValueError("allowed_clarification_ids must be unique")

    expected_actions = set(candidate_action_ids)
    observed_actions = {decision.action_id for decision in result.action_decisions}
    missing = sorted(expected_actions - observed_actions)
    unknown = sorted(observed_actions - expected_actions)
    if missing or unknown:
        raise ValueError(
            "recommendation action coverage must exactly match the supplied menu; "
            f"missing={missing}, unknown={unknown}"
        )

    unknown_scopes = sorted(set(result.blocked_scopes) - set(allowed_blocked_scopes))
    if unknown_scopes:
        raise ValueError(
            "recommendation result contains blocked scopes outside the supplied menu: "
            f"{unknown_scopes}"
        )

    unknown_clarifications = sorted(
        set(result.required_clarification_ids) - set(allowed_clarification_ids)
    )
    if unknown_clarifications:
        raise ValueError(
            "recommendation result contains clarification IDs outside the supplied menu: "
            f"{unknown_clarifications}"
        )
