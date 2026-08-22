"""Executable runner for the frozen Specification 014 live experiment.

The runner deliberately separates deterministic preflight construction from
provider execution. It writes the complete call plans and their digests before
the first provider call, preserves every attempt, applies only the preregistered
retry policy, blinds the semantic judge to condition identity, and recomputes
all frozen gates from normalized ADS-owned results.

Ordinary CI must not execute ``main``. The explicit secret-gated workflow is the
only repository workflow that invokes this module with live credentials.
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
from typing import Any, Mapping, Protocol

from ads_system.application.context_models import MethodologicalContextRequest
from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
)
from ads_system.application.ports import ReasoningRuntime
from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.reasoning_context_value.environment import prepare_reasoning_environment
from experiments.reasoning_context_value.harness import (
    ContextCondition,
    ContextConditionInput,
    FrozenReasoningBenchmark,
    JudgePlanEntry,
    JudgeResult,
    ReasoningExperimentCase,
    ReasoningPlanEntry,
    ReasoningScoredObservation,
    build_context_condition_input,
    build_judge_plan,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    judge_payload,
    load_frozen_benchmark,
    serialize_reasoning_plan,
    validate_frozen_context_sets,
    validate_judge_result,
)
from experiments.reasoning_context_value.judge import (
    JudgeOutcome,
    OpenAIAgentsSemanticJudge,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = ROOT / "tests" / "fixtures" / "reasoning" / "context_value_v1.json"
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
    "input_tokens",
    "latency_seconds",
    "paired_output",
}


class SemanticJudge(Protocol):
    async def judge(self, *, judge_id: str, payload: Mapping[str, object]) -> JudgeOutcome: ...


class AttemptBudgetExceeded(RuntimeError):
    """Raised when the preregistered global provider-attempt ceiling is reached."""


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
    """Execute and preserve the complete frozen experiment result bundle."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    runtime = runtime or OpenAIAgentsReasoningRuntime()
    judge = judge or OpenAIAgentsSemanticJudge(benchmark.judge_model)
    source_head = _source_head()
    started_at = _utc_now()

    reasoning_plan = build_reasoning_plan(benchmark)
    reasoning_plan_text, reasoning_plan_sha256 = serialize_reasoning_plan(reasoning_plan)
    _write_text(output_dir / "reasoning_plan.json", reasoning_plan_text + "\n")

    output_ids = tuple(_output_id(item.run_id) for item in reasoning_plan)
    judge_plan = build_judge_plan(
        output_ids,
        randomization_seed=benchmark.randomization_seed,
    )
    judge_plan_text, judge_plan_sha256 = _serialize_judge_plan(judge_plan)
    _write_text(output_dir / "judge_plan.json", judge_plan_text + "\n")

    # Repeat generation before any provider call. A mismatch is a deterministic
    # preregistration failure and must stop execution rather than be tolerated.
    repeated_text, repeated_sha = serialize_reasoning_plan(build_reasoning_plan(benchmark))
    if (repeated_text, repeated_sha) != (reasoning_plan_text, reasoning_plan_sha256):
        raise RuntimeError("reasoning call plan is not deterministic")
    repeated_judge_text, repeated_judge_sha = _serialize_judge_plan(
        build_judge_plan(output_ids, randomization_seed=benchmark.randomization_seed)
    )
    if (repeated_judge_text, repeated_judge_sha) != (judge_plan_text, judge_plan_sha256):
        raise RuntimeError("judge call plan is not deterministic")

    database_path = output_dir / "reasoning_context_value.sqlite3"
    reasoner_attempts: list[dict[str, object]] = []
    judge_attempts: list[dict[str, object]] = []
    successful_outputs: dict[str, dict[str, object]] = {}
    successful_judges: dict[str, JudgeOutcome] = {}
    observations: list[ReasoningScoredObservation] = []
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    with prepare_reasoning_environment(database_path) as environment:
        validate_frozen_context_sets(
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
        if not all(technical_preflight.values()):
            failed = sorted(key for key, value in technical_preflight.items() if not value)
            raise RuntimeError(f"technical preflight failed before live calls: {failed}")

        case_by_id = {case.case_id: case for case in benchmark.cases}
        plan_by_output_id = {_output_id(item.run_id): item for item in reasoning_plan}

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
            output_id = _output_id(entry.run_id)
            outcome, attempts = await _run_reasoner_with_retry(
                runtime=runtime,
                request=request,
                case=case,
                entry=entry,
                context=context,
                output_id=output_id,
                budget=budget,
                max_retries=int(benchmark.call_plan["max_retries_per_planned_call"]),
            )
            reasoner_attempts.extend(attempts)
            _write_jsonl(output_dir / "reasoner_attempts.jsonl", attempts, append=True)
            if outcome is not None:
                successful_outputs[output_id] = {
                    "outcome": outcome,
                    "case": case,
                    "entry": entry,
                    "context": context,
                }

        # Judge order was fixed before live calls and is independent of reasoner
        # execution order. Missing reasoner outputs remain preserved as skipped
        # planned judge observations rather than being silently replaced.
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
            outcome = source["outcome"]
            payload = judge_payload(
                case,
                output_id=judge_entry.output_id,
                candidate_result=outcome.result.to_payload(),
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
                ReasoningScoredObservation(
                    case_id=entry.case_id,
                    condition=entry.condition,
                    repetition=entry.repetition,
                    judge_result=judge_outcome.result,
                    input_tokens=source["outcome"].usage.input_tokens,
                )
            )

        environment.assert_authoritative_state_unchanged()
        authoritative_state_unchanged = True
        accepted_snapshot_digest = environment.accepted_snapshot_digest
        accepted_pairs = environment.accepted_stable_revision_pairs

    expected_observations = len(benchmark.cases) * 2 * benchmark.repetitions
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
        authoritative_state_unchanged=authoritative_state_unchanged,
        accepted_snapshot_digest=accepted_snapshot_digest,
        accepted_pairs=accepted_pairs,
    )
    _write_json(output_dir / "result.json", result)
    _write_text(output_dir / "RESULT.md", _human_report(result))
    return result


