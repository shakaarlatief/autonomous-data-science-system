from __future__ import annotations

from pathlib import Path

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelGeneration, ModelMessage, ModelUsage
from ads_v0.treatments import BaselineTreatmentRunner


class FlakyModel:
    """Deterministic model double with configurable transient failures."""

    def __init__(self, *, failures_before_success: int, payload: dict) -> None:
        self.failures_before_success = failures_before_success
        self.payload = dict(payload)
        self.attempts = 0

    def generate(self, messages: tuple[ModelMessage, ...]) -> ModelGeneration:
        self.attempts += 1
        if self.attempts <= self.failures_before_success:
            raise RuntimeError(f"transient failure {self.attempts}")
        return ModelGeneration(
            payload=self.payload,
            model_name="flaky-model",
            usage=ModelUsage(input_tokens=12, output_tokens=4, total_tokens=16),
            provider_metadata={"provider": "fake", "response_id": "fake-1"},
        )


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("retry_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def test_transient_generation_failure_is_retried_and_traced(case_bundle: Path) -> None:
    model = FlakyModel(
        failures_before_success=1,
        payload={
            "rationale": "Inspect available project artifacts.",
            "command": {"type": "list_artifacts"},
        },
    )
    runner = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=model,
        condition="B0",
        run_id="transient-retry",
        max_model_calls=1,
        max_generation_retries=2,
    )

    result = runner.run()

    assert not result.completed
    assert result.model_calls == 1
    assert result.generation_attempts == 2
    assert result.generation_failures == 1
    assert result.terminal_generation_error is None
    assert result.total_tokens == 16

    error_events = [
        event for event in result.workspace.events if event.event_type == "MODEL_GENERATION_ERROR"
    ]
    success_events = [
        event for event in result.workspace.events if event.event_type == "MODEL_GENERATION"
    ]
    assert len(error_events) == 1
    assert len(success_events) == 1
    assert error_events[0].details["attempt_in_turn"] == 1
    assert success_events[0].details["generation_attempts_so_far"] == 2
    assert success_events[0].details["provider_metadata"]["provider"] == "fake"
    assert success_events[0].details["usage"]["total_tokens"] == 16


def test_exhausted_generation_retries_end_run_without_crashing(case_bundle: Path) -> None:
    model = FlakyModel(
        failures_before_success=99,
        payload={
            "rationale": "This payload should never be reached.",
            "command": {"type": "list_artifacts"},
        },
    )
    runner = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=model,
        condition="B1",
        run_id="exhausted-retry",
        max_model_calls=5,
        max_generation_retries=2,
    )

    result = runner.run()

    assert not result.completed
    assert result.model_calls == 0
    assert result.generation_attempts == 3
    assert result.generation_failures == 3
    assert result.terminal_generation_error is not None
    assert "transient failure 3" in result.terminal_generation_error

    terminal_events = [
        event
        for event in result.workspace.events
        if event.event_type == "RUN_TERMINATED_GENERATION_ERROR"
    ]
    assert len(terminal_events) == 1
    assert terminal_events[0].details["generation_attempts"] == 3
    assert terminal_events[0].details["generation_failures"] == 3


def test_generation_retry_policy_validation(case_bundle: Path) -> None:
    model = FlakyModel(
        failures_before_success=0,
        payload={
            "rationale": "Inspect.",
            "command": {"type": "list_artifacts"},
        },
    )

    with pytest.raises(ValueError, match="cannot be negative"):
        BaselineTreatmentRunner(
            bundle_dir=case_bundle,
            model=model,
            condition="B0",
            run_id="invalid-retry-budget",
            max_generation_retries=-1,
        )
