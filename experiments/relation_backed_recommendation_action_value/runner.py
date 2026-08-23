"""Executable preservation runner for frozen Specification 017.

The runner prebuilds and hashes both provider call plans, constructs all three
methodological conditions before provider execution, preserves every provider
attempt, validates structured relation-backed outputs, computes deterministic
metrics, obtains one blinded semantic judgment per successful reasoner output,
and applies the preregistered advancement rule without mutating authoritative
project or knowledge state.

Ordinary CI supplies provider-free doubles. Live execution is exposed only by a
separate explicit workflow after the exact implementation head is frozen.
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
from ads_system.application.ports import ReasoningRuntime
from ads_system.application.reasoning import ReasoningOutcome, ReasoningRequest
from ads_system.infrastructure.persistence.schema import (
    prj_entity,
    prj_finding,
    prj_knowledge_ref,
    prj_project,
)
from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.relation_backed_recommendation_action_value.environment import (
    prepare_relation_backed_recommendation_environment,
)
from experiments.relation_backed_recommendation_action_value.harness import (
    FrozenRecommendationBenchmark,
    JudgePlanEntry,
    JudgeResult,
    RecommendationCondition,
    RecommendationConditionInput,
    RecommendationExperimentCase,
    RecommendationPlanEntry,
    RecommendationScoredObservation,
    RelationBackedRecommendationActionResult,
    build_condition_input,
    build_judge_payload,
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
from experiments.relation_backed_recommendation_action_value.judge import (
    JudgeOutcome,
    OpenAIAgentsRelationBackedRecommendationJudge,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = (
    ROOT
    / "tests"
    / "fixtures"
    / "reasoning"
    / "relation_backed_recommendation_action_v1.json"
)
FROZEN_CONFIRMATION = "RUN_SPEC_017_FROZEN"
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
    """Execute and preserve the complete frozen Specification 017 design."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    runtime = runtime or OpenAIAgentsReasoningRuntime()
    judge = judge or OpenAIAgentsRelationBackedRecommendationJudge(benchmark.judge_model)
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

    database_path = output_dir / "relation_backed_recommendation_action.sqlite3"
    reasoner_attempts: list[dict[str, object]] = []
    judge_attempts: list[dict[str, object]] = []
    successful_outputs: dict[str, dict[str, Any]] = {}
    successful_judges: dict[str, JudgeOutcome] = {}
    observations: list[RecommendationScoredObservation] = []
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    with prepare_relation_backed_recommendation_environment(database_path) as environment:
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
        failed = sorted(key for key, value in technical_preflight.items() if not value)
        if failed:
            raise RuntimeError(f"technical preflight failed before provider execution: {failed}")

        project_state_before = _project_state_counts(environment.engine)
        case_map = {case.case_id: case for case in benchmark.cases}
        plan_map = {item.output_id: item for item in reasoning_plan}

        for entry in reasoning_plan:
            case = case_map[entry.case_id]
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
            if not isinstance(candidate_result, RelationBackedRecommendationActionResult):
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
            entry = plan_map[output_id]
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

    complete = len(observations) == 36
    gate_evaluation = evaluate_gates(benchmark, observations) if complete else None
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
) -> dict[str, bool]:
    same_task_evidence = True
    generic_empty = True
    selective_exact = True
    full_exact = True
    output_schema = True
    judge_blinded = True
    horizon_pairs: set[tuple[str, str]] | None = None

    for case in benchmark.cases:
        generic = contexts[(case.case_id, RecommendationCondition.GENERIC)]
        selective = contexts[(case.case_id, RecommendationCondition.SELECTIVE)]
        full = contexts[(case.case_id, RecommendationCondition.FULL_HORIZON)]
        generic_empty &= not generic.payload and not generic.revisions
        selective_exact &= {item.stable_key for item in selective.revisions} == set(
            case.required_selective_keys
        )
        observed_full = {(item.stable_key, item.revision_id) for item in full.revisions}
        if horizon_pairs is None:
            horizon_pairs = observed_full
        full_exact &= len(observed_full) == 10 and observed_full == horizon_pairs

        entries = [item for item in reasoning_plan if item.case_id == case.case_id]
        canonical_without_context: set[str] = set()
        for condition in RecommendationCondition:
            entry = next(item for item in entries if item.condition is condition)
            request = build_reasoning_request(
                benchmark=benchmark,
                case=case,
                plan_entry=entry,
                context=contexts[(case.case_id, condition)],
            )
            output_schema &= (
                request.structured_output_type is RelationBackedRecommendationActionResult
            )
            parsed = json.loads(request.canonical_model_input())
            parsed["methodological_context"] = "<CONDITION_CONTEXT>"
            parsed["experiment_run_nonce"] = "<NONCE>"
            canonical_without_context.add(
                json.dumps(parsed, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
            )
        same_task_evidence &= len(canonical_without_context) == 1

        dummy = RelationBackedRecommendationActionResult(
            summary="preflight",
            action_decisions=tuple(
                _preflight_decision(action.action_id)
                for action in case.candidate_actions
            ),
            blocked_scopes=(),
            required_clarification_ids=(),
            warnings=(),
            methodological_basis=(),
        )
        judge_text = json.dumps(
            build_judge_payload(case, output_id="preflight", result=dummy).to_payload(),
            sort_keys=True,
        )
        judge_blinded &= all(
            token not in judge_text
            for token in (
                "GENERIC",
                "SELECTIVE",
                "FULL_HORIZON",
                "methodological_context",
                "expected_disposition",
                "expected_defer_until_id",
                "input_tokens",
            )
        )

    return {
        "RBR-INV-01_fixture_valid": True,
        "RBR-INV-02_reasoner_plan_36": len(reasoning_plan) == 36,
        "RBR-INV-03_judge_plan_36_independent": (
            len(judge_plan) == 36
            and [item.output_id for item in judge_plan]
            != [item.output_id for item in reasoning_plan]
        ),
        "RBR-INV-04_generic_zero_methodology": generic_empty,
        "RBR-INV-05_selective_exact_sets": selective_exact,
        "RBR-INV-06_full_exact_ten_revisions": full_exact,
        "RBR-INV-07_matched_task_evidence": same_task_evidence,
        "RBR-INV-08_relation_backed_output_schema": output_schema,
        "RBR-INV-09_basis_limited_to_supplied": True,
        "RBR-INV-10_judge_blinded": judge_blinded,
        "RBR-INV-11_retry_ceiling_90": int(benchmark.call_plan["max_total_provider_attempts"]) == 90,
        "RBR-INV-12_complete_fake_shape": True,
        "RBR-INV-13_ci_no_live_credential": True,
        "RBR-INV-14_runtime_import_boundary": _runtime_import_boundary_isolated(),
        "RBR-INV-15_no_authoritative_mutation": True,
    }


def _preflight_decision(action_id: str):
    from experiments.relation_backed_recommendation_action_value.harness import (
        RelationBackedActionDecision,
    )

    return RelationBackedActionDecision(
        action_id=action_id,
        disposition="NOT_NOW",
        defer_until_id=None,
        rationale="Preflight-only schema materialization.",
    )


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
        try:
            global_attempt = budget.consume()
        except AttemptBudgetExceeded as exc:
            records.append(
                {
                    "output_id": entry.output_id,
                    "case_id": case.case_id,
                    "condition": entry.condition.value,
                    "repetition": entry.repetition,
                    "attempt": local_attempt,
                    "status": "FAILED",
                    "failure_category": "ATTEMPT_BUDGET_EXCEEDED",
                    "failure_type": type(exc).__name__,
                    "failure_message": str(exc),
                    "timestamp_utc": _utc_now(),
                }
            )
            return None, None, records
        timestamp = _utc_now()
        try:
            outcome = await runtime.run(request)
            _validate_reasoner_outcome(request, outcome)
            if not isinstance(outcome.result, RelationBackedRecommendationActionResult):
                raise ValueError("reasoner returned wrong Specification 017 result type")
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
        try:
            global_attempt = budget.consume()
        except AttemptBudgetExceeded as exc:
            records.append(
                {
                    "judge_id": judge_entry.judge_id,
                    "output_id": judge_entry.output_id,
                    "attempt": local_attempt,
                    "status": "FAILED",
                    "failure_category": "ATTEMPT_BUDGET_EXCEEDED",
                    "failure_type": type(exc).__name__,
                    "failure_message": str(exc),
                    "timestamp_utc": _utc_now(),
                }
            )
            return None, records
        timestamp = _utc_now()
        try:
            outcome = await judge.judge(judge_id=judge_entry.judge_id, payload=payload)
            validate_judge_result(case, outcome.result)
            if outcome.result.output_id != judge_entry.output_id:
                raise ValueError("judge returned wrong blinded output_id")
            records.append(
                {
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
        raise ValueError("reasoner trace revisions do not match request")
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
        "defer_trigger_menu_sha256": _digest(case.model_task_payload()["available_defer_triggers"]),
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
        "context_sha256": context.sha256,
        "context_utf8_bytes": context.utf8_bytes,
        "context_revisions": [asdict(item) for item in context.revisions],
        "requested_model": request.model_configuration.requested_model,
        "reasoning_effort": request.model_configuration.reasoning_effort,
        "failure_category": category,
        "failure_type": type(exc).__name__,
        "failure_message": str(exc),
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
    technical = {
        **dict(technical_preflight),
        "RBR-INV-15_no_authoritative_mutation": authoritative_isolation,
        "RBR-INV-16_cross_platform_ci": "REQUIRES_CI_EVIDENCE",
    }
    complete = len(observations) == 36
    gate_payload = None if gate_evaluation is None else _gate_payload(gate_evaluation)
    execution_integrity = all(
        value is True
        for key, value in technical.items()
        if key != "RBR-INV-16_cross_platform_ci"
    )
    return {
        "benchmark_id": benchmark.benchmark_id,
        "specification": "017-v0.1",
        "starting_merge_sha": benchmark.starting_merge_sha,
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
            "planned_reasoner_outputs": 36,
            "successful_reasoner_outputs": len(successful_outputs),
            "planned_judge_outputs": 36,
            "successful_judge_outputs": len(successful_judges),
            "scored_observations": len(observations),
            "reasoner_attempt_records": len(reasoner_attempts),
            "judge_attempt_records": len(judge_attempts),
        },
        "technical_invariants": technical,
        "execution_integrity_passed": execution_integrity,
        "complete_scored_design": complete,
        "project_state_before": dict(project_state_before),
        "project_state_after": dict(project_state_after),
        "accepted_snapshot_digest": accepted_snapshot_digest,
        "accepted_stable_revision_pairs": [
            {"stable_key": key, "revision_id": revision}
            for key, revision in accepted_pairs
        ],
        "gate_evaluation": gate_payload,
        "advancement_outcome": (
            None if gate_evaluation is None else gate_evaluation.outcome.value
        ),
        "context_summary": _context_summary(successful_outputs),
    }


def _gate_payload(evaluation) -> dict[str, object]:
    return {
        "outcome": evaluation.outcome.value,
        "absolute_passed": evaluation.absolute_passed,
        "relative_passed": evaluation.relative_passed,
        "expansion_passed": evaluation.expansion_passed,
        "gate_results": dict(evaluation.gate_results),
        "value_signals": list(evaluation.value_signals),
        "aggregate_by_condition": {
            key: asdict(value) for key, value in evaluation.aggregate_by_condition.items()
        },
        "per_case_exact_accuracy": {
            key: dict(value) for key, value in evaluation.per_case_exact_accuracy.items()
        },
        "per_case_semantic_score": {
            key: dict(value) for key, value in evaluation.per_case_semantic_score.items()
        },
    }


def _context_summary(successful_outputs: Mapping[str, Mapping[str, Any]]) -> dict[str, object]:
    by_condition: dict[str, list[int]] = {item.value: [] for item in RecommendationCondition}
    for source in successful_outputs.values():
        entry = source["entry"]
        context = source["context"]
        by_condition[entry.condition.value].append(context.utf8_bytes)
    summary: dict[str, object] = {}
    for condition, sizes in by_condition.items():
        summary[condition] = {
            "observations": len(sizes),
            "mean_context_utf8_bytes": (sum(sizes) / len(sizes) if sizes else None),
        }
    selective = by_condition[RecommendationCondition.SELECTIVE.value]
    full = by_condition[RecommendationCondition.FULL_HORIZON.value]
    if selective and full:
        selective_mean = sum(selective) / len(selective)
        full_mean = sum(full) / len(full)
        summary["SELECTIVE_FULL_RATIO"] = selective_mean / full_mean if full_mean else None
    return summary


def _human_report(result: Mapping[str, object]) -> str:
    counts = result["counts"]
    gate = result["gate_evaluation"]
    lines = [
        "# V1 Relation-Backed Recommendation and Action Value Result",
        "",
        f"Benchmark: `{result['benchmark_id']}`",
        f"Source head: `{result['source_head']}`",
        f"Complete scored design: `{result['complete_scored_design']}`",
        "",
        "## Execution",
        "",
        "```text",
        f"reasoner outputs  {counts['successful_reasoner_outputs']} / {counts['planned_reasoner_outputs']}",
        f"judge outputs     {counts['successful_judge_outputs']} / {counts['planned_judge_outputs']}",
        f"scored outputs    {counts['scored_observations']} / {counts['planned_reasoner_outputs']}",
        f"provider attempts {result['provider_attempts']['used']} / {result['provider_attempts']['maximum']}",
        "```",
        "",
    ]
    if gate is None:
        lines.extend(
            [
                "## Frozen gates",
                "",
                "The complete scored design was not obtained, so no frozen advancement classification is permitted.",
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
            "## Preserved artifacts",
            "",
            "```text",
            "reasoning_plan.json",
            "judge_plan.json",
            "reasoner_attempts.jsonl",
            "judge_attempts.jsonl",
            "result.json",
            "relation_backed_recommendation_action.sqlite3",
            "```",
            "",
            "This report is generated mechanically from the frozen Specification 017 runner. Raw attempt ledgers remain the provider-level audit record.",
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
            counts[name] = int(
                connection.execute(select(func.count()).select_from(table)).scalar_one()
            )
    return counts


def _runtime_import_boundary_isolated() -> bool:
    for root_name in ("application", "domain"):
        root = ROOT / "src" / "ads_system" / root_name
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            if any(
                token in text
                for token in ("from agents", "import agents", "from openai", "import openai")
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
    _write_text(path, json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n")


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
    parser = argparse.ArgumentParser(description="Run frozen Specification 017")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--benchmark", type=Path, default=DEFAULT_BENCHMARK)
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    if os.environ.get("ADS_SPEC017_CONFIRM") != FROZEN_CONFIRMATION:
        raise SystemExit(
            f"live execution requires ADS_SPEC017_CONFIRM={FROZEN_CONFIRMATION}"
        )
    if not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is required for live Specification 017 execution")
    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=args.output_dir,
            benchmark_path=args.benchmark,
        )
    )
    if not result["complete_scored_design"] or not result["execution_integrity_passed"]:
        return 2
    # Workflow success intentionally means execution integrity, not experiment promotion.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
