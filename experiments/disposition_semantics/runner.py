"""Executable runner for the frozen Specification 016 diagnostic.

The runner separates deterministic preflight construction from provider
execution, writes the complete randomized call plan before the first provider
call, preserves every attempt, applies only the preregistered retry policy, and
recomputes all hard gates from normalized ADS-owned results.

Ordinary CI must not execute ``main``. The explicit secret-gated live workflow
is the only repository workflow that may invoke this module with live
credentials.
"""

from __future__ import annotations

import argparse
import asyncio
from dataclasses import asdict
from datetime import datetime, timezone
from importlib.metadata import PackageNotFoundError, version
import json
import os
from pathlib import Path
import platform
import subprocess
from typing import Mapping

from ads_system.application.ports import ReasoningRuntime
from ads_system.application.reasoning import ReasoningOutcome, ReasoningRequest
from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.disposition_semantics.harness import (
    DiagnosticOutcome,
    DispositionObservation,
    DispositionPair,
    DispositionPlanEntry,
    DispositionSemanticsResult,
    FrozenDispositionBenchmark,
    build_reasoning_plan,
    build_reasoning_request,
    evaluate_gates,
    historical_ra02_spec016_admissibility,
    load_frozen_benchmark,
    make_observation,
    pair_by_id,
    serialize_reasoning_plan,
    validate_result_for_pair,
)


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_BENCHMARK = ROOT / "tests" / "fixtures" / "reasoning" / "disposition_semantics_v1.json"
HISTORICAL_SPEC015_FIXTURE = ROOT / "tests" / "fixtures" / "reasoning" / "recommendation_action_v1.json"
RETRYABLE_FAILURES = {
    "TRANSPORT_FAILURE",
    "PROVIDER_FAILURE",
    "INCOMPLETE_RESPONSE",
    "INVALID_STRUCTURED_RESPONSE",
}


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
) -> dict[str, object]:
    """Execute and preserve the complete frozen Specification 016 bundle."""

    output_dir.mkdir(parents=True, exist_ok=True)
    benchmark = load_frozen_benchmark(benchmark_path)
    runtime = runtime or OpenAIAgentsReasoningRuntime()
    source_head = _source_head()
    started_at = _utc_now()

    plan = build_reasoning_plan(benchmark)
    plan_text, plan_sha256 = serialize_reasoning_plan(plan)
    _write_text(output_dir / "reasoning_plan.json", plan_text + "\n")

    repeated_text, repeated_sha = serialize_reasoning_plan(build_reasoning_plan(benchmark))
    if (repeated_text, repeated_sha) != (plan_text, plan_sha256):
        raise RuntimeError("Specification 016 call plan is not deterministic")

    technical_preflight = _technical_preflight(benchmark, plan)
    if not all(technical_preflight.values()):
        failed = sorted(key for key, value in technical_preflight.items() if not value)
        raise RuntimeError(f"technical preflight failed before live calls: {failed}")

    attempts: list[dict[str, object]] = []
    observations: list[DispositionObservation] = []
    successful_outputs = 0
    budget = ProviderAttemptBudget(int(benchmark.call_plan["max_total_provider_attempts"]))

    for entry in plan:
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
        _write_jsonl(output_dir / "reasoner_attempts.jsonl", records, append=True)
        if outcome is None:
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
        gate=gate,
    )
    _write_json(output_dir / "result.json", result)
    _write_text(output_dir / "RESULT.md", _human_report(result))
    return result


def _technical_preflight(
    benchmark: FrozenDispositionBenchmark,
    plan: tuple[DispositionPlanEntry, ...],
) -> dict[str, bool]:
    expected = int(benchmark.call_plan["planned_successful_reasoner_calls"])
    requests = [build_reasoning_request(benchmark=benchmark, plan_entry=entry) for entry in plan]
    return {
        "DS-INV-01_fixture_structurally_valid": True,
        "DS-INV-02_exact_36_call_plan": len(plan) == expected == 36,
        "DS-INV-03_unique_run_ids": len({entry.run_id for entry in plan}) == len(plan),
        "DS-INV-04_unique_nonces": len({entry.run_nonce for entry in plan}) == len(plan),
        "DS-INV-05_no_methodological_context": all(
            not request.knowledge_revisions
            and dict(request.methodological_context_payload) == {}
            for request in requests
        ),
        "DS-INV-06_truth_blinded_inputs": all(
            "expected_disposition" not in request.canonical_model_input()
            and "expected_defer_until_id" not in request.canonical_model_input()
            for request in requests
        ),
        "DS-INV-07_structured_output_type": all(
            request.structured_output_type is DispositionSemanticsResult
            for request in requests
        ),
        "DS-INV-08_no_tools_or_cross_call_state": True,
        "DS-INV-09_application_runtime_import_isolated": _runtime_import_boundary_isolated(),
        "DS-INV-10_historical_spec015_not_rescored": True,
    }


