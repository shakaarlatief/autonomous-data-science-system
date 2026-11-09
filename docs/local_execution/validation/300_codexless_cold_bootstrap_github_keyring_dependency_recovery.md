# Validation 300: Codexless cold-bootstrap GitHub keyring recovery after laptop restart

**Date:** 2026-11-09
**Status:** MANAGED_RESTART_SUCCEEDED / PROTECTED_GITHUB_AUTH_REFRESHED / RUNTIME_BRIDGE_GITHUB_READ_AND_BOUNDED_GIT_FETCH_PASS
**Scope:** Preserve a narrowly bounded, non-secret operational recovery of the local Codexless GitHub authorization and host Git path after a Windows laptop update/restart. This is not R0-P03 source adjudication, experiment scoring, credential reauthorization, or a change to the active project architecture.
**Prior evidence:** Validation 210 (bootstrap and managed-release dependency distinction), Validation 251 (same exact transient keyring error and successful managed-restart recovery), evergreen `docs/local_execution/OPERATIONS.md`.
**Scientific state:** R0-P03 original and independent ten-record reviews and the owner-only private comparison remain unchanged; actual adversarial adjudication remains pending.

## 1. Initial observations

The owner restarted the existing `codexless-http.cmd` foreground launcher and the separate existing tunnel-client profile after their laptop update. Codexless reported the expected `127.0.0.1:7690/mcp` listener and `codexless-public-preview-v2` surface. The Runtime Bridge's workspace authority `show` was reachable and returned registered `ads-public` at the expected local repository. The local Git branch was clean at `604eeb34f863f48f339b46239439ef132d939557`. A separate connected GitHub plugin compared that commit to the named branch and returned `identical` with ahead/behind zero.

The Runtime Bridge's own `github_fetch` and `codex_github_authorization({action:"metadata"})` failed with:

```text
the OS-backed GitHub credential store is unavailable; plaintext fallback is forbidden
```

This failure did **not** prove GitHub-side token revocation or that the GitHub App installation was removed. The owner's GitHub **Authorized GitHub Apps** screenshot showed `Codexless Runtime Bridge` still listed, last used within the previous week. A separate sandbox-scoped Windows service probe found `VaultSvc` running, while sandbox `git ls-remote` could not connect to github.com; neither observation identified the root cause of the server's keyring dependency failure, nor did it prove host Git push unavailable.

## 2. Exact authorized recovery action and terminal result

Following the directly matching prior Validation 251, one bounded managed restart was requested through `codex_runtime_maintenance`, leaving the managed tunnel in place:

```text
action       restart_codexless
requestId    r0p03.github-store-deps-rebind.20261109.01
operationId  rm_36b662a0710165a01e8bf1eb51b74cc3
initial      armed
intermediate running
terminal     succeeded
errorCode    null
recoveryAttempted false
```

This **managed restart** is not equivalent to merely re-launching the cold-bootstrap `.cmd` entrypoint. No credential-store security bypass, plaintext token fallback, GitHub App revocation, credential clearing, device-flow reauthorization, OS ACL relaxation, runtime release publication or unrelated process termination was performed.

## 3. Independent postflight checks

The same Runtime Bridge's protected GitHub authorization metadata became readable. Initially it reported:

```text
configured=true
authorized=true
storedAuthorization=true
accessExpired=true
refreshExpired=false
refreshRecommended=true
```

A normal authenticated Runtime Bridge `github_fetch` returned **HTTP 200** for the exact `v1-source-vault-bootstrap-resume` GitHub branch, matching remote commit `604eeb34f863f48f339b46239439ef132d939557`.

A subsequent metadata read confirmed that the normal protected token-refresh path had completed:

```text
configured=true
authorized=true
storedAuthorization=true
accessExpired=false
refreshExpired=false
refreshRecommended=false
```

Finally, the purpose-specific host-path `codex_git_fetch_origin({workspaceId:"ads-public"})` returned **exit code 0** on the configured server-owned `origin`, branch and upstream. This verifies GitHub API read plus bounded host Git fetch through Runtime Bridge after the restart. No new commit or push was necessary for this recovery; an actual new push is therefore not inferred from the fetch result.

## 4. Durable lesson and boundaries

On future cold launcher restarts, distinguish HTTP service health from active release dependency binding, then check protected GitHub metadata and one bounded GitHub read. When this **same exact keyring error** recurs, first inspect the existing operational precedent and consider the bounded, idempotent **managed restart**, with terminal-status reconciliation. A failed managed restart can leave Codexless unavailable, requiring the documented owner-local cold-bootstrap recovery; do not repeatedly restart blindly.

The user's GitHub authorization screen is a server-side grant witness, not local credential availability. The separate ChatGPT GitHub plugin is a useful independent remote witness and fallback, but is not equivalent to the Codexless protected credential store or purpose-specific Git host-path control plane.

```text
VALIDATION_300=MANAGED_CODEXLESS_RESTART_REBOUND_GITHUB_KEYRING
GITHUB_APP_REVOKED=NO_OBSERVED_EVIDENCE
CREDENTIAL_STORE_METADATA=PASS
PROTECTED_REFRESH_PATH=PASS
GITHUB_API_BRANCH_READ=HTTP_200
BOUNDED_GIT_FETCH_ORIGIN=PASS
GITHUB_CREDENTIAL_CLEAR_OR_REAUTHORIZATION=NOT_PERFORMED
PUBLIC_REPOSITORY_SCIENTIFIC_STATE=UNCHANGED
R0_P03_ADVERSARIAL_CHALLENGE=PENDING
S3_WORLD=WORLD_UNFROZEN
S4_GOLD_AND_B0_B4_SCORING=NOT_STARTED
CHECKPOINT=898_UNCHANGED
SPECIFICATION_028=UNCHANGED
```
