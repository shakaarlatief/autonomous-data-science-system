# Validation 235: real synthetic operation timing and evidence-aware admission assessment

**Date:** 2026-10-12
**Status:** EXECUTABLE_SYNTHETIC_TIMING_AND_EVIDENCE_CHECKS_PASS / HUMAN_BURDEN_UNQUALIFIED
**Research:** Research 547
**Scope:** Actual non-owner synthetic signer/admission timing and verified descriptive outcome evidence.
**Parent:** Research 547 / Checkpoint 883 / Validation 234.
**Authority:** Non-owner synthetic run, actual OpenSSH Ed25519 and Node synthetic P-256 verification, no real trial or owner keys.

New code: `experiments/r0_p01_successor_synthetic/synthetic_measurement.py`. New tests: `tests/unit/test_r0_p01_synthetic_measurement.py`. No changes to original V02 harness, real owner records, approved B01/B02 files or existing synthetic claim journal implementation.

The script performs a genuine monotonic `perf_counter_ns` measurement from immediately before a synthetic signer call through tested trusted-admission verification, and stores the elapsed milliseconds plus actual **scripted call count** in the existing governed journal. Independent expected test outcomes verify honest reporting for valid admission, signed invalid statement and interruption. A delayed synthetic signer confirms observed latency increases. An `INTERRUPTED` case calls no signer. An accident followed by authorized synthetic replacement keeps both entries, preserves the first event's observations and never reuses the old signature.

The evidence assessment uses the existing verified durable journal, not an assertion such as `COMPLETED`, to determine cryptographic admission. It explicitly marks missing observation coverage if a signature has committed without timing evidence. A separate Python process independently replays committed proof verification for the same report. The postadmission/preobservation crash gap is intentionally **not** claimed repaired.

Observed focused executable run:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-883-exec tests/unit/test_r0_p01_synthetic_measurement.py tests/unit/test_r0_p01_governed_run_evidence.py tests/unit/test_r0_p01_trusted_claim_store.py tests/unit/test_r0_p01_run_bound_acceptance.py tests/unit/test_r0_p01_durable_synthetic_admission.py tests/unit/test_r0_p01_signed_unauthorized_admission.py tests/unit/test_r0_p01_cryptographic_sensitivity.py
........................................................................ [ 45%]
........................................................................ [ 91%]
.............                                                            [100%]
157 passed in 20.85s
```

Existing structural/provenance and collaboration regressions:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-883-structural tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 85%]
............                                                             [100%]
84 passed in 16.93s
```

Together: **24 new runnable tests**, 157 execution-facing synthetic tests, 84 structural guards, **241 focused passing checks**. These totals do not include real human operation, a hardware authenticator, an independently frozen F1 scorer or real Attempt 002 execution. Repository integrity/routing postflight must pass before publication.

```text
VALIDATION_235=REAL_SYNTHETIC_MONOTONIC_MEASUREMENT_PASS
NEW_TESTS=24
FOCUSED_TESTS=241
POSTADMISSION_MEASUREMENT_GAP=DISCLOSED_UNRESOLVED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
