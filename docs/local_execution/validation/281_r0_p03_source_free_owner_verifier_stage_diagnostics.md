# Validation 281: Source-free owner verifier stage-safe diagnostics

**Date:** 2026-10-29
**Status:** STATIC_ALLOWLIST_STAGE_DIAGNOSTICS_IMPLEMENTED_AND_TESTED / LIVE_OWNER_DIAGNOSTIC_NOT_YET_RERUN
**Scope:** Repair attribution for the existing S1 A2 owner-only strict verifier failure, without creating a recipient, rerunning an independent candidate, accessing owner secrets or loosening the scientist's full-report gate.
**Basis:** Research 613 and earlier Research 612 / Validation 279–280.

## Exact changes

1. `experiments/r0_p03_navigation_probe/s1_a2_candidate_protected_output_probe.py`: added a frozen allowlist of source-free known validation errors. The `owner-verify` CLI now emits a separate `SOURCE_FREE_A2_OWNER_HOLD_CODE=<approved code>` **only** when it catches an enumerated `ProbeHold`. An unknown `ProbeHold` maps to `OWNER_UNCLASSIFIED_HOLD`; all other input, OS and subprocess errors retain the prior generic `SOURCE_FREE_A2_PROBE_HOLD`. The existing generic hold marker and exit code 2 are unchanged. No exception message, OpenSSL stderr, private report, path, canary, nonce or passphrase is disclosed. The candidate `seal` CLI remains unchanged.
2. `tests/unit/test_r0_p03_s1_a2_candidate_protected_output_probe.py`: added four mock-only CLI tests of known safe output codes and suppression of arbitrary sensitive text, using only invented command arguments and a synthetic fake passphrase. No actual owner operation is executed.

**No changes** were made to the existing owner key, owner recipient, certificate, saved ciphertext or receipt. No change was made to passphrase input handling, cryptographic authentication, CMS parser or canonical report schema. An 8-byte minimum passphrase constraint remains in the Python path until an observed diagnostic confirms or rules out that particular issue.

## Tests and evidence

- Existing owner PowerShell SelfTest: previously reported PASS (Validation 280).
- Focused owner/CMS probe regression after patch: **41 passed in 3.40 seconds**, including the four new static allowlist tests.
- Direct attached ciphertext SHA-256: **2,527 bytes**, `a99c16edc049fb87f630803ee026752ff9d06625ef35f88386e92f36b70512fd` (independent local attachment check).
- Owner-reported `OWNER_KEY_UNLOCK=PASS` and `OWNER_CMS_DECRYPT=PASS` confirm positive native OpenSSL witness but **not** complete Python report validation.
- A genuine owner `Verify` after this patch **has not yet been performed**.

**Observed containment hazard:** The subsequent Git status showed an unexpected untracked repository-root file named `NUL` after the owner's separate direct OpenSSL `-out NUL` decryption test. The filename alone was inspected, **never its content**. It may contain synthetic plaintext and private fictional canaries. This is not part of the protected owner handoff and must not be staged, read by the exposed coordinator or published. The owner has been asked to remove that exact file locally via the Windows extended-length file path. Cleanup is **pending confirmation**; no protected-output privacy admission is possible while the risk remains. Do not reuse bare `-out NUL` as an assumed Windows discard sink. See Research 613.

No independent negative test has yet proved the future task-author route cannot access the restricted reviewer output. This diagnostic is source-free and does not promote real source-reviewer admission, confidential custody, author-world freeze or B0–B4 scoring.

## Owner continuation

In the owner's own ordinary PowerShell terminal, using the **existing recipient identifier**, invoke `scripts/r0_p03_s1_a2_owner_source_free_recipient.ps1 -Action Verify`. Enter the existing passphrase locally. If the strict validation succeeds, the wrapper will print the usual complete readback and recovery markers. If it fails with a known `ProbeHold`, the output now includes the safe category `SOURCE_FREE_A2_OWNER_HOLD_CODE=<code>` followed by the generic hold and wrapper hold. Report **only** the markers. Do not repeat `Receive`, regenerate credentials, print decrypted content, send secret paths, or rerun the candidate without new evidence.

```text
VALIDATION_281=STATIC_OWNER_VERIFIER_HOLD_DIAGNOSTIC_READY
TESTS=41_PASS
REAL_OWNER_RECOVERY_STRICT_VERIFICATION=PENDING
HISTORICAL_SOURCE_DELIVERY=ZERO
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
