# Bounded semantic Git fetch MCP dispatch experiment opened

**Date:** 2026-09-01  
**Status:** `EXPERIMENT AUTHORIZED / IMPLEMENTATION PENDING / NO ARCHITECTURE ACCEPTANCE YET`  
**Result:** `CONTROLLED SEMANTIC-TOOL A/B EXPERIMENT FROZEN`  
**Scope:** Define the smallest first experiment for testing whether ordinary ChatGPT can dispatch a bounded local Git fetch through Codexless when Git is exposed as a narrow semantic MCP action instead of an arbitrary command tool.  
**Authority:** Bounded local-execution validation design. This record authorizes only the experiment defined below; it does not accept a new permanent execution architecture.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/016_direct_git_acl_repair_network_profile_and_outer_tool_safety_boundary.md`, `path:docs/DEVELOPMENT_METHOD.md`

## 1. Routing decision

MC-0009 originally made Claude's independent Message 001 a blocking prerequisite before implementation of a new direct-Git MCP architecture.

On 2026-09-01 the project owner explicitly chose to proceed with the smallest controlled experiment without waiting for Claude. Claude review remains deferred and may still provide later counter-design value, but it is no longer a gate for this experiment.

This does not convert the experiment into accepted architecture. The experiment must still be falsifiable, narrow, reversible, and independently evidenced.

## 2. Starting evidence

Validation 016 established the current layered boundary:

```text
ChatGPT reaches Codexless                           PASS
model-free command/exec                            PASS for permitted commands
ads-direct-git selected                            PASS
trusted ADS root                                   PASS
.git explicit write projection                     PASS
stale workspace-capability DENY ACL                CONFIRMED + REPAIRED
previous .git/FETCH_HEAD permission denial         RESOLVED
inherit networkAccess=true                         PASS
readOnly -> :read-only                             PASS
readOnly network widening absent                   PASS
final generic git fetch dispatch                   BLOCKED BEFORE LOCAL EXECUTION
```

The remaining unproven question is whether the outer ChatGPT safety decision is tied materially to the broad generic MCP command contract or whether bounded local Git fetch is categorically blocked even when exposed as a semantic action.

## 3. Exact Codexless source seam inspected

The evaluated local Codexless release remains:

```text
Codexless version    0.1.1-preview.5
source revision      ae9ee9201431a1241786ca938cb67f2e1b017f2b
```

The exact public source shows:

```text
src/public-server-factory.mjs
    registers codex.command_exec as a caller-supplied argv tool
    caller may choose command, cwd, access and timeout within the schema
    annotations are:
        readOnlyHint     false
        destructiveHint  true
        idempotentHint   false
        openWorldHint    true

src/surface-contracts.mjs
    PUBLIC_TOOL_ALLOWLIST contains 42 tools
    codex.command_exec is the only generic model-free command surface
    codex.process exists only on the broader household/workbench surface

src/public-runtime.mjs
    public command execution is backed by CodexAuthorityExecutor
    CODEXLESS_DEFAULT_CWD, CODEXLESS_PROFILE and config overrides are host-side

src/codex-authority-executor.mjs
    exec() resolves trusted cwd and permission authority locally
    command/exec is sent to official Codex App Server
    access=readOnly downscopes to :read-only
    access=inherit uses the fixed locally resolved ceiling
```

Therefore the cleanest first A/B test does not require a new host-process lane. The same `CodexAuthorityExecutor.exec()` backend can be used while changing only the public MCP contract from arbitrary argv to one exact Git action.

## 4. Primary-source safety semantics

Current MCP tool annotations are hints rather than security boundaries. Their standard meanings remain:

```text
readOnlyHint
    true only if the tool does not modify its environment

destructiveHint
    true when a modifying action may make destructive/non-additive updates

idempotentHint
    true only when repeating the same call has no additional environmental effect

openWorldHint
    true when the tool interacts with external/open-world entities
```

The experiment must not mislabel Git fetch merely to influence host safety behavior.

OpenAI's current Developer Mode documentation confirms that custom MCP write/modify actions are supported in ChatGPT, that confirmation depends on permissions/context/impact, and that especially risky actions may be blocked instead of offered for approval. It does not document a categorical prohibition on Git fetch.

## 5. First experimental MCP action

The first tool is deliberately semantic and caller-minimal:

```text
name
    codex.git_fetch_origin

title
    Fetch Origin for Trusted Project

input schema
    strict empty object

caller-controlled command            NONE
caller-controlled cwd                NONE
caller-controlled remote             NONE
caller-controlled URL                NONE
caller-controlled refspec            NONE
caller-controlled branch             NONE
caller-controlled credentials        NONE
caller-controlled permission profile NONE
```

Proposed description:

```text
Fetch updated Git references from the existing local `origin` remote for the
Codexless host-configured trusted project. This action runs exactly
`git fetch origin` through official Codex App Server command/exec using the
locally fixed inherited Codex permission profile. The caller cannot provide a
command, cwd, remote, URL, refspec, branch, credentials, or permission profile.
The action does not merge, checkout, reset, rebase, commit, push, or modify
working-tree files. It may update `.git/FETCH_HEAD` and remote-tracking refs
according to normal Git fetch semantics, so it is a write/modify action.
```

The exact first annotations remain deliberately conservative and truthful:

```text
readOnlyHint:     false
destructiveHint:  true
idempotentHint:   false
openWorldHint:    true
```

Rationale:

- fetch writes Git metadata, so `readOnlyHint:true` would be false;
- remote-tracking refs can be rewritten by legitimate remote history changes, so the first test does not claim additive-only behavior;
- the remote can change between calls, so the test does not claim idempotence;
- the operation contacts GitHub through the configured remote, so it is open-world.

Keeping the same conservative four hint values as generic `codex.command_exec` is useful experimentally. If ChatGPT dispatches the semantic tool while blocking generic command execution, the strongest changed variables are tool name/title/description/schema and removal of arbitrary caller-supplied command authority, not annotation laundering.

## 6. Exact backend behavior

The first implementation should use the already-proven public authority executor:

```javascript
executor.exec({
  command: ["git", "fetch", "origin"],
  access: "inherit",
  timeoutMs: 30_000,
})
```

No caller `cwd` is passed. The existing host-configured Codexless default cwd and trusted-root resolver remain authoritative.

The returned structured evidence should preserve at least:

```text
exitCode
stdout
stderr
permissionCeiling
permissionProfile
cwd
authoritySource
trustedAncestor
```

The implementation must not expose `codex.process`, shell strings, command templates, arbitrary Git subcommands, arbitrary remotes, or a generic host-process wrapper.

## 7. Minimal Codexless source-change set

For the experimental local build/patch, change only the smallest necessary public contract surfaces:

```text
src/surface-contracts.mjs
    add codex.git_fetch_origin to PUBLIC_TOOL_ALLOWLIST

