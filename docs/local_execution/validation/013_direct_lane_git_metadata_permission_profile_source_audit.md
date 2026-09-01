# Direct-lane Git metadata permission-profile source audit

**Date:** 2026-09-01  
**Status:** SOURCE AUDIT COMPLETE / PREFERRED BOUNDED PROFILE IDENTIFIED / LOCAL RUNTIME VALIDATION PENDING  
**Scope:** Determine whether the accepted Codexless direct `command_exec` lane can perform ordinary ADS Git metadata writes without a full Codex agent turn by changing only the bridge-local Codex permission profile, while preserving the existing trusted-project and public-tool boundaries.  
**Authority:** Bounded technical evidence for the post-Research-105 direct-lane authority audit. This record does not itself authorize Source Vault ingestion or claim that the candidate profile has passed local runtime validation.  
**Declared references:** `research:105`, `checkpoint:270`, `path:docs/local_execution/validation/002_codexless_local_install_doctor_ready.md`, `path:docs/local_execution/validation/012_controlled_write_read_delete_local_operation_verified.md`, `path:docs/CURRENT_STATE.md`

## 1. Question

Research 105 closed successfully as `ACCEPTED_FOR_ADS_LOCAL_EXECUTION`, but the controlled proof exposed one important asymmetry:

```text
ordinary direct workspace writes       PASS
sandboxed direct command execution     PASS
.git/FETCH_HEAD write                  DENIED by current command/exec sandbox
formal Codex approval-aware Git pull   PASS after exact one-time approval
```

The follow-up question is whether ADS can make routine repository-local Git operations available through the same direct ChatGPT -> Codexless -> Codex App Server `command/exec` lane without launching a model-bearing Codex agent merely to cross the `.git` boundary.

The project owner explicitly permits loosening security restrictions that ADS itself introduced when that is useful, but the target remains the smallest practical authority rather than unrestricted host access.

## 2. Exact evaluated versions

The source audit was deliberately pinned to the versions that produced the accepted Research 105 evidence.

```text
Codexless version                 0.1.1-preview.5
Codexless source revision         ae9ee9201431a1241786ca938cb67f2e1b017f2b
local Codex CLI                   0.151.0
OpenAI Codex 0.151.0 tag commit   78c290807ce710180111df227df3b7a4fe845452
```

OpenAI released Codex 0.152.0 on 2026-09-01, but the capability needed for this experiment is already present in the exact locally installed 0.151.0 source. An upgrade is therefore not a prerequisite for the bounded validation.

## 3. The `.git` denial is a Codex workspace-policy behavior

The exact Codex 0.151.0 permission implementation constructs the built-in workspace-write policy by granting write access to project roots and then adding default read-only project-root subpaths for:

```text
.git
.agents
.codex
```

This matches the observed Research 105 failure at `.git/FETCH_HEAD`.

The important implementation detail is that the metadata guard is not an unconditional global prohibition. The same 0.151.0 implementation checks whether a protected metadata path has a more specific explicit write entry. If such an entry exists beneath the protected metadata root, the metadata-write denial no longer applies to that path.

Therefore the observed failure is not evidence that Git metadata is impossible through `command/exec`. It is evidence that the current inherited `:workspace` profile intentionally does not contain an explicit `.git` write grant.

## 4. Codex 0.151.0 supports a narrower custom profile

The exact 0.151.0 configuration model supports named user permission profiles with:

```text
extends
workspace_roots
filesystem
network
```

The profile resolver can inherit from the built-in `:workspace` profile. Filesystem permissions support scoped entries, including a `:workspace_roots` scope with a specific subpath and access mode.

This is sufficient to express the desired policy conceptually as:

```toml
[permissions.ads-direct-git]
extends = ":workspace"

[permissions.ads-direct-git.filesystem.":workspace_roots"]
".git" = "write"
```

Because the child profile extends `:workspace`, ordinary workspace behavior remains. Because only `.git` receives the additional scoped write grant, `.agents` and `.codex` keep the inherited protected/read-only treatment. User-defined profiles compile with restricted network access unless network permissions are explicitly widened.

## 5. The installed Codexless revision can inject and fix that profile locally

The exact installed Codexless revision already provides both required host-side controls:

```text
CODEXLESS_CONFIG_OVERRIDES_FILE
CODEXLESS_PROFILE
```

`CODEXLESS_CONFIG_OVERRIDES_FILE` must contain local JSON of the form:

```json
{
  "overrides": [
    "key=value"
  ]
}
```

Codexless passes every supplied override to the Codex App Server as `-c key=value` before `app-server --stdio`.

The exact OpenAI Codex override machinery preserves raw inline permission maps and literal scoped keys. A bridge-local override equivalent to the TOML profile can therefore be represented as the candidate:

```text
permissions.ads-direct-git={extends=":workspace",filesystem={":workspace_roots"={".git"="write"}}}
```

with:

```text
CODEXLESS_PROFILE=ads-direct-git
```

This exact string remains a **runtime-validation candidate**, not a frozen operational fact, until the local 0.151.0 bridge successfully parses, lists and executes under it.

## 6. Codexless keeps remote profile escalation closed

This candidate does not require allowing ChatGPT to choose arbitrary Codex profiles.

