from __future__ import annotations

import json

import pytest

from ads_system.application.recommendation import (
    RecommendationActionDecision,
    RecommendationActionResult,
    RecommendationDisposition,
    validate_recommendation_action_result,
)
from ads_system.application.reasoning import (
    ReasoningModelConfiguration,
    ReasoningOutputKind,
    ReasoningRequest,
    validate_methodological_basis,
)


def _result() -> RecommendationActionResult:
    return RecommendationActionResult(
        summary="Resolve the validity gates before model comparison.",
        action_decisions=(
            RecommendationActionDecision(
                action_id="establish-prediction-moment",
                disposition=RecommendationDisposition.BLOCKING_REQUIRED,
                rationale="Prediction timing defines the information boundary.",
            ),
            RecommendationActionDecision(
                action_id="compare-random-forest-now",
                disposition=RecommendationDisposition.DEFER,
                rationale="Model comparison should wait for the validity gates.",
            ),
        ),
        blocked_scopes=("model-comparison-claims",),
        required_clarification_ids=("prediction-moment",),
        warnings=(),
        methodological_basis=(),
    )


def test_recommendation_result_validates_exact_candidate_menu() -> None:
    result = _result()
    validate_recommendation_action_result(
        result,
        candidate_action_ids=(
            "establish-prediction-moment",
            "compare-random-forest-now",
        ),
        allowed_blocked_scopes=("model-comparison-claims",),
        allowed_clarification_ids=("prediction-moment",),
    )

    with pytest.raises(ValueError, match="exactly match the supplied menu"):
        validate_recommendation_action_result(
            result,
            candidate_action_ids=(
                "establish-prediction-moment",
                "compare-random-forest-now",
                "compare-gradient-boosted-trees-now",
            ),
            allowed_blocked_scopes=("model-comparison-claims",),
            allowed_clarification_ids=("prediction-moment",),
        )


def test_recommendation_result_rejects_unknown_scopes_and_clarifications() -> None:
    result = RecommendationActionResult(
        summary="A bounded result.",
        action_decisions=(
            RecommendationActionDecision(
                action_id="a",
                disposition=RecommendationDisposition.RECOMMENDED,
                rationale="It addresses the current objective.",
            ),
        ),
        blocked_scopes=("unknown-scope",),
        required_clarification_ids=("unknown-clarification",),
        warnings=(),
        methodological_basis=(),
    )

    with pytest.raises(ValueError, match="blocked scopes outside"):
        validate_recommendation_action_result(
            result,
            candidate_action_ids=("a",),
            allowed_blocked_scopes=(),
            allowed_clarification_ids=(),
        )


def test_recommendation_result_rejects_duplicate_action_ids() -> None:
    with pytest.raises(ValueError, match="unique action IDs"):
        RecommendationActionResult(
            summary="A bounded result.",
            action_decisions=(
                RecommendationActionDecision(
                    action_id="same",
                    disposition=RecommendationDisposition.RECOMMENDED,
                    rationale="First.",
                ),
                RecommendationActionDecision(
                    action_id="same",
                    disposition=RecommendationDisposition.NOT_NOW,
                    rationale="Second.",
                ),
            ),
            blocked_scopes=(),
            required_clarification_ids=(),
            warnings=(),
            methodological_basis=(),
        )


def test_generic_recommendation_request_has_structured_task_payload_and_empty_basis() -> None:
    request = ReasoningRequest(
        run_id="ra-generic-1",
        run_nonce="nonce-1",
        system_instruction="Classify every supplied candidate action.",
        user_task="Choose what should happen next.",
        project_evidence={"project.task": "binary classification"},
        task_payload={
            "candidate_actions": [
                {"action_id": "a", "label": "Do A", "cost_units": 1}
            ],
            "available_blocked_scopes": [],
            "available_clarifications": [],
        },
        methodological_context_payload={},
        methodological_context_sha256="0" * 64,
        knowledge_revisions=(),
        model_configuration=ReasoningModelConfiguration(
            requested_model="gpt-5.6-sol",
            reasoning_effort="medium",
            verbosity="low",
            max_output_tokens=4000,
        ),
        structured_output_kind=ReasoningOutputKind.RECOMMENDATION_ACTION,
    )

    payload = json.loads(request.canonical_model_input())
    assert payload["task_payload"]["candidate_actions"][0]["action_id"] == "a"
    assert request.structured_output_kind is ReasoningOutputKind.RECOMMENDATION_ACTION

    result = RecommendationActionResult(
        summary="Do A now.",
        action_decisions=(
            RecommendationActionDecision(
                action_id="a",
                disposition=RecommendationDisposition.RECOMMENDED,
                rationale="It addresses the current objective.",
            ),
        ),
        blocked_scopes=(),
        required_clarification_ids=(),
        warnings=(),
        methodological_basis=(),
    )
    validate_methodological_basis(result, request.knowledge_revisions)


def test_generic_recommendation_result_cannot_claim_unsupplied_methodological_basis() -> None:
    result = RecommendationActionResult(
        summary="A bounded result.",
        action_decisions=(
            RecommendationActionDecision(
                action_id="a",
                disposition=RecommendationDisposition.RECOMMENDED,
                rationale="It addresses the current objective.",
            ),
        ),
        blocked_scopes=(),
        required_clarification_ids=(),
        warnings=(),
        methodological_basis=("random-forest",),
    )

    with pytest.raises(ValueError, match="outside supplied context"):
        validate_methodological_basis(result, ())
