"""Provider-free executable harness for the frozen Specification 020 diagnostic.

The runner writes and hashes the complete deterministic plan before invoking a
runtime, preserves every attempt, applies only the preregistered retry policy,
and recomputes every hard gate from hidden fixture truth.

There is intentionally no live runtime default and no command-line entry point
at this checkpoint. A caller must inject a ``ReasoningRuntime`` explicitly.
This keeps the implementation boundary provider-free until a later exact green
checkpoint separately authorizes live execution.
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import subprocess
from typing import Mapping

from ads_system.application.ports import ReasoningRuntime
from ads_system.application.reasoning import ReasoningOutcome, ReasoningRequest
from experiments.blocking_calibration.harness import (
    BlockingCalibrationResult,
    BlockingObservation,
    BlockingPair,
    BlockingPlanEntry,
    DiagnosticOutcome,
    FrozenBlockingBenchmark,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    load_frozen_benchmark,
    make_observation,
    pair_by_id,
    serialize_reasoning_plan,
    validate_result_for_pair,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = (
    ROOT / "tests" / "fixtures" / "reasoning" / "blocking_calibration_v1.json"
)
RETRYABLE_FAILURES = {
    "TRANSPORT_FAILURE",
    "PROVIDER_FAILURE",
    "INCOMPLETE_RESPONSE",
    "INVALID_STRUCTURED_RESPONSE",
}


class AttemptBudgetExceeded(RuntimeError):
    """Raised if a caller tries to consume beyond the frozen global ceiling."""


class ProviderAttemptBudget:
    """Track the hard Specification 020 provider-attempt ceiling."""

    def __init__(self, maximum: int) -> None:
        if maximum <= 0:
            raise ValueError("provider attempt maximum must be positive")
        self.maximum = maximum
        self.used = 0

    @property
    def exhausted(self) -> bool:
        return self.used >= self.maximum

    def consume(self) -> int:
        if self.exhausted:
            raise AttemptBudgetExceeded(
                f"provider attempt ceiling exhausted: {self.used}/{self.maximum}"
            )
        self.used += 1
        return self.used


async def execute_provider_free_experiment(
    *,
    output_dir: Path,
    runtime: ReasoningRuntime,
    benchmark_path: Path = DEFAULT_BENCHMARK,
) -> dict[str, object]:
    """Execute and preserve the frozen diagnostic using an injected runtime."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    source_head = _source_head()
    started_at = _utc_now()

    plan = build_reasoning_plan(benchmark)
    plan_text, plan_sha256 = serialize_reasoning_plan(plan)
    _write_text(output_dir / "reasoning_plan.json", plan_text + "\n")

    repeated_text, repeated_sha = serialize_reasoning_plan(build_reasoning_plan(benchmark))
    if (repeated_text, repeated_sha) != (plan_text, plan_sha256):
        raise RuntimeError("Specification 020 call plan is not deterministic")

    technical_preflight = _technical_preflight(benchmark, plan)
    if not all(technical_preflight.values()):
        failed = sorted(key for key, value in technical_preflight.items() if not value)
        raise RuntimeError(f"technical preflight failed before runtime calls: {failed}")

    attempts: list[dict[str, object]] = []
    observations: list[BlockingObservation] = []
    successful_outputs = 0
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    attempts_path = output_dir / "reasoner_attempts.jsonl"
    if attempts_path.exists():
        attempts_path.unlink()

    for entry in plan:
        if budget.exhausted:
            break

        pair = pair_by_id(benchmark, entry.pair_id)
        request = build_reasoning_request(benchmark=benchmark, plan_entry=entry)
        outcome, records = await _run_with_retry(
            runtime=runtime,
            request=request,
            pair=pair,
            entry=entry,
            budget=budget,
            max_retries=int(benchmark.call_plan["max_retries_per_planned_call"]),
        )
        attempts.extend(records)
        _write_jsonl(attempts_path, records, append=True)

        if outcome is None:
            if budget.exhausted:
                break
            continue

        successful_outputs += 1
        observations.append(make_observation(benchmark, entry, outcome.result))

    expected_outputs = int(benchmark.call_plan["planned_successful_reasoner_calls"])
    execution_complete = successful_outputs == expected_outputs
    gate = evaluate_gates(
        benchmark,
        observations,
        execution_complete=execution_complete,
    )
    result = _aggregate_result(
        benchmark=benchmark,
        source_head=source_head,
        started_at=started_at,
        finished_at=_utc_now(),
        plan_sha256=plan_sha256,
        technical_preflight=technical_preflight,
        attempts=attempts,
        observations=observations,
        successful_outputs=successful_outputs,
        provider_attempts_used=budget.used,
        attempt_budget_exhausted=budget.exhausted,
        gate=gate,
    )
    _write_json(output_dir / "result.json", result)
    _write_text(output_dir / "RESULT.md", _human_report(result))
    return result


