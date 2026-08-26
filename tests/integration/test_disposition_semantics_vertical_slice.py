from __future__ import annotations

import asyncio
from pathlib import Path
from types import SimpleNamespace

from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.disposition_semantics.harness import (
    DispositionSemanticsResult,
    build_reasoning_plan,
    build_reasoning_request,
    load_frozen_benchmark,
)


FIXTURE = Path("tests/fixtures/reasoning/disposition_semantics_v1.json")


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
        assert agent.output_type is DispositionSemanticsResult
        usage = SimpleNamespace(
            input_tokens=120,
            output_tokens=24,
            total_tokens=144,
            input_tokens_details=None,
            output_tokens_details=None,
        )
        return SimpleNamespace(
            final_output=DispositionSemanticsResult(
                disposition="DEFER",
                defer_until_id="model-family-selected",
                rationale="The supplied plan waits for the explicit unresolved trigger.",
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


def test_openai_adapter_forwards_ads_owned_structured_output_type_without_live_sdk() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    entry = next(
        item
        for item in build_reasoning_plan(benchmark)
        if item.variant_id == "DS-01-DEFER"
    )
    request = build_reasoning_request(benchmark=benchmark, plan_entry=entry)

    outcome = asyncio.run(_ProviderFreeAdapter().run(request))

    assert isinstance(outcome.result, DispositionSemanticsResult)
    assert outcome.result.disposition == "DEFER"
    assert outcome.result.defer_until_id == "model-family-selected"
    assert outcome.trace.request_digest == request.semantic_digest()
    assert outcome.trace.knowledge_revisions == ()
    assert outcome.usage.input_tokens == 120
    assert _FakeAgent.last_instance is not None
    assert _FakeAgent.last_instance.output_type is DispositionSemanticsResult


def test_application_and_domain_layers_remain_provider_sdk_free() -> None:
    for root_name in ("application", "domain"):
        root = Path("src/ads_system") / root_name
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            assert "from agents" not in text
            assert "import agents" not in text
            assert "from openai" not in text
            assert "import openai" not in text
