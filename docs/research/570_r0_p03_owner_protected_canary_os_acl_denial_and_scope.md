# Research 570: R0-P03 owner-protected canary and bounded Windows ACL isolation

**Date:** 2026-10-14
**Status:** OWNER_CANARY_ACL_READ_DENIAL_OBSERVED / COMPLETE_ARM_AGENT_HOST_AND_GOLD_CUSTODY_NOT_QUALIFIED
**Scope:** Compare the owner-created unprotected and protected disposable synthetic-canary directories using the same Codex sandbox identity and both the bounded file reader and general command execution, and identify the remaining independent reviewer/custodian and arm-agent obligations.
**Parent:** Research 513 §6, Research 559 Option A, Research 564–569, Validation 258, MC-0030; starting legitimate project HEAD `0ffede8bb15572250834680337e89a0c248e3ecf`.
**Authority:** Synthetic access observation only. No security policy changes by the ADS agents, owner key, real reference packet, R0-P03 arm author, scorer, source freeze, migration or architecture choice.

## 1. Owner setup and evidentiary scope

The owner ran the previously reviewed PowerShell procedure in the **ordinary Windows desktop session**, creating a new randomly named `ADS-P03-PROTECTED-*` directory under local application data. The owner’s script disabled inherited permissions **for that newly created directory only**, added explicit inherited FullControl rules for the current Windows user SID and SYSTEM, and created one random `SYNTHETIC_ONLY_` text canary. The owner reported:

- `OwnerCanRead=True`.
- `InheritanceProtected=True`.
- A complete SHA-256 of the synthetic-only text file, preserved in the chat-level experiment evidence; it is not necessary to publish an account-local path or canary value in project knowledge.
- The exact canary path was provided for the test, but is intentionally omitted from this public record.

The owner-positive existence and read check is necessary: a model-side `FileNotFound` would not count as an access denial. The original unprotected canary remained a **distinct** prior experiment: that first folder inherited general group read rights and the Codex sandbox successfully read the fake file. No private user data, reference answers, keys, or other owner documents were targeted.

## 2. Actual access tests against the same protected file

The task owner invoked the current purpose-specific public ADS Runtime Bridge tools with `cwd` set to the ADS trusted workspace:

| Route and effective principal | Observed result | Interpretation |
|---|---|---|
| `codex_read_many` with the exact outside-root protected canary path | Explicit refusal: path outside trusted root | **Tool boundary enforced** for this file |
| `codex_command_exec(access=readOnly)` running ordinary sandbox PowerShell, `[IO.File]::ReadAllBytes` | `Shakaar\CodexSandboxOffline`; `READ_RESULT=WINDOWS_ACCESS_DENIED`; `UnauthorizedAccessException` | **OS-level file read denied** for the tested sandbox principal |
| Same read-only command execution route running Python’s `Path.open('rb')` | `read_result=WINDOWS_ACCESS_DENIED`; `PermissionError` | Independent language/API check of the **same effective OS read exclusion** |

The command-level checks did **not** print the canary, any recovered contents, or secret material. The OS-level read denials are not inferred from the `codex_read_many` root-policy denial. The two ordinary programmatic file-open operations actually attempted to read bytes, and the operating system refused both. Unlike the original unprotected-folder test, this is not a false success obtained by testing a nonexistent file: the owner directly verified its existence and readability.

**Scope precision:** This demonstrates a real negative read decision for the current Codex command sandbox Windows security token on exactly one protected synthetic owner file. Two language APIs under the same token are corroborating reads, **not two independent principals**. We did not inspect or change Windows token memberships, prove the entire ACL evaluation chain, remove admin or backup privileges, or test owner-user processes, unrestricted Claude CLI, browser/connector tools, file-export avenues, symlink inheritance across other paths, device-backed stores or model prompt-context leakage.

## 3. Comparison with prior falsification

| Property | Earlier unprotected synthetic folder (Research 569) | New protected synthetic folder (this record) |
|---|---|---|
| Owner-side positive read | True | True |
| Inheritance | Enabled | Disabled (owner-reported) |
| `codex_read_many` outside trusted workspace | DENIED | DENIED |
| Codex sandbox PowerShell byte read | **SUCCESS** (prior isolation failure) | **UnauthorizedAccessException** |
| Codex sandbox Python byte read | Not tested then | **PermissionError** |
| Complete experiment/custody qualification | Not qualified | **Still not qualified** |

