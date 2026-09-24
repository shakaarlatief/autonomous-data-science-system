# Research 280: P-D6 Executor Capability / Trust Separation Result

**Date:** 2026-09-24
**Status:** P-D6 PASS / WF-A34-A36 EMPIRICALLY SUPPORTED / NO TARGET EXECUTOR OR PROVIDER SELECTED / NO OWNER ASSURANCE DECISION
**Parent protocol:** Research 277
**Harness freeze:** Research 279
**Frozen harness commit:** a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9
**Probe:** P-D6
**Candidate:** WARRANT-F V0.2
**Scope:** Record the frozen-harness execution result for executor capability versus trust separation.
**Authority:** Empirical architecture evidence only.

## 1. Result

Observed:

    P-D6
    result     PASS
    executors  6
    eligible   4

Durable evidence:

    experiments/r8c_assurance_probe_v01/evidence/p_d6_run_001.json

The result self-binds to:

    HARNESS_COMMIT=a84e111e6dd60d1b56380a8aeb78fd842b1cf4f9
    HASH_BASIS=GIT_BLOB_BYTES_AT_COMMIT

and its two file hashes exactly match Research 279.

## 2. Preregistered assertions

### Actor/model label invariance

Two executor records differed in actor label:

    model-A
    model-B

while capability and trust records were identical.

Observed:

    eligibility identical
    missing capability/trust sets identical
    trust tier identical

PASS.

### Missing capability blocks eligibility

The Git-API-only executor lacked:

    process_execute

Observed:

    eligible=false
    missing_capabilities=["process_execute"]

PASS.

### Missing trust property blocks eligibility

The local-unbound executor had process capability but lacked:

    subject_bound

Observed:

    eligible=false
    missing_trust_properties=["subject_bound"]

PASS.

### Hosted label does not confer T2

Two executors both had:

    surface_label=hosted

but differed in producer authenticity.

Observed:

    isolated + producer_authentic + subject_bound
        -> T2

    isolated + subject_bound only
        -> T2_ISOLATED_ONLY

PASS.

### Request semantics remain invariant

The exact assurance request was unchanged across all executor evaluations.

PASS.

## 3. Negative control

A deliberately wrong trust classifier mapped:

    surface_label=hosted
        -> T2

For the isolated-only hosted executor:

    bad surface-based tier
        T2

    correct property-based tier
        T2_ISOLATED_ONLY

The negative control therefore discriminated as intended.

## 4. Architecture interpretation

P-D6 supports:

    WF-A34 EXECUTOR CAPABILITY MODEL

    WF-A35 EXECUTION SURFACE != TRUST

    WF-A36 PROVIDER / WORKFLOW MECHANISM FREEDOM

It also directly supports the owner's side-note interpretation:

    current ChatGPT / Claude / Codex / Claude Code capability differences
        may matter to execution planning

but:

    model identity
        does not own assurance semantics

and:

    local / hosted / Git-API execution label
        does not by itself determine assurance trust

## 5. Scope limits

The probe does NOT establish:

    which real model currently has which complete capability set

    that any current hosted runner is authentic T2

    that GitHub is the target provider

    that local execution is preferred

    that one planner implementation is production-ready

This is a semantic-architecture feasibility result.

## 6. Result class

Under Research 277:

    P_D6=PASS
    TARGET_ARCHITECTURE_EVIDENCE=SUPPORTED
    CURRENT_PROVIDER_SELECTED=false
    MODEL_SPECIFIC_SEMANTICS_REQUIRED=false

WARRANT-F V0.2 requires no amendment from this probe.

## 7. Current state

    P_H=INCONCLUSIVE
    P_D6=PASS

    COMPLETED_DECISION_PROBES=2_OF_8
    UNRESOLVED_AMEND_RESULTS=0
    HARNESS_INVALID_RESULTS=0

    OWNER_ASSURANCE_DECISION=HELD
    NEXT=P_D3_BOUNDARY_ABSENCE
