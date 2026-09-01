# Direct Git profile runtime application diagnostic

**Date:** 2026-09-01  
**Status:** `DIRECT_GIT_PROFILE_PARTIAL / MACHINE-LOCAL CONFIG MATERIALIZED / HOST-SIDE RESTART REQUIRED`  
**Scope:** Continue the post-Research-105 direct-lane authority audit by attempting to apply the candidate `ads-direct-git` Codex permission profile to the real tunneled Codexless runtime without launching a Codex model agent.  
**Authority:** Bounded local-execution evidence only. This record does not claim that `.git` writes have passed under `ads-direct-git`, does not authorize Source Vault ingestion, and does not supersede the public state/routing authority.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/013_direct_lane_git_metadata_permission_profile_source_audit.md`, `path:docs/CURRENT_STATE.md`

## 1. Diagnostic environment

The disposable diagnostic used only the real ADS checkout:

```text
C:\Projects_Data\autonomous-data-science-system
```

The persistent ADS interaction remained `chatgpt-14`; the diagnostic chat did not allocate a persistent ADS session identity.

Observed starting Git state:

```text
branch
    v1-source-vault-bootstrap-resume

local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    97dac340782d1c823f1d27f9f52f4cf691a651ac

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 6]
```

The working tree was clean. The origin-tracking ref was re-read before local configuration mutation and remained `97dac340782d1c823f1d27f9f52f4cf691a651ac`.

## 2. Live Codexless runtime before candidate application

The real running bridge reported:

```text
Codexless                 0.1.1-preview.5
Codex CLI                 0.151.0
default cwd               C:\Projects_Data\autonomous-data-science-system
trusted root              C:\Projects_Data\autonomous-data-science-system
live permission ceiling   :workspace
readOnly downscope        :read-only
authority source          codex-quiet-profile-resolver
```

The loopback public Codexless service remained healthy and ready on:

```text
127.0.0.1:7690
```

with the existing 42-tool `codexless-public-preview-v1` surface. The Secure MCP Tunnel remained running and was not modified.

## 3. Candidate machine-local configuration materialized

Exactly one durable diagnostic configuration artifact was created in the already Git-ignored private operational surface:

```text
C:\Projects_Data\autonomous-data-science-system\.ads-private\codexless\ads-direct-git-overrides.json
```

Its exact non-secret content is:

```json
{
  "overrides": [
    "permissions.ads-direct-git={extends=\":workspace\",filesystem={\":workspace_roots\"={\".git\"=\"write\"}}}"
  ]
}
```

The intended startup environment is:

```text
CODEXLESS_PROFILE=ads-direct-git
CODEXLESS_CONFIG_OVERRIDES_FILE=<machine-local override file above>
CODEXLESS_DEFAULT_CWD=C:\Projects_Data\autonomous-data-science-system
```

No tracked repository file, Source Registry content, Source Vault content, original source corpus, credential, token, backup payload, recovery artifact, browser configuration, or unrelated host path was changed by this diagnostic.

## 4. Runtime application boundary encountered

A minimum Codexless-only restart/reload was attempted through the existing public direct tool surface without touching the tunnel.

The new environment did not become active.

Afterward, the loopback listener was still owned by the original running Codexless process and a fresh model-free project-context read still reported:

```text
activePermissionProfile   :workspace
config override count     0
```

Therefore the running tunneled service did not inherit either `CODEXLESS_PROFILE=ads-direct-git` or the override file.

This is consistent with the intended public Codexless boundary: the exposed 42-tool surface contains bounded model-free command execution but does not expose generic host-process supervision for restarting the service that implements that surface.

The diagnostic did not fall back to:

```text
danger-full-access
codex.process
unsandboxed generic host execution
Codex model agent
```

## 5. Nested doctor is not a valid substitute for host restart

A doctor invocation launched inside the existing `command_exec` sandbox could not read the host Codexless runtime-routing state or host Codex trust configuration. It failed with host-state isolation errors including an `EPERM` against Codexless runtime-install state and a missing trusted-root view.

This does **not** classify `ads-direct-git` as invalid. It establishes that a nested sandboxed doctor cannot prove a startup profile that has not been applied to the real host-side Codexless process.

Consequently the following remain unproven:

```text
ads-direct-git parses successfully in the real host runtime
ads-direct-git appears as an allowed permission profile
ads-direct-git is the active inherit ceiling
```

The following remain proven from the unchanged live service:

```text
readOnly request -> :read-only
trusted root      -> ADS repository root
inherit ceiling   -> :workspace
```

## 6. Primary Git metadata test deliberately not run

`git fetch origin` was **not** executed.

That was the correct fail-closed behavior. Because the candidate had not become the live profile, running `git fetch` would only repeat the already-understood `:workspace` test and would not validate the candidate.

Therefore:

```text
.git/FETCH_HEAD write under ads-direct-git   NOT TESTED
git pull --ff-only under ads-direct-git      NOT TESTED
```

No Codex model turn was launched and no formal Codex agent approval was used.

## 7. Final Git and protection state

Final Git state remained:

```text
local HEAD
    063fdc99c76d7821efc58bb83823bcad33c068c5

origin/v1-source-vault-bootstrap-resume
    97dac340782d1c823f1d27f9f52f4cf691a651ac

status
    ## v1-source-vault-bootstrap-resume...origin/v1-source-vault-bootstrap-resume [behind 6]
```

The tracked working tree remained clean. No commit, merge, rebase, reset, push, force-update, or GitHub write occurred in the disposable diagnostic.

Protected Source Universe state was not traversed merely to strengthen the assertion. Protection evidence is based on the exact command/path audit, absence of any issued mutation against protected paths, and the clean tracked Git state.

## 8. Classification

The bounded classification is:

```text
DIRECT_GIT_PROFILE_PARTIAL
```

The candidate profile is **not rejected**. Its local configuration is materialized, but runtime application and `.git` write behavior remain unvalidated because the existing service must be restarted from outside its own bounded public MCP surface.

## 9. Smallest next step

No broader permission profile is justified.

The next operation is purely host-side service supervision:

1. stop only the existing Codexless HTTP process bound to loopback port `7690`;
2. keep the Secure MCP Tunnel running;
3. restart the existing installed `codexless-http.cmd` with the candidate startup environment;
4. verify `/healthz` and `/readyz` return healthy again on the same loopback endpoint;
5. from a fresh direct bridge call, verify `ads-direct-git` is the active inherit ceiling while `readOnly` remains `:read-only`;
6. only then run direct `git fetch origin` with `access=inherit`;
7. if successful, verify `.git/FETCH_HEAD` was writable, re-read local/origin HEADs, and perform strict fast-forward pull through the same direct lane only if still required.

The source-audit candidate from validation 013 remains the preferred bounded design. The current blocker is service restart/application, not evidence requiring a more permissive filesystem policy.
