"""OpenAI Agents SDK adapter for the Specification 005 runtime bakeoff.

This module is intentionally experiment-local. Framework-specific Agent and
RunState types stay inside this adapter. The surrounding harness continues to
own project/context identity, methodological revision provenance, approval
semantics, authoritative side-effect idempotency, normalized trace data, and
the structured RuntimeRecommendation returned to ADS.
"""

from __future__ import annotations

from dataclasses import asdict
from importlib.metadata import version
import json
from pathlib import Path
from typing import Any

from agents import Agent, RunConfig, Runner, RunState
from agents.decorators import tool

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


OPENAI_AGENTS_PACKAGE = "openai-agents"
OPENAI_AGENTS_EXPECTED_VERSION = "0.19.4"


class OpenAIAgentsCandidate:
    """Thin translation layer between the ADS harness and OpenAI Agents SDK."""

    def __init__(
        self,
        reference_gateway: MethodologicalReferenceGateway,
        proposal_ledger: ProposalLedger,
    ) -> None:
        self._reference_gateway = reference_gateway
        self._proposal_ledger = proposal_ledger

    @property
    def sdk_version(self) -> str:
        return version(OPENAI_AGENTS_PACKAGE)

    async def run(self, workload: RuntimeWorkloadInput, model: Any) -> RuntimeOutcome:
        trace = self._new_trace(workload)
        trace.record(
            "runtime",
            "start",
            f"openai-agents-sdk/{self.sdk_version}",
        )
        agent = self._build_agent(workload, model)
        result = await Runner.run(
            agent,
            self._model_input(workload),
            context=self._local_context(workload),
            run_config=RunConfig(tracing_disabled=True),
        )
        self._record_model_usage(trace, model)
        return self._normalize_result(workload, result, trace)

    async def resume(
        self,
        workload: RuntimeWorkloadInput,
        serialized_token: str,
        decision: ApprovalDecision,
        model: Any,
    ) -> RuntimeOutcome:
        token = RuntimeResumeToken.from_json(serialized_token)
        self._validate_resume_token(workload, token)
        state_json = token.execution_state.get("openai_agents_run_state")
        if not isinstance(state_json, dict):
            raise ValueError("resume token is missing OpenAI Agents RunState JSON")

        recorded_version = token.execution_state.get("openai_agents_version")
        if recorded_version != self.sdk_version:
            raise ValueError(
                "serialized OpenAI Agents state version does not match the active SDK"
            )

        trace = self._restore_trace(workload, token)
        trace.record("runtime", "resume", decision.value)

        agent = self._build_agent(workload, model)
        state = await RunState.from_json(
            initial_agent=agent,
            state_json=state_json,
            strict_context=True,
        )
        interruptions = state.get_interruptions()
        if len(interruptions) != 1:
            return RuntimeOutcome(
                RuntimeStatus.FAILED,
                trace,
                error=(
                    "expected exactly one pending approval after RunState restore; "
                    f"observed {len(interruptions)}"
                ),
            )

        pending = interruptions[0]
        if decision is ApprovalDecision.APPROVE:
            state.approve(pending, always_approve=False)
            trace.record("approval", pending.name or "unknown_tool", "approved")
        else:
            state.reject(
                pending,
                always_reject=False,
                rejection_message=(
                    "The human rejected authoritative project-state creation. "
                    "Continue with a recommendation without creating it."
                ),
            )
            trace.record("approval", pending.name or "unknown_tool", "rejected")

        result = await Runner.run(
            agent,
            state,
            run_config=RunConfig(tracing_disabled=True),
        )
        self._record_model_usage(trace, model)
        return self._normalize_result(workload, result, trace)

    def _build_agent(self, workload: RuntimeWorkloadInput, model: Any) -> Agent[Any]:
        gateway = self._reference_gateway
        ledger = self._proposal_ledger
        idempotency_key = f"proposal:{workload.run_id}:production-missingness"

        @tool
        def inspect_project_fact(key: str) -> str:
            """Read one explicitly requested fact from the current ADS project snapshot."""

            if key not in workload.project.facts:
                raise ValueError(f"unknown project fact: {key!r}")
            return workload.project.facts[key]

        @tool
        def lookup_methodological_reference(query: str) -> str:
            """Look up one side-effect-free methodological reference."""

            return gateway.lookup(query)

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
            name="ADS principal reasoner",
            instructions=(
                "Reason only over the bounded ADS context supplied in the input and "
                "the explicit tools. Do not infer hidden project history. Read project "
                "facts only through inspect_project_fact. Use the methodological reference "
                "tool when useful. Creating an Investigation proposal is an authoritative "
                "project action and must remain approval-gated. Return the final answer as "
                "the required RuntimeRecommendation structured output."
            ),
            model=model,
            tools=[
                inspect_project_fact,
                lookup_methodological_reference,
                create_investigation_proposal,
            ],
            output_type=RuntimeRecommendation,
        )

    @staticmethod
    def _model_input(workload: RuntimeWorkloadInput) -> str:
        payload = {
            "user_intent": workload.user_intent,
            "project": {
                "project_id": workload.project.project_id,
                "snapshot_id": workload.project.snapshot_id,
                "available_fact_keys": sorted(workload.project.facts),
            },
            "methodological_context": {
                "pack_id": workload.context_pack.pack_id,
                "digest": workload.context_pack.semantic_digest(),
                "revisions": [
                    asdict(item) for item in workload.context_pack.revisions
                ],
                "retrieval_rationale": list(workload.context_pack.rationale),
                "hard_constraints": list(workload.context_pack.hard_constraints),
            },
        }
        return json.dumps(payload, sort_keys=True, ensure_ascii=False)

    @staticmethod
    def _local_context(workload: RuntimeWorkloadInput) -> dict[str, str]:
        return {
            "run_id": workload.run_id,
            "project_id": workload.project.project_id,
            "project_snapshot_id": workload.project.snapshot_id,
            "context_pack_id": workload.context_pack.pack_id,
            "context_pack_digest": workload.context_pack.semantic_digest(),
        }

    def _normalize_result(
        self,
        workload: RuntimeWorkloadInput,
        result: Any,
        trace: RuntimeTrace,
    ) -> RuntimeOutcome:
        interruptions = list(result.interruptions)
        if interruptions:
            if len(interruptions) != 1:
                return RuntimeOutcome(
                    RuntimeStatus.FAILED,
                    trace,
                    error=(
                        "expected exactly one approval interruption for the representative "
                        f"workload; observed {len(interruptions)}"
                    ),
                )
            interruption = interruptions[0]
            normalized_interrupt = self._normalize_interrupt(workload, interruption)
            trace.record(
                "interrupt",
                normalized_interrupt.tool_name,
                normalized_interrupt.interrupt_id,
            )
            state = result.to_state()
            state_json = state.to_json(strict_context=True)
            token = RuntimeResumeToken(
                run_id=workload.run_id,
                next_step=1,
                interrupt=normalized_interrupt,
                context_pack_id=workload.context_pack.pack_id,
                context_pack_digest=workload.context_pack.semantic_digest(),
                project_snapshot_id=workload.project.snapshot_id,
                proposal_idempotency_key=(
                    f"proposal:{workload.run_id}:production-missingness"
                ),
                execution_state={
                    "openai_agents_version": self.sdk_version,
                    "openai_agents_run_state": state_json,
                    "ads_trace_events": [asdict(event) for event in trace.events],
                },
            )
            return RuntimeOutcome(
                RuntimeStatus.INTERRUPTED,
                trace,
                interruption=normalized_interrupt,
                resume_token=token,
            )

        recommendation = result.final_output
        if not isinstance(recommendation, RuntimeRecommendation):
            return RuntimeOutcome(
                RuntimeStatus.FAILED,
                trace,
                error=(
                    "OpenAI Agents candidate did not return ADS RuntimeRecommendation; "
                    f"observed {type(recommendation).__name__}"
                ),
            )
        try:
            self._validate_recommendation(workload, recommendation)
        except ValueError as exc:
            trace.record("validation", "structured_output", "rejected")
            return RuntimeOutcome(RuntimeStatus.FAILED, trace, error=str(exc))
        trace.record("validation", "structured_output", "accepted")
        return RuntimeOutcome(
            RuntimeStatus.COMPLETED,
            trace,
            recommendation=recommendation,
        )

    @staticmethod
    def _normalize_interrupt(
        workload: RuntimeWorkloadInput,
        interruption: Any,
    ) -> RuntimeInterrupt:
        name = interruption.name or "unknown_tool"
        raw_arguments = interruption.arguments
        arguments: dict[str, str]
        if isinstance(raw_arguments, str):
            parsed = json.loads(raw_arguments)
            if not isinstance(parsed, dict):
                raise ValueError("approval interruption arguments are not a JSON object")
            arguments = {str(key): str(value) for key, value in parsed.items()}
        elif isinstance(raw_arguments, dict):
            arguments = {
                str(key): str(value) for key, value in raw_arguments.items()
            }
        else:
            arguments = {}
        call_id = getattr(interruption, "call_id", None)
        return RuntimeInterrupt(
            interrupt_id=(
                str(call_id)
                if call_id
                else f"approval:{workload.run_id}:{name}"
            ),
            kind="TOOL_APPROVAL",
            tool_name=name,
            arguments=arguments,
            reason="OpenAI Agents SDK paused the approval-gated function tool before execution.",
        )

    @staticmethod
    def _record_model_usage(trace: RuntimeTrace, model: Any) -> None:
        calls = getattr(model, "calls", None)
        if calls is not None:
            trace.record("runtime_metric", "scripted_model_calls", str(len(calls)))

    @staticmethod
    def _new_trace(workload: RuntimeWorkloadInput) -> RuntimeTrace:
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
    def _restore_trace(
        workload: RuntimeWorkloadInput,
        token: RuntimeResumeToken,
    ) -> RuntimeTrace:
        trace = OpenAIAgentsCandidate._new_trace(workload)
        raw_events = token.execution_state.get("ads_trace_events", [])
        if not isinstance(raw_events, list):
            raise ValueError("resume token has invalid ADS trace event state")
        trace.events = [
            RuntimeTraceEvent(
                sequence=int(item["sequence"]),
                kind=str(item["kind"]),
                name=str(item["name"]),
                detail=str(item["detail"]),
            )
            for item in raw_events
        ]
        return trace

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
        supplied = {item.revision_id for item in workload.context_pack.revisions}
        referenced = set(recommendation.referenced_revision_ids)
        unknown = referenced - supplied
        if unknown:
            raise ValueError(
                "structured recommendation references knowledge revisions outside "
                f"the supplied context pack: {sorted(unknown)}"
            )
        if not recommendation.next_investigation.strip():
            raise ValueError("structured recommendation has no next investigation")
        if not recommendation.validation_implication.strip():
            raise ValueError("structured recommendation has no validation implication")


def candidate_import_boundary_violations(repository_root: Path) -> list[str]:
    """Return production ADS modules that import the candidate framework directly."""

    violations: list[str] = []
    source_root = repository_root / "src" / "ads_system"
    for path in source_root.rglob("*.py"):
        text = path.read_text(encoding="utf-8")
        if "import agents" in text or "from agents" in text:
            violations.append(str(path.relative_to(repository_root)))
    return violations
