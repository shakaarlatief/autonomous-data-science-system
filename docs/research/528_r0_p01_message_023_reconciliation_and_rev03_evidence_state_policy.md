# Research 528: R0-P01 Message 023 reconciliation and REV03 evidence-state policy

**Date:** 2026-10-10
**Status:** AMEND_REVISED_DRAFT RECONCILED / REV03 UNFROZEN / TARGETED REVIEW NEXT
**Scope:** Reconcile Claude's R1–R4 blockers and R5–R9 refinements against the unfrozen successor design, preserving Attempt 001 and any unapproved owner or family-governance decisions.
**Parent:** Research 527 / Checkpoint 863 / MC-0030 Message 023 / Research 513
**Validation:** Validation 217, static draft consistency only
**Candidate:** GOVERNED_LEDGER_KERNEL_V02 unselected
**Authority:** No Research 513 interpretation approval, stopping-policy assent, prospective contract freeze, Attempt 002, owner key, WebAuthn registration, production implementation, migration, Specification 028 amendment or authority switch.

Claude Message 023, commit `8783994f267718be6a24a86fb6c4151d0ca93249` (parent `879063d0156f650ca081d6188ac5128c80783c9f`), adds only the reviewer message and returns `AMEND_REVISED_DRAFT`. C1/C3/C4/C5 were accepted at design level. The critique's new primary defect is that G1/G2 used successful setup rather than actual completed proof evidence. The review is comparative: Claude also designed parts of the earlier recommendations.

## Blocking R1–R4 dispositions

| Finding | Resolution in UNFROZEN REV03 |
|---|---|
| **R1: false REOPEN** | Define scorer-derived A/B `evidence_state`: NOT_REALIZABLE requires genuine capability evidence; COMPLETED requires same-attempt terminal P0 and S01/S02/S03 event receipts; INCOMPLETE means remaining incomplete events even if setup succeeded. Owner S and exhausted unlocks are terminal events; process Ctrl+C/crash or VERIFIER_ERROR is not. G1 returns REOPEN only when neither proof-viable and **both** states COMPLETED/NOT_REALIZABLE. G2 flags PASS when alternative arm INCOMPLETE, regardless of setup status. L01/P5/P6/control 13 remain full eligibility gates. |
| **R2: discretionary INVALID subtype** | Exact ordered source flags define INVALID_INTEGRITY first, INVALID_INSTRUMENT second, INVALID_INCOMPLETE via G1 third. Scorer derives the reason, reports source flags, and may not accept a free-text reclassification. Substantiation of a repaired defect happens only in a separate governed exceptional-claim decision, never by editing scored evidence. |
| **R3: verifier fault misflagged as integrity** | VERIFIER_ERROR sets distinct `integrity.verifier_error`, `integrity.instrument_failure` and enumerated kind; it does **not** set `integrity.attempt_integrity_failure`. Genuine integrity and instrument flags together resolve INVALID_INTEGRITY. |
| **R4: contradictory JSON** | Delete obsolete `open_review_blockers`, replace vague G1/G2 text with structured evidence-state rules, add exact raw-flag schema and keep only one `unresolved_blockers` sequence, identical to the ten IDs in contract §11. The stopping policy retains seven non-overlapping cases, two-new-claim cap, ALL_REQUIRED exception conditions and no after-PASS claim. |

## Secondary R5–R9 outcomes

The revised draft distinguishes owner S (terminal event, run continues when possible) from Ctrl+C (whole claimed attempt abort, scored); dependent controls are FAIL/unexecuted when an earlier proof is missing. Snapshot design adds exclusive temporary files, fsync, qualified Windows no-overwrite atomic rename, previous-file-byte hash links and a **named owner postrun final-head/count witness before scoring**; missing/corrupted evidence is mechanically fail-closed. This is not crash resume or rollback resistance without an external witness.

PASS_WITH_SELECTION terminates the successor family even if G2 declares the selection uncontested. Windows Node RP state requires separately qualified process-group isolation or durable owner-local RP event receipts, with no invented completed registration/assertion after Ctrl+C. R9 refinements cover probe-instance versus production-domain context, explicit rejection layer, full old-statement digest set including negative copies, preclaim-page-only forbidden-API scan, user-agent mismatch report, synthetic Chromium/CTAP2 virtual authenticator limits and external power loss consuming a claim.

## Targeted validation and next boundary

Validation 217 reports **nine purely static/design scenario checks** passing, covering false-REOPEN, evidence-state, integrity/instrument precedence, JSON case uniqueness and blocker matching. They are not live Windows or successor scorer tests. The revised sources are `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md` and `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json` (REV03; historical revisions remain in Git).

Next: a **targeted** Claude Message 025 check of R1–R4 and bounded R5–R9 changes, rather than another automatically broadened review cycle. On technical convergence, Research 513 G1/G2 family interpretation and the owner's **stopping-policy** approval must be handled separately, **before freeze**. Distinct subsequent owner trial authorization follows only after prospective implementation and full synthetic qualification.

Original Attempt 001 remains immutable AMEND (A 12/13 controls, recovery FAIL, S02 130.849 seconds, B/C incomplete). Its marker, raw snapshots, hash-verified backup, keys and frozen V02 code are untouched. R0-P02 PASS, R0-P03 pending; physical target unselected; Specification 028 and unrelated scientific INCOMPLETE unchanged.

```text
RESEARCH_528=CLAUDE_MESSAGE_023_RECONCILED
V03_DRAFT=REV03_UNFROZEN
G1_G2_FAMILY_APPROVAL=NOT_GIVEN
OWNER_STOPPING_POLICY_APPROVAL=NOT_GIVEN
ATTEMPT_002=NOT_AUTHORIZED
NEXT=MC0030_TARGETED_RECHECK
```
