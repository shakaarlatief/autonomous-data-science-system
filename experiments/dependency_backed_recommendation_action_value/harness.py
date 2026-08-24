"""Provider-neutral harness for frozen Specification 021.

This module owns the experiment semantics that must remain independent from the
provider adapter: frozen-fixture validation, explicit project-relation audits,
deterministic three-condition planning, exact methodological-context
construction, system-owned methodology provenance, strict action-local pointer
validation, deterministic recommendation metrics, blinded judge payloads, and
the preregistered complete-design advancement rule.

No function in this module mutates authoritative project state. Evaluator truth
is retained in fixture-side objects and is deliberately omitted from reasoner
and judge inputs except for the semantic rubric explicitly allowed by
Specification 021.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
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
from ads_system.application.reasoning import (
    KnowledgeRevisionPointer,
    ReasoningModelConfiguration,
    ReasoningRequest,
)


CONTROL_INCLUDED = "CONTROL_INCLUDED"
GENERIC_CONTEXT_PAYLOAD: dict[str, object] = {}


class RecommendationCondition(StrEnum):
    GENERIC = "GENERIC"
    SELECTIVE = "SELECTIVE"
    FULL_HORIZON = "FULL_HORIZON"


class RecommendationDisposition(StrEnum):
    BLOCKING_REQUIRED = "BLOCKING_REQUIRED"
    RECOMMENDED = "RECOMMENDED"
    DEFER = "DEFER"
    NOT_NOW = "NOT_NOW"


class AdvancementOutcome(StrEnum):
    PROMOTE = "PROMOTE_DEPENDENCY_BACKED_RECOMMENDATION_SEAM"
    SAFE_NOT_DIFFERENTIATED = "SAFE_BUT_NOT_DIFFERENTIATED"
    FAIL = "FAIL"


@dataclass(frozen=True, slots=True)
class DependencyBackedActionDecision:
    """One model-owned decision over one supplied candidate action identity."""

    action_id: str
    disposition: str
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    defer_until_id: str | None
    rationale: str

    def __post_init__(self) -> None:
        if not self.action_id.strip():
            raise ValueError("action_id must be non-empty")
        try:
            normalized = RecommendationDisposition(self.disposition)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"unsupported disposition: {self.disposition!r}") from exc
        object.__setattr__(self, "disposition", normalized.value)
        for field_name in (
            "blocking_requirement_id",
            "blocked_scope_id",
            "defer_until_id",
        ):
            value = getattr(self, field_name)
            if value is not None and not value.strip():
                raise ValueError(f"{field_name} must be null or non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")

    def to_payload(self) -> dict[str, object]:
        return {
            "action_id": self.action_id,
            "disposition": self.disposition,
            "blocking_requirement_id": self.blocking_requirement_id,
            "blocked_scope_id": self.blocked_scope_id,
            "defer_until_id": self.defer_until_id,
            "rationale": self.rationale,
        }


@dataclass(frozen=True, slots=True)
class DependencyBackedRecommendationActionResult:
    """Experiment-owned structured result for one Specification 021 reasoner call."""

    summary: str
    action_decisions: tuple[DependencyBackedActionDecision, ...]
    warnings: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("summary must be non-empty")
        action_ids = [item.action_id for item in self.action_decisions]
        if len(action_ids) != len(set(action_ids)):
            raise ValueError("action_decisions must contain unique action IDs")
        if any(not warning.strip() for warning in self.warnings):
            raise ValueError("warnings cannot contain empty strings")
        if len(self.warnings) != len(set(self.warnings)):
            raise ValueError("warnings must not contain duplicates")

    def to_payload(self) -> dict[str, object]:
        return {
            "summary": self.summary,
            "action_decisions": [item.to_payload() for item in self.action_decisions],
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True, slots=True)
class Requirement:
    requirement_id: str
    description: str
    status: str


@dataclass(frozen=True, slots=True)
class DownstreamScope:
    scope_id: str
    description: str
    active: bool
    intended_to_be_defended: bool


@dataclass(frozen=True, slots=True)
class ScopeRequirementRelation:
    scope_id: str
    relation: str
    requirement_id: str


@dataclass(frozen=True, slots=True)
class DeferTrigger:
    trigger_id: str
    description: str
    status: str


@dataclass(frozen=True, slots=True)
class ActionRequirementRelation:
    action_id: str
    relation: str
    requirement_id: str


@dataclass(frozen=True, slots=True)
class ActionTriggerRelation:
    action_id: str
    relation: str
    trigger_id: str


@dataclass(frozen=True, slots=True)
class CandidateAction:
    action_id: str
    label: str
    cost_units: int
    expected_disposition: RecommendationDisposition
    expected_blocking_requirement_id: str | None
    expected_blocked_scope_id: str | None
    expected_defer_until_id: str | None
    critical: bool


@dataclass(frozen=True, slots=True)
class RubricObligation:
    obligation_id: str
    critical: bool
    description: str


@dataclass(frozen=True, slots=True)
class RecommendationExperimentCase:
    case_id: str
    case_class: str
    task_id: str
    requested_reasoning_functions: tuple[str, ...]
    required_selective_keys: tuple[str, ...]
    project_evidence: Mapping[str, object]
    user_task: str
    requirements: tuple[Requirement, ...]
    downstream_scopes: tuple[DownstreamScope, ...]
    scope_requirement_relations: tuple[ScopeRequirementRelation, ...]
    defer_triggers: tuple[DeferTrigger, ...]
    action_requirement_relations: tuple[ActionRequirementRelation, ...]
    action_trigger_relations: tuple[ActionTriggerRelation, ...]
    candidate_actions: tuple[CandidateAction, ...]
    rubric: tuple[RubricObligation, ...]

    @property
    def candidate_action_ids(self) -> tuple[str, ...]:
        return tuple(item.action_id for item in self.candidate_actions)

    @property
    def requirement_ids(self) -> tuple[str, ...]:
        return tuple(item.requirement_id for item in self.requirements)

    @property
    def scope_ids(self) -> tuple[str, ...]:
        return tuple(item.scope_id for item in self.downstream_scopes)

    @property
    def trigger_ids(self) -> tuple[str, ...]:
        return tuple(item.trigger_id for item in self.defer_triggers)

    def model_task_payload(self) -> dict[str, object]:
        """Return the complete system-owned project/action/relation payload without truth."""

        return {
            "requested_reasoning_functions": list(self.requested_reasoning_functions),
            "requirements": [asdict(item) for item in self.requirements],
            "downstream_scopes": [asdict(item) for item in self.downstream_scopes],
            "scope_requirement_relations": [
                asdict(item) for item in self.scope_requirement_relations
            ],
            "defer_triggers": [asdict(item) for item in self.defer_triggers],
            "candidate_actions": [
                {"action_id": item.action_id, "label": item.label}
                for item in self.candidate_actions
            ],
            "action_requirement_relations": [
                asdict(item) for item in self.action_requirement_relations
            ],
            "action_trigger_relations": [
                asdict(item) for item in self.action_trigger_relations
            ],
        }


@dataclass(frozen=True, slots=True)
class FrozenRecommendationBenchmark:
    benchmark_id: str
    starting_integration_head: str
    randomization_seed: int
    repetitions: int
    full_horizon_keys: tuple[str, ...]
    common_reasoner_instruction: str
    reasoner_model: ReasoningModelConfiguration
    judge_model: ReasoningModelConfiguration
    call_plan: Mapping[str, object]
    absolute_gate: Mapping[str, object]
    relative_gate: Mapping[str, object]
    expansion_gate: Mapping[str, object]
    promotion_value_signals: Mapping[str, object]
    technical_invariants: tuple[str, ...]
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
class SystemContextProvenance:
    """System-owned exact provenance for one supplied methodology payload."""

    condition: RecommendationCondition
    supplied_revisions: tuple[KnowledgeRevisionPointer, ...]
    methodology_payload_sha256: str
    methodology_payload_bytes: int

    def to_payload(self) -> dict[str, object]:
        return {
            "condition": self.condition.value,
            "supplied_revisions": [asdict(item) for item in self.supplied_revisions],
            "methodology_payload_sha256": self.methodology_payload_sha256,
            "methodology_payload_bytes": self.methodology_payload_bytes,
        }


@dataclass(frozen=True, slots=True)
class RecommendationConditionInput:
    condition: RecommendationCondition
    payload: Mapping[str, object]
    sha256: str
    utf8_bytes: int
    revisions: tuple[KnowledgeRevisionPointer, ...]
    pack: MethodologicalContextPack | None = None

    @property
    def provenance(self) -> SystemContextProvenance:
        return SystemContextProvenance(
            condition=self.condition,
            supplied_revisions=self.revisions,
            methodology_payload_sha256=self.sha256,
            methodology_payload_bytes=self.utf8_bytes,
        )


@dataclass(frozen=True, slots=True)
class SystemProvenancePlanEntry:
    output_id: str
    run_nonce: str
    case_id: str
    repetition: int
    provenance: SystemContextProvenance


@dataclass(frozen=True, slots=True)
class RecommendationMetrics:
    exact_disposition_accuracy: float
    critical_action_omissions: int
    under_recommendations: int
    over_recommendations: int
    unnecessary_recommended_cost: int
    blocking_false_positives: int
    blocking_pointer_errors: int
    defer_pointer_errors: int


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
    blocking_false_positives: int
    blocking_pointer_errors: int
    defer_pointer_errors: int


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


@dataclass(frozen=True, slots=True)
class JudgePayload:
    output_id: str
    user_task: str
    project_evidence: Mapping[str, object]
    task_menu: Mapping[str, object]
    rubric: tuple[RubricObligation, ...]
    candidate_result: Mapping[str, object]

    def to_payload(self) -> dict[str, object]:
        return {
            "output_id": self.output_id,
            "user_task": self.user_task,
            "project_evidence": dict(self.project_evidence),
            "task_menu": dict(self.task_menu),
            "rubric": [asdict(item) for item in self.rubric],
            "candidate_result": dict(self.candidate_result),
            "score_definitions": {
                "0": "Absent, materially wrong, or contradicted.",
                "1": "Partially or implicitly satisfied without a material contradiction.",
                "2": "Explicitly and correctly satisfied.",
            },
            "judge_may_add_obligations": False,
        }


def _canonical_json(payload: object) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _digest_payload(payload: object) -> tuple[str, int]:
    text = _canonical_json(payload)
    encoded = text.encode("utf-8")
    return hashlib.sha256(encoded).hexdigest(), len(encoded)


def load_frozen_benchmark(path: Path) -> FrozenRecommendationBenchmark:
    """Load and fail closed on every prospectively frozen fixture invariant."""

    raw = json.loads(path.read_text(encoding="utf-8"))
    reasoner = raw["reasoner"]
    judge = raw["judge"]
    benchmark = FrozenRecommendationBenchmark(
        benchmark_id=str(raw["benchmark_id"]),
        starting_integration_head=str(raw["starting_integration_head"]),
        randomization_seed=int(raw["randomization_seed"]),
        repetitions=int(raw["reasoner_repetitions_per_condition"]),
        full_horizon_keys=tuple(str(value) for value in raw["full_horizon_keys"]),
        common_reasoner_instruction=str(raw["common_reasoner_instruction"]),
        reasoner_model=ReasoningModelConfiguration(
            requested_model=str(reasoner["model"]),
            reasoning_effort=str(reasoner["reasoning_effort"]),
            verbosity=str(reasoner["text_verbosity"]),
            max_output_tokens=int(reasoner["max_output_tokens"]),
            store=bool(reasoner.get("store", False)),
        ),
        judge_model=ReasoningModelConfiguration(
            requested_model=str(judge["model"]),
            reasoning_effort=str(judge["reasoning_effort"]),
            verbosity=str(judge["text_verbosity"]),
            max_output_tokens=int(judge["max_output_tokens"]),
            store=False,
        ),
        call_plan=dict(raw["call_plan"]),
        absolute_gate=dict(raw["absolute_gate"]),
        relative_gate=dict(raw["relative_gate"]),
        expansion_gate=dict(raw["expansion_gate"]),
        promotion_value_signals=dict(raw["promotion_value_signals"]),
        technical_invariants=tuple(str(value) for value in raw["technical_invariants"]),
        cases=tuple(_load_case(item) for item in raw["cases"]),
    )
    validate_fixture_construction(
        benchmark,
        raw_conditions=tuple(raw["conditions"]),
        raw_dispositions=tuple(raw["dispositions"]),
    )
    return benchmark


def _load_case(raw: Mapping[str, object]) -> RecommendationExperimentCase:
    def _optional(value: object) -> str | None:
        return None if value is None else str(value)

    return RecommendationExperimentCase(
        case_id=str(raw["case_id"]),
        case_class=str(raw["class"]),
        task_id=str(raw["task_id"]),
        requested_reasoning_functions=tuple(
            str(value) for value in raw["requested_reasoning_functions"]  # type: ignore[index]
        ),
        required_selective_keys=tuple(
            str(value) for value in raw["required_selective_keys"]  # type: ignore[index]
        ),
        project_evidence=dict(raw["project_evidence"]),  # type: ignore[arg-type]
        user_task=str(raw["user_task"]),
        requirements=tuple(
            Requirement(
                requirement_id=str(item["requirement_id"]),
                description=str(item["description"]),
                status=str(item["status"]),
            )
            for item in raw["requirements"]  # type: ignore[index]
        ),
        downstream_scopes=tuple(
            DownstreamScope(
                scope_id=str(item["scope_id"]),
                description=str(item["description"]),
                active=bool(item["active"]),
                intended_to_be_defended=bool(item["intended_to_be_defended"]),
            )
            for item in raw["downstream_scopes"]  # type: ignore[index]
        ),
        scope_requirement_relations=tuple(
            ScopeRequirementRelation(
                scope_id=str(item["scope_id"]),
                relation=str(item["relation"]),
                requirement_id=str(item["requirement_id"]),
            )
            for item in raw["scope_requirement_relations"]  # type: ignore[index]
        ),
        defer_triggers=tuple(
            DeferTrigger(
                trigger_id=str(item["trigger_id"]),
                description=str(item["description"]),
                status=str(item["status"]),
            )
            for item in raw["defer_triggers"]  # type: ignore[index]
        ),
        action_requirement_relations=tuple(
            ActionRequirementRelation(
                action_id=str(item["action_id"]),
                relation=str(item["relation"]),
                requirement_id=str(item["requirement_id"]),
            )
            for item in raw["action_requirement_relations"]  # type: ignore[index]
        ),
        action_trigger_relations=tuple(
            ActionTriggerRelation(
                action_id=str(item["action_id"]),
                relation=str(item["relation"]),
                trigger_id=str(item["trigger_id"]),
            )
            for item in raw["action_trigger_relations"]  # type: ignore[index]
        ),
        candidate_actions=tuple(
            CandidateAction(
                action_id=str(item["action_id"]),
                label=str(item["label"]),
                cost_units=int(item["cost_units"]),
                expected_disposition=RecommendationDisposition(str(item["expected_disposition"])),
                expected_blocking_requirement_id=_optional(
                    item.get("expected_blocking_requirement_id")
                ),
                expected_blocked_scope_id=_optional(item.get("expected_blocked_scope_id")),
                expected_defer_until_id=_optional(item.get("expected_defer_until_id")),
                critical=bool(item["critical"]),
            )
            for item in raw["candidate_actions"]  # type: ignore[index]
        ),
        rubric=tuple(
            RubricObligation(
                obligation_id=str(item["obligation_id"]),
                critical=bool(item["critical"]),
                description=str(item["description"]),
            )
            for item in raw["rubric"]  # type: ignore[index]
        ),
    )


def validate_fixture_construction(
    benchmark: FrozenRecommendationBenchmark,
    *,
    raw_conditions: tuple[object, ...] | None = None,
    raw_dispositions: tuple[object, ...] | None = None,
) -> None:
    """Mechanically enforce DBRA-INV-01/02 and relation-truth construction rules."""

    if len(benchmark.cases) != 4:
        raise ValueError("Specification 021 requires exactly four cases")
    if len({case.case_id for case in benchmark.cases}) != 4:
        raise ValueError("Specification 021 case IDs must be unique")
    if benchmark.repetitions != 3:
        raise ValueError("Specification 021 requires exactly three repetitions")
    if raw_conditions is not None and {str(value) for value in raw_conditions} != {
        item.value for item in RecommendationCondition
    }:
        raise ValueError("condition set drifted")
    if raw_dispositions is not None and {str(value) for value in raw_dispositions} != {
        item.value for item in RecommendationDisposition
    }:
        raise ValueError("disposition set drifted")

    expected_selective_sets = {
        "DBRA-01": {
            "prediction-moment",
            "prediction-time-feature-eligibility",
            "temporal-validation",
        },
        "DBRA-02": {"gradient-boosted-trees", "random-forest"},
        "DBRA-03": {"ecdf", "histogram"},
        "DBRA-04": {"class-imbalance", "missing-data"},
    }
    expected_full = {
        "bagging",
        "class-imbalance",
        "ecdf",
        "gradient-boosted-trees",
        "histogram",
        "missing-data",
        "prediction-moment",
        "prediction-time-feature-eligibility",
        "random-forest",
        "temporal-validation",
    }
    if set(benchmark.full_horizon_keys) != expected_full or len(benchmark.full_horizon_keys) != 10:
        raise ValueError("frozen FULL_HORIZON key set drifted")

    for case in benchmark.cases:
        if set(case.required_selective_keys) != expected_selective_sets[case.case_id]:
            raise ValueError(f"{case.case_id} frozen SELECTIVE key set drifted")
        if not case.requested_reasoning_functions:
            raise ValueError(f"{case.case_id} must request at least one reasoning function")
        if not case.candidate_actions or not case.rubric:
            raise ValueError(f"{case.case_id} candidate actions and rubric must be non-empty")

        _require_unique(case.requirement_ids, f"{case.case_id} requirement IDs")
        _require_unique(case.scope_ids, f"{case.case_id} scope IDs")
        _require_unique(case.trigger_ids, f"{case.case_id} trigger IDs")
        _require_unique(case.candidate_action_ids, f"{case.case_id} action IDs")
        _require_unique(
            tuple(item.obligation_id for item in case.rubric),
            f"{case.case_id} rubric IDs",
        )

        requirement_ids = set(case.requirement_ids)
        scope_ids = set(case.scope_ids)
        trigger_ids = set(case.trigger_ids)
        action_ids = set(case.candidate_action_ids)
        for relation in case.scope_requirement_relations:
            if relation.relation != "DEPENDS_ON":
                raise ValueError(f"{case.case_id} unsupported scope relation {relation.relation}")
            if relation.scope_id not in scope_ids or relation.requirement_id not in requirement_ids:
                raise ValueError(f"{case.case_id} scope relation references unknown identity")
        for relation in case.action_requirement_relations:
            if relation.relation != "RESOLVES":
                raise ValueError(f"{case.case_id} unsupported action-requirement relation")
            if relation.action_id not in action_ids or relation.requirement_id not in requirement_ids:
                raise ValueError(f"{case.case_id} resolver relation references unknown identity")
        for relation in case.action_trigger_relations:
            if relation.relation != "WAITS_FOR":
                raise ValueError(f"{case.case_id} unsupported action-trigger relation")
            if relation.action_id not in action_ids or relation.trigger_id not in trigger_ids:
                raise ValueError(f"{case.case_id} defer relation references unknown identity")

        for action in case.candidate_actions:
            if action.cost_units <= 0:
                raise ValueError(f"{case.case_id}/{action.action_id} cost must be positive")
            blocking_pairs = _valid_blocking_pairs(case, action.action_id)
            wait_triggers = _valid_wait_triggers(case, action.action_id)
            if action.expected_disposition is RecommendationDisposition.BLOCKING_REQUIRED:
                expected_pair = (
                    action.expected_blocking_requirement_id,
                    action.expected_blocked_scope_id,
                )
                if expected_pair not in blocking_pairs:
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} BLOCKING truth lacks exact relation-backed construction"
                    )
                if action.expected_defer_until_id is not None:
                    raise ValueError("BLOCKING truth must have null defer pointer")
                if wait_triggers:
                    raise ValueError("BLOCKING truth must not also carry an active WAITS_FOR relation")
            elif action.expected_disposition is RecommendationDisposition.DEFER:
                if action.expected_blocking_requirement_id is not None or action.expected_blocked_scope_id is not None:
                    raise ValueError("DEFER truth must have null blocking pointers")
                if action.expected_defer_until_id not in wait_triggers:
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} DEFER truth lacks exact unresolved WAITS_FOR trigger"
                    )
                if blocking_pairs:
                    raise ValueError("DEFER truth must not satisfy a complete blocking construction")
            else:
                if any(
                    value is not None
                    for value in (
                        action.expected_blocking_requirement_id,
                        action.expected_blocked_scope_id,
                        action.expected_defer_until_id,
                    )
                ):
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} {action.expected_disposition.value} truth must have null pointers"
                    )
                if blocking_pairs:
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} non-BLOCKING truth satisfies a complete blocking construction"
                    )
                if wait_triggers:
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} non-DEFER truth has an active WAITS_FOR relation"
                    )

    expected_reasoner_calls = 4 * 3 * 3
    if int(benchmark.call_plan["planned_reasoner_calls"]) != expected_reasoner_calls:
        raise ValueError("frozen reasoner call count must be 36")
    if int(benchmark.call_plan["planned_judge_calls"]) != expected_reasoner_calls:
        raise ValueError("frozen judge call count must be 36")
    if int(benchmark.call_plan["planned_successful_calls"]) != 72:
        raise ValueError("frozen planned successful provider calls must be 72")
    if int(benchmark.call_plan["max_total_provider_attempts"]) != 90:
        raise ValueError("frozen provider-attempt ceiling must be 90")
    if int(benchmark.call_plan["max_retries_per_planned_call"]) != 1:
        raise ValueError("frozen retry maximum must be one per planned call")


def _require_unique(values: Sequence[str], label: str) -> None:
    if any(not value.strip() for value in values):
        raise ValueError(f"{label} must contain non-empty values")
    if len(values) != len(set(values)):
        raise ValueError(f"{label} must be unique")


def _valid_blocking_pairs(
    case: RecommendationExperimentCase,
    action_id: str,
) -> set[tuple[str, str]]:
    unresolved = {
        item.requirement_id for item in case.requirements if item.status == "UNRESOLVED"
    }
    active_scopes = {
        item.scope_id
        for item in case.downstream_scopes
        if item.active and item.intended_to_be_defended
    }
    resolved_requirements = {
        item.requirement_id
        for item in case.action_requirement_relations
        if item.action_id == action_id and item.relation == "RESOLVES"
    }
    pairs: set[tuple[str, str]] = set()
    for relation in case.scope_requirement_relations:
        if (
            relation.relation == "DEPENDS_ON"
            and relation.scope_id in active_scopes
            and relation.requirement_id in unresolved
            and relation.requirement_id in resolved_requirements
        ):
            pairs.add((relation.requirement_id, relation.scope_id))
    return pairs


def _valid_wait_triggers(case: RecommendationExperimentCase, action_id: str) -> set[str]:
    unresolved = {
        item.trigger_id for item in case.defer_triggers if item.status == "UNRESOLVED"
    }
    return {
        item.trigger_id
        for item in case.action_trigger_relations
        if item.action_id == action_id
        and item.relation == "WAITS_FOR"
        and item.trigger_id in unresolved
    }


def build_reasoning_plan(
    benchmark: FrozenRecommendationBenchmark,
) -> tuple[RecommendationPlanEntry, ...]:
    """Build the frozen block-randomized 36-call reasoner plan."""

    rng = random.Random(benchmark.randomization_seed)
    entries: list[RecommendationPlanEntry] = []
    ordinal = 0
    for case in benchmark.cases:
        for repetition in range(1, benchmark.repetitions + 1):
            conditions = list(RecommendationCondition)
            rng.shuffle(conditions)
            for condition in conditions:
                ordinal += 1
                opaque = hashlib.sha256(
                    (
                        f"{benchmark.benchmark_id}|{benchmark.randomization_seed}|{ordinal}|"
                        f"{case.case_id}|{repetition}|{condition.value}"
                    ).encode("utf-8")
                ).hexdigest()
                entries.append(
                    RecommendationPlanEntry(
                        output_id=f"dbra-{opaque[:16]}",
                        run_nonce=f"nonce-{opaque[16:40]}",
                        case_id=case.case_id,
                        repetition=repetition,
                        condition=condition,
                    )
                )
    if len(entries) != 36:
        raise AssertionError("internal Specification 021 plan cardinality error")
    return tuple(entries)


def build_judge_plan(
    output_ids: Sequence[str],
    *,
    randomization_seed: int,
) -> tuple[JudgePlanEntry, ...]:
    ids = list(output_ids)
    _require_unique(ids, "reasoner output IDs")
    rng = random.Random(randomization_seed ^ 0x21D3A77B)
    rng.shuffle(ids)
    return tuple(
        JudgePlanEntry(
            judge_id="dbra-judge-"
            + hashlib.sha256(
                f"{randomization_seed}|{position}|{output_id}".encode("utf-8")
            ).hexdigest()[:16],
            output_id=output_id,
        )
        for position, output_id in enumerate(ids, start=1)
    )


def serialize_reasoning_plan(
    plan: Sequence[RecommendationPlanEntry],
) -> tuple[str, str]:
    payload = [
        {
            "output_id": item.output_id,
            "run_nonce": item.run_nonce,
            "case_id": item.case_id,
            "repetition": item.repetition,
            "condition": item.condition.value,
        }
        for item in plan
    ]
    text = _canonical_json(payload)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def serialize_judge_plan(plan: Sequence[JudgePlanEntry]) -> tuple[str, str]:
    text = _canonical_json([asdict(item) for item in plan])
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_system_provenance_plan(
    reasoning_plan: Sequence[RecommendationPlanEntry],
    contexts: Mapping[tuple[str, RecommendationCondition], RecommendationConditionInput],
) -> tuple[SystemProvenancePlanEntry, ...]:
    result = tuple(
        SystemProvenancePlanEntry(
            output_id=item.output_id,
            run_nonce=item.run_nonce,
            case_id=item.case_id,
            repetition=item.repetition,
            provenance=contexts[(item.case_id, item.condition)].provenance,
        )
        for item in reasoning_plan
    )
    if len(result) != 36:
        raise ValueError("system provenance plan must contain exactly 36 entries")
    return result


def serialize_system_provenance_plan(
    plan: Sequence[SystemProvenancePlanEntry],
) -> tuple[str, str]:
    payload = [
        {
            "output_id": item.output_id,
            "run_nonce": item.run_nonce,
            "case_id": item.case_id,
            "repetition": item.repetition,
            "provenance": item.provenance.to_payload(),
        }
        for item in plan
    ]
    text = _canonical_json(payload)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def case_by_id(
    benchmark: FrozenRecommendationBenchmark,
    case_id: str,
) -> RecommendationExperimentCase:
    matches = [item for item in benchmark.cases if item.case_id == case_id]
    if len(matches) != 1:
        raise KeyError(f"unknown case_id: {case_id}")
    return matches[0]


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
                    f"FULL_HORIZON candidate {candidate.stable_key!r} is no longer accepted-current"
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
    return MethodologicalContextPack(
        schema_version=1,
        task_id=request.task_id,
        requested_reasoning_functions=tuple(sorted(request.requested_reasoning_functions)),
        knowledge=tuple(items),
        missing_context_keys=tuple(
            sorted({key for item in items for key in item.missing_context_keys})
        ),
    )


def build_condition_input(
    condition: RecommendationCondition,
    horizon: MethodologicalHorizon,
    request: MethodologicalContextRequest,
    *,
    uow_factory,
) -> RecommendationConditionInput:
    if condition is RecommendationCondition.GENERIC:
        digest, size = _digest_payload(GENERIC_CONTEXT_PAYLOAD)
        return RecommendationConditionInput(
            condition=condition,
            payload=GENERIC_CONTEXT_PAYLOAD,
            sha256=digest,
            utf8_bytes=size,
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
        raise ValueError(f"unsupported condition: {condition!r}")

    serialized = serialize_methodological_context_pack(pack)
    revisions = tuple(
        KnowledgeRevisionPointer(item.asset.stable_key, item.asset.revision_id)
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


def validate_frozen_condition_sets(
    benchmark: FrozenRecommendationBenchmark,
    horizon: MethodologicalHorizon,
    *,
    max_assets: int,
    uow_factory,
) -> None:
    """Fail closed if any frozen GENERIC/SELECTIVE/FULL treatment has drifted."""

    if len(horizon.included) != 10:
        raise ValueError("FULL_HORIZON requires exactly ten included assets")
    full_expected = {(item.stable_key, item.revision_id) for item in horizon.included}
    if {item.stable_key for item in horizon.included} != set(benchmark.full_horizon_keys):
        raise ValueError("wide Horizon stable-key set differs from frozen FULL_HORIZON")

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
        if generic.revisions or generic.payload or generic.provenance.supplied_revisions:
            raise ValueError(f"{case.case_id} GENERIC contains methodology")

        selective = build_condition_input(
            RecommendationCondition.SELECTIVE,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        if {item.stable_key for item in selective.revisions} != set(case.required_selective_keys):
            raise ValueError(f"{case.case_id} SELECTIVE exact stable-key set drifted")

        full = build_condition_input(
            RecommendationCondition.FULL_HORIZON,
            horizon,
            request,
            uow_factory=uow_factory,
        )
        if {(item.stable_key, item.revision_id) for item in full.revisions} != full_expected:
            raise ValueError(f"{case.case_id} FULL_HORIZON exact revisions drifted")


def build_reasoning_request(
    *,
    benchmark: FrozenRecommendationBenchmark,
    case: RecommendationExperimentCase,
    plan_entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
) -> ReasoningRequest:
    """Build one matched request while excluding all hidden evaluator truth."""

    if case.case_id != plan_entry.case_id or context.condition is not plan_entry.condition:
        raise ValueError("plan entry, case, and context do not match")
    request = ReasoningRequest(
        run_id=plan_entry.output_id,
        run_nonce=plan_entry.run_nonce,
        system_instruction=benchmark.common_reasoner_instruction,
        user_task=case.user_task,
        project_evidence={
            "project_evidence": dict(case.project_evidence),
            "task_menu": case.model_task_payload(),
        },
        methodological_context_payload=context.payload,
        methodological_context_sha256=context.sha256,
        knowledge_revisions=context.revisions,
        model_configuration=benchmark.reasoner_model,
        structured_output_type=DependencyBackedRecommendationActionResult,
    )
    assert_evaluator_truth_absent(request)
    return request


def assert_evaluator_truth_absent(request: ReasoningRequest) -> None:
    text = request.canonical_model_input()
    forbidden = (
        "expected_disposition",
        "expected_blocking_requirement_id",
        "expected_blocked_scope_id",
        "expected_defer_until_id",
        '"critical"',
        '"rubric"',
        '"cost_units"',
        "promotion_value_signals",
        "absolute_gate",
        "relative_gate",
        "expansion_gate",
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"evaluator truth leaked into reasoner input: {leaked}")


def validate_dependency_backed_result(
    case: RecommendationExperimentCase,
    result: DependencyBackedRecommendationActionResult,
) -> DependencyBackedRecommendationActionResult:
    """Validate exact action coverage and the supplied relation-pointer semantics."""

    expected_actions = set(case.candidate_action_ids)
    observed_actions = {item.action_id for item in result.action_decisions}
    missing = sorted(expected_actions - observed_actions)
    unknown = sorted(observed_actions - expected_actions)
    if missing or unknown:
        raise ValueError(
            "action coverage must exactly match supplied menu; "
            f"missing={missing}, unknown={unknown}"
        )

    requirement_ids = set(case.requirement_ids)
    scope_ids = set(case.scope_ids)
    trigger_ids = set(case.trigger_ids)
    for decision in result.action_decisions:
        for field_name, value, valid_ids in (
            ("blocking_requirement_id", decision.blocking_requirement_id, requirement_ids),
            ("blocked_scope_id", decision.blocked_scope_id, scope_ids),
            ("defer_until_id", decision.defer_until_id, trigger_ids),
        ):
            if value is not None and value not in valid_ids:
                raise ValueError(f"{decision.action_id} has unknown {field_name}: {value}")

        disposition = RecommendationDisposition(decision.disposition)
        if disposition is RecommendationDisposition.BLOCKING_REQUIRED:
            if decision.blocking_requirement_id is None or decision.blocked_scope_id is None:
                raise ValueError(
                    f"{decision.action_id} BLOCKING_REQUIRED requires requirement and scope pointers"
                )
            if decision.defer_until_id is not None:
                raise ValueError(f"{decision.action_id} BLOCKING_REQUIRED requires null defer pointer")
            if (
                decision.blocking_requirement_id,
                decision.blocked_scope_id,
            ) not in _valid_blocking_pairs(case, decision.action_id):
                raise ValueError(
                    f"{decision.action_id} BLOCKING_REQUIRED pointers lack a complete supplied blocking construction"
                )
        elif disposition is RecommendationDisposition.DEFER:
            if decision.blocking_requirement_id is not None or decision.blocked_scope_id is not None:
                raise ValueError(f"{decision.action_id} DEFER requires null blocking pointers")
            if decision.defer_until_id not in _valid_wait_triggers(case, decision.action_id):
                raise ValueError(
                    f"{decision.action_id} DEFER must point to one unresolved supplied WAITS_FOR trigger"
                )
        else:
            if any(
                value is not None
                for value in (
                    decision.blocking_requirement_id,
                    decision.blocked_scope_id,
                    decision.defer_until_id,
                )
            ):
                raise ValueError(
                    f"{decision.action_id} {disposition.value} requires all relation pointers null"
                )
    return result


def evaluate_recommendation_result(
    case: RecommendationExperimentCase,
    result: DependencyBackedRecommendationActionResult,
) -> RecommendationMetrics:
    """Compute the frozen deterministic recommendation metrics."""

    validate_dependency_backed_result(case, result)
    expected = {item.action_id: item for item in case.candidate_actions}
    decisions = {item.action_id: item for item in result.action_decisions}
    exact = 0
    critical_omissions = 0
    under = 0
    over = 0
    unnecessary_cost = 0
    blocking_false_positives = 0
    blocking_pointer_errors = 0
    defer_pointer_errors = 0

    for action_id, action in expected.items():
        decision = decisions[action_id]
        predicted = RecommendationDisposition(decision.disposition)
        if predicted is action.expected_disposition:
            exact += 1
        if (
            action.expected_disposition is RecommendationDisposition.BLOCKING_REQUIRED
            and predicted is not RecommendationDisposition.BLOCKING_REQUIRED
        ):
            critical_omissions += 1
        if (
            action.expected_disposition is RecommendationDisposition.RECOMMENDED
            and predicted in {RecommendationDisposition.DEFER, RecommendationDisposition.NOT_NOW}
        ):
            under += 1
        if (
            action.expected_disposition in {RecommendationDisposition.DEFER, RecommendationDisposition.NOT_NOW}
            and predicted in {RecommendationDisposition.RECOMMENDED, RecommendationDisposition.BLOCKING_REQUIRED}
        ):
            over += 1
            unnecessary_cost += action.cost_units
        if (
            action.expected_disposition is not RecommendationDisposition.BLOCKING_REQUIRED
            and predicted is RecommendationDisposition.BLOCKING_REQUIRED
        ):
            blocking_false_positives += 1

        if action.expected_disposition is RecommendationDisposition.BLOCKING_REQUIRED:
            if (
                predicted is not RecommendationDisposition.BLOCKING_REQUIRED
                or decision.blocking_requirement_id != action.expected_blocking_requirement_id
                or decision.blocked_scope_id != action.expected_blocked_scope_id
            ):
                blocking_pointer_errors += 1
        elif decision.blocking_requirement_id is not None or decision.blocked_scope_id is not None:
            blocking_pointer_errors += 1

        if action.expected_disposition is RecommendationDisposition.DEFER:
            if (
                predicted is not RecommendationDisposition.DEFER
                or decision.defer_until_id != action.expected_defer_until_id
            ):
                defer_pointer_errors += 1
        elif decision.defer_until_id is not None:
            defer_pointer_errors += 1

    return RecommendationMetrics(
        exact_disposition_accuracy=exact / len(case.candidate_actions),
        critical_action_omissions=critical_omissions,
        under_recommendations=under,
        over_recommendations=over,
        unnecessary_recommended_cost=unnecessary_cost,
        blocking_false_positives=blocking_false_positives,
        blocking_pointer_errors=blocking_pointer_errors,
        defer_pointer_errors=defer_pointer_errors,
    )


def build_judge_payload(
    case: RecommendationExperimentCase,
    *,
    output_id: str,
    result: DependencyBackedRecommendationActionResult,
) -> JudgePayload:
    payload = JudgePayload(
        output_id=output_id,
        user_task=case.user_task,
        project_evidence=dict(case.project_evidence),
        task_menu=case.model_task_payload(),
        rubric=case.rubric,
        candidate_result=result.to_payload(),
    )
    text = _canonical_json(payload.to_payload())
    forbidden = (
        "GENERIC",
        "SELECTIVE",
        "FULL_HORIZON",
        "methodological_context",
        "selection_reason",
        "knowledge_revisions",
        "methodology_payload_sha256",
        "input_tokens",
        "latency_seconds",
        "expected_disposition",
        "expected_blocking_requirement_id",
        "expected_blocked_scope_id",
        "expected_defer_until_id",
        '"cost_units"',
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"condition/context/evaluator metadata leaked into judge payload: {leaked}")
    return payload


def validate_judge_result(
    case: RecommendationExperimentCase,
    result: JudgeResult,
) -> JudgeResult:
    expected_ids = [item.obligation_id for item in case.rubric]
    observed_ids = [item.obligation_id for item in result.obligation_scores]
    if observed_ids != expected_ids:
        raise ValueError(
            f"judge obligation IDs/order drifted for {case.case_id}: "
            f"expected {expected_ids}, observed {observed_ids}"
        )
    recomputed = sum(item.score for item in result.obligation_scores) / (
        2 * len(result.obligation_scores)
    )
    if abs(recomputed - result.normalized_score) > 1e-9:
        raise ValueError("judge normalized score is inconsistent with obligation scores")
    critical_ids = {item.obligation_id for item in case.rubric if item.critical}
    critical_failure = any(
        item.obligation_id in critical_ids and item.score == 0
        for item in result.obligation_scores
    )
    if critical_failure != result.critical_failure:
        raise ValueError("judge critical_failure is inconsistent with frozen rubric")
    return result


def evaluate_gates(
    benchmark: FrozenRecommendationBenchmark,
    observations: Sequence[RecommendationScoredObservation],
) -> RecommendationGateEvaluation:
    """Apply all frozen absolute, relative, expansion, and value rules."""

    if len(observations) != 36:
        raise ValueError(f"gate evaluation requires 36 scored observations, got {len(observations)}")
    by_key: dict[tuple[str, RecommendationCondition, int], RecommendationScoredObservation] = {}
    for item in observations:
        key = (item.case_id, item.condition, item.repetition)
        if key in by_key:
            raise ValueError(f"duplicate scored observation: {key}")
        if item.output_id != item.judge_result.output_id:
            raise ValueError("observation output ID differs from judge output ID")
        by_key[key] = item

    aggregate = {
        condition: _aggregate(
            [item for item in observations if item.condition is condition]
        )
        for condition in RecommendationCondition
    }
    per_case_exact: dict[str, dict[str, float]] = {}
    per_case_semantic: dict[str, dict[str, float]] = {}
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

    selective = aggregate[RecommendationCondition.SELECTIVE]
    generic = aggregate[RecommendationCondition.GENERIC]
    full = aggregate[RecommendationCondition.FULL_HORIZON]
    a = benchmark.absolute_gate
    r = benchmark.relative_gate
    gates: dict[str, bool] = {}

    gates["DBRA-G01"] = selective.critical_action_omissions <= int(
        a["selective_max_critical_action_omissions"]
    )
    gates["DBRA-G02"] = selective.blocking_false_positives <= int(
        a["selective_max_blocking_false_positives"]
    )
    gates["DBRA-G03"] = selective.blocking_pointer_errors <= int(
        a["selective_max_blocking_pointer_errors"]
    )
    gates["DBRA-G04"] = selective.defer_pointer_errors <= int(
        a["selective_max_defer_pointer_errors"]
    )
    gates["DBRA-G05"] = selective.exact_disposition_accuracy >= float(
        a["selective_min_aggregate_exact_disposition_accuracy"]
    )
    gates["DBRA-G06"] = all(
        per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_exact_disposition_accuracy"])
        for case in benchmark.cases
    )
    gates["DBRA-G07"] = selective.semantic_score >= float(
        a["selective_min_aggregate_semantic_score"]
    )
    gates["DBRA-G08"] = all(
        per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_semantic_score"])
        for case in benchmark.cases
    )

    gates["DBRA-G09"] = selective.exact_disposition_accuracy >= (
        generic.exact_disposition_accuracy
        + float(r["selective_minus_generic_aggregate_exact_accuracy_floor"])
    )
    gates["DBRA-G10"] = all(
        per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= per_case_exact[case.case_id][RecommendationCondition.GENERIC.value]
        + float(r["selective_minus_generic_per_case_exact_accuracy_floor"])
        for case in benchmark.cases
    )
    gates["DBRA-G11"] = selective.exact_disposition_accuracy >= (
        full.exact_disposition_accuracy
        + float(r["selective_minus_full_aggregate_exact_accuracy_floor"])
    )
    gates["DBRA-G12"] = all(
        per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= per_case_exact[case.case_id][RecommendationCondition.FULL_HORIZON.value]
        + float(r["selective_minus_full_per_case_exact_accuracy_floor"])
        for case in benchmark.cases
    )
    gates["DBRA-G13"] = selective.semantic_score >= (
        generic.semantic_score
        + float(r["selective_minus_generic_aggregate_semantic_floor"])
    )
    gates["DBRA-G14"] = all(
        per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= per_case_semantic[case.case_id][RecommendationCondition.GENERIC.value]
        + float(r["selective_minus_generic_per_case_semantic_floor"])
        for case in benchmark.cases
    )
    gates["DBRA-G15"] = selective.semantic_score >= (
        full.semantic_score
        + float(r["selective_minus_full_aggregate_semantic_floor"])
    )
    gates["DBRA-G16"] = all(
        per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= per_case_semantic[case.case_id][RecommendationCondition.FULL_HORIZON.value]
        + float(r["selective_minus_full_per_case_semantic_floor"])
        for case in benchmark.cases
    )
    gates["DBRA-G17"] = selective.critical_action_omissions <= generic.critical_action_omissions
    gates["DBRA-G18"] = selective.blocking_false_positives <= generic.blocking_false_positives
    gates["DBRA-G19"] = selective.under_recommendations <= generic.under_recommendations
    gates["DBRA-G20"] = selective.defer_pointer_errors <= generic.defer_pointer_errors

    gates["DBRA-G21"] = (
        selective.unnecessary_recommended_cost <= full.unnecessary_recommended_cost
    )
    gates["DBRA-G22"] = selective.over_recommendations <= full.over_recommendations
    gates["DBRA-G23"] = selective.blocking_false_positives <= full.blocking_false_positives

    absolute_passed = all(gates[f"DBRA-G{index:02d}"] for index in range(1, 9))
    relative_passed = all(gates[f"DBRA-G{index:02d}"] for index in range(9, 21))
    expansion_passed = all(gates[f"DBRA-G{index:02d}"] for index in range(21, 24))

    value_signals: list[str] = []
    if selective.exact_disposition_accuracy >= generic.exact_disposition_accuracy + 0.05:
        value_signals.append("S1")
    if selective.semantic_score >= generic.semantic_score + 0.05:
        value_signals.append("S2")
    if selective.critical_action_omissions < generic.critical_action_omissions:
        value_signals.append("S3")
    if selective.blocking_false_positives < generic.blocking_false_positives:
        value_signals.append("S4")
    if selective.under_recommendations < generic.under_recommendations:
        value_signals.append("S5")
    if selective.defer_pointer_errors < generic.defer_pointer_errors:
        value_signals.append("S6")
    if selective.unnecessary_recommended_cost < full.unnecessary_recommended_cost:
        value_signals.append("S7")
    if selective.over_recommendations < full.over_recommendations:
        value_signals.append("S8")
    if selective.blocking_false_positives < full.blocking_false_positives:
        value_signals.append("S9")

    if not (absolute_passed and relative_passed and expansion_passed):
        outcome = AdvancementOutcome.FAIL
    elif value_signals:
        outcome = AdvancementOutcome.PROMOTE
    else:
        outcome = AdvancementOutcome.SAFE_NOT_DIFFERENTIATED

    return RecommendationGateEvaluation(
        outcome=outcome,
        absolute_passed=absolute_passed,
        relative_passed=relative_passed,
        expansion_passed=expansion_passed,
        gate_results=gates,
        value_signals=tuple(value_signals),
        aggregate_by_condition={item.value: aggregate[item] for item in RecommendationCondition},
        per_case_exact_accuracy=per_case_exact,
        per_case_semantic_score=per_case_semantic,
    )


def _aggregate(observations: Sequence[RecommendationScoredObservation]) -> ConditionAggregate:
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
        under_recommendations=sum(item.metrics.under_recommendations for item in observations),
        over_recommendations=sum(item.metrics.over_recommendations for item in observations),
        unnecessary_recommended_cost=sum(
            item.metrics.unnecessary_recommended_cost for item in observations
        ),
        blocking_false_positives=sum(
            item.metrics.blocking_false_positives for item in observations
        ),
        blocking_pointer_errors=sum(
            item.metrics.blocking_pointer_errors for item in observations
        ),
        defer_pointer_errors=sum(item.metrics.defer_pointer_errors for item in observations),
    )


def _mean(values) -> float:
    items = list(values)
    if not items:
        raise ValueError("mean requires at least one value")
    return sum(items) / len(items)


def canonical_core_payload(case: RecommendationExperimentCase) -> str:
    """Canonical condition-invariant project/action/relation payload for matched audits."""

    return _canonical_json(
        {
            "user_task": case.user_task,
            "project_evidence": dict(case.project_evidence),
            "task_menu": case.model_task_payload(),
        }
    )
