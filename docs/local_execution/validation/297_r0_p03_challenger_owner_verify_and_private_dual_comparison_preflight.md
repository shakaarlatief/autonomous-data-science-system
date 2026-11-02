# Validation 297: Second Wave0 report owner readback and private paired-comparison qualification

**Date:** 2026-11-02
**Status:** SECOND_CHALLENGER_SAVED_OWNER_VERIFY_PASS_REPORTED / FICTIONAL_DUAL_CMS_COMPARE_AND_RECOMPUTE_TESTED / REAL_PRIVATE_COMPARISON_NOT_EXECUTED
**Scope:** Preserve owner-supplied successful separate `Verify` of the second Wave0 encrypted first-pass report, and qualify a new owner-only mechanical comparison of two complete authenticated real-source review reports through source-free fictional testing, without reading actual private owner records.
**Research:** 620 and 617–619.
**Specification:** 028 (unchanged).

## 1. Material new owner observation

The owner supplied the following real owner-local PowerShell output:

```text
Passphrase for existing owner-held encrypted reviewer key:
{"actual_adversarial_challenge": "PENDING", "author_world": "WORLD_UNFROZEN", "complete_independent_source_records": 10, "independent_source_dispositions": "RESTRICTED_NOT_PRINTED", "original_reviewer_conclusions_exposed_to_challenger": false, "original_reviewer_report_opened_by_coordinator": false, "original_source_batch_bound": "PASS", "owner_independent_challenger_cms_authenticated": "PASS"}
S1_WAVE0_OWNER_INDEPENDENT_FIRST_PASS_READBACK=PASS
S1_WAVE0_CHALLENGER_OWNER_FULL_READBACK=PASS
S1_WAVE0_CHALLENGER_OWNER_RECHECK=PASS
```

This is the full **separate `Verify` action**, not the original second-session reported sealing receipt. The recorded source batch is exact, the saved ciphertext authenticated, the ten canonical challenger records complete and the first reviewer report remains unexposed to the public coordinator. The second original `Receive` log is not independently provided in this turn, so mark it **NOT_DIRECTLY_OBSERVED** rather than fabricating its success. No actual disposition labels, source paths or reviewer/challenger conclusions were printed. The absence of first-reviewer exposure remains a declared first-pass field and bounded Level B session model, not provider-level independent proof.

## 2. New code and first source-free qualification

New independent Python module:
`experiments/r0_p03_navigation_probe/s1_wave0_owner_private_compare.py`.

New owner-side PowerShell wrapper:
`scripts/r0_p03_s1_owner_wave0_private_compare.ps1`.

New invented-source tests:
`tests/unit/test_r0_p03_s1_wave0_owner_private_compare.py`.

The comparator accepts exactly the existing original-source ZIP and both original authenticated ciphertext files at their pinned SHA-256 values. It authenticates both under the existing owner key, validates each role-specific ten-record schema, compares only matching pinned source identities, and creates a **complete owner-restricted paired dossier**. Mechanical differences in proposed disposition, inspection, scoped claims, context gaps, contamination risk and rationale are retained **inside** the encrypted dossier; matching labels are not taken to prove scientific agreement. The output is a new, no-overwrite, owner-directory-only AES-256-GCM CMS file, not public plaintext, and is independently revalidated by `Verify` against a freshly recomputed complete paired dossier. It does not modify either original CMS or any public knowledge source.

The first five invented-only test cases returned **5/5 PASS**: actual synthetic AES-256-GCM encryption and decryption, ten-record pairing and private difference preservation, deterministic independent recomputation, wrong passphrase failure before output creation, input tamper failure, already-present-output refusal and private-dossier tamper rejection. These tests use **only fictional source bodies, rationales and keys** in ignored pytest scratch, not owner files. Additional integrated regressions and repository validation must be recorded separately as actually observed.

A PowerShell AST syntax check initially timed out twice through the execution bridge. A later independent invocation returned **`OWNER_COMPARE_AST=PASS`** with exit code zero. These earlier timeouts are retained as nonresults, not silently counted as failures or successful tests. The actual owner `SelfTest`/`Compare`/`Verify` have **not** been executed in this conversation. An owner-only real comparison must never be invoked by the exposed Runtime Bridge.

**Regression postflight:** First five fictional-only tests passed, followed by a focused **20/20 PASS** run of the new comparator, challenger, original protected report and original source-wave selectors, plus separately executed historical evidence, frontend expansion, capacity and eligibility mapping suites **91/91 PASS**. Total targeted coverage **111/111 PASS** across the two separately executed successful suites. A first attempted combined run timed out without an observed result and was superseded by these two bounded runs; no combined-pass timing is asserted. **Prepublication repository evidence:** An initial aggregate integrity invocation timed out with no validator result. A separate retry returned exit zero, with all six repository checks PASS and `PUBLIC_REPOSITORY_INTEGRITY=PASS`. `git diff --check` returned exit zero, with only standard Windows LF-to-CRLF advisories. The exact seven intended public-safe paths were confirmed: Research 620, Validation 297, both continuity indexes, the new private comparator Python module, new owner-only PowerShell wrapper and fictional-only tests. No private CMS, owner credentials or original-source selection manifest were added. Guarded commit and remote branch publication remain separate postflights.

## 3. Next owner-only operation and exact boundary

From the owner's **ordinary interactive** PowerShell, run:

```powershell
Set-Location 'C:\Projects_Data\autonomous-data-science-system'
& .\scripts\r0_p03_s1_owner_wave0_private_compare.ps1 -Action SelfTest

$recipientId = (Read-Host 'Enter original Wave0 owner recipient ID').Trim()
& .\scripts\r0_p03_s1_owner_wave0_private_compare.ps1 -Action Compare -RecipientId $recipientId
```

Only after `Compare=PASS`, run the separate `-Action Verify -RecipientId $recipientId`. The owner must enter the **same preexisting key passphrase** locally, not paste it into this conversation. If Compare fails after writing an output, do not overwrite or retry the creation step blindly: inspect the fixed safe HOLD and use a qualified private `Verify` path where appropriate.

The comparison and its sealed protected dossier do **not** authorize handing the first reviewer's private conclusions to the challenger. Actual next-stage materiality adjudication needs separately authorized restricted access and a genuine adversarial critique of substantial disagreements and potential common blind spots.

```text
VALIDATION_297=SECOND_CHALLENGER_VERIFY_REPORTED_PASS_AND_PRIVATE_COMPARATOR_TESTED
SECOND_CHALLENGER_OWNER_VERIFY=OWNER_REPORTED_PASS
SECOND_CHALLENGER_OWNER_RECEIVE=NOT_DIRECTLY_RELAYED
TWO_SOURCE_STATUS_REPORTS=10_EACH_AUTHENTICATED
NEW_COMPARATOR_SYNTHETIC_TESTS=5_OF_5_PASS
POWER_SHELL_COMPARE_PARSER=UNOBSERVED_AFTER_BRIDGE_TIMEOUT
REAL_OWNER_PRIVATE_COMPARISON=NOT_EXECUTED
ACTUAL_ADVERSARIAL_CHALLENGE=PENDING
SOURCE_ADMISSIONS=ZERO
S3=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
