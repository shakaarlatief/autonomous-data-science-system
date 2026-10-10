# R0-P01 B01: owner approves prospective Research 513 interpretation

**Date:** 2026-10-10
**Status:** ACCEPTED / PROSPECTIVE ONLY / NO OWNER TRIAL
**Scope:** Record the human owner's explicit ACCEPT_B01 response for the separately identified prospective R0-P01 successor, without retroactive effects or implied execution consent.
**Parent:** Research 529 / Checkpoint 865 / owner decision packet / original frozen Research 513
**Authority:** Human owner acceptance of B01 only, recorded by ChatGPT. Does not constitute an approved implementation, scorer fixture freeze, architecture selection, or owner-sensitive execution.

## Exact human decision and accepted source

The human owner responded in this project conversation: `ACCEPT_B01 and ACCEPT_B02`. This is explicit acceptance of B01 and separately B02, not a generic "proceed". This record concerns **B01 only**.

- Decision: `ACCEPT_B01`.
- Referenced contract source: `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md` at clean published parent HEAD `83619072f3c127b715252f909e042a7226b5780c`.
- Accepted contract proposal **exact worktree-byte SHA-256**: `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175`.
- Paired policy proposal **exact worktree-byte SHA-256**: `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c`, separately accepted under B02.
- The original `R0_P01_GOVERNED_PREFREEZE_DECISIONS_UNAPPROVED.md` is a **historical predecision packet**. Do not rewrite it retroactively. This later signed-off decision record is the prospective authority for B01.

## Exact scope of the approval

For a separately identified and prospectively frozen R0-P01 successor only, B01 accepts the following interpretation of Research 513:

1. Every **claimed** successor attempt eventually receives exactly one unchanged P01 primary result class: `PASS_WITH_SELECTION`, `AMEND`, `REOPEN`, or `INVALID`. Owner decline before claim is `NOT_RUN_PRECLAIM`, not a class; `SCORING_PENDING_QUALIFIED_ENVIRONMENT` is temporary processing, not an escape from scoring.
2. Per-arm `evidence_state` is `NOT_REALIZABLE` only with genuine capability evidence, `COMPLETED` only after every P0/S01/S02/S03 owner proof event has an immutable terminal receipt, or `INCOMPLETE` otherwise. A durably consumed WebAuthn NotAllowedError/timeout/cancelled assertion is a terminal **no-proof** event; native SSH owner S/budget exhaustion is likewise terminal. A missing receipt, process abort, or mere setup REALIZABLE is not a completed owner proof assessment.
3. G1 prohibits `REOPEN` when neither A nor B is viable but one or both have INCOMPLETE evidence. G2 leaves the original arm eligibility and selection untouched while mandating `OTHER_ARM_INCOMPLETE` disclosure for an eligible arm chosen without a completed alternative.
4. `INVALID_INTEGRITY`, `INVALID_INSTRUMENT`, and `INVALID_INCOMPLETE` remain mechanical subordinate reasons for the same P01 INVALID class, with exact source flags and integrity precedence. A missing final-head owner witness is `SCORER_DERIVED / DISCLOSURE_ONLY` and does not change result.
5. Research 513's original global result vocabulary, all old security/burden/time/volume gates and original Attempt 001 classification remain unchanged. This approval is for the new prospective family interpretation only.

## Boundaries

This does not freeze revised implementation bytes, authorize real owner key generation, launch a WebAuthn ceremony, claim Attempt 002, re-score Attempt 001, select GOVERNED_LEDGER_KERNEL_V02, switch project authority, or approve an exception after result observation.

```text
B01=ACCEPTED_BY_EXPLICIT_HUMAN_OWNER
APPLICATION=PROSPECTIVE_R0_P01_SUCCESSOR_ONLY
ATTEMPT_001=IMMUTABLE_AMEND
SUCCESSOR_EXACT_FREEZE=NOT_YET_QUALIFIED
OWNER_EXECUTION=NOT_AUTHORIZED
```
