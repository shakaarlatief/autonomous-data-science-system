from __future__ import annotations

from dataclasses import replace
import json
from pathlib import Path

import pytest

from ads_system.application.reasoning import KnowledgeRevisionPointer
from experiments.system_owned_provenance_recommendation_action_value.harness import (
    AdvancementOutcome,
    JudgeObligationScore,
    JudgeResult,
    RecommendationCondition,
    RecommendationConditionInput,
    RecommendationMetrics,
    RecommendationScoredObservation,
    SystemProvenanceActionDecision,
    SystemProvenanceRecommendationActionResult,
    build_judge_payload,
    build_judge_plan,
    build_reasoning_plan,
    build_reasoning_request,
    build_system_provenance_plan,
    case_by_id,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    serialize_judge_plan,
    serialize_reasoning_plan,
    serialize_system_provenance_plan,
    validate_system_provenance_result,
)


FIXTURE = Path(
    "tests/fixtures/reasoning/system_owned_provenance_recommendation_action_v1.json"
)
BASE_FIXTURE = Path(
    "tests/fixtures/reasoning/relation_backed_recommendation_action_v1.json"
)


def _benchmark():
    return load_frozen_benchmark(FIXTURE)


def _perfect_result(case):
    return SystemProvenanceRecommendationActionResult(
        summary="The supplied project state is classified under the frozen action menu.",
        action_decisions=tuple(
            SystemProvenanceActionDecision(
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
                ),
                judge_result=_perfect_judge(case, entry.output_id),
            )
        )
    return benchmark, observations


def test_overlay_loader_locks_base_fixture_and_applies_only_frozen_delta() -> None:
    benchmark = _benchmark()
    assert benchmark.benchmark_id == (
        "v1-system-owned-provenance-recommendation-action-value-v0.1"
    )
    assert benchmark.randomization_seed == 2026082304
    assert benchmark.starting_merge_sha == "ecf37585f576a3c4fd84a884dee4650b52ab1519"
    assert len(benchmark.cases) == 4
    assert "methodological_basis" not in benchmark.common_reasoner_instruction
    assert "system records supplied context provenance separately" in (
        benchmark.common_reasoner_instruction
    )

    base = json.loads(BASE_FIXTURE.read_text(encoding="utf-8"))
    for effective_case, base_case in zip(benchmark.cases, base["cases"], strict=True):
        assert effective_case.case_id == base_case["case_id"]
        assert dict(effective_case.project_evidence) == base_case["project_evidence"]
        assert [item.action_id for item in effective_case.candidate_actions] == [
            item["action_id"] for item in base_case["candidate_actions"]
        ]
        assert [item.expected_disposition.value for item in effective_case.candidate_actions] == [
            item["expected_disposition"] for item in base_case["candidate_actions"]
        ]
        assert [item.expected_defer_until_id for item in effective_case.candidate_actions] == [
            item["expected_defer_until_id"] for item in base_case["candidate_actions"]
        ]
        assert effective_case.expected_blocked_scopes == tuple(
            base_case["expected_blocked_scopes"]
        )
        assert effective_case.expected_required_clarification_ids == tuple(
            base_case["expected_required_clarification_ids"]
        )


