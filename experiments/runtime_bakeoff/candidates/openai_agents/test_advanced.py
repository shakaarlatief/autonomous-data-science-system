from __future__ import annotations

import asyncio
import json
from typing import Any

from experiments.runtime_bakeoff.candidates.openai_agents.adapter import OpenAIAgentsCandidate
from experiments.runtime_bakeoff.candidates.openai_agents.advanced import (
    OpenAIAgentsExtendedEvaluator,
)
from experiments.runtime_bakeoff.candidates.openai_agents.release_model import (
    ReleaseScriptedModel,
    assistant_message,
    function_call,
)
from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE, representative_workload
from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    InMemoryReferenceGateway,
    ProposalLedger,
    RuntimeStatus,
)


def _recommendation_message(workload, *, approved: bool = False):
    payload = {
        "response": {
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
                    else "The next investigation remains a recommendation only."
                ),
            ],
            "referenced_revision_ids": [
                item.revision_id for item in workload.context_pack.revisions
            ],
        }
    }
    return assistant_message(json.dumps(payload, sort_keys=True))


class DelayedReleaseScriptedModel(ReleaseScriptedModel):
    """Deterministic model that exposes a cancellation point before its first response."""

    def __init__(self, steps, *, delay_seconds: float = 5.0) -> None:
        super().__init__(steps)
        self.delay_seconds = delay_seconds
        self.started: asyncio.Event | None = None

    async def get_response(self, *args: Any, **kwargs: Any):
        if self.started is None:
            self.started = asyncio.Event()
        self.started.set()
        await asyncio.sleep(self.delay_seconds)
        return await super().get_response(*args, **kwargs)


def test_openai_agents_native_stdio_mcp_gate() -> None:
    workload = representative_workload(run_id="openai-mcp")
    ledger = ProposalLedger()
    core = OpenAIAgentsCandidate(InMemoryReferenceGateway(REFERENCE_FIXTURE), ledger)
    evaluator = OpenAIAgentsExtendedEvaluator(core)
    model = ReleaseScriptedModel(
        [
            [
                function_call(
                    "inspect_project_fact",
                    {"key": "prediction_moment"},
                    call_id="mcp_fact",
                ),
                function_call(
                    "lookup_methodological_reference",
                    {"query": "missingness validation leakage"},
                    call_id="mcp_reference",
                ),
            ],
            [_recommendation_message(workload)],
        ]
    )

    outcome = asyncio.run(evaluator.run_with_local_mcp(workload, model))

    assert outcome.status is RuntimeStatus.COMPLETED, outcome.error
    assert outcome.recommendation is not None
    assert ledger.created_count == 0
    model.assert_complete()
    assert model.first_call is not None
    assert "lookup_methodological_reference" in model.first_call["tool_names"]
    assert any(
        event.kind == "tool" and event.name == "lookup_methodological_reference"
        for event in outcome.trace.events
    )
    assert any(
        event.kind == "runtime_metric" and event.name == "latency_ms"
        for event in outcome.trace.events
    )


def test_openai_agents_application_cancellation_is_observable() -> None:
    async def scenario():
        workload = representative_workload(run_id="openai-cancel")
        core = OpenAIAgentsCandidate(
            InMemoryReferenceGateway(REFERENCE_FIXTURE),
            ProposalLedger(),
        )
        evaluator = OpenAIAgentsExtendedEvaluator(core)
        model = DelayedReleaseScriptedModel([[_recommendation_message(workload)]])

        task = asyncio.create_task(evaluator.run_observed(workload, model))
        while model.started is None:
            await asyncio.sleep(0)
        await model.started.wait()
        assert evaluator.cancel(workload.run_id) is True
        return await task

    outcome = asyncio.run(scenario())

    assert outcome.status is RuntimeStatus.CANCELLED
    assert any(
        event.kind == "runtime"
        and event.name == "cancel"
        and event.detail == "application-requested"
        for event in outcome.trace.events
    )


