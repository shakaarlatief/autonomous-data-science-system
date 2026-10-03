# MC-0029 Message 020: Claude D-1 Integrated Replay Evaluator B

```text
Thread                          MC-0029
Message                         020
Author / collaborator           Claude
Role                            INDEPENDENT EVALUATOR B AUTHOR (blinded)
Interaction environment         Claude
Interaction session             claude-04
Conversation title              04 - Assurance and Delivery Architecture Design
Coordination branch             v1-source-vault-bootstrap-resume
Probe                           HYBRID_D1_REAL_EVENT_REPLAY_V01
Transport                       Claude-side GitHub connector (Research 485)
Authority                       Collaboration evidence only. Selects nothing. Authorizes nothing.
```

## 1. Source, head and routing verification

```text
remote head (git ls-remote)        0cffdedc001596f169e45498fc6224763552f145 = expected
current_routing.json boundary      operative-hybrid-done-evaluator-b
MC-0029 STATE phase / next actor   DRP03_HYBRID_D1_EVALUATOR_B / claude
THREAD current boundary            NEXT=CLAUDE_MESSAGE020_D1_EVALUATOR_B
Message 019 frozen base            7fa4f3d6e9b607d39dc264a7d84283aaafe0f0cf
D-1 inputs at 7fa4f3d6 vs head     all four permitted inputs byte-identical
routing contradiction              none
```

**Hash-basis finding (not content drift).** The four permitted inputs as committed (LF blobs) do not match the SHA-256 values recorded in Research 492 §1. All four recorded digests do match the same files with **CRLF line endings**. The frozen content is therefore unchanged, but Research 492's digests were computed over working-tree bytes rather than `GIT_BLOB_BYTES_AT_COMMIT`. This is the recurring line-ending hash-basis defect, and the freeze record's digests should be restated on the Git-blob basis. Committed-blob SHA-256:

```text
accepted_j1.json          cffbeffc45e0adeda0adbb6b240b4b9968f461f3af4ce3f89af716776742ebe4
source_facts.json         3b5ceaa50765297c34d8d1cfa2f6230ba1d3263f457aa3f6f71dd51f39b6ded3
definitions.json          b1852c008fe9f61026cc44b24e5f936c8ec22d129989cb09019ae004805d98ac
evaluator_contract.json   01acbd0a3d4e9f497cf27bba6472a4265e1fe585aa9ca04122da8a38efa5cccf
```

## 2. Blindness attestation

I authored Evaluator B from only these permitted files, each fetched individually by exact path:

- `experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json`
- `experiments/ao10_hybrid_d1_replay_v01/source_facts.json`
- `experiments/ao10_hybrid_d1_replay_v01/definitions.json`
- `experiments/ao10_hybrid_d1_replay_v01/evaluator_contract.json`

plus Research 490, 491 and 492 (explanatory), Message 019, and the routing, inbox, MC-0029 `STATE.json` and `THREAD.md` for authority verification.

I did **not** open, list into, search into or derive anything from:

- `experiments/ao10_hybrid_d1_replay_v01/evaluator_key.json`;
- `experiments/ao10_hybrid_d1_replay_v01/evaluator_chatgpt_a.py`;
- any Evaluator A output;
- any D-1 comparison or result artifact;
- any hidden R2 item-level material.

No repository-wide search was run, and no full checkout of any commit containing the D-1 directory was made, so no blinded file was ever on disk in this interaction. The "D-1 inputs at 7fa4f3d6 vs head" comparison fetched only the four permitted files at both commits. Research 492's key digest was visible as text in that permitted record; it was not used.

## 3. Evaluator B source (`evaluator_claude_b.py`)

