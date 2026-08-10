"""Resumable one-attempt-at-a-time executor for Prototype V0 held-out runs.

This module is intentionally conservative because a held-out treatment attempt is
paid, confirmatory evidence and must not be silently duplicated, reordered, or
replaced for behavioral reasons.

The executor therefore treats the materialized run plan and attempt directories
as an append-only local execution ledger. Every invocation revalidates the
frozen H1/H2 bundle identities and checks that ``run_plan.json`` is exactly the
plan implied by the preregistered protocol plus those bundle identities.

Only the earliest unresolved slot may advance. A single explicit ``run-next``
invocation can launch at most one treatment attempt. Before provider inference
begins, the executor creates an attempt directory and writes
``attempt_started.json``. If the process later terminates ambiguously before a
valid summary is available, a future invocation pauses instead of making a
second paid call under the same attempt identity.

Replacement attempts follow Foundation 012 exactly:

* a terminal provider/infrastructure generation failure after the registered
  retries is non-behavior-evaluable and may receive a replacement attempt;
* behavioral outcomes such as poor methodology, deterministic failure, Python
  error/timeout, incomplete work, or treatment resource exhaustion resolve the
  slot and are never replaced;
* at most two replacements are allowed after the initial attempt.

The module contains no semantic judging logic. Treatment execution must be
frozen and complete before the blinded judge is run.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Mapping

from .calibrate import run_openai_baseline
from .calibrate_p0 import run_openai_p0
from .heldout_execution import (
    DEFAULT_BUNDLE_ROOT,
    DEFAULT_FINGERPRINT_PATH,
    DEFAULT_PLAN_PATH,
    DEFAULT_PROTOCOL_PATH,
    FrozenBundleValidation,
    HeldOutSlot,
    attempt_id,
    build_plan_document,
    materialize_run_plan,
    validate_frozen_bundles,
)
from .prepare_heldout import load_protocol


DEFAULT_ATTEMPTS_ROOT = Path("results/held_out/attempts")
_ATTEMPT_STARTED_FILE = "attempt_started.json"
_ATTEMPT_RECORD_FILE = "attempt_record.json"
_SUMMARY_FILE = "summary.json"
_MAX_TOTAL_ATTEMPTS_PER_SLOT = 3

_STATUS_READY_INITIAL = "READY_INITIAL"
_STATUS_READY_REPLACEMENT = "READY_REPLACEMENT"
_STATUS_INTERRUPTED = "INTERRUPTED_ATTEMPT"
_STATUS_REPLACEMENTS_EXHAUSTED = "REPLACEMENTS_EXHAUSTED"
_STATUS_COMPLETE = "EXPERIMENT_COMPLETE"


@dataclass(frozen=True)
class NextAttemptStatus:
    """Current deterministic held-out execution position."""

    status: str
    slot: HeldOutSlot | None
    attempt_number: int | None
    attempt_id: str | None
    message: str


@dataclass(frozen=True)
class AttemptExecutionContext:
    """Frozen configuration supplied to exactly one treatment attempt."""

    slot: HeldOutSlot
    attempt_number: int
    attempt_id: str
    bundle_dir: Path
    output_dir: Path
    model_name: str
    reasoning_effort: str
    max_model_calls: int
    max_total_tokens: int
    max_python_execution_attempts: int
    max_generation_retries: int
    max_output_tokens: int
    python_timeout_seconds: int
    provider_request_timeout_seconds: int


AttemptRunner = Callable[[AttemptExecutionContext], None]


def _read_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Expected a JSON object in {path}.")
    return payload


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(
        json.dumps(dict(payload), indent=2, sort_keys=True, default=str),
        encoding="utf-8",
    )


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _slot_from_payload(payload: Mapping[str, Any]) -> HeldOutSlot:
    return HeldOutSlot(
        slot_index=int(payload["slot_index"]),
        variant=str(payload["variant"]),
        replicate=int(payload["replicate"]),
        position_in_replicate=int(payload["position_in_replicate"]),
        condition=str(payload["condition"]),
        slot_id=str(payload["slot_id"]),
    )


def load_and_validate_materialized_plan(
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
) -> tuple[dict[str, Any], tuple[HeldOutSlot, ...], dict[str, FrozenBundleValidation]]:
    """Revalidate frozen inputs and require exact agreement with run_plan.json.

    The plan is not trusted merely because it exists. Every invocation derives
    the expected plan again from the preregistered protocol and freshly verified
    local bundle identities, then requires structural equality with the
    materialized plan. This catches plan edits, bundle drift, and configuration
    drift before any paid treatment call can begin.
    """

    path = Path(plan_path)
    if not path.is_file():
        raise FileNotFoundError(
            f"Held-out run plan does not exist: {path}. Materialize it first."
        )

    protocol = load_protocol(protocol_path)
    validations = validate_frozen_bundles(
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    expected = build_plan_document(protocol=protocol, validations=validations)
    actual = _read_json(path)
    if actual != expected:
        raise ValueError(
            "Materialized held-out run plan does not exactly match the current "
            "frozen protocol and verified bundle identities. Refusing execution."
        )

    slots = materialize_run_plan(protocol)
    return actual, slots, validations


def _attempt_output_dir(attempts_root: Path, slot: HeldOutSlot, number: int) -> Path:
    return attempts_root / attempt_id(slot, number)


def _validate_summary_identity(
    *,
    summary: Mapping[str, Any],
    slot: HeldOutSlot,
    expected_attempt_id: str,
) -> None:
    if str(summary.get("run_id")) != expected_attempt_id:
        raise ValueError(
            f"Attempt summary run_id does not match directory identity: {expected_attempt_id}."
        )
    if str(summary.get("condition")) != slot.condition:
        raise ValueError(
            f"Attempt summary condition does not match slot {slot.slot_id}."
        )
    if not isinstance(summary.get("behavior_evaluable"), bool):
        raise ValueError("Attempt summary is missing boolean behavior_evaluable.")


def _classification_from_summary(summary: Mapping[str, Any]) -> dict[str, Any]:
    behavior_evaluable = bool(summary["behavior_evaluable"])
    terminal_error = summary.get("terminal_generation_error")

    if behavior_evaluable:
        return {
            "behavior_evaluable": True,
            "replacement_eligible": False,
            "slot_resolved": True,
            "classification": "BEHAVIOR_EVALUABLE",
            "reason": (
                "Behavior-evaluable treatment outcome. Behavioral failures, "
                "including budget exhaustion or incomplete work, are not replaced."
            ),
        }

    if not isinstance(terminal_error, str) or not terminal_error.strip():
        raise ValueError(
            "A non-behavior-evaluable attempt must record a terminal generation error."
        )

    return {
        "behavior_evaluable": False,
        "replacement_eligible": True,
        "slot_resolved": False,
        "classification": "NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE",
        "reason": (
            "Terminal provider/infrastructure generation failure after the common "
            "retry policy; replacement is allowed inside the same slot."
        ),
    }


def _attempt_state(
    *,
    attempts_root: Path,
    slot: HeldOutSlot,
    number: int,
) -> tuple[str, dict[str, Any] | None]:
    """Return ABSENT, COMPLETE, or INTERRUPTED for one attempt identity."""

    output_dir = _attempt_output_dir(attempts_root, slot, number)
    if not output_dir.exists():
        return "ABSENT", None
    if not output_dir.is_dir():
        raise ValueError(f"Attempt path is not a directory: {output_dir}")

    expected_id = attempt_id(slot, number)
    started_path = output_dir / _ATTEMPT_STARTED_FILE
    summary_path = output_dir / _SUMMARY_FILE
    record_path = output_dir / _ATTEMPT_RECORD_FILE

    if record_path.is_file():
        record = _read_json(record_path)
        if str(record.get("attempt_id")) != expected_id:
            raise ValueError(f"Attempt record identity mismatch in {record_path}.")
        if not summary_path.is_file():
            raise ValueError(f"Attempt record exists without summary: {record_path}.")
        summary = _read_json(summary_path)
        _validate_summary_identity(
            summary=summary,
            slot=slot,
            expected_attempt_id=expected_id,
        )
        expected_classification = _classification_from_summary(summary)
        for key in (
            "behavior_evaluable",
            "replacement_eligible",
            "slot_resolved",
            "classification",
        ):
            if record.get(key) != expected_classification[key]:
                raise ValueError(
                    f"Attempt record classification disagrees with summary in {record_path}."
                )
        return "COMPLETE", record

    if summary_path.is_file():
        summary = _read_json(summary_path)
        _validate_summary_identity(
            summary=summary,
            slot=slot,
            expected_attempt_id=expected_id,
        )
        classification = _classification_from_summary(summary)
        return "SUMMARY_WITHOUT_RECORD", {
            "summary": summary,
            "classification": classification,
        }

    if started_path.is_file():
        started = _read_json(started_path)
        if str(started.get("attempt_id")) != expected_id:
            raise ValueError(f"Attempt-start identity mismatch in {started_path}.")
        return "INTERRUPTED", started

    raise ValueError(
        f"Attempt directory exists without {_ATTEMPT_STARTED_FILE}, {_SUMMARY_FILE}, "
        f"or {_ATTEMPT_RECORD_FILE}: {output_dir}"
    )


def _reconstruct_record_from_summary(
    *,
    attempts_root: Path,
    slot: HeldOutSlot,
    number: int,
    plan_sha256: str,
    payload: Mapping[str, Any],
) -> dict[str, Any]:
    """Recover bookkeeping after a crash that occurred after summary persistence.

    This operation performs no model call. It exists specifically to prevent a
    successfully persisted paid attempt from being duplicated merely because the
    executor process stopped before writing its final bookkeeping record.
    """

    output_dir = _attempt_output_dir(attempts_root, slot, number)
    summary = dict(payload["summary"])
    classification = dict(payload["classification"])
    record = {
        "attempt_id": attempt_id(slot, number),
        "attempt_number": number,
        "slot": asdict(slot),
        "plan_sha256": plan_sha256,
        "reconciled_from_existing_summary": True,
        "recorded_at_utc": _utc_now(),
        **classification,
        "summary": summary,
    }
    _write_json(output_dir / _ATTEMPT_RECORD_FILE, record)
    return record


def determine_next_status(
    *,
    slots: tuple[HeldOutSlot, ...],
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
) -> NextAttemptStatus:
    """Select the earliest unresolved slot without performing inference."""

    root = Path(attempts_root)

    for slot in slots:
        for number in range(1, _MAX_TOTAL_ATTEMPTS_PER_SLOT + 1):
            state, payload = _attempt_state(
                attempts_root=root,
                slot=slot,
                number=number,
            )

            if state == "ABSENT":
                if number == 1:
                    return NextAttemptStatus(
                        status=_STATUS_READY_INITIAL,
                        slot=slot,
                        attempt_number=1,
                        attempt_id=attempt_id(slot, 1),
                        message=f"Initial attempt is ready for earliest unresolved slot {slot.slot_id}.",
                    )

                previous_state, previous = _attempt_state(
                    attempts_root=root,
                    slot=slot,
                    number=number - 1,
                )
                if previous_state != "COMPLETE" or previous is None:
                    raise ValueError(
                        f"Attempt sequence for {slot.slot_id} is internally inconsistent."
                    )
                if not bool(previous["replacement_eligible"]):
                    raise ValueError(
                        f"Later attempt missing after a resolved slot state for {slot.slot_id}."
                    )
                return NextAttemptStatus(
                    status=_STATUS_READY_REPLACEMENT,
                    slot=slot,
                    attempt_number=number,
                    attempt_id=attempt_id(slot, number),
                    message=(
                        f"Replacement attempt {number} is ready inside unresolved slot "
                        f"{slot.slot_id}."
                    ),
                )

            if state == "INTERRUPTED":
                return NextAttemptStatus(
                    status=_STATUS_INTERRUPTED,
                    slot=slot,
                    attempt_number=number,
                    attempt_id=attempt_id(slot, number),
                    message=(
                        "An attempt-start marker exists without a valid persisted summary. "
                        "Refusing to duplicate the potentially paid attempt."
                    ),
                )

            if state == "SUMMARY_WITHOUT_RECORD":
                return NextAttemptStatus(
                    status="SUMMARY_RECONCILIATION_REQUIRED",
                    slot=slot,
                    attempt_number=number,
                    attempt_id=attempt_id(slot, number),
                    message=(
                        "A valid treatment summary exists without the executor record. "
                        "Reconcile bookkeeping before launching another attempt."
                    ),
                )

            if state != "COMPLETE" or payload is None:
                raise AssertionError(f"Unhandled attempt state: {state}")

            if bool(payload["slot_resolved"]):
                break

            if not bool(payload["replacement_eligible"]):
                raise ValueError(
                    f"Unresolved attempt is not replacement eligible for {slot.slot_id}."
                )

            if number == _MAX_TOTAL_ATTEMPTS_PER_SLOT:
                return NextAttemptStatus(
                    status=_STATUS_REPLACEMENTS_EXHAUSTED,
                    slot=slot,
                    attempt_number=number,
                    attempt_id=attempt_id(slot, number),
                    message=(
                        f"All three attempts for {slot.slot_id} ended non-behavior-evaluable. "
                        "Held-out execution must pause for investigation."
                    ),
                )
        else:
            raise AssertionError("Unreachable attempt-loop state.")

    return NextAttemptStatus(
        status=_STATUS_COMPLETE,
        slot=None,
        attempt_number=None,
        attempt_id=None,
        message="All 30 preregistered held-out slots are resolved.",
    )


def _execution_context(
    *,
    plan: Mapping[str, Any],
    slot: HeldOutSlot,
    attempt_number: int,
    bundle_root: Path,
    attempts_root: Path,
) -> AttemptExecutionContext:
    model = plan.get("treatment_model")
    if not isinstance(model, Mapping):
        raise ValueError("Materialized run plan is missing treatment_model.")

    if str(model.get("provider")) != "openai":
        raise ValueError("Prototype V0 held-out executor supports only registered OpenAI provider.")

    python_timeout = int(model["python_timeout_seconds"])
    provider_timeout = int(model["provider_request_timeout_seconds"])
    if python_timeout != 60 or provider_timeout != 300:
        raise ValueError(
            "Registered timeout configuration differs from the frozen Version 0 runtime."
        )

    current_attempt_id = attempt_id(slot, attempt_number)
    return AttemptExecutionContext(
        slot=slot,
        attempt_number=attempt_number,
        attempt_id=current_attempt_id,
        bundle_dir=bundle_root / slot.variant,
        output_dir=attempts_root / current_attempt_id,
        model_name=str(model["model"]),
        reasoning_effort=str(model["reasoning_effort"]),
        max_model_calls=int(model["max_successful_model_calls"]),
        max_total_tokens=int(model["max_observed_total_tokens"]),
        max_python_execution_attempts=int(model["max_python_execution_attempts"]),
        max_generation_retries=int(model["max_additional_generation_retries"]),
        max_output_tokens=int(model["max_output_tokens_per_call"]),
        python_timeout_seconds=python_timeout,
        provider_request_timeout_seconds=provider_timeout,
    )


def _production_attempt_runner(context: AttemptExecutionContext) -> None:
    """Dispatch one frozen held-out attempt to the appropriate treatment runner."""

    if context.slot.condition in {"B0", "B1"}:
        run_openai_baseline(
            bundle_dir=context.bundle_dir,
            condition=context.slot.condition,
            run_id=context.attempt_id,
            output_dir=context.output_dir,
            model_name=context.model_name,
            reasoning_effort=context.reasoning_effort,
            max_model_calls=context.max_model_calls,
            max_total_tokens=context.max_total_tokens,
            max_python_execution_attempts=context.max_python_execution_attempts,
            max_generation_retries=context.max_generation_retries,
            max_output_tokens=context.max_output_tokens,
        )
        return

    if context.slot.condition == "P0":
        run_openai_p0(
            bundle_dir=context.bundle_dir,
            run_id=context.attempt_id,
            output_dir=context.output_dir,
            model_name=context.model_name,
            reasoning_effort=context.reasoning_effort,
            max_model_calls=context.max_model_calls,
            max_total_tokens=context.max_total_tokens,
            max_python_execution_attempts=context.max_python_execution_attempts,
            max_generation_retries=context.max_generation_retries,
            max_output_tokens=context.max_output_tokens,
        )
        return

    raise ValueError(f"Unknown held-out condition: {context.slot.condition}")


def reconcile_pending_summary(
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
) -> dict[str, Any] | None:
    """Reconcile one summary-without-record state without launching inference."""

    _, slots, _ = load_and_validate_materialized_plan(
        plan_path=plan_path,
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    status = determine_next_status(slots=slots, attempts_root=attempts_root)
    if status.status != "SUMMARY_RECONCILIATION_REQUIRED":
        return None

    assert status.slot is not None
    assert status.attempt_number is not None
    plan_sha = _sha256_file(Path(plan_path))
    state, payload = _attempt_state(
        attempts_root=Path(attempts_root),
        slot=status.slot,
        number=status.attempt_number,
    )
    if state != "SUMMARY_WITHOUT_RECORD" or payload is None:
        raise RuntimeError("Reconciliation target changed unexpectedly.")

    return _reconstruct_record_from_summary(
        attempts_root=Path(attempts_root),
        slot=status.slot,
        number=status.attempt_number,
        plan_sha256=plan_sha,
        payload=payload,
    )


def execute_next_attempt(
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    attempt_runner: AttemptRunner | None = None,
) -> dict[str, Any]:
    """Launch exactly one eligible held-out attempt, or refuse safely."""

    plan, slots, validations = load_and_validate_materialized_plan(
        plan_path=plan_path,
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    root = Path(attempts_root)
    status = determine_next_status(slots=slots, attempts_root=root)

    if status.status == "SUMMARY_RECONCILIATION_REQUIRED":
        record = reconcile_pending_summary(
            plan_path=plan_path,
            protocol_path=protocol_path,
            fingerprint_path=fingerprint_path,
            bundle_root=bundle_root,
            attempts_root=attempts_root,
        )
        assert record is not None
        return {
            "action": "RECONCILED_EXISTING_SUMMARY",
            "launched_model_attempt": False,
            "attempt_record": record,
        }

    if status.status not in {_STATUS_READY_INITIAL, _STATUS_READY_REPLACEMENT}:
        return {
            "action": status.status,
            "launched_model_attempt": False,
            "message": status.message,
        }

    assert status.slot is not None
    assert status.attempt_number is not None
    assert status.attempt_id is not None

    context = _execution_context(
        plan=plan,
        slot=status.slot,
        attempt_number=status.attempt_number,
        bundle_root=Path(bundle_root),
        attempts_root=root,
    )
    if context.output_dir.exists():
        raise FileExistsError(
            f"Attempt output directory already exists: {context.output_dir}"
        )
    context.output_dir.mkdir(parents=True, exist_ok=False)

    plan_sha = _sha256_file(Path(plan_path))
    bundle_validation = validations[status.slot.variant]
    started = {
        "attempt_id": context.attempt_id,
        "attempt_number": context.attempt_number,
        "slot": asdict(context.slot),
        "started_at_utc": _utc_now(),
        "plan_sha256": plan_sha,
        "bundle_sha256": bundle_validation.aggregate_sha256,
        "registered_configuration": {
            "model": context.model_name,
            "reasoning_effort": context.reasoning_effort,
            "max_model_calls": context.max_model_calls,
            "max_total_tokens": context.max_total_tokens,
            "max_python_execution_attempts": context.max_python_execution_attempts,
            "max_generation_retries": context.max_generation_retries,
            "max_output_tokens": context.max_output_tokens,
            "python_timeout_seconds": context.python_timeout_seconds,
            "provider_request_timeout_seconds": context.provider_request_timeout_seconds,
        },
    }
    _write_json(context.output_dir / _ATTEMPT_STARTED_FILE, started)

    runner = attempt_runner or _production_attempt_runner
    started_perf = time.perf_counter()
    runner(context)
    wall_clock = time.perf_counter() - started_perf

    summary_path = context.output_dir / _SUMMARY_FILE
    if not summary_path.is_file():
        raise RuntimeError(
            "Treatment runner returned without writing summary.json. The attempt-start "
            "marker is retained and future execution will pause rather than duplicate it."
        )

    summary = _read_json(summary_path)
    _validate_summary_identity(
        summary=summary,
        slot=context.slot,
        expected_attempt_id=context.attempt_id,
    )
    classification = _classification_from_summary(summary)
    record = {
        "attempt_id": context.attempt_id,
        "attempt_number": context.attempt_number,
        "slot": asdict(context.slot),
        "plan_sha256": plan_sha,
        "bundle_sha256": bundle_validation.aggregate_sha256,
        "reconciled_from_existing_summary": False,
        "started_at_utc": started["started_at_utc"],
        "finished_at_utc": _utc_now(),
        "wall_clock_seconds": wall_clock,
        **classification,
        "summary": summary,
    }
    _write_json(context.output_dir / _ATTEMPT_RECORD_FILE, record)

    return {
        "action": "ATTEMPT_COMPLETED",
        "launched_model_attempt": True,
        "attempt_record": record,
    }


def status_document(
    *,
    plan_path: str | Path = DEFAULT_PLAN_PATH,
    protocol_path: str | Path = DEFAULT_PROTOCOL_PATH,
    fingerprint_path: str | Path = DEFAULT_FINGERPRINT_PATH,
    bundle_root: str | Path = DEFAULT_BUNDLE_ROOT,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
) -> dict[str, Any]:
    """Return a no-inference snapshot of the next held-out execution action."""

    _, slots, validations = load_and_validate_materialized_plan(
        plan_path=plan_path,
        protocol_path=protocol_path,
        fingerprint_path=fingerprint_path,
        bundle_root=bundle_root,
    )
    status = determine_next_status(slots=slots, attempts_root=attempts_root)
    resolved_slots = 0
    for slot in slots:
        first_state, _ = _attempt_state(
            attempts_root=Path(attempts_root),
            slot=slot,
            number=1,
        )
        if first_state == "ABSENT":
            break
        slot_status = determine_next_status(slots=(slot,), attempts_root=attempts_root)
        if slot_status.status == _STATUS_COMPLETE:
            resolved_slots += 1
        else:
            break

    return {
        "status": status.status,
        "message": status.message,
        "next_slot": asdict(status.slot) if status.slot is not None else None,
        "next_attempt_number": status.attempt_number,
        "next_attempt_id": status.attempt_id,
        "resolved_slots": resolved_slots,
        "total_slots": len(slots),
        "validated_bundle_sha256": {
            variant: validation.aggregate_sha256
            for variant, validation in validations.items()
        },
        "launched_model_attempt": False,
    }


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Inspect or advance Prototype V0 held-out execution. The run-next "
            "command launches at most one paid treatment attempt."
        )
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("status", help="Validate frozen inputs and show the next action.")
    subparsers.add_parser(
        "run-next",
        help="Launch exactly one eligible held-out attempt, or reconcile/pause safely.",
    )
    return parser.parse_args()


def _print_status(payload: Mapping[str, Any]) -> None:
    print(f"Status: {payload['status']}")
    print(f"Resolved slots: {payload['resolved_slots']}/{payload['total_slots']}")
    if payload.get("next_attempt_id"):
        print(f"Next attempt: {payload['next_attempt_id']}")
    print(str(payload["message"]))
    print("Model attempt launched: False")


def _print_run_result(payload: Mapping[str, Any]) -> None:
    print(f"Action: {payload['action']}")
    print(f"Model attempt launched: {payload['launched_model_attempt']}")
    record = payload.get("attempt_record")
    if isinstance(record, Mapping):
        print(f"Attempt: {record['attempt_id']}")
        print(f"Classification: {record['classification']}")
        print(f"Behavior evaluable: {record['behavior_evaluable']}")
        print(f"Replacement eligible: {record['replacement_eligible']}")
        print(f"Slot resolved: {record['slot_resolved']}")
    elif payload.get("message"):
        print(str(payload["message"]))


def main() -> None:
    args = _parse_args()
    if args.command == "status":
        _print_status(status_document())
        return

    if args.command == "run-next":
        _print_run_result(execute_next_attempt())
        return

    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    main()
