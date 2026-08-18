"""Condition-neutral orchestration around the frozen Prototype V0 held-out runner.

The supervisor removes repetitive human transport work without changing the
registered treatment semantics. It delegates every paid attempt to
``heldout_runner.execute_next_attempt`` unchanged, mechanically verifies the
persisted result, and advances only when the verifier establishes experiment
integrity.

The supervisor may execute several preregistered attempts sequentially in one
local process. It never runs attempts concurrently, never changes slot order,
never performs semantic judging, and never injects previous outcomes into later
treatments. Ordinary behavioral outcomes such as Python errors, deterministic
failures, incomplete work, or budget exhaustion are retained exactly as the
frozen protocol requires and do not by themselves block later slots.
"""

from __future__ import annotations

import argparse
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from .heldout_runner import execute_next_attempt, status_document
from .heldout_verifier import (
    DEFAULT_VERIFICATION_ROOT,
    backfill_verification,
    verify_attempt,
)


DEFAULT_SUPERVISOR_ROOT = Path("results/held_out/supervisor")
DEFAULT_EXPORT_ROOT = Path("results/held_out/supervisor_exports")
SUPERVISOR_SCHEMA_VERSION = "v0.1.0"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def _write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(dict(payload), indent=2, sort_keys=True), encoding="utf-8"
    )


def _verification_preflight() -> dict[str, Any]:
    aggregate = backfill_verification()
    if aggregate["integrity_failed"]:
        failed = [
            item["attempt_id"]
            for item in aggregate["reports"]
            if item["integrity_status"] != "PASS"
        ]
        raise RuntimeError(
            "Existing completed attempts failed mechanical verification. "
            f"Refusing new paid inference until reviewed: {failed}"
        )
    return aggregate


def supervisor_status() -> dict[str, Any]:
    """Return frozen runner status plus current verification coverage."""

    runner = status_document()
    verification = backfill_verification()
    return {
        "schema_version": SUPERVISOR_SCHEMA_VERSION,
        "generated_at_utc": _utc_now(),
        "runner": runner,
        "verification": {
            "attempts_verified": verification["attempts_verified"],
            "integrity_passed": verification["integrity_passed"],
            "integrity_failed": verification["integrity_failed"],
        },
        "boundary": {
            "sequential_only": True,
            "changes_treatment_behavior": False,
            "performs_semantic_judging": False,
        },
    }


def run_batch(*, max_model_attempts: int) -> dict[str, Any]:
    """Run sequential frozen attempts until a safety pause or explicit limit.

    ``max_model_attempts`` counts only invocations that actually launch a paid
    treatment attempt. No-inference summary reconciliation does not consume the
    caller's model-attempt allowance.
    """

    if max_model_attempts <= 0:
        raise ValueError("max_model_attempts must be positive.")

    preflight = _verification_preflight()
    batch_id = f"batch-{_stamp()}"
    started = _utc_now()
    entries: list[dict[str, Any]] = []
    model_attempts_launched = 0
    stop_reason = "MAX_MODEL_ATTEMPTS_REACHED"

    while model_attempts_launched < max_model_attempts:
        result = execute_next_attempt()
        action = str(result["action"])
        launched = bool(result.get("launched_model_attempt", False))
        if launched:
            model_attempts_launched += 1

        entry: dict[str, Any] = {
            "action": action,
            "launched_model_attempt": launched,
        }
        record = result.get("attempt_record")
        if isinstance(record, Mapping):
            attempt_value = str(record["attempt_id"])
            verification = verify_attempt(attempt_value)
            entry.update(
                {
                    "attempt_id": attempt_value,
                    "classification": record.get("classification"),
                    "behavior_evaluable": record.get("behavior_evaluable"),
                    "replacement_eligible": record.get("replacement_eligible"),
                    "slot_resolved": record.get("slot_resolved"),
                    "verification_integrity_status": verification[
                        "integrity_status"
                    ],
                    "review_flags": verification[
                        "behavioral_observations"
                    ].get("review_flags", []),
                    "mechanical_summary": verification["mechanical_summary"],
                }
            )
            entries.append(entry)
            if verification["integrity_status"] != "PASS":
                stop_reason = "MECHANICAL_VERIFICATION_FAILED"
                break
            # A valid non-behavior-evaluable provider failure remains unresolved,
            # so the next loop iteration naturally launches its preregistered
            # replacement inside the same slot. Behavioral outcomes resolve their
            # slots and the frozen runner naturally advances to the next slot.
            continue

        entries.append(entry)
        if action == "EXPERIMENT_COMPLETE":
            stop_reason = "EXPERIMENT_COMPLETE"
            break
        if action == "RECONCILED_EXISTING_SUMMARY":
            continue

        stop_reason = action
        break

    final_status = status_document()
    payload = {
        "schema_version": SUPERVISOR_SCHEMA_VERSION,
        "batch_id": batch_id,
        "started_at_utc": started,
        "finished_at_utc": _utc_now(),
        "max_model_attempts": max_model_attempts,
        "model_attempts_launched": model_attempts_launched,
        "stop_reason": stop_reason,
        "preflight": {
            "attempts_verified": preflight["attempts_verified"],
            "integrity_failed": preflight["integrity_failed"],
        },
        "entries": entries,
        "final_runner_status": final_status,
        "boundary": {
            "uses_frozen_execute_next_attempt": True,
            "sequential_only": True,
            "changes_slot_order": False,
            "changes_replacement_policy": False,
            "performs_semantic_judging": False,
            "writes_inside_attempt_directories": False,
        },
    }
    target = DEFAULT_SUPERVISOR_ROOT / f"{batch_id}.json"
    _write_json(target, payload)
    return payload


