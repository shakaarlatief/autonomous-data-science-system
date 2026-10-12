# Validation 242: independent synthetic WebAuthn ES256 verification component

**Date:** 2026-10-12
**Parent:** Research 554 / Checkpoint 890 / Validation 241
**Status:** 47_NEW_TESTS_PASS / 509_FOCUSED_PASS / PUBLIC_POSTFLIGHT_PENDING
**Scope:** Verification-only P-256 assertion with exact trust, statement, challenge and RP-origin binding, tested using ephemeral non-owner signatures; preservation of earlier cryptographic/F1/structural checks.
**Authority:** Bounded test result, not real browser/Windows Hello credential provenance or F1/F2 freeze.

New files:

```text
experiments/r0_p01_successor_synthetic/independent_webauthn_es256_verify.mjs
tests/unit/test_r0_p01_independent_webauthn_es256_verifier.py
```

No modification to historical RP, existing signing worker, approved owner B01/B02 source/decision receipts, original Attempt 001 evidence, or production architecture.

Targeted first run: **44 passed, zero failures** in 2.95 seconds. Before publication, the request parser was hardened to reject duplicate keys anywhere in the outer wire request. Three additional adversarial tests then passed, **47/47 new cases**, with the remaining focused regression to be rerun on the final files.

Regression commands used `python -B -m pytest -q -p no:cacheprovider` with group-specific `--basetemp=.venv/.p01-890-group-N`:

| Group | Scope | Outcome |
|---|---|---|
| 1 | New WebAuthn + independent SSH + source/receipt/B01 references | **246/246 PASS** |
| 2 | Historical/synthetic cryptographic and run-bound admission | **63/63 PASS** |
| 3 | Trusted claim store and governed evidence | **70/70 PASS** |
| 4 | Synthetic measurement and atomic finalization | **46/46 PASS** |
| 5 | Clause/site/review/scorer-boundary structural guards | **84/84 PASS** |
| **Total** | **425 executable + 84 structural** | **509/509 PASS** |

The tests verified existing worker-produced genuine synthetic ES256 proof material, separately enrolled public keys, and rejection of malformed/wrong source attributes. They did not invoke `navigator.credentials` in a browser, establish Windows Hello capability, capture real RP challenge/consumption events, or qualify a native process lifecycle. The scorer-side implementation is separately authored but uses the same standard Node crypto backend as the signer worker. No human owner credential or trial was used.

The exact committed-target public integrity check, publication, and GitHub postflight remain separate and will be evaluated before completion is claimed.

```text
VALIDATION_242=BOUNDED_ES256_CRYPTO_VERIFIER_PASS
EXECUTABLE=425
STRUCTURAL=84
FOCUSED_TOTAL=509
ATTEMPT_002=NOT_AUTHORIZED
```
