# Bounded semantic strict-fast-forward Git pull contract frozen

**Date:** 2026-09-01  
**Status:** `SEMANTIC_GIT_PULL_FF_ONLY_CONTRACT_FROZEN / LOCAL IMPLEMENTATION AUTHORIZED / DISPATCH NOT YET TESTED`  
**Result:** `CONTROLLED STRICT-FAST-FORWARD SYNCHRONIZATION EXPERIMENT FROZEN`  
**Scope:** Define the smallest next semantic MCP experiment for synchronizing the checked-out ADS branch after Validation 018 proved bounded model-free `git fetch origin` dispatch.  
**Authority:** Bounded local-execution validation design. This record authorizes only the exact experimental implementation and dispatch sequence defined below. It does not accept pull as permanent ADS architecture and does not authorize commit, push, reset, rebase, checkout, merge commits, arbitrary Git commands, generic host-process access, or Source Vault ingestion.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/017_bounded_semantic_git_fetch_mcp_dispatch_experiment_opened.md`, `path:docs/local_execution/validation/018_semantic_git_fetch_origin_dispatch_verified.md`, `path:docs/CURRENT_STATE.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Why this record exists

Validation 018 closed the fetch-specific question:

```text
ChatGPT -> codex.git_fetch_origin -> Codex command/exec -> git fetch origin
    VERIFIED / EXIT 0
```

That result does not prove checked-out-branch synchronization. A pull-like action is materially stronger because it can advance local `HEAD` and replace working-tree file contents.

The next experiment must therefore be frozen separately before any local Codexless source change or semantic pull dispatch.

## 2. Experimental question

The bounded question is:

```text
Can ordinary ChatGPT dispatch one semantic, caller-argument-free,
strict-fast-forward synchronization action for the trusted ADS repository
through the existing Codexless authority path, while preserving a clean-tree
precondition, refusing divergence, and avoiding merge/rebase/reset/checkout
or arbitrary Git authority?
```

This is a controlled capability experiment, not an attempt to route around ChatGPT/OpenAI safety. If the outer host blocks the action, the block is evidence and the experiment stops.

## 3. Exact semantic action

The experimental action is:

```text
name
    codex.git_pull_ff_only

title
    Fast-Forward Trusted ADS Branch

input schema
    strict empty object
```

Caller-controlled values are deliberately absent:

```text
command             NONE
cwd                 NONE
remote              NONE
URL                 NONE
refspec             NONE
branch              NONE
credentials         NONE
permission profile  NONE
merge strategy      NONE
rebase mode         NONE
```

For this first experiment, the branch and upstream are fixed to the current ADS development branch:

```text
branch    v1-source-vault-bootstrap-resume
upstream  origin/v1-source-vault-bootstrap-resume
remote    origin
```

If ADS later moves to another branch, this experimental action must fail closed or be replaced by a separately reviewed contract. The caller must not be allowed to repurpose it dynamically.

## 4. Required preconditions

The semantic action must perform fixed read-only preflight through the existing Codex authority executor before any synchronization mutation.

It must fail closed unless all of the following are true:

```text
trusted repository root
    the existing host-configured ADS root resolved by Codexless

current branch
    exactly v1-source-vault-bootstrap-resume

configured upstream
    exactly origin/v1-source-vault-bootstrap-resume

working tree and index
    clean
    no staged changes
    no unstaged changes
    no untracked files

repository operation state
    no merge/rebase/cherry-pick/revert state that would make branch
    synchronization ambiguous
```

Ignored files do not by themselves make the Git working tree dirty.

A precondition failure must return a bounded diagnostic and must not invoke the synchronization mutation.

## 5. Fixed synchronization command

The first implementation must use the same audited `CodexAuthorityExecutor.exec()` and official Codex App Server `command/exec` primitive used by the verified fetch action.

The mutation is fixed to:

```text
git pull --ff-only --no-rebase --no-tags --no-recurse-submodules origin v1-source-vault-bootstrap-resume
```

with:

```text
access     inherit
timeout    30 seconds
profile    host-resolved ads-direct-git ceiling
cwd        no caller-supplied cwd
```

The explicit flags are part of the contract:

```text
--ff-only
    refuse any update that cannot be represented as a strict fast-forward

--no-rebase
    prevent repository/user pull.rebase configuration from turning the action
    into a rebase

--no-tags
    avoid an unnecessary tag-fetch expansion for this branch synchronization

--no-recurse-submodules
    avoid recursively updating/fetching submodules as part of this first test
```

No shell string, wrapper, arbitrary argv, alternate remote, caller-selected branch, force option, reset, checkout, rebase, or merge-commit path may be exposed.

## 6. Git-configured behavior boundary

A fast-forward working-tree update can still exercise normal Git behavior associated with the trusted repository and host Git configuration, including checkout filters or hooks if such behavior is configured.

For this experiment, those mechanisms are not granted as new caller authority. They are part of the already trusted local Git/repository environment. However the implementation must not add, edit, enable, or widen hooks, filters, credential helpers, global Git configuration, or repository configuration to make the experiment pass.

If implementation inspection discovers an active hook/filter configuration that materially broadens the expected effect beyond ordinary tracked-file replacement, stop and preserve that fact before dispatch rather than silently treating it as irrelevant.

## 7. Postconditions and verification

Before mutation, capture through read-only operations at least:

```text
branch
upstream
local HEAD
remote-tracking HEAD
status --short --branch
clean-tree result
```

After a successful exit status, use only read-only inspection to establish:

```text
branch remains exactly v1-source-vault-bootstrap-resume
working tree remains clean
index remains clean
local HEAD after
origin/v1-source-vault-bootstrap-resume after
local HEAD == origin-tracking HEAD
```

