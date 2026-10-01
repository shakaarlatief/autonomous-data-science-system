# Research 431: P8 V6 grouping contract repair qualified and deployed

**Date:** 2026-10-01
**Status:** P8 V6 QUALIFIED / DEPLOYED / VERIFIED / ONE FRESH RESUME AUTHORIZED
**Parent:** Research 429 / Research 430
**Scope:** Implement, qualify, publish, activate and verify the narrow prospective Key Author B grouping output-contract repair authorized by Research 429.
**Authority:** Mechanical grouping-harness repair only. This record does not inspect or edit failed Key B semantic output, alter accepted Key B labels or grouping decisions, change MUST_JOIN/MUST_SPLIT semantics, change frozen packets, expose Key A or Key B hidden semantics, perform construct comparison, score DRP-03, implement the successor architecture, migrate repository state, retire the oracle, or switch authority.

## 1. V6 implementation

The private local-runtime source is synchronized at:

    a192ed3637ec96b4d492f712116c9b977e35965b

with commit:

    Add P8 V6 grouping contract repair

The immutable release is:

    release id        p8-key-b-ops-v6
    target version    0.1.1-preview.70-p8-grouping-contract-repair
    surface           codexless-public-preview-v2
    tool count        177
    manifest SHA-256  f931861e0f64af40189b99a49a3fa669dcfa7f41cb82f5398283e80133ada2bd

The external purpose-specific P8 action schema is unchanged.

## 2. Prospective grouping contract repair

V6 implements the Research 429 repair without using the hidden failed grouping output.

The grouping generation schema is now derived from the mechanically supplied eligible item IDs for the current event. Pair endpoints are constrained to that eligible domain. For fewer than two eligible IDs, both pair arrays are mechanically constrained to zero items.

The post-output validator still requires:

    exact grouping object and pair fields
    both endpoints eligible
    distinct endpoints
    non-empty reason
    no duplicate pair
    no MUST_JOIN / MUST_SPLIT collision

Representation-only requirements are now normalized mechanically:

    pair orientation is canonicalized lexicographically
    pair-list ordering is canonicalized deterministically
    existing reason trim behavior is retained

The normalization does not:

    change MUST_JOIN versus MUST_SPLIT
    add or remove a pair
    resolve a join/split collision
    change reason content beyond existing trim behavior
    inspect or use the hidden failed output

The semantic grouping rule and grouping floor remain unchanged.

## 3. Qualification

The V6 regression adds explicit coverage for:

    eligible-domain endpoint schema
    singleton eligible-domain zero-pair contract
    reversed pair orientation canonicalization
    pair-list ordering canonicalization
    ineligible endpoint rejection
    self-pair rejection
    duplicate rejection after orientation normalization
    cross-list MUST_JOIN / MUST_SPLIT collision rejection

The managed release also carries and passed the required inherited suite:

    existing P8 regression
    P8 headless runner smoke
    P7 component-key regression
    P6 legacy regression
    P6 headless runner smoke
    P5 private-ops regression
    P4 private-ops regression
    Codex compatibility RPC-timeout regression
    public surface registration
    flexible authority regression
    bounded Git fetch regression
    bounded Git pull regression
    runtime release regression
    runtime release dependency integration

Managed lifecycle:

    prepare                 PASS
    publish                 SUCCEEDED
    restart / activation    SUCCEEDED
    post-activation verify  VERIFIED
    mismatchCount           0

No activation recovery was required.

## 4. Preserved live P8 boundary

Post-activation purpose-specific status is mechanically unchanged:

    P8 prepared                    true
    P8 authorized                  true
    runner                         HOLD
    Key B STATE                    ACCEPTED
    classification batches         15 / 15
    attention gate                 PASS
    grouping events                10 / 13
    grouping floor                 NOT RUN
    component commitment           NOT FROZEN
    error                          P8_SEMANTIC_OUTPUT_INVALID
    quality replacement required   false
    hidden semantic details        false

Therefore no accepted Key B artifact was regenerated or edited by deployment.

## 5. Resume authority

Research 429 authorized exactly one fresh resume_after_hold after a qualified and deployed V6 repair.

That precondition is now satisfied.

The next action is:

    ONE FRESH P8 resume_after_hold

The accepted prefix must remain frozen. The resumed worker must begin at the first still-unaccepted grouping event under the existing fresh-process, zero-tool, stdin-only, no-session-persistence and Key-A-blind contract.

If a new governed HOLD occurs, stop and disposition that boundary. No automatic retry loop is authorized.
