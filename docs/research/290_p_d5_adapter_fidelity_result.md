# Research 290: P-D5 Adapter Fidelity Result

**Date:** 2026-09-24
**Status:** P-D5 PASS / CONSUMER-SIDE ADAPTER MODEL SUPPORTED / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Harness freeze:** Research 289
**Frozen harness commit:** 669134254f370802698dad8c299a02613bf4a8bb
**Frozen source commit:** 721545c46b94e0a87c87a572fb357ff314f6913f
**Probe:** P-D5
**Candidate:** WARRANT-F V0.2
**Scope:** Record the frozen-harness execution result for Product/JW1 native-result adapter fidelity.
**Authority:** Empirical architecture evidence only.

## 1. Result

Observed:

    P-D5
    result PASS

Durable evidence:

    experiments/r8c_assurance_probe_v01/evidence/p_d5_run_001.json

The result binds to the exact frozen harness and source commit recorded in Research 289.

## 2. Product native path

Native representation:

    pytest JUnit XML

Observed mappings:

    pass              -> PASS
    fail              -> FAIL
    skipped only      -> INCOMPLETE
    collection error  -> HARNESS_INVALID
    zero collected    -> INCOMPLETE
    truncated XML     -> HARNESS_INVALID
    zero claim match  -> UNVERIFIED

The deliberately faulty Product adapter classified a failing parseable report as PASS and was distinguished by the fail witness.

## 3. JW1 native path

Native representation:

    project-knowledge CLI JSON contract

Observed mappings:

    ok=true           -> PASS
    ok=false          -> FAIL
    truncated JSON    -> HARNESS_INVALID

The frozen source commit contains the native CLI contract evidence and the deliberately faulty JW1 adapter was distinguished by the fail witness.

## 4. Architecture interpretation

P-D5 supports the consumer-side adaptation rule:

    Product owns Product-native result semantics
    JW1 owns JW1-native result semantics
    Project Engineering adapts those results into neutral assurance evidence

Neither Product nor JW1 needs to import an Engineering assurance contract merely to produce qualifying results.

The probe therefore supports:

    CONSUMER_SIDE_ADAPTER_DEFAULT=true
    PRODUCT_ENGINEERING_IMPORT_REQUIRED=false
    JW1_ENGINEERING_IMPORT_REQUIRED=false

## 5. Scope limits

This probe does not select:

    pytest as the permanent Product test framework
    JUnit XML as the permanent Product result format
    the current JW1 CLI JSON shape as permanent
    a concrete Engineering adapter implementation
    a CI provider

Those are realization choices.

The result supports the architectural seam, not current tool preservation.

## 6. Result class

Under Research 277:

    P_D5=PASS
    TARGET_ARCHITECTURE_EVIDENCE=SUPPORTED
    TARGET_ARCHITECTURE_AMENDMENT_REQUIRED=false

## 7. Current state

    P_H=INCONCLUSIVE
    P_D6=PASS
    P_D3=PASS
    P_D5=PASS

    COMPLETED_VALID_DECISION_PROBES=4_OF_8
    UNRESOLVED_AMEND_RESULTS=0
    HARNESS_INVALID_ACTIVE_RESULTS=0

    OWNER_ASSURANCE_DECISION=HELD
    NEXT=P_D1_WARRANT_PROPORTIONALITY
