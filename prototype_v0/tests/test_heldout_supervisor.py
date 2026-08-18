from __future__ import annotations

from pathlib import Path

import ads_v0.heldout_supervisor as supervisor


def _record(
    attempt_id: str,
    *,
    classification: str = "BEHAVIOR_EVALUABLE",
    behavior_evaluable: bool = True,
    replacement_eligible: bool = False,
    slot_resolved: bool = True,
) -> dict:
    return {
        "attempt_id": attempt_id,
        "classification": classification,
        "behavior_evaluable": behavior_evaluable,
        "replacement_eligible": replacement_eligible,
        "slot_resolved": slot_resolved,
    }


def _verification(attempt_id: str, *, passed: bool = True) -> dict:
    return {
        "attempt_id": attempt_id,
        "integrity_status": "PASS" if passed else "FAIL",
        "behavioral_observations": {"review_flags": []},
        "mechanical_summary": {
            "completed": True,
            "budget_exhausted": False,
        },
    }


def _preflight() -> dict:
    return {
        "attempts_verified": 10,
        "integrity_passed": 10,
        "integrity_failed": 0,
        "reports": [],
    }


def _status(next_attempt: str = "h1-r04-p0-a01") -> dict:
    return {
        "status": "READY_INITIAL",
        "message": "ready",
        "next_attempt_id": next_attempt,
        "resolved_slots": 12,
        "total_slots": 30,
    }


def test_batch_runs_multiple_clean_attempts_sequentially(
    tmp_path: Path,
    monkeypatch,
) -> None:
    results = iter(
        [
            {
                "action": "ATTEMPT_COMPLETED",
                "launched_model_attempt": True,
                "attempt_record": _record("h1-r04-b1-a01"),
            },
            {
                "action": "ATTEMPT_COMPLETED",
                "launched_model_attempt": True,
                "attempt_record": _record("h1-r04-p0-a01"),
            },
        ]
    )
    monkeypatch.setattr(supervisor, "_verification_preflight", _preflight)
    monkeypatch.setattr(supervisor, "execute_next_attempt", lambda: next(results))
    monkeypatch.setattr(
        supervisor,
        "verify_attempt",
        lambda attempt_id: _verification(attempt_id),
    )
    monkeypatch.setattr(supervisor, "status_document", _status)
    monkeypatch.setattr(supervisor, "DEFAULT_SUPERVISOR_ROOT", tmp_path / "supervisor")

    payload = supervisor.run_batch(max_model_attempts=2)

    assert payload["model_attempts_launched"] == 2
    assert payload["stop_reason"] == "MAX_MODEL_ATTEMPTS_REACHED"
    assert [entry["attempt_id"] for entry in payload["entries"]] == [
        "h1-r04-b1-a01",
        "h1-r04-p0-a01",
    ]
    assert all(
        entry["verification_integrity_status"] == "PASS"
        for entry in payload["entries"]
    )


def test_batch_automatically_keeps_replacement_inside_same_slot(
    tmp_path: Path,
    monkeypatch,
) -> None:
    results = iter(
        [
            {
                "action": "ATTEMPT_COMPLETED",
                "launched_model_attempt": True,
                "attempt_record": _record(
                    "h1-r04-b1-a01",
                    classification="NON_BEHAVIOR_EVALUABLE_PROVIDER_FAILURE",
                    behavior_evaluable=False,
                    replacement_eligible=True,
                    slot_resolved=False,
                ),
            },
            {
                "action": "ATTEMPT_COMPLETED",
                "launched_model_attempt": True,
                "attempt_record": _record("h1-r04-b1-a02"),
            },
        ]
    )
    monkeypatch.setattr(supervisor, "_verification_preflight", _preflight)
    monkeypatch.setattr(supervisor, "execute_next_attempt", lambda: next(results))
    monkeypatch.setattr(
        supervisor,
        "verify_attempt",
        lambda attempt_id: _verification(attempt_id),
    )
    monkeypatch.setattr(supervisor, "status_document", _status)
    monkeypatch.setattr(supervisor, "DEFAULT_SUPERVISOR_ROOT", tmp_path / "supervisor")

    payload = supervisor.run_batch(max_model_attempts=2)

    assert payload["model_attempts_launched"] == 2
    assert payload["entries"][0]["replacement_eligible"]
    assert payload["entries"][1]["slot_resolved"]


def test_batch_pauses_immediately_on_verifier_integrity_failure(
    tmp_path: Path,
    monkeypatch,
) -> None:
    calls = 0

    def execute() -> dict:
        nonlocal calls
        calls += 1
        return {
            "action": "ATTEMPT_COMPLETED",
            "launched_model_attempt": True,
            "attempt_record": _record("h1-r04-b1-a01"),
        }

    monkeypatch.setattr(supervisor, "_verification_preflight", _preflight)
    monkeypatch.setattr(supervisor, "execute_next_attempt", execute)
    monkeypatch.setattr(
        supervisor,
        "verify_attempt",
        lambda attempt_id: _verification(attempt_id, passed=False),
    )
    monkeypatch.setattr(supervisor, "status_document", _status)
    monkeypatch.setattr(supervisor, "DEFAULT_SUPERVISOR_ROOT", tmp_path / "supervisor")

    payload = supervisor.run_batch(max_model_attempts=5)

    assert calls == 1
    assert payload["model_attempts_launched"] == 1
    assert payload["stop_reason"] == "MECHANICAL_VERIFICATION_FAILED"


def test_preflight_refuses_new_inference_when_existing_verification_failed(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        supervisor,
        "backfill_verification",
        lambda: {
            "attempts_verified": 1,
            "integrity_passed": 0,
            "integrity_failed": 1,
            "reports": [
                {
                    "attempt_id": "h1-r01-b0-a01",
                    "integrity_status": "FAIL",
                }
            ],
        },
    )

    try:
        supervisor._verification_preflight()
    except RuntimeError as exc:
        assert "h1-r01-b0-a01" in str(exc)
    else:
        raise AssertionError("Expected verifier preflight to block new inference.")
