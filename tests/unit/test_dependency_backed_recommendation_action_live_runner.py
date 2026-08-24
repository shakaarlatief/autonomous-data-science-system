from __future__ import annotations

import asyncio
import json
from pathlib import Path

from experiments.dependency_backed_recommendation_action_value import live_runner


ROOT = Path(__file__).resolve().parents[2]
LIVE_WORKFLOW = (
    ROOT / ".github" / "workflows" / "v1-dependency-backed-recommendation-action-live.yml"
)


def test_live_wrapper_only_adds_execution_annotation(
    tmp_path: Path,
    monkeypatch,
) -> None:
    runtime_marker = object()
    captured: dict[str, object] = {}
    frozen_result: dict[str, object] = {
        "specification": "021",
        "complete_scored_design": True,
        "execution_integrity": True,
        "advancement_outcome": "SAFE_BUT_NOT_DIFFERENTIATED",
        "gate_evaluation": {"sentinel": "unchanged"},
        "counts": {"successful_reasoner_outputs": 36, "successful_judge_outputs": 36},
    }

    monkeypatch.setattr(
        live_runner,
        "OpenAIAgentsReasoningRuntime",
        lambda: runtime_marker,
    )

    async def fake_execute_frozen_experiment(*, output_dir: Path, runtime) -> dict[str, object]:
        captured["output_dir"] = output_dir
        captured["runtime"] = runtime
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / "result.json").write_text(
            json.dumps(frozen_result, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        return dict(frozen_result)

    monkeypatch.setattr(
        live_runner,
        "execute_frozen_experiment",
        fake_execute_frozen_experiment,
    )

    output_dir = tmp_path / "live-result"
    result = asyncio.run(live_runner.execute_live_experiment(output_dir=output_dir))

    assert captured == {"output_dir": output_dir, "runtime": runtime_marker}
    for key, value in frozen_result.items():
        assert result[key] == value
    assert result["execution"] == {
        "mode": "live",
        "governed": True,
        "specification": "021",
    }
    persisted = json.loads((output_dir / "result.json").read_text(encoding="utf-8"))
    assert persisted == result


def test_live_workflow_is_tightly_scoped_to_frozen_specification_021() -> None:
    text = LIVE_WORKFLOW.read_text(encoding="utf-8")

    assert "spec021-dependency-backed-recommendation-value-001" in text
    assert "RUN_SPEC_021_FROZEN" in text
    assert "inputs.expected_source_sha" in text
    assert "${GITHUB_SHA}" in text
    assert "OPENAI_API_KEY" in text
    assert "tests/unit/test_dependency_backed_recommendation_action_live_runner.py" in text
    assert "experiments.dependency_backed_recommendation_action_value.live_runner" in text
    assert "actions/upload-artifact@v4" in text

    forbidden_inputs = (
        "model:",
        "prompt:",
        "command:",
        "benchmark:",
        "fixture:",
        "workflow:",
        "ref:",
    )
    dispatch_block = text.split("workflow_dispatch:", 1)[1].split("permissions:", 1)[0]
    for token in forbidden_inputs:
        assert token not in dispatch_block
