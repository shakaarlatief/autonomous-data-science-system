"""Explicit provider-capable entry point for frozen Specification 022.

Importing this module performs no provider call and does not initialize the
embedding model. Live execution occurs only when ``execute_live_experiment`` or
the CLI entry point is invoked by a later separately governed workflow.
"""

from __future__ import annotations

import argparse
import asyncio
from pathlib import Path
from typing import Sequence

from ads_system.infrastructure.runtime.openai_agents import (
    OpenAIAgentsReasoningRuntime,
)
from experiments.methodological_navigation_coverage.dense_fastembed import (
    FastEmbedDenseRetriever,
)
from experiments.methodological_navigation_coverage.runner import (
    execute_experiment,
)


async def execute_live_experiment(*, output_dir: Path) -> dict[str, object]:
    """Execute the frozen design through exact live runtime dependencies."""

    runtime = OpenAIAgentsReasoningRuntime()
    return await execute_experiment(
        output_dir=output_dir,
        reasoner_runtime=runtime,
        judge_runtime=runtime,
        dense_retriever_factory=lambda assets: FastEmbedDenseRetriever(assets),
        execution_mode="live",
    )


def _parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute the frozen Specification 022 methodological coverage diagnostic."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        required=True,
        help="Empty directory in which raw evidence is sealed before interpretation.",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    result = asyncio.run(execute_live_experiment(output_dir=args.output_dir))
    print(
        "Specification 022 execution complete: "
        f"{result['execution_complete']}; outcome={result['advancement_outcome']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
