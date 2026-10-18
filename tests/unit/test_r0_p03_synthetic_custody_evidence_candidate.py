"""Ensure incomplete custody evidence cannot become a scored PASS."""
import copy
import json
from pathlib import Path

import pytest

from experiments.r0_p03_navigation_probe.synthetic_custody_evidence_candidate import (
    OS_DENIED, READ_SUCCEEDED, classify, classify_file
)

FIXTURE = Path(__file__).parents[2] / "experiments/r0_p03_navigation_probe/synthetic_custody_evidence_candidate.json"


def test_exact_live_relay_classifies_only_owner_readback_and_root_refusal():
    evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))
    result = classify_file(FIXTURE)
    assert evidence["owner_report"]["claimed_sha256"] == (
        "681a62e12187586f99c60a7a93119bf25fedde8af27c274026283828db90f393"
    )
    assert result["synthetic_complete_packet_owner_report"] == "PASS"
    assert result["bounded_reader_refusal"] == "WORKSPACE_ROOT_REFUSAL"
    assert result["os_denial_both_sandbox_routes"] == "NOT_EXERCISED"
    assert result["scoped_status"] == "FAKE_C1_OWNER_READBACK_AND_TOOL_SCOPE_ONLY_OS_DENIAL_UNVERIFIED"
    assert result["full_real_gold_custody_qualified"] is False
    assert result["real_r0_p03_score_authorized"] is False


def test_one_real_read_failure_is_not_two_os_denials():
    evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))
    evidence["bridge_observations"]["read_only_sandbox_open"] = OS_DENIED
    result = classify(evidence)
    assert result["os_denial_both_sandbox_routes"] == "NOT_EXERCISED"
    assert result["real_r0_p03_score_authorized"] is False


def test_two_actual_os_denials_are_only_scoped_fake_evidence():
    evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))
    evidence["bridge_observations"]["read_only_sandbox_open"] = OS_DENIED
    evidence["bridge_observations"]["inherit_sandbox_open"] = OS_DENIED
    result = classify(evidence)
    assert result["os_denial_both_sandbox_routes"] == "PASS"
    assert result["full_real_gold_custody_qualified"] is False
    assert result["real_r0_p03_score_authorized"] is False


def test_successful_file_read_falsifies_protective_barrier():
    evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))
    evidence["bridge_observations"]["inherit_sandbox_open"] = READ_SUCCEEDED
    result = classify(evidence)
    assert result["scoped_status"] == "OWNER_FAKE_PACKET_SAFETY_BARRIER_FAILED"
    assert result["full_real_gold_custody_qualified"] is False


@pytest.mark.parametrize("patch", [
    lambda r: r.update(synthetic_marker="REAL_GOLD"),
    lambda r: r["owner_report"].update(real_gold_or_keys_used=True),
    lambda r: r["owner_report"].update(case_distribution={"legacy": 9, "primary": 11}),
    lambda r: r["owner_report"].update(claimed_sha256="not-a-hash"),
    lambda r: r["bridge_observations"].update(bounded_reader="OS_ACCESS_DENIED"),
    lambda r: r["bridge_observations"].update(inherit_sandbox_open="SYNTHETIC_PASS"),
    lambda r: r.update(research_boundary="R0_P03_SCORED"),
])
def test_false_evidence_rejected(patch):
    evidence = json.loads(FIXTURE.read_text(encoding="utf-8"))
    patch(evidence)
    with pytest.raises(ValueError):
        classify(evidence)
