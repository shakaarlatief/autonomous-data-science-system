# Validation 271: External V0.4 method review preservation and V0.5 stage-precedence regression checks

**Date:** 2026-10-28
**Status:** SOURCE_FREE_EXTERNAL_REPORT_PRESERVED / V05_STATIC_METHOD_GUARDS_PASS / V05_INDEPENDENT_REVIEW_PENDING / REAL_SOURCE_HOLD
**Scope:** Verify provenance-bound preservation of one owner-supplied separate-session V0.4 critique, exact prior V0.4 immutable identity, bounded V0.5 textual repair of the two reported material decision-stage ambiguities, and continued source/gold/scoring holds.
**Authority:** Local deterministic text and evidence-integrity checks. They cannot verify actual LLM review provenance, semantic correctness of future source decisions, independent actor identities, private historical evidence custody, author visibility, or external acceptance of V0.5.

## 1. Exact input and evidence identities

```text
V04_SOURCE_BYTES=23276
V04_SOURCE_SHA256=b9945bd4fb36a7da1b4573b3ccc8c54cc92add02b1c4d0c412ffdbafd108f39d
V04_EXTERNAL_REVIEW_BRIEF_BYTES=7594
V04_EXTERNAL_REVIEW_BRIEF_SHA256=cbef6723ea6df7c8449e6f187de7dafc43f591f3c3d5eb301110474174696c10
OWNER_UPLOADED_FULL_REPORT_BYTES=49518
OWNER_UPLOADED_FULL_REPORT_SHA256=2c405b630e0b8e7141ecd585e3ca8b06eb9292f8fddf6e88fa62cdacc90fa7da
REPOSITORY_LF_REPORT_BYTES=48885
REPOSITORY_LF_REPORT_SHA256=449e411a1c55e3ba7b6dc62f414a7f98579f29eb451f6bdade06e7ee11e461bf
RAW_TO_REPO_NORMALIZATION=CRLF_TO_LF_ONLY
RAW_REPORT_TERMINAL_NEWLINE=ABSENT
REPORT_PHYSICAL_LINES=634
```

A full reviewer-authored text copy is retained at `experiments/r0_p03_navigation_probe/reviewer_intake_evidence/20261028_v04_independent_method_review_report.txt`, and Research 605 records the original-upload and normalized-copy digests. This is **user-relayed** external-session content; neither the self-reported tool access nor claimed lack of prior exposure has been independently audited.

## 2. Contract transition and material correction scope

The reviewer submitted `AMEND_MATERIAL_CONTRADICTION`, reporting 18 source-free fictional adversarial probes and two material ambiguities: M1, prechallenge conditional source bundle context erroneously requiring prior independent acceptance; and M2, substantive negative-search coverage potentially mislabeled semantic HOLD solely because the challenger has not acted.

The coordinator checked the relevant exact original V0.4 wording in Sections 1/3/5/7/9 and authored a separate prospective V0.5. V0.4 was **not edited**.

V0.5 corrects the independent-challenge precedence at the positive-context and negative-coverage interfaces. It requires adequately delivered/inspected context, exact membership, substantive evidence and witnessed negative-search materiality before candidate proposal, but reserves independent acceptance, atomic author disclosure and world freeze for later qualified stages. Any genuine missing/prohibited material, incomplete inspection or unresolved material coverage gap continues to impose scoped semantic HOLD/veto and/or packet/world release HOLD.

The new `CONDITIONALLY_CLOSED` dependency state is **not** a seventh content disposition, acceptance outcome or permission to release. All original release/author-world requirements remain.

## 3. Executed static regression validation

```text
Focused test module:
  tests/unit/test_r0_p03_v05_method_precedence_contract.py

Initial focused attempt:
  14 passed, 1 failed
  Cause: test asserted an obsolete paraphrase in Section 10's proposed follow-up.
  Repair: changed that test to match the authored exact text,
          "test exactly two invented situations".
  No method/source semantics were changed for this test correction.

Corrected command:
  .venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_v05_method_20261028b
  tests/unit/test_r0_p03_v05_method_precedence_contract.py

Corrected result:
  15 passed in 0.07s
```

The tests verify unchanged source V0.4 SHA-256/length, normalized complete reviewer copy and hashes, exact unaccepted V0.5 status, context-bundle proposal/acceptance separation, missing-context substantive veto, negative-search evidence versus challenge precedence, preservation of **all six** original dispositions, and unchanged challenge/release, original Checkpoint 898, Specification 028, gold and B0–B4 hold markers.

**Limitation of method:** These are structural and textual regression guards, **not** automated semantic proof. They do not themselves reproduce an external review of V0.5, certify model behavior, or determine whether an actual historical claim can safely enter an author packet. An independently scoped direct M1/M2 follow-up, if necessary, must be explicitly recorded as a new event.

## 4. Release and role qualifications unchanged

```text
VALIDATION_271=SOURCE_FREE_METHOD_TEXT_AND_EVIDENCE_REGRESSIONS_PASS
FOCUSED_REGRESSION_TESTS=15_PASS
EXTERNAL_V04_CRITIQUE=RECEIVED_AMEND_MATERIAL_CONTRADICTION
V05_STAGE_PRECEDENCE=COORDINATOR_REPAIRED_NOT_INDEPENDENTLY_ACCEPTED
REAL_NON_ARM_REVIEWER_AND_CHALLENGER=NOT_ADMITTED
REAL_HISTORICAL_SOURCE_RECORDS_READ=ZERO
SOURCE_ADMISSIONS=ZERO
AUTHOR_WORLD=UNFROZEN
HIDDEN_REFERENCE_GOLD=NONE
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
