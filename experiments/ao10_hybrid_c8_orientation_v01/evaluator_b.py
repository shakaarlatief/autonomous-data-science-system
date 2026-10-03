PROJECTION_VERSION = "HYBRID_C8_V01"

def evaluate(row):
    f = row["facts"]

    predicates = {
        "invalid": (
            (not f["source_facts_valid"])
            or f["conflict_present"]
            or (f["deferral_present"] and not f["deferral_valid"])
        ),
        "deferred": f["deferral_present"] and f["deferral_valid"],
        "satisfied": f["requirement_satisfied"],
        "coverage_gap": not f["coverage_complete"],
        "evidence_gap": f["evidence_required"] and not f["evidence_valid"],
        "qualification_gap": f["qualification_required"] and not f["qualification_complete"],
        "activation_gap": f["activation_required"] and not f["activation_effective"],
    }

    state_rules = (
        ("REVIEW_REQUIRED", "invalid"),
        ("DEFERRED", "deferred"),
        ("SATISFIED", "satisfied"),
    )
    state = "OPEN"
    for candidate, predicate_name in state_rules:
        if predicates[predicate_name]:
            state = candidate
            break

    if state == "REVIEW_REQUIRED":
        gap = "REVIEW"
    elif state in {"DEFERRED", "SATISFIED"}:
        gap = "NONE"
    else:
        gap = "REVIEW"
        for candidate_gap, predicate_name in (
            ("COVERAGE", "coverage_gap"),
            ("EVIDENCE", "evidence_gap"),
            ("QUALIFICATION", "qualification_gap"),
            ("ACTIVATION", "activation_gap"),
        ):
            if predicates[predicate_name]:
                gap = candidate_gap
                break

    return {
        "requirement_id": row["requirement_id"],
        "projection_version": PROJECTION_VERSION,
        "state": state,
        "next_gap": gap,
    }
