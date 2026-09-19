"""Restricted G009 units: declarations only; no module initialization or imports."""


def inventory_entry(item):
    return {"source_path": item["source_path"], "semantic_id": item["semantic_id"],
            "profile": item["profile"], "content_digest": item["content_digest"]}


def source_inventory(inputs):
    return {"schema_version": "1", "authority_class": "derived",
            "sources": [entry(item) for item in inputs]}


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


def unique_values(values):
    result = []
    for value in sorted_values(values):
        if value not in result:
            result = result + [value]
    return result


def normalized_scope(scope):
    result = {}
    for key in sorted_values(scope):
        value = scope[key]
        if is_text(value):
            result = {**result, key: value}
        else:
            result = {**result, key: unique(value)}
    return result


def scope_token(scope):
    token = ""
    normalized = normalize_scope(scope)
    for key in sorted_values(normalized):
        value = normalized[key]
        if is_text(value):
            token = token + key + "=" + value + ";"
        else:
            token = token + key + "="
            for item in value:
                token = token + item + ","
            token = token + ";"
    return token


def normalized_relations(relations):
    keyed = []
    for relation in relations:
        scope = normalize_scope(relation["scope"]) if "scope" in relation else {}
        row = {"mode": relation["mode"], "target": relation["target"], "scope": scope}
        keyed = keyed + [(relation["mode"] + "|" + relation["target"] + "|" + scope_key(scope), row)]
    return [row for key, row in sorted_values(keyed)]


def catalog_entry(item):
    declaration = item["declaration"]
    return {
        "source_path": item["source_path"],
        "semantic_id": item["semantic_id"],
        "profile": item["profile"],
        "kind": declaration["kind"],
        "state": item["state"],
        "scope": normalize_scope(declaration["scope"]) if "scope" in declaration else {},
        "content_digest": item["content_digest"],
    }


def source_catalog(inputs):
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "sources": [catalog(item) for item in inputs
                    if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED"],
    }


def has_temporal_control(declaration):
    return ("effective_from" in declaration or "effective_to" in declaration
            or "authority_from" in declaration or "authority_to" in declaration)


def identity_transition_record(item):
    declaration = item["declaration"]
    return {
        "source_path": item["source_path"],
        "semantic_id": item["semantic_id"],
        "authority_class": item["authority_class"],
        "state": item["state"],
        "content_digest": item["content_digest"],
        "transition_class": declaration["transition_class"],
        "predecessors": unique(declaration["predecessors"]),
        "successors": unique(declaration["successors"]) if "successors" in declaration else [],
        "resolution_behavior": declaration["resolution_behavior"],
        "provenance": unique(declaration["provenance"]),
        "temporal": temporal(declaration),
        "effective_from": declaration["effective_from"] if "effective_from" in declaration else None,
        "effective_to": declaration["effective_to"] if "effective_to" in declaration else None,
        "authority_from": declaration["authority_from"] if "authority_from" in declaration else None,
        "authority_to": declaration["authority_to"] if "authority_to" in declaration else None,
    }


def identity_source_record(item):
    declaration = item["declaration"]
    return {
        "source_path": item["source_path"],
        "semantic_id": item["semantic_id"],
        "authority_class": item["authority_class"],
        "profile": item["profile"],
        "state": item["state"],
        "content_digest": item["content_digest"],
        "temporal": temporal(declaration),
        "effective_from": declaration["effective_from"] if "effective_from" in declaration else None,
        "effective_to": declaration["effective_to"] if "effective_to" in declaration else None,
        "authority_from": declaration["authority_from"] if "authority_from" in declaration else None,
        "authority_to": declaration["authority_to"] if "authority_to" in declaration else None,
    }