```python
"""HYBRID_D1_REAL_EVENT_REPLAY_V01 - Evaluator B (independently authored by Claude / claude-04).

Authored only from the reviewer-facing D-1 materials:
    experiments/ao10_hybrid_d1_replay_v01/accepted_j1.json
    experiments/ao10_hybrid_d1_replay_v01/source_facts.json
    experiments/ao10_hybrid_d1_replay_v01/definitions.json
    experiments/ao10_hybrid_d1_replay_v01/evaluator_contract.json
with Research 490-492 as explanatory context.

Standard library only. Deterministic. No file, network or model access inside evaluate.
Only structured fields are consumed; accepted_effect_statement prose is never interpreted.
"""

GITHUB_CONNECTOR = "CLAUDE_SIDE_GITHUB_CONNECTOR"
OPEN_RESET = "OPEN_RESET"

COMPONENT_TO_PREDICATE = {
    "TRANSPORT_ATTESTED_GITHUB_CONNECTOR": "transport_attested_github_connector",
    "AUTHORIZED_PATH_ONLY": "authorized_path_only",
    "COMMIT_RECEIPT_BOUND_TO_CORRECTION_HEAD": "commit_receipt_bound_to_correction_head",
}

EVIDENCE_FIELDS = (
    "git_commit_receipt_present",
    "commit_parent_observed",
    "changed_paths_observed",
    "message_transport_attestation_present",
)

SHARED_PREDICATE_ORDER = (
    "transport_attested_github_connector",
    "authorized_path_only",
    "commit_receipt_bound_to_correction_head",
    "runtime_bridge_prohibition_not_violated",
    "evidence_valid",
    "qualification_complete",
    "authorization_exercise_valid",
    "lineage_transition_valid",
)


def _is_sha(value, length):
    if not isinstance(value, str) or len(value) != length:
        return False
    return all(ch in "0123456789abcdef" for ch in value)


def _dict(value):
    return value if isinstance(value, dict) else {}


def _effects_by_type(accepted_j1):
    by_type = {}
    for effect in accepted_j1.get("effects") or []:
        if isinstance(effect, dict):
            by_type.setdefault(effect.get("type"), []).append(effect)
    return by_type


def _single(by_type, effect_type):
    found = by_type.get(effect_type) or []
    return found[0] if len(found) == 1 else None


def _acceptance_binding_valid(accepted_j1, source_facts):
    """Structural validity of the owner-accepted J1 boundary and its binding to the
    governing correction recorded in the source facts."""
    if accepted_j1.get("owner_decision") != "ACCEPT":
        return False
    if not _is_sha(accepted_j1.get("owner_packet_sha256"), 64):
        return False
    if not isinstance(accepted_j1.get("owner_decision_record"), str) or not accepted_j1.get("owner_decision_record"):
        return False
    if not isinstance(accepted_j1.get("source_authority"), str) or not accepted_j1.get("source_authority"):
        return False
    correction = _dict(source_facts.get("correction"))
    if accepted_j1.get("source_correction_commit") != correction.get("commit"):
        return False

    effects = [e for e in accepted_j1.get("effects") or [] if isinstance(e, dict)]
    ids = [e.get("accepted_effect_id") for e in effects]
    if not effects or any(not isinstance(i, str) or not i for i in ids) or len(set(ids)) != len(ids):
        return False
    for effect in effects:
        if not isinstance(effect.get("accepted_effect_statement"), str) or not effect.get("accepted_effect_statement"):
            return False
        disposition = effect.get("accounting_disposition")
        if disposition == "REALIZATION_TRACKED":
            contract = _dict(effect.get("completion_contract"))
            if contract.get("authority") not in ("GOVERNING_ACCEPTANCE", "ACCEPTED_DOMAIN_CONTRACT"):
                return False
            if not isinstance(contract.get("required_components"), list) or not contract.get("required_components"):
                return False
        elif disposition == "NO_REALIZATION_REQUIRED":
            if not isinstance(effect.get("accounting_reason"), str) or not effect.get("accounting_reason"):
                return False
        else:
            return False

    by_type = _effects_by_type(accepted_j1)
    for effect_type in ("REQUIRE", "PROHIBIT", "AUTHORIZE", "LIFECYCLE"):
        if _single(by_type, effect_type) is None:
            return False
    return True


def _source_fact_contract_valid(source_facts):
    """Structural validity (presence and types) of the J2 source-fact record."""
    if not isinstance(source_facts.get("fixture_id"), str) or not source_facts.get("fixture_id"):
        return False
    correction = source_facts.get("correction")
    action = source_facts.get("action")
    evidence = source_facts.get("evidence")
    if not isinstance(correction, dict) or not isinstance(evidence, dict):
        return False
    if not _is_sha(correction.get("commit"), 40):
        return False
    if not isinstance(correction.get("claude_runtime_bridge_available"), bool):
        return False
    for key in (
        "authorized_transport",
        "authorized_path",
        "predecessor_rule_id",
        "successor_rule_id",
        "lineage_relation",
        "realization_succession",
    ):
        if not isinstance(correction.get(key), str) or not correction.get(key):
            return False
    for key in EVIDENCE_FIELDS:
        if not isinstance(evidence.get(key), bool):
            return False
    if action is None:
        return True
    if not isinstance(action, dict):
        return False
    if not _is_sha(action.get("commit"), 40) or not _is_sha(action.get("parent"), 40):
        return False
    paths = action.get("changed_paths")
    if not isinstance(paths, list) or any(not isinstance(p, str) for p in paths):
        return False
    if not isinstance(action.get("message_transport_attestation"), str):
        return False
    if not isinstance(action.get("message_only_authorized_path_written_attestation"), bool):
        return False
    return True


def _shared_predicates(accepted_j1, source_facts):
    correction = _dict(source_facts.get("correction"))
    action = _dict(source_facts.get("action"))
    evidence = _dict(source_facts.get("evidence"))
    lifecycle = _single(_effects_by_type(accepted_j1), "LIFECYCLE") or {}
    lineage = _dict(lifecycle.get("lineage"))

    transport = (
        action.get("message_transport_attestation") == correction.get("authorized_transport")
        and correction.get("authorized_transport") == GITHUB_CONNECTOR
    )
    path_only = (
        isinstance(action.get("changed_paths"), list)
        and action.get("changed_paths") == [correction.get("authorized_path")]
        and action.get("message_only_authorized_path_written_attestation") is True
    )
    receipt = (
        action.get("parent") is not None
        and action.get("parent") == correction.get("commit")
        and evidence.get("git_commit_receipt_present") is True
    )
    no_bridge = (
        correction.get("claude_runtime_bridge_available") is False
        and action.get("message_transport_attestation") == GITHUB_CONNECTOR
    )
    evidence_valid = all(evidence.get(key) is True for key in EVIDENCE_FIELDS)
    qualification = transport and path_only and receipt and no_bridge
    authorization = transport and path_only and receipt
    lineage_valid = (
        correction.get("lineage_relation") == "REPLACE"
        and lineage.get("relation") == "REPLACE"
        and correction.get("predecessor_rule_id") == lineage.get("predecessor_id")
        and correction.get("successor_rule_id") == lineage.get("successor_id")
        and lineage.get("predecessor_id") is not None
        and lineage.get("successor_id") is not None
        and correction.get("realization_succession") == OPEN_RESET
        and lineage.get("realization_succession") == OPEN_RESET
    )
    values = {
        "transport_attested_github_connector": bool(transport),
        "authorized_path_only": bool(path_only),
        "commit_receipt_bound_to_correction_head": bool(receipt),
        "runtime_bridge_prohibition_not_violated": bool(no_bridge),
        "evidence_valid": bool(evidence_valid),
        "qualification_complete": bool(qualification),
        "authorization_exercise_valid": bool(authorization),
        "lineage_transition_valid": bool(lineage_valid),
    }
    return {key: values[key] for key in SHARED_PREDICATE_ORDER}


def _lineage_relation_valid(accepted_j1, predicates):
    by_type = _effects_by_type(accepted_j1)
    lifecycle = _single(by_type, "LIFECYCLE")
    if lifecycle is None:
        return False
    lineage = _dict(lifecycle.get("lineage"))
    successor = lineage.get("successor_id")
    predecessor = lineage.get("predecessor_id")
    require_ids = set(e.get("accepted_effect_id") for e in by_type.get("REQUIRE") or [])
    return (
        lineage.get("relation") == "REPLACE"
        and predecessor != successor
        and successor in require_ids
        and lineage.get("realization_succession") == OPEN_RESET
        and predicates["lineage_transition_valid"]
    )


def evaluate(accepted_j1, source_facts):
    accepted_j1 = _dict(accepted_j1)
    source_facts = _dict(source_facts)
    by_type = _effects_by_type(accepted_j1)
    require = _single(by_type, "REQUIRE") or {}
    prohibit = _single(by_type, "PROHIBIT") or {}
    authorize = _single(by_type, "AUTHORIZE")
    lifecycle = _single(by_type, "LIFECYCLE") or {}
    correction = _dict(source_facts.get("correction"))
    action_present = isinstance(source_facts.get("action"), dict)

    acceptance_valid = _acceptance_binding_valid(accepted_j1, source_facts)
    source_valid = _source_fact_contract_valid(source_facts)
    predicates = _shared_predicates(accepted_j1, source_facts)
    lineage_valid = _lineage_relation_valid(accepted_j1, predicates)

    # Accepted authorization path must agree with the correction's authorized path.
    exercise = _dict((authorize or {}).get("exercise_contract"))
    authorization_path_consistent = authorize is not None and exercise.get("exact_authorized_path") == correction.get(
        "authorized_path"
    )
    governing_valid = acceptance_valid and lineage_valid and authorization_path_consistent

    # Current effects after the replayed action (definitions.currentness).
    current = []
    if acceptance_valid:
        for effect in accepted_j1.get("effects") or []:
            eid = effect.get("accepted_effect_id")
            etype = effect.get("type")
            if etype in ("REQUIRE", "PROHIBIT"):
                current.append(eid)
            elif etype == "AUTHORIZE":
                if not action_present:
                    current.append(eid)
            elif etype == "LIFECYCLE":
                if not lineage_valid:
                    current.append(eid)
    current = sorted(set(current))

    # Realization succession from the accepted REPLACE (OPEN_RESET initialization).
    initialization = []
    if lineage_valid:
        initialization.append(
            {"effect_id": _dict(lifecycle.get("lineage")).get("successor_id"), "mode": OPEN_RESET}
        )
    initialization.sort(key=lambda entry: entry["effect_id"])

    # J3 requirement satisfaction for the realization-tracked REQUIRE.
    contract = _dict(require.get("completion_contract"))
    components = contract.get("required_components") or []
    components_known = bool(components) and all(c in COMPONENT_TO_PREDICATE for c in components)
    coverage_complete = components_known and all(predicates[COMPONENT_TO_PREDICATE[c]] for c in components)
    evidence_ok = predicates["evidence_valid"] or contract.get("evidence_required") is False
    qualification_ok = predicates["qualification_complete"] or contract.get("qualification_required") is False
    activation_ok = contract.get("activation_required") is not True
    requirement_satisfied = bool(
        acceptance_valid
        and source_valid
        and require.get("accounting_disposition") == "REALIZATION_TRACKED"
        and contract.get("composition_rule") == "ALL_REQUIRED"
        and coverage_complete
        and evidence_ok
        and qualification_ok
        and activation_ok
    )

    # Standing prohibition visibility.
    standing = _dict(prohibit.get("standing_enforcement"))
    if standing.get("mode") == "DETECTIVE_ONLY" and standing.get("control_ref"):
        if predicates["runtime_bridge_prohibition_not_violated"]:
            standing_status = "DETECTIVE_ONLY_COMPLIANT"
        else:
            standing_status = "DETECTIVE_ONLY_VIOLATION"
    else:
        standing_status = "UNBOUND_REVIEW_REQUIRED"

    # Bounded authorization exercise.
    if not action_present:
        authorization_status = "NOT_EXERCISED"
    elif authorize is not None and predicates["authorization_exercise_valid"] and authorization_path_consistent:
        authorization_status = "EXERCISED_VALID"
    else:
        authorization_status = "EXERCISED_INVALID"

    # Review routing (precedence: governing > integration > assurance).
    review_owner = None
    if not governing_valid:
        review_owner = "GOVERNING_OWNER"
    elif not source_valid or (
        action_present
        and not (predicates["authorized_path_only"] and predicates["commit_receipt_bound_to_correction_head"])
    ):
        review_owner = "INTEGRATION_OWNER"
    elif action_present and not (
        predicates["evidence_valid"]
        and predicates["qualification_complete"]
        and predicates["transport_attested_github_connector"]
        and predicates["runtime_bridge_prohibition_not_violated"]
    ):
        review_owner = "ASSURANCE_OWNER"
    elif standing_status == "UNBOUND_REVIEW_REQUIRED":
        review_owner = "GOVERNING_OWNER"
    review_required = review_owner is not None

    # Generated realization orientation and next gap. REVIEW_REQUIRED orientation is
    # reserved for invalid or contradictory acceptance / source / lineage bindings;
    # evidence or qualification gaps still route to review but orient as OPEN + gap.
    structural_review = not governing_valid or not source_valid
    if structural_review:
        orientation, next_gap = "REVIEW_REQUIRED", "REVIEW"
    elif requirement_satisfied:
        orientation, next_gap = "SATISFIED", "NONE"
    else:
        orientation = "OPEN"
        if not action_present:
            next_gap = "UNOWNED"
        elif not coverage_complete:
            next_gap = "COVERAGE"
        elif not evidence_ok:
            next_gap = "EVIDENCE"
        elif not qualification_ok:
            next_gap = "QUALIFICATION"
        elif not activation_ok:
            next_gap = "ACTIVATION"
        else:
            next_gap = "REVIEW"

    return {
        "fixture_id": source_facts.get("fixture_id"),
        "acceptance_binding_valid": acceptance_valid,
        "source_fact_contract_valid": source_valid,
        "shared_predicates": predicates,
        "lineage_relation_valid": lineage_valid,
        "current_effect_ids": current,
        "realization_initialization": initialization,
        "requirement_satisfied": requirement_satisfied,
        "realization_orientation": orientation,
        "next_gap": next_gap,
        "standing_prohibition_enforcement": standing_status,
        "authorization_exercise_status": authorization_status,
        "review_required": review_required,
        "review_owner": review_owner,
    }
```

