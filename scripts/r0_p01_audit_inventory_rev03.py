"""Read-only F1 normative-surface audit inventory, not a semantic approval engine.

Source extraction uses exact committed Git blobs. Included normative surfaces:
* Approved V03 REV04 contract sections 1..11 and approved policy normative roots
* Frozen V02 addendum sections 2..19
* Frozen V02 control definitions sections 1..14
* Frozen V01 implementation contract sections 1..15
* All fixture.json and result_contract.json leaf nodes

Every extracted source unit is REVIEW_PENDING. The reviewer must individually
classify inherited units as INHERITED_UNCHANGED, SUPERSEDED_BY_REV04 (with an
exact superseding unit), or NOT_APPLICABLE_TO_SUCCESSOR (with a reason).
No automatically inferred semantic mapping can be labelled APPROVED.
"""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
FILES = {
    "REV04_CONTRACT": "docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md",
    "REV04_POLICY": "docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json",
    "V02_ADDENDUM": "experiments/r0_p01_owner_acceptance_v01/implementation_contract_addendum_v02.md",
    "V01_CONTROLS": "experiments/r0_p01_owner_acceptance_v01/security_control_contract.md",
    "V01_CONTRACT": "experiments/r0_p01_owner_acceptance_v01/implementation_contract.md",
    "V01_FIXTURE": "experiments/r0_p01_owner_acceptance_v01/fixture.json",
    "V01_RESULT": "experiments/r0_p01_owner_acceptance_v01/result_contract.json",
}
SECTIONS = {
    "REV04_CONTRACT": set(range(1, 12)),
    "V02_ADDENDUM": set(range(2, 20)),
    "V01_CONTROLS": set(range(1, 15)),
    "V01_CONTRACT": set(range(1, 16)),
}
HDR = re.compile(r"^## (\d+)\.")
SUBHDR = re.compile(r"^### ")
LIST = re.compile(r"^\s*(?:[-*]|\d+\.)\s")
FENCE = chr(96) * 3
# Review of the normative status of each top-level key is itself mandatory.
POLICY_NORMATIVE = set((
    "predecessor", "claim_cap", "unchanged_eligibility", "run_dispositions",
    "primary_scored_classifications", "cases", "forbidden",
    "invalid_reason_subclasses", "processing_states", "guards",
    "scorer_identity_interpretation", "raw_flag_schema", "evidence_state",
    "attempt_terminal_vs_event_terminal", "snapshot_evidence",
    "browser_node_interrupt", "reporting", "webauthn_assertion_failure_table",
    "evidence_disclosures", "rejection_layer_values",
    "preclaim_browser_forbidden_scan_scope", "old_digest_set_scope",
    "synthetic_webauthn_test",
))
POLICY_NON_NORMATIVE = {
    "schema":"static schema identifier; reviewed version boundary still applies",
    "status":"historical drafting status before owner acceptance",
    "authority":"historical drafting-state attribution",
    "related_contract":"source pointer, with exact content hashed elsewhere",
    "draft_date":"document drafting metadata",
    "successor_proposal":"predecision lifecycle proposal; operational attempt claims governed elsewhere",
    "freeze_authorized":"historical unapproved freeze flag, never mutated retroactively",
    "owner_execution_authorized":"historical unapproved owner execution flag",
    "draft_revision":"document revision identity",
    "review_disposition":"historical design-review status",
    "unresolved_blockers":"historical design progress, not executable security predicate",
    "owner_stopping_policy_approved":"historical pre-B02 decision Boolean",
    "optional_nonbinding_diagnostics":"explicitly nonbinding output suggestion, no scoring authority",
}
assert not (POLICY_NORMATIVE & set(POLICY_NON_NORMATIVE))

def committed(root: Path, relative: str) -> bytes:
    """Use committed Git blob bytes without Windows CRLF checkout conversion."""
    return subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=root)

def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()

def decode_json(raw: bytes) -> Any:
    def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key: {key}")
            result[key] = value
        return result
    return json.loads(raw, object_pairs_hook=unique)

def _unit(label: str, source_id: str, text: str, **extra: Any) -> dict[str, Any]:
    """Construct a reviewer-owned source unit with exact text digest."""
    return {
        "id": label,
        "source_id": source_id,
        "text_sha256": digest(text.encode("utf-8")),
        "excerpt": text[:200],
        "candidate_requirement_ids": [],
        "review": {
            "status": "PENDING_INDEPENDENT_SEMANTIC_AUDIT",
            "reviewer": None,
            "review_message": None,
            "disposition": None,
            "reason": None,
            "superseded_by_unit": None,
            "approved_requirement_ids": [],
        },
        **extra,
    }

