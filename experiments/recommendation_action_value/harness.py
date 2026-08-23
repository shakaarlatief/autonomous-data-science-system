"""Framework-neutral harness for frozen Specification 015.

This module owns recommendation/action experiment semantics rather than provider
execution. It loads the preregistered benchmark, constructs the three context
conditions, creates deterministic reasoner/judge plans, builds ADS-owned
requests, computes exact recommendation metrics, validates blinded judge
results, and applies the frozen three-way advancement rule.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
import hashlib
import json
from pathlib import Path
import random
from typing import Mapping, Sequence

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
from ads_system.application.recommendation import (
    RecommendationActionResult,
    RecommendationDisposition,
    validate_recommendation_action_result,
)
from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningModelConfiguration,
    ReasoningOutputKind,
    ReasoningRequest,
    validate_methodological_basis,
)


class RecommendationCondition(StrEnum):
    GENERIC = "GENERIC"
    SELECTIVE = "SELECTIVE"
    FULL_HORIZON = "FULL_HORIZON"


class AdvancementOutcome(StrEnum):
    PROMOTE_BOUNDED_RECOMMENDATION_SEAM = "PROMOTE_BOUNDED_RECOMMENDATION_SEAM"
    SAFE_BUT_NOT_DIFFERENTIATED = "SAFE_BUT_NOT_DIFFERENTIATED"
    FAIL = "FAIL"


@dataclass(frozen=True, slots=True)
class CandidateAction:
    action_id: str
    label: str
    cost_units: int
    expected_disposition: RecommendationDisposition
    critical: bool


@dataclass(frozen=True, slots=True)
class ClarificationOption:
    clarification_id: str
    description: str


@dataclass(frozen=True, slots=True)
class RubricObligation:
    obligation_id: str
    critical: bool
    description: str


@dataclass(frozen=True, slots=True)
class RecommendationExperimentCase:
    case_id: str
    case_class: str
    source_case_id: str
    task_id: str
    requested_reasoning_functions: tuple[str, ...]
    required_selective_keys: tuple[str, ...]
    allowed_additional_basis_keys: tuple[str, ...]
    project_evidence: Mapping[str, object]
    user_task: str
    available_blocked_scopes: tuple[str, ...]
    expected_blocked_scopes: tuple[str, ...]
    available_clarifications: tuple[ClarificationOption, ...]
    expected_required_clarification_ids: tuple[str, ...]
    candidate_actions: tuple[CandidateAction, ...]
    rubric: tuple[RubricObligation, ...]

    @property
    def candidate_action_ids(self) -> tuple[str, ...]:
        return tuple(action.action_id for action in self.candidate_actions)

    @property
    def allowed_clarification_ids(self) -> tuple[str, ...]:
        return tuple(item.clarification_id for item in self.available_clarifications)

    def model_task_payload(self) -> dict[str, object]:
        """Return the condition-invariant model-facing task menu.

        Evaluator truth such as expected dispositions, critical flags, expected
        blocked scopes, expected clarifications, and semantic rubric is omitted.
        """

        return {
            "requested_reasoning_functions": list(self.requested_reasoning_functions),
            "candidate_actions": [
                {
                    "action_id": action.action_id,
                    "label": action.label,
                    "cost_units": action.cost_units,
                }
                for action in self.candidate_actions
            ],
            "available_blocked_scopes": list(self.available_blocked_scopes),
            "available_clarifications": [
                {
                    "clarification_id": item.clarification_id,
                    "description": item.description,
                }
                for item in self.available_clarifications
            ],
        }


@dataclass(frozen=True, slots=True)
class FrozenRecommendationBenchmark:
    benchmark_id: str
    randomization_seed: int
    repetitions: int
    common_reasoner_instruction: str
    reasoner_model: ReasoningModelConfiguration
    judge_model: ReasoningModelConfiguration
    absolute_gate: Mapping[str, object]
    relative_gate: Mapping[str, object]
    expansion_gate: Mapping[str, object]
    promotion_value_signals: Mapping[str, object]
    call_plan: Mapping[str, object]
    cases: tuple[RecommendationExperimentCase, ...]


@dataclass(frozen=True, slots=True)
class RecommendationPlanEntry:
    output_id: str
    run_nonce: str
    case_id: str
    repetition: int
    condition: RecommendationCondition


@dataclass(frozen=True, slots=True)
class JudgePlanEntry:
    judge_id: str
    output_id: str


@dataclass(frozen=True, slots=True)
class RecommendationConditionInput:
    condition: RecommendationCondition
    payload: Mapping[str, object]
    sha256: str
    utf8_bytes: int
    revisions: tuple[KnowledgeRevisionPointer, ...]
    pack: MethodologicalContextPack | None = None


@dataclass(frozen=True, slots=True)
class RecommendationMetrics:
    exact_disposition_accuracy: float
    critical_action_omissions: int
    under_recommendations: int
    over_recommendations: int
    unnecessary_recommended_cost: int
    blocking_scope_false_negatives: int
    blocking_scope_false_positives: int
    required_clarification_false_negatives: int
    unsupported_methodological_basis: int


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
class RecommendationScoredObservation:
    output_id: str
    case_id: str
    condition: RecommendationCondition
    repetition: int
    metrics: RecommendationMetrics
    judge_result: JudgeResult


@dataclass(frozen=True, slots=True)
class ConditionAggregate:
    exact_disposition_accuracy: float
    semantic_score: float
    critical_action_omissions: int
    under_recommendations: int
    over_recommendations: int
    unnecessary_recommended_cost: int
    blocking_scope_false_negatives: int
    blocking_scope_false_positives: int
    required_clarification_false_negatives: int
    unsupported_methodological_basis: int


@dataclass(frozen=True, slots=True)
class RecommendationGateEvaluation:
    outcome: AdvancementOutcome
    absolute_passed: bool
    relative_passed: bool
    expansion_passed: bool
    gate_results: Mapping[str, bool]
    value_signals: tuple[str, ...]
    aggregate_by_condition: Mapping[str, ConditionAggregate]
    per_case_exact_accuracy: Mapping[str, Mapping[str, float]]
    per_case_semantic_score: Mapping[str, Mapping[str, float]]


CONTROL_INCLUDED = "CONTROL_INCLUDED"
GENERIC_CONTEXT_PAYLOAD: dict[str, object] = {}


def _canonical_json(payload: object) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest_payload(payload: object) -> tuple[str, int]:
    text = _canonical_json(payload)
    encoded = text.encode("utf-8")
    return hashlib.sha256(encoded).hexdigest(), len(encoded)


def load_frozen_benchmark(path: Path) -> FrozenRecommendationBenchmark:
    raw = json.loads(path.read_text(encoding="utf-8"))
    cases = tuple(_load_case(item) for item in raw["cases"])
    if len(cases) != 4:
        raise ValueError(f"Specification 015 requires exactly four cases, observed {len(cases)}")
    if len({case.case_id for case in cases}) != len(cases):
        raise ValueError("recommendation benchmark case IDs must be unique")

    expected_conditions = {
        RecommendationCondition.GENERIC.value,
        RecommendationCondition.SELECTIVE.value,
        RecommendationCondition.FULL_HORIZON.value,
    }
    observed_conditions = {str(value) for value in raw["conditions"]}
    if observed_conditions != expected_conditions:
        raise ValueError(
            f"frozen conditions drifted: expected {sorted(expected_conditions)}, "
            f"observed {sorted(observed_conditions)}"
        )

    reasoner = raw["reasoner"]
    judge = raw["judge"]
    return FrozenRecommendationBenchmark(
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
        absolute_gate=dict(raw["absolute_gate"]),
        relative_gate=dict(raw["relative_gate"]),
        expansion_gate=dict(raw["expansion_gate"]),
        promotion_value_signals=dict(raw["promotion_value_signals"]),
        call_plan=dict(raw["call_plan"]),
        cases=cases,
    )


def _load_case(raw: Mapping[str, object]) -> RecommendationExperimentCase:
    actions = tuple(
        CandidateAction(
            action_id=str(item["action_id"]),
            label=str(item["label"]),
            cost_units=int(item["cost_units"]),
            expected_disposition=RecommendationDisposition(str(item["expected_disposition"])),
            critical=bool(item["critical"]),
        )
        for item in raw["candidate_actions"]  # type: ignore[index]
    )
    if len(actions) != 6:
        raise ValueError(
            f"{raw['case_id']} must contain exactly six frozen candidate actions"
        )
    if len({item.action_id for item in actions}) != len(actions):
        raise ValueError(f"{raw['case_id']} candidate action IDs must be unique")
    if any(item.cost_units <= 0 for item in actions):
        raise ValueError(f"{raw['case_id']} action cost units must be positive")

    clarifications = tuple(
        ClarificationOption(
            clarification_id=str(item["clarification_id"]),
            description=str(item["description"]),
        )
        for item in raw["available_clarifications"]  # type: ignore[index]
    )
    if len({item.clarification_id for item in clarifications}) != len(clarifications):
        raise ValueError(f"{raw['case_id']} clarification IDs must be unique")

    rubric = tuple(
        RubricObligation(
            obligation_id=str(item["obligation_id"]),
            critical=bool(item["critical"]),
            description=str(item["description"]),
        )
        for item in raw["rubric"]  # type: ignore[index]
    )
    if not rubric:
        raise ValueError(f"{raw['case_id']} rubric must not be empty")
    if len({item.obligation_id for item in rubric}) != len(rubric):
        raise ValueError(f"{raw['case_id']} rubric obligation IDs must be unique")

    expected_blocked = tuple(str(value) for value in raw["expected_blocked_scopes"])  # type: ignore[index]
    available_blocked = tuple(str(value) for value in raw["available_blocked_scopes"])  # type: ignore[index]
    if not set(expected_blocked).issubset(set(available_blocked)):
        raise ValueError(f"{raw['case_id']} expected blocked scopes must be available")

    expected_clarifications = tuple(
        str(value) for value in raw["expected_required_clarification_ids"]  # type: ignore[index]
    )
    if not set(expected_clarifications).issubset(
        {item.clarification_id for item in clarifications}
    ):
        raise ValueError(f"{raw['case_id']} expected clarifications must be available")

    return RecommendationExperimentCase(
        case_id=str(raw["case_id"]),
        case_class=str(raw["class"]),
        source_case_id=str(raw["source_case_id"]),
        task_id=str(raw["task_id"]),
        requested_reasoning_functions=tuple(
            str(value) for value in raw["requested_reasoning_functions"]  # type: ignore[index]
        ),
        required_selective_keys=tuple(
            str(value) for value in raw["required_selective_keys"]  # type: ignore[index]
        ),
        allowed_additional_basis_keys=tuple(
            str(value) for value in raw["allowed_additional_basis_keys"]  # type: ignore[index]
        ),
        project_evidence=dict(raw["project_evidence"]),  # type: ignore[arg-type]
        user_task=str(raw["user_task"]),
        available_blocked_scopes=available_blocked,
        expected_blocked_scopes=expected_blocked,
        available_clarifications=clarifications,
        expected_required_clarification_ids=expected_clarifications,
        candidate_actions=actions,
        rubric=rubric,
    )


def build_reasoning_plan(
    benchmark: FrozenRecommendationBenchmark,
) -> tuple[RecommendationPlanEntry, ...]:
    """Generate the frozen three-condition plan deterministically."""

    rng = random.Random(benchmark.randomization_seed)
    entries: list[RecommendationPlanEntry] = []
    ordinal = 0
    for case in benchmark.cases:
        for repetition in range(1, benchmark.repetitions + 1):
            block = list(RecommendationCondition)
            rng.shuffle(block)
            for condition in block:
                ordinal += 1
                opaque = hashlib.sha256(
                    (
                        f"{benchmark.benchmark_id}|{benchmark.randomization_seed}|"
                        f"{ordinal}|{case.case_id}|{repetition}|{condition.value}"
                    ).encode("utf-8")
                ).hexdigest()
                entries.append(
                    RecommendationPlanEntry(
                        output_id=f"ra-{opaque[:16]}",
                        run_nonce=f"nonce-{opaque[16:40]}",
                        case_id=case.case_id,
                        repetition=repetition,
                        condition=condition,
                    )
                )
    expected = len(benchmark.cases) * benchmark.repetitions * 3
    if len(entries) != expected:
        raise AssertionError("internal recommendation plan cardinality error")
    return tuple(entries)


def build_judge_plan(
    output_ids: Sequence[str],
    *,
    randomization_seed: int,
) -> tuple[JudgePlanEntry, ...]:
    unique_ids = list(output_ids)
    if len(unique_ids) != len(set(unique_ids)):
        raise ValueError("output_ids must be unique")
    rng = random.Random(randomization_seed ^ 0x71A9C40D)
    rng.shuffle(unique_ids)
    return tuple(
        JudgePlanEntry(
            judge_id="ra-judge-"
            + hashlib.sha256(
                f"{randomization_seed}|{position}|{output_id}".encode("utf-8")
            ).hexdigest()[:16],
            output_id=output_id,
        )
        for position, output_id in enumerate(unique_ids, start=1)
    )


def serialize_reasoning_plan(
    plan: Sequence[RecommendationPlanEntry],
) -> tuple[str, str]:
    payload = [
        {
            "case_id": item.case_id,
            "condition": item.condition.value,
            "output_id": item.output_id,
            "repetition": item.repetition,
            "run_nonce": item.run_nonce,
        }
        for item in plan
    ]
    text = _canonical_json(payload)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def serialize_judge_plan(plan: Sequence[JudgePlanEntry]) -> tuple[str, str]:
    payload = [
        {"judge_id": item.judge_id, "output_id": item.output_id}
        for item in plan
    ]
    text = _canonical_json(payload)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_full_horizon_pack(
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> MethodologicalContextPack:
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

    aggregate_missing = tuple(
        sorted({key for item in items for key in item.missing_context_keys})
    )
    return MethodologicalContextPack(
        schema_version=1,
        task_id=request.task_id,
        requested_reasoning_functions=tuple(sorted(request.requested_reasoning_functions)),
        knowledge=tuple(items),
        missing_context_keys=aggregate_missing,
    )


def build_condition_input(
    condition: RecommendationCondition,
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> RecommendationConditionInput:
    if condition is RecommendationCondition.GENERIC:
        digest, utf8_bytes = _digest_payload(GENERIC_CONTEXT_PAYLOAD)
        return RecommendationConditionInput(
            condition=condition,
            payload=GENERIC_CONTEXT_PAYLOAD,
            sha256=digest,
            utf8_bytes=utf8_bytes,
            revisions=(),
            pack=None,
        )

    if condition is RecommendationCondition.SELECTIVE:
        pack = select_methodological_context(
            horizon,
            request,
            uow_factory=uow_factory,
        ).pack
    elif condition is RecommendationCondition.FULL_HORIZON:
        pack = build_full_horizon_pack(horizon, request, uow_factory=uow_factory)
    else:
        raise ValueError(f"unsupported recommendation condition: {condition!r}")

    serialized = serialize_methodological_context_pack(pack)
    revisions = tuple(
        KnowledgeRevisionPointer(
            stable_key=item.asset.stable_key,
            revision_id=item.asset.revision_id,
        )
        for item in pack.knowledge
    )
    return RecommendationConditionInput(
        condition=condition,
        payload=methodological_context_pack_payload(pack),
        sha256=serialized.sha256,
        utf8_bytes=serialized.utf8_bytes,
        revisions=revisions,
        pack=pack,
    )


def build_reasoning_request(
    *,
    benchmark: FrozenRecommendationBenchmark,
    case: RecommendationExperimentCase,
    plan_entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
) -> ReasoningRequest:
    if plan_entry.case_id != case.case_id:
        raise ValueError("plan entry case does not match recommendation case")
    if plan_entry.condition is not context.condition:
        raise ValueError("plan entry condition does not match context condition")

    return ReasoningRequest(
        run_id=plan_entry.output_id,
        run_nonce=plan_entry.run_nonce,
        system_instruction=benchmark.common_reasoner_instruction,
        user_task=case.user_task,
        project_evidence=case.project_evidence,
        task_payload=case.model_task_payload(),
        methodological_context_payload=context.payload,
        methodological_context_sha256=context.sha256,
        knowledge_revisions=context.revisions,
        model_configuration=benchmark.reasoner_model,
        structured_output_kind=ReasoningOutputKind.RECOMMENDATION_ACTION,
    )


def validate_frozen_condition_sets(
    benchmark: FrozenRecommendationBenchmark,
    horizon: MethodologicalHorizon,
    *,
    max_assets: int,
    uow_factory,
) -> None:
    """Fail before live calls if any frozen treatment identity has drifted."""

    if len(horizon.included) != 10:
        raise ValueError(
            f"frozen FULL_HORIZON requires 10 included assets, observed {len(horizon.included)}"
        )

    for case in benchmark.cases:
        request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=max_assets,
        )
        generic = build_condition_input(
            RecommendationCondition.GENERIC,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        if generic.revisions or generic.payload:
            raise ValueError(f"{case.case_id} GENERIC contains methodological knowledge")

        selective = build_condition_input(
            RecommendationCondition.SELECTIVE,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        observed = {item.stable_key for item in selective.revisions}
        expected = set(case.required_selective_keys)
        if observed != expected:
            raise ValueError(
                f"{case.case_id} SELECTIVE set drifted: expected {sorted(expected)}, "
                f"observed {sorted(observed)}"
            )

        full = build_condition_input(
            RecommendationCondition.FULL_HORIZON,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        if len(full.revisions) != 10:
            raise ValueError(f"{case.case_id} FULL_HORIZON does not contain 10 revisions")


def evaluate_recommendation_result(
    case: RecommendationExperimentCase,
    result: RecommendationActionResult,
    *,
    supplied_revisions: tuple[KnowledgeRevisionPointer, ...],
) -> RecommendationMetrics:
    """Compute Specification 015 exact metrics from hidden fixture truth."""

    validate_recommendation_action_result(
        result,
        candidate_action_ids=case.candidate_action_ids,
        allowed_blocked_scopes=case.available_blocked_scopes,
        allowed_clarification_ids=case.allowed_clarification_ids,
    )

    supplied = {item.stable_key for item in supplied_revisions}
    unsupported_basis = len(set(result.methodological_basis) - supplied)
    validate_methodological_basis(result, supplied_revisions)

    expected = {action.action_id: action for action in case.candidate_actions}
    decisions = {decision.action_id: decision for decision in result.action_decisions}

    exact = 0
    critical_omissions = 0
    under = 0
    over = 0
    unnecessary_cost = 0

    for action_id, action in expected.items():
        predicted = decisions[action_id].disposition
        if predicted is action.expected_disposition:
            exact += 1
        if (
            action.expected_disposition is RecommendationDisposition.BLOCKING_REQUIRED
            and predicted is not RecommendationDisposition.BLOCKING_REQUIRED
        ):
            critical_omissions += 1
        if (
            action.expected_disposition is RecommendationDisposition.RECOMMENDED
            and predicted
            in {RecommendationDisposition.DEFER, RecommendationDisposition.NOT_NOW}
        ):
            under += 1
        if (
            action.expected_disposition
            in {RecommendationDisposition.DEFER, RecommendationDisposition.NOT_NOW}
            and predicted
            in {
                RecommendationDisposition.RECOMMENDED,
                RecommendationDisposition.BLOCKING_REQUIRED,
            }
        ):
            over += 1
            unnecessary_cost += action.cost_units

    expected_scopes = set(case.expected_blocked_scopes)
    predicted_scopes = set(result.blocked_scopes)
    expected_clarifications = set(case.expected_required_clarification_ids)
    predicted_clarifications = set(result.required_clarification_ids)

    return RecommendationMetrics(
        exact_disposition_accuracy=exact / len(case.candidate_actions),
        critical_action_omissions=critical_omissions,
        under_recommendations=under,
        over_recommendations=over,
        unnecessary_recommended_cost=unnecessary_cost,
        blocking_scope_false_negatives=len(expected_scopes - predicted_scopes),
        blocking_scope_false_positives=len(predicted_scopes - expected_scopes),
        required_clarification_false_negatives=len(
            expected_clarifications - predicted_clarifications
        ),
        unsupported_methodological_basis=unsupported_basis,
    )


def validate_judge_result(
    case: RecommendationExperimentCase,
    result: JudgeResult,
) -> JudgeResult:
    expected_ids = [item.obligation_id for item in case.rubric]
    observed_ids = [item.obligation_id for item in result.obligation_scores]
    if observed_ids != expected_ids:
        raise ValueError(
            f"judge obligation IDs/order do not match frozen rubric for {case.case_id}: "
            f"expected {expected_ids}, observed {observed_ids}"
        )

    recomputed = sum(item.score for item in result.obligation_scores) / (
        2 * len(result.obligation_scores)
    )
    if abs(recomputed - result.normalized_score) > 1e-9:
        raise ValueError(
            "judge normalized score is inconsistent: "
            f"reported {result.normalized_score}, recomputed {recomputed}"
        )

    critical_ids = {item.obligation_id for item in case.rubric if item.critical}
    critical_failure = any(
        item.obligation_id in critical_ids and item.score == 0
        for item in result.obligation_scores
    )
    if critical_failure != result.critical_failure:
        raise ValueError("judge critical_failure is inconsistent with frozen rubric scores")
    return result


def evaluate_gates(
    benchmark: FrozenRecommendationBenchmark,
    observations: Sequence[RecommendationScoredObservation],
) -> RecommendationGateEvaluation:
    """Apply the frozen absolute, relative, expansion, and value-signal rules."""

    expected_count = len(benchmark.cases) * 3 * benchmark.repetitions
    if len(observations) != expected_count:
        raise ValueError(
            f"gate evaluation requires {expected_count} scored observations, "
            f"observed {len(observations)}"
        )

    by_key: dict[
        tuple[str, RecommendationCondition, int], RecommendationScoredObservation
    ] = {}
    case_ids = {case.case_id for case in benchmark.cases}
    for observation in observations:
        if observation.case_id not in case_ids:
            raise ValueError(f"unknown scored case: {observation.case_id}")
        if observation.output_id != observation.judge_result.output_id:
            raise ValueError("scored observation output_id and judge output_id differ")
        key = (observation.case_id, observation.condition, observation.repetition)
        if key in by_key:
            raise ValueError(f"duplicate scored observation: {key}")
        by_key[key] = observation

    aggregate: dict[RecommendationCondition, ConditionAggregate] = {}
    per_case_exact: dict[str, dict[str, float]] = {}
    per_case_semantic: dict[str, dict[str, float]] = {}

    for condition in RecommendationCondition:
        condition_items = [item for item in observations if item.condition is condition]
        aggregate[condition] = _aggregate(condition_items)

    for case in benchmark.cases:
        exact_row: dict[str, float] = {}
        semantic_row: dict[str, float] = {}
        for condition in RecommendationCondition:
            items = [
                by_key[(case.case_id, condition, repetition)]
                for repetition in range(1, benchmark.repetitions + 1)
            ]
            exact_row[condition.value] = _mean(
                item.metrics.exact_disposition_accuracy for item in items
            )
            semantic_row[condition.value] = _mean(
                item.judge_result.normalized_score for item in items
            )
        per_case_exact[case.case_id] = exact_row
        per_case_semantic[case.case_id] = semantic_row

    s = aggregate[RecommendationCondition.SELECTIVE]
    g = aggregate[RecommendationCondition.GENERIC]
    f = aggregate[RecommendationCondition.FULL_HORIZON]
    a = benchmark.absolute_gate
    r = benchmark.relative_gate

    gates: dict[str, bool] = {}
    gates["RA-G01"] = s.critical_action_omissions <= int(
        a["selective_max_critical_action_omissions"]
    )
    gates["RA-G02"] = s.blocking_scope_false_negatives <= int(
        a["selective_max_blocking_scope_false_negatives"]
    )
    gates["RA-G03"] = s.unsupported_methodological_basis <= int(
        a["selective_max_unsupported_basis_failures"]
    )
    gates["RA-G04"] = s.exact_disposition_accuracy >= float(
        a["selective_min_aggregate_exact_disposition_accuracy"]
    )
    gates["RA-G05"] = all(
        per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_exact_disposition_accuracy"])
        for case in benchmark.cases
    )
    gates["RA-G06"] = s.semantic_score >= float(
        a["selective_min_aggregate_semantic_score"]
    )
    gates["RA-G07"] = all(
        per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_semantic_score"])
        for case in benchmark.cases
    )

    gates["RA-G08"] = (
        s.exact_disposition_accuracy
        >= g.exact_disposition_accuracy
        + float(r["selective_minus_generic_aggregate_exact_accuracy_floor"])
        and all(
            per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_exact[case.case_id][RecommendationCondition.GENERIC.value]
            + float(r["selective_minus_generic_per_case_exact_accuracy_floor"])
            for case in benchmark.cases
        )
    )
    gates["RA-G09"] = (
        s.exact_disposition_accuracy
        >= f.exact_disposition_accuracy
        + float(r["selective_minus_full_aggregate_exact_accuracy_floor"])
        and all(
            per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_exact[case.case_id][RecommendationCondition.FULL_HORIZON.value]
            + float(r["selective_minus_full_per_case_exact_accuracy_floor"])
            for case in benchmark.cases
        )
    )
    gates["RA-G10"] = (
        s.semantic_score
        >= g.semantic_score
        + float(r["selective_minus_generic_aggregate_semantic_floor"])
        and all(
            per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_semantic[case.case_id][RecommendationCondition.GENERIC.value]
            + float(r["selective_minus_generic_per_case_semantic_floor"])
            for case in benchmark.cases
        )
    )
    gates["RA-G11"] = (
        s.semantic_score
        >= f.semantic_score
        + float(r["selective_minus_full_aggregate_semantic_floor"])
        and all(
            per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_semantic[case.case_id][RecommendationCondition.FULL_HORIZON.value]
            + float(r["selective_minus_full_per_case_semantic_floor"])
            for case in benchmark.cases
        )
    )
    gates["RA-G12"] = (
        s.critical_action_omissions <= g.critical_action_omissions
        and s.under_recommendations <= g.under_recommendations
    )
    gates["RA-G13"] = (
        s.unnecessary_recommended_cost <= f.unnecessary_recommended_cost
    )
    gates["RA-G14"] = s.over_recommendations <= f.over_recommendations
    gates["RA-G15"] = (
        s.blocking_scope_false_positives <= f.blocking_scope_false_positives
    )

    absolute_passed = all(gates[f"RA-G{number:02d}"] for number in range(1, 8))
    relative_passed = all(gates[f"RA-G{number:02d}"] for number in range(8, 13))
    expansion_passed = all(gates[f"RA-G{number:02d}"] for number in range(13, 16))

    value_signals: list[str] = []
    if s.exact_disposition_accuracy >= g.exact_disposition_accuracy + 0.05:
        value_signals.append(
            "SELECTIVE_AGGREGATE_EXACT_ACCURACY_AT_LEAST_0_05_ABOVE_GENERIC"
        )
    if s.critical_action_omissions < g.critical_action_omissions:
        value_signals.append("SELECTIVE_FEWER_TOTAL_CRITICAL_OMISSIONS_THAN_GENERIC")
    if s.under_recommendations < g.under_recommendations:
        value_signals.append("SELECTIVE_FEWER_TOTAL_UNDER_RECOMMENDATIONS_THAN_GENERIC")
    if s.unnecessary_recommended_cost < f.unnecessary_recommended_cost:
        value_signals.append(
            "SELECTIVE_LOWER_TOTAL_UNNECESSARY_RECOMMENDED_COST_THAN_FULL_HORIZON"
        )
    if s.over_recommendations < f.over_recommendations:
        value_signals.append(
            "SELECTIVE_FEWER_TOTAL_OVER_RECOMMENDATIONS_THAN_FULL_HORIZON"
        )
    if s.blocking_scope_false_positives < f.blocking_scope_false_positives:
        value_signals.append(
            "SELECTIVE_FEWER_TOTAL_BLOCKING_SCOPE_FALSE_POSITIVES_THAN_FULL_HORIZON"
        )

    allowed_signals = set(benchmark.promotion_value_signals["signals"])
    if not set(value_signals).issubset(allowed_signals):
        raise AssertionError("computed a value signal not present in the frozen fixture")

    safety_passed = absolute_passed and relative_passed and expansion_passed
    required_signal_count = int(
        benchmark.promotion_value_signals["minimum_required_signals"]
    )
    if not safety_passed:
        outcome = AdvancementOutcome.FAIL
    elif len(value_signals) >= required_signal_count:
        outcome = AdvancementOutcome.PROMOTE_BOUNDED_RECOMMENDATION_SEAM
    else:
        outcome = AdvancementOutcome.SAFE_BUT_NOT_DIFFERENTIATED

    return RecommendationGateEvaluation(
        outcome=outcome,
        absolute_passed=absolute_passed,
        relative_passed=relative_passed,
        expansion_passed=expansion_passed,
        gate_results=gates,
        value_signals=tuple(value_signals),
        aggregate_by_condition={key.value: value for key, value in aggregate.items()},
        per_case_exact_accuracy=per_case_exact,
        per_case_semantic_score=per_case_semantic,
    )


def _aggregate(
    observations: Sequence[RecommendationScoredObservation],
) -> ConditionAggregate:
    if not observations:
        raise ValueError("cannot aggregate an empty condition")
    return ConditionAggregate(
        exact_disposition_accuracy=_mean(
            item.metrics.exact_disposition_accuracy for item in observations
        ),
        semantic_score=_mean(item.judge_result.normalized_score for item in observations),
        critical_action_omissions=sum(
            item.metrics.critical_action_omissions for item in observations
        ),
        under_recommendations=sum(
            item.metrics.under_recommendations for item in observations
        ),
        over_recommendations=sum(
            item.metrics.over_recommendations for item in observations
        ),
        unnecessary_recommended_cost=sum(
            item.metrics.unnecessary_recommended_cost for item in observations
        ),
        blocking_scope_false_negatives=sum(
            item.metrics.blocking_scope_false_negatives for item in observations
        ),
        blocking_scope_false_positives=sum(
            item.metrics.blocking_scope_false_positives for item in observations
        ),
        required_clarification_false_negatives=sum(
            item.metrics.required_clarification_false_negatives for item in observations
        ),
        unsupported_methodological_basis=sum(
            item.metrics.unsupported_methodological_basis for item in observations
        ),
    )


def _mean(values) -> float:
    items = list(values)
    if not items:
        raise ValueError("cannot compute mean of empty values")
    return sum(items) / len(items)
