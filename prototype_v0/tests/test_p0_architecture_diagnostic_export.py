from __future__ import annotations

import json
import zipfile
from pathlib import Path

from ads_v0 import p0_architecture_diagnostic_export as export


def _write_json(path: Path, payload) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _write_attempt(root: Path, attempt_id: str) -> None:
    attempt = root / attempt_id
    attempt.mkdir(parents=True, exist_ok=True)
    _write_json(attempt / "attempt_started.json", {"attempt_id": attempt_id})
    _write_json(attempt / "attempt_record.json", {"attempt_id": attempt_id})
    _write_json(
        attempt / "summary.json",
        {
            "condition": "P0",
            "run_id": attempt_id,
            "behavior_evaluable": True,
        },
    )
    _write_json(attempt / "deterministic_evaluation.json", {"passed_all_critical": True})
    _write_json(attempt / "milestones.json", {"final_report": None})
    _write_json(attempt / "conversation.json", {"messages": []})
    (attempt / "trace.jsonl").write_text(
        json.dumps({"event_type": "P0_STATE_CONTROL_ERROR"}) + "\n",
        encoding="utf-8",
    )
    _write_json(
        attempt / "p0_state.json",
        {
            "step": 5,
            "objects": [
                {
                    "id": "Q1",
                    "type": "QUESTION",
                    "status": "REOPENED",
                    "tags": ["priority:repair"],
                },
                {
                    "id": "AC1",
                    "type": "ACTION",
                    "status": "BLOCKED",
                    "tags": [],
                },
            ],
            "relations": [
                {"source_id": "Q1", "relation": "DEPENDS_ON", "target_id": "F1"}
            ],
        },
    )
    _write_json(
        attempt / "p0_state_history.json",
        [
            {
                "object_id": "Q1",
                "new_status_or_value": "REOPENED",
            },
            {
                "object_id": "A1",
                "new_status_or_value": "INVALIDATED",
            },
        ],
    )
    _write_json(
        attempt / "p0_knowledge_activations.json",
        [
            {
                "component_id": "K-INFO-003",
                "reopen_count": 1,
            }
        ],
    )


def _decoded_result(path: Path) -> None:
    rows = []
    for index in range(1, 31):
        condition = "P0" if index <= 10 else ("B0" if index <= 20 else "B1")
        rows.append(
            {
                "slot_index": index,
                "variant": "H1" if index % 2 else "H2",
                "replicate": ((index - 1) % 5) + 1,
                "condition": condition,
                "attempt_id": f"attempt-{index:02d}",
                "completed": True,
                "completed_within_budget": index % 2 == 0,
                "budget_exhausted": index % 2 == 1,
                "targeted_architecture_score": 1.8,
                "critical_failure_events": 0,
            }
        )
    _write_json(
        path,
        {
            "schema_version": "semantic_judge_decoded_v0_1",
            "decoder_read_after_freeze_verification": True,
            "frozen_semantic_aggregate_sha256": "abc123",
            "run_rows": rows,
        },
    )


def test_build_manifest_selects_only_p0_and_summarizes_state(tmp_path: Path) -> None:
    decoded = tmp_path / "decoded.json"
    attempts = tmp_path / "attempts"
    _decoded_result(decoded)
    for index in range(1, 11):
        _write_attempt(attempts, f"attempt-{index:02d}")

    manifest, files = export.build_export_manifest(
        decoded_result_path=decoded,
        attempts_root=attempts,
    )

    assert manifest["p0_case_count"] == 10
    assert len(files) == 10 * len(export._REQUIRED_FILES)
    assert all(case["attempt_id"].startswith("attempt-") for case in manifest["cases"])
    first = manifest["cases"][0]["structural_diagnostics"]
    assert first["p0_state_control_error_events"] == 1
    assert first["blocked_action_object_count"] == 1
    assert first["reopened_transition_count"] == 1
    assert first["invalidated_transition_count"] == 1
    assert first["knowledge_reopen_total"] == 1
    assert manifest["boundary"]["includes_non_P0_treatment_trajectories"] is False
    assert manifest["boundary"]["includes_semantic_private_decoder"] is False


def test_export_contains_only_allowlisted_p0_attempt_artifacts(tmp_path: Path) -> None:
    decoded = tmp_path / "decoded.json"
    attempts = tmp_path / "attempts"
    exports = tmp_path / "exports"
    _decoded_result(decoded)
    for index in range(1, 11):
        _write_attempt(attempts, f"attempt-{index:02d}")
    # A decoder-shaped file outside the allowlist must never be copied.
    _write_json(tmp_path / "private_decoder.json", {"secret": True})

    manifest, archive_path = export.export_p0_architecture_diagnostics(
        decoded_result_path=decoded,
        attempts_root=attempts,
        export_root=exports,
    )

    assert manifest["p0_case_count"] == 10
    with zipfile.ZipFile(archive_path) as archive:
        names = archive.namelist()
        assert names[0] == "p0_architecture_diagnostic_manifest.json"
        assert all("private_decoder" not in name for name in names)
        assert len(names) == 1 + 10 * len(export._REQUIRED_FILES)
        assert all(
            name == "p0_architecture_diagnostic_manifest.json"
            or name.startswith("attempts/attempt-")
            for name in names
        )
