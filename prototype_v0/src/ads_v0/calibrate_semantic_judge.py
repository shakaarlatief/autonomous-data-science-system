"""Calibrate the preregistered two-pass semantic judge on baseline trajectories.

This command runs the condition-blinded semantic evaluator on the six already
observed development-calibration trajectories. It does not alter treatment
behavior, rerun B0/B1, or expose condition labels to the judge model.

Raw judge outputs are written under a caller-selected directory. The expected
use is an ignored ``results/raw/...`` location because the outputs can be large
and contain redundant evaluator text. A compact terminal summary reports score
vectors and whether blinded manual adjudication is required.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .semantic_judge import build_blinded_judge_packet, evaluate_two_passes


DEFAULT_RUN_IDS = (
    "dev-b0-03",
    "dev-b1-01",
    "dev-b0-04",
    "dev-b1-02",
    "dev-b1-03",
    "dev-b0-05",
)


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def run_calibration(
    *,
    bundle_dir: Path,
    results_root: Path,
    output_dir: Path,
    model: str,
    reasoning_effort: str,
    max_output_tokens: int,
) -> dict[str, Any]:
    """Evaluate the six fixed baseline calibration trajectories twice each."""

    output_dir.mkdir(parents=True, exist_ok=True)
    rows: list[dict[str, Any]] = []

    for run_id in DEFAULT_RUN_IDS:
        run_dir = results_root / run_id
        if not run_dir.is_dir():
            raise FileNotFoundError(f"Missing calibration trajectory: {run_dir}")

        packet = build_blinded_judge_packet(bundle_dir=bundle_dir, run_dir=run_dir)
        result = evaluate_two_passes(
            packet,
            model=model,
            reasoning_effort=reasoning_effort,
            max_output_tokens=max_output_tokens,
        )
        result_path = output_dir / f"{run_id}.json"
        _write_json(result_path, result)

        consensus = result["consensus"]
        rows.append(
            {
                "run_id": run_id,
                "packet_sha256": result["packet_sha256"],
                "consensus_scores": consensus["consensus_scores"],
                "semantic_critical_consensus": consensus[
                    "semantic_critical_consensus"
                ],
                "targeted_architecture_score": consensus[
                    "targeted_architecture_score"
                ],
                "strong_targeted_pass": consensus["strong_targeted_pass"],
                "manual_adjudication_required": consensus[
                    "manual_adjudication_required"
                ],
                "disagreements": consensus["disagreements"],
                "judge_pass_total_tokens": [
                    judge_pass["usage"].get("total_tokens")
                    for judge_pass in result["passes"]
                ],
            }
        )

        score_text = ", ".join(
            f"{name}={score}"
            for name, score in consensus["consensus_scores"].items()
        )
        print(
            f"{run_id}: targeted={consensus['targeted_architecture_score']} "
            f"manual={consensus['manual_adjudication_required']} | {score_text}"
        )

    summary = {
        "calibration_type": "pre_p0_two_pass_semantic_judge",
        "bundle": str(bundle_dir),
        "judge_model": model,
        "reasoning_effort": reasoning_effort,
        "runs": rows,
        "manual_adjudication_run_count": sum(
            bool(row["manual_adjudication_required"]) for row in rows
        ),
    }
    _write_json(output_dir / "calibration_summary.json", summary)
    return summary


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calibrate the blinded semantic judge on six B0/B1 trajectories."
    )
    parser.add_argument(
        "--bundle",
        type=Path,
        default=Path("generated/development"),
    )
    parser.add_argument(
        "--results-root",
        type=Path,
        default=Path("results/raw"),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("results/raw/judge-calibration-v0-1"),
    )
    parser.add_argument("--model", default="gpt-5.6-terra")
    parser.add_argument(
        "--reasoning-effort",
        choices=["none", "low", "medium", "high", "xhigh", "max"],
        default="high",
    )
    parser.add_argument("--max-output-tokens", type=int, default=30_000)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    summary = run_calibration(
        bundle_dir=args.bundle,
        results_root=args.results_root,
        output_dir=args.output,
        model=args.model,
        reasoning_effort=args.reasoning_effort,
        max_output_tokens=args.max_output_tokens,
    )
    print(
        "Manual-adjudication runs: "
        f"{summary['manual_adjudication_run_count']} / {len(summary['runs'])}"
    )
    print(f"Output: {args.output.resolve()}")


if __name__ == "__main__":
    main()
