# Research 525: R0-P01 Claude critique reconciliation and prospective successor design boundary

**Date:** 2026-10-10
**Status:** AMEND_PROSPECTIVE_DIRECTION ACCEPTED WITH QUALIFICATIONS / DRAFT DESIGN NEXT
**Scope:** Reconcile Claude MC-0030 Message 018 and Research 524 against the frozen owner evidence and code, correct a historical raw-file hash transcription by appended erratum, and route a possible successor to non-executing design.
**Parent:** Research 524 / Checkpoint 860 / MC-0030 Messages 017 and 018
**Validation:** Validation 216 (raw-file SHA-256 erratum), with original Validation 215 unchanged
**Candidate:** GOVERNED_LEDGER_KERNEL_V02, still unselected
**Authority:** No successor trial freeze, credential setup or signing, modification of Attempt 001, physical-target selection, production implementation, migration, Specification 028 amendment, Runtime Bridge extraction or authority switch.
**Interaction:** ChatGPT / chatgpt-37 task owner; Claude / claude-04 comparative critic, not blind to V02 contractual foundations.

## 1. Independent verification

The repository was fast-forwarded from `096caceeaaf9aaad8548fc688bf5fb635c78f050` to `c4de7bb52c7f85d7ecf230a622e7ba69329a6121`. The latter has exactly the former parent and changes only `docs/model_collaboration/threads/MC-0030/messages/018_claude_r0_p01_amend_triage_critique.md`. It reports `AMEND_PROSPECTIVE_DIRECTION`.

Attempt 001 remains irreversibly claimed, with 25 preserved numbered snapshots and separately hash-matched backup. The unchanged scorer correctly classifies `AMEND / VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY`. Arm A has 12/13 security controls PASS and RECOVERY_CREDENTIAL_DRY_RUN FAIL; S02 recorded 130.8491039001383 seconds against 120, no qualifying infrastructure exception; B/C are interrupted, unqualified. No original thresholds, keys, marker, raw records, contracts or result are changed.

Validation 216 independently rehashed original and backup raw-0024.json to `A48E066ADEA499EB17E4D6240CB459DF315B91F444FDEE4F42AB880BDDC60296`. Both Research 523 and Checkpoint 859 contain the same one-character transcription error at hex digit 58 (`c` rather than `d`); Validation 215 is correct. The original records remain historical and untouched. The scorer's canonical-object `raw_sha256` has a different byte basis.

## 2. Claude F1–F11 reconciliation

