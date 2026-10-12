# Validation 236: atomic synthetic accepted signature and timing receipt

**Date:** 2026-10-12
**Research:** Research 548
**Scope:** Actual synthetic precommit/postcommit process crash tests for a single transaction containing verified signature admission and monotonic technical-operation measurement.
**Parent:** Checkpoint 884 / Validation 235.
**Status:** 22_NEW_ATOMIC_SYNTHETIC_TESTS_PASS / FULL_HUMAN_EXPERIMENT_UNQUALIFIED
**Authority:** Non-owner synthetic Ed25519 and ES256 cryptographic operations only.

Changed `experiments/r0_p01_successor_synthetic/trusted_claim_store.py` to accept optional `measurement_started_ns` for an atomic measured-admission path, without altering SQLite schema version 2 or the prior unmeasured admission API. Changed `synthetic_measurement.py` to use that path on successful synthetic signing and avoid a second completion-observation transaction. Added `tests/unit/test_r0_p01_atomic_measurement_finalization.py` with 22 tests across the two cryptographic mechanisms, including genuinely separate child processes exiting abruptly before and after commit.

The measured path computes a monotonic elapsed interval from just before the scripted signature request to just **before** the commit, then commits admitted proof and `COMPLETED` observation together. The duration excludes the SQLite commit/fsync, human time, actual Windows Hello and real owner credentials. Bad proof, invalid timestamps or missing authorization reject without state change; reopening after postcommit crash returns both proof and observation. Legacy unmeasured acceptance is still explicitly reported as incomplete observation coverage.

Observed standalone new module:

```text
python -B -m pytest -q -x -p no:cacheprovider --basetemp=.venv/.p01-884-atomic-a tests/unit/test_r0_p01_atomic_measurement_finalization.py
......................                                                   [100%]
22 passed in 3.77s
```

Observed re-executed focused groups (the first larger combined command timed out in the bridge and was not counted):

```text
--basetemp=.venv/.p01-884-core-a
tests/unit/test_r0_p01_atomic_measurement_finalization.py
tests/unit/test_r0_p01_synthetic_measurement.py
tests/unit/test_r0_p01_governed_run_evidence.py
tests/unit/test_r0_p01_trusted_claim_store.py
116 passed in 16.88s

--basetemp=.venv/.p01-884-core-b
tests/unit/test_r0_p01_run_bound_acceptance.py
tests/unit/test_r0_p01_durable_synthetic_admission.py
tests/unit/test_r0_p01_signed_unauthorized_admission.py
tests/unit/test_r0_p01_cryptographic_sensitivity.py
63 passed in 10.24s

--basetemp=.venv/.p01-884-structural
tests/unit/test_r0_p01_f1_site_decisions.py
tests/unit/test_r0_p01_scoring_boundary_rev02.py
tests/unit/test_r0_p01_pending_review_register.py
tests/unit/test_r0_p01_scoring_boundary_candidates.py
tests/unit/test_r0_p01_clause_audit_receipts.py
tests/unit/test_r0_p01_f1_audit_rev03.py
tests/unit/test_r0_p01_successor_trace_guard.py
84 passed in 17.28s
```

**263 focused PASS**: 179 genuine execution-facing synthetic crypto/issuance/admission/measurement tests, plus 84 historical structural/provenance tests. No human experiment, actual owner passphrase/Hello, or full successor-scoring qualification. Repository integrity and routing validations must pass separately before publication.

```text
VALIDATION_236=SYNTHETIC_ACCEPTANCE_AND_MEASUREMENT_ATOMIC_PASS
NEW_TESTS=22
FOCUSED_TOTAL=263
REAL_ATTEMPT_002=NOT_AUTHORIZED
```
