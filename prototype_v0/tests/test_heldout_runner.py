from __future__ import annotations

import json
from pathlib import Path

import pytest

from ads_v0.heldout_execution import validate_and_write_plan
from ads_v0.heldout_runner import (
    AttemptExecutionContext,
    determine_next_status,
    execute_next_attempt,
    load_and_validate_materialized_plan,
    status_document,
)
from ads_v0.prepare_heldout import fingerprint_bundle, load_protocol


PROTOTYPE_ROOT = Path(__file__).resolve().parents[1]
PROTOCOL_PATH = PROTOTYPE_ROOT / "configs" / "held_out_protocol_v0_1.json"


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def _execution_fixture(tmp_path: Path) -> tuple[Path, Path, Path, Path]:
    protocol = load_protocol(PROTOCOL_PATH)
    bundle_root = tmp_path / "held_out"
    frozen_bundles: dict[str, dict] = {}

    for variant, spec in protocol["held_out_cases"].items():
        bundle = bundle_root / variant
        _write_json(
            bundle / "evaluator_only" / "manifest.json",
            {
                "case_id": spec["case_id"],
                "surface_variant": spec["surface_variant"],
                "data_seed": spec["seed_start"],
            },
        )
        _write_json(
            bundle / "evaluator_only" / "self_test_report.json",
            {"passed": True, "checks": []},
        )
        visible = bundle / "visible" / "project_brief.md"
        visible.parent.mkdir(parents=True, exist_ok=True)
        visible.write_text(f"frozen {variant}\n", encoding="utf-8")

        fingerprint = fingerprint_bundle(bundle)
        frozen_bundles[variant] = {
            "case_id": spec["case_id"],
            "selected_seed": spec["seed_start"],
            "seed_start": spec["seed_start"],
            "first_candidate_passed": True,
            "file_count": fingerprint["file_count"],
            "aggregate_sha256": fingerprint["aggregate_sha256"],
        }

    fingerprint_path = tmp_path / "fingerprints.json"
    _write_json(
        fingerprint_path,
        {
            "protocol_version": protocol["protocol_version"],
            "bundles": frozen_bundles,
        },
    )

    plan_path = tmp_path / "run_plan.json"
    validate_and_write_plan(
        protocol_path=PROTOCOL_PATH,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        output_path=plan_path,
    )
    attempts_root = tmp_path / "attempts"
    return bundle_root, fingerprint_path, plan_path, attempts_root


def _fake_runner(*, behavior_evaluable: bool, completed: bool = True):
    calls: list[AttemptExecutionContext] = []

    def run(context: AttemptExecutionContext) -> None:
        calls.append(context)
        _write_json(
            context.output_dir / "summary.json",
            {
                "condition": context.slot.condition,
                "run_id": context.attempt_id,
                "completed": completed,
                "completed_within_budget": completed,
                "budget_exhausted": False,
                "behavior_evaluable": behavior_evaluable,
                "terminal_generation_error": (
                    None
                    if behavior_evaluable
                    else "ModelGenerationError: simulated provider failure"
                ),
                "model_calls": 1,
                "generation_attempts": 1,
                "generation_failures": 0 if behavior_evaluable else 1,
                "input_tokens": 100,
                "output_tokens": 10,
                "total_tokens": 110,
                "python_execution_attempts": 0,
            },
        )

    return run, calls


def _execute(
    *,
    plan_path: Path,
    fingerprint_path: Path,
    bundle_root: Path,
    attempts_root: Path,
    runner,
):
    return execute_next_attempt(
        plan_path=plan_path,
        protocol_path=PROTOCOL_PATH,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        attempt_runner=runner,
    )


def _status(
    *,
    plan_path: Path,
    fingerprint_path: Path,
    bundle_root: Path,
    attempts_root: Path,
):
    return status_document(
        plan_path=plan_path,
        protocol_path=PROTOCOL_PATH,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
    )


def test_status_starts_at_exact_first_preregistered_slot(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)

    status = _status(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
    )

    assert status["status"] == "READY_INITIAL"
    assert status["next_attempt_id"] == "h1-r01-b0-a01"
    assert status["next_slot"]["slot_index"] == 1
    assert status["next_slot"]["condition"] == "B0"
    assert status["resolved_slots"] == 0
    assert not status["launched_model_attempt"]


