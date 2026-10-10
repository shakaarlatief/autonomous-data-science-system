# R0-P01 prospective prefreeze decisions: owner packet (UNAPPROVED)

**Date:** 2026-10-10
**Status:** TWO DISTINCT OWNER DECISIONS OPEN / NOT OWNER AUTHORIZATION
**Scope:** Describe prospective Research 513 family interpretation B01 and exact stopping policy B02, with consequences and alternatives, before any new successor fixture or implementation freeze.
**Parent:** Research 529 / Validation 218 / V03 REV04 unfrozen contract and policy
**Authority:** Only a human owner can expressly decide B01 and B02. Preparing this packet neither approves either choice nor starts Attempt 002.

## B01: prospective evidence-state and result interpretation

**Proposal:** For a **new separately frozen R0-P01 successor only**, preserve Research 513's five global result classes and P01's four specific scored classes while defining when an interrupted attempt provides enough evidence to infer architecture infeasibility.

- Every **claimed** attempt eventually receives exactly one P01 class (PASS_WITH_SELECTION, AMEND, REOPEN or INVALID) after qualified scoring. Declining before claim is NOT_RUN; an unqualified scorer environment is temporarily pending, not an alternative final score.
- A/B arms have NOT_REALIZABLE with genuine capability evidence, COMPLETED after P0 plus S01/S02/S03 each records a terminal proof event, or INCOMPLETE otherwise. Completed SSH owner Stop/exhausted unlocks and durably RP-consumed NotAllowedError/timeout/cancellation count as **terminal no-proof evidence**, not as successful owner signatures. Ctrl+C/crash/unvisited event does not count completed; NotSupportedError requires independently eligible capability evidence.
- **G1:** Neither arm viable means REOPEN only if both completed viability evidence or were genuinely not realizable; otherwise INVALID_INCOMPLETE without architecture inference.
- **G2:** Preserve inherited security/timing/selection gates, but when one arm is eligible and its comparator incomplete, the selection records `OTHER_ARM_INCOMPLETE` as an uncontested result.
- INVALID_INTEGRITY, INVALID_INSTRUMENT and INVALID_INCOMPLETE are deterministic subordinate **reasons** for INVALID, not new primary classes. The historical Attempt 001 AMEND is not rescored, retried or reinterpreted.

**B01 choices:** `ACCEPT_B01`, `AMEND_B01` (describe change), or `DECLINE_B01`. Approval is limited to **prospective Research 513 family interpretation** and does not authorize any actual owner action.

## B02: finite stopping policy

**Proposal:** Approve the exact revision/hash of `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json` as a governance decision **before** future protocol freeze.

- Historical Attempt 001 is consumed AMEND. This follow-up family permits at most **two new owner claim events**, an intended Attempt 002 and at most one separately owner-approved, independently qualified exceptional Attempt 003.
- No automatic Attempt 003. Every exceptional condition must be satisfied together (`ALL_REQUIRED`). INVALID_INSTRUMENT can potentially support a genuinely substantiated and tested instrument repair under a new freeze without a different mechanism hypothesis, within cap. AMEND/REOPEN/INVALID_INCOMPLETE require a new falsifiable hypothesis for any exception, and INVALID_INTEGRITY admits none under this policy.
- **After PASS_WITH_SELECTION, even with G2**, no new claim in this family may be used to change which arm won. Future engineering of a different arm would require separate downstream qualification, not an R0-P01 retry.
- A person may decline before claim (NOT_RUN). If a claimed run is interrupted by owner Ctrl+C, OS reboot, power loss or owner abort, the claim is consumed and still scored. An owner may always stop; the evidence consequence is disclosed rather than being used to pressure continued participation.
- Missing a later independent owner final-head witness only weakens tamper assurance and is disclosure-only; it never changes the result or grants another attempt. A proven snapshot chain breach has the frozen higher-priority integrity consequence.
- Approving this policy does **not** approve key generation, WebAuthn registration, native passphrase/biometric use, or starting Attempt 002. Those require a separately frozen and synthetically qualified implementation and a **third distinct owner authorization**.

**B02 choices:** `ACCEPT_B02`, `AMEND_B02` (describe change), or `DECLINE_B02`. The exact policy bytes and SHA-256 must be pinned in the subsequent decision receipt.

## Separate approvals and next steps

Both choices are independently available; the owner may accept one and amend or decline the other. A generic "proceed" is not approval. Without both approvals, do not freeze this successor. Even with both approvals, next steps are reviewed exact fixture/contract/scorer implementation, exhaustive error-site and Windows/OpenSSH/browser tests, synthetic A/B/C qualification, and only afterwards asking whether the owner wishes to run an actual fresh Attempt 002. No real keys, secrets or owner proofs are needed to decide B01/B02.

```text
B01=UNAPPROVED
B02=UNAPPROVED
SUCCESSOR_V03_REV04=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