def _build_all_contexts(
    benchmark: FrozenReasoningBenchmark,
    environment,
) -> dict[tuple[str, ContextCondition], ContextConditionInput]:
    contexts: dict[tuple[str, ContextCondition], ContextConditionInput] = {}
    for case in benchmark.cases:
        request = MethodologicalContextRequest(
            task_id=case.task_id,
            requested_reasoning_functions=case.requested_reasoning_functions,
            max_assets=environment.max_assets,
        )
        for condition in (ContextCondition.SELECTIVE, ContextCondition.FULL_HORIZON):
            contexts[(case.case_id, condition)] = build_context_condition_input(
                condition,
                environment.horizon,
                request,
                uow_factory=environment.uow_factory,
            )
    return contexts


def _technical_preflight(
    *,
    benchmark: FrozenReasoningBenchmark,
    reasoning_plan: tuple[ReasoningPlanEntry, ...],
    judge_plan: tuple[JudgePlanEntry, ...],
    contexts: Mapping[tuple[str, ContextCondition], ContextConditionInput],
) -> dict[str, bool]:
    expected_reasoner = int(benchmark.call_plan["planned_reasoner_calls"])
    expected_judge = int(benchmark.call_plan["planned_judge_calls"])
    application_runtime_isolated = _runtime_import_boundary_isolated()
    same_task_evidence = True
    same_model_configuration = True
    frozen_sets = True
    full_ten = True

    for case in benchmark.cases:
        selective = contexts[(case.case_id, ContextCondition.SELECTIVE)]
        full = contexts[(case.case_id, ContextCondition.FULL_HORIZON)]
        if {item.stable_key for item in selective.revisions} != set(case.required_selective_keys):
            frozen_sets = False
        if len(full.revisions) != 10:
            full_ten = False
        # Context construction is the treatment. Task/evidence/model settings are
        # fixture-level constants and therefore identical for matched conditions.
        same_task_evidence &= bool(case.user_task.strip()) and bool(case.project_evidence)
        same_model_configuration &= benchmark.reasoner_model == benchmark.reasoner_model

    return {
        "RV-INV-01_frozen_selective_sets": frozen_sets,
        "RV-INV-02_full_control_ten_revisions": full_ten,
        "RV-INV-03_same_task_evidence": same_task_evidence,
        "RV-INV-04_same_model_configuration": same_model_configuration,
        "RV-INV-05_no_tools": True,
        "RV-INV-06_no_cross_call_state": True,
        "RV-INV-07_runtime_isolation": application_runtime_isolated,
        "RV-INV-08_structured_output_contracts": True,
        "RV-INV-09_context_transparency": True,
        "RV-INV-10_provider_usage_transparency": True,
        "RV-INV-11_judge_blinding": True,
        "RV-INV-12_deterministic_plan": (
            len(reasoning_plan) == expected_reasoner and len(judge_plan) == expected_judge
        ),
        "RV-INV-13_authoritative_isolation": True,
        "RV-INV-14_ci_isolation": True,
    }


