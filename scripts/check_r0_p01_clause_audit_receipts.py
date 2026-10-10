"""Read-only verification of independently authored R0-P01 per-batch audit receipts.

This checker establishes source identity and exact-once batch membership, not
correctness of the reviewer's semantic judgments. An ACCEPTED line is a reviewer
finding and does not change owner-governed F1 freeze status or source contracts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_NORMATIVE_AUDIT_BATCH_PLAN_REV03_UNFROZEN.json"
INVENTORY = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json"
MESSAGE_DIR = ROOT / "docs/model_collaboration/threads/MC-0030/messages"
AUDIT_FNAME = re.compile(r"^(\d{3})_claude_r0_p01_clause_audit_batch(\d{3})\.md$")
FUTURE_ROW = re.compile(r"^[A-Z0-9_:\-\[\]\.]+[|]")
DISPOSITIONS = {"INHERITED_UNCHANGED", "NOT_APPLICABLE_TO_SUCCESSOR", "SUPERSEDED_BY_REV04"}
STATUSES = {"ACCEPTED", "PENDING"}
FIRST_RECEIPT_HEADER = "## 4. Machine-checkable receipt"

def parse_receipt(path: Path, batch_number: int) -> dict[str, tuple[str, str, str, str, str]]:
    """Read controlled receipt fields; reject duplicates and unknown dispositions."""
    s = path.read_text(encoding="utf-8")
    if batch_number == 1:
        assert FIRST_RECEIPT_HEADER in s
        block = s.split(FIRST_RECEIPT_HEADER,1)[1].split("## 5.",1)[0]
    else:
        if s.count("BEGIN_AUDIT_RECEIPT") != 1 or s.count("END_AUDIT_RECEIPT") != 1:
            raise ValueError(f"{path.name}: missing exact receipt delimiter")
        block = s.split("BEGIN_AUDIT_RECEIPT",1)[1].split("END_AUDIT_RECEIPT",1)[0]
    out: dict[str, tuple[str, str, str, str, str]] = {}
    for line in block.splitlines():
        line=line.strip()
        if not line or not FUTURE_ROW.match(line):
            continue
        if batch_number==1 and not line.startswith("V01_CONTROLS-L"):
            continue
        parts=line.split("|")
        if batch_number==1:
            if len(parts)!=5:
                raise ValueError(f"{path.name}: legacy row not five columns")
            unit,disposition,ids,status,blocker = parts
            basis="LEGACY_MESSAGE033_HUMAN_PER_UNIT_TABLE"
        else:
            if len(parts)!=6:
                raise ValueError(f"{path.name}: row not six columns")
            unit,disposition,ids,status,blocker,basis=parts
        if not unit or unit in out:
            raise ValueError(f"{path.name}: empty/duplicate unit {unit}")
        prefix=disposition.split(":",1)[0]
        if prefix not in DISPOSITIONS:
            raise ValueError(f"{path.name}: invalid disposition {disposition}")
        if status not in STATUSES:
            raise ValueError(f"{path.name}: invalid status {status}")
        # A demonstrably inapplicable source item must not be forced into an
        # unrelated requirement simply to satisfy an audit schema.
        no_ids = ids == "-"
        if (no_ids and prefix != "NOT_APPLICABLE_TO_SUCCESSOR") or (not ids) or (status=="PENDING" and not blocker) or not basis:
            raise ValueError(f"{path.name}: missing/invalid IDs, pending reason or source basis for {unit}")
        out[unit]=(disposition,ids,status,blocker,basis)
    if not out:
        raise ValueError(f"{path.name}: no parseable rows")
    return out

def verify_batch(number: int, message: Path, plan: dict, inventory: dict) -> dict:
    """Ensure receipt covers exactly assigned, committed source units."""
    batch=plan["audit_batches"][number-1]
    if batch["batch_id"]!=f"Q0-AUDIT-{number:03}":
        raise ValueError("batch identity mismatch")
    if message.name!=(
        "033_claude_r0_p01_clause_audit_batch001.md" if number==1
        else f"{number+33:03}_claude_r0_p01_clause_audit_batch{number:03}.md"
    ):
        raise ValueError("wrong canonical batch message name")
    ids=batch["unit_ids"]
    if hashlib.sha256(("\n".join(ids)+"\n").encode("utf-8")).hexdigest()!=batch["unit_id_list_sha256"]:
        raise ValueError("plan batch hash incorrect")
    sources={x["id"]:x for x in inventory["units"]}
    if any(uid not in sources or sources[uid]["source_id"]!=batch["source_id"] for uid in ids):
        raise ValueError("unit source ownership mismatch")
    rows=parse_receipt(message,number)
    if set(rows)!=set(ids):
        missing=set(ids)-set(rows)
        extra=set(rows)-set(ids)
        raise ValueError(f"batch {number:03} receipt incomplete missing={sorted(missing)[:5]} extra={sorted(extra)[:5]}")
    if len(rows)!=len(ids):
        raise ValueError("duplicate receipt entries")
    if number>1 and not all("Reviewer: claude-04" in message.read_text(encoding="utf-8") for _ in [0]):
        raise ValueError("missing named independent reviewer attestation")
    return {"batch":number, "units":len(rows),"accepted":sum(x[2]=="ACCEPTED" for x in rows.values()),
            "pending":sum(x[2]=="PENDING" for x in rows.values()),
            "sha256":hashlib.sha256(message.read_bytes()).hexdigest()}

def audit_summary(root: Path = ROOT) -> dict:
    """Read actual message files and fail on any ambiguous or out-of-plan audit."""
    plan=json.loads((root/PLAN.relative_to(ROOT)).read_text(encoding="utf-8"))
    inventory=json.loads((root/INVENTORY.relative_to(ROOT)).read_text(encoding="utf-8"))
    if plan["source_inventory_sha256"]!=hashlib.sha256((root/INVENTORY.relative_to(ROOT)).read_bytes()).hexdigest():
        raise ValueError("source inventory changed since batch partition")
    if plan["batch_count"]!=18 or plan["total_units"]!=1022:
        raise ValueError("unexpected audit scope")
    records=[]
    for number in range(1,19):
        name="033_claude_r0_p01_clause_audit_batch001.md" if number==1 else f"{number+33:03}_claude_r0_p01_clause_audit_batch{number:03}.md"
        path=root/MESSAGE_DIR.relative_to(ROOT)/name
        if not path.exists():
            # Do not skip a prior missing batch and count future batches as a
            # contiguous completed prefix.
            if any((root/MESSAGE_DIR.relative_to(ROOT)/(f"{n+33:03}_claude_r0_p01_clause_audit_batch{n:03}.md")).exists() for n in range(number+1,19)):
                raise ValueError(f"missing earlier audit batch {number:03}")
            break
        records.append(verify_batch(number,path,plan,inventory))
    scanned=[]
    for path in (root/MESSAGE_DIR.relative_to(ROOT)).glob("*_claude_r0_p01_clause_audit_batch*.md"):
        m=AUDIT_FNAME.fullmatch(path.name)
        if not m:
            raise ValueError(f"unrecognized audit receipt file {path.name}")
        n=int(m.group(2))
        if n<1 or n>18:
            raise ValueError("out of range audit batch")
        if path.name!=("033_claude_r0_p01_clause_audit_batch001.md" if n==1 else f"{n+33:03}_claude_r0_p01_clause_audit_batch{n:03}.md"):
            raise ValueError(f"incorrect message sequence {path.name}")
        scanned.append(n)
    if len(scanned)!=len(records):
        raise ValueError("audit files inconsistent with validated contiguous prefix")
    return {"batch_count":len(records),"reviewed_units":sum(x["units"] for x in records),
            "accepted":sum(x["accepted"] for x in records),
            "pending":sum(x["pending"] for x in records),"results":records,
            "semantic_review_by_task_owner":"NOT_AUTOMATICALLY_APPROVED",
            "F1_frozen":False,"F2_frozen":False,"attempt_002_authorized":False}

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    d=audit_summary()
    if args.json:
        print(json.dumps(d,indent=2))
    else:
        print(f"R0_P01_CLAUSE_AUDIT_RECEIPTS=PASS batches={d['batch_count']}/18 "
              f"units={d['reviewed_units']}/1022 accepted={d['accepted']} pending={d['pending']}")
        print("F1_SEMANTIC_APPROVAL=NOT_GIVEN; ATTEMPT_002=NOT_AUTHORIZED")
