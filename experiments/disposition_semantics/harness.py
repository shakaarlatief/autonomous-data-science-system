"""Framework-neutral harness for Specification 016.

The module owns the frozen benchmark semantics, contrastive fixture audit,
deterministic randomized call plan, provider-neutral request construction, exact
result validation, and deterministic gate evaluation. It deliberately contains
no provider SDK import and no reusable-methodology treatment logic.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from enum import StrEnum
import hashlib
import json
from pathlib import Path
import random
from typing import Mapping, Sequence

from ads_system.application.reasoning import (
    ReasoningModelConfiguration,
    ReasoningRequest,
)


EMPTY_CONTEXT_PAYLOAD: dict[str, object] = {}
EMPTY_CONTEXT_SHA256 = hashlib.sha256(b"{}").hexdigest()


class Disposition(StrEnum):
    DEFER = "DEFER"
    NOT_NOW = "NOT_NOW"


class DiagnosticOutcome(StrEnum):
    SUPPORTED = "DISPOSITION_BOUNDARY_SUPPORTED"
    NOT_SUPPORTED = "DISPOSITION_BOUNDARY_NOT_SUPPORTED"
    INCOMPLETE = "INCOMPLETE"


@dataclass(frozen=True, slots=True)
class DispositionSemanticsResult:
    """Experiment-only structured output for one Specification 016 call."""

    disposition: str
    defer_until_id: str | None
    rationale: str

    def __post_init__(self) -> None:
        try:
            normalized = Disposition(self.disposition)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"unsupported disposition: {self.disposition!r}") from exc
        object.__setattr__(self, "disposition", normalized.value)
        if self.defer_until_id is not None and not self.defer_until_id.strip():
            raise ValueError("defer_until_id must be null or non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")

    def to_payload(self) -> dict[str, object]:
        return {
            "disposition": self.disposition,
            "defer_until_id": self.defer_until_id,
            "rationale": self.rationale,
        }


@dataclass(frozen=True, slots=True)
class DeferTrigger:
    trigger_id: str
    description: str

    def __post_init__(self) -> None:
        if not self.trigger_id.strip():
            raise ValueError("trigger_id must be non-empty")
        if not self.description.strip():
            raise ValueError("trigger description must be non-empty")


@dataclass(frozen=True, slots=True)
class DispositionVariant:
    variant_id: str
    variant_evidence: Mapping[str, object]
    expected_disposition: Disposition
    expected_defer_until_id: str | None


@dataclass(frozen=True, slots=True)
class DispositionPair:
    pair_id: str
    domain: str
    action_id: str
    action_label: str
    triggers: tuple[DeferTrigger, ...]
    shared_project_evidence: Mapping[str, object]
    variants: tuple[DispositionVariant, ...]


@dataclass(frozen=True, slots=True)
class FrozenDispositionBenchmark:
    benchmark_id: str
    starting_merge_sha: str
    randomization_seed: int
    repetitions_per_variant: int
    common_instruction: str
    user_task: str
    reasoner_model: ReasoningModelConfiguration
    call_plan: Mapping[str, object]
    hard_gates: Mapping[str, object]
    pairs: tuple[DispositionPair, ...]


@dataclass(frozen=True, slots=True)
class DispositionPlanEntry:
    run_id: str
    run_nonce: str
    pair_id: str
    variant_id: str
    repetition: int


@dataclass(frozen=True, slots=True)
class DispositionObservation:
    pair_id: str
    variant_id: str
    repetition: int
    result: DispositionSemanticsResult


@dataclass(frozen=True, slots=True)
class GateEvaluation:
    completed: bool
    structured_validity_passed: bool
    aggregate_accuracy_passed: bool
    variant_majority_passed: bool
    pair_polarity_passed: bool
    defer_pointer_passed: bool
    not_now_null_pointer_passed: bool
    aggregate_exact_disposition_accuracy: float
    correct_repetitions_by_variant: Mapping[str, int]
    pair_side_correct_repetitions: Mapping[str, Mapping[str, int]]
    expected_defer_pointer_accuracy: float
    expected_not_now_null_pointer_accuracy: float
    outcome: DiagnosticOutcome

    @property
    def all_hard_gates_passed(self) -> bool:
        return (
            self.completed
            and self.structured_validity_passed
            and self.aggregate_accuracy_passed
            and self.variant_majority_passed
            and self.pair_polarity_passed
            and self.defer_pointer_passed
            and self.not_now_null_pointer_passed
        )


def load_frozen_benchmark(path: Path) -> FrozenDispositionBenchmark:
    raw = json.loads(path.read_text(encoding="utf-8"))
    reasoner = raw["reasoner"]
    pairs = tuple(_load_pair(item) for item in raw["pairs"])
    benchmark = FrozenDispositionBenchmark(
        benchmark_id=str(raw["benchmark_id"]),
        starting_merge_sha=str(raw["starting_merge_sha"]),
        randomization_seed=int(raw["randomization_seed"]),
        repetitions_per_variant=int(raw["repetitions_per_variant"]),
        common_instruction=str(raw["common_instruction"]),
        user_task=str(raw["user_task"]),
        reasoner_model=ReasoningModelConfiguration(
            requested_model=str(reasoner["model"]),
            reasoning_effort=str(reasoner["reasoning_effort"]),
            verbosity=str(reasoner["text_verbosity"]),
            max_output_tokens=int(reasoner["max_output_tokens"]),
            store=False,
        ),
        call_plan=dict(raw["call_plan"]),
        hard_gates=dict(raw["hard_gates"]),
        pairs=pairs,
    )
    validate_fixture_construction(benchmark)
    return benchmark


def _load_pair(raw: Mapping[str, object]) -> DispositionPair:
    action = raw["candidate_action"]
    if not isinstance(action, dict):
        raise ValueError("candidate_action must be an object")
    raw_triggers = raw["available_defer_triggers"]
    raw_variants = raw["variants"]
    if not isinstance(raw_triggers, list) or not isinstance(raw_variants, list):
        raise ValueError("triggers and variants must be arrays")
    shared = raw["shared_project_evidence"]
    if not isinstance(shared, dict):
        raise ValueError("shared_project_evidence must be an object")
    return DispositionPair(
        pair_id=str(raw["pair_id"]),
        domain=str(raw["domain"]),
        action_id=str(action["action_id"]),
        action_label=str(action["label"]),
        triggers=tuple(
            DeferTrigger(
                trigger_id=str(item["trigger_id"]),
                description=str(item["description"]),
            )
            for item in raw_triggers
        ),
        shared_project_evidence=dict(shared),
        variants=tuple(_load_variant(item) for item in raw_variants),
    )


def _load_variant(raw: Mapping[str, object]) -> DispositionVariant:
    evidence = raw["variant_evidence"]
    if not isinstance(evidence, dict):
        raise ValueError("variant_evidence must be an object")
    pointer = raw.get("expected_defer_until_id")
    return DispositionVariant(
        variant_id=str(raw["variant_id"]),
        variant_evidence=dict(evidence),
        expected_disposition=Disposition(str(raw["expected_disposition"])),
        expected_defer_until_id=(None if pointer is None else str(pointer)),
    )


def validate_fixture_construction(benchmark: FrozenDispositionBenchmark) -> None:
    """Validate the structural construct-validity rules before live calls."""

    if len(benchmark.pairs) != 6:
        raise ValueError(f"Specification 016 requires 6 pairs, observed {len(benchmark.pairs)}")
    if benchmark.repetitions_per_variant != 3:
        raise ValueError("Specification 016 requires exactly 3 repetitions per variant")

    pair_ids = [pair.pair_id for pair in benchmark.pairs]
    if len(pair_ids) != len(set(pair_ids)):
        raise ValueError("pair IDs must be unique")

    variant_ids: list[str] = []
    for pair in benchmark.pairs:
        if not pair.pair_id.strip() or not pair.domain.strip():
            raise ValueError("pair_id and domain must be non-empty")
        if not pair.action_id.strip() or not pair.action_label.strip():
            raise ValueError(f"{pair.pair_id} action identity must be non-empty")
        if not pair.triggers:
            raise ValueError(f"{pair.pair_id} must supply at least one defer trigger")
        trigger_ids = [item.trigger_id for item in pair.triggers]
        if len(trigger_ids) != len(set(trigger_ids)):
            raise ValueError(f"{pair.pair_id} trigger IDs must be unique")
        if len(pair.variants) != 2:
            raise ValueError(f"{pair.pair_id} must contain exactly two variants")
        observed_labels = {item.expected_disposition for item in pair.variants}
        if observed_labels != {Disposition.DEFER, Disposition.NOT_NOW}:
            raise ValueError(
                f"{pair.pair_id} must contain one DEFER and one NOT_NOW variant"
            )

        for variant in pair.variants:
            variant_ids.append(variant.variant_id)
            if not variant.variant_id.strip():
                raise ValueError("variant_id must be non-empty")
            overlap = set(pair.shared_project_evidence) & set(variant.variant_evidence)
            if overlap:
                raise ValueError(
                    f"{variant.variant_id} variant evidence overwrites shared keys: "
                    f"{sorted(overlap)}"
                )
            if variant.expected_disposition is Disposition.DEFER:
                if variant.expected_defer_until_id not in trigger_ids:
                    raise ValueError(
                        f"{variant.variant_id} DEFER truth must point to a supplied trigger"
                    )
            elif variant.expected_defer_until_id is not None:
                raise ValueError(
                    f"{variant.variant_id} NOT_NOW truth must have a null defer pointer"
                )

    if len(variant_ids) != len(set(variant_ids)):
        raise ValueError("variant IDs must be unique")

    expected_calls = len(benchmark.pairs) * 2 * benchmark.repetitions_per_variant
    planned = int(benchmark.call_plan["planned_successful_reasoner_calls"])
    if expected_calls != 36 or planned != expected_calls:
        raise ValueError(
            f"frozen call count drifted: expected 36, fixture declares {planned}"
        )
    if int(benchmark.call_plan["max_total_provider_attempts"]) != 45:
        raise ValueError("frozen maximum provider attempts must be 45")


def build_reasoning_plan(
    benchmark: FrozenDispositionBenchmark,
) -> tuple[DispositionPlanEntry, ...]:
    """Generate and globally randomize the frozen 36-call plan deterministically."""

    raw_entries: list[tuple[str, str, int]] = []
    for pair in benchmark.pairs:
        for variant in pair.variants:
            for repetition in range(1, benchmark.repetitions_per_variant + 1):
                raw_entries.append((pair.pair_id, variant.variant_id, repetition))

    rng = random.Random(benchmark.randomization_seed)
    rng.shuffle(raw_entries)

    plan: list[DispositionPlanEntry] = []
    for ordinal, (pair_id, variant_id, repetition) in enumerate(raw_entries, start=1):
        opaque = hashlib.sha256(
            (
                f"{benchmark.benchmark_id}|{benchmark.randomization_seed}|{ordinal}|"
                f"{pair_id}|{variant_id}|{repetition}"
            ).encode("utf-8")
        ).hexdigest()
        plan.append(
            DispositionPlanEntry(
                run_id=f"ds-{opaque[:16]}",
                run_nonce=f"nonce-{opaque[16:40]}",
                pair_id=pair_id,
                variant_id=variant_id,
                repetition=repetition,
            )
        )
    return tuple(plan)


def serialize_reasoning_plan(
    plan: Sequence[DispositionPlanEntry],
) -> tuple[str, str]:
    payload = [asdict(item) for item in plan]
    text = json.dumps(
        payload,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def pair_by_id(
    benchmark: FrozenDispositionBenchmark,
    pair_id: str,
) -> DispositionPair:
    matches = [item for item in benchmark.pairs if item.pair_id == pair_id]
    if len(matches) != 1:
        raise KeyError(f"unknown pair_id: {pair_id}")
    return matches[0]


def variant_by_id(pair: DispositionPair, variant_id: str) -> DispositionVariant:
    matches = [item for item in pair.variants if item.variant_id == variant_id]
    if len(matches) != 1:
        raise KeyError(f"unknown variant_id {variant_id!r} for pair {pair.pair_id}")
    return matches[0]


def build_reasoning_request(
    *,
    benchmark: FrozenDispositionBenchmark,
    plan_entry: DispositionPlanEntry,
) -> ReasoningRequest:
    """Build a provider-neutral request containing no evaluator truth."""

    pair = pair_by_id(benchmark, plan_entry.pair_id)
    variant = variant_by_id(pair, plan_entry.variant_id)
    project_evidence: dict[str, object] = {
        "candidate_action": {
            "action_id": pair.action_id,
            "label": pair.action_label,
        },
        "available_defer_triggers": [
            {
                "trigger_id": trigger.trigger_id,
                "description": trigger.description,
            }
            for trigger in pair.triggers
        ],
        "shared_project_evidence": dict(pair.shared_project_evidence),
        "variant_project_evidence": dict(variant.variant_evidence),
    }
    request = ReasoningRequest(
        run_id=plan_entry.run_id,
        run_nonce=plan_entry.run_nonce,
        system_instruction=benchmark.common_instruction,
        user_task=benchmark.user_task,
        project_evidence=project_evidence,
        methodological_context_payload=EMPTY_CONTEXT_PAYLOAD,
        methodological_context_sha256=EMPTY_CONTEXT_SHA256,
        knowledge_revisions=(),
        model_configuration=benchmark.reasoner_model,
        structured_output_type=DispositionSemanticsResult,
    )
    assert_evaluator_truth_absent(request)
    return request


def assert_evaluator_truth_absent(request: ReasoningRequest) -> None:
    """Guard against accidental hidden-truth leakage into model input."""

    text = request.canonical_model_input()
    forbidden = (
        "expected_disposition",
        "expected_defer_until_id",
        "min_aggregate_exact_disposition_accuracy",
        "expected_defer_pointer_accuracy",
        "expected_not_now_null_pointer_accuracy",
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"evaluator truth leaked into reasoner input: {leaked}")


def validate_result_for_pair(
    pair: DispositionPair,
    result: DispositionSemanticsResult,
) -> DispositionSemanticsResult:
    """Validate pointer invariants against the supplied trigger menu."""

    disposition = Disposition(result.disposition)
    valid_trigger_ids = {item.trigger_id for item in pair.triggers}
    if disposition is Disposition.DEFER:
        if result.defer_until_id not in valid_trigger_ids:
            raise ValueError(
                f"DEFER result must identify one supplied trigger; observed "
                f"{result.defer_until_id!r}"
            )
    elif result.defer_until_id is not None:
        raise ValueError("NOT_NOW result must have defer_until_id == null")
    return result


def make_observation(
    benchmark: FrozenDispositionBenchmark,
    plan_entry: DispositionPlanEntry,
    result: DispositionSemanticsResult,
) -> DispositionObservation:
    pair = pair_by_id(benchmark, plan_entry.pair_id)
    validate_result_for_pair(pair, result)
    return DispositionObservation(
        pair_id=plan_entry.pair_id,
        variant_id=plan_entry.variant_id,
        repetition=plan_entry.repetition,
        result=result,
    )


def evaluate_gates(
    benchmark: FrozenDispositionBenchmark,
    observations: Sequence[DispositionObservation],
    *,
    execution_complete: bool = True,
) -> GateEvaluation:
    """Apply the frozen Specification 016 deterministic hard gates exactly."""

    expected_count = len(benchmark.pairs) * 2 * benchmark.repetitions_per_variant
    if not execution_complete or len(observations) != expected_count:
        return GateEvaluation(
            completed=False,
            structured_validity_passed=False,
            aggregate_accuracy_passed=False,
            variant_majority_passed=False,
            pair_polarity_passed=False,
            defer_pointer_passed=False,
            not_now_null_pointer_passed=False,
            aggregate_exact_disposition_accuracy=0.0,
            correct_repetitions_by_variant={},
            pair_side_correct_repetitions={},
            expected_defer_pointer_accuracy=0.0,
            expected_not_now_null_pointer_accuracy=0.0,
            outcome=DiagnosticOutcome.INCOMPLETE,
        )

    by_key: dict[tuple[str, str, int], DispositionObservation] = {}
    for observation in observations:
        key = (observation.pair_id, observation.variant_id, observation.repetition)
        if key in by_key:
            raise ValueError(f"duplicate observation: {key}")
        pair = pair_by_id(benchmark, observation.pair_id)
        variant_by_id(pair, observation.variant_id)
        validate_result_for_pair(pair, observation.result)
        by_key[key] = observation

    expected_keys = {
        (pair.pair_id, variant.variant_id, repetition)
        for pair in benchmark.pairs
        for variant in pair.variants
        for repetition in range(1, benchmark.repetitions_per_variant + 1)
    }
    if set(by_key) != expected_keys:
        missing = sorted(expected_keys - set(by_key))
        extra = sorted(set(by_key) - expected_keys)
        raise ValueError(f"observation key set drifted; missing={missing}, extra={extra}")

    correct_total = 0
    correct_by_variant: dict[str, int] = {}
    pair_sides: dict[str, dict[str, int]] = {}
    defer_pointer_correct = 0
    defer_pointer_total = 0
    not_now_null_correct = 0
    not_now_total = 0

    for pair in benchmark.pairs:
        pair_sides[pair.pair_id] = {}
        for variant in pair.variants:
            correct = 0
            for repetition in range(1, benchmark.repetitions_per_variant + 1):
                observed = by_key[(pair.pair_id, variant.variant_id, repetition)].result
                disposition_match = (
                    Disposition(observed.disposition) is variant.expected_disposition
                )
                if disposition_match:
                    correct += 1
                    correct_total += 1

                if variant.expected_disposition is Disposition.DEFER:
                    defer_pointer_total += 1
                    if (
                        disposition_match
                        and observed.defer_until_id == variant.expected_defer_until_id
                    ):
                        defer_pointer_correct += 1
                else:
                    not_now_total += 1
                    if disposition_match and observed.defer_until_id is None:
                        not_now_null_correct += 1

            correct_by_variant[variant.variant_id] = correct
            pair_sides[pair.pair_id][variant.expected_disposition.value] = correct

    aggregate_accuracy = correct_total / expected_count
    defer_pointer_accuracy = defer_pointer_correct / defer_pointer_total
    not_now_null_accuracy = not_now_null_correct / not_now_total

    structured_valid = True
    aggregate_passed = aggregate_accuracy >= float(
        benchmark.hard_gates["min_aggregate_exact_disposition_accuracy"]
    )
    min_variant = int(benchmark.hard_gates["min_correct_repetitions_per_variant"])
    variant_passed = all(value >= min_variant for value in correct_by_variant.values())
    min_pair_side = int(benchmark.hard_gates["min_correct_repetitions_per_pair_side"])
    pair_passed = all(
        counts.get(Disposition.DEFER.value, 0) >= min_pair_side
        and counts.get(Disposition.NOT_NOW.value, 0) >= min_pair_side
        for counts in pair_sides.values()
    )
    defer_passed = defer_pointer_accuracy == float(
        benchmark.hard_gates["expected_defer_pointer_accuracy"]
    )
    not_now_passed = not_now_null_accuracy == float(
        benchmark.hard_gates["expected_not_now_null_pointer_accuracy"]
    )

    all_passed = (
        structured_valid
        and aggregate_passed
        and variant_passed
        and pair_passed
        and defer_passed
        and not_now_passed
    )
    return GateEvaluation(
        completed=True,
        structured_validity_passed=structured_valid,
        aggregate_accuracy_passed=aggregate_passed,
        variant_majority_passed=variant_passed,
        pair_polarity_passed=pair_passed,
        defer_pointer_passed=defer_passed,
        not_now_null_pointer_passed=not_now_passed,
        aggregate_exact_disposition_accuracy=aggregate_accuracy,
        correct_repetitions_by_variant=correct_by_variant,
        pair_side_correct_repetitions=pair_sides,
        expected_defer_pointer_accuracy=defer_pointer_accuracy,
        expected_not_now_null_pointer_accuracy=not_now_null_accuracy,
        outcome=(
            DiagnosticOutcome.SUPPORTED
            if all_passed
            else DiagnosticOutcome.NOT_SUPPORTED
        ),
    )


def historical_ra02_spec016_admissibility(
    historical_fixture_path: Path,
) -> dict[str, str]:
    """Describe whether historical RA-02 DEFER examples meet new construction rules.

    This function does not rescore Specification 015. It simply checks whether
    its expected-DEFER actions contain the explicit trigger relation required
    for a *new* unambiguous Specification 016 DEFER benchmark example.
    """

    raw = json.loads(historical_fixture_path.read_text(encoding="utf-8"))
    cases = [item for item in raw["cases"] if item["case_id"] == "RA-02"]
    if len(cases) != 1:
        raise ValueError("historical fixture must contain exactly one RA-02 case")
    case = cases[0]
    expected_defer_actions = [
        item for item in case["candidate_actions"] if item["expected_disposition"] == "DEFER"
    ]
    result: dict[str, str] = {}
    for action in expected_defer_actions:
        action_id = str(action["action_id"])
        has_explicit_pointer = "expected_defer_until_id" in action
        has_trigger_menu = bool(case.get("available_defer_triggers"))
        result[action_id] = (
            "ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER"
            if has_explicit_pointer and has_trigger_menu
            else "NOT_ADMISSIBLE_AS_UNAMBIGUOUS_SPEC016_DEFER"
        )
    return result


def perfect_result_for_variant(
    pair: DispositionPair,
    variant: DispositionVariant,
) -> DispositionSemanticsResult:
    """Provider-free fake-runtime helper for the frozen expected result."""

    del pair
    return DispositionSemanticsResult(
        disposition=variant.expected_disposition.value,
        defer_until_id=variant.expected_defer_until_id,
        rationale="Provider-free deterministic fake result for harness validation.",
    )
