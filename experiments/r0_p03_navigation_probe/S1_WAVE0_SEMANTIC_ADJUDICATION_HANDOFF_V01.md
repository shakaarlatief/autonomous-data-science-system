# R0-P03 Wave0: owner-authorized semantic adjudication handoff V0.1

**Date:** 2026-11-09
**Status:** SEPARATE_NON_ARM_ADJUDICATOR_DISCLOSURE_AUTHORIZED / OWNER_HANDBACK_CODE_FICTIONAL_TESTED / REAL_ADJUDICATION_PENDING
**Authority:** The owner explicitly replied "Yes, I authorize." to the specific proposal to provide all ten source files, both complete initial private assessments and the newly owner-authenticated adversarial challenge to **one separate non-arm semantic adjudicator**. The previously verified owner-held paired comparison is part of that same bounded evidence chain. No access to other historical sources, private gold, arm results, task authors or coordinator is authorized.

## Owner: exact local preflight and export

Run **only** in your ordinary interactive PowerShell (never inside the exposed Runtime Bridge) from the ADS repository:

```powershell
Set-Location 'C:\Projects_Data\autonomous-data-science-system'

& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 -Action SelfTest

$recipientId = (Read-Host 'Enter the EXISTING Wave0 owner recipient ID').Trim()

& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 `
    -Action Export -RecipientId $recipientId

& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 `
    -Action VerifyExport -RecipientId $recipientId
```

The `SelfTest` checks the original source ZIP and both actual Python entrypoints without touching owner-private evidence. Expected:

```text
S1_WAVE0_SEMANTIC_OWNER_MODULE_IMPORTS=PASS
S1_WAVE0_SEMANTIC_OWNER_PREFLIGHT=PASS
S1_WAVE0_SEMANTIC_OWNER_PRIVATE_EVIDENCE_OPENED=NO
```

The `Export` operation requires a separate, exact interactive confirmation: `AUTHORIZE WAVE0 SEMANTIC ADJUDICATION EXPORT`. It then prompts locally for the **existing encrypted owner key passphrase**, reauthenticates the two initial CMS reports, recomputes their paired comparison, independently reconstructs the previously verified restricted challenge ZIP, and authenticates/validates the newer adversarial CMS at known fixed SHA-256 `e2d2c31d0486b9314b1d5902776da866397cb092963ac75c95e7b5c6f313ac03`. The owner need not create a key, public certificate, first-pass or challenge anew.

`Export` creates **one no-overwrite RESTRICTED PLAINTEXT ZIP** under the existing owner ACL directory:

```text
R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip
```

It contains exactly seven members: original historical ten-source ZIP, complete paired first-pass report with rationale, full authenticated adversarial challenge report, owner **public** encryption certificate, manifest, bounded adjudication brief and standalone `ADJUDICATION_SUBMIT.py`.

Expected safe terminal completion markers:

```text
S1_WAVE0_OWNER_SEMANTIC_PACKET_EXPORT=PASS
S1_WAVE0_OWNER_SEMANTIC_EXPORT=PASS
S1_WAVE0_OWNER_SEMANTIC_PACKET_VERIFYEXPORT=PASS
S1_WAVE0_OWNER_SEMANTIC_EXPORT_RECHECK=PASS
```

The export script reports only safe packet SHA-256 and byte count, exact ten-source count and fixed authentication markers. `VerifyExport` reauthenticates all protected original inputs, reconstructs the packet deterministically, and verifies the previously saved ZIP bytes exactly. **Do not rerun Export blindly if an error occurs**: it may have written the packet already and refuses overwriting it.

## Adjudicator: deliver to exactly one qualified separate non-arm session

If the original source challenger session is still accessible, do **not** reuse it for supposedly independent adjudication: the owner's authorization is for a **separate** non-arm semantic adjudicator. Choose a fresh Temporary Chat outside this Project with no connected apps, no previous confidential project material and no hidden-gold access. A Temporary Chat is pragmatic Level B session hygiene, not a claim of complete provider-level or OS-level isolation.

**Owner personally uploads exactly** `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION_INPUT.zip` from the private directory. This is unencrypted restricted plaintext on upload; the receiving model provider sees the original sources and source-specific rationales. It is **not** safe for public Git, general Project attachments, model-arm, task/gold or scoring sessions.

The following is an exact, bounded ready-to-paste instruction for the separate adjudicator:

