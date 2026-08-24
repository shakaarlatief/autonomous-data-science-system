from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace

from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.blocking_calibration.harness import (
    BlockingCalibrationResult,
    build_reasoning_plan,
    build_reasoning_request,
    load_frozen_benchmark,
)


FIXTURE = Path("tests/fixtures/reasoning/blocking_calibration_v1.json")


class _FakeModelSettings:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs


class _FakeAgent:
    last_instance = None

    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs
        self.output_type = kwargs["output_type"]
        _FakeAgent.last_instance = self


class _FakeRunConfig:
    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs


class _FakeRunner:
    @staticmethod
    async def run(agent, model_input, *, run_config, max_turns):
        del model_input, run_config, max_turns
        assert agent.output_type is BlockingCalibrationResult
        usage = SimpleNamespace(
            input_tokens=140,
            output_tokens=30,
            total_tokens=170,
            input_tokens_details=None,
            output_tokens_details=None,
        )
        return SimpleNamespace(
            final_output=BlockingCalibrationResult(
                disposition="BLOCKING_REQUIRED",
                blocking_requirement_id="feature-x-availability-confirmed",
                blocked_scope_id="defend-live-scoring-validity",
                rationale="The supplied active scope explicitly depends on the unresolved feature-availability requirement.",
            ),
            context_wrapper=SimpleNamespace(usage=usage),
            raw_responses=[],
        )


class _FakeReasoning:
    def __init__(self, *, effort: str) -> None:
        self.effort = effort


class _ProviderFreeAdapter(OpenAIAgentsReasoningRuntime):
    @property
    def runtime_version(self) -> str:
        return "0.19.4-test-double"

    @staticmethod
    def _load_agents_module():
        return SimpleNamespace(
            ModelSettings=_FakeModelSettings,
            Agent=_FakeAgent,
            RunConfig=_FakeRunConfig,
            Runner=_FakeRunner,
        )

    @staticmethod
    def _load_reasoning_type():
        return _FakeReasoning


def test_openai_adapter_forwards_blocking_calibration_output_type_without_live_sdk() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    entry = next(
        item
        for item in build_reasoning_plan(benchmark)
        if item.variant_id == "BC-01-BLOCKING"
    )
    request = build_reasoning_request(benchmark=benchmark, plan_entry=entry)

    outcome = asyncio.run(_ProviderFreeAdapter().run(request))

    assert isinstance(outcome.result, BlockingCalibrationResult)
    assert outcome.result.disposition == "BLOCKING_REQUIRED"
    assert outcome.result.blocking_requirement_id == "feature-x-availability-confirmed"
    assert outcome.result.blocked_scope_id == "defend-live-scoring-validity"
    assert outcome.trace.request_digest == request.semantic_digest()
    assert outcome.trace.knowledge_revisions == ()
    assert outcome.usage.input_tokens == 140
    assert _FakeAgent.last_instance is not None
    assert _FakeAgent.last_instance.output_type is BlockingCalibrationResult


def test_application_and_domain_layers_remain_provider_sdk_free() -> None:
    for root_name in ("application", "domain"):
        root = Path("src/ads_system") / root_name
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            assert "from agents" not in text
            assert "import agents" not in text
            assert "from openai" not in text
            assert "import openai" not in text
