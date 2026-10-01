# Research 428: P8 V5 Compact Classification Schema Qualified and Deployed

**Date:** 2026-10-01
**Status:** V5 QUALIFIED / DEPLOYED / EXACTLY VERIFIED / KEY B RESUME NEXT
**Parent:** Research 427
**Scope:** Preserve qualification and deployment of the compact P8 classification-schema transport repair before resuming Key Author B semantics.
**Authority:** Mechanical control-plane qualification only. This record does not inspect or alter hidden Key B semantic output, accepted labels, frozen packets, semantic rules, Key A private semantics, construct comparison, DRP-03 scoring, successor architecture implementation, migration, oracle retirement, or authority switch.

## 1. Compact V5 repair

The V5 repair replaces the transport-unsafe positional per-presentation schema with a compact per-batch classification schema.

The compact schema binds:

    presentations minItems = exact batch count
    presentations maxItems = exact batch count
    presentation_id = enum of exact current batch IDs
    normative/normative_kind conditional
    all other frozen semantic fields unchanged

The existing post-output validator remains unchanged and continues to require an exact current-batch presentation-ID bijection and every frozen semantic field constraint.

The classification prompt continues to require exactly one record per current presentation in the frozen batch order.

No failed semantic output was read or used to tune the repair.

## 2. Qualification

Local-runtime source:

    release = p8-key-b-ops-v5
    source head = 1298ee37770dd1a8e39dac8f10f8ce2e0e43836f
    target version = 0.1.1-preview.68-p8-compact-classification-schema
    target tool count = 177

The dedicated P8 regression passes with all 15 classification batches, all 13 grouping events, isolation checks, gate-failure checks and resume checks.

The compact-schema regression additionally verifies:

    exact min/max batch count
    current-batch presentation-ID enum
    normative=true -> frozen normative-kind enum
    normative=false -> normative_kind null
    a synthetic 400-presentation schema remains below the frozen 30000-character transport bound

The headless zero-tool/no-session-persistence smoke remains part of the managed release regression set.

## 3. Managed deployment

Managed release preparation passed.

Managed publication completed successfully.

Managed Runtime Bridge restart completed successfully.

Exact post-activation release verification returned:

    mismatchCount = 0

Therefore the active Runtime Bridge now carries the compact P8 V5 classification-schema transport.

## 4. Preserved Key B state

The accepted semantic prefix remains:

    STATE = ACCEPTED
    BIRTH classification = 3 / 15 ACCEPTED

No additional semantic unit was accepted during V4 failure diagnosis or V5 repair/deployment.

The current hold originated from the mechanically diagnosed V4 transport failure:

    P8_WORKER_FAILURE

The repair changes only schema transport shape. It does not change accepted semantics or the acceptance validator.

## 5. Resume disposition

Research 427 authorized a fresh continuation after a transport-safe repair is qualified and deployed.

Those prerequisites are now satisfied.

The next allowed semantic action is:

    resume_after_hold

The accepted prefix must be preserved.

The resumed attempt must use a fresh Claude process/session under the existing zero-tool, stdin-only, no-session-persistence isolation contract.

If a new governed hold occurs, stop and disposition that new boundary rather than retry looping.

## 6. Boundary

    P8_V5_COMPACT_SCHEMA = QUALIFIED
    P8_V5_DEPLOYMENT = VERIFIED
    RELEASE_MISMATCH_COUNT = 0
    KEY_B_STATE = ACCEPTED
    KEY_B_BIRTH_CLASSIFICATION = 3 / 15 ACCEPTED
    HIDDEN_SEMANTIC_DETAILS_EXPOSED = false

    NEXT = P8_RESUME_AFTER_HOLD