def markdown_units(source_id: str, raw: bytes) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Index all section contents without counting Markdown table syntax as duties."""
    lines = raw.decode("utf-8").splitlines()
    active: int | None = None
    heading = ""
    units = []
    exclusions = []
    previous_header = None
    i = 0
    include = SECTIONS[source_id]
    while i < len(lines):
        l = lines[i]
        section = HDR.match(l)
        if section:
            active = int(section.group(1))
            heading = l
            previous_header = None
            i += 1
            continue
        if l.startswith("#"):
            if active in include:
                heading = l
            i += 1
            continue
        if active not in include or not l.strip():
            if l.strip():
                exclusions.append({
                    "source_id":source_id, "line":i+1,
                    "reason":"OUTSIDE_SELECTED_NUMBERED_SECTIONS_REVIEW_REQUIRED",
                    "text_sha256":digest(l.encode("utf-8")),
                })
            i += 1
            continue
        start = i
        if l.startswith("|"):
            if i+1 < len(lines) and re.match(r"^\|\s*:?[-]{3,}", lines[i+1]):
                previous_header = l
                exclusions.append({"source_id":source_id,"line":i+1,"reason":"MARKDOWN_TABLE_HEADER_CONTEXT","text_sha256":digest(l.encode("utf-8"))})
                i += 1
                continue
            if re.match(r"^\|\s*:?[-]{3,}", l):
                exclusions.append({"source_id":source_id,"line":i+1,"reason":"MARKDOWN_TABLE_SEPARATOR_SYNTAX","text_sha256":digest(l.encode("utf-8"))})
                i += 1
                continue
            i += 1
        elif l.startswith(FENCE):
            i += 1
            while i < len(lines) and not lines[i].startswith(FENCE):
                i += 1
            if i >= len(lines):
                raise ValueError(f"{source_id}: unterminated fence line {start+1}")
            i += 1
        elif LIST.match(l):
            i += 1
            while i < len(lines) and lines[i].strip() and not LIST.match(lines[i]) and not lines[i].startswith(("#","|",FENCE)):
                i += 1
        else:
            i += 1
            while i < len(lines) and lines[i].strip() and not LIST.match(lines[i]) and not lines[i].startswith(("#","|",FENCE)):
                i += 1
        text = "\n".join(lines[start:i])
        u = _unit(
            f"{source_id}-L{start+1:04d}", source_id, text,
            section=active, heading_context=heading,
            line_start=start+1, line_end=i,
            header_context=previous_header if l.startswith("|") else None,
            inherited=source_id != "REV04_CONTRACT",
        )
        units.append(u)
    if len({u["id"] for u in units}) != len(units):
        raise ValueError(f"{source_id}: duplicated source IDs")
    return units, exclusions

def json_units(source_id: str, raw: bytes, policy: bool) -> tuple[list[dict[str, Any]], dict[str, str]]:
    """Index all JSON leaves; policy metadata exclusions are explicit."""
    data = decode_json(raw)
    if not isinstance(data, dict):
        raise ValueError("source JSON must be object")
    roots = set(data)
    classification = {}
    if policy:
        missing = (POLICY_NORMATIVE|set(POLICY_NON_NORMATIVE))-roots
        extra = roots-(POLICY_NORMATIVE|set(POLICY_NON_NORMATIVE))
        if missing or extra:
            raise ValueError(f"policy root registry mismatch missing={missing} extra={extra}")
        classification = {r:("NORMATIVE" if r in POLICY_NORMATIVE else "NON_NORMATIVE") for r in roots}
    else:
        classification = {r:"INHERITED_REVIEW_REQUIRED" for r in roots}
    result = []
    def walk(path: str, node: Any, norm: str) -> None:
        if isinstance(node, dict) and node:
            for k in sorted(node):
                walk(path+"."+k,node[k],norm)
        elif isinstance(node,list) and node:
            for ix,v in enumerate(node):
                walk(f"{path}[{ix}]",v,norm)
        else:
            encoded = json.dumps(node,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False)
            result.append(_unit(f"{source_id}:{path}",source_id,encoded,json_path=path,root_status=norm,inherited=not policy))
    for key in sorted(roots):
        # Intentionally index nonnormative metadata too so changing its presence
        # cannot silently turn it into a normative obligation.
        walk(key,data[key],classification[key])
    return result,classification

def inventory(root: Path = ROOT) -> dict[str, Any]:
    """Produce an F1 audit *candidate*, not a completed clause map."""
    units = []
    table_exclusions = []
    source_hashes = {}
    policy_status = {}
    for source_id, relative in FILES.items():
        raw = committed(root,relative)
        source_hashes[source_id] = digest(raw)
        if relative.endswith(".md"):
            items, excluded = markdown_units(source_id,raw)
            units.extend(items)
            table_exclusions.extend(excluded)
        else:
            items, statuses = json_units(source_id,raw,source_id=="REV04_POLICY")
            units.extend(items)
            if source_id=="REV04_POLICY":
                policy_status=statuses
    ids=[u["id"] for u in units]
    if len(set(ids))!=len(ids):
        raise ValueError("duplicate source unit across all inputs")
    return {
        "schema_version":1,
        "status":"UNFROZEN_INDEPENDENT_CLAUSE_AUDIT_PENDING",
        "approved_source_sha256":{
            "contract":"9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175",
            "policy":"9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c",
        },
        "sources":FILES,
        "source_sha256":source_hashes,
        "policy_root_classification":policy_status,
        "policy_non_normative_reason":POLICY_NON_NORMATIVE,
        "table_syntax_context_exclusions":table_exclusions,
        "units":units,
        "semantic_review_required":True,
        "F1_frozen":False,
        "F2_frozen":False,
        "owner_attempt_002_authorized":False,
    }
