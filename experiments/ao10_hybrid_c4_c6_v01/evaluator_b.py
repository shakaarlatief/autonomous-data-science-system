AUTHORIZED_CRITERION_OWNERS = frozenset(("GOVERNING_ACCEPTANCE", "ACCEPTED_DOMAIN_CONTRACT"))

def evaluate_granularity(fixture):
    accepted = frozenset(fixture["accepted_effect_ids"])
    membership = []
    wide_requirements = set()
    for row in fixture["requirements"]:
        effect_ids = tuple(row["effect_ids"])
        if len(effect_ids) != 1:
            wide_requirements.add(row["requirement_id"])
        membership.extend((effect, row["requirement_id"]) for effect in effect_ids if effect in accepted)

    counts = {effect: sum(1 for member, _ in membership if member == effect) for effect in accepted}
    missing = sorted(effect for effect, count in counts.items() if count == 0)
    duplicates = sorted(effect for effect, count in counts.items() if count > 1)
    expected_sequences = {
        (x["sequence_id"], x["predecessor_ref"], x["successor_ref"])
        for x in fixture["required_sequences"]
    }
    actual_sequences = {
        (x["sequence_id"], x["predecessor_ref"], x["successor_ref"])
        for x in fixture["sequences"]
    }
    sequence_valid = actual_sequences == expected_sequences
    split_required = len(wide_requirements) > 0
    valid = not (split_required or missing or duplicates) and sequence_valid

    if split_required:
        outcome = "SPLIT_REQUIRED"
    elif valid and expected_sequences:
        outcome = "VALID_WITH_SEPARATE_SEQUENCE"
    elif valid:
        outcome = "VALID"
    else:
        outcome = "INVALID"

    return {
        "granularity_valid": valid,
        "split_required": split_required,
        "missing_effects": missing,
        "duplicate_effects": duplicates,
        "invalid_multi_effect_requirements": sorted(wide_requirements),
        "sequence_valid": sequence_valid,
        "outcome": outcome,
    }

def evaluate_completion(fixture):
    criterion = fixture["completion_contract"]
    binding = fixture["bound_contract"]
    declarations = tuple(fixture["realizer_declarations"])

    criterion_key = (criterion["criterion_id"], criterion["revision"], criterion["requirement_ref"])
    binding_key = (binding["criterion_id"], binding["revision"], fixture["requirement_ref"])
    owner_ok = criterion["authority_class"] in AUTHORIZED_CRITERION_OWNERS
    override_free = all(row.get("completion_override") is None for row in declarations)
    contract_ok = owner_ok and criterion_key == binding_key and override_free

    required = frozenset(criterion["required_components"])
    valid_rows = tuple(
        row for row in declarations
        if row.get("declaration_valid", False) and row["requirement_ref"] == fixture["requirement_ref"]
    )
    invalid_row_exists = len(valid_rows) != len(declarations)
    claimed = frozenset(
        component
        for row in valid_rows
        for component in row["covers_components"]
    )
    unknown = claimed.difference(required)
    recognized = claimed.intersection(required)
    coverage_complete = (
        contract_ok
        and not invalid_row_exists
        and not unknown
        and criterion["composition_rule"] == "ALL_REQUIRED"
        and required.issubset(recognized)
    )

    f = fixture["source_facts"]
    checks = {
        "evidence_valid": (not criterion["evidence_required"]) or all(
            (f["evidence_present"], f["evidence_exact_subject"], f["evidence_fresh"])
        ),
        "qualification_complete": (not criterion["qualification_required"]) or f["qualification_passed"],
        "activation_effective": (not criterion["activation_required"]) or f["activation_effective"],
    }
    review = (not contract_ok) or invalid_row_exists or bool(unknown) or f["conflict_present"]
    satisfied = all((
        f["requirement_active"],
        contract_ok,
        coverage_complete,
        checks["evidence_valid"],
        checks["qualification_complete"],
        checks["activation_effective"],
        not f["conflict_present"],
    ))
    return {
        "completion_contract_valid": contract_ok,
        "coverage_complete": coverage_complete,
        **checks,
        "requirement_satisfied": satisfied,
        "review_required": review,
    }
