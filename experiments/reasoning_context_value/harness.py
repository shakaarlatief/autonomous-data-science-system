"""Framework-neutral harness for the frozen Specification 014 experiment.

This module owns experiment semantics: frozen task/rubric loading, deterministic
randomization, context-condition construction, request construction, blinded
judge contracts, and gate calculations. Provider/framework execution remains
behind separate adapters.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
import hashlib
import json
from pathlib import Path
import random
from typing import Any, Mapping, Sequence

from ads_system.application.context_models import (
    MethodologicalContextPack,
    MethodologicalContextRequest,
    SelectedContextKnowledge,
)
from ads_system.application.context_selection import (
    methodological_context_pack_payload,
    select_methodological_context,
    serialize_methodological_context_pack,
)
from ads_system.application.horizon_models import MethodologicalHorizon
from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningModelConfiguration,
    ReasoningRequest,
)


class ContextCondition(StrEnum):
    SELECTIVE = "SELECTIVE"
    FULL_HORIZON = "FULL_HORIZON"


@dataclass(frozen=True, slots=True)
class RubricObligation:
    obligation_id: str
    critical: bool
    description: str


@dataclass(frozen=True, slots=True)
class ReasoningExperimentCase:
    case_id: str
    source_case_id: str
    task_id: str
    requested_reasoning_functions: tuple[str, ...]
    project_evidence: Mapping[str, object]
    user_task: str
    required_selective_keys: tuple[str, ...]
    allowed_additional_basis_keys: tuple[str, ...]
    rubric: tuple[RubricObligation, ...]


@dataclass(frozen=True, slots=True)
class ReasoningPlanEntry:
    run_id: str
    run_nonce: str
    case_id: str
    repetition: int
    condition: ContextCondition


@dataclass(frozen=True, slots=True)
class JudgePlanEntry:
    judge_id: str
    output_id: str


@dataclass(frozen=True, slots=True)
class FrozenReasoningBenchmark:
    benchmark_id: str
    randomization_seed: int
    repetitions: int
    common_reasoner_instruction: str
    reasoner_model: ReasoningModelConfiguration
    judge_model: ReasoningModelConfiguration
    quality_gate: Mapping[str, object]
    efficiency_gate: Mapping[str, object]
    call_plan: Mapping[str, object]
    cases: tuple[ReasoningExperimentCase, ...]


@dataclass(frozen=True, slots=True)
class ContextConditionInput:
    condition: ContextCondition
    pack: MethodologicalContextPack
    payload: Mapping[str, object]
    sha256: str
    utf8_bytes: int
    revisions: tuple[KnowledgeRevisionPointer, ...]


@dataclass(frozen=True, slots=True)
class JudgeObligationScore:
    obligation_id: str
    score: int
    rationale: str

    def __post_init__(self) -> None:
        if self.score not in {0, 1, 2}:
            raise ValueError("judge obligation score must be 0, 1, or 2")
        if not self.rationale.strip():
            raise ValueError("judge obligation rationale must be non-empty")


@dataclass(frozen=True, slots=True)
class JudgeResult:
    output_id: str
    obligation_scores: tuple[JudgeObligationScore, ...]
    normalized_score: float
    critical_failure: bool
    judge_summary: str

    def __post_init__(self) -> None:
        if not self.output_id.strip():
            raise ValueError("output_id must be non-empty")
        if not self.obligation_scores:
            raise ValueError("obligation_scores must be non-empty")
        if not 0.0 <= self.normalized_score <= 1.0:
            raise ValueError("normalized_score must be between 0 and 1")
        if not self.judge_summary.strip():
            raise ValueError("judge_summary must be non-empty")


@dataclass(frozen=True, slots=True)
class ReasoningScoredObservation:
    case_id: str
    condition: ContextCondition
    repetition: int
    judge_result: JudgeResult
    input_tokens: int


@dataclass(frozen=True, slots=True)
class GateEvaluation:
    quality_passed: bool
    efficiency_passed: bool
    aggregate_selective_quality: float
    aggregate_full_quality: float
    per_case_quality: Mapping[str, Mapping[str, float]]
    critical_regressions: tuple[str, ...]
    aggregate_input_token_ratio: float
    per_case_input_token_ratios: Mapping[str, float]
    matched_pair_token_failures: tuple[str, ...]


CONTROL_INCLUDED = "CONTROL_INCLUDED"


def load_frozen_benchmark(path: Path) -> FrozenReasoningBenchmark:
    raw = json.loads(path.read_text(encoding="utf-8"))
    cases = tuple(_load_case(item) for item in raw["cases"])
    _validate_unique_case_ids(cases)

    reasoner = raw["reasoner"]
    judge = raw["judge"]
    return FrozenReasoningBenchmark(
        benchmark_id=str(raw["benchmark_id"]),
        randomization_seed=int(raw["randomization_seed"]),
        repetitions=int(raw["reasoner_repetitions_per_condition"]),
        common_reasoner_instruction=str(raw["common_reasoner_instruction"]),
        reasoner_model=ReasoningModelConfiguration(
            requested_model=str(reasoner["model"]),
            reasoning_effort=str(reasoner["reasoning_effort"]),
            verbosity=str(reasoner["text_verbosity"]),
            max_output_tokens=int(reasoner["max_output_tokens"]),
            store=False,
        ),
        judge_model=ReasoningModelConfiguration(
            requested_model=str(judge["model"]),
            reasoning_effort=str(judge["reasoning_effort"]),
            verbosity=str(judge["text_verbosity"]),
            max_output_tokens=int(judge["max_output_tokens"]),
            store=False,
        ),
        quality_gate=dict(raw["quality_gate"]),
        efficiency_gate=dict(raw["efficiency_gate"]),
        call_plan=dict(raw["call_plan"]),
        cases=cases,
    )


def build_reasoning_plan(benchmark: FrozenReasoningBenchmark) -> tuple[ReasoningPlanEntry, ...]:
    """Generate the frozen matched-pair plan deterministically from the seed."""

    rng = random.Random(benchmark.randomization_seed)
    entries: list[ReasoningPlanEntry] = []
    ordinal = 0
    for case in benchmark.cases:
        for repetition in range(1, benchmark.repetitions + 1):
            pair = [ContextCondition.SELECTIVE, ContextCondition.FULL_HORIZON]
            rng.shuffle(pair)
            for condition in pair:
                ordinal += 1
                opaque = hashlib.sha256(
                    (
                        f"{benchmark.benchmark_id}|{benchmark.randomization_seed}|"
                        f"{ordinal}|{case.case_id}|{repetition}|{condition.value}"
                    ).encode("utf-8")
                ).hexdigest()
                entries.append(
                    ReasoningPlanEntry(
                        run_id=f"rv-{opaque[:16]}",
                        run_nonce=f"nonce-{opaque[16:40]}",
                        case_id=case.case_id,
                        repetition=repetition,
                        condition=condition,
                    )
                )
    return tuple(entries)


def build_judge_plan(
    output_ids: Sequence[str],
    *,
    randomization_seed: int,
) -> tuple[JudgePlanEntry, ...]:
    """Independently shuffle judge order without exposing context conditions."""

    unique_ids = list(output_ids)
    if len(unique_ids) != len(set(unique_ids)):
        raise ValueError("output_ids must be unique")
    rng = random.Random(randomization_seed ^ 0x5A17C0DE)
    rng.shuffle(unique_ids)
    return tuple(
        JudgePlanEntry(
            judge_id="judge-" + hashlib.sha256(
                f"{randomization_seed}|{position}|{output_id}".encode("utf-8")
            ).hexdigest()[:16],
            output_id=output_id,
        )
        for position, output_id in enumerate(unique_ids, start=1)
    )


def serialize_reasoning_plan(plan: Sequence[ReasoningPlanEntry]) -> tuple[str, str]:
    payload = [
        {
            "case_id": item.case_id,
            "condition": item.condition.value,
            "repetition": item.repetition,
            "run_id": item.run_id,
            "run_nonce": item.run_nonce,
        }
        for item in plan
    ]
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_full_horizon_pack(
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> MethodologicalContextPack:
    """Materialize all included Horizon candidates through the compact projection."""

    items: list[SelectedContextKnowledge] = []
    with uow_factory() as uow:
        for candidate in horizon.included:
            asset = uow.navigation.get_context_asset(candidate.stable_key, candidate.revision_id)
            if asset is None:
                raise ValueError(
                    f"FULL_HORIZON candidate {candidate.stable_key!r} is no longer current accepted"
                )
            items.append(
                SelectedContextKnowledge(
                    asset=asset,
                    selection_reason=CONTROL_INCLUDED,
                    origin=candidate.origin,
                    applicability_state=candidate.applicability_state,
                    missing_context_keys=candidate.missing_context_keys,
                    relation_source_key=candidate.relation_source_key,
                    relation_type=candidate.relation_type,
                    relation_revision_id=candidate.relation_revision_id,
                )
            )

    aggregate_missing = tuple(sorted({key for item in items for key in item.missing_context_keys}))
    return MethodologicalContextPack(
        schema_version=1,
        task_id=request.task_id,
        requested_reasoning_functions=tuple(sorted(request.requested_reasoning_functions)),
        knowledge=tuple(items),
        missing_context_keys=aggregate_missing,
    )


def build_context_condition_input(
    condition: ContextCondition,
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> ContextConditionInput:
    if condition is ContextCondition.SELECTIVE:
        pack = select_methodological_context(
            horizon,
            request,
            uow_factory=uow_factory,
        ).pack
    elif condition is ContextCondition.FULL_HORIZON:
        pack = build_full_horizon_pack(horizon, request, uow_factory=uow_factory)
    else:
        raise ValueError(f"unsupported context condition: {condition!r}")

    serialized = serialize_methodological_context_pack(pack)
    revisions = tuple(
        KnowledgeRevisionPointer(
            stable_key=item.asset.stable_key,
            revision_id=item.asset.revision_id,
        )
        for item in pack.knowledge
    )
    return ContextConditionInput(
        condition=condition,
        pack=pack,
        payload=methodological_context_pack_payload(pack),
        sha256=serialized.sha256,
        utf8_bytes=serialized.utf8_bytes,
        revisions=revisions,
    )


def build_reasoning_request(
    *,
    benchmark: FrozenReasoningBenchmark,
    case: ReasoningExperimentCase,
    plan_entry: ReasoningPlanEntry,
    context: ContextConditionInput,
) -> ReasoningRequest:
    if plan_entry.case_id != case.case_id:
        raise ValueError("plan entry case does not match reasoning case")
    if plan_entry.condition is not context.condition:
        raise ValueError("plan entry condition does not match context condition")
    return ReasoningRequest(
        run_id=plan_entry.run_id,
        run_nonce=plan_entry.run_nonce,
        system_instruction=benchmark.common_reasoner_instruction,
        user_task=case.user_task,
        project_evidence=case.project_evidence,
        methodological_context_payload=context.payload,
        methodological_context_sha256=context.sha256,
        knowledge_revisions=context.revisions,
        model_configuration=benchmark.reasoner_model,
    )


def validate_frozen_context_sets(
    benchmark: FrozenReasoningBenchmark,
    horizon: MethodologicalHorizon,
    *,
    max_assets: int,
    uow_factory,
) -> None:
    """Fail before live calls if accepted SELECTIVE/FULL conditions drifted."""

    if len(horizon.included) != 10:
        raise ValueError(f"frozen FULL_HORIZON requires 10 included assets, observed {len(horizon.included)}")
    for case in benchmark.cases:
        request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=max_assets,
        )
        selective = build_context_condition_input(
            ContextCondition.SELECTIVE,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        observed = {item.stable_key for item in selective.revisions}
        expected = set(case.required_selective_keys)
        if observed != expected:
            raise ValueError(
                f"{case.case_id} SELECTIVE set drifted: expected {sorted(expected)}, observed {sorted(observed)}"
            )
        full = build_context_condition_input(
            ContextCondition.FULL_HORIZON,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        if len(full.revisions) != 10:
            raise ValueError(f"{case.case_id} FULL_HORIZON does not contain 10 revisions")
        if selective.utf8_bytes >= full.utf8_bytes:
            raise ValueError(f"{case.case_id} selective context is not smaller than full control")


def validate_judge_result(case: ReasoningExperimentCase, result: JudgeResult) -> JudgeResult:
    expected_ids = [item.obligation_id for item in case.rubric]
    observed_ids = [item.obligation_id for item in result.obligation_scores]
    if observed_ids != expected_ids:
        raise ValueError(
            f"judge obligation IDs/order do not match frozen rubric for {case.case_id}: "
            f"expected {expected_ids}, observed {observed_ids}"
        )
    recomputed = sum(item.score for item in result.obligation_scores) / (2 * len(result.obligation_scores))
    if abs(recomputed - result.normalized_score) > 1e-9:
        raise ValueError(
            f"judge normalized score is inconsistent: reported {result.normalized_score}, recomputed {recomputed}"
        )
    critical_ids = {item.obligation_id for item in case.rubric if item.critical}
    recomputed_critical_failure = any(
        item.obligation_id in critical_ids and item.score == 0
        for item in result.obligation_scores
    )
    if recomputed_critical_failure != result.critical_failure:
        raise ValueError("judge critical_failure is inconsistent with frozen rubric scores")
    return result


def evaluate_gates(
    benchmark: FrozenReasoningBenchmark,
    observations: Sequence[ReasoningScoredObservation],
) -> GateEvaluation:
    """Evaluate the preregistered quality and input-token gates."""

    expected_count = len(benchmark.cases) * 2 * benchmark.repetitions
    if len(observations) != expected_count:
        raise ValueError(
            f"gate evaluation requires {expected_count} scored observations, observed {len(observations)}"
        )

    by_key: dict[tuple[str, ContextCondition, int], ReasoningScoredObservation] = {}
    for observation in observations:
        key = (observation.case_id, observation.condition, observation.repetition)
        if key in by_key:
            raise ValueError(f"duplicate scored observation: {key}")
        by_key[key] = observation

    selective_scores: list[float] = []
    full_scores: list[float] = []
    selective_tokens: list[int] = []
    full_tokens: list[int] = []
    per_case_quality: dict[str, dict[str, float]] = {}
    per_case_ratios: dict[str, float] = {}
    pair_failures: list[str] = []

    for case in benchmark.cases:
        s_case: list[ReasoningScoredObservation] = []
        f_case: list[ReasoningScoredObservation] = []
        for repetition in range(1, benchmark.repetitions + 1):
            s = by_key[(case.case_id, ContextCondition.SELECTIVE, repetition)]
            f = by_key[(case.case_id, ContextCondition.FULL_HORIZON, repetition)]
            s_case.append(s)
            f_case.append(f)
            if s.input_tokens >= f.input_tokens:
                pair_failures.append(f"{case.case_id}/rep-{repetition}")

        s_quality = _mean(item.judge_result.normalized_score for item in s_case)
        f_quality = _mean(item.judge_result.normalized_score for item in f_case)
        per_case_quality[case.case_id] = {
            ContextCondition.SELECTIVE.value: s_quality,
            ContextCondition.FULL_HORIZON.value: f_quality,
            "difference": s_quality - f_quality,
        }
        s_tokens_mean = _mean(float(item.input_tokens) for item in s_case)
        f_tokens_mean = _mean(float(item.input_tokens) for item in f_case)
        per_case_ratios[case.case_id] = s_tokens_mean / f_tokens_mean
        selective_scores.extend(item.judge_result.normalized_score for item in s_case)
        full_scores.extend(item.judge_result.normalized_score for item in f_case)
        selective_tokens.extend(item.input_tokens for item in s_case)
        full_tokens.extend(item.input_tokens for item in f_case)

    aggregate_s = _mean(selective_scores)
    aggregate_f = _mean(full_scores)
    quality_floor = float(benchmark.quality_gate["aggregate_selective_minus_full_floor"])
    case_floor = float(benchmark.quality_gate["per_case_selective_minus_full_floor"])

    critical_regressions = _critical_regressions(benchmark, by_key)
    quality_passed = (
        aggregate_s >= aggregate_f + quality_floor
        and all(values["difference"] >= case_floor for values in per_case_quality.values())
        and not critical_regressions
    )

    aggregate_ratio = _mean(float(value) for value in selective_tokens) / _mean(
        float(value) for value in full_tokens
    )
    max_case_ratio = float(
        benchmark.efficiency_gate["max_mean_selective_to_full_input_token_ratio_per_case"]
    )
    max_aggregate_ratio = float(
        benchmark.efficiency_gate["max_aggregate_selective_to_full_input_token_ratio"]
    )
    efficiency_passed = (
        not pair_failures
        and all(value <= max_case_ratio for value in per_case_ratios.values())
        and aggregate_ratio <= max_aggregate_ratio
    )

    return GateEvaluation(
        quality_passed=quality_passed,
        efficiency_passed=efficiency_passed,
        aggregate_selective_quality=aggregate_s,
        aggregate_full_quality=aggregate_f,
        per_case_quality=per_case_quality,
        critical_regressions=tuple(critical_regressions),
        aggregate_input_token_ratio=aggregate_ratio,
        per_case_input_token_ratios=per_case_ratios,
        matched_pair_token_failures=tuple(pair_failures),
    )


def judge_payload(
    case: ReasoningExperimentCase,
    *,
    output_id: str,
    candidate_result: Mapping[str, object],
) -> dict[str, object]:
    """Build a condition-blinded payload for semantic judging."""

    return {
        "output_id": output_id,
        "user_task": case.user_task,
        "project_evidence": dict(case.project_evidence),
        "rubric": [asdict(item) for item in case.rubric],
        "candidate_result": dict(candidate_result),
        "score_definitions": {
            "0": "Absent, materially wrong, or contradicted.",
            "1": "Partially or implicitly satisfied without a material contradiction.",
            "2": "Explicitly and correctly satisfied.",
        },
        "judge_may_add_obligations": False,
    }


def _load_case(raw: Mapping[str, Any]) -> ReasoningExperimentCase:
    rubric = tuple(
        RubricObligation(
            obligation_id=str(item["obligation_id"]),
            critical=bool(item["critical"]),
            description=str(item["description"]),
        )
        for item in raw["rubric"]
    )
    if not rubric:
        raise ValueError("each reasoning case must contain at least one rubric obligation")
    obligation_ids = [item.obligation_id for item in rubric]
    if len(obligation_ids) != len(set(obligation_ids)):
        raise ValueError("rubric obligation IDs must be unique within a case")
    return ReasoningExperimentCase(
        case_id=str(raw["case_id"]),
        source_case_id=str(raw["source_case_id"]),
        task_id=str(raw["task_id"]),
        requested_reasoning_functions=tuple(str(value) for value in raw["requested_reasoning_functions"]),
        project_evidence=dict(raw["project_evidence"]),
        user_task=str(raw["user_task"]),
        required_selective_keys=tuple(str(value) for value in raw["required_selective_keys"]),
        allowed_additional_basis_keys=tuple(str(value) for value in raw["allowed_additional_basis_keys"]),
        rubric=rubric,
    )


def _validate_unique_case_ids(cases: Sequence[ReasoningExperimentCase]) -> None:
    ids = [case.case_id for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("reasoning case IDs must be unique")


def _critical_regressions(
    benchmark: FrozenReasoningBenchmark,
    by_key: Mapping[tuple[str, ContextCondition, int], ReasoningScoredObservation],
) -> list[str]:
    required_count = int(benchmark.quality_gate["critical_obligation_repetitions_required"])
    satisfaction_floor = int(benchmark.quality_gate["obligation_satisfied_score_floor"])
    regressions: list[str] = []
    for case in benchmark.cases:
        critical_ids = [item.obligation_id for item in case.rubric if item.critical]
        for obligation_id in critical_ids:
            full_count = 0
            selective_count = 0
            for repetition in range(1, benchmark.repetitions + 1):
                for condition, target in (
                    (ContextCondition.FULL_HORIZON, "full"),
                    (ContextCondition.SELECTIVE, "selective"),
                ):
                    observation = by_key[(case.case_id, condition, repetition)]
                    score = next(
                        item.score
                        for item in observation.judge_result.obligation_scores
                        if item.obligation_id == obligation_id
                    )
                    if score >= satisfaction_floor:
                        if target == "full":
                            full_count += 1
                        else:
                            selective_count += 1
            if full_count >= required_count and selective_count < required_count:
                regressions.append(
                    f"{case.case_id}/{obligation_id}: full={full_count}, selective={selective_count}"
                )
    return regressions


def _mean(values: Sequence[float] | Any) -> float:
    realized = list(values)
    if not realized:
        raise ValueError("cannot compute mean of an empty sequence")
    return sum(realized) / len(realized)
