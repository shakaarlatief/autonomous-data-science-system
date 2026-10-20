# Validation 268: S1 fictional reviewer-report CMS schema and protected-receipt mechanics

**Date:** 2026-10-20
**Status:** LOCAL_FAKE_REVIEWER_REPORT_HANDOFF_MECHANICS_PASS / OWNER_CROSS_SESSION_TRIAL_NOT_EXECUTED
**Scope:** Verify the bounded report sender/readback created under Research 601 while retaining old fixed-reference CMS and fake-recipient regressions. No actual reviewer, owner protected store, real source or scored task.
**Basis:** Research 589/594/600–601, the exact source-free `s1_fake_reviewer_report_handoff.py` and its tests. Checkpoint 898/Specification 028 remain unchanged.

## 1. Actual tested source and command

```text
New implementation:
  experiments/r0_p03_navigation_probe/s1_fake_reviewer_report_handoff.py
New tests:
  tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py
Existing regression tests:
  tests/unit/test_r0_p03_temporary_author_fake_cms_sender.py
  tests/unit/test_r0_p03_synthetic_cms_recipient_preflight.py

Final executed command:
  .venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_fake_reviewer_20261020b
  tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py
  tests/unit/test_r0_p03_temporary_author_fake_cms_sender.py
  tests/unit/test_r0_p03_synthetic_cms_recipient_preflight.py

Final result: 19 passed in 2.88s
```

A later consolidated S1 regression execution included the new fake reviewer sender plus the prior fictional actor, journal, transport, fake-custody and CMS test modules. It returned **75 passed in 2.51s** with no failures:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
  --basetemp=.venv/.r0_p03_s1_fake_reviewer_20261020c
  tests/unit/test_r0_p03_s1_fake_reviewer_report_handoff.py
  tests/unit/test_r0_p03_temporary_author_fake_cms_sender.py
  tests/unit/test_r0_p03_synthetic_cms_recipient_preflight.py
  tests/unit/test_r0_p03_s1_role_boundary_synthetic.py
  tests/unit/test_r0_p03_s1_transport_custody_synthetic.py
  tests/unit/test_r0_p03_synthetic_custody_evidence_candidate.py
```

The first execution returned `18 passed, 1 failed`, solely in the new subprocess CLI sender because a bare `openssl` was not discoverable from its Windows PATH. The prior qualified Git-for-Windows OpenSSL location was added as an **explicit Windows-only fallback**; the script still fails closed if both lookups fail. The identical command with a new isolated pytest basetemp passed. No unrelated old code, owner keys, Windows ACLs or runtime service configuration were modified.

## 2. Positive and adversarial observations

| Test area | Result | Correct evidence scope |
| --- | --- | --- |
| Exact fabricated source roster | 3 fixed fake IDs, predetermined fake hashes, complete accounting | Not a complete historical review |
| Variable fake reviewer dispositions | HOLD/missing and unsupported component accepted only under typed/incomplete-state constraints | Not a semantic source-status oracle |
| Nonfictional/extra source fields and private notes | Rejected by closed fake-only schema and note vocabulary | Cannot process genuine arbitrary reviewer notes by design |
| Strict boolean evidence | Truthy strings and numeric substitutes rejected | Not independently observed identity |
| Public receipt safety | Rejects source IDs, private notes, source-status counts, invalid marker and invalid digest | Only a narrow fixed schema; not a general publication-history proof |
| Sender and recipient CLI | Separate subprocess runs, OpenSSL authenticated CMS encryption/decryption and full canonical fake JSON readback PASS | Both processes ran in the same local environment; no owner recipient yet |
| Tampered ciphertext/wrong digest | Failed owner fake readback; cannot return provisional decrypt stdout | No claim of permanent confidential encrypted evidence custody |
| Unchanged old CMS behavior | Existing fixed 9+12 sender and fake-recipient test suite still PASS | No new author/reference/gold acceptance |
| Public-only certificate | Private-key-looking PEM rejected; ciphertext output refuses overwrite | Does not establish production key-management isolation |

A disposable throwaway RSA key and self-signed public cert were created in ignored `.venv` test scratch by pytest and were not sent to a separate chat, owner or provider. The new CLI sender reads a bounded in-memory/stdin fictional report; the file output is only ciphertext. The separate CLI `verify` prints a fixed PASS/FAIL line and no decrypted fake note. The hash-only public receipt has no per-record disposition or private rationale.

## 3. Critical untested boundary

This report **does not** establish actual owner-controlled restricted storage, independent reviewer/private-output confidentiality, remote Temporary Chat tool context or trust, a real independent source-status challenger, actual producer to owner packet transfer, durable key/payload recovery under a separate owner process, model provider retention behavior, final author packet exclusion or real source safety.

The new fabricated report differs from the old fixed 9+12 packet, so the old strict PowerShell owner recipient **must not** be invoked as a reader for the new format without an independently validated new owner-side workflow. The code's `verify` is a mechanics check, not an approved actual owner-custody adapter.

## 4. Stop and next test

The next meaningful test, only after explicitly choosing an owner-controlled *fictional* recipient/output location and session/tool route, is **one** real independent Temporary Chat to owner encrypted reviewer-shaped report handoff with verified full readback and a safe coordinator receipt. Such a result would qualify that bounded transport property only. Further local fake CMS tests do not substitute for owner-mediated output custody.

```text
VALIDATION_268=LOCAL_FAKE_CMS_REVIEWER_REPORT_MECHANICS_PASS
FOCUSED_CMS_REGRESSION_TESTS=19_PASS
CONSOLIDATED_S1_REGRESSION_TESTS=75_PASS
FIRST_RUN_FAILURE=WINDOWS_OPENSSL_CLI_PATH_CORRECTED
ACTUAL_SEPARATE_REVIEWER_SESSION=NOT_USED
REAL_OWNER_REVIEWER_CUSTODY=NOT_APPROVED_OR_TESTED
REAL_SOURCE_RECORDS_READ=ZERO
REAL_SOURCE_ADMISSION=ZERO
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
