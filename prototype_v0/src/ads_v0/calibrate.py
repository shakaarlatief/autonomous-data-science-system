"""CLI for running real-model B0/B1 Prototype V0 calibration trajectories.

The command intentionally operates on an already generated and self-validated
benchmark bundle. It does not generate or mutate benchmark truth while a model
run is in progress.

The first supported real provider adapter is OpenAI Responses API, isolated
behind the provider-neutral ``ModelClient`` protocol. Provider/model choice is
experiment configuration rather than a production architecture decision.

Development-calibration defaults are deliberately conservative enough to limit
paid inference while still leaving substantially more room than the nine-turn
clean scripted trajectory. Reasoning-model output budgets must also accommodate
hidden reasoning tokens, not only visible JSON. The current 30,000-token ceiling
therefore follows the first real calibration failure and exceeds the 25,000-token
starting buffer recommended in current OpenAI reasoning guidance. These remain
calibration defaults, not frozen held-out budgets.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .openai_model import OpenAIResponsesModel
from .treatments import BaselineTreatmentRunner, TreatmentRunResult


DEFAULT_MAX_MODEL_CALLS = 20
DEFAULT_MAX_OUTPUT_TOKENS = 30_000
DEFAULT_MAX_GENERATION_RETRIES = 2


def run_openai_baseline(
    *,
    bundle_dir: Path,
    condition: str,
    run_id: str,
    output_dir: Path,
    model_name: str,
    reasoning_effort: str,
    max_model_calls: int,
    max_generation_retries: int,
    max_output_tokens: int,
) -> TreatmentRunResult:
    """Run one B0/B1 trajectory with the provisional OpenAI adapter."""

    output_dir.mkdir(parents=True, exist_ok=True)
    trace_path = output_dir / "trace.jsonl"

    model = OpenAIResponsesModel(
        model=model_name,
        reasoning_effort=reasoning_effort,
        max_output_tokens=max_output_tokens,
        store=True,
        use_previous_response_id=True,
    )
    runner = BaselineTreatmentRunner(
        bundle_dir=bundle_dir,
        model=model,
        condition=condition,
        run_id=run_id,
        max_model_calls=max_model_calls,
        max_generation_retries=max_generation_retries,
        trace_path=trace_path,
    )
    result = runner.run()
    _write_run_artifacts(
        result,
        output_dir,
        run_config={
            "provider": "openai",
            "requested_model": model_name,
            "reasoning_effort": reasoning_effort,
            "max_model_calls": max_model_calls,
            "max_generation_retries": max_generation_retries,
            "max_output_tokens_per_call": max_output_tokens,
        },
    )
    return result


def _write_run_artifacts(
    result: TreatmentRunResult,
    output_dir: Path,
    *,
    run_config: dict[str, Any],
) -> None:
    """Persist condition-neutral outputs plus baseline conversation diagnostics."""

    summary = {
        "condition": result.condition,
        "run_id": result.run_id,
        "completed": result.completed,
        "run_config": run_config,
        "model_calls": result.model_calls,
        "generation_attempts": result.generation_attempts,
        "generation_failures": result.generation_failures,
        "terminal_generation_error": result.terminal_generation_error,
        "input_tokens": result.input_tokens,
        "output_tokens": result.output_tokens,
        "total_tokens": result.total_tokens,
        "project_phase": result.workspace.phase.value,
        "deterministic_passed_all": result.deterministic_evaluation[
            "passed_all_deterministic"
        ],
        "deterministic_passed_critical": result.deterministic_evaluation[
            "passed_all_critical"
        ],
        "critical_failures": result.deterministic_evaluation["critical_failures"],
    }
    _write_json(output_dir / "summary.json", summary)
    _write_json(
        output_dir / "deterministic_evaluation.json",
        result.deterministic_evaluation,
    )
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


def _write_json(path: Path, payload: Any) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run a real-model Prototype V0 B0/B1 calibration trajectory."
    )
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--condition", choices=["B0", "B1"], required=True)
    parser.add_argument("--run-id", type=str, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--provider", choices=["openai"], default="openai")
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-5.6-terra",
        help="Provisional calibration model. Provider choice is not architecture.",
    )
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument(
        "--max-model-calls",
        type=int,
        default=DEFAULT_MAX_MODEL_CALLS,
        help="Development-calibration call ceiling; not a frozen held-out budget.",
    )
    parser.add_argument(
        "--max-generation-retries",
        type=int,
        default=DEFAULT_MAX_GENERATION_RETRIES,
        help=(
            "Additional provider-generation attempts allowed for one reasoning turn. "
            "The same policy should be used for all experimental conditions."
        ),
    )
    parser.add_argument(
        "--max-output-tokens",
        type=int,
        default=DEFAULT_MAX_OUTPUT_TOKENS,
        help=(
            "Per-call ceiling including reasoning, visible output, and formatting "
            "tokens where applicable."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.provider != "openai":  # Defensive for future provider additions.
        raise ValueError(f"Unsupported provider: {args.provider}")

    result = run_openai_baseline(
        bundle_dir=args.bundle,
        condition=args.condition,
        run_id=args.run_id,
        output_dir=args.output,
        model_name=args.model,
        reasoning_effort=args.reasoning_effort,
        max_model_calls=args.max_model_calls,
        max_generation_retries=args.max_generation_retries,
        max_output_tokens=args.max_output_tokens,
    )

    print(f"Condition: {result.condition}")
    print(f"Completed: {result.completed}")
    print(f"Successful model calls: {result.model_calls}")
    print(f"Generation attempts: {result.generation_attempts}")
    print(f"Generation failures: {result.generation_failures}")
    print(f"Total observed tokens: {result.total_tokens}")
    print(
        "Critical deterministic assertions passed: "
        f"{result.deterministic_evaluation['passed_all_critical']}"
    )
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
