"""HYBRID_D1_REAL_EVENT_REPLAY_V01 - Evaluator B (independently authored by Claude / claude-04).

Authored only from the reviewer-facing D-1 materials:
    experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json
    experiments/ao10_hybrid_d1_replay_v01/source_facts.json
    experiments/ao10_hybrid_d1_replay_v01/definitions.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_contract.json
with Research 490-492 as explanatory context.

Standard library only. Deterministic. No file, network or model access inside evaluate.
Only structured fields are consumed; accepted_effect_statement prose is never interpreted.
"""

GITHUB_CONNECTOR = "CLAUDE_SIDE_GITHUB_CONNECTOR"
OPEN_RESET = "OPEN_RESET"

COMPONENT_TO_PREDICATE = {
    "TRANSPORT_ATTESTED_GITHUB_CONNECTOR": "transport_attested_github_connector",
    "AUTHORIZED_PATH_ONLY": "authorized_path_only",
    "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD": "commit_receipt_bound_to_correction_head",
}

EVIDENCE_FIELDS = (
    "git_commit_receipt_present",
    "commit_parent_observed",
    "changed_paths_observed",
    "message_transport_attestation_present",
)

SHARED_PREDICATE_ORDER = (
    "transport_attested_github_connector",
    "authorized_path_only",
    "commit_receipt_bound_to_correction_head",
    "runtime_bridge_prohibition_not_violated",
    "evidence_valid",
    "qualification_complete",
    "authorization_exercise_valid",
    "lineage_transition_valid",
)


def _is_sha(value, length):
    if not isinstance(value, str) or len(value) != length:
        return False
    return all(ch in "0123456789abcdef" for ch in value)


def _dict(value):
    return value if isinstance(value, dict) else {}


def _effects_by_type(accepted_j1):
    by_type = {}
    for effect in accepted_j1.get("effects") or []:
        if isinstance(effect, dict):
            by_type.setdefault(effect.get("type"), []).append(effect)
    return by_type


def _single(by_type, effect_type):
    found = by_type.get(effect_type) or []
    return found[0] if len(found) == 1 else None


def _acceptance_binding_valid(accepted_j1, source_facts):
    """Structural validity of the owner-accepted J1 boundary and its binding to the
    governing correction recorded in the source facts."""
    if accepted_j1.get("owner_decision") != "ACCEPT":
        return False
    if not _is_sha(accepted_j1.get("owner_packet_sha256"), 64):
        return False
    if not isinstance(accepted_j1.get("owner_decision_record"), str) or not accepted_j1.get("owner_decision_record"):
        return False
    if not isinstance(accepted_j1.get("source_authority"), str) or not accepted_j1.get("source_authority"):
        return False
    correction = _dict(source_facts.get("correction"))
    if accepted_j1.get("source_correction_commit") != correction.get("commit"):
        return False

    effects = [e for e in accepted_j1.get("effects") or [] if isinstance(e, dict)]
    ids = [e.get("accepted_effect_id") for e in effects]
    if not effects or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        return False
    for effect in effects:
        if not isinstance(effect.get("accepted_effect_statement"), str) or not effect.get("accepted_effect_statement"):
            return False
        disposition = effect.get("accounting_disposition")
        if disposition == "REALIZATION_TRACKED":
            contract = _dict(effect.get("completion_contract"))
            if contract.get("authority") not in ("GOVERNING_ACCEPTANCE", "ACCEPTED_DOMAIN_CONTRACT"):
                return False
            if not isinstance(contract.get("required_components"), list) or not contract.get("required_components"):
                return False
        elif disposition == "NO_REALIZATION_REQUIRED":
            if not isinstance(effect.get("accounting_reason"), str) or not effect.get("accounting_reason"):
                return False
        else:
            return False

    by_type = _effects_by_type(accepted_j1)
    for effect_type in ("REQUIRE", "PROHIBIT", "AUTHORIZE", "LIFECYCLE"):
        if _single(by_type, effect_type) is None:
            return False
    return True


def _source_fact_contract_valid(source_facts):
    """Structural validity (presence and types) of the J2 source-fact record."""
    if not isinstance(source_facts.get("fixture_id"), str) or not source_facts.get("fixture_id"):
        return False
    correction = source_facts.get("correction")
    action = source_facts.get("action")
    evidence = source_facts.get("evidence")
    if not isinstance(correction, dict) or not isinstance(evidence, dict):
        return False
    if not _is_sha(correction.get("commit"), 40):
        return False
    if not isinstance(correction.get("claude_runtime_bridge_available"), bool):
        return False
    for key in (
        "authorized_transport",
        "authorized_path",
        "predecessor_rule_id",
        "successor_rule_id",
        "lineage_relation",
        "realization_succession",
    ):
        if not isinstance(correction.get(key), str) or not correction.get(key):
            return False
    for key in EVIDENCE_FIELDS:
        if not isinstance(evidence.get(key), bool):
            return False
    if action is None:
        return True
    if not isinstance(action, dict):
        return False
    if not _is_sha(action.get("commit"), 40) or not _is_sha(action.get("parent"), 40):
        return False
    paths = action.get("changed_paths")
    if not isinstance(paths, list) or any(not isinstance(p, str) for p in paths):
        return False
    if not isinstance(action.get("message_transport_attestation"), str):
        return False
    if not isinstance(action.get("message_only_authorized_path_written_attestation"), bool):
        return False
    return True


