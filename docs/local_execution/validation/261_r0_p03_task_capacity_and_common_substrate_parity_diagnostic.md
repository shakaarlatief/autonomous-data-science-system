# Validation 261: R0-P03 task-capacity and common-substrate diagnostic

**Date:** 2026-10-16
**Status:** MECHANICAL_CHECKS_VERIFIED / SEMANTIC_TASK_CAPACITY_AND_RUNTIME_PARITY_NOT_QUALIFIED
**Scope:** Verify exact-Git diagnostic receipts and conservative synthetic parity/authority guards without selecting tasks, generating references or executing arms.
**Parent:** Research 577; Research 513/559/560/561/576; Checkpoint 898.
**Baseline:** Clean branch `v1-source-vault-bootstrap-resume` at `912d6709e8f83591c0a5446531a8b0e38a59007d`; native Desktop Codex/codex-01 is exposed implementer/verifier, ChatGPT/chatgpt-39 owns independent acceptance.

## Execution and expected interpretation

The diagnostic retains source pin `c57556a8bf993a1d327e9197acb7b7c745071cd8`, verifies blob bytes and all eleven existing citation witnesses, and binds design JSONs at the published engineering baseline. A citation mismatch is a mechanical failure; exact matches do not prove authority, coverage or answerability. Equality and known-signal guards reject unequal/missing common capabilities, false authority, inferred J2, stale checkpoint promotion and common B2 repetitions. Synthetic positive cases establish only guard behavior. Unknown semantic encodings, independent source meaning and real runtime parity remain unqualified.

Saved receipt: `experiments/r0_p03_navigation_probe/task_capacity_parity_diagnostic_candidate.json`. Reproduce with:

```text
.venv/Scripts/python.exe -B -m experiments.r0_p03_navigation_probe.role_frame_candidate --capacity-parity
```

Actual findings: all 36 events, 74 blob-bound source-header observations, 21 events with recognized external-file citations; category hinted/cited counts **21/14, 7/6, 12/8, 17/12**; matching cardinality ceiling 12; independently answerable counts null. All 10+1 specimen citations match; required carrier fields incomplete, synthetic J2 only, stale derived 564 versus historical routing 895, runtime parity unqualified. These are engineering diagnostics, not tasks/gold or a fixture. Research 577 explains unresolved source paths and neighborhood limits.

## Executable checks

Baseline four-module run: **46 passed in 32.89s**. Final focused command:

```text
.venv/Scripts/python.exe -B -m pytest -q -p no:cacheprovider
 tests/unit/test_r0_p03_capacity_parity_diagnostic.py
 tests/unit/test_r0_p03_role_frame_candidate.py
 tests/unit/test_r0_p03_source_census.py
 tests/unit/test_r0_p03_independent_reference_intake.py
 tests/unit/test_r0_p03_source_only_capsule.py
 --basetemp=.venv/.p03-capacity-verification-fixed
```

The first combined run found one real parser defect: a bare root-directory token such as `tools/` was omitted. The path grammar was corrected to retain it as an unexpanded directory, and the saved receipt regenerated. Ambiguous targets also remain unresolved rather than entering source-neighborhood counts. No task/corpus or source pin was changed. That run was **1 failed / 89 passed**; final results follow in postflight.

New tests cover deterministic saved receipts, fixed pins, all-event coverage, overlap-only ceilings, literal lifecycle headers, missing/ambiguous/directory links, outside-frame paths, incomplete closures, tampered quotes and Git batch corruption. Synthetic tests cover equal B0–B3 with optional B4, every missing B0 capability, equal-but-contaminated views, false governing promotion of proposal/implementation/schema/test/derived roles, inferred J2, stale versus digest-unverified matching checkpoints, B2 common/reverse duplication and semantically unqualified novel links. No model or reviewer inference.

## Final postflight

Corrected combined run: **90 passed in 32.77s** (44 new diagnostic cases and 46 existing regressions), no warnings. Direct CLI output parsed equal to the saved JSON receipt. No semantic/runtime or scored PASS is implied.

```text
.venv/Scripts/python.exe -B scripts/check_repository_integrity.py --checked-branch v1-source-vault-bootstrap-resume
```

All **six components PASS**, `PUBLIC_REPOSITORY_INTEGRITY=PASS`. `git diff --check` PASS; new files separately checked for trailing whitespace/final newline. Git reports expected LF-to-CRLF normalization notices, not whitespace errors. **19 preservation assertions PASS**: exact five modified/four new files, unchanged published HEAD/branch/empty index, prior exposure/notes/THREAD history, phase/participants/ChatGPT ownership, live routing and Checkpoint 898, all three historical design JSONs and original gate values. No ADS staging, commit or push.

SHA-256 receipts (UTF-8 LF working files):

| File | SHA-256 |
| --- | --- |
| `experiments/r0_p03_navigation_probe/role_frame_candidate.py` | `028c52087469719805871a03f654280dac9cf04d0a37ef3e20d6de4bdded49a1` |
| `experiments/r0_p03_navigation_probe/task_capacity_parity_diagnostic_candidate.json` | `bc6ca322c34bfefe5fe31b35a0ebb046354724c31f692fb99b00855bc2636400` |
| `tests/unit/test_r0_p03_capacity_parity_diagnostic.py` | `ea8a0d0767228b75d2094b81878134aa54fff7fc5cf0ff9c142fd7ed5730216f` |

Hashes bind this uncommitted engineering result; they do not freeze a scored fixture or hidden reference. No new model dispatch, gold custody, security trial, legacy adjudication or private mutation occurred. Next independent acceptance/publication is ChatGPT's responsibility.
