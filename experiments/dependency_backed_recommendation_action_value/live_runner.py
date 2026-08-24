"""Explicit live execution boundary for frozen Specification 021.

The scientific experiment remains owned by
:mod:`experiments.dependency_backed_recommendation_action_value.runner`. This
module contributes only the provider-capable execution wrapper permitted after
Checkpoint 176: invoke the already frozen experiment through the accepted ADS
runtime/judge boundary and annotate the preserved result as a governed live
execution.

Importing this module never contacts a provider. Provider calls can occur only
when ``execute_live_experiment`` or the CLI ``main`` is explicitly invoked with
the provider dependencies and credential available through the separately
governed target workflow.
"""

from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Sequence

from ads_system.infrastructure.runtime.openai_agents import OpenAIAgentsReasoningRuntime
from experiments.dependency_backed_recommendation_action_value.runner import (
    execute_frozen_experiment,
)


def _mark_live_execution(
    result: dict[str, object],
    output_dir: Path,
) -> dict[str, object]:
    """Annotate execution mode without modifying frozen scientific content."""

    result["execution"] = {
        "mode": "live",
        "governed": True,
        "specification": "021",
    }
    (output_dir / "result.json").write_text(
        json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return result


async def execute_live_experiment(*, output_dir: Path) -> dict[str, object]:
    """Execute Specification 021 through its accepted provider-capable runtime."""

    runtime = OpenAIAgentsReasoningRuntime()
    result = await execute_frozen_experiment(
        output_dir=output_dir,
        runtime=runtime,
    )
    return _mark_live_execution(result, output_dir)


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute the frozen Specification 021 recommendation-value experiment."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Directory in which the complete frozen result bundle is preserved.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    """CLI entry point used only by the governed Specification 021 live workflow."""

    args = _parse_args(argv)
    result = asyncio.run(execute_live_experiment(output_dir=args.output_dir))
    print(f"Specification 021 advancement outcome: {result.get('advancement_outcome')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
