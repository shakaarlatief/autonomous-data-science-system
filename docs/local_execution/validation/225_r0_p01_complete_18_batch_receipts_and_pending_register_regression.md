# Validation 225: Completed 18-batch R0-P01 reviewer receipts and exact pending index

**Date:** 2026-10-11
**Status:** SOURCE_COVERAGE_RECEIPT_PASS / 55 REVIEWER FINDINGS UNRESOLVED / NO F1 FREEZE
**Parent:** Research 536 / MC-0030 Messages 043–051 / Checkpoint 872
**Scope:** Verify published messages-only 9-commit continuation, exact historical and final audit counts, and source-byte reproducibility of a separate pending-reviewer-finding register.
**Authority:** Public read-only clause index, no real owner credentials or F1/F2 freeze.

Independent GitHub comparison `dbd333335e545a563f0311597fcf85b9413e793f..bacabf65b317e459fadab7f4a7b07cad6b661320` shows **nine added files**, MC-0030 Messages 043–051, with no changes to scripts, tests, routing, source contracts or historical evidence. Guarded fast-forward-only pull succeeded with a clean local tracked worktree and the same HEAD. Read-only `git log --reverse` confirms each commit directly parents the preceding one.

Read-only receipt validation:

```text
R0_P01_CLAUSE_AUDIT_RECEIPTS=PASS batches=18/18 units=1022/1022 accepted=967 pending=55
F1_SEMANTIC_APPROVAL=NOT_GIVEN; ATTEMPT_002=NOT_AUTHORIZED
```

Prior subtotal (first nine batches) is preserved at 472 reviewed / 428 reviewer accepted / 44 pending. Continuation total is 550 / 539 / 11. The fixture and result-contract leaves have zero reviewer PENDING, but this is **not** evidence that their successor implementation or goldens have passed.

The previous regression erroneously asserted the temporary 9/18 progress counts. The replacement test pins the final 18/18, 1022/1022 and 967/55 without claiming F1 qualification and preserves the 9-batch historical subtotal. It fails if the committed audit corpus changes without deliberate reconciliation.

The candidate pending-review register is derived exclusively from the 18 receipt messages and exact source-unit/digest identities, in per-unit form. Its SHA-256 at initial generation is `b4a596492d5e3e9e3a782e2b97f2072f3cf1def8b2374e46ed7bd8fb1f07e241`, with 55 unique pending units, 33 distinct blocker strings, source split V01_CONTROLS 10 / V02_ADDENDUM 14 / V01_CONTRACT 12 / REV04_CONTRACT 8 / REV04_POLICY 11. `scripts/check_r0_p01_pending_review_register.py` detects altered source/reviewer hashes, missing pending rows or falsely changed status and is read-only by default. All task-owner resolutions remain UNRESOLVED; no approved policy byte or reviewer message is edited.

Observed combined focused regression:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.tmp/p01-872-all-20261011 tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
...............................................                          [100%]
47 passed in 4.00s
```

Scope limits: The 47 tests establish source/audit/checker integrity and synthetic negative behavior. They do NOT implement all 117 planned F1 tests, validate real SSH/WebAuthn proof, adjudicate B01/B02 source semantics, or authorize a new physical architecture or real Attempt 002.

```text
VALIDATION_225=COMPLETE_REVIEWER_RECEIPT_REGRESSION_PASS
SOURCE_UNITS=1022
REVIEWER_PENDING=55
F1_F2=UNFROZEN
OWNER_ATTEMPT_002=NOT_AUTHORIZED
```
