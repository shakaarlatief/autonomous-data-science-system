# Validation 291: Owner-reported real Wave0 recipient creation

**Date:** 2026-10-30
**Status:** OWNER_REPORTED_REAL_WAVE0_RECIPIENT_PREPARED / ACTUAL_REVIEWER_SOURCE_DELIVERY_NOT_YET_OBSERVED
**Scope:** Reconcile the owner's actual local encrypted-recipient preparation result after the exact Wave0 historical-source authorization in Validation 290, and identify the next bounded separate-session reviewer delivery without disclosing owner credentials or restricted source-specific findings.
**Research:** 617–618.
**Specification:** 028 (unchanged).
**Evidence provenance:** The owner pasted three safe terminal output markers after receiving the exact SelfTest/Prepare commands. The public engineering coordinator did not run, inspect or receive the owner's private key, passphrase, LocalAppData folder, downloaded public certificate, certificate hash or nonsecret recipient ID.

## 1. Actual owner-reported output

The owner provided precisely:

```text
S1_REAL_REVIEW_OWNER_RECIPIENT_PREPARED=PASS
S1_REAL_REVIEW_OWNER_PRIVATE_KEY_ENCRYPTED=TRUE
S1_REAL_REVIEW_CUSTODY_EXCLUSION_PROVEN=FALSE
```

These markers are emitted by `scripts/r0_p03_s1_owner_real_review_recipient.ps1 -Action Prepare` **after** the local `Verify-Batch` check, generation of a new password-protected RSA key pair, encrypted-private-key header validation, public-certificate existence/format check and public-certificate export to Downloads. The observation is **owner-relayed**, not an independently observed local command invocation. The success marker is stronger evidence than a speculative "I tried" message, but does not authenticate who executed the owner's terminal or prove a cryptographic identity against the coordinator.

The owner has **not pasted** the separate SelfTest output `S1_REAL_REVIEW_OWNER_PREFLIGHT=PASS`; do not silently mark that action independently observed merely because Prepare completed. The successfully reported Prepare itself executes the source ZIP prerequisites and demonstrates their owner-reported completion. The script also emits public certificate path, SHA-256 and recipient ID on success, but these three *additional* values have not yet been supplied to this engineering chat; do not invent them or assert their identities.

## 2. Qualified outcome and continuing holds

- `PREPARED=PASS`: **owner-reported success** of the purpose-specific new real-review key/certificate generation and public export, not the previous fictional-only key reuse.
- `PRIVATE_KEY_ENCRYPTED=TRUE`: **owner-reported encrypted at-rest key header**, not end-to-end provider confidentiality.
- `CUSTODY_EXCLUSION_PROVEN=FALSE`: correctly preserved limitation. Ordinary owner+SYSTEM ACL does not establish same-Windows-user process exclusion, independent provider isolation or direct author-route access denial.
- No real source ZIP has been reported delivered to a separate reviewer. No source-status assessment, ciphertext, owner `Receive`/`Verify`, independent challenge, author packet or scored B0–B4 run exists from this report.

The prior explicit approval **still applies** solely to this exact 10-file 26,416-byte Wave0 archive, SHA-256 `c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387`, original pin `c57556a8bf993a1d327e9197acb7b7c745071cd8`, new owner-held public recipient and one permanently excluded non-arm reviewer.

## 3. Next action without extra key-generation or generic tests

The owner retains the reported public certificate at the location printed by their successful Prepare operation, which conventionally has filename `S1_REAL_REVIEW_OWNER_PUBLIC_<recipient-id>.pem` in Downloads. This **public certificate only** may be attached to one fresh, non-Project, Unpersonalized Temporary Chat, along with:

1. The exact owner-local Wave0 review ZIP (SHA-256 above).
2. `experiments/r0_p03_navigation_probe/S1_REAL_SOURCE_STATUS_WAVE0_REVIEWER_HANDOFF_V01.md`.
3. `experiments/r0_p03_navigation_probe/s1_source_status_protected_route.py`.
4. The newly generated public certificate (never the private key).

The supplied reviewer prompt will require actual ZIP byte/manifest identity validation, bounded source-status review of all ten original files, complete private in-memory report sealing under the public cert, and only a ciphertext artifact plus nonanswer-bearing public receipt. The reviewer session must not browse public design/gold, use connected apps, reuse the author-view witness, create gold/scored tasks or reveal reviewer findings in chat text. Source-specific reasoning must remain ciphertext-only. If crypto or file access fails, hold; do not substitute plaintext.

Owner certificate path and public hash do not need to enter this conversation before proceeding if the owner can identify and attach the file directly. The owner must keep the private key and passphrase out of chat. The actual reviewer report remains for future private owner `Receive` and `Verify` operations.

## 4. Status

```text
VALIDATION_291=OWNER_REPORTED_REAL_WAVE0_RECIPIENT_PREPARED
WAVE0_EXACT_BATCH_OWNER_AUTHORIZED=YES
OWNER_PREPARE_SUCCESS=REPORTED_PASS
OWNER_ENCRYPTED_PRIVATE_KEY=REPORTED_TRUE
OWNER_CUSTODY_EXCLUSION=NOT_PROVEN
OWNER_SEPARATE_SELFTEST_OUTPUT=NOT_RELAYED
PUBLIC_CERTIFICATE_EXPORTED=OWNER_REPORTED_BY_PREPARE_SUCCESS
PUBLIC_CERTIFICATE_PATH_HASH_AND_RECIPIENT_ID=NOT_RELAYED
ACTUAL_REVIEWER_SESSION_STARTED=NO_EVIDENCE
ACTUAL_HISTORICAL_SOURCE_DELIVERY=NO_EVIDENCE
ACTUAL_REVIEWER_PROTECTED_REPORT=NOT_CREATED_AS_FAR_AS_REPORTED
OWNER_REAL_RECEIVE_AND_VERIFY=NOT_EXECUTED_AS_FAR_AS_REPORTED
INDEPENDENT_CHALLENGER=NOT_ADMITTED
AUTHOR_SOURCE_ADMISSIONS=ZERO
S3_AUTHOR_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
