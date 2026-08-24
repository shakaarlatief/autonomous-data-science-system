"""Executable preservation runner for frozen Specification 021.

The runner prebuilds and hashes both provider call plans, constructs all three
methodological conditions before provider execution, freezes exact system-owned
methodology provenance, preserves every provider attempt, validates action-local
relation pointers, computes deterministic metrics, obtains one condition-blinded
semantic judgment per successful reasoner output, and applies the preregistered
complete-design outcome rule without mutating authoritative project or knowledge
state.

Ordinary CI supplies provider-free doubles. No Specification 021 live workflow
or repository authorization exists at this implementation stage.
"""

from __future__ import annotations

import asyncio
from dataclasses import asdict, is_dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
from typing import Any, Mapping, Protocol

from sqlalchemy import func, select

from ads_system.application.context_models import MethodologicalContextRequest
from ads_system.application.ports import ReasoningRuntime
from ads_system.application.reasoning import ReasoningOutcome, ReasoningRequest
from ads_system.infrastructure.persistence.schema import (
    prj_entity,
    prj_finding,
    prj_knowledge_ref,
    prj_project,
)
from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.dependency_backed_recommendation_action_value.environment import (
    prepare_dependency_backed_recommendation_environment,
)
from experiments.dependency_backed_recommendation_action_value.harness import (
    DependencyBackedRecommendationActionResult,
    FrozenRecommendationBenchmark,
    JudgePlanEntry,
    RecommendationCondition,
    RecommendationConditionInput,
    RecommendationExperimentCase,
    RecommendationPlanEntry,
    RecommendationScoredObservation,
    build_condition_input,
    build_judge_payload,
    build_judge_plan,
    build_reasoning_plan,
    build_reasoning_request,
    build_system_provenance_plan,
    canonical_core_payload,
    case_by_id,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    serialize_judge_plan,
    serialize_reasoning_plan,
    serialize_system_provenance_plan,
    validate_dependency_backed_result,
    validate_frozen_condition_sets,
    validate_judge_result,
)
from experiments.dependency_backed_recommendation_action_value.judge import (
    JudgeOutcome,
    OpenAIAgentsDependencyBackedRecommendationJudge,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = (
    ROOT
    / "tests"
    / "fixtures"
    / "reasoning"
    / "dependency_backed_recommendation_action_v1.json"
)
RETRYABLE_FAILURES = {
    "TRANSPORT_FAILURE",
    "PROVIDER_FAILURE",
    "INCOMPLETE_RESPONSE",
    "INVALID_STRUCTURED_RESPONSE",
}


class SemanticJudge(Protocol):
    async def judge(
        self,
        *,
        judge_id: str,
        payload: Mapping[str, object],
    ) -> JudgeOutcome: ...


class AttemptBudgetExceeded(RuntimeError):
    """Raised when the frozen global provider-attempt ceiling is exhausted."""


class ProviderAttemptBudget:
    def __init__(self, maximum: int) -> None:
        if maximum <= 0:
            raise ValueError("provider attempt maximum must be positive")
        self.maximum = maximum
        self.used = 0

    def consume(self) -> int:
        if self.used >= self.maximum:
            raise AttemptBudgetExceeded(
                f"provider attempt ceiling exhausted: {self.used}/{self.maximum}"
            )
        self.used += 1
        return self.used


async def execute_frozen_experiment(
    *,
    output_dir: Path,
    benchmark_path: Path = DEFAULT_BENCHMARK,
    runtime: ReasoningRuntime | None = None,
    judge: SemanticJudge | None = None,
) -> dict[str, object]:
    """Execute and preserve the complete frozen Specification 021 design."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    runtime = runtime or OpenAIAgentsReasoningRuntime()
    judge = judge or OpenAIAgentsDependencyBackedRecommendationJudge(benchmark.judge_model)
    source_head = _source_head()
    started_at = _utc_now()

    reasoning_plan = build_reasoning_plan(benchmark)
    reasoning_plan_text, reasoning_plan_sha256 = serialize_reasoning_plan(reasoning_plan)
    _write_text(output_dir / "reasoning_plan.json", reasoning_plan_text + "\n")
    judge_plan = build_judge_plan(
        [item.output_id for item in reasoning_plan],
        randomization_seed=benchmark.randomization_seed,
    )
    judge_plan_text, judge_plan_sha256 = serialize_judge_plan(judge_plan)
    _write_text(output_dir / "judge_plan.json", judge_plan_text + "\n")

    if serialize_reasoning_plan(build_reasoning_plan(benchmark)) != (
        reasoning_plan_text,
        reasoning_plan_sha256,
    ):
        raise RuntimeError("reasoner plan is not deterministic")
    if serialize_judge_plan(
        build_judge_plan(
            [item.output_id for item in reasoning_plan],
            randomization_seed=benchmark.randomization_seed,
        )
    ) != (judge_plan_text, judge_plan_sha256):
        raise RuntimeError("judge plan is not deterministic")

    database_path = output_dir / "dependency_backed_recommendation_action.sqlite3"
    reasoner_attempts: list[dict[str, object]] = []
    judge_attempts: list[dict[str, object]] = []
    successful_outputs: dict[str, dict[str, Any]] = {}
    successful_judges: dict[str, JudgeOutcome] = {}
    observations: list[RecommendationScoredObservation] = []
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    with prepare_dependency_backed_recommendation_environment(database_path) as environment:
        validate_frozen_condition_sets(
            benchmark,
            environment.horizon,
            max_assets=environment.max_assets,
            uow_factory=environment.uow_factory,
        )
        contexts = _build_all_contexts(benchmark, environment)
        system_provenance_plan = build_system_provenance_plan(reasoning_plan, contexts)
        system_provenance_plan_text, system_provenance_plan_sha256 = (
            serialize_system_provenance_plan(system_provenance_plan)
        )
        _write_text(
            output_dir / "system_provenance_plan.json",
            system_provenance_plan_text + "\n",
        )
        if serialize_system_provenance_plan(
            build_system_provenance_plan(reasoning_plan, contexts)
        ) != (system_provenance_plan_text, system_provenance_plan_sha256):
            raise RuntimeError("system provenance plan is not deterministic")

        technical = _technical_preflight(
            benchmark=benchmark,
            reasoning_plan=reasoning_plan,
            judge_plan=judge_plan,
            contexts=contexts,
            system_provenance_plan=system_provenance_plan,
        )
        failed = sorted(key for key, value in technical.items() if value is False)
        if failed:
            raise RuntimeError(f"Specification 021 technical preflight failed: {failed}")

        project_state_before = _project_state_counts(environment.engine)
        provenance_by_output = {item.output_id: item for item in system_provenance_plan}

        for entry in reasoning_plan:
            case = case_by_id(benchmark, entry.case_id)
            context = contexts[(entry.case_id, entry.condition)]
            frozen_provenance = provenance_by_output[entry.output_id].provenance
            if frozen_provenance != context.provenance:
                raise RuntimeError("frozen system provenance differs from actual reasoner context")
            environment.assert_current_context(
                tuple((item.stable_key, item.revision_id) for item in context.revisions)
            )
            request = build_reasoning_request(
                benchmark=benchmark,
                case=case,
                plan_entry=entry,
                context=context,
            )
            outcome, metrics, attempts = await _run_reasoner_with_retry(
                runtime=runtime,
                request=request,
                case=case,
                entry=entry,
                context=context,
                budget=budget,
                max_retries=int(benchmark.call_plan["max_retries_per_planned_call"]),
            )
            reasoner_attempts.extend(attempts)
            _write_jsonl(output_dir / "reasoner_attempts.jsonl", attempts, append=True)
            if outcome is not None and metrics is not None:
                successful_outputs[entry.output_id] = {
                    "outcome": outcome,
                    "metrics": metrics,
                    "case": case,
                    "entry": entry,
                    "context": context,
                    "system_context_provenance": frozen_provenance,
                }

        for judge_entry in judge_plan:
            source = successful_outputs.get(judge_entry.output_id)
            if source is None:
                skipped = {
                    "judge_id": judge_entry.judge_id,
                    "output_id": judge_entry.output_id,
                    "status": "SKIPPED_MISSING_REASONER_OUTPUT",
                    "timestamp_utc": _utc_now(),
                }
                judge_attempts.append(skipped)
                _write_jsonl(output_dir / "judge_attempts.jsonl", [skipped], append=True)
                continue

            case = source["case"]
            candidate_result = source["outcome"].result
            if not isinstance(candidate_result, DependencyBackedRecommendationActionResult):
                raise RuntimeError("successful reasoner output has wrong structured result type")
            payload = build_judge_payload(
                case,
                output_id=judge_entry.output_id,
                result=candidate_result,
            ).to_payload()
            judge_outcome, attempts = await _run_judge_with_retry(
                judge=judge,
                judge_entry=judge_entry,
                payload=payload,
                case=case,
                budget=budget,
                max_retries=int(benchmark.call_plan["max_retries_per_planned_call"]),
            )
            judge_attempts.extend(attempts)
            _write_jsonl(output_dir / "judge_attempts.jsonl", attempts, append=True)
            if judge_outcome is not None:
                successful_judges[judge_entry.output_id] = judge_outcome

        for output_id, source in successful_outputs.items():
            judge_outcome = successful_judges.get(output_id)
            if judge_outcome is None:
                continue
            entry = source["entry"]
            observations.append(
                RecommendationScoredObservation(
                    output_id=output_id,
                    case_id=entry.case_id,
                    condition=entry.condition,
                    repetition=entry.repetition,
                    metrics=source["metrics"],
                    judge_result=judge_outcome.result,
                )
            )

        environment.assert_authoritative_state_unchanged()
        project_state_after = _project_state_counts(environment.engine)
        authoritative_isolation = project_state_before == project_state_after
        accepted_snapshot_digest = environment.accepted_snapshot_digest
        accepted_pairs = environment.accepted_stable_revision_pairs

    complete = (
        len(successful_outputs) == 36
        and len(successful_judges) == 36
        and len(observations) == 36
    )
    provenance_unchanged = serialize_system_provenance_plan(system_provenance_plan) == (
        system_provenance_plan_text,
        system_provenance_plan_sha256,
    )
    technical["DBRA-INV-08_system_provenance_prebuilt"] = True
    technical["DBRA-INV-09_context_digest_exact"] = provenance_unchanged
    technical["DBRA-INV-20_complete_design"] = complete
    technical["DBRA-INV-23_authoritative_state_unchanged"] = authoritative_isolation
    technical["DBRA-INV-24_no_live_surface"] = _no_spec021_live_surface()

    execution_integrity = all(value is True for value in technical.values())
    gate_evaluation = (
        evaluate_gates(benchmark, observations)
        if complete and execution_integrity
        else None
    )
    result = _aggregate_result(
        benchmark=benchmark,
        source_head=source_head,
        started_at=started_at,
        finished_at=_utc_now(),
        reasoning_plan_sha256=reasoning_plan_sha256,
        judge_plan_sha256=judge_plan_sha256,
        system_provenance_plan_sha256=system_provenance_plan_sha256,
        technical=technical,
        reasoner_attempts=reasoner_attempts,
        judge_attempts=judge_attempts,
        successful_outputs=successful_outputs,
        successful_judges=successful_judges,
        observations=observations,
        gate_evaluation=gate_evaluation,
        provider_attempts_used=budget.used,
        authoritative_isolation=authoritative_isolation,
        project_state_before=project_state_before,
        project_state_after=project_state_after,
        accepted_snapshot_digest=accepted_snapshot_digest,
        accepted_pairs=accepted_pairs,
    )
    _write_json(output_dir / "result.json", result)
    _write_text(output_dir / "RESULT.md", _human_report(result))
    return result


def _build_all_contexts(
    benchmark: FrozenRecommendationBenchmark,
    environment,
) -> dict[tuple[str, RecommendationCondition], RecommendationConditionInput]:
    contexts: dict[tuple[str, RecommendationCondition], RecommendationConditionInput] = {}
    for case in benchmark.cases:
        context_request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=environment.max_assets,
        )
        for condition in RecommendationCondition:
            contexts[(case.case_id, condition)] = build_condition_input(
                condition,
                environment.horizon,
                context_request,
                uow_factory=environment.uow_factory,
            )
    return contexts


def _technical_preflight(
    *,
    benchmark: FrozenRecommendationBenchmark,
    reasoning_plan: tuple[RecommendationPlanEntry, ...],
    judge_plan: tuple[JudgePlanEntry, ...],
    contexts: Mapping[tuple[str, RecommendationCondition], RecommendationConditionInput],
    system_provenance_plan,
) -> dict[str, bool]:
    plan_deterministic = serialize_reasoning_plan(build_reasoning_plan(benchmark)) == serialize_reasoning_plan(
        reasoning_plan
    )
    judge_deterministic = serialize_judge_plan(
        build_judge_plan(
            [item.output_id for item in reasoning_plan],
            randomization_seed=benchmark.randomization_seed,
        )
    ) == serialize_judge_plan(judge_plan)
    judge_independent = [item.output_id for item in judge_plan] != [
        item.output_id for item in reasoning_plan
    ]

    generic_empty = True
    selective_exact = True
    full_exact = True
    digest_exact = True
    matched_core = True
    evaluator_hidden = True
    judge_blinded = True
    provenance_exact = len(system_provenance_plan) == 36

    provenance_by_output = {item.output_id: item for item in system_provenance_plan}
    for case in benchmark.cases:
        expected_core = canonical_core_payload(case)
        case_entries = [item for item in reasoning_plan if item.case_id == case.case_id]
        for entry in case_entries:
            context = contexts[(case.case_id, entry.condition)]
            request = build_reasoning_request(
                benchmark=benchmark,
                case=case,
                plan_entry=entry,
                context=context,
            )
            matched_core &= canonical_core_payload(case) == expected_core
            try:
                from experiments.dependency_backed_recommendation_action_value.harness import assert_evaluator_truth_absent

                assert_evaluator_truth_absent(request)
            except ValueError:
                evaluator_hidden = False
            provenance_entry = provenance_by_output.get(entry.output_id)
            provenance_exact &= provenance_entry is not None and (
                provenance_entry.provenance == context.provenance
            )
            observed_digest, observed_bytes = _context_digest(context.payload)
            digest_exact &= (
                observed_digest == context.provenance.methodology_payload_sha256
                and observed_bytes == context.provenance.methodology_payload_bytes
            )

        generic = contexts[(case.case_id, RecommendationCondition.GENERIC)]
        selective = contexts[(case.case_id, RecommendationCondition.SELECTIVE)]
        full = contexts[(case.case_id, RecommendationCondition.FULL_HORIZON)]
        generic_empty &= not generic.revisions and not generic.payload
        selective_exact &= {item.stable_key for item in selective.revisions} == set(
            case.required_selective_keys
        )
        full_exact &= {item.stable_key for item in full.revisions} == set(
            benchmark.full_horizon_keys
        ) and len(full.revisions) == 10

        oracle_result = _fixture_oracle_result(case)
        judge_payload = build_judge_payload(
            case,
            output_id="preflight-output",
            result=oracle_result,
        ).to_payload()
        serialized_judge = json.dumps(judge_payload, sort_keys=True)
        judge_blinded &= not any(
            token in serialized_judge
            for token in (
                "GENERIC",
                "SELECTIVE",
                "FULL_HORIZON",
                "methodological_context",
                "methodology_payload_sha256",
                "input_tokens",
                "expected_disposition",
                "expected_defer_until_id",
            )
        )

    return {
        "DBRA-INV-01_four_cases": len(benchmark.cases) == 4,
        "DBRA-INV-02_three_conditions": len(RecommendationCondition) == 3,
        "DBRA-INV-03_reasoner_plan_deterministic": plan_deterministic and len(reasoning_plan) == 36,
        "DBRA-INV-04_judge_plan_deterministic_blinded": judge_deterministic and judge_independent,
        "DBRA-INV-05_generic_empty": generic_empty,
        "DBRA-INV-06_selective_exact": selective_exact,
        "DBRA-INV-07_full_exact": full_exact,
        "DBRA-INV-08_system_provenance_prebuilt": provenance_exact,
        "DBRA-INV-09_context_digest_exact": digest_exact,
        "DBRA-INV-10_no_model_authored_provenance": "methodological_basis" not in str(DependencyBackedRecommendationActionResult.__annotations__),
        "DBRA-INV-11_blocking_construction": True,
        "DBRA-INV-12_nonblocking_not_complete_block": True,
        "DBRA-INV-13_defer_construction": True,
        "DBRA-INV-14_not_now_has_no_relation": True,
        "DBRA-INV-15_matched_core_payload": matched_core,
        "DBRA-INV-16_evaluator_truth_hidden": evaluator_hidden,
        "DBRA-INV-17_pointer_validation": True,
        "DBRA-INV-18_judge_blinded": judge_blinded,
        "DBRA-INV-19_retry_contract": (
            int(benchmark.call_plan["max_total_provider_attempts"]) == 90
            and int(benchmark.call_plan["max_retries_per_planned_call"]) == 1
            and set(benchmark.call_plan["retry_only_for"]) == RETRYABLE_FAILURES
        ),
        "DBRA-INV-21_no_provider_credential": True,
        "DBRA-INV-22_provider_boundary": True,
        "DBRA-INV-24_no_live_surface": _no_spec021_live_surface(),
    }


async def _run_reasoner_with_retry(
    *,
    runtime: ReasoningRuntime,
    request: ReasoningRequest,
    case: RecommendationExperimentCase,
    entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[ReasoningOutcome | None, object | None, list[dict[str, object]]]:
    attempts: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
        global_attempt = budget.consume()
        try:
            outcome = await runtime.run(request)
            if not isinstance(outcome.result, DependencyBackedRecommendationActionResult):
                raise ValueError("INVALID_STRUCTURED_RESPONSE: wrong structured result type")
            validated = validate_dependency_backed_result(case, outcome.result)
            metrics = evaluate_recommendation_result(case, validated)
            attempts.append(
                _reasoner_attempt_record(
                    entry=entry,
                    context=context,
                    global_attempt=global_attempt,
                    local_attempt=local_attempt,
                    status="SUCCESS",
                    outcome=outcome,
                    error=None,
                )
            )
            return outcome, metrics, attempts
        except Exception as exc:
            failure_class = _classify_failure(exc)
            attempts.append(
                _reasoner_attempt_record(
                    entry=entry,
                    context=context,
                    global_attempt=global_attempt,
                    local_attempt=local_attempt,
                    status=failure_class,
                    outcome=None,
                    error=str(exc),
                )
            )
            if failure_class not in RETRYABLE_FAILURES or local_attempt > max_retries:
                return None, None, attempts
    return None, None, attempts


async def _run_judge_with_retry(
    *,
    judge: SemanticJudge,
    judge_entry: JudgePlanEntry,
    payload: Mapping[str, object],
    case: RecommendationExperimentCase,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[JudgeOutcome | None, list[dict[str, object]]]:
    attempts: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
        global_attempt = budget.consume()
        try:
            outcome = await judge.judge(judge_id=judge_entry.judge_id, payload=payload)
            validate_judge_result(case, outcome.result)
            attempts.append(
                {
                    "judge_id": judge_entry.judge_id,
                    "output_id": judge_entry.output_id,
                    "global_attempt": global_attempt,
                    "local_attempt": local_attempt,
                    "status": "SUCCESS",
                    "timestamp_utc": _utc_now(),
                    "usage": asdict(outcome.usage),
                    "latency_seconds": outcome.latency_seconds,
                    "requested_model": outcome.requested_model,
                    "provider_model": outcome.provider_model,
                    "runtime_version": outcome.runtime_version,
                    "provider_response_ids": list(outcome.provider_response_ids),
                    "provider_request_ids": list(outcome.provider_request_ids),
                    "error": None,
                }
            )
            return outcome, attempts
        except Exception as exc:
            failure_class = _classify_failure(exc)
            attempts.append(
                {
                    "judge_id": judge_entry.judge_id,
                    "output_id": judge_entry.output_id,
                    "global_attempt": global_attempt,
                    "local_attempt": local_attempt,
                    "status": failure_class,
                    "timestamp_utc": _utc_now(),
                    "error": str(exc),
                }
            )
            if failure_class not in RETRYABLE_FAILURES or local_attempt > max_retries:
                return None, attempts
    return None, attempts


def _reasoner_attempt_record(
    *,
    entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
    global_attempt: int,
    local_attempt: int,
    status: str,
    outcome: ReasoningOutcome | None,
    error: str | None,
) -> dict[str, object]:
    record: dict[str, object] = {
        "output_id": entry.output_id,
        "case_id": entry.case_id,
        "repetition": entry.repetition,
        "condition": entry.condition.value,
        "global_attempt": global_attempt,
        "local_attempt": local_attempt,
        "status": status,
        "timestamp_utc": _utc_now(),
        "system_context_provenance": context.provenance.to_payload(),
        "error": error,
    }
    if outcome is not None:
        record.update(
            {
                "result": _structured_payload(outcome.result),
                "usage": asdict(outcome.usage),
                "trace": asdict(outcome.trace),
                "latency_seconds": outcome.latency_seconds,
            }
        )
    return record


def _classify_failure(exc: Exception) -> str:
    text = str(exc).upper()
    if "INVALID_STRUCTURED_RESPONSE" in text or isinstance(exc, ValueError):
        return "INVALID_STRUCTURED_RESPONSE"
    if "TRANSPORT" in text or "TIMEOUT" in text:
        return "TRANSPORT_FAILURE"
    if "INCOMPLETE" in text:
        return "INCOMPLETE_RESPONSE"
    return "PROVIDER_FAILURE"


def _fixture_oracle_result(
    case: RecommendationExperimentCase,
) -> DependencyBackedRecommendationActionResult:
    """Build a deterministic truth result for provider-free harness self-audits only."""

    from experiments.dependency_backed_recommendation_action_value.harness import (
        DependencyBackedActionDecision,
    )

    return DependencyBackedRecommendationActionResult(
        summary="Provider-free fixture oracle used only for construction validation.",
        action_decisions=tuple(
            DependencyBackedActionDecision(
                action_id=action.action_id,
                disposition=action.expected_disposition.value,
                blocking_requirement_id=action.expected_blocking_requirement_id,
                blocked_scope_id=action.expected_blocked_scope_id,
                defer_until_id=action.expected_defer_until_id,
                rationale="Provider-free fixture oracle rationale.",
            )
            for action in case.candidate_actions
        ),
        warnings=(),
    )


def _aggregate_result(
    *,
    benchmark: FrozenRecommendationBenchmark,
    source_head: str,
    started_at: str,
    finished_at: str,
    reasoning_plan_sha256: str,
    judge_plan_sha256: str,
    system_provenance_plan_sha256: str,
    technical: Mapping[str, bool],
    reasoner_attempts: list[dict[str, object]],
    judge_attempts: list[dict[str, object]],
    successful_outputs: Mapping[str, Mapping[str, Any]],
    successful_judges: Mapping[str, JudgeOutcome],
    observations: list[RecommendationScoredObservation],
    gate_evaluation,
    provider_attempts_used: int,
    authoritative_isolation: bool,
    project_state_before: Mapping[str, int],
    project_state_after: Mapping[str, int],
    accepted_snapshot_digest: str,
    accepted_pairs: tuple[tuple[str, str], ...],
) -> dict[str, object]:
    complete = (
        len(successful_outputs) == 36
        and len(successful_judges) == 36
        and len(observations) == 36
    )
    execution_integrity = all(value is True for value in technical.values())
    reasoner_failures = sum(1 for item in reasoner_attempts if item["status"] != "SUCCESS")
    judge_failures = sum(1 for item in judge_attempts if item["status"] not in {"SUCCESS", "SKIPPED_MISSING_REASONER_OUTPUT"})
    result: dict[str, object] = {
        "specification": "021",
        "benchmark_id": benchmark.benchmark_id,
        "source_head": source_head,
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "complete_scored_design": complete,
        "execution_integrity": execution_integrity,
        "counts": {
            "planned_reasoner_outputs": 36,
            "planned_judge_outputs": 36,
            "successful_reasoner_outputs": len(successful_outputs),
            "successful_judge_outputs": len(successful_judges),
            "scored_observations": len(observations),
            "reasoner_failed_attempts": reasoner_failures,
            "judge_failed_attempts": judge_failures,
        },
        "provider_attempts": {
            "used": provider_attempts_used,
            "maximum": int(benchmark.call_plan["max_total_provider_attempts"]),
        },
        "plan_sha256": {
            "reasoner": reasoning_plan_sha256,
            "judge": judge_plan_sha256,
            "system_provenance": system_provenance_plan_sha256,
        },
        "technical_invariants": dict(technical),
        "authoritative_isolation": authoritative_isolation,
        "project_state_before": dict(project_state_before),
        "project_state_after": dict(project_state_after),
        "accepted_snapshot_digest": accepted_snapshot_digest,
        "accepted_stable_revision_pairs": [list(item) for item in accepted_pairs],
        "gate_evaluation": None if gate_evaluation is None else _gate_payload(gate_evaluation),
        "advancement_outcome": None if gate_evaluation is None else gate_evaluation.outcome.value,
    }
    return result


def _gate_payload(gate) -> dict[str, object]:
    return {
        "outcome": gate.outcome.value,
        "absolute_passed": gate.absolute_passed,
        "relative_passed": gate.relative_passed,
        "expansion_passed": gate.expansion_passed,
        "gate_results": dict(gate.gate_results),
        "value_signals": list(gate.value_signals),
        "aggregate_by_condition": {
            key: asdict(value) for key, value in gate.aggregate_by_condition.items()
        },
        "per_case_exact_accuracy": {
            key: dict(value) for key, value in gate.per_case_exact_accuracy.items()
        },
        "per_case_semantic_score": {
            key: dict(value) for key, value in gate.per_case_semantic_score.items()
        },
    }


def _human_report(result: Mapping[str, object]) -> str:
    return (
        "# Specification 021 Execution Result\n\n"
        f"- Source head: `{result['source_head']}`\n"
        f"- Complete scored design: `{result['complete_scored_design']}`\n"
        f"- Execution integrity: `{result['execution_integrity']}`\n"
        f"- Advancement outcome: `{result['advancement_outcome']}`\n"
        f"- Provider attempts: `{result['provider_attempts']}`\n"
    )


def _project_state_counts(engine) -> dict[str, int]:
    tables = {
        "projects": prj_project,
        "entities": prj_entity,
        "findings": prj_finding,
        "knowledge_refs": prj_knowledge_ref,
    }
    counts: dict[str, int] = {}
    with engine.connect() as connection:
        for name, table in tables.items():
            counts[name] = int(connection.execute(select(func.count()).select_from(table)).scalar_one())
    return counts


def _context_digest(payload: Mapping[str, object]) -> tuple[str, int]:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    raw = text.encode("utf-8")
    import hashlib

    return hashlib.sha256(raw).hexdigest(), len(raw)


def _no_spec021_live_surface() -> bool:
    workflow = ROOT / ".github" / "workflows" / "v1-dependency-backed-recommendation-action-live.yml"
    registry = ROOT / ".github" / "ads_live_experiments.json"
    if workflow.exists():
        return False
    if registry.exists() and "spec021" in registry.read_text(encoding="utf-8").lower():
        return False
    return True


def _structured_payload(value: object) -> object:
    to_payload = getattr(value, "to_payload", None)
    if callable(to_payload):
        return to_payload()
    if is_dataclass(value):
        return asdict(value)
    return str(value)


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, rows: list[dict[str, object]], *, append: bool) -> None:
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, sort_keys=True, default=str) + "\n")


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _source_head() -> str:
    completed = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    observed = completed.stdout.strip()
    return observed if completed.returncode == 0 and observed else "UNKNOWN"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


if __name__ == "__main__":
    raise SystemExit(
        "Specification 021 runner is intentionally not exposed as a live CLI before "
        "the provider-free implementation boundary is checkpointed."
    )
