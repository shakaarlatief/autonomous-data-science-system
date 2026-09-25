# Research 317: DRP-09 Assurance-Request Claim-Integrity Harness Freeze

**Date:** 2026-09-25
**Status:** DRP-09 FIXTURE + HARNESS FROZEN / EXECUTION NOT YET RUN / NO RESULT OBSERVED
**Parent protocol:** Research 316 / AO10-DRP-V01
**Probe:** DRP-09
**Protocol freeze commit:** 58b099896bcca0b804b6efee92dc45e4ab25a6aa
**Scope:** Freeze the target-shaped fixture and deterministic harness for testing that AO request shaping cannot suppress policy-required WARRANT-F assurance.
**Authority:** Probe implementation freeze only. The harness is temporary qualification machinery and does not select target code, policy storage, provider, runtime, or production interface.

## 1. Probe question

Can AO invoke WARRANT-F without gaining the ability to suppress policy-required claims, weaken consequence/freshness/trust requirements, or bypass exact subject/base-revision binding?

Research 316 preregisters a zero-tolerance AMEND if one policy-required claim can be lost through request shaping.

## 2. Harness surface

    experiments/ao10_drp09_assurance_request_integrity_v01/README.md
    experiments/ao10_drp09_assurance_request_integrity_v01/policy.json
    experiments/ao10_drp09_assurance_request_integrity_v01/cases.json
    experiments/ao10_drp09_assurance_request_integrity_v01/probe.py

Frozen SHA-256:

    README.md
        be00bb0e5963f34392b2a1aed372addae9540e342529d5dd9e3e5da1d6351c54

    policy.json
        609e9e22d6acca60b059861ead0b2fbf7ac73ded4b6e95d9d195a9fedcecdd2a

    cases.json
        33ab9a8f88f95b13430483ab387b70199d3260f39b619ad9d3de4101b62ca7df

    probe.py
        d856a675eda9c64b360ce2d34c2958626a557185df974edf443c1e6eba385782

## 3. Frozen policy fixture

The effective policy owns:

    subject_id
    subject_revision
    required base revision
    required claim set
    consequence floor
    consequence ordering
    trust floor
    freshness ceiling
    known profile shorthands
    governed supplemental-check mapping

The three baseline policy-required claims are:

    claim:exact-binding
    claim:semantic-contract
    claim:negative-control

The request may carry requested_claims for compatibility/adversarial testing, but the correct evaluator never treats that field as authoritative.

## 4. Frozen request cases

The fixture contains 13 cases, exceeding the preregistered minimum of 12:

    C01 normal
    C02 omit one requested claim
    C03 omit multiple requested claims
    C04 alternate profile shorthand
    C05 stale subject revision
    C06 stale base revision
    C07 weaker requested consequence
    C08 missing trust context
    C09 supplemental informational context
    C10 governed extra check
    C11 unknown profile
    C12 contradictory profile/context
    C13 stale evidence

Expected decisions are frozen in cases.json before execution.

No result has been observed.

## 5. Seeded-violation witness

The harness contains a deliberately faulty evaluator mode that derives effective claims from request.requested_claims rather than policy.required_claims.

The witness is evaluated on C02 and C03.

The probe is valid only if the harness detects both seeded suppression defects.

This is a sensitivity witness for the exact architecture failure DRP-09 is designed to prevent.

## 6. Decision rules

PASS only if:

    all 13 frozen cases match their frozen expected decision

    all policy-required claims remain in the effective claim set for every case

    the governed extra-check case adds its supplemental claim without removing
    any policy claim

    exact subject/base mismatch remains fail-visible

    consequence/trust/freshness cannot be weakened by request/profile/context

    both faulty-normalizer seeded violations are detected

Any required-claim suppression is AMEND.

A harness defect is HARNESS_INVALID, not a target failure.

## 7. Pre-execution validation

Completed without running the probe:

    Python AST parse            PASS
    policy.json parse           PASS
    cases.json parse            PASS

Scored execution has NOT occurred.

## 8. Frozen execution

From repository root:

    .\.venv\Scripts\python.exe experiments\ao10_drp09_assurance_request_integrity_v01\probe.py --output experiments\ao10_drp09_assurance_request_integrity_v01\results\run_001

The result directory does not yet exist.

Expected evidence:

    experiments/ao10_drp09_assurance_request_integrity_v01/results/run_001/result.json

Exit 0 is permitted only when all frozen cases pass and both seeded violations are caught.

## 9. Current boundary

    DRP09_PROTOCOL=RESEARCH316_FROZEN
    DRP09_HARNESS=RESEARCH317_FROZEN
    DRP09_EXECUTED=false
    DRP09_RESULT=NONE

    OWNER_DECISION=HELD
    PRODUCTION_IMPLEMENTATION_AUTHORIZED=false
    PHYSICAL_MIGRATION_AUTHORIZED=false
    AUTHORITY_SWITCH_ALLOWED=false

    NEXT=EXECUTE_DRP09
