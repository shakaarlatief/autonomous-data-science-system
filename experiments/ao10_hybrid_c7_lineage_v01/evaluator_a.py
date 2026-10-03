ALLOWED_CLASSES = {"CARRY_FORWARD","REPLACE","SPLIT","MERGE","RETIRE"}
ALLOWED_DISPOSITIONS = {"FULLY_MAPPED","PARTIAL_WITH_EXPLICIT_RETIREMENT"}

def evaluate(fixture):
    corpus = {r["requirement_id"]: r for r in fixture["requirements"] if r.get("accepted", False)}
    retirements = {r["retirement_ref"]: r for r in fixture.get("accepted_retirements", [])}
    relations = fixture["relations"]

    authority_valid = all(r.get("authority_valid", False) for r in relations)
    effective_boundary_valid = all(r.get("effective_boundary_valid", False) for r in relations)
    continuity_valid = True
    structural_valid = True
    retired_remainders = set()

    def retirement_ok(ref):
        row = retirements.get(ref)
        return bool(row and row.get("authority_valid") and row.get("evidence_valid"))

    for relation in relations:
        cls = relation["relation_class"]
        preds = relation["predecessors"]
        succs = relation["successors"]
        if cls not in ALLOWED_CLASSES or not relation.get("provenance"):
            structural_valid = False
        if len(set(preds)) != len(preds) or len(set(succs)) != len(succs):
            structural_valid = False
        if any(x not in corpus for x in preds + succs):
            structural_valid = False

        if cls == "CARRY_FORWARD":
            card = len(preds) == 1 and len(succs) == 1 and preds == succs
            digest_ok = (
                relation.get("semantic_digest_before") == relation.get("semantic_digest_after")
                and preds
                and relation.get("semantic_digest_before") == corpus.get(preds[0], {}).get("semantic_digest")
            )
            continuity_valid = continuity_valid and card and digest_ok
            structural_valid = structural_valid and card
        elif cls == "REPLACE":
            structural_valid = structural_valid and len(preds) == 1 and len(succs) == 1 and preds != succs
        elif cls == "SPLIT":
            structural_valid = structural_valid and len(preds) == 1 and len(succs) >= 2
        elif cls == "MERGE":
            structural_valid = structural_valid and len(preds) >= 2 and len(succs) == 1
        elif cls == "RETIRE":
            structural_valid = structural_valid and len(preds) >= 1 and len(succs) == 0
            structural_valid = structural_valid and bool(relation.get("retirement_evidence_ref"))
            structural_valid = structural_valid and retirement_ok(relation.get("retirement_ref"))

        if cls in {"REPLACE","SPLIT","MERGE"}:
            dispositions = relation.get("predecessor_dispositions", {})
            if set(dispositions) != set(preds):
                structural_valid = False
            for pred in preds:
                row = dispositions.get(pred, {})
                if row.get("disposition") not in ALLOWED_DISPOSITIONS:
                    structural_valid = False
                if row.get("disposition") == "PARTIAL_WITH_EXPLICIT_RETIREMENT":
                    ref = row.get("retirement_ref")
                    retired_remainders.add(ref)
                    if not retirement_ok(ref):
                        structural_valid = False

    outgoing = {}
    edges = {}
    retired = set()
    for relation in relations:
        cls = relation["relation_class"]
        if cls == "CARRY_FORWARD":
            continue
        for pred in relation["predecessors"]:
            outgoing.setdefault(pred, []).append(relation["relation_id"])
        if cls == "RETIRE":
            retired.update(relation["predecessors"])
        else:
            for pred in relation["predecessors"]:
                edges.setdefault(pred, set()).update(relation["successors"])

    conflict = any(len(ids) > 1 for ids in outgoing.values())

    nodes = set(corpus)
    state = {}
    cycle = False
    def visit(node):
        nonlocal cycle
        state[node] = 1
        for target in edges.get(node, ()):
            if state.get(target) == 1:
                cycle = True
            elif state.get(target, 0) == 0:
                visit(target)
        state[node] = 2
    for node in sorted(nodes):
        if state.get(node, 0) == 0:
            visit(node)

    accounted = set(fixture.get("unaffected_predecessors", []))
    for relation in relations:
        accounted.update(relation["predecessors"])
    scope = set(fixture["transition_scope_predecessors"])
    unmapped = sorted(scope - accounted)

    valid = (
        structural_valid
        and authority_valid
        and effective_boundary_valid
        and continuity_valid
        and not conflict
        and not cycle
        and not unmapped
    )

    current = {}
    if valid:
        carry = {
            r["predecessors"][0]
            for r in relations
            if r["relation_class"] == "CARRY_FORWARD"
        }
        unaffected = set(fixture.get("unaffected_predecessors", []))
        def terminal_targets(start):
            if start in unaffected or start in carry:
                return {start}
            if start in retired:
                return set()
            seen = set()
            stack = [start]
            terminals = set()
            while stack:
                node = stack.pop()
                if node in seen:
                    continue
                seen.add(node)
                targets = edges.get(node, set())
                if not targets:
                    if node != start:
                        terminals.add(node)
                else:
                    stack.extend(targets)
            return terminals
        for pred in sorted(scope):
            current[pred] = sorted(terminal_targets(pred))

    return {
        "valid": valid,
        "review_required": not valid,
        "authority_valid": authority_valid,
        "effective_boundary_valid": effective_boundary_valid,
        "continuity_valid": continuity_valid,
        "conflict": conflict,
        "cycle": cycle,
        "unmapped": unmapped,
        "current_targets_by_predecessor": current,
        "retired": sorted(retired) if valid else [],
        "retired_remainder_refs": sorted(x for x in retired_remainders if x) if valid else [],
    }
