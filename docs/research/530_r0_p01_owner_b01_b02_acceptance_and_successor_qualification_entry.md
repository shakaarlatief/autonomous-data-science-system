# Research 530: R0-P01 B01/B02 accepted, qualification preparation next

**Date:** 2026-10-10
**Status:** EXPLICIT B01/B02 HUMAN APPROVALS / PROSPECTIVE QUALIFICATION NEXT
**Scope:** Register distinct owner acceptance of the previously proposed Research 513 interpretation and finite stopping policy, and open synthetic fixture/implementation preparation without trial execution.
**Parent:** Research 529 / Validation 218 / Checkpoint 865 / MC-0030 Message 026
**Authority:** Human governance approval only, not new fixture or implementation freeze, real credentials, Attempt 002 execution, physical-target selection, production migration or authority switch.

The human explicitly said `ACCEPT_B01 and ACCEPT_B02` in this project conversation. The clean, published parent SHA was `83619072f3c127b715252f909e042a7226b5780c`. The **exact approved REV04 contract** is `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md`, SHA-256 `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175`. The **exact B02 policy** is `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json`, SHA-256 `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c`. Both verified directly from unchanged bytes before receipt writing.

Three new sources are authoritative for the approvals: separate `R0_P01_B01_OWNER_ACCEPTANCE_20261010.md` and `R0_P01_B02_OWNER_ACCEPTANCE_20261010.md`, and `R0_P01_PREFREEZE_OWNER_DECISIONS_RECEIPT_20261010.json` under `docs/research/r0_p01_successor_design/`. B01 approves prospective G1/G2 evidence-state and deterministic INVALID reasons solely for a future separately frozen successor, leaving original Attempt 001 AMEND. B02 independently approves at most two new claims, no automatic third attempt, no claim after PASS or integrity failure under this policy, with **ALL_REQUIRED** conditions for exceptional work.

**Critical time semantics:** The approved JSON still contains its old `owner_stopping_policy_approved=false` because it was written *before* the human approval. This is historical proposal status, **not** a denial of the later acceptance. Editing it now would destroy the accepted exact-file SHA-256. The separate receipt documents the new authority; future versioned implementation manifests must bind both approved proposal and approval receipt, not change the accepted original bytes.

## Next technical qualification sequence

Q0: Compare Research 513, accepted REV04 proposal, original V02 frozen source **read-only**, and approvals. Produce precise traceable control matrix for original security/timing/volume constraints, synthetic key-dependent P5/P6 template and disjoint future statement identity. Never access old owner private keys.

Q1: Design a separately identifiable exact prospective fixture and scored protocol: canonical sign-what-you-see bytes, static T3, signed-statement domain constraints, scorer result flags and precedence, full error-site/Node/browser disposition inventory, evidence write and final-owner witness contract, synthetic known-answer tests and per-arm comparison fairness. **This design must be qualified before any new real owner use.**

Q2: Implement the new successor with **synthetic credentials only**. Allow complete reconsideration of files, software design, workflow, branching, tooling, CI and collaboration methods where better justified; old implementation layout is not an architectural constraint. Require owner-controlled SSH three-invocation under one statement/timer, WebAuthn RP verification, preclaim same-harness KAT, tri-state valid/invalid/verifier error, complete per-arm P0/S01–03 evidence states, G1/G2, original thirteen hard controls and B02 claim cap.

Q3: Qualify on target Windows with synthetic keys: native OpenSSH interactive prompt, Ctrl+C behavior, process-group Node RP and durable receipts, true malformed owner input re-prompt, browser reachability-only preclaim/virtual WebAuthn limitations, atomic no-overwrite snapshots, predecessor hash links and final-head witness. No cross-process resume is promised.

Q4: Full synthetic A/B/C integrated dry run, P0/P5/P6/security-negative controls, S01/S02/S03/L01 burden and volume checks, error/interrupt cases and independent scorer review. All observed failures and fidelity limits must remain visible.

Q5: Independently qualify versioned exact fixture/scorer/harness/Node source and runtime hashes, prospective freeze/test records and negative controls before any new owner attempt. Any meaningful revision needs reviewed prospective refreeze, not post-result tuning.

Q6: **Third distinct human authorization** before creating Attempt 002 claim, owner SSH primary/recovery credentials, real WebAuthn registration or real proof. B01/B02 do not authorize Q6.

No successor implementation work has been done in this decision-recording step. Attempt 001 remains immutable AMEND, R0-P02 PASS, R0-P03 pending, GOVERNED_LEDGER_KERNEL_V02 unselected, THIN_CENTRED_HYBRID_V03 selected, Specification 028 and scientific INCOMPLETE unchanged.

```text
RESEARCH_530=B01_B02_ACCEPTED
OWNER_ATTEMPT_002=NOT_AUTHORIZED
SUCCESSOR_FIXTURE_FREEZE=NOT_YET_QUALIFIED
NEXT=EXACT_PROSPECTIVE_QUALIFICATION_PREPARATION
```
