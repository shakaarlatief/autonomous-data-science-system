# Validation 230: signed-but-unauthorized R0-P01 admission regression

**Date:** 2026-10-11
**Status:** SYNTHETIC_REAL_SIGNATURE_AND_AUTHORIZATION_NEGATIVE_TESTS_PASS
**Scope:** Verify actual synthetic Ed25519/ES256 signatures against historical trust-ledger admission rules; require all rejected decisions to leave admission-authoritative state unchanged.
**Parent:** Research 542; Checkpoint 878; Validation 229.
**Authority:** Public non-owner synthetic cryptography; no production attempt, owner SSH/WebAuthn credentials or policy change.

The new module `tests/unit/test_r0_p01_signed_unauthorized_admission.py` contains **19 tests**. Every negative trial verifies a valid cryptographic proof before exercising a separate denial condition: replayed acceptance ID, disallowed recovery/PRIMARY role, unregistered signer, outdated governed dependency, changed presented owner view, wrong event item and stale signer set. It also tests accepted recovery rotation, old-primary rejection after rotation, new-primary acceptance, and separate AMEND/REJECT admission without ACCEPT effects. The rejection helper compares deep snapshots of all mutable trust state, not only entry counts or the stated denial reason.

Test execution profile: allowed non-owner `inherit` workspace profile because Windows OpenSSH verifies against ephemeral **public** temporary files. Synthetic signer KeyObjects remain inside the Node child process. The runner neither reads owner secrets nor starts Attempt 002.

Observed focused run:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-878-admission-a tests/unit/test_r0_p01_signed_unauthorized_admission.py
...................                                                      [100%]
19 passed in 2.09s
```

Observed combined R0-P01 regression:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-878-admission-combined tests/unit/test_r0_p01_signed_unauthorized_admission.py tests/unit/test_r0_p01_cryptographic_sensitivity.py tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 64%]
.......................................                                  [100%]
111 passed in 19.00s
```

**Count distinction:** 19 new executable admission tests + 8 previous executable signature-sensitivity tests + 84 earlier source/guard regressions. The result does not mean 111 fully qualified successor security controls. It demonstrates specifically exercised historical V02 pathways. The new, approved owner-authorized replacement procedure is unaffected; an accidental retry is never a legitimate basis to replay a consumed same-trial governing acceptance.

Repository integrity and checkpoint/routing checks must pass before publication.

```text
VALIDATION_230=REAL_SYNTHETIC_ADMISSION_GUARD_PASS
NEW_ADMISSION_REGRESSIONS=19
ALL_FOCUSED_REGRESSIONS=111
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
