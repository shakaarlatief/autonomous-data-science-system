"""HYBRID_D2_LINEAGE_EXTENSION_V01 - Evaluator B (independently authored by Claude / claude-04).

Authored only from:
    docs/research/482_d2_extended_lineage_realization_succession_protocol.md
    experiments/ao10_hybrid_d2_lineage_v01/reviewer_fixtures.json
    experiments/ao10_hybrid_d2_lineage_v01/evaluator_contract.json

Standard library only. Deterministic. No file, network or model access.
No free-text semantic adjudication: only structured fixture fields are consumed.
"""

SEMANTIC_SUCCESSION_TYPES = ("REPLACE", "REPARTITION", "REINSTATE")
SUPPORTED_TYPES = ("CARRY_FORWARD",) + SEMANTIC_SUCCESSION_TYPES

MODE_CONTINUITY = "CONTINUITY"
MODE_OPEN_RESET = "OPEN_RESET"
MODE_CARRY = "CARRY_FACTS_FOR_REVALIDATION"


def _ids(items):
    return [item.get("effect_id") for item in items]


def _validate_repartition(predecessors, successors, fixture, reasons):
    """Section 3-5 structural rules for REPARTITION. Returns True if valid."""
    valid = True
    if len(predecessors) < 2 or len(successors) < 2:
        reasons.add("REPARTITION_CARDINALITY_INVALID")
        valid = False

    pred_portions = {}
    for p in predecessors:
        if p.get("status") != "ACTIVE":
            reasons.add("PREDECESSOR_NOT_ACTIVE")
            valid = False
        pred_portions[p.get("effect_id")] = list(p.get("source_portions") or [])

    succ_portions = {}
    succ_boundary = {}
    for s in successors:
        succ_portions[s.get("effect_id")] = list(s.get("target_portions") or [])
        succ_boundary[s.get("effect_id")] = s.get("effective_boundary")

    # Count how many times each (predecessor, portion) is accounted for.
    accounted = {}
    supplied_targets = set()
    for row in fixture.get("mapping") or []:
        src_id = row.get("source_effect_id")
        src_portion = row.get("source_portion")
        tgt_id = row.get("target_effect_id")
        tgt_portion = row.get("target_portion")
        if (
            src_id not in pred_portions
            or src_portion not in pred_portions[src_id]
            or tgt_id not in succ_portions
            or tgt_portion not in succ_portions[tgt_id]
        ):
            reasons.add("MAPPING_REFERENCE_INVALID")
            valid = False
            continue
        key = (src_id, src_portion)
        accounted[key] = accounted.get(key, 0) + 1
        supplied_targets.add((tgt_id, tgt_portion))

    mapped_keys = set(accounted)
    for row_list, code in (
        (fixture.get("retired_source_portions") or [], "RETIRED"),
        (fixture.get("unaffected_source_portions") or [], "UNAFFECTED"),
    ):
        for entry in row_list:
            src_id = entry.get("source_effect_id") if isinstance(entry, dict) else None
            src_portion = entry.get("source_portion") if isinstance(entry, dict) else None
            if src_id not in pred_portions or src_portion not in pred_portions[src_id]:
                reasons.add("MAPPING_REFERENCE_INVALID")
                valid = False
                continue
            key = (src_id, src_portion)
            if key in mapped_keys:
                reasons.add("SOURCE_PORTION_MULTIPLY_ACCOUNTED")
                valid = False
            accounted[key] = accounted.get(key, 0) + 1

    for src_id in sorted(pred_portions):
        for portion in pred_portions[src_id]:
            count = accounted.get((src_id, portion), 0)
            if count == 0:
                reasons.add("SOURCE_PORTION_UNACCOUNTED")
                valid = False
            elif count > 1:
                if (src_id, portion) in mapped_keys and _mapping_count(fixture, src_id, portion) > 1:
                    reasons.add("SOURCE_PORTION_MAPPED_TWICE")
                else:
                    reasons.add("SOURCE_PORTION_MULTIPLY_ACCOUNTED")
                valid = False

    for tgt_id in sorted(succ_portions):
        for portion in succ_portions[tgt_id]:
            if (tgt_id, portion) not in supplied_targets:
                reasons.add("TARGET_PORTION_UNSUPPLIED")
                valid = False

    # Section 5 atomic predecessor / effective-boundary rule.
    for src_id in sorted(pred_portions):
        targets = set()
        for row in fixture.get("mapping") or []:
            if row.get("source_effect_id") == src_id and row.get("target_effect_id") in succ_boundary:
                targets.add(row.get("target_effect_id"))
        if len(targets) > 1:
            boundaries = set(succ_boundary[t] for t in targets)
            if len(boundaries) > 1:
                reasons.add("ATOMIC_PREDECESSOR_STAGGERED_BOUNDARY")
                valid = False
    return valid


