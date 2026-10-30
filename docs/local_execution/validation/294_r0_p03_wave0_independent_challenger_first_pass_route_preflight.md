# Validation 294: Wave0 separate independent first-pass challenger route, prior private review protected

**Date:** 2026-10-30
**Status:** CHALLENGER_FIRST_PASS_SYNTHETIC_CMS_AND_OWNER_SCRIPT_SYNTAX_PASS / ACTUAL_SECOND_SOURCE_DELIVERY_NOT_AUTHORIZED_OR_EXECUTED
**Scope:** Verify bounded new challenger-specific delivery/custody mechanics after the owner reported successful real first-reviewer Receive/Verify, with synthetic-only cryptography tests and no private report read from owner storage, no second real-source transfer and no false claim of completed adversarial challenge.
**Research:** 619 and 617–618.
**Specification:** 028 unchanged.
**Basis:** Validation 293's relayed two authenticating owner-side outputs, exact first reviewer ciphertext digest from Validation 292 and the unchanged source ZIP SHA-256 from Validation 288.

## 1. Owner-reported predecessor state

The owner relayed two full successful calls from the existing owner real-review script:

```text
S1_REAL_REVIEW_OWNER_RECEIVE=PASS
S1_REAL_REVIEW_OWNER_RECHECK=PASS
S1_REVIEWER_OWNER_COMPLETE_PRIVATE_READBACK=PASS
S1_REAL_REVIEW_OWNER_FULL_READBACK=PASS
authenticated_ciphertext=PASS
complete_reviewer_records=10
source_ref_and_batch=PASS
reviewer_dispositions=RESTRICTED_NOT_PRINTED
challenge_state=PENDING
author_world=WORLD_UNFROZEN
```

This resolves the earlier owner-recovery HOLD **only** for exact, complete protected delivery. The exposed coordinator did not observe real decryption, private dispositions or review quality. The existing reviewer report stays owner-held and never enters the new challenger source-first-pass packet.

## 2. Actual verification of newly prepared first-pass route

The new challenger route was implemented with **separate role identity**, exact-source ten-file archive verification, original reviewer **ciphertext digest only**, `first_reviewer_report_seen=false` and `first_reviewer_conclusions_seen=false` in the report schema, required `ACTUAL_ADVERSARIAL_CHALLENGE_PENDING`, ten independently written complete-file status proposals and no source admissions. The new ciphertext filename differs from the existing reviewer report; the private owner recipient ID/key can be reused without exposing the key to the challenger.

Synthetic-only tests created invented ten-source ZIP blobs and a new **fictional** encrypted RSA certificate/key in ignored test scratch. Observations:

- Distinct independent report schema rejects confusion with the original reviewer format.
- Exact source-row identity, canonical record count, incomplete/duplicate source, unauthorized status or excerpt, role and false first-reviewer-exposure fields fail closed.
- Actual OpenSSL CMS AES-256-GCM encryption/decryption succeeds for the **fictional** report, and wrong passphrase / one-byte ciphertext modification are rejected.
- Integrated focused regression: **14/14 tests PASSED**, consisting of four new challenger tests, six original protected reviewer route tests and four first-wave source-selection tests.
- The owner-only PowerShell script's AST parsing returned `OWNER_CHALLENGER_SCRIPT_AST=PASS`; it was **not** actually executed with owner private keys or recipient ID.

The new script `scripts/r0_p03_s1_owner_wave0_challenger_first_pass.ps1` has `SelfTest`, `Receive` and `Verify`, not a key creation action. It will require that the original reviewer ciphertext is still saved in the original owner-only folder and matches SHA-256 `9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366`. It creates only a distinct challenger ciphertext/owner receipt with no overwrite, verifies source ZIP and original reviewer preserved, and prints no private conclusions. Real independent owner execution and second encrypted report recovery are still **untested**.

The new challenger handoff requires **five exact attachments**: identical original owner-local source ZIP, source-status challenger handoff, new challenger module, its public-safe original protected source reader dependency, and the same public-only owner certificate. It explicitly **excludes** the first-reviewer ciphertext, its restricted report, owner receipt and key.

**Integrated prepublication regression:** An additional combined run of the new challenger module, original Wave0 protected reviewer transport, first-wave source selector, historical source audit, frontend expansion, task-capacity and neutral eligibility mapping produced **105/105 PASS (25.78 seconds)**. The separately executed aggregate repository integrity check returned **all six family-aware checks PASS and `PUBLIC_REPOSITORY_INTEGRITY=PASS`**. `git diff --check` exited zero, with only known nonblocking Windows LF-to-CRLF advisories. The exact intended public-safe worktree contains nine paths: two continuity indexes, Research 619, Validations 293–294, new challenger handoff, new challenger Python module, new owner-only PowerShell script and new invented-source tests. No original owner key or reviewer-private ciphertext was staged.

**2026-10-30 postpublication portability correction:** The first published challenger module imported its public-safe source validator through the ADS Python package path. Independently uploaded files in a fresh Temporary Chat may instead reside in one flat attachment directory, so the module now falls back **only when the ADS package is absent** to the exact named sibling `s1_source_status_protected_route.py`, without requiring web or repository access. A new synthetic source-free regression copies only these two modules into an otherwise isolated temporary directory and loads the challenger with Python `-I -B`; result `INDEPENDENT_TWO_FLAT_ATTACHMENTS=PASS`. The combined source/crypto and existing architecture-diagnostic suite subsequently passed **106/106 in 26.87s**. This correction changes only how the public code dependency resolves; it does not touch the owner key, saved first-reviewer CMS, exact original source ZIP, reviewer report, source-status decisions, actor permissions or science hold. The owner-only PowerShell wrapper remains unexecuted with real keys.

## 3. Not yet established

- No new independent source-status challenger has actually received the ten original files in a second session; the original owner approval for the first reviewer did not automatically authorize **this exact second recipient's source transfer**.
- No actual blind-to-reviewer second review, protected second ciphertext, owner second readback, owner-only *two-report* comparison or substantive adversarial critique of original reviewer reasoning has occurred.
- A second-session report can **claim** not to have seen the first reviewer, but cannot cryptographically prove provider-level non-exposure; record this residual Level B limitation.
- Exact material disagreements, source classifications and text-specific contamination details remain unavailable to the public coordinator. A future private owner-only comparator and targeted adversarial challenge still require engineering and owner approval after actual independent assessment, not speculative source labels now.
- No external source, reference/gold, arm data, new test questions, or blind author packet is admitted.

## 4. Nonpromotion status

```text
VALIDATION_294=INDEPENDENT_CHALLENGER_FIRST_PASS_PREPARED
PREVIOUS_FIRST_REVIEWER_OWNER_RECEIVE_AND_VERIFY=REPORTED_PASS
CHALLENGER_SPECIFIC_SOURCE_FREE_CMS_REGRESSIONS=14_OF_14_PASS
CHALLENGER_OWNER_SCRIPT_AST_PARSE=PASS
CHALLENGER_OWNER_ACTUAL_RECEIVE_OR_VERIFY=NOT_EXECUTED
CHALLENGER_EXACT_SECOND_SOURCE_DELIVERY_AUTHORIZATION=PENDING
CHALLENGER_FIRST_PASS_SOURCE_DELIVERY=ZERO
CHALLENGER_PRIVATE_REPORT=NOT_CREATED
ACTUAL_ADVERSARIAL_CHALLENGE=NOT_STARTED
SOURCE_STATUS_ADMISSIONS=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
