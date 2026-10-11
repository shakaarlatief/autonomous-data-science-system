# Validation 232: R0-P01 signed fresh-run claim identity and cross-run cryptographic replay

**Date:** 2026-10-11
**Status:** 21_REAL_SYNTHETIC_CLAIM_NONCE_SECURITY_TESTS_PASS / FULL_SUCCESSOR_UNQUALIFIED
**Scope:** Test different trusted run identities inside actual SSHSIG/ES256 signed bytes, not only an unsigned external SQLite run label.
**Parent:** Research 544 / Checkpoint 880 / Validation 231.
**Authority:** Public non-owner cryptographic testing only. No owner attempt, Windows Hello device, F1/F2 freeze, or policy edit.

Added `run_bound_acceptance.py`, a separate `run_bound_crypto.mjs` synthetic signer/verifier and `test_r0_p01_run_bound_acceptance.py`. All private signing keys are ephemeral Node KeyObjects held in memory. The Python SSH verifier writes only public allowlist/proof files. No historical V02 code or Attempt 001 evidence changed.

The new signature format includes exact `protocol` and 256-bit `claim_nonce` fields. The cryptographic verifier requires an independently supplied **trusted expected entire statement**: an attacker cannot merely claim the old run's nonce as the new run's identity. Ed25519 SSHSIG uses the new `ads-r0-p01-claimed-run-v1` namespace, and ES256 uses a challenge hashing the exact signed statement. Tests establish both valid positive controls and actual invalid-context/replayed-signature negatives under **the same signer and acceptance ID** across run 1/run 2.

### Observed executable tests

```text
python -B -m pytest -q -x -p no:cacheprovider --basetemp=.venv/.p01-880-run-bound-first tests/unit/test_r0_p01_run_bound_acceptance.py
.....................                                                    [100%]
21 passed in 0.97s
```

The initial combined execution exceeded the tool bridge timeout without returning pytest results; no success was inferred from the timeout. The same 11 module scopes were then executed in two bounded groups with both successfully completed:

```text
... --basetemp=.venv/.p01-880-executable [new run-bound + three previous executable synthetic modules]
...............................................................          [100%]
63 passed in 10.08s

... --basetemp=.venv/.p01-880-structural [seven historical source/review guard modules]
........................................................................ [ 85%]
............                                                             [100%]
84 passed in 17.28s
```

**Total focused evidence: 147 PASS**, comprising 63 genuine executable synthetic cryptographic/admission/durability tests and 84 source/review/regression structural tests. Results are reported separately to avoid misrepresenting structural audit guards as cryptographic tests.

### Deliberate limitations

Signature-level cross-run proof binding is demonstrated but does not implement a durable authoritative nonce issuer, exact expected-statement retrieval, complete successor trust/role admission, SQLite journal reconciliation, owner-visible confirmation, hardware WebAuthn or a scored F1/F2 oracle. The WebAuthn-style ES256 path is synthetic and cannot prove Windows Hello capability. Node/test label restrictions ensure only synthetic non-owner crypto is used. A real owner experiment has not started and requires separate explicit authorization.

```text
VALIDATION_232=SIGNED_RUN_NONCE_NEGATIVE_PASS
EXECUTABLE_SYNTHETIC_TESTS=63
STRUCTURAL_REGRESSION_TESTS=84
TOTAL_FOCUSED_TESTS=147
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
