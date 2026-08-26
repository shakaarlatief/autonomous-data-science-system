"""Remaining OpenAI Agents SDK 0.19.4 gates for Specification 005.

This module extends the already validated core adapter with the capabilities
that still require direct evidence: real MCP integration, application-driven
cancellation, bounded tool timeout behavior, controlled retry/failure behavior,
and normalized ADS-owned observability.

The code remains experiment-local. It is intentionally not a production runtime
port and does not move project state, methodological authority, provenance, or
side-effect idempotency into the SDK.
"""

from __future__ import annotations

import asyncio
from collections import defaultdict
import json
import sys
from time import perf_counter
from typing import Any

from agents import Agent, RunConfig, Runner
from agents.decorators import tool
from agents.exceptions import ToolTimeoutError
from agents.lifecycle import RunHooks
from agents.mcp import MCPServerStdio

from experiments.runtime_bakeoff.candidates.openai_agents.adapter import (
    OpenAIAgentsCandidate,
)
from experiments.runtime_bakeoff.harness import (
    ProposalLedger,
    RuntimeOutcome,
    RuntimeRecommendation,
    RuntimeStatus,
    RuntimeTrace,
    RuntimeWorkloadInput,
)


class ADSNormalizedRunHooks(RunHooks):
    """Translate SDK lifecycle callbacks into the stable experiment trace format."""

    def __init__(self, trace: RuntimeTrace) -> None:
        self.trace = trace
        self._tool_started_at: dict[str, float] = {}
        self._tool_attempts: defaultdict[str, int] = defaultdict(int)

    @staticmethod
    def _tool_name(tool: Any) -> str:
        return str(getattr(tool, "name", type(tool).__name__))

    @staticmethod
    def _call_id(context: Any, tool_name: str) -> str:
        return str(getattr(context, "tool_call_id", tool_name))

    async def on_llm_start(
        self,
        context: Any,
        agent: Any,
        system_prompt: str | None,
        input_items: list[Any],
    ) -> None:
        del context, system_prompt, input_items
        self.trace.record("model", "start", str(getattr(agent, "name", "agent")))

    async def on_llm_end(self, context: Any, agent: Any, response: Any) -> None:
        del context, agent
        usage = getattr(response, "usage", None)
        if usage is None:
            self.trace.record("runtime_metric", "token_usage", "unavailable")
            return

        requests = getattr(usage, "requests", None)
        input_tokens = getattr(usage, "input_tokens", None)
        output_tokens = getattr(usage, "output_tokens", None)
        self.trace.record(
            "runtime_metric",
            "model_usage",
            json.dumps(
                {
                    "requests": requests,
                    "input_tokens": input_tokens,
                    "output_tokens": output_tokens,
                },
                sort_keys=True,
            ),
        )

    async def on_tool_start(self, context: Any, agent: Any, tool: Any) -> None:
        del agent
        name = self._tool_name(tool)
        call_id = self._call_id(context, name)
        self._tool_attempts[name] += 1
        attempt = self._tool_attempts[name]
        if attempt > 1:
            self.trace.record("retry", name, f"attempt={attempt}")
        arguments = getattr(context, "tool_arguments", None)
        self.trace.record(
            "tool",
            name,
            json.dumps(
                {"phase": "start", "call_id": call_id, "arguments": arguments},
                sort_keys=True,
                default=str,
            ),
        )
        self._tool_started_at[call_id] = perf_counter()

    async def on_tool_end(
        self,
        context: Any,
        agent: Any,
        tool: Any,
        result: object,
    ) -> None:
        del agent
        name = self._tool_name(tool)
        call_id = self._call_id(context, name)
        started = self._tool_started_at.pop(call_id, None)
        elapsed_ms = None if started is None else round((perf_counter() - started) * 1000, 3)
        detail = json.dumps(
            {
                "phase": "end",
                "call_id": call_id,
                "elapsed_ms": elapsed_ms,
                "result": str(result),
            },
            sort_keys=True,
        )
        self.trace.record("tool", name, detail)
        if "error" in str(result).lower():
            self.trace.record("error", name, str(result))


