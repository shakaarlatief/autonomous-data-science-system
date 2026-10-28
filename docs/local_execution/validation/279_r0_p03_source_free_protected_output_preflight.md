# Validation 279: Source-free S1 A2 candidate protected-output schema and encrypted-key preflight

**Date:** 2026-10-28
**Status:** LOCAL_SOURCE_FREE_CRYPTOGRAPHIC_AND_SCHEMA_PREFLIGHT_PASS / EXTERNAL_OWNER_CANDIDATE_ROUTE_NOT_TESTED
**Scope:** Qualify the local executable and tests for a new actual-candidate-to-owner **source-free** protected-output test, without granting real-source access or creating actual owner credentials.
**Basis:** Research 609–612, Validation 275–278; actor-admission gate A2-R01–R08; Checkpoint 898 and Specification 028 unchanged.

## Source and byte identity

```text
CODE=experiments/r0_p03_navigation_probe/s1_a2_candidate_protected_output_probe.py
BRIEF=experiments/r0_p03_navigation_probe/S1_A2_CANDIDATE_PROTECTED_OUTPUT_ROUTE_PROBE_V01.md
TEST=tests/unit/test_r0_p03_s1_a2_candidate_protected_output_probe.py
REAL_SOURCE_INPUTS=NONE
OWNER_REAL_PRIVATE_KEY_CREATED=NO
CANDIDATE_TEMPORARY_CHAT_TEST_EXECUTED=NO
```

The standalone sender rejects any real historical source input. Its two required inputs must match exact prior source-free text/PNG SHA-256 identities; extra records are invented missing/held entries only. It never outputs the private report plaintext to a file, channel or receipt, but uses authenticated OpenSSL CMS and fixed public-safe receipt fields.

The owner-side full-report reader is distinct, requires the actual private key and its interactive passphrase, and rejects noninteractive owner input at the CLI. No key from earlier fake CMS trials is imported or reused.

## Local tests and corrections

Focused source-free `pytest`:

```text
tests/unit/test_r0_p03_s1_a2_candidate_protected_output_probe.py
26 passed
```

The tests cover 0, 1, 2 or 3 missing optional entries; two mandatory exact-source records; fresh private canaries; duplicate/unknown/incorrect identity fields; incorrect representation and bytes; forbidden assertions of reviewer independence or historical review; noncanonical JSON; complete authenticated RSA/CMS AES-256-GCM encryption and private-key readback; wrong ciphertext hash, duplicate output, wrong encrypted-key passphrase and modified ciphertext authentication denial.

First run: two failed assertions due to overly broad test expectations (a legitimate optional-record reduction and a safe counter name). Both were narrowed with no report-contract weakening.

Second credential test: Git OpenSSL's `req` rejected an explicit `-aes256` option. The test fixture was corrected to create a password-encrypted RSA key using `-passout` and no `-nodes`, while retaining actual encrypted-key CMS recovery. The test-only passphrase is public and disposable, **not** an owner secret or candidate key. All tests then passed.

The owner key is **not** generated in these tests. Automated test-only RSA keys and CMS ciphertext remain inside ignored `.venv` scratch; no protected owner file or credential location was opened.

## Actual A2 qualification limits

This local test proves compatibility and rejection behavior of the new fixture-bound schema and cryptographic code only. It does not establish that the candidate can execute OpenSSL, that the candidate can seal to the actual approved recipient, that the owner has recovered that candidate's complete ciphertext, that the key is exclusive from project-attached tools, or that the future author cannot access the record. Even strong password-encryption at rest does not prove same-Windows-SID process isolation or prevent owner terminal compromise. Those are distinct **actual environment** properties, not a reason to promote a local synthetic test to actor admission.

```text
VALIDATION_279=SOURCE_FREE_VARIABLE_REPORT_AND_ENCRYPTED_KEY_PREFLIGHT_PASS
LOCAL_PROTECTED_OUTPUT_TESTS=26_PASS
OWNER_APPROVED_RECIPIENT=NOT_SELECTED
OWNER_PRIVATE_CUSTODY_WITNESS=NOT_EXECUTED
CANDIDATE_PROTECTED_OUTPUT=NOT_EXECUTED
FUTURE_AUTHOR_INTERFACE_DENIAL=NOT_TESTED
REVIEWER_CHALLENGER_ADMISSION=NONE
REAL_HISTORICAL_SOURCE_BYTES_DELIVERED=ZERO
S3_AUTHOR_WORLD=UNFROZEN
S4_GOLD=NONE
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
