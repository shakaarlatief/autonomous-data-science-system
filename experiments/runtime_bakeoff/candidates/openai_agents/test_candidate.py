from __future__ import annotations

import asyncio
import json
from pathlib import Path

from agents.testing import ScriptedModel, assistant_message, function_call

from experiments.runtime_bakeoff.candidates.openai_agents.adapter import (
    OPENAI_AGENTS_EXPECTED_VERSION,
    OpenAIAgentsCandidate,
    candidate_import_boundary_violations,
)
from experiments.runtime_bakeoff.fixtures import REFERENCE_FIXTURE, representative_workload
from experiments.runtime_bakeoff.harness import (
    ApprovalDecision,
    InMemoryReferenceGateway,
    ProposalLedger,
    RuntimeRecommendation,
    RuntimeStatus,
)


def _initial_model() -> ScriptedModel:
    return ScriptedModel(
        [
            [
                function_call(
                    "inspect_project_fact",
                    {"key": "prediction_moment"},
                    call_id="call_prediction",
                ),
                function_call(
                    "inspect_project_fact",
                    {"key": "production_missingness"},
                    call_id="call_missingness",
                ),
                function_call(
                    "lookup_methodological_reference",
                    {"query": "missingness validation leakage"},
                    call_id="call_reference",
                ),
            ],
            [
                function_call(
                    "create_investigation_proposal",
                    {
                        "title": (
                            "Investigate production-time missingness before "
                            "validation design"
                        )
                    },
                    call_id="call_proposal",
                )
            ],
        ]
    )


def _recommendation_payload(workload, *, approved: bool) -> dict[str, object]:
    return {
        "next_investigation": (
            "Characterize production-time missingness and feature availability "
            "before finalizing validation."
        ),
        "validation_implication": (
            "Reassess chronological validation and feature construction against "
            "the confirmed prediction moment."
        ),
        "reasons": [
            (
                "Production-time missingness can change what information is "
                "legitimately available at prediction time."
            ),
            (
                "The approved Investigation proposal is recorded through ADS."
                if approved
                else (
                    "The Investigation remains recommended even though project-state "
                    "creation was rejected."
                )
            ),
        ],
        "referenced_revision_ids": [
            item.revision_id for item in workload.context_pack.revisions
        ],
    }


def _final_model(workload, *, approved: bool = True) -> ScriptedModel:
    return ScriptedModel(
        [
            [
                assistant_message(
                    json.dumps(
                        _recommendation_payload(workload, approved=approved),
                        sort_keys=True,
                    )
                )
            ]
        ]
    )


def _dependencies():
    gateway = InMemoryReferenceGateway(REFERENCE_FIXTURE)
    ledger = ProposalLedger()
    return gateway, ledger


def test_candidate_dependency_is_isolated_from_production_ads_modules() -> None:
    repository_root = Path(__file__).resolve().parents[4]
    assert candidate_import_boundary_violations(repository_root) == []


def test_openai_agents_core_gate_interrupts_before_authoritative_side_effect() -> None:
    workload = representative_workload(run_id="openai-core-interrupt")
    gateway, ledger = _dependencies()
    candidate = OpenAIAgentsCandidate(gateway, ledger)
    model = _initial_model()

    outcome = asyncio.run(candidate.run(workload, model))

    assert candidate.sdk_version == OPENAI_AGENTS_EXPECTED_VERSION
    assert outcome.status is RuntimeStatus.INTERRUPTED
    assert outcome.interruption is not None
    assert outcome.interruption.tool_name == "create_investigation_proposal"
    assert outcome.resume_token is not None
    assert ledger.created_count == 0
    assert gateway.calls == 1
    assert len(model.calls) == 2
    model.assert_complete()

    first_input = json.dumps(model.first_call.input, sort_keys=True, default=str)
    assert workload.context_pack.semantic_digest() in first_input
    for revision in workload.context_pack.revisions:
        assert revision.revision_id in first_input
    assert workload.project.facts["prediction_moment"] not in first_input
    assert workload.project.facts["production_missingness"] not in first_input