def test_openai_agents_function_tool_timeout_is_bounded_and_observable() -> None:
    workload = representative_workload(run_id="openai-timeout")
    core = OpenAIAgentsCandidate(
        InMemoryReferenceGateway(REFERENCE_FIXTURE),
        ProposalLedger(),
    )
    evaluator = OpenAIAgentsExtendedEvaluator(core)
    model = ReleaseScriptedModel(
        [
            [
                function_call(
                    "bounded_delay",
                    {"seconds": 0.2},
                    call_id="timeout_call",
                )
            ]
        ]
    )

    outcome = asyncio.run(
        evaluator.run_timeout_probe(
            workload,
            model,
            timeout_seconds=0.02,
            delay_seconds=0.2,
        )
    )

    assert outcome.status is RuntimeStatus.FAILED
    assert outcome.error is not None
    assert any(event.kind == "timeout" for event in outcome.trace.events)
    assert any(
        event.kind == "error" and event.name == "ToolTimeoutError"
        for event in outcome.trace.events
    )


def test_openai_agents_controlled_read_failure_can_retry_without_side_effect_replay() -> None:
    workload = representative_workload(run_id="openai-retry")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE, fail_first=True)
    ledger = ProposalLedger()
    core = OpenAIAgentsCandidate(gateway, ledger)
    evaluator = OpenAIAgentsExtendedEvaluator(core)
    initial_model = ReleaseScriptedModel(
        [
            [
                function_call(
                    "lookup_methodological_reference",
                    {"query": "missingness validation leakage"},
                    call_id="retry_reference_1",
                )
            ],
            [
                function_call(
                    "lookup_methodological_reference",
                    {"query": "missingness validation leakage"},
                    call_id="retry_reference_2",
                )
            ],
            [
                function_call(
                    "create_investigation_proposal",
                    {"title": "Investigate production-time missingness before validation design"},
                    call_id="retry_proposal",
                )
            ],
        ]
    )

    interrupted = asyncio.run(evaluator.run_observed(workload, initial_model))

    assert interrupted.status is RuntimeStatus.INTERRUPTED, interrupted.error
    assert interrupted.resume_token is not None
    assert gateway.calls == 2
    assert ledger.created_count == 0
    assert any(
        event.kind == "retry"
        and event.name == "lookup_methodological_reference"
        and event.detail == "attempt=2"
        for event in interrupted.trace.events
    )
    assert any(
        event.kind == "error" and event.name == "lookup_methodological_reference"
        for event in interrupted.trace.events
    )

    serialized = interrupted.resume_token.to_json()
    for _ in range(2):
        resumed_model = ReleaseScriptedModel(
            [[_recommendation_message(workload, approved=True)]]
        )
        outcome = asyncio.run(
            OpenAIAgentsCandidate(gateway, ledger).resume(
                workload,
                serialized,
                ApprovalDecision.APPROVE,
                resumed_model,
            )
        )
        assert outcome.status is RuntimeStatus.COMPLETED
        resumed_model.assert_complete()

    assert ledger.created_count == 1
    assert ledger.execution_attempts == 2


def test_openai_agents_normalized_trace_contains_required_stable_evidence() -> None:
    workload = representative_workload(run_id="openai-observability")
    core = OpenAIAgentsCandidate(
        InMemoryReferenceGateway(REFERENCE_FIXTURE),
        ProposalLedger(),
    )
    evaluator = OpenAIAgentsExtendedEvaluator(core)
    model = ReleaseScriptedModel(
        [
            [
                function_call(
                    "inspect_project_fact",
                    {"key": "prediction_moment"},
                    call_id="observe_fact",
                )
            ],
            [_recommendation_message(workload)],
        ]
    )

    outcome = asyncio.run(evaluator.run_observed(workload, model))

    assert outcome.status is RuntimeStatus.COMPLETED, outcome.error
    trace = outcome.trace
    assert trace.run_id == workload.run_id
    assert trace.project_snapshot_id == workload.project.snapshot_id
    assert trace.context_pack_id == workload.context_pack.pack_id
    assert trace.context_pack_digest == workload.context_pack.semantic_digest()
    assert trace.knowledge_revision_ids == tuple(
        item.revision_id for item in workload.context_pack.revisions
    )
    assert any(
        event.kind == "runtime_metric" and event.name == "model_identity"
        for event in trace.events
    )
    assert any(
        event.kind == "runtime_metric" and event.name == "model_usage"
        for event in trace.events
    )
    assert any(
        event.kind == "runtime_metric" and event.name == "latency_ms"
        for event in trace.events
    )
    tool_events = [
        event for event in trace.events
        if event.kind == "tool" and event.name == "inspect_project_fact"
    ]
    assert len(tool_events) >= 2
    assert any('"phase": "start"' in event.detail for event in tool_events)
    assert any('"phase": "end"' in event.detail for event in tool_events)
