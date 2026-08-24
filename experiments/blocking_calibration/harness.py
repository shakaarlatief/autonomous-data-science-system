"""Provider-neutral harness for Specification 020.

This module owns the frozen contrastive benchmark semantics, construction audit,
deterministic randomized call plan, truth-blinded request construction, strict
supplied-ID validation, and deterministic hard-gate evaluation for the
RECOMMENDED versus BLOCKING_REQUIRED calibration diagnostic.

It deliberately imports no provider SDK and contains no methodological-context
treatment logic. The result types are experiment-only and must not be treated as
authoritative project objects.
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


class BlockingDisposition(StrEnum):
    BLOCKING_REQUIRED = "BLOCKING_REQUIRED"
    RECOMMENDED = "RECOMMENDED"


class DiagnosticOutcome(StrEnum):
    SUPPORTED = "BLOCKING_BOUNDARY_SUPPORTED"
    NOT_SUPPORTED = "BLOCKING_BOUNDARY_NOT_SUPPORTED"
    INCOMPLETE = "INCOMPLETE"


@dataclass(frozen=True, slots=True)
class BlockingCalibrationResult:
    """Experiment-only structured output for one Specification 020 call."""

    disposition: str
    blocking_requirement_id: str | None
    blocked_scope_id: str | None
    rationale: str

    def __post_init__(self) -> None:
        try:
            normalized = BlockingDisposition(self.disposition)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"unsupported disposition: {self.disposition!r}") from exc
        object.__setattr__(self, "disposition", normalized.value)

        for field_name, value in (
            ("blocking_requirement_id", self.blocking_requirement_id),
            ("blocked_scope_id", self.blocked_scope_id),
        ):
            if value is not None and not value.strip():
                raise ValueError(f"{field_name} must be null or non-empty")
        if not self.rationale.strip():
            raise ValueError("rationale must be non-empty")

    def to_payload(self) -> dict[str, object]:
        return {
            "disposition": self.disposition,
            "blocking_requirement_id": self.blocking_requirement_id,
            "blocked_scope_id": self.blocked_scope_id,
            "rationale": self.rationale,
        }


@dataclass(frozen=True, slots=True)
class BlockingRequirement:
    requirement_id: str
    description: str

    def __post_init__(self) -> None:
        if not self.requirement_id.strip():
            raise ValueError("requirement_id must be non-empty")
        if not self.description.strip():
            raise ValueError("requirement description must be non-empty")


@dataclass(frozen=True, slots=True)
class DownstreamScope:
    scope_id: str
    description: str

    def __post_init__(self) -> None:
        if not self.scope_id.strip():
            raise ValueError("scope_id must be non-empty")
        if not self.description.strip():
            raise ValueError("scope description must be non-empty")


@dataclass(frozen=True, slots=True)
class BlockingVariant:
    variant_id: str
    variant_evidence: Mapping[str, object]
    expected_disposition: BlockingDisposition
    expected_blocking_requirement_id: str | None
    expected_blocked_scope_id: str | None


@dataclass(frozen=True, slots=True)
class BlockingPair:
    pair_id: str
    domain: str
    action_id: str
    action_label: str
    requirements: tuple[BlockingRequirement, ...]
    downstream_scopes: tuple[DownstreamScope, ...]
    shared_project_evidence: Mapping[str, object]
    variants: tuple[BlockingVariant, ...]


@dataclass(frozen=True, slots=True)
class FrozenBlockingBenchmark:
    benchmark_id: str
    starting_integration_sha: str
    randomization_seed: int
    repetitions_per_variant: int
    common_instruction: str
    user_task: str
    reasoner_model: ReasoningModelConfiguration
    call_plan: Mapping[str, object]
    hard_gates: Mapping[str, object]
    pairs: tuple[BlockingPair, ...]


@dataclass(frozen=True, slots=True)
class BlockingPlanEntry:
    run_id: str
    run_nonce: str
    pair_id: str
    variant_id: str
    repetition: int


@dataclass(frozen=True, slots=True)
class BlockingObservation:
    pair_id: str
    variant_id: str
    repetition: int
    result: BlockingCalibrationResult


@dataclass(frozen=True, slots=True)
class GateEvaluation:
    completed: bool
    structured_validity_passed: bool
    aggregate_accuracy_passed: bool
    variant_majority_passed: bool
    pair_polarity_passed: bool
    blocking_joint_pointer_passed: bool
    recommended_null_pointer_passed: bool
    aggregate_exact_disposition_accuracy: float
    correct_repetitions_by_variant: Mapping[str, int]
    pair_side_correct_repetitions: Mapping[str, Mapping[str, int]]
    expected_blocking_requirement_pointer_accuracy: float
    expected_blocked_scope_pointer_accuracy: float
    expected_blocking_joint_pointer_accuracy: float
    expected_recommended_null_pointer_correctness: float
    outcome: DiagnosticOutcome

    @property
    def all_hard_gates_passed(self) -> bool:
        return (
            self.completed
            and self.structured_validity_passed
            and self.aggregate_accuracy_passed
            and self.variant_majority_passed
            and self.pair_polarity_passed
            and self.blocking_joint_pointer_passed
            and self.recommended_null_pointer_passed
        )


def load_frozen_benchmark(path: Path) -> FrozenBlockingBenchmark:
    raw = json.loads(path.read_text(encoding="utf-8"))
    reasoner = raw["reasoner"]
    if not isinstance(reasoner, dict):
        raise ValueError("reasoner must be an object")
    raw_pairs = raw["pairs"]
    if not isinstance(raw_pairs, list):
        raise ValueError("pairs must be an array")

    benchmark = FrozenBlockingBenchmark(
        benchmark_id=str(raw["benchmark_id"]),
        starting_integration_sha=str(raw["starting_integration_sha"]),
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
        pairs=tuple(_load_pair(item) for item in raw_pairs),
    )
    validate_fixture_construction(benchmark)
    return benchmark


def _load_pair(raw: Mapping[str, object]) -> BlockingPair:
    action = raw["candidate_action"]
    requirements = raw["available_requirements"]
    scopes = raw["available_downstream_scopes"]
    shared = raw["shared_project_evidence"]
    variants = raw["variants"]
    if not isinstance(action, dict):
        raise ValueError("candidate_action must be an object")
    if not isinstance(requirements, list):
        raise ValueError("available_requirements must be an array")
    if not isinstance(scopes, list):
        raise ValueError("available_downstream_scopes must be an array")
    if not isinstance(shared, dict):
        raise ValueError("shared_project_evidence must be an object")
    if not isinstance(variants, list):
        raise ValueError("variants must be an array")

    return BlockingPair(
        pair_id=str(raw["pair_id"]),
        domain=str(raw["domain"]),
        action_id=str(action["action_id"]),
        action_label=str(action["label"]),
        requirements=tuple(
            BlockingRequirement(
                requirement_id=str(item["requirement_id"]),
                description=str(item["description"]),
            )
            for item in requirements
        ),
        downstream_scopes=tuple(
            DownstreamScope(
                scope_id=str(item["scope_id"]),
                description=str(item["description"]),
            )
            for item in scopes
        ),
        shared_project_evidence=dict(shared),
        variants=tuple(_load_variant(item) for item in variants),
    )


def _load_variant(raw: Mapping[str, object]) -> BlockingVariant:
    evidence = raw["variant_evidence"]
    if not isinstance(evidence, dict):
        raise ValueError("variant_evidence must be an object")
    requirement_pointer = raw.get("expected_blocking_requirement_id")
    scope_pointer = raw.get("expected_blocked_scope_id")
    return BlockingVariant(
        variant_id=str(raw["variant_id"]),
        variant_evidence=dict(evidence),
        expected_disposition=BlockingDisposition(str(raw["expected_disposition"])),
        expected_blocking_requirement_id=(
            None if requirement_pointer is None else str(requirement_pointer)
        ),
        expected_blocked_scope_id=(None if scope_pointer is None else str(scope_pointer)),
    )


def validate_fixture_construction(benchmark: FrozenBlockingBenchmark) -> None:
    """Validate every frozen construct-validity rule before execution."""

    if len(benchmark.pairs) != 6:
        raise ValueError(f"Specification 020 requires 6 pairs, observed {len(benchmark.pairs)}")
    if benchmark.repetitions_per_variant != 3:
        raise ValueError("Specification 020 requires exactly 3 repetitions per variant")
    if not benchmark.benchmark_id.strip() or not benchmark.starting_integration_sha.strip():
        raise ValueError("benchmark identity and starting integration SHA must be non-empty")
    if not benchmark.common_instruction.strip() or not benchmark.user_task.strip():
        raise ValueError("reasoner instruction and user task must be non-empty")

    pair_ids = [pair.pair_id for pair in benchmark.pairs]
    if len(pair_ids) != len(set(pair_ids)):
        raise ValueError("pair IDs must be unique")

    variant_ids: list[str] = []
    for pair in benchmark.pairs:
        if not pair.pair_id.strip() or not pair.domain.strip():
            raise ValueError("pair_id and domain must be non-empty")
        if not pair.action_id.strip() or not pair.action_label.strip():
            raise ValueError(f"{pair.pair_id} action identity must be non-empty")
        if not pair.requirements:
            raise ValueError(f"{pair.pair_id} must supply at least one requirement")
        if not pair.downstream_scopes:
            raise ValueError(f"{pair.pair_id} must supply at least one downstream scope")

        requirement_ids = [item.requirement_id for item in pair.requirements]
        scope_ids = [item.scope_id for item in pair.downstream_scopes]
        if len(requirement_ids) != len(set(requirement_ids)):
            raise ValueError(f"{pair.pair_id} requirement IDs must be unique")
        if len(scope_ids) != len(set(scope_ids)):
            raise ValueError(f"{pair.pair_id} downstream-scope IDs must be unique")
        if len(pair.variants) != 2:
            raise ValueError(f"{pair.pair_id} must contain exactly two variants")

        observed_labels = {variant.expected_disposition for variant in pair.variants}
        if observed_labels != {
            BlockingDisposition.BLOCKING_REQUIRED,
            BlockingDisposition.RECOMMENDED,
        }:
            raise ValueError(
                f"{pair.pair_id} must contain one BLOCKING_REQUIRED and one RECOMMENDED variant"
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

            if variant.expected_disposition is BlockingDisposition.BLOCKING_REQUIRED:
                if variant.expected_blocking_requirement_id not in requirement_ids:
                    raise ValueError(
                        f"{variant.variant_id} blocking truth must point to a supplied requirement"
                    )
                if variant.expected_blocked_scope_id not in scope_ids:
                    raise ValueError(
                        f"{variant.variant_id} blocking truth must point to a supplied downstream scope"
                    )
            else:
                if variant.expected_blocking_requirement_id is not None:
                    raise ValueError(
                        f"{variant.variant_id} RECOMMENDED truth must have a null requirement pointer"
                    )
                if variant.expected_blocked_scope_id is not None:
                    raise ValueError(
                        f"{variant.variant_id} RECOMMENDED truth must have a null scope pointer"
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
    if int(benchmark.call_plan["max_retries_per_planned_call"]) != 1:
        raise ValueError("frozen retry count must be exactly one per planned call")


def build_reasoning_plan(
    benchmark: FrozenBlockingBenchmark,
) -> tuple[BlockingPlanEntry, ...]:
    """Generate and globally randomize the frozen 36-call plan deterministically."""

    raw_entries: list[tuple[str, str, int]] = []
    for pair in benchmark.pairs:
        for variant in pair.variants:
            for repetition in range(1, benchmark.repetitions_per_variant + 1):
                raw_entries.append((pair.pair_id, variant.variant_id, repetition))

    rng = random.Random(benchmark.randomization_seed)
    rng.shuffle(raw_entries)

    plan: list[BlockingPlanEntry] = []
    for ordinal, (pair_id, variant_id, repetition) in enumerate(raw_entries, start=1):
        opaque = hashlib.sha256(
            (
                f"{benchmark.benchmark_id}|{benchmark.randomization_seed}|{ordinal}|"
                f"{pair_id}|{variant_id}|{repetition}"
            ).encode("utf-8")
        ).hexdigest()
        plan.append(
            BlockingPlanEntry(
                run_id=f"bc-{opaque[:16]}",
                run_nonce=f"nonce-{opaque[16:40]}",
                pair_id=pair_id,
                variant_id=variant_id,
                repetition=repetition,
            )
        )
    return tuple(plan)


def serialize_reasoning_plan(
    plan: Sequence[BlockingPlanEntry],
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
    benchmark: FrozenBlockingBenchmark,
    pair_id: str,
) -> BlockingPair:
    matches = [item for item in benchmark.pairs if item.pair_id == pair_id]
    if len(matches) != 1:
        raise KeyError(f"unknown pair_id: {pair_id}")
    return matches[0]


def variant_by_id(pair: BlockingPair, variant_id: str) -> BlockingVariant:
    matches = [item for item in pair.variants if item.variant_id == variant_id]
    if len(matches) != 1:
        raise KeyError(f"unknown variant_id {variant_id!r} for pair {pair.pair_id}")
    return matches[0]


def build_reasoning_request(
    *,
    benchmark: FrozenBlockingBenchmark,
    plan_entry: BlockingPlanEntry,
) -> ReasoningRequest:
    """Build a deterministic provider-neutral request containing no evaluator truth."""

    pair = pair_by_id(benchmark, plan_entry.pair_id)
    variant = variant_by_id(pair, plan_entry.variant_id)
    project_evidence: dict[str, object] = {
        "candidate_action": {
            "action_id": pair.action_id,
            "label": pair.action_label,
        },
        "available_requirements": [
            {
                "requirement_id": requirement.requirement_id,
                "description": requirement.description,
            }
            for requirement in pair.requirements
        ],
        "available_downstream_scopes": [
            {
                "scope_id": scope.scope_id,
                "description": scope.description,
            }
            for scope in pair.downstream_scopes
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
        structured_output_type=BlockingCalibrationResult,
    )
    assert_evaluator_truth_absent(request)
    return request


def assert_evaluator_truth_absent(request: ReasoningRequest) -> None:
    """Guard against accidental hidden-truth or gate leakage into model input."""

    text = request.canonical_model_input()
    forbidden = (
        "expected_disposition",
        "expected_blocking_requirement_id",
        "expected_blocked_scope_id",
        "min_aggregate_exact_disposition_accuracy",
        "expected_blocking_joint_pointer_accuracy",
        "expected_recommended_null_pointer_correctness",
        "BC-G01",
        "BC-G02",
        "BC-G03",
        "BC-G04",
        "BC-G05",
        "BC-G06",
    )
    leaked = [token for token in forbidden if token in text]
    if leaked:
        raise ValueError(f"evaluator truth leaked into reasoner input: {leaked}")


def validate_result_for_pair(
    pair: BlockingPair,
    result: BlockingCalibrationResult,
) -> BlockingCalibrationResult:
    """Validate disposition-pointer invariants against supplied stable IDs."""

    disposition = BlockingDisposition(result.disposition)
    valid_requirement_ids = {item.requirement_id for item in pair.requirements}
    valid_scope_ids = {item.scope_id for item in pair.downstream_scopes}

    if disposition is BlockingDisposition.BLOCKING_REQUIRED:
        if result.blocking_requirement_id not in valid_requirement_ids:
            raise ValueError(
                "BLOCKING_REQUIRED result must identify one supplied requirement; "
                f"observed {result.blocking_requirement_id!r}"
            )
        if result.blocked_scope_id not in valid_scope_ids:
            raise ValueError(
                "BLOCKING_REQUIRED result must identify one supplied downstream scope; "
                f"observed {result.blocked_scope_id!r}"
            )
    else:
        if result.blocking_requirement_id is not None:
            raise ValueError("RECOMMENDED result must have blocking_requirement_id == null")
        if result.blocked_scope_id is not None:
            raise ValueError("RECOMMENDED result must have blocked_scope_id == null")
    return result


def make_observation(
    benchmark: FrozenBlockingBenchmark,
    plan_entry: BlockingPlanEntry,
    result: BlockingCalibrationResult,
) -> BlockingObservation:
    pair = pair_by_id(benchmark, plan_entry.pair_id)
    validate_result_for_pair(pair, result)
    return BlockingObservation(
        pair_id=plan_entry.pair_id,
        variant_id=plan_entry.variant_id,
        repetition=plan_entry.repetition,
        result=result,
    )


def evaluate_gates(
    benchmark: FrozenBlockingBenchmark,
    observations: Sequence[BlockingObservation],
    *,
    execution_complete: bool = True,
) -> GateEvaluation:
    """Mechanically recompute all frozen Specification 020 hard gates."""

    observation_by_key: dict[tuple[str, str, int], BlockingObservation] = {}
    for observation in observations:
        key = (observation.pair_id, observation.variant_id, observation.repetition)
        if key in observation_by_key:
            raise ValueError(f"duplicate observation: {key}")
        pair = pair_by_id(benchmark, observation.pair_id)
        variant_by_id(pair, observation.variant_id)
        if observation.repetition not in range(1, benchmark.repetitions_per_variant + 1):
            raise ValueError(f"invalid repetition for observation: {key}")
        validate_result_for_pair(pair, observation.result)
        observation_by_key[key] = observation

    expected_keys = {
        (pair.pair_id, variant.variant_id, repetition)
        for pair in benchmark.pairs
        for variant in pair.variants
        for repetition in range(1, benchmark.repetitions_per_variant + 1)
    }
    completed = (
        execution_complete
        and len(observations) == 36
        and set(observation_by_key) == expected_keys
    )

    correct_total = 0
    correct_by_variant: dict[str, int] = {
        variant.variant_id: 0
        for pair in benchmark.pairs
        for variant in pair.variants
    }
    pair_side_correct: dict[str, dict[str, int]] = {
        pair.pair_id: {
            BlockingDisposition.BLOCKING_REQUIRED.value: 0,
            BlockingDisposition.RECOMMENDED.value: 0,
        }
        for pair in benchmark.pairs
    }

    blocking_requirement_correct = 0
    blocking_scope_correct = 0
    blocking_joint_correct = 0
    recommended_null_correct = 0

    for observation in observations:
        pair = pair_by_id(benchmark, observation.pair_id)
        variant = variant_by_id(pair, observation.variant_id)
        result = observation.result
        disposition_correct = result.disposition == variant.expected_disposition.value
        if disposition_correct:
            correct_total += 1
            correct_by_variant[variant.variant_id] += 1
            pair_side_correct[pair.pair_id][variant.expected_disposition.value] += 1

        if variant.expected_disposition is BlockingDisposition.BLOCKING_REQUIRED:
            requirement_correct = (
                disposition_correct
                and result.blocking_requirement_id
                == variant.expected_blocking_requirement_id
            )
            scope_correct = (
                disposition_correct
                and result.blocked_scope_id == variant.expected_blocked_scope_id
            )
            if requirement_correct:
                blocking_requirement_correct += 1
            if scope_correct:
                blocking_scope_correct += 1
            if requirement_correct and scope_correct:
                blocking_joint_correct += 1
        else:
            if (
                disposition_correct
                and result.blocking_requirement_id is None
                and result.blocked_scope_id is None
            ):
                recommended_null_correct += 1

    aggregate_accuracy = correct_total / 36
    blocking_requirement_accuracy = blocking_requirement_correct / 18
    blocking_scope_accuracy = blocking_scope_correct / 18
    blocking_joint_accuracy = blocking_joint_correct / 18
    recommended_null_correctness = recommended_null_correct / 18

    structured_validity_passed = True
    aggregate_accuracy_passed = aggregate_accuracy >= float(
        benchmark.hard_gates["min_aggregate_exact_disposition_accuracy"]
    )
    variant_majority_passed = all(
        count >= int(benchmark.hard_gates["min_correct_repetitions_per_variant"])
        for count in correct_by_variant.values()
    )
    pair_polarity_passed = all(
        count >= int(benchmark.hard_gates["min_correct_repetitions_per_pair_side"])
        for pair_counts in pair_side_correct.values()
        for count in pair_counts.values()
    )
    blocking_joint_pointer_passed = blocking_joint_accuracy == float(
        benchmark.hard_gates["expected_blocking_joint_pointer_accuracy"]
    )
    recommended_null_pointer_passed = recommended_null_correctness == float(
        benchmark.hard_gates["expected_recommended_null_pointer_correctness"]
    )

    if not completed:
        outcome = DiagnosticOutcome.INCOMPLETE
    elif (
        structured_validity_passed
        and aggregate_accuracy_passed
        and variant_majority_passed
        and pair_polarity_passed
        and blocking_joint_pointer_passed
        and recommended_null_pointer_passed
    ):
        outcome = DiagnosticOutcome.SUPPORTED
    else:
        outcome = DiagnosticOutcome.NOT_SUPPORTED

    return GateEvaluation(
        completed=completed,
        structured_validity_passed=structured_validity_passed,
        aggregate_accuracy_passed=aggregate_accuracy_passed,
        variant_majority_passed=variant_majority_passed,
        pair_polarity_passed=pair_polarity_passed,
        blocking_joint_pointer_passed=blocking_joint_pointer_passed,
        recommended_null_pointer_passed=recommended_null_pointer_passed,
        aggregate_exact_disposition_accuracy=aggregate_accuracy,
        correct_repetitions_by_variant=correct_by_variant,
        pair_side_correct_repetitions=pair_side_correct,
        expected_blocking_requirement_pointer_accuracy=blocking_requirement_accuracy,
        expected_blocked_scope_pointer_accuracy=blocking_scope_accuracy,
        expected_blocking_joint_pointer_accuracy=blocking_joint_accuracy,
        expected_recommended_null_pointer_correctness=recommended_null_correctness,
        outcome=outcome,
    )


def perfect_result_for_variant(
    pair: BlockingPair,
    variant: BlockingVariant,
) -> BlockingCalibrationResult:
    """Create an evaluator-truth result for provider-free gate tests only."""

    del pair
    if variant.expected_disposition is BlockingDisposition.BLOCKING_REQUIRED:
        return BlockingCalibrationResult(
            disposition=BlockingDisposition.BLOCKING_REQUIRED.value,
            blocking_requirement_id=variant.expected_blocking_requirement_id,
            blocked_scope_id=variant.expected_blocked_scope_id,
            rationale="Provider-free perfect result for frozen gate evaluation.",
        )
    return BlockingCalibrationResult(
        disposition=BlockingDisposition.RECOMMENDED.value,
        blocking_requirement_id=None,
        blocked_scope_id=None,
        rationale="Provider-free perfect result for frozen gate evaluation.",
    )