def test_openai_agents_run_state_resumes_after_process_boundary() -> None:
    workload = representative_workload(run_id="openai-process-resume")
    gateway, ledger = _dependencies()
    first_candidate = OpenAIAgentsCandidate(gateway, ledger)
    first_model = _initial_model()

    interrupted = asyncio.run(first_candidate.run(workload, first_model))
    assert interrupted.resume_token is not None
    serialized = interrupted.resume_token.to_json()
    assert gateway.calls == 1

    resumed_candidate = OpenAIAgentsCandidate(gateway, ledger)
    resumed_model = _final_model(workload, approved=True)
    outcome = asyncio.run(
        resumed_candidate.resume(
            workload,
            serialized,
            ApprovalDecision.APPROVE,
            resumed_model,
        )
    )

    assert outcome.status is RuntimeStatus.COMPLETED
    assert isinstance(outcome.recommendation, RuntimeRecommendation)
    assert outcome.recommendation.referenced_revision_ids == tuple(
        item.revision_id for item in workload.context_pack.revisions
    )
    assert ledger.created_count == 1
    assert gateway.calls == 1
    assert len(resumed_model.calls) == 1
    resumed_model.assert_complete()
    assert any(
        event.kind == "approval" and event.detail == "approved"
        for event in outcome.trace.events
    )
    assert any(
        event.kind == "validation"
        and event.name == "structured_output"
        and event.detail == "accepted"
        for event in outcome.trace.events
    )


def test_openai_agents_repeated_resume_keeps_ads_side_effect_at_most_once() -> None:
    workload = representative_workload(run_id="openai-repeat-resume")
    gateway, ledger = _dependencies()
    candidate = OpenAIAgentsCandidate(gateway, ledger)
    interrupted = asyncio.run(candidate.run(workload, _initial_model()))
    assert interrupted.resume_token is not None
    serialized = interrupted.resume_token.to_json()

    for _ in range(2):
        resumed_candidate = OpenAIAgentsCandidate(gateway, ledger)
        model = _final_model(workload, approved=True)
        outcome = asyncio.run(
            resumed_candidate.resume(
                workload,
                serialized,
                ApprovalDecision.APPROVE,
                model,
            )
        )
        assert outcome.status is RuntimeStatus.COMPLETED
        model.assert_complete()

    assert ledger.created_count == 1
    assert ledger.execution_attempts == 2
    assert gateway.calls == 1


def test_openai_agents_rejection_does_not_create_project_state() -> None:
    workload = representative_workload(run_id="openai-reject")
    gateway, ledger = _dependencies()
    candidate = OpenAIAgentsCandidate(gateway, ledger)
    interrupted = asyncio.run(candidate.run(workload, _initial_model()))
    assert interrupted.resume_token is not None

    resumed = OpenAIAgentsCandidate(gateway, ledger)
    model = _final_model(workload, approved=False)
    outcome = asyncio.run(
        resumed.resume(
            workload,
            interrupted.resume_token.to_json(),
            ApprovalDecision.REJECT,
            model,
        )
    )

    assert outcome.status is RuntimeStatus.COMPLETED
    assert ledger.created_count == 0
    assert gateway.calls == 1
    model.assert_complete()
    assert any(
        event.kind == "approval" and event.detail == "rejected"
        for event in outcome.trace.events
    )


def test_openai_agents_serialized_state_is_runtime_state_not_project_authority() -> None:
    workload = representative_workload(run_id="openai-state-boundary")
    gateway, ledger = _dependencies()
    candidate = OpenAIAgentsCandidate(gateway, ledger)

    outcome = asyncio.run(candidate.run(workload, _initial_model()))

    assert outcome.resume_token is not None
    state = outcome.resume_token.execution_state["openai_agents_run_state"]
    assert isinstance(state, dict)
    serialized_state = json.dumps(state, sort_keys=True, default=str)

    assert workload.context_pack.semantic_digest() in serialized_state
    assert workload.project.snapshot_id in serialized_state
    assert ledger.created_count == 0
    assert "Finding" not in serialized_state
    assert "Decision" not in serialized_state


def test_openai_agents_stale_ads_context_is_rejected_before_sdk_resume() -> None:
    from dataclasses import replace

    workload = representative_workload(run_id="openai-stale-context")
    gateway, ledger = _dependencies()
    candidate = OpenAIAgentsCandidate(gateway, ledger)
    interrupted = asyncio.run(candidate.run(workload, _initial_model()))
    assert interrupted.resume_token is not None

    changed = replace(
        workload,
        project=replace(workload.project, snapshot_id="project-snapshot-runtime-999"),
    )
    model = _final_model(changed, approved=True)

    try:
        asyncio.run(
            OpenAIAgentsCandidate(gateway, ledger).resume(
                changed,
                interrupted.resume_token.to_json(),
                ApprovalDecision.APPROVE,
                model,
            )
        )
    except ValueError as exc:
        assert "authoritative workload context" in str(exc)
    else:
        raise AssertionError("stale authoritative ADS context was not rejected")

    assert ledger.created_count == 0
    assert len(model.calls) == 0
