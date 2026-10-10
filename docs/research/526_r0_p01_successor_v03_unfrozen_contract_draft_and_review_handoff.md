# Research 526: R0-P01 prospective V03 successor contract draft and peer-review handoff

**Date:** 2026-10-10
**Status:** EXACT CANDIDATE DRAFT COMPLETE / INDEPENDENT CRITICAL REVIEW NEXT / NOT FROZEN
**Scope:** Record a non-executing detailed prospective R0-P01 full successor protocol and machine-readable stopping policy, including every known new-boundary risk and required independent review.
**Parent:** Research 525 / Validation 216 / Checkpoint 861 / MC-0030 Message 019
**Source family:** Research 513 and original R0-P01 V0.1/V0.2 frozen contracts, preserved as historical authority for Attempt 001
**Candidate:** GOVERNED_LEDGER_KERNEL_V02, unselected
**Authority:** Draft research only. Not a contract refreeze, owner-sensitive trial, start marker, key creation, production implementation, migration, Specification 028 amendment, or authority switch.
**Interaction:** ChatGPT / chatgpt-37 task owner.

## 1. Draft artifacts

The source-of-truth proposal is:

- `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md`: full sectioned design with experimental invariants, attempt identity, owner credential lifecycle, exact role-cue tiers, bounded unlock-event design, WebAuthn setup, A/B/C arm/control order, timing, evidence, scoring, stopping policy, preregistration tests and explicit review blockers.
- `docs/research/r0_p01_successor_design/R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json`: machine-readable **proposal** mapping complete scored outcomes and unscored operational stops to precommitted follow-up dispositions. `freeze_authorized=false`; `owner_execution_authorized=false`.

Both are proposal artifacts only. Neither may be executed as a credential or proof workflow or substituted for the next independently qualified actual protocol freeze. Any future reviewer can recommend changes without violating a nonexistent successor result.

## 2. Key choices made prospectively

1. **Immutable predecessor:** Attempt 001 remains AMEND, not rescored or patched. The old marker, 25 raw snapshots, independent backup, distinct original owner keys and validation record remain unchanged.
2. **New identity:** Candidate Attempt 002 would have an exclusive new start claim, new separate public evidence and owner-only fresh Ed25519 keys, unique statement context/acceptance namespace, attempt-local new WebAuthn identity and automated disjointness tests against prior proof digests. No owner setup takes place now.
3. **Security gates unchanged:** 13/13 controls, zero-miss rule, A/B selection and C nonselection, 1/2/4/30-effect burden, original 60/120/120 seconds, volume and edit/secret gates untouched.
4. **Exactly one owner decision/proof event:** Three *prospective* SSH passphrase unlock opportunities only after a demonstrably recoverable no-proof-created error; no generic subprocess retry, new decision, new acceptance ID, timer reset or fourth chance. WebAuthn platform UV retries remain opaque and explicitly **not** falsely described as equal to SSH.
5. **Owner display:** Governing T1 and possible explanatory T2 information are display-bound according to AC-1, while frozen procedural T3 (primary/recovery role cues, time notices, safe localhost opening) is visibly outside decision view and both signature digests.
6. **Timing honesty:** New subinterval monotonic landmarks provide diagnosis but do not excuse elapsed signing time. S02's original 130.8491039001383-second miss is permanently preserved without asserting its cause.
7. **No invented crash recovery:** Old numbered append-only records were never a qualified resume journal. Proposed minimal successor has safe arm-boundary pauses only within one process, not cross-process resumption. A Windows SIGINT confirmation layer is optional and prohibited unless independently qualified with native children. No trick to make Ctrl+C copying work.
8. **Verifier known-answer gate:** Before scoring real public owner proofs, synthetic positive and negative SSH/WebAuthn verifications must succeed in that *same authorized execution environment*. Preflight problems do not silently become owner signature INVALID.
9. **Finite attempt policy:** At most one separately owner-approved new Attempt 002 by default, with no automatic Attempt 003. A successor PASS is qualified **only** under its own prospective contract and must be presented together with original AMEND. Scored AMEND/REOPEN/INVALID and unscored terminations each stop, with different governed consequences.

## 3. Actual remaining review blockers

The draft is detailed, but intentionally not yet freeze-ready. Independent reviewer must resolve at least:

- How to recognize an incorrect native Windows OpenSSH passphrase without logging secrets, swallowing the owner prompt, or retrying non-unlock errors.
- Whether `TERMINATED_UNSCORED` and `ENVIRONMENT_PREFLIGHT_BLOCKED` can be represented as no-probe-result rather than illegally adding a fifth Research 513 result class, and when interrupted-arm data may legitimately support AMEND or REOPEN.
- Exact prior/new statement digest noncollision, public-identity comparisons without unnecessary fingerprint publication, and claims about the limits of key-creation-time provenance.
- Whether the noncredential browser preflight scope and assisted localhost browser launch can be tested without contaminating WebAuthn capability outcomes.
- How to measure/control Windows Ctrl+C, subprocess cancellation, incomplete proof files and evidence append-only preservation, while intentionally avoiding unproven cross-process resumption.
- Whether owner-facing stopping-policy approval and anticipated proof/setup burden are sufficiently explicit before any new irreversible claim.
- All implementation/conformance vectors still need prospective generation and independent test; none has been produced with owner credentials.

These are substantive **BLOCKERS**, not license to loosen Research 513 after seeing the outcome. The successor is not approved even though the draft exists.

## 4. Task-owner next action and boundaries

Request bounded independent adversarial review from Claude / claude-04 using existing MC-0030 thread, or an independent reviewer of equivalent capability if required. The reviewer should critique the exact draft and policy and return `ACCEPT_DRAFT_FOR_PROSPECTIVE_REFREEZE_DESIGN`, `AMEND_DRAFT_BEFORE_FREEZE`, or `REOPEN_QUALIFICATION_APPROACH`, with minimum concrete contract corrections. This is **not** selection of a physical target.

After review, ChatGPT reconciles differences, prepares a potentially freeze-ready **exact** V03 fixture, proof/error tests, implementation constraints, result normalization and owner-facing authorization package, then independently qualifies artifacts. Only then can the human explicitly decide whether to begin Attempt 002.

Research 513's preferred R0-P02 -> P01 -> P03 scored order remains. Parallel *design research* for P03 does not authorize its scored run or a change in probe order.

```text
RESEARCH_526=R0_P01_SUCCESSOR_V03_DRAFT_READY_FOR_CRITIQUE
SUCCESSOR_PROTOCOL_FREEZE=NOT_AUTHORIZED
SUCCESSOR_OWNER_EXECUTION=NOT_AUTHORIZED
CURRENT_BOUNDARY=p-one-successor-draft-review
NEXT=MC0030_INDEPENDENT_DRAFT_CRITIQUE
```
