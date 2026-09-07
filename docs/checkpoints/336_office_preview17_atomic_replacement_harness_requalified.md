# Checkpoint 336: Office Preview.17 Atomic Replacement Harness Requalified

**Date:** 2026-09-07
**Status:** SECOND HOST ATTEMPT ROLLED BACK / ATOMIC PUBLICATION HARNESS REQUALIFIED / HOST RETRY NEXT
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 121 Office whole-file native handoff
**Scope:** Preserves the second preview.17 host publication failure, exact rollback verification, correction of the Windows atomic replacement/rollback primitives, and two successful complete requalification preflights.
**Authority:** Validation 094 contains the exact failure localization, installed-file hashes, atomic replacement correction, smoke-test coverage and requalification evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The second ordinary-host preview.17 publication attempt passed all preflight regressions and reached host confirmation, but the first existing-file replacement failed because Windows PowerShell/.NET rejected the four-argument `File.Replace` call with a null backup path. The helper caught the failure and the installed runtime was independently verified back at the exact preview.16 hashes, with all three new Office files absent and the AB-020 semantic-Git hash unchanged.

The helper now uses `File.Replace(candidateTemp, livePath, timestampedBackupPath, true)` directly, and rollback uses a separately verified rollback temp plus a real displaced-file backup path. A bounded preflight smoke test now exercises this exact atomic replacement primitive. The full no-publish preflight has passed twice after the correction.

Corrected helper SHA-256:

```text
05839717f1b09360c514d86985180b57dd029b088b1b09a0bdc129f9b54a5ee5
```

The next action is another ordinary-host `-Publish` retry. No restart should occur until the retry reports `OFFICE_FILE_LINK_PUBLICATION_RESULT=PASS` and all nine installed files are independently verified.

```text
CHECKPOINT_336 = OFFICE_PREVIEW17_ATOMIC_REPLACEMENT_HARNESS_REQUALIFIED
```
