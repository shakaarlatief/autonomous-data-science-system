from __future__ import annotations

from dataclasses import replace
from pathlib import Path

import pytest

from ads_system.application.reasoning import KnowledgeRevisionPointer
from experiments.relation_backed_recommendation_action_value.harness import (
    AdvancementOutcome,
    JudgeObligationScore,
    JudgeResult,
    RecommendationCondition,
    RecommendationMetrics,
    RecommendationScoredObservation,
    RelationBackedActionDecision,
    RelationBackedRecommendationActionResult,
    assert_evaluator_truth_absent,
    build_judge_payload,
    build_judge_plan,
    build_reasoning_plan,
    build_reasoning_request,
    case_by_id,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    serialize_judge_plan,
    serialize_reasoning_plan,
    validate_relation_backed_result,
)
from experiments.relation_backed_recommendation_action_value.harness import (
    RecommendationConditionInput,
)


FIXTURE = Path("tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json")


def _benchmark():
    return load_frozen_benchmark(FIXTURE)


def _perfect_result(case, *, basis: tuple[str, ...] = ()):
    return RelationBackedRecommendationActionResult(
        summary="The supplied project state is classified under the frozen action menu.",
        action_decisions=tuple(
            RelationBackedActionDecision(
                action_id=action.action_id,
                disposition=action.expected_disposition.value,
                defer_until_id=action.expected_defer_until_id,
                rationale="Disposition follows the supplied project state and sequencing evidence.",
            )
            for action in case.candidate_actions
        ),
        blocked_scopes=case.expected_blocked_scopes,
        required_clarification_ids=case.expected_required_clarification_ids,
        warnings=(),
        methodological_basis=basis,
    )


def _perfect_judge(case, output_id: str, *, score: int = 2) -> JudgeResult:
    obligations = tuple(
        JudgeObligationScore(
            obligation_id=item.obligation_id,
            score=score,
            rationale="Frozen obligation is satisfied.",
        )
        for item in case.rubric
    )
    normalized = sum(item.score for item in obligations) / (2 * len(obligations))
    return JudgeResult(
        output_id=output_id,
        obligation_scores=obligations,
        normalized_score=normalized,
        critical_failure=False,
        judge_summary="Frozen rubric satisfied.",
    )


def _perfect_observations():
    benchmark = _benchmark()
    observations = []
    for entry in build_reasoning_plan(benchmark):
        case = case_by_id(benchmark, entry.case_id)
        observations.append(
            RecommendationScoredObservation(
                output_id=entry.output_id,
                case_id=entry.case_id,
                condition=entry.condition,
                repetition=entry.repetition,
                metrics=RecommendationMetrics(
                    exact_disposition_accuracy=1.0,
                    critical_action_omissions=0,
                    under_recommendations=0,
                    over_recommendations=0,
                    unnecessary_recommended_cost=0,
                    blocking_scope_false_negatives=0,
                    blocking_scope_false_positives=0,
                    required_clarification_false_negatives=0,
                    required_clarification_false_positives=0,
                    defer_pointer_errors=0,
                    unsupported_methodological_basis_failures=0,
                ),
                judge_result=_perfect_judge(case, entry.output_id),
            )
        )
    return benchmark, observations


def test_frozen_fixture_and_plans_are_deterministic() -> None:
    benchmark = _benchmark()
    assert benchmark.benchmark_id == "v1-relation-backed-recommendation-action-value-v0.1"
    assert len(benchmark.cases) == 4

    plan_1 = build_reasoning_plan(benchmark)
    plan_2 = build_reasoning_plan(benchmark)
    assert plan_1 == plan_2
    assert len(plan_1) == 36
    assert len({item.output_id for item in plan_1}) == 36
    assert len({item.run_nonce for item in plan_1}) == 36
    reasoner_text_1, reasoner_digest_1 = serialize_reasoning_plan(plan_1)
    reasoner_text_2, reasoner_digest_2 = serialize_reasoning_plan(plan_2)
    assert reasoner_text_1 == reasoner_text_2
    assert reasoner_digest_1 == reasoner_digest_2

    judge_1 = build_judge_plan(
        [item.output_id for item in plan_1],
        randomization_seed=benchmark.randomization_seed,
    )
    judge_2 = build_judge_plan(
        [item.output_id for item in plan_2],
        randomization_seed=benchmark.randomization_seed,
    )
    assert judge_1 == judge_2
    assert len(judge_1) == 36
    assert [item.output_id for item in judge_1] != [item.output_id for item in plan_1]
    assert serialize_judge_plan(judge_1) == serialize_judge_plan(judge_2)


