# Semantic Git fetch MCP dispatch verified

**Date:** 2026-09-01  
**Status:** `SEMANTIC_GIT_FETCH_MCP_DISPATCH_VERIFIED`  
**Result:** `PASS / BOUNDED MODEL-FREE GIT FETCH EXECUTED THROUGH SEMANTIC MCP ACTION`  
**Scope:** Preserve the completed B-side of Validation 017, including the live-factory implementation correction, ChatGPT action refresh, authority invariants, exact one-call `git fetch origin` result, and the A/B interpretation against the previously blocked generic command surface.  
**Authority:** Bounded local-execution evidence. This record proves only the fixed semantic `codex.git_fetch_origin` action for the trusted ADS repository. It does not accept pull, commit, push, reset, rebase, checkout, arbitrary Git commands, generic host-process access, or broader local authority.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md`, `path:docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md`, `path:docs/CURRENT_STATE.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Question tested

Validation 017 froze a narrow A/B experiment after the generic public command surface was blocked by ChatGPT/OpenAI safety before local execution:

```text
A
surface     codex.command_exec
request     ["git", "fetch", "origin"], access=inherit
result      BLOCKED BEFORE LOCAL EXECUTION

B
surface     codex.git_fetch_origin
request     {}
backend     fixed ["git", "fetch", "origin"] through the same Codex authority path
result      to be observed
```

The purpose was not to bypass platform safety. The purpose was to test whether the host distinguishes an arbitrary command contract from a truthful, bounded semantic action whose caller cannot select the command, repository, remote, branch, URL, refspec, credentials, or permission profile.

## 2. Local implementation correction before dispatch

The first local experimental patch correctly added `codex.git_fetch_origin` to the public allowlist, but initially registered the tool in `src/public-server-factory.mjs`.

The running Codexless HTTP path actually constructed the public server through:

```text
mcp-http-public.mjs
    -> createCodexlessRuntime({ mode: "public" })
    -> createCodexToolboxServerFactory(...)
    -> mcp-server-factory.mjs
```

This mismatch caused the live MCP server to reject initialization with:

```text
toolAllowlist contains tools not registered by this server configuration:
codex.git_fetch_origin
```

The Secure MCP Tunnel therefore remained live but reported `503` readiness with an MCP initialize failure.

The correction moved the semantic registration into the actual live `mcp-server-factory.mjs` path, limited it to `publicPreview`, retained the allowlist entry, removed the unused duplicate experimental registration, and updated the focused regression test to validate the live factory rather than the unused factory.

No authority widening was required for this correction.

The final focused local contract test passed:

```text
node --check src/surface-contracts.mjs             PASS
node --check src/public-server-factory.mjs         PASS
node --check src/mcp-server-factory.mjs            PASS
node test/bounded-git-fetch-origin.mjs              PASS

Bounded semantic git_fetch_origin live-factory contract PASS
```

## 3. Final semantic action contract

The caller-visible action is:

```text
name    codex.git_fetch_origin
title   Fetch Origin for Trusted Project
schema  strict empty object
```

Caller-controlled values remain:

```text
command             NONE
cwd                 NONE
remote              NONE
URL                 NONE
refspec             NONE
branch              NONE
credentials         NONE
permission profile  NONE
```

The fixed backend call remains:

```javascript
executor.exec({
  command: ["git", "fetch", "origin"],
  access: "inherit",
  timeoutMs: 30_000,
})
```

The conservative annotation contract remained unchanged from Validation 017:

```text
readOnlyHint:     false
destructiveHint:  true
idempotentHint:   false
openWorldHint:    true
```

The ChatGPT discovery rendering did not expose the raw annotation object, so those values were verified from the local source/contract test rather than inferred from the host UI.

## 4. Surface and tunnel refresh

The unmodified Codexless `0.1.1-preview.5` public allowlist contained 42 total actions. Three of those app-only actions are private to the MCP app UI:

```text
codex.agent_card_state
codex.agent_commit
codex.agent_decline
```

Therefore the pre-experiment surface was:

```text
total MCP actions          42
private app-only actions    3
publicly callable actions  39
```

Adding `codex.git_fetch_origin` produced:

```text
total MCP actions          43
private app-only actions    3
publicly callable actions  40
```

After the live-factory correction:

```text
Codexless /healthz       200 / healthy / toolCount 43
Tunnel /healthz          200 / live
Tunnel /readyz           200 / ready
```

The existing ChatGPT developer MCP app was then refreshed through its `Vernieuwen` action. A fresh disposable ChatGPT discovery check reported all 40 publicly callable tools and exposed `codex.git_fetch_origin` with an empty caller schema.

## 5. Authority invariants before dispatch

The pre-dispatch discovery check confirmed:

