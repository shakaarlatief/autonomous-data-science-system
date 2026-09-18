# Validation 210: GitHub Keyring Release-Dependency Restart Recovery Qualified

**Date:** 2026-09-18
**Status:** PASS / ROOT CAUSE LOCALIZED / CONTROLLED RESTART RECOVERED GITHUB / EVERGREEN RUNBOOK HARDENED
**Scope:** Preserve the resolved failure in which a directly launched Codexless runtime remained broadly healthy while its active managed release's GitHub keyring runtime dependency was not bound into the worker, causing GitHub calls to fail with `GITHUB_KEYRING_UNAVAILABLE`.
**Authority:** Historical operational validation evidence. The evergreen procedure is `docs/local_execution/OPERATIONS.md`. This record does not change the active PKA-G013 route, project-knowledge authority, GitHub authorization policy or runtime-release contract.

## 1. Incident summary

An out-of-band ChatGPT diagnostic on 2026-09-18 encountered a GitHub-only failure after Codexless had otherwise started normally.

Reported incident state:

```text
runtime version   0.1.1-preview.47-browser-current-plugin-compat-public
surface           codexless-public-preview-v2
tool count        172
GitHub error      GITHUB_KEYRING_UNAVAILABLE
```

The local ADS checkout and its Git remote were healthy. The GitHub tools were present. The failure occurred before an ordinary GitHub repository read could reach GitHub.

The protected-store error meant the running GitHub runtime could not access the OS-backed credential/keyring layer. Plaintext credential fallback remained intentionally unavailable.

## 2. Why ordinary health was misleading

The active managed release declared the fixed runtime dependency:

```text
github-keyring-win32-x64
```

and the dependency generation itself was already provisioned.

The direct launcher can start the installed HTTP runtime and register the public tool surface without independently reconstructing the active managed release's runtime-dependency binding. The resulting process can therefore satisfy broad HTTP/tool-surface health while a dependency-backed subsystem is unusable.

The reproduced distinction is:

```text
direct launcher
    -> installed HTTP runtime starts
    -> public tools can register
    -> active release dependency binding is not guaranteed to be reconstructed

bounded runtime-maintenance restart
    -> reads active managed release state
    -> resolves targetDependencies
    -> starts replacement worker with runtimeDependencies
    -> revalidates the replacement runtime
```

This is a runtime lifecycle/binding failure, not evidence that the GitHub App, repository, authorization record or GitHub API contract disappeared.

## 3. Reconciliation with existing architecture

Read-only reconciliation against the current private local-runtime source confirms the dependency-aware restart design.

The one-shot restart supervisor initializes the dependency set from the active release's `targetDependencies` and passes that set to the replacement worker launcher as `runtimeDependencies`. When a pending forward/rollback activation exists, the supervisor selects the corresponding target/previous dependency set.

This matches existing public Validation 144, which had already qualified live Runtime Release v2 activation of `github-keyring-win32-x64` and proved that the replacement worker started with the exact prepared dependency generation.

The new incident therefore does not invalidate the release architecture. It exposes an operational distinction that the old runbook did not preserve strongly enough: a direct launcher start is not equivalent to the semantic restart supervisor once active releases carry runtime dependencies.

## 4. Recovery

The incident was repaired without reinstalling Codexless, replacing GitHub credentials, clearing the protected store, recreating the GitHub App or widening permissions.

The successful recovery used the bounded Codexless runtime-maintenance restart path so the replacement worker inherited the active release dependency context.

Operational conclusion:

```text
active release
    -> targetDependencies
    -> github-keyring-win32-x64
    -> replacement worker runtimeDependencies
    -> protected GitHub credential store available
```

## 5. Independent live post-recovery verification

After receiving the incident record in the formal ADS project chat, `chatgpt-26` independently performed read-only live checks through the recovered Runtime Bridge.

The live Codexless health endpoint independently confirmed the same active runtime identity reported by the incident record:

```text
ok                true
version           0.1.1-preview.47-browser-current-plugin-compat-public
surface           codexless-public-preview-v2
tool count        172
```

`codex.github_authorization` metadata returned:

```text
configured          true
initialized         true
authorized          true
storedAuthorization true
accessExpired       false
refreshExpired      false
authMode            github-app-user-token-device-flow
host                github.com
surface             codexless-public-preview-v2
```

A bounded `github_get_repo` call for the public ADS repository also succeeded and returned the expected repository identity and permission set, including pull, triage, push, maintain and admin.

This verifies the current recovered chain:

```text
Runtime Bridge
    -> protected authorization store
    -> GitHub runtime
    -> installation-authorized repository read
    -> PASS
```

No mutation was required for this qualification.

## 6. Evergreen recovery rule

If GitHub later fails with `GITHUB_KEYRING_UNAVAILABLE` while Codexless HTTP health and the public tool surface still look correct:

```text
1. do not reauthorize GitHub first;
2. verify general Codexless and tunnel health;
3. confirm the GitHub tools remain present;
4. when available, confirm the active release expects the keyring dependency and the dependency generation exists;
5. if the runtime was directly launched, suspect missing release dependency binding;
6. invoke codex.runtime_maintenance restart_codexless with a fresh stable requestId;
7. reconcile that request until durable status=succeeded;
8. verify protected GitHub authorization metadata;
9. verify one bounded read-only github_get_repo call.
```

Only if the semantic restart fails to restore protected-store access should investigation move to token expiry, App installation scope, repository permissions, dependency corruption or credential replacement.

## 7. Runbook correction

The previous evergreen operations text described stop + direct `codexless-http.cmd` relaunch as a controlled restart. That wording is no longer correct for dependency-bound managed releases.

The runbook now distinguishes:

```text
direct launcher
    bootstrap/start path

codex.runtime_maintenance restart_codexless
    preferred semantic replacement path
    required when active managed-release runtime dependencies must be reconstructed
```

For a cold state where no runtime is callable, direct launch may bootstrap the HTTP service. Once Runtime Bridge is reachable, a semantic restart must follow before dependency-backed subsystems are relied upon.

The managed tunnel should remain running for an ordinary Codexless-only semantic restart.

## 8. Project-route impact

This is operational preservation only.

```text
PKA-G001..PKA-G012     PASS / unchanged
PKA-G013               NEXT / unchanged
W1 migration           NOT STARTED
current authority      current continuity architecture
authority switch       false
```

```text
VALIDATION_210=PASS
GITHUB_KEYRING_RECOVERY=QUALIFIED
SEMANTIC_RESTART_DEPENDENCY_REBINDING=REQUIRED_WHEN_APPLICABLE
G013_ROUTE=UNCHANGED
```
