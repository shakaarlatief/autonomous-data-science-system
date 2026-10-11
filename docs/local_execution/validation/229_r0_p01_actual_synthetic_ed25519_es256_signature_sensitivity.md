# Validation 229: actual synthetic SSH Ed25519 and WebAuthn ES256 negative-test sensitivity

**Date:** 2026-10-11
**Status:** EIGHT_EXECUTION_FACING_SYNTHETIC_TESTS_PASS / NOT AN OWNER EXPERIMENT
**Scope:** Real non-owner synthetic signature generation, actual Ed25519/OpenSSH and ES256/Node verification, and source-input metamorphic checks against original V02.
**Parent:** Research 541 / Checkpoint 877 / owner replacement policy Research 540.
**Authority:** Public engineering validation only. No live owner credentials, WebAuthn platform ceremony, real attempt marker, P01 successor freeze or B01/B02 change.

New test file: `tests/unit/test_r0_p01_cryptographic_sensitivity.py` (eight executable integration/security checks). Keys are ephemeral synthetic in-memory Node KeyObjects labelled `SYNTHETIC-NON-OWNER-`; only public credentials and signatures are returned to Python. The existing original verifier uses temporary public-material files and actual Windows OpenSSH `ssh-keygen -Y verify`, while WebAuthn ES256 uses the existing Node verifier. No owner profile/key file is consulted. The original historical harness, contracts, frozen fixture and Attempt 001 evidence are never edited.

Environment observed: Node `v24.19.0`, Windows OpenSSH `ssh-keygen` located at `C:\WINDOWS\System32\OpenSSH\ssh-keygen.EXE`. Preliminary `readOnly` bridge profile yielded SSH positive false only because `tempfile.TemporaryDirectory` could not be created. This tool-profile error was isolated and the same baseline verified `True` under an authorized workspace execution profile. No cryptographic defect is inferred from the preliminary sandbox result.

Observed focused regression:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-877-crypto-sensitivity-all tests/unit/test_r0_p01_cryptographic_sensitivity.py
........                                                                 [100%]
8 passed in 0.54s
```

The checks include a well-framed Ed25519 signature mutation, embedded-allowlisted-key spoofing with a signature from an independent synthetic signer, exact signed-decision alteration, old C02 header-mutation weakness, C09 input-flow metamorphism, DER-valid ECDSA signature mutation, and a cross-signer ES256 assertion negative. Positive controls run through both actual verifiers. They prove only these exercised branches under the tested host environment, not all 13 security controls nor the future F1/F2 implementation. All results must remain public nonsecret synthetic tests.

The broader focused source/receipt/scenario regression was also executed with the new suite:

```text
python -B -m pytest -q -p no:cacheprovider --basetemp=.venv/.p01-877-focused-regression tests/unit/test_r0_p01_cryptographic_sensitivity.py tests/unit/test_r0_p01_f1_site_decisions.py tests/unit/test_r0_p01_scoring_boundary_rev02.py tests/unit/test_r0_p01_pending_review_register.py tests/unit/test_r0_p01_scoring_boundary_candidates.py tests/unit/test_r0_p01_clause_audit_receipts.py tests/unit/test_r0_p01_f1_audit_rev03.py tests/unit/test_r0_p01_successor_trace_guard.py
........................................................................ [ 78%]
....................                                                     [100%]
92 passed in 16.09s
```

The 92 results consist of eight new real cryptographic/derivation tests and 84 earlier source-audit/guard tests. Only eight are the new executable security sensitivity tests. Project-integrity postflight must pass separately before publication.

```text
VALIDATION_229=REAL_SYNTHETIC_CRYPTO_REGRESSION_PASS
OWNER_CREDENTIAL_USE=NONE
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
