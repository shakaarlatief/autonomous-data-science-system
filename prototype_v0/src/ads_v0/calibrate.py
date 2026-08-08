"""CLI for running real-model B0/B1 Prototype V0 calibration trajectories.

The command intentionally operates on an already generated and self-validated
benchmark bundle. It does not generate or mutate benchmark truth while a model
run is in progress.

The first supported real provider adapter is OpenAI Responses API, isolated
behind the provider-neutral ``ModelClient`` protocol. Provider/model choice is
experiment configuration rather than a production architecture decision.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .model import ModelMessage
from .openai_model import OpenAIResponsesModel
from .treatments import BaselineTreatmentRunner, TreatmentRunResult


def run_openai_baseline(
    *,
    bundle_dir: Path,
    condition: str,
    run_id: str,
    output_dir: Path,
    model_name: str,
    reasoning_effort: str,
    max_model_calls: int,
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
        trace_path=trace_path,
    )
    result = runner.run()
    _write_run_artifacts(result, output_dir, model_name, reasoning_effort)
    return result


def _write_run_artifacts(
    result: TreatmentRunResult,
    output_dir: Path,
    requested_model: str,
    reasoning_effort: str,
) -> None:
    """Persist condition-neutral outputs plus baseline conversation diagnostics."""

    summary = {
        "condition": result.condition,
        "run_id": result.run_id,
        "completed": result.completed,
        "requested_model": requested_model,
        "reasoning_effort": reasoning_effort,
        "model_calls": result.model_calls,
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
    parser.add_argument("--max-model-calls", type=int, default=40)
    parser.add_argument("--max-output-tokens", type=int, default=12_000)
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
        max_output_tokens=args.max_output_tokens,
    )

    print(f"Condition: {result.condition}")
    print(f"Completed: {result.completed}")
    print(f"Model calls: {result.model_calls}")
    print(f"Total tokens: {result.total_tokens}")
    print(
        "Critical deterministic assertions passed: "
        f"{result.deterministic_evaluation['passed_all_critical']}"
    )
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
