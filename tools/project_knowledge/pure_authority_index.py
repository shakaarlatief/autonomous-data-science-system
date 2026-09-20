"""Restricted authority-index units: declarations only."""


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
