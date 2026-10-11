# Research 536: R0-P01 complete independent clause audit and gated prospective F1 reconciliation

**Date:** 2026-10-11
**Status:** 18/18 SOURCE UNITS REVIEWED BY CLAUDE; TASK-OWNER SEMANTIC RECONCILIATION OPEN; F1 NOT FROZEN
**Parent:** Research 535 / Validation 224 / Checkpoint 871 / MC-0030 Messages 043–051; older Messages 033, 035–042 and interim stop summary 052
**Scope:** Establish exact completion/provenance of the formerly bounded 1,022-unit independent source review; correct its stale 9-batch regression; preserve all 55 reviewer-pending findings; define substantive, prioritized F1 reconciliation obligations.
**Authority:** Public-source review and prospective specification analysis only. No inherited/approved source rewrite, Credential attempt, owner evidence read, experiment rerun, physical architecture selection or production authority switch.

## 1. Audit verified, but F1 still blocked

GitHub comparison from the preceding Checkpoint 871 HEAD `dbd333335e545a563f0311597fcf85b9413e793f` to the new Claude HEAD `bacabf65b317e459fadab7f4a7b07cad6b661320` showed **nine added messages only**, MC-0030 043–051 (Q0-AUDIT-010–018), with no source, test, governance, routing or historical evidence modifications. Guarded fast-forward pull synchronized the registered public workspace cleanly. Read-only Git log confirmed nine individually parent-linked commits.

The actual receipt checker independently counted **18/18 batches, 1,022/1,022 source units, 967 reviewer ACCEPTED and 55 reviewer PENDING**. The preceding first-nine-batch historical subtotal remains 472 units, 428 accepted and 44 pending. Batches 010–018 contributed 550, 539, 11 respectively. All 13 V01 security controls are represented at reviewer source level, and approved REV04 policy, original fixture and original result JSON units have now been audited.

**Critical distinction:** A reviewer ACCEPTED source mapping does not imply a completed synthetic security test, a qualified owner-run, a verified F1 scorer, or task-owner acceptance of its final interpretation. The 55 PENDING source units and independent reviewer recommendations require task-owner technical reconciliation. Neither exact reviewer coverage nor the source-index guard is sufficient for F1 freeze.

The derived `R0_P01_F1_PENDING_AUDIT_RECONCILIATION_REV01_UNFROZEN.json` preserves exactly 55 rows with original source-unit IDs, individual source text digests, reviewer message digests, requirement mappings, inherited dispositions, exact blocker strings and evidence bases. It is mechanically reproducible from every committed reviewer receipt through `scripts/check_r0_p01_pending_review_register.py`; all task-owner resolutions are `UNRESOLVED`. The 55 rows span V01_CONTROLS 10, V02_ADDENDUM 14, V01_CONTRACT 12, REV04_CONTRACT 8 and REV04_POLICY 11. Fixture and result JSON have zero PENDING reviewer leaves, **not** zero implementation/synthetic-test obligations.

There are 33 distinct blocker-field strings among those 55 source rows. Multiple strings refer to the same causal missing contract or test. They must be grouped carefully without losing exact per-unit resolution and without extrapolating an independent semantic signoff.

## 2. Highest priority: scoring-class and owner-exception-sensitive boundaries

**GATE S1: B05-A1, NOT_REALIZABLE.** Contract and policy both depend on a `frozen capability evidence` predicate without a complete admissible capability-test sequence, contemporaneous receipt schema, signer/source attestation, timing rule or negative case vocabulary. The WebAuthn NotSupportedError assertion-time branch is especially risky after successful credential registration. F1 must define a closed, independently verifiable `NOT_REALIZABLE` gate that cannot convert owner refusal, timeout, cancellation, incomplete setup or unavailable evidence into verified inability. It must preserve B01's exact G1 meaning; if the candidate interpretation changes that owner-approved gate, it is not automatically adoptable and requires governed reconciliation.

**GATE S2: B07-A3, SSH pre-sign check versus integrity.** REV04 §4.1 can stop a signing event at a failed pre-sign check, but §8.6 covers positively evidenced identity/key/header/agent changes as potential attempt-level `INVALID_INTEGRITY`; the policy's COMPLETED enumerated terminal outcomes lack a corresponding check-failure category. F1 must define a source-site-identified truth table separating actual identity substitution/invariant violation from absent tooling, no proof and normal event stop. It must say which evidence marks an arm COMPLETED or INCOMPLETE and maintain the B01/B02 no-exception integrity boundary. No generic mapping of all precheck exceptions to `INTEGRITY` or all to `INCOMPLETE` is admissible.

**GATE S3: B08-A1/B10-F1, Ctrl+C and Node RP failure.** The approved policy gives both a causal "unprovoked" and a temporal "before recorded abort" interpretation of node_rp_failure, plus a rebuttable "by default" owner Ctrl+C classification with no rebuttal evidence. F1 must specify event ordering, evidence and tie-breaking when two durable streams do not establish total order, and test simultaneous/ambiguous events. Misclassifying an owner abort as Node instrument failure changes B02 exception possibilities. The independent reviewer candidate "unorderable => INCOMPLETE" remains only a proposed decision, not silently accepted policy.

