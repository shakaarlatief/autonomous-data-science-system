from __future__ import annotations

import asyncio
import json
from pathlib import Path

from experiments.blocking_calibration import live_runner


LIVE_WORKFLOW = Path(".github/workflows/v1-blocking-calibration-live.yml")


def test_live_wrapper_injects_runtime_and_marks_only_execution_metadata(
    tmp_path: Path,
    monkeypatch,
) -> None:
    runtime_sentinel = object()
    captured: dict[str, object] = {}

    monkeypatch.setattr(
        live_runner,
        "OpenAIAgentsReasoningRuntime",
        lambda: runtime_sentinel,
    )

    async def fake_execute_provider_free_experiment(*, output_dir: Path, runtime):
        captured["runtime"] = runtime
        captured["output_dir"] = output_dir
        output_dir.mkdir(parents=True, exist_ok=True)
        result: dict[str, object] = {
            "environment": {
                "requested_model": "gpt-5.6-sol",
                "provider_free_implementation_boundary": True,
            },
            "advancement_outcome": "INCOMPLETE",
            "gate_evaluation": {"completed": False},
            "counts": {"successful_reasoner_outputs": 0},
        }
        (output_dir / "result.json").write_text(
            json.dumps(result),
            encoding="utf-8",
        )
        (output_dir / "RESULT.md").write_text("provider-neutral report\n", encoding="utf-8")
        return result

    monkeypatch.setattr(
        live_runner,
        "execute_provider_free_experiment",
        fake_execute_provider_free_experiment,
    )

    result = asyncio.run(live_runner.execute_live_experiment(output_dir=tmp_path))

    assert captured == {"runtime": runtime_sentinel, "output_dir": tmp_path}
    assert result["advancement_outcome"] == "INCOMPLETE"
    assert result["gate_evaluation"] == {"completed": False}
    environment = result["environment"]
    assert isinstance(environment, dict)
    assert environment["requested_model"] == "gpt-5.6-sol"
    assert environment["provider_free_implementation_boundary"] is False
    assert environment["execution_mode"] == "live"

    persisted = json.loads((tmp_path / "result.json").read_text(encoding="utf-8"))
    assert persisted == result
    assert (tmp_path / "RESULT.md").read_text(encoding="utf-8") == "provider-neutral report\n"


def test_live_workflow_is_fixed_to_governed_specification_020_boundary() -> None:
    text = LIVE_WORKFLOW.read_text(encoding="utf-8")

    required_fragments = (
        "workflow_dispatch:",
        "launch_id:",
        "expected_source_sha:",
        "confirmation:",
        "spec020-blocking-calibration-001",
        "RUN_SPEC_020_FROZEN",
        '${{ inputs.expected_source_sha }}',
        '${GITHUB_SHA}',
        "OPENAI_API_KEY",
        "Validate frozen provider-free implementation before live calls",
        "tests/unit/test_blocking_calibration_live_runner.py",
        "python -m experiments.blocking_calibration.live_runner",
        "openai-agents==0.19.4",
        "actions/upload-artifact@v4",
    )
    for fragment in required_fragments:
        assert fragment in text

    forbidden_fragments = (
        "model:",
        "prompt:",
        "command:",
        "benchmark_path:",
        "fixture_path:",
    )
    for fragment in forbidden_fragments:
        assert fragment not in text
