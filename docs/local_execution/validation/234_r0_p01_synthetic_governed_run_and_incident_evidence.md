# Validation 234: synthetic governed run initiation and nonsecret interruption evidence

**Date:** 2026-10-11
**Status:** EXECUTABLE_SYNTHETIC_GOVERNED_EVIDENCE_PASS / NO_OWNER_TRIAL
**Scope:** Verify that synthetic run-specific procedural decisions and observed interruption/error/effort records are durably linked to cryptographically validated claim identity, without confusing the two kinds of authority.
**Parent:** Research 546 / Checkpoint 882 / Validation 233.
**Authority:** Public synthetic testing only, no live owner execution, hardware WebAuthn, F1/F2 qualification, or production authentication claim.

Changed source: `experiments/r0_p01_successor_synthetic/trusted_claim_store.py`, expanding the existing, replaceable synthetic store with a schema-v2 governed-issuance mode, transactional authorization association and durable nonsecret observations. New tests: `tests/unit/test_r0_p01_governed_run_evidence.py`.

A valid synthetic owner-controller record can issue a claim in governed mode; otherwise issuance fails without mutation. A new valid synthetic record can separately authorize replacement after a documented Ctrl+C accident. That original interruption remains observable with supplied elapsed time and interaction count, while the first genuine signature is rejected for the superseded run and the replacement requires its own cryptographic proof. The SQLite record is **not** evidence of actual real-owner identity and no test launches a real owner action.

Observed executable focused regression:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-882-executable tests/unit/test_r0_p01_governed_run_evidence.py tests/unit/test_r0_p01_trusted_claim_store.py tests/unit/test_r0_p01_run_bound_acceptance.py tests/unit/test_r0_p01_durable_synthetic_admission.py tests/unit/test_r0_p01_signed_unauthorized_admission.py tests/unit/test_r0_p01_cryptographic_sensitivity.py
........................................................................ [ 54%]
.............................................................            [100%]
133 passed in 17.94s
```

Existing source/contract and collaboration guards:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-882-structural tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 85%]
............                                                             [100%]
84 passed in 16.86s
```

Composition: **44 new synthetic governed-evidence cases**, 89 prior executable synthetic crypto/claim/durability tests, 84 structural guards. Total **217 passing focused tests**. The final schema-v2 change and repository-integrity checks must be verified in postflight before publication.

Known limits: synthetic permission field is trusted-controller test data and cannot prove human consent; observations are supplied measurements, not independently instrumented timing; keyword screening is not secret detection; no whole-database anti-rollback. Historical owner evidence, B01/B02 approval bytes, and real Attempt 001 remain untouched.

```text
VALIDATION_234=GOVERNED_SYNTHETIC_RUN_PERMISSION_AND_OBSERVATIONS_PASS
NEW_TEST_CASES=44
FOCUSED_REGRESSIONS=217
REAL_ATTEMPT=NOT_AUTHORIZED
```