def _shared_predicates(accepted_j1, source_facts):
    correction = _dict(source_facts.get("correction"))
    action = _dict(source_facts.get("action"))
    evidence = _dict(source_facts.get("evidence"))
    lifecycle = _single(_effects_by_type(accepted_j1), "LIFECYCLE") or {}
    lineage = _dict(lifecycle.get("lineage"))

    transport = (
        action.get("message_transport_attestation") == correction.get("authorized_transport")
        and correction.get("authorized_transport") == GITHUB_CONNECTOR
    )
    path_only = (
        isinstance(action.get("changed_paths"), list)
        and action.get("changed_paths") == [correction.get("authorized_path")]
        and action.get("message_only_authorized_path_written_attestation") is True
    )
    receipt = (
        action.get("parent") is not None
        and action.get("parent") == correction.get("commit")
        and evidence.get("git_commit_receipt_present") is True
    )
    no_bridge = (
        correction.get("claude_runtime_bridge_available") is False
        and action.get("message_transport_attestation") == GITHUB_CONNECTOR
    )
    evidence_valid = all(evidence.get(key) is True for key in EVIDENCE_FIELDS)
    qualification = transport and path_only and receipt and no_bridge
    authorization = transport and path_only and receipt
    lineage_valid = (
        correction.get("lineage_relation") == "REPLACE"
        and lineage.get("relation") == "REPLACE"
        and correction.get("predecessor_rule_id") == lineage.get("predecessor_id")
        and correction.get("successor_rule_id") == lineage.get("successor_id")
        and lineage.get("predecessor_id") is not None
        and lineage.get("successor_id") is not None
        and correction.get("realization_succession") == OPEN_RESET
        and lineage.get("realization_succession") == OPEN_RESET
    )
    values = {
        "transport_attested_github_connector": bool(transport),
        "authorized_path_only": bool(path_only),
        "commit_receipt_bound_to_correction_head": bool(receipt),
        "runtime_bridge_prohibition_not_violated": bool(no_bridge),
        "evidence_valid": bool(evidence_valid),
        "qualification_complete": bool(qualification),
        "authorization_exercise_valid": bool(authorization),
        "lineage_transition_valid": bool(lineage_valid),
    }
    return {key: values[key] for key in SHARED_PREDICATE_ORDER}


def _lineage_relation_valid(accepted_j1, predicates):
    by_type = _effects_by_type(accepted_j1)
    lifecycle = _single(by_type, "LIFECYCLE")
    if lifecycle is None:
        return False
    lineage = _dict(lifecycle.get("lineage"))
    successor = lineage.get("successor_id")
    predecessor = lineage.get("predecessor_id")
    require_ids = set(e.get("accepted_effect_id") for e in by_type.get("REQUIRE") or [])
    return (
        lineage.get("relation") == "REPLACE"
        and predecessor != successor
        and successor in require_ids
        and lineage.get("realization_succession") == OPEN_RESET
        and predicates["lineage_transition_valid"]
    )


