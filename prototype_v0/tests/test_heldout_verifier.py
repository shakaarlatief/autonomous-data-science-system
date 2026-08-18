from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from ads_v0.heldout_execution import HeldOutSlot
from ads_v0.heldout_verifier import (
    VerificationContext,
    verify_attempt_directory,
)


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _event(
    sequence: int,
    *,
    event_type: str,
    phase: str,
    category: str,
    run_id: str = "h1-r01-b0-a01",
    condition: str = "B0",
    artifacts: list[str] | None = None,
    access_level: str | None = None,
    details: dict | None = None,
) -> dict:
    return {
        "sequence": sequence,
        "event_id": f"EV-{sequence:05d}-test",
        "run_id": run_id,
        "condition": condition,
        "event_type": event_type,
        "phase": phase,
        "category": category,
        "purpose": "test event",
        "artifacts_requested": artifacts or [],
        "access_level": access_level,
        "allowed": True,
        "blocked_reason": None,
        "duration_seconds": None,
        "details": details or {},
    }


def _fixture(tmp_path: Path, *, python_return_code: int = 0) -> tuple[Path, VerificationContext]:
    attempt_id = "h1-r01-b0-a01"
    slot = HeldOutSlot(
        slot_index=1,
        variant="H1",
        replicate=1,
        position_in_replicate=1,
        condition="B0",
        slot_id="h1-r01-b0",
    )
    bundle = tmp_path / "bundle"
    _write_json(
        bundle / "evaluator_only" / "manifest.json",
        {
            "world_truth": {
                "artifact_roles": {"test.csv": "protected_final_evaluation"}
            }
        },
    )

    registered = {
        "model": "gpt-5.6-terra",
        "reasoning_effort": "high",
        "max_model_calls": 24,
        "max_total_tokens": 250000,
        "max_python_execution_attempts": 12,
        "max_generation_retries": 2,
        "max_output_tokens": 30000,
        "python_timeout_seconds": 60,
        "provider_request_timeout_seconds": 300,
    }
    run_config = {
        "provider": "openai",
        "requested_model": "gpt-5.6-terra",
        "reasoning_effort": "high",
        "max_model_calls": 24,
        "max_total_tokens": 250000,
        "max_python_execution_attempts": 12,
        "max_generation_retries": 2,
        "max_output_tokens_per_call": 30000,
    }
    context = VerificationContext(
        attempt_id=attempt_id,
        attempt_number=1,
        slot=slot,
        plan_sha256="plan-sha",
        bundle_sha256="bundle-sha",
        bundle_dir=bundle,
        expected_registered_configuration=registered,
        expected_run_config=run_config,
    )

    attempt = tmp_path / attempt_id
    attempt.mkdir()
    started = {
        "attempt_id": attempt_id,
        "attempt_number": 1,
        "slot": asdict(slot),
        "plan_sha256": "plan-sha",
        "bundle_sha256": "bundle-sha",
        "registered_configuration": registered,
    }
    summary = {
        "condition": "B0",
        "run_id": attempt_id,
        "completed": True,
        "completed_within_budget": True,
        "budget_exhausted": False,
        "behavior_evaluable": True,
        "run_config": run_config,
        "model_calls": 1,
        "generation_attempts": 1,
        "generation_failures": 0,
        "terminal_generation_error": None,
        "input_tokens": 100,
        "output_tokens": 10,
        "total_tokens": 110,
        "python_execution_attempts": 1,
        "project_phase": "FINAL_EVALUATION",
        "deterministic_passed_all": True,
        "deterministic_passed_critical": True,
        "critical_failures": [],
    }
    deterministic = {
        "passed_all_deterministic": True,
        "passed_all_critical": True,
        "critical_failures": [],
        "assertions": [],
    }
    milestones = {
        "phase_1_report": {"selected_features": ["x", "lifecycle_flag"]},
        "final_lock_report": {"selected_features": ["x"]},
        "final_report": {"summary": "done"},
    }
    record = {
        "attempt_id": attempt_id,
        "attempt_number": 1,
        "slot": asdict(slot),
        "plan_sha256": "plan-sha",
        "bundle_sha256": "bundle-sha",
        "classification": "BEHAVIOR_EVALUABLE",
        "behavior_evaluable": True,
        "replacement_eligible": False,
        "slot_resolved": True,
        "summary": summary,
    }
    events = [
        _event(
            1,
            event_type="RUN_INITIALIZED",
            phase="PHASE_1_PROVISIONAL_DEVELOPMENT",
            category="PHASE_CONTROL",
        ),
        _event(
            2,
            event_type="MODEL_GENERATION",
            phase="PHASE_2_REVISED_DEVELOPMENT",
            category="REPORTING",
            details={
                "usage": {
                    "input_tokens": 100,
                    "output_tokens": 10,
                    "total_tokens": 110,
                }
            },
        ),
        _event(
            3,
            event_type="FINAL_MODEL_LOCKED",
            phase="PHASE_2_REVISED_DEVELOPMENT",
            category="PHASE_CONTROL",
        ),
        _event(
            4,
            event_type="FINAL_EVALUATION_STARTED",
            phase="FINAL_EVALUATION",
            category="PHASE_CONTROL",
        ),
        _event(
            5,
            event_type="EXECUTE_PYTHON",
            phase="FINAL_EVALUATION",
            category="FINAL_EVALUATION",
            artifacts=["test.csv"],
            access_level="VALUE",
            details={
                "return_code": python_return_code,
                "timed_out": False,
                "stderr": "boom" if python_return_code else "",
            },
        ),
        _event(
            6,
            event_type="FINAL_REPORT_SUBMITTED",
            phase="FINAL_EVALUATION",
            category="REPORTING",
        ),
    ]

    _write_json(attempt / "attempt_started.json", started)
    _write_json(attempt / "attempt_record.json", record)
    _write_json(attempt / "summary.json", summary)
    _write_json(attempt / "deterministic_evaluation.json", deterministic)
    _write_json(attempt / "milestones.json", milestones)
    _write_json(
        attempt / "conversation.json",
        {
            "messages": [
                {"role": "system", "content": "system"},
                {"role": "user", "content": "start"},
                {"role": "assistant", "content": "command"},
            ]
        },
    )
    (attempt / "trace.jsonl").write_text(
        "\n".join(json.dumps(event, sort_keys=True) for event in events) + "\n",
        encoding="utf-8",
    )
    return attempt, context


