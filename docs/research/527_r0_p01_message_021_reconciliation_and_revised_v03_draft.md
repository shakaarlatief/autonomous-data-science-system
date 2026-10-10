# Research 527: R0-P01 Message 021 reconciliation and revised unfrozen successor

**Date:** 2026-10-10
**Status:** MESSAGE 021 RECONCILED / V03 DRAFT REV02 / NOT FROZEN
**Scope:** Resolve Claude's five blocking critiques in an unfrozen protocol/policy draft without changing original R0-P01 evidence or creating owner credentials.
**Parent:** Research 526, Checkpoint 862, MC-0030 Message 021, frozen Research 513/V02
**Authority:** Prospective research/drafting only. Neither Research 513 family-interpretation, owner stopping policy, new fixture, implementation, physical target, migration nor owner execution is approved.

The guarded fast-forward to `e431b4de38949a6e9014b02a1212bcc6039815f7` introduced only Claude Message 021, parent `40e54de2181aec9abda913ad81180795c18f6a22`. Claude's verdict was `AMEND_DRAFT_BEFORE_FREEZE`; prior participation was disclosed, so this was comparative critique.

## Adjudication of C1–C5

| Criticism | Disposition and corrected proposed contract |
|---|---|
| C1 fragile unlock error classifier | ACCEPT. Drop stderr parsing and localization dependency. Keep inherited-console native `ssh-keygen -Y sign` invocation shape; recheck key/header, public identity, canonical statement bytes, agent, executable and signature absence before each of max three invocations. Nonzero plus no signature leads to owner choice R or S while timer continues; unexpected output is terminal. No automatic retry and no passphrase disclosure. |
| C2 escaping scored results by abort | ACCEPT with differentiated INVALID reasons. Each claimed attempt eventually receives one of P01's four classes. Proposed G1 requires both cryptographic arms resolved for REOPEN; otherwise if neither proof-viable and one unresolved, INVALID_INCOMPLETE. Proposed G2 flags PASS/selection when the other arm is interrupted as OTHER_ARM_INCOMPLETE, without changing eligibility. `SCORING_PENDING_QUALIFIED_ENVIRONMENT` is temporary, not a fifth score. Research 513 global vocabulary has five classes including PASS; P01 uses four. G1/G2 require **explicit prospective family-level interpretation approval before freeze**. |
| C3 in-trial verifier failures | ACCEPT. VALID/INVALID/VERIFIER_ERROR must distinguish completed bad signature from verifier malfunction. Frozen synthetic positive/negative SSHSIG and WebAuthn KAT plus secure temporary-file probe run **in the owner harness environment before claim**, with no marker on failure. In-trial verifier error preserves any public proof and ends with INVALID_INSTRUMENT, not owner signature failure. Scorer also KAT-gated in its own environment. |
| C4 impossible statement preregistration | ACCEPT. Structural VERIFY enforces exact successor context, synthetic project_id and acceptance-ID prefix, rejecting old-context proofs. P5/P6 use synthetic-key golden-vector templates because owner key IDs do not exist preclaim. Prior real statement digests are compared at runtime only as defense-in-depth; old public IDs checked locally. Correct AC-1: envelope_digest binds canonical envelope, shown_digest binds rendered owner-view bytes. |
| C5 non-finite stop rule | ACCEPT with INVALID_INCOMPLETE separated from instrument failure. **Absolute two new claims** in this successor family: prospective Attempt 002, plus at most one separately approved exceptional Attempt 003. Exception conditions are ALL_REQUIRED; an independently substantiated instrument repair may keep the mechanism hypothesis; other exceptions require a genuinely changed falsifiable hypothesis; integrity breach grants no exception in this policy. NOT_RUN applies only before claim. Owner approval of stop rules required **before protocol freeze**, followed by separate execution approval after implementation qualification. Beyond cap requires a new governed Research 513 preregistration, not same-policy retry. |

## Supporting improvements

The updated draft requires matched preclaim browser user-agent and launch method (reachability-only, no WebAuthn API); postclaim registration only; explicit B P6 dependence on **new A recovery key**; drop optional Ctrl+C handler; no cross-process resume; fixed T3 R/S and safe browser wording; a conservative harness-observed mechanical interaction floor; browser-monotonic assertion landmarks; raw snapshot previous-file hash linkage with an *independently witnessed final digest* (not a resume journal); tests against embedded historical attempt-ID literals; and a full synthetic A→B→C compositional dry run before freeze.

**Open work is real:** These are draft-level resolutions, not tested Windows signing and WebAuthn implementation. No Research 513 G1/G2 interpretation or stopping-policy consent has been given. Target-machine synthetic native-prompt and Ctrl+C receipt, KAT and tri-state VERIFY qualification, synthetic P5/P6 vectors, WebAuthn preflight and full synthetic test, hash-chained snapshot verification, exact scorer branch proof and separate authorization package still precede any freeze.

Source drafts revised in place while UNFROZEN (Git retains their original versions): `docs/research/r0_p01_successor_design/R0_P01_CONTRACT_V03_UNFROZEN_DRAFT.md` and `R0_P01_OUTCOME_POLICY_V03_UNFROZEN_DRAFT.json`. Reviewer should critique the **new actual content**, not assume acceptance based on this rationale.

Attempt 001 remains immutable `AMEND / VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY`; A 12/13 controls PASS with P6 recovery FAIL, S02 130.8491039001383 s, B/C interrupted; old marker, 25 snapshots, backup, old keys and frozen code unchanged. R0-P02 PASS, R0-P03 pending, physical GOVERNED_LEDGER_KERNEL_V02 unselected, Specification 028 and unrelated scientific INCOMPLETE unchanged.

```text
RESEARCH_527=REVISED_DRAFT_READY_FOR_CRITIQUE
C1_C5=PROPOSED_RESOLUTIONS_UNFROZEN
RESEARCH_513_G1_G2=NOT_APPROVED
OWNER_STOPPING_POLICY=NOT_APPROVED
ATTEMPT_002=NOT_AUTHORIZED
NEXT=BOUNDED_INDEPENDENT_REV02_DRAFT_REVIEW
```
