# Research 429: Key Author B Grouping Output-Contract Harness Repair

**Date:** 2026-10-01
**Status:** GROUPING OUTPUT-CONTRACT HARNESS INVALID / ACCEPTED PREFIX PRESERVED / PROSPECTIVE P8 V6 REPAIR AUTHORIZED
**Parent:** Research 428 / Research 423
**Scope:** Diagnose the late Key Author B grouping HOLD using only non-semantic mechanical evidence and freeze the narrow prospective grouping-output harness repair before another semantic attempt.
**Authority:** Mechanical control-plane diagnosis and repair design only. This record does not inspect or edit failed Key B semantic output, change accepted Key B labels or grouping decisions, change frozen packets or semantic rules, expose Key A or Key B hidden semantics, perform construct comparison, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. Live progress before HOLD

The V5 run completed:

    STATE = ACCEPTED
    BIRTH classification = 15 / 15 ACCEPTED
    BIRTH attention gate = PASS
    BIRTH grouping = 10 / 13 ACCEPTED

and then stopped fail-closed with:

    runnerStatus = HOLD
    errorCode = P8_SEMANTIC_OUTPUT_INVALID
    qualityReplacementRequired = false
    groupingFloor = NOT_RUN
    component commitment = NOT_FROZEN
    hiddenSemanticDetailsExposed = false

No failed grouping output has been inspected.

## 2. Mechanical diagnosis

The active grouping generation schema and post-output validator are not isomorphic.

The generation schema currently permits grouping pairs whose item IDs are arbitrary strings and does not encode:

    eligibility against the mechanically supplied current-event eligible item set
    canonical pair orientation
    cross-list pair collision exclusion
    canonical array ordering

The prompt states canonical pair orientation and ordering, but the structured-output schema does not enforce them.

The post-output validator is stricter. It requires:

    both item IDs belong to the current eligible item set
    item_id_a < item_id_b
    no duplicate/collision across MUST_JOIN and MUST_SPLIT
    each pair list already be in canonical lexicographic order

Therefore a response may satisfy the supplied structured-output schema yet be rejected by the post-validator for representation/contract reasons.

Because the task owner does not inspect the held output, the exact violating row or condition is intentionally unknown. The demonstrated schema/validator non-isomorphism is sufficient to make this held attempt uninterpretable as semantic evidence.

## 3. Classification

The failed-attempt grouping output-contract layer is:

    HARNESS_INVALID

This does not invalidate the accepted prefix.

The following remain frozen:

    STATE
    all 15 accepted BIRTH classification batches
    BIRTH attention PASS
    10 accepted BIRTH grouping events

The HOLD is not:

    BIRTH grouping-floor failure
    construct-validity failure
    semantic disagreement with Key A

The grouping floor has not run and Key A/B comparison has not begun.

## 4. Narrow prospective repair

The repair must make the grouping generation contract materially closer to the already-existing validator while keeping semantic acceptance rules unchanged.

The next P8 release must:

    derive the grouping schema from the mechanically supplied eligible item IDs
    constrain both pair endpoints to that eligible domain
    keep pair reasons non-empty and bounded
    keep MUST_JOIN / MUST_SPLIT semantics unchanged
    keep global duplicate/collision rejection unchanged
    keep the post-output semantic validator unchanged for semantic contradictions

Pure storage-order requirements are representation mechanics rather than semantic judgments. The harness may canonicalize pair orientation and list order before the unchanged semantic collision/eligibility checks, provided this normalization:

    never changes MUST_JOIN versus MUST_SPLIT
    never adds or removes a pair
    never changes pair reason text except existing trim behavior
    never resolves a join/split collision
    never uses hidden failed output to tune behavior

This prevents semantically irrelevant ordering from becoming a stochastic rejection surface while retaining semantic fail-closed behavior.

## 5. Accepted-prefix preservation

No accepted artifact may be regenerated or edited.

The next attempt starts at the first still-unaccepted grouping event.

It must use a fresh Claude process/session under the existing:

    zero-tool
    stdin-only
    no-session-persistence
    Key-A-blind

contract.

## 6. Qualification requirements

Before semantic resume:

    grouping-schema eligible-domain regression PASS
    pair-orientation canonicalization regression PASS
    pair-list ordering canonicalization regression PASS
    cross-list collision rejection regression PASS
    existing P8 regression PASS
    P8 headless isolation regression PASS
    inherited P7/P6/P5/P4 regressions PASS
    public surface registration PASS
    bounded Git regressions PASS
    runtime release regressions PASS
    managed publish/restart/verify PASS
    mismatchCount = 0

The external purpose-specific P8 action schema does not change.

## 7. Recovery rule

After qualification and deployment:

    one fresh resume_after_hold is allowed

with the accepted prefix preserved.

If a new governed HOLD occurs, stop and disposition that new boundary. No automatic retry loop is authorized.

## 8. Current boundary

    KEY_B_STATE = ACCEPTED
    KEY_B_BIRTH_CLASSIFICATION = 15 / 15 ACCEPTED
    KEY_B_ATTENTION_GATE = PASS
    KEY_B_GROUPING = 10 / 13 ACCEPTED
    KEY_B_GROUPING_FLOOR = NOT_RUN
    KEY_B_COMPONENT_COMMITMENT = NOT_FROZEN

    CURRENT_RUNNER = HOLD
    ERROR_CODE = P8_SEMANTIC_OUTPUT_INVALID
    GROUPING_OUTPUT_CONTRACT = HARNESS_INVALID
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    ACCEPTED_PREFIX = PRESERVE
    PROSPECTIVE_GROUPING_REPAIR = AUTHORIZED
    NEXT = IMPLEMENT_QUALIFY_DEPLOY_P8_V6_GROUPING_CONTRACT_REPAIR