The change in actual accessible behavior is consistent with protected permissions excluding the sandbox account. We did not rerun a controlled pair of old/new folders under identical simultaneous conditions or prove which individual ACE caused the decision. The actual file read results suffice for the bounded decision.

## 4. Implications for R0-P03 architecture and work procedures

The owner has approved a **temporary experiment-specific restriction**: B0–B4 architecture-arm authors must operate only in a verified gold-blind execution/tool/context boundary; unrelated ADS development need not change. This observation makes a narrowly scoped owner-controlled Windows-protected directory a **credible candidate** for a future custodian component. It does **not** establish that all future arm-author tools or models are confined to the `CodexSandboxOffline` account, and does not authorize blindly selecting that folder as the permanent gold location.

For any future author route, qualify all available code execution, alternate workspaces and connectors, browser/network access, Git/source/transcripts, model inherited context, prompt-input gold contamination and credential exposure. Especially exclude ordinary desktop-user Claude Code *from arm authoring* unless it is separately sandboxed/qualified; under the owner's account, it could have owner-equivalent file rights irrespective of the Codex sandbox denial.

Separately, verify that the **fresh independent reference author** sees only the closed eligible source world and cannot see old answers or compared arms; an **owner-controlled collector** can store the *complete* packet with a protected private key or genuine owner-only store; original plaintext logs/stream captures stay outside authoring access; frozen bytes/commitments match; owner recovery works after a restart; and the eventual scorer and at least two fresh adjudicators see only appropriately released references. A protected folder alone cannot solve these identity, output or scientific independence gates.

The previous fake-only OpenSSL CMS AES-256-GCM public-recipient trial shows that the encryptor need not have the owner's private key, but **no production key, certificate, writer privilege or durable packet is approved or deployed**.

## 5. Required next qualification and preservation

1. Preserve the protected owner canary until the task owner and owner agree no more authorized tool-route checks are needed. The original unprotected synthetic folder may be deleted by the owner at their discretion. **No ADS agent should attempt to delete or modify the owner directory** via bridge tooling.
2. Define a binding, enforceable **B0–B4 arm-author host profile**: exact Windows/agent identity, effective model tools, code execution, read roots, local/global instructions, connector inventory, inherited context and network/output routes. Use this profile for the actual arm implementation, not merely the testing shell.
3. Exercise additional genuinely distinct allowed tool routes, if any, against synthetic protected canaries, with explicit owner-positive existence and accurate root-policy-vs-OS-policy attribution. If the model’s remaining broad tool routes cannot be bounded, withhold arm-agent qualification.
4. Only then perform a separate owner-assisted **synthetic** public-recipient collector/private-key/complete-output retention and independent recovery test. No real scored reference packet until the author and custody roles also qualify.

No original Research 513 arm parity/scoring/preregistration rules or Research 559 legacy Option A are changed, and no R0-P03 historical or primary task, reference, implementation, scored arm, migration or physical selection was undertaken. Checkpoint 898 and `p-three-reviewer-execution-authority-qualification` remain unchanged.

```text
OWNER_PROTECTED_CANARY_REPORTED_READABLE=TRUE
OWNER_PROTECTED_INHERITANCE_REPORTED_TRUE=TRUE
BOUNDED_FILE_READER_OUTSIDE_ROOT=DENIED
SANDBOX_POWERSHELL_OWNER_CANARY=OS_ACCESS_DENIED
SANDBOX_PYTHON_OWNER_CANARY=OS_ACCESS_DENIED
ACL_ISOLATION_FOR_TESTED_SANDBOX_PRINCIPAL=POSITIVE
COMPLETE_ARM_AUTHOR_ENVIRONMENT=NOT_QUALIFIED
OWNER_PRIVATE_KEY_AND_COMPLETE_GOLD_CUSTODY=NOT_QUALIFIED
R0_P03_SCORE=NONE
CHECKPOINT=898_UNCHANGED
```
