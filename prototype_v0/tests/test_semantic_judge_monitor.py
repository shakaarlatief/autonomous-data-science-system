from __future__ import annotations

import json
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path

from ads_v0 import semantic_judge_monitor as monitor


def _write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _prepare(root: Path, case_count: int) -> list[str]:
    blind_ids = [f"case-{index:016x}" for index in range(1, case_count + 1)]
    _write_json(
        root / monitor.PREPARED_MANIFEST_FILE,
        {
            "schema_version": "semantic_judge_supervisor_v0_1",
            "case_count": case_count,
            "cases": [
                {"blind_id": blind_id, "packet_sha256": f"sha-{index}"}
                for index, blind_id in enumerate(blind_ids, start=1)
            ],
        },
    )
    return blind_ids


def _write_pass(root: Path, blind_id: str, pass_number: int) -> None:
    _write_json(
        root / monitor.BLINDED_DIR / blind_id / f"pass_{pass_number}.json",
        {"pass_number": pass_number, "judgment": {}},
    )


def _write_consensus(root: Path, blind_id: str, *, manual: bool = False) -> None:
    _write_json(
        root / monitor.BLINDED_DIR / blind_id / "consensus.json",
        {
            "consensus": {
                "manual_adjudication_required": manual,
            }
        },
    )


def test_snapshot_reports_active_condition_blind_pass_and_elapsed_time(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_ids = _prepare(root, 2)
    first = blind_ids[0]

    started = datetime.now(timezone.utc) - timedelta(seconds=25)
    provider_dir = root / monitor.BLINDED_DIR / first / monitor.PROVIDER_ATTEMPTS_DIR
    _write_json(
        provider_dir / "pass_1_attempt_01_started.json",
        {
            "blind_id": first,
            "logical_pass": 1,
            "provider_attempt": 1,
            "started_at_utc": started.isoformat(),
        },
    )

    snapshot = monitor.snapshot_progress(semantic_root=root)

    assert snapshot.prepared_cases == 2
    assert snapshot.logical_passes_persisted == 0
    assert snapshot.logical_passes_required == 4
    assert snapshot.completed_cases == 0
    assert snapshot.provider_calls_recorded == 1
    assert snapshot.next_blind_id == first
    assert snapshot.next_case_position == 1
    assert snapshot.next_logical_pass == 1
    assert len(snapshot.active_passes) == 1

    active = snapshot.active_passes[0]
    assert active.blind_id == first
    assert active.case_position == 1
    assert active.total_cases == 2
    assert active.logical_pass == 1
    assert active.provider_attempt == 1
    assert active.elapsed_seconds is not None
    assert active.elapsed_seconds >= 20


def test_completed_snapshot_counts_consensus_and_manual_cases(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_ids = _prepare(root, 2)

    for blind_id in blind_ids:
        _write_pass(root, blind_id, 1)
        _write_pass(root, blind_id, 2)
    _write_consensus(root, blind_ids[0], manual=False)
    _write_consensus(root, blind_ids[1], manual=True)

    snapshot = monitor.snapshot_progress(semantic_root=root)

    assert snapshot.logical_passes_persisted == 4
    assert snapshot.logical_passes_required == 4
    assert snapshot.completed_cases == 2
    assert snapshot.manual_adjudication_cases == 1
    assert snapshot.active_passes == ()
    assert snapshot.next_blind_id is None
    assert snapshot.next_case_position is None
    assert snapshot.next_logical_pass is None
    assert snapshot.judge_complete is True


def test_completed_provider_attempt_is_not_reported_active(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_id = _prepare(root, 1)[0]
    provider_dir = root / monitor.BLINDED_DIR / blind_id / monitor.PROVIDER_ATTEMPTS_DIR

    _write_json(
        provider_dir / "pass_1_attempt_01_started.json",
        {"started_at_utc": datetime.now(timezone.utc).isoformat()},
    )
    _write_json(
        provider_dir / "pass_1_attempt_01_success.json",
        {"completed_at_utc": datetime.now(timezone.utc).isoformat()},
    )
    _write_pass(root, blind_id, 1)

    snapshot = monitor.snapshot_progress(semantic_root=root)

    assert snapshot.provider_calls_recorded == 1
    assert snapshot.active_passes == ()
    assert snapshot.logical_passes_persisted == 1
    assert snapshot.next_blind_id == blind_id
    assert snapshot.next_logical_pass == 2


def test_monitor_never_depends_on_private_decoder(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_id = _prepare(root, 1)[0]

    # Deliberately invalid and sensitive-looking content. The monitor must never
    # read this file, so its existence cannot affect condition-blind observability.
    private_decoder = root / "private_decoder.json"
    private_decoder.write_text('{"condition":"P0",', encoding="utf-8")

    _write_pass(root, blind_id, 1)
    snapshot = monitor.snapshot_progress(semantic_root=root)

    assert snapshot.prepared_cases == 1
    assert snapshot.logical_passes_persisted == 1
    assert snapshot.next_logical_pass == 2


def test_formatted_snapshot_includes_local_time_and_progress(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_id = _prepare(root, 1)[0]
    snapshot = monitor.snapshot_progress(semantic_root=root)

    rendered = monitor._format_snapshot(snapshot)

    assert re.match(r"^\[\d{2}:\d{2}:\d{2}\]", rendered)
    assert f"next={blind_id}" in rendered
    assert "case=1/1" in rendered
    assert "pass=1/2" in rendered
    assert "logical_passes=0/2" in rendered
    assert "completed_cases=0/1" in rendered


def test_snapshot_is_read_only(tmp_path: Path) -> None:
    root = tmp_path / "semantic"
    blind_id = _prepare(root, 1)[0]
    case_dir = root / monitor.BLINDED_DIR / blind_id
    case_dir.mkdir(parents=True, exist_ok=True)

    before = sorted(path.relative_to(root).as_posix() for path in root.rglob("*"))
    monitor.snapshot_progress(semantic_root=root)
    after = sorted(path.relative_to(root).as_posix() for path in root.rglob("*"))

    assert after == before
