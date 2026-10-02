import copy, hashlib, json, sys
from pathlib import Path

EXPECTED_OWNERS={
    "SP3-A":"governance-development",
    "SP3-B":"project-system-verification",
    "SP3-C":"domain-contract-integration",
}
EXPECTED_SCOPE="OPERATIVE-V0.2"

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def validate_realizer(root, reqs, r):
    clauses={x["clause_ref"]:x for x in reqs["requirements"]}
    if r["realizer_id"] not in EXPECTED_OWNERS:
        return False
    if r["realizer_owner"] != EXPECTED_OWNERS[r["realizer_id"]]:
        return False
    if r["scope_ref"] != EXPECTED_SCOPE:
        return False
    artifact=Path(root)/r["artifact_ref"]
    if not artifact.is_file() or digest(artifact) != r["artifact_sha256"]:
        return False
    if not r["realizes"]:
        return False
    for edge in r["realizes"]:
        c=clauses.get(edge["clause_ref"])
        if c is None or not c["active"]:
            return False
        if c["scope_ref"] != r["scope_ref"]:
            return False
        if edge["coverage_mode"] not in {"FULL","PARTIAL"}:
            return False
    return True

def mutate(base, mutation):
    r=copy.deepcopy(base)
    if "artifact_sha256" in mutation:
        r["artifact_sha256"]=mutation["artifact_sha256"]
    if "realizer_owner" in mutation:
        r["realizer_owner"]=mutation["realizer_owner"]
    if "scope_ref" in mutation:
        r["scope_ref"]=mutation["scope_ref"]
    if "clause_ref" in mutation:
        r["realizes"][0]["clause_ref"]=mutation["clause_ref"]
    return r

if __name__=="__main__":
    root=Path(sys.argv[1])
    req=json.load(open(root/"requirements.json",encoding="utf-8"))
    dec=json.load(open(root/"realizer_declarations.json",encoding="utf-8"))
    neg=json.load(open(root/"coverage_negative_controls.json",encoding="utf-8"))
    positives={r["realizer_id"]:validate_realizer(root,req,r) for r in dec["realizers"]}
    byid={r["realizer_id"]:r for r in dec["realizers"]}
    negatives={}
    for c in neg["controls"]:
        candidate=mutate(byid[c["base_realizer"]],c["mutation"])
        negatives[c["id"]]=validate_realizer(root,req,candidate)
    print(json.dumps({"positives":positives,"negatives":negatives},sort_keys=True))
