"""Read-only live observability for Prototype V0 semantic judging.

This module is deliberately outside the semantic-judge execution path. It launches
no model calls, writes no semantic evidence, changes no judge state, and never
reads the private condition decoder. Its only purpose is to render human-friendly
progress from already-persisted blinded semantic-judge artifacts.

The design follows the same separation used for held-out treatment execution:
execution owns correctness and state transitions, while a sidecar observer owns
presentation. The observer can therefore be started, stopped, or fail without
changing the paid evaluation process.

The monitor exposes only condition-blind information:

* opaque blinded case identity and position;
* logical pass number;
* persisted logical-pass and completed-case counts;
* provider-attempt count;
* whether a provider attempt appears active;
* elapsed wall-clock time for an active provider attempt;
* manual-adjudication case count; and
* periodic liveness heartbeats.

It intentionally does not load ``private_decoder.json`` and therefore cannot map
opaque case IDs back to B0, B1, P0, variant, replicate, or treatment-run identity.
"""

from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_SEMANTIC_ROOT = Path("results/held_out/semantic_judge")
PREPARED_MANIFEST_FILE = "prepared_manifest.json"
BLINDED_DIR = "blinded"
PROVIDER_ATTEMPTS_DIR = "provider_attempts"
LOGICAL_PASSES = (1, 2)

_PROVIDER_STARTED_PATTERN = re.compile(
    r"^pass_(?P<pass_number>[12])_attempt_(?P<attempt_number>\d+)_started\.json$"
)


@dataclass(frozen=True)
class ActiveSemanticPass:
    """Condition-blind progress for one provider attempt currently in flight."""

    blind_id: str
    case_position: int
    total_cases: int
    logical_pass: int
    provider_attempt: int
    started_at_utc: str | None
    elapsed_seconds: float | None


@dataclass(frozen=True)
class SemanticJudgeMonitorSnapshot:
    """Read-only snapshot of persisted semantic-judge progress."""

    generated_at_utc: str
    prepared_cases: int
    logical_passes_persisted: int
    logical_passes_required: int
    completed_cases: int
    manual_adjudication_cases: int
    provider_calls_recorded: int
    active_passes: tuple[ActiveSemanticPass, ...]
    next_blind_id: str | None
    next_case_position: int | None
    next_logical_pass: int | None
    judge_complete: bool

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _safe_json(path: Path) -> dict[str, Any] | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, dict) else None


def _parse_utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def _elapsed_seconds(started_at_utc: Any, *, now_utc: datetime) -> float | None:
    started = _parse_utc(started_at_utc)
    if started is None:
        return None
    return max(0.0, (now_utc - started).total_seconds())


def _prepared_case_ids(root: Path) -> list[str]:
    manifest = _safe_json(root / PREPARED_MANIFEST_FILE)
    if manifest is None:
        return []
    rows = manifest.get("cases")
    if not isinstance(rows, list):
        return []

    blind_ids: list[str] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        blind_id = row.get("blind_id")
        if isinstance(blind_id, str) and blind_id:
            blind_ids.append(blind_id)
    return sorted(set(blind_ids))


def _provider_attempt_state(
    case_dir: Path,
    *,
    logical_pass: int,
    now_utc: datetime,
    case_position: int,
    total_cases: int,
) -> tuple[int, list[ActiveSemanticPass]]:
    """Return provider-call count and any active attempt for one logical pass."""

    provider_dir = case_dir / PROVIDER_ATTEMPTS_DIR
    if not provider_dir.exists():
        return 0, []

    started: list[tuple[int, Path, dict[str, Any] | None]] = []
    for path in provider_dir.glob(f"pass_{logical_pass}_attempt_*_started.json"):
        match = _PROVIDER_STARTED_PATTERN.match(path.name)
        if match is None:
            continue
        attempt_number = int(match.group("attempt_number"))
        started.append((attempt_number, path, _safe_json(path)))

    active: list[ActiveSemanticPass] = []
    pass_persisted = (case_dir / f"pass_{logical_pass}.json").is_file()
    if not pass_persisted:
        for attempt_number, _, payload in started:
            prefix = provider_dir / f"pass_{logical_pass}_attempt_{attempt_number:02d}"
            success = Path(str(prefix) + "_success.json")
            error = Path(str(prefix) + "_error.json")
            if success.is_file() or error.is_file():
                continue
            started_at = payload.get("started_at_utc") if payload is not None else None
            active.append(
                ActiveSemanticPass(
                    blind_id=case_dir.name,
                    case_position=case_position,
                    total_cases=total_cases,
                    logical_pass=logical_pass,
                    provider_attempt=attempt_number,
                    started_at_utc=(
                        str(started_at) if isinstance(started_at, str) else None
                    ),
                    elapsed_seconds=_elapsed_seconds(started_at, now_utc=now_utc),
                )
            )

    active.sort(key=lambda item: item.provider_attempt)
    return len(started), active


