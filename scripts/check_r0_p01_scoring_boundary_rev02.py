"""Fail-closed structural guard for the R0-P01 F1 REV02 scoring-boundary review.

This is deliberately not an executable owner-proof scorer, scientific outcome
oracle, or policy authority. It ensures that independent-review amendments,
the agreed committed source corpus, all 24 scenario identities/dispositions,
and the 18 open scoring-gate source findings are preserved for adjudication.

The checker refuses unknown scenarios, silent source mutations, loss of a
known owner-exception risk, and made-up inherited source anchors. It does not
prove that a source-grounded conditional outcome is technically correct.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

try:
    from scripts import check_r0_p01_pending_review_register as pending
except ModuleNotFoundError:
    import check_r0_p01_pending_review_register as pending

ROOT = Path(__file__).resolve().parents[1]
REV02 = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV02_UNFROZEN.json"
REV01 = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV01_UNFROZEN.json"
INVENTORY = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json"
GATES = ("B05-A1", "B07-A3", "B08-A1", "B11-A1")
EXPECTED = {
    "S1-01": "SOURCE_DETERMINED", "S1-02": "SOURCE_DETERMINED",
    "S1-03": "SOURCE_DETERMINED", "S1-04": "CANDIDATE_BLOCKED",
    "S1-05": "CANDIDATE_BLOCKED", "S2-01": "SOURCE_DETERMINED",
    "S2-02": "SOURCE_DETERMINED", "S2-03": "CANDIDATE_BLOCKED",
    "S2-04": "SOURCE_DETERMINED", "S3-01": "SOURCE_DETERMINED",
    "S3-02": "SOURCE_DETERMINED", "S3-03": "CANDIDATE_BLOCKED",
    "S3-04": "SOURCE_DETERMINED", "S4-01": "SOURCE_DETERMINED",
    "S4-02": "SOURCE_DETERMINED", "S4-03": "SOURCE_DETERMINED",
    "S4-04": "SOURCE_DETERMINED", "X1": "CANDIDATE_BLOCKED",
    "X2": "SOURCE_DETERMINED", "X3": "CANDIDATE_BLOCKED",
    "X4": "CANDIDATE_BLOCKED", "X5": "SOURCE_DETERMINED",
    "X6": "SOURCE_DETERMINED", "X7": "SOURCE_DETERMINED",
}
AMENDED = {"S1-02", "S1-04", "S2-02", "S2-03", "S2-04", "S3-01", "S3-02", "S3-04", "S4-01"}
PREMISES = {
    "other_arm_evidence", "proof_viability", "raw_flags",
    "process_isolation", "flag_origin", "receipt_producer"
}
FIELDS = {
    "id", "gate", "slug", "determination", "source_basis", "conditions",
    "source_grounded_conclusion", "f1_evidence_or_test", "qualification_boundary",
    "review_055_status", "claim_scope", "premises", "blocked_reason",
    "owner_policy_interpretation", "f1_decision_record"
}
SOURCE_PATHS = {
    "contract": ("REV04_CONTRACT", "docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md"),
    "policy": ("REV04_POLICY", "docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json"),
}
EXPECTED_HEX = {
    "contract": "9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175",
    "policy": "9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c",
}
SOURCE_REF = re.compile(r"^(?:REV04_CONTRACT|V01_CONTRACT|V02_ADDENDUM|V01_CONTROLS)-L\d{4}$|^(?:REV04_POLICY|V01_FIXTURE|V01_RESULT):[A-Za-z0-9_.\[\]-]+$")


def validate_payload(
    revision: dict, inventory: dict, register: dict, root: Path = ROOT
) -> dict:
    """Validate exact scope and source-backed provenance, not human assent."""
    if revision["schema_version"] != 2 or revision["status"] != "REV02_UNFROZEN_INDEPENDENT_AMENDMENT_REVIEW_PENDING":
        raise ValueError("revised F1 review status not approved")
    if revision["independent_review"] != "MC-0030_MESSAGE055_AMEND_REV01_TARGETED":
        raise ValueError("independent review provenance absent")
    if revision["gate_order"] != list(GATES):
        raise ValueError("scoring gate order changed")
    if set(revision["scenario_fields"]) != FIELDS:
        raise ValueError("REV02 field shape mismatch")
    if set(revision["determination_types"]) != {"SOURCE_DETERMINED", "CANDIDATE_BLOCKED"}:
        raise ValueError("REV02 improper determination states")
    if revision["accepted_decisions"] != ["B01", "B02"]:
        raise ValueError("B01/B02 acceptance flags missing")
    if revision["claude_audit_results"] != {
        "reviewed": 1022, "reviewer_accepted": 967, "reviewer_pending": 55
    }:
        raise ValueError("independent reviewer results changed")
    if "not a complete/scored F1 oracle" not in revision["authority"]:
        raise ValueError("F1 oracle authority overstated")
    for typ, (source_id, rel) in SOURCE_PATHS.items():
        digest = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if (revision[f"source_{typ}"] != rel or
            revision["approved_source_sha256"][typ] != EXPECTED_HEX[typ] or
            inventory["approved_source_sha256"][typ] != EXPECTED_HEX[typ] or
            digest != EXPECTED_HEX[typ]):
            raise ValueError(f"owner-approved {typ} source hash altered")
    owner_receipts = [
        "docs/research/r0_p01_successor_design/R0_P01_B01_OWNER_ACCEPTANCE_20261010.md",
        "docs/research/r0_p01_successor_design/R0_P01_B02_OWNER_ACCEPTANCE_20261010.md",
    ]
    if revision["source_owner_decisions"] != owner_receipts:
        raise ValueError("missing original owner acceptance records")
    for rel in owner_receipts:
        body = (root / rel).read_text(encoding="utf-8")
        if not all(d in body for d in EXPECTED_HEX.values()):
            raise ValueError("owner decision source hashes not actually bound")
    if revision["reviewer_risk_register"] != str(pending.DEST).replace("\\", "/"):
        raise ValueError("incorrect independent pending register source")
    src_ids = {u["id"] for u in inventory["units"]}
    rows = revision["cases"]
    if len(rows) != len(EXPECTED) or {x["id"] for x in rows} != set(EXPECTED):
        raise ValueError("required per-case identities changed or omitted")
    if len(set(x["id"] for x in rows)) != len(rows):
        raise ValueError("duplicate scenario identifier")
    counts = {"SOURCE_DETERMINED": 0, "CANDIDATE_BLOCKED": 0}
    source_citations: dict[str, list[str]] = {}
    for case in rows:
        case_id = case["id"]
        if set(case) != FIELDS:
            raise ValueError(f"{case_id}: revised case fields incomplete")
        if case["determination"] != EXPECTED[case_id]:
            raise ValueError(f"{case_id}: approved-review determination silently changed")
        counts[case["determination"]] += 1
        if case_id.startswith("X"):
            if case["review_055_status"] != "NEW_CROSS_FAMILY_CASE":
                raise ValueError(f"{case_id}: missing cross-family origin")
        elif case["review_055_status"] != (
            "AMEND_PRECONDITION_OR_CONCLUSION" if case_id in AMENDED
            else "CONFIRMED_AS_STATED"
        ):
            raise ValueError(f"{case_id}: loss of independent per-case decision")
        if not isinstance(case["gate"], str) or case["gate"] not in GATES:
            raise ValueError(f"{case_id}: invalid gate identity")
        if case_id.startswith("S") and case["gate"] != GATES[int(case_id[1])-1]:
            raise ValueError(f"{case_id}: unrelated gate mapping")
        if case_id.startswith("X") and not case["gate"]:
            raise ValueError(f"{case_id}: lost cross-family home gate")
        refs = case["source_basis"]
        if not isinstance(refs, list) or len(refs) < 2 or len(refs) != len(set(refs)):
            raise ValueError(f"{case_id}: missing or duplicate source references")
        for ref in refs:
            if not SOURCE_REF.fullmatch(ref) or ref not in src_ids:
                raise ValueError(f"{case_id}: unsupported exact source unit {ref}")
            source_citations.setdefault(ref, []).append(case_id)
        if case["claim_scope"] not in {"EVENT_OR_ARM_EVIDENCE_ONLY", "CONDITIONAL_ATTEMPT_CLASS"}:
            raise ValueError(f"{case_id}: false whole-attempt score scope")
        if not isinstance(case["premises"], dict) or set(case["premises"]) != PREMISES:
            raise ValueError(f"{case_id}: unknown/absent scorer premises")
        if not all(isinstance(v,str) and v.strip() for v in case["premises"].values()):
            raise ValueError(f"{case_id}: empty flag, origin, other-arm or evidence premise")
        if case["claim_scope"] == "CONDITIONAL_ATTEMPT_CLASS":
            if case["premises"]["raw_flags"] == "NO_SILENT_INFERENCE":
                raise ValueError(f"{case_id}: conditional whole-attempt class has no flag premise")
        if case["determination"] == "CANDIDATE_BLOCKED":
            if not isinstance(case["blocked_reason"], str) or len(case["blocked_reason"].strip()) < 35:
                raise ValueError(f"{case_id}: unresolved case lacks explicit blocked reason")
        elif case["blocked_reason"] is not None:
            raise ValueError(f"{case_id}: source-determined case uses unsupported blocked reason")
        for key in (
            "conditions", "source_grounded_conclusion", "f1_evidence_or_test",
            "qualification_boundary", "owner_policy_interpretation", "f1_decision_record",
        ):
            if not isinstance(case[key], str) or len(case[key].strip()) < 9:
                raise ValueError(f"{case_id}: empty normative case content or decision state")
        if case["owner_policy_interpretation"] != "NOT_REQUESTED_NO_OWNER_POLICY_CHANGE":
            raise ValueError(f"{case_id}: unapproved policy interpretation embedded")
    if counts != {"SOURCE_DETERMINED": 17, "CANDIDATE_BLOCKED": 7}:
        raise ValueError("REV02 review category totals changed")
    original = {row["unit_id"] for row in register["pending"] if any(
        code in row["blocker"] for code in GATES)}
    coverage = revision["open_gate_pending_coverage"]
    if len(coverage) != len(original) or len(original) != 18:
        raise ValueError("18 open scoring-gate source rows not preserved")
    if {x["unit_id"] for x in coverage} != original or len({x["unit_id"] for x in coverage})!=len(coverage):
        raise ValueError("missing or extra original scoring-gate pending source")
    for row in coverage:
        ids = sorted(source_citations.get(row["unit_id"], []))
        if sorted(row["case_ids"]) != ids:
            raise ValueError(f"source pending/case references not reconciled for {row['unit_id']}")
        if row["resolution"] not in {"CITED_PENDING_F1_REVIEW", "DEFERRED_F1_SOURCE_SITE_OR_RECEIPT_DESIGN"}:
            raise ValueError("silently approved reviewer pending unit")
        if not isinstance(row["reason"],str) or len(row["reason"]) < 55:
            raise ValueError("missing explicit pending reviewer deferral reason")
        if row["resolution"] == "CITED_PENDING_F1_REVIEW" and not ids:
            raise ValueError("claimed cited source unit has no associated case")
        if row["resolution"] != "CITED_PENDING_F1_REVIEW" and ids:
            raise ValueError("deferred despite explicit scenario citations")
    for needed in (
        "V01_CONTRACT-L0223", "V01_CONTRACT-L0231",
        "REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.outcome",
        "REV04_POLICY:webauthn_assertion_failure_table.NotSupportedError.proof_viability_receipt",
    ):
        if needed not in source_citations:
            raise ValueError(f"crucial B05 inherited source uncited: {needed}")
    if register["audit_summary"]["pending_units"] != 55 or any(
        x["task_owner_resolution"] != "UNRESOLVED" for x in register["pending"]):
        raise ValueError("independent reviewer pending findings not preserved")
    return {"scenarios":len(rows),"determinations":counts,"pending_gate_sources":len(original),"cited_gate_sources":sum(bool(x["case_ids"]) for x in coverage)}


def validate() -> dict:
    catalogue = json.loads(REV02.read_text(encoding="utf-8"))
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    register = pending.manifest(ROOT)
    return validate_payload(catalogue, inventory, register)


if __name__ == "__main__":
    result=validate()
    print("R0_P01_F1_SCORING_REV02_SOURCE_GUARD=PASS cases=%d determined=%d blocked=%d pending_gate_units=%d cited=%d" % (
        result["scenarios"],result["determinations"]["SOURCE_DETERMINED"],
        result["determinations"]["CANDIDATE_BLOCKED"],
        result["pending_gate_sources"],result["cited_gate_sources"],
    ))
    print("INTERPRETATION_APPROVAL=NOT_GIVEN; B01_B02=UNCHANGED; F1_F2=UNFROZEN; ATTEMPT_002=NOT_AUTHORIZED")