## 4. Syntax and runtime validation summary

Runtime validation only; no scoring:

```text
py_compile                                   PASS
imports                                      none (standard library not even needed)
evaluate(accepted_j1, source_facts) runs     PASS, no exception
output keys == required_output_fields order  PASS
shared_predicates key set == contract set    PASS
realization_initialization fields/modes      PASS
orientation / next_gap / standing /
  authorization / review_owner in allowed    PASS
current_effect_ids lexically sorted          PASS
inputs not mutated                           PASS
5 repeated runs identical (determinism)      PASS
```

No output was compared with the hidden key or with Evaluator A. D-1 was not scored.

## 5. Ambiguities in the reviewer-facing specification

1. **Three material fields have no frozen definition:** `acceptance_binding_valid`, `source_fact_contract_valid` and `lineage_relation_valid`.
   - Evaluator B treats `acceptance_binding_valid` as structural binding validity: owner decision `ACCEPT`; a 64-hex owner packet digest; a non-empty decision record and source authority; the accepted source correction commit equal to the source-fact correction commit; unique, non-empty effect IDs and statements; a valid accounting disposition (a completion contract for TRACKED, a reason for NO_REALIZATION_REQUIRED); and exactly one REQUIRE, PROHIBIT, AUTHORIZE and LIFECYCLE effect.
   - `source_fact_contract_valid` is presence and type validity of the J2 record (commit and parent SHA shapes, boolean evidence, string fields).
   - `lineage_relation_valid` is the accepted LIFECYCLE REPLACE with distinct predecessor and successor, a successor that is an accepted REQUIRE, OPEN_RESET succession, and `lineage_transition_valid`.