def _technical_preflight(
    benchmark: FrozenBlockingBenchmark,
    plan: tuple[BlockingPlanEntry, ...],
) -> dict[str, bool]:
    expected = int(benchmark.call_plan["planned_successful_reasoner_calls"])
    requests = [build_reasoning_request(benchmark=benchmark, plan_entry=entry) for entry in plan]
    return {
        "BC-INV-01_fixture_structurally_valid": True,
        "BC-INV-02_exact_36_call_plan": len(plan) == expected == 36,
        "BC-INV-03_unique_run_ids": len({entry.run_id for entry in plan}) == len(plan),
        "BC-INV-04_unique_nonces": len({entry.run_nonce for entry in plan}) == len(plan),
        "BC-INV-05_no_methodological_context": all(
            not request.knowledge_revisions
            and dict(request.methodological_context_payload) == {}
            for request in requests
        ),
        "BC-INV-06_truth_blinded_inputs": all(
            "expected_disposition" not in request.canonical_model_input()
            and "expected_blocking_requirement_id" not in request.canonical_model_input()
            and "expected_blocked_scope_id" not in request.canonical_model_input()
            for request in requests
        ),
        "BC-INV-07_structured_output_type": all(
            request.structured_output_type is BlockingCalibrationResult
            for request in requests
        ),
        "BC-INV-08_no_tools_or_cross_call_state": True,
        "BC-INV-09_application_runtime_import_isolated": _runtime_import_boundary_isolated(),
        "BC-INV-10_no_live_runtime_default": True,
    }