def test_overlay_loader_fails_closed_when_locked_base_blob_drifts(tmp_path) -> None:
    overlay = json.loads(FIXTURE.read_text(encoding="utf-8"))
    altered_base = tmp_path / "altered-base.json"
    altered_base.write_text(BASE_FIXTURE.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    overlay["base_fixture"] = str(altered_base.resolve())
    altered_overlay = tmp_path / "overlay.json"
    altered_overlay.write_text(json.dumps(overlay), encoding="utf-8")

    with pytest.raises(ValueError, match="base fixture Git blob drifted"):
        load_frozen_benchmark(altered_overlay)


def test_reasoner_and_judge_plans_are_deterministic_under_new_seed() -> None:
    benchmark = _benchmark()
    plan_1 = build_reasoning_plan(benchmark)
    plan_2 = build_reasoning_plan(benchmark)
    assert plan_1 == plan_2
    assert len(plan_1) == 36
    assert len({item.output_id for item in plan_1}) == 36
    assert all(item.output_id.startswith("spra-") for item in plan_1)
    assert serialize_reasoning_plan(plan_1) == serialize_reasoning_plan(plan_2)

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


def test_model_owned_result_has_no_methodological_provenance_field() -> None:
    fields = set(SystemProvenanceRecommendationActionResult.__dataclass_fields__)
    assert "methodological_basis" not in fields
    result = _perfect_result(case_by_id(_benchmark(), "RB-01"))
    assert "methodological_basis" not in result.to_payload()


def test_reasoner_request_uses_system_context_but_model_schema_has_no_provenance() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-01")
    entry = next(
        item
        for item in build_reasoning_plan(benchmark)
        if item.case_id == case.case_id
        and item.condition is RecommendationCondition.GENERIC
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
    assert request.structured_output_type is SystemProvenanceRecommendationActionResult
    assert request.knowledge_revisions == ()
    assert request.methodological_context_sha256 == context.provenance.methodology_payload_sha256
    model_input = request.canonical_model_input()
    assert "methodological_basis" not in model_input
    assert "expected_disposition" not in model_input


def test_system_provenance_plan_is_deterministic_and_condition_exact() -> None:
    benchmark = _benchmark()
    reasoning_plan = build_reasoning_plan(benchmark)
    contexts = {}
    for case in benchmark.cases:
        for condition in RecommendationCondition:
            if condition is RecommendationCondition.GENERIC:
                revisions = ()
                payload = {}
                digest = "44136fa355b3678a1146ad16f7e8649e94fb4fc21fe77e8310c060f61caaff8a"
                size = 2
            elif condition is RecommendationCondition.SELECTIVE:
                revisions = tuple(
                    KnowledgeRevisionPointer(stable_key=key, revision_id=f"rev-{key}")
                    for key in case.required_selective_keys
                )
                payload = {"condition": "selective", "case": case.case_id}
                encoded = json.dumps(
                    payload, sort_keys=True, separators=(",", ":")
                ).encode("utf-8")
                import hashlib
                digest = hashlib.sha256(encoded).hexdigest()
                size = len(encoded)
            else:
                revisions = tuple(
                    KnowledgeRevisionPointer(stable_key=f"asset-{index}", revision_id=f"rev-{index}")
                    for index in range(10)
                )
                payload = {"condition": "full", "case": case.case_id}
                encoded = json.dumps(
                    payload, sort_keys=True, separators=(",", ":")
                ).encode("utf-8")
                import hashlib
                digest = hashlib.sha256(encoded).hexdigest()
                size = len(encoded)
            contexts[(case.case_id, condition)] = RecommendationConditionInput(
                condition=condition,
                payload=payload,
                sha256=digest,
                utf8_bytes=size,
                revisions=revisions,
            )

    plan_1 = build_system_provenance_plan(reasoning_plan, contexts)
    plan_2 = build_system_provenance_plan(reasoning_plan, contexts)
    assert plan_1 == plan_2
    assert len(plan_1) == 36
    assert serialize_system_provenance_plan(plan_1) == serialize_system_provenance_plan(plan_2)
    by_output = {item.output_id: item for item in plan_1}
    for reasoner_entry in reasoning_plan:
        record = by_output[reasoner_entry.output_id]
        expected = contexts[(reasoner_entry.case_id, reasoner_entry.condition)].provenance
        assert record.provenance == expected
        if reasoner_entry.condition is RecommendationCondition.GENERIC:
            assert record.provenance.supplied_revisions == ()
        elif reasoner_entry.condition is RecommendationCondition.FULL_HORIZON:
            assert len(record.provenance.supplied_revisions) == 10


def test_result_validator_enforces_action_and_defer_pointer_contract_without_basis() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-02")
    result = _perfect_result(case)
    assert validate_system_provenance_result(case, result) is result

    decisions = list(result.action_decisions)
    deferred_index = next(
        index for index, item in enumerate(decisions) if item.disposition == "DEFER"
    )
    decisions[deferred_index] = replace(decisions[deferred_index], defer_until_id=None)
    invalid = replace(result, action_decisions=tuple(decisions))
    with pytest.raises(ValueError, match="DEFER must point"):
        validate_system_provenance_result(case, invalid)


def test_exact_metrics_remain_scientific_truth_metrics_only() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-01")
    metrics = evaluate_recommendation_result(case, _perfect_result(case))
    assert metrics.exact_disposition_accuracy == 1.0
    assert metrics.defer_pointer_errors == 0
    assert metrics.critical_action_omissions == 0
    assert metrics.blocking_scope_false_negatives == 0
    assert metrics.required_clarification_false_negatives == 0
    assert "unsupported_methodological_basis_failures" not in metrics.__dataclass_fields__


def test_judge_payload_is_blinded_to_condition_context_provenance_usage_and_truth() -> None:
    benchmark = _benchmark()
    case = case_by_id(benchmark, "RB-04")
    payload = build_judge_payload(
        case,
        output_id="opaque-output",
        result=_perfect_result(case),
    ).to_payload()
    text = json.dumps(payload, sort_keys=True)
    for forbidden in (
        "SELECTIVE",
        "FULL_HORIZON",
        "methodological_context",
        "system_context_provenance",
        "methodology_payload_sha256",
        "expected_disposition",
        "input_tokens",
        "methodological_basis",
    ):
        assert forbidden not in text


def test_perfect_ceiling_is_safe_but_not_differentiated() -> None:
    benchmark, observations = _perfect_observations()
    evaluation = evaluate_gates(benchmark, observations)
    assert evaluation.absolute_passed
    assert evaluation.relative_passed
    assert evaluation.expansion_passed
    assert evaluation.value_signals == ()
    assert evaluation.outcome is AdvancementOutcome.SAFE_NOT_DIFFERENTIATED


def test_preregistered_generic_gap_can_promote_when_safety_gates_pass() -> None:
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
    assert not evaluation.gate_results["SPRA-G03"]
    assert evaluation.outcome is AdvancementOutcome.FAIL
