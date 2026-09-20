"""Restricted workstream-graph units: declarations only."""


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
