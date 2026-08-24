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
from experiments.blocking_calibration.harness import BlockingCalibrationResult
from experiments.blocking_calibration.runner import execute_provider_free_experiment


FIXTURE = Path("tests/fixtures/reasoning/blocking_calibration_v1.json")


class VisibleEvidenceFakeRuntime:
    """Provider-free runtime using only model-visible Specification 020 evidence."""

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
        requirements = project_evidence["available_requirements"]
        scopes = project_evidence["available_downstream_scopes"]
        variant = project_evidence["variant_project_evidence"]
        assert isinstance(requirements, list)
        assert isinstance(scopes, list)
        assert isinstance(variant, dict)

        unresolved_requirement = any(
            key.startswith("requirement.")
            and key.endswith(".status")
            and value == "UNRESOLVED"
            for key, value in variant.items()
        )
        explicit_dependency = any(
            key.startswith("scope.")
            and key.endswith(".depends_on")
            and value not in {"none", "none_additional"}
            for key, value in variant.items()
        )

        if unresolved_requirement and explicit_dependency:
            result = BlockingCalibrationResult(
                disposition="BLOCKING_REQUIRED",
                blocking_requirement_id=str(requirements[0]["requirement_id"]),
                blocked_scope_id=str(scopes[0]["scope_id"]),
                rationale="The supplied active defended scope explicitly depends on the supplied unresolved requirement, and the action is represented as resolving it.",
            )
        else:
            result = BlockingCalibrationResult(
                disposition="RECOMMENDED",
                blocking_requirement_id=None,
                blocked_scope_id=None,
                rationale="The action is worthwhile, but no supplied active defended scope is represented as blocked on it.",
            )

        return ReasoningOutcome(
            result=result,
            usage=ReasoningUsage(
                input_tokens=120,
                output_tokens=24,
                total_tokens=144,
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
        execute_provider_free_experiment(
            output_dir=tmp_path,
            benchmark_path=FIXTURE,
            runtime=runtime,
        )
    )

    assert result["complete_scored_design"] is True
    assert result["advancement_outcome"] == "BLOCKING_BOUNDARY_SUPPORTED"
    assert result["overall_frozen_gate_passed"] is True
    assert result["counts"]["successful_reasoner_outputs"] == 36
    assert result["provider_attempts"]["used"] == 36
    assert result["gate_evaluation"]["aggregate_exact_disposition_accuracy"] == 1.0
    assert result["gate_evaluation"]["expected_blocking_joint_pointer_accuracy"] == 1.0
    assert result["gate_evaluation"]["expected_recommended_null_pointer_correctness"] == 1.0

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
    serialized_attempts = json.dumps(attempts)
    assert "expected_disposition" not in serialized_attempts
    assert "expected_blocking_requirement_id" not in serialized_attempts
    assert "expected_blocked_scope_id" not in serialized_attempts


def test_runner_preserves_retry_attempt_without_changing_frozen_result(tmp_path: Path) -> None:
    runtime = VisibleEvidenceFakeRuntime(fail_first_request_once=True)
    result = asyncio.run(
        execute_provider_free_experiment(
            output_dir=tmp_path,
            benchmark_path=FIXTURE,
            runtime=runtime,
        )
    )

    assert result["advancement_outcome"] == "BLOCKING_BOUNDARY_SUPPORTED"
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
