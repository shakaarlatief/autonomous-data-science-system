"""OpenAI Agents SDK adapter for the ADS-owned stateless ReasoningRuntime port.

Framework/provider imports are intentionally lazy. Ordinary repository CI can
validate ADS application logic without installing or contacting the live
runtime dependency. Explicit live workflows install the frozen SDK version
before executing provider calls.
"""

from __future__ import annotations

from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
import json
import time
from typing import Any

from ads_system.application.recommendation import RecommendationActionResult
from ads_system.application.reasoning import (
    ReasoningContextValueResult,
    ReasoningOutcome,
    ReasoningOutputKind,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
    validate_methodological_basis,
)


OPENAI_AGENTS_PACKAGE = "openai-agents"
OPENAI_AGENTS_EXPECTED_VERSION = "0.19.4"
RUNTIME_NAME = "openai-agents-sdk"


class OpenAIAgentsReasoningRuntime:
    """No-tool OpenAI Agents SDK implementation of the ADS reasoning port."""

    def __init__(self, *, require_expected_version: bool = True) -> None:
        self._require_expected_version = require_expected_version

    @property
    def runtime_version(self) -> str:
        try:
            observed = version(OPENAI_AGENTS_PACKAGE)
        except PackageNotFoundError as exc:
            raise RuntimeError(
                "openai-agents is required for the live reasoning runtime; "
                f"expected {OPENAI_AGENTS_EXPECTED_VERSION}"
            ) from exc
        if self._require_expected_version and observed != OPENAI_AGENTS_EXPECTED_VERSION:
            raise RuntimeError(
                "OpenAI Agents SDK version does not match the frozen experiment: "
                f"expected {OPENAI_AGENTS_EXPECTED_VERSION}, observed {observed}"
            )
        return observed

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        agents = self._load_agents_module()
        reasoning_type = self._load_reasoning_type()
        runtime_version = self.runtime_version
        output_type = self._output_type(request.structured_output_kind)

        model_settings = agents.ModelSettings(
            reasoning=reasoning_type(effort=request.model_configuration.reasoning_effort),
            verbosity=request.model_configuration.verbosity,
            max_tokens=request.model_configuration.max_output_tokens,
            store=request.model_configuration.store,
            preserve_raw_usage=True,
        )
        agent = agents.Agent(
            name="ADS principal reasoner",
            instructions=request.system_instruction,
            model=request.model_configuration.requested_model,
            model_settings=model_settings,
            tools=[],
            output_type=output_type,
        )

        started = time.perf_counter()
        result = await agents.Runner.run(
            agent,
            request.canonical_model_input(),
            run_config=agents.RunConfig(tracing_disabled=True),
            max_turns=1,
        )
        latency_seconds = time.perf_counter() - started

        final_output = result.final_output
        if not isinstance(final_output, output_type):
            raise ValueError(
                "OpenAI Agents runtime returned an unexpected ADS structured result; "
                f"expected {output_type.__name__}, observed {type(final_output).__name__}"
            )
        validate_methodological_basis(final_output, request.knowledge_revisions)

        usage = self._normalize_usage(result)
        provider_model = self._provider_model(result, request.model_configuration.requested_model)
        trace = ReasoningTrace(
            run_id=request.run_id,
            request_digest=request.semantic_digest(),
            methodological_context_sha256=request.methodological_context_sha256,
            knowledge_revisions=request.knowledge_revisions,
            requested_model=request.model_configuration.requested_model,
            provider_model=provider_model,
            runtime_name=RUNTIME_NAME,
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
        return ReasoningOutcome(
            result=final_output,
            usage=usage,
            trace=trace,
            latency_seconds=latency_seconds,
        )

    @staticmethod
    def _output_type(kind: ReasoningOutputKind) -> type:
        if kind is ReasoningOutputKind.CONTEXT_VALUE:
            return ReasoningContextValueResult
        if kind is ReasoningOutputKind.RECOMMENDATION_ACTION:
            return RecommendationActionResult
        raise ValueError(f"unsupported ADS reasoning output kind: {kind!r}")

    @staticmethod
    def _load_agents_module() -> Any:
        try:
            return import_module("agents")
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "openai-agents is not installed; the live reasoning runtime must be executed "
                "through the frozen secret-gated environment"
            ) from exc

    @staticmethod
    def _load_reasoning_type() -> Any:
        try:
            module = import_module("openai.types.shared")
        except ModuleNotFoundError as exc:
            raise RuntimeError(
                "the OpenAI Python client required by openai-agents is not installed"
            ) from exc
        return module.Reasoning

    @staticmethod
    def _normalize_usage(result: Any) -> ReasoningUsage:
        sdk_usage = result.context_wrapper.usage
        input_details = getattr(sdk_usage, "input_tokens_details", None)
        output_details = getattr(sdk_usage, "output_tokens_details", None)

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

        raw_entries: list[dict[str, Any] | None] = []
        for response in result.raw_responses:
            raw = getattr(response, "raw_usage", None)
            if raw is None:
                raw_entries.append(None)
            else:
                raw_entries.append(json.loads(json.dumps(raw, sort_keys=True)))

        return ReasoningUsage(
            input_tokens=int(sdk_usage.input_tokens),
            output_tokens=int(sdk_usage.output_tokens),
            total_tokens=int(sdk_usage.total_tokens),
            cached_input_tokens=(
                int(cached_tokens) if cached_tokens is not None else None
            ),
            reasoning_tokens=(
                int(reasoning_tokens) if reasoning_tokens is not None else None
            ),
            service_tier=OpenAIAgentsReasoningRuntime._service_tier(raw_entries),
            raw_provider_usage={"responses": raw_entries},
        )

    @staticmethod
    def _service_tier(raw_entries: list[dict[str, Any] | None]) -> str | None:
        for entry in reversed(raw_entries):
            if not isinstance(entry, dict):
                continue
            value = entry.get("service_tier")
            if value is not None:
                return str(value)
        return None

    @staticmethod
    def _provider_model(result: Any, requested_model: str) -> str:
        """Extract provider model metadata when the SDK preserves it.

        ModelResponse intentionally normalizes provider responses and does not
        expose a top-level model field. Some response output items preserve
        provider_data with the concrete model name. The requested model is used
        only as a transparent fallback when that metadata is absent.
        """

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
