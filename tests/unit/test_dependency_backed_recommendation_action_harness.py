from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pytest

from experiments.dependency_backed_recommendation_action_value.harness import (
    AdvancementOutcome,
    DependencyBackedActionDecision,
    DependencyBackedRecommendationActionResult,
    JudgeObligationScore,
    JudgeResult,
    RecommendationCondition,
    RecommendationDisposition,
    RecommendationMetrics,
    RecommendationScoredObservation,
    build_judge_payload,
    build_judge_plan,
    build_reasoning_plan,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    validate_dependency_backed_result,
)


ROOT = Path(__file__).resolve().parents[2]
FIXTURE = (
    ROOT
    / "tests"
    / "fixtures"
    / "reasoning"
    / "dependency_backed_recommendation_action_v1.json"
)


def _oracle_result(case) -> DependencyBackedRecommendationActionResult:
    return DependencyBackedRecommendationActionResult(
        summary="Deterministic provider-free oracle result.",
        action_decisions=tuple(
            DependencyBackedActionDecision(
                action_id=action.action_id,
                disposition=action.expected_disposition.value,
                blocking_requirement_id=action.expected_blocking_requirement_id,
                blocked_scope_id=action.expected_blocked_scope_id,
                defer_until_id=action.expected_defer_until_id,
                rationale="Deterministic provider-free rationale.",
            )
            for action in case.candidate_actions
        ),
        warnings=(),
    )


def _perfect_judge(case, output_id: str) -> JudgeResult:
    return JudgeResult(
        output_id=output_id,
        obligation_scores=tuple(
            JudgeObligationScore(
                obligation_id=item.obligation_id,
                score=2,
                rationale="Explicitly and correctly satisfied.",
            )
            for item in case.rubric
        ),
        normalized_score=1.0,
        critical_failure=False,
        judge_summary="All obligations satisfied.",
    )


def test_frozen_fixture_and_plans_are_exact_and_deterministic() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)

    assert [case.case_id for case in benchmark.cases] == [
        "DBRA-01",
        "DBRA-02",
        "DBRA-03",
        "DBRA-04",
    ]
    assert benchmark.randomization_seed == 2026082402
    assert benchmark.repetitions == 3
    assert len(benchmark.full_horizon_keys) == 10

    first = build_reasoning_plan(benchmark)
    second = build_reasoning_plan(benchmark)
    assert first == second
    assert len(first) == 36
    assert {entry.condition for entry in first} == set(RecommendationCondition)
    assert len({entry.output_id for entry in first}) == 36
    assert len({entry.run_nonce for entry in first}) == 36

    judges = build_judge_plan(
        [entry.output_id for entry in first],
        randomization_seed=benchmark.randomization_seed,
    )
    assert judges == build_judge_plan(
        [entry.output_id for entry in first],
        randomization_seed=benchmark.randomization_seed,
    )
    assert len(judges) == 36
    assert [item.output_id for item in judges] != [item.output_id for item in first]


def test_oracle_outputs_validate_and_score_exactly() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    for case in benchmark.cases:
        result = _oracle_result(case)
        assert validate_dependency_backed_result(case, result) is result
        metrics = evaluate_recommendation_result(case, result)
        assert metrics.exact_disposition_accuracy == 1.0
        assert metrics.critical_action_omissions == 0
        assert metrics.under_recommendations == 0
        assert metrics.over_recommendations == 0
        assert metrics.unnecessary_recommended_cost == 0
        assert metrics.blocking_false_positives == 0
        assert metrics.blocking_pointer_errors == 0
        assert metrics.defer_pointer_errors == 0


def test_nonblocking_model_shortlist_cannot_invent_blocking_relation() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    case = next(item for item in benchmark.cases if item.case_id == "DBRA-02")
    result = _oracle_result(case)
    decisions = list(result.action_decisions)
    first = decisions[0]
    decisions[0] = replace(
        first,
        disposition=RecommendationDisposition.BLOCKING_REQUIRED.value,
        blocking_requirement_id="invented-requirement",
        blocked_scope_id="scope-model-family-selection",
    )
    invalid = replace(result, action_decisions=tuple(decisions))

    with pytest.raises(ValueError, match="unknown blocking_requirement_id"):
        validate_dependency_backed_result(case, invalid)


def test_defer_requires_exact_supplied_wait_relation() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    case = next(item for item in benchmark.cases if item.case_id == "DBRA-03")
    result = _oracle_result(case)
    decisions = list(result.action_decisions)
    index = next(
        i for i, item in enumerate(decisions) if item.action_id == "compare-log-transformation"
    )
    decisions[index] = replace(decisions[index], defer_until_id=None)
    invalid = replace(result, action_decisions=tuple(decisions))

    with pytest.raises(ValueError, match="DEFER must point"):
        validate_dependency_backed_result(case, invalid)


def test_judge_payload_is_condition_and_evaluator_blinded() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    case = benchmark.cases[0]
    payload = build_judge_payload(
        case,
        output_id="opaque-output",
        result=_oracle_result(case),
    ).to_payload()
    text = str(payload)

    for forbidden in (
        "GENERIC",
        "SELECTIVE",
        "FULL_HORIZON",
        "methodological_context",
        "methodology_payload_sha256",
        "expected_disposition",
        "expected_blocking_requirement_id",
        "expected_defer_until_id",
        "cost_units",
    ):
        assert forbidden not in text


def test_equal_perfect_conditions_are_safe_but_not_differentiated() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    observations: list[RecommendationScoredObservation] = []
    for case in benchmark.cases:
        oracle_metrics = evaluate_recommendation_result(case, _oracle_result(case))
        for condition in RecommendationCondition:
            for repetition in range(1, 4):
                output_id = f"{case.case_id}-{condition.value}-{repetition}"
                observations.append(
                    RecommendationScoredObservation(
                        output_id=output_id,
                        case_id=case.case_id,
                        condition=condition,
                        repetition=repetition,
                        metrics=oracle_metrics,
                        judge_result=_perfect_judge(case, output_id),
                    )
                )

    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.absolute_passed is True
    assert evaluation.relative_passed is True
    assert evaluation.expansion_passed is True
    assert evaluation.value_signals == ()
    assert evaluation.outcome is AdvancementOutcome.SAFE_NOT_DIFFERENTIATED


def test_selective_blocking_false_positive_fails_absolute_gate() -> None:
    benchmark = load_frozen_benchmark(FIXTURE)
    observations: list[RecommendationScoredObservation] = []
    for case in benchmark.cases:
        base_metrics = evaluate_recommendation_result(case, _oracle_result(case))
        for condition in RecommendationCondition:
            for repetition in range(1, 4):
                metrics = base_metrics
                if case.case_id == "DBRA-02" and condition is RecommendationCondition.SELECTIVE:
                    metrics = RecommendationMetrics(
                        exact_disposition_accuracy=5 / 6,
                        critical_action_omissions=0,
                        under_recommendations=0,
                        over_recommendations=0,
                        unnecessary_recommended_cost=0,
                        blocking_false_positives=1,
                        blocking_pointer_errors=1,
                        defer_pointer_errors=0,
                    )
                output_id = f"{case.case_id}-{condition.value}-{repetition}"
                observations.append(
                    RecommendationScoredObservation(
                        output_id=output_id,
                        case_id=case.case_id,
                        condition=condition,
                        repetition=repetition,
                        metrics=metrics,
                        judge_result=_perfect_judge(case, output_id),
                    )
                )

    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.gate_results["DBRA-G02"] is False
    assert evaluation.gate_results["DBRA-G03"] is False
    assert evaluation.outcome is AdvancementOutcome.FAIL