src/public-server-factory.mjs
    register codex.git_fetch_origin
    strict empty input schema
    fixed executor.exec call above
    conservative annotations above

test/public-contract.mjs
    update expected public surface and verify the fixed action contract

test/public-registration-allowlist.mjs
    update/verify exact registration allowlist
```

Do not modify `src/public-command-policy.mjs`, do not expose household `codex.process`, and do not broaden `PUBLIC_BASE_INSTRUCTIONS` for the first A/B test unless tool discovery itself proves to be the blocker. The user can explicitly request the named tool, so changing server-wide instructions would add an unnecessary experimental variable.

If implementation mechanics require an additional focused test file, that is acceptable, but the public runtime authority model must remain unchanged.

## 8. Local authority invariants

The existing machine-local authority boundary must remain unchanged for the first experiment:

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
```

No `danger-full-access`, generic unsandboxed process tool, credential forwarding, new remote URL, or broad host filesystem authority may be introduced to make the test pass.

## 9. Controlled A/B experiment

The prior A observation is already frozen:

```text
A
surface     codex.command_exec
request     ["git", "fetch", "origin"], access=inherit
result      blocked by ChatGPT/OpenAI safety before local dispatch
```

The first B experiment is:

```text
B
surface     codex.git_fetch_origin
request     {}
backend     fixed ["git", "fetch", "origin"] through same CodexAuthorityExecutor
result      observe exact host behavior
```

Required execution sequence after the experimental Codexless runtime is refreshed:

```text
1. verify the public MCP surface exposes codex.git_fetch_origin;
2. verify project_context still reports ads-direct-git, the trusted ADS root,
   explicit .git writable root, override count 2 and inherit networkAccess=true;
3. separately verify readOnly still resolves to :read-only;
4. explicitly invoke codex.git_fetch_origin once;
5. if ChatGPT presents a normal one-time confirmation, the project owner may
   approve exactly that action;
6. record whether the invocation is blocked before dispatch, reaches Codex and
   fails locally, or succeeds;
7. if it reaches local execution, immediately record local/origin HEAD and
   git status without performing pull, commit, push, reset, rebase or checkout;
8. preserve the exact outcome as the next validation record before expanding
   the Git surface.
```

## 10. Interpretation matrix

```text
B blocked before dispatch
    semantic narrowing alone did not establish dispatchability;
    do not call direct Git impossible yet without examining the exact host
    action classification/permission state and other bounded semantic designs.

B presented for confirmation
    outer host distinguishes the semantic action from the generic command;
    confirmation behavior is itself evidence even before local result.

B dispatched but failed inside Codex
    outer tool-contract hypothesis is supported;
    diagnose only the new inner failure and do not widen unrelated authority.

B dispatched and git fetch succeeds
    model-free ChatGPT -> bounded semantic MCP -> Codex command/exec -> Git
    fetch is empirically proven for the trusted ADS repository.
```

A successful fetch does not yet accept pull/commit/push tools. Each stronger semantic action requires its own contract and risk analysis.

## 11. Why `codex.process` is not the first experiment

The inspected Codexless source explicitly keeps `codex.process` off the public 42-tool surface and treats it as a broader host-process capability. Exposing it now would change both the outer MCP contract and the inner execution/credential boundary at once.

That would make the experiment harder to interpret and would widen authority unnecessarily.

The first test therefore reuses the same official Codex App Server `command/exec` primitive whose filesystem/network profile has already been audited.

## 12. Stop conditions

Stop the first experiment immediately if any of the following occurs:

```text
tool implementation requires generic caller-supplied shell/argv authority
public codex.process exposure becomes necessary
ads-direct-git must be widened beyond the current filesystem/network boundary
readOnly no longer downscopes to :read-only
trusted ADS-root binding changes
Secure MCP Tunnel authority must be broadened
Source Universe or unrelated host state would be touched
```

Those conditions require a new design decision rather than silent scope expansion.

## 13. Current classification

```text
SEMANTIC_GIT_FETCH_TOOL_CONTRACT     FROZEN FOR FIRST EXPERIMENT
LOCAL CODEXLESS IMPLEMENTATION       PENDING
CHATGPT DISPATCH RESULT              NOT YET TESTED
DIRECT MODEL-FREE GIT FETCH          NOT YET PROVEN
MC-0009 CLAUDE RESPONSE              DEFERRED / NON-BLOCKING
SOURCE VAULT                         PAUSED / UNCHANGED
```
