from __future__ import annotations

import argparse
import difflib
import json
import re
from itertools import combinations
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm_tokens(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def similarity(a: str, b: str) -> float:
    ta, tb = norm_tokens(a), norm_tokens(b)
    j = len(ta & tb) / len(ta | tb) if (ta | tb) else 1.0
    s = difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()
    return max(j, s)


def derive_state(facts: dict) -> str:
    if facts["deferral_refs"]:
        return "DEFERRED"
    if not facts["realization_relation_refs"]:
        return "UNLINKED"
    if not facts["evidence_refs"]:
        return "LINKED"
    if not facts["qualification_refs"]:
        return "EVIDENCED"
    if not facts["activation_refs"]:
        return "QUALIFIED"
    return "OPERATIONAL"


def validate_annotation(ann, scope, defs, schema):
    errors=[]
    for k in schema["required_top"]:
        if k not in ann: errors.append(f"missing top field {k}")
    if ann.get("base") != scope["base"]:
        errors.append("base mismatch")
    expected=[x["path"] for x in scope["primary_sources"]]
    got=[x.get("source_path") for x in ann.get("source_annotations",[])]
    if got != expected:
        errors.append("source annotations must exactly match frozen source order")
        return errors
    role_by_path={x["path"]:x["role"] for x in scope["primary_sources"]}
    info_by_path={x["path"]:x for x in scope["primary_sources"]}
    prop_ids=set()
    unit_ids=set()
    for sa in ann["source_annotations"]:
        p=sa["source_path"]
        if sa.get("source_role") != role_by_path[p]:
            errors.append(f"{p}: source_role mismatch")
        if role_by_path[p]=="NEGATIVE_CONTROL" and sa.get("obligation_units") and sa.get("creates_no_obligation_units"):
            errors.append(f"{p}: negative control cannot both create units and assert none")
        allowed=info_by_path[p].get("allowed_headings")
        all_headings=set(info_by_path[p].get("headings",[]))
        for unit in sa.get("obligation_units",[]):
            uid=f"{p}::{unit.get('unit_id')}"
            if uid in unit_ids: errors.append(f"duplicate unit id {uid}")
            unit_ids.add(uid)
            anchor=unit.get("source_anchor")
            if anchor not in all_headings:
                errors.append(f"{uid}: source_anchor not an exact frozen heading")
            if allowed is not None and anchor not in allowed:
                errors.append(f"{uid}: source_anchor outside allowed review scope")
            for req in schema["obligation_unit_required"]:
                if req not in unit: errors.append(f"{uid}: missing {req}")
            facts=unit.get("realization_facts",{})
            for req in schema["realization_facts_required"]:
                if req not in facts or not isinstance(facts.get(req),list):
                    errors.append(f"{uid}: invalid/missing facts {req}")
            for prop in unit.get("propositions",[]):
                for req in schema["proposition_required"]:
                    if req not in prop: errors.append(f"{uid}: proposition missing {req}")
                pid=f"{p}::{prop.get('proposition_id')}"
                if pid in prop_ids: errors.append(f"duplicate proposition id {pid}")
                prop_ids.add(pid)
                if not str(prop.get("statement","")).strip():
                    errors.append(f"{pid}: blank proposition")
        if not sa.get("obligation_units") and not sa.get("creates_no_obligation_units"):
            errors.append(f"{p}: zero units requires explicit creates_no_obligation_units")
    return errors


def flatten(ann):
    out=[]
    for sa in ann["source_annotations"]:
        for unit in sa["obligation_units"]:
            for prop in unit["propositions"]:
                out.append({
                    "source_path":sa["source_path"],
                    "anchor":unit["source_anchor"],
                    "unit_id":unit["unit_id"],
                    "prop_id":prop["proposition_id"],
                    "statement":prop["statement"],
                    "state":derive_state(unit["realization_facts"]),
                    "witness_tags":unit["witness_tags"],
                })
    return out


def match_props(a,b,threshold):
    candidates=[]
    for i,pa in enumerate(a):
        for j,pb in enumerate(b):
            if pa["source_path"]!=pb["source_path"] or pa["anchor"]!=pb["anchor"]:
                continue
            score=similarity(pa["statement"],pb["statement"])
            if score>=threshold:
                candidates.append((score,i,j))
    candidates.sort(reverse=True)
    used_a=set(); used_b=set(); matches=[]
    for score,i,j in candidates:
        if i in used_a or j in used_b: continue
        used_a.add(i); used_b.add(j); matches.append((i,j,score))
    return matches


def f1_from_matches(n_a,n_b,m):
    return (2*m/(n_a+n_b)) if (n_a+n_b) else 1.0


def grouping_f1(a,b,matches):
    # Only matched propositions can be compared for grouping agreement.
    labels_a=[]; labels_b=[]
    for (x,(ia,ib,_)), (y,(ja,jb,_)) in combinations(enumerate(matches),2):
        if a[ia]["source_path"] != a[ja]["source_path"]:
            continue
        labels_a.append(a[ia]["unit_id"]==a[ja]["unit_id"])
        labels_b.append(b[ib]["unit_id"]==b[jb]["unit_id"])
    if not labels_a:
        return 1.0
    tp=sum(x and y for x,y in zip(labels_a,labels_b))
    fp=sum(x and not y for x,y in zip(labels_a,labels_b))
    fn=sum((not x) and y for x,y in zip(labels_a,labels_b))
    if tp==fp==fn==0:
        return 1.0
    return 2*tp/(2*tp+fp+fn)


def witness_set(ann):
    return {tag for sa in ann["source_annotations"] for u in sa["obligation_units"] for tag in u["witness_tags"]}


def find_control_state(flat,control,threshold=0.45):
    best=None
    for p in flat:
        if p["source_path"]!=control["source_path"] or p["anchor"]!=control["source_anchor"]:
            continue
        score=similarity(p["statement"],control["match_text"])
        if best is None or score>best[0]:
            best=(score,p)
    if best is None or best[0] < threshold:
        return None
    return best[1]["state"]


def false_gap_rate(flat,key):
    results=[]
    for c in key["false_gap_controls"]:
        state=find_control_state(flat,c)
        false_gap = state != "OPERATIONAL"
        results.append({"id":c["id"],"derived_state":state,"false_gap":false_gap})
    rate=sum(x["false_gap"] for x in results)/len(results)
    return rate,results


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--annotation-a",required=True)
    ap.add_argument("--annotation-b",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()

    scope=load(ROOT/"review_scope.json")
    defs=load(ROOT/"definitions.json")
    schema=load(ROOT/"annotation_schema.json")
    key=load(ROOT/"evaluator_key.json")
    a=load(Path(args.annotation_a)); b=load(Path(args.annotation_b))

    ea=validate_annotation(a,scope,defs,schema)
    eb=validate_annotation(b,scope,defs,schema)
    if ea or eb:
        result={"probe":"DRP-03","primary_class":"HARNESS_INVALID","errors":{"a":ea,"b":eb}}
        out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
        (out/"result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(result,sort_keys=True)); return 2

    fa,fb=flatten(a),flatten(b)
    matches=match_props(fa,fb,defs["proposition_matching"]["match_threshold"])
    prop_f1=f1_from_matches(len(fa),len(fb),len(matches))
    group_f1=grouping_f1(fa,fb,matches)

    wa,wb=witness_set(a),witness_set(b)
    required=set(defs["required_witness_tags"])
    witness_ok=(required<=wa and required<=wb)

    neg_paths={x["path"] for x in scope["primary_sources"] if x["role"]=="NEGATIVE_CONTROL"}
    neg_a=sum(len(sa["obligation_units"]) for sa in a["source_annotations"] if sa["source_path"] in neg_paths)
    neg_b=sum(len(sa["obligation_units"]) for sa in b["source_annotations"] if sa["source_path"] in neg_paths)

    rate_a,fg_a=false_gap_rate(fa,key)
    rate_b,fg_b=false_gap_rate(fb,key)

    derived_ok=True; derived=[]
    for f in key["derived_state_fixtures"]:
        actual=derive_state(f["facts"]); ok=actual==f["expected"]; derived_ok &= ok
        derived.append({"id":f["id"],"expected":f["expected"],"actual":actual,"ok":ok})

    th=defs["thresholds"]
    passed=(
        prop_f1>=th["proposition_set_f1_min"]
        and group_f1>=th["grouping_agreement_min"]
        and witness_ok
        and rate_a<=th["false_gap_rate_max"]
        and rate_b<=th["false_gap_rate_max"]
        and neg_a<=th["negative_control_units_max"]
        and neg_b<=th["negative_control_units_max"]
        and derived_ok
    )
    primary="PASS" if passed else "AMEND"
    result={
      "probe":"DRP-03","protocol":"AO10-DRP-V01","primary_class":primary,
      "reviewer_a_propositions":len(fa),"reviewer_b_propositions":len(fb),
      "matched_propositions":len(matches),"proposition_set_f1":prop_f1,
      "grouping_agreement_f1":group_f1,
      "witnesses":{"required":sorted(required),"a":sorted(wa),"b":sorted(wb),"both_ok":witness_ok},
      "negative_control_unit_counts":{"a":neg_a,"b":neg_b},
      "false_gap":{"a_rate":rate_a,"b_rate":rate_b,"a":fg_a,"b":fg_b},
      "derived_state_fixtures":derived,
      "thresholds":th,
      "matches":[{"a_prop":fa[i]["prop_id"],"b_prop":fb[j]["prop_id"],"source":fa[i]["source_path"],"anchor":fa[i]["anchor"],"similarity":score} for i,j,score in matches]
    }
    out=Path(args.output); out.mkdir(parents=True,exist_ok=True)
    (out/"result.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ["probe","primary_class","proposition_set_f1","grouping_agreement_f1"]},sort_keys=True))
    return 0 if passed else 1

if __name__=="__main__":
    raise SystemExit(main())
