"""Provider-neutral harness for frozen Specification 019.

The harness owns the experiment semantics that must remain independent from the
live provider adapter: frozen-fixture validation, deterministic three-condition
planning, exact methodological-context construction, relation-backed structured
result validation, deterministic action/pointer metrics, blinded judge payloads,
and the preregistered three-way advancement rule.

No function in this module mutates authoritative project state. Evaluator truth
is retained in the fixture-side case objects and is deliberately omitted from
reasoner and judge inputs except for the semantic rubric explicitly allowed by
Specification 019.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
import hashlib
import json
from pathlib import Path
import random
import subprocess
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
    PROMOTE = "PROMOTE_SYSTEM_PROVENANCE_RECOMMENDATION_SEAM"
    SAFE_NOT_DIFFERENTIATED = "SAFE_BUT_NOT_DIFFERENTIATED"
    FAIL = "FAIL"


@dataclass(frozen=True, slots=True)
class SystemProvenanceActionDecision:
    """One structured disposition for one supplied candidate action."""

    action_id: str
    disposition: str
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
        if self.defer_until_id is not None and not self.defer_until_id.strip():
            raise ValueError("defer_until_id must be null or non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")

    def to_payload(self) -> dict[str, object]:
        return {
            "action_id": self.action_id,
            "disposition": self.disposition,
            "defer_until_id": self.defer_until_id,
            "rationale": self.rationale,
        }


@dataclass(frozen=True, slots=True)
class SystemProvenanceRecommendationActionResult:
    """Experiment-owned structured result for one Specification 019 call."""

    summary: str
    action_decisions: tuple[SystemProvenanceActionDecision, ...]
    blocked_scopes: tuple[str, ...]
    required_clarification_ids: tuple[str, ...]
    warnings: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.summary.strip():
            raise ValueError("summary must be non-empty")
        action_ids = [item.action_id for item in self.action_decisions]
        if len(action_ids) != len(set(action_ids)):
            raise ValueError("action_decisions must contain unique action IDs")
        for field_name in (
            "blocked_scopes",
            "required_clarification_ids",
            "warnings",
        ):
            values = getattr(self, field_name)
            if any(not value.strip() for value in values):
                raise ValueError(f"{field_name} cannot contain empty strings")
            if len(values) != len(set(values)):
                raise ValueError(f"{field_name} must not contain duplicates")

    def to_payload(self) -> dict[str, object]:
        return {
            "summary": self.summary,
            "action_decisions": [item.to_payload() for item in self.action_decisions],
            "blocked_scopes": list(self.blocked_scopes),
            "required_clarification_ids": list(self.required_clarification_ids),
            "warnings": list(self.warnings),
        }


@dataclass(frozen=True, slots=True)
class DeferTrigger:
    trigger_id: str
    description: str


@dataclass(frozen=True, slots=True)
class CandidateAction:
    action_id: str
    label: str
    cost_units: int
    expected_disposition: RecommendationDisposition
    expected_defer_until_id: str | None
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
    source_reasoning_case_id: str
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
    available_defer_triggers: tuple[DeferTrigger, ...]
    candidate_actions: tuple[CandidateAction, ...]
    rubric: tuple[RubricObligation, ...]

    @property
    def candidate_action_ids(self) -> tuple[str, ...]:
        return tuple(item.action_id for item in self.candidate_actions)

    @property
    def clarification_ids(self) -> tuple[str, ...]:
        return tuple(item.clarification_id for item in self.available_clarifications)

    @property
    def defer_trigger_ids(self) -> tuple[str, ...]:
        return tuple(item.trigger_id for item in self.available_defer_triggers)

    def model_task_payload(self) -> dict[str, object]:
        """Return condition-invariant task/menu evidence without evaluator truth."""

        return {
            "requested_reasoning_functions": list(self.requested_reasoning_functions),
            "candidate_actions": [
                {"action_id": item.action_id, "label": item.label}
                for item in self.candidate_actions
            ],
            "available_blocked_scopes": list(self.available_blocked_scopes),
            "available_clarifications": [
                {
                    "clarification_id": item.clarification_id,
                    "description": item.description,
                }
                for item in self.available_clarifications
            ],
            "available_defer_triggers": [
                {"trigger_id": item.trigger_id, "description": item.description}
                for item in self.available_defer_triggers
            ],
        }


@dataclass(frozen=True, slots=True)
class FrozenRecommendationBenchmark:
    benchmark_id: str
    starting_merge_sha: str
    randomization_seed: int
    repetitions: int
    common_reasoner_instruction: str
    reasoner_model: ReasoningModelConfiguration
    judge_model: ReasoningModelConfiguration
    call_plan: Mapping[str, object]
    absolute_gate: Mapping[str, object]
    relative_gate: Mapping[str, object]
    expansion_gate: Mapping[str, object]
    promotion_value_signals: Mapping[str, object]
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
    """System-owned exact provenance for one reasoner methodology payload."""

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
    blocking_scope_false_negatives: int
    blocking_scope_false_positives: int
    required_clarification_false_negatives: int
    required_clarification_false_positives: int
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
    blocking_scope_false_negatives: int
    blocking_scope_false_positives: int
    required_clarification_false_negatives: int
    required_clarification_false_positives: int
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


def _git_blob_sha(raw_bytes: bytes) -> str:
    header = f"blob {len(raw_bytes)}\0".encode("utf-8")
    return hashlib.sha1(header + raw_bytes).hexdigest()


def _repository_blob_sha(path: Path, *, repository_root: Path) -> str:
    """Resolve tracked Git object identity without depending on checkout line endings."""

    resolved_path = path.resolve()
    resolved_root = repository_root.resolve()
    try:
        relative = resolved_path.relative_to(resolved_root)
    except ValueError:
        return _git_blob_sha(path.read_bytes())

    completed = subprocess.run(
        ["git", "rev-parse", f"HEAD:{relative.as_posix()}"],
        cwd=resolved_root,
        check=False,
        capture_output=True,
        text=True,
    )
    observed = completed.stdout.strip()
    if completed.returncode == 0 and len(observed) == 40:
        return observed
    return _git_blob_sha(path.read_bytes())


def load_frozen_benchmark(path: Path) -> FrozenRecommendationBenchmark:
    """Load the Specification 019 overlay and fail closed on base-fixture drift."""

    overlay = json.loads(path.read_text(encoding="utf-8"))
    root = Path(__file__).resolve().parents[2]
    base_path = root / str(overlay["base_fixture"])
    base_bytes = base_path.read_bytes()
    observed_blob = _repository_blob_sha(base_path, repository_root=root)
    expected_blob = str(overlay["base_fixture_git_blob_sha"])
    if observed_blob != expected_blob:
        raise ValueError(
            "Specification 019 base fixture Git blob drifted: "
            f"expected {expected_blob}, observed {observed_blob}"
        )

    raw = json.loads(base_bytes.decode("utf-8"))
    raw["benchmark_id"] = str(overlay["benchmark_id"])
    raw["starting_merge_sha"] = str(overlay["starting_integration_head"])
    raw["randomization_seed"] = int(overlay["randomization_seed_override"])
    raw["absolute_gate"] = dict(overlay["absolute_gate"])

    delta = overlay["common_reasoner_instruction_delta"]
    instruction = str(raw["common_reasoner_instruction"])
    removed = str(delta["remove"])
    if removed not in instruction:
        raise ValueError("Specification 019 reasoner-instruction delta no longer matches base fixture")
    instruction = instruction.replace(removed, str(delta["add"]), 1)
    raw["common_reasoner_instruction"] = instruction

    cases = tuple(_load_case(item) for item in raw["cases"])
    reasoner = raw["reasoner"]
    judge = raw["judge"]
    benchmark = FrozenRecommendationBenchmark(
        benchmark_id=str(raw["benchmark_id"]),
        starting_merge_sha=str(raw["starting_merge_sha"]),
        randomization_seed=int(raw["randomization_seed"]),
        repetitions=int(raw["reasoner_repetitions_per_condition"]),
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
        cases=cases,
    )
    validate_fixture_construction(benchmark, raw_conditions=tuple(raw["conditions"]))
    return benchmark


def _load_case(raw: Mapping[str, object]) -> RecommendationExperimentCase:
    actions = tuple(
        CandidateAction(
            action_id=str(item["action_id"]),
            label=str(item["label"]),
            cost_units=int(item["cost_units"]),
            expected_disposition=RecommendationDisposition(str(item["expected_disposition"])),
            expected_defer_until_id=(
                None
                if item.get("expected_defer_until_id") is None
                else str(item["expected_defer_until_id"])
            ),
            critical=bool(item["critical"]),
        )
        for item in raw["candidate_actions"]  # type: ignore[index]
    )
    clarifications = tuple(
        ClarificationOption(str(item["clarification_id"]), str(item["description"]))
        for item in raw["available_clarifications"]  # type: ignore[index]
    )
    triggers = tuple(
        DeferTrigger(str(item["trigger_id"]), str(item["description"]))
        for item in raw["available_defer_triggers"]  # type: ignore[index]
    )
    rubric = tuple(
        RubricObligation(
            obligation_id=str(item["obligation_id"]),
            critical=bool(item["critical"]),
            description=str(item["description"]),
        )
        for item in raw["rubric"]  # type: ignore[index]
    )
    return RecommendationExperimentCase(
        case_id=str(raw["case_id"]),
        case_class=str(raw["class"]),
        source_reasoning_case_id=str(raw["source_reasoning_case_id"]),
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
        available_blocked_scopes=tuple(
            str(value) for value in raw["available_blocked_scopes"]  # type: ignore[index]
        ),
        expected_blocked_scopes=tuple(
            str(value) for value in raw["expected_blocked_scopes"]  # type: ignore[index]
        ),
        available_clarifications=clarifications,
        expected_required_clarification_ids=tuple(
            str(value)
            for value in raw["expected_required_clarification_ids"]  # type: ignore[index]
        ),
        available_defer_triggers=triggers,
        candidate_actions=actions,
        rubric=rubric,
    )


def validate_fixture_construction(
    benchmark: FrozenRecommendationBenchmark,
    *,
    raw_conditions: tuple[object, ...] | None = None,
) -> None:
    """Mechanically enforce the preregistered benchmark construction contract."""

    if len(benchmark.cases) != 4:
        raise ValueError("Specification 019 requires exactly four cases")
    if len({case.case_id for case in benchmark.cases}) != 4:
        raise ValueError("Specification 019 case IDs must be unique")
    if benchmark.repetitions != 3:
        raise ValueError("Specification 019 requires exactly three repetitions")
    if raw_conditions is not None:
        observed = {str(value) for value in raw_conditions}
        expected = {item.value for item in RecommendationCondition}
        if observed != expected:
            raise ValueError(
                f"condition set drifted: expected {sorted(expected)}, observed {sorted(observed)}"
            )

    expected_selective_sets = {
        "RB-01": {"prediction-moment", "prediction-time-feature-eligibility", "temporal-validation"},
        "RB-02": {"random-forest", "gradient-boosted-trees"},
        "RB-03": {"histogram", "ecdf"},
        "RB-04": {"class-imbalance", "missing-data"},
    }
    for case in benchmark.cases:
        if set(case.required_selective_keys) != expected_selective_sets[case.case_id]:
            raise ValueError(f"{case.case_id} frozen selective keys drifted")
        if len(case.candidate_actions) < 1:
            raise ValueError(f"{case.case_id} requires candidate actions")
        if len(case.candidate_action_ids) != len(set(case.candidate_action_ids)):
            raise ValueError(f"{case.case_id} candidate action IDs must be unique")
        if len(case.clarification_ids) != len(set(case.clarification_ids)):
            raise ValueError(f"{case.case_id} clarification IDs must be unique")
        if len(case.defer_trigger_ids) != len(set(case.defer_trigger_ids)):
            raise ValueError(f"{case.case_id} defer trigger IDs must be unique")
        if not set(case.expected_blocked_scopes).issubset(case.available_blocked_scopes):
            raise ValueError(f"{case.case_id} expected blocked scopes must be supplied")
        if not set(case.expected_required_clarification_ids).issubset(case.clarification_ids):
            raise ValueError(f"{case.case_id} expected clarifications must be supplied")
        trigger_ids = set(case.defer_trigger_ids)
        for action in case.candidate_actions:
            if action.cost_units <= 0:
                raise ValueError(f"{case.case_id} action costs must be positive")
            if action.expected_disposition is RecommendationDisposition.DEFER:
                if action.expected_defer_until_id not in trigger_ids:
                    raise ValueError(
                        f"{case.case_id}/{action.action_id} DEFER truth must point to a supplied trigger"
                    )
            elif action.expected_defer_until_id is not None:
                raise ValueError(
                    f"{case.case_id}/{action.action_id} non-DEFER truth must have null pointer"
                )
        if not case.rubric:
            raise ValueError(f"{case.case_id} rubric must not be empty")
        rubric_ids = [item.obligation_id for item in case.rubric]
        if len(rubric_ids) != len(set(rubric_ids)):
            raise ValueError(f"{case.case_id} rubric IDs must be unique")

    expected_reasoner = 4 * 3 * 3
    if int(benchmark.call_plan["planned_reasoner_calls"]) != expected_reasoner:
        raise ValueError("frozen reasoner call count must be 36")
    if int(benchmark.call_plan["planned_judge_calls"]) != expected_reasoner:
        raise ValueError("frozen judge call count must be 36")
    if int(benchmark.call_plan["planned_successful_calls"]) != 72:
        raise ValueError("frozen successful provider call count must be 72")
    if int(benchmark.call_plan["max_total_provider_attempts"]) != 90:
        raise ValueError("frozen maximum provider attempts must be 90")
    if int(benchmark.call_plan["max_retries_per_planned_call"]) != 1:
        raise ValueError("frozen maximum retries per planned call must be one")


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
                        output_id=f"spra-{opaque[:16]}",
                        run_nonce=f"nonce-{opaque[16:40]}",
                        case_id=case.case_id,
                        repetition=repetition,
                        condition=condition,
                    )
                )
    if len(entries) != 36:
        raise AssertionError("internal Specification 019 plan cardinality error")
    return tuple(entries)


def build_judge_plan(
    output_ids: Sequence[str],
    *,
    randomization_seed: int,
) -> tuple[JudgePlanEntry, ...]:
    ids = list(output_ids)
    if len(ids) != len(set(ids)):
        raise ValueError("output_ids must be unique")
    rng = random.Random(randomization_seed ^ 0x17B4A913)
    rng.shuffle(ids)
    return tuple(
        JudgePlanEntry(
            judge_id="spra-judge-"
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
    """Bind every planned output to immutable system-owned context provenance."""

    result: list[SystemProvenancePlanEntry] = []
    for item in reasoning_plan:
        context = contexts[(item.case_id, item.condition)]
        result.append(
            SystemProvenancePlanEntry(
                output_id=item.output_id,
                run_nonce=item.run_nonce,
                case_id=item.case_id,
                repetition=item.repetition,
                provenance=context.provenance,
            )
        )
    return tuple(result)


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
        raise ValueError(
            f"FULL_HORIZON requires exactly ten included assets, observed {len(horizon.included)}"
        )
    full_expected = {
        (item.stable_key, item.revision_id) for item in horizon.included
    }
    for case in benchmark.cases:
        request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=max_assets,
        )
        generic = build_condition_input(
            RecommendationCondition.GENERIC, horizon, request, uow_factory=uow_factory
        )
        if generic.revisions or generic.payload:
            raise ValueError(f"{case.case_id} GENERIC contains methodological knowledge")

        selective = build_condition_input(
            RecommendationCondition.SELECTIVE, horizon, request, uow_factory=uow_factory
        )
        observed_selective = {item.stable_key for item in selective.revisions}
        if observed_selective != set(case.required_selective_keys):
            raise ValueError(
                f"{case.case_id} SELECTIVE set drifted: expected "
                f"{sorted(case.required_selective_keys)}, observed {sorted(observed_selective)}"
            )

        full = build_condition_input(
            RecommendationCondition.FULL_HORIZON, horizon, request, uow_factory=uow_factory
        )
        observed_full = {(item.stable_key, item.revision_id) for item in full.revisions}
        if observed_full != full_expected:
            raise ValueError(f"{case.case_id} FULL_HORIZON exact revisions drifted")


def build_reasoning_request(
    *,
    benchmark: FrozenRecommendationBenchmark,
    case: RecommendationExperimentCase,
    plan_entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
) -> ReasoningRequest:
    """Build one condition-matched request with hidden evaluator truth excluded."""

    if case.case_id != plan_entry.case_id:
        raise ValueError("plan entry case does not match case")
    if context.condition is not plan_entry.condition:
        raise ValueError("plan entry condition does not match context")
    project_evidence = {
        "project_evidence": dict(case.project_evidence),
        "task_menu": case.model_task_payload(),
    }
    request = ReasoningRequest(
        run_id=plan_entry.output_id,
        run_nonce=plan_entry.run_nonce,
        system_instruction=benchmark.common_reasoner_instruction,
        user_task=case.user_task,
        project_evidence=project_evidence,
        methodological_context_payload=context.payload,
        methodological_context_sha256=context.sha256,
        knowledge_revisions=context.revisions,
        model_configuration=benchmark.reasoner_model,
        structured_output_type=SystemProvenanceRecommendationActionResult,
    )
    assert_evaluator_truth_absent(request)
    return request


def assert_evaluator_truth_absent(request: ReasoningRequest) -> None:
    text = request.canonical_model_input()
    forbidden = (
        "expected_disposition",
        "expected_defer_until_id",
        "expected_blocked_scopes",
        "expected_required_clarification_ids",
        '"critical"',
        '"rubric"',
        '"cost_units"',
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"evaluator truth leaked into reasoner input: {leaked}")


def validate_system_provenance_result(
    case: RecommendationExperimentCase,
    result: SystemProvenanceRecommendationActionResult,
) -> SystemProvenanceRecommendationActionResult:
    expected_actions = set(case.candidate_action_ids)
    observed_actions = {item.action_id for item in result.action_decisions}
    missing = sorted(expected_actions - observed_actions)
    unknown = sorted(observed_actions - expected_actions)
    if missing or unknown:
        raise ValueError(
            "action coverage must exactly match supplied menu; "
            f"missing={missing}, unknown={unknown}"
        )
    unknown_scopes = sorted(set(result.blocked_scopes) - set(case.available_blocked_scopes))
    if unknown_scopes:
        raise ValueError(f"unknown blocked scopes: {unknown_scopes}")
    unknown_clarifications = sorted(
        set(result.required_clarification_ids) - set(case.clarification_ids)
    )
    if unknown_clarifications:
        raise ValueError(f"unknown clarification IDs: {unknown_clarifications}")

    valid_triggers = set(case.defer_trigger_ids)
    for decision in result.action_decisions:
        disposition = RecommendationDisposition(decision.disposition)
        if disposition is RecommendationDisposition.DEFER:
            if decision.defer_until_id not in valid_triggers:
                raise ValueError(
                    f"{decision.action_id} DEFER must point to one supplied trigger"
                )
        elif decision.defer_until_id is not None:
            raise ValueError(
                f"{decision.action_id} non-DEFER disposition must have null defer pointer"
            )

    return result


def evaluate_recommendation_result(
    case: RecommendationExperimentCase,
    result: SystemProvenanceRecommendationActionResult,
) -> RecommendationMetrics:
    """Compute all frozen deterministic metrics from hidden evaluator truth."""

    validate_system_provenance_result(case, result)
    expected = {item.action_id: item for item in case.candidate_actions}
    decisions = {item.action_id: item for item in result.action_decisions}
    exact = 0
    critical_omissions = 0
    under = 0
    over = 0
    unnecessary_cost = 0
    pointer_errors = 0

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
        if action.expected_disposition is RecommendationDisposition.DEFER:
            if predicted is not RecommendationDisposition.DEFER or (
                decision.defer_until_id != action.expected_defer_until_id
            ):
                pointer_errors += 1
        elif decision.defer_until_id is not None:
            pointer_errors += 1

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
        required_clarification_false_positives=len(
            predicted_clarifications - expected_clarifications
        ),
        defer_pointer_errors=pointer_errors,
    )


def build_judge_payload(
    case: RecommendationExperimentCase,
    *,
    output_id: str,
    result: SystemProvenanceRecommendationActionResult,
) -> JudgePayload:
    """Construct the condition/context/usage-blinded semantic judge payload."""

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
        "input_tokens",
        "latency_seconds",
        "expected_disposition",
        "expected_defer_until_id",
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"condition/evaluator metadata leaked into judge payload: {leaked}")
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
    """Apply the frozen Specification 019 quality, relative, expansion, and value rules."""

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
        condition: _aggregate([item for item in observations if item.condition is condition])
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
            exact_row[condition.value] = _mean(item.metrics.exact_disposition_accuracy for item in items)
            semantic_row[condition.value] = _mean(item.judge_result.normalized_score for item in items)
        per_case_exact[case.case_id] = exact_row
        per_case_semantic[case.case_id] = semantic_row

    s = aggregate[RecommendationCondition.SELECTIVE]
    g = aggregate[RecommendationCondition.GENERIC]
    f = aggregate[RecommendationCondition.FULL_HORIZON]
    a = benchmark.absolute_gate
    r = benchmark.relative_gate
    gates: dict[str, bool] = {}

    gates["SPRA-G01"] = s.critical_action_omissions <= int(a["selective_max_critical_action_omissions"])
    gates["SPRA-G02"] = s.blocking_scope_false_negatives <= int(a["selective_max_blocking_scope_false_negatives"])
    gates["SPRA-G03"] = s.defer_pointer_errors <= int(a["selective_max_defer_pointer_errors"])
    gates["SPRA-G04"] = s.required_clarification_false_negatives <= int(a["selective_max_required_clarification_false_negatives"])
    gates["SPRA-G05"] = s.exact_disposition_accuracy >= float(a["selective_min_aggregate_exact_disposition_accuracy"])
    gates["SPRA-G06"] = all(
        per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_exact_disposition_accuracy"])
        for case in benchmark.cases
    )
    gates["SPRA-G07"] = s.semantic_score >= float(a["selective_min_aggregate_semantic_score"])
    gates["SPRA-G08"] = all(
        per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
        >= float(a["selective_min_per_case_semantic_score"])
        for case in benchmark.cases
    )

    gates["SPRA-G09"] = (
        s.exact_disposition_accuracy >= g.exact_disposition_accuracy + float(r["selective_minus_generic_aggregate_exact_accuracy_floor"])
        and all(
            per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_exact[case.case_id][RecommendationCondition.GENERIC.value]
            + float(r["selective_minus_generic_per_case_exact_accuracy_floor"])
            for case in benchmark.cases
        )
    )
    gates["SPRA-G10"] = (
        s.exact_disposition_accuracy >= f.exact_disposition_accuracy + float(r["selective_minus_full_aggregate_exact_accuracy_floor"])
        and all(
            per_case_exact[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_exact[case.case_id][RecommendationCondition.FULL_HORIZON.value]
            + float(r["selective_minus_full_per_case_exact_accuracy_floor"])
            for case in benchmark.cases
        )
    )
    gates["SPRA-G11"] = (
        s.semantic_score >= g.semantic_score + float(r["selective_minus_generic_aggregate_semantic_floor"])
        and all(
            per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_semantic[case.case_id][RecommendationCondition.GENERIC.value]
            + float(r["selective_minus_generic_per_case_semantic_floor"])
            for case in benchmark.cases
        )
    )
    gates["SPRA-G12"] = (
        s.semantic_score >= f.semantic_score + float(r["selective_minus_full_aggregate_semantic_floor"])
        and all(
            per_case_semantic[case.case_id][RecommendationCondition.SELECTIVE.value]
            >= per_case_semantic[case.case_id][RecommendationCondition.FULL_HORIZON.value]
            + float(r["selective_minus_full_per_case_semantic_floor"])
            for case in benchmark.cases
        )
    )
    gates["SPRA-G13"] = s.critical_action_omissions <= g.critical_action_omissions
    gates["SPRA-G14"] = s.blocking_scope_false_negatives <= g.blocking_scope_false_negatives
    gates["SPRA-G15"] = s.under_recommendations <= g.under_recommendations
    gates["SPRA-G16"] = s.required_clarification_false_negatives <= g.required_clarification_false_negatives
    gates["SPRA-G17"] = s.defer_pointer_errors <= g.defer_pointer_errors

    gates["SPRA-G18"] = s.unnecessary_recommended_cost <= f.unnecessary_recommended_cost
    gates["SPRA-G19"] = s.over_recommendations <= f.over_recommendations
    gates["SPRA-G20"] = s.blocking_scope_false_positives <= f.blocking_scope_false_positives
    gates["SPRA-G21"] = s.required_clarification_false_positives <= f.required_clarification_false_positives

    absolute_passed = all(gates[f"SPRA-G{number:02d}"] for number in range(1, 9))
    relative_passed = all(gates[f"SPRA-G{number:02d}"] for number in range(9, 18))
    expansion_passed = all(gates[f"SPRA-G{number:02d}"] for number in range(18, 22))

    value_signals: list[str] = []
    if s.exact_disposition_accuracy >= g.exact_disposition_accuracy + 0.05:
        value_signals.append("SELECTIVE_AGGREGATE_EXACT_ACCURACY_AT_LEAST_0_05_ABOVE_GENERIC")
    if s.semantic_score >= g.semantic_score + 0.05:
        value_signals.append("SELECTIVE_AGGREGATE_SEMANTIC_SCORE_AT_LEAST_0_05_ABOVE_GENERIC")
    if s.critical_action_omissions < g.critical_action_omissions:
        value_signals.append("SELECTIVE_FEWER_TOTAL_CRITICAL_OMISSIONS_THAN_GENERIC")
    if s.blocking_scope_false_negatives < g.blocking_scope_false_negatives:
        value_signals.append("SELECTIVE_FEWER_TOTAL_BLOCKING_SCOPE_FALSE_NEGATIVES_THAN_GENERIC")
    if s.under_recommendations < g.under_recommendations:
        value_signals.append("SELECTIVE_FEWER_TOTAL_UNDER_RECOMMENDATIONS_THAN_GENERIC")
    if s.required_clarification_false_negatives < g.required_clarification_false_negatives:
        value_signals.append("SELECTIVE_FEWER_TOTAL_REQUIRED_CLARIFICATION_FALSE_NEGATIVES_THAN_GENERIC")
    if s.defer_pointer_errors < g.defer_pointer_errors:
        value_signals.append("SELECTIVE_FEWER_TOTAL_DEFER_POINTER_ERRORS_THAN_GENERIC")
    if s.unnecessary_recommended_cost < f.unnecessary_recommended_cost:
        value_signals.append("SELECTIVE_LOWER_TOTAL_UNNECESSARY_RECOMMENDED_COST_THAN_FULL_HORIZON")
    if s.over_recommendations < f.over_recommendations:
        value_signals.append("SELECTIVE_FEWER_TOTAL_OVER_RECOMMENDATIONS_THAN_FULL_HORIZON")
    if s.blocking_scope_false_positives < f.blocking_scope_false_positives:
        value_signals.append("SELECTIVE_FEWER_TOTAL_BLOCKING_SCOPE_FALSE_POSITIVES_THAN_FULL_HORIZON")

    allowed = set(benchmark.promotion_value_signals["signals"])
    if not set(value_signals).issubset(allowed):
        raise AssertionError("computed a value signal not preregistered in the fixture")
    all_safety = absolute_passed and relative_passed and expansion_passed
    required_signals = int(benchmark.promotion_value_signals["minimum_required_signals"])
    if not all_safety:
        outcome = AdvancementOutcome.FAIL
    elif len(value_signals) >= required_signals:
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
        aggregate_by_condition={key.value: value for key, value in aggregate.items()},
        per_case_exact_accuracy=per_case_exact,
        per_case_semantic_score=per_case_semantic,
    )


def _aggregate(observations: Sequence[RecommendationScoredObservation]) -> ConditionAggregate:
    if not observations:
        raise ValueError("cannot aggregate an empty condition")
    return ConditionAggregate(
        exact_disposition_accuracy=_mean(item.metrics.exact_disposition_accuracy for item in observations),
        semantic_score=_mean(item.judge_result.normalized_score for item in observations),
        critical_action_omissions=sum(item.metrics.critical_action_omissions for item in observations),
        under_recommendations=sum(item.metrics.under_recommendations for item in observations),
        over_recommendations=sum(item.metrics.over_recommendations for item in observations),
        unnecessary_recommended_cost=sum(item.metrics.unnecessary_recommended_cost for item in observations),
        blocking_scope_false_negatives=sum(item.metrics.blocking_scope_false_negatives for item in observations),
        blocking_scope_false_positives=sum(item.metrics.blocking_scope_false_positives for item in observations),
        required_clarification_false_negatives=sum(item.metrics.required_clarification_false_negatives for item in observations),
        required_clarification_false_positives=sum(item.metrics.required_clarification_false_positives for item in observations),
        defer_pointer_errors=sum(item.metrics.defer_pointer_errors for item in observations),
    )


def _mean(values) -> float:
    items = list(values)
    if not items:
        raise ValueError("cannot compute mean of empty values")
    return sum(items) / len(items)