The installed Codexless authority executor treats `CODEXLESS_PROFILE` as a host-side profile override. It validates that the profile is currently allowed by Codex and requires the command working directory to remain under an explicitly trusted Codex project/root. For an `inherit` command, the fixed host profile becomes the permission ceiling. A caller requesting `readOnly` is still downscoped to `:read-only`.

The direct remote call therefore remains structurally:

```text
ChatGPT caller
    chooses command + cwd + readOnly/inherit

Codexless host policy
    fixes trusted ADS root
    fixes ads-direct-git permission ceiling
    rejects untrusted cwd
    rejects arbitrary remote profile selection

Codex App Server
    enforces the custom filesystem policy
```

This is materially different from giving the remote caller a `danger-full-access` switch.

## 7. Alternative host-process lane exists but is not preferred

The evaluated Codexless source also contains `codex.process`, backed by Codex App Server `process/spawn`. Codex itself defines `process/spawn` as a standalone host process launched without a Codex sandbox. Codexless explicitly describes this as suitable for host Git metadata and credential-store operations.

However, `codex.process` is intentionally excluded from the public 42-tool surface currently exposed through the ADS Secure MCP Tunnel. It belongs to the broader household/workbench surface.

Exposing that surface would solve the `.git` problem by bypassing the command sandbox, but it would enlarge the public tool surface and introduce an unsandboxed host-process primitive. That is unnecessary if the narrower custom `command/exec` profile works.

Therefore the preferred order is:

```text
1. bounded custom command/exec profile
2. keep existing public 42-tool surface
3. keep process/spawn unexposed
4. consider host-process exposure only if the bounded profile cannot satisfy required Git operations
```

## 8. ChatGPT plug-in permission is a separate layer

The current ChatGPT connection permission was inspected during this audit and remains on the user's default low-risk-action policy. No app-level broadening was performed.

That setting is not the root cause of the `.git/FETCH_HEAD` denial. The denied command already reached the local Codex command sandbox. Changing ChatGPT to `Allow all actions` would therefore not, by itself, add `.git` write permission inside Codex.

The app permission can be reconsidered only if a later direct call is blocked at the ChatGPT action-policy layer. It should not be widened preemptively to solve a lower-layer filesystem policy that has a narrower remedy.

## 9. Selected local-validation candidate

The preferred candidate for the next controlled diagnostic is:

```text
profile id                         ads-direct-git
base profile                       :workspace
additional write                   :workspace_roots/.git
.agents                            inherited protected/read-only
.codex                             inherited protected/read-only
unrelated host filesystem          no new write grant
network                            restricted unless explicitly changed
public Codexless surface           unchanged / 42 tools
codex.process                      not exposed
remote profile selection           not exposed
Codex model turn                   not required for command_exec
```

The machine-local override file must remain outside public Git. It is execution configuration, not public repository authority.

## 10. Controlled local validation plan

The next diagnostic must remain bounded and reversible.

1. Re-read the public branch HEAD immediately before local synchronization.
2. Verify the local ADS branch and working tree are clean.
3. Fast-forward only to the then-current `origin/v1-source-vault-bootstrap-resume` when required.
4. Materialize the candidate Codexless config-overrides JSON only in the approved machine-local/private operational surface.
5. Restart the existing public Codexless bridge with `CODEXLESS_PROFILE=ads-direct-git` and the override file.
6. Run Codexless doctor/authority validation and prove that Codex lists and accepts `ads-direct-git` as the fixed host profile ceiling.
7. Prove that `readOnly` calls still resolve to `:read-only`.
8. Run a direct `command_exec` Git metadata operation with `access=inherit`. The preferred first operation is `git fetch origin`, because it exercises `.git/FETCH_HEAD` without changing tracked working-tree files.
9. Verify the command succeeds without launching a Codex model turn and without formal agent approval.
10. Verify the working tree remains clean and record any remote-tracking movement separately from working-tree mutation.
11. If the local branch is behind after the fetch, use a strict `git pull --ff-only origin v1-source-vault-bootstrap-resume` through the same direct lane and verify the resulting HEAD exactly.
12. Verify the protected Source Universe state remains unchanged.
13. Preserve evidence and explicitly classify the direct profile before using it for permanent Source Vault work.

No Source Registry, Source Vault, original corpus, `.ads-private` secrets, backup/recovery artifact, browser authority or unrelated host path is part of this diagnostic.

## 11. Current conclusion

The source audit materially narrows the problem.

The preferred architecture is no longer "make Codex unrestricted" and is no longer "run a full Codex agent whenever Git needs `.git`". The installed stack appears to support a third path:

```text
public ChatGPT bridge
    -> existing public Codexless command_exec
    -> fixed bridge-local custom profile extending :workspace
    -> explicit .git write only under trusted workspace roots
    -> ordinary Git metadata operations without a model-bearing agent turn
```

This is source-supported by the exact installed Codexless revision and the exact Codex 0.151.0 release implementation. It remains **LOCAL RUNTIME VALIDATION PENDING** until the real ADS bridge proves the profile can be parsed, selected and used successfully on the local checkout.

Source Vault ingestion remains paused and unchanged during that validation.