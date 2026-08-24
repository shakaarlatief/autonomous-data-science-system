from __future__ import annotations

import asyncio
import json
from pathlib import Path

from experiments.blocking_calibration import live_runner


LIVE_WORKFLOW = Path(".github/workflows/v1-blocking-calibration-live.yml")
RESULT_REPORT = Path("experiments/blocking_calibration/V1_BLOCKING_CALIBRATION_RESULT.md")
RESULT_CHECKPOINT = Path(
    "docs/checkpoints/171_recommended_vs_blocking_required_calibration_boundary_supported.md"
)


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


def test_live_workflow_is_retired_without_losing_frozen_provenance() -> None:
    """The one-shot live surface must not survive promotion after evidence is frozen."""
    assert not LIVE_WORKFLOW.exists()

    expected_fragments = (
        "82cfbdd38e9b6c5b4c6ab4e3bd1e4e20f545766a",
        "32701999678",
        "9510887324",
        "BLOCKING_BOUNDARY_SUPPORTED",
    )
    for path in (RESULT_REPORT, RESULT_CHECKPOINT):
        text = path.read_text(encoding="utf-8")
        for fragment in expected_fragments:
            assert fragment in text
