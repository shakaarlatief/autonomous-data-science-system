# Validation 240: read-only synthetic issuer source and independent SSH proof replay

**Date:** 2026-10-12
**Research:** Research 552
**Parent:** Research 551 / Validation 239 / Checkpoint 887
**Scope:** Real OpenSSH re-verification from trusted-context-bound local synthetic issuer state, negative tamper and restart controls, and adjacent R0-P01 regressions.
**Status:** 22_NEW_SOURCE_TESTS_PASS / 431_FOCUSED_PASS / PUBLIC_POSTFLIGHT_PENDING
**Authority:** Non-owner test-only evidence; no real R0-P01 owner attempt or F1/F2 freeze.

Two files were added, with no change to the existing `SyntheticClaimStore`, legacy R0-P01 harness, approved B01/B02 bytes, or old experiments:

```text
experiments/r0_p01_successor_synthetic/independent_ssh_claim_source.py
tests/unit/test_r0_p01_independent_ssh_claim_source.py
```

The source consumer opens the existing database with SQLite `mode=ro`, checks the externally supplied expected issuer genesis and nonce, reconstructs claim statements, reads the entire selected transaction snapshot, and invokes native OpenSSH for every recorded admission. The fresh-process test does **not** import the signing worker as an active process or use a stored private signer key. The new consumer deliberately does **not** return `event_terminal` or claim source-origin attestation.

Actual focused commands on the worktree used `python -B -m pytest -q -p no:cacheprovider`, with group-specific `--basetemp=.venv/.p01-888-group-N`:

| Group | Test scope | Result |
|---|---|---|
| 1 | New source-consumer + prior SSH observation + B01 receipt/numeric references | **168/168 PASS** |
| 2 | Real non-owner crypto/admission and run-bound tests | **63/63 PASS** |
| 3 | Trusted claim store and governed synthetic evidence | **70/70 PASS** |
| 4 | Synthetic measurement and atomic finalization | **46/46 PASS** |
| 5 | Clause/source-flag/review/trace structural guards | **84/84 PASS** |
| **Total** | **347 executable + 84 structural** | **431/431 PASS** |

The standalone source test initially passed **21/21**, then the reader was refined to close the SQLite connection explicitly and classify malformed journal inputs uniformly as `UnqualifiedSourceError`; the final grouped tests passed after that refinement. There were no observed failed regression tests or test-fitted threshold changes.

A subsequent twenty-second test **deliberately bypasses the trusted issuer admission method**, writes a self-consistent `ADMITTED` row containing a genuinely valid separately obtained synthetic proof, and confirms that the consumer can only verify proof validity as presented, while explicitly leaving producer origin unauthenticated. This is a demonstrated limitation, not a forged source authenticated as real. The final new source module alone passes **22/22**.

The new mechanism detects **local record corruption and wrong trusted-claim binding**. It does not prove independent issuer origin, currentness against hostile full-journal rollback, true owner authorization or genuine F1 completion. No source-origin qualification, cryptographic key enrollment, owner prompt or WebAuthn platform operation occurred.

The published-HEAD public aggregate integrity gate and branch synchronization will be checked and recorded separately after publication. These focused test groups are not a complete integrated V3 gate.

```text
VALIDATION_240=BOUNDED_SSH_SOURCE_REVERIFICATION_PASS
FOCUSED_TESTS=431
ORIGIN_ATTESTATION=NOT_QUALIFIED
F1_F2=UNFROZEN
ATTEMPT_002=NOT_AUTHORIZED
```
