from __future__ import annotations

import asyncio
from pathlib import Path

from ads_system.application.recommendation import (
    RecommendationActionDecision,
    RecommendationActionResult,
)
from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
)
from experiments.recommendation_action_value.harness import (
    AdvancementOutcome,
    JudgeObligationScore,
    JudgeResult,
    build_reasoning_plan,
    load_frozen_benchmark,
)
from experiments.recommendation_action_value.judge import JudgeOutcome
from experiments.recommendation_action_value.runner import execute_frozen_experiment


FIXTURE = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "reasoning"
    / "recommendation_action_v1.json"
)


class FakeRecommendationRuntime:
    """Provider-free runtime double for the complete frozen 36-call reasoner plan."""

    def __init__(self, expected_results: dict[str, RecommendationActionResult]) -> None:
        self.expected_results = expected_results
        self.requests: list[ReasoningRequest] = []

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        self.requests.append(request)
        result = self.expected_results[request.run_id]
        supplied_count = len(request.knowledge_revisions)
        input_tokens = 700 if supplied_count == 0 else 1100 if supplied_count < 10 else 3000
        return ReasoningOutcome(
            result=result,
            usage=ReasoningUsage(
                input_tokens=input_tokens,
                output_tokens=180,
                total_tokens=input_tokens + 180,
                cached_input_tokens=0,
                reasoning_tokens=40,
                service_tier="fake",
            ),
            trace=ReasoningTrace(
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
            ),
            latency_seconds=0.01,
        )


class FakeRecommendationJudge:
    """Condition-blinded fake judge returning a consistent perfect semantic score."""

    def __init__(self) -> None:
        self.payloads: list[dict[str, object]] = []

    async def judge(self, *, judge_id: str, payload) -> JudgeOutcome:
        captured = dict(payload)
        self.payloads.append(captured)
        scores = tuple(
            JudgeObligationScore(
                obligation_id=str(item["obligation_id"]),
                score=2,
                rationale="Deterministic provider-free semantic score.",
            )
            for item in captured["rubric"]
        )
        result = JudgeResult(
            output_id=str(captured["output_id"]),
            obligation_scores=scores,
            normalized_score=1.0,
            critical_failure=False,
            judge_summary="All frozen semantic obligations satisfied in fake evaluation.",
        )
        return JudgeOutcome(
            judge_id=judge_id,
            result=result,
            usage=ReasoningUsage(
                input_tokens=600,
                output_tokens=120,
                total_tokens=720,
                cached_input_tokens=0,
                reasoning_tokens=30,
                service_tier="fake",
            ),
            latency_seconds=0.01,
            requested_model="gpt-5.6-sol",
            provider_model="gpt-5.6-sol",
            runtime_version="fake-1",
            provider_response_ids=(f"judge-response-{judge_id}",),
            provider_request_ids=(f"judge-request-{judge_id}",),
        )


def _expected_results() -> dict[str, RecommendationActionResult]:
    benchmark = load_frozen_benchmark(FIXTURE)
    case_by_id = {case.case_id: case for case in benchmark.cases}
    results: dict[str, RecommendationActionResult] = {}
    for entry in build_reasoning_plan(benchmark):
        case = case_by_id[entry.case_id]
        results[entry.output_id] = RecommendationActionResult(
            summary="Follow the frozen project dependencies and current objective.",
            action_decisions=tuple(
                RecommendationActionDecision(
                    action_id=action.action_id,
                    disposition=action.expected_disposition,
                    rationale="This disposition follows the supplied project microstate.",
                )
                for action in case.candidate_actions
            ),
            blocked_scopes=case.expected_blocked_scopes,
            required_clarification_ids=case.expected_required_clarification_ids,
            warnings=(),
            methodological_basis=(),
        )
    return results


def test_frozen_recommendation_action_vertical_slice_is_provider_free_and_complete(
    tmp_path: Path,
) -> None:
    runtime = FakeRecommendationRuntime(_expected_results())
    judge = FakeRecommendationJudge()
    output_dir = tmp_path / "result"

    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=output_dir,
            benchmark_path=FIXTURE,
            runtime=runtime,
            judge=judge,
        )
    )

    assert result["complete_scored_design"] is True
    assert result["provider_free_execution_valid"] is True
    assert result["advancement_outcome"] == AdvancementOutcome.SAFE_BUT_NOT_DIFFERENTIATED.value
    assert result["counts"]["successful_reasoner_outputs"] == 36
    assert result["counts"]["successful_judge_outputs"] == 36
    assert result["provider_attempts"]["used"] == 72

    gate = result["gate_evaluation"]
    assert gate["absolute_passed"] is True
    assert gate["relative_passed"] is True
    assert gate["expansion_passed"] is True
    assert gate["value_signals"] == []
    assert all(gate["gate_results"].values())

    assert len(runtime.requests) == 36
    generic = [request for request in runtime.requests if not request.knowledge_revisions]
    selective = [
        request
        for request in runtime.requests
        if 0 < len(request.knowledge_revisions) < 10
    ]
    full = [request for request in runtime.requests if len(request.knowledge_revisions) == 10]
    assert len(generic) == 12
    assert len(selective) == 12
    assert len(full) == 12
    assert {len(request.knowledge_revisions) for request in selective} == {2, 3}

    for request in generic:
        assert dict(request.methodological_context_payload) == {}
        assert request.knowledge_revisions == ()
        assert "GENERIC" not in request.canonical_model_input()
    for request in runtime.requests:
        assert request.task_payload is not None
        assert "expected_disposition" not in request.canonical_model_input()
        assert "expected_blocked_scopes" not in request.canonical_model_input()
        assert "expected_required_clarification_ids" not in request.canonical_model_input()

    assert len(judge.payloads) == 36
    for payload in judge.payloads:
        serialized = str(payload)
        assert "GENERIC" not in serialized
        assert "SELECTIVE" not in serialized
        assert "FULL_HORIZON" not in serialized
        assert "methodological_context" not in payload
        assert "context_sha256" not in payload
        assert "expected_disposition" not in serialized
        assert "expected_blocked_scopes" not in serialized
        assert "expected_required_clarification_ids" not in serialized
        assert "input_tokens" not in payload
        assert "latency_seconds" not in payload

    assert result["project_state_before"] == {
        "prj_project": 0,
        "prj_entity": 0,
        "prj_finding": 0,
        "prj_knowledge_ref": 0,
    }
    assert result["project_state_after"] == result["project_state_before"]

    technical = result["technical_invariants"]
    for key, value in technical.items():
        if key == "RA-INV-18_cross_platform_provider_free":
            assert value == "REQUIRES_CI_EVIDENCE"
        else:
            assert value is True

    assert (output_dir / "reasoning_plan.json").is_file()
    assert (output_dir / "judge_plan.json").is_file()
    assert (output_dir / "reasoner_attempts.jsonl").is_file()
    assert (output_dir / "judge_attempts.jsonl").is_file()
    assert (output_dir / "result.json").is_file()
    assert (output_dir / "RESULT.md").is_file()
    assert (output_dir / "recommendation_action_value.sqlite3").is_file()