def snapshot_progress(
    *,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
) -> SemanticJudgeMonitorSnapshot:
    """Return one condition-blind, read-only semantic progress snapshot."""

    root = Path(semantic_root)
    blind_ids = _prepared_case_ids(root)
    total_cases = len(blind_ids)
    now_utc = _utc_now()

    logical_passes = 0
    completed_cases = 0
    manual_cases = 0
    provider_calls = 0
    active: list[ActiveSemanticPass] = []
    next_blind_id: str | None = None
    next_case_position: int | None = None
    next_logical_pass: int | None = None

    for case_position, blind_id in enumerate(blind_ids, start=1):
        case_dir = root / BLINDED_DIR / blind_id

        for logical_pass in LOGICAL_PASSES:
            if (case_dir / f"pass_{logical_pass}.json").is_file():
                logical_passes += 1
            elif next_blind_id is None:
                next_blind_id = blind_id
                next_case_position = case_position
                next_logical_pass = logical_pass

            count, active_items = _provider_attempt_state(
                case_dir,
                logical_pass=logical_pass,
                now_utc=now_utc,
                case_position=case_position,
                total_cases=total_cases,
            )
            provider_calls += count
            active.extend(active_items)

        consensus = _safe_json(case_dir / "consensus.json")
        if consensus is not None:
            completed_cases += 1
            consensus_payload = consensus.get("consensus")
            if isinstance(consensus_payload, dict) and bool(
                consensus_payload.get("manual_adjudication_required", False)
            ):
                manual_cases += 1

    required = total_cases * len(LOGICAL_PASSES)
    judge_complete = total_cases > 0 and completed_cases == total_cases
    if judge_complete:
        next_blind_id = None
        next_case_position = None
        next_logical_pass = None

    return SemanticJudgeMonitorSnapshot(
        generated_at_utc=now_utc.isoformat(),
        prepared_cases=total_cases,
        logical_passes_persisted=logical_passes,
        logical_passes_required=required,
        completed_cases=completed_cases,
        manual_adjudication_cases=manual_cases,
        provider_calls_recorded=provider_calls,
        active_passes=tuple(active),
        next_blind_id=next_blind_id,
        next_case_position=next_case_position,
        next_logical_pass=next_logical_pass,
        judge_complete=judge_complete,
    )


def _duration_text(seconds: float | None) -> str:
    if seconds is None:
        return "unknown"
    total = max(0, int(seconds))
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def _snapshot_signature(snapshot: SemanticJudgeMonitorSnapshot) -> tuple[Any, ...]:
    active = tuple(
        (
            item.blind_id,
            item.case_position,
            item.logical_pass,
            item.provider_attempt,
            int(item.elapsed_seconds or 0) // 5,
        )
        for item in snapshot.active_passes
    )
    return (
        snapshot.prepared_cases,
        snapshot.logical_passes_persisted,
        snapshot.completed_cases,
        snapshot.manual_adjudication_cases,
        snapshot.provider_calls_recorded,
        snapshot.next_blind_id,
        snapshot.next_case_position,
        snapshot.next_logical_pass,
        snapshot.judge_complete,
        active,
    )


def _format_snapshot(snapshot: SemanticJudgeMonitorSnapshot, *, heartbeat: bool = False) -> str:
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = f"[{timestamp}]"
    if heartbeat:
        prefix += " heartbeat"

    if snapshot.active_passes:
        activity_parts = []
        for item in snapshot.active_passes:
            activity_parts.append(
                " ".join(
                    [
                        f"active={item.blind_id}",
                        f"case={item.case_position}/{item.total_cases}",
                        f"pass={item.logical_pass}/2",
                        f"provider_attempt={item.provider_attempt}",
                        f"elapsed={_duration_text(item.elapsed_seconds)}",
                    ]
                )
            )
        activity = " | ".join(activity_parts)
    elif snapshot.next_blind_id is not None:
        activity = (
            f"active=none next={snapshot.next_blind_id} "
            f"case={snapshot.next_case_position}/{snapshot.prepared_cases} "
            f"pass={snapshot.next_logical_pass}/2"
        )
    else:
        activity = "active=none next=none"

    return (
        f"{prefix} {activity} | "
        f"logical_passes={snapshot.logical_passes_persisted}/"
        f"{snapshot.logical_passes_required} "
        f"completed_cases={snapshot.completed_cases}/{snapshot.prepared_cases} "
        f"manual_cases={snapshot.manual_adjudication_cases} "
        f"provider_calls={snapshot.provider_calls_recorded}"
    )


def watch(
    *,
    interval_seconds: float = 5.0,
    heartbeat_seconds: float = 60.0,
    semantic_root: str | Path = DEFAULT_SEMANTIC_ROOT,
) -> None:
    """Print progress changes and periodic heartbeats without modifying execution."""

    if interval_seconds <= 0:
        raise ValueError("interval_seconds must be positive.")
    if heartbeat_seconds <= 0:
        raise ValueError("heartbeat_seconds must be positive.")

    print(
        "Read-only semantic-judge monitor started. It launches no model calls, "
        "writes no semantic state, and never reads the private decoder.",
        flush=True,
    )
    print("Press Ctrl+C to stop monitoring; this does not stop judge execution.", flush=True)

    previous_signature: tuple[Any, ...] | None = None
    last_print = 0.0
    try:
        while True:
            snapshot = snapshot_progress(semantic_root=semantic_root)
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
        print(
            "Semantic-judge monitor stopped. Judge execution was not modified.",
            flush=True,
        )


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read-only live monitor for Prototype V0 blinded semantic judging."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="Print one condition-blind progress snapshot.")

    watch_parser = sub.add_parser(
        "watch",
        help="Watch semantic-judge progress without modifying execution.",
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
