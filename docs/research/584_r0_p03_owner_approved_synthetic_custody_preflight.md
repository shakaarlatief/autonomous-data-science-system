# Research 584: Owner-approved R0-P03 synthetic reference-custody preflight

**Date:** 2026-10-18
**Status:** OWNER_APPROVED / SCRIPT_PREPARED_AND_SELFTESTED / OWNER_CREATION_AND_ACCESS_POSTFLIGHT_PENDING
**Scope:** Prepare the specifically approved owner-controlled fake-only 9+12 reference-custody experiment, reusing bounded Research 570 findings without changing unrelated Windows folders, real answers, production secrets, private companion duties or scientific authority.
**Basis:** Research 513/559/565–570, owner-accepted Research 576 Level B, Research 582–583, and explicit owner reply "I approve." to one new protected owner-controlled synthetic-only folder.
**Provenance:** ChatGPT/chatgpt-39 exposed engineering coordinator. No owner-terminal Create operation has occurred yet.
**Authority:** Owner permits the stated fake-only folder trial. No production gold, real key, scored actor, new owner identity, permission weakening or project cutover is authorized.

## 1. Required owner execution boundary

Runtime Bridge read-only command calls run as Shakaar CodexSandboxOffline; inherited command calls run as Shakaar CodexSandboxOnline. Neither is the ordinary Windows owner process. The registered Runtime Bridge provides no general owner impersonation or unrestricted host ACL mutation. Creating a substitute agent-owned directory would not test the desired boundary.

Prepared only these engineering paths:

- scripts/r0_p03_owner_synthetic_custody.ps1
- tests/unit/test_r0_p03_owner_synthetic_custody_script.py

The script supports Create, Verify and SelfTest. The SelfTest operation generates fictional 9-legacy and 12-primary slots, four categories of three, detects simulated altered/truncated packet bytes using SHA-256, and writes nothing. The Create operation forbids selecting an existing directory. In a normal non-elevated owner PowerShell process only, it makes a fresh GUID-named folder directly under the owner's existing LocalAppData root. It creates the directory atomically with a protected discretionary access control list that permits the current owner SID and SYSTEM only, and checks the resulting ACL before any file writes. It refuses Codex sandbox identities, SYSTEM and elevated administrative PowerShell.

Inside that protected new folder, Create writes exactly two files with CreateNew semantics: a complete fictional 21-case JSON packet and a source-free manifest binding the version, content digest, byte count and case distribution. It launches Verify in a separate PowerShell process under the same owner identity, which checks the ACL, file roster, complete bytes/digest, regenerated exact synthetic packet and manifest. This is immediate separate-process recovery, not a real computer-restart durability trial.

The only data marker is SYNTHETIC_ONLY_R0_P03_NO_REAL_GOLD and each reference claim/source is overtly fictional. No actual ADS questions, answers, gold, owner signing key or production credentials are handled. The script emits only a folder path, digest and PASS/error markers, never packet contents.

## 2. One owner command after publication

Run from ordinary Windows PowerShell, not Run as Administrator:

    & "C:\Projects_Data\autonomous-data-science-system\scripts\r0_p03_owner_synthetic_custody.ps1" -Action Create

If the local script execution policy blocks execution, the alternative is one process-scoped invocation, without changing any persistent policy:

    powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Projects_Data\autonomous-data-science-system\scripts\r0_p03_owner_synthetic_custody.ps1" -Action Create

Return only the synthetic directory, digest and PASS/error markers. Do not retry Create after an uncertain result, because the procedure may have left a unique synthetic folder. Do not remove the folder until the bounded direct-access checks are finished; the owner retains authority over disposal.

## 3. Independent bridge postflight, not yet completed

After owner-created path and digest are supplied, ChatGPT will probe only that exact fabricated target, and will not print packet contents. First distinguish an out-of-root file-reader refusal from OS-level denial. Next attempt sandbox file-byte reads under the currently exposed read-only and inherited Codex Windows identities and record denial, success, absent file or tool failure accurately. Keep owner-positive digest and independent fresh-owner-process readback distinct from the sandbox results.

Neither a single tested ACL nor a denied model-free command establishes that all future B0-B4 arm authors are excluded. Owner-equivalent Claude/other CLI, connected accounts, alternate tools, provider model context, output transcripts, hidden-gold collector and whole-packet versioning for real answers remain separate readiness gates. If a read is unexpectedly allowed, stop and investigate that precise path without downgrading ACL restrictions or falsely declaring a scoped PASS.

Only a nonsecret receipt and bounded classification may enter public project knowledge; never publish an owner-local absolute path, real answer bytes or secret. Prior Research 566/568 synthetic encryption and Research 570 scoped OS denial remain historically valid but are not a substitute for this new actual test.

## 4. Preparation status and scientific preservation

The PowerShell parser and SelfTest already completed successfully in the registered ADS sandbox without creating any owner folder. The test also rejects an arbitrary Create destination. These constitute only preflight checks.

Until the owner actually executes Create, full owner-custody and access-denial qualification is UNOBSERVED. The experiment keeps the primary 12/legacy 9 scientific requirements, Research 513/559/576, prior rehearsal questions' exclusion, Checkpoint 898, existing routing, Specification 028 and B0-B4 scoring boundary unchanged.

R0_P03_OWNER_SYNTHETIC_CUSTODY=OWNER_APPROVED_PREPARED_NOT_EXECUTED
R0_P03_SCORED_TASKS=NONE
R0_P03_REAL_GOLD=NONE
R0_P03_SCORE=NONE
