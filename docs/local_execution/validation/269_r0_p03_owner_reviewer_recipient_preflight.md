# Validation 269: Owner recipient preflight for fictional reviewer-report CMS

**Date:** 2026-10-21
**Status:** SOURCE_FREE_POWERSHELL_INTEROPERABILITY_PASS / OWNER_DESKTOP_CUSTODY_UNTESTED / REAL_SOURCE_REVIEW_HOLD
**Scope:** Validate the newly dedicated fictional reviewer CMS recipient without invoking its owner-only Prepare, Receive or Verify actions. Preserve all earlier reference and S1 fake-custody regressions.
**Authority:** Observed test evidence only. Does not authorize owner account/file mutations, confidential actual source review, reference gold or scoring.

## 1. Examined and newly added artifacts

```text
New owner-only recipient:
  scripts/r0_p03_fake_reviewer_recipient.ps1

New isolated test suite:
  tests/unit/test_r0_p03_fake_reviewer_recipient.py

Existing counterpart:
  experiments/r0_p03_navigation_probe/s1_fake_reviewer_report_handoff.py

Existing old recipient, unchanged:
  scripts/r0_p03_fake_public_recipient.ps1

Fictional only:
  3 fixed invented source IDs, SHA-256 hashes, dispositions and note codes

Owner key location:
  NOT ACCESSED
Owner temporary folder:
  NOT CREATED
Real source or historical gold:
  NONE
```

The new script uses a separate filename and private-folder namespace and does not share its packet format or write destinations with the old 9+12-case owner fake recipient.

## 2. Executed tests, failures and corrections

**First direct PowerShell SelfTest** completed with:

```text
S1_FAKE_REVIEWER_RECIPIENT_SELFTEST=PASS
S1_OWNER_ACCOUNT_AND_FILES_UNTOUCHED=TRUE
```

**First isolated interoperability test run:** the Python test harness constructed a large PowerShell `-EncodedCommand` containing the entire function prelude. This exceeded Windows command-line argument limits (WinError 206). Test harness changed to write only fictional test fragments to ignored `.venv` temporary `.ps1` files and execute via `-File`. No owner-only action was called.

**Second focused run:** 27 tests passed after that correction.

**Final focused run** added actual Python-sender-to-PowerShell-recipient AES-256-GCM authenticated decrypt and complete report check; one tampered ciphertext is denied. Test command:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.s1_fake_reviewer_owner_20261021c
  tests/unit/test_r0_p03_fake_reviewer_recipient.py
  tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py

28 passed in 9.90s
```

**Full relevant regression run:** eight source-free modules, including new owner parser, new fake sender, old fixed fake recipient and reference CMS, mock role, journal/transport and fake custody tests:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.s1_fake_reviewer_owner_20261021d
  tests/unit/test_r0_p03_fake_reviewer_recipient.py
  tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py
  tests/unit/test_r0_p03_temporary_author_fake_cms_sender.py
  tests/unit/test_r0_p03_synthetic_cms_recipient_preflight.py
  tests/unit/test_r0_p03_s1_role_boundary_synthetic.py
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py
  tests/unit/test_r0_p03_fake_public_recipient.py

96 passed in 14.27s
```

## 3. Evidence boundaries

| Check | Observed qualification | Not qualified |
| --- | --- | --- |
| PowerShell 5.1 syntax, in-memory fake schema | PASS, exact marker/keys, three invented hashes and strict status/notes; missing source HOLD | Real source role or representation judgment |
| Cross-language report serialization | Python canonical fake JSON accepted by PowerShell | Arbitrary real reviewer narrative |
| Negative reports | Missing/duplicate/nonfictional source, wrong SHA, wrong scope, invalid status/notes/boolean rejected | Exhaustive protection against all malformed JSON or real semantic contamination |
| Python CMS to PowerShell | Actual throwaway RSA/OpenSSL AES-256-GCM decrypt and full report check PASS | Owner-held private key/owner API route |
| Modified CMS | Authentication failure yields only fixed FAIL in isolated test | Real confidential decrypted report backup/log lifecycle |
| Windows key generation helper | Native stderr-drained disposable fake key/cert creation in ignored test scratch PASS | Owner LocalAppData DACL and real desktop process |
| No-overwrite/identity/ACL guards | Present in new owner script, reviewed statically; Prepare/Receive/Verify unexecuted | Actual Windows ACL isolation, directory creation, recovery or user approval |
| Old 9+12 recipient | Source unchanged, earlier test suite still PASS | Production reference custody or approved owner secret reuse |
| Consolidated regressions | 96 PASS | New Temporary Chat/file-transfer boundary |

Tests ran using the authorized Runtime Bridge command route. The scripts and test fixtures contain only fictional source names and fake notes; no protected historic R0-P03 source, actual old gold, owner key, owner recipient directory or external reviewer connector was read.

## 4. Next bounded owner decision

Before any actual `Prepare` execution, the owner must expressly approve creation of a fresh disposable **fictional-only** recipient directory under their LocalAppData and export of a **public** certificate to Downloads. The subsequent independent Temporary Chat receives only the sender script and public certificate, never owner key/folder, ADS historical source or this coordination transcript. The owner may then execute Receive/Verify after downloading the exact fake CMS and checking the public digest. Do not rerun uncertain partial operations without inspecting the state.

A clean end-to-end user-mediated trial would establish a narrow fictional transfer/recovery result. It would not authorize real source review or freeze an author world.

```text
VALIDATION_269=SOURCE_FREE_OWNER_RECIPIENT_PREFLIGHT_PASS
FOCUSED_UNIT_TESTS=28_PASS
CONSOLIDATED_S1_AND_OLD_RECIPIENT_TESTS=96_PASS
WINERROR_206=TEST_HARNESS_REPAIRED
REAL_OWNER_PREPARE_RECEIVE_VERIFY=NOT_EXECUTED
REAL_TEMPORARY_CHAT_REPORT_TRANSFER=NOT_EXECUTED
REAL_REVIEWER_CUSTODY=UNQUALIFIED
SOURCE_ADMISSIONS=ZERO
SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
