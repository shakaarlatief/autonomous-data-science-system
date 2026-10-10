"""Purely synthetic mutation tests for the bounded audit-receipt validator."""
from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from scripts.check_r0_p01_clause_audit_receipts import (
    INVENTORY, MESSAGE_DIR, PLAN, ROOT, audit_summary, parse_receipt, verify_batch,
)


def test_existing_batch001_receipt_is_complete_and_not_f1_authorization() -> None:
    actual=audit_summary()
    assert actual["batch_count"]==1
    assert actual["reviewed_units"]==49
    assert actual["accepted"]==39
    assert actual["pending"]==10
    assert actual["F1_frozen"] is False
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
