# Validation 228: Message 057 source-site decision table provenance and reviewer case-text pin tests

**Date:** 2026-10-11
**Status:** STATIC_CASE_PROVENANCE_AND_DECISION_TABLE_PASS / SEMANTIC REVIEW OUTSTANDING
**Parent:** Research 539 / Checkpoint 875 / MC-0030 Message 058
**Scope:** Public synthetic regression of 15 candidate source/receipt site rows and immutable reviewed-case semantic pins, with no owner credential use.
**Authority:** Only synthetic source-identity and case-regression evidence, not real owner proof or F1/F2 signoff.

The candidate table includes 15 source/receipt site rows, required qualification flags Q1–Q7, all seven blocked-source cases and their exact frozen source-unit references. `scripts/check_r0_p01_f1_site_decisions.py` checks historical independently reviewed REV02 case text against Git commit `41e8b0c3af10f789a24e8c708a3a2ad11c990fee`, refusing silently inverted meaning even if corresponding local pin hashes are changed. It cannot make the unreviewed D01–D15 semantics correct.

12 new synthetic negative checks cover missing X1 or S3-03 review interpretation via hash mutation, dropping the client get() invocation prerequisite, an adversarial concurrent premise-and-hash change, dropping Q1 or the blocked-case set, false unconditional REOPEN, missing evidence fields, unknown source IDs, and premature F1/owner approval.

Observed new focused tests:
```text
tests/unit/test_r0_p01_f1_site_decisions.py
............                                                             [100%]
12 passed in 0.18s
```

The combined previous 72 tests and twelve new tests passed:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-875-all-regression tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 85%]
............                                                             [100%]
84 passed in 16.02s
```

Repository integrity/routing is validated separately before checkpoint publication. The present tests are not the 117 prospective F1 owner-authentication runtime tests and cannot establish scored event/attempt outcome correctness.

```text
VALIDATION_228=REVIEWED_TEXT_PINS_AND_SITE_ROSTER_PASS
F1_SEMANTIC_APPROVAL=NOT_GIVEN
ATTEMPT_002=NOT_AUTHORIZED
```