> You are the independently assigned **NON-ARM R0-P03 Wave0 semantic source-status adjudicator**, not a primary task writer, hidden-gold annotator, B0–B4 arm engineer, scorer or public project coordinator. Your role is to make ten evidence-grounded prospective source-status decisions or justified HOLDs based **only** on the attached restricted ZIP.
>
> **Before inspecting any source**, state your actual tools and source-access capabilities, any relevant prior exposure, session independence limitations, and whether you can really read nested ZIPs and encrypt a binary CMS. Do not claim privacy or isolation not actually verified.
>
> Open `ADJUDICATION_BRIEF.txt` and `ADJUDICATION_MANIFEST.json`. Inspect every original source in `ORIGINAL_WAVE0_SOURCES.zip`, both complete first-pass reviewer rationales in `PAIRED_FIRST_PASSES.json`, and the newly authenticated ten-record substantive adversarial critique in `SUBSTANTIVE_CHALLENGE.json`. The original reports and challenge are historical evidence and must remain unchanged.
>
> For **each of all ten sources**, assess the historical/version authority, exact original-byte support for earlier claims, which previous counterarguments survive, unverified references or media, strongest falsifier, and claim materiality **separately from author-disclosure/old-gold leakage materiality**. Challenge apparent agreement and distinguish incomplete context from confirmed contamination. Do not invent missing evidence, use majority voting or force consensus.
>
> Record exactly one of the bounded decisions per source: `PROSPECTIVE_WHOLE_FILE_CANDIDATE`, `AUXILIARY_ONLY_EXCLUDED_FROM_AUTHOR`, `PROHIBIT_AUTHOR_EXPOSURE` or `HOLD_FOR_MATERIAL_EVIDENCE`. Every choice needs specific source-grounded reasoning, distinct disclosure reasoning and a concrete falsification/next-evidence condition. HOLD whenever material external context is unavailable. A candidate is **not an author admission**. Do not produce actual author packets or gold.
>
> Produce a **new complete ten-record restricted decision register** matching the bundled standalone `ADJUDICATION_SUBMIT.py` `TOP_FIELDS`/`RECORD_FIELDS` schema and `validate_report`. Encrypt it with AES-256-GCM CMS DER using **only the owner's PUBLIC certificate contained in the ZIP**, outputting the genuine binary file `R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms`. Do not ask for the owner's private key or passphrase.
>
> Return only the downloadable CMS binary plus a safe receipt with its filename, byte count, SHA-256, successful ten-record/schema/encryption markers and any method limitations. **Do not print source names, source-to-status maps, findings or reasoning in the chat.** Do not access external websites, connected apps, GitHub, past chats, memory, other source files or unprovided gold. If you cannot inspect all sources or produce an actual binary CMS, report HOLD honestly rather than a claimed PASS.

The model can use the standalone sender `seal(report_dict, packet_zip_bytes)` or its `seal` CLI action. The sender validates that the entire structured report is bound to the supplied original source ZIP, paired first passes, substantive challenge, source identities and explicit non-release status before encryption. It does not prove the model's actual reasoning correct.

## Owner: sealed result intake after actual new adjudication

After the separate adjudicator returns a *real binary CMS*, download it personally to Downloads. Return to normal owner PowerShell:

```powershell
$decisionCms = Join-Path $env:USERPROFILE 'Downloads\R0_P03_S1_WAVE0_OWNER_SEMANTIC_ADJUDICATION.cms'
$expectedSha = '<reported full 64-character lowercase SHA-256>'
# First check that the downloaded file's size and SHA-256 match the safe receipt.
& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 `
    -Action Receive -RecipientId $recipientId `
    -Ciphertext $decisionCms -ExpectedSha256 $expectedSha

& .\scripts\r0_p03_s1_owner_wave0_semantic_adjudication.ps1 `
    -Action Verify -RecipientId $recipientId
```

Owner `Receive` saves the exact CMS and private receipt with **no overwrite** before authentication; a HOLD may leave those files present. Do not rerun blindly if it fails. A separate `Verify` checks exact packet identity and the ten source decisions under the same owner encrypted key. Share only fixed safe receipts with the public coordinator.

**After** those steps, the evidence is eligible for an additional owner-side scientific acceptance/coverage decision. The adjudicator's records remain `PROPOSED_DECISIONS_REQUIRE_OWNER_QUALIFICATION`; no source is automatically admitted. Resolve material HOLDs or document their justified exclusion, then move into prospective source-world closure and primary 12-task / neutral 9-legacy preparation rather than recurring open-ended reviews.

```text
OWNER_AUTHORIZATION=NEW_SEPARATE_SEMANTIC_ADJUDICATOR_EXACT_WAVE0
REAL_SEMANTIC_PACKET_EXPORT=NOT_EXECUTED_IN_PUBLIC_COORDINATOR
EXTERNAL_ADJUDICATOR_REVIEW=PENDING
NEW_SEMANTIC_DECISION_CMS=PENDING
SOURCE_WORLD=WORLD_UNFROZEN
AUTHOR_ADMISSIONS=ZERO
GOLD_AND_B0_B4_SCORING=NOT_STARTED
```
