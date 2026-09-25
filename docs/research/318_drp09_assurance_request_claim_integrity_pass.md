# Research 318: DRP-09 Assurance-Request Claim-Integrity PASS

**Date:** 2026-09-25
**Status:** DRP-09 PASS / POLICY-DERIVED CLAIM INTEGRITY SUPPORTED / V0.3 RETAINED / NEXT DRP-05A/05B
**Protocol:** Research 316 / AO10-DRP-V01
**Harness freeze:** Research 317
**Harness freeze commit:** 97ece84d0deb123e6e647fcf90462f0f8e608c8b
**Probe:** DRP-09
**Execution result:** experiments/ao10_drp09_assurance_request_integrity_v01/results/run_001/result.json
**Durable result evidence:** docs/research/project_knowledge_activation_orchestration/ao10/evidence/drp09_run001_result.json
**Result SHA-256:** 09911fb59ca24642818ce88d28295811a7c1ca2498c27091c0ec620a531fd367
**Scope:** Reconcile the first scored AO-10 decision-relevant probe against its preregistered decision rule.
**Authority:** Research result only. This does not accept V0.3 or authorize production realization.

## 1. Frozen execution

Exact command:

    .\.venv\Scripts\python.exe experiments\ao10_drp09_assurance_request_integrity_v01\probe.py --output experiments\ao10_drp09_assurance_request_integrity_v01\results\run_001

Observed summary:

    probe                         DRP-09
    frozen cases                  13
    cases passed                  13 / 13
    seeded faulty witnesses       2
    seeded violations caught      2 / 2
    harness exit                  0
    all_pass                      true

No threshold, fixture or harness change occurred after result observation.

## 2. Required-claim omission resistance

C02 omits one request-side claim and C03 omits multiple request-side claims.

Under the correct evaluator:

    effective claims still contain all policy-required claims
    decision remains ADMIT when all other policy conditions are satisfied

This demonstrates the intended semantic distinction:

    request-provided claim hints/context
        are not authority

    effective gate policy
        owns the mandatory claim set

The intentionally faulty normalizer instead derives effective claims from request.requested_claims.

Both seeded omission defects are caught as:

    POLICY_REQUIRED_CLAIM_SUPPRESSED
    -> REFUSE

The sensitivity witness therefore works.

## 3. Other policy-ownership checks

The frozen cases also establish in the target-shaped fixture:

    stale subject revision              -> REFUSE
    stale base revision                 -> REFUSE
    consequence below policy floor      -> REFUSE
    missing/insufficient trust          -> REVIEW_REQUIRED
    stale evidence                      -> REFUSE
    unknown profile hint                -> REVIEW_REQUIRED
    supplemental informational context  -> cannot suppress claims
    governed extra-check request        -> may add a claim without removing policy claims

All policy-required claims remain present in every evaluated case, including refusal/review cases.

## 4. Architecture inference

Primary class:

    PASS

Evidence class:

    TARGET_ARCHITECTURE_EVIDENCE

DRP-09 supports the Research 315 / V0.3 amendment:

    AO does not own or choose the effective required claim set
    profile is invocation shorthand only
    AO context cannot weaken policy-owned consequence/freshness/trust
    WARRANT-F computes effective claims from effective gate policy
    supplemental checks may only add through governed extension semantics

No V0.3 amendment is required from this probe.

The probe does not claim:

    production adapter correctness
    provider-host enforcement
    real evidence-store correctness
    deployment integration
    complete WARRANT-F implementation

Those remain realization-stage concerns.

## 5. Current state

    DRP09=PASS
    DRP09_CASES=13_OF_13
    DRP09_SEEDED_VIOLATIONS_CAUGHT=2_OF_2
    V03_ASSURANCE_SEAM=RETAIN

    DRP_RESULT_COUNT=1
    UNRESOLVED_AMEND_RESULTS=0
    ACTIVE_HARNESS_INVALID_RESULTS=0

    OWNER_DECISION=NOT_READY
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=DRP05A_DRP05B_CORPUS_AND_HARNESS_FREEZE
