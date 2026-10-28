# Validation 272: Source-free V0.5 M1/M2 check and S1 A2 actor-gate preflight

**Date:** 2026-10-28
**Status:** SOURCE_FREE_FINGERPRINT_AND_SCOPE_PASS / PRIOR_V05_STATIC_REGRESSIONS_PASS / NO_EXTERNAL_V05_CRITIQUE_OR_REAL_ACTOR_TEST
**Scope:** Preflight two independent, forward-looking candidate documents introduced in Research 606. Verify immutable reviewed V0.5 identity, exact attachment byte contracts, evidence-status controls, and preservation of all downstream scientific holds.
**Authority:** File and textual-invariant validation only. No external review, actual actor admission, OS/provider isolation, real source delivery, restricted report or author-view access-denial test was performed.

## 1. Exact source-free input fingerprints

```text
V05_METHOD:
  experiments/r0_p03_navigation_probe/NON_ARM_SOURCE_STATUS_REVIEWER_CONTRACT_CANDIDATE_V05.md
  BYTES=28270
  SHA256=1c787fe7daa1222b2923c06891b4db72717a0d9c32126ebaac846d31c27ae79a

FOCUSED_EXTERNAL_BRIEF:
  experiments/r0_p03_navigation_probe/NON_ARM_SOURCE_STATUS_V05_M1_M2_FOCUSED_INDEPENDENT_CHECK_V01.md
  BYTES=5676
  SHA256=1bdccf3510e5df9b4953386246884ecea1b9472866d5fea1ff0dbb22fc74b284

S1_A2_ACTOR_GATE_CANDIDATE:
  experiments/r0_p03_navigation_probe/S1_REVIEWER_CHALLENGER_ACTOR_ADMISSION_GATE_CANDIDATE_V01.md
  BYTES=10744
  SHA256=c09064c153cda896d752d0c1ade6c65fefc02e6b11674311cf43dc569ad596e7
```

All three source-free files were read as UTF-8, had LF-only/newline-terminated content, and contained no temporary authoring placeholder. The focused brief names the exact V0.5 hash, requires real input/tool disclosures, tests repaired M1/M2 with disqualifying cases and forbids real-source inspection. The S1 A2 candidate carries eight observable real-route admission gates (A2-R01 to A2-R08), distinguishing NOT_TESTED, EVIDENCE_PENDING, REPORTED_ONLY, VERIFIED_BOUNDED and FAILED_OR_HOLD, and retaining fail-closed real source HOLD.

## 2. Bounded checks actually executed

First fingerprint/scoping check produced the correct three SHA-256s, but its final textual assertion mistakenly expected the marker `SPECIFICATION_028_UNCHANGED` instead of the published marker `SPECIFICATION_028=UNCHANGED`. The checker assertion was corrected on the next run. **Neither source document changed** for that failure.

Corrected source-free preflight:

```text
SOURCE_FREE_SCOPE_AND_GATE_STATUS=PASS
```

Regression suite, unchanged from Validation 271:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_a2_reconnect_20261028
  tests/unit/test_r0_p03_v05_method_precedence_contract.py

15 passed in 0.05s
```

The test suite is a document-level guard for V0.5 stage precedence; it does **not** evaluate the new actor gate's correctness or simulate an independently qualified reviewer. The source-free preflight checks are not a replacement for session-side evidence collection and separate owner decision.

## 3. Status/independence holds

```text
VALIDATION_272=SOURCE_FREE_PREPARATION_PASS
V05_INDEPENDENT_FOCUSED_CHECK=NOT_RECEIVED
A2_REAL_REVIEWER=NOT_ADMITTED
A2_REAL_CHALLENGER=NOT_ADMITTED
A2_ACTOR_CAPABILITY_PROBES=NOT_EXECUTED
A2_REAL_SOURCE_INTAKE_AND_RENDER=NOT_TESTED
A2_PRIVATE_REVIEW_CUSTODY=NOT_QUALIFIED
A2_FUTURE_AUTHOR_VIEW_DENIAL=NOT_TESTED
S1_A1_FICTIONAL_CMS=OWNER_REPORTED_PASS
S2_REAL_SOURCE_ADJUDICATION=NOT_STARTED
S3_AUTHOR_WORLD=UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
