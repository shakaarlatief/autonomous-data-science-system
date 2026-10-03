from collections import defaultdict, deque

VALID_CLASSES = frozenset(("CARRY_FORWARD","REPLACE","SPLIT","MERGE","RETIRE"))
VALID_DISPOSITIONS = frozenset(("FULLY_MAPPED","PARTIAL_WITH_EXPLICIT_RETIREMENT"))

def evaluate(fixture):
    accepted = {
        row["requirement_id"]: row["semantic_digest"]
        for row in fixture["requirements"]
        if row.get("accepted", False)
    }
    retirement_table = {
        row["retirement_ref"]: (
            bool(row.get("authority_valid")),
            bool(row.get("evidence_valid")),
        )
        for row in fixture.get("accepted_retirements", [])
    }

    normalized = []
    continuity_valid = True
    structural_valid = True
    authority_bits = []
    boundary_bits = []
    retired_remainders = set()
    retired_nodes = set()

    for r in fixture["relations"]:
        cls = r["relation_class"]
        preds = tuple(r["predecessors"])
        succs = tuple(r["successors"])
        authority_bits.append(bool(r.get("authority_valid")))
        boundary_bits.append(bool(r.get("effective_boundary_valid")))

        if cls not in VALID_CLASSES or not r.get("provenance"):
            structural_valid = False
        if len(preds) != len(set(preds)) or len(succs) != len(set(succs)):
            structural_valid = False
        if any(x not in accepted for x in preds + succs):
            structural_valid = False

        if cls == "CARRY_FORWARD":
            shape_ok = len(preds) == len(succs) == 1 and preds == succs
            digest_ok = bool(preds) and (
                r.get("semantic_digest_before") == r.get("semantic_digest_after") == accepted.get(preds[0])
            )
            continuity_valid = continuity_valid and shape_ok and digest_ok
            structural_valid = structural_valid and shape_ok
        elif cls == "REPLACE":
            structural_valid = structural_valid and len(preds) == len(succs) == 1 and preds != succs
        elif cls == "SPLIT":
            structural_valid = structural_valid and len(preds) == 1 and len(succs) >= 2
        elif cls == "MERGE":
            structural_valid = structural_valid and len(preds) >= 2 and len(succs) == 1
        elif cls == "RETIRE":
            structural_valid = structural_valid and len(preds) >= 1 and not succs
            rr = r.get("retirement_ref")
            ev = r.get("retirement_evidence_ref")
            ok = retirement_table.get(rr) == (True, True)
            structural_valid = structural_valid and bool(ev) and ok
            retired_nodes.update(preds)

        if cls in {"REPLACE","SPLIT","MERGE"}:
            disp = r.get("predecessor_dispositions", {})
            if frozenset(disp) != frozenset(preds):
                structural_valid = False
            for pred in preds:
                row = disp.get(pred, {})
                kind = row.get("disposition")
                if kind not in VALID_DISPOSITIONS:
                    structural_valid = False
                elif kind == "PARTIAL_WITH_EXPLICIT_RETIREMENT":
                    ref = row.get("retirement_ref")
                    retired_remainders.add(ref)
                    if retirement_table.get(ref) != (True, True):
                        structural_valid = False

        normalized.append((r["relation_id"], cls, preds, succs))

    authority_valid = all(authority_bits)
    effective_boundary_valid = all(boundary_bits)

    semantic_rows = [row for row in normalized if row[1] != "CARRY_FORWARD"]
    by_pred = defaultdict(set)
    adjacency = defaultdict(set)
    for relation_id, cls, preds, succs in semantic_rows:
        for pred in preds:
            by_pred[pred].add(relation_id)
            if cls != "RETIRE":
                adjacency[pred].update(succs)

    conflict = any(len(v) > 1 for v in by_pred.values())

    indegree = {node: 0 for node in accepted}
    for pred, succs in adjacency.items():
        for succ in succs:
            indegree[succ] = indegree.get(succ, 0) + 1
            indegree.setdefault(pred, indegree.get(pred, 0))
    q = deque(sorted(node for node, degree in indegree.items() if degree == 0))
    visited = 0
    local = dict(indegree)
    while q:
        node = q.popleft()
        visited += 1
        for succ in sorted(adjacency.get(node, ())):
            local[succ] -= 1
            if local[succ] == 0:
                q.append(succ)
    cycle = visited != len(indegree)

    scoped = frozenset(fixture["transition_scope_predecessors"])
    accounted = set(fixture.get("unaffected_predecessors", []))
    for _, _, preds, _ in normalized:
        accounted.update(preds)
    unmapped = sorted(scoped.difference(accounted))

    valid = all((
        structural_valid,
        authority_valid,
        effective_boundary_valid,
        continuity_valid,
        not conflict,
        not cycle,
        not unmapped,
    ))

    current = {}
    if valid:
        carry = frozenset(
            row[2][0] for row in normalized
            if row[1] == "CARRY_FORWARD"
        )
        unaffected = frozenset(fixture.get("unaffected_predecessors", []))
        for origin in sorted(scoped):
            if origin in unaffected or origin in carry:
                current[origin] = [origin]
                continue
            if origin in retired_nodes:
                current[origin] = []
                continue
            reachable = set()
            frontier = list(adjacency.get(origin, ()))
            while frontier:
                node = frontier.pop()
                if node in reachable:
                    continue
                reachable.add(node)
                next_nodes = adjacency.get(node, set())
                if next_nodes:
                    frontier.extend(next_nodes)
            terminals = sorted(
                node for node in reachable
                if not adjacency.get(node) and node not in retired_nodes
            )
            current[origin] = terminals

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
        "retired": sorted(retired_nodes) if valid else [],
        "retired_remainder_refs": sorted(x for x in retired_remainders if x) if valid else [],
    }