If `HEAD` changed, additionally verify that the pre-operation `HEAD` is an ancestor of the post-operation `HEAD`. This independently supports strict fast-forward behavior.

The tool must not auto-retry an uncertain or failed mutation. It must not attempt rollback with reset/checkout/rebase or any other compensating write. If the pull may have executed but postcondition evidence is incomplete, return a fail-visible uncertain result and require read-only inspection.

## 8. MCP annotations

The semantic action remains a truthful write/open-world action. The first contract uses the same conservative hint values as the verified fetch experiment:

```text
readOnlyHint:     false
destructiveHint:  true
idempotentHint:   false
openWorldHint:    true
```

Rationale:

- local `HEAD` and working-tree files may change, so it is not read-only;
- tracked files can be replaced by the newer fast-forward state, so the first experiment keeps the destructive hint conservative;
- the remote may change between calls, so idempotence is not claimed;
- the action contacts the configured GitHub remote, so it is open-world.

The annotations must not be weakened merely to influence host dispatch.

## 9. Minimal Codexless implementation boundary

Starting from the verified local fetch patch, the expected source change is limited to the public semantic surface:

```text
src/surface-contracts.mjs
    add codex.git_pull_ff_only to PUBLIC_TOOL_ALLOWLIST

src/mcp-server-factory.mjs
    register codex.git_pull_ff_only only for publicPreview
    strict empty caller schema
    fixed preflight
    fixed synchronization command
    fixed read-only postflight verification
    preserve existing authority evidence in the result

test/bounded-git-pull-ff-only.mjs
    focused regression for exact schema, command, preconditions,
    annotations, public-only registration and absence of caller authority
```

Expected surface after the experimental local patch:

```text
total MCP actions          44
private app-only actions    3
publicly callable actions  41
```

Do not modify the generic public command policy, expose `codex.process`, change Codex authority resolution, broaden filesystem/network permissions, change ACLs, alter Secure MCP Tunnel authority, or touch Source Universe state.

## 10. Authority invariants

The first experiment retains the already-audited authority boundary:

```text
CODEXLESS_PROFILE                ads-direct-git
trusted ADS root                 unchanged
filesystem                       :workspace + explicit .git write
inherit network                  enabled
readOnly downscope               :read-only
Secure MCP Tunnel                unchanged
ACL repair                       unchanged
Source Universe                  untouched
browser authority                unchanged
credentials                      existing Git/Codex environment only
```

No `danger-full-access`, unsandboxed public process tool, arbitrary shell, credential forwarding, new remote, global Git mutation, or permission widening is authorized.

## 11. Controlled dispatch sequence

After the local implementation is syntax/contract tested and the live MCP runtime/app surface is refreshed:

```text
1. verify total/public tool counts and discovery of codex.git_pull_ff_only;
2. verify the caller schema is empty and the action description matches this contract;
3. verify inherit still resolves to ads-direct-git with networkAccess=true;
4. verify readOnly still resolves to :read-only;
5. record branch, local HEAD, upstream HEAD, status and cleanliness read-only;
6. invoke codex.git_pull_ff_only exactly once;
7. if ChatGPT/OpenAI blocks before local execution, stop immediately;
8. if local execution is reached, do not retry automatically on failure/uncertainty;
9. perform only the frozen read-only postcondition checks;
10. preserve the exact result before expanding the Git surface further.
```

Do not use `codex.command_exec` as a fallback to run pull. Do not use `codex.process`, a Codex agent, a wrapper, or an alternate Git mutation to rescue a blocked semantic action during this experiment.

## 12. Interpretation matrix

```text
blocked before dispatch
    outer ChatGPT/OpenAI safety did not dispatch this stronger semantic action;
    stop without workaround

precondition failure
    semantic tool behaved safely and no pull mutation should occur

dispatched but Git refuses non-fast-forward/divergence
    expected fail-closed behavior; no reset/rebase/merge workaround

dispatched and strict fast-forward succeeds
    bounded model-free checked-out-branch synchronization is empirically proven
    for this exact branch/tool contract

postcondition uncertain
    mutation may have occurred; no retry or rollback; inspect read-only and preserve
```

A successful result still does not accept commit, push, arbitrary checkout, reset, rebase, merge commits, force behavior, or general-purpose Git execution.

## 13. Stop conditions

Stop before implementation or dispatch if any of the following becomes necessary:

```text
caller-supplied command/remote/refspec/branch authority
public codex.process exposure
permission-profile widening beyond the current ads-direct-git boundary
loss of readOnly -> :read-only downscope
trusted ADS-root change
ACL or Secure MCP Tunnel widening
Git configuration/hook/filter mutation to make the test pass
Source Universe mutation
force/reset/rebase/checkout fallback
```

Those conditions require a new design decision rather than silent scope expansion.

## 14. Current classification

```text
SEMANTIC_GIT_FETCH_ORIGIN                 VERIFIED
SEMANTIC_GIT_PULL_FF_ONLY_CONTRACT        FROZEN
LOCAL PULL TOOL IMPLEMENTATION            AUTHORIZED / NOT YET PERFORMED
CHATGPT PULL DISPATCH                     NOT YET TESTED
DIRECT MODEL-FREE CHECKOUT SYNCHRONIZATION NOT YET PROVEN
MC-0009 CLAUDE RESPONSE                   DEFERRED / NON-BLOCKING
SOURCE VAULT                              PAUSED / UNCHANGED
```

This record is the implementation authority for the next local Codexless pull experiment. No stronger Git capability is implied.