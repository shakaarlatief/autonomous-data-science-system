from __future__ import annotations

from pathlib import Path

import pytest

from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningTrace,
    ReasoningUsage,
)
from experiments.relation_backed_recommendation_action_value.harness import (
    AdvancementOutcome,
    JudgeObligationScore,
    JudgeResult,
    RelationBackedActionDecision,
    RelationBackedRecommendationActionResult,
    build_reasoning_plan,
    case_by_id,
    load_frozen_benchmark,
)
from experiments.relation_backed_recommendation_action_value.judge import JudgeOutcome
from experiments.relation_backed_recommendation_action_value.runner import (
    execute_frozen_experiment,
)


FIXTURE = Path("tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json")


class PerfectRuntime:
    def __init__(self, results_by_run_id):
        self.results_by_run_id = results_by_run_id
        self.calls = 0

    async def run(self, request):
        self.calls += 1
        result = self.results_by_run_id[request.run_id]
        return ReasoningOutcome(
            result=result,
            usage=ReasoningUsage(
                input_tokens=500 + len(request.knowledge_revisions) * 100,
                output_tokens=120,
                total_tokens=620 + len(request.knowledge_revisions) * 100,
                cached_input_tokens=0,
                reasoning_tokens=20,
                service_tier="default",
                raw_provider_usage={"fake": True},
            ),
            trace=ReasoningTrace(
                run_id=request.run_id,
                request_digest=request.semantic_digest(),
                methodological_context_sha256=request.methodological_context_sha256,
                knowledge_revisions=request.knowledge_revisions,
                requested_model=request.model_configuration.requested_model,
                provider_model=request.model_configuration.requested_model,
                runtime_name="fake-runtime",
                runtime_version="test",
                provider_response_ids=(f"response-{request.run_id}",),
                provider_request_ids=(f"request-{request.run_id}",),
            ),
            latency_seconds=0.01,
        )


class PerfectJudge:
    def __init__(self):
        self.calls = 0

    async def judge(self, *, judge_id: str, payload):
        self.calls += 1
        output_id = str(payload["output_id"])
        rubric = payload["rubric"]
        scores = tuple(
            JudgeObligationScore(
                obligation_id=str(item["obligation_id"]),
                score=2,
                rationale="The candidate explicitly satisfies the frozen semantic obligation.",
            )
            for item in rubric
        )
        result = JudgeResult(
            output_id=output_id,
            obligation_scores=scores,
            normalized_score=1.0,
            critical_failure=False,
            judge_summary="All frozen obligations are satisfied.",
        )
        return JudgeOutcome(
            judge_id=judge_id,
            result=result,
            usage=ReasoningUsage(
                input_tokens=400,
                output_tokens=80,
                total_tokens=480,
                cached_input_tokens=0,
                reasoning_tokens=10,
                service_tier="default",
                raw_provider_usage={"fake": True},
            ),
            latency_seconds=0.01,
            requested_model="gpt-5.6-sol",
            provider_model="gpt-5.6-sol",
            runtime_version="test",
            provider_response_ids=(f"judge-response-{judge_id}",),
            provider_request_ids=(f"judge-request-{judge_id}",),
        )


def _perfect_results_by_run_id():
    benchmark = load_frozen_benchmark(FIXTURE)
    results = {}
    for entry in build_reasoning_plan(benchmark):
        case = case_by_id(benchmark, entry.case_id)
        results[entry.output_id] = RelationBackedRecommendationActionResult(
            summary="The frozen action menu is classified consistently with the supplied project state.",
            action_decisions=tuple(
                RelationBackedActionDecision(
                    action_id=action.action_id,
                    disposition=action.expected_disposition.value,
                    defer_until_id=action.expected_defer_until_id,
                    rationale="The disposition follows the supplied project evidence and exact sequencing relation.",
                )
                for action in case.candidate_actions
            ),
            blocked_scopes=case.expected_blocked_scopes,
            required_clarification_ids=case.expected_required_clarification_ids,
            warnings=(),
            methodological_basis=(),
        )
    return results


@pytest.mark.asyncio
async def test_complete_fake_vertical_slice_preserves_state_and_returns_safe_ceiling(tmp_path) -> None:
    runtime = PerfectRuntime(_perfect_results_by_run_id())
    judge = PerfectJudge()
    output_dir = tmp_path / "spec017"

    result = await execute_frozen_experiment(
        output_dir=output_dir,
        benchmark_path=FIXTURE,
        runtime=runtime,
        judge=judge,
    )

    assert runtime.calls == 36
    assert judge.calls == 36
    assert result["complete_scored_design"] is True
    assert result["execution_integrity_passed"] is True
    assert result["provider_attempts"]["used"] == 72
    assert result["counts"]["successful_reasoner_outputs"] == 36
    assert result["counts"]["successful_judge_outputs"] == 36
    assert result["counts"]["scored_observations"] == 36
    assert result["project_state_before"] == result["project_state_after"]
    assert result["advancement_outcome"] == AdvancementOutcome.SAFE_NOT_DIFFERENTIATED.value
    assert result["gate_evaluation"]["absolute_passed"] is True
    assert result["gate_evaluation"]["relative_passed"] is True
    assert result["gate_evaluation"]["expansion_passed"] is True
    assert result["gate_evaluation"]["value_signals"] == []
    assert result["context_summary"]["SELECTIVE_FULL_RATIO"] < 1.0

    for name in (
        "reasoning_plan.json",
        "judge_plan.json",
        "reasoner_attempts.jsonl",
        "judge_attempts.jsonl",
        "result.json",
        "RESULT.md",
        "relation_backed_recommendation_action.sqlite3",
    ):
        assert (output_dir / name).exists()
