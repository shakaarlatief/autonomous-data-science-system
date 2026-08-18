"""Read-only mechanical verification for Prototype V0 held-out attempts.

This module is evaluator-side infrastructure. It does not generate treatment
commands, call a model provider, mutate attempt artifacts, or perform semantic
judging. Its job is to turn the repeated manual post-run checks used during the
first held-out slots into a reproducible condition-neutral verifier.

Verification reports are written outside the append-only treatment attempt
folders. The verifier therefore observes a completed attempt without changing
the evidence that later semantic evaluation will consume.
"""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from .evaluator import evaluate_deterministic_behavior
from .heldout_execution import (
    DEFAULT_BUNDLE_ROOT,
    DEFAULT_FINGERPRINT_PATH,
    DEFAULT_PLAN_PATH,
    DEFAULT_PROTOCOL_PATH,
    FrozenBundleValidation,
    HeldOutSlot,
    attempt_id,
)
from .heldout_runner import (
    DEFAULT_ATTEMPTS_ROOT,
    load_and_validate_materialized_plan,
)
from .runtime import TraceEvent


DEFAULT_VERIFICATION_ROOT = Path("results/held_out/mechanical_verification")
VERIFICATION_SCHEMA_VERSION = "v0.1.0"
_REQUIRED_ARTIFACTS = (
    "attempt_started.json",
    "attempt_record.json",
    "summary.json",
    "deterministic_evaluation.json",
    "milestones.json",
    "conversation.json",
    "trace.jsonl",
)
_ATTEMPT_RE = re.compile(r"^(?P<slot>h[12]-r\d{2}-(?:b0|b1|p0))-a(?P<number>\d{2})$")


@dataclass(frozen=True)
class VerificationContext:
    """Frozen expectations for one concrete attempt identity."""

    attempt_id: str
    attempt_number: int
    slot: HeldOutSlot
    plan_sha256: str
    bundle_sha256: str
    bundle_dir: Path
    expected_registered_configuration: dict[str, Any]
    expected_run_config: dict[str, Any]


@dataclass(frozen=True)
class MechanicalCheck:
    """One verifier assertion about persisted experiment mechanics."""

    check_id: str
    name: str
    passed: bool
    details: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected JSON object in {path}.")
    return payload


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _artifact_hashes(attempt_dir: Path) -> dict[str, str]:
    return {
        name: _sha256_file(attempt_dir / name)
        for name in _REQUIRED_ARTIFACTS
        if (attempt_dir / name).is_file()
    }


def _read_trace(path: Path) -> list[TraceEvent]:
    events: list[TraceEvent] = []
    for line_number, raw_line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line.strip():
            continue
        payload = json.loads(raw_line)
        if not isinstance(payload, dict):
            raise ValueError(f"Trace line {line_number} is not a JSON object.")
        payload = dict(payload)
        payload["artifacts_requested"] = tuple(payload.get("artifacts_requested", ()))
        events.append(TraceEvent(**payload))
    return events


def _check(
    check_id: str,
    name: str,
    passed: bool,
    **details: Any,
) -> MechanicalCheck:
    return MechanicalCheck(
        check_id=check_id,
        name=name,
        passed=bool(passed),
        details=details,
    )


def _expected_classification(summary: Mapping[str, Any]) -> dict[str, Any]:
    behavior_evaluable = summary.get("behavior_evaluable")
    if not isinstance(behavior_evaluable, bool):
        raise ValueError("summary.json is missing boolean behavior_evaluable.")

    if behavior_evaluable:
        return {
            "classification": "BEHAVIOR_EVALUABLE",
            "behavior_evaluable": True,
            "replacement_eligible": False,
            "slot_resolved": True,
        }

    terminal_error = summary.get("terminal_generation_error")
    if not isinstance(terminal_error, str) or not terminal_error.strip():
        raise ValueError(
            "Non-behavior-evaluable summary is missing terminal_generation_error."
        )
    return {
        "classification": "NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE",
        "behavior_evaluable": False,
        "replacement_eligible": True,
        "slot_resolved": False,
    }


