"""Condition-blinded semantic judge for frozen Specification 021.

Deterministic software owns exact dispositions, requirement/scope pointers,
defer pointers, and system-owned provenance integrity. The semantic judge is
limited to the preregistered rubric obligations requiring interpretation of the
candidate rationale and project-state consistency.
"""

from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
import json
import time
from typing import Any, Mapping

from ads_system.application.reasoning import ReasoningModelConfiguration, ReasoningUsage
from experiments.dependency_backed_recommendation_action_value.harness import JudgeResult


OPENAI_AGENTS_PACKAGE = "openai-agents"
OPENAI_AGENTS_EXPECTED_VERSION = "0.19.4"


@dataclass(frozen=True, slots=True)
class JudgeOutcome:
    judge_id: str
    result: JudgeResult
    usage: ReasoningUsage
    latency_seconds: float
    requested_model: str
    provider_model: str
    runtime_version: str
    provider_response_ids: tuple[str, ...]
    provider_request_ids: tuple[str, ...]


class OpenAIAgentsDependencyBackedRecommendationJudge:
    """No-tool OpenAI Agents implementation of the frozen blinded judge."""

    def __init__(
        self,
        model_configuration: ReasoningModelConfiguration,
        *,
        require_expected_version: bool = True,
    ) -> None:
        self._model_configuration = model_configuration
        self._require_expected_version = require_expected_version

    @property
    def runtime_version(self) -> str:
        try:
            observed = version(OPENAI_AGENTS_PACKAGE)
        except PackageNotFoundError as exc:
            raise RuntimeError(
                "openai-agents is required for the live Specification 021 judge; "
                f"expected {OPENAI_AGENTS_EXPECTED_VERSION}"
            ) from exc
        if self._require_expected_version and observed != OPENAI_AGENTS_EXPECTED_VERSION:
            raise RuntimeError(
                "OpenAI Agents SDK version does not match the frozen judge environment: "
                f"expected {OPENAI_AGENTS_EXPECTED_VERSION}, observed {observed}"
            )
        return observed

    async def judge(self, *, judge_id: str, payload: Mapping[str, object]) -> JudgeOutcome:
        agents = self._load_agents_module()
        reasoning_type = self._load_reasoning_type()
        runtime_version = self.runtime_version
        settings = self._model_configuration
        model_settings = agents.ModelSettings(
            reasoning=reasoning_type(effort=settings.reasoning_effort),
            verbosity=settings.verbosity,
            max_tokens=settings.max_output_tokens,
            store=settings.store,
            preserve_raw_usage=True,
        )
        agent = agents.Agent(
            name="ADS blinded dependency-backed recommendation judge",
            instructions=(
                "Score only the rubric obligations supplied in the input. Do not add, "
                "remove, merge, or reinterpret obligations. Return scores in exact rubric "
                "order. Score 0 when an obligation is absent, materially wrong, or "
                "contradicted; 1 when partially or implicitly satisfied without material "
                "contradiction; 2 when explicitly and correctly satisfied. Compute "
                "normalized_score as sum(scores)/(2*number_of_obligations). Set "
                "critical_failure true exactly when at least one critical rubric item "
                "receives score 0. Judge only against the visible user task, project "
                "evidence, supplied requirement/scope/action/trigger relation menus, "
                "candidate structured result, and frozen rubric. Do not infer which "
                "experimental condition produced the candidate. Exact expected "
                "dispositions and expected relation pointers are intentionally hidden and "
                "evaluated separately by deterministic software."
            ),
            model=settings.requested_model,
            model_settings=model_settings,
            tools=[],
            output_type=JudgeResult,
        )
        model_input = json.dumps(
            dict(payload), sort_keys=True, separators=(",", ":"), ensure_ascii=False
        )
        started = time.perf_counter()
        result = await agents.Runner.run(
            agent,
            model_input,
            run_config=agents.RunConfig(tracing_disabled=True),
            max_turns=1,
        )
        latency_seconds = time.perf_counter() - started
        final_output = result.final_output
        if not isinstance(final_output, JudgeResult):
            raise ValueError(
                "Specification 021 judge did not return JudgeResult; "
                f"observed {type(final_output).__name__}"
            )
        raw_entries = self._raw_usage_entries(result)
        return JudgeOutcome(
            judge_id=judge_id,
            result=final_output,
            usage=self._normalize_usage(result, raw_entries),
            latency_seconds=latency_seconds,
            requested_model=settings.requested_model,
            provider_model=self._provider_model(result, settings.requested_model),
            runtime_version=runtime_version,
            provider_response_ids=tuple(
                str(response.response_id)
                for response in result.raw_responses
                if getattr(response, "response_id", None)
            ),
            provider_request_ids=tuple(
                str(response.request_id)
                for response in result.raw_responses
                if getattr(response, "request_id", None)
            ),
        )

    @staticmethod
    def _load_agents_module() -> Any:
        try:
            return import_module("agents")
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "openai-agents is not installed; the semantic judge may run only in "
                "the frozen explicit live environment"
            ) from exc

    @staticmethod
    def _load_reasoning_type() -> Any:
        try:
            return import_module("openai.types.shared").Reasoning
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "the OpenAI Python client required by openai-agents is not installed"
            ) from exc

    @staticmethod
    def _raw_usage_entries(result: Any) -> list[dict[str, Any] | None]:
        entries: list[dict[str, Any] | None] = []
        for response in result.raw_responses:
            raw = getattr(response, "raw_usage", None)
            entries.append(None if raw is None else json.loads(json.dumps(raw, sort_keys=True)))
        return entries

    @staticmethod
    def _normalize_usage(
        result: Any,
        raw_entries: list[dict[str, Any] | None],
    ) -> ReasoningUsage:
        usage = result.context_wrapper.usage
        input_details = getattr(usage, "input_tokens_details", None)
        output_details = getattr(usage, "output_tokens_details", None)
        cached_tokens = (
            getattr(input_details, "cached_tokens", None)
            if input_details is not None
            else None
        )
        reasoning_tokens = (
            getattr(output_details, "reasoning_tokens", None)
            if output_details is not None
            else None
        )
        return ReasoningUsage(
            input_tokens=int(usage.input_tokens),
            output_tokens=int(usage.output_tokens),
            total_tokens=int(usage.total_tokens),
            cached_input_tokens=(int(cached_tokens) if cached_tokens is not None else None),
            reasoning_tokens=(int(reasoning_tokens) if reasoning_tokens is not None else None),
            service_tier=OpenAIAgentsDependencyBackedRecommendationJudge._service_tier(raw_entries),
            raw_provider_usage={"responses": raw_entries},
        )

    @staticmethod
    def _service_tier(raw_entries: list[dict[str, Any] | None]) -> str | None:
        for entry in reversed(raw_entries):
            if isinstance(entry, dict) and entry.get("service_tier") is not None:
                return str(entry["service_tier"])
        return None

    @staticmethod
    def _provider_model(result: Any, requested_model: str) -> str:
        for response in reversed(result.raw_responses):
            for item in reversed(getattr(response, "output", ())):
                provider_data = getattr(item, "provider_data", None)
                if isinstance(provider_data, dict) and provider_data.get("model"):
                    return str(provider_data["model"])
                model_dump = getattr(item, "model_dump", None)
                if callable(model_dump):
                    dumped = model_dump()
                    if isinstance(dumped, dict):
                        provider_data = dumped.get("provider_data")
                        if isinstance(provider_data, dict) and provider_data.get("model"):
                            return str(provider_data["model"])
        return requested_model
