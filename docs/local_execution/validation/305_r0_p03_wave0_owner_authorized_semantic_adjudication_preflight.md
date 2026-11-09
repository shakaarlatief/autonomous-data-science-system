# Validation 305: Wave0 owner-authorized semantic adjudication handoff, fictional-only preflight

**Date:** 2026-11-09
**Status:** OWNER_AUTHORIZATION_RECORDED / PURPOSE_SPECIFIC_SEMANTIC_HANDOFF_IMPLEMENTED / FICTIONAL_END_TO_END_AND_INTEGRATED_TESTS_PASS / REAL_OWNER_EXPORT_PENDING
**Research:** 623, 622, 621, 617–620. **Specification:** 028 unchanged. **Checkpoint:** 898 unchanged.
**Scope:** Deliver a source-specific decision/HOLD phase for exactly ten previously assessed and owner-authenticated Wave0 sources with one separately authorized non-arm adjudicator, without decryption of real owner evidence through the exposed Runtime Bridge or publication of private source findings.

## 1. Authority, source and role boundary

The user replied **"Yes, I authorize."** directly to the explicit proposal to provide **the same ten original historical sources**, the **two complete initial restricted assessments**, and the **newly owner-authenticated substantive adversarial challenge**, to **one separate non-arm semantic adjudicator solely to produce ten decisions or justified HOLDs**. This new authorization is distinguished from the previous restricted challenge permission and recorded before any real semantic adjudicator export. The owner-held paired comparison binds the earlier full records. No broader historical population, task/gold material, future blind authors, arms, scorers, connected apps or public coordinator is included.

Previously authenticated actual source-identity witnesses:
- Original ten-file archive SHA-256 `c90c2d7120ffd32657e6506f876acd10e9779dc968ba9da8fb7f12604aa58387`.
- First reviewer CMS SHA-256 `9194093b4a4b452b90638bf80eb491d0898c0a7330a77275be74ac9f4aa5a366`.
- Independent first pass CMS SHA-256 `50952716754e72a6df915928d1e86c612b510aedc6b3f11c012d9d08b537da64`.
- Owner complete paired comparison CMS SHA-256 `f55b6c11e619b8a9b61431564ff19b80073ddfec0b61d8f21d577917cdf66ef3`.
- Owner-authenticated adversarial challenge CMS SHA-256 `e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03`, challenger-reported size 49,653 bytes, independent owner `Verify` PASS in Validation 304.

These are immutable input identities; no access to their private content via this exposed session is implied.

## 2. Implemented bounded owner-to-adjudicator route

`experiments/r0_p03_navigation_probe/s1_wave0_semantic_adjudication_packet.py` authenticates the first/second CMS and the paired comparison, reconstructs and checks the original restricted challenge packet against its exact contents, then authenticates and validates the real substantive challenge CMS at its fixed identity. It creates a deterministic, **restricted PLAINTEXT**, seven-member ZIP in the **same owner ACL-protected recipient directory** with exclusive no-overwrite creation and distinct exact-byte `VerifyExport`. It never writes the four decrypted originals separately. The recipient's provider will receive the restricted plaintext if the owner personally uploads the ZIP.

`experiments/r0_p03_navigation_probe/s1_wave0_semantic_decision_report.py` contains a standalone schema for exactly ten source/version-bound decisions or HOLDs. For each record, it requires three-layer inspection claims, historical authority and evidence, strongest opposing interpretation, explicit **claim** vs **disclosure** materiality, gaps, reasoned decision, falsifier and next action. It explicitly prohibits auto-author-release by requiring `author_release=NONE` for every record and `source_world=WORLD_UNFROZEN`; decisions remain `PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION`. The code encrypts the complete report via AES-256-GCM CMS using only the owner's **public** certificate. Separate owner-only authentication/decryption validates the entire report without printing source-specific results.

`scripts/r0_p03_s1_owner_wave0_semantic_adjudication.ps1` runs `SelfTest/Export/VerifyExport/Receive/Verify` with original owner recipient, key, public cert, exact prior file hashes and owner-directory ACL. `Export` requires a local `AUTHORIZE WAVE0 SEMANTIC ADJUDICATION EXPORT` confirmation. Both actual packet and later encrypted decisions are no-overwrite owner-held artifacts. A failed `Receive` may have stored its CMS and receipt before authenticated readback; never repeat blindly.

