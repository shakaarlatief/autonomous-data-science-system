# Validation 215: R0-P01 Attempt 001 owner evidence preservation and independent scoring

**Date:** 2026-10-10
**Status:** EVIDENCE BACKUP VERIFIED / FROZEN OWNER RESULT AMEND
**Research:** Research 523
**Parent:** Validation 214 / Checkpoint 858
**Scope:** Read-only independent verification of owner Attempt 001 evidence and scorer behavior after real owner execution.
**Boundary:** The private keys and passphrases are owner-only and were not inspected, supplied, copied, or operated by the model or Runtime Bridge. No harness restart, new proof, replay, repair, fixture/threshold change, or marker reset.

## Source identification

- Branch `v1-source-vault-bootstrap-resume`; HEAD and origin at `89736b2515fa80f1c21be3350e112663e1e58a92`.
- The tracked working tree was observed clean afterward.
- Original append-only public records: `%LOCALAPPDATA%\ADS-R0-P01-Owner-Evidence-001\raw-0000.json` through `raw-0024.json` (25).
- Production marker: `%LOCALAPPDATA%\ADS-R0-P01\attempt-001.started.json` exists.
- Independently copied archive: `%LOCALAPPDATA%\ADS-R0-P01-Evidence-Backup-20261010-081030`.
- The owner verified all 25 SHA-256 copy/original pairs, marker pair, parseable JSON, and contiguous snapshot sequence.
- ChatGPT independently reverified the latest exact-file original and backup hash: `A48E066ADEA499EB17E4D6240CB459DF315B91F444FDEE4F42AB880BDDC60296`.
- The frozen scorer's JSON canonical-object digest, not the raw-file hash: `7b92c9c743d14384847ec75e1da814043cda13ed593faca4c07db5e843b44faf`.

## Observed event and controls

The final raw observation records `ATTEMPT_001_STARTED_BEFORE_OWNER_SENSITIVE_SETUP` and `OWNER_RUN_INTERRUPTED`; all three recorded `integrity` booleans are false. Arm A is REALIZABLE with 12/13 security controls passing and `RECOVERY_CREDENTIAL_DRY_RUN` failing. Recovery's recorded P6 verifier result is INVALID; primary P0 and primary rotation P5 are VALID. All four A burden records have proof success true. Arm B and Arm C setup statuses are SETUP_INTERRUPTED; both remain unqualified.

Small-trial mechanical seconds:
```text
S01 5.1785007999278605
S02 130.8491039001383
S03 5.868030599784106
median 5.868030599784106
L01 5.499281600117683
```
S02 exceeds its individual 120-second gate. No qualifying infrastructure-only interruption receipt is recorded. No time adjustments are authorized.

## Scoring environment pitfall and resolution

1. First frozen score run in Runtime Bridge `readOnly` profile returned `INVALID/RESULT_IDENTITY_PROVENANCE_OR_EVIDENCE_DEFECT`.
2. A read-only tracing diagnostic localized it to `score.py` preserved verifier-result consistency (line 147 at this freeze).
3. Direct public-proof re-verification in the same restricted command environment returned False for previously recorded VALID SSH proofs.
4. The frozen SSH verifier needs Python `tempfile.TemporaryDirectory` to materialize transient **public** key/proof/statement files; an isolated temporary-directory probe in this restricted profile raised `FileNotFoundError: No usable temporary directory`. The scorer's read-only invocation was therefore not a valid qualification environment.
5. Repeating only the *derived scoring operation*, with the **same frozen score.py** and **same unchanged raw-0024.json**, under authorized `inherit`/`:workspace` command execution returned exit 0 and the canonical `AMEND` result below.
6. Subsequent independent read-only checks confirmed the original raw snapshot hash remained unchanged and repository tracked status was clean.

This environment difference is not a second owner attempt and does not alter any scored owner data.

## Authoritative derived scorer output (selected fields)

```text
classification=AMEND
reason=VIABLE_PROOF_WITHOUT_FULL_ELIGIBILITY
selected_arm=null
arms.A.realizability=REALIZABLE
arms.A.proof_viable=true
arms.A.selection_eligible=false
arms.A.median_small_mechanical_seconds=5.868030599784106
arms.A.large_mechanical_seconds=5.499281600117683
arms.B.setup_status=SETUP_INTERRUPTED
arms.B.proof_viable=false
arms.B.selection_eligible=false
arms.C.setup_status=SETUP_INTERRUPTED
arms.C.proof_viable=false
arms.C.selection_eligible=false
inventory.projected_acceptance_count=97
inventory.projected_effect_count=157
```

The control failure, S02 time-gate miss, and Arm-B incompleteness remain independent, non-overridden observations. The implementation file bytes and frozen security/timing rules were not changed. This validation report is a derived, non-secret record; it must not be used to replace the raw evidence.

```text
VALIDATION_215=R0_P01_OWNER_EVIDENCE_AND_SCORE_CHECKED
ORIGINAL_AND_BACKUP_FINAL_HASH_MATCH=true
FROZEN_SCORE_CLASSIFICATION=AMEND
R0_P01_ATTEMPT_001_RETRY_ALLOWED=false
```
