from __future__ import annotations

import json
from pathlib import Path

from ads_v0.heldout_monitor import snapshot_progress


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_jsonl(path: Path, payloads: list[dict], *, trailing_partial: str | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for payload in payloads:
            handle.write(json.dumps(payload) + "\n")
        if trailing_partial is not None:
            handle.write(trailing_partial)


def test_snapshot_reports_active_attempt_progress_without_writing(tmp_path: Path) -> None:
    attempts = tmp_path / "attempts"
    verification = tmp_path / "verification"
    active = attempts / "h1-r05-p0-a01"

    _write_json(active / "attempt_started.json", {"attempt_id": active.name})
    _write_jsonl(
        active / "trace.jsonl",
        [
            {
                "sequence": 1,
                "event_type": "MODEL_GENERATION",
                "phase": "PHASE_1_PROVISIONAL_DEVELOPMENT",
                "allowed": True,
            },
            {
                "sequence": 2,
                "event_type": "EXECUTE_PYTHON",
                "phase": "PHASE_1_PROVISIONAL_DEVELOPMENT",
                "allowed": True,
            },
            {
                "sequence": 3,
                "event_type": "MODEL_GENERATION_ERROR",
                "phase": "PHASE_1_PROVISIONAL_DEVELOPMENT",
                "allowed": False,
            },
        ],
        trailing_partial='{"sequence": 4, "event_type":',
    )

    snapshot = snapshot_progress(
        attempts_root=attempts,
        verification_root=verification,
    )

    assert snapshot.completed_attempt_records == 0
    assert snapshot.verification_reports == 0
    assert len(snapshot.active_attempts) == 1
    progress = snapshot.active_attempts[0]
    assert progress.attempt_id == active.name
    assert progress.trace_events == 3
    assert progress.successful_model_generations == 1
    assert progress.generation_errors == 1
    assert progress.python_execution_attempts == 1
    assert progress.latest_sequence == 3
    assert progress.latest_phase == "PHASE_1_PROVISIONAL_DEVELOPMENT"
    assert progress.latest_event_type == "MODEL_GENERATION_ERROR"

    # The observer must not create or mutate experiment files.
    assert sorted(path.name for path in active.iterdir()) == [
        "attempt_started.json",
        "trace.jsonl",
    ]


def test_snapshot_counts_completed_and_verification_integrity(tmp_path: Path) -> None:
    attempts = tmp_path / "attempts"
    verification = tmp_path / "verification"

    first = attempts / "h1-r04-b1-a01"
    second = attempts / "h1-r04-p0-a01"
    _write_json(first / "attempt_started.json", {"attempt_id": first.name})
    _write_json(first / "attempt_record.json", {"attempt_id": first.name})
    _write_json(second / "attempt_started.json", {"attempt_id": second.name})
    _write_json(second / "attempt_record.json", {"attempt_id": second.name})

    _write_json(
        verification / "h1-r04-b1-a01.json",
        {"attempt_id": first.name, "integrity_status": "PASS"},
    )
    _write_json(
        verification / "h1-r04-p0-a01.json",
        {"attempt_id": second.name, "integrity_status": "FAIL"},
    )
    _write_json(
        verification / "index.json",
        {
            "attempts_verified": 2,
            "integrity_passed": 1,
            "integrity_failed": 1,
            "reports": [],
        },
    )

    snapshot = snapshot_progress(
        attempts_root=attempts,
        verification_root=verification,
    )

    assert snapshot.completed_attempt_records == 2
    assert snapshot.verification_reports == 2
    assert snapshot.verification_integrity_failures == (second.name,)
    assert snapshot.active_attempts == ()
    assert snapshot.latest_completed_attempt == second.name


def test_snapshot_ignores_invalid_verification_json_for_observability(tmp_path: Path) -> None:
    attempts = tmp_path / "attempts"
    verification = tmp_path / "verification"
    verification.mkdir(parents=True)
    (verification / "partial.json").write_text('{"attempt_id":', encoding="utf-8")

    snapshot = snapshot_progress(
        attempts_root=attempts,
        verification_root=verification,
    )

    assert snapshot.verification_reports == 0
    assert snapshot.verification_integrity_failures == ()
