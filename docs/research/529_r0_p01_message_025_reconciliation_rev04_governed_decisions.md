# Research 529: Claude Message 025 reconciliation and REV04 governed boundary

**Date:** 2026-10-10
**Status:** TARGETED T1–T3 DESIGN RECONCILED / TWO OWNER PREFREEZE DECISIONS PENDING
**Scope:** Reconcile Claude Message 025 against V02 harness and frozen Research 513, document corrected unfrozen successor V03 REV04 proposal, and prepare independent B01/B02 governance decisions without a new owner trial.
**Parent:** Research 528 / Validation 217 / Checkpoint 864 / MC-0030 Message 025
**Validation:** Validation 218, draft-only consistency
**Candidate:** GOVERNED_LEDGER_KERNEL_V02 unselected
**Authority:** Research and owner-decision preparation only. No family interpretation approved, stopping policy accepted, contract freeze, Attempt 002 claim, key creation, signature, WebAuthn ceremony, production implementation, physical-target selection, migration, Specification 028 amendment or authority switch.

The clean branch fast-forwarded from `5cd1761ebf98e67904745ef28e874ee306471175` to `1a331cf2997a2048a2209d89053e1dd6ea2b45ba`, adding only Claude Message 025. Claude returned `AMEND_REV03_TARGETED`, accepted previous R1–R4 substantially and R5–R9 after spot checking, and identified three narrow ordinary-event branch mistakes. Claude explicitly said no additional Claude review round is needed if T1–T3 are applied. This does not waive independent **implementation** qualification.

## Finding-level reconciliation

| Finding | Disposition | Corrected REV04 prospective rule |
|---|---|---|
| T1 WebAuthn cancelled assertion not event-terminal | ACCEPT | Add `WEBAUTHN_ASSERTION_NOT_COMPLETED` when the RP durably records an issued and consumed assertion with NotAllowedError, cancellation or timeout. Like SSH owner S/exhausted unlock budget, it is terminal **no-proof** evidence, not a valid proof. Genuine NotSupportedError uses frozen capability receipts, while other browser/RP faults are instrument failures. Never claim completion from a missing RP receipt. Update G1/G2 scenarios for B completed cancellations. |
| T2 V02 catch-all maps ordinary input/tool errors to integrity | ACCEPT | Add prospective closed exception-site/owner-input table, §8.6: malformed uncaptured decision/CONFIRM/setup input re-prompts with no new proof or integrity failure; exact R/S retry semantics unchanged. Tool, Node, verifier and client faults get instrument flags; real identity/secret/tamper violations remain integrity; owner Ctrl+C is abort. The generic exception-to-integrity fallback is removed from the JSON. Every actual successor raise, subprocess, Node and browser failure site must pass an independent exhaustive inventory and synthetic mapping tests before freeze. |
| T3 missing witness unnamed; flag origin confused | ACCEPT | `evidence.final_head_witness_absent` is SCORER_DERIVED and DISCLOSURE_ONLY. Its absence weakens independent tamper assurance but **never** changes result or permits another claim. Actual chain/provenance mismatches retain integrity consequences. Enumerate eleven flag origins including separately derived instrument summary and scorer-derived hash checks; no discretionary INVALID reasons. |

The optional `pre_fault_counterfactual_class` is not introduced as a new scoring rule; a future nonbinding diagnostic would need an exact prospective definition. REV04 normalizes prior accidental backslash-escaped Markdown code ticks in the **unfrozen draft only**. Frozen historical contracts and Attempt 001 remain untouched.

## Targeted design validation

Validation 218 checks ten identical §11/JSON blockers, seven outcome rows, two-new-claim maximum, ALL_REQUIRED exceptions, no claim after PASS or after integrity under this policy, seven terminal outcomes and eleven flag origins. Fourteen static simulated branch scenarios PASS, including A nonviable + B all cancelled -> REOPEN; A eligible + B all completed cancellations -> PASS without G2; A eligible + B truly interrupted -> PASS with G2; ordinary owner typo does not change result; missing witness does not change AMEND/REOPEN; instrument vs integrity precedence remains fixed. This validates design rules, **not** Windows SSH/Node/WebAuthn, the real successor scorer, snapshot atomicity or future owner proof.

## Governed next action, no inferred approval

There are two separate proposed human decisions in `docs/research/r0_p01_successor_design/R0_P01_GOVERNED_PREFREEZE_DECISIONS_UNAPPROVED.md`:

**B01: Research 513 prospective interpretation.** Approve/decline/amend the G1/G2 proof-`evidence_state` qualification, four-class P01 primary scoring of all **claimed** attempts, and deterministic INVALID reason hierarchy. Keep Research 513 and original Attempt 001 unchanged, and apply this only to a separately frozen successor.

**B02: stopping policy.** Independently approve/decline/amend the exact REV04 JSON: historical 001 remains AMEND; at most two **new** claims in successor family (planned 002, at most exceptional 003); no automatic 003; all exception conditions required; no claim after PASS or integrity failure within policy; owner Ctrl+C or external crash consumes claim; an owner declining before the claim is NOT_RUN; separate future trial execution authorization still mandatory.

**Both decisions are unapproved.** A generic request to proceed is not consent. After explicit decisions, an independently reviewed prospective fixture/harness/scorer freeze and complete synthetic A/B/C qualification would be required before requesting a **third, separate** authorization to run owner Attempt 002.

The original Attempt 001 remains irreversibly `AMEND / VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY` (A 12/13 controls, recovery FAIL, S02 130.8491039001383 seconds, B/C interrupted). Original marker, 25 raw snapshots, independent backup, private keys and frozen code untouched. R0-P02 PASS, R0-P03 pending, physical target unselected, Specification 028 unchanged, unrelated scientific experiment INCOMPLETE.

```text
RESEARCH_529=REV04_T1_T3_RECONCILED
VALIDATION_218=STATIC_SCENARIO_PASS
B01_APPROVAL=NOT_GIVEN
B02_APPROVAL=NOT_GIVEN
ATTEMPT_002=NOT_AUTHORIZED
NEXT=HUMAN_PREFREEZE_GOVERNANCE_DECISIONS
```
