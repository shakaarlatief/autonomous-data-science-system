"""Purely synthetic mutation tests for the bounded audit-receipt validator."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from scripts.check_r0_p01_clause_audit_receipts import (
    INVENTORY, MESSAGE_DIR, PLAN, ROOT, audit_summary, parse_receipt, verify_batch,
)


def test_completed_campaign_receipts_are_complete_and_not_f1_authorization() -> None:
    """Pin the entire independent audit campaign without confusing it with F1.

    Counts describe reviewer-issued ACCEPTED/PENDING semantic audit statuses.
    They are not the count of implemented controls, passing tests, or frozen
    requirements. A later change to the committed reviewer corpus must be
    explicitly reconciled here rather than silently accepted as historical
    approval.
    """
    actual=audit_summary()
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    assert actual["batch_count"]==plan["batch_count"]==18
    assert actual["reviewed_units"]==plan["total_units"]==1022
    assert actual["accepted"]==967
    assert actual["pending"]==55
    assert actual["accepted"]+actual["pending"]==actual["reviewed_units"]
    assert sum(x["units"] for x in actual["results"][:9])==472
    assert sum(x["accepted"] for x in actual["results"][:9])==428
    assert sum(x["pending"] for x in actual["results"][:9])==44
    assert actual["semantic_review_by_task_owner"]=="NOT_AUTOMATICALLY_APPROVED"
    assert actual["F1_frozen"] is False
    assert actual["F2_frozen"] is False
    assert actual["attempt_002_authorized"] is False


def test_existing_review_contains_zero_duplicate_ids() -> None:
    message = MESSAGE_DIR/"033_claude_r0_p01_clause_audit_batch001.md"
    receipt = parse_receipt(message,1)
    assert len(receipt)==49


def test_future_batch_with_exact_65_units_is_verifiable(tmp_path: Path) -> None:
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    inventory=json.loads(INVENTORY.read_text(encoding="utf-8"))
    batch=plan["audit_batches"][1]
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    rows=[f"{u}|INHERITED_UNCHANGED|R01|PENDING|EVIDENCE_PENDING|V02_ADDENDUM-L0024" for u in batch["unit_ids"]]
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+"\n".join(rows)+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    item=verify_batch(2,path,plan,inventory)
    assert item["units"]==65 and item["pending"]==65


def test_missing_future_unit_rejected(tmp_path: Path) -> None:
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    inventory=json.loads(INVENTORY.read_text(encoding="utf-8"))
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    rows=[f"{u}|INHERITED_UNCHANGED|R01|PENDING|EVIDENCE_PENDING|V02_ADDENDUM-L0024" for u in plan["audit_batches"][1]["unit_ids"][:-1]]
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+"\n".join(rows)+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    with pytest.raises(ValueError,match="incomplete"):
        verify_batch(2,path,plan,inventory)


def test_duplicate_future_unit_rejected(tmp_path: Path) -> None:
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    row="V02_ADDENDUM-L0024|INHERITED_UNCHANGED|C01|PENDING|X|V02_ADDENDUM-L0024"
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+row+"\n"+row+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    with pytest.raises(ValueError,match="duplicate unit"):
        parse_receipt(path,2)


def test_valid_inapplicable_metadata_unit_may_have_no_requirement(tmp_path: Path) -> None:
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    row="V02_ADDENDUM-L0024|NOT_APPLICABLE_TO_SUCCESSOR|-|ACCEPTED||V02_ADDENDUM-L0024;metadata-only"
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+row+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    assert parse_receipt(path,2)[row.split("|")[0]][1]=="-"


def test_applicable_requirement_may_not_be_empty_placeholder(tmp_path: Path) -> None:
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    row="V02_ADDENDUM-L0024|INHERITED_UNCHANGED|-|ACCEPTED||V02_ADDENDUM-L0024"
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+row+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    with pytest.raises(ValueError,match="missing/invalid IDs"):
        parse_receipt(path,2)


def test_pending_without_blocker_rejected(tmp_path: Path) -> None:
    path=tmp_path/"035_claude_r0_p01_clause_audit_batch002.md"
    row="V02_ADDENDUM-L0024|INHERITED_UNCHANGED|R01|PENDING||V02_ADDENDUM-L0024"
    path.write_text("Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"+row+"\nEND_AUDIT_RECEIPT\n",encoding="utf-8")
    with pytest.raises(ValueError,match="pending reason"):
        parse_receipt(path,2)


@pytest.mark.parametrize("batch_number", [10,14,18])
def test_json_path_ids_are_parsed_for_all_remaining_source_types(
    tmp_path: Path, batch_number: int,
) -> None:
    """Prove that real lowercase, array-indexed JSON-path IDs survive parsing.

    This does not attest semantic accuracy of fabricated synthetic receipt rows.
    The representative receipts include every original assigned source-unit ID,
    not a hand-picked simplified prefix.
    """
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    inventory=json.loads(INVENTORY.read_text(encoding="utf-8"))
    batch=plan["audit_batches"][batch_number-1]
    assert batch["source_id"] in {"REV04_POLICY","V01_FIXTURE","V01_RESULT"}
    assert all(":" in uid for uid in batch["unit_ids"])
    path=tmp_path/f"{batch_number+33:03}_claude_r0_p01_clause_audit_batch{batch_number:03}.md"
    rows=[
        f"{uid}|INHERITED_UNCHANGED|R01|PENDING|SYNTHETIC_STRUCTURE_ONLY|{batch['source_id']};test"
        for uid in batch["unit_ids"]
    ]
    path.write_text(
        "Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"
        +"\n".join(rows)
        +"\nEND_AUDIT_RECEIPT\n",
        encoding="utf-8",
    )
    parsed=parse_receipt(path,batch_number)
    assert set(parsed)==set(batch["unit_ids"])
    assert verify_batch(batch_number,path,plan,inventory)["units"]==len(batch["unit_ids"])


def test_json_path_receipt_does_not_silently_drop_one_unit(tmp_path: Path) -> None:
    """A partial lowercase JSON receipt must fail instead of returning a PASS."""
    plan=json.loads(PLAN.read_text(encoding="utf-8"))
    inventory=json.loads(INVENTORY.read_text(encoding="utf-8"))
    batch=plan["audit_batches"][9]
    path=tmp_path/"043_claude_r0_p01_clause_audit_batch010.md"
    rows=[
        f"{uid}|INHERITED_UNCHANGED|R01|PENDING|SYNTHETIC_ONLY|REV04_POLICY;test"
        for uid in batch["unit_ids"][:-1]
    ]
    path.write_text(
        "Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"
        +"\n".join(rows)
        +"\nEND_AUDIT_RECEIPT\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError,match="incomplete"):
        verify_batch(10,path,plan,inventory)

def test_future_receipt_rejects_unrecognized_nonempty_row(tmp_path: Path) -> None:
    """Malformed receipt rows must not disappear silently from audit evidence."""
    path=tmp_path/"043_claude_r0_p01_clause_audit_batch010.md"
    valid="REV04_POLICY:claim_cap.absolute_new_claim_cap|INHERITED_UNCHANGED|R01|PENDING|TEST|REV04_POLICY;test"
    path.write_text(
        "Reviewer: claude-04\nBEGIN_AUDIT_RECEIPT\n"
        +valid
        +"\nREV04_POLICY:unexpected/path|INHERITED_UNCHANGED|R01|PENDING|TEST|TEST"
        +"\nEND_AUDIT_RECEIPT\n",encoding="utf-8",
    )
    with pytest.raises(ValueError,match="unsupported receipt row"):
        parse_receipt(path,10)
