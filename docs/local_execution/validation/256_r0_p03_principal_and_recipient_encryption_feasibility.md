# Validation 256: R0-P03 principal separation and recipient-encryption feasibility

**Date:** 2026-10-14
**Status:** READ_ONLY_CAPABILITY_CENSUS_PASS / SYNTHETIC_OWNER_TO_CUSTODIAN_ACCESS_TRIAL_NOT_RUN
**Scope:** Record observed sandbox/tool identities, registered workspace-exposure limits, installed public-recipient cryptography surfaces, and the exact missing human and actor-boundary evidence, without changing accounts, keys, repository authority or scored data.
**Parent:** Research 567; Research 565-566; Validation 254-255; Research 513 and 559.
**Starting HEAD:** `8ff5ce900be08cd0ca7da3f06e62571e18d920bb` on `v1-source-vault-bootstrap-resume`.
**Authority:** Live read-only capability observations and prospective method, not a principal-isolation attestation for all agents, not cryptographic qualification, and not independent reference authoring.

## Actual read-only observations

The baseline checkout was clean and synchronized at the declared commit. Early Codexless `codex.command_exec` calls intermittently timed out even for harmless Git commands; the narrower `codex_read_many` and read-only workspace-registry call succeeded. The command route subsequently recovered, and a later Git status/HEAD read was successful. No bridge permission or trust setting was altered to recover it.

The Codexless registry `show` exposed existing authorized workspaces for ADS public, existing private companion, private runtime, other data projects and personal-document roots. This is **an access-scope inventory**, not proof any entire user-profile folder is readable and not permission to use any of these roots as P03 gold custody. The sensitive concrete local workspace coordinates are deliberately not copied into this public validation.

PowerShell via public-project `codex.command_exec`, with its resolved read-only profile, identified the execution account as the *CodexSandboxOffline* Windows identity. Its SID was not retained in public evidence. A second no-turn `codex_project_context` returned `workspaceWrite` (with networkAccess false), public-project root, and unavailable implicit skills due to structure mismatch; do not claim that zero returned skill entries means none exist. Normal owner-terminal Claude Code execution is an independently distinct context by path/interaction, but the exact Windows security principal and effective tools in each future arm-author run remain to be tested directly.

Read-only program discovery confirmed `OpenSSL 3.2.3` bundled with Git for Windows at a path not on the executable PATH; `openssl cms -help` advertises recipient certificate encryption/decryption, binary mode and streaming. Windows PowerShell 5.1 exposes `Protect-CmsMessage` and `Unprotect-CmsMessage`. This establishes candidate mature encryption tools only. **No test certificate, private key, credential, protected production packet or encrypted synthetic CMS packet was created** in this bounded stage. The existing 7-Zip simulated-output pipe observations remain separately recorded in Validation 255, with no promotion to a qualified real secret path.

## Proposed owner-assisted synthetic preflight (not executed)

1. Determine which future arm authors can have local filesystem/shell/tool access, including whether unrestricted Claude Code under the ordinary desktop user remains in scope. No agent denial test can be interpreted without the intended principal.
2. Obtain explicit approval for a disposable, owner-created synthetic canary in a non-ADS owner-controlled location, without altering existing workspace trust or automatically repurposing a private repository. Record owner-side identity and location **privately**; publish only scrubbed test receipt.
3. Use actual authorized proposed future arm-author tools/principal(s) to attempt the precise canary read. Record correlated success or failure and distinguish a workspace policy denial from a Windows ACL denial. Include other reachable apps/connectors if they are in the authoring threat boundary. Negative evidence from one tool cannot certify all tools.
4. Separately qualify an owner-only private key or protected store. A public recipient certificate could let a collector encrypt without accessing that private key, using existing CMS support; the owner-controlled restoration path must be observed with disposable data and demonstrate key inaccessibility to authors. The existing synthetic output-pipe test cannot substitute for these stages.
5. Verify that raw reviewer answer stdout, debug logs, caches and returned chat text remain outside arm-author reach. Freeze packet digest, complete retrievable restricted version and allowed scorer disclosure **before** arm construction. Stop if any boundary remains unqualified.

**No actual owner canary, encryption key, ACL update, secret, new local Windows user, role change, fresh annotator, task, reference, private-storage write or scored navigation arm was created here.** Research 513/559 and Checkpoint 898 remain unchanged.

## Qualification disposition

The evidence supports a distinct Codex sandbox principal and the local availability of standard public-recipient encryption tools. Neither establishes complete independent gold custody. The next owner's bounded choice is the **allowed execution scope for future arm authors**: this determines whether one owner-only directory or a separate cryptographic/identity boundary could actually prevent answer contamination.

```text
LOCAL_BRIDGE_PRINCIPAL=CODEX_SANDBOX_OFFLINE
FUTURE_CLAUDE_AUTHOR_PRINCIPAL=UNQUALIFIED
PUBLIC_RECIPIENT_CRYPTO=AVAILABLE_NOT_TRIALED
REAL_CUSTODY_AND_REF_ANNOTATOR=NOT_QUALIFIED
REFERENCE_PACKET=NONE
P03_SCORES=NONE
CHECKPOINT=898_UNCHANGED
```
