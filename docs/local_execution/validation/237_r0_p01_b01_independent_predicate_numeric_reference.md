# Validation 237: independent B01 derived predicate and numeric selection reference

**Date:** 2026-10-12
**Research:** Research 549
**Scope:** Test prospective accepted B01 expected classifications without importing the earlier 288-row candidate oracle or existing harness/scorer, with exact-rational numeric selection and projected-volume calculations.
**Status:** SOURCE_GROUNDED_BOUNDED_B01_REFERENCE_PASS / F1_NOT_FROZEN
**Parent:** Checkpoint 885 / Validation 236
**Authority:** Synthetic non-owner derived-predicate and numeric-only F1 preparation.

New modules:
- experiments/r0_p01_successor_synthetic/independent_b01_oracle.py
- tests/unit/test_r0_p01_f1_independent_b01_outcomes.py

The test-only evaluator independently encodes B01 precedence of source-validated integrity and instrument flags, the G1 incomplete-evidence guard, viability and eligibility, G2 uncontested selection disclosure, and explicit prospective numeric selection. It uses exact decimal/rational arithmetic at the approved 10-second small, 15-second large and B tie-break thresholds, with 97 projected acceptances, 90-minute duration ceiling, and 100-acceptance maximum. The tests use manually declared expected outputs, not generated expectations copied from the candidate.

The older 288-row draft was consumed **only for diagnostic comparison**: 286 rows match the applicable complete derived-predicate classification. Two rows, CASE-281 and CASE-282, remain underdetermined because both arms are eligible and their numeric winning arm is not included. This is not an independent full-score verification or proof that raw evidence interpretation is correct. All original drafts/approvals remain unchanged.

Observed new test result:

```text
python -B -m pytest -q -x -p no:cacheprovider --basetemp=.venv/.p01-885-oracle-b tests/unit/test_r0_p01_f1_independent_b01_outcomes.py
....................................................................     [100%]
68 passed in 0.09s
```

The first attempted combined prior-regression invocation timed out without providing a result and is not counted. Individual bounded reruns:

```text
--basetemp=.venv/.p01-885-atomic-measured
tests/unit/test_r0_p01_atomic_measurement_finalization.py
tests/unit/test_r0_p01_synthetic_measurement.py
46 passed in 6.64s

--basetemp=.venv/.p01-885-governed
tests/unit/test_r0_p01_governed_run_evidence.py
tests/unit/test_r0_p01_trusted_claim_store.py
70 passed in 7.90s

--basetemp=.venv/.p01-885-sig
tests/unit/test_r0_p01_run_bound_acceptance.py
tests/unit/test_r0_p01_durable_synthetic_admission.py
tests/unit/test_r0_p01_signed_unauthorized_admission.py
tests/unit/test_r0_p01_cryptographic_sensitivity.py
63 passed in 7.90s

--basetemp=.venv/.p01-885-structural
seven source/scorer/provenance guard modules
84 passed in 14.25s
```

**331 focused PASS** = 68 new test-only B01 derived-reference cases + 179 prior executable synthetic security/evidence cases + 84 existing structural/provenance checks. This is **not** full F1 oracle qualification. Current source/raw-receipt derivation, independently reviewed expected data, final Windows owner environment and F2 remain unqualified. Final governance checks required before checkpoint publication.

```text
VALIDATION_237=B01_PREDICATE_REFERENCE_PASS
NEW_TESTS=68
FOCUSED_TOTAL=331
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