def export_supervisor_state(*, output_path: Path | None = None) -> Path:
    """Create a compact export containing no raw treatment conversation."""

    DEFAULT_SUPERVISOR_ROOT.mkdir(parents=True, exist_ok=True)
    DEFAULT_VERIFICATION_ROOT.mkdir(parents=True, exist_ok=True)
    DEFAULT_EXPORT_ROOT.mkdir(parents=True, exist_ok=True)

    snapshot = supervisor_status()
    snapshot_path = DEFAULT_SUPERVISOR_ROOT / "current_snapshot.json"
    _write_json(snapshot_path, snapshot)

    target = output_path or (
        DEFAULT_EXPORT_ROOT / f"heldout_supervisor_export_{_stamp()}.zip"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        target,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        for path in sorted(DEFAULT_VERIFICATION_ROOT.glob("*.json")):
            archive.write(
                path,
                arcname=f"mechanical_verification/{path.name}",
            )
        for path in sorted(DEFAULT_SUPERVISOR_ROOT.glob("*.json")):
            archive.write(path, arcname=f"supervisor/{path.name}")
    return target


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Condition-neutral supervisor for frozen Prototype V0 held-out "
            "execution."
        )
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser(
        "status",
        help="Verify completed attempts and show the next frozen action.",
    )
    sub.add_parser(
        "verify-existing",
        help="Retroactively verify all completed attempts without inference.",
    )
    run = sub.add_parser(
        "run-batch",
        help=(
            "Sequentially run and mechanically verify up to N paid attempts, "
            "pausing on integrity failure or runner safety state."
        ),
    )
    run.add_argument("--max-model-attempts", type=int, required=True)
    export = sub.add_parser(
        "export",
        help=(
            "Create one compact ZIP of verifier and supervisor reports for "
            "review."
        ),
    )
    export.add_argument("--output", type=Path, default=None)
    return parser.parse_args()


def _print_status(payload: Mapping[str, Any]) -> None:
    runner = payload["runner"]
    verification = payload["verification"]
    print(f"Runner status: {runner['status']}")
    print(f"Resolved slots: {runner['resolved_slots']}/{runner['total_slots']}")
    print(f"Verified completed attempts: {verification['attempts_verified']}")
    print(f"Verification integrity failures: {verification['integrity_failed']}")
    if runner.get("next_attempt_id"):
        print(f"Next attempt: {runner['next_attempt_id']}")
    print(str(runner["message"]))


def _print_batch(payload: Mapping[str, Any]) -> None:
    print(f"Batch: {payload['batch_id']}")
    print(f"Model attempts launched: {payload['model_attempts_launched']}")
    print(f"Stop reason: {payload['stop_reason']}")
    for entry in payload["entries"]:
        attempt = entry.get("attempt_id")
        if attempt:
            print(
                f"{attempt}: {entry.get('classification')} / "
                f"verification={entry.get('verification_integrity_status')}"
            )
        else:
            print(f"Action: {entry['action']}")
    final_status = payload["final_runner_status"]
    print(
        f"Resolved slots now: "
        f"{final_status['resolved_slots']}/{final_status['total_slots']}"
    )
    if final_status.get("next_attempt_id"):
        print(f"Next attempt: {final_status['next_attempt_id']}")


def main() -> None:
    args = _parse_args()
    if args.command == "status":
        _print_status(supervisor_status())
        return
    if args.command == "verify-existing":
        result = backfill_verification()
        print(f"Completed attempts verified: {result['attempts_verified']}")
        print(f"Integrity passed: {result['integrity_passed']}")
        print(f"Integrity failed: {result['integrity_failed']}")
        for report in result["reports"]:
            flags = ",".join(report["review_flags"]) or "none"
            print(
                f"{report['attempt_id']}: {report['integrity_status']} "
                f"review_flags={flags}"
            )
        return
    if args.command == "run-batch":
        payload = run_batch(max_model_attempts=args.max_model_attempts)
        _print_batch(payload)
        export_path = export_supervisor_state()
        print(f"Compact review export: {export_path.resolve()}")
        return
    if args.command == "export":
        path = export_supervisor_state(output_path=args.output)
        print(f"Compact review export: {path.resolve()}")
        return
    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    main()
