"""ADS-owned direct model-call control for the Specification 005 bakeoff.

This module deliberately implements only the small amount of orchestration
needed by the representative workload. It is evidence for the complexity that
ADS must own when using direct model calls without an agent runtime.

No provider SDK is required for deterministic tests. A live provider adapter
can implement ``DirectModelClient`` later without changing the ADS-owned
workload, interruption, provenance, or side-effect contracts.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from typing import Protocol

from .harness import (
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


class TransientModelError(RuntimeError):
    """Synthetic/provider-normalized transient model failure."""


@dataclass(frozen=True)
class DirectToolCall:
    call_id: str
    name: str
    arguments: dict[str, str]


@dataclass(frozen=True)
class DirectModelResponse:
    tool_calls: tuple[DirectToolCall, ...] = ()
    recommendation: RuntimeRecommendation | None = None

    def __post_init__(self) -> None:
        if bool(self.tool_calls) == bool(self.recommendation):
            raise ValueError(
                "A direct-model response must contain either tool calls or one recommendation"
            )


@dataclass(frozen=True)
class DirectModelRequest:
    run_id: str
    messages: tuple[dict[str, object], ...]
    available_tools: tuple[str, ...]
    timeout_seconds: float


class DirectModelClient(Protocol):
    provider_id: str
    model_id: str

    def complete(self, request: DirectModelRequest) -> DirectModelResponse:
        """Return one model turn in normalized ADS experiment form."""


class ScriptedDirectModel:
    """Deterministic fake direct-model client used by infrastructure tests."""

    def __init__(
        self,
        steps: list[DirectModelResponse | Exception],
        *,
        provider_id: str = "scripted-provider",
        model_id: str = "scripted-direct-model",
    ) -> None:
        self.provider_id = provider_id
        self.model_id = model_id
        self._steps = list(steps)
        self.calls: list[DirectModelRequest] = []

    def complete(self, request: DirectModelRequest) -> DirectModelResponse:
        self.calls.append(request)
        if not self._steps:
            raise AssertionError("ScriptedDirectModel received an unexpected model call")
        step = self._steps.pop(0)
        if isinstance(step, Exception):
            raise step
        return step


class _ToolFailure(RuntimeError):
    pass


class _ModelFailure(RuntimeError):
    pass


class DirectModelCallRuntime:
    """Small direct-call tool loop used as the no-framework bakeoff control."""

    AVAILABLE_TOOLS = (
        "inspect_project_fact",
        "lookup_methodological_reference",
        "create_investigation_proposal",
    )

    def __init__(
        self,
        model: DirectModelClient,
        reference_gateway: MethodologicalReferenceGateway,
        proposal_ledger: ProposalLedger,
        *,
        max_turns: int = 6,
        max_model_attempts: int = 2,
        max_reference_attempts: int = 2,
        model_timeout_seconds: float = 30.0,
    ) -> None:
        if max_turns < 1:
            raise ValueError("max_turns must be positive")
        if max_model_attempts < 1:
            raise ValueError("max_model_attempts must be positive")
        if max_reference_attempts < 1:
            raise ValueError("max_reference_attempts must be positive")
        if model_timeout_seconds <= 0:
            raise ValueError("model_timeout_seconds must be positive")

        self._model = model
        self._reference_gateway = reference_gateway
        self._proposal_ledger = proposal_ledger
        self._max_turns = max_turns
        self._max_model_attempts = max_model_attempts
        self._max_reference_attempts = max_reference_attempts
        self._model_timeout_seconds = model_timeout_seconds
        self._cancelled_runs: set[str] = set()

    def cancel(self, run_id: str) -> None:
        self._cancelled_runs.add(run_id)

    def run(self, workload: RuntimeWorkloadInput) -> RuntimeOutcome:
        trace = self._new_trace(workload)
        trace.record("runtime", "start", "direct-model-call")
        trace.record(
            "model",
            "identity",
            f"{self._model.provider_id}/{self._model.model_id}",
        )
        messages = self._initial_messages(workload)
        return self._drive(workload, messages, trace)

    def resume(
        self,
        workload: RuntimeWorkloadInput,
        serialized_token: str,
        decision: ApprovalDecision,
    ) -> RuntimeOutcome:
        token = RuntimeResumeToken.from_json(serialized_token)
        self._validate_resume_token(workload, token)
        messages, pending_call, trace = self._restore_execution_state(workload, token)
        trace.record("runtime", "resume", decision.value)

        if self._is_cancelled(workload.run_id, trace):
            return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)

        if pending_call.name != "create_investigation_proposal":
            return RuntimeOutcome(
                RuntimeStatus.FAILED,
                trace,
                error=f"unsupported pending approval tool: {pending_call.name}",
            )

        if decision is ApprovalDecision.REJECT:
            trace.record("approval", pending_call.name, "rejected")
            result = "Project-state creation rejected by the human."
        else:
            created = self._proposal_ledger.create_once(
                token.proposal_idempotency_key,
                {
                    "title": pending_call.arguments["title"],
                    "source_run_id": workload.run_id,
                    "project_snapshot_id": workload.project.snapshot_id,
                    "context_pack_digest": workload.context_pack.semantic_digest(),
                },
            )
            trace.record(
                "approval",
                pending_call.name,
                "executed" if created else "already-executed",
            )
            result = (
                "Investigation proposal recorded exactly once."
                if created
                else "Investigation proposal was already recorded for this idempotency key."
            )

        messages.append(self._tool_result_message(pending_call, result))
        return self._drive(workload, messages, trace)

    def _drive(
        self,
        workload: RuntimeWorkloadInput,
        messages: list[dict[str, object]],
        trace: RuntimeTrace,
    ) -> RuntimeOutcome:
        for turn in range(1, self._max_turns + 1):
            if self._is_cancelled(workload.run_id, trace):
                return RuntimeOutcome(RuntimeStatus.CANCELLED, trace)

            try:
                response = self._complete_with_retry(workload, messages, trace, turn)
            except _ModelFailure as exc:
                return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))

            if response.recommendation is not None:
                try:
                    self._validate_recommendation(workload, response.recommendation)
                except ValueError as exc:
                    trace.record("validation", "structured_output", "rejected")
                    return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
                trace.record("model", "structured_output", "accepted")
                return RuntimeOutcome(
                    RuntimeStatus.COMPLETED,
                    trace,
                    recommendation=response.recommendation,
                )

            for call in response.tool_calls:
                messages.append(self._tool_call_message(call))

                if call.name == "create_investigation_proposal":
                    interrupt = RuntimeInterrupt(
                        interrupt_id=f"approval:{workload.run_id}:{call.call_id}",
                        kind="TOOL_APPROVAL",
                        tool_name=call.name,
                        arguments=dict(call.arguments),
                        reason=(
                            "Creating a project Investigation proposal is an "
                            "authoritative side effect."
                        ),
                    )
                    trace.record("interrupt", call.name, interrupt.interrupt_id)
                    token = RuntimeResumeToken(
                        run_id=workload.run_id,
                        next_step=turn + 1,
                        interrupt=interrupt,
                        context_pack_id=workload.context_pack.pack_id,
                        context_pack_digest=workload.context_pack.semantic_digest(),
                        project_snapshot_id=workload.project.snapshot_id,
                        proposal_idempotency_key=(
                            f"proposal:{workload.run_id}:production-missingness"
                        ),
                        execution_state=self._serialize_execution_state(
                            messages,
                            call,
                            trace,
                        ),
                    )
                    return RuntimeOutcome(
                        RuntimeStatus.INTERRUPTED,
                        trace,
                        interruption=interrupt,
                        resume_token=token,
                    )

                try:
                    result = self._execute_read_only_tool(workload, call, trace)
                except _ToolFailure as exc:
                    return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
                messages.append(self._tool_result_message(call, result))

        trace.record("runtime", "max_turns", str(self._max_turns))
        return RuntimeOutcome(
            RuntimeStatus.FAILED,
            trace,
            error=f"direct model-call runtime exceeded max_turns={self._max_turns}",
        )

    def _complete_with_retry(
        self,
        workload: RuntimeWorkloadInput,
        messages: list[dict[str, object]],
        trace: RuntimeTrace,
        turn: int,
    ) -> DirectModelResponse:
        for attempt in range(1, self._max_model_attempts + 1):
            request = DirectModelRequest(
                run_id=workload.run_id,
                messages=tuple(messages),
                available_tools=self.AVAILABLE_TOOLS,
                timeout_seconds=self._model_timeout_seconds,
            )
            trace.record(
                "model_call",
                self._model.model_id,
                f"turn={turn};attempt={attempt}",
            )
            try:
                return self._model.complete(request)
            except (TransientModelError, TimeoutError) as exc:
                trace.record(
                    "retry",
                    "model_call",
                    f"turn={turn};attempt={attempt};error={type(exc).__name__}",
                )
                if attempt == self._max_model_attempts:
                    raise _ModelFailure(str(exc)) from exc
        raise AssertionError("unreachable")

    def _execute_read_only_tool(
        self,
        workload: RuntimeWorkloadInput,
        call: DirectToolCall,
        trace: RuntimeTrace,
    ) -> str:
        if call.name == "inspect_project_fact":
            key = call.arguments.get("key")
            if key is None or key not in workload.project.facts:
                raise _ToolFailure(f"unknown project fact: {key!r}")
            trace.record("tool", call.name, key)
            return workload.project.facts[key]

        if call.name == "lookup_methodological_reference":
            query = call.arguments.get("query")
            if not query:
                raise _ToolFailure("lookup_methodological_reference requires query")
            for attempt in range(1, self._max_reference_attempts + 1):
                try:
                    result = self._reference_gateway.lookup(query)
                    trace.record("tool", call.name, query)
                    return result
                except RuntimeError as exc:
                    trace.record(
                        "retry",
                        call.name,
                        f"attempt={attempt};error={type(exc).__name__}",
                    )
                    if attempt == self._max_reference_attempts:
                        raise _ToolFailure(str(exc)) from exc
            raise AssertionError("unreachable")

        raise _ToolFailure(f"unsupported tool call: {call.name}")

    @staticmethod
    def _initial_messages(
        workload: RuntimeWorkloadInput,
    ) -> list[dict[str, object]]:
        context_payload = {
            "project_id": workload.project.project_id,
            "project_snapshot_id": workload.project.snapshot_id,
            "project_facts_available_by_tool": sorted(workload.project.facts),
            "context_pack_id": workload.context_pack.pack_id,
            "context_pack_digest": workload.context_pack.semantic_digest(),
            "knowledge_revisions": [
                asdict(item) for item in workload.context_pack.revisions
            ],
            "retrieval_rationale": list(workload.context_pack.rationale),
            "hard_constraints": list(workload.context_pack.hard_constraints),
        }
        return [
            {
                "role": "system",
                "content": (
                    "You are the principal ADS reasoner. Use only the supplied "
                    "bounded methodological context and available tools. "
                    "Authoritative project-state creation requires approval. "
                    "Return the final answer as RuntimeRecommendation."
                ),
            },
            {
                "role": "user",
                "content": workload.user_intent,
                "ads_context": context_payload,
            },
        ]

    @staticmethod
    def _tool_call_message(call: DirectToolCall) -> dict[str, object]:
        return {
            "role": "assistant",
            "type": "tool_call",
            "call_id": call.call_id,
            "name": call.name,
            "arguments": dict(call.arguments),
        }

    @staticmethod
    def _tool_result_message(
        call: DirectToolCall,
        result: str,
    ) -> dict[str, object]:
        return {
            "role": "tool",
            "type": "tool_result",
            "call_id": call.call_id,
            "name": call.name,
            "content": result,
        }

    @staticmethod
    def _serialize_execution_state(
        messages: list[dict[str, object]],
        pending_call: DirectToolCall,
        trace: RuntimeTrace,
    ) -> dict[str, object]:
        return {
            "messages": json.loads(json.dumps(messages)),
            "pending_call": asdict(pending_call),
            "trace_events": [asdict(event) for event in trace.events],
        }

    def _restore_execution_state(
        self,
        workload: RuntimeWorkloadInput,
        token: RuntimeResumeToken,
    ) -> tuple[list[dict[str, object]], DirectToolCall, RuntimeTrace]:
        state = token.execution_state
        messages_raw = state.get("messages")
        pending_raw = state.get("pending_call")
        events_raw = state.get("trace_events")
        if not isinstance(messages_raw, list):
            raise ValueError("resume token is missing direct-call messages")
        if not isinstance(pending_raw, dict):
            raise ValueError("resume token is missing pending direct-call tool")
        if not isinstance(events_raw, list):
            raise ValueError("resume token is missing normalized trace history")

        messages = json.loads(json.dumps(messages_raw))
        pending_call = DirectToolCall(
            call_id=str(pending_raw["call_id"]),
            name=str(pending_raw["name"]),
            arguments={
                str(key): str(value)
                for key, value in dict(pending_raw["arguments"]).items()
            },
        )
        trace = self._new_trace(workload)
        trace.events = [
            RuntimeTraceEvent(
                sequence=int(item["sequence"]),
                kind=str(item["kind"]),
                name=str(item["name"]),
                detail=str(item["detail"]),
            )
            for item in events_raw
        ]
        return messages, pending_call, trace

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

    def _is_cancelled(self, run_id: str, trace: RuntimeTrace) -> bool:
        if run_id not in self._cancelled_runs:
            return False
        trace.record("runtime", "cancel", "requested")
        return True

    @staticmethod
    def _validate_resume_token(
        workload: RuntimeWorkloadInput,
        token: RuntimeResumeToken,
    ) -> None:
        expected = (
            workload.run_id,
            workload.project.snapshot_id,
            workload.context_pack.pack_id,
            workload.context_pack.semantic_digest(),
        )
        observed = (
            token.run_id,
            token.project_snapshot_id,
            token.context_pack_id,
            token.context_pack_digest,
        )
        if observed != expected:
            raise ValueError(
                "resume token does not match authoritative workload context"
            )

    @staticmethod
    def _validate_recommendation(
        workload: RuntimeWorkloadInput,
        recommendation: RuntimeRecommendation,
    ) -> None:
        supplied = {
            item.revision_id for item in workload.context_pack.revisions
        }
        referenced = set(recommendation.referenced_revision_ids)
        unknown = referenced - supplied
        if unknown:
            raise ValueError(
                "structured recommendation references knowledge revisions "
                f"outside the supplied context pack: {sorted(unknown)}"
            )
        if not recommendation.next_investigation.strip():
            raise ValueError("structured recommendation has no next investigation")
        if not recommendation.validation_implication.strip():
            raise ValueError("structured recommendation has no validation implication")