def _mapping_count(fixture, src_id, portion):
    count = 0
    for row in fixture.get("mapping") or []:
        if row.get("source_effect_id") == src_id and row.get("source_portion") == portion:
            count += 1
    return count


def _validate_relation(fixture, reasons):
    rtype = fixture.get("relation_type")
    predecessors = list(fixture.get("predecessors") or [])
    successors = list(fixture.get("successors") or [])
    pred_ids = _ids(predecessors)
    succ_ids = _ids(successors)

    if rtype not in SUPPORTED_TYPES:
        reasons.add("RELATION_TYPE_UNSUPPORTED")
        return False
    if not predecessors or not successors:
        reasons.add("RELATION_CARDINALITY_INVALID")
        return False
    if len(set(succ_ids)) != len(succ_ids) or len(set(pred_ids)) != len(pred_ids):
        reasons.add("DUPLICATE_EFFECT_ID")
        return False

    if rtype == "CARRY_FORWARD":
        valid = True
        if len(predecessors) != 1 or len(successors) != 1:
            reasons.add("RELATION_CARDINALITY_INVALID")
            return False
        if succ_ids[0] != pred_ids[0]:
            reasons.add("CARRY_FORWARD_IDENTITY_CHANGED")
            valid = False
        if predecessors[0].get("status") != "ACTIVE":
            reasons.add("PREDECESSOR_NOT_ACTIVE")
            valid = False
        if fixture.get("semantic_digest_unchanged") is not True:
            reasons.add("SEMANTIC_DIGEST_CHANGED")
            valid = False
        if fixture.get("carrier_revision_valid") is not True:
            reasons.add("CARRIER_REVISION_INVALID")
            valid = False
        return valid

    # Semantic succession: successors must be new identities.
    if set(succ_ids) & set(pred_ids):
        if rtype == "REINSTATE":
            reasons.add("REINSTATE_REUSES_RETIRED_IDENTITY")
        else:
            reasons.add("SUCCESSOR_REUSES_PREDECESSOR_IDENTITY")
        return False

    if rtype == "REPLACE":
        valid = True
        if len(predecessors) != 1 or len(successors) != 1:
            reasons.add("RELATION_CARDINALITY_INVALID")
            valid = False
        if any(p.get("status") != "ACTIVE" for p in predecessors):
            reasons.add("PREDECESSOR_NOT_ACTIVE")
            valid = False
        return valid

    if rtype == "REINSTATE":
        valid = True
        if any(p.get("status") != "RETIRED" for p in predecessors):
            reasons.add("REINSTATE_PREDECESSOR_NOT_RETIRED")
            valid = False
        return valid

    return _validate_repartition(predecessors, successors, fixture, reasons)


def _evaluate_carry(fixture, reasons):
    """Section 8. Returns {successor_id: set(target components)} if valid, None if
    absent, or False if present but invalid."""
    carry = fixture.get("carry") or {}
    if carry.get("present") is not True:
        return None

    predecessors = {p.get("effect_id"): p for p in fixture.get("predecessors") or []}
    successors = {s.get("effect_id"): s for s in fixture.get("successors") or []}
    ok = True
    if carry.get("authority_valid") is not True:
        reasons.add("CARRY_AUTHORITY_INVALID")
        ok = False
    if carry.get("effective_boundary_valid") is not True:
        reasons.add("CARRY_EFFECTIVE_BOUNDARY_INVALID")
        ok = False
    if fixture.get("source_realization_facts_current") is not True:
        reasons.add("CARRY_SOURCE_FACTS_NOT_CURRENT")
        ok = False
    if fixture.get("source_realization_facts_fresh") is not True:
        reasons.add("CARRY_SOURCE_FACTS_STALE")
        ok = False

    rows = list(carry.get("component_mapping") or [])
    if not rows:
        reasons.add("CARRY_MAPPING_EMPTY")
        ok = False
    seen_sources = set()
    carried = {}
    for row in rows:
        src_id = row.get("source_effect_id")
        src_comp = row.get("source_component")
        tgt_id = row.get("target_effect_id")
        tgt_comp = row.get("target_component")
        if src_id not in predecessors or src_comp not in (predecessors[src_id].get("realization_components") or []):
            reasons.add("CARRY_SOURCE_COMPONENT_UNKNOWN")
            ok = False
            continue
        if tgt_id not in successors or tgt_comp not in (successors[tgt_id].get("required_components") or []):
            reasons.add("CARRY_TARGET_COMPONENT_UNKNOWN")
            ok = False
            continue
        if (src_id, src_comp) in seen_sources:
            reasons.add("CARRY_SOURCE_COMPONENT_MAPPED_TWICE")
            ok = False
            continue
        seen_sources.add((src_id, src_comp))
        carried.setdefault(tgt_id, set()).add(tgt_comp)

    for tgt_id in sorted(carried):
        if successors[tgt_id].get("qualification_required") is True and carry.get("qualification_rechecked") is not True:
            reasons.add("CARRY_QUALIFICATION_NOT_RECHECKED")
            ok = False

    if not ok:
        reasons.add("CARRY_REJECTED")
        return False
    return carried


