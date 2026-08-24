"""Explicit live execution entry point for frozen Specification 020.

The scientific experiment remains owned by :mod:`experiments.blocking_calibration.runner`.
This module contributes only the provider-capable execution boundary allowed after
Checkpoint 169: instantiate the accepted ADS-owned OpenAI Agents runtime, execute the
already frozen provider-neutral experiment, and mark the preserved environment record
as a live execution.

Importing this module does not call a provider.  A provider call can occur only when
``execute_live_experiment`` or the CLI ``main`` is invoked by the separately governed
live workflow with a provider credential present.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Sequence

from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.blocking_calibration.runner import execute_provider_free_experiment


def _mark_live_execution(result: dict[str, object], output_dir: Path) -> dict[str, object]:
    """Replace provider-free implementation metadata with exact live-run metadata.

    The frozen observations, gates, counts, plan identity, and scientific outcome are
    left untouched.  Only the execution-environment annotation is changed because the
    underlying generic runner is also used by provider-free injected runtimes.
    """

    raw_environment = result.get("environment")
    if not isinstance(raw_environment, dict):
        raise RuntimeError("Specification 020 result has no mutable environment record")

    environment = dict(raw_environment)
    environment["provider_free_implementation_boundary"] = False
    environment["execution_mode"] = "live"
    result["environment"] = environment

    (output_dir / "result.json").write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return result


async def execute_live_experiment(*, output_dir: Path) -> dict[str, object]:
    """Execute the exact frozen diagnostic through the accepted live runtime adapter."""

    runtime = OpenAIAgentsReasoningRuntime()
    result = await execute_provider_free_experiment(output_dir=output_dir, runtime=runtime)
    return _mark_live_execution(result, output_dir)


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute the frozen Specification 020 blocking-calibration diagnostic."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory in which the complete frozen result bundle is preserved.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point used only by the governed Specification 020 live workflow."""

    args = _parse_args(argv)
    result = asyncio.run(execute_live_experiment(output_dir=args.output_dir))
    outcome = result.get("advancement_outcome")
    print(f"Specification 020 advancement outcome: {outcome}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