| Finding | Task-owner disposition | Justification and limit |
|---|---|---|
| F1: bounded credential unlock retries | ACCEPT PRINCIPLE, QUALIFY SYMMETRY | Frozen SSH calls `ssh-keygen -Y sign` once; nonzero yields no proof. WebAuthn delegates UV retries to the platform inside one `navigator.credentials.get` call. A proposed 3-attempt SSH unlock budget is sensible *inside one unchanged owner statement/proof event*, with all attempts timed, but platform UV attempt numbers cannot reliably be observed or forced to three. Do not claim literal identical A/B policies. |
| F2: new keys and attempt-bound signed statement | ACCEPT WITH PROVENANCE LIMIT | A successor needs a fresh primary/recovery probe keypair generated after its exclusive claim, distinct acceptance namespace/context and public-ID inequality. A local owner setup receipt substantiates ordering; SSHSIG alone does not cryptographically attest to key creation time. Public fingerprint deny-list comparisons can occur in private-local nonsecret evidence, avoiding unnecessary publication of personally linkable IDs to a public repository. |
| F3: three view tiers | ACCEPT | T1 semantic governing payload inside envelope_digest and shown_digest; T2 decision-relevant explanatory context in shown_digest only; T3 fixed non-governing procedural role/timer/browser guidance outside the signed view. No variable T2 added to the synthetic successor; future owner-view context remains a separate R1 requirement. |
| F4: mechanical sub-intervals | ACCEPT | Preserve original total decision-to-VERIFY interval and 60/120/120 gates, with monotonic diagnostic subintervals including preview, launch, unlock, verify. No subtraction of S02 or future unknown delays. Consultation before decision is part of ungated semantic review and must not coach the decision. |
| F5: stop rule | ACCEPT | Repeated complete attempts can be trial-level retry-to-green. Freeze a finite outcome/consequence table *before* future implementation. Preferred default: no automatic Attempt 003, even after AMEND; any later exceptionally authorized work needs a newly specified falsifiable hypothesis and governed owner authorization. |
| F6: browser opening, Ctrl+C, resume | QUALIFIED AMEND | Browser opening after localhost readiness may prevent copy interruption. SIGINT confirmation needs Windows/native-child tests and must not block the owner's unconditional abort. The frozen `Attempt.preserve()` wrote numbered exclusive JSON snapshots; there is **no hash-chained recovery journal** or durable cursor. Cross-process arm-boundary resume requires a newly designed and tested source-of-truth, in-flight ceremony handling, challenge expiry, exactly-once admission and hash-linked continuity. Simpler same-process breaks are preferred unless resume proves worthwhile. |
| F7: repeated participant | ACCEPT WITH DISCLOSURE | Experience with normal signing is representative of the same owner's steady-state usage, but not first-use generalization. A rare recovery credential has different long-term retention requirements. |
| F8: full successor and P03 | CONDITIONAL ACCEPT | Full independent A/B/C testing avoids cherry-picked P6/S02 grafts. P03 design may advance separately, but any change to Research 513's preferred *execution order* must be prospectively authorized before P03 results; a second scored probe or physical target selection is not started by this note. |
| F9: future UX and rare recovery | ACCEPT AS TRACKED REQUIREMENTS | Real governing decisions need purpose, provenance, history, options and consequences bound appropriately through shown_digest without silently extending envelope authority. Dormant recovery-key storage/drills are operational R1 requirements. Track here and in current state until the future R1 architecture records have a specific home. |
| F10: verifier known-answer preflight | ACCEPT | Before scoring owner records, test fixed synthetic known-good SSHSIG/WebAuthn proofs and known-bad mutations with the *same* execution profile. Inability to write transient **public** SSH verification files is an environment blocker, not a real signature failure. No owner private key access. |
| F11: SHA-256 mismatch | RESOLVED | Validation 216 is the new erratum; preserve earlier records unchanged. |

This is a disclosed, observation-informed **prospective probe-protocol correction**, not a claim that all modifications were identified before owner use. No credible evidence requires reopening owner-exclusive cryptography or GOVERNED_LEDGER_KERNEL_V02's current architecture family.

## 3. Proposed successor stopping/consequence policy, NOT YET FROZEN

| Successor result | Proposed required consequence |
|---|---|
| PASS_WITH_SELECTION | Qualification applies *only* to the new, fully frozen successor and selected arm; visibly retain Attempt 001 AMEND and the owner's practice/learning effect |
| AMEND with viable crypto but security/recovery/burden shortfall | Stop ordinary repeat attempts. Owner decides between a bounded trust-root/UX/batch amendment, deferral, or documented further architecture research. No automatic Attempt 003. |
| REOPEN | Reconsider load-bearing owner authenticity/recovery architecture, not just operator wording; no automatic rerun |
| INVALID due to substantiated harness or environment integrity defect | Preserve evidence and stop. Any exceptional new attempt must be separately owner-authorized with a distinct hypothesis, protocol identity, independent freeze and no partial graft |
| Incomplete owner-aborted run or NOT_REALIZABLE arm | Freeze exact mapping to existing primary result classes beforehand; no invented PASS, no replacing failed arm after outcome observation |

This is an engineering **proposal**, not owner assent or a live contract. The scorer's final result vocabulary, branch ordering, null/incomplete normalization, total permitted attempts and exception policy must be frozen prior to a successor launch. A natural default is at most one complete successor in this specific P01 follow-up family; future work after failure requires a separately justified governance record.

## 4. Constraints for the next non-executing exact design draft

