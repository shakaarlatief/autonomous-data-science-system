# Validation 233: durable issuer and accepted signed-run claim integration

**Date:** 2026-10-11
**Status:** 26_SYNTHETIC_TRUSTED_ISSUER_ADMISSION_TESTS_PASS
**Scope:** Test cryptographically run-bound claim issuance, supersession, authorization, admission and restart recovery in a replaceable SQLite synthetic prototype.
**Parent:** Research 545 / Checkpoint 881 / Validation 232.
**Authority:** Synthetic public-material security tests only. No owner credentials, production ADS acceptance or authorization of Attempt 002.

The new `experiments/r0_p01_successor_synthetic/trusted_claim_store.py` integrates the signed `claim_nonce` from Checkpoint 880 into atomic durable issuance and one-time admission. `tests/unit/test_r0_p01_trusted_claim_store.py` runs **26 actual synthetic integration regressions**, parametrized over Windows OpenSSH SSHSIG Ed25519 and Node WebAuthn-shaped ES256. Keys remain ephemeral in the Node synthetic signer process; the journal stores only public credential identities, signed statement/proof bytes and SHA-256 metadata. Testing is performed in the authorized non-owner workspace execution profile.

A denied action does not alter the database. Child-process tests demonstrate precommit rollback, postcommit recovery without an acknowledgment, dual-writer concurrent issuance and admission, actual signer mismatch, wrong-run replay denial, wrong signed semantic context, lost database and altered persisted evidence. Ordinary reopening never creates an empty new store or silently forgets consumed claim IDs.

### Exact observed tests

```text
python -B -m pytest -q -x -p no:cacheprovider --basetemp=.venv/.p01-881-claim-b tests/unit/test_r0_p01_trusted_claim_store.py
..........................                                               [100%]
26 passed in 7.60s
```

All non-owner executable suites, including the new one, were rerun together:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-881-executable tests/unit/test_r0_p01_trusted_claim_store.py tests/unit/test_r0_p01_run_bound_acceptance.py tests/unit/test_r0_p01_durable_synthetic_admission.py tests/unit/test_r0_p01_signed_unauthorized_admission.py tests/unit/test_r0_p01_cryptographic_sensitivity.py
........................................................................ [ 80%]
.................                                                        [100%]
89 passed in 18.32s
```

Prior audit/scoring-source regressions independently rerun:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-881-structural tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 85%]
............                                                             [100%]
84 passed in 17.22s
```

**Totals: 89 executable synthetic security tests + 84 structural/audit guards = 173 passing focused tests**. None represents a real owner-proof ceremony or an approved complete successor. The historic V02, approved B01/B02 policy bytes and Attempt 001 remain unchanged.

A malicious whole-file rollback or deletion, durable owner-specific issuance consent, Windows Hello device verification, full scorer, realistic owner burden and safety qualification remain outstanding. Repository integrity and routing postflight must pass separately before publication.

```text
VALIDATION_233=DURABLE_TRUSTED_NONCE_ISSUANCE_AND_ADMISSION_SYNTHETIC_PASS
NEW_SYNTHETIC_TESTS=26
FOCUSED_TESTS=173
OWNER_CREDENTIAL_USE=NONE
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
