from __future__ import annotations

from pathlib import Path

import pytest

from experiments.disposition_semantics.harness import (
    DiagnosticOutcome,
    Disposition,
    DispositionObservation,
    DispositionSemanticsResult,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    historical_ra02_spec016_admissibility,
    load_frozen_benchmark,
    pair_by_id,
    perfect_result_for_variant,
    serialize_reasoning_plan,
    validate_result_for_pair,
    variant_by_id,
)


FIXTURE = Path("tests/fixtures/reasoning/disposition_semantics_v1.json")
HISTORICAL_FIXTURE = Path("tests/fixtures/reasoning/recommendation_action_v1.json")


def _benchmark():
    return load_frozen_benchmark(FIXTURE)


def _perfect_observations():
    benchmark = _benchmark()
    observations: list[DispositionObservation] = []
    for entry in build_reasoning_plan(benchmark):
        pair = pair_by_id(benchmark, entry.pair_id)
        variant = variant_by_id(pair, entry.variant_id)
        observations.append(
            DispositionObservation(
                pair_id=entry.pair_id,
                variant_id=entry.variant_id,
                repetition=entry.repetition,
                result=perfect_result_for_variant(pair, variant),
            )
        )
    return benchmark, observations


def test_fixture_and_plan_are_frozen_complete_and_deterministic() -> None:
    benchmark = _benchmark()
    assert len(benchmark.pairs) == 6
    assert sum(len(pair.variants) for pair in benchmark.pairs) == 12

    first = build_reasoning_plan(benchmark)
    second = build_reasoning_plan(benchmark)
    assert first == second
    assert len(first) == 36
    assert len({entry.run_id for entry in first}) == 36
    assert len({entry.run_nonce for entry in first}) == 36

    first_text, first_digest = serialize_reasoning_plan(first)
    second_text, second_digest = serialize_reasoning_plan(second)
    assert first_text == second_text
    assert first_digest == second_digest
    assert len(first_digest) == 64


def test_reasoning_request_is_truth_blinded_and_has_no_methodology() -> None:
    benchmark = _benchmark()
    entry = build_reasoning_plan(benchmark)[0]
    request = build_reasoning_request(benchmark=benchmark, plan_entry=entry)

    text = request.canonical_model_input()
    assert "expected_disposition" not in text
    assert "expected_defer_until_id" not in text
    assert request.knowledge_revisions == ()
    assert dict(request.methodological_context_payload) == {}
    assert request.structured_output_type is DispositionSemanticsResult
    assert request.structured_output_schema_id.endswith("DispositionSemanticsResult")


def test_result_pointer_contract_rejects_invalid_combinations() -> None:
    benchmark = _benchmark()
    pair = pair_by_id(benchmark, "DS-01")

    valid_defer = DispositionSemanticsResult(
        disposition="DEFER",
        defer_until_id="model-family-selected",
        rationale="The model family must be selected first.",
    )
    validate_result_for_pair(pair, valid_defer)

    with pytest.raises(ValueError, match="supplied trigger"):
        validate_result_for_pair(
            pair,
            DispositionSemanticsResult(
                disposition="DEFER",
                defer_until_id="invented-trigger",
                rationale="Invalid pointer.",
            ),
        )

    with pytest.raises(ValueError, match="NOT_NOW"):
        validate_result_for_pair(
            pair,
            DispositionSemanticsResult(
                disposition="NOT_NOW",
                defer_until_id="model-family-selected",
                rationale="A NOT_NOW output cannot carry a defer trigger.",
            ),
        )

    with pytest.raises(ValueError, match="unsupported disposition"):
        DispositionSemanticsResult(
            disposition="RECOMMENDED",
            defer_until_id=None,
            rationale="Outside this diagnostic taxonomy.",
        )


def test_perfect_fake_result_supports_boundary() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(benchmark, observations)

    assert evaluation.completed is True
    assert evaluation.all_hard_gates_passed is True
    assert evaluation.outcome is DiagnosticOutcome.SUPPORTED
    assert evaluation.aggregate_exact_disposition_accuracy == 1.0
    assert evaluation.expected_defer_pointer_accuracy == 1.0
    assert evaluation.expected_not_now_null_pointer_accuracy == 1.0
    assert all(value == 3 for value in evaluation.correct_repetitions_by_variant.values())


def test_single_exact_label_miss_fails_strict_pointer_side_gate() -> None:
    benchmark, observations = _perfect_observations()
    target_index = next(
        index
        for index, observation in enumerate(observations)
        if variant_by_id(
            pair_by_id(benchmark, observation.pair_id), observation.variant_id
        ).expected_disposition
        is Disposition.NOT_NOW
    )
    target = observations[target_index]
    pair = pair_by_id(benchmark, target.pair_id)
    valid_trigger = pair.triggers[0].trigger_id
    observations[target_index] = DispositionObservation(
        pair_id=target.pair_id,
        variant_id=target.variant_id,
        repetition=target.repetition,
        result=DispositionSemanticsResult(
            disposition="DEFER",
            defer_until_id=valid_trigger,
            rationale="Deliberate provider-free miss for gate testing.",
        ),
    )

    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.aggregate_exact_disposition_accuracy > 0.95
    assert evaluation.aggregate_accuracy_passed is True
    assert evaluation.variant_majority_passed is True
    assert evaluation.pair_polarity_passed is True
    assert evaluation.not_now_null_pointer_passed is False
    assert evaluation.outcome is DiagnosticOutcome.NOT_SUPPORTED


def test_incomplete_observation_set_returns_incomplete() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(
        benchmark,
        observations[:-1],
        execution_complete=False,
    )
    assert evaluation.completed is False
    assert evaluation.outcome is DiagnosticOutcome.INCOMPLETE


def test_historical_ra02_defer_examples_are_not_rewritten_but_fail_new_admissibility() -> None:
    result = historical_ra02_spec016_admissibility(HISTORICAL_FIXTURE)
    assert result == {
        "add-generic-bagging-baseline": "NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER",
        "plot-all-feature-histograms-before-shortlist": "NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER",
    }
