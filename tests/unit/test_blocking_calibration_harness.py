from __future__ import annotations

from pathlib import Path

import pytest

from experiments.blocking_calibration.harness import (
    BlockingCalibrationResult,
    BlockingDisposition,
    BlockingObservation,
    DiagnosticOutcome,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    load_frozen_benchmark,
    pair_by_id,
    perfect_result_for_variant,
    serialize_reasoning_plan,
    validate_result_for_pair,
    variant_by_id,
)


FIXTURE = Path("tests/fixtures/reasoning/blocking_calibration_v1.json")


def _benchmark():
    return load_frozen_benchmark(FIXTURE)


def _perfect_observations():
    benchmark = _benchmark()
    observations: list[BlockingObservation] = []
    for entry in build_reasoning_plan(benchmark):
        pair = pair_by_id(benchmark, entry.pair_id)
        variant = variant_by_id(pair, entry.variant_id)
        observations.append(
            BlockingObservation(
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
    assert benchmark.starting_integration_sha == (
        "b9c9c3a38935983075a9ca88632177980bb20ede"
    )

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
    assert "expected_blocking_requirement_id" not in text
    assert "expected_blocked_scope_id" not in text
    assert "BC-G05" not in text
    assert request.knowledge_revisions == ()
    assert dict(request.methodological_context_payload) == {}
    assert request.structured_output_type is BlockingCalibrationResult
    assert request.structured_output_schema_id.endswith("BlockingCalibrationResult")


def test_result_pointer_contract_rejects_invalid_combinations() -> None:
    benchmark = _benchmark()
    pair = pair_by_id(benchmark, "BC-01")

    valid_blocking = BlockingCalibrationResult(
        disposition="BLOCKING_REQUIRED",
        blocking_requirement_id="feature-x-availability-confirmed",
        blocked_scope_id="defend-live-scoring-validity",
        rationale="The active defended scope explicitly depends on the supplied unresolved requirement.",
    )
    validate_result_for_pair(pair, valid_blocking)

    with pytest.raises(ValueError, match="supplied requirement"):
        validate_result_for_pair(
            pair,
            BlockingCalibrationResult(
                disposition="BLOCKING_REQUIRED",
                blocking_requirement_id="invented-requirement",
                blocked_scope_id="defend-live-scoring-validity",
                rationale="Invalid requirement pointer.",
            ),
        )

    with pytest.raises(ValueError, match="supplied downstream scope"):
        validate_result_for_pair(
            pair,
            BlockingCalibrationResult(
                disposition="BLOCKING_REQUIRED",
                blocking_requirement_id="feature-x-availability-confirmed",
                blocked_scope_id="invented-scope",
                rationale="Invalid scope pointer.",
            ),
        )

    with pytest.raises(ValueError, match="RECOMMENDED"):
        validate_result_for_pair(
            pair,
            BlockingCalibrationResult(
                disposition="RECOMMENDED",
                blocking_requirement_id="feature-x-availability-confirmed",
                blocked_scope_id=None,
                rationale="A recommended output cannot carry a blocking requirement.",
            ),
        )

    with pytest.raises(ValueError, match="unsupported disposition"):
        BlockingCalibrationResult(
            disposition="DEFER",
            blocking_requirement_id=None,
            blocked_scope_id=None,
            rationale="Outside this diagnostic taxonomy.",
        )


def test_perfect_fake_result_supports_boundary() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(benchmark, observations)

    assert evaluation.completed is True
    assert evaluation.all_hard_gates_passed is True
    assert evaluation.outcome is DiagnosticOutcome.SUPPORTED
    assert evaluation.aggregate_exact_disposition_accuracy == 1.0
    assert evaluation.expected_blocking_requirement_pointer_accuracy == 1.0
    assert evaluation.expected_blocked_scope_pointer_accuracy == 1.0
    assert evaluation.expected_blocking_joint_pointer_accuracy == 1.0
    assert evaluation.expected_recommended_null_pointer_correctness == 1.0
    assert all(value == 3 for value in evaluation.correct_repetitions_by_variant.values())


def test_single_recommended_miss_fails_strict_null_pointer_side_gate() -> None:
    benchmark, observations = _perfect_observations()
    target_index = next(
        index
        for index, observation in enumerate(observations)
        if variant_by_id(
            pair_by_id(benchmark, observation.pair_id), observation.variant_id
        ).expected_disposition
        is BlockingDisposition.RECOMMENDED
    )
    target = observations[target_index]
    pair = pair_by_id(benchmark, target.pair_id)
    observations[target_index] = BlockingObservation(
        pair_id=target.pair_id,
        variant_id=target.variant_id,
        repetition=target.repetition,
        result=BlockingCalibrationResult(
            disposition="BLOCKING_REQUIRED",
            blocking_requirement_id=pair.requirements[0].requirement_id,
            blocked_scope_id=pair.downstream_scopes[0].scope_id,
            rationale="Deliberate provider-free miss for strict gate testing.",
        ),
    )

    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.aggregate_exact_disposition_accuracy > 0.95
    assert evaluation.aggregate_accuracy_passed is True
    assert evaluation.variant_majority_passed is True
    assert evaluation.pair_polarity_passed is True
    assert evaluation.recommended_null_pointer_passed is False
    assert evaluation.outcome is DiagnosticOutcome.NOT_SUPPORTED


def test_single_blocking_pointer_miss_is_rejected_before_gate_scoring() -> None:
    benchmark = _benchmark()
    pair = pair_by_id(benchmark, "BC-01")
    with pytest.raises(ValueError, match="supplied requirement"):
        validate_result_for_pair(
            pair,
            BlockingCalibrationResult(
                disposition="BLOCKING_REQUIRED",
                blocking_requirement_id="not-supplied",
                blocked_scope_id="defend-live-scoring-validity",
                rationale="Deliberate invalid structured output.",
            ),
        )


def test_incomplete_observation_set_returns_incomplete() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(
        benchmark,
        observations[:-1],
        execution_complete=False,
    )
    assert evaluation.completed is False
    assert evaluation.outcome is DiagnosticOutcome.INCOMPLETE
