# R0-P01 B02: owner approves finite successor stopping policy

**Date:** 2026-10-10
**Status:** ACCEPTED / EXACT REV04 POLICY / NO OWNER TRIAL
**Scope:** Record the human owner's explicit ACCEPT_B02 decision binding the exact REV04 machine-readable stopping policy by SHA-256 before any successor protocol freeze.
**Parent:** Research 529 / Checkpoint 865 / owner decision packet / B01 independent decision
**Authority:** Human approval of the finite stopping rule only, recorded by ChatGPT. Does not approve a real owner attempt or an automatic conditional rerun.

## Exact human decision and byte-bound target

The human owner responded: `ACCEPT_B01 and ACCEPT_B02`. This record concerns **B02 only**.

- Decision: `ACCEPT_B02`.
- Exact policy: `docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json` at published parent HEAD `83619072f3c127b715252f909e042a7226b5780c`.
- Accepted **exact-file SHA-256**: `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c`. Verify against the source bytes before deriving any later immutable implementation contract.
- Related REV04 contract SHA-256: `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175`.
- The policy's historical embedded `owner_stopping_policy_approved=false`, `freeze_authorized=false`, `owner_execution_authorized=false` are **predecision drafting-state fields**. Do **not** modify the owner-approved proposal in place to toggle them: that would change the approved hash. The distinct human decision receipt is authoritative for the B02 acceptance; a **new** future implementation manifest must bind both proposal hash and decision receipt and carry its own accurately qualified lifecycle status.

## Exact terms accepted

1. Original Attempt 001 remains consumed and AMEND. **Absolute cap of two new owner claim events** in this successor family, the proposed Attempt 002 and at most one separately authorized exceptional Attempt 003. Neither starts by default.
2. Every exceptional condition is `ALL_REQUIRED`, including bounded documented cause/remedy, specific fresh human approval, independent prospective freeze and tests, new exclusive attempt identity/keys/evidence, and remaining numerical capacity. Further retries beyond the cap require a separately justified and preregistered new Research 513 governance decision, not the same policy silently extended.
3. After `PASS_WITH_SELECTION`, including G2 uncontested selection, no further family claim may change the winning arm. After `INVALID_INTEGRITY`, this policy permits **no** exceptional new claim.
4. A substantiated instrument-only defect might justify one independently reviewed, repaired exceptional claim within cap, with fresh authorization and evidence. `AMEND`, `REOPEN`, or `INVALID_INCOMPLETE` require a genuinely new falsifiable mechanism hypothesis plus all required conditions; no attempt-level retry-to-green.
5. Human decline **before** a claim is `NOT_RUN_PRECLAIM`. Once claimed, owner Ctrl+C, abandonment, power loss or crash still consumes the claim and the preserved evidence must ultimately receive one scored P01 class after qualified processing. The owner retains the absolute right to stop at any time.
6. `evidence.final_head_witness_absent` is disclosure-only. A genuinely proven tamper/chain violation retains its stronger integrity classification. No missing evidence may be silently converted into a valid owner proof or a free trial.

## Effect and limits

B02 is now accepted before a potential freeze, but the accepted JSON remains `UNFROZEN_NOT_EXECUTABLE` until a separate prospective freeze binds qualified fixture, scorer, harness and known-answer tests. This acceptance cannot be read as permission to create Attempt 002 start marker, owner SSH credentials, WebAuthn registration, or execute any live user ceremony. A **third later explicit human execution authorization** is mandatory after full synthetic qualification.

```text
B02=ACCEPTED_BY_EXPLICIT_HUMAN_OWNER
POLICY_SHA256=9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c
MAX_NEW_CLAIMS=2
AUTO_ATTEMPT_003=FORBIDDEN
POST_PASS_EXTRA_CLAIM=FORBIDDEN
OWNER_EXECUTION=NOT_AUTHORIZED
```
