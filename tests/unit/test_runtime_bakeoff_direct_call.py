import json

from experiments.runtime_bakeoff.direct_call import (
    DirectModelCallRuntime,
    DirectModelResponse,
    DirectToolCall,
    ScriptedDirectModel,
    TransientModelError,
)
from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE, representative_workload
from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    InMemoryReferenceGateway,
    ProposalLedger,
    RuntimeRecommendation,
    RuntimeStatus,
)


def _readonly_calls() -> DirectModelResponse:
    return DirectModelResponse(
        tool_calls=(
            DirectToolCall(
                call_id="call-prediction",
                name="inspect_project_fact",
                arguments={"key": "prediction_moment"},
            ),
            DirectToolCall(
                call_id="call-missingness",
                name="inspect_project_fact",
                arguments={"key": "production_missingness"},
            ),
            DirectToolCall(
                call_id="call-reference",
                name="lookup_methodological_reference",
                arguments={"query": "missingness validation leakage"},
            ),
        )
    )


def _proposal_call() -> DirectModelResponse:
    return DirectModelResponse(
        tool_calls=(
            DirectToolCall(
                call_id="call-proposal",
                name="create_investigation_proposal",
                arguments={
                    "title": "Investigate production-time missingness before validation design"
                },
            ),
        )
    )


def _recommendation(workload, *, approved: bool = True) -> RuntimeRecommendation:
    approval_reason = (
        "The approved investigation proposal is now recorded."
        if approved
        else "The investigation remains recommended even though project-state creation was rejected."
    )
    return RuntimeRecommendation(
        next_investigation=(
            "Characterize production-time missingness and feature availability "
            "before finalizing validation."
        ),
        validation_implication=(
            "Reassess chronological validation and feature construction against "
            "the confirmed prediction moment."
        ),
        reasons=(
            "Production-time missingness changes what information is legitimately available.",
            approval_reason,
        ),
        referenced_revision_ids=tuple(
            item.revision_id for item in workload.context_pack.revisions
        ),
    )


def _runtime(
    steps,
    *,
    gateway=None,
    ledger=None,
    model_timeout_seconds: float = 17.0,
):
    workload = representative_workload()
    model = ScriptedDirectModel(list(steps))
    gateway = gateway or InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ledger or ProposalLedger()
    runtime = DirectModelCallRuntime(
        model,
        gateway,
        ledger,
        model_timeout_seconds=model_timeout_seconds,
    )
    return workload, runtime, model, gateway, ledger


def test_direct_model_control_interrupts_before_authoritative_side_effect() -> None:
    workload, runtime, model, gateway, ledger = _runtime(
        [_readonly_calls(), _proposal_call()]
    )

    outcome = runtime.run(workload)

    assert outcome.status is RuntimeStatus.INTERRUPTED
    assert outcome.resume_token is not None
    assert outcome.interruption is not None
    assert outcome.interruption.tool_name == "create_investigation_proposal"
    assert ledger.created_count == 0
    assert gateway.calls == 1
    assert len(model.calls) == 2

    first_request = model.calls[0]
    payload = json.dumps(first_request.messages, sort_keys=True)
    assert workload.context_pack.semantic_digest() in payload
    for revision in workload.context_pack.revisions:
        assert revision.revision_id in payload
    assert first_request.available_tools == DirectModelCallRuntime.AVAILABLE_TOOLS
    assert first_request.timeout_seconds == 17.0


def test_direct_model_resume_survives_process_boundary_without_replaying_reads() -> None:
    workload, first_runtime, _, gateway, ledger = _runtime(
        [_readonly_calls(), _proposal_call()]
    )
    interrupted = first_runtime.run(workload)
    assert interrupted.resume_token is not None
    serialized = interrupted.resume_token.to_json()
    assert gateway.calls == 1

    resumed_model = ScriptedDirectModel(
        [DirectModelResponse(recommendation=_recommendation(workload))]
    )
    resumed_runtime = DirectModelCallRuntime(resumed_model, gateway, ledger)

    outcome = resumed_runtime.resume(
        workload,
        serialized,
        ApprovalDecision.APPROVE,
    )

    assert outcome.status is RuntimeStatus.COMPLETED
    assert outcome.recommendation is not None
    assert ledger.created_count == 1
    assert gateway.calls == 1
    assert len(resumed_model.calls) == 1
    assert any(
        event.kind == "approval" and event.detail == "executed"
        for event in outcome.trace.events
    )
    assert len(outcome.trace.events) > len(interrupted.trace.events)


