PROJECTION_VERSION = "HYBRID_C8_V01"

def evaluate(row):
    f = row["facts"]

    if (not f["source_facts_valid"]) or f["conflict_present"] or (
        f["deferral_present"] and not f["deferral_valid"]
    ):
        state, gap = "REVIEW_REQUIRED", "REVIEW"
    elif f["deferral_present"] and f["deferral_valid"]:
        state, gap = "DEFERRED", "NONE"
    elif f["requirement_satisfied"]:
        state, gap = "SATISFIED", "NONE"
    else:
        state = "OPEN"
        if not f["coverage_complete"]:
            gap = "COVERAGE"
        elif f["evidence_required"] and not f["evidence_valid"]:
            gap = "EVIDENCE"
        elif f["qualification_required"] and not f["qualification_complete"]:
            gap = "QUALIFICATION"
        elif f["activation_required"] and not f["activation_effective"]:
            gap = "ACTIVATION"
        else:
            gap = "REVIEW"

    return {
        "requirement_id": row["requirement_id"],
        "projection_version": PROJECTION_VERSION,
        "state": state,
        "next_gap": gap,
    }
