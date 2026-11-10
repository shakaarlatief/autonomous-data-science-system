"""Task-independent real-source closure audit: fail-closed synthetic controls.

Invented candidate byte blobs and fictional supplemental metadata demonstrate
accounting, source pin binding, refusal of automatic source admission and
deterministic safe aggregates. Live census is separately run at the actual
pinned Git repository and never relies on synthetic claims of status.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe import (
    source_world_coverage_gate as gate,
)

PIN = "a" * 40


def make_input():
    bodies = {
        "README.md": b"# Fake orientation\n",
        "docs/DECISIONS.md": b"# Fake decisions\n",
        "frontend/src/fixture.ts": b"const product = true;\n",
        "src/ads_system/app.py": b"x = 1\n",
        "tests/unit/test_unit.py": b"def test_dummy(): pass\n",
    }
    candidates = {p: (gate.sha1git(raw), raw) for p, raw in bodies.items()}
    others = [
        {
            "path": "docs/checkpoints/001_record.md",
            "git_blob_oid": gate.sha1git(b"# Fictional historical witness\n"),
            "sha256": sha256(b"# Fictional historical witness\n").hexdigest(),
            "bytes": len(b"# Fictional historical witness\n"),
            "role_hint": "historical_checkpoint_evidence",
            "status": "REVIEW_ONLY_NOT_ADMITTED",
            "review_flags": [],
        },
        {
            "path": "docs/local_execution/validation/001_report.md",
            "git_blob_oid": gate.sha1git(b"Fake PASS\n"),
            "sha256": sha256(b"Fake PASS\n").hexdigest(),
            "bytes": len(b"Fake PASS\n"),
            "role_hint": "execution_validation_evidence",
            "status": "REVIEW_ONLY_NOT_ADMITTED",
            "review_flags": ["LEGACY_W5_REFERENCE"],
        },
        {
            "path": "docs/research/003_media.png",
            "git_blob_oid": "b" * 40,
            "role_hint": "historical_research_and_decision_basis",
            "status": "NON_TEXT_UNSUPPORTED_NOT_ADMITTED",
            "review_flags": ["UNSUPPORTED_MEDIA"],
        },
    ]
    supplemental = {
        "source_ref": PIN,
        "admission_decision": "NONE_ADMITTED_BY_LEXICAL_OR_PATH_CENSUS",
        "review_record_count": len(others),
        "review_records": others,
    }
    return candidates, supplemental


def test_complete_disjoint_accounting_and_no_auto_admission():
    candidate, historical = make_input()
    ledger, receipt = gate.reconcile(candidate, historical, source_ref=PIN)
    assert len(ledger["source_records"]) == 8
    assert receipt["complete_roster_records"] == 8
    assert receipt["preliminary_candidate_unqualified"] == 5
    assert receipt["historical_total"] == 3
    assert receipt["historical_review_only"] == 2
    assert receipt["unsupported_historical"] == 1
    assert receipt["source_admissions"] == 0
    assert receipt["world_status"] == "WORLD_UNFROZEN"
    assert receipt["release_status"] == "SCORED_AUTHOR_WORLD_NOT_READY"
    assert all(x["status"] == gate.NO_ADMISSION for x in ledger["source_records"])
    assert all(x["path"] not in json.dumps(receipt) for x in ledger["source_records"])


def test_category_gap_uses_families_not_lexical_screen():
    candidate, historical = make_input()
    _, receipt = gate.reconcile(candidate, historical, source_ref=PIN)
    categories = receipt["task_category_capacity_diagnostics"]
    assert categories["cold_start_current_orientation"][
        "review_only_or_unsupported_family_hints"] == ["historical_status"]
    assert categories["impact_analysis_architecture_evolution"][
        "review_only_or_unsupported_family_hints"] == ["historical_status"]
    assert categories["exact_source_authority_recovery"][
        "review_only_or_unsupported_family_hints"] == [
            "historical_status", "execution_evidence"
        ]
    assert categories["cross_plane_discovery"][
        "review_only_or_unsupported_family_hints"] == []
    assert all(
        row["task_answerability"] == "NOT_PROVEN"
        for row in categories.values()
    )


def test_bad_pin_duplicate_candidate_and_mismatched_ref_hold():
    candidate, historical = make_input()
    with pytest.raises(ValueError, match="Unpinned"):
        gate.reconcile(candidate, historical, source_ref="invalid")
    other = deepcopy(historical)
    other["source_ref"] = "f" * 40
    with pytest.raises(ValueError, match="source ref mismatch"):
        gate.reconcile(candidate, other, source_ref=PIN)
    other = deepcopy(historical)
    other["review_records"][0]["path"] = "README.md"
    with pytest.raises(ValueError, match="Overlapping"):
        gate.reconcile(candidate, other, source_ref=PIN)


def test_flag_absence_not_authorized_and_attempted_admission_rejected():
    candidate, historical = make_input()
    historical["review_records"][0]["review_flags"] = []
    _, result = gate.reconcile(candidate, historical, source_ref=PIN)
    assert result["source_admissions"] == 0
    historical["review_records"][0]["status"] = "ADMITTED"
    with pytest.raises(ValueError, match="Overlapping"):
        gate.reconcile(candidate, historical, source_ref=PIN)


def test_unsupported_does_not_masquerade_as_examined_text():
    candidate, historical = make_input()
    historical["review_records"][-1]["sha256"] = "a" * 64
    with pytest.raises(ValueError, match="unsupported"):
        gate.reconcile(candidate, historical, source_ref=PIN)
    candidate, historical = make_input()
    historical["review_records"][-1]["status"] = "REVIEW_ONLY_NOT_ADMITTED"
    with pytest.raises(ValueError, match="Missing text"):
        gate.reconcile(candidate, historical, source_ref=PIN)


def test_reject_source_identity_drift_and_bad_role():
    candidate, historical = make_input()
    path = "README.md"
    candidate[path] = ("0" * 40, candidate[path][1])
    with pytest.raises(ValueError, match="candidate source identity"):
        gate.reconcile(candidate, historical, source_ref=PIN)
    candidate, historical = make_input()
    historical["review_records"][0]["role_hint"] = "governing"
    with pytest.raises(ValueError, match="Overlapping"):
        gate.reconcile(candidate, historical, source_ref=PIN)


def test_deterministic_source_roster_fingerprint_and_safe_summary():
    candidate, historical = make_input()
    ledger1, receipt1 = gate.reconcile(candidate, historical, source_ref=PIN)
    ledger2, receipt2 = gate.reconcile(dict(reversed(list(candidate.items()))),
                                       historical, source_ref=PIN)
    assert ledger1 == ledger2
    assert receipt1 == receipt2
    assert len(receipt1["roster_sha256"]) == 64
    assert receipt1["roster_sha256"] == ledger1["roster_sha256"]
    # Even source-specific malicious strings never surface in public receipt.
    historical["review_records"][0]["review_flags"] = [
        "RESTRICTED_ANSWER_SHOULD_NOT_LEAK"
    ]
    _, receipt3 = gate.reconcile(candidate, historical, source_ref=PIN)
    assert receipt3["roster_sha256"] != receipt1["roster_sha256"]
    assert "RESTRICTED_ANSWER_SHOULD_NOT_LEAK" not in json.dumps(receipt3)


def test_reject_historical_count_drift_and_unknown_family():
    candidate, historical = make_input()
    historical["review_record_count"] = 0
    with pytest.raises(ValueError, match="count drift"):
        gate.reconcile(candidate, historical, source_ref=PIN)
    candidate, historical = make_input()
    historical["review_records"][0]["path"] = "../outside.md"
    with pytest.raises(ValueError, match="Overlapping"):
        gate.reconcile(candidate, historical, source_ref=PIN)


def test_unscored_real_corpus_entrypoint_refuses_wrong_historical_pin(
    tmp_path: Path,
):
    with pytest.raises(ValueError, match="Historical source pin changed"):
        gate.compute(tmp_path, pin="f" * 40)
