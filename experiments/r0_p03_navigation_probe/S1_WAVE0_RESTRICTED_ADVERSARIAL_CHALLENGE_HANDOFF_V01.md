# R0-P03 Wave0: real restricted adversarial challenge, owner-authorized second-stage handoff V0.1

**Date:** 2026-11-09
**Status:** OWNER_EXPLICITLY_AUTHORIZED / IMPLEMENTATION_SYNTHETIC_ONLY_QUALIFIED / ACTUAL_CHALLENGE_PENDING
**Role:** One NON-ARM substantive adversarial source-status challenger. Prefer resuming the original independent first-pass challenger session **only if it remains accessible**. If not, open a genuinely separate fresh Temporary Chat and describe it truthfully as a **third** non-arm challenge actor, not the original first-pass actor.
**Input:** Exactly one owner-exported restricted challenge ZIP, `R0_P03_S1_WAVE0_RESTRICTED_ADVERSARIAL_INPUT.zip`. The owner must not upload that ZIP into the exposed ADS Project/coordinator conversation, GitHub or any blind author/evaluator session.
**Separation:** Original reviewer and first-pass challenger already completed and their two original ciphertexts must remain immutable. This stage **deliberately discloses** both prior rationales only to the challenger. The first-pass report's historical independence is retained, but the new stage is not blind to those findings.

## 1. Scope of disclosure explicitly authorized by owner

The owner explicitly authorized the "next restricted adversarial challenge" after receiving the specific proposal to release the *same ten historical source files*, the **complete first-reviewer restricted report**, **complete blind independent first-pass challenger report**, and **owner-authenticated complete paired comparison** to one non-arm adversarial challenger. This authorization does not extend to original or future gold, other historical source batches, B0–B4 design/outputs, broader project connected apps, primary task authors or the exposed public coordinator.

This ZIP is **restricted plaintext**, unlike the existing owner CMS artifacts. It must only be created and held in the existing ACL-protected owner directory, uploaded personally to one authorized challenger session, and kept out of repository version control, emails, browser public sharing and project-wide attachments. The authorized Temporary Chat provider will receive the restricted source and report contents and its storage/retention controls are a platform-level matter; "Temporary" alone is not cryptographic independence.

## 2. Owner-local preflight and controlled export

From the owner's ordinary interactive PowerShell, and **never through the exposed Runtime Bridge**:

```powershell
Set-Location 'C:\Projects_Data\autonomous-data-science-system'
& .\scripts\r0_p03_s1_owner_wave0_adversarial_challenge.ps1 -Action SelfTest

$recipientId = (Read-Host 'Enter the original Wave0 owner recipient ID').Trim()

& .\scripts\r0_p03_s1_owner_wave0_adversarial_challenge.ps1 `
    -Action Export -RecipientId $recipientId

& .\scripts\r0_p03_s1_owner_wave0_adversarial_challenge.ps1 `
    -Action VerifyExport -RecipientId $recipientId
```

Export additionally requests the exact local confirmation string `AUTHORIZE WAVE0 RESTRICTED CHALLENGE EXPORT`. It then asks for the owner's **existing encrypted key passphrase in the local terminal**, as does `VerifyExport`. It creates no new key. The output is `R0_P03_S1_WAVE0_RESTRICTED_ADVERSARIAL_INPUT.zip` in the same existing protected owner folder as the three authenticated CMS files. The output contains the exact original ten-source ZIP, the complete paired restricted reasoning/claims JSON, the owner's **public-only certificate**, the self-contained `CHALLENGE_SUBMIT.py` CMS sender, a manifest and a bounded challenger brief.

Expected owner-safe markers:

```text
S1_WAVE0_ADVERSARIAL_MODULE_IMPORTS=PASS
S1_WAVE0_ADVERSARIAL_OWNER_PREFLIGHT=PASS
S1_WAVE0_ADVERSARIAL_PRIVATE_INPUTS_OPENED=NO
S1_WAVE0_OWNER_ADVERSARIAL_PACKET_EXPORT=PASS
S1_WAVE0_OWNER_RESTRICTED_ADVERSARIAL_EXPORT=PASS
S1_WAVE0_OWNER_ADVERSARIAL_PACKET_VERIFYEXPORT=PASS
S1_WAVE0_OWNER_RESTRICTED_ADVERSARIAL_EXPORT_RECHECK=PASS
```

The Python CLI prints one safe SHA-256 and byte length for the **restricted packet**. The output ZIP must **not** be uploaded to the current Project conversation, even for debugging. If export reports HOLD, **do not blindly repeat**: a no-overwrite protected output may already exist.

## 3. Paste this scope into the authorized Temporary Chat with the ZIP attached

