# Research 427: P8 V4 Schema Transport Failure and Compact Contract Repair

**Date:** 2026-10-01
**Status:** V4 DEPLOYED / TRANSPORT HARNESS INVALID / COMPACT V5 REPAIR NEXT
**Parent:** Research 426
**Scope:** Record the mechanically diagnosed P8 worker failure after the first schema-contract repair and freeze the next transport-safe repair.
**Authority:** Mechanical harness diagnosis and repair design only. No Key B semantic output is inspected or changed.

## 1. V4 deployment

Research 426's first repair was implemented and qualified as:

    release = p8-key-b-ops-v4
    local-runtime source head = 47160230b226218b26b0e81edc3d1291d1b5fe24
    target version = 0.1.1-preview.67-p8-classification-contract
    target tool count = 177

Managed prepare, publish, restart and exact post-activation verify all passed.

Post-activation:

    mismatchCount = 0

The accepted Key B prefix remained:

    STATE accepted
    BIRTH classification 3 / 15 accepted

## 2. Immediate post-repair HOLD

The one governed fresh resume preserved the accepted prefix but stopped immediately with:

    P8_WORKER_FAILURE

No additional semantic unit was accepted.

The failure occurred before the attention gate and before grouping.

## 3. Mechanical transport diagnosis

The V4 repair encoded every current presentation position as a separate JSON-Schema prefix item so the generation contract could bind exact IDs/order plus the normative/normative_kind conditional.

For the next frozen classification batch, public packet inspection gives:

    presentation count = 223
    generated JSON-schema length = 236899 characters

The P8 invocation passes the entire JSON schema to Claude Code as one command-line argument through:

    --json-schema <serialized schema>

A non-semantic local spawn reproduction using a single 236899-character argument fails synchronously with:

    ENAMETOOLONG

The P8 worker maps a raw non-P8 spawn error to:

    P8_WORKER_FAILURE

This exactly explains the observed error class without reading any Key B semantic output.

Therefore:

    P8_V4_SCHEMA_TRANSPORT = HARNESS_INVALID

## 4. Compact V5 contract

The next repair must preserve the semantic validator and all frozen inputs while reducing the schema to transport-safe size.

The per-batch schema will bind:

    presentations minItems = batch count
    presentations maxItems = batch count
    presentation_id = enum of exact current batch IDs
    normative/normative_kind conditional in a compact item schema

The prompt continues to require:

    exactly one row per current presentation
    same frozen batch order

The existing post-validator continues to enforce the exact batch bijection and all semantic field constraints.

The schema must not duplicate the full row contract once per presentation.

## 5. Qualification

Before another semantic resume:

    compact-schema regression PASS
    largest frozen-batch schema-size regression PASS
    next-batch schema-size regression PASS
    P8 regression PASS
    headless isolation smoke PASS
    managed publish/restart/verify PASS
    mismatchCount = 0

Accepted STATE and the three accepted BIRTH batches remain frozen.

## 6. Boundary

    KEY_B_STATE = ACCEPTED
    KEY_B_BIRTH_CLASSIFICATION = 3 / 15 ACCEPTED
    CURRENT_RUNNER = HOLD
    CURRENT_ERROR = P8_WORKER_FAILURE
    V4_SCHEMA_TRANSPORT = HARNESS_INVALID
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    NEXT = IMPLEMENT_QUALIFY_DEPLOY_COMPACT_P8_V5
