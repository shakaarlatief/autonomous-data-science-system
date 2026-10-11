"""Static guard for prospective R0-P01 scoring-boundary scenario candidates.

The scenarios are a source-grounded F1 design and peer-review input, NOT a
qualified scoring oracle. The guard enforces exact approved-source hashes,
reviewer-hypothesis labels, referenced committed source-unit existence, and
scope. It deliberately does not infer which candidate semantic interpretation
should govern B01/B02 or prove a real owner run is safe.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOGUE = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_SCORING_BOUNDARY_CANDIDATES_REV01_UNFROZEN.json"
INVENTORY = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_NORMATIVE_AUDIT_INVENTORY_REV03_UNFROZEN.json"
GATES = ("B05-A1", "B07-A3", "B08-A1", "B11-A1")
FIELDS = (
    "id", "gate", "slug", "determination", "source_basis", "conditions",
    "source_grounded_conclusion", "f1_evidence_or_test", "qualification_boundary",
)
POLICY_REF = re.compile(r"^REV04_POLICY:.+$")
CONTRACT_REF = re.compile(r"^REV04_CONTRACT-L\d{4}$")


def validate_payload(catalogue: dict, inventory: dict, root: Path = ROOT) -> dict:
    """Fail if sources, scope, required fields, or case provenance drift."""
    if catalogue["schema_version"] != 1:
        raise ValueError("unsupported candidate catalogue version")
    if catalogue["status"] != "UNFROZEN_PROSPECTIVE_SOURCE_COMPARISON":
        raise ValueError("candidate catalogue claims unreviewed status change")
    if catalogue["gate_order"] != list(GATES):
        raise ValueError("gate order must preserve critical four")
    if catalogue["scenario_fields"] != list(FIELDS):
        raise ValueError("scenario field shape drift")
    if set(catalogue["determination_types"]) != {"SOURCE_DETERMINED", "CANDIDATE_BLOCKED"}:
        raise ValueError("unreviewed determination status")
    if catalogue["accepted_decisions"] != ["B01", "B02"]:
        raise ValueError("owner-approved B01/B02 source anchor drift")
    if catalogue["claude_audit_results"] != {
        "reviewed": 1022, "reviewer_accepted": 967, "reviewer_pending": 55,
    }:
        raise ValueError("Claude audit count provenance mismatch")
    allowed_sources = {
        "contract": "docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md",
        "policy": "docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json",
    }
    for role, rel in allowed_sources.items():
        if catalogue[f"source_{role}"] != rel:
            raise ValueError(f"unexpected contract/policy source {role}")
        actual_sha = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if catalogue["approved_source_sha256"][role] != actual_sha:
            raise ValueError(f"source byte hash changed {role}")
        if inventory["approved_source_sha256"][role] != actual_sha:
            raise ValueError(f"inventory/source mismatch {role}")
    source_ids = {x["id"] for x in inventory["units"]}
    seen: set[str] = set()
    per_gate = {k: 0 for k in GATES}
    per_disposition = {k: 0 for k in catalogue["determination_types"]}
    for case in catalogue["cases"]:
        if set(case) != set(FIELDS):
            raise ValueError(f"scenario field mismatch: {case.get('id')}")
        identity = case["id"]
        if not re.fullmatch(r"S[1-4]-\d{2}", identity) or identity in seen:
            raise ValueError("duplicate or malformed scenario identity")
        seen.add(identity)
        if case["gate"] not in GATES or identity[1] != str(GATES.index(case["gate"]) + 1):
            raise ValueError("scenario family/gate mismatch")
        per_gate[case["gate"]] += 1
        status = case["determination"]
        if status not in per_disposition:
            raise ValueError("unreviewed determination")
        per_disposition[status] += 1
        for field in FIELDS:
            if field != "source_basis" and (not isinstance(case[field], str) or not case[field].strip()):
                raise ValueError(f"scenario field empty {identity}:{field}")
        refs = case["source_basis"]
        if not isinstance(refs, list) or len(refs) < 2 or len(refs) != len(set(refs)):
            raise ValueError("each scenario needs at least two distinct source anchors")
        for ref in refs:
            if not (CONTRACT_REF.fullmatch(ref) or POLICY_REF.fullmatch(ref)):
                raise ValueError(f"invalid source ref {ref}")
            if ref not in source_ids:
                raise ValueError(f"uncaptured source ref {ref}")
        if status == "CANDIDATE_BLOCKED" and "unresolved" not in (
            case["source_grounded_conclusion"]+" "+case["qualification_boundary"]+
            " "+case["f1_evidence_or_test"]
        ).lower() and not any(t in (
            case["source_grounded_conclusion"]+" "+case["qualification_boundary"]+
            " "+case["f1_evidence_or_test"]
        ).lower() for t in ("not approved", "cannot", "require", "blocked")):
            raise ValueError("candidate insufficiently marked as blocked")
    if len(seen) < 12 or any(v < 3 for v in per_gate.values()) or per_disposition["CANDIDATE_BLOCKED"] < 4:
        raise ValueError("insufficient cross-boundary scenario coverage")
    if "NOT approved F1 oracle" not in catalogue["authority"]:
        raise ValueError("missing explicit non-approval marker")
    return {"scenario_count": len(seen), "per_gate": per_gate, "determinations": per_disposition}


def validate() -> dict:
    catalogue = json.loads(CATALOGUE.read_text(encoding="utf-8"))
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    return validate_payload(catalogue, inventory)


if __name__ == "__main__":
    result = validate()
    print("R0_P01_SCORING_BOUNDARY_CANDIDATES=PASS scenarios=%d gates=%d source_determined=%d candidate_blocked=%d" % (
        result["scenario_count"], len(GATES),
        result["determinations"]["SOURCE_DETERMINED"],
        result["determinations"]["CANDIDATE_BLOCKED"],
    ))
    print("SEMANTIC_APPROVAL=NOT_GIVEN; B01_B02=IMMUTABLE; F1_F2=UNFROZEN; ATTEMPT_002=NOT_AUTHORIZED")
