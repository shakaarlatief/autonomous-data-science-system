# Research 425: Fresh Key Author B Initial Semantic-Output Hold and Governed Replacement

**Date:** 2026-10-01
**Status:** KEY B STARTED / STATE ACCEPTED / BIRTH PREFIX 1 ACCEPTED / SEMANTIC-OUTPUT VALIDATION HOLD / FRESH REPLACEMENT ALLOWED
**Parent:** Research 424 / Research 423
**Scope:** Preserve the first live Key Author B P8 execution boundary and disposition the bounded semantic-output validation HOLD without inspecting hidden Key B semantics.
**Authority:** Governance and recovery disposition only. This record does not edit Key B semantic output, change labels, weaken validators, alter frozen inputs, expose hidden semantic content, perform construct comparison, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. P8 production qualification completed

After provider-local connector refresh, the purpose-specific P8 action surface became available:

    codex.p8_key_b_operation

The live bounded sequence completed:

    status
    prepare -> LIVE_SMOKE_RUNNING
    status -> liveSmoke PASS
    prepare -> PASS
    explicit owner authorization
    authorize_phase -> PASS
    run_until_boundary -> RUNNING

The live non-semantic Claude smoke passed before semantic authorization.

No generic command-path substitute was used for Key B semantic execution.

## 2. Live execution progress before HOLD

The bounded status now reports:

    p8Prepared = true
    p8Authorized = true
    p8Complete = false
    currentPhase = P8_KEY_B_HOLD
    runnerStatus = HOLD

    liveSmoke = PASS
    stateAccepted = true
    acceptedClassificationBatches = 1
    attentionGate = NOT_RUN
    acceptedGroupingEvents = 0
    groupingFloor = NOT_RUN
    commitmentFrozen = false

    errorCode = P8_SEMANTIC_OUTPUT_INVALID
    qualityReplacementRequired = false
    hiddenSemanticDetailsExposed = false
    next = GOVERNED_HOLD_DISPOSITION_REQUIRED

Therefore the accepted prefix is:

    STATE = ACCEPTED
    BIRTH classification = 1 / 15 ACCEPTED

No BIRTH attention gate or grouping phase has run.

## 3. Bounded diagnosis

The task owner has not inspected:

    the failed structured semantic output
    accepted Key B semantic artifacts
    Key B labels
    STATE answers
    precedent text
    presentation identities associated with the failed attempt
    grouping information
    Key A private semantics

A direct attempt to read the Key B private root through the generic workspace reader was rejected because that machine-local root is intentionally not an admitted public workspace.

Diagnosis therefore uses only:

    purpose-specific public-safe P8 status
    qualified P8 implementation contract
    frozen Research 423 recovery semantics

The qualified P8 implementation classifies:

    P8_BIRTH_ATTENTION_QUALITY_FAIL
    P8_BIRTH_GROUPING_FLOOR_FAIL

as non-resumable semantic gates.

By contrast, the implementation treats:

    P8_SEMANTIC_OUTPUT_INVALID

as a bounded technical/attempt HOLD that is eligible for `resume_after_hold`.

The validator failure means the fresh semantic process returned a structure/value combination that did not satisfy the already-frozen output contract. It does not establish that the accepted Key B prefix is invalid, and it is not the preregistered attention-quality failure.

## 4. Recovery disposition

The governed disposition is:

    FRESH_REPLACEMENT_ALLOWED

with all of the following constraints:

    preserve accepted STATE
    preserve the first accepted BIRTH classification batch
    archive the held orchestration
    do not edit or repair the failed semantic output
    do not expose the failed semantic output to the task owner
    do not alter the validator
    do not alter the frozen input packet
    do not alter the semantic prompt based on hidden failed content
    use a fresh Claude process/session for the replacement attempt
    preserve zero-tool / stdin-only / no-session-persistence isolation
    continue only through the purpose-specific P8 resume_after_hold action

Exactly one governed fresh resume is authorized from this HOLD.

This is not retry-to-green. No accepted semantic label is changed and no quality metric has been observed or optimized.

## 5. Repeated-failure rule

If `P8_SEMANTIC_OUTPUT_INVALID` recurs before the next semantic unit is accepted, stop again.

A repeated failure at the same boundary requires prospective prompt/schema/structured-output contract diagnosis using only non-semantic mechanical evidence. It must not trigger an automatic retry loop or hidden-output inspection.

If the fresh replacement succeeds, normal sequential P8 execution may continue until the next governed boundary.

## 6. Current boundary

    P8_LIVE_SMOKE = PASS
    P8_PREPARED = true
    P8_AUTHORIZED = true

    KEY_B_STATE = ACCEPTED
    KEY_B_BIRTH_CLASSIFICATION = 1 / 15 ACCEPTED
    KEY_B_ATTENTION_GATE = NOT_RUN
    KEY_B_GROUPING = 0 / 13
    KEY_B_GROUPING_FLOOR = NOT_RUN
    KEY_B_COMPONENT_COMMITMENT = NOT_FROZEN

    P8_RUNNER = HOLD
    ERROR_CODE = P8_SEMANTIC_OUTPUT_INVALID
    QUALITY_REPLACEMENT_REQUIRED = false
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    DISPOSITION = FRESH_REPLACEMENT_ALLOWED
    NEXT = ONE_GOVERNED_RESUME_AFTER_HOLD
