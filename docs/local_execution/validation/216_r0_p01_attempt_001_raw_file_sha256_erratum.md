# Validation 216: R0-P01 Attempt 001 final raw SHA-256 erratum

**Date:** 2026-10-10
**Status:** VERIFIED NON-SECRET HISTORICAL TRANSCRIPTION ERRATUM
**Scope:** Verify original and backup raw-0024.json exact file hashes, resolve conflicting historical documentation, and preserve every earlier file unchanged.
**Parent:** Research 523 / Validation 215 / Checkpoint 859 / MC-0030 Message 018
**Authority:** Correction of an evidence citation only, not scoring, credential operations, a new trial or replacement evidence.

## Independent read-only checks

Codexless Runtime Bridge executed SHA-256 over the existing *non-secret* public evidence file and its separately preserved backup:

```text
original: %LOCALAPPDATA%\ADS-R0-P01-Owner-Evidence-001\raw-0024.json
backup:   %LOCALAPPDATA%\ADS-R0-P01-Evidence-Backup-20261010-081030\raw-0024.json
exact-file SHA256, both:
A48E066ADEA499EB17E4D6240CB459DF315B91F444FDEE4F42AB880BDDC60296
MATCH=true
```

Repository search identifies **two** incorrect historical exact-file digests and one correct record:

| File | Last digits | Verdict |
|---|---|---|
| Research 523 | `...AB880BDCC60296` | Incorrect hex position 58: `c` should be `d` |
| Checkpoint 859 | `...AB880BDCC60296` | Same error |
| Validation 215 | `...AB880BDDC60296` | Correct |

Claude Message 018 identified the Research 523 / Validation 215 discrepancy; independent repository search additionally found Checkpoint 859. **Do not edit the historical records.** This validation is the explicit appended erratum.

The frozen scorer's different `raw_sha256=7b92c9c743d14384847ec75e1da814043cda13ed593faca4c07db5e843b44faf` is a canonical JSON object digest, **not** the exact raw-file-byte SHA-256. Keep both byte bases separately labelled.

No snapshot, attempt marker, key, backup, frozen implementation, score or observed P01 result was modified. For a successor, produce hashes mechanically in evidence records and independently recompute instead of manually transcribing.

```text
VALIDATION_216=R0_P01_RAW_FILE_HASH_ERRATUM
RAW_FILE_SHA256_MATCH=true
RESEARCH_523_AND_CHECKPOINT_859_DIGIT_58=INCORRECT
VALIDATION_215=CORRECT
OWNER_EVIDENCE_MUTATION=NONE
```