def _current_effect_ids(fixture, relation_valid):
    rtype = fixture.get("relation_type")
    boundary = fixture.get("evaluation_boundary")
    predecessors = list(fixture.get("predecessors") or [])
    successors = list(fixture.get("successors") or [])
    active_preds = [p.get("effect_id") for p in predecessors if p.get("status") == "ACTIVE"]

    if not relation_valid:
        # A rejected transition takes no effect: currently active predecessors stay current.
        return sorted(set(active_preds))

    def effective(succ):
        b = succ.get("effective_boundary")
        return b is not None and boundary is not None and b <= boundary

    if rtype == "CARRY_FORWARD":
        return sorted(set(active_preds))

    current = set(s.get("effect_id") for s in successors if effective(s))

    if rtype == "REINSTATE":
        return sorted(current)

    succ_by_id = {s.get("effect_id"): s for s in successors}
    if rtype == "REPLACE":
        succ = successors[0]
        if not effective(succ):
            current.update(active_preds)
        return sorted(current)

    # REPARTITION (Section 6).
    unaffected = set()
    for entry in fixture.get("unaffected_source_portions") or []:
        if isinstance(entry, dict):
            unaffected.add(entry.get("source_effect_id"))
    for p in predecessors:
        pid = p.get("effect_id")
        if p.get("status") != "ACTIVE":
            continue
        if pid in unaffected:
            current.add(pid)
            continue
        targets = set(
            row.get("target_effect_id")
            for row in fixture.get("mapping") or []
            if row.get("source_effect_id") == pid
        )
        # Retired portions take effect with the predecessor's (synchronized) mapped boundary;
        # a predecessor with only retired portions is closed by the transition itself.
        if all(effective(succ_by_id[t]) for t in targets if t in succ_by_id):
            continue
        current.add(pid)
    return sorted(current)


def evaluate_fixture(fixture):
    reasons = set()
    rtype = fixture.get("relation_type")
    relation_valid = _validate_relation(fixture, reasons)
    review_required = not relation_valid

    initialization = []
    if relation_valid:
        predecessors = list(fixture.get("predecessors") or [])
        successors = list(fixture.get("successors") or [])
        reaccepted = fixture.get("successor_deferral_reaccepted") or {}
        any_pred_deferral = any(p.get("deferral_active") is True for p in predecessors)

        if rtype == "CARRY_FORWARD":
            pred = predecessors[0]
            succ = successors[0]
            facts_ok = (
                fixture.get("source_realization_facts_current") is True
                and fixture.get("source_realization_facts_fresh") is True
            )
            carried = []
            if facts_ok:
                required = set(succ.get("required_components") or [])
                carried = sorted(set(pred.get("realization_components") or []) & required)
            elif pred.get("realization_components"):
                reasons.add("CONTINUITY_REALIZATION_FACTS_NOT_PRESERVED")
                review_required = True
            initialization.append(
                {
                    "successor_id": succ.get("effect_id"),
                    "mode": MODE_CONTINUITY,
                    "carried_components": carried,
                    "deferral_rebound": pred.get("deferral_active") is True,
                }
            )
        else:
            carry_result = _evaluate_carry(fixture, reasons)
            if carry_result is False:
                review_required = True
            for succ in successors:
                sid = succ.get("effect_id")
                mode = MODE_OPEN_RESET
                carried = []
                if isinstance(carry_result, dict) and carry_result.get(sid):
                    mode = MODE_CARRY
                    carried = sorted(carry_result[sid])
                rebound = reaccepted.get(sid) is True
                if rebound:
                    reasons.add("DEFERRAL_REBOUND")
                elif any_pred_deferral:
                    reasons.add("DEFERRAL_NOT_CARRIED")
                initialization.append(
                    {
                        "successor_id": sid,
                        "mode": mode,
                        "carried_components": carried,
                        "deferral_rebound": rebound,
                    }
                )

    initialization.sort(key=lambda entry: entry["successor_id"])
    return {
        "fixture_id": fixture.get("fixture_id"),
        "relation_valid": relation_valid,
        "current_effect_ids": _current_effect_ids(fixture, relation_valid),
        "successor_initialization": initialization,
        "review_required": review_required,
        "reason_codes": sorted(reasons),
    }
