"""Fault-injection checks for the candidate inherited-clause F1 audit boundary.

All modified data is copied in memory. No owner signatures, historical
attempt evidence, credentials, future claim markers or F1 freeze are used.
"""
from __future__ import annotations

import copy
from pathlib import Path

import pytest

from scripts import r0_p01_audit_inventory_rev03 as source
from scripts.check_r0_p01_f1_audit_rev03 import (
    BASE, BATCHES, CATALOG, INVENTORY, PRIOR, ROOT, SEEDS,
    check, read_json, validate,
)


@pytest.fixture(scope="module")
def documents() -> dict:
    return {
        "actual": read_json(ROOT, INVENTORY),
        "baseline": source.inventory(ROOT),
        "batches": read_json(ROOT, BATCHES),
        "catalog": read_json(ROOT, CATALOG),
        "seeds": read_json(ROOT, SEEDS),
        "prior": read_json(ROOT, PRIOR),
    }


def faults(records: dict) -> list[str]:
    doc = copy.deepcopy(records)
    return validate(
        doc["actual"], doc["baseline"], doc["batches"],
        doc["catalog"], doc["seeds"], doc["prior"],
    )


def test_checked_in_unfrozen_audit_has_no_structural_defects() -> None:
    assert check() == []


def test_old_security_control_unit_cannot_disappear(documents: dict) -> None:
    x = copy.deepcopy(documents)
    x["actual"]["units"] = [
        u for u in x["actual"]["units"]
        if u["id"] != "V01_CONTROLS-L0013"
    ]
    assert any("normative unit" in e for e in faults(x))


def test_old_security_definition_binding_cannot_be_substituted(documents: dict) -> None:
    x = copy.deepcopy(documents)
    for u in x["actual"]["units"]:
        if u["source_id"]=="V01_CONTROLS" and u.get("section")==7:
            u["candidate_requirement_ids"] = ["C09"]
    assert any("control 7" in e for e in faults(x))


def test_missing_approved_policy_root_fails_closed() -> None:
    root_doc = source.decode_json(source.committed(ROOT,source.FILES["REV04_POLICY"]))
    root_doc.pop("forbidden")
    import json
    with pytest.raises(ValueError, match="policy root registry mismatch"):
        source.json_units("REV04_POLICY", json.dumps(root_doc).encode("utf-8"), True)


def test_copied_audit_unit_must_preserve_source_digest(documents: dict) -> None:
    x = copy.deepcopy(documents)
    x["actual"]["units"][12]["text_sha256"] = "0"*64
    assert any("unit source mismatch" in e for e in faults(x))


def test_premature_approval_without_reviewer_fails(documents: dict) -> None:
    x = copy.deepcopy(documents)
    x["actual"]["units"][4]["review"]["status"]="APPROVED"
    assert any("unsubstantiated approved reviewer" in e for e in faults(x))


def test_orphan_audit_batch_fails(documents: dict) -> None:
    x = copy.deepcopy(documents)
    x["batches"]["audit_batches"][0]["unit_ids"].pop(0)
    assert any("source-unit coverage" in e for e in faults(x))


def test_windows_native_prompt_and_owner_local_receipts_are_distinct(documents: dict) -> None:
    x = copy.deepcopy(documents)
    ids={v["test_id"]:v for v in x["catalog"]["tests"]}
    assert ids["T-NATIVE-PROMPT-VISIBILITY"]["layer"]=="OWNER_MACHINE_MANUAL"
    ids["T-SSH-PROMPT"]["layer"]="PURE"
    assert any("wrong native test layer" in e for e in faults(x))


def test_numeric_selected_arm_volume_not_a_free_optimisation(documents: dict) -> None:
    x = copy.deepcopy(documents)
    case=next(x for x in x["seeds"]["selection_and_volume_seeds"] if x["id"]=="SEL-001")
    assert case["frozen_selection"]=="B"
    assert case["expected_class"]=="AMEND"
    case["selected_projected_minutes_exact"]="87.3"
    assert any("selected-arm projected volume" in e for e in faults(x))


def test_review_does_not_authorize_attempt(documents: dict) -> None:
    x = copy.deepcopy(documents)
    x["actual"]["owner_attempt_002_authorized"]=True
    assert any("owner execution falsely authorized" in e for e in faults(x))


def test_unreviewed_units_cannot_claim_inherited_disposition(documents: dict) -> None:
    x = copy.deepcopy(documents)
    u=next(x for x in x["actual"]["units"] if x["source_id"]=="V01_CONTROLS")
    u["review"]["status"]="APPROVED"
    u["review"]["reviewer"]="reviewer-A"
    u["review"]["review_message"]="MC-0030-UNSIGNED"
    assert any("missing inherited disposition" in e for e in faults(x))


def test_table_syntax_is_not_mapped_as_normative_obligation(documents: dict) -> None:
    x=documents["actual"]
    assert all(
        u["excerpt"][:6] not in ("|---|","| ---")
        for u in x["units"] if u["source_id"].endswith("CONTRACT")
    )
    assert any(e["reason"]=="MARKDOWN_TABLE_SEPARATOR_SYNTAX"
               for e in x["table_syntax_context_exclusions"])
