# Research 602: Owner-side fictional S1 reviewer-report recipient, isolated from legacy reference custody

**Date:** 2026-10-21
**Status:** OWNER_SCRIPT_AUTHORED_AND_SOURCE_FREE_TESTED / PREPARE_RECEIVE_VERIFY_NOT_OWNER_EXECUTED / REAL_REVIEW_HOLD
**Scope:** Implement the minimum owner-side handoff for the three-record fictional source-status reviewer report introduced in Research 601. Preserve the older 9+12 fake reference recipient as a distinct, untouched contract. Test the new parser and cross-language CMS authenticity with disposable keys, then request a separate owner decision before creating a protected owner folder or invoking an external Temporary Chat.
**Basis:** Research 513/559/576/586–589/594/600–601; Validation 268–269; current prospective S1 owner-mediated route V0.1, Checkpoint 898 and Specification 028.
**Authority:** Source-free engineering only. Neither an independently admitted real source-status reviewer nor an owner/private review-custody system has been qualified. No real historical sources, protected reviewer ledger, independent challenge, task author, hidden gold or B0–B4 scored case were accessed.

## 1. Deliberately separate recipient, unchanged old reference logic

The pre-existing `scripts/r0_p03_fake_public_recipient.ps1` is expressly restricted to nine invented legacy plus twelve invented primary reference cases. Its cryptographic readback and strict old packet validator cannot legitimately accept an unrelated source-status reviewer report.

Added `scripts/r0_p03_fake_reviewer_recipient.ps1`, with distinct file names, marker, folder prefix and parser. The old script has **not** been modified. The new script is a Windows PowerShell 5.1 owner-side interface with four explicit actions:

- `SelfTest`: pure in-memory schema and negative-case validation; no owner identity lookup, key generation, private folder, downloads or permission mutation;
- `Prepare`: **only when separately approved and run by the non-elevated desktop owner**, allocate one NEW random direct child of LocalAppData with inheritance-disabled DACL limited to the owner SID and SYSTEM, create a disposable RSA key and self-signed certificate for fictional use, and export only the public certificate to standard Downloads;
- `Receive`: after a separate Temporary Chat actually produces the exact named fake CMS, require the existing approved folder, exact Downloads basename, expected ciphertext SHA-256, non-reparse file, bounded size and clean no-overwrite target; authenticate/decrypt in memory and validate the complete fake report **before** storing ciphertext and a private owner receipt. Launch `Verify` in a new owner PowerShell process;
- `Verify`: recheck directory/key/certificate/ciphertext/receipt and ACL expectations, ciphertext digest, AEAD validity, complete synthetic report schema and owner-only private report digest; print fixed PASS/FAIL-style markers rather than decrypted fake notes.

This implementation copies the *safeguards* of the old owner-only fake key workflow but does not copy its old 9+12 source format. OpenSSL key generation consumes native stderr through asynchronous process drains, explicitly avoiding the previously observed Windows PowerShell 5.1 progress/NativeCommandError failure in Research 588.

**Design limit:** The owner file ACL checks and owner identity guards are code paths awaiting **actual owner-desktop execution**. Running tests against disposable Python/PowerShell files under ignored `.venv` does not prove owner LocalAppData ACLs, owner/agent separation, confidential backup/retention, non-repudiation, private recipient lifecycle or independent AI reviewer role.

## 2. Exact format and cross-language agreement

The new owner-side PowerShell validator accepts only the already implemented Python `s1-fictional-reviewer-report-v1` data contract, not arbitrary historical source-status notes. The whole private report must include:

- fictional manifest and marker, exact top-level keys, explicit false nonqualification flags;
- **exactly three** distinct invented source IDs and verified fixed SHA-256 source hashes;
- strict boolean delivered and inspected values, an explicit missing-source HOLD, typed file/span/representation-component status, and complete per-item accounting;
- only the closed inventoried fake private-note codes, including an invented restricted design cue;
- no added keys or free-text real source paths, IDs or actual gold material.