2. **REVIEW_REQUIRED orientation versus review routing.** `definitions.j3` reserves REVIEW_REQUIRED orientation for invalid or contradictory acceptance, source or lineage. `review_routing` sends evidence and qualification failures to ASSURANCE_OWNER. Evaluator B decouples them: those failures set `review_required` / `review_owner` but orient as OPEN with the matching `next_gap`.
3. **Review-owner precedence when several classes fail is unspecified.** Evaluator B uses GOVERNING_OWNER > INTEGRATION_OWNER > ASSURANCE_OWNER. A false transport attestation or runtime-bridge predicate routes to ASSURANCE_OWNER (it is a qualification input). An unbound standing control routes to GOVERNING_OWNER.
4. **A cross-check not in the definitions:** the accepted E03 `exact_authorized_path` must equal `correction.authorized_path`. A mismatch is treated as a governing contradiction (REVIEW_REQUIRED / GOVERNING_OWNER, EXERCISED_INVALID). The real fixture is consistent.
5. **Currentness is given only for this fixture** (`definitions.currentness`). Evaluator B generalizes:
   - REQUIRE and PROHIBIT stay current;
   - AUTHORIZE is consumed when any action exists, and stays current otherwise;
   - LIFECYCLE becomes historical when the lineage relation is valid;
   - no effect is current when the acceptance binding is invalid.
6. **`realization_initialization` ordering** is not stated in `sorting`. Evaluator B sorts by `effect_id`, and emits nothing when the lineage relation is invalid.
7. **No-action branch** (not exercised by the real fixture): NOT_EXERCISED, orientation OPEN with `next_gap` UNOWNED, and no review raised from absent action facts.
8. **`shared_predicates` key order** is non-semantic per the contract. Evaluator B emits the contract's `shared_predicate_fields` order.

```text
MC0029_MESSAGE020=COMPLETE
EVALUATOR=B (claude-04, independently authored)
BLIND_TO_KEY_AND_EVALUATOR_A=true
D1_SCORED=false
HASH_BASIS_FINDING=RESEARCH492_DIGESTS_ARE_CRLF_WORKING_TREE_NOT_GIT_BLOB
HIDDEN_R2_DETAILS=SEALED
NEXT_AFTER_MESSAGE020=CHATGPT_MATERIALIZE_AND_SCORE_D1
```
