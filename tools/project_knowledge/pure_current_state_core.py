"""Restricted current-state-core units: declarations only."""


def core_single(candidates, role):
    if length(candidates) != 1:
        fail_view("CURRENT_STATE_ROLE_CARDINALITY", "Expected exactly one canonical owner for " + role)
    return candidates[0]


def core_fields(declaration, names, role):
    for name in names:
        if name not in declaration or declaration[name] == None:
            fail_view("CURRENT_STATE_MISSING_CONTROL", role + " requires " + name)
    return {name: declaration[name] for name in names}


def core_reference(inputs, identity):
    return single([item["declaration"] for item in inputs if item["semantic_id"] == identity],
                  "reference " + identity)


def core_procedure(inputs, identity):
    candidates = [item["declaration"] for item in inputs
                  if item["semantic_id"] == identity and item["profile"] == "governing_procedure.v1"]
    if length(candidates) != 1:
        fail_view("CURRENT_STATE_REFERENCE_TYPE", "governing_procedure must resolve to one canonical governing procedure")
    return candidates[0]


def core_paused(inputs, declaration):
    controls = fields(declaration, ["semantic_id", "state", "resume_target"], "paused resumable workstream")
    reference(inputs, controls["resume_target"])
    has_procedure = "governing_procedure" in declaration
    has_milestones = "orientation_milestones" in declaration
    if has_procedure:
        reference(inputs, declaration["governing_procedure"])
        procedure(inputs, declaration["governing_procedure"])
    if has_milestones:
        milestones = sorted_values([(item["milestone_id"], item["state"])
                                    for item in declaration["orientation_milestones"]])
    if has_procedure and has_milestones:
        return {"semantic_id": controls["semantic_id"], "state": controls["state"],
                "resume_target": controls["resume_target"], "governing_procedure": declaration["governing_procedure"],
                "orientation_milestones": [{"milestone_id": identity, "state": state} for identity, state in milestones]}
    if has_procedure:
        return {"semantic_id": controls["semantic_id"], "state": controls["state"],
                "resume_target": controls["resume_target"], "governing_procedure": declaration["governing_procedure"]}
    if has_milestones:
        return {"semantic_id": controls["semantic_id"], "state": controls["state"],
                "resume_target": controls["resume_target"],
                "orientation_milestones": [{"milestone_id": identity, "state": state} for identity, state in milestones]}
    return {"semantic_id": controls["semantic_id"], "state": controls["state"],
            "resume_target": controls["resume_target"]}


def current_state_core(inputs):
    active = single([item["declaration"] for item in inputs
                     if item["profile"] == "workstream.v1"
                     and item["declaration"]["kind"] == "PROJECT_KNOWLEDGE_ARCHITECTURE_WORKSTREAM"
                     and item["declaration"]["state"] == "ACTIVE"], "active project workstream")
    boundary = single([item["declaration"] for item in inputs
                       if item["profile"] == "project_boundary.v1"
                       and item["declaration"]["kind"] == "PROJECT_INTEGRATION_BOUNDARY"], "integration boundary")
    specification = single([item["declaration"] for item in inputs
                            if item["profile"] == "semantic_source.v1"
                            and item["declaration"]["kind"] == "SPECIFICATION"], "current specification")
    experiment = single([item["declaration"] for item in inputs
                         if item["profile"] == "semantic_source.v1"
                         and item["declaration"]["kind"] == "EXPERIMENT_RESULT"], "current experiment")
    active_core = fields(active, ["semantic_id", "state", "objective", "execution_anchor", "stage"],
                         "active project workstream")
    reference(inputs, active_core["stage"]["stage_id"])
    paused_owners = sorted_values([(item["semantic_id"], item["declaration"]) for item in inputs
                                   if item["profile"] == "workstream.v1"
                                   and item["declaration"]["state"] == "PAUSED"
                                   and "expected_to_resume" in item["declaration"]
                                   and item["declaration"]["expected_to_resume"] == True])
    return {"schema_version": "1", "active_workstream": active_core,
            "integration_boundary": fields(boundary, ["semantic_id", "promoted_branch", "promoted_commit"],
                                           "integration boundary"),
            "current_specification": fields(specification, ["semantic_id"], "current specification"),
            "current_experiment": fields(experiment, ["semantic_id", "outcome"], "current experiment"),
            "paused_workstreams": [paused(inputs, declaration) for identity, declaration in paused_owners]}