def identity_static_resolution(identity, sources, transitions):
    frontier = [(identity, [])]
    terminals = []
    retired = []
    paths = []
    temporal_required = False
    root_transition_class = None
    continuity_preserved = False
    while frontier:
        current, trail = frontier[0]
        frontier = frontier[1:]
        if current in trail:
            fail_view("IDENTITY_VIEW_CYCLE", "Identity view encountered a transition cycle")
        owners = [item for item in sources if item["semantic_id"] == current]
        if any_temporal([item["declaration"] for item in owners]):
            temporal_required = True
        touching_temporal = [transition for transition in transitions
                             if transition["temporal"] == True
                             and (current in transition["predecessors"]
                                  or current in transition["successors"])]
        if touching_temporal:
            temporal_required = True
        outgoing = [transition for transition in transitions
                    if transition["authority_class"] == "canonical"
                    and transition["temporal"] == False
                    and transition["state"] != "PAUSED"
                    and transition["state"] != "BLOCKED"
                    and transition["state"] != "SUPERSEDED"
                    and current in transition["predecessors"]
                    and not (transition["transition_class"] in
                             ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT"]
                             and transition["predecessors"] == transition["successors"])]
        annotations = [transition for transition in transitions
                       if transition["authority_class"] == "canonical"
                       and transition["temporal"] == False
                       and transition["state"] != "PAUSED"
                       and transition["state"] != "BLOCKED"
                       and transition["state"] != "SUPERSEDED"
                       and current in transition["predecessors"]
                       and transition["transition_class"] in
                           ["MOVE_OR_RENAME", "REPRESENTATION_REPLACEMENT"]
                       and transition["predecessors"] == transition["successors"]]
        if current == identity and annotations:
            continuity_preserved = True
        paths = paths + [transition["source_path"] for transition in annotations]
        if length(outgoing) > 1:
            fail_view("IDENTITY_VIEW_CONFLICT", "Identity view encountered conflicting static transitions")
        if length(outgoing) == 0:
            terminals = terminals + [current]
        else:
            transition = outgoing[0]
            if current == identity:
                root_transition_class = transition["transition_class"]
            paths = paths + [transition["source_path"]]
            if transition["transition_class"] == "RETIRE":
                retired = retired + [current]
            else:
                for successor in transition["successors"]:
                    frontier = frontier + [(successor, trail + [current])]
    terminal_ids = unique(terminals)
    retired_ids = unique(retired)
    current_carriers = unique([
        item["source_path"] for item in sources
        if item["authority_class"] == "canonical"
        and item["state"] != "SUPERSEDED"
        and item["semantic_id"] in terminal_ids
        and temporal(item["declaration"]) == False
    ])
    canonical_owner = any_true([
        item["authority_class"] == "canonical"
        and item["state"] != "SUPERSEDED"
        and item["semantic_id"] == identity
        and temporal(item["declaration"]) == False
        for item in sources
    ])
    mapping = {
        "MERGE": "MERGED",
        "SPLIT": "SPLIT",
        "SUPERSEDE": "SUPERSEDED",
        "RETIRE": "RETIRED",
        "REDIRECT": "REDIRECTED",
    }
    disposition = "TEMPORAL_CONTEXT_REQUIRED" if temporal_required else (
        mapping[root_transition_class] if root_transition_class != None else (
            "CURRENT" if canonical_owner else "HISTORICAL"
        )
    )
    return {
        "semantic_id": identity,
        "disposition": disposition,
        "static_terminal_ids": terminal_ids,
        "static_retired_ids": retired_ids,
        "static_current_carriers": current_carriers,
        "transition_paths": unique(paths),
        "history_carriers": unique([
            item["source_path"] for item in sources if item["semantic_id"] == identity
        ]),
        "continuity_preserved": continuity_preserved,
        "temporal_resolution_required": temporal_required,
    }


def any_temporal(declarations):
    result = False
    for declaration in declarations:
        if temporal(declaration):
            result = True
    return result


def identity_index(inputs):
    sources = [item for item in inputs if item["semantic_id"] != None]
    transitions = [transition_record(item) for item in inputs
                   if item["profile"] == "identity_transition.v1"]
    endpoint_ids = []
    for transition in transitions:
        endpoint_ids = endpoint_ids + transition["predecessors"] + transition["successors"]
    identities = unique([item["semantic_id"] for item in sources] + endpoint_ids)
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "resolution_basis": "STATIC_PLUS_EXPLICIT_TEMPORAL_DEFER",
        "identities": [resolve_identity_row(identity, sources, transitions) for identity in identities],
        "sources": [identity_source(item) for item in sources],
        "transitions": transitions,
    }


