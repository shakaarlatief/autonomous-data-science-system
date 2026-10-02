import json, sys

if __name__ == "__main__":
    d=json.load(open(sys.argv[1],encoding="utf-8"))
    out={}
    for row in d["fixtures"]:
        x=row["facts"]
        p={}
        p["coverage_present"]=bool(x["coverage_edges_present"])
        p["coverage_valid"]=all((p["coverage_present"], bool(x["coverage_edges_valid"])))
        p["deferral_effective"]=all((
            bool(x["deferral_present"]),
            bool(x["deferral_authorized"]),
            bool(x["deferral_scope_valid"]),
            bool(x["deferral_temporally_valid"]),
        ))
        p["evidence_valid"]=any((
            not bool(x["evidence_required"]),
            all((bool(x["evidence_present"]),bool(x["evidence_exact_subject"]),bool(x["evidence_fresh"]))),
        ))
        p["qualification_complete"]=any((not bool(x["qualification_required"]),bool(x["qualification_passed"])))
        p["activation_effective"]=any((not bool(x["activation_required"]),bool(x["activation_effective"])))
        p["conflict_present"]=bool(x["conflict_present"])
        p["realization_satisfied"]=all((
            bool(x["clause_active"]),
            not p["conflict_present"],
            any((
                p["deferral_effective"],
                all((p["coverage_valid"],p["evidence_valid"],p["qualification_complete"],p["activation_effective"])),
            )),
        ))
        p["review_required"]=all((
            bool(x["clause_active"]),
            any((
                p["conflict_present"],
                all((p["coverage_present"],not p["coverage_valid"])),
                all((bool(x["deferral_present"]),not p["deferral_effective"])),
            )),
        ))
        out[row["fixture_id"]]=p
    print(json.dumps(out,sort_keys=True))