1. New attempt identity, IDs/context within the *same* SignedAcceptanceStatement field set, own fixed golden hashes, durable start claim and separate immutable evidence; preserve old marker/raw-0000..raw-0024/backup/credentials exactly.
2. Fresh primary and recovery keypairs created solely by the human **after** the new claimed start. Check public-ID inequality against owner-local historic evidence; do not publish private paths or personally identifying keys by default. Probe-only keys, no auto agent, secrets never enter model/Codex/Claude/logs/arguments/environment.
3. Fix a narrow three-unlock SSH policy per unchanged proof event, with no new statement, changed acceptance ID or signature after terminal failure. Retry only a clearly classified recoverable unlock error; unexpected partial signature, key mismatch, invalid statement, IO defect or other failure ends the event. Account for every attempt in interactions and unrounded monotonic mechanical time. Record first-unlock success and non-secret failure category. WebAuthn platform attempts remain opaque.
4. Preserve all 13 controls including negatives/zero misses, A/B/C arms and C's nonselectability, 1/2/4/30 effect packet, 60-second median, 120-second max small, 120-second L01, zero manual metadata edits, secret boundary, original volume rule and A/B deterministic selection.
5. Freeze exact T3 guidance before any proof, role-specific PRIMARY and RECOVERY messages, owner decision versus timed proof boundary, localhost instructions and owner friction neutrality. Add no varying T2 effects in this mechanical benchmark. Do not shift preview outside its measured interval.
6. Add monotonic event landmarks within existing timing. Provide optional nonsecret `consulted_before_decision` observational field, not a gate. Running clocks need not be shown. Never apply a retrospective correction to S02.
7. Preclaim browser reachability only from a separate credential-free preview; prohibit WebAuthn credential/capability requests during preflight. Owner browser can open from the local harness after registered server readiness, with safe fallback.
8. Specify hard interrupt rules. Programmatic localhost launch is a modest simplification; Ctrl+C guard on Windows and especially cross-process resumption must demonstrate correctness in preregistered synthetic/no-secret tests. Consider **no cross-process resume** for initial successor rather than assume hashes/serial JSON snapshots suffice. Do not reissue begun owner events.
9. Scorer capability: valid and invalid synthetic signature known-answer tests in the exact verifier execution environment, clear environment-failure outcome prior to owner scoring.
10. Independent adversarial review, exact prospective contract/fixture freeze, then qualified implementation before asking the owner for a separate explicit authorization to start. No attempt, keygen, browser UV or signing is authorized now.

## 5. Eight questions from Claude: preliminary recommendations

- Unlock budget: favor 3 narrowly bounded SSH unlock chances within same event; **do not claim same platform-internal retry count**.
- Fresh keys: require new attempt-scoped keys; public-ID comparison remains owner-local unless disclosure authorized.
- Stopping rule: recommend §3, in particular no automatic Attempt 003; owner must approve it before live execution.
- Raw hash: Validation 216 resolves it, no manual user rehash needed.
- Arm C: retain S01/L01 comparator and explicit user-role provenance boundary.
- Arm breaks: support planned same-process pauses outside timed events if desired; cross-process resume needs substantive new design before promising it.
- P03: allow non-executing parallel design; a scored ordering change requires preregistered amendment.
- R1: record owner-view T2 purpose/history/provenance/consequence and rare-recovery-key durability as explicit future obligations, not validated production features.

**Next step:** Build the full prospective successor contract and stopping-policy **draft**, submit it for bounded independent adversarial qualification, then decide whether to freeze and implement it. This record does not freeze an experiment or authorize new owner operations. No owner action is needed merely to continue analysis.

R0-P02 PASS, R0-P03 pending; logical THIN_CENTRED_HYBRID_V03 selected; physical GOVERNED_LEDGER_KERNEL_V02 still only a candidate; Specification 028 authority and unrelated scientific experiment INCOMPLETE remain unchanged.

```text
RESEARCH_525=CLAUDE_TRIAGE_RECONCILED
R0_P01_ATTEMPT_001=AMEND_PRESERVED
SUCCESSOR_DESIGN=DRAFT_ONLY
SUCCESSOR_FREEZE=NOT_AUTHORIZED
OWNER_SENSITIVE_ACTION=NOT_AUTHORIZED
NEXT=PROSPECTIVE_SUCCESSOR_EXACT_CONTRACT_DRAFT
```