async def _run_with_retry(
    *,
    runtime: ReasoningRuntime,
    request: ReasoningRequest,
    pair: DispositionPair,
    entry: DispositionPlanEntry,
    budget: ProviderAttemptBudget,
    max_retries: int,
) -> tuple[ReasoningOutcome | None, list[dict[str, object]]]:
    records: list[dict[str, object]] = []
    for local_attempt in range(1, max_retries + 2):
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
        except Exception as exc:
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
    pair: DispositionPair,
    outcome: ReasoningOutcome,
) -> None:
    if not isinstance(outcome.result, DispositionSemanticsResult):
        raise ValueError(
            "reasoner did not return DispositionSemanticsResult; observed "
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
        raise ValueError("Specification 016 must not supply knowledge revisions")
    if outcome.usage.input_tokens <= 0:
        raise ValueError("provider did not report positive input token usage")
    if not outcome.trace.provider_model.strip():
        raise ValueError("provider model identity is empty")


def _success_record(
    *,
    request: ReasoningRequest,
    entry: DispositionPlanEntry,
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
    entry: DispositionPlanEntry,
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
    benchmark: FrozenDispositionBenchmark,
    source_head: str,
    started_at: str,
    finished_at: str,
    plan_sha256: str,
    technical_preflight: Mapping[str, bool],
    attempts: list[dict[str, object]],
    observations: list[DispositionObservation],
    successful_outputs: int,
    provider_attempts_used: int,
    gate,
) -> dict[str, object]:
    historical = historical_ra02_spec016_admissibility(HISTORICAL_SPEC015_FIXTURE)
    result: dict[str, object] = {
        "benchmark_id": benchmark.benchmark_id,
        "specification": "016-v0.1",
        "starting_merge_sha": benchmark.starting_merge_sha,
        "source_head": source_head,
        "started_at_utc": started_at,
        "finished_at_utc": finished_at,
        "reasoning_plan_sha256": plan_sha256,
        "environment": {
            "requested_model": benchmark.reasoner_model.requested_model,
            "reasoning_effort": benchmark.reasoner_model.reasoning_effort,
            "openai_agents_version": _package_version("openai-agents"),
            "openai_client_version": _package_version("openai"),
            "python_version": platform.python_version(),
        },
        "provider_attempts": {
            "used": provider_attempts_used,
            "maximum": int(benchmark.call_plan["max_total_provider_attempts"]),
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
        "historical_ra02_spec016_admissibility": historical,
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
        "defer_pointer_passed": gate.defer_pointer_passed,
        "not_now_null_pointer_passed": gate.not_now_null_pointer_passed,
        "all_hard_gates_passed": gate.all_hard_gates_passed,
        "aggregate_exact_disposition_accuracy": gate.aggregate_exact_disposition_accuracy,
        "correct_repetitions_by_variant": dict(gate.correct_repetitions_by_variant),
        "pair_side_correct_repetitions": {
            key: dict(value) for key, value in gate.pair_side_correct_repetitions.items()
        },
        "expected_defer_pointer_accuracy": gate.expected_defer_pointer_accuracy,
        "expected_not_now_null_pointer_accuracy": gate.expected_not_now_null_pointer_accuracy,
        "outcome": gate.outcome.value,
    }


def _human_report(result: Mapping[str, object]) -> str:
    counts = result["counts"]
    gate = result["gate_evaluation"]
    provider_attempts = result["provider_attempts"]
    lines = [
        "# V1 Disposition Semantics Diagnostic Result",
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
        f"validated outputs   {counts['validated_observations']}",
        f"failed attempts     {counts['failed_attempt_records']}",
        "```",
        "",
        "## Frozen gates",
        "",
        "```text",
        f"completed                         {gate['completed']}",
        f"structured validity               {gate['structured_validity_passed']}",
        f"aggregate exact accuracy          {gate['aggregate_exact_disposition_accuracy']:.6f}",
        f"aggregate accuracy gate           {gate['aggregate_accuracy_passed']}",
        f"variant majority gate             {gate['variant_majority_passed']}",
        f"pair polarity gate                {gate['pair_polarity_passed']}",
        f"DEFER pointer accuracy            {gate['expected_defer_pointer_accuracy']:.6f}",
        f"DEFER pointer gate                {gate['defer_pointer_passed']}",
        f"NOT_NOW null-pointer accuracy     {gate['expected_not_now_null_pointer_accuracy']:.6f}",
        f"NOT_NOW null-pointer gate         {gate['not_now_null_pointer_passed']}",
        "```",
        "",
        "## Historical Specification 015 diagnostic",
        "",
        "This diagnostic does not rescore Specification 015. It only tests whether its historical RA-02 expected-DEFER examples satisfy the stronger construction rule used by Specification 016.",
        "",
        "```text",
    ]
    for action_id, status in sorted(
        result["historical_ra02_spec016_admissibility"].items()
    ):
        lines.append(f"{action_id}: {status}")
    lines.extend(
        [
            "```",
            "",
            "## Audit artifacts",
            "",
            "```text",
            "reasoning_plan.json",
            "reasoner_attempts.jsonl",
            "result.json",
            "RESULT.md",
            "```",
            "",
            "This report is generated mechanically from the frozen Specification 016 runner. Raw attempt records remain the provider-level audit source.",
            "",
        ]
    )
    return "\n".join(lines)


def _usage_payload(outcome: ReasoningOutcome) -> dict[str, object]:
    usage = outcome.usage
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


def _package_version(package: str) -> str | None:
    try:
        return version(package)
    except PackageNotFoundError:
        return None


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
    parser = argparse.ArgumentParser(
        description="Run frozen Specification 016 disposition-semantics diagnostic"
    )
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
        help="Frozen Specification 016 benchmark fixture",
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
    print("V1_DISPOSITION_SEMANTICS_JSON=" + json.dumps(result, sort_keys=True, default=str))


if __name__ == "__main__":
    main()
