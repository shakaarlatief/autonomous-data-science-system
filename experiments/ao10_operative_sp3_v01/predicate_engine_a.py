import json, sys

def evaluate(f):
    coverage_present = f["coverage_edges_present"]
    coverage_valid = coverage_present and f["coverage_edges_valid"]
    deferral_effective = (
        f["deferral_present"]
        and f["deferral_authorized"]
        and f["deferral_scope_valid"]
        and f["deferral_temporally_valid"]
    )
    evidence_valid = (
        (not f["evidence_required"])
        or (
            f["evidence_present"]
            and f["evidence_exact_subject"]
            and f["evidence_fresh"]
        )
    )
    qualification_complete = (not f["qualification_required"]) or f["qualification_passed"]
    activation_effective = (not f["activation_required"]) or f["activation_effective"]
    conflict_present = f["conflict_present"]
    realization_satisfied = (
        f["clause_active"]
        and (not conflict_present)
        and (
            deferral_effective
            or (
                coverage_valid
                and evidence_valid
                and qualification_complete
                and activation_effective
            )
        )
    )
    review_required = (
        f["clause_active"]
        and (
            conflict_present
            or (coverage_present and not coverage_valid)
            or (f["deferral_present"] and not deferral_effective)
        )
    )
    return {
        "coverage_present": coverage_present,
        "coverage_valid": coverage_valid,
        "deferral_effective": deferral_effective,
        "evidence_valid": evidence_valid,
        "qualification_complete": qualification_complete,
        "activation_effective": activation_effective,
        "conflict_present": conflict_present,
        "realization_satisfied": realization_satisfied,
        "review_required": review_required,
    }

if __name__ == "__main__":
    doc=json.load(open(sys.argv[1],encoding="utf-8"))
    print(json.dumps({x["fixture_id"]:evaluate(x["facts"]) for x in doc["fixtures"]},sort_keys=True))
