# Research 534: R0-P01 Batch 001 false-positive control findings and bounded one-prompt remaining audit

**Date:** 2026-10-10
**Scope:** Reconcile Claude MC-0030 Message 033, distinguish design assurance from historical Attempt 001 results, and replace *only this one audit's* manual per-batch prompt relay with an optional bounded autonomous reviewer workflow.
**Parent:** Checkpoint 869 / Research 533 / Validation 222 / MC-0030 Messages 032–033
**Status:** AMEND_AUDIT_BATCH001 ACCEPTED FOR TARGETED PROSPECTIVE DESIGN / REMAINING BATCH AUDIT PREPARATION
**Authority:** Read-only review and prospective audit planning only. No changing Attempt 001, approved B01/B02, frozen source, F1/F2, owner credentials, or project-wide collaboration policy.

## 1. Claude 033 independently received and inspected

GitHub showed exactly one new commit `f3a01208e64eeae4a79bba24bada72e8e789ce03` atop `fe240ba8c983589baefaf6c222176bf126facf36`, adding only MC-0030 Message 033. Guarded fast-forward pull succeeded and local tracked worktree was clean before reconciliation. The actual committed review includes a 49-row per-unit receipt, which we independently parsed against the SHA-bound batch plan. Exactly 49 distinct assigned V01 security-control IDs occur, with 39 `ACCEPTED` reviewer dispositions and 10 `PENDING` outcomes. This does **not** imply 39 currently qualified implementation tests or owner/task-owner final approval. Three V01 preamble lines 5/7/9 are normative and must become indexed units; lines 3/4 are metadata.

Independent read-only comparison confirmed these original V02 prescription and implementation facts:

- V02 addendum §8 P01-C06 row 2 specifies XOR of the **first raw proof byte**. Both a decoded SSHSIG blob and an ES256 DER signature may fail structural parsing on that change, allowing a false C02 PASS without exercising signature mathematics.
- V02 row 9 changes an in-memory `repository_note` separate from the inputs to ordinary verification; original harness also writes this to `obs['separate_metadata']`. This cannot establish that the semantic base would remain stable when a truly unrelated change appears in the semantic-base source context.
- V02 row 7 uses the old `R0-P01-<ARM>-SEC-...` replacement acceptance-ID grammar. The original harness uses the same old string. The successor must use its valid attempt-specific ID syntax before C07 class A can qualify a cryptographic rejection.

The above are **evidence of coverage defects in prescribed synthetic test constructions**, not retroactive authority to rescore or change Attempt 001. Future green status must be contingent on reaching the named verification layer.

## 2. Prospective design dispositions, not source edits

**A1 (C02) ACCEPT TARGETED STRENGTHENING:** Preserve the old first-byte corruption only as a STRUCTURAL negative. Add a syntactically valid mutation of the Ed25519 signature bytes within a structurally intact SSHSIG envelope; an independently constructed DER-valid, altered ES256 signature; and a distinct non-owner synthetic signer over the *same* exact statement. Require proof rejection at the correct CRYPTOGRAPHIC stage, and separate role/ADMIT denial where a cryptographically valid proof is signed by an unregistered identity. A parser-only rejection never satisfies the cryptographic-strengthening assertion.

**A2 (C09) ACCEPT TARGETED STRENGTHENING:** Replace the tautological no-op with a *metamorphic* test of the actual semantic-base derivation entrypoint. Change repository metadata in a fully supplied source-context input that otherwise preserves governing dependencies, recompute the semantic base through that same code path, and assert the digest and valid original proof are unchanged and fresh ADMIT succeeds. Include a paired governing-dependency perturbation demonstrating that the same entrypoint **does** change the digest when relevant state changes. Reviewers must check that the unrelated change truly reaches the derivation boundary rather than being prefiltered by the test harness.

**A3 (C07) ACCEPT:** Use a format-valid successor acceptance ID, preserving other fields and the old proof. Require rejection due to CRYPTOGRAPHIC statement mismatch for class A, separately ADMIT duplicate rejection for class B.

**A4 (C06) ACCEPT AS NON-GATING DIAGNOSTIC:** Preserve approved structural wrong-project rejection as gating, and additionally exercise signature verification of the mutated project-bound statement. Do not silently change the original C06 pass rule.

**A5 (splits) ACCEPT:** Model C11's four, C12's five, and C13's two independently testable assertions under preserved source-unit provenance. Do not incorrectly count grammatical split count as a new security control.

**A6 (missing rule text) ACCEPT:** Add checkable prospectively inherited rules prohibiting production trust-root/recovery changes and result-informed weakening/renaming/omission of any C01–C13 predicate. Bind approval of any strengthening by source-based, human-visible change ledger, not an automatic assumption that stricter means compatible.

