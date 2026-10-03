ALLOWED_AUTHORITY = {"GOVERNING_ACCEPTANCE", "ACCEPTED_DOMAIN_CONTRACT"}

def evaluate_granularity(fixture):
    accepted = list(fixture["accepted_effect_ids"])
    counts = {effect: 0 for effect in accepted}
    invalid_multi = []
    for requirement in fixture["requirements"]:
        effects = list(requirement["effect_ids"])
        if len(effects) != 1:
            invalid_multi.append(requirement["requirement_id"])
        for effect in effects:
            if effect in counts:
                counts[effect] += 1
    missing = sorted(effect for effect, count in counts.items() if count == 0)
    duplicate = sorted(effect for effect, count in counts.items() if count > 1)
    split_required = bool(invalid_multi)
    sequence_valid = sorted(fixture["sequences"], key=lambda x: x["sequence_id"]) == sorted(
        fixture["required_sequences"], key=lambda x: x["sequence_id"]
    )
    valid = not split_required and not missing and not duplicate and sequence_valid
    if fixture["required_sequences"] and valid:
        outcome = "VALID_WITH_SEPARATE_SEQUENCE"
    elif split_required:
        outcome = "SPLIT_REQUIRED"
    elif valid:
        outcome = "VALID"
    else:
        outcome = "INVALID"
    return {
        "granularity_valid": valid,
        "split_required": split_required,
        "missing_effects": missing,
        "duplicate_effects": duplicate,
        "invalid_multi_effect_requirements": sorted(invalid_multi),
        "sequence_valid": sequence_valid,
        "outcome": outcome,
    }

def evaluate_completion(fixture):
    contract = fixture["completion_contract"]
    bound = fixture["bound_contract"]
    declarations = fixture["realizer_declarations"]
    authority_valid = contract["authority_class"] in ALLOWED_AUTHORITY
    binding_valid = (
        contract["criterion_id"] == bound["criterion_id"]
        and contract["revision"] == bound["revision"]
        and contract["requirement_ref"] == fixture["requirement_ref"]
    )
    unauthorized_override = any(d.get("completion_override") is not None for d in declarations)
    completion_contract_valid = authority_valid and binding_valid and not unauthorized_override

    required = set(contract["required_components"])
    covered = set()
    unknown = set()
    declaration_invalid = False
    for declaration in declarations:
        if not declaration.get("declaration_valid", False) or declaration["requirement_ref"] != fixture["requirement_ref"]:
            declaration_invalid = True
            continue
        for component in declaration["covers_components"]:
            if component in required:
                covered.add(component)
            else:
                unknown.add(component)

    coverage_complete = (
        completion_contract_valid
        and not declaration_invalid
        and not unknown
        and contract["composition_rule"] == "ALL_REQUIRED"
        and covered == required
    )

    facts = fixture["source_facts"]
    evidence_valid = (
        (not contract["evidence_required"])
        or (facts["evidence_present"] and facts["evidence_exact_subject"] and facts["evidence_fresh"])
    )
    qualification_complete = (not contract["qualification_required"]) or facts["qualification_passed"]
    activation_effective = (not contract["activation_required"]) or facts["activation_effective"]
    review_required = (
        not completion_contract_valid
        or declaration_invalid
        or bool(unknown)
        or facts["conflict_present"]
    )
    satisfied = (
        facts["requirement_active"]
        and completion_contract_valid
        and coverage_complete
        and evidence_valid
        and qualification_complete
        and activation_effective
        and not facts["conflict_present"]
    )
    return {
        "completion_contract_valid": completion_contract_valid,
        "coverage_complete": coverage_complete,
        "evidence_valid": evidence_valid,
        "qualification_complete": qualification_complete,
        "activation_effective": activation_effective,
        "requirement_satisfied": satisfied,
        "review_required": review_required,
    }