```text
permission ceiling        ads-direct-git
effective inherit profile ads-direct-git
profile extends            :workspace
authority source           host-profile-override
sandbox                    workspaceWrite
explicit writable root     .git
inherit networkAccess      true
readOnly downscope         :read-only
trusted ADS root           unchanged
```

The read-only inspection lane remained downscoped even though the inherit ceiling had the bounded Git metadata/network authority required for the experiment.

No `codex.process`, Codex agent, wrapper, alternate Git command, permission widening, ACL widening, new remote, or credential forwarding was introduced.

## 6. Exact execution result

Immediately before the semantic fetch:

```text
branch
    v1-source-vault-bootstrap-resume

local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

upstream
    origin/v1-source-vault-bootstrap-resume

upstream commit
    ca42678c9873d350ab5dd9d2b577f36eecdc5854

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 12]

working tree
    clean
```

`codex.git_fetch_origin` was then invoked exactly once.

Result:

```text
exit status                 0
stdout                      empty
stderr                      empty
requested access            inherit
effective permission        ads-direct-git
permission ceiling          ads-direct-git
authority source            host-profile-override
```

No outer ChatGPT/OpenAI block occurred. The semantic tool reached local Codex execution and the fixed Git fetch succeeded.

## 7. Post-dispatch verification

Read-only inspection after the successful action reported:

```text
branch                       unchanged
local HEAD                   063fdc99c76d7821efc58bb83823bcad33c068c5
upstream commit              ca42678c9873d350ab5dd9d2b577f36eecdc5854
status                       identical / behind 12
working tree                 clean / unchanged
```

`.git/FETCH_HEAD` was demonstrably refreshed:

```text
before timestamp  2026-09-01T16:45:08.3729850Z
after timestamp   2026-09-01T17:25:19.4063452Z
length before     8711 bytes
length after      8711 bytes
SHA-256 before    f1e35235bc0b4679e1577222d36fc8e6ce3bd3007a8104eefe340feafb91592d
SHA-256 after     f1e35235bc0b4679e1577222d36fc8e6ce3bd3007a8104eefe340feafb91592d
```

The timestamp change proves the fetch rewrote/refreshed `FETCH_HEAD`. The identical length and digest show that the fetched reference content available at that moment was unchanged.

The semantic fetch did not update local `HEAD`, merge anything, or change working-tree files, which is normal Git fetch behavior.

## 8. A/B interpretation

The completed comparison is:

```text
A: generic codex.command_exec + git fetch origin
   -> BLOCKED BY CHATGPT/OPENAI BEFORE LOCAL EXECUTION

B: bounded codex.git_fetch_origin + same underlying authority backend
   -> DISPATCHED AND EXECUTED SUCCESSFULLY, EXIT 0
```

This supports the narrower conclusion that the MCP action contract materially affected dispatchability for this operation. The strongest changed variables were the semantic action identity/description/schema and removal of arbitrary caller command authority. The underlying trusted ADS root, `ads-direct-git` authority ceiling, inherit network state, and Codex App Server command/exec execution primitive did not need to become broader.

This result does not prove that semantic naming alone determines ChatGPT safety behavior, that every bounded semantic tool will be allowed, or that Git operations are categorically allowed. It proves this exact bounded semantic fetch contract in this exact tested environment.

## 9. Verified classification

```text
SEMANTIC_GIT_FETCH_TOOL_CONTRACT      VERIFIED
LIVE PUBLIC MCP REGISTRATION          VERIFIED
CHATGPT APP REFRESH                   VERIFIED
PUBLIC CALLABLE DISCOVERY             40 / PASS
CODEx.GIT_FETCH_ORIGIN DISCOVERY      PASS
INHERIT AUTHORITY                     ads-direct-git / PASS
INHERIT NETWORK                       true / PASS
READONLY DOWNSCOPE                    :read-only / PASS
OUTER CHATGPT DISPATCH                PASS
LOCAL CODEX COMMAND/EXEC              PASS
GIT FETCH ORIGIN                      PASS / EXIT 0
FETCH_HEAD REFRESH                    PASS
WORKING TREE PRESERVATION             PASS
PULL / COMMIT / PUSH / RESET / REBASE NOT TESTED / NOT ACCEPTED
SOURCE VAULT                          PAUSED / UNCHANGED
```

## 10. Boundary and next step

This validation closes the fetch-specific question opened by Validation 017.

It does not close the broader question of direct checked-out-branch synchronization. A future semantic fast-forward pull action would have a materially different effect because it can update local `HEAD` and working-tree files.

Therefore no `codex.git_pull_ff_only` implementation is authorized by this record. If the project continues that investigation, it must first freeze a separate bounded contract with explicit fast-forward-only semantics, clean-tree/precondition behavior, caller authority, failure modes, postconditions, and stop conditions.

Until that stronger operation is either verified or deliberately deferred, the already-proven formal Codex permission-aware route remains available for local synchronization.

The Source Universe and permanent Source Vault were not touched by this validation.