> You are acting only as the NON-ARM R0-P03 Wave0 substantive source-status adversarial challenger. This is an owner-authorized second-stage critique of exactly ten real historical project sources. You are not the future blind primary author, independent gold/reference annotator, B0–B4 arm author, scored evaluator, or public ADS coordinator. Do not use project memory, connected apps, external web/GitHub, other conversations, or unprovided evidence.
>
> Before inspecting, state whether you are **the original first-pass challenger session resuming** or a **new third-party challenge session**, and disclose your actual accessible tools, prior relevant exposure, and any independence limitations. Never claim stronger model/session isolation than you can observe.
>
> Read `CHALLENGE_BRIEF.txt` and `CHALLENGE_MANIFEST.json` inside the attached ZIP. Then verify the nested exact ten-source original ZIP and all ten complete pairs in `OWNER_PRIVATE_PAIRED_EVIDENCE.json`. The first reviewer and independent first pass are immutable prior evidence. You are **now deliberately permitted** to read both private sets of reasoning; do not retroactively change the first pass.
>
> Perform the actual adversarial scientific work on **all ten original sources**, including cases where both prior dispositions match. Assess each earlier claim and assumption against exact original text, context, current-versus-historical authority and possible protected design/gold exposure. Distinguish material disagreement from mere paraphrase, and investigate **shared mistaken agreement**. Record opposing interpretations, actual source-grounded counterevidence, missing uninspectable context, what would falsify each view, and separate claim materiality from disclosure materiality. If source context is missing, preserve an explicit HOLD rather than invent evidence or force consensus.
>
> Produce exactly one **new complete ten-record, source-bound restricted challenge report** following the `CHALLENGE_SUBMIT.py` report schema. Encrypt the report to the **included PUBLIC certificate** with the bundled sender function `seal(report_dict, packet_zip_bytes)` or its `seal` CLI action, generating a genuine binary `R0_P03_S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE.cms` file. Never ask for or access the owner's private key or passphrase. Return the CMS file and only safe counts, encryption integrity receipt and SHA-256; never print individual paths, dispositions, private rationales or comparative findings in chat. Do not create gold, author packet, experimental score or release decisions. If you cannot inspect the attachments or seal the real report, report HOLD and the exact technical reason without fabricating success.

The ZIP includes the complete instruction text as `CHALLENGE_BRIEF.txt`. In the Temporary Chat, `CHALLENGE_SUBMIT.py` is intentionally standalone with no import of the owner's repository; its schema is explicit in the file's `TOP_KEYS`, `RECORD_KEYS` and `validate_report` implementation. It can be extracted to scratch and called with `seal(report_dict, packet_zip_bytes)` using standard Python and OpenSSL, without writing private report plaintext to a disk file. A reviewer may require time to actually inspect every source; making a report schema object is not a substitute for source analysis.

## 4. Owner-only protected output intake after actual challenge

Only once the challenger returns a real CMS binary, download the file personally. **Do not share that file here.** In normal owner PowerShell use:

```powershell
$challengeFile = Join-Path $env:USERPROFILE 'Downloads\R0_P03_S1_WAVE0_OWNER_ADVERSARIAL_CHALLENGE.cms'
$expected = '<the new ciphertext SHA-256 from the challenger safe receipt>'

& .\scripts\r0_p03_s1_owner_wave0_adversarial_challenge.ps1 `
    -Action Receive -RecipientId $recipientId `
    -Ciphertext $challengeFile -ExpectedSha256 $expected

& .\scripts\r0_p03_s1_owner_wave0_adversarial_challenge.ps1 `
    -Action Verify -RecipientId $recipientId
```

Check both ciphertext bytes and SHA-256 independently before Receive. Receipt and ciphertext are saved separately with **no overwrite** in the original protected owner directory. A failed Receive may already have copied both, so do not rerun blindly. A separate `Verify` again authenticates/validates the full ten-source challenge report and returns safe markers, not restricted findings. The CMS readback is **not** owner source-status adjudication or author-world freeze.

## 5. Scientific continuation after challenge

The substantive response may reveal that both first passes shared an error, that reviewers disagree due to unresolved external context, or that no admissible conclusion can be supported yet. The next step is an owner-private, source-grounded assessment of actual material objections and decisions. Ten reviewed sources do not imply a completely qualified 2,133-record historical evidence population. Once defensible corpus-source qualification and independent task/reference input closure are sufficient, move to the preregistered twelve primary tasks, separately neutralized nine legacy cases, prospective split and B0–B4 execution.

```text
SECOND_STAGE_OWNER_DISCLOSURE=AUTHORIZED_2026_11_09
CHALLENGER_PACKET=REAL_EXPORT_PENDING
CHALLENGER_SUBSTANTIVE_REPORT=PENDING
CHALLENGER_OWNER_READBACK=PENDING
ACTUAL_ADVERSARIAL_ADJUDICATION=NOT_COMPLETED
SOURCE_AUTHOR_ADMISSIONS=0
S3_WORLD=WORLD_UNFROZEN
S4_B0_B4_SCORING=NOT_STARTED
```