def test_reasoner_input_excludes_hidden_truth_and_is_condition_neutral_except_context() -> None:
    benchmark = _benchmark()
    case = benchmark.cases[0]
    entry = next(
        item
        for item in build_reasoning_plan(benchmark)
        if item.case_id == case.case_id and item.condition is RecommendationCondition.GENERIC
    )
    context = RecommendationConditionInput(
        condition=RecommendationCondition.GENERIC,
        payload={},
        sha256="44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a",
        utf8_bytes=2,
        revisions=(),
    )
    request = build_reasoning_request(
        benchmark=benchmark,
        case=case,
        plan_entry=entry,
        context=context,
    )
    assert_evaluator_truth_absent(request)
    model_input = request.canonical_model_input()
    assert "expected_disposition" not in model_input
    assert "expected_defer_until_id" not in model_input
    assert '"critical"' not in model_input
    assert '"cost_units"' not in model_input
    assert "available_defer_triggers" in model_input


def test_relation_backed_validator_enforces_pointer_and_basis_contracts() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-02")
    revisions = tuple(
        KnowledgeRevisionPointer(stable_key=key, revision_id=f"rev-{index}")
        for index, key in enumerate(case.required_selective_keys, start=1)
    )
    result = _perfect_result(case, basis=case.required_selective_keys)
    assert validate_relation_backed_result(
        case,
        result,
        supplied_revisions=revisions,
    ) is result

    decisions = list(result.action_decisions)
    deferred_index = next(
        index for index, item in enumerate(decisions) if item.disposition == "DEFER"
    )
    decisions[deferred_index] = replace(decisions[deferred_index], defer_until_id=None)
    invalid = replace(result, action_decisions=tuple(decisions))
    with pytest.raises(ValueError, match="DEFER must point"):
        validate_relation_backed_result(case, invalid, supplied_revisions=revisions)

    unsupported = replace(result, methodological_basis=("unknown-asset",))
    with pytest.raises(ValueError, match="unsupported methodological basis"):
        validate_relation_backed_result(case, unsupported, supplied_revisions=revisions)


def test_exact_metrics_include_pointer_and_clarification_false_positive_dimensions() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-01")
    result = _perfect_result(case)
    metrics = evaluate_recommendation_result(case, result, supplied_revisions=())
    assert metrics.exact_disposition_accuracy == 1.0
    assert metrics.defer_pointer_errors == 0
    assert metrics.critical_action_omissions == 0
    assert metrics.blocking_scope_false_negatives == 0
    assert metrics.required_clarification_false_negatives == 0
    assert metrics.required_clarification_false_positives == 0


def test_judge_payload_is_blinded_to_condition_context_usage_and_exact_truth() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-04")
    payload = build_judge_payload(
        case,
        output_id="opaque-output",
        result=_perfect_result(case),
    ).to_payload()
    text = str(payload)
    assert "SELECTIVE" not in text
    assert "FULL_HORIZON" not in text
    assert "expected_disposition" not in text
    assert "methodological_context" not in text
    assert "input_tokens" not in text


def test_perfect_ceiling_is_safe_but_not_differentiated() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.absolute_passed
    assert evaluation.relative_passed
    assert evaluation.expansion_passed
    assert evaluation.value_signals == ()
    assert evaluation.outcome is AdvancementOutcome.SAFE_NOT_DIFFERENTIATED


def test_preregistered_generic_gap_can_promote_when_all_safety_gates_still_pass() -> None:
    benchmark, observations = _perfect_observations()
    changed = list(observations)
    generic_indices = [
        index
        for index, item in enumerate(changed)
        if item.condition is RecommendationCondition.GENERIC
    ]
    for index in generic_indices[:3]:
        item = changed[index]
        changed[index] = replace(
            item,
            metrics=replace(item.metrics, exact_disposition_accuracy=0.5),
        )
    evaluation = evaluate_gates(benchmark, changed)
    assert evaluation.absolute_passed
    assert evaluation.relative_passed
    assert evaluation.expansion_passed
    assert (
        "SELECTIVE_AGGREGATE_EXACT_ACCURACY_AT_LEAST_0_05_ABOVE_GENERIC"
        in evaluation.value_signals
    )
    assert evaluation.outcome is AdvancementOutcome.PROMOTE


def test_selective_pointer_error_forces_fail() -> None:
    benchmark, observations = _perfect_observations()
    changed = list(observations)
    index = next(
        index
        for index, item in enumerate(changed)
        if item.condition is RecommendationCondition.SELECTIVE
    )
    item = changed[index]
    changed[index] = replace(
        item,
        metrics=replace(item.metrics, defer_pointer_errors=1),
    )
    evaluation = evaluate_gates(benchmark, changed)
    assert not evaluation.absolute_passed
    assert not evaluation.gate_results["RBR-G04"]
    assert evaluation.outcome is AdvancementOutcome.FAIL