def authority_candidate(item):
    declaration = item["declaration"]
    return {
        "source_path": item["source_path"],
        "semantic_id": item["semantic_id"],
        "profile": item["profile"],
        "kind": declaration["kind"],
        "state": item["state"],
        "scope": normalize_scope(declaration["scope"]) if "scope" in declaration else {},
        "relations": normalize_relations(declaration["relations"]) if "relations" in declaration else [],
        "governed_action_classes": unique(declaration["governed_action_classes"])
            if "governed_action_classes" in declaration else [],
        "members": unique(declaration["members"]) if "members" in declaration else [],
        "combination_semantics": declaration["combination_semantics"]
            if "combination_semantics" in declaration else None,
        "effective_from": declaration["effective_from"] if "effective_from" in declaration else None,
        "effective_to": declaration["effective_to"] if "effective_to" in declaration else None,
        "authority_from": declaration["authority_from"] if "authority_from" in declaration else None,
        "authority_to": declaration["authority_to"] if "authority_to" in declaration else None,
        "content_digest": item["content_digest"],
        "declaration": declaration,
    }


def authority_index(inputs):
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "resolution_note": "Candidate/index inputs only; task-scoped authority remains resolver-owned",
        "candidates": [authority_candidate(item) for item in inputs
                       if item["authority_class"] == "canonical"
                       and item["state"] != "SUPERSEDED"
                       and item["profile"] != "identity_transition.v1"],
    }


def workstream_dependency_closure(workstreams, identity):
    closure = []
    frontier = [identity]
    visited = []
    while frontier:
        current = frontier[0]
        frontier = frontier[1:]
        if current in visited:
            continue
        visited = visited + [current]
        matches = [row for row in workstreams if row[0] == current]
        if length(matches) != 1:
            fail_view("WORKSTREAM_VIEW_REFERENCE", "Workstream graph dependency must resolve exactly once")
        declaration = matches[0][1]
        dependencies = unique(declaration["depends_on"]) if "depends_on" in declaration else []
        for dependency in dependencies:
            if dependency not in closure:
                closure = closure + [dependency]
                frontier = frontier + [dependency]
    return unique(closure)


def workstream_parent_chain(workstreams, contexts, identity):
    chain = []
    current = identity
    limit = length(workstreams) + length(contexts) + 1
    steps = 0
    while steps < limit:
        matches = [row for row in workstreams if row[0] == current]
        if length(matches) != 1:
            return chain
        declaration = matches[0][1]
        if "parent" not in declaration:
            return chain
        parent = declaration["parent"]
        if parent in chain or parent == identity:
            fail_view("WORKSTREAM_VIEW_PARENT_CYCLE", "Workstream graph contains a parent cycle")
        if parent not in contexts:
            fail_view("WORKSTREAM_VIEW_REFERENCE", "Workstream parent must resolve in current context")
        chain = chain + [parent]
        current = parent
        steps = steps + 1
    fail_view("WORKSTREAM_VIEW_PARENT_CYCLE", "Workstream parent chain exceeds bounded corpus")


def workstream_node(workstreams, contexts, identity):
    matches = [row for row in workstreams if row[0] == identity]
    if length(matches) != 1:
        fail_view("WORKSTREAM_VIEW_IDENTITY", "Workstream identity must resolve exactly once")
    declaration = matches[0][1]
    source_path = matches[0][2]
    closure = dependency_closure(workstreams, identity)
    blockers = []
    for dependency in closure:
        target = [row for row in workstreams if row[0] == dependency]
        if length(target) != 1:
            fail_view("WORKSTREAM_VIEW_REFERENCE", "Workstream dependency must resolve exactly once")
        if target[0][1]["state"] != "COMPLETED":
            blockers = blockers + [dependency]
    state = declaration["state"]
    readiness = state
    if state == "ACTIVE":
        readiness = "RUNNABLE" if length(blockers) == 0 else "DEPENDENCY_BLOCKED"
    return {
        "semantic_id": identity,
        "source_path": source_path,
        "state": state,
        "readiness": readiness,
        "objective": declaration["objective"] if "objective" in declaration else None,
        "parent": declaration["parent"] if "parent" in declaration else None,
        "parent_chain": parent_chain(workstreams, contexts, identity),
        "depends_on": unique(declaration["depends_on"]) if "depends_on" in declaration else [],
        "dependency_closure": closure,
        "dependency_blockers": unique(blockers),
        "expected_to_resume": declaration["expected_to_resume"]
            if "expected_to_resume" in declaration else False,
        "pause_reason": declaration["pause_reason"] if "pause_reason" in declaration else None,
        "return_condition": declaration["return_condition"] if "return_condition" in declaration else None,
        "resume_target": declaration["resume_target"] if "resume_target" in declaration else None,
        "current_anchor": declaration["current_anchor"] if "current_anchor" in declaration else (
            declaration["execution_anchor"]["current_boundary"] if "execution_anchor" in declaration else None),
        "risk_or_reopen_triggers": unique(declaration["risk_or_reopen_triggers"])
            if "risk_or_reopen_triggers" in declaration else [],
        "temporal": temporal(declaration),
    }


