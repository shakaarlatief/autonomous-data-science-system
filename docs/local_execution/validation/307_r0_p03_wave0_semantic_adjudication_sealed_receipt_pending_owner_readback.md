# Validation 307: Real Wave0 semantic adjudicator sealed-receipt, pending owner readback

**Date:** 2026-11-09
**Status:** SEPARATE_NON_ARM_ADJUDICATOR_REPORTED_TEN_SOURCE_CMS / AUTHENTICATED_OWNER_READBACK_PENDING / OWNER_SCIENTIFIC_QUALIFICATION_PENDING
**Research:** 623 and 622. **Prior validation:** 304–306.
**Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.
**Authority:** Safe receipt relayed by owner from the newly authorized separate non-arm semantic adjudicator, not direct inspection of private evidence by this coordinator.

## 1. Received safe receipt and identity

The user relayed the adjudicator's safe report for `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms`. It claims:

| Reported property | Value |
| --- | --- |
| Encrypted CMS binary size | 51,235 bytes |
| SHA-256 | `8868f308c2e4273eb06726705985bfb12a06a9ddff94a9b25e1f31018bc3fa78` |
| Original historical sources examined | 10/10 |
| Initial assessments examined | 20/20 |
| Substantive adversarial challenge records examined | 10/10 |
| New proposed decision records | 10/10 |
| Input integrity / provenance | PASS |
| Supplied schema validation | PASS |
| Canonical report validation | PASS |
| CMS DER structure | PASS |
| AES-256-GCM encryption | PASS |
| Recipient | Bundled owner public certificate |
| Owner acceptance | PENDING |
| Author release | NONE |

The adjudicator explicitly noted that the owner's private key was not available or requested, and therefore **owner-side decryption/authenticated plaintext readback was not tested**. References requiring historical evidence absent from the bounded packet remained qualified or unresolved. The adjudicator reported consulting no external sources. It supplied no source-to-decision map, restricted rationale, or underlying private comparison to this coordinator.

The filename, size and digest are **adjudicator-reported, owner-relayed**, not yet independently owner-hashed in this conversation. The user's message includes "Download", but does not establish that the file has already been downloaded to the owner's laptop. There is no reason to access, transfer, decrypt, copy or materialize the real CMS via Runtime Bridge or public Git.

## 2. Existing owner intake path

Validation 305 already qualified the owner-only `scripts/r0_p03_s1_owner_wave0_semantic_adjudication.ps1` `Receive` and `Verify` route using invented source evidence. Validation 306 records a real owner-side independently recomputed adjudication input packet, with `VerifyExport` PASS.

Next, the owner **personally** downloads the genuine binary CMS from the separate adjudicator's Temporary Chat to the local Downloads folder, checks **exactly 51,235 bytes and the above SHA-256** using ordinary interactive PowerShell, and invokes `-Action Receive` **once** with the existing recipient ID, file path and expected SHA-256. After successful authenticated readback, owner invokes a **separate `-Action Verify`**. Only safe markers, fixed no-source-specific JSON and status can be shared with the exposed coordinator.

**Failure rule:** `Receive` may write its no-overwrite protected ciphertext and receipt *before* authenticating the report. If it fails, do **not** repeat it blindly. Reconcile the protected state and fixed error code without exposing confidential findings. A successful later `Verify` demonstrates digest-bound authenticated recovery but is not scientific acceptance.

The owner must never provide the private key or passphrase to the adjudicator, coordinator, Runtime Bridge or GitHub.

## 3. Scientific consequence and remaining gate

A genuine ten-record semantic adjudication is now **reported** by the separate role. Once the CMS is owner-authenticated, its source-specific proposals still require an owner-qualified decision as to evidential adequacy, author-disclosure materiality, scope, unresolved HOLDs, and source-world eligibility. A complete ten-record submission proves accounting, not truth or that any `PROSPECTIVE_WHOLE_FILE_CANDIDATE` may be admitted to the blind author.

Do not infer the per-decision category counts from a receipt that reports only a total of ten. Do not automatically expand the same multi-actor review procedure to the separate 2,133 source-review population. Preserve prospective, task-independent risk-based source-family closure, explicit exclusions and material unknowns, then advance to actual twelve primary tasks, nine neutralized legacy cases, independently protected reference answers and the fair Level B B0–B4 experiment.

```text
VALIDATION_307=ADJUDICATOR_REPORTED_SEALED_TEN_SOURCE_SEMANTIC_DECISION_REGISTER
SEMANTIC_ADJUDICATION_CMS_BYTES=51235_REPORTED
SEMANTIC_ADJUDICATION_CMS_SHA256=8868f308c2e4273eb06726705985bfb12a06a9ddff94a9b25e1f31018bc3fa78_REPORTED
ORIGINAL_SOURCE_EXAMINATION=10_OF_10_REPORTED
INITIAL_ASSESSMENT_EXAMINATION=20_OF_20_REPORTED
ADVERSARIAL_CHALLENGE_EXAMINATION=10_OF_10_REPORTED
NEW_PROPOSED_DECISION_RECORDS=10_OF_10_REPORTED
OWNER_DOWNLOADED_FILE_IDENTITY=NOT_YET_REPORTED
OWNER_SEMANTIC_RECEIVE=NOT_YET_REPORTED
OWNER_SEMANTIC_SEPARATE_VERIFY=NOT_YET_REPORTED
SEMANTIC_SOURCE_DECISION_COUNTS=UNKNOWN_RESTRICTED
SOURCE_WORLD_ADMISSIONS=ZERO
AUTHOR_RELEASE=NONE
OWNER_ACCEPTANCE=PENDING
AUTHOR_WORLD=WORLD_UNFROZEN
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
