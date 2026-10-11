"""Generate and verify an exact pending-review index from Claude audit receipts.

The index is a lossless *review finding* index. It is not a normative-source
amendment, an approval of Claude's accepted rows, a scorer oracle or a grant of
owner-trial authority. It reads only the committed public audit corpus and
unfrozen inventory; no historical owner evidence or credentials are accessed.

Default mode is read-only verification. The explicit --write mode regenerates
the derived register after upstream independently reviewed audit changes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

try:
    from scripts.check_r0_p01_clause_audit_receipts import (
        INVENTORY, MESSAGE_DIR, PLAN, ROOT, audit_summary, parse_receipt
    )
except ModuleNotFoundError:
    from check_r0_p01_clause_audit_receipts import (
        INVENTORY, MESSAGE_DIR, PLAN, ROOT, audit_summary, parse_receipt
    )

DEST = Path("docs/research/r0_p01_successor_design/R0_P01_F1_PENDING_AUDIT_RECONCILIATION_REV01_UNFROZEN.json")


def manifest(root: Path = ROOT) -> dict:
    """Transcribe all independently reviewed but unresolved source units.

    The complete audit's receipt checker establishes exact-once source-ID
    coverage. This function separately materializes its unresolved subset
    without deduplicating cross-source occurrences of the same causal blocker.
    """
    status = audit_summary(root)
    if status["batch_count"] != 18 or status["reviewed_units"] != 1022:
        raise ValueError("partial audit: do not manufacture a complete pending register")
    plan = json.loads((root / PLAN.relative_to(ROOT)).read_text(encoding="utf-8"))
    inv_path = root / INVENTORY.relative_to(ROOT)
    inventory = json.loads(inv_path.read_text(encoding="utf-8"))
    units = {u["id"]: u for u in inventory["units"]}
    entries = []
    source_messages = []
    for batch in plan["audit_batches"]:
        batch_no = int(batch["batch_id"].split("-")[-1])
        name = ("033_claude_r0_p01_clause_audit_batch001.md"
                if batch_no == 1 else
                f"{batch_no+33:03}_claude_r0_p01_clause_audit_batch{batch_no:03}.md")
        path = root / MESSAGE_DIR.relative_to(ROOT) / name
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        source_messages.append({"batch_id": batch["batch_id"],
                                "message_path": str((MESSAGE_DIR / name).relative_to(root)).replace("\\", "/"),
                                "message_sha256": sha})
        for unit_id, result in parse_receipt(path, batch_no).items():
            disposition, targets, state, blocker, basis = result
            if state != "PENDING":
                continue
            source = units[unit_id]
            if not blocker or not basis:
                raise ValueError(f"incomplete pending source receipt: {unit_id}")
            entries.append({
                "batch_id": batch["batch_id"],
                "unit_id": unit_id,
                "source_id": source["source_id"],
                "source_text_sha256": source["text_sha256"],
                "review_message": name,
                "review_message_sha256": sha,
                "reviewer_disposition": disposition,
                "reviewed_requirement_ids": targets.split(",") if targets != "-" else [],
                "blocker": blocker,
                "reviewed_basis": basis,
                "task_owner_resolution": "UNRESOLVED",
                "prospective_f1_status": "NOT_QUALIFIED",
            })
    if len(entries) != status["pending"] or status["accepted"] + len(entries) != status["reviewed_units"]:
        raise ValueError("independent reviewer pending counts do not reconcile")
    families = sorted(set(
        b for entry in entries
        for b in entry["blocker"].split(";")
        if b
    ))
    return {
        "schema_version": 1,
        "status": "UNFROZEN_REVIEWER_FINDINGS_TASK_OWNER_RECONCILIATION_PENDING",
        "authority": "Indexes Claude independent audit receipts; cannot approve normative semantics, change accepted B01/B02 policy or authorize an experiment.",
        "source_audit_plan": str(PLAN.relative_to(root)).replace("\\", "/"),
        "source_audit_inventory": str(INVENTORY.relative_to(root)).replace("\\", "/"),
        "source_audit_inventory_sha256": hashlib.sha256(inv_path.read_bytes()).hexdigest(),
        "audit_summary": {
            "batches": status["batch_count"],
            "reviewed_units": status["reviewed_units"],
            "reviewer_accepted_units": status["accepted"],
            "pending_units": status["pending"],
            "open_blocker_field_values": len(set(x["blocker"] for x in entries)),
        },
        "reviewer_message_digests": source_messages,
        "pending": entries,
        "warning": "A reviewer ACCEPTED row is NOT an independently qualified implemented security control. The pending register is not a complete inventory of all future F1/F2 deficiencies.",
        "F1_frozen": False,
        "F2_frozen": False,
        "owner_attempt_002_authorized": False,
    }


def serialized(obj: dict) -> bytes:
    return (json.dumps(obj, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def validate(root: Path = ROOT) -> None:
    """Require exact reproducibility from current immutable reviewer receipts."""
    output = root / DEST
    if not output.exists():
        raise ValueError(f"missing derived reconciliation register {DEST}")
    generated = serialized(manifest(root))
    if generated != output.read_bytes():
        raise ValueError("pending register diverged from reviewer receipts, messages, source units or counts")
    print("R0_P01_PENDING_REGISTER=PASS reviewer_pending=55 reviewed=1022 batches=18")
    print("TASK_OWNER_RECONCILIATION=NOT_COMPLETE; F1_F2=UNFROZEN; ATTEMPT_002=NOT_AUTHORIZED")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="explicitly update public, derived candidate register")
    args = ap.parse_args()
    if args.write:
        out = ROOT / DEST
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(serialized(manifest()))
        print(f"REGENERATED={DEST}")
    validate()
