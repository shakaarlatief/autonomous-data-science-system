# Research 567: R0-P03 reviewer-to-custodian principal and recipient-key feasibility

**Date:** 2026-10-14
**Status:** READ_ONLY_PRINCIPAL_AND_RECIPIENT_CIPHER_FEASIBILITY / NO OWNER_CUSTODIAN OR REAL GOLD QUALIFIED
**Scope:** Identify which available Windows and tool-access boundaries are actually evidenced, distinguish encrypted output capture from decryption-key custody, and specify the smallest prospective owner-assisted synthetic boundary test without modifying credentials, ACLs, storage authority or benchmark data.
**Parent:** Research 513, 559, 561-566; Validation 255; published HEAD `8ff5ce900be08cd0ca7da3f06e62571e18d920bb`.
**Authority:** Non-governing R0-P03 prefixture engineering research. No R0 scientific freeze, key, certificate, production archive, reviewer assignment, scoring, new principal, migration or physical architecture authorization.

## 1. Newly grounded capability observations

A read-only live Codexless workspace registry inspection found that the bridge admits several roots beyond ADS's public repository, including other project and personal-document locations. Registration indicates a permitted tool route, not blanket OS visibility, but demonstrates why a random non-ADS folder or vague secrecy claim cannot be assumed inaccessible to *all* development agents. Exact private directory coordinates are not reproduced here.

A read-only PowerShell execution through the public Codex Runtime Bridge returned a **distinct sandbox Windows principal** (`CodexSandboxOffline`) rather than the user's ordinary desktop principal. The same principal was returned on repeated scoped checks. The Codex App Server project bootstrap reported `workspaceWrite`, `networkAccess=false`, a single public-repository runtime root, and **unavailable** implicit skill routing due to `IMPLICIT_SKILLS_STRUCTURE_MISMATCH`; an unavailable skill inventory is not proof of no inherited skills. An early series of ordinary command invocations timed out; read-only project context and file-read calls subsequently succeeded, and ordinary command execution recovered. No host trust, privileges, account, sandbox configuration or workspace registry record was changed.

**Crucial distinction:** A separate Windows sandbox principal means an owner-controlled ACL or out-of-root policy *may* exclude that particular Codex route. It does **not** imply that ordinary Windows-terminal Claude Code, a browser, other connected apps, all Codex modes, or a future B0-B4 author share that principal or are excluded. The owner-terminal Claude Code preflight proved restricted Read/Glob/Grep denial on specific synthetic routes, not general confinement of every later Claude invocation. Distinct tool configuration and OS identity are both dimensions of independence.

## 2. Public-recipient encryption as an alternative to agent-side passwords

Read-only executable inspection found OpenSSL **3.2.3** at the existing Git-for-Windows executable path, although bare `openssl` was not on PATH. `openssl cms -help` advertises `-encrypt`, `-decrypt`, certificate recipients, binary data and streaming. Windows PowerShell 5.1 also exposes `Protect-CmsMessage` and `Unprotect-CmsMessage` cmdlets. These are capability observations, **not a completed cryptographic trial**, and no user's certificate store or private key content was inspected.

A plausible **C2b recipient-key sealed-output design** is:

1. The owner or independently authorized custodian maintains a private decryption key or credential **outside any future arm-author accessible principal**; the encryptor receives only the corresponding public recipient certificate.
2. An independent reviewer operates within a constrained source/context host and emits a deliberately bounded final structured answer. A trusted collector accepts the output without logging it and immediately encrypts to the public recipient, never requiring the private key or a production decryption password.
3. The complete ciphertext is durably and recoverably versioned with exact source revision, immutable packet identity and a public digest commitment before arm implementation. Verify the **plaintext packet commitment** at authorized recovery. The complete plaintext and all original stdout/debug/provider traces must remain unavailable to arm authors.
4. Later, only the separately authorized scorer/custodian decrypts, and fresh evaluators receive the correct limited inputs under a prospectively frozen scoring/disclosure rule.

