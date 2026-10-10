# Validation 221: R0-P01 Q0 REV02 source clause guard and F1 candidate table

**Date:** 2026-10-10
**Status:** STATIC CLAUSE INVENTORY AND GUARD TESTS PASS / SEMANTIC MAPPINGS NOT APPROVED
**Scope:** Verify structurally enumerated approved contract/policy units, review-pending mappings, test catalogue, frozen control bindings, source hash basis and data-only B01 decision predicate candidate.
**Parent:** Research 532 / Claude MC-0030 Message 029 / approved B01/B02 receipts
**Authority:** Static public-source and in-memory mutation tests only. No independent source semantics review, actual new scorer, P01 trial or F1/F2 freeze.

The locally admitted Runtime Bridge read the approved committed V03 REV04 contract and policy via Git blob bytes. The Python clause inventory recognized 166 contract clause/passage/table/fence units in sections 1–11 and 185 policy JSON leaves across named normative roots, exactly 351 units. Q0 REV02 contains 53 C/R requirements (13 C + 40 R) with 105 distinct planned test IDs, named test layer and oracle, and explicit source-review status. Twenty-two section-level weak associations are honestly recorded and **block** semantic F1 approval pending manual review.

The revised SHA-256 guard uses committed Git blob byte basis rather than a Windows checked-out file's potentially transformed CRLF bytes, and public known-answer SHA-256 of `abc`. It fails if an approved unit disappears or its source digest/location changes, a requirement is orphaned, a test is uncatalogued, a hard control position is changed, or the new F1/F2 statuses imply an unauthorized freeze.

Observed commands:

```text
python -B scripts/check_r0_p01_successor_trace.py
R0_P01_Q0_TRACE_GUARD=PASS requirements=53 controls=13 clauses=351 catalogued_tests=105 approved_sources=2 historical_artifacts=7
QUALIFICATION_SCOPE=STATIC_TRACEABILITY_ONLY_NOT_OWNER_EXECUTION

python -B -m pytest -q -p no:cacheprovider --basetemp=.tmp/p01-q0-rev02-20261010 tests/unit/test_r0_p01_successor_trace_guard.py
.................                                                        [100%]
17 passed in 1.37s
```

The proposed 288-row B01 predicate table has six per-arm feasible evidence/viability/eligibility triplets and all combinations with two fault flags and binary volume. Static structural checks assert 288 distinct rows and selected G1/G2/fault precedence outcomes; its class counts were INVALID 226, REOPEN 8, AMEND 43, PASS_WITH_SELECTION 11. **It is not F1-frozen**; there is no claim of independent full oracle validation or real 10/15-second arm-selection and B02 exception coverage.

Original V02 source hashes, approved B01/B02 exact proposal hashes and owner Attempt 001 evidence remain unchanged. F1 prospective fixture/oracle and F2 source/run freeze are still pending.

```text
VALIDATION_221=STRUCTURAL_Q0_REV02_PASS
MAPPING_SEMANTICS=NOT_REVIEWED
F1_ORACLE_COMPLETE=FALSE
F1_FROZEN=FALSE
F2_FROZEN=FALSE
ATTEMPT_002=NOT_AUTHORIZED
```