def test_behavior_evaluable_attempt_resolves_slot_without_replacement(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    runner, calls = _fake_runner(behavior_evaluable=True)

    result = _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=runner,
    )

    assert result["action"] == "ATTEMPT_COMPLETED"
    assert result["launched_model_attempt"]
    assert result["attempt_record"]["attempt_id"] == "h1-r01-b0-a01"
    assert result["attempt_record"]["slot_resolved"]
    assert not result["attempt_record"]["replacement_eligible"]
    assert len(calls) == 1

    status = _status(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
    )
    assert status["next_attempt_id"] == "h1-r01-b1-a01"
    assert status["resolved_slots"] == 1


def test_provider_failure_replacement_stays_inside_same_slot(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    failing_runner, _ = _fake_runner(behavior_evaluable=False, completed=False)

    first = _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=failing_runner,
    )
    assert first["attempt_record"]["replacement_eligible"]

    status = _status(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
    )
    assert status["status"] == "READY_REPLACEMENT"
    assert status["next_attempt_id"] == "h1-r01-b0-a02"
    assert status["next_slot"]["slot_id"] == "h1-r01-b0"


def test_three_non_behavior_evaluable_attempts_pause_execution(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    failing_runner, calls = _fake_runner(behavior_evaluable=False, completed=False)

    for _ in range(3):
        result = _execute(
            plan_path=plan_path,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
            attempts_root=attempts_root,
            runner=failing_runner,
        )
        assert result["action"] == "ATTEMPT_COMPLETED"

    status = _status(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
    )
    assert status["status"] == "REPLACEMENTS_EXHAUSTED"
    assert status["next_attempt_id"] == "h1-r01-b0-a03"
    assert len(calls) == 3

    no_launch = _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=failing_runner,
    )
    assert no_launch["action"] == "REPLACEMENTS_EXHAUSTED"
    assert not no_launch["launched_model_attempt"]
    assert len(calls) == 3


def test_interrupted_attempt_marker_blocks_duplicate_paid_execution(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    attempt_dir = attempts_root / "h1-r01-b0-a01"
    _write_json(
        attempt_dir / "attempt_started.json",
        {
            "attempt_id": "h1-r01-b0-a01",
            "attempt_number": 1,
        },
    )
    runner, calls = _fake_runner(behavior_evaluable=True)

    result = _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=runner,
    )

    assert result["action"] == "INTERRUPTED_ATTEMPT"
    assert not result["launched_model_attempt"]
    assert calls == []


def test_existing_summary_is_reconciled_without_new_model_attempt(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    attempt_dir = attempts_root / "h1-r01-b0-a01"
    _write_json(
        attempt_dir / "attempt_started.json",
        {"attempt_id": "h1-r01-b0-a01", "attempt_number": 1},
    )
    _write_json(
        attempt_dir / "summary.json",
        {
            "condition": "B0",
            "run_id": "h1-r01-b0-a01",
            "behavior_evaluable": True,
            "terminal_generation_error": None,
            "completed": False,
            "budget_exhausted": True,
        },
    )
    runner, calls = _fake_runner(behavior_evaluable=True)

    result = _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=runner,
    )

    assert result["action"] == "RECONCILED_EXISTING_SUMMARY"
    assert not result["launched_model_attempt"]
    assert result["attempt_record"]["slot_resolved"]
    assert result["attempt_record"]["reconciled_from_existing_summary"]
    assert calls == []
    assert (attempt_dir / "attempt_record.json").is_file()


def test_executor_revalidates_plan_and_passes_registered_limits(tmp_path: Path) -> None:
    bundle_root, fingerprint_path, plan_path, attempts_root = _execution_fixture(tmp_path)
    runner, calls = _fake_runner(behavior_evaluable=True)

    _execute(
        plan_path=plan_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
        attempts_root=attempts_root,
        runner=runner,
    )

    context = calls[0]
    assert context.model_name == "gpt-5.6-terra"
    assert context.reasoning_effort == "high"
    assert context.max_model_calls == 24
    assert context.max_total_tokens == 250000
    assert context.max_python_execution_attempts == 12
    assert context.max_generation_retries == 2
    assert context.max_output_tokens == 30000
    assert context.python_timeout_seconds == 60
    assert context.provider_request_timeout_seconds == 300

    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    plan["slots"][0]["condition"] = "P0"
    _write_json(plan_path, plan)

    with pytest.raises(ValueError, match="does not exactly match"):
        load_and_validate_materialized_plan(
            plan_path=plan_path,
            protocol_path=PROTOCOL_PATH,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
        )
