# Controlled write/read/delete local operation verified

**Date:** 2026-09-01  
**Research:** `docs/research/105_codexless_local_execution_bridge_evaluation.md`  
**Classification:** `CONTROLLED_LOCAL_WRITE_PATH_VERIFIED`

## Interaction provenance

The governed validation was coordinated from the persistent ADS interaction:

```text
Interaction environment  ChatGPT
Project / workspace      Autonomous Data Science System
Interaction session      chatgpt-14
Conversation title       14 - Codexless Write Validation and Source Vault Resume
Primary collaborator     ChatGPT
```

The local execution itself was intentionally performed from a fresh disposable ChatGPT diagnostic interaction with the ADS Codexless Local Bridge. That diagnostic interaction did **not** allocate or consume a persistent ADS ChatGPT session ID.

The formal Codex agent used for the permission-aware portion of the proof reported:

```text
agent                       agent_a7f8d488-f385-4760-8b31-cdf4368b9b80
turn                        01a05c87-939d-7bb3-bb04-5958a8b76026
model                       gpt-5.6-sol
reasoning effort            low
working directory           C:\Projects_Data\autonomous-data-science-system
```

These identifiers are preserved only as bounded execution provenance. Repository state remains the authority.

## Synchronization prerequisite

The local checkout began clean but one commit behind its matching origin-tracking branch:

```text
local HEAD   284c99e094a44750404fa197da127bfaf6d9b93a
origin HEAD  063fdc99c76d7821efc58bb83823bcad33c068c5
branch       v1-source-vault-bootstrap-resume
working tree clean
```

A direct bridge `command_exec` attempt using the inherited `:workspace` / `workspaceWrite` Codex project context reached the real local repository but failed before synchronization because Git could not write `.git/FETCH_HEAD`:

```text
git pull --ff-only
error: cannot open '.git/FETCH_HEAD': Permission denied
```

The failed attempt left the working tree clean and made no repository mutation.

## Formal permission-aware fast-forward

The formal Codex agent lane then reached the same Git boundary and paused at an explicit command approval request.

The exact pending command was:

```text
"C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -Command 'git pull --ff-only origin v1-source-vault-bootstrap-resume'
```

The approval request asked only whether to allow that exact fast-forward-only pull so Git could update `.git/FETCH_HEAD` and synchronize the current branch. It requested no additional permissions.

The project owner granted a one-time approval. No persistent "always allow" preference was established as part of this validation.

The strict fast-forward then succeeded:

```text
284c99e094a44750404fa197da127bfaf6d9b93a
    ->
063fdc99c76d7821efc58bb83823bcad33c068c5
```

No merge, rebase, reset, commit, push, or GitHub write occurred.

Post-synchronization equality was proven:

```text
local HEAD                                    063fdc99c76d7821efc58bb83823bcad33c068c5
origin/v1-source-vault-bootstrap-resume       063fdc99c76d7821efc58bb83823bcad33c068c5
working tree                                  clean
```

## Disposable controlled write proof

The agent created exactly one non-authoritative test artifact:

```text
tests/research105_disposable_probe_20260901_7f3c9a2e.txt
```

Exact UTF-8 content:

```text
Research 105 disposable controlled-write proof.
Nonce: 20260901-7f3c9a2e
```

The file ended with a newline. The exact readback representation was:

```text
"Research 105 disposable controlled-write proof.\nNonce: 20260901-7f3c9a2e\n"
```

Verification result:

```text
text-exact match   True
byte-exact match   True
byte count         73
SHA-256            2489c0a51e8c8f003043b8bd59f75fbf46590301a243d316645b4e2f990be564
```

The first attempted verification command produced a PowerShell parser error before reading or modifying anything. The agent then used a Base64 byte-comparison path, which produced the successful exact verification above.

## Deletion, cleanup and protected-state result

The agent deleted only the disposable artifact.

Final artifact existence:

```text
False
```

Final Git status:

```text
## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume
```

There were no staged or unstaged changes.

The paths changed by the one-commit fast-forward were inspected and no protected Source Universe path appeared. The final state after the disposable cycle was also verified.

```text
Source Registry              unchanged by the controlled proof
Source Vault                 unchanged by the controlled proof
original source corpus       unchanged
.ads-private secrets         unchanged
backup payloads              unchanged
recovery artifacts           unchanged
```

## Product/runtime observations

Two limitations remain important but do not invalidate the proof:

1. The direct model-free command lane can reach and inspect the real local repository, but the current `:workspace` command-execution sandbox does not permit at least the Git metadata write required for `.git/FETCH_HEAD`. The formal agent lane successfully crossed that boundary only through an exact approval request.
2. The Call Codex Rich Card remained visually in a `Codex running` state while the underlying agent was actually `awaitingApproval`. Reading the bounded agent state exposed the exact pending command immediately. This is an observability/UI limitation that should not be mistaken for active model reasoning.

The persistent `chatgpt-14` conversation also experienced intermittent ChatGPT host rejection of Developer MCP invocation after earlier successful bridge calls. Fresh disposable conversations remained able to invoke the bridge. This is preserved as a host/runtime integration limitation rather than reclassified as a local bridge failure.

Browser integration remains deferred.

## Result

The Research 105 controlled write boundary passed in full:

```text
strict fast-forward synchronization    PASS
local/origin equality                  PASS
disposable write                       PASS
text-exact readback                    PASS
byte-exact readback                    PASS
delete-only cleanup                    PASS
final clean working tree               PASS
protected Source Universe unchanged    PASS
visible permission denial/approval     PASS
```

This evidence supports the Research 105 classification `ACCEPTED_FOR_ADS_LOCAL_EXECUTION`, with the direct-lane authority and approval-routing limitations documented explicitly rather than hidden.