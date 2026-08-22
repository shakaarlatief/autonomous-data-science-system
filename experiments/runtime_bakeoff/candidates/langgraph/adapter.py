"""LangGraph 1.2.10 durability comparator for the Specification 005 bakeoff.

The implementation deliberately keeps LangGraph below an ADS-owned adapter.
Graph state is runtime execution state, not project or methodological authority.
The representative workload, exact context-pack provenance, structured result,
approval semantics, and authoritative proposal idempotency remain owned by the
framework-neutral runtime-bakeoff harness.

The comparator uses a small explicit StateGraph rather than a prebuilt agent so
that checkpoint, interrupt, restart, retry, and replay semantics remain visible.
The principal reasoner is a deterministic provider-neutral double whose next
turn depends only on the persisted transcript. A production provider adapter
could replace that double without changing ADS authority or the graph contract.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict
import json
from pathlib import Path
from time import perf_counter
from typing import Annotated, Any, Protocol, TypedDict
import operator

from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langgraph.errors import NodeTimeoutError
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, RetryPolicy, interrupt

from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    MethodologicalReferenceGateway,
    ProposalLedger,
    RuntimeInterrupt,
    RuntimeOutcome,
    RuntimeRecommendation,
    RuntimeResumeToken,
    RuntimeStatus,
    RuntimeTrace,
    RuntimeTraceEvent,
    RuntimeWorkloadInput,
)


LANGGRAPH_VERSION = "1.2.10"
CHECKPOINT_SQLITE_VERSION = "3.1.1"
MCP_ADAPTER_VERSION = "0.3.1"


class LangGraphToolCall(TypedDict):
    call_id: str
    name: str
    arguments: dict[str, str]


class LangGraphTurn(TypedDict, total=False):
    tool_call: LangGraphToolCall
    recommendation: dict[str, Any]


class LangGraphExecutionState(TypedDict, total=False):
    transcript: Annotated[list[dict[str, Any]], operator.add]
    trace_events: Annotated[list[dict[str, str]], operator.add]
    pending_call: LangGraphToolCall | None
    recommendation: dict[str, Any] | None


class LangGraphReasoner(Protocol):
    model_id: str

    async def next_turn(
        self,
        transcript: list[dict[str, Any]],
        workload: RuntimeWorkloadInput,
    ) -> LangGraphTurn:
        """Return one deterministic/provider-normalized reasoning turn."""


class DeterministicLangGraphReasoner:
    """Provider-neutral reasoner double driven entirely by persisted transcript state.

    The double is intentionally stateless. Reconstructing it in a new runtime
    process therefore cannot accidentally supply hidden progress. The graph
    checkpoint must contain enough execution state to determine the next turn.
    """

    model_id = "deterministic-langgraph-reasoner"

    async def next_turn(
        self,
        transcript: list[dict[str, Any]],
        workload: RuntimeWorkloadInput,
    ) -> LangGraphTurn:
        completed_tools = {
            str(item.get("name"))
            for item in transcript
            if item.get("type") == "tool_result"
        }

        if "inspect_project_fact" not in completed_tools:
            return {
                "tool_call": {
                    "call_id": "lg_fact_prediction_moment",
                    "name": "inspect_project_fact",
                    "arguments": {"key": "prediction_moment"},
                }
            }

        if "lookup_methodological_reference" not in completed_tools:
            return {
                "tool_call": {
                    "call_id": "lg_reference_missingness",
                    "name": "lookup_methodological_reference",
                    "arguments": {"query": "missingness validation leakage"},
                }
            }

        if "create_investigation_proposal" not in completed_tools:
            return {
                "tool_call": {
                    "call_id": "lg_proposal_missingness",
                    "name": "create_investigation_proposal",
                    "arguments": {
                        "title": "Investigate production-time missingness before validation design"
                    },
                }
            }

        proposal_result = next(
            (
                str(item.get("content", ""))
                for item in reversed(transcript)
                if item.get("type") == "tool_result"
                and item.get("name") == "create_investigation_proposal"
            ),
            "",
        )
        approved = "recorded" in proposal_result.lower() or "already" in proposal_result.lower()
        revisions = tuple(item.revision_id for item in workload.context_pack.revisions)
        return {
            "recommendation": {
                "next_investigation": (
                    "Characterize production-time missingness and feature availability "
                    "before finalizing validation."
                ),
                "validation_implication": (
                    "Reassess chronological validation and feature construction against "
                    "the confirmed prediction moment."
                ),
                "reasons": [
                    "Production-time missingness changes what information is legitimately available.",
                    (
                        "The approved Investigation proposal is recorded through ADS."
                        if approved
                        else "The Investigation proposal was not approved for creation."
                    ),
                ],
                "referenced_revision_ids": list(revisions),
            }
        }


class DelayedLangGraphReasoner(DeterministicLangGraphReasoner):
    """Reasoner double exposing a deterministic cancellation point."""

    model_id = "delayed-langgraph-reasoner"

    def __init__(self, delay_seconds: float = 5.0) -> None:
        self.delay_seconds = delay_seconds
        self.started = asyncio.Event()

    async def next_turn(
        self,
        transcript: list[dict[str, Any]],
        workload: RuntimeWorkloadInput,
    ) -> LangGraphTurn:
        self.started.set()
        await asyncio.sleep(self.delay_seconds)
        return await super().next_turn(transcript, workload)


class ApprovalReplayProbe:
    """Harmless test instrumentation proving node restart around interrupt().

    This counter is deliberately not project state. It exists only to observe
    how many times the approval node entered before/while replaying the same
    persisted interrupt checkpoint.
    """

    def __init__(self) -> None:
        self.entries = 0

    def record_entry(self) -> int:
        self.entries += 1
        return self.entries


class LangGraphCandidate:
    """ADS adapter around one explicit LangGraph durability comparator."""

    def __init__(
        self,
        checkpoint_path: str | Path,
        reasoner: LangGraphReasoner,
        reference_gateway: MethodologicalReferenceGateway,
        proposal_ledger: ProposalLedger,
        *,
        replay_probe: ApprovalReplayProbe | None = None,
        mcp_tool: Any | None = None,
    ) -> None:
        self.checkpoint_path = str(Path(checkpoint_path))
        self.reasoner = reasoner
        self.reference_gateway = reference_gateway
        self.proposal_ledger = proposal_ledger
        self.replay_probe = replay_probe or ApprovalReplayProbe()
        self.mcp_tool = mcp_tool
        self._active_tasks: dict[str, asyncio.Task[Any]] = {}
        self._lookup_attempts: dict[str, int] = {}

    @property
    def runtime_id(self) -> str:
        return f"langgraph/{LANGGRAPH_VERSION}"

    async def run(self, workload: RuntimeWorkloadInput) -> RuntimeOutcome:
        """Run until completion or approval interruption using persistent SQLite checkpoints."""

        started = perf_counter()
        current_task = asyncio.current_task()
        if current_task is not None:
            self._active_tasks[workload.run_id] = current_task

        try:
            async with AsyncSqliteSaver.from_conn_string(self.checkpoint_path) as saver:
                graph = self._build_graph(workload, saver)
                config = self._thread_config(workload.run_id)
                initial_state: LangGraphExecutionState = {
                    "transcript": [],
                    "trace_events": [
                        self._event("runtime", "start", self.runtime_id),
                        self._event("model", "identity", self.reasoner.model_id),
                        self._event(
                            "context",
                            "pack",
                            json.dumps(
                                {
                                    "context_pack_id": workload.context_pack.pack_id,
                                    "context_pack_digest": workload.context_pack.semantic_digest(),
                                    "project_snapshot_id": workload.project.snapshot_id,
                                    "knowledge_revision_ids": [
                                        item.revision_id for item in workload.context_pack.revisions
                                    ],
                                },
                                sort_keys=True,
                            ),
                        ),
                    ],
                    "pending_call": None,
                    "recommendation": None,
                }
                result = await graph.ainvoke(initial_state, config=config)
                snapshot = await graph.aget_state(config)
                return self._normalize_result(
                    workload,
                    result,
                    snapshot.config,
                    started=started,
                )
        except asyncio.CancelledError:
            trace = self._new_trace(workload)
            trace.record("runtime", "start", self.runtime_id)
            trace.record("model", "identity", self.reasoner.model_id)
            trace.record("runtime", "cancel", "application-requested")
            trace.record("runtime_metric", "latency_ms", self._elapsed_ms(started))
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)
        except Exception as exc:
            trace = self._new_trace(workload)
            trace.record("runtime", "start", self.runtime_id)
            trace.record("error", type(exc).__name__, str(exc))
            trace.record("runtime_metric", "latency_ms", self._elapsed_ms(started))
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
        finally:
            if current_task is not None and self._active_tasks.get(workload.run_id) is current_task:
                self._active_tasks.pop(workload.run_id, None)

    async def resume(
        self,
        workload: RuntimeWorkloadInput,
        serialized_token: str,
        decision: ApprovalDecision,
    ) -> RuntimeOutcome:
        """Resume the exact persisted interrupt checkpoint in a newly created adapter instance."""

        token = RuntimeResumeToken.from_json(serialized_token)
        self._validate_resume_token(workload, token)
        started = perf_counter()
        execution_state = token.execution_state
        thread_id = str(execution_state.get("thread_id", ""))
        checkpoint_id = str(execution_state.get("checkpoint_id", ""))
        checkpoint_path = str(execution_state.get("checkpoint_path", ""))
        if not thread_id or not checkpoint_id:
            raise ValueError("LangGraph resume token is missing thread/checkpoint identity")
        if Path(checkpoint_path) != Path(self.checkpoint_path):
            raise ValueError("LangGraph resume token points to a different checkpoint database")

        async with AsyncSqliteSaver.from_conn_string(self.checkpoint_path) as saver:
            graph = self._build_graph(workload, saver)
            config = {
                "configurable": {
                    "thread_id": thread_id,
                    "checkpoint_id": checkpoint_id,
                }
            }
            try:
                result = await graph.ainvoke(
                    Command(resume=decision is ApprovalDecision.APPROVE),
                    config=config,
                )
                snapshot = await graph.aget_state(
                    {"configurable": {"thread_id": thread_id}}
                )
                outcome = self._normalize_result(
                    workload,
                    result,
                    snapshot.config,
                    started=started,
                    resumed_decision=decision,
                )
                return outcome
            except Exception as exc:
                trace = self._new_trace(workload)
                trace.record("runtime", "resume", decision.value)
                trace.record("error", type(exc).__name__, str(exc))
                trace.record("runtime_metric", "latency_ms", self._elapsed_ms(started))
                return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

    def cancel(self, run_id: str) -> bool:
        """Cancel an active graph invocation through the ADS application boundary."""

        task = self._active_tasks.get(run_id)
        if task is None or task.done():
            return False
        task.cancel()
        return True

    async def timeout_probe(
        self,
        workload: RuntimeWorkloadInput,
        *,
        timeout_seconds: float = 0.02,
        delay_seconds: float = 0.2,
    ) -> RuntimeOutcome:
        """Exercise released async-node timeout behavior without an external provider."""

        started = perf_counter()

        class TimeoutState(TypedDict, total=False):
            value: str

        async def slow_node(state: TimeoutState) -> dict[str, str]:
            del state
            await asyncio.sleep(delay_seconds)
            return {"value": "completed"}

        builder = StateGraph(TimeoutState)
        builder.add_node("slow", slow_node, timeout=timeout_seconds)
        builder.add_edge(START, "slow")
        builder.add_edge("slow", END)
        graph = builder.compile()

        try:
            await graph.ainvoke({})
        except NodeTimeoutError as exc:
            trace = self._new_trace(workload)
            trace.record("runtime", "start", self.runtime_id)
            trace.record("timeout", "slow", str(exc))
            trace.record("error", type(exc).__name__, str(exc))
            trace.record("runtime_metric", "latency_ms", self._elapsed_ms(started))
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
        except Exception as exc:
            trace = self._new_trace(workload)
            trace.record("runtime", "start", self.runtime_id)
            trace.record("error", type(exc).__name__, str(exc))
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

        trace = self._new_trace(workload)
        trace.record("runtime", "start", self.runtime_id)
        return RuntimeOutcome(
            RuntimeStatus.FAILED,
            trace,
            error="timeout probe unexpectedly completed without NodeTimeoutError",
        )

    def _build_graph(
        self,
        workload: RuntimeWorkloadInput,
        saver: AsyncSqliteSaver,
    ):
        lookup_attempts = self._lookup_attempts

        async def principal_reasoner(
            state: LangGraphExecutionState,
        ) -> dict[str, Any]:
            transcript = list(state.get("transcript", []))
            turn = await self.reasoner.next_turn(transcript, workload)
            events = [
                self._event(
                    "model_call",
                    self.reasoner.model_id,
                    f"transcript_items={len(transcript)}",
                )
            ]
            if "recommendation" in turn:
                return {
                    "recommendation": dict(turn["recommendation"]),
                    "pending_call": None,
                    "trace_events": events
                    + [self._event("model", "structured_output", "candidate")],
                }
            return {
                "pending_call": dict(turn["tool_call"]),
                "recommendation": None,
                "trace_events": events,
            }

        async def inspect_project_fact(
            state: LangGraphExecutionState,
        ) -> dict[str, Any]:
            call = self._require_pending_call(state, "inspect_project_fact")
            key = call["arguments"].get("key")
            if key is None or key not in workload.project.facts:
                raise ValueError(f"unknown project fact: {key!r}")
            result = workload.project.facts[key]
            return {
                "pending_call": None,
                "transcript": [self._tool_result(call, result)],
                "trace_events": [
                    self._event(
                        "tool",
                        call["name"],
                        json.dumps(
                            {
                                "call_id": call["call_id"],
                                "arguments": call["arguments"],
                                "result": result,
                            },
                            sort_keys=True,
                        ),
                    )
                ],
            }

        async def lookup_methodological_reference(
            state: LangGraphExecutionState,
        ) -> dict[str, Any]:
            call = self._require_pending_call(
                state,
                "lookup_methodological_reference",
            )
            query = call["arguments"].get("query")
            if not query:
                raise ValueError("lookup_methodological_reference requires query")

            attempt_key = f"{workload.run_id}:{call['call_id']}"
            lookup_attempts[attempt_key] = lookup_attempts.get(attempt_key, 0) + 1
            attempt = lookup_attempts[attempt_key]

            if self.mcp_tool is None:
                result = self.reference_gateway.lookup(query)
            else:
                result = await self.mcp_tool.ainvoke({"query": query})
                result = str(result)

            events: list[dict[str, str]] = []
            if attempt > 1:
                events.append(
                    self._event(
                        "retry",
                        call["name"],
                        f"attempt={attempt}",
                    )
                )
            events.append(
                self._event(
                    "tool",
                    call["name"],
                    json.dumps(
                        {
                            "call_id": call["call_id"],
                            "arguments": call["arguments"],
                            "attempt": attempt,
                            "result": result,
                            "transport": "mcp" if self.mcp_tool is not None else "gateway",
                        },
                        sort_keys=True,
                    ),
                )
            )
            return {
                "pending_call": None,
                "transcript": [self._tool_result(call, result)],
                "trace_events": events,
            }

        async def create_investigation_proposal(
            state: LangGraphExecutionState,
        ) -> dict[str, Any]:
            call = self._require_pending_call(
                state,
                "create_investigation_proposal",
            )
            entry = self.replay_probe.record_entry()
            approved = interrupt(
                {
                    "kind": "TOOL_APPROVAL",
                    "tool_name": call["name"],
                    "call_id": call["call_id"],
                    "arguments": call["arguments"],
                    "reason": (
                        "Creating a project Investigation proposal is an authoritative side effect."
                    ),
                }
            )

            events: list[dict[str, str]] = []
            if entry > 1:
                events.append(
                    self._event(
                        "replay",
                        "approval_node_restart",
                        f"entry={entry}",
                    )
                )

            if not bool(approved):
                result = "Project-state creation rejected by the human."
                events.append(self._event("approval", call["name"], "rejected"))
            else:
                idempotency_key = (
                    f"proposal:{workload.run_id}:production-missingness"
                )
                created = self.proposal_ledger.create_once(
                    idempotency_key,
                    {
                        "title": call["arguments"]["title"],
                        "source_run_id": workload.run_id,
                        "project_snapshot_id": workload.project.snapshot_id,
                        "context_pack_digest": workload.context_pack.semantic_digest(),
                    },
                )
                result = (
                    "Investigation proposal recorded exactly once."
                    if created
                    else "Investigation proposal already existed for this idempotency key."
                )
                events.append(
                    self._event(
                        "approval",
                        call["name"],
                        "executed" if created else "already-executed",
                    )
                )

            return {
                "pending_call": None,
                "transcript": [self._tool_result(call, result)],
                "trace_events": events,
            }

        def route_after_reasoner(state: LangGraphExecutionState) -> str:
            if state.get("recommendation") is not None:
                return END
            call = state.get("pending_call")
            if not call:
                raise ValueError("reasoner produced neither recommendation nor tool call")
            name = call.get("name")
            if name not in {
                "inspect_project_fact",
                "lookup_methodological_reference",
                "create_investigation_proposal",
            }:
                raise ValueError(f"unsupported LangGraph tool call: {name!r}")
            return str(name)

        retry_policy = RetryPolicy(
            initial_interval=0.001,
            backoff_factor=1.0,
            max_interval=0.001,
            max_attempts=2,
            jitter=False,
            retry_on=RuntimeError,
        )

        builder = StateGraph(LangGraphExecutionState)
        builder.add_node("principal_reasoner", principal_reasoner)
        builder.add_node("inspect_project_fact", inspect_project_fact)
        builder.add_node(
            "lookup_methodological_reference",
            lookup_methodological_reference,
            retry_policy=retry_policy,
        )
        builder.add_node(
            "create_investigation_proposal",
            create_investigation_proposal,
        )
        builder.add_edge(START, "principal_reasoner")
        builder.add_conditional_edges("principal_reasoner", route_after_reasoner)
        builder.add_edge("inspect_project_fact", "principal_reasoner")
        builder.add_edge("lookup_methodological_reference", "principal_reasoner")
        builder.add_edge("create_investigation_proposal", "principal_reasoner")
        return builder.compile(checkpointer=saver)

    def _normalize_result(
        self,
        workload: RuntimeWorkloadInput,
        result: dict[str, Any],
        checkpoint_config: dict[str, Any],
        *,
        started: float,
        resumed_decision: ApprovalDecision | None = None,
    ) -> RuntimeOutcome:
        trace = self._trace_from_state(workload, result)
        if resumed_decision is not None:
            trace.record("runtime", "resume", resumed_decision.value)
        trace.record("runtime_metric", "latency_ms", self._elapsed_ms(started))

        interrupts = result.get("__interrupt__", ())
        if interrupts:
            pending = result.get("pending_call")
            if not isinstance(pending, dict):
                return RuntimeOutcome(
                    RuntimeStatus.FAILED,
                    trace,
                    error="LangGraph interrupt did not preserve the pending tool call",
                )
            first = interrupts[0]
            interrupt_value = getattr(first, "value", {})
            interrupt_id = str(
                getattr(first, "id", None)
                or f"approval:{workload.run_id}:{pending.get('call_id', 'unknown')}"
            )
            runtime_interrupt = RuntimeInterrupt(
                interrupt_id=interrupt_id,
                kind=str(interrupt_value.get("kind", "TOOL_APPROVAL")),
                tool_name=str(interrupt_value.get("tool_name", pending.get("name", ""))),
                arguments={
                    str(key): str(value)
                    for key, value in dict(
                        interrupt_value.get("arguments", pending.get("arguments", {}))
                    ).items()
                },
                reason=str(
                    interrupt_value.get(
                        "reason",
                        "Authoritative side effect requires approval.",
                    )
                ),
            )
            configurable = dict(checkpoint_config.get("configurable", {}))
            checkpoint_id = str(configurable.get("checkpoint_id", ""))
            thread_id = str(configurable.get("thread_id", workload.run_id))
            if not checkpoint_id:
                return RuntimeOutcome(
                    RuntimeStatus.FAILED,
                    trace,
                    error="LangGraph interruption did not expose a persisted checkpoint_id",
                )
            trace.record("interrupt", runtime_interrupt.tool_name, interrupt_id)
            trace.record("checkpoint", "persisted", checkpoint_id)
            token = RuntimeResumeToken(
                run_id=workload.run_id,
                next_step=0,
                interrupt=runtime_interrupt,
                context_pack_id=workload.context_pack.pack_id,
                context_pack_digest=workload.context_pack.semantic_digest(),
                project_snapshot_id=workload.project.snapshot_id,
                proposal_idempotency_key=(
                    f"proposal:{workload.run_id}:production-missingness"
                ),
                execution_state={
                    "runtime": self.runtime_id,
                    "thread_id": thread_id,
                    "checkpoint_id": checkpoint_id,
                    "checkpoint_path": self.checkpoint_path,
                },
            )
            return RuntimeOutcome(
                RuntimeStatus.INTERRUPTED,
                trace,
                interruption=runtime_interrupt,
                resume_token=token,
            )

        raw_recommendation = result.get("recommendation")
        if not isinstance(raw_recommendation, dict):
            return RuntimeOutcome(
                RuntimeStatus.FAILED,
                trace,
                error="LangGraph run completed without RuntimeRecommendation payload",
            )
        try:
            recommendation = RuntimeRecommendation(
                next_investigation=str(raw_recommendation["next_investigation"]),
                validation_implication=str(raw_recommendation["validation_implication"]),
                reasons=tuple(str(item) for item in raw_recommendation["reasons"]),
                referenced_revision_ids=tuple(
                    str(item) for item in raw_recommendation["referenced_revision_ids"]
                ),
            )
            self._validate_recommendation(workload, recommendation)
        except (KeyError, TypeError, ValueError) as exc:
            trace.record("validation", "structured_output", "rejected")
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

        trace.record("validation", "structured_output", "accepted")
        return RuntimeOutcome(
            RuntimeStatus.COMPLETED,
            trace,
            recommendation=recommendation,
        )

    def _trace_from_state(
        self,
        workload: RuntimeWorkloadInput,
        result: dict[str, Any],
    ) -> RuntimeTrace:
        trace = self._new_trace(workload)
        raw_events = result.get("trace_events", [])
        for raw in raw_events:
            if not isinstance(raw, dict):
                continue
            trace.record(
                str(raw.get("kind", "runtime")),
                str(raw.get("name", "event")),
                str(raw.get("detail", "")),
            )
        return trace

    def _new_trace(self, workload: RuntimeWorkloadInput) -> RuntimeTrace:
        return RuntimeTrace(
            run_id=workload.run_id,
            project_snapshot_id=workload.project.snapshot_id,
            context_pack_id=workload.context_pack.pack_id,
            context_pack_digest=workload.context_pack.semantic_digest(),
            knowledge_revision_ids=tuple(
                item.revision_id for item in workload.context_pack.revisions
            ),
        )

    @staticmethod
    def _event(kind: str, name: str, detail: str) -> dict[str, str]:
        return {"kind": kind, "name": name, "detail": detail}

    @staticmethod
    def _tool_result(call: LangGraphToolCall, result: str) -> dict[str, Any]:
        return {
            "type": "tool_result",
            "call_id": call["call_id"],
            "name": call["name"],
            "content": result,
        }

    @staticmethod
    def _require_pending_call(
        state: LangGraphExecutionState,
        expected_name: str,
    ) -> LangGraphToolCall:
        call = state.get("pending_call")
        if not isinstance(call, dict):
            raise ValueError(f"{expected_name} node has no pending call")
        if call.get("name") != expected_name:
            raise ValueError(
                f"{expected_name} node received pending call {call.get('name')!r}"
            )
        return call

    @staticmethod
    def _thread_config(run_id: str) -> dict[str, dict[str, str]]:
        return {"configurable": {"thread_id": run_id}}

    @staticmethod
    def _elapsed_ms(started: float) -> str:
        return f"{(perf_counter() - started) * 1000:.3f}"

    @staticmethod
    def _validate_recommendation(
        workload: RuntimeWorkloadInput,
        recommendation: RuntimeRecommendation,
    ) -> None:
        expected = tuple(item.revision_id for item in workload.context_pack.revisions)
        if recommendation.referenced_revision_ids != expected:
            raise ValueError(
                "structured recommendation does not reference the exact methodological revisions"
            )

    @staticmethod
    def _validate_resume_token(
        workload: RuntimeWorkloadInput,
        token: RuntimeResumeToken,
    ) -> None:
        observed = (
            token.run_id,
            token.project_snapshot_id,
            token.context_pack_id,
            token.context_pack_digest,
        )
        expected = (
            workload.run_id,
            workload.project.snapshot_id,
            workload.context_pack.pack_id,
            workload.context_pack.semantic_digest(),
        )
        if observed != expected:
            raise ValueError(
                "authoritative project/context identity changed after LangGraph interruption"
            )


async def load_local_mcp_tool() -> tuple[Any, Any]:
    """Return the released LangChain MCP client and reference tool for the candidate gate.

    The caller retains the client for the lifetime of the test. The default
    MultiServerMCPClient stdio behavior creates a session for each tool call,
    which is sufficient for this side-effect-free single-call reference server.
    """

    from langchain_mcp_adapters.client import MultiServerMCPClient
    import sys

    client = MultiServerMCPClient(
        {
            "methodology": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [
                    "-m",
                    "experiments.runtime_bakeoff.candidates.langgraph.local_mcp_server",
                ],
            }
        }
    )
    tools = await client.get_tools()
    tool = next(
        item for item in tools if item.name == "lookup_methodological_reference"
    )
    return client, tool
