from __future__ import annotations

import asyncio
from dataclasses import replace
from pathlib import Path

from experiments.runtime_bakeoff.candidates.langgraph.adapter import (
    ApprovalReplayProbe,
    DelayedLangGraphReasoner,
    DeterministicLangGraphReasoner,
    LangGraphCandidate,
    load_local_mcp_tool,
)
from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE, representative_workload
from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    InMemoryReferenceGateway,
    MethodologicalContextPack,
    ProposalLedger,
    RuntimeStatus,
)


def _checkpoint(tmp_path: Path, name: str) -> Path:
    return tmp_path / f"{name}.sqlite"


def test_langgraph_domain_boundary_and_single_reasoner_tool_loop(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-core")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ProposalLedger()
    probe = ApprovalReplayProbe()
    candidate = LangGraphCandidate(
        _checkpoint(tmp_path, "core"),
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
        replay_probe=probe,
    )

    outcome = asyncio.run(candidate.run(workload))

    assert outcome.status is RuntimeStatus.INTERRUPTED, outcome.error
    assert outcome.interruption is not None
    assert outcome.interruption.tool_name == "create_investigation_proposal"
    assert outcome.resume_token is not None
    assert gateway.calls == 1
    assert ledger.created_count == 0
    assert probe.entries == 1
    assert any(
        event.kind == "model" and event.name == "identity"
        for event in outcome.trace.events
    )
    assert any(
        event.kind == "tool" and event.name == "inspect_project_fact"
        for event in outcome.trace.events
    )
    assert any(
        event.kind == "tool" and event.name == "lookup_methodological_reference"
        for event in outcome.trace.events
    )
    assert any(event.kind == "checkpoint" for event in outcome.trace.events)


def test_langgraph_sqlite_resume_restarts_interrupt_node_without_replaying_completed_reads(
    tmp_path: Path,
) -> None:
    workload = representative_workload(run_id="langgraph-resume")
    checkpoint_path = _checkpoint(tmp_path, "resume")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ProposalLedger()
    probe = ApprovalReplayProbe()

    first_runtime = LangGraphCandidate(
        checkpoint_path,
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
        replay_probe=probe,
    )
    interrupted = asyncio.run(first_runtime.run(workload))

    assert interrupted.status is RuntimeStatus.INTERRUPTED, interrupted.error
    assert interrupted.resume_token is not None
    serialized = interrupted.resume_token.to_json()
    assert gateway.calls == 1
    assert probe.entries == 1

    resumed_runtime = LangGraphCandidate(
        checkpoint_path,
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
        replay_probe=probe,
    )
    completed = asyncio.run(
        resumed_runtime.resume(workload, serialized, ApprovalDecision.APPROVE)
    )

    assert completed.status is RuntimeStatus.COMPLETED, completed.error
    assert completed.recommendation is not None
    assert gateway.calls == 1
    assert probe.entries == 2
    assert ledger.created_count == 1
    assert ledger.execution_attempts == 1
    assert any(
        event.kind == "replay" and event.name == "approval_node_restart"
        for event in completed.trace.events
    )

    repeated_runtime = LangGraphCandidate(
        checkpoint_path,
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
        replay_probe=probe,
    )
    repeated = asyncio.run(
        repeated_runtime.resume(workload, serialized, ApprovalDecision.APPROVE)
    )

    assert repeated.status is RuntimeStatus.COMPLETED, repeated.error
    assert repeated.recommendation is not None
    assert gateway.calls == 1
    assert probe.entries == 3
    assert ledger.created_count == 1
    assert ledger.execution_attempts == 2


def test_langgraph_rejection_resumes_without_authoritative_side_effect(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-reject")
    checkpoint_path = _checkpoint(tmp_path, "reject")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ProposalLedger()
    probe = ApprovalReplayProbe()

    interrupted = asyncio.run(
        LangGraphCandidate(
            checkpoint_path,
            DeterministicLangGraphReasoner(),
            gateway,
            ledger,
            replay_probe=probe,
        ).run(workload)
    )
    assert interrupted.resume_token is not None

    outcome = asyncio.run(
        LangGraphCandidate(
            checkpoint_path,
            DeterministicLangGraphReasoner(),
            gateway,
            ledger,
            replay_probe=probe,
        ).resume(
            workload,
            interrupted.resume_token.to_json(),
            ApprovalDecision.REJECT,
        )
    )

    assert outcome.status is RuntimeStatus.COMPLETED, outcome.error
    assert outcome.recommendation is not None
    assert ledger.created_count == 0
    assert ledger.execution_attempts == 0
    assert probe.entries == 2


def test_langgraph_resume_rejects_changed_authoritative_context(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-stale")
    checkpoint_path = _checkpoint(tmp_path, "stale")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ProposalLedger()

    interrupted = asyncio.run(
        LangGraphCandidate(
            checkpoint_path,
            DeterministicLangGraphReasoner(),
            gateway,
            ledger,
        ).run(workload)
    )
    assert interrupted.resume_token is not None

    changed_pack = MethodologicalContextPack(
        pack_id=workload.context_pack.pack_id,
        revisions=workload.context_pack.revisions,
        rationale=workload.context_pack.rationale + ("authoritative context changed",),
        hard_constraints=workload.context_pack.hard_constraints,
    )
    changed_workload = replace(workload, context_pack=changed_pack)

    candidate = LangGraphCandidate(
        checkpoint_path,
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
    )
    try:
        asyncio.run(
            candidate.resume(
                changed_workload,
                interrupted.resume_token.to_json(),
                ApprovalDecision.APPROVE,
            )
        )
    except ValueError as exc:
        assert "authoritative project/context identity changed" in str(exc)
    else:
        raise AssertionError("changed authoritative context should reject resume")


def test_langgraph_retry_policy_retries_transient_read_before_interrupt(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-retry")
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE, fail_first=True)
    ledger = ProposalLedger()
    candidate = LangGraphCandidate(
        _checkpoint(tmp_path, "retry"),
        DeterministicLangGraphReasoner(),
        gateway,
        ledger,
    )

    outcome = asyncio.run(candidate.run(workload))

    assert outcome.status is RuntimeStatus.INTERRUPTED, outcome.error
    assert gateway.calls == 2
    assert ledger.created_count == 0
    assert any(
        event.kind == "retry"
        and event.name == "lookup_methodological_reference"
        and event.detail == "attempt=2"
        for event in outcome.trace.events
    )


def test_langgraph_async_node_timeout_is_bounded_and_observable(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-timeout")
    candidate = LangGraphCandidate(
        _checkpoint(tmp_path, "timeout"),
        DeterministicLangGraphReasoner(),
        InMemoryReferenceGateway(REFERENCE_FIXTURE),
        ProposalLedger(),
    )

    outcome = asyncio.run(
        candidate.timeout_probe(
            workload,
            timeout_seconds=0.02,
            delay_seconds=0.2,
        )
    )

    assert outcome.status is RuntimeStatus.FAILED
    assert outcome.error is not None
    assert any(event.kind == "timeout" for event in outcome.trace.events)
    assert any(event.name == "NodeTimeoutError" for event in outcome.trace.events)


def test_langgraph_application_cancellation_is_observable(tmp_path: Path) -> None:
    async def scenario():
        workload = representative_workload(run_id="langgraph-cancel")
        reasoner = DelayedLangGraphReasoner(delay_seconds=5.0)
        candidate = LangGraphCandidate(
            _checkpoint(tmp_path, "cancel"),
            reasoner,
            InMemoryReferenceGateway(REFERENCE_FIXTURE),
            ProposalLedger(),
        )
        task = asyncio.create_task(candidate.run(workload))
        await reasoner.started.wait()
        assert candidate.cancel(workload.run_id) is True
        return await task

    outcome = asyncio.run(scenario())

    assert outcome.status is RuntimeStatus.CANCELLED
    assert any(
        event.kind == "runtime"
        and event.name == "cancel"
        and event.detail == "application-requested"
        for event in outcome.trace.events
    )


def test_langgraph_real_stdio_mcp_tool_is_used_before_approval(tmp_path: Path) -> None:
    async def scenario():
        workload = representative_workload(run_id="langgraph-mcp")
        client, tool = await load_local_mcp_tool()
        candidate = LangGraphCandidate(
            _checkpoint(tmp_path, "mcp"),
            DeterministicLangGraphReasoner(),
            InMemoryReferenceGateway(REFERENCE_FIXTURE),
            ProposalLedger(),
            mcp_tool=tool,
        )
        outcome = await candidate.run(workload)
        return outcome, client

    outcome, _client = asyncio.run(scenario())

    assert outcome.status is RuntimeStatus.INTERRUPTED, outcome.error
    assert any(
        event.kind == "tool"
        and event.name == "lookup_methodological_reference"
        and '"transport": "mcp"' in event.detail
        for event in outcome.trace.events
    )


def test_langgraph_trace_preserves_stable_ads_provenance(tmp_path: Path) -> None:
    workload = representative_workload(run_id="langgraph-observe")
    candidate = LangGraphCandidate(
        _checkpoint(tmp_path, "observe"),
        DeterministicLangGraphReasoner(),
        InMemoryReferenceGateway(REFERENCE_FIXTURE),
        ProposalLedger(),
    )

    outcome = asyncio.run(candidate.run(workload))

    assert outcome.status is RuntimeStatus.INTERRUPTED, outcome.error
    trace = outcome.trace
    assert trace.run_id == workload.run_id
    assert trace.project_snapshot_id == workload.project.snapshot_id
    assert trace.context_pack_id == workload.context_pack.pack_id
    assert trace.context_pack_digest == workload.context_pack.semantic_digest()
    assert trace.knowledge_revision_ids == tuple(
        item.revision_id for item in workload.context_pack.revisions
    )
    assert any(event.kind == "runtime" and event.name == "start" for event in trace.events)
    assert any(event.kind == "model_call" for event in trace.events)
    assert any(event.kind == "tool" for event in trace.events)
    assert any(event.kind == "interrupt" for event in trace.events)
    assert any(event.kind == "checkpoint" for event in trace.events)
    assert any(
        event.kind == "runtime_metric" and event.name == "latency_ms"
        for event in trace.events
    )