def workstream_graph(inputs):
    workstreams = sorted_values([
        (item["semantic_id"], item["declaration"], item["source_path"])
        for item in inputs
        if item["profile"] == "workstream.v1"
        and item["authority_class"] == "canonical"
        and item["state"] != "SUPERSEDED"
    ])
    if any_true([row[0] == None for row in workstreams]):
        fail_view("WORKSTREAM_VIEW_IDENTITY", "Workstream graph requires authored semantic identities")
    identities = [row[0] for row in workstreams]
    if length(unique(identities)) != length(identities):
        fail_view("WORKSTREAM_VIEW_IDENTITY", "Workstream graph identities must be unique")
    contexts = unique([
        item["semantic_id"] for item in inputs
        if item["authority_class"] == "canonical"
        and item["state"] != "SUPERSEDED"
        and item["semantic_id"] != None
    ])
    nodes = [node(workstreams, contexts, identity) for identity in identities]
    temporal_required = any_true([entry["temporal"] == True for entry in nodes])
    ready = [] if temporal_required else unique([
        entry["semantic_id"] for entry in nodes if entry["readiness"] == "RUNNABLE"
    ])
    ancestor_context = unique([
        ancestor for entry in nodes if entry["semantic_id"] in ready
        for ancestor in entry["parent_chain"]
    ])
    branches = unique([identity for identity in ready if identity not in ancestor_context])
    disposition = "TEMPORAL_CONTEXT_REQUIRED" if temporal_required else (
        "NO_READY_WORKSTREAM" if length(ready) == 0 else (
            "UNIQUE_PRIMARY_ROUTE" if length(branches) == 1 else "NO_UNIQUE_PRIMARY_ROUTE"
        )
    )
    primary = branches[0] if disposition == "UNIQUE_PRIMARY_ROUTE" else None
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "nodes": nodes,
        "active_ready_set": ready,
        "route": {
            "disposition": disposition,
            "primary": primary,
            "branches": branches,
        },
        "temporal_context_required": temporal_required,
    }


def subject_memberships(item):
    declaration = item["declaration"]
    identity = item["semantic_id"]
    rows = [
        ("profile", item["profile"], identity if identity != None else "", item["source_path"]),
        ("kind", declaration["kind"], identity if identity != None else "", item["source_path"]),
    ]
    if "scope" in declaration:
        for facet in sorted_values(declaration["scope"]):
            value = declaration["scope"][facet]
            values = [value] if is_text(value) else unique(value)
            for member in values:
                rows = rows + [("scope:" + facet, member,
                                identity if identity != None else "", item["source_path"])]
    return rows


def subject_index(inputs):
    keyed = []
    for item in inputs:
        if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED":
            keyed = keyed + memberships(item)
    rows = []
    for axis, value, identity, path in sorted_values(keyed):
        rows = rows + [{
            "axis": axis,
            "value": value,
            "semantic_id": identity if identity != "" else None,
            "source_path": path,
        }]
    return {"schema_version": "1", "authority_class": "derived", "memberships": rows}


