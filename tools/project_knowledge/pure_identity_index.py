"""Restricted identity-index units: declarations only."""


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
