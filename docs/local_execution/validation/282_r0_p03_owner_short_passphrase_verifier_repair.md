# Validation 282: R0-P03 S1 A2 existing owner passphrase acceptance repair

**Date:** 2026-10-29
**Status:** SOURCE_FREE_OWNER_VERIFIER_INPUT_POLICY_REPAIRED_AND_SYNTHETIC_TESTED / LIVE_OWNER_CANONICAL_READBACK_PENDING
**Scope:** Correct an observed mismatch between OpenSSL owner key creation and Python `owner-verify` input acceptance, without retrieving the existing owner credential, decrypting the owner ciphertext here, changing report-schema validation or advancing scientific source-review gates.
**Basis:** Research 612–613, Validation 279–281, Checkpoint 898, and exact S1 A2 owner-reported safe diagnostic markers.

## Actual observed failure and limits

In the owner's ordinary local PowerShell, an existing recipient's `-Action Verify` reached the private-key passphrase prompt and returned:

```text
SOURCE_FREE_A2_OWNER_HOLD_CODE=OWNER_PASSPHRASE_INPUT_INVALID
SOURCE_FREE_A2_PROBE_HOLD
S1_A2_OWNER_HOLD=OWNER_REPORT_READBACK_FAILED
```

The new allowlisted stage code establishes that `owner_verify_ciphertext` rejected input *before* the private file, OpenSSL CMS or complete report validation stages. Before repair, the Python reader required 8–256 UTF-8 bytes and rejected CR/LF. The existing `Prepare` path accepted OpenSSL's native passphrase policy and did not impose that eight-byte minimum. A previous independent direct OpenSSL owner-side decrypt was **owner reported** PASS, not proof of canonical five-record recovery. The safe code does not distinguish a short, empty, overly long or line-delimited input, and the owner did not disclose their actual passphrase or its length. Thus the narrower concrete conclusion is **verifier-side passphrase input rejection**, not proof of its particular private value or of a defective owner key.

## Exact bounded code repair

- In `experiments/r0_p03_navigation_probe/s1_a2_candidate_protected_output_probe.py`, changed only the owner-side transport acceptance threshold from `8 <= len(passphrase) <= 256` to `1 <= len(passphrase) <= 256`, with a standalone explanatory comment. The existing recipient's passphrase is not being changed or re-enrolled.
- Continued refusing empty, CR/LF-containing, non-byte and larger-than-256-byte input. No exception text, OpenSSL stderr, credential property, key path, private canary or decrypted report is printed.
- Kept exact ciphertext hash and file checks, OpenSSL recipient and encrypted-key authentication, authenticated CMS result gating, canonical JSON, exact record population, false role flags, and existing bounded public-safe diagnostic outputs unchanged. The candidate `seal` route, PowerShell recipient helper, ciphertext and owner receipt are unchanged.
- In `tests/unit/test_r0_p03_s1_a2_candidate_protected_output_probe.py`, added synthetic short-input acceptance boundary tests (1, 5, 7 bytes), invalid input transport rejection cases, and a genuine synthetic RSA/OpenSSL AES-256-GCM CMS round-trip using a disposable encrypted key with a deliberately public six-byte test passphrase. An incorrect short test passphrase still produces `CMS_AUTHENTICATION_FAILED`. No real owner file or credential is touched.

**Focused verification:** Existing protected-output and owner helper test suites, run through the repository's installed Python in ignored test scratch, reported **50 passed in 2.74 seconds**. This is focused engineering evidence only; actual owner `Verify` has **not** yet been repeated against the saved encrypted report following this repair. Public aggregate integrity and publication status must be assessed separately before the owner is asked to rerun the locally installed script.

## Continuing boundary

The intended owner operation is `-Action Verify` **once** with the same recipient ID, same saved CMS ciphertext, same encrypted key and passphrase entered only at the owner's own PowerShell prompt. Report only fixed safe output markers. Do not run `Receive` again, create a new recipient, rerun the candidate, send private materials to ChatGPT, or use `-out NUL`.

A source-free successful complete readback would validate only the explicitly bounded receipt/record recovery. It would not prove A2-R05 confidential custody, A2-R07 future blinded-author access denial, independent reviewer/challenger admission, real historical source approval, S3 author-world freeze, hidden gold, or B0–B4 scoring.

```text
OWNER_INPUT_REJECTION=OBSERVED_BEFORE_CMS
ROOT_CAUSE_CLASS=VERIFIER_INPUT_POLICY_MISMATCH
EXACT_OWNER_PASSPHRASE_LENGTH=NOT_OBSERVED
OWNER_CREDENTIAL_OR_CIPHERTEXT_CHANGED=NO
SYNTHETIC_SHORT_CMS_ROUNDTRIP=PASS
FOCUSED_TESTS=50_PASS
REAL_OWNER_CANONICAL_READBACK=PENDING
HISTORICAL_SOURCE_DELIVERY=ZERO
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
