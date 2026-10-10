# Validation 222: R0-P01 inherited-source F1 audit structure and candidate oracle seeds

**Date:** 2026-10-10
**Status:** STRUCTURAL AUDIT READINESS PASS / SEMANTIC F1 APPROVAL NOT GIVEN
**Scope:** Check source-unit and test-catalogue identity, unchanged accepted contract hashes, inherited C01–C13 definitions, deterministic reviewer-batch partition, rational selected-arm volume and false-freeze safeguards.
**Parent:** Research 533 / Claude Message 031 / owner B01/B02 approvals
**Authority:** Read-only committed public-source and in-memory negative tests only; not an owner execution, new crypto oracle or F1/F2 freeze.

Recomputed from the seven committed source surfaces, not Windows working-tree CRLF normalization:

```text
SOURCE_UNITS=1022
REV04_CONTRACT_UNITS=156
REV04_POLICY_LEAVES=237
V02_ADDENDUM_UNITS=102
V01_SECURITY_CONTROL_UNITS=49
V01_IMPLEMENTATION_UNITS=165
V01_FIXTURE_LEAVES=254
V01_RESULT_LEAVES=59
REVIEW_BATCHES=18
TEST_IDS=117_PLANNED
ORACLE_SEEDS=7_SELECTION_VOLUME+12_ELIGIBILITY+12_B02=31
```

The old policy sources SHA-256 are unchanged: REV04 contract `9160a30c481c1c67c2ec857238f5a04b44f618b2ef589ef4f1c514eb3b3d6175`; B02 JSON `9b5bbc4d2c4802fc80b46bcaa3d003640c33e8e4784d39ef7995dbf193dff86c`. No historical frozen source was edited.

The candidate inventory includes explicit dispositions to be decided by an independent reviewer for inherited/superseded/not-applicable clauses, seven table header and separator exclusions each, 38 additional excluded nonblank lines flagged for explicit review, and 13 positional original security-control-definition anchors. All 1,022 source units still require substantive review.

Observed local guard output:

```text
R0_P01_F1_AUDIT_STRUCTURE=PASS units=1022 batches=18 planned_tests=117
F1_SEMANTIC_APPROVAL=NOT_GIVEN; F2=UNFROZEN; OWNER_ATTEMPT_002=NOT_AUTHORIZED
```

Observed isolated new suite:

```text
pytest -q -p no:cacheprovider --basetemp=.tmp/p01-f1-audit-869-20261010 tests/unit/test_r0_p01_f1_audit_rev03.py
............ [100%]
12 passed in 1.07s
```

A subsequent combined regression run covered the preceding Q0 REV02 guard suite plus this new audit suite:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.tmp/p01-f1-869-combined-20261010 tests/unit/test_r0_p01_successor_trace_guard.py tests/unit/test_r0_p01_f1_audit_rev03.py
.............................                                            [100%]
29 passed in 2.39s
```

This is static and fault-injection regression only, not 29 independently approved F1 expected-output tests.

The 12 tests include deletion of an inherited C unit, substitution of its control identity, deletion of a previously excluded policy root, fake source digest, fake reviewer approval, missing batch member, wrong Windows-native test layer, incorrect rational selected-arm projected minutes, false owner authorization, missing inherited disposition and table-syntax separation.

**Limits:** The separate older REV02 clause guard and 17 tests remain historical. None of the new 117 test IDs has executable expected-vector approval; no blind second implementation, independent SSHSIG scorer, native Windows/WebAuthn run, fixture freeze or complete B02 oracle exists. Review of all inherited and approved unit meanings, including excluded-line normative status, remains blocking.

```text
VALIDATION_222=STRUCTURAL_F1_AUDIT_GUARD_PASS
CLAUSE_SEMANTIC_AUDIT=NOT_PERFORMED
F1_FROZEN=FALSE
F2_FROZEN=FALSE
OWNER_ATTEMPT_002=NOT_AUTHORIZED
```