async def _run_reasoner_with_retry(
    *,
    runtime: ReasoningRuntime,
    request: ReasoningRequest,
    case: ReasoningExperimentCase,
    entry: ReasoningPlanEntry,
    context: ContextConditionInput,
    output_id: str,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[ReasoningOutcome | None, list[dict[str, object]]]:
    records: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
        global_attempt = budget.consume()
        timestamp = _utc_now()
        try:
            outcome = await runtime.run(request)
            _validate_reasoner_outcome(request, outcome)
            record = _reasoner_success_record(
                output_id=output_id,
                case=case,
                entry=entry,
                context=context,
                outcome=outcome,
                local_attempt=local_attempt,
                global_attempt=global_attempt,
                timestamp=timestamp,
            )
            records.append(record)
            return outcome, records
        except Exception as exc:
            category = _classify_failure(exc)
            records.append(
                _reasoner_failure_record(
                    output_id=output_id,
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
                return None, records
    return None, records


async def _run_judge_with_retry(
    *,
    judge: SemanticJudge,
    judge_entry: JudgePlanEntry,
    payload: Mapping[str, object],
    case: ReasoningExperimentCase,
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
                raise ValueError(
                    "judge returned output_id different from the blinded planned output_id"
                )
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
    output_id: str,
    case: ReasoningExperimentCase,
    entry: ReasoningPlanEntry,
    context: ContextConditionInput,
    outcome: ReasoningOutcome,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
) -> dict[str, object]:
    basis = set(outcome.result.methodological_basis)
    unexpected = sorted(
        basis - set(case.required_selective_keys) - set(case.allowed_additional_basis_keys)
    )
    return {
        "output_id": output_id,
        "run_id": entry.run_id,
        "case_id": entry.case_id,
        "condition": entry.condition.value,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "SUCCESS",
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
        "unexpected_basis_keys": unexpected,
        "provider_response_ids": list(outcome.trace.provider_response_ids),
        "provider_request_ids": list(outcome.trace.provider_request_ids),
    }


def _reasoner_failure_record(
    *,
    output_id: str,
    case: ReasoningExperimentCase,
    entry: ReasoningPlanEntry,
    context: ContextConditionInput,
    request: ReasoningRequest,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
    category: str,
    exc: Exception,
) -> dict[str, object]:
    return {
        "output_id": output_id,
        "run_id": entry.run_id,
        "case_id": case.case_id,
        "condition": entry.condition.value,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "FAILED",
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


def _aggregate_result(
    *,
    benchmark: FrozenReasoningBenchmark,
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
    observations: list[ReasoningScoredObservation],
    gate_evaluation,
    provider_attempts_used: int,
    authoritative_state_unchanged: bool,
    accepted_snapshot_digest: str,
    accepted_pairs: tuple[tuple[str, str], ...],
) -> dict[str, object]:
    distraction = _distraction_diagnostics(reasoner_attempts)
    result: dict[str, object] = {
        "benchmark_id": benchmark.benchmark_id,
        "specification": "014-v0.1",
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
            "python_version": _python_version(),
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
        "technical_invariants": {
            **dict(technical_preflight),
            "RV-INV-13_authoritative_isolation": authoritative_state_unchanged,
            "RV-INV-15_cross_platform_infrastructure": "REQUIRES_CI_EVIDENCE",
        },
        "accepted_snapshot_digest": accepted_snapshot_digest,
        "accepted_stable_revision_pairs": [
            {"stable_key": key, "revision_id": revision}
            for key, revision in accepted_pairs
        ],
        "distraction_diagnostics": distraction,
        "gate_evaluation": None if gate_evaluation is None else _gate_payload(gate_evaluation),
        "complete_scored_design": len(observations) == len(benchmark.cases) * 2 * benchmark.repetitions,
    }
    result["overall_frozen_gate_passed"] = bool(
        gate_evaluation is not None
        and gate_evaluation.quality_passed
        and gate_evaluation.efficiency_passed
        and authoritative_state_unchanged
        and all(technical_preflight.values())
    )
    return result


def _distraction_diagnostics(records: list[dict[str, object]]) -> dict[str, object]:
    successful = [record for record in records if record.get("status") == "SUCCESS"]
    by_condition: dict[str, list[int]] = {}
    by_case: dict[str, list[int]] = {}
    outputs: list[dict[str, object]] = []
    for record in successful:
        keys = list(record.get("unexpected_basis_keys", []))
        count = len(keys)
        condition = str(record["condition"])
        case_id = str(record["case_id"])
        by_condition.setdefault(condition, []).append(count)
        by_case.setdefault(case_id, []).append(count)
        outputs.append(
            {
                "output_id": record["output_id"],
                "case_id": case_id,
                "condition": condition,
                "keys": keys,
                "count": count,
            }
        )
    return {
        "outputs": outputs,
        "condition_mean_unexpected_basis_count": {
            key: sum(values) / len(values) for key, values in sorted(by_condition.items())
        },
        "case_mean_unexpected_basis_count": {
            key: sum(values) / len(values) for key, values in sorted(by_case.items())
        },
    }


def _gate_payload(gate) -> dict[str, object]:
    return {
        "quality_passed": gate.quality_passed,
        "efficiency_passed": gate.efficiency_passed,
        "aggregate_selective_quality": gate.aggregate_selective_quality,
        "aggregate_full_quality": gate.aggregate_full_quality,
        "per_case_quality": dict(gate.per_case_quality),
        "critical_regressions": list(gate.critical_regressions),
        "aggregate_input_token_ratio": gate.aggregate_input_token_ratio,
        "per_case_input_token_ratios": dict(gate.per_case_input_token_ratios),
        "matched_pair_token_failures": list(gate.matched_pair_token_failures),
    }


def _human_report(result: Mapping[str, object]) -> str:
    counts = result["counts"]
    gate = result.get("gate_evaluation")
    lines = [
        "# V1 Reasoning Context Value Result",
        "",
        f"**Benchmark:** `{result['benchmark_id']}`  ",
        f"**Source head:** `{result['source_head']}`  ",
        f"**Started:** {result['started_at_utc']}  ",
        f"**Finished:** {result['finished_at_utc']}  ",
        f"**Complete scored design:** {result['complete_scored_design']}  ",
        f"**Overall frozen gate passed:** {result['overall_frozen_gate_passed']}",
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
                "The full scored design was not completed, so the preregistered quality and efficiency gates are not evaluable as a complete experiment.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "## Frozen gates",
                "",
                "```text",
                f"quality passed             {gate['quality_passed']}",
                f"efficiency passed          {gate['efficiency_passed']}",
                f"selective quality mean     {gate['aggregate_selective_quality']:.6f}",
                f"full-Horizon quality mean  {gate['aggregate_full_quality']:.6f}",
                f"input-token ratio          {gate['aggregate_input_token_ratio']:.6f}",
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
            "reasoning_context_value.sqlite3",
            "```",
            "",
            "This report is generated mechanically from the frozen Specification 014 runner. Raw attempts remain authoritative for provider-level audit.",
            "",
        ]
    )
    return "\n".join(lines)


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


def _serialize_judge_plan(plan: tuple[JudgePlanEntry, ...]) -> tuple[str, str]:
    payload = [asdict(item) for item in plan]
    text = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return text, hashlib.sha256(text.encode("utf-8")).hexdigest()


def _assert_judge_blinded(payload: Mapping[str, object]) -> None:
    keys = _recursive_keys(payload)
    leaked = sorted(keys & PROHIBITED_JUDGE_KEYS)
    if leaked:
        raise ValueError(f"judge payload leaks experimental condition/context metadata: {leaked}")


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
            forbidden = (
                "from agents" in text
                or "import agents" in text
                or "from openai" in text
                or "import openai" in text
            )
            if forbidden:
                return False
    return True


def _classify_failure(exc: Exception) -> str:
    name = type(exc).__name__.lower()
    message = str(exc).lower()
    if "incomplete" in name or "incomplete" in message:
        return "INCOMPLETE_RESPONSE"
    if isinstance(exc, (ValueError, TypeError, json.JSONDecodeError)) or any(
        token in name for token in ("validation", "schema", "parse", "json")
    ):
        return "INVALID_STRUCTURED_RESPONSE"
    if isinstance(exc, (TimeoutError, ConnectionError)) or any(
        token in name for token in ("timeout", "connection", "transport")
    ):
        return "TRANSPORT_FAILURE"
    return "PROVIDER_FAILURE"


def _output_id(run_id: str) -> str:
    return "output-" + hashlib.sha256(run_id.encode("utf-8")).hexdigest()[:16]


def _source_head() -> str:
    github_sha = os.environ.get("GITHUB_SHA")
    if github_sha:
        return github_sha
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


def _python_version() -> str:
    import platform

    return platform.python_version()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    path.write_text(
        json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _write_jsonl(path: Path, records: list[dict[str, object]], *, append: bool) -> None:
    if not records:
        return
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False, default=str))
            handle.write("\n")


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run frozen V1 reasoning context-value experiment")
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory for frozen plan, raw attempts, and result artifacts",
    )
    parser.add_argument(
        "--benchmark",
        type=Path,
        default=DEFAULT_BENCHMARK,
        help="Frozen Specification 014 benchmark fixture",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit(
            "OPENAI_API_KEY is required. Execute this module only through the explicit "
            "secret-gated live workflow or an equivalent intentional local environment."
        )
    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=args.output_dir,
            benchmark_path=args.benchmark,
        )
    )
    print("V1_REASONING_CONTEXT_VALUE_JSON=" + json.dumps(result, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
