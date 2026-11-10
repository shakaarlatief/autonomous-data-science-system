"""Pre-holdout scientific method freeze fidelity and authorization guards.

No withheld evidence is opened by these tests. The only executable evidence
is the already published source-free rule/interpretation and their owner-
authorized, unscored exact-digest freeze. A successful test is not a
source-status finding or experiment score.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXPERIMENT = ROOT / "experiments/r0_p03_navigation_probe"
FREEZE = EXPERIMENT / "R0_P03_SOURCE_FAMILY_FALSIFICATION_METHOD_FREEZE_V01.json"
HANDOFF = EXPERIMENT / "R0_P03_SOURCE_FAMILY_FALSIFICATION_REVIEWER_HANDOFF_V01.md"
RULE_HASH = "9e402bbaa5f190d72b55e76f38979ea032f90c724e2385e99c20da3e0a4b1268"
INTERPRETATION_HASH = "7594b420f215c311c4075a98c2775857c0e359e712efbec397d3ac969d8862ff"
HOLDOUT_HASH = "3d7236f3b69d496fd99d597f452ac5dec108716655b0724f80bbc2971c66c4b3"


def freeze() -> dict:
    return json.loads(FREEZE.read_text(encoding="utf-8"))


def test_freeze_owner_scope_is_exact_and_non_scored() -> None:
    state = freeze()
    assert state["identifier"] == "R0_P03_SOURCE_FAMILY_FALSIFICATION_METHOD_FREEZE_V01"
    assert state["schema_version"] == 1
    assert state["owner_decision"]["verbatim_acceptance"] == "I ACCEPT."
    assert state["frozen_method"]["state"] == "OWNER_ACCEPTED_FROZEN_FOR_FALSIFICATION_ONLY"
    assert "16-case" in state["owner_decision"]["accepted_scope"]
    assert "DIFFERENT non-arm reviewer" in state["owner_decision"]["authorized_disclosure"]
    assert state["custody_and_outcome"]["source_admissions"] == 0
    assert state["custody_and_outcome"]["author_world"] == "WORLD_UNFROZEN"
    assert state["custody_and_outcome"]["b0_b4_scoring"] == "NOT_STARTED"
    assert state["custody_and_outcome"]["gold"] == "NOT_STARTED"
    assert state["custody_and_outcome"]["original_rule_or_companion_modified"] is False
    assert state["heldout_packet"]["transfer_status"] == "AUTHORIZED_NOT_YET_CONFIRMED_TRANSFERRED"


def test_frozen_public_method_exact_bytes_and_git_safety_attribute() -> None:
    state = freeze()
    records = [
        (state["frozen_method"]["original_rule"], RULE_HASH, 18580),
        (state["frozen_method"]["companion_interpretation"], INTERPRETATION_HASH, 8178),
    ]
    attributes = (ROOT / ".gitattributes").read_text(encoding="utf-8")
    for record, digest, length in records:
        file = ROOT / record["path"]
        body = file.read_bytes()
        assert len(body) == record["bytes"] == length
        assert sha256(body).hexdigest() == record["sha256"] == digest
        assert record["path"] + " -text" in attributes
    assert state["frozen_method"]["frozen_by_this_separate_manifest"] is True


def test_holdout_commitment_without_accessing_heldout_contents() -> None:
    state = freeze()
    holdout = state["heldout_packet"]
    assert holdout["filename"] == "R0_P03_SOURCE_QUALIFICATION_FALSIFICATION_RESTRICTED.zip"
    assert holdout["bytes"] == 1384419
    assert holdout["sha256"] == HOLDOUT_HASH
    assert holdout["cases"] == 16
    assert holdout["strata"] == 8
    assert holdout["status"] == (
        "EXACT_LOCAL_FILE_HASH_REVERIFIED_WITHOUT_INSPECTING_SOURCE_CONTENT"
    )
    assert "Calibration source packet" in state["owner_decision"]["not_authorized"]
    assert "Restricted calibration case assessments" in state["owner_decision"]["not_authorized"]
    assert "Public repository publication of holdout" in state["owner_decision"]["not_authorized"]


def test_handoff_binds_every_expected_input_and_restricts_case_outputs() -> None:
    text = HANDOFF.read_text(encoding="utf-8")
    for expected in (RULE_HASH, INTERPRETATION_HASH, HOLDOUT_HASH):
        assert expected in text
    assert "different" in text.lower()
    assert "Temporary Chat" in text
    assert "FALSIFICATION_CASES_ASSIGNED = 16" in text
    assert "SOURCE_ADMISSIONS = ZERO" in text
    assert "R0_P03_SOURCE_FAMILY_FALSIFICATION_SOURCE_FREE_SUMMARY.md" in text
    assert "R0_P03_SOURCE_FAMILY_FALSIFICATION_CASES_RESTRICTED.md" in text
    assert "No transfer is automatically performed" in text
    assert "The owner must not attach" in text
