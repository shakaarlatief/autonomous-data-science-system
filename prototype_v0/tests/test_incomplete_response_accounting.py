from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest

from ads_v0.casegen import CaseConfig, generate_case_bundle
from ads_v0.model import ModelGenerationError, ModelMessage, ModelUsage
from ads_v0.openai_model import OpenAIResponsesModel
from ads_v0.treatments import BaselineTreatmentRunner


class IncompleteResponses:
    def __init__(self) -> None:
        self.calls: list[dict] = []

    def create(self, **kwargs):
        self.calls.append(kwargs)
        return SimpleNamespace(
            id="resp-incomplete-1",
            status="incomplete",
            model=kwargs["model"],
            output_text="",
            incomplete_details=SimpleNamespace(reason="max_output_tokens"),
            usage=SimpleNamespace(
                input_tokens=250,
                output_tokens=30_000,
                total_tokens=30_250,
                output_tokens_details=SimpleNamespace(reasoning_tokens=30_000),
            ),
        )


class IncompleteClient:
    def __init__(self) -> None:
        self.responses = IncompleteResponses()


class UsageReportingFailureModel:
    def generate(self, messages: tuple[ModelMessage, ...]):
        raise ModelGenerationError(
            "generation exhausted fixed output budget",
            retryable=False,
            provider="fake-provider",
            error_code="max_output_tokens",
            usage=ModelUsage(
                input_tokens=11,
                output_tokens=97,
                total_tokens=108,
            ),
            provider_metadata={
                "response_id": "fake-incomplete-response",
                "reasoning_tokens": 97,
            },
        )


@pytest.fixture(scope="module")
def case_bundle(tmp_path_factory: pytest.TempPathFactory) -> Path:
    output = tmp_path_factory.mktemp("incomplete_usage_case") / "case"
    generate_case_bundle(output, CaseConfig())
    return output


def test_openai_incomplete_response_preserves_usage_and_specific_reason() -> None:
    client = IncompleteClient()
    model = OpenAIResponsesModel(client=client)

    messages = [
        ModelMessage(role="system", content="system instructions"),
        ModelMessage(role="user", content="begin project"),
    ]

    with pytest.raises(ModelGenerationError) as error_info:
        model.generate(messages)

    error = error_info.value
    assert error.retryable is False
    assert error.provider == "openai"
    assert error.error_code == "max_output_tokens"
    assert error.usage.input_tokens == 250
    assert error.usage.output_tokens == 30_000
    assert error.usage.total_tokens == 30_250
    assert error.provider_metadata["reasoning_tokens"] == 30_000
    assert error.provider_metadata["response_id"] == "resp-incomplete-1"
    assert client.responses.calls[0]["max_output_tokens"] == 30_000


def test_runner_accumulates_observable_usage_from_failed_generation(
    case_bundle: Path,
) -> None:
    result = BaselineTreatmentRunner(
        bundle_dir=case_bundle,
        model=UsageReportingFailureModel(),
        condition="B0",
        run_id="failed-generation-with-usage",
        max_model_calls=5,
        max_generation_retries=2,
    ).run()

    assert not result.completed
    assert result.model_calls == 0
    assert result.generation_attempts == 1
    assert result.generation_failures == 1
    assert result.input_tokens == 11
    assert result.output_tokens == 97
    assert result.total_tokens == 108

    error_event = next(
        event
        for event in result.workspace.events
        if event.event_type == "MODEL_GENERATION_ERROR"
    )
    assert error_event.details["error_code"] == "max_output_tokens"
    assert error_event.details["usage"]["total_tokens"] == 108
    assert error_event.details["provider_metadata"]["reasoning_tokens"] == 97

    terminal_event = next(
        event
        for event in result.workspace.events
        if event.event_type == "RUN_TERMINATED_GENERATION_ERROR"
    )
    assert terminal_event.details["observable_usage_so_far"]["total_tokens"] == 108
