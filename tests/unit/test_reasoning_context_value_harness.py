from __future__ import annotations

from pathlib import Path

import pytest

from experiments.reasoning_context_value.harness import (
    ContextCondition,
    JudgeObligationScore,
    JudgeResult,
    ReasoningScoredObservation,
    build_judge_plan,
    build_reasoning_plan,
    evaluate_gates,
    load_frozen_benchmark,
    serialize_reasoning_plan,
    validate_judge_result,
)


ROOT = Path(__file__).resolve().parents[2]
BENCHMARK = ROOT / "tests" / "fixtures" / "reasoning" / "context_value_v1.json"


def _judge_result(case, *, score: int = 2) -> JudgeResult:
    scores = tuple(
        JudgeObligationScore(
            obligation_id=item.obligation_id,
            score=score,
            rationale="Deterministic fake score for harness validation.",
        )
        for item in case.rubric
    )
    normalized = sum(item.score for item in scores) / (2 * len(scores))
    return JudgeResult(
        output_id="output-test",
        obligation_scores=scores,
        normalized_score=normalized,
        critical_failure=any(item.critical and score == 0 for item in case.rubric),
        judge_summary="Deterministic fake judge result.",
    )


def test_frozen_reasoning_and_judge_plans_are_deterministic() -> None:
    benchmark = load_frozen_benchmark(BENCHMARK)
    first = build_reasoning_plan(benchmark)
    second = build_reasoning_plan(benchmark)
    assert first == second
    assert len(first) == 24
    assert {item.condition for item in first} == {
        ContextCondition.SELECTIVE,
        ContextCondition.FULL_HORIZON,
    }

    first_text, first_sha = serialize_reasoning_plan(first)
    second_text, second_sha = serialize_reasoning_plan(second)
    assert (first_text, first_sha) == (second_text, second_sha)

    output_ids = [f"output-{index:02d}" for index in range(24)]
    judges_a = build_judge_plan(output_ids, randomization_seed=benchmark.randomization_seed)
    judges_b = build_judge_plan(output_ids, randomization_seed=benchmark.randomization_seed)
    assert judges_a == judges_b
    assert len(judges_a) == 24
    assert {item.output_id for item in judges_a} == set(output_ids)


def test_judge_result_is_recomputed_against_frozen_rubric() -> None:
    benchmark = load_frozen_benchmark(BENCHMARK)
    case = benchmark.cases[0]
    valid = _judge_result(case)
    validate_judge_result(case, valid)

    invalid = JudgeResult(
        output_id="output-test",
        obligation_scores=valid.obligation_scores,
        normalized_score=0.5,
        critical_failure=False,
        judge_summary="Invalid reported aggregate.",
    )
    with pytest.raises(ValueError, match="normalized score is inconsistent"):
        validate_judge_result(case, invalid)


def test_preregistered_gates_pass_for_quality_preserved_and_reduced_tokens() -> None:
    benchmark = load_frozen_benchmark(BENCHMARK)
    observations: list[ReasoningScoredObservation] = []
    for case in benchmark.cases:
        for repetition in range(1, benchmark.repetitions + 1):
            for condition, tokens in (
                (ContextCondition.SELECTIVE, 100),
                (ContextCondition.FULL_HORIZON, 200),
            ):
                observations.append(
                    ReasoningScoredObservation(
                        case_id=case.case_id,
                        condition=condition,
                        repetition=repetition,
                        judge_result=_judge_result(case, score=2),
                        input_tokens=tokens,
                    )
                )

    gate = evaluate_gates(benchmark, observations)
    assert gate.quality_passed
    assert gate.efficiency_passed
    assert gate.aggregate_selective_quality == 1.0
    assert gate.aggregate_full_quality == 1.0
    assert gate.aggregate_input_token_ratio == 0.5
    assert not gate.critical_regressions
    assert not gate.matched_pair_token_failures


def test_critical_regression_fails_quality_gate() -> None:
    benchmark = load_frozen_benchmark(BENCHMARK)
    observations: list[ReasoningScoredObservation] = []
    target_case = benchmark.cases[0]
    target_critical = next(item for item in target_case.rubric if item.critical)

    for case in benchmark.cases:
        for repetition in range(1, benchmark.repetitions + 1):
            for condition, tokens in (
                (ContextCondition.SELECTIVE, 100),
                (ContextCondition.FULL_HORIZON, 200),
            ):
                scores = []
                for obligation in case.rubric:
                    score = 2
                    if (
                        case.case_id == target_case.case_id
                        and condition is ContextCondition.SELECTIVE
                        and obligation.obligation_id == target_critical.obligation_id
                    ):
                        score = 0
                    scores.append(
                        JudgeObligationScore(
                            obligation_id=obligation.obligation_id,
                            score=score,
                            rationale="Frozen synthetic regression probe.",
                        )
                    )
                normalized = sum(item.score for item in scores) / (2 * len(scores))
                observations.append(
                    ReasoningScoredObservation(
                        case_id=case.case_id,
                        condition=condition,
                        repetition=repetition,
                        judge_result=JudgeResult(
                            output_id=f"{case.case_id}-{condition.value}-{repetition}",
                            obligation_scores=tuple(scores),
                            normalized_score=normalized,
                            critical_failure=any(
                                obligation.critical and score.score == 0
                                for obligation, score in zip(case.rubric, scores, strict=True)
                            ),
                            judge_summary="Frozen synthetic regression probe.",
                        ),
                        input_tokens=tokens,
                    )
                )

    gate = evaluate_gates(benchmark, observations)
    assert not gate.quality_passed
    assert gate.efficiency_passed
    assert gate.critical_regressions
