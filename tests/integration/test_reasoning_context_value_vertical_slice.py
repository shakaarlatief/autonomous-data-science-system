from __future__ import annotations

import asyncio
from pathlib import Path

from ads_system.application.reasoning import (
    ReasoningContextValueResult,
    ReasoningOutcome,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
)
from experiments.reasoning_context_value.harness import (
    JudgeObligationScore,
    JudgeResult,
)
from experiments.reasoning_context_value.judge import JudgeOutcome
from experiments.reasoning_context_value.runner import execute_frozen_experiment


class FakeReasoningRuntime:
    """Provider-free runtime double that preserves the ADS request/trace contract."""

    def __init__(self) -> None:
        self.requests: list[ReasoningRequest] = []

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        self.requests.append(request)
        supplied_keys = tuple(item.stable_key for item in request.knowledge_revisions)
        result = ReasoningContextValueResult(
            answer="Deterministic provider-free vertical-slice result.",
            proposed_actions=("Inspect the frozen task-specific evidence.",),
            required_clarifications=(),
            warnings=(),
            methodological_basis=(supplied_keys[0],),
        )
        input_tokens = 2000 if len(request.knowledge_revisions) == 10 else 1000
        usage = ReasoningUsage(
            input_tokens=input_tokens,
            output_tokens=100,
            total_tokens=input_tokens + 100,
            cached_input_tokens=0,
            reasoning_tokens=20,
            service_tier="fake",
        )
        trace = ReasoningTrace(
            run_id=request.run_id,
            request_digest=request.semantic_digest(),
            methodological_context_sha256=request.methodological_context_sha256,
            knowledge_revisions=request.knowledge_revisions,
            requested_model=request.model_configuration.requested_model,
            provider_model=request.model_configuration.requested_model,
            runtime_name="fake-runtime",
            runtime_version="1",
            provider_response_ids=(f"response-{request.run_id}",),
            provider_request_ids=(f"request-{request.run_id}",),
        )
        return ReasoningOutcome(
            result=result,
            usage=usage,
            trace=trace,
            latency_seconds=0.01,
        )


class FakeSemanticJudge:
    """Condition-blinded judge double returning a consistent perfect rubric score."""

    def __init__(self) -> None:
        self.payloads: list[dict[str, object]] = []

    async def judge(self, *, judge_id: str, payload) -> JudgeOutcome:
        captured = dict(payload)
        self.payloads.append(captured)
        scores = tuple(
            JudgeObligationScore(
                obligation_id=str(item["obligation_id"]),
                score=2,
                rationale="Deterministic provider-free judge score.",
            )
            for item in captured["rubric"]
        )
        result = JudgeResult(
            output_id=str(captured["output_id"]),
            obligation_scores=scores,
            normalized_score=1.0,
            critical_failure=False,
            judge_summary="All frozen obligations explicitly satisfied in fake evaluation.",
        )
        return JudgeOutcome(
            judge_id=judge_id,
            result=result,
            usage=ReasoningUsage(
                input_tokens=500,
                output_tokens=100,
                total_tokens=600,
                cached_input_tokens=0,
                reasoning_tokens=20,
                service_tier="fake",
            ),
            latency_seconds=0.01,
            requested_model="gpt-5.6-sol",
            provider_model="gpt-5.6-sol",
            runtime_version="fake-1",
            provider_response_ids=(f"judge-response-{judge_id}",),
            provider_request_ids=(f"judge-request-{judge_id}",),
        )


def test_frozen_reasoning_context_vertical_slice_is_provider_free_and_deterministic(
    tmp_path: Path,
) -> None:
    runtime = FakeReasoningRuntime()
    judge = FakeSemanticJudge()
    output_dir = tmp_path / "result"

    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=output_dir,
            runtime=runtime,
            judge=judge,
        )
    )

    assert result["overall_frozen_gate_passed"] is True
    assert result["complete_scored_design"] is True
    assert result["counts"]["successful_reasoner_outputs"] == 24
    assert result["counts"]["successful_judge_outputs"] == 24
    assert result["provider_attempts"]["used"] == 48
    assert result["gate_evaluation"]["quality_passed"] is True
    assert result["gate_evaluation"]["efficiency_passed"] is True
    assert result["gate_evaluation"]["aggregate_input_token_ratio"] == 0.5

    assert len(runtime.requests) == 24
    selective = [request for request in runtime.requests if len(request.knowledge_revisions) < 10]
    full = [request for request in runtime.requests if len(request.knowledge_revisions) == 10]
    assert len(selective) == 12
    assert len(full) == 12
    assert {len(request.knowledge_revisions) for request in selective} == {2, 3}

    # Matched conditions differ only in nonce/run identity and methodological
    # context. Task evidence and model configuration remain exactly shared.
    by_task: dict[str, list[ReasoningRequest]] = {}
    for request in runtime.requests:
        by_task.setdefault(request.user_task, []).append(request)
    assert len(by_task) == 4
    for requests in by_task.values():
        assert len(requests) == 6
        first = requests[0]
        assert all(request.project_evidence == first.project_evidence for request in requests)
        assert all(request.model_configuration == first.model_configuration for request in requests)

    assert len(judge.payloads) == 24
    for payload in judge.payloads:
        assert "condition" not in payload
        assert "methodological_context" not in payload
        assert "context_sha256" not in payload
        assert "input_tokens" not in payload
        assert "latency_seconds" not in payload

    assert (output_dir / "reasoning_plan.json").is_file()
    assert (output_dir / "judge_plan.json").is_file()
    assert (output_dir / "reasoner_attempts.jsonl").is_file()
    assert (output_dir / "judge_attempts.jsonl").is_file()
    assert (output_dir / "result.json").is_file()
    assert (output_dir / "RESULT.md").is_file()

    technical = result["technical_invariants"]
    for key, value in technical.items():
        if key == "RV-INV-15_cross_platform_infrastructure":
            assert value == "REQUIRES_CI_EVIDENCE"
        else:
            assert value is True