async def _run_with_retry(
    *,
    runtime: ReasoningRuntime,
    request: ReasoningRequest,
    pair: BlockingPair,
    entry: BlockingPlanEntry,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[ReasoningOutcome | None, list[dict[str, object]]]:
    records: list[dict[str, object]] = []

    for local_attempt in range(1, max_retries + 2):
        if budget.exhausted:
            return None, records

        global_attempt = budget.consume()
        timestamp = _utc_now()
        try:
            outcome = await runtime.run(request)
            _validate_outcome(request, pair, outcome)
            records.append(
                _success_record(
                    request=request,
                    entry=entry,
                    outcome=outcome,
                    local_attempt=local_attempt,
                    global_attempt=global_attempt,
                    timestamp=timestamp,
                )
            )
            return outcome, records
        except Exception as exc:  # provider/runtime boundary is intentionally broad
            category = _classify_failure(exc)
            records.append(
                _failure_record(
                    request=request,
                    entry=entry,
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


def _validate_outcome(
    request: ReasoningRequest,
    pair: BlockingPair,
    outcome: ReasoningOutcome,
) -> None:
    if not isinstance(outcome.result, BlockingCalibrationResult):
        raise ValueError(
            "reasoner did not return BlockingCalibrationResult; observed "
            f"{type(outcome.result).__name__}"
        )
    validate_result_for_pair(pair, outcome.result)
    if outcome.trace.run_id != request.run_id:
        raise ValueError("reasoner trace run_id does not match request")
    if outcome.trace.request_digest != request.semantic_digest():
        raise ValueError("reasoner trace request digest does not match request")
    if outcome.trace.methodological_context_sha256 != request.methodological_context_sha256:
        raise ValueError("reasoner trace context digest does not match request")
    if outcome.trace.knowledge_revisions != ():
        raise ValueError("Specification 020 must not supply knowledge revisions")
    if outcome.usage.input_tokens <= 0:
        raise ValueError("runtime did not report positive input token usage")
    if not outcome.trace.provider_model.strip():
        raise ValueError("provider model identity is empty")


def _success_record(
    *,
    request: ReasoningRequest,
    entry: BlockingPlanEntry,
    outcome: ReasoningOutcome,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
) -> dict[str, object]:
    return {
        "run_id": entry.run_id,
        "pair_id": entry.pair_id,
        "variant_id": entry.variant_id,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "SUCCESS",
        "request_digest": request.semantic_digest(),
        "requested_model": outcome.trace.requested_model,
        "provider_model": outcome.trace.provider_model,
        "runtime_name": outcome.trace.runtime_name,
        "runtime_version": outcome.trace.runtime_version,
        "usage": _usage_payload(outcome),
        "latency_seconds": outcome.latency_seconds,
        "structured_result": outcome.result.to_payload(),
        "provider_response_ids": list(outcome.trace.provider_response_ids),
        "provider_request_ids": list(outcome.trace.provider_request_ids),
    }


def _failure_record(
    *,
    request: ReasoningRequest,
    entry: BlockingPlanEntry,
    local_attempt: int,
    global_attempt: int,
    timestamp: str,
    category: str,
    exc: Exception,
) -> dict[str, object]:
    return {
        "run_id": entry.run_id,
        "pair_id": entry.pair_id,
        "variant_id": entry.variant_id,
        "repetition": entry.repetition,
        "attempt": local_attempt,
        "global_provider_attempt": global_attempt,
        "timestamp_utc": timestamp,
        "status": "FAILED",
        "request_digest": request.semantic_digest(),
        "requested_model": request.model_configuration.requested_model,
        "failure_category": category,
        "failure_type": type(exc).__name__,
        "failure_message": str(exc),
    }


def _aggregate_result(
    *,
    benchmark: FrozenBlockingBenchmark,
    source_head: str,
    started_at: str,
    finished_at: str,
    plan_sha256: str,
    technical_preflight: Mapping[str, bool],
    attempts: list[dict[str, object]],
    observations: list[BlockingObservation],
    successful_outputs: int,
    provider_attempts_used: int,
    attempt_budget_exhausted: bool,
    gate,
) -> dict[str, object]:
    result: dict[str, object] = {
        "benchmark_id": benchmark.benchmark_id,
        "specification": "020-v0.1",
        "starting_integration_sha": benchmark.starting_integration_sha,
        "source_head": source_head,
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "reasoning_plan_sha256": plan_sha256,
        "environment": {
            "requested_model": benchmark.reasoner_model.requested_model,
            "reasoning_effort": benchmark.reasoner_model.reasoning_effort,
            "verbosity": benchmark.reasoner_model.verbosity,
            "max_output_tokens": benchmark.reasoner_model.max_output_tokens,
            "python_version": platform.python_version(),
            "provider_free_implementation_boundary": True,
        },
        "provider_attempts": {
            "used": provider_attempts_used,
            "maximum": int(benchmark.call_plan["max_total_provider_attempts"]),
            "exhausted": attempt_budget_exhausted,
        },
        "counts": {
            "planned_reasoner_outputs": int(
                benchmark.call_plan["planned_successful_reasoner_calls"]
            ),
            "successful_reasoner_outputs": successful_outputs,
            "attempt_records": len(attempts),
            "validated_observations": len(observations),
            "failed_attempt_records": sum(
                1 for item in attempts if item.get("status") == "FAILED"
            ),
        },
        "technical_invariants": dict(technical_preflight),
        "gate_evaluation": _gate_payload(gate),
        "complete_scored_design": gate.completed,
        "advancement_outcome": gate.outcome.value,
    }
    result["overall_frozen_gate_passed"] = bool(
        gate.outcome is DiagnosticOutcome.SUPPORTED
        and gate.all_hard_gates_passed
        and all(technical_preflight.values())
    )
    return result


def _gate_payload(gate) -> dict[str, object]:
    return {
        "completed": gate.completed,
        "structured_validity_passed": gate.structured_validity_passed,
        "aggregate_accuracy_passed": gate.aggregate_accuracy_passed,
        "variant_majority_passed": gate.variant_majority_passed,
        "pair_polarity_passed": gate.pair_polarity_passed,
        "blocking_joint_pointer_passed": gate.blocking_joint_pointer_passed,
        "recommended_null_pointer_passed": gate.recommended_null_pointer_passed,
        "all_hard_gates_passed": gate.all_hard_gates_passed,
        "aggregate_exact_disposition_accuracy": gate.aggregate_exact_disposition_accuracy,
        "correct_repetitions_by_variant": dict(gate.correct_repetitions_by_variant),
        "pair_side_correct_repetitions": {
            key: dict(value) for key, value in gate.pair_side_correct_repetitions.items()
        },
        "expected_blocking_requirement_pointer_accuracy": (
            gate.expected_blocking_requirement_pointer_accuracy
        ),
        "expected_blocked_scope_pointer_accuracy": (
            gate.expected_blocked_scope_pointer_accuracy
        ),
        "expected_blocking_joint_pointer_accuracy": (
            gate.expected_blocking_joint_pointer_accuracy
        ),
        "expected_recommended_null_pointer_correctness": (
            gate.expected_recommended_null_pointer_correctness
        ),
        "outcome": gate.outcome.value,
    }


def _human_report(result: Mapping[str, object]) -> str:
    counts = result["counts"]
    gate = result["gate_evaluation"]
    provider_attempts = result["provider_attempts"]
    assert isinstance(counts, dict)
    assert isinstance(gate, dict)
    assert isinstance(provider_attempts, dict)
    return "\n".join(
        [
            "# V1 RECOMMENDED versus BLOCKING_REQUIRED Calibration Diagnostic Result",
            "",
            f"**Benchmark:** `{result['benchmark_id']}`  ",
            f"**Source head:** `{result['source_head']}`  ",
            f"**Started:** {result['started_at_utc']}  ",
            f"**Finished:** {result['finished_at_utc']}  ",
            f"**Advancement outcome:** `{result['advancement_outcome']}`  ",
            f"**Overall frozen gate passed:** {result['overall_frozen_gate_passed']}",
            "",
            "## Execution",
            "",
            "```text",
            f"successful outputs  {counts['successful_reasoner_outputs']} / {counts['planned_reasoner_outputs']}",
            f"provider attempts   {provider_attempts['used']} / {provider_attempts['maximum']}",
            f"attempt cap reached {provider_attempts['exhausted']}",
            f"validated outputs   {counts['validated_observations']}",
            f"failed attempts     {counts['failed_attempt_records']}",
            "```",
            "",
            "## Frozen gates",
            "",
            "```text",
            f"completed                              {gate['completed']}",
            f"structured validity                    {gate['structured_validity_passed']}",
            f"aggregate exact accuracy               {gate['aggregate_exact_disposition_accuracy']:.6f}",
            f"aggregate accuracy gate                {gate['aggregate_accuracy_passed']}",
            f"every variant majority                 {gate['variant_majority_passed']}",
            f"every pair both sides majority         {gate['pair_polarity_passed']}",
            f"blocking requirement pointer accuracy  {gate['expected_blocking_requirement_pointer_accuracy']:.6f}",
            f"blocked-scope pointer accuracy          {gate['expected_blocked_scope_pointer_accuracy']:.6f}",
            f"joint blocking pointer accuracy         {gate['expected_blocking_joint_pointer_accuracy']:.6f}",
            f"recommended null-pointer correctness    {gate['expected_recommended_null_pointer_correctness']:.6f}",
            f"all hard gates                          {gate['all_hard_gates_passed']}",
            "```",
            "",
            "This report is mechanically derived from the frozen Specification 020 fixture.",
            "",
        ]
    )


def _usage_payload(outcome: ReasoningOutcome) -> dict[str, object]:
    return {
        "input_tokens": outcome.usage.input_tokens,
        "output_tokens": outcome.usage.output_tokens,
        "total_tokens": outcome.usage.total_tokens,
        "cached_input_tokens": outcome.usage.cached_input_tokens,
        "reasoning_tokens": outcome.usage.reasoning_tokens,
    }


def _classify_failure(exc: Exception) -> str:
    if isinstance(exc, (TimeoutError, ConnectionError)):
        return "TRANSPORT_FAILURE"
    if isinstance(exc, ValueError):
        return "INVALID_STRUCTURED_RESPONSE"
    message = str(exc).lower()
    if "incomplete" in message:
        return "INCOMPLETE_RESPONSE"
    return "PROVIDER_FAILURE"


def _runtime_import_boundary_isolated() -> bool:
    for root_name in ("application", "domain"):
        root = ROOT / "src" / "ads_system" / root_name
        for path in root.rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            if any(
                token in text
                for token in (
                    "from agents",
                    "import agents",
                    "from openai",
                    "import openai",
                )
            ):
                return False
    return True


def _source_head() -> str:
    try:
        completed = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return "UNKNOWN"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _write_json(path: Path, payload: Mapping[str, object]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _write_jsonl(
    path: Path,
    records: list[dict[str, object]],
    *,
    append: bool,
) -> None:
    mode = "a" if append else "w"
    with path.open(mode, encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, ensure_ascii=False) + "\n")


def _write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
