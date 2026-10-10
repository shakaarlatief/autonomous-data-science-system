"""Read-only deterministic inventory of the human-approved P01 REV04 clauses.

Contract sections 1..11 are split into line-indexed paragraphs, table rows,
list items, and fenced blocks. All leaf paths below the policy's normative
roots are indexed. Mapping these units to requirements needs peer review;
mechanical completeness does not establish semantic coverage.
"""
from __future__ import annotations
import hashlib
import json
import re
import subprocess
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md"
POLICY = "docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json"
POLICY_ROOTS = (
 "claim_cap","guards","evidence_state","raw_flag_schema",
 "attempt_terminal_vs_event_terminal","snapshot_evidence",
 "browser_node_interrupt","reporting","webauthn_assertion_failure_table",
 "evidence_disclosures","cases","unchanged_eligibility",
 "rejection_layer_values","preclaim_browser_forbidden_scan_scope",
 "old_digest_set_scope","synthetic_webauthn_test",
)
HDR = re.compile(r"^## (\d+)\.")
SUBHDR = re.compile(r"^### ([0-9]+(?:\.[0-9]+)?)")
LIST = re.compile(r"^(?:\s*\d+\.|\s*[-*])\s")
FENCE = chr(96) * 3

def blob(root: Path, name: str) -> bytes:
    """Hash committed Git blobs, never CRLF-transformed working-tree bytes."""
    if name.startswith("/") or "\\" in name or ".." in Path(name).parts:
        raise ValueError("unsafe source name")
    return subprocess.check_output(["git","show",f"HEAD:{name}"],cwd=root)

def h(value: Any) -> str:
    if isinstance(value,str): raw=value.encode("utf-8")
    else: raw=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(",",":"),allow_nan=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()

def contract_units(data: bytes) -> list[dict[str,Any]]:
    lines=data.decode("utf-8").splitlines()
    result=[]
    sec=None;sub=None;i=0
    while i<len(lines):
        line=lines[i]
        m=HDR.match(line)
        if m:
            sec=int(m.group(1));sub=None;i+=1;continue
        m=SUBHDR.match(line)
        if m:sub=m.group(1);i+=1;continue
        if sec not in range(1,12) or not line.strip() or line.startswith("#"):
            i+=1;continue
        start=i
        if line.startswith(FENCE):
            i+=1
            while i<len(lines) and not lines[i].startswith(FENCE):i+=1
            if i>=len(lines):raise ValueError("unclosed fenced block")
            i+=1
        elif line.startswith("|"):
            i+=1
        elif LIST.match(line):
            i+=1
            while i<len(lines) and lines[i].strip() and not LIST.match(lines[i]) and not lines[i].startswith(("#","|",FENCE)):i+=1
        else:
            i+=1
            while i<len(lines) and lines[i].strip() and not LIST.match(lines[i]) and not lines[i].startswith(("#","|",FENCE)):i+=1
        piece="\n".join(lines[start:i])
        result.append({"unit_id":f"CONTRACT-L{start+1:04d}","source":"contract","section":str(sec),"subsection":sub,"line_start":start+1,"line_end":i,"source_sha256":h(piece),"excerpt":piece[:200]})
    if len({x["unit_id"] for x in result})!=len(result):raise ValueError("duplicate contract unit")
    return result

def policy_units(data:bytes) -> list[dict[str,Any]]:
    def distinct(pairs):
        o={}
        for k,v in pairs:
            if k in o:raise ValueError("duplicate policy JSON key")
            o[k]=v
        return o
    doc=json.loads(data,object_pairs_hook=distinct)
    result=[]
    def walk(path,value):
        if isinstance(value,dict) and value:
            for k in sorted(value):walk(path+"."+k,value[k])
        elif isinstance(value,list) and value:
            for i,v in enumerate(value):walk(f"{path}[{i}]",v)
        else:
            result.append({"unit_id":"POLICY-"+path,"source":"policy","json_path":path,"source_sha256":h(value),"excerpt":repr(value)[:200]})
    for root in POLICY_ROOTS:
        if root not in doc:raise ValueError("policy normative root missing: "+root)
        walk(root,doc[root])
    if len({x["unit_id"] for x in result})!=len(result):raise ValueError("duplicate policy path")
    return result

def source_units(root:Path=ROOT)->list[dict[str,Any]]:
    return contract_units(blob(root,CONTRACT))+policy_units(blob(root,POLICY))
