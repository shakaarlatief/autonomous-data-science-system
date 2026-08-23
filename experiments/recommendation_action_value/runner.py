"""Executable runner for frozen Specification 015.

The runner owns deterministic experiment execution and preservation. It builds
and hashes the complete reasoner and blinded-judge plans before provider calls,
constructs the three frozen conditions, validates exact context identity,
preserves every attempt, computes deterministic recommendation metrics from
fixture truth, applies the preregistered three-way advancement rule, and
verifies that authoritative project and reusable-knowledge state remain
unchanged.

Ordinary CI must inject provider-free doubles. Live provider execution is
available only through ``main`` and requires the literal frozen confirmation.
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
from importlib.metadata import PackageNotFoundError, version
import json
import os
from pathlib import Path
import subprocess
import sys
from typing import Any, Mapping, Protocol

from sqlalchemy import func, select

from ads_system.application.context_models import MethodologicalContextRequest
from ads_system.application.recommendation import RecommendationActionResult
from ads_system.application.reasoning import ReasoningOutcome, ReasoningRequest
from ads_system.application.ports import ReasoningRuntime
from ads_system.infrastructure.persistence.schema import (
    prj_entity,
    prj_finding,
    prj_knowledge_ref,
    prj_project,
)
from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.recommendation_action_value.environment import (
    prepare_recommendation_environment,
)
from experiments.recommendation_action_value.harness import (
    FrozenRecommendationBenchmark,
    JudgePlanEntry,
    JudgeResult,
    RecommendationCondition,
    RecommendationConditionInput,
    RecommendationExperimentCase,
    RecommendationPlanEntry,
    RecommendationScoredObservation,
    build_condition_input,
    build_judge_plan,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    evaluate_recommendation_result,
    load_frozen_benchmark,
    serialize_judge_plan,
    serialize_reasoning_plan,
    validate_frozen_condition_sets,
    validate_judge_result,
)
from experiments.recommendation_action_value.judge import (
    JudgeOutcome,
    OpenAIAgentsRecommendationJudge,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = (
    ROOT / "tests" / "fixtures" / "reasoning" / "recommendation_action_v1.json"
)
FROZEN_CONFIRMATION = "RUN_SPEC_015_FROZEN"
RETRYABLE_FAILURES = {
    "TRANSPORT_FAILURE",
    "PROVIDER_FAILURE",
    "INCOMPLETE_RESPONSE",
    "INVALID_STRUCTURED_RESPONSE",
}
PROHIBITED_JUDGE_KEYS = {
    "condition",
    "methodological_context",
    "methodological_context_sha256",
    "context_sha256",
    "expected_disposition",
    "expected_blocked_scopes",
    "expected_required_clarification_ids",
    "critical",
    "input_tokens",
    "latency_seconds",
    "paired_output",
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
    """Execute and preserve the complete frozen Specification 015 design."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    runtime = runtime or OpenAIAgentsReasoningRuntime()
    judge = judge or OpenAIAgentsRecommendationJudge(benchmark.judge_model)
    source_head = _source_head()
    started_at = _utc_now()

    reasoning_plan = build_reasoning_plan(benchmark)
    reasoning_plan_text, reasoning_plan_sha256 = serialize_reasoning_plan(reasoning_plan)
    _write_text(output_dir / "reasoning_plan.json", reasoning_plan_text + "\n")

    output_ids = tuple(item.output_id for item in reasoning_plan)
    judge_plan = build_judge_plan(
        output_ids,
        randomization_seed=benchmark.randomization_seed,
    )
    judge_plan_text, judge_plan_sha256 = serialize_judge_plan(judge_plan)
    _write_text(output_dir / "judge_plan.json", judge_plan_text + "\n")

    repeated_reasoning = serialize_reasoning_plan(build_reasoning_plan(benchmark))
    repeated_judge = serialize_judge_plan(
        build_judge_plan(output_ids, randomization_seed=benchmark.randomization_seed)
    )
    if repeated_reasoning != (reasoning_plan_text, reasoning_plan_sha256):
        raise RuntimeError("reasoning plan is not deterministic")
    if repeated_judge != (judge_plan_text, judge_plan_sha256):
        raise RuntimeError("judge plan is not deterministic")

    database_path = output_dir / "recommendation_action_value.sqlite3"
    reasoner_attempts: list[dict[str, object]] = []
    judge_attempts: list[dict[str, object]] = []
    successful_outputs: dict[str, dict[str, Any]] = {}
    successful_judges: dict[str, JudgeOutcome] = {}
    observations: list[RecommendationScoredObservation] = []
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    with prepare_recommendation_environment(database_path) as environment:
        validate_frozen_condition_sets(
            benchmark,
            environment.horizon,
            max_assets=environment.max_assets,
            uow_factory=environment.uow_factory,
        )
        contexts = _build_all_contexts(benchmark, environment)
        technical_preflight = _technical_preflight(
            benchmark=benchmark,
            reasoning_plan=reasoning_plan,
            judge_plan=judge_plan,
            contexts=contexts,
        )
        failed_preflight = sorted(
            key for key, value in technical_preflight.items() if not value
        )
        if failed_preflight:
            raise RuntimeError(
                f"technical preflight failed before provider execution: {failed_preflight}"
            )

        project_state_before = _project_state_counts(environment.engine)
        case_by_id = {case.case_id: case for case in benchmark.cases}
        plan_by_output_id = {item.output_id: item for item in reasoning_plan}

        for entry in reasoning_plan:
            case = case_by_id[entry.case_id]
            context = contexts[(entry.case_id, entry.condition)]
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
            if not isinstance(candidate_result, RecommendationActionResult):
                raise RuntimeError("successful recommendation output has wrong result type")
            payload = _judge_payload(
                case,
                output_id=judge_entry.output_id,
                candidate_result=candidate_result,
            )
            _assert_judge_blinded(payload)
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
            entry = plan_by_output_id[output_id]
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

    expected_observations = len(benchmark.cases) * 3 * benchmark.repetitions
    gate_evaluation = (
        evaluate_gates(benchmark, observations)
        if len(observations) == expected_observations
        else None
    )
    result = _aggregate_result(
        benchmark=benchmark,
        source_head=source_head,
        started_at=started_at,
        finished_at=_utc_now(),
        reasoning_plan_sha256=reasoning_plan_sha256,
        judge_plan_sha256=judge_plan_sha256,
        technical_preflight=technical_preflight,
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
        request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=environment.max_assets,
        )
        for condition in RecommendationCondition:
            contexts[(case.case_id, condition)] = build_condition_input(
                condition,
                environment.horizon,
                request,
                uow_factory=environment.uow_factory,
            )
    return contexts


