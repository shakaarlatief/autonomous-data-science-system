"""Read-only live observability for Prototype V0 held-out execution.

This module is deliberately outside the frozen treatment and supervisor execution
path. It launches no model calls, writes no experiment artifacts, changes no run
state, and performs no semantic judging. Its only purpose is to make long
sequential held-out batches observable while they are running.

The monitor watches the existing append-only attempt ledger and mechanical
verification directory. It tolerates a trace file being appended concurrently by
the treatment process and reports only mechanically observable progress such as:

* the active attempt identity;
* current project phase and latest trace event;
* successful model-generation count observed in the trace;
* provider-generation error count;
* Python execution-attempt count;
* completed attempt-record count; and
* completed mechanical-verification report count and integrity failures.

Because a started attempt without an executor record can mean either "currently
running" or "interrupted" when viewed by a separate process, this monitor does
not classify such a directory as interrupted. It reports it neutrally as an
active/pending attempt. The frozen runner remains the authority for execution
state and replacement semantics.
"""

from __future__ import annotations

import argparse
import json
import time
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_ATTEMPTS_ROOT = Path("results/held_out/attempts")
DEFAULT_VERIFICATION_ROOT = Path("results/held_out/mechanical_verification")


@dataclass(frozen=True)
class ActiveAttemptProgress:
    """Observable progress for one started attempt without a final executor record."""

    attempt_id: str
    trace_events: int
    successful_model_generations: int
    generation_errors: int
    python_execution_attempts: int
    latest_sequence: int | None
    latest_phase: str | None
    latest_event_type: str | None


@dataclass(frozen=True)
class MonitorSnapshot:
    """Read-only filesystem snapshot of current held-out execution progress."""

    generated_at_utc: str
    completed_attempt_records: int
    verification_reports: int
    verification_integrity_failures: tuple[str, ...]
    active_attempts: tuple[ActiveAttemptProgress, ...]
    latest_completed_attempt: str | None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _safe_json(path: Path) -> dict[str, Any] | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _read_trace_tolerant(path: Path) -> list[dict[str, Any]]:
    """Read complete JSONL records while another process may append the file.

    A concurrently written final line may temporarily be incomplete. Such a line
    is ignored rather than treated as an experiment defect because this module is
    an observer, not an integrity verifier.
    """

    if not path.is_file():
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []

    events: list[dict[str, Any]] = []
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            events.append(payload)
    return events


def _python_attempt_count(events: list[dict[str, Any]]) -> int:
    return sum(
        1
        for event in events
        if event.get("event_type") == "EXECUTE_PYTHON"
        and bool(event.get("allowed", False))
    )


def _active_progress(attempt_dir: Path) -> ActiveAttemptProgress:
    events = _read_trace_tolerant(attempt_dir / "trace.jsonl")
    latest = events[-1] if events else {}
    return ActiveAttemptProgress(
        attempt_id=attempt_dir.name,
        trace_events=len(events),
        successful_model_generations=sum(
            1 for event in events if event.get("event_type") == "MODEL_GENERATION"
        ),
        generation_errors=sum(
            1 for event in events if event.get("event_type") == "MODEL_GENERATION_ERROR"
        ),
        python_execution_attempts=_python_attempt_count(events),
        latest_sequence=(
            int(latest["sequence"])
            if isinstance(latest.get("sequence"), int)
            else None
        ),
        latest_phase=(
            str(latest["phase"]) if latest.get("phase") is not None else None
        ),
        latest_event_type=(
            str(latest["event_type"])
            if latest.get("event_type") is not None
            else None
        ),
    )


def snapshot_progress(
    *,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    verification_root: str | Path = DEFAULT_VERIFICATION_ROOT,
) -> MonitorSnapshot:
    """Return one condition-neutral read-only progress snapshot."""

    attempts = Path(attempts_root)
    verification = Path(verification_root)

    attempt_dirs = sorted(
        [path for path in attempts.glob("*") if path.is_dir()]
        if attempts.exists()
        else []
    )

    completed: list[str] = []
    active: list[ActiveAttemptProgress] = []
    for attempt_dir in attempt_dirs:
        if (attempt_dir / "attempt_record.json").is_file():
            completed.append(attempt_dir.name)
            continue
        if (attempt_dir / "attempt_started.json").is_file():
            active.append(_active_progress(attempt_dir))

    verification_files = sorted(verification.glob("*.json")) if verification.exists() else []
    integrity_failures: list[str] = []
    valid_verification_reports = 0
    for path in verification_files:
        payload = _safe_json(path)
        if payload is None:
            continue

        attempt_id = payload.get("attempt_id")
        integrity_status = payload.get("integrity_status")
        if not isinstance(attempt_id, str) or integrity_status not in {"PASS", "FAIL"}:
            # The verification directory also contains aggregate metadata such as
            # index.json. Only attempt-level reports belong in live report counts.
            continue

        valid_verification_reports += 1
        if integrity_status != "PASS":
            integrity_failures.append(attempt_id)

    return MonitorSnapshot(
        generated_at_utc=_utc_now(),
        completed_attempt_records=len(completed),
        verification_reports=valid_verification_reports,
        verification_integrity_failures=tuple(sorted(integrity_failures)),
        active_attempts=tuple(active),
        latest_completed_attempt=completed[-1] if completed else None,
    )


