# Validation 285: Actual test-only author-view intake receipt and A2-R07 denial hold

**Date:** 2026-10-29
**Status:** SOURCE_FREE_INTAKE_REPORT_PRESERVED_AND_FINGERPRINT_MATCHED / LIVE_AUTHOR_ACCESS_DENIAL_NOT_TESTED
**Scope:** Record direct verification of owner-uploaded separate-session report bytes, complete report preservation, exact match to previously published source-free public brief and deliberately unpromoted role/tool access claims.
**Basis:** Research 614–615, Validation 283–284, Checkpoint 898, Specification 028.

## Source and receipt

The owner uploaded one complete, UTF-8 text export, **Geplakte tekst(20261029-094055).txt**. The exposed coordinator independently read the **exact mounted upload bytes** using the conversation file runtime, not through Codexless or by searching private repositories.

```text
ORIGINAL_BYTE_LENGTH=10497
ORIGINAL_SHA256=1f0ef2067acf9fb7e311045b2f1061acf26d103597d4f452b09e5966a2a25bf4
ORIGINAL_CRLF_COUNT=152
ORIGINAL_LINES=153
ORIGINAL_FINAL_NEWLINE=NO
LF_NORMALIZED_BYTE_LENGTH=10345
LF_NORMALIZED_SHA256=2b47c5ffe8d0a3000f0a6175023b7e2e7df14aeafcc2bf355a9108a8025a3698
NORMALIZATION=CRLF_TO_LF_ONLY
```

The **full report**, not an abstract or fabricated transcript, is preserved at `experiments/r0_p03_navigation_probe/author_view_intake_evidence/20261029_a2_test_only_author_view_intake_report.txt`. A read-only SHA-256 of the newly written repository copy matches the expected LF-normalized digest. No byte-identical-upload claim is made about this LF-normalized repository file; the original uploaded CRLF byte hash remains the independent source identifier.

## Cross-boundary comparison

The report says the test-only session locally used Python to read the attached `S1_A2_FUTURE_AUTHOR_VIEW_ROUTE_INTAKE_V01.md`, observed exactly **5,684 bytes**, SHA-256 `090ccfc8e6a78fa1bb841deb4e8c074ea65446312da20af75a8bcd5cbb49b67e`, decoded valid UTF-8 and observed `ADS_A2_AUTHOR_VIEW_INTAKE_PUBLIC_V01`. Both raw-file size and digest match the coordinator's independently known, published preparation artifact. Reported actor execution remains **owner-relayed**; the exposed coordinator did **not** directly observe Python inside the separate Temporary Chat.

Exact safe report conclusion:

```text
A2_R07_TEST_ACTOR=NON_AUTHOR_SOURCE_FREE
A2_R07_PUBLIC_BRIEF_VISIBLE=YES
A2_R07_AUTHOR_VIEW_INTAKE=INTAKE_REPORTED_ONLY
A2_R07_OWNER_RESTRICTED_TARGET_REQUESTED=NO
A2_R07_DIRECT_AUTHOR_ACCESS_DENIAL=NOT_TESTED
A2_R07_ACTUAL_PRIMARY_AUTHOR_ADMITTED=NO
A2_R07_HISTORICAL_SOURCES_DELIVERED=ZERO
A2_R07_SCORING=NOT_STARTED
```

The report separately says `NEGATIVE_ACCESS_TEST_NOT_INSTRUMENTABLE`; no actual known-existing owner-controlled synthetic target, owner authorization for a negative test or direct denied-read result was present. The owner has not yet independently reported the Temporary Chat/Project/connected-app UI controls. The report's visible-tool inventory, lack of unexpected exposure, Temporary Chat label and connected-app availability are **not** an owner-observed UI or provider-signed denial attestation.

## Qualified engineering finding

**Yes, bounded:** The owner-relayed positive attachment receipt describes a tool-enabled separate test-only candidate that apparently read the intended exact source-free brief; precommitted digest agreement strongly supports that specific permitted-byte transfer.

**No, explicitly held:** Reviewer-only custody confidentiality; actual future blind-author's inability to access owner-controlled records, history, web or alternate connected tools; provider/model independence; separately authorized reviewer/challenger identity; real source eligibility; S3 source-world freeze and scored B0–B4 comparisons.

The immediate next evidence should be **owner-confirmed actual UI/tool configuration**, followed by a route-specific denial witness if genuinely implementable, or a separately adjudicated restricted packet-only threat model if not. No extra fictional CMS, credential rotation, real source transfer or new actor admission was performed.

**Focused verification completed:** The new `tests/unit/test_r0_p03_a2_test_only_author_view_intake_receipt.py` ran in ignored isolated pytest scratch and returned **3 passed in 0.03 seconds**. It checks the complete LF-normalized 10,345-byte report SHA-256 and 153-line record, the published 5,684-byte public intake SHA-256, exact reported positive-read markers, and the explicit `NOT_TESTED`/`NEGATIVE_ACCESS_TEST_NOT_INSTRUMENTABLE` nonpromotion. It tests only public synthetic evidence and cannot establish a real denied read. **Aggregate repository-integrity check: PASS**, including family-aware contracts, Project Knowledge, checkpoint metadata, Knowledge Map, model collaboration and current routing. `git diff --check` exited successfully with no whitespace violation (only the existing Windows LF-to-CRLF advisory). The exact working-tree change list is the six declared source-free continuity/receipt files. Guarded Git commit and push are separate subsequent publication gates and are not claimed until observed.

```text
VALIDATION_285=SOURCE_FREE_OWNER_RELAYED_AUTHOR_VIEW_INTAKE_RECONCILED
ORIGINAL_REPORT_READ_BY_COORDINATOR=YES
REPOSITORY_NORMALIZED_REPORT_PRESERVED=YES
PREPARED_AUTHOR_BRIEF_SHA256_COMPARISON=MATCH
ACTUAL_EXTERNAL_ACTOR_TOOL_EXECUTION=DIRECTLY_UNOBSERVED
ACTUAL_NEGATIVE_ACCESS_DENIAL=NOT_TESTED
OWNER_UI_MODE_AND_CONNECTIONS=UNVERIFIED
REAL_HISTORICAL_SOURCE_DELIVERY=ZERO
AUTHOR_WORLD=WORLD_UNFROZEN
B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```