EXPECTED_OWNER_PACKET_SHA256 = "2ac7ec839138189b5657da4c8f78f8c938ac3227da1c7af7f3c6f3fda7ae4fb4"
EXPECTED_PROBE_ID = "HYBRID_D1_REAL_EVENT_REPLAY_V01"
EXPECTED_FIXTURE_ID = "REAL_CLAUDE_MESSAGE018_TRANSPORT_CORRECTION"
GITHUB_TRANSPORT = "CLAUDE_SIDE_GITHUB_CONNECTOR"


def _effect_by_type(accepted_j1, effect_type):
    matches = [row for row in accepted_j1["effects"] if row["type"] == effect_type]
    return matches[0] if len(matches) == 1 else None


def evaluate(accepted_j1, source_facts):
    requirement = _effect_by_type(accepted_j1, "REQUIRE")
    prohibition = _effect_by_type(accepted_j1, "PROHIBIT")
    authorization = _effect_by_type(accepted_j1, "AUTHORIZE")
    lifecycle = _effect_by_type(accepted_j1, "LIFECYCLE")

    acceptance_binding_valid = (
        accepted_j1.get("schema_version") == 1
        and accepted_j1.get("probe_id") == EXPECTED_PROBE_ID
        and accepted_j1.get("owner_decision") == "ACCEPT"
        and accepted_j1.get("owner_packet_sha256") == EXPECTED_OWNER_PACKET_SHA256
        and len(accepted_j1.get("effects", [])) == 4
        and all(x is not None for x in (requirement, prohibition, authorization, lifecycle))
    )

    correction = source_facts.get("correction", {})
    action = source_facts.get("action", {})
    evidence = source_facts.get("evidence", {})

    authorized_path = correction.get("authorized_path")
    source_fact_contract_valid = (
        source_facts.get("schema_version") == 1
        and source_facts.get("fixture_id") == EXPECTED_FIXTURE_ID
        and correction.get("commit") == accepted_j1.get("source_correction_commit")
        and correction.get("authorized_transport") == GITHUB_TRANSPORT
        and isinstance(action.get("changed_paths"), list)
        and len(action.get("changed_paths", [])) >= 1
        and bool(action.get("commit"))
        and bool(action.get("parent"))
    )

    transport_attested_github_connector = (
        action.get("message_transport_attestation") == GITHUB_TRANSPORT
        and correction.get("authorized_transport") == GITHUB_TRANSPORT
    )

    authorized_path_only = (
        action.get("changed_paths") == [authorized_path]
        and action.get("message_only_authorized_path_written_attestation") is True
    )

    commit_receipt_bound_to_correction_head = (
        action.get("parent") == correction.get("commit")
        and evidence.get("git_commit_receipt_present") is True
    )

    runtime_bridge_prohibition_not_violated = (
        correction.get("claude_runtime_bridge_available") is False
        and action.get("message_transport_attestation") == GITHUB_TRANSPORT
    )

    evidence_valid = all(
        evidence.get(name) is True
        for name in (
            "git_commit_receipt_present",
            "commit_parent_observed",
            "changed_paths_observed",
            "message_transport_attestation_present",
        )
    )

    qualification_complete = (
        transport_attested_github_connector
        and authorized_path_only
        and commit_receipt_bound_to_correction_head
        and runtime_bridge_prohibition_not_violated
    )

    authorization_exercise_valid = (
        authorization is not None
        and authorization.get("exercise_contract", {}).get("exact_authorized_path") == authorized_path
        and transport_attested_github_connector
        and authorized_path_only
        and commit_receipt_bound_to_correction_head
    )

    lifecycle_lineage = lifecycle.get("lineage", {}) if lifecycle else {}
    lineage_transition_valid = (
        lifecycle is not None
        and lifecycle_lineage.get("relation") == "REPLACE"
        and lifecycle_lineage.get("predecessor_id") == correction.get("predecessor_rule_id")
        and lifecycle_lineage.get("successor_id") == correction.get("successor_rule_id")
        and lifecycle_lineage.get("successor_id") == requirement.get("accepted_effect_id")
        and lifecycle_lineage.get("realization_succession") == "OPEN_RESET"
        and correction.get("lineage_relation") == "REPLACE"
        and correction.get("realization_succession") == "OPEN_RESET"
    )

    shared_predicates = {
        "transport_attested_github_connector": transport_attested_github_connector,
        "authorized_path_only": authorized_path_only,
        "commit_receipt_bound_to_correction_head": commit_receipt_bound_to_correction_head,
        "runtime_bridge_prohibition_not_violated": runtime_bridge_prohibition_not_violated,
        "evidence_valid": evidence_valid,
        "qualification_complete": qualification_complete,
        "authorization_exercise_valid": authorization_exercise_valid,
        "lineage_transition_valid": lineage_transition_valid,
    }

    completion = requirement.get("completion_contract", {}) if requirement else {}
    expected_components = {
        "TRANSPORT_ATTESTED_GITHUB_CONNECTOR": transport_attested_github_connector,
        "AUTHORIZED_PATH_ONLY": authorized_path_only,
        "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD": commit_receipt_bound_to_correction_head,
    }
    required_components = completion.get("required_components", [])
    component_set_valid = set(required_components) == set(expected_components) and len(required_components) == 3
    all_required_components_true = (
        component_set_valid
        and all(expected_components[name] for name in required_components)
    )

    requirement_satisfied = (
        acceptance_binding_valid
        and source_fact_contract_valid
        and requirement is not None
        and requirement.get("accounting_disposition") == "REALIZATION_TRACKED"
        and completion.get("composition_rule") == "ALL_REQUIRED"
        and all_required_components_true
        and evidence_valid
        and qualification_complete
    )

    if lineage_transition_valid and requirement is not None:
        realization_initialization = {
            "effect_id": requirement["accepted_effect_id"],
            "mode": "OPEN_RESET",
        }
    else:
        realization_initialization = {
            "effect_id": requirement["accepted_effect_id"] if requirement else "",
            "mode": "OPEN_RESET",
        }

    if not acceptance_binding_valid or not source_fact_contract_valid or not lineage_transition_valid:
        realization_orientation = "REVIEW_REQUIRED"
        next_gap = "REVIEW"
    elif requirement_satisfied:
        realization_orientation = "SATISFIED"
        next_gap = "NONE"
    elif not all_required_components_true:
        realization_orientation = "OPEN"
        next_gap = "COVERAGE"
    elif not evidence_valid:
        realization_orientation = "OPEN"
        next_gap = "EVIDENCE"
    elif not qualification_complete:
        realization_orientation = "OPEN"
        next_gap = "QUALIFICATION"
    else:
        realization_orientation = "REVIEW_REQUIRED"
        next_gap = "REVIEW"

    enforcement = prohibition.get("standing_enforcement", {}) if prohibition else {}
    if prohibition is None or enforcement.get("mode") != "DETECTIVE_ONLY" or not enforcement.get("control_ref"):
        standing_prohibition_enforcement = "UNBOUND_REVIEW_REQUIRED"
    elif runtime_bridge_prohibition_not_violated:
        standing_prohibition_enforcement = "DETECTIVE_ONLY_COMPLIANT"
    else:
        standing_prohibition_enforcement = "DETECTIVE_ONLY_VIOLATION"

    if not action.get("commit"):
        authorization_exercise_status = "NOT_EXERCISED"
    elif authorization_exercise_valid:
        authorization_exercise_status = "EXERCISED_VALID"
    else:
        authorization_exercise_status = "EXERCISED_INVALID"

    current_effect_ids = sorted(
        row["accepted_effect_id"]
        for row in accepted_j1.get("effects", [])
        if row.get("type") in {"REQUIRE", "PROHIBIT"}
    )

    review_required = (
        not acceptance_binding_valid
        or not source_fact_contract_valid
        or not lineage_transition_valid
        or not requirement_satisfied
        or standing_prohibition_enforcement != "DETECTIVE_ONLY_COMPLIANT"
        or authorization_exercise_status != "EXERCISED_VALID"
    )

    if not review_required:
        review_owner = None
    elif not acceptance_binding_valid or not lineage_transition_valid:
        review_owner = "GOVERNING_OWNER"
    elif not source_fact_contract_valid or not transport_attested_github_connector or not authorized_path_only or not commit_receipt_bound_to_correction_head:
        review_owner = "INTEGRATION_OWNER"
    else:
        review_owner = "ASSURANCE_OWNER"

    return {
        "fixture_id": source_facts.get("fixture_id"),
        "acceptance_binding_valid": acceptance_binding_valid,
        "source_fact_contract_valid": source_fact_contract_valid,
        "shared_predicates": shared_predicates,
        "lineage_relation_valid": lineage_transition_valid,
        "current_effect_ids": current_effect_ids,
        "realization_initialization": realization_initialization,
        "requirement_satisfied": requirement_satisfied,
        "realization_orientation": realization_orientation,
        "next_gap": next_gap,
        "standing_prohibition_enforcement": standing_prohibition_enforcement,
        "authorization_exercise_status": authorization_exercise_status,
        "review_required": review_required,
        "review_owner": review_owner,
    }