def test_repeated_resume_keeps_proposal_side_effect_at_most_once() -> None:
    workload, first_runtime, _, gateway, ledger = _runtime(
        [_readonly_calls(), _proposal_call()]
    )
    interrupted = first_runtime.run(workload)
    assert interrupted.resume_token is not None
    serialized = interrupted.resume_token.to_json()

    for _ in range(2):
        model = ScriptedDirectModel(
            [DirectModelResponse(recommendation=_recommendation(workload))]
        )
        runtime = DirectModelCallRuntime(model, gateway, ledger)
        outcome = runtime.resume(
            workload,
            serialized,
            ApprovalDecision.APPROVE,
        )
        assert outcome.status is RuntimeStatus.COMPLETED

    assert ledger.created_count == 1
    assert ledger.execution_attempts == 2
    assert gateway.calls == 1


def test_rejected_approval_returns_to_model_without_creating_project_state() -> None:
    workload, first_runtime, _, gateway, ledger = _runtime(
        [_readonly_calls(), _proposal_call()]
    )
    interrupted = first_runtime.run(workload)
    assert interrupted.resume_token is not None

    model = ScriptedDirectModel(
        [DirectModelResponse(recommendation=_recommendation(workload, approved=False))]
    )
    runtime = DirectModelCallRuntime(model, gateway, ledger)
    outcome = runtime.resume(
        workload,
        interrupted.resume_token.to_json(),
        ApprovalDecision.REJECT,
    )

    assert outcome.status is RuntimeStatus.COMPLETED
    assert ledger.created_count == 0
    assert any(
        event.kind == "approval" and event.detail == "rejected"
        for event in outcome.trace.events
    )


def test_direct_model_call_retries_transient_model_failure() -> None:
    workload, runtime, model, _, ledger = _runtime(
        [
            TransientModelError("synthetic transient model failure"),
            _readonly_calls(),
            _proposal_call(),
        ]
    )

    outcome = runtime.run(workload)

    assert outcome.status is RuntimeStatus.INTERRUPTED
    assert ledger.created_count == 0
    assert len(model.calls) == 3
    assert any(
        event.kind == "retry" and event.name == "model_call"
        for event in outcome.trace.events
    )


def test_direct_model_control_cancels_before_approved_side_effect() -> None:
    workload, first_runtime, _, gateway, ledger = _runtime(
        [_readonly_calls(), _proposal_call()]
    )
    interrupted = first_runtime.run(workload)
    assert interrupted.resume_token is not None

    model = ScriptedDirectModel(
        [DirectModelResponse(recommendation=_recommendation(workload))]
    )
    runtime = DirectModelCallRuntime(model, gateway, ledger)
    runtime.cancel(workload.run_id)

    outcome = runtime.resume(
        workload,
        interrupted.resume_token.to_json(),
        ApprovalDecision.APPROVE,
    )

    assert outcome.status is RuntimeStatus.CANCELLED
    assert ledger.created_count == 0
    assert len(model.calls) == 0


def test_direct_model_control_rejects_unknown_knowledge_revision_in_output() -> None:
    workload = representative_workload()
    invalid = RuntimeRecommendation(
        next_investigation="Investigate missingness.",
        validation_implication="Reassess validation.",
        reasons=("Synthetic invalid provenance case.",),
        referenced_revision_ids=("kr-not-in-context",),
    )
    model = ScriptedDirectModel([DirectModelResponse(recommendation=invalid)])
    runtime = DirectModelCallRuntime(
        model,
        InMemoryReferenceGateway(REFERENCE_FIXTURE),
        ProposalLedger(),
    )

    outcome = runtime.run(workload)

    assert outcome.status is RuntimeStatus.FAILED
    assert outcome.error is not None
    assert "outside the supplied context pack" in outcome.error


def test_direct_model_resume_token_contains_only_ads_owned_serializable_state() -> None:
    workload, runtime, _, _, _ = _runtime([_readonly_calls(), _proposal_call()])

    outcome = runtime.run(workload)

    assert outcome.resume_token is not None
    serialized = outcome.resume_token.to_json()
    restored = json.loads(serialized)

    assert restored["execution_state"]["messages"]
    assert restored["execution_state"]["pending_call"]["name"] == (
        "create_investigation_proposal"
    )
    assert restored["execution_state"]["trace_events"]
    for forbidden in ("Agent", "Thread", "Graph", "RunState"):
        assert forbidden not in serialized
