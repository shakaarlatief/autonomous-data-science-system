from collections import Counter, defaultdict

ALLOWED_MODES = {"CONTINUITY", "OPEN_RESET", "CARRY_FACTS_FOR_REVALIDATION"}


def _init(successor_id, mode="OPEN_RESET", carried_components=None, deferral_rebound=False):
    return {
        "successor_id": successor_id,
        "mode": mode,
        "carried_components": sorted(carried_components or []),
        "deferral_rebound": bool(deferral_rebound),
    }


def _portion_key(row):
    return (row["source_effect_id"], row["source_portion"])


def _target_key(row):
    return (row["target_effect_id"], row["target_portion"])


def _relation_validation(fixture):
    relation_type = fixture["relation_type"]
    predecessors = {x["effect_id"]: x for x in fixture["predecessors"]}
    successors = {x["effect_id"]: x for x in fixture["successors"]}
    reasons = []

    if relation_type == "REPARTITION":
        if len(predecessors) < 2 or len(successors) < 2:
            reasons.append("REPARTITION_CARDINALITY_INVALID")

        source_inventory = {
            (p["effect_id"], portion)
            for p in predecessors.values()
            for portion in p["source_portions"]
        }
        target_inventory = {
            (s["effect_id"], portion)
            for s in successors.values()
            for portion in s["target_portions"]
        }

        mapping_source = []
        mapping_target = []
        target_ids_by_predecessor = defaultdict(set)

        for row in fixture["mapping"]:
            sk = _portion_key(row)
            tk = _target_key(row)
            mapping_source.append(sk)
            mapping_target.append(tk)

            if sk not in source_inventory:
                reasons.append("UNKNOWN_SOURCE_PORTION")
            if tk not in target_inventory:
                reasons.append("UNKNOWN_TARGET_PORTION")
            if row["source_effect_id"] in predecessors and row["target_effect_id"] in successors:
                target_ids_by_predecessor[row["source_effect_id"]].add(row["target_effect_id"])

        mapped_counts = Counter(mapping_source)
        if any(count > 1 for count in mapped_counts.values()):
            reasons.append("SOURCE_PORTION_DOUBLE_MAPPED")

        retired = {
            (x["source_effect_id"], x["source_portion"])
            for x in fixture["retired_source_portions"]
        }
        unaffected = {
            (x["source_effect_id"], x["source_portion"])
            for x in fixture["unaffected_source_portions"]
        }
        accounted = set(mapping_source) | retired | unaffected
        if source_inventory - accounted:
            reasons.append("UNACCOUNTED_SOURCE_PORTION")
        if accounted - source_inventory:
            reasons.append("UNKNOWN_ACCOUNTED_SOURCE_PORTION")

        if target_inventory - set(mapping_target):
            reasons.append("UNSUPPLIED_TARGET_PORTION")

        for predecessor_id, target_ids in target_ids_by_predecessor.items():
            if len(target_ids) > 1:
                boundaries = {
                    successors[target_id]["effective_boundary"]
                    for target_id in target_ids
                }
                if len(boundaries) > 1:
                    reasons.append("ATOMIC_PREDECESSOR_STAGGER")

    elif relation_type == "REINSTATE":
        if len(predecessors) != 1 or len(successors) != 1:
            reasons.append("REINSTATE_CARDINALITY_INVALID")
        else:
            predecessor = next(iter(predecessors.values()))
            successor = next(iter(successors.values()))
            if predecessor["status"] != "RETIRED":
                reasons.append("REINSTATE_PREDECESSOR_NOT_RETIRED")
            if predecessor["effect_id"] == successor["effect_id"]:
                reasons.append("REINSTATE_REUSES_RETIRED_ID")

    elif relation_type == "REPLACE":
        if len(predecessors) != 1 or len(successors) != 1:
            reasons.append("REPLACE_CARDINALITY_INVALID")

    elif relation_type == "CARRY_FORWARD":
        if len(predecessors) != 1 or len(successors) != 1:
            reasons.append("CARRY_FORWARD_CARDINALITY_INVALID")
        else:
            predecessor = next(iter(predecessors.values()))
            successor = next(iter(successors.values()))
            if predecessor["effect_id"] != successor["effect_id"]:
                reasons.append("CARRY_FORWARD_IDENTITY_CHANGED")
            if fixture["semantic_digest_unchanged"] is not True:
                reasons.append("CARRY_FORWARD_SEMANTIC_CHANGE")
            if fixture["carrier_revision_valid"] is not True:
                reasons.append("CARRY_FORWARD_REVISION_INVALID")

    else:
        reasons.append("UNSUPPORTED_RELATION_TYPE")

    return len(reasons) == 0, sorted(set(reasons))


