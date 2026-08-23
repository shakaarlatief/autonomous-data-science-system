from __future__ import annotations

from dataclasses import replace
from pathlib import Path

from ads_system.application.recommendation import (
    RecommendationActionDecision,
    RecommendationActionResult,
)
from experiments.recommendation_action_value.harness import (
    AdvancementOutcome,
    JudgeObligationScore,
    JudgeResult,
    RecommendationCondition,
    RecommendationMetrics,
    RecommendationScoredObservation,
    build_judge_plan,
    build_reasoning_plan,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    serialize_judge_plan,
    serialize_reasoning_plan,
)


FIXTURE = (
    Path(__file__).resolve().parents[1]
    / "fixtures"
    / "reasoning"
    / "recommendation_action_v1.json"
)


def _perfect_result(case) -> RecommendationActionResult:
    return RecommendationActionResult(
        summary="Follow the frozen project dependencies and current objective.",
        action_decisions=tuple(
            RecommendationActionDecision(
                action_id=action.action_id,
                disposition=action.expected_disposition,
                rationale="This disposition follows the supplied project state.",
            )
            for action in case.candidate_actions
        ),
        blocked_scopes=case.expected_blocked_scopes,
        required_clarification_ids=case.expected_required_clarification_ids,
        warnings=(),
        methodological_basis=(),
    )


def _perfect_judge(case, output_id: str) -> JudgeResult:
    return JudgeResult(
        output_id=output_id,
        obligation_scores=tuple(
            JudgeObligationScore(
                obligation_id=obligation.obligation_id,
                score=2,
                rationale="The frozen obligation is explicitly satisfied.",
            )
            for obligation in case.rubric
        ),
        normalized_score=1.0,
        critical_failure=False,
        judge_summary="All frozen obligations are satisfied.",
    )


def _perfect_observations(benchmark) -> list[RecommendationScoredObservation]:
    cases = {case.case_id: case for case in benchmark.cases}
    observations: list[RecommendationScoredObservation] = []
    for entry in build_reasoning_plan(benchmark):
        case = cases[entry.case_id]
        result = _perfect_result(case)
        metrics = evaluate_recommendation_result(
            case,
            result,
            supplied_revisions=(),
        )
        observations.append(
            RecommendationScoredObservation(
                output_id=entry.output_id,
                case_id=entry.case_id,
                condition=entry.condition,
                repetition=entry.repetition,
                metrics=metrics,
                judge_result=_perfect_judge(case, entry.output_id),
            )
        )
    return observations


def test_frozen_benchmark_and_plans_are_deterministic() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    assert len(benchmark.cases) == 4
    assert benchmark.repetitions == 3

    first = build_reasoning_plan(benchmark)
    second = build_reasoning_plan(benchmark)
    assert first == second
    assert len(first) == 36
    assert len({item.output_id for item in first}) == 36

    first_text, first_digest = serialize_reasoning_plan(first)
    second_text, second_digest = serialize_reasoning_plan(second)
    assert first_text == second_text
    assert first_digest == second_digest

    judge_first = build_judge_plan(
        [item.output_id for item in first],
        randomization_seed=benchmark.randomization_seed,
    )
    judge_second = build_judge_plan(
        [item.output_id for item in first],
        randomization_seed=benchmark.randomization_seed,
    )
    assert judge_first == judge_second
    assert len(judge_first) == 36
    assert {item.output_id for item in judge_first} == {
        item.output_id for item in first
    }
    assert serialize_judge_plan(judge_first) == serialize_judge_plan(judge_second)


def test_model_task_payload_excludes_hidden_evaluator_truth() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    case = benchmark.cases[0]
    payload = case.model_task_payload()

    assert payload["requested_reasoning_functions"] == ["VALIDITY_CONSTRAINT"]
    assert "expected_blocked_scopes" not in payload
    assert "expected_required_clarification_ids" not in payload
    assert "rubric" not in payload
    for action in payload["candidate_actions"]:
        assert set(action) == {"action_id", "label", "cost_units"}
        assert "expected_disposition" not in action
        assert "critical" not in action


def test_exact_evaluator_counts_validity_gate_failures() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    case = next(item for item in benchmark.cases if item.case_id == "RA-01")

    result = RecommendationActionResult(
        summary="Proceed without blocking anything.",
        action_decisions=tuple(
            RecommendationActionDecision(
                action_id=action.action_id,
                disposition=(
                    action.expected_disposition
                    if not action.critical
                    else "NOT_NOW"
                ),
                rationale="Test result.",
            )
            for action in case.candidate_actions
        ),
        blocked_scopes=(),
        required_clarification_ids=(),
        warnings=(),
        methodological_basis=(),
    )

    metrics = evaluate_recommendation_result(
        case,
        result,
        supplied_revisions=(),
    )
    assert metrics.critical_action_omissions == 3
    assert metrics.blocking_scope_false_negatives == 2
    assert metrics.required_clarification_false_negatives == 1
    assert metrics.exact_disposition_accuracy == 0.5


def test_perfect_three_way_ceiling_is_safe_but_not_differentiated() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    evaluation = evaluate_gates(benchmark, _perfect_observations(benchmark))

    assert evaluation.absolute_passed
    assert evaluation.relative_passed
    assert evaluation.expansion_passed
    assert not evaluation.value_signals
    assert evaluation.outcome is AdvancementOutcome.SAFE_BUT_NOT_DIFFERENTIATED
    assert all(evaluation.gate_results.values())


def test_preregistered_positive_signal_promotes_only_after_all_safety_gates_pass() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    observations = _perfect_observations(benchmark)

    generic_index = next(
        index
        for index, observation in enumerate(observations)
        if observation.condition is RecommendationCondition.GENERIC
        and observation.case_id == "RA-02"
        and observation.repetition == 1
    )
    generic = observations[generic_index]
    observations[generic_index] = replace(
        generic,
        metrics=replace(
            generic.metrics,
            exact_disposition_accuracy=5 / 6,
            under_recommendations=1,
        ),
    )

    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.absolute_passed
    assert evaluation.relative_passed
    assert evaluation.expansion_passed
    assert "SELECTIVE_FEWER_TOTAL_UNDER_RECOMMENDATIONS_THAN_GENERIC" in evaluation.value_signals
    assert evaluation.outcome is AdvancementOutcome.PROMOTE_BOUNDED_RECOMMENDATION_SEAM


def test_selective_critical_omission_forces_fail() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    observations = _perfect_observations(benchmark)

    selective_index = next(
        index
        for index, observation in enumerate(observations)
        if observation.condition is RecommendationCondition.SELECTIVE
    )
    selective = observations[selective_index]
    observations[selective_index] = replace(
        selective,
        metrics=RecommendationMetrics(
            exact_disposition_accuracy=selective.metrics.exact_disposition_accuracy,
            critical_action_omissions=1,
            under_recommendations=selective.metrics.under_recommendations,
            over_recommendations=selective.metrics.over_recommendations,
            unnecessary_recommended_cost=selective.metrics.unnecessary_recommended_cost,
            blocking_scope_false_negatives=selective.metrics.blocking_scope_false_negatives,
            blocking_scope_false_positives=selective.metrics.blocking_scope_false_positives,
            required_clarification_false_negatives=selective.metrics.required_clarification_false_negatives,
            unsupported_methodological_basis=selective.metrics.unsupported_methodological_basis,
        ),
    )

    evaluation = evaluate_gates(benchmark, observations)
    assert not evaluation.gate_results["RA-G01"]
    assert evaluation.outcome is AdvancementOutcome.FAIL