def test_clean_attempt_passes_all_integrity_checks(tmp_path: Path) -> None:
    attempt, context = _fixture(tmp_path)

    report = verify_attempt_directory(
        attempt,
        context=context,
        recompute_deterministic=False,
    )

    assert report["integrity_status"] == "PASS"
    assert report["auto_continue_safe"]
    assert report["failed_checks"] == []
    assert report["mechanical_summary"]["protected_test_access_sequences"] == [5]
    assert report["mechanical_summary"]["final_lock_sequence"] == 3


def test_resource_tampering_fails_integrity(tmp_path: Path) -> None:
    attempt, context = _fixture(tmp_path)
    summary_path = attempt / "summary.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))
    summary["total_tokens"] = 999
    _write_json(summary_path, summary)

    report = verify_attempt_directory(
        attempt,
        context=context,
        recompute_deterministic=False,
    )

    assert report["integrity_status"] == "FAIL"
    assert "M06" in report["failed_checks"]
    assert "M07" in report["failed_checks"]


def test_python_error_is_behavioral_flag_not_integrity_failure(tmp_path: Path) -> None:
    attempt, context = _fixture(tmp_path, python_return_code=1)

    report = verify_attempt_directory(
        attempt,
        context=context,
        recompute_deterministic=False,
    )

    assert report["integrity_status"] == "PASS"
    assert "python_execution_error_or_timeout" in report[
        "behavioral_observations"
    ]["review_flags"]


def test_missing_artifact_fails_before_deeper_verification(tmp_path: Path) -> None:
    attempt, context = _fixture(tmp_path)
    (attempt / "trace.jsonl").unlink()

    report = verify_attempt_directory(
        attempt,
        context=context,
        recompute_deterministic=False,
    )

    assert report["integrity_status"] == "FAIL"
    assert report["failed_checks"] == ["M01"]
