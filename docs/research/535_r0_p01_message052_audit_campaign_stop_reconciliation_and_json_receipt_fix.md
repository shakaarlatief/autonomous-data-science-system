# Research 535: R0-P01 independent audit stopped correctly, JSON receipt parsing repaired, batches 010–018 next

**Date:** 2026-10-11
**Status:** RECEIPT_CHECKER_DEFECT_REPAIRED / CLAUSE_AUDIT_PARTIAL / F1 NOT APPROVED
**Parent:** Research 534 / Validation 223 / Checkpoint 870 / MC-0030 Messages 035–042, 052
**Scope:** Reconcile Claude's independently preserved 8 audit batches and stop summary, minimally repair public audit receipt validation for lowercase JSON-path unit IDs, and permit one continuation of the same audit-specific campaign at Batch 010.
**Authority:** Public-source read-only review coordination and public validator/unit-test changes only; no rewrite of prior reviewer messages or source normative contracts, no F1/F2 freeze, actual owner trial or physical architecture decision.

## 1. Independent publication and coverage

GitHub comparison from `7f056f0cd33d7232eac5646a7b870624c9e23b4b` to the coordination branch identified exactly **nine** added files, Messages 035–042 and 052, with no modifications outside the authorized Claude message directory. The guarded local fast-forward pull returned HEAD `dc96718bd8df53dd9f7e3d3e2d67aada82285a09`, clean worktree. Message 052 reports Batch 009's commit `dca325789db07d6899c3c921f2807e2c60c0d1ae`.

The receipt validator passes on this committed tree, reporting **9/18 reviewed batches, 472/1022 reviewed source units, 428 reviewer ACCEPTED and 44 PENDING**. The eight newly completed batches 002–009 account for 423 units (389 ACCEPTED, 34 PENDING). This is **not** 428 qualified security tests, 428 ChatGPT semantic approvals or F1 approval. The V01 controls, V02 addendum, V01 implementation contract and successor REV04 contract have full batch receipts. The 237 REV04 policy, 254 V01 fixture and 59 V01 result-contract JSON units (550 units, batches 010–018) remain unreviewed.

## 2. Validated stop condition and exact tooling remedy

The original `FUTURE_ROW = re.compile(r"^[A-Z0-9_:\-\[\]\.]+[|]")` rejected every JSON-path unit ID because those names contain lowercase characters, while `parse_receipt()` silently skipped unmatched lines. On the remaining JSON sources that would produce no rows and make valid audits impossible. The stop before Batch 010 was correct.

The bounded correction changes `FUTURE_ROW` to `^[A-Za-z0-9_:\-\[\]\.]+[|]` while preserving previously committed source unit identities and receipt semantics. It also makes a nonempty unrecognized line **fail closed** inside future (Batch 002 onward) delimited receipts, rather than silently dropping malformed unit IDs. The original Batch 001 human-readable legacy parser remains unchanged. The existing committed-batch test asserts the current 9/18, 472, 428 and 44 totals instead of stale 1/18 values.

Regression now covers complete SHA-bound assigned IDs for representative batches 010 (REV04_POLICY), 014 (V01_FIXTURE including indexed effects) and 018 (V01_RESULT), rejects an incomplete JSON receipt, and rejects unsupported nonempty receipt text. Those tests instantiate synthetic receipt files in isolated pytest directories without authoring auditor judgments or owner data. Combined old and new Q0 guard regression passes **42/42**, with no actual F1 source map approved.

## 3. Scoring-sensitive findings remain open

The full Message 052 prioritized register is the authoritative independent audit finding set for the first nine batches. In particular:

- **B05-A1:** An exact NOT_REALIZABLE capability predicate and contemporaneous evidence receipt are not frozen. Without one, G1 could conflate genuinely unavailable capability with unfinished Arm B, changing INVALID_INCOMPLETE versus REOPEN. Do not invent proof of NOT_REALIZABLE; F1 must specify a closed rule, with owner-governed reconciliation if it changes the approved interpretation.
- **B07-A3:** REV04 SSH pre-sign checks describe event-terminal outcomes, while the integrity table treats verified agent/key/header structural identity changes as attempt-level INVALID_INTEGRITY. Their distinction must be decided through an exact per-source evidence and flag decision table before freezing F1; do not unilaterally downgrade actual integrity breaches.
- **B08-A1:** Owner Ctrl+C and Node RP exit ordering ambiguities may affect INVALID_INSTRUMENT versus INVALID_INCOMPLETE and thus B02 exception rights. A prospective deterministic order/evidence rule, independently justified against frozen policy, is required before F1; Claude's proposed default INCOMPLETE is a candidate, not an approved policy amendment.

Other nontrivial gaps include synthetic ADMIT negatives for stale signed semantic base/signer set and ordinary RECOVERY-key acceptance denial; prospective exact successor IDs and T3 prompt table; cryptographic C02, non-tautological C09 and grammar-valid C07 vectors; incompatibilities between old V01 stdlib-only/three-file implementation bounds and the proposed in-process scorer. The inheritance inventory also needs three V01 control preamble units, three V02 preamble units, reviewed data-artifact coverage and a semantic disposition type for successor REV04 units. These concerns are deferred for independent reconciliation and F1 qualification, not silently resolved by this validator fix.

The approved B01/B02 stopping/classification policy, hard 13 controls and frozen Attempt 001 remain unchanged. Any discovered semantic conflict requiring owner interpretation must stop rather than be settled solely by agent speculation.

## 4. Continuation boundary

The previously authorized **audit-specific** one-prompt campaign in MC-0030 Message 034 remains governing. It already reserved Batch 010–018 reviewer filenames `043`–`051`, even though an optional early stop summary was committed as Message 052. Preserve these exact existing reservations and commit-history provenance; Message 052 remains an immutable interim stop summary, **not** an audit completion notice. This state does not change normal ChatGPT–Claude collaboration or authorize editing any script by Claude.

After the fix is committed and published, Claude may resume **Q0-AUDIT-010** with Message 043 and independently continue through Message 051 if safe. Claude must first fetch the repaired HEAD, re-verify all nine existing committed batch receipts, and then inspect every remaining JSON unit, including the policy metadata and trial-effect semantics. JSON leaves that share a golden-vector property may cite the same independently checked batch-level calculation but still need exact individual receipt IDs and independently reasoned semantic status. The final completion summary, if requested, will require a new later-numbered message authorized separately; do not overwrite historical Message 052.

Before F1: task owner must reconcile all reviewer findings, explicitly account for original/successor normative sources and excluded lines, independently qualify code/expected vectors and control-test sensitivity, and preserve the distinct future owner execution-approval gate.

```text
RESEARCH_535=CLAUDE_052_STOP_RECONCILED
BATCHES_RECEIPTED=9_OF_18
UNITS_REVIEWED=472_OF_1022
REVIEWER_ACCEPTED=428
REVIEWER_PENDING=44
JSON_ID_REGEX_FIXED=YES
BATCH010_TO_018=RESUME_ALLOWED_AFTER_PUBLICATION
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