def _parse_attempt_id(value: str) -> tuple[str, int]:
    match = _ATTEMPT_RE.fullmatch(value.lower())
    if match is None:
        raise ValueError(f"Unrecognized held-out attempt id: {value}")
    return match.group("slot"), int(match.group("number"))


def resolve_verification_context(
    attempt_id_value: str,
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
) -> VerificationContext:
    """Resolve one attempt against the freshly revalidated frozen plan."""

    plan, slots, validations = load_and_validate_materialized_plan(
        plan_path=plan_path,
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    slot_id, attempt_number = _parse_attempt_id(attempt_id_value)
    matches = [slot for slot in slots if slot.slot_id == slot_id]
    if len(matches) != 1:
        raise ValueError(
            f"Attempt does not map to exactly one frozen slot: {attempt_id_value}"
        )
    slot = matches[0]
    canonical_id = attempt_id(slot, attempt_number)
    if canonical_id != attempt_id_value.lower():
        raise ValueError(
            f"Attempt identity is not canonical: expected {canonical_id}, "
            f"got {attempt_id_value}."
        )

    model = plan.get("treatment_model")
    if not isinstance(model, Mapping):
        raise ValueError("Frozen run plan is missing treatment_model.")

    registered = {
        "model": str(model["model"]),
        "reasoning_effort": str(model["reasoning_effort"]),
        "max_model_calls": int(model["max_successful_model_calls"]),
        "max_total_tokens": int(model["max_observed_total_tokens"]),
        "max_python_execution_attempts": int(model["max_python_execution_attempts"]),
        "max_generation_retries": int(model["max_additional_generation_retries"]),
        "max_output_tokens": int(model["max_output_tokens_per_call"]),
        "python_timeout_seconds": int(model["python_timeout_seconds"]),
        "provider_request_timeout_seconds": int(
            model["provider_request_timeout_seconds"]
        ),
    }
    run_config = {
        "provider": str(model["provider"]),
        "requested_model": str(model["model"]),
        "reasoning_effort": str(model["reasoning_effort"]),
        "max_model_calls": int(model["max_successful_model_calls"]),
        "max_total_tokens": int(model["max_observed_total_tokens"]),
        "max_python_execution_attempts": int(model["max_python_execution_attempts"]),
        "max_generation_retries": int(model["max_additional_generation_retries"]),
        "max_output_tokens_per_call": int(model["max_output_tokens_per_call"]),
    }
    validation: FrozenBundleValidation = validations[slot.variant]
    return VerificationContext(
        attempt_id=canonical_id,
        attempt_number=attempt_number,
        slot=slot,
        plan_sha256=_sha256_file(Path(plan_path)),
        bundle_sha256=validation.aggregate_sha256,
        bundle_dir=Path(bundle_root) / slot.variant,
        expected_registered_configuration=registered,
        expected_run_config=run_config,
    )


def verify_attempt_directory(
    attempt_dir: str | Path,
    *,
    context: VerificationContext,
    recompute_deterministic: bool = True,
) -> dict[str, Any]:
    """Verify one completed attempt directory without mutating it."""

    directory = Path(attempt_dir)
    checks: list[MechanicalCheck] = []
    missing = [
        name for name in _REQUIRED_ARTIFACTS if not (directory / name).is_file()
    ]
    checks.append(
        _check(
            "M01",
            "required_attempt_artifacts_present",
            not missing,
            missing=missing,
        )
    )
    if missing:
        return _report(
            context=context,
            attempt_dir=directory,
            checks=checks,
            mechanical_summary={},
            behavioral_observations={
                "review_flags": ["missing_required_artifacts"]
            },
        )

    started = _read_json(directory / "attempt_started.json")
    record = _read_json(directory / "attempt_record.json")
    summary = _read_json(directory / "summary.json")
    deterministic = _read_json(directory / "deterministic_evaluation.json")
    milestones = _read_json(directory / "milestones.json")
    conversation = _read_json(directory / "conversation.json")
    events = _read_trace(directory / "trace.jsonl")

    slot_payload = asdict(context.slot)
    identity_passed = (
        started.get("attempt_id") == context.attempt_id
        and int(started.get("attempt_number", -1)) == context.attempt_number
        and started.get("slot") == slot_payload
        and record.get("attempt_id") == context.attempt_id
        and int(record.get("attempt_number", -1)) == context.attempt_number
        and record.get("slot") == slot_payload
        and summary.get("run_id") == context.attempt_id
        and summary.get("condition") == context.slot.condition
        and directory.name == context.attempt_id
    )
    checks.append(
        _check(
            "M02",
            "attempt_identity_matches_frozen_slot",
            identity_passed,
            expected_attempt_id=context.attempt_id,
            expected_slot=slot_payload,
        )
    )

    provenance_passed = (
        started.get("plan_sha256") == context.plan_sha256
        and record.get("plan_sha256") == context.plan_sha256
        and started.get("bundle_sha256") == context.bundle_sha256
        and record.get("bundle_sha256") == context.bundle_sha256
    )
    checks.append(
        _check(
            "M03",
            "plan_and_bundle_provenance_match_frozen_inputs",
            provenance_passed,
            expected_plan_sha256=context.plan_sha256,
            expected_bundle_sha256=context.bundle_sha256,
            started_plan_sha256=started.get("plan_sha256"),
            record_plan_sha256=record.get("plan_sha256"),
            started_bundle_sha256=started.get("bundle_sha256"),
            record_bundle_sha256=record.get("bundle_sha256"),
        )
    )

    config_passed = (
        started.get("registered_configuration")
        == context.expected_registered_configuration
        and summary.get("run_config") == context.expected_run_config
    )
    checks.append(
        _check(
            "M04",
            "registered_runtime_configuration_matches_frozen_plan",
            config_passed,
            expected_registered_configuration=(
                context.expected_registered_configuration
            ),
            observed_registered_configuration=started.get(
                "registered_configuration"
            ),
            expected_run_config=context.expected_run_config,
            observed_run_config=summary.get("run_config"),
        )
    )

    try:
        expected_classification = _expected_classification(summary)
        classification_passed = (
            record.get("summary") == summary
            and all(
                record.get(key) == value
                for key, value in expected_classification.items()
            )
        )
    except ValueError as exc:
        expected_classification = {"error": str(exc)}
        classification_passed = False
    checks.append(
        _check(
            "M05",
            "summary_and_executor_classification_are_consistent",
            classification_passed,
            expected_classification=expected_classification,
            observed={
                key: record.get(key)
                for key in (
                    "classification",
                    "behavior_evaluable",
                    "replacement_eligible",
                    "slot_resolved",
                )
            },
        )
    )

    resource_fields = (
        "model_calls",
        "generation_attempts",
        "generation_failures",
        "input_tokens",
        "output_tokens",
        "total_tokens",
        "python_execution_attempts",
    )
    numeric_ok = all(
        isinstance(summary.get(key), int) and int(summary[key]) >= 0
        for key in resource_fields
    )
    max_calls = context.expected_registered_configuration["max_model_calls"]
    max_python = context.expected_registered_configuration[
        "max_python_execution_attempts"
    ]
    max_tokens = context.expected_registered_configuration["max_total_tokens"]
    resource_passed = numeric_ok
    if numeric_ok:
        resource_passed = (
            int(summary["input_tokens"]) + int(summary["output_tokens"])
            == int(summary["total_tokens"])
            and int(summary["generation_attempts"])
            == int(summary["model_calls"]) + int(summary["generation_failures"])
            and int(summary["model_calls"]) <= max_calls
            and int(summary["python_execution_attempts"]) <= max_python
            and (
                bool(summary.get("budget_exhausted"))
                or int(summary["total_tokens"]) <= max_tokens
            )
            and (
                not bool(summary.get("completed_within_budget"))
                or (
                    bool(summary.get("completed"))
                    and not bool(summary.get("budget_exhausted"))
                    and int(summary["total_tokens"]) <= max_tokens
                )
            )
            and (
                int(summary["total_tokens"]) <= max_tokens
                or bool(summary.get("budget_exhausted"))
            )
        )
    checks.append(
        _check(
            "M06",
            "resource_accounting_and_budget_flags_are_self_consistent",
            resource_passed,
            observed={key: summary.get(key) for key in resource_fields},
            completed=summary.get("completed"),
            completed_within_budget=summary.get("completed_within_budget"),
            budget_exhausted=summary.get("budget_exhausted"),
            limits={
                "max_model_calls": max_calls,
                "max_python_execution_attempts": max_python,
                "max_total_tokens": max_tokens,
            },
        )
    )

    sequences = [event.sequence for event in events]
    run_ids = {event.run_id for event in events}
    conditions = {event.condition for event in events}
    event_ids = [event.event_id for event in events]
    successful_generation_events = [
        event for event in events if event.event_type == "MODEL_GENERATION"
    ]
    failed_generation_events = [
        event for event in events if event.event_type == "MODEL_GENERATION_ERROR"
    ]
    python_events = [
        event for event in events if event.event_type == "EXECUTE_PYTHON"
    ]

    usage_events = successful_generation_events + failed_generation_events
    usage_input = sum(
        int(event.details.get("usage", {}).get("input_tokens", 0))
        for event in usage_events
    )
    usage_output = sum(
        int(event.details.get("usage", {}).get("output_tokens", 0))
        for event in usage_events
    )
    usage_total = sum(
        int(event.details.get("usage", {}).get("total_tokens", 0))
        for event in usage_events
    )

    trace_passed = (
        sequences == list(range(1, len(events) + 1))
        and len(set(event_ids)) == len(event_ids)
        and run_ids == {context.attempt_id}
        and conditions == {context.slot.condition}
        and len(successful_generation_events) == summary.get("model_calls")
        and len(failed_generation_events) == summary.get("generation_failures")
        and len(usage_events) == summary.get("generation_attempts")
        and len(python_events) == summary.get("python_execution_attempts")
        and usage_input == summary.get("input_tokens")
        and usage_output == summary.get("output_tokens")
        and usage_total == summary.get("total_tokens")
    )
    checks.append(
        _check(
            "M07",
            "trace_is_contiguous_and_reconciles_resource_counts",
            trace_passed,
            event_count=len(events),
            successful_generation_events=len(successful_generation_events),
            failed_generation_events=len(failed_generation_events),
            python_events=len(python_events),
            traced_usage={
                "input_tokens": usage_input,
                "output_tokens": usage_output,
                "total_tokens": usage_total,
            },
        )
    )

    deterministic_passed = True
    deterministic_error: str | None = None
    if recompute_deterministic:
        try:
            recomputed = evaluate_deterministic_behavior(
                bundle_dir=context.bundle_dir,
                events=events,
                phase_1_report=milestones.get("phase_1_report"),
                final_lock_report=milestones.get("final_lock_report"),
            )
            deterministic_passed = recomputed == deterministic
        except Exception as exc:
            deterministic_passed = False
            deterministic_error = f"{type(exc).__name__}: {exc}"

    behavior_evaluable = summary.get("behavior_evaluable") is True
    if behavior_evaluable:
        deterministic_passed = (
            deterministic_passed
            and summary.get("deterministic_passed_all")
            == deterministic.get("passed_all_deterministic")
            and summary.get("deterministic_passed_critical")
            == deterministic.get("passed_all_critical")
            and summary.get("critical_failures")
            == deterministic.get("critical_failures")
        )
    checks.append(
        _check(
            "M08",
            "persisted_deterministic_evaluation_recomputes_exactly",
            deterministic_passed,
            recomputation_error=deterministic_error,
            stored_passed_all=deterministic.get("passed_all_deterministic"),
            stored_passed_critical=deterministic.get("passed_all_critical"),
            stored_critical_failures=deterministic.get("critical_failures"),
        )
    )

    final_lock_events = [
        event for event in events if event.event_type == "FINAL_MODEL_LOCKED"
    ]
    final_eval_started = [
        event for event in events if event.event_type == "FINAL_EVALUATION_STARTED"
    ]
    final_report_events = [
        event for event in events if event.event_type == "FINAL_REPORT_SUBMITTED"
    ]
    completed = summary.get("completed") is True
    milestone_passed = (
        (not completed or milestones.get("final_report") is not None)
        and (not final_lock_events or milestones.get("final_lock_report") is not None)
        and (not final_report_events or milestones.get("final_report") is not None)
        and (not completed or len(final_report_events) == 1)
    )
    checks.append(
        _check(
            "M09",
            "milestone_artifacts_match_trace_completion_state",
            milestone_passed,
            completed=completed,
            phase_1_report_present=milestones.get("phase_1_report") is not None,
            final_lock_report_present=milestones.get("final_lock_report") is not None,
            final_report_present=milestones.get("final_report") is not None,
            final_lock_event_sequences=[
                event.sequence for event in final_lock_events
            ],
            final_evaluation_start_sequences=[
                event.sequence for event in final_eval_started
            ],
            final_report_event_sequences=[
                event.sequence for event in final_report_events
            ],
        )
    )

    protected_name: str | None = None
    final_test_accesses: list[TraceEvent] = []
    protected_sequence_passed = True
    protected_error: str | None = None
    try:
        manifest = _read_json(
            context.bundle_dir / "evaluator_only" / "manifest.json"
        )
        roles = manifest["world_truth"]["artifact_roles"]
        protected = [
            name
            for name, role in roles.items()
            if role == "protected_final_evaluation"
        ]
        if len(protected) != 1:
            raise ValueError(
                f"Expected one protected final artifact; got {protected}"
            )
        protected_name = protected[0]
        final_test_accesses = [
            event
            for event in events
            if event.allowed
            and event.access_level == "VALUE"
            and protected_name in event.artifacts_requested
        ]
        lock_sequences = [event.sequence for event in final_lock_events]
        first_lock = min(lock_sequences) if lock_sequences else None
        protected_sequence_passed = (
            len(final_test_accesses) <= 1
            and all(
                event.phase == "FINAL_EVALUATION"
                for event in final_test_accesses
            )
            and (
                not final_test_accesses
                or (
                    first_lock is not None
                    and first_lock < final_test_accesses[0].sequence
                )
            )
        )
    except Exception as exc:
        protected_sequence_passed = False
        protected_error = f"{type(exc).__name__}: {exc}"
    checks.append(
        _check(
            "M10",
            "protected_final_value_access_is_single_and_after_lock",
            protected_sequence_passed,
            protected_artifact=protected_name,
            access_sequences=[
                event.sequence for event in final_test_accesses
            ],
            recomputation_error=protected_error,
        )
    )

    messages = conversation.get("messages")
    conversation_passed = isinstance(messages, list) and all(
        isinstance(message, dict)
        and message.get("role") in {"system", "user", "assistant"}
        and isinstance(message.get("content"), str)
        for message in (messages or [])
    )
    if conversation_passed and isinstance(messages, list):
        assistant_messages = sum(
            message.get("role") == "assistant" for message in messages
        )
        conversation_passed = assistant_messages == summary.get("model_calls")
    else:
        assistant_messages = None
    checks.append(
        _check(
            "M11",
            "conversation_shape_matches_successful_model_calls",
            conversation_passed,
            assistant_messages=assistant_messages,
            model_calls=summary.get("model_calls"),
        )
    )

    python_failures = [
        {
            "sequence": event.sequence,
            "return_code": event.details.get("return_code"),
            "timed_out": event.details.get("timed_out"),
            "stderr_present": bool(
                str(event.details.get("stderr", "")).strip()
            ),
        }
        for event in python_events
        if event.details.get("return_code") != 0
        or bool(event.details.get("timed_out"))
    ]
    command_errors = [
        event.sequence
        for event in events
        if event.event_type == "TREATMENT_COMMAND_ERROR"
    ]
    generation_error_sequences = [
        event.sequence for event in failed_generation_events
    ]
    review_flags: list[str] = []
    if summary.get("budget_exhausted"):
        review_flags.append("budget_exhausted")
    if not summary.get("completed"):
        review_flags.append("incomplete_run")
    if python_failures:
        review_flags.append("python_execution_error_or_timeout")
    if command_errors:
        review_flags.append("treatment_command_error")
    if generation_error_sequences:
        review_flags.append("provider_generation_retry_or_failure")
    if behavior_evaluable and not deterministic.get(
        "passed_all_deterministic", False
    ):
        review_flags.append("deterministic_assertion_failure")

    final_features: list[str] = []
    final_lock_report = milestones.get("final_lock_report")
    if (
        isinstance(final_lock_report, dict)
        and isinstance(final_lock_report.get("selected_features"), list)
    ):
        final_features = [
            str(value) for value in final_lock_report["selected_features"]
        ]

    mechanical_summary = {
        "condition": summary.get("condition"),
        "behavior_evaluable": summary.get("behavior_evaluable"),
        "classification": record.get("classification"),
        "completed": summary.get("completed"),
        "completed_within_budget": summary.get("completed_within_budget"),
        "budget_exhausted": summary.get("budget_exhausted"),
        "project_phase": summary.get("project_phase"),
        "model_calls": summary.get("model_calls"),
        "generation_attempts": summary.get("generation_attempts"),
        "generation_failures": summary.get("generation_failures"),
        "python_execution_attempts": summary.get("python_execution_attempts"),
        "input_tokens": summary.get("input_tokens"),
        "output_tokens": summary.get("output_tokens"),
        "total_tokens": summary.get("total_tokens"),
        "deterministic_passed_all": deterministic.get(
            "passed_all_deterministic"
        ),
        "deterministic_passed_critical": deterministic.get(
            "passed_all_critical"
        ),
        "critical_failures": deterministic.get("critical_failures"),
        "final_selected_features": final_features,
        "phase_1_report_present": milestones.get("phase_1_report") is not None,
        "final_lock_report_present": (
            milestones.get("final_lock_report") is not None
        ),
        "final_report_present": milestones.get("final_report") is not None,
        "final_lock_sequence": min(
            (event.sequence for event in final_lock_events), default=None
        ),
        "final_evaluation_start_sequence": min(
            (event.sequence for event in final_eval_started), default=None
        ),
        "protected_test_access_sequences": [
            event.sequence for event in final_test_accesses
        ],
        "final_report_sequence": min(
            (event.sequence for event in final_report_events), default=None
        ),
        "python_failures": python_failures,
        "treatment_command_error_sequences": command_errors,
        "provider_generation_error_sequences": generation_error_sequences,
    }
    behavioral_observations = {"review_flags": review_flags}
    return _report(
        context=context,
        attempt_dir=directory,
        checks=checks,
        mechanical_summary=mechanical_summary,
        behavioral_observations=behavioral_observations,
    )


def _report(
    *,
    context: VerificationContext,
    attempt_dir: Path,
    checks: Sequence[MechanicalCheck],
    mechanical_summary: Mapping[str, Any],
    behavioral_observations: Mapping[str, Any],
) -> dict[str, Any]:
    failed = [check.check_id for check in checks if not check.passed]
    return {
        "schema_version": VERIFICATION_SCHEMA_VERSION,
        "verified_at_utc": _utc_now(),
        "attempt_id": context.attempt_id,
        "slot": asdict(context.slot),
        "attempt_number": context.attempt_number,
        "integrity_status": "PASS" if not failed else "FAIL",
        "auto_continue_safe": not failed,
        "failed_checks": failed,
        "checks": [check.to_dict() for check in checks],
        "mechanical_summary": dict(mechanical_summary),
        "behavioral_observations": dict(behavioral_observations),
        "source_artifact_sha256": _artifact_hashes(attempt_dir),
        "verifier_boundary": {
            "calls_model_provider": False,
            "mutates_attempt_artifacts": False,
            "performs_semantic_judging": False,
        },
    }


def verify_attempt(
    attempt_id_value: str,
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    verification_root: str | Path = DEFAULT_VERIFICATION_ROOT,
    write_report: bool = True,
) -> dict[str, Any]:
    """Resolve, verify, and optionally persist one attempt report."""

    context = resolve_verification_context(
        attempt_id_value,
        plan_path=plan_path,
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    attempt_dir = Path(attempts_root) / context.attempt_id
    if not attempt_dir.is_dir():
        raise FileNotFoundError(
            f"Attempt directory does not exist: {attempt_dir}"
        )
    report = verify_attempt_directory(attempt_dir, context=context)
    if write_report:
        root = Path(verification_root)
        root.mkdir(parents=True, exist_ok=True)
        target = root / f"{context.attempt_id}.json"
        target.write_text(
            json.dumps(report, indent=2, sort_keys=True), encoding="utf-8"
        )
    return report


def completed_attempt_ids(
    *,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
) -> list[str]:
    """Return attempt ids with persisted executor records, sorted by slot/attempt."""

    root = Path(attempts_root)
    if not root.is_dir():
        return []
    values: list[tuple[int, int, str]] = []
    for directory in root.iterdir():
        if (
            not directory.is_dir()
            or not (directory / "attempt_record.json").is_file()
        ):
            continue
        try:
            record = _read_json(directory / "attempt_record.json")
            slot = record["slot"]
            values.append(
                (
                    int(slot["slot_index"]),
                    int(record["attempt_number"]),
                    directory.name,
                )
            )
        except Exception:
            values.append((10**9, 10**9, directory.name))
    return [value[2] for value in sorted(values)]


def backfill_verification(
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    verification_root: str | Path = DEFAULT_VERIFICATION_ROOT,
) -> dict[str, Any]:
    """Verify every completed attempt with the same frozen verifier."""

    reports = [
        verify_attempt(
            value,
            plan_path=plan_path,
            protocol_path=protocol_path,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
            attempts_root=attempts_root,
            verification_root=verification_root,
            write_report=True,
        )
        for value in completed_attempt_ids(attempts_root=attempts_root)
    ]
    aggregate = {
        "schema_version": VERIFICATION_SCHEMA_VERSION,
        "generated_at_utc": _utc_now(),
        "attempts_verified": len(reports),
        "integrity_passed": sum(
            report["integrity_status"] == "PASS" for report in reports
        ),
        "integrity_failed": sum(
            report["integrity_status"] != "PASS" for report in reports
        ),
        "reports": [
            {
                "attempt_id": report["attempt_id"],
                "integrity_status": report["integrity_status"],
                "auto_continue_safe": report["auto_continue_safe"],
                "review_flags": report["behavioral_observations"].get(
                    "review_flags", []
                ),
                "mechanical_summary": report["mechanical_summary"],
            }
            for report in reports
        ],
    }
    root = Path(verification_root)
    root.mkdir(parents=True, exist_ok=True)
    (root / "index.json").write_text(
        json.dumps(aggregate, indent=2, sort_keys=True), encoding="utf-8"
    )
    return aggregate
