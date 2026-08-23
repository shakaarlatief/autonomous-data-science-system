from __future__ import annotations

import asyncio
import json
from pathlib import Path

from ads_system.application.reasoning import (
    ReasoningOutcome,
    ReasoningRequest,
    ReasoningTrace,
    ReasoningUsage,
)
from experiments.disposition_semantics.harness import DispositionSemanticsResult
from experiments.disposition_semantics.runner import execute_frozen_experiment


FIXTURE = Path("tests/fixtures/reasoning/disposition_semantics_v1.json")


class VisibleEvidenceFakeRuntime:
    """Provider-free runtime that uses only model-visible Specification 016 evidence."""

    def __init__(self, *, fail_first_request_once: bool = False) -> None:
        self.fail_first_request_once = fail_first_request_once
        self.calls = 0
        self.failed_run_ids: set[str] = set()

    async def run(self, request: ReasoningRequest) -> ReasoningOutcome:
        self.calls += 1
        if self.fail_first_request_once and not self.failed_run_ids:
            self.failed_run_ids.add(request.run_id)
            raise TimeoutError("deliberate provider-free transport failure")

        project_evidence = dict(request.project_evidence)
        triggers = project_evidence["available_defer_triggers"]
        variant = project_evidence["variant_project_evidence"]
        assert isinstance(triggers, list)
        assert isinstance(variant, dict)

        unresolved = [
            key
            for key, value in variant.items()
            if key.startswith("trigger.")
            and key.endswith(".status")
            and value == "UNRESOLVED"
        ]
        if unresolved:
            trigger_id = str(triggers[0]["trigger_id"])
            result = DispositionSemanticsResult(
                disposition="DEFER",
                defer_until_id=trigger_id,
                rationale="The supplied state explicitly makes this planned action wait for the supplied unresolved trigger.",
            )
        else:
            result = DispositionSemanticsResult(
                disposition="NOT_NOW",
                defer_until_id=None,
                rationale="No supplied trigger activates this action as current next work.",
            )

        return ReasoningOutcome(
            result=result,
            usage=ReasoningUsage(
                input_tokens=100,
                output_tokens=20,
                total_tokens=120,
            ),
            trace=ReasoningTrace(
                run_id=request.run_id,
                request_digest=request.semantic_digest(),
                methodological_context_sha256=request.methodological_context_sha256,
                knowledge_revisions=request.knowledge_revisions,
                requested_model=request.model_configuration.requested_model,
                provider_model="provider-visible-fake-model",
                runtime_name="visible-evidence-fake-runtime",
                runtime_version="1.0",
            ),
            latency_seconds=0.001,
        )


def test_runner_completes_full_frozen_design_with_visible_evidence_fake_runtime(
    tmp_path: Path,
) -> None:
    runtime = VisibleEvidenceFakeRuntime()
    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=tmp_path,
            benchmark_path=FIXTURE,
            runtime=runtime,
        )
    )

    assert result["complete_scored_design"] is True
    assert result["advancement_outcome"] == "DISPOSITION_BOUNDARY_SUPPORTED"
    assert result["overall_frozen_gate_passed"] is True
    assert result["counts"]["successful_reasoner_outputs"] == 36
    assert result["provider_attempts"]["used"] == 36
    assert result["gate_evaluation"]["aggregate_exact_disposition_accuracy"] == 1.0
    assert result["gate_evaluation"]["expected_defer_pointer_accuracy"] == 1.0
    assert result["gate_evaluation"]["expected_not_now_null_pointer_accuracy"] == 1.0

    assert (tmp_path / "reasoning_plan.json").exists()
    assert (tmp_path / "reasoner_attempts.jsonl").exists()
    assert (tmp_path / "result.json").exists()
    assert (tmp_path / "RESULT.md").exists()

    plan = json.loads((tmp_path / "reasoning_plan.json").read_text(encoding="utf-8"))
    attempts = [
        json.loads(line)
        for line in (tmp_path / "reasoner_attempts.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    assert len(plan) == 36
    assert len(attempts) == 36
    assert all(item["status"] == "SUCCESS" for item in attempts)
    assert all("expected_disposition" not in json.dumps(item) for item in attempts)


def test_runner_preserves_retry_attempt_without_changing_frozen_result(tmp_path: Path) -> None:
    runtime = VisibleEvidenceFakeRuntime(fail_first_request_once=True)
    result = asyncio.run(
        execute_frozen_experiment(
            output_dir=tmp_path,
            benchmark_path=FIXTURE,
            runtime=runtime,
        )
    )

    assert result["advancement_outcome"] == "DISPOSITION_BOUNDARY_SUPPORTED"
    assert result["provider_attempts"]["used"] == 37
    assert result["counts"]["failed_attempt_records"] == 1

    attempts = [
        json.loads(line)
        for line in (tmp_path / "reasoner_attempts.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
    ]
    failed = [item for item in attempts if item["status"] == "FAILED"]
    assert len(failed) == 1
    assert failed[0]["failure_category"] == "TRANSPORT_FAILURE"