The sender encrypts a canonical JSON fake report with OpenSSL CMS AES-256-GCM using **only the public certificate**, emits `R0_P03_FAKE_REVIEWER_REPORT.cms` plus a strictly bounded public metadata receipt, and does not write the plaintext. The owner receiver uses the separately held disposable private key. Verification checks the complete private report, not merely ciphertext existence or hash. On a GCM authentication failure, captured provisional plaintext must never leave the process as a success output.

For the fake trial alone, the owner receipt includes a **private** plaintext report digest for exact readback. This is not published. For future real records even source-specific hashes, output length, filenames and error messages would require independent privacy and cumulative-publication scrutiny.

## 3. Tests performed and discovered integration issue

The owner script's direct `SelfTest` ran successfully in the authorized read-only project command context:

```text
S1_FAKE_REVIEWER_RECIPIENT_SELFTEST=PASS
S1_OWNER_ACCOUNT_AND_FILES_UNTOUCHED=TRUE
```

The first Python-initiated isolated PowerShell cross-language test tried to pass the complete function prelude in an `-EncodedCommand` argument and failed due to Windows process command-line length limits (WinError 206). The error was in **test delivery**, not the source-status validator. The harness was changed to write disposable testing-only PowerShell scripts in ignored `.venv` temporary directories and invoke them with a short `-File` argument. No owner action is included in those extracted tests.

The corrected focus run passed **27 tests**. An additional disposable RSA certificate, Python sender to PowerShell CMS-decrypt/full-fake-report test and deliberately tampered-ciphertext rejection test brought the focused count to **28 passing**. The consolidated eight-module suite passed **96 tests** including the old recipient, old fake sender, S1 transport/journal and role simulations (Validation 269).

The cross-language test demonstrates a genuine Python AES-256-GCM CMS encrypted report is accepted by PowerShell, with fake private-note content excluded from stdout and tampered ciphertext rejected. It does not demonstrate a separate owner-held key, genuine new Temporary Chat, approved private output destination, or author-facing source exclusion.

## 4. Owner-controlled handoff is the next actual boundary

The remaining meaningful A1 step in the proportionate S1 M1 workflow is **one**, deliberately authorized, **fictional-only** owner recipient Prepare → standalone Temporary Chat reviewer-shaped fictional CMS sender → owner Receive/Verify cycle. Do not use or overwrite the Research 589 owner fake reference key/folder, do not require two Windows accounts by default, and do not introduce a dedicated secret service solely because the code now exists.

This stage prepared the new owner recipient implementation and test evidence but **did not call `Prepare`, `Receive`, or `Verify` against the owner's protected directory**. The specific owner execution step should only follow confirmation that the user accepts creation of a new one-time fake-only LocalAppData recipient and a public-only certificate in Downloads. Owner should not paste the private key, owner path or decrypted report into the coordination chat. If any action fails after producing partial state, stop and diagnose; do not blindly rerun `Prepare` or `Receive`.

Once owner readback is verified, the fake-only trial must stop. Any real historical-source admission still requires V0.4 independent acceptance, a genuine non-arm reviewer/challenger, pinned source-batch/representation fidelity, private evidence custody and an independently screened author-source packet.

## 5. Scientific stop conditions

```text
RESEARCH_602=NEW_SOURCE_FREE_OWNER_RECIPIENT_IMPLEMENTED
OLD_9_PLUS_12_RECIPIENT=UNMODIFIED
NEW_OWNER_RECIPIENT_SELFTEST=PASS
PYTHON_TO_POWERSHELL_CMS_INTEROP=PASS_FAKE_ONLY
OWNER_PROTECTED_PREPARE=NOT_EXECUTED
OWNER_DOWNLOADS_RECEIVE=NOT_EXECUTED
LIVE_TEMPORARY_CHAT_REVIEWER_HANDOFF=NOT_EXECUTED
OWNER_PRIVATE_REAL_SOURCE_STATUS_LEDGER=NOT_QUALIFIED
SOURCE_STATUS_METHOD_V04=NOT_INDEPENDENTLY_ACCEPTED
REAL_SOURCE_REVIEW=NOT_STARTED
SOURCE_ADMISSIONS=ZERO
HIDDEN_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