The full owner commands, separate Temporary Chat prompt and return route are documented in `experiments/r0_p03_navigation_probe/S1_WAVE0_SEMANTIC_ADJUDICATION_HANDOFF_V01.md`. This separate adjudicator is NOT the same previous substantive challenger and must not be a future experimental task/answer/scoring/arm actor.

## 3. Actually observed source-free qualification

The new decision-register route was exercised only on **invented ten-source originals**, fabricated first-pass reviews, fabricated adversarial challenge reports, a disposable encrypted RSA keypair and fictional ten-decision outcomes. The crypto and packet format functions were the same actual implementation to be used by the owner/challenger, but *no owner-real private files were opened or tested by the coordinator*.

Tests cover:
- Exact previously authenticated first/second/comparison and third-stage challenge source binding, successful deterministic owner-restricted packet creation, separate byte-level `VerifyExport`, unchanged input CMS files and no-overwrite.
- All three original/private evidence layers in seven-member packet, full ten-record decision register with source identities and complete reasoning fields.
- Real AES-256-GCM CMS report encryption/decryption and complete owner-bound schema readback with no source-specific terminal output and no author admissions.
- Prior challenge tampering, saved packet tampering, missing source decisions, false inspection, attempted source auto-release, no justified HOLD next action, wrong passphrase, mismatched public certificate.
- Exact Python `-m` import route and owner PowerShell control tokens, preventing the previous direct-script import-path failure.

The first full focused run reported one non-dangerous **validation-error priority** issue: `required_next_action=NONE` under HOLD was rejected by the generic nonempty substantive-explanation rule before reaching the dedicated HOLD-specific check. This was corrected by evaluating the exact HOLD sentinel first, preserving both strict rejection and a meaningful fixed error code. The subsequent complete **20/20** invented-only test run returned PASS. A separate integrated run combining original Wave0 source/reviewer/challenger/challenge and new adjudication tests returned **35/35 PASS**. PowerShell AST check returned **`SEMANTIC_OWNER_WRAPPER_AST=PASS`**.

Repository public integrity, Git diff and guarded commit/push status are separate postflight observations; do not count a timeout or missing observation as PASS. All new tests are synthetic only; no real source-specific status or challenger conclusion may be inferred from fictional fixtures.

## 4. Genuine next work

Once public source-free code is published, the owner uses **ordinary interactive PowerShell**, not Runtime Bridge, to run the new `-Action SelfTest`, then `-Action Export` once with the same original recipient ID and passphrase, then a separate `-Action VerifyExport`. If these pass, upload **only** `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip` into exactly one separately scoped non-arm Temporary Chat with no connected apps, using the handoff instructions. The adjudicator should actually inspect all ten sources and prior arguments, submit ten genuine reasoned decisions/HOLDs under AES-256-GCM CMS, and return a safe size/hash/limitations receipt. Then owner `Receive` and separate `Verify` authenticate the sealed results locally without printing any source-specific information.

Even a complete authentic decision register requires **owner qualification**, not automatic release. The genuine scientific outcome can include unresolved HOLDs that remain excluded from a prospectively justified, narrower source world. The broader 2,133 historical records remain review-only until an efficient risk-stratified source-family closure can support actual 12-task plus nine neutral-legacy reference construction and B0–B4 fair scoring.

```text
VALIDATION_305=OWNER_AUTHORIZED_SEPARATE_SEMANTIC_ADJUDICATION_ROUTE_SYNTHETICALLY_QUALIFIED
OWNER_DISCLOSURE=EXACT_TEN_SOURCES_FIRST_TWO_REVIEWS_AND_ADVERSARIAL_CHALLENGE
FOUR_OWNER_INPUT_CMS=PRIOR_OWNER_AUTHENTICATED
NEW_SEMANTIC_PACKET_REAL_EXPORT=NOT_EXECUTED
INDEPENDENT_EXTERNAL_SEMANTIC_ADJUDICATOR=NOT_YET_RUN
NEW_SEMANTIC_CMS=NOT_YET_RETURNED
FICTIONAL_FOCUSED_TESTS=20_OF_20_PASS
INTEGRATED_SOURCE_ROUTE_TESTS=35_OF_35_PASS
POWER_SHELL_AST=PASS
RELEASE_AUTHORIZATION=NONE
OWNER_ACCEPTED_SOURCE_DECISIONS=ZERO
SOURCE_AUTHOR_ADMISSIONS=ZERO
S3_WORLD=WORLD_UNFROZEN
S4_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
