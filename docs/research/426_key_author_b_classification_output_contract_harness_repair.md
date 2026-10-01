# Research 426: Key Author B Classification Output-Contract Non-Isomorphism and Prospective Harness Repair

**Date:** 2026-10-01
**Status:** HARNESS INVALID AT CLASSIFICATION OUTPUT CONTRACT / ACCEPTED PREFIX PRESERVED / PROSPECTIVE REPAIR AUTHORIZED
**Parent:** Research 425 / Research 423
**Scope:** Diagnose the repeated Key Author B `P8_SEMANTIC_OUTPUT_INVALID` HOLD using only non-semantic mechanical evidence and freeze the narrow prospective harness repair before another semantic replacement attempt.
**Authority:** Mechanical control-plane diagnosis and repair design. This record does not inspect or edit failed Key B semantic output, change any accepted Key B label, weaken semantic validators, change frozen packets, expose Key A or Key B hidden semantics, compare keys, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. Repeated bounded failure

After the single governed replacement authorized by Research 425, the P8 runner advanced from:

    STATE accepted
    BIRTH classification 1 / 15 accepted

to:

    STATE accepted
    BIRTH classification 3 / 15 accepted

and then again stopped with:

    runnerStatus = HOLD
    errorCode = P8_SEMANTIC_OUTPUT_INVALID
    qualityReplacementRequired = false
    attentionGate = NOT_RUN
    grouping = 0 / 13
    hiddenSemanticDetailsExposed = false

The replacement therefore made real forward progress before the same validation-error class recurred.

No failed structured semantic output has been inspected.

## 2. Mechanical contract diagnosis

The active P8 implementation has two separate classification contracts.

The structured-output JSON schema currently allows:

    presentation_id = any string
    presentations array = any length
    normative = true or false
    normative_kind = any frozen kind or null

without making `normative_kind` conditional on `normative`.

The post-output validator is stricter. It requires:

    exact presentation count for the current frozen batch
    exact current-batch presentation IDs
    one record for every required presentation
    normative = true  -> normative_kind in frozen kind enum
    normative = false -> normative_kind = null

Therefore the JSON schema supplied to the semantic process is not isomorphic to the validator that decides acceptance.

An output can satisfy the supplied structured-output schema and still be rejected mechanically by the post-validator.

This diagnosis requires no access to the failed semantic values.

## 3. Classification

The relevant P8 classification output-contract layer is:

    HARNESS_INVALID

for the failed attempts that reached this schema/validator gap.

This does not invalidate accepted semantic artifacts.

Accepted STATE and the three accepted BIRTH classification batches already passed the stricter validator and remain frozen.

The observed failure is also not:

    BIRTH attention-quality failure
    BIRTH grouping-floor failure
    semantic disagreement with Key A
    construct-validity failure

Those gates have not run.

## 4. Narrow prospective repair

The frozen repair is to make the semantic structured-output schema project the already-existing validator constraints before generation.

For each BIRTH classification batch, the control plane must derive a batch-specific schema mechanically from the frozen batch.

The batch-specific schema must bind:

    presentations minItems = current batch presentation count
    presentations maxItems = current batch presentation count
    presentation_id = one of the exact current batch IDs
    normative = true  -> normative_kind = one frozen normative kind
    normative = false -> normative_kind = null

The post-validator remains unchanged.

The frozen semantic fields remain unchanged.

The frozen input batch remains unchanged.

The semantic meaning of every field remains unchanged.

The prompt may continue to state the already-frozen rule:

    if normative=false, normative_kind must be null

No hidden failed output is used to tune the repair.

## 5. Accepted-prefix preservation

The repair must preserve:

    STATE = accepted
    BIRTH classification accepted prefix = 3 / 15

No accepted artifact may be regenerated.

No accepted semantic value may be edited.

The next replacement starts at the first still-unaccepted batch with a fresh Claude process/session.

## 6. Qualification requirements

Before the repaired runtime is allowed to resume Key B semantics:

    dynamic classification-schema regression PASS
    exact current-batch ID binding regression PASS
    exact batch-length binding regression PASS
    normative/normative_kind conditional regression PASS
    existing P8 Key B regression PASS
    P8 headless zero-tool/no-persistence smoke regression PASS
    P7/P6/P5/P4 regressions PASS
    public surface registration PASS
    bounded Git regressions PASS
    runtime release regressions PASS
    managed publish/restart/verify PASS
    mismatchCount = 0

The external purpose-specific P8 action schema does not change.

## 7. Recovery after qualification

After the repaired runtime is qualified and active:

    one fresh resume_after_hold is allowed

with:

    accepted prefix preserved
    failed attempts archived
    fresh Claude session
    zero tools
    stdin-only semantic input
    no session persistence
    no hidden-output inspection

If `P8_SEMANTIC_OUTPUT_INVALID` recurs after this contract repair, stop again. Do not create an automatic retry loop.

## 8. Current boundary

    KEY_B_STATE = ACCEPTED
    KEY_B_BIRTH_CLASSIFICATION = 3 / 15 ACCEPTED
    KEY_B_ATTENTION_GATE = NOT_RUN
    KEY_B_GROUPING = 0 / 13
    KEY_B_COMPONENT_COMMITMENT = NOT_FROZEN

    CURRENT_RUNNER = HOLD
    ERROR_CODE = P8_SEMANTIC_OUTPUT_INVALID
    CLASSIFICATION_OUTPUT_CONTRACT = HARNESS_INVALID
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    ACCEPTED_PREFIX = PRESERVE
    PROSPECTIVE_SCHEMA_REPAIR = AUTHORIZED
    NEXT = IMPLEMENT_QUALIFY_DEPLOY_P8_CLASSIFICATION_SCHEMA_REPAIR