**GATE S4: B11-A1, SSH proof budget terminal vocabulary.** REV04 contract uses `PROOF_NOT_CREATED` for exhaustion, while its approved policy terminal outcome list uses `SSH_UNLOCK_BUDGET_EXHAUSTED`. F1 needs one frozen canonical event/result vocabulary and a documented bidirectional interpretation of the other term, preserving exact 3-invocation budget and source evidence. Otherwise a legitimate event-terminal Arm A proof failure might be scored INCOMPLETE solely due to representation mismatch.

These four gates must be resolved with explicit source references, evidence states, expected classification vectors, historical compatibility and independent negative checks before any F1 scoring oracle approval. Owner accepted B01/B02 cannot be rewritten silently.

## 3. Additional substantive qualification gates

**GATE T (security test sensitivity):** Fix the original C02 parser-only "forged" proof test by requiring structurally valid but cryptographically invalid signatures and an exact-statement non-owner signer negative. Make C09 a genuine semantic-base metamorphic test with unrelated input reaching the actual derivation boundary and a paired governing dependency mutation. Fix C07 class A to use a successor-valid acceptance ID so crypto rejection rather than format rejection is exercised. Add offline ACCEPT→AMEND C05, stale *genuinely signed* signer-set and semantic-base ADMIT negatives, and RECOVERY-key ordinary ACCEPT denial. Test outcomes must have expected rejection layers and genuinely independent expected values. The 13 control predicates and no-post-hoc-weakening rule remain governing.

**GATE F (fixture and owner ceremony exactness):** Enumerate successor acceptance IDs for A/B/C, complete the T3 instruction-byte table for every arm/role, select successor context/view/schema strings and rederive independent goldens. The original V02 frozen vectors are historical old-context checks, not copied as F1 target. Distinguish the fixture's grammar version `G1` from the scorer's G1/G2 validity/exception interpretation. Freeze Arm B P5 same-attempt Arm A PRIMARY+RECOVERY targets and B P6 same-attempt recovery dependency, without historical key fallback. Bind projected volume to the *selected* arm and exact `5400/97`-second median ceiling. The full result-contract eligibility predicate also needs L01 success, non-null measurements, friction-rating range and qualified infrastructure exception, not merely the abbreviated V01 JSON summary; viability, COMPLETED state, and full eligibility remain separate.

**GATE I (implementation/independence contract):** Resolve the old V01 "three files, Python standard library only, Node built-ins only" implementation boundaries against REV04's in-process independent SSHSIG/Ed25519 scorer and separate p01_spec/core/owner/rp/score roles. User-established project authority expressly permits redesign of *any* implementation layer; no existing V01 file count or language restriction should be silently assumed immutable when it prevents a stronger architecture. Nevertheless, prospective replacement rules, imports, per-role file read lists, runtime pins, native Windows/ConPTY qualification, separate RP and harness chains, and blind-oracle author isolation require explicit source-based review and F1/F2 scoping. Claude remains source auditor, not the second blind implementation/scorer author.

**GATE M (normative-source migration and reviewer dispositions):** Preserve original 18-batch evidence but prepare a successor trace that includes the six normative preamble lines (V01 controls 5/7/9 and V02 addendum 12/14/18), exact inherited additions/data-source hashes and reviewed distinction among original obligations, approved REV04 successor text and review-derived engineering requirements R34–R40. Current inherited-review disposition `INHERITED_UNCHANGED` is overloaded for REV04-approved successor leaves: future approved trace should distinguish these semantically rather than rewrite Claude's historical receipts. Resolve stale metadata such as B12-A1 `PROPOSED_RESEARCH_513_G1_G2_NOT_APPROVED` by separate provenance/derived policy view referencing owner B01 acceptance; do not alter the approved JSON bytes retroactively.

## 4. Execution order and next bounded task

The completed audit has earned a transition from **source collection** to **source-driven prospective F1 specification reconciliation**. There is no justification to ask the user to relay additional high-volume source-review prompts, and there is no need to rerun any of the 18 batches just because 55 rows are PENDING.

Next technical work should first author and independently challenge the cross-source scoring-boundary matrix for S1–S4, without selecting unapproved B01/B02 changes; then close security control-vector coverage (T), exact fixture/oracle data (F), independence and native implementation contract (I), and derived per-unit trace (M). This is a dependency order, not a fixed mandate for separate prompt rounds or a frozen architecture.

All unresolved findings must remain citable until each has an explicit source-compatible resolution and supporting expected tests. If ambiguity genuinely changes owner-approved eligibility, integrity, claim stopping or exception policy, request a *targeted separate owner interpretation* before freezing the conflicting semantics; never conflate that with real Attempt 002 execution authorization.

Original Attempt 001 stays immutable AMEND, B01/B02 accepted, P02 PASS, P03 pending, physical realization unselected, Specification 028 and project authority unchanged. F1 and F2 UNFROZEN. Third explicit owner execution authorization for Attempt 002 is still absent.

```text
RESEARCH_536=FULL_CLAUSE_REVIEW_QUALIFIED_AS_RECEIPTS
REVIEWER_BATCHES=18_OF_18
REVIEWER_SOURCE_UNITS=1022_OF_1022
REVIEWER_ACCEPTED=967
REVIEWER_PENDING=55
RECONCILIATION_PRIORITY=S1_S2_S3_S4_THEN_T_F_I_M
OWNER_POLICY_APPROVAL=NOT_INFERRED
F1=NOT_FROZEN
F2=NOT_FROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