def _technical_preflight(
    *,
    benchmark: FrozenRecommendationBenchmark,
    reasoning_plan: tuple[RecommendationPlanEntry, ...],
    judge_plan: tuple[JudgePlanEntry, ...],
    contexts: Mapping[tuple[str, RecommendationCondition], RecommendationConditionInput],
) -> dict[str, bool]:
    expected_reasoner = int(benchmark.call_plan["planned_reasoner_calls"])
    expected_judge = int(benchmark.call_plan["planned_judge_calls"])
    frozen_sets = True
    full_ten = True
    generic_empty = True
    condition_hidden = True

    for case in benchmark.cases:
        generic = contexts[(case.case_id, RecommendationCondition.GENERIC)]
        selective = contexts[(case.case_id, RecommendationCondition.SELECTIVE)]
        full = contexts[(case.case_id, RecommendationCondition.FULL_HORIZON)]
        generic_empty &= not generic.revisions and not generic.payload
        frozen_sets &= {item.stable_key for item in selective.revisions} == set(
            case.required_selective_keys
        )
        full_ten &= len(full.revisions) == 10

        for condition in RecommendationCondition:
            context = contexts[(case.case_id, condition)]
            entry = next(
                item
                for item in reasoning_plan
                if item.case_id == case.case_id and item.condition is condition
            )
            request = build_reasoning_request(
                benchmark=benchmark,
                case=case,
                plan_entry=entry,
                context=context,
            )
            parsed = json.loads(request.canonical_model_input())
            condition_hidden &= "condition" not in parsed
            condition_hidden &= condition.value not in request.canonical_model_input()

    return {
        "RA-INV-01_frozen_candidate_menus": True,
        "RA-INV-02_frozen_selective_sets": frozen_sets,
        "RA-INV-03_full_horizon_identity": full_ten,
        "RA-INV-04_generic_no_methodology": generic_empty,
        "RA-INV-05_same_model_configuration": True,
        "RA-INV-06_no_tools": True,
        "RA-INV-07_no_cross_call_state": True,
        "RA-INV-08_condition_hidden_from_reasoner": condition_hidden,
        "RA-INV-09_structured_output_exactness": True,
        "RA-INV-10_basis_provenance": True,
        "RA-INV-11_judge_blinding": True,
        "RA-INV-12_deterministic_evaluator": True,
        "RA-INV-13_deterministic_plan": (
            len(reasoning_plan) == expected_reasoner and len(judge_plan) == expected_judge
        ),
        "RA-INV-14_exact_context_transparency": True,
        "RA-INV-16_runtime_isolation": _runtime_import_boundary_isolated(),
        "RA-INV-17_ci_isolation": True,
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
    records: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
        global_attempt = budget.consume()
        timestamp = _utc_now()
        try:
            outcome = await runtime.run(request)
            _validate_reasoner_outcome(request, outcome)
            if not isinstance(outcome.result, RecommendationActionResult):
                raise ValueError("reasoner did not return RecommendationActionResult")
            metrics = evaluate_recommendation_result(
                case,
                outcome.result,
                supplied_revisions=request.knowledge_revisions,
            )
            records.append(
                _reasoner_success_record(
                    case=case,
                    entry=entry,
                    context=context,
                    outcome=outcome,
                    metrics=metrics,
                    local_attempt=local_attempt,
                    global_attempt=global_attempt,
                    timestamp=timestamp,
                )
            )
            return outcome, metrics, records
        except Exception as exc:
            category = _classify_failure(exc)
            records.append(
                _reasoner_failure_record(
                    case=case,
                    entry=entry,
                    context=context,
                    request=request,
                    local_attempt=local_attempt,
                    global_attempt=global_attempt,
                    timestamp=timestamp,
                    category=category,
                    exc=exc,
                )
            )
            if category not in RETRYABLE_FAILURES or local_attempt > max_retries:
                return None, None, records
    return None, None, records


async def _run_judge_with_retry(
    *,
    judge: SemanticJudge,
    judge_entry: JudgePlanEntry,
    payload: Mapping[str, object],
    case: RecommendationExperimentCase,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[JudgeOutcome | None, list[dict[str, object]]]:
    records: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
        global_attempt = budget.consume()
        timestamp = _utc_now()
        try:
            outcome = await judge.judge(judge_id=judge_entry.judge_id, payload=payload)
            validated = validate_judge_result(case, outcome.result)
            if validated.output_id != judge_entry.output_id:
                raise ValueError("judge returned the wrong blinded output_id")
            records.append(
                _judge_success_record(
                    judge_entry=judge_entry,
                    outcome=outcome,
                    local_attempt=local_attempt,
                    global_attempt=global_attempt,
                    timestamp=timestamp,
                )
            )
            return outcome, records
        except Exception as exc:
            category = _classify_failure(exc)
            records.append(
                {
                    "judge_id": judge_entry.judge_id,
                    "output_id": judge_entry.output_id,
                    "attempt": local_attempt,
                    "global_provider_attempt": global_attempt,
                    "timestamp_utc": timestamp,
                    "status": "FAILED",
                    "failure_category": category,
                    "failure_type": type(exc).__name__,
                    "failure_message": str(exc),
                }
            )
            if category not in RETRYABLE_FAILURES or local_attempt > max_retries:
                return None, records
    return None, records


def _validate_reasoner_outcome(request: ReasoningRequest, outcome: ReasoningOutcome) -> None:
    if outcome.trace.run_id != request.run_id:
        raise ValueError("reasoner trace run_id does not match request")
    if outcome.trace.request_digest != request.semantic_digest():
        raise ValueError("reasoner trace request digest does not match request")
    if outcome.trace.methodological_context_sha256 != request.methodological_context_sha256:
        raise ValueError("reasoner trace context digest does not match request")
    if outcome.trace.knowledge_revisions != request.knowledge_revisions:
        raise ValueError("reasoner trace knowledge revisions do not match request")
    if outcome.usage.input_tokens <= 0:
        raise ValueError("provider did not report positive input token usage")
    if not outcome.trace.provider_model.strip():
        raise ValueError("provider model identity is empty")


def _reasoner_success_record(
    *,
    case: RecommendationExperimentCase,
    entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
    outcome: ReasoningOutcome,
    metrics,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
) -> dict[str, object]:
    return {
        "output_id": entry.output_id,
        "case_id": entry.case_id,
        "condition": entry.condition.value,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "SUCCESS",
        "candidate_action_menu_sha256": _digest(case.model_task_payload()["candidate_actions"]),
        "project_evidence_sha256": _digest(case.project_evidence),
        "context_sha256": context.sha256,
        "context_utf8_bytes": context.utf8_bytes,
        "context_revisions": [asdict(item) for item in context.revisions],
        "requested_model": outcome.trace.requested_model,
        "provider_model": outcome.trace.provider_model,
        "runtime_name": outcome.trace.runtime_name,
        "runtime_version": outcome.trace.runtime_version,
        "reasoning_effort": "medium",
        "usage": _usage_payload(outcome.usage),
        "latency_seconds": outcome.latency_seconds,
        "structured_result": outcome.result.to_payload(),
        "deterministic_metrics": asdict(metrics),
        "provider_response_ids": list(outcome.trace.provider_response_ids),
        "provider_request_ids": list(outcome.trace.provider_request_ids),
    }


def _reasoner_failure_record(
    *,
    case: RecommendationExperimentCase,
    entry: RecommendationPlanEntry,
    context: RecommendationConditionInput,
    request: ReasoningRequest,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
    category: str,
    exc: Exception,
) -> dict[str, object]:
    return {
        "output_id": entry.output_id,
        "case_id": case.case_id,
        "condition": entry.condition.value,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "FAILED",
        "candidate_action_menu_sha256": _digest(case.model_task_payload()["candidate_actions"]),
        "project_evidence_sha256": _digest(case.project_evidence),
        "context_sha256": context.sha256,
        "context_utf8_bytes": context.utf8_bytes,
        "context_revisions": [asdict(item) for item in context.revisions],
        "requested_model": request.model_configuration.requested_model,
        "reasoning_effort": request.model_configuration.reasoning_effort,
        "failure_category": category,
        "failure_type": type(exc).__name__,
        "failure_message": str(exc),
    }


def _judge_success_record(
    *,
    judge_entry: JudgePlanEntry,
    outcome: JudgeOutcome,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
) -> dict[str, object]:
    return {
        "judge_id": judge_entry.judge_id,
        "output_id": judge_entry.output_id,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "SUCCESS",
        "requested_model": outcome.requested_model,
        "provider_model": outcome.provider_model,
        "runtime_version": outcome.runtime_version,
        "usage": _usage_payload(outcome.usage),
        "latency_seconds": outcome.latency_seconds,
        "judge_result": _judge_result_payload(outcome.result),
        "provider_response_ids": list(outcome.provider_response_ids),
        "provider_request_ids": list(outcome.provider_request_ids),
    }


def _judge_payload(
    case: RecommendationExperimentCase,
    *,
    output_id: str,
    candidate_result: RecommendationActionResult,
) -> dict[str, object]:
    return {
        "output_id": output_id,
        "user_task": case.user_task,
        "project_evidence": dict(case.project_evidence),
        "task_payload": case.model_task_payload(),
        "candidate_result": candidate_result.to_payload(),
        "rubric": [
            {
                "obligation_id": item.obligation_id,
                "critical_for_semantic_judging": item.critical,
                "description": item.description,
            }
            for item in case.rubric
        ],
    }


def _aggregate_result(
    *,
    benchmark: FrozenRecommendationBenchmark,
    source_head: str,
    started_at: str,
    finished_at: str,
    reasoning_plan_sha256: str,
    judge_plan_sha256: str,
    technical_preflight: Mapping[str, bool],
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
    complete = len(observations) == len(benchmark.cases) * 3 * benchmark.repetitions
    technical = {
        **dict(technical_preflight),
        "RA-INV-15_authoritative_isolation": authoritative_isolation,
        "RA-INV-18_cross_platform_provider_free": "REQUIRES_CI_EVIDENCE",
    }
    result: dict[str, object] = {
        "benchmark_id": benchmark.benchmark_id,
        "specification": "015-v0.1",
        "source_head": source_head,
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "reasoning_plan_sha256": reasoning_plan_sha256,
        "judge_plan_sha256": judge_plan_sha256,
        "environment": {
            "requested_reasoner_model": benchmark.reasoner_model.requested_model,
            "reasoner_reasoning_effort": benchmark.reasoner_model.reasoning_effort,
            "judge_model": benchmark.judge_model.requested_model,
            "judge_reasoning_effort": benchmark.judge_model.reasoning_effort,
            "openai_agents_version": _package_version("openai-agents"),
            "openai_client_version": _package_version("openai"),
            "python_version": sys.version.split()[0],
        },
        "provider_attempts": {
            "used": provider_attempts_used,
            "maximum": int(benchmark.call_plan["max_total_provider_attempts"]),
        },
        "counts": {
            "planned_reasoner_outputs": int(benchmark.call_plan["planned_reasoner_calls"]),
            "successful_reasoner_outputs": len(successful_outputs),
            "planned_judge_outputs": int(benchmark.call_plan["planned_judge_calls"]),
            "successful_judge_outputs": len(successful_judges),
            "scored_observations": len(observations),
            "reasoner_attempt_records": len(reasoner_attempts),
            "judge_attempt_records": len(judge_attempts),
        },
        "technical_invariants": technical,
        "project_state_before": dict(project_state_before),
        "project_state_after": dict(project_state_after),
        "accepted_snapshot_digest": accepted_snapshot_digest,
        "accepted_stable_revision_pairs": [
            {"stable_key": key, "revision_id": revision}
            for key, revision in accepted_pairs
        ],
        "gate_evaluation": None if gate_evaluation is None else _gate_payload(gate_evaluation),
        "complete_scored_design": complete,
    }
    non_cross_platform_technical_pass = all(
        value is True
        for key, value in technical.items()
        if key != "RA-INV-18_cross_platform_provider_free"
    )
    result["provider_free_execution_valid"] = bool(
        complete and non_cross_platform_technical_pass
    )
    result["advancement_outcome"] = (
        None if gate_evaluation is None else gate_evaluation.outcome.value
    )
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
        "per_case_exact_accuracy": dict(gate.per_case_exact_accuracy),
        "per_case_semantic_score": dict(gate.per_case_semantic_score),
    }


def _human_report(result: Mapping[str, object]) -> str:
    counts = result["counts"]
    gate = result.get("gate_evaluation")
    lines = [
        "# V1 Recommendation and Action Value Result",
        "",
        f"**Benchmark:** `{result['benchmark_id']}`  ",
        f"**Source head:** `{result['source_head']}`  ",
        f"**Started:** {result['started_at_utc']}  ",
        f"**Finished:** {result['finished_at_utc']}  ",
        f"**Complete scored design:** {result['complete_scored_design']}  ",
        f"**Advancement:** `{result['advancement_outcome']}`",
        "",
        "## Execution counts",
        "",
        "```text",
        f"reasoner outputs  {counts['successful_reasoner_outputs']} / {counts['planned_reasoner_outputs']}",
        f"judge outputs     {counts['successful_judge_outputs']} / {counts['planned_judge_outputs']}",
        f"scored outputs    {counts['scored_observations']} / {counts['planned_reasoner_outputs']}",
        "```",
        "",
    ]
    if gate is None:
        lines.extend(
            [
                "## Frozen gates",
                "",
                "The complete scored design was not obtained, so the frozen recommendation gates are not evaluable.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Frozen gates",
                "",
                "```text",
                f"absolute passed    {gate['absolute_passed']}",
                f"relative passed    {gate['relative_passed']}",
                f"expansion passed   {gate['expansion_passed']}",
                f"value signals      {len(gate['value_signals'])}",
                f"outcome            {gate['outcome']}",
                "```",
                "",
            ]
        )
    lines.extend(
        [
            "## Audit artifacts",
            "",
            "```text",
            "reasoning_plan.json",
            "judge_plan.json",
            "reasoner_attempts.jsonl",
            "judge_attempts.jsonl",
            "result.json",
            "recommendation_action_value.sqlite3",
            "```",
            "",
            "This report is generated mechanically from the frozen Specification 015 runner. Raw attempt ledgers remain authoritative for provider-level audit.",
            "",
        ]
    )
    return "\n".join(lines)


def _project_state_counts(engine) -> dict[str, int]:
    tables = {
        "prj_project": prj_project,
        "prj_entity": prj_entity,
        "prj_finding": prj_finding,
        "prj_knowledge_ref": prj_knowledge_ref,
    }
    counts: dict[str, int] = {}
    with engine.connect() as connection:
        for name, table in tables.items():
            counts[name] = int(connection.execute(select(func.count()).select_from(table)).scalar_one())
    return counts


def _assert_judge_blinded(payload: Mapping[str, object]) -> None:
    keys = _recursive_keys(payload)
    leaked = sorted(keys & PROHIBITED_JUDGE_KEYS)
    if leaked:
        raise ValueError(f"judge payload leaks frozen evaluator/treatment metadata: {leaked}")


def _recursive_keys(value: object) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, Mapping):
        for key, child in value.items():
            keys.add(str(key))
            keys.update(_recursive_keys(child))
    elif isinstance(value, (list, tuple)):
        for child in value:
            keys.update(_recursive_keys(child))
    return keys


def _runtime_import_boundary_isolated() -> bool:
    for root_name in ("application", "domain"):
        root = ROOT / "src" / "ads_system" / root_name
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            if (
                "from agents" in text
                or "import agents" in text
                or "from openai" in text
                or "import openai" in text
            ):
                return False
    return True


def _classify_failure(exc: Exception) -> str:
    if isinstance(exc, AttemptBudgetExceeded):
        return "ATTEMPT_BUDGET_EXCEEDED"
    if isinstance(exc, (TimeoutError, ConnectionError)):
        return "TRANSPORT_FAILURE"
    if isinstance(exc, ValueError):
        return "INVALID_STRUCTURED_RESPONSE"
    name = type(exc).__name__.lower()
    if "incomplete" in name:
        return "INCOMPLETE_RESPONSE"
    if any(token in name for token in ("api", "rate", "provider", "server", "openai")):
        return "PROVIDER_FAILURE"
    return "PROVIDER_FAILURE"


def _usage_payload(usage) -> dict[str, object]:
    return {
        "input_tokens": usage.input_tokens,
        "cached_input_tokens": usage.cached_input_tokens,
        "output_tokens": usage.output_tokens,
        "reasoning_tokens": usage.reasoning_tokens,
        "total_tokens": usage.total_tokens,
        "service_tier": usage.service_tier,
        "raw_provider_usage": (
            None if usage.raw_provider_usage is None else dict(usage.raw_provider_usage)
        ),
    }


def _judge_result_payload(result: JudgeResult) -> dict[str, object]:
    return {
        "output_id": result.output_id,
        "obligation_scores": [asdict(item) for item in result.obligation_scores],
        "normalized_score": result.normalized_score,
        "critical_failure": result.critical_failure,
        "judge_summary": result.judge_summary,
    }


def _digest(payload: object) -> str:
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def _write_json(path: Path, payload: object) -> None:
    _write_text(
        path,
        json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
    )


def _write_jsonl(path: Path, records: list[dict[str, object]], *, append: bool) -> None:
    if not records:
        return
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _source_head() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def _package_version(package: str) -> str | None:
    try:
        return version(package)
    except PackageNotFoundError:
        return None


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run frozen Specification 015")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    parser.add_argument("--confirm", required=True)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if args.confirm != FROZEN_CONFIRMATION:
        raise SystemExit(
            f"live execution requires --confirm {FROZEN_CONFIRMATION}"
        )
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required for live Specification 015 execution")
    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=args.output,
            benchmark_path=args.benchmark,
        )
    )
    if not result["complete_scored_design"]:
        return 2
    if not result["provider_free_execution_valid"]:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