def obligation_rows(item):
    declaration = item["declaration"]
    rows = []
    if item["profile"] == "governing_procedure.v1" and item["state"] == "ACTIVE":
        categories = [
            ("PRECONDITION", "preconditions"),
            ("PROHIBITION", "prohibitions"),
            ("POSTCONDITION", "required_postconditions"),
            ("FAIL_CLOSED", "fail_closed_conditions"),
        ]
        for category, field in categories:
            values = declaration[field]
            for ordinal in sequence_range(length(values)):
                rows = rows + [{
                    "source_path": item["source_path"],
                    "semantic_id": item["semantic_id"],
                    "category": category,
                    "ordinal": ordinal,
                    "constraint_id": None,
                    "requirement": values[ordinal],
                }]
        constraints = declaration["mandatory_constraints"]
        for ordinal in sequence_range(length(constraints)):
            constraint = constraints[ordinal]
            rows = rows + [{
                "source_path": item["source_path"],
                "semantic_id": item["semantic_id"],
                "category": "MANDATORY_CONSTRAINT",
                "ordinal": ordinal,
                "constraint_id": constraint["constraint_id"],
                "requirement": constraint["requirement"],
            }]
    if item["profile"] == "workstream.v1" and "expected_to_resume" in declaration:
        if (item["state"] in ["PAUSED", "BLOCKED"]
                and declaration["expected_to_resume"] == True
                and "return_condition" in declaration):
            rows = rows + [{
                "source_path": item["source_path"],
                "semantic_id": item["semantic_id"],
                "category": "RETURN_CONDITION",
                "ordinal": 0,
                "constraint_id": None,
                "requirement": declaration["return_condition"],
            }]
    return rows


def risk_obligation_index(inputs):
    risks = []
    obligations = []
    for item in inputs:
        if item["authority_class"] == "canonical" and item["state"] != "SUPERSEDED":
            declaration = item["declaration"]
            if "risk_or_reopen_triggers" in declaration:
                for trigger in unique(declaration["risk_or_reopen_triggers"]):
                    risks = risks + [{
                        "source_path": item["source_path"],
                        "semantic_id": item["semantic_id"],
                        "trigger": trigger,
                    }]
            obligations = obligations + obligations_for(item)
    risk_keyed = sorted_values([
        (row["trigger"], row["semantic_id"] if row["semantic_id"] != None else "",
         row["source_path"], row) for row in risks
    ])
    obligation_keyed = sorted_values([
        (row["source_path"], row["category"], row["ordinal"],
         row["constraint_id"] if row["constraint_id"] != None else "", row) for row in obligations
    ])
    return {
        "schema_version": "1",
        "authority_class": "derived",
        "risks": [row for trigger, identity, path, row in risk_keyed],
        "obligations": [row for path, category, ordinal, constraint_id, row in obligation_keyed],
    }


def current_state_core_markdown(value):
    active = value["active_workstream"]
    boundary = value["integration_boundary"]
    experiment = value["current_experiment"]
    text = "# Current State Core\n\n"
    text = text + "## Active workstream\n\n"
    text = text + "- Semantic ID: " + active["semantic_id"] + "\n"
    text = text + "- State: " + active["state"] + "\n"
    text = text + "- Objective: " + active["objective"] + "\n"
    text = text + "- Stage: " + active["stage"]["stage_id"] + "\n"
    text = text + "- Checkpoint: " + as_text(active["execution_anchor"]["checkpoint"]) + "\n\n"
    text = text + "## Integration boundary\n\n"
    text = text + "- Semantic ID: " + boundary["semantic_id"] + "\n"
    text = text + "- Promoted branch: " + boundary["promoted_branch"] + "\n"
    text = text + "- Promoted commit: " + boundary["promoted_commit"] + "\n\n"
    text = text + "## Current specification and experiment\n\n"
    text = text + "- Specification: " + value["current_specification"]["semantic_id"] + "\n"
    text = text + "- Experiment: " + experiment["semantic_id"] + "\n"
    text = text + "- Outcome: " + experiment["outcome"] + "\n\n"
    text = text + "## Paused resumable workstreams\n\n"
    if length(value["paused_workstreams"]) == 0:
        text = text + "None.\n"
    else:
        for workstream in value["paused_workstreams"]:
            text = text + "- " + workstream["semantic_id"] + " -> " + workstream["resume_target"] + "\n"
    return utf8_text(text)
