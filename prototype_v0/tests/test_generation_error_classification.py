from __future__ import annotations

from pathlib import Path

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelGenerationError, ModelMessage
from ads_v0.treatments import BaselineTreatmentRunner


class PermanentFailureModel:
    """Model double that exposes a non-retryable configuration/auth-style error."""

    def __init__(self) -> None:
        self.attempts = 0

    def generate(self, messages: tuple[ModelMessage, ...]):
        self.attempts += 1
        raise ModelGenerationError(
            "provider rejected the configured model",
            retryable=False,
            provider="fake-provider",
            error_code=404,
        )


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("permanent_generation_error_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def test_non_retryable_model_error_terminates_without_spending_retry_budget(
    case_bundle: Path,
) -> None:
    model = PermanentFailureModel()
    result = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=model,
        condition="B0",
        run_id="permanent-generation-error",
        max_model_calls=10,
        max_generation_retries=4,
    ).run()

    assert not result.completed
    assert result.model_calls == 0
    assert result.generation_attempts == 1
    assert result.generation_failures == 1
    assert model.attempts == 1
    assert result.terminal_generation_error is not None

    error_event = next(
        event
        for event in result.workspace.events
        if event.event_type == "MODEL_GENERATION_ERROR"
    )
    assert error_event.details["retryable"] is False
    assert error_event.details["provider"] == "fake-provider"
    assert error_event.details["error_code"] == 404

    terminal_event = next(
        event
        for event in result.workspace.events
        if event.event_type == "RUN_TERMINATED_GENERATION_ERROR"
    )
    assert terminal_event.details["retry_budget_exhausted"] is False