This is potentially cleaner than a symmetric 7-Zip collector that has to receive the owner's password. It does **not** imply that public-key encryption automatically authenticates the origin or binds the experimental oracle. Choose a vetted authenticated envelope/signature/commitment mechanism if security requirements demand it; do not invent a custom hybrid cipher or pretend ordinary 7zAES is AEAD.

The private key must not be placed as an unprotected file in a directory accessible to agents, including other processes running under the *same* Windows account. A user-held passphrase to an encrypted key, a separate OS identity, a hardware-confirmed private key, or an offline key can be candidates, but **none** has been qualified. The owner-side decryption action and recoverability require a separate test. Cryptography cannot retroactively protect original plaintext exposed by reviewer stdout, automatic transcript storage, process logs, debug archives or model context.

## 3. Why an ordinary folder is not yet a qualified store

The sandbox is a distinct account from the normal desktop, which gives a concrete prospective negative-access experiment. However, the bridge's per-root trust restrictions and Windows ACLs must be separated in the evidence: a tool denial from a workspace root does not automatically prove OS ACL denial, and a path inaccessible to Codex does not establish inaccessibility from a Claude Code session operating with the owner's ordinary desktop rights.

A meaningful synthetic **owner-assisted** trial needs (a) a harmless unique canary created by the owner in a precisely designated, disposable, non-ADS location; (b) the tested principal(s) attempting actual read, not merely `Test-Path` or asking the model whether it can read; (c) explicit output-source and private-key exclusion; and (d) owner-visible exact cleanup. Do **not** copy private contents into ADS or widen the Runtime Bridge's trusted roots to make testing easier.

If all B0-B4 authoring is compelled to use only a demonstrably confined bridge identity, a restricted owner vault may be viable without a new Windows user. If arm authors also launch unrestricted Claude/code/browser tools under the ordinary desktop account, the same-location folder is not a sufficient boundary. Either formally restrict those future authoring routes or choose real key/identity separation independent of the owner account.

## 4. Proportionate decision before another test

Do **not** install new tools, create a private Git repository or automatically change ACLs. Already-installed OpenSSL and Windows CMS make a public-recipient encryption route technically plausible without putting a decryption password in the model-facing encryptor, but only after an independently controlled recovery/private-key path is designated.

The **smallest next step requiring the human owner** is to clarify the intended *future B0-B4 authoring execution scope*: will Claude Code/other coding agents be allowed to run as ordinary desktop-user processes, or can all such authors be restricted to a verified sandbox or distinct user? This is a project workflow choice rather than merely a directory selection. The owner must then authorize a concrete custody identity/key location and at most one *synthetic* principal-access and output-to-recovery trial. If no separate principal/key or allowed restricted authoring route is established, **stop before independent real gold**.

No fresh annotator is assigned and no scored evaluators are commissioned. Original Research 513 9/12 case totals, their `>=8/9` and `>=10/12` gates, zero false authority, corpus and B0-B4 rules, Research 559 legacy Option A and Checkpoint 898 remain unchanged.

```text
CODEX_SANDBOX_PRINCIPAL=OBSERVED_DISTINCT_FROM_NORMAL_DESKTOP
OTHER_AGENT_PRINCIPALS=NOT_EXHAUSTIVELY_CHECKED
OPENSSL_CMS_TOOL=AVAILABLE_NOT_EXERCISED_WITH_KEYS
OWNER_PRIVATE_KEY_OR_VAULT=NOT_DESIGNATED
OUTPUT_AND_KEY_ACCESS_SEPARATION=NOT_QUALIFIED
PROSPECTIVE_OWNER_WORKFLOW_CHOICE=REQUIRED_BEFORE_REAL_GOLD
NEXT_BOUNDARY=p-three-reviewer-execution-authority-qualification
CHECKPOINT=898_UNCHANGED
```