class OpenAIAgentsExtendedEvaluator:
    """Bounded evaluator for the remaining OpenAI Agents SDK candidate gates."""

    def __init__(self, core: OpenAIAgentsCandidate) -> None:
        self._core = core
        self._active_tasks: dict[str, asyncio.Task[Any]] = {}

    def cancel(self, run_id: str) -> bool:
        """Request cancellation of an active candidate run through the application boundary."""

        task = self._active_tasks.get(run_id)
        if task is None or task.done():
            return False
        task.cancel()
        return True

    async def run_observed(
        self,
        workload: RuntimeWorkloadInput,
        model: Any,
    ) -> RuntimeOutcome:
        """Run the core candidate with ADS-normalized lifecycle observability."""

        trace = self._core._new_trace(workload)
        hooks = ADSNormalizedRunHooks(trace)
        started = perf_counter()
        trace.record("runtime", "start", f"openai-agents-sdk/{self._core.sdk_version}")
        trace.record("runtime_metric", "model_identity", type(model).__name__)

        current_task = asyncio.current_task()
        if current_task is not None:
            self._active_tasks[workload.run_id] = current_task

        try:
            agent = self._core._build_agent(workload, model)
            result = await Runner.run(
                agent,
                self._core._model_input(workload),
                context=self._core._local_context(workload),
                hooks=hooks,
                run_config=RunConfig(tracing_disabled=True),
            )
            self._core._record_model_usage(trace, model)
            outcome = self._core._normalize_result(workload, result, trace)
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return outcome
        except asyncio.CancelledError:
            trace.record("runtime", "cancel", "application-requested")
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)
        except Exception as exc:
            trace.record("error", type(exc).__name__, str(exc))
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
        finally:
            if current_task is not None and self._active_tasks.get(workload.run_id) is current_task:
                self._active_tasks.pop(workload.run_id, None)

    async def run_timeout_probe(
        self,
        workload: RuntimeWorkloadInput,
        model: Any,
        *,
        timeout_seconds: float = 0.02,
        delay_seconds: float = 0.2,
    ) -> RuntimeOutcome:
        """Prove released function-tool timeout behavior through a bounded async tool."""

        trace = self._core._new_trace(workload)
        hooks = ADSNormalizedRunHooks(trace)
        started = perf_counter()
        trace.record("runtime", "start", f"openai-agents-sdk/{self._core.sdk_version}")

        @tool(
            timeout=timeout_seconds,
            timeout_behavior="raise_exception",
            failure_error_function=None,
        )
        async def bounded_delay(seconds: float) -> str:
            """Sleep for the requested synthetic delay to exercise tool timeout behavior."""

            await asyncio.sleep(seconds)
            return "delay completed"

        agent = Agent(
            name="ADS timeout probe",
            instructions="Call bounded_delay exactly once.",
            model=model,
            tools=[bounded_delay],
        )

        try:
            await Runner.run(
                agent,
                json.dumps({"delay_seconds": delay_seconds}),
                context=self._core._local_context(workload),
                hooks=hooks,
                run_config=RunConfig(tracing_disabled=True),
            )
        except ToolTimeoutError as exc:
            trace.record("timeout", "bounded_delay", str(exc))
            trace.record("error", type(exc).__name__, str(exc))
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
        except Exception as exc:
            trace.record("error", type(exc).__name__, str(exc))
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

        return RuntimeOutcome(
            RuntimeStatus.FAILED,
            trace,
            error="timeout probe unexpectedly completed without ToolTimeoutError",
        )

    async def run_with_local_mcp(
        self,
        workload: RuntimeWorkloadInput,
        model: Any,
    ) -> RuntimeOutcome:
        """Run the representative read path through a real local stdio MCP server."""

        trace = self._core._new_trace(workload)
        hooks = ADSNormalizedRunHooks(trace)
        started = perf_counter()
        trace.record("runtime", "start", f"openai-agents-sdk/{self._core.sdk_version}")
        trace.record("runtime_metric", "model_identity", type(model).__name__)

        server = MCPServerStdio(
            params={
                "command": sys.executable,
                "args": [
                    "-m",
                    "experiments.runtime_bakeoff.candidates.openai_agents.local_mcp_server",
                ],
            },
            cache_tools_list=True,
            name="ads-methodological-reference",
            client_session_timeout_seconds=2,
            max_retry_attempts=1,
            retry_backoff_seconds_base=0.01,
            failure_error_function=None,
        )

        try:
            async with server:
                agent = self._build_mcp_agent(workload, model, server)
                result = await Runner.run(
                    agent,
                    self._core._model_input(workload),
                    context=self._core._local_context(workload),
                    hooks=hooks,
                    run_config=RunConfig(tracing_disabled=True),
                )
            self._core._record_model_usage(trace, model)
            outcome = self._core._normalize_result(workload, result, trace)
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return outcome
        except Exception as exc:
            trace.record("error", type(exc).__name__, str(exc))
            trace.record(
                "runtime_metric",
                "latency_ms",
                f"{(perf_counter() - started) * 1000:.3f}",
            )
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

    def _build_mcp_agent(
        self,
        workload: RuntimeWorkloadInput,
        model: Any,
        server: Any,
    ) -> Agent[Any]:
        ledger: ProposalLedger = self._core._proposal_ledger
        idempotency_key = f"proposal:{workload.run_id}:production-missingness"

        @tool
        def inspect_project_fact(key: str) -> str:
            """Read one explicitly requested fact from the current ADS project snapshot."""

            if key not in workload.project.facts:
                raise ValueError(f"unknown project fact: {key!r}")
            return workload.project.facts[key]

        @tool(needs_approval=True)
        def create_investigation_proposal(title: str) -> str:
            """Create an ADS Investigation proposal after explicit human approval."""

            created = ledger.create_once(
                idempotency_key,
                {
                    "title": title,
                    "source_run_id": workload.run_id,
                    "project_snapshot_id": workload.project.snapshot_id,
                    "context_pack_digest": workload.context_pack.semantic_digest(),
                },
            )
            return (
                "Investigation proposal recorded exactly once."
                if created
                else "Investigation proposal already existed for this idempotency key."
            )

        return Agent(
            name="ADS principal reasoner with MCP",
            instructions=(
                "Reason only over the bounded ADS context supplied in the input and explicit "
                "tools. Read project facts through inspect_project_fact. Use the MCP "
                "lookup_methodological_reference tool for methodological reference lookup. "
                "Return the final answer as RuntimeRecommendation structured output."
            ),
            model=model,
            tools=[inspect_project_fact, create_investigation_proposal],
            mcp_servers=[server],
            mcp_config={"failure_error_function": None},
            output_type=RuntimeRecommendation,
        )
