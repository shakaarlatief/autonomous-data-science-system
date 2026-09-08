# Validation 144: GitHub G0 Keyring Generation Live Activation Qualified

**Date:** 2026-09-08
**Status:** PASS / EXACT KEYRING GENERATION ACTIVE / PUBLIC GITHUB ACTIONS STILL ZERO / AUTH SURFACE NEXT
**Research:** Research 123
**Scope:** Qualify the first live Runtime Release v2 dependency activation for the exact server-owned GitHub keyring package generation, while preserving the 63-tool public surface and keeping live GitHub authorization disabled.

## 1. Private v2 release bundle

The private local-runtime repository now preserves:

```text
private source HEAD   19a4d1852f99f0d10d1a5b4bca23c0f39d825bb1
releaseId             github-g0-keyring-activation-v2
manifest schema       codexless.runtime-release-bundle.v2
target version        0.1.1-preview.23-github-g0-keyring
target surface        codexless-public-preview-v2
target tool count     63
file count            2
regression count      15
runtime dependency    github-keyring-win32-x64
manifest SHA-256      33d8b19ae09c10f602857828e1257c8e5db1d050646d9769eeb9c09ee6ff81f1
```

The v2 manifest exposes only the fixed dependency id. Package name, version, registry, platform package, integrity hashes, install command, destination and worker path remain server-owned.

The private release-bundle commit is:

```text
19a4d1852f99f0d10d1a5b4bca23c0f39d825bb1
Add GitHub G0 keyring activation release
```

Its private push passed:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

## 2. Real exact-generation smoke before publication

Before the live release was committed, a fresh real dependency preparation plus exact worker-binding smoke imported `@napi-rs/keyring` only through the immutable runtime dependency resolver.

The smoke passed against:

```text
dependencyId  github-keyring-win32-x64
treeSha256    abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
Entry         function
```

No credential value was read or written. Scratch package state was removed after the child process exited.

The same smoke is included as the fifteenth release regression. It requires exactly one bound dependency, resolves the exact root package through the prepared generation and verifies only that the native keyring `Entry` constructor is present.

## 3. Live Runtime Release v2 preparation

The live dependency-aware runtime prepared the v2 release successfully:

```text
status                   prepared
fileCount                2
runtimeDependencyCount   1
manifestSha256           33d8b19ae09c10f602857828e1257c8e5db1d050646d9769eeb9c09ee6ff81f1
```

Prepublication verification correctly reported the two release payload files as not yet installed while the prepared dependency generation itself validated:

```text
status                   verification_failed
fileCount                2
runtimeDependencyCount   1
mismatchCount            2
```

## 4. Publication

One bounded v2 publication operation was submitted:

```text
operationId   rm_080792c073690364c32fa90c7c1da128
requestId     r123.g0.keyring.publish.20260908.01
action        publish_release
status        succeeded
errorCode     null
```

Publication ran all fifteen declared regressions, including the exact prepared-generation keyring smoke, before exposing pending activation.

Fresh postpublication verification returned:

```text
status                   verified
runtimeDependencyCount   1
mismatchCount            0
```

## 5. Activation

The bounded restart supervisor activated the dependency-aware pending release:

```text
operationId        rm_41cf35130455181ec38697d2aa1ae435
requestId          r123.g0.keyring.activate.20260908.01
action             restart_codexless
status             succeeded
errorCode          null
recoveryAttempted  false
```

The replacement worker had to satisfy the exact target runtime contract while starting with the v2 target dependency binding. Successful activation therefore proves that startup could read and revalidate the prepared immutable generation under the new worker.

## 6. Postactivation evidence

Fresh verification after restart returned:

```text
status                   verified
targetVersion            0.1.1-preview.23-github-g0-keyring
targetSurfaceVersion     codexless-public-preview-v2
targetToolCount          63
fileCount                2
runtimeDependencyCount   1
mismatchCount            0
```

The exact keyring dependency generation is now active for the live worker. The public MCP surface remains 63 tools because this release changes no public allowlist or MCP action registration.

The internal GitHub kernel is still intentionally unconfigured unless `CODEXLESS_GITHUB_APP_CLIENT_ID` is present. No live device flow, token creation, Credential Manager GitHub-token write or GitHub API request has been started by this qualification.

## 7. Next boundary

G0 transport, protected storage and exact package deployment are now live-capable. Before action bundles can use them, Research 123 needs one explicit, bounded authorization-control contract for the developer MCP surface. The native connector manages account authorization outside its 89 action inventory; Codexless therefore needs a deliberate support surface rather than hiding OAuth side effects inside an arbitrary parity action.

The next design/implementation gate is to choose and qualify the smallest public authorization lifecycle that can:

```text
- report configured / authorized metadata without exposing tokens;
- start GitHub App device flow and return only authorizationRef, userCode, verificationUri and timing metadata;
- poll/status/cancel one exact in-memory authorizationRef;
- clear the protected GitHub token record only through explicit user intent;
- expose no client secret, access token, refresh token, device_code, keyring payload, arbitrary URL/header/scope or package authority;
- remain separate from the 89 parity-action count.
```

Only after that support surface is live-qualified should the first read-only parity action bundle be published.

```text
VALIDATION144=PASS
PRIVATE_RUNTIME_HEAD=19a4d1852f99f0d10d1a5b4bca23c0f39d825bb1
KEYRING_RELEASE_ID=github-g0-keyring-activation-v2
KEYRING_MANIFEST_SHA256=33d8b19ae09c10f602857828e1257c8e5db1d050646d9769eeb9c09ee6ff81f1
LIVE_RUNTIME_VERSION=0.1.1-preview.23-github-g0-keyring
RUNTIME_DEPENDENCY_COUNT=1
KEYRING_TREE_SHA256=abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
PUBLIC_TOOL_COUNT=63
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=DESIGN_AND_IMPLEMENT_GITHUB_AUTHORIZATION_CONTROL_SURFACE
```
