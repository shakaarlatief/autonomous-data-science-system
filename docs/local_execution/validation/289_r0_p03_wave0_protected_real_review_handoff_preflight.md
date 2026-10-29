# Validation 289: Wave0 real-source handoff and new owner-only CMS route preflight

**Date:** 2026-10-29
**Status:** EXACT_BATCH_BOUND_REAL_SOURCE_REVIEW_TRANSPORT_SYNTHETIC_TESTED / OWNER_RUNTIME_AND_REAL_SOURCE_DELIVERY_UNEXECUTED
**Scope:** Observe and qualify the bounded new protected-output transport mechanics for the existing staged ten-source historical wave without reading any actual owner-private key, dispatching historical source bytes, leaking reviewer-only rationale, appointing a reviewer/challenger or commencing scored work.
**Basis:** Research 617–618, Validation 288, owner Level B direction, Checkpoint 898 and Specification 028.

## 1. Exact original-source batch read-only check

The new Python module `s1_source_status_protected_route.py` read the *already staged* exact Wave0 ZIP from ignored local `.venv` in a read-only inspection, verified the outer SHA-256 and independently loaded all ten original source entries with matching Git blob SHA-1 framing, SHA-256 and exact sizes. It returned only:

```text
ACTUAL_WAVE0_VERIFIER=PASS
ROWS=10
SOURCE_BODIES_NOT_PRINTED=TRUE
```

No source-specific path, original body, proposed source status or forbidden reviewer note was copied into the public coordinator output. The original Git repository was already public; the newly assembled review-selection manifest remains unpublished.

## 2. Synthetic-only actual CMS interoperability and defect repair

The new `tests/unit/test_r0_p03_s1_source_status_protected_route.py` constructs ten **invented** source files in a synthetic ZIP, patches only the test's expected hash constants, and builds a complete fictional source-status restricted report. It exercises:

- Exact ten-record manifest alignment and source blob validation, source-identity drift, incomplete report and unsupported role rejection.
- No promotion of uninspected files, `CHALLENGE_PENDING` and `WORLD_UNFROZEN` constraints, complete-file-only reporting and no unqualified exact excerpt/conditional bundle.
- Strict canonical JSON and duplicate-field rejection.
- Real OpenSSL CMS AES-256-GCM encryption and decryption using a brand-new **fictional-only** encrypted RSA test key in ignored test scratch. Wrong key passphrase and altered authenticated ciphertext are rejected; private notes are never printed in passing assertions or public receipts.

The initial first run reported **4 pass / 2 fail**, revealing two defects before real-source work: a generic error wrapper overwrote the duplicate-JSON diagnostic code; and the CMS verification invoked OpenSSL without `-in <ciphertext file>` while also using stdin for owner passphrase, causing real decryption to fail. Both were repaired explicitly. The corrected rerun returned **6/6 PASS** in 0.82s. A subsequent combined run with the four first-wave source selector tests returned **10/10 PASS** in 0.97s.

## 3. Owner-only PowerShell recipient non-execution boundary

The separately implemented `scripts/r0_p03_s1_owner_real_review_recipient.ps1` was parsed using the Windows PowerShell AST parser, returning `OWNER_PS_PARSE=PASS`. A deliberately read-only command to invoke its `SelfTest` in the exposed noninteractive Codex sandbox was blocked **before execution** by that host's PowerShell script execution policy, so it is not represented as an owner-side `SelfTest` PASS. No policy was changed, and no bypass, key generation, real CMS decrypt, owner-only directory read, or owner-level interactive command was performed.

The script explicitly provides `SelfTest`, `Prepare`, `Receive` and `Verify` only for a user-operated ordinary local PowerShell session. Its ordinary Windows owner+SYSTEM DACL does **not** by itself prove that another same-SID application cannot inspect that user's protected storage. Actual real private owner credential creation, receipt, verified readback and later separate challenger admission remain **unexecuted**.

## 4. Next gate

The handoff and source/transport tools are authored for a **specific preexisting** source ZIP, exact size 26,416 bytes, SHA-256 `c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387`. No source batch was sent to another model. An explicit informed owner authorization must still cover exactly this batch, a fresh reviewer-only session, a distinct newly generated public recipient/custody route, and role exclusions. The new reviewer output must remain protected, and returned safe markers should not imply source-status admission or independent challenger acceptance.

If authorized, the immediate next operational observation is local owner script `SelfTest` and newly generated owner recipient, **not** another fabricated CMS loop. Owner `Prepare` should only follow a successful local selftest and explicit authorization; the final real reviewer can then inspect the permitted batch and generate restricted source-status proposals.

**Observed prepublication verification:** The integrated suite covering this new protected route plus Wave0 selection, historical evidence review, frontend expansion, capacity and neutral mapping returned **101/101 PASS in 25.82 seconds**. The first aggregate integrity invocation timed out inside the authorized execution host without an observed validator result; the separate retry exited zero, with all six checks PASS and `PUBLIC_REPOSITORY_INTEGRITY=PASS`. `git diff --check` exited zero (only standard Windows LF-to-CRLF advisory). The exact worktree contained **eight intended public-safe paths**: new Python reviewer transport, new real owner PowerShell recipient, source-free test, public handoff, Research 618, Validation 289 and the two continuity indexes. The actual original source ZIP and selected-path manifest remained Git-ignored. Guarded Git commit/push and independent remote verification are separate follow-on actions; no completion is claimed until observed. Source-free synthetic checks cannot certify the actual owner session or independent reviewer identity.

```text
VALIDATION_289=OWNER_ROUTE_PREPARATION_WITH_SYNTHETIC_AES_GCM_VERIFICATION
NEW_REAL_SOURCE_REVIEW_OWNER_KEY=NOT_GENERATED
NEW_REAL_SOURCE_REVIEW_OWNER_SHELL_SELFTEST=NOT_EXECUTED
PROTECTED_OUTPUT_PLAINTEXT_PUBLISHED=NO
REAL_WAVE0_SOURCE_BYTES_SENT_EXTERNALLY=NO
REAL_REVIEWER_AND_CHALLENGER=NOT_ADMITTED
OWNER_BATCH_SPECIFIC_APPROVAL=PENDING
S3=WORLD_UNFROZEN
S4=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028_UNCHANGED
```
