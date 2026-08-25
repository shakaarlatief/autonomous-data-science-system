from __future__ import annotations

import asyncio
from pathlib import Path

import experiments.methodological_navigation_coverage.live_runner as live_runner


def test_live_entry_point_delegates_without_provider_call_on_import(
    monkeypatch,
    tmp_path: Path,
) -> None:
    observed = {}

    async def fake_execute_experiment(**kwargs):
        observed.update(kwargs)
        return {
            "execution_complete": False,
            "advancement_outcome": None,
        }

    monkeypatch.setattr(live_runner, "execute_experiment", fake_execute_experiment)
    result = asyncio.run(
        live_runner.execute_live_experiment(output_dir=tmp_path / "live")
    )

    assert result["execution_complete"] is False
    assert observed["execution_mode"] == "live"
    assert observed["output_dir"] == tmp_path / "live"
    assert observed["reasoner_runtime"] is observed["judge_runtime"]
    assert callable(observed["dense_retriever_factory"])
