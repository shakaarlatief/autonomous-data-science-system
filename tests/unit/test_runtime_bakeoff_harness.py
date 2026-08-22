from dataclasses import replace

import pytest

from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE, representative_workload
from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    DirectControlRuntime,
    InMemoryReferenceGateway,
    MethodologicalContextPack,
    ProposalLedger,
    RuntimeResumeToken,
    RuntimeStatus,
)


def _runtime(*, fail_first_reference: bool = False):
    gateway = InMemoryReferenceGateway(
        REFERENCE_FIXTURE,
        fail_first=fail_first_reference,
    )
    ledger = ProposalLedger()
    runtime = DirectControlRuntime(gateway, ledger)
    return runtime, gateway, ledger


def test_context_pack_digest_is_deterministic_and_content_sensitive() -> None:
    workload = representative_workload()
    first = workload.context_pack.semantic_digest()
    second = workload.context_pack.semantic_digest()
    assert first == second
    assert len(first) == 64

    changed_pack = MethodologicalContextPack(
        pack_id=workload.context_pack.pack_id,
        revisions=workload.context_pack.revisions,
        rationale=workload.context_pack.rationale + ("new rationale",),
        hard_constraints=workload.context_pack.hard_constraints,
    )
    assert changed_pack.semantic_digest() != first


def test_direct_control_interrupt_preserves_exact_context_provenance() -> None:
    workload = representative_workload()
    runtime, _, ledger = _runtime()

    outcome = runtime.run(workload)

    assert outcome.status is RuntimeStatus.INTERRUPTED
    assert outcome.interruption is not None
    assert outcome.resume_token is not None
    assert ledger.created_count == 0
    assert outcome.trace.project_snapshot_id == workload.project.snapshot_id
    assert outcome.trace.context_pack_id == workload.context_pack.pack_id
    assert outcome.trace.context_pack_digest == workload.context_pack.semantic_digest()
    assert outcome.trace.knowledge_revision_ids == tuple(
        revision.revision_id for revision in workload.context_pack.revisions
    )


def test_resume_token_round_trips_without_framework_types() -> None:
    workload = representative_workload()
    runtime, _, _ = _runtime()
    outcome = runtime.run(workload)
    assert outcome.resume_token is not None

    payload = outcome.resume_token.to_json()
    restored = RuntimeResumeToken.from_json(payload)

    assert restored == outcome.resume_token
    assert "Agent" not in payload
    assert "Thread" not in payload
    assert "Graph" not in payload


def test_approval_executes_authoritative_side_effect_at_most_once() -> None:
    workload = representative_workload()
    runtime, _, ledger = _runtime()
    interrupted = runtime.run(workload)
    assert interrupted.resume_token is not None
    token = interrupted.resume_token.to_json()

    first = runtime.resume(workload, token, ApprovalDecision.APPROVE)
    second = runtime.resume(workload, token, ApprovalDecision.APPROVE)

    assert first.status is RuntimeStatus.COMPLETED
    assert second.status is RuntimeStatus.COMPLETED
    assert ledger.created_count == 1
    assert ledger.execution_attempts == 2
    assert first.recommendation is not None
    assert first.recommendation.referenced_revision_ids == tuple(
        revision.revision_id for revision in workload.context_pack.revisions
    )


def test_rejection_does_not_create_project_state() -> None:
    workload = representative_workload()
    runtime, _, ledger = _runtime()
    interrupted = runtime.run(workload)
    assert interrupted.resume_token is not None

    outcome = runtime.resume(
        workload,
        interrupted.resume_token.to_json(),
        ApprovalDecision.REJECT,
    )

    assert outcome.status is RuntimeStatus.COMPLETED
    assert ledger.created_count == 0
    assert outcome.recommendation is not None


def test_transient_reference_failure_is_retried_before_any_side_effect() -> None:
    workload = representative_workload()
    runtime, gateway, ledger = _runtime(fail_first_reference=True)

    outcome = runtime.run(workload)

    assert outcome.status is RuntimeStatus.INTERRUPTED
    assert gateway.calls == 2
    assert ledger.created_count == 0
    retry_events = [event for event in outcome.trace.events if event.kind == "retry"]
    assert len(retry_events) == 1


def test_cancelled_run_cannot_execute_approved_side_effect() -> None:
    workload = representative_workload()
    runtime, _, ledger = _runtime()
    interrupted = runtime.run(workload)
    assert interrupted.resume_token is not None

    runtime.cancel(workload.run_id)
    outcome = runtime.resume(
        workload,
        interrupted.resume_token.to_json(),
        ApprovalDecision.APPROVE,
    )

    assert outcome.status is RuntimeStatus.CANCELLED
    assert ledger.created_count == 0


def test_resume_rejects_changed_authoritative_context() -> None:
    workload = representative_workload()
    runtime, _, _ = _runtime()
    interrupted = runtime.run(workload)
    assert interrupted.resume_token is not None

    changed_project = replace(
        workload.project,
        snapshot_id="project-snapshot-runtime-002",
    )
    changed_workload = replace(workload, project=changed_project)

    with pytest.raises(ValueError, match="authoritative workload context"):
        runtime.resume(
            changed_workload,
            interrupted.resume_token.to_json(),
            ApprovalDecision.APPROVE,
        )