**A7 (preamble) ACCEPT:** Propose three newly indexed units for V01 control scope, public predicate vocabulary and PASS/FAIL domain; account for metadata lines without silent omission. Since the committed REV03 inventory hash and batch IDs already bind to the old index, add a new successor audit-index revision **after** independent findings are collected, preserving old batch source identity as reviewed historical evidence rather than silently overwriting it.

**A8 (B P5 dependency) ACCEPT:** Add a citable prospective fixture rule tying B rotation V2 PRIMARY/RECOVERY to same-attempt Arm A public keys and `FAIL / UNEXECUTED_ROTATION_TARGET_ABSENT` when unavailable. Derive exact basis from frozen V02 addendum §9; do not invent old-key fallback. This is a fixture clarification, not a B01/B02 amendment.

**A9 (ordinary RECOVERY role) ACCEPT AS MISSING NEGATIVE:** Add independently checked ADMIT denial `CURRENT_ROLE_DENIED` for a mathematically valid recovery-credential signature over an ordinary acceptance statement. The reviewer of inherited AC-6 shall identify the exact source identity and result semantics.

**C05 AMEND-substitution ambiguity:** Include both ACCEPT→REJECT and ACCEPT→AMEND offline signed-statement substitution negatives unless subsequent source analysis proves a conflict. No additional real owner proof may be requested. Keep reviewer disposition pending until exact vectors exist.

Ten pending Batch 001 units remain pending; 39 accepted are *reviewer* decisions, not task-owner blanket approval. Repair and later verification evidence must link to source-unit IDs and expected vectors, never auto-close these pending dispositions.

## 3. Why continue auditing, and why not 17 user prompts?

Batch 001 exposed test vectors that can produce **false positive security-control results**. That is a strong justification to investigate the remaining inherited implementation rules and result contracts. A one-off, *audit-specific* autonomous Claude instruction is proportionate to this task: Claude can review the 17 remaining bounded batches while preserving each batch's exact result as a distinct committed MC-0030 message, without user relay between ordinary batches.

This is not a general inter-agent control-plane redesign or a permanent change to MC-0030 collaboration methods. The user explicitly permits normal manual ChatGPT–Claude prompting and only wishes to avoid 17 manual relays for this unusually broad audit. The 18-batch count is an engineering decomposition, not a frozen assurance axiom: Claude must surface a well-supported alternative or unexpectedly redundant non-normative material as a **scope reconsideration proposal**, not unilaterally skip units or claim completed coverage.

**Failure policy:** Continue past bounded and recorded `PENDING` findings that can be assessed later, including A1–A9. Halt on source-hash/authority mismatches, inability to substantively examine a source, actual normative contradiction requiring an owner interpretation, uncertainty about secret exposure, inability to write/verify durable per-unit receipts or commit through approved Git authority, or resource/context limits. A batch with honest PENDING findings may be durably complete as a review without being semantically accepted for F1. Unfinished batches must not be mislabelled completed.

**Output:** Exact per-unit reviewed disposition, normative meaning and C/R mappings, source basis, test sufficiency and blockers in each SHA-bound batch. For batches 002–018, files **035 through 051** are reserved as separate audit messages, with **052** as optional aggregate/stop summary. A read-only checker verifies contiguous batch receipt names, IDs, completeness and state flags. Passing its static syntax checker does not establish substantive correctness; ChatGPT must independently reconcile the full evidence before mapping approval.

**Independence:** Claude remains clause reviewer only. A different blind actor will eventually author the second golden implementation and scorer, with no exposure to primary code/expected outputs prior to the relevant recorded attestation. Do not create implementation or F1/F2 freezes inside this audit. All human owner controls remain outside agent approval.

## 4. Next boundary

Research 534 / Validation 223 / Checkpoint 870 / MC-0030 Message 034 authorize only the scoped remaining audit effort. The user can deliver Message 034 to Claude **once**. If Claude cannot complete the entire campaign within one run, retained verified batch commits allow resumption without repeating completed work; no automatic promise of background work is implied.

```text
MESSAGE033_VERDICT=AMEND_AUDIT_BATCH001
BATCH001=49_REVIEWED_39_ACCEPTED_10_PENDING
C02_C09_C07_TEST_SENSITIVITY_DEFECTS=REQUIRES_PROSPECTIVE_FIX
BATCH002_TO_018=ONE_PROMPT_BOUNDED_CLAUDE_CAMPAIGN_PROPOSED
GENERAL_CLAUDE_COLLABORATION_WORKFLOW=UNCHANGED
F1=NOT_FROZEN
F2=NOT_FROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