def _current_effect_ids(fixture, relation_valid):
    predecessors = {x["effect_id"]: x for x in fixture["predecessors"]}
    successors = {x["effect_id"]: x for x in fixture["successors"]}
    evaluation_boundary = fixture["evaluation_boundary"]

    if not relation_valid:
        return sorted(
            p["effect_id"] for p in predecessors.values()
            if p["status"] == "ACTIVE"
        )

    relation_type = fixture["relation_type"]

    if relation_type == "CARRY_FORWARD":
        predecessor = next(iter(predecessors.values()))
        return [predecessor["effect_id"]]

    if relation_type == "REINSTATE":
        return sorted(
            s["effect_id"] for s in successors.values()
            if s["effective_boundary"] <= evaluation_boundary
        )

    if relation_type == "REPLACE":
        predecessor = next(iter(predecessors.values()))
        successor = next(iter(successors.values()))
        if successor["effective_boundary"] <= evaluation_boundary:
            return [successor["effect_id"]]
        return [predecessor["effect_id"]] if predecessor["status"] == "ACTIVE" else []

    if relation_type == "REPARTITION":
        current = {
            s["effect_id"] for s in successors.values()
            if s["effective_boundary"] <= evaluation_boundary
        }

        mapping_by_predecessor = defaultdict(list)
        for row in fixture["mapping"]:
            mapping_by_predecessor[row["source_effect_id"]].append(row)

        unaffected_by_predecessor = defaultdict(set)
        for row in fixture["unaffected_source_portions"]:
            unaffected_by_predecessor[row["source_effect_id"]].add(row["source_portion"])

        for predecessor in predecessors.values():
            if predecessor["status"] != "ACTIVE":
                continue
            pid = predecessor["effect_id"]
            if unaffected_by_predecessor[pid]:
                current.add(pid)
                continue

            rows = mapping_by_predecessor[pid]
            all_effective = all(
                successors[row["target_effect_id"]]["effective_boundary"] <= evaluation_boundary
                for row in rows
            )
            if not all_effective:
                current.add(pid)

        return sorted(current)

    return []


def _carry_validation(fixture):
    carry = fixture["carry"]
    if not carry["present"]:
        return True, [], defaultdict(list)

    predecessors = {x["effect_id"]: x for x in fixture["predecessors"]}
    successors = {x["effect_id"]: x for x in fixture["successors"]}
    reasons = []

    if not carry["authority_valid"]:
        reasons.append("CARRY_AUTHORITY_INVALID")
    if not carry["effective_boundary_valid"]:
        reasons.append("CARRY_BOUNDARY_INVALID")
    if not fixture["source_realization_facts_current"]:
        reasons.append("CARRY_SOURCE_FACTS_NOT_CURRENT")
    if not fixture["source_realization_facts_fresh"]:
        reasons.append("CARRY_STALE_FACTS")

    source_keys = []
    target_keys = []
    carried = defaultdict(list)

    for row in carry["component_mapping"]:
        source_keys.append((row["source_effect_id"], row["source_component"]))
        target_keys.append((row["target_effect_id"], row["target_component"]))

        predecessor = predecessors.get(row["source_effect_id"])
        successor = successors.get(row["target_effect_id"])

        if predecessor is None or row["source_component"] not in predecessor["realization_components"]:
            reasons.append("CARRY_UNKNOWN_SOURCE_COMPONENT")
        if successor is None or row["target_component"] not in successor["required_components"]:
            reasons.append("CARRY_UNKNOWN_TARGET_COMPONENT")
        if successor is not None:
            carried[row["target_effect_id"]].append(row["target_component"])

    if any(count > 1 for count in Counter(source_keys).values()):
        reasons.append("CARRY_SOURCE_COMPONENT_DOUBLE_MAPPED")
    if any(count > 1 for count in Counter(target_keys).values()):
        reasons.append("CARRY_TARGET_COMPONENT_DOUBLE_MAPPED")

    for successor_id, components in carried.items():
        successor = successors[successor_id]
        if successor["qualification_required"] and not carry["qualification_rechecked"]:
            reasons.append("CARRY_QUALIFICATION_NOT_RECHECKED")

    return len(reasons) == 0, sorted(set(reasons)), carried


def evaluate_fixture(fixture):
    relation_valid, relation_reasons = _relation_validation(fixture)

    if not relation_valid:
        return {
            "fixture_id": fixture["fixture_id"],
            "relation_valid": False,
            "current_effect_ids": _current_effect_ids(fixture, False),
            "successor_initialization": [],
            "review_required": True,
            "reason_codes": relation_reasons,
        }

    relation_type = fixture["relation_type"]
    successors = sorted(fixture["successors"], key=lambda x: x["effect_id"])
    inits = []
    reasons = []
    review_required = False

    if relation_type == "CARRY_FORWARD":
        predecessor = fixture["predecessors"][0]
        facts_ok = (
            fixture["source_realization_facts_current"]
            and fixture["source_realization_facts_fresh"]
        )
        carried = predecessor["realization_components"] if facts_ok else []
        if not fixture["source_realization_facts_current"]:
            reasons.append("CONTINUITY_SOURCE_FACTS_NOT_CURRENT")
            review_required = True
        if not fixture["source_realization_facts_fresh"]:
            reasons.append("CONTINUITY_STALE_FACTS")
            review_required = True
        inits.append(_init(
            predecessor["effect_id"],
            "CONTINUITY",
            carried,
            predecessor["deferral_active"],
        ))
    else:
        carry_valid, carry_reasons, carried_by_successor = _carry_validation(fixture)
        if fixture["carry"]["present"] and not carry_valid:
            reasons.extend(carry_reasons)
            review_required = True

        for successor in successors:
            successor_id = successor["effect_id"]
            deferral_rebound = bool(
                fixture["successor_deferral_reaccepted"].get(successor_id, False)
            )
            if fixture["carry"]["present"] and carry_valid:
                inits.append(_init(
                    successor_id,
                    "CARRY_FACTS_FOR_REVALIDATION",
                    carried_by_successor.get(successor_id, []),
                    deferral_rebound,
                ))
            else:
                inits.append(_init(
                    successor_id,
                    "OPEN_RESET",
                    [],
                    deferral_rebound,
                ))

    return {
        "fixture_id": fixture["fixture_id"],
        "relation_valid": True,
        "current_effect_ids": _current_effect_ids(fixture, True),
        "successor_initialization": sorted(inits, key=lambda x: x["successor_id"]),
        "review_required": review_required,
        "reason_codes": sorted(set(reasons)),
    }
