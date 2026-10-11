"""Review-boundary guard for R0-P01 F1 site/receipt decision candidates.

Pins every reviewed REV02 scenario's semantic text and premise values to the
independently reviewed historical Git blob. Validates exact coverage of seven
Q qualifications and seven originally blocked source cases. Candidate table
is NOT an executable scoring oracle or human B01/B02 amendment.

This check intentionally fails when a reviewed scenario changes even when an
accompanying local pin file is simultaneously rewritten: the historical Git
object at the fixed reviewer-approved source commit is also read and checked.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

try:
    from scripts.check_r0_p01_scoring_boundary_rev02 import ROOT, INVENTORY, REV02, EXPECTED
except ModuleNotFoundError:
    from check_r0_p01_scoring_boundary_rev02 import ROOT, INVENTORY, REV02, EXPECTED

PINS = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_REVIEWED_REV02_CASE_PINS_V01_UNFROZEN.json"
SITE = ROOT / "docs/research/r0_p01_successor_design/R0_P01_F1_TECHNICAL_SITE_RECEIPT_DECISIONS_REV01_UNFROZEN.json"
COMMIT = "41e8b0c3af10f789a24e8c708a3a2ad11c990fee"
BLOCKED = {"S1-04", "S1-05", "S2-03", "S3-03", "X1", "X3", "X4"}
REQUIRED_Q = {f"Q{i}" for i in range(1, 8)}
SITE_IDS = {f"D{i:02}" for i in range(1, 16)}
RECEIPT_FIELDS = {
    "id","qualification","scenario_ids","site","phase","predicate",
    "evidence_required","source_basis","decision_if_proven","unproven_or_exception",
    "expected_class","decision_status","owner_action",
}
REVIEWED_FIELDS = ["conditions","source_grounded_conclusion","qualification_boundary","premises","source_basis"]
ALLOWED_STATUSES = {
    "BLOCKED_NATIVE_WINDOWS_TEST","CANDIDATE_TECHNICAL_REVIEW",
    "NEEDS_INDEPENDENT_TECHNICAL_DECISION",
}
SENSITIVE_BLOCKERS = {"D01","D04","D05","D06","D09","D10","D11","D12","D13","D15"}
REQUIRED_SITES = {
    "D01":"SSH_NATIVE_CTRLC_INVOCATION",
    "D02":"WEBAUTHN_RP_TIMEOUT_NO_CLIENT_INVOCATION",
    "D03":"WEBAUTHN_CONSUMED_NOTALLOWED_AFTER_CLIENT_GET",
    "D04":"WEBAUTHN_NOTSUPPORTED_POST_VERIFIED_REGISTRATION",
    "D05":"WEBAUTHN_SETUP_CAPABILITY_RECEIPT",
    "D06":"OPENSSH_PINNED_RUNTIME_REPLACED_AFTER_CLAIM",
    "D07":"SSH_PROCESS_CREATION_FAILURE",
    "D08":"SSH_PROCESS_STARTED_MISSING_DLL_NONZERO",
    "D09":"SSH_AGENT_LOADED_BEFORE_P0",
    "D10":"SSH_PRIVATE_KEY_PASSPHRASE_REENCRYPTION",
    "D11":"SSH_BUDGET_NORMAL_THREE_INVOCATIONS",
    "D12":"SNAPSHOT_PROMOTION_CRASH_ATOMICITY",
    "D13":"RP_OWNER_ABORT_NODE_EXIT_UNORDERABLE",
    "D14":"WEBAUTHN_LATE_SUCCESS_AFTER_HARNESS_STOP",
    "D15":"G2_UNCONTESTED_SELECTION_FALSE_CAPABILITY",
}


def canonical_case_bytes(case: dict, fields: list[str]) -> bytes:
    selected = {name: case[name] for name in fields}
    return json.dumps(
        selected, sort_keys=True, separators=(",",":"), ensure_ascii=False
    ).encode("utf-8")


def historical_blob(root: Path, revision: str, rel: str) -> bytes:
    result = subprocess.run(
        ["git","show",f"{revision}:{rel}"],cwd=root,stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,timeout=15,check=False,
    )
    if result.returncode:
        raise ValueError(f"cannot verify independently reviewed source Git blob {rel}")
    return result.stdout


def validate_payload(pins: dict, rev02: dict, table: dict, inventory: dict, historical: bytes) -> dict:
    """Structural assurances only; textual meaning requires independent review."""
    if pins["version"] != 1 or pins["reviewed_commit"] != COMMIT:
        raise ValueError("reviewed provenance commit changed")
    if pins["reviewer_message"] != "MC-0030_MESSAGE057":
        raise ValueError("peer review identity lost")
    if pins["canonical_fields"] != REVIEWED_FIELDS:
        raise ValueError("canonical text fields changed")
    if pins["committed_git_blob_sha256"] != hashlib.sha256(historical).hexdigest():
        raise ValueError("historical Git blob digest changed")
    source = json.loads(historical.decode("utf-8"))
    if source["schema_version"] != 2 or len(source["cases"]) != 24:
        raise ValueError("historical source no longer known reviewer draft")
    reviewed = {x["id"]: x for x in source["cases"]}
    current = {x["id"]: x for x in rev02["cases"]}
    if set(reviewed) != set(EXPECTED) or set(current) != set(EXPECTED):
        raise ValueError("reviewed scenario roster drift")
    if set(pins["pinned_case_sha256"]) != set(EXPECTED) or set(pins["case_premises_exact"]) != set(EXPECTED):
        raise ValueError("reviewed case pin set incomplete")
    for key in sorted(EXPECTED):
        original=reviewed[key]
        current_row=current[key]
        actual=hashlib.sha256(canonical_case_bytes(original,REVIEWED_FIELDS)).hexdigest()
        if pins["pinned_case_sha256"][key]!=actual:
            raise ValueError(f"{key}: stored semantic hash not grounded in independently reviewed Git source")
        if hashlib.sha256(canonical_case_bytes(current_row,REVIEWED_FIELDS)).hexdigest()!=actual:
            raise ValueError(f"{key}: source meaning changed without new independent review")
        if pins["case_premises_exact"][key]!=original["premises"] or current_row["premises"]!=original["premises"]:
            raise ValueError(f"{key}: original premise values or enumeration drift")
    if table["schema_version"]!=1 or table["status"]!="UNFROZEN_SOURCE_SITE_AND_RECEIPT_DECISION_CANDIDATES":
        raise ValueError("table prematurely claims qualification")
    if table["approved_sources"]!={"contract":"9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175",
                                   "policy":"9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c"}:
        raise ValueError("human-accepted source identity drift")
    if table["review_anchor"]!="MC-0030_MESSAGE057_ACCEPT_REV02_WITH_PRECISE_QUALIFICATIONS":
        raise ValueError("review 057 acceptance missing")
    if set(table["qualifications"])!=REQUIRED_Q or len(table["qualifications"])!=7:
        raise ValueError("missing Q1-Q7")
    if set(table["blocked_rev02_cases"])!=BLOCKED or len(table["blocked_rev02_cases"])!=7:
        raise ValueError("original seven blocked cases misrepresented")
    if table["owner_policy_interpretation"]!="NONE_CURRENTLY_REQUIRED":
        raise ValueError("unapproved owner interpretation")
    if table["completion"]!="REQUIRES_INDEPENDENT_SOURCE_AND_POLICY_REVIEW_BEFORE_SEVEN_CLASS_VECTORS":
        raise ValueError("claimed oracle qualification")
    if table["F1_frozen"] or table["F2_frozen"] or table["attempt_002_authorized"]:
        raise ValueError("unauthorized owner trial or freeze")
    rows=table["rows"]
    if len(rows)!=15 or {x["id"] for x in rows}!=SITE_IDS:
        raise ValueError("closed source/site decision row set missing or duplicated")
    units={u["id"] for u in inventory["units"]}
    cites=set()
    qual=set()
    status_count={}
    for row in rows:
        if set(row)!=RECEIPT_FIELDS:
            raise ValueError(f"{row['id']}: missing closed site/receipt fields")
        if row["site"]!=REQUIRED_SITES[row["id"]]:
            raise ValueError(f"{row['id']}: essential source site changed")
        if row["decision_status"] not in ALLOWED_STATUSES:
            raise ValueError(f"{row['id']}: draft technical status no longer controlled")
        status_count[row["decision_status"]]=status_count.get(row["decision_status"],0)+1
        qs=row["qualification"]
        ids=row["scenario_ids"]
        refs=row["source_basis"]
        evidence=row["evidence_required"]
        if not (isinstance(qs,list) and qs and set(qs)<=REQUIRED_Q and
                isinstance(ids,list) and ids and set(ids)<=set(EXPECTED) and
                isinstance(refs,list) and len(refs)>=2 and
                isinstance(evidence,list) and len(evidence)>=2):
            raise ValueError(f"{row['id']}: missing Q, scenario, source or evidence premise")
        if any(ref not in units for ref in refs):
            raise ValueError(f"{row['id']}: unsupported frozen source-unit reference")
        if row["id"] in SENSITIVE_BLOCKERS and row["decision_status"]=="CANDIDATE_TECHNICAL_REVIEW":
            raise ValueError(f"{row['id']}: unreviewed scoring-sensitive site silently cleared")
        if row["expected_class"] in {"PASS", "REOPEN"}:
            raise ValueError(f"{row['id']}: cannot claim an unconditional whole-attempt outcome")
        for k in ["predicate","decision_if_proven","unproven_or_exception","owner_action","expected_class","phase"]:
            if not isinstance(row[k],str) or (len(row[k].strip())<8 and not (k=="owner_action" and row[k]=="NONE")):
                raise ValueError(f"{row['id']}: missing concrete conditional {k}")
        qual.update(qs)
        cites.update(ids)
    if qual!=REQUIRED_Q or not BLOCKED<=cites:
        raise ValueError("Q1-Q7 or seven blocked scenario rows not comprehensively traced")
    return {"source_pins":len(EXPECTED),"candidate_site_rows":len(rows),"qualifications":len(qual),
            "blocked_scenarios":len(BLOCKED),"site_statuses":status_count}


def validate() -> dict:
    pins=json.loads(PINS.read_text(encoding="utf-8"))
    rev02=json.loads(REV02.read_text(encoding="utf-8"))
    table=json.loads(SITE.read_text(encoding="utf-8"))
    inventory=json.loads(INVENTORY.read_text(encoding="utf-8"))
    source=historical_blob(ROOT,COMMIT,pins["source_path"])
    return validate_payload(pins,rev02,table,inventory,source)


if __name__=="__main__":
    report=validate()
    print("R0_P01_F1_SITE_DECISIONS=PASS reviewed_pins=%d site_rows=%d Q=%d blocked_cases=%d" % (
        report["source_pins"],report["candidate_site_rows"],report["qualifications"],report["blocked_scenarios"],
    ))
    print("SEMANTIC_APPROVAL=PEER_REVIEW_REQUIRED; F1_F2=UNFROZEN; OWNER_ATTEMPT_002=NOT_AUTHORIZED")
