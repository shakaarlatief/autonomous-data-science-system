"""CLI for real-model P0 development calibration.

This command is intentionally introduced only after the B0/B1 calibration,
held-out protocol, held-out bundle identities, and semantic judge were frozen.
It runs P0 on the development bundle only. The development case may be used to
debug P0 implementation and understand its behavior, but it is not held-out
evidence of architectural success.

The defaults match the preregistered common held-out treatment envelope so P0
cannot be developed around an unbounded reasoning budget.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .p0 import P0TreatmentRunResult
from .p0_controller import P0TreatmentRunner
from .p0_openai_model import OpenAIP0ResponsesModel


DEFAULT_MAX_MODEL_CALLS = 24
DEFAULT_MAX_TOTAL_TOKENS = 250_000
DEFAULT_MAX_PYTHON_EXECUTION_ATTEMPTS = 12
DEFAULT_MAX_OUTPUT_TOKENS = 30_000
DEFAULT_MAX_GENERATION_RETRIES = 2


def run_openai_p0(
    *,
    bundle_dir: Path,
    run_id: str,
    output_dir: Path,
    model_name: str,
    reasoning_effort: str,
    max_model_calls: int,
    max_total_tokens: int,
    max_python_execution_attempts: int,
    max_generation_retries: int,
    max_output_tokens: int,
) -> P0TreatmentRunResult:
    """Run one P0 development trajectory using the registered model family."""

    output_dir.mkdir(parents=True, exist_ok=True)
    trace_path = output_dir / "trace.jsonl"
    model = OpenAIP0ResponsesModel(
        model=model_name,
        reasoning_effort=reasoning_effort,
        max_output_tokens=max_output_tokens,
        store=True,
        use_previous_response_id=True,
    )
    runner = P0TreatmentRunner(
        bundle_dir=bundle_dir,
        model=model,
        run_id=run_id,
        max_model_calls=max_model_calls,
        max_total_tokens=max_total_tokens,
        max_python_execution_attempts=max_python_execution_attempts,
        max_generation_retries=max_generation_retries,
        trace_path=trace_path,
    )
    result = runner.run()
    _write_p0_run_artifacts(
        result,
        output_dir,
        run_config={
            "provider": "openai",
            "requested_model": model_name,
            "reasoning_effort": reasoning_effort,
            "max_model_calls": max_model_calls,
            "max_total_tokens": max_total_tokens,
            "max_python_execution_attempts": max_python_execution_attempts,
            "max_generation_retries": max_generation_retries,
            "max_output_tokens_per_call": max_output_tokens,
        },
    )
    return result


def _write_p0_run_artifacts(
    result: P0TreatmentRunResult,
    output_dir: Path,
    *,
    run_config: dict[str, Any],
) -> None:
    behavior_evaluable = result.terminal_generation_error is None
    deterministic = result.deterministic_evaluation

    summary = {
        "condition": result.condition,
        "run_id": result.run_id,
        "completed": result.completed,
        "completed_within_budget": result.completed_within_budget,
        "budget_exhausted": result.budget_exhausted,
        "behavior_evaluable": behavior_evaluable,
        "run_config": run_config,
        "model_calls": result.model_calls,
        "generation_attempts": result.generation_attempts,
        "generation_failures": result.generation_failures,
        "terminal_generation_error": result.terminal_generation_error,
        "input_tokens": result.input_tokens,
        "output_tokens": result.output_tokens,
        "total_tokens": result.total_tokens,
        "python_execution_attempts": result.python_execution_attempts,
        "project_phase": result.workspace.phase.value,
        "deterministic_passed_all": (
            deterministic["passed_all_deterministic"] if behavior_evaluable else None
        ),
        "deterministic_passed_critical": (
            deterministic["passed_all_critical"] if behavior_evaluable else None
        ),
        "critical_failures": (
            deterministic["critical_failures"] if behavior_evaluable else []
        ),
    }
    _write_json(output_dir / "summary.json", summary)
    _write_json(output_dir / "deterministic_evaluation.json", deterministic)
    _write_json(
        output_dir / "milestones.json",
        {
            "phase_1_report": result.workspace.phase_1_report,
            "final_lock_report": result.workspace.final_lock_report,
            "final_report": result.workspace.final_report,
        },
    )
    _write_json(
        output_dir / "conversation.json",
        {
            "messages": [
                {"role": message.role, "content": message.content}
                for message in result.messages
            ]
        },
    )
    _write_json(output_dir / "p0_state.json", result.state_snapshot)
    _write_json(output_dir / "p0_state_history.json", list(result.state_history))
    _write_json(
        output_dir / "p0_knowledge_activations.json",
        list(result.knowledge_activations),
    )


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run one real-model Prototype V0 P0 development trajectory."
    )
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--run-id", type=str, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", type=str, default="gpt-5.6-terra")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--max-model-calls", type=int, default=DEFAULT_MAX_MODEL_CALLS)
    parser.add_argument("--max-total-tokens", type=int, default=DEFAULT_MAX_TOTAL_TOKENS)
    parser.add_argument(
        "--max-python-execution-attempts",
        type=int,
        default=DEFAULT_MAX_PYTHON_EXECUTION_ATTEMPTS,
    )
    parser.add_argument(
        "--max-generation-retries",
        type=int,
        default=DEFAULT_MAX_GENERATION_RETRIES,
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=DEFAULT_MAX_OUTPUT_TOKENS,
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    result = run_openai_p0(
        bundle_dir=args.bundle,
        run_id=args.run_id,
        output_dir=args.output,
        model_name=args.model,
        reasoning_effort=args.reasoning_effort,
        max_model_calls=args.max_model_calls,
        max_total_tokens=args.max_total_tokens,
        max_python_execution_attempts=args.max_python_execution_attempts,
        max_generation_retries=args.max_generation_retries,
        max_output_tokens=args.max_output_tokens,
    )

    print("Condition: P0")
    print(f"Completed: {result.completed}")
    print(f"Completed within budget: {result.completed_within_budget}")
    print(f"Budget exhausted: {result.budget_exhausted}")
    print(f"Successful model calls: {result.model_calls}")
    print(f"Generation attempts: {result.generation_attempts}")
    print(f"Generation failures: {result.generation_failures}")
    print(f"Total observed tokens: {result.total_tokens}")
    print(f"Python execution attempts: {result.python_execution_attempts}")

    behavior_evaluable = result.terminal_generation_error is None
    print(f"Behavioral evaluation eligible: {behavior_evaluable}")
    if behavior_evaluable:
        print(
            "Critical deterministic assertions passed: "
            f"{result.deterministic_evaluation['passed_all_critical']}"
        )
    else:
        print("Critical deterministic assertions passed: not scored")
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
