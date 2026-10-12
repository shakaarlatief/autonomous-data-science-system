# Validation 241: independent SSHSIG Ed25519 verification component

**Date:** 2026-10-12
**Parent:** Research 553 / Checkpoint 889
**Status:** 31_NEW_TESTS_PASS / 462_FOCUSED_PASS / PUBLIC_INTEGRITY_PENDING
**Scope:** Synthetic source-independent SSHSIG parsing, separately reconstructed signed-message verification and comparison against native Windows OpenSSH; legacy F1/security/structural regressions.
**Authority:** Bounded independent-verification candidate, not frozen F1/F2 or real owner proof.

Added:

```text
experiments/r0_p01_successor_synthetic/independent_sshsig_verify.mjs
tests/unit/test_r0_p01_independent_sshsig_verifier.py
```

The verifier has a `--verify-only` mode. Its own parser reconstructs the SSHSIG V1 fields and protocol-specific signed bytes before performing Ed25519 public-key verification with Node built-in crypto. It imports neither historical Python harness, signing worker, nor OpenSSH verification function. Tests use actual synthetic ephemeral signatures and explicitly compare verified outcomes to real Windows OpenSSH.

Initial **30/31** test result contained one expectation-shape defect: a correctly rejected mutated signature included evidence hashes in addition to reason/verdict. The test assertion was amended to check verdict, reason and expected digest. No verifier repair or post-observation security threshold tuning was needed.

Final focused groups (`python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-889-focused-N`):

| Group | Description | Result |
|---|---|---|
| 1 | 31 new independent SSHSIG + earlier native/source/F1 references | **199/199 PASS** |
| 2 | Existing cryptographic admission and run-bound regressions | **63/63 PASS** |
| 3 | Trusted claim store and governed evidence | **70/70 PASS** |
| 4 | Synthetic measurement and finalization | **46/46 PASS** |
| 5 | Structural/provenance and F1 source guards | **84/84 PASS** |
| **Total** | **378 executable + 84 structural** | **462/462 PASS** |

No owner key, passphrase, physical WebAuthn/Windows Hello authenticator, browser ceremony, live claim marker or Attempt 002 trial was accessed. No production target/semantic authority has changed. This is independent of the owner harness's OpenSSH verification path but is not a complete source-attested scorer or an independently authored blind oracle.

Public integrity and exact commit/remote postflight are separately evaluated before publication completion.

```text
VALIDATION_241=BOUNDED_INDEPENDENT_SSH_SIG_VERIFICATION_PASS
FOCUSED=462
INTEGRATED_F1_SCORER=NOT_QUALIFIED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
