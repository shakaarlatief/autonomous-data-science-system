from __future__ import annotations

import asyncio
import json
from pathlib import Path

from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
)
from experiments.dependency_backed_recommendation_action_value.harness import (
    AdvancementOutcome,
    DependencyBackedActionDecision,
    DependencyBackedRecommendationActionResult,
    JudgeObligationScore,
    JudgeResult,
    load_frozen_benchmark,
)
from experiments.dependency_backed_recommendation_action_value.judge import JudgeOutcome
from experiments.dependency_backed_recommendation_action_value.runner import (
    DEFAULT_BENCHMARK,
    execute_frozen_experiment,
)


class FakeReasoningRuntime:
    """Provider-free oracle double proving the complete ADS request/trace pipeline."""

    def __init__(self) -> None:
        benchmark = load_frozen_benchmark(DEFAULT_BENCHMARK)
        self._case_by_task = {case.user_task: case for case in benchmark.cases}
        self.requests: list[ReasoningRequest] = []

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        self.requests.append(request)
        case = self._case_by_task[request.user_task]
        result = DependencyBackedRecommendationActionResult(
            summary="Deterministic provider-free complete-design result.",
            action_decisions=tuple(
                DependencyBackedActionDecision(
                    action_id=action.action_id,
                    disposition=action.expected_disposition.value,
                    blocking_requirement_id=action.expected_blocking_requirement_id,
                    blocked_scope_id=action.expected_blocked_scope_id,
                    defer_until_id=action.expected_defer_until_id,
                    rationale="Deterministic provider-free rationale satisfying the frozen truth.",
                )
                for action in case.candidate_actions
            ),
            warnings=(),
        )
        revision_count = len(request.knowledge_revisions)
        input_tokens = 700 if revision_count == 0 else 1200 if revision_count < 10 else 2600
        usage = ReasoningUsage(
            input_tokens=input_tokens,
            output_tokens=180,
            total_tokens=input_tokens + 180,
            cached_input_tokens=0,
            reasoning_tokens=40,
            service_tier="fake",
            raw_provider_usage={
                "responses": [
                    {
                        "input_tokens": input_tokens,
                        "output_tokens": 180,
                        "total_tokens": input_tokens + 180,
                        "service_tier": "fake",
                    }
                ]
            },
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
                raw_provider_usage={
                    "responses": [
                        {
                            "input_tokens": 500,
                            "output_tokens": 100,
                            "total_tokens": 600,
                            "service_tier": "fake",
                        }
                    ]
                },
            ),
            latency_seconds=0.01,
            requested_model="gpt-5.6-sol",
            provider_model="gpt-5.6-sol",
            runtime_version="fake-1",
            provider_response_ids=(f"judge-response-{judge_id}",),
            provider_request_ids=(f"judge-request-{judge_id}",),
        )


def test_frozen_spec021_vertical_slice_is_provider_free_complete_and_deterministic(
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

    assert result["complete_scored_design"] is True
    assert result["execution_integrity"] is True
    assert result["counts"]["successful_reasoner_outputs"] == 36
    assert result["counts"]["successful_judge_outputs"] == 36
    assert result["counts"]["scored_observations"] == 36
    assert result["provider_attempts"]["used"] == 72
    assert result["provider_attempts"]["maximum"] == 90
    assert result["advancement_outcome"] == AdvancementOutcome.SAFE_NOT_DIFFERENTIATED.value

    gate = result["gate_evaluation"]
    assert gate["absolute_passed"] is True
    assert gate["relative_passed"] is True
    assert gate["expansion_passed"] is True
    assert gate["value_signals"] == []

    assert len(runtime.requests) == 36
    generic = [request for request in runtime.requests if len(request.knowledge_revisions) == 0]
    selective = [request for request in runtime.requests if 0 < len(request.knowledge_revisions) < 10]
    full = [request for request in runtime.requests if len(request.knowledge_revisions) == 10]
    assert len(generic) == 12
    assert len(selective) == 12
    assert len(full) == 12
    assert {len(request.knowledge_revisions) for request in selective} == {2, 3}

    by_task: dict[str, list[ReasoningRequest]] = {}
    for request in runtime.requests:
        by_task.setdefault(request.user_task, []).append(request)
        model_text = request.canonical_model_input()
        for forbidden in (
            "expected_disposition",
            "expected_blocking_requirement_id",
            "expected_blocked_scope_id",
            "expected_defer_until_id",
            '"cost_units"',
            '"rubric"',
        ):
            assert forbidden not in model_text
    assert len(by_task) == 4
    for requests in by_task.values():
        assert len(requests) == 9
        first = requests[0]
        assert all(request.project_evidence == first.project_evidence for request in requests)
        assert all(request.model_configuration == first.model_configuration for request in requests)

    assert len(judge.payloads) == 36
    for payload in judge.payloads:
        text = str(payload)
        for forbidden in (
            "GENERIC",
            "SELECTIVE",
            "FULL_HORIZON",
            "methodological_context",
            "methodology_payload_sha256",
            "input_tokens",
            "latency_seconds",
            "expected_disposition",
            "expected_defer_until_id",
        ):
            assert forbidden not in text

    for filename in (
        "reasoning_plan.json",
        "judge_plan.json",
        "system_provenance_plan.json",
        "reasoner_attempts.jsonl",
        "judge_attempts.jsonl",
        "result.json",
        "RESULT.md",
    ):
        assert (output_dir / filename).is_file()

    reasoner_attempts = [
        json.loads(line)
        for line in (output_dir / "reasoner_attempts.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    judge_attempts = [
        json.loads(line)
        for line in (output_dir / "judge_attempts.jsonl").read_text(encoding="utf-8").splitlines()
    ]
    assert len(reasoner_attempts) == 36
    assert len(judge_attempts) == 36
    assert all(item["status"] == "SUCCESS" for item in reasoner_attempts)
    assert all(item["status"] == "SUCCESS" for item in judge_attempts)
    assert all(
        item["usage"]["raw_provider_usage"]["responses"][0]["service_tier"] == "fake"
        for item in reasoner_attempts
    )
    assert all(
        item["usage"]["raw_provider_usage"]["responses"][0]["service_tier"] == "fake"
        for item in judge_attempts
    )

    technical = result["technical_invariants"]
    assert len(technical) == 24
    assert all(value is True for value in technical.values())
