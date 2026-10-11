# Validation 231: synthetic durable admission and restart/replay qualification

**Date:** 2026-10-11
**Status:** 15_SYNTHETIC_DURABILITY_TESTS_PASS / CROSS_RUN_NONCE_REQUIRED
**Scope:** Execute a bounded SQLite-backed synthetic trust-admission prototype across child-process restart, abrupt termination, concurrent writers and persisted public-signer rotation.
**Parent:** Research 543 / Checkpoint 879 / Validation 230.
**Authority:** Public non-owner keys and temporary SQLite files only; no real owner experiment, production datastore or frozen F1/F2 approval.

### Exact tested behaviors

New source: `experiments/r0_p01_successor_synthetic/durable_admission.py`. New tests: `tests/unit/test_r0_p01_durable_synthetic_admission.py`. Every successful or rejected persisted record is reverified using real historical Ed25519/ES256 proof verification and the historical Ledger trust/role rules. Initialization requires explicit `create=True`; reopen is fail-closed if no database exists. All state-changing admissions serialize with SQLite `BEGIN IMMEDIATE` and use a FULL synchronous transaction for accepted event, consumed ID and head hash. The tests assert precommit abrupt exit rollback, postcommit/pre-response durability, two competing subprocess outcomes, updated signer-set after process restart, reject-state invariance and corrupt/missing-file fail-closed behavior.

The final test deliberately confirms the historical V02 deficiency: since the owner's signed statement has no run nonce, independent trial databases cannot cryptographically distinguish the same old signed acceptance. This is **a reproduced open security requirement**, not a claim that a future fresh owner-authorized run is replay-protected.

Focused test command/result:

```text
python -B -m pytest -q -x -p no:cacheprovider --basetemp=.venv/.p01-879-durable-e tests/unit/test_r0_p01_durable_synthetic_admission.py
...............                                                          [100%]
15 passed in 5.85s
```

Combined historical-source and executable synthetic regressions:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-879-all-focused tests/unit/test_r0_p01_durable_synthetic_admission.py tests/unit/test_r0_p01_signed_unauthorized_admission.py tests/unit/test_r0_p01_cryptographic_sensitivity.py tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 57%]
......................................................                   [100%]
126 passed in 24.66s
```

**Composition:** 15 new executable crash/restart integration tests + 27 earlier actual synthetic crypto/admission tests + 84 audit/provenance structural regressions. No owner key, real trial marker, external network request or frozen successor implementation was used. SQLite hash-chain integrity does not imply trust against malicious whole-database rollback. Source/routing and repository-integrity postflight are required before checkpoint publication.

```text
VALIDATION_231=RESTART_CRASH_REPLAY_EXECUTABLE_TESTS_PASS
NEW_DURABLE_TESTS=15
TOTAL_FOCUSED_TESTS=126
CROSS_RUN_SIGNED_NONCE=REQUIRED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