def evaluate(accepted_j1, source_facts):
    accepted_j1 = _dict(accepted_j1)
    source_facts = _dict(source_facts)
    by_type = _effects_by_type(accepted_j1)
    require = _single(by_type, "REQUIRE") or {}
    prohibit = _single(by_type, "PROHIBIT") or {}
    authorize = _single(by_type, "AUTHORIZE")
    lifecycle = _single(by_type, "LIFECYCLE") or {}
    correction = _dict(source_facts.get("correction"))
    action_present = isinstance(source_facts.get("action"), dict)

    acceptance_valid = _acceptance_binding_valid(accepted_j1, source_facts)
    source_valid = _source_fact_contract_valid(source_facts)
    predicates = _shared_predicates(accepted_j1, source_facts)
    lineage_valid = _lineage_relation_valid(accepted_j1, predicates)

    # Accepted authorization path must agree with the correction's authorized path.
    exercise = _dict((authorize or {}).get("exercise_contract"))
    authorization_path_consistent = authorize is not None and exercise.get("exact_authorized_path") == correction.get(
        "authorized_path"
    )
    governing_valid = acceptance_valid and lineage_valid and authorization_path_consistent

    # Current effects after the replayed action (definitions.currentness).
    current = []
    if acceptance_valid:
        for effect in accepted_j1.get("effects") or []:
            eid = effect.get("accepted_effect_id")
            etype = effect.get("type")
            if etype in ("REQUIRE", "PROHIBIT"):
                current.append(eid)
            elif etype == "AUTHORIZE":
                if not action_present:
                    current.append(eid)
            elif etype == "LIFECYCLE":
                if not lineage_valid:
                    current.append(eid)
    current = sorted(set(current))

    # Realization succession from the accepted REPLACE (OPEN_RESET initialization).
    initialization = []
    if lineage_valid:
        initialization.append(
            {"effect_id": _dict(lifecycle.get("lineage")).get("successor_id"), "mode": OPEN_RESET}
        )
    initialization.sort(key=lambda entry: entry["effect_id"])

    # J3 requirement satisfaction for the realization-tracked REQUIRE.
    contract = _dict(require.get("completion_contract"))
    components = contract.get("required_components") or []
    components_known = bool(components) and all(c in COMPONENT_TO_PREDICATE for c in components)
    coverage_complete = components_known and all(predicates[COMPONENT_TO_PREDICATE[c]] for c in components)
    evidence_ok = predicates["evidence_valid"] or contract.get("evidence_required") is False
    qualification_ok = predicates["qualification_complete"] or contract.get("qualification_required") is False
    activation_ok = contract.get("activation_required") is not True
    requirement_satisfied = bool(
        acceptance_valid
        and source_valid
        and require.get("accounting_disposition") == "REALIZATION_TRACKED"
        and contract.get("composition_rule") == "ALL_REQUIRED"
        and coverage_complete
        and evidence_ok
        and qualification_ok
        and activation_ok
    )

    # Standing prohibition visibility.
    standing = _dict(prohibit.get("standing_enforcement"))
    if standing.get("mode") == "DETECTIVE_ONLY" and standing.get("control_ref"):
        if predicates["runtime_bridge_prohibition_not_violated"]:
            standing_status = "DETECTIVE_ONLY_COMPLIANT"
        else:
            standing_status = "DETECTIVE_ONLY_VIOLATION"
    else:
        standing_status = "UNBOUND_REVIEW_REQUIRED"

    # Bounded authorization exercise.
    if not action_present:
        authorization_status = "NOT_EXERCISED"
    elif authorize is not None and predicates["authorization_exercise_valid"] and authorization_path_consistent:
        authorization_status = "EXERCISED_VALID"
    else:
        authorization_status = "EXERCISED_INVALID"

    # Review routing (precedence: governing > integration > assurance).
    review_owner = None
    if not governing_valid:
        review_owner = "GOVERNING_OWNER"
    elif not source_valid or (
        action_present
        and not (predicates["authorized_path_only"] and predicates["commit_receipt_bound_to_correction_head"])
    ):
        review_owner = "INTEGRATION_OWNER"
    elif action_present and not (
        predicates["evidence_valid"]
        and predicates["qualification_complete"]
        and predicates["transport_attested_github_connector"]
        and predicates["runtime_bridge_prohibition_not_violated"]
    ):
        review_owner = "ASSURANCE_OWNER"
    elif standing_status == "UNBOUND_REVIEW_REQUIRED":
        review_owner = "GOVERNING_OWNER"
    review_required = review_owner is not None

    # Generated realization orientation and next gap. REVIEW_REQUIRED orientation is
    # reserved for invalid or contradictory acceptance / source / lineage bindings;
    # evidence or qualification gaps still route to review but orient as OPEN + gap.
    structural_review = not governing_valid or not source_valid
    if structural_review:
        orientation, next_gap = "REVIEW_REQUIRED", "REVIEW"
    elif requirement_satisfied:
        orientation, next_gap = "SATISFIED", "NONE"
    else:
        orientation = "OPEN"
        if not action_present:
            next_gap = "UNOWNED"
        elif not coverage_complete:
            next_gap = "COVERAGE"
        elif not evidence_ok:
            next_gap = "EVIDENCE"
        elif not qualification_ok:
            next_gap = "QUALIFICATION"
        elif not activation_ok:
            next_gap = "ACTIVATION"
        else:
            next_gap = "REVIEW"

    return {
        "fixture_id": source_facts.get("fixture_id"),
        "acceptance_binding_valid": acceptance_valid,
        "source_fact_contract_valid": source_valid,
        "shared_predicates": predicates,
        "lineage_relation_valid": lineage_valid,
        "current_effect_ids": current,
        "realization_initialization": initialization,
        "requirement_satisfied": requirement_satisfied,
        "realization_orientation": orientation,
        "next_gap": next_gap,
        "standing_prohibition_enforcement": standing_status,
        "authorization_exercise_status": authorization_status,
        "review_required": review_required,
        "review_owner": review_owner,
    }