def _snapshot_signature(snapshot: MonitorSnapshot) -> tuple[Any, ...]:
    """Return fields whose changes are useful enough to print immediately."""

    active = tuple(
        (
            item.attempt_id,
            item.trace_events,
            item.successful_model_generations,
            item.generation_errors,
            item.python_execution_attempts,
            item.latest_sequence,
            item.latest_phase,
            item.latest_event_type,
        )
        for item in snapshot.active_attempts
    )
    return (
        snapshot.completed_attempt_records,
        snapshot.verification_reports,
        snapshot.verification_integrity_failures,
        snapshot.latest_completed_attempt,
        active,
    )


def _format_snapshot(snapshot: MonitorSnapshot, *, heartbeat: bool = False) -> str:
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = f"[{timestamp}]"
    if heartbeat:
        prefix += " heartbeat"

    if snapshot.active_attempts:
        active_parts = []
        for item in snapshot.active_attempts:
            active_parts.append(
                " ".join(
                    [
                        f"active={item.attempt_id}",
                        f"phase={item.latest_phase or 'pending_trace'}",
                        f"calls={item.successful_model_generations}",
                        f"python={item.python_execution_attempts}",
                        f"gen_errors={item.generation_errors}",
                        f"trace={item.trace_events}",
                        f"last={item.latest_event_type or 'none'}",
                    ]
                )
            )
        activity = " | ".join(active_parts)
    else:
        activity = "active=none"

    failure_text = (
        ",".join(snapshot.verification_integrity_failures)
        if snapshot.verification_integrity_failures
        else "none"
    )
    return (
        f"{prefix} {activity} | completed_attempts={snapshot.completed_attempt_records} "
        f"verified={snapshot.verification_reports} integrity_failures={failure_text}"
    )


def watch(
    *,
    interval_seconds: float = 5.0,
    heartbeat_seconds: float = 60.0,
    attempts_root: str | Path = DEFAULT_ATTEMPTS_ROOT,
    verification_root: str | Path = DEFAULT_VERIFICATION_ROOT,
) -> None:
    """Continuously print progress changes and periodic liveness heartbeats."""

    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be positive.")
    if heartbeat_seconds <= 0:
        raise ValueError("heartbeat_seconds must be positive.")

    print(
        "Read-only held-out monitor started. It launches no model calls and writes no experiment state.",
        flush=True,
    )
    print("Press Ctrl+C to stop monitoring; this does not stop the supervisor.", flush=True)

    previous_signature: tuple[Any, ...] | None = None
    last_print = 0.0
    try:
        while True:
            snapshot = snapshot_progress(
                attempts_root=attempts_root,
                verification_root=verification_root,
            )
            signature = _snapshot_signature(snapshot)
            now = time.monotonic()
            changed = signature != previous_signature
            heartbeat_due = now - last_print >= heartbeat_seconds
            if changed or heartbeat_due:
                print(
                    _format_snapshot(snapshot, heartbeat=heartbeat_due and not changed),
                    flush=True,
                )
                last_print = now
                previous_signature = signature
            time.sleep(interval_seconds)
    except KeyboardInterrupt:
        print("Held-out monitor stopped. Supervisor execution was not modified.", flush=True)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only live monitor for Prototype V0 held-out execution."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Print one read-only progress snapshot.")

    watch_parser = sub.add_parser(
        "watch",
        help="Watch attempt progress and print changes without modifying execution.",
    )
    watch_parser.add_argument("--interval-seconds", type=float, default=5.0)
    watch_parser.add_argument("--heartbeat-seconds", type=float, default=60.0)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    if args.command == "status":
        print(_format_snapshot(snapshot_progress()))
        return
    if args.command == "watch":
        watch(
            interval_seconds=args.interval_seconds,
            heartbeat_seconds=args.heartbeat_seconds,
        )
        return
    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    main()
