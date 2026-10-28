# Validation 276: Candidate text/PNG fidelity report reconciled against original source-free fixtures

**Date:** 2026-10-28
**Status:** ORIGINAL_FIXTURES_AND_CANDIDATE_REPORTED_VALUES_MATCH / EXTERNAL_TOOL_EXECUTION_REPORTED_ONLY / ACTUAL_ROLE_AND_CUSTODY_NOT_QUALIFIED
**Scope:** Check exact original-source fixture bytes and independent PNG pixel counts against the user-relayed candidate-session outcome `TEXT_AND_PNG_BYTES_AND_RENDER_VERIFIED`, while preserving source provenance and rejecting unsupported reviewer/custody promotions.
**Basis:** Research 609–610 and Validation 275; source-free generated fixtures with two exact `.gitattributes` byte-preservation rules. Scientific Checkpoint 898 and Specification 028 are unchanged.

## 1. Source-free evidence reference

The candidate's full source-free response is visible as user-pasted text in the conversation, with normalized, table-repaired transcription saved to:

`experiments/r0_p03_navigation_probe/reviewer_intake_evidence/20261028_a2_candidate_fidelity_owner_relayed_report.md`

**Important:** The repository transcription is not a byte-for-byte export from the candidate Temporary Chat and cannot be used to claim original upstream message integrity or independently observed tool calls. Its SHA-256 is an integrity check for the **transcription itself**, not a cryptographic authenticity credential.

The prior environment-intake report `INTAKE_LIMITED` is unchanged. The candidate's raw-file verification assertions and tool invocation list are reported, not independently audited.

## 2. Exact input evidence independently checked

```text
BRIEF_BYTES=5392
BRIEF_SHA256=c00df15f79b1b734a40efa34b5fe14aed536fdedafb4acba49a77114974e384c
TEXT_BYTES=193
TEXT_SHA256=8af9f2f5ea35071e1e8db50e0f467188a63b0a2ad390e5a3eba3853b109603fb
PNG_BYTES=291
PNG_SHA256=fb598054eef1c3200b13967887f225d41acfd88059c6a335f9cb4655fa3cb05f

TEXT_CRLF=5
TEXT_TAB=1
TEXT_TRAILING_NEWLINE=NO
BRIEF_CRLF=0
BRIEF_LF=50
BRIEF_TRAILING_NEWLINE=YES

PNG_DIMENSIONS=48x32
PNG_COLOR_MODE=RGB
PNG_PIXEL_RED_219_61_47=651
PNG_PIXEL_BLUE_45_96_207=641
PNG_PIXEL_GREEN_42_178_86=212
PNG_PIXEL_PALE_248_234_202=32
PNG_PIXELS_TOTAL=1536
PNG_METADATA_COMMENT=S1 A2 source-free integrity probe
PNG_CHUNKS=IHDR_tEXt_IDAT_IEND
```

Every value above matches the corresponding value explicitly reported by the candidate. The comparison is independent of its own inability to consult pre-upload hashes, since the local original fixtures were separately recorded before the candidate ran.

## 3. Deterministic checks and status

`tests/unit/test_r0_p03_s1_a2_candidate_report_reconciliation.py` verifies all three original digests, the reported normalized transcript values, actual PNG pixel-color counts, text-file line endings, claimed limitation on upstream pre-upload identity, and nonpromotion of the source-free test to real reviewer/challenger independence, private custody or historical source admission.

This is a **mechanical** consistency check. The same model instance observing a user paste plus locally computed originals cannot establish that the candidate did in fact invoke `hashlib` or Pillow, only that its reported observations are consistent with independent source-free evidence.

The original six-plus-one Validation 275 test suite remains separately valid and must continue to pass in the combined focused suite. Each of the three attachments is harmless. No protected input or file access was required.

## 4. Publication diagnostics and independent failure boundary

The first combined focused run passed 42/42 and the public repository-integrity gate passed after adding missing Research 610 Scope metadata. Repeated guarded semantic Git commits had previously returned timeouts with empty index and unchanged HEAD. A smaller five-path guarded fixture commit similarly failed internally and was reconciled as not committed. A harmless **direct command-route dry-run** `git add -n` was separately denied at `.git/index.lock` by Codex sandbox permissions in approximately 0.06 seconds. This direct command-route denial is **not evidence that the bounded host-Git route failed in the same way**; it is evidence against bypassing it with raw Git. The guarded operation's exact root cause remains undetermined. Publication is not claimed until remote verification succeeds. Preserve all local changes and avoid ACL/policy widening.

## 5. Qualification boundary

```text
VALIDATION_276=A2_SOURCE_FREE_CANDIDATE_REPORTED_VALUES_MATCH_ORIGINALS
A2_R03_R04_CANDIDATE_TEXT_AND_PNG=REPORTED_MATCH
A2_ATTACHMENT_PREUPLOAD_IDENTITY=COORDINATOR_ORIGINAL_DIGEST_COMPARISON_MATCH
A2_CANDIDATE_TOOL_EXECUTION=SELF_REPORTED_NOT_INDEPENDENTLY_AUDITED
A2_REAL_SOURCE_FORMAT_FIDELITY=NOT_QUALIFIED
A2_R05_PRIVATE_REVIEWER_RECIPIENT=NOT_QUALIFIED
A2_R06_SEPARATE_CHALLENGER=NOT_QUALIFIED
A2_R07_PRIMARY_AUTHOR_ACCESS_DENIAL=NOT_TESTED
ACTUAL_REVIEWER_ADMISSION=NO
REAL_SOURCE_RECORDS_DELIVERED=ZERO
SOURCE_ADMISSIONS=ZERO
WORLD_FROZEN=NO
GOLD=NONE
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
