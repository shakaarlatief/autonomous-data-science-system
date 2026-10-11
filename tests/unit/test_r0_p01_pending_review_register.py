"""Regression tests for the provenance-locked pending-audit register.

These tests protect transfer of independently reviewed source-unit findings into
prospective task-owner reconciliation. They do not certify the reviewer
interpretations or execute owner-authenticated controls.
"""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path

import pytest

from scripts import check_r0_p01_pending_review_register as pending


def test_complete_register_reproduces_all_55_pending_source_units() -> None:
    source = pending.manifest()
    counts = source["audit_summary"]
    assert counts == {
        "batches": 18,
        "reviewed_units": 1022,
        "reviewer_accepted_units": 967,
        "pending_units": 55,
        "open_blocker_field_values": 33,
    }
    assert len(source["pending"]) == 55
    assert len({x["unit_id"] for x in source["pending"]}) == 55
    assert source["F1_frozen"] is False
    assert source["F2_frozen"] is False
    assert source["owner_attempt_002_authorized"] is False


def test_register_is_byte_reproducible_from_review_corpus() -> None:
    pending.validate()
    assert (pending.ROOT / pending.DEST).read_bytes() == pending.serialized(pending.manifest())


def test_batch_001_is_preserved_without_reclassification() -> None:
    source = pending.manifest()
    grouped = Counter(x["batch_id"] for x in source["pending"])
    assert grouped["Q0-AUDIT-001"] == 10
    assert grouped["Q0-AUDIT-009"] == 0
    assert sum(grouped.values()) == 55
    assert grouped["Q0-AUDIT-013"] == 3


def test_crucial_pending_findings_remain_visible_and_unresolved() -> None:
    rows = pending.manifest()["pending"]
    for code in ("B05-A1", "B07-A3", "B08-A1", "B11-A1"):
        matched = [r for r in rows if code in r["blocker"]]
        assert matched, f"high-impact finding {code} absent"
        assert all(x["task_owner_resolution"] == "UNRESOLVED" for x in matched)


def test_misreported_accepted_count_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    baseline = pending.audit_summary()
    tampered = dict(baseline)
    tampered["accepted"] = baseline["accepted"] + 1
    monkeypatch.setattr(pending, "audit_summary", lambda _root: tampered)
    with pytest.raises(ValueError, match="pending counts do not reconcile"):
        pending.manifest()
