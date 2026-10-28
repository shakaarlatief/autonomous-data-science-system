# Validation 275: Candidate Temporary Chat intake preservation and text/PNG source-free fixture integrity

**Date:** 2026-10-28
**Status:** COMPLETE_INTAKE_REPORT_PRESERVED / SOURCE_FREE_FIXTURES_LOCALLY_VERIFIED / CANDIDATE_BINARY_ROUTE_NOT_YET_TESTED
**Scope:** Preserve one user-relayed real candidate-session environment intake, distinguish observed versus reported capability, preflight new source-free mixed-modality fixtures and instructions, and establish exact expected checksums for a subsequent **same-session** receipt and interpretation comparison.
**Authority:** Local read/byte/PNG decoder tests, not evidence of independent reviewer identity, actual cross-session isolation, file upload through the separate candidate model, owner-only report custody or future author-route access denial.

## 1. Intake evidence identity

```text
UPLOADED_NAME=Geplakte tekst(20261028-135243).txt
UPLOADED_BYTES=16570
UPLOADED_SHA256=2d35452210e56e298402fad34ebe33420143f40f1029091369588052ba347d20
UPLOADED_LINE_ENDINGS=236_CRLF
UPLOADED_PHYSICAL_LINES=237
UPLOADED_TERMINAL_NEWLINE=FALSE

REPOSITORY_COPY=experiments/r0_p03_navigation_probe/reviewer_intake_evidence/20261028_a2_candidate_reviewer_environment_intake_report.txt
REPOSITORY_BYTES=16334
REPOSITORY_SHA256=610dd4025dbb5bc129e12ed1670dcae7efc0d9d66460893f9f4d9d9e466146dc
NORMALIZATION=CRLF_TO_LF_ONLY
REPOSITORY_FINAL_NEWLINE=FALSE
```

The exact owner-uploaded and line-ending-normalized variants are **different byte streams**; they must never be described as byte-identical. The complete 237-line source-free response is preserved, without a coordinator-written summary replacing it. The report returned `INTAKE_LIMITED` and actual reviewer and challenger statuses `PENDING`. Reported Temporary Chat/session environment designation and tool visibility were not independently inspected by this coordinator.

## 2. Locally generated, newly distinct synthetic fixtures

```text
TEXT_FILE=experiments/r0_p03_navigation_probe/a2_source_free_fidelity_unicode_crlf.txt
TEXT_BYTES=193
TEXT_SHA256=8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb
TEXT_CRLF_COUNT=5
TEXT_ENDS_NEWLINE=FALSE
TEXT_UTF8_DECODE=PASS
TEXT_TAB_COUNT=1

PNG_FILE=experiments/r0_p03_navigation_probe/a2_source_free_fidelity_pattern.png
PNG_BYTES=291
PNG_SHA256=fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f
PNG_DIMENSIONS=48x32
PNG_COLOR_TYPE=RGB_8_BIT
PNG_CHUNKS=IHDR_tEXt_IDAT_IEND
PNG_ALL_CHUNK_CRC=PASS
PNG_ZLIB_DECODE=PASS
PNG_PIXEL_SAMPLES=PASS
PNG_METADATA=BENIGN_COMMENT_PRESENT

BRIEF=experiments/r0_p03_navigation_probe/S1_A2_CANDIDATE_FIDELITY_PROBE_V01.md
BRIEF_BYTES=5392
BRIEF_SHA256=c00df15f79b1b734a40efa34b5fe14aed536fdedafb4acba49a77114974e384c
```

Fixture bytes, digests, CRLF preservation and PNG chunk/CRC/zlib/pixel structure were verified **locally only**. This is an objective, known expected-value reference for a **non-scored engineering capability probe**, not hidden scientific gold. The candidate has not received the fixtures, and expected digests are intentionally absent from its narrow intake brief.

## 3. Test execution

New deterministic guard:

`tests/unit/test_r0_p03_s1_a2_intake_and_fixtures.py`

Initial attempt:

```text
5 passed, 1 failed
Cause: an assertion expected non-Markdown wording 'do not prove raw-byte parity'
while the brief's actual sentence correctly said 'does *not* prove raw-byte parity'.
Repair: change only the asserted exact text; the source-free fixture bytes and
candidate instructions were unchanged.
```

Corrected command:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
--basetemp=.venv/.r0_p03_a2_fidelity_20261028b
tests/unit/test_r0_p03_s1_a2_intake_and_fixtures.py

6 passed in 0.06s
```

A subsequent precommit Git check identified `core.autocrlf=true`. Exact CRLF text bytes would not be portable without a file-specific rule. Two scoped root `.gitattributes` entries therefore mark only the new CRLF fixture `-text` and the PNG `binary`. During the first actual preview.83 guarded commit, Git's staged diff checker correctly rejected each deliberate CRLF terminator as trailing whitespace and the guarded transaction restored the index. We amended **only the exact CRLF fixture** to use `-text whitespace=cr-at-eol`, so Git recognizes the carriage return as a line-ending component rather than trailing whitespace while preserving the original 193 fixture bytes and enforcing normal checks on every other file. `git check-attr` verifies these rules; `git hash-object` on the CRLF file with versus without filters produced **identical blob identity** `be4f60e2f5504ad3e73fba52316ef27f2eb947f8`. A seventh local check guards the exact rules. Final focused test command:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
--basetemp=.venv/.r0_p03_a2_fidelity_20261028c
tests/unit/test_r0_p03_s1_a2_intake_and_fixtures.py

7 passed in 0.08s
```

These tests cover local report identity and claimed admission limits, exact UTF-8 bytes and CRLF data, PNG CRCs, compressed image pixels, mandatory capability-bounded brief semantics and strict nonpromotion of the candidate session. They do **not** test actual external attachment handling, model visual understanding, private report transfer or role independence.

## 4. Strict next observation

The next observation requires the owner to send exactly the three new source-free fixture/brief files to the previously used Temporary Chat candidate, **if that session remains available**. The owner must send no repo, source-world history, real historical files, credentials, private reviewer ledger or old scoring/gold artifacts. The prospective candidate must report its actual raw bytes/digests when independently accessible, decoded text properties and visually decoded PNG evidence with explicit incomplete/unknown indicators. We compare against the exact values above without promoting a failed or partial observation to PASS.

**No actual source transfer permission is implied.** Subsequent protected-output and neutral author-route denial tests are separate and require owner-approved exact routes, not mere repeated A1 fictional CMS success.

```text
VALIDATION_275=SOURCE_FREE_INTAKE_AND_FIXTURE_LOCAL_INTEGRITY_PASS
CANDIDATE_INTAKE=INTAKE_LIMITED_REPORTED_ONLY
SAME_SESSION_TEXT_AND_PNG_FIDELITY=PREPARED_NOT_EXECUTED
LOCAL_NEW_FOCUSED_TESTS=7_PASS
PRIVATE_REVIEWER_OUTPUT=NOT_QUALIFIED
FUTURE_AUTHOR_ROUTE_DENIAL=NOT_TESTED
REAL_REVIEWER_CHALLENGER=NOT_ADMITTED
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
WORLD_FROZEN=NO
GOLD=NONE
SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
