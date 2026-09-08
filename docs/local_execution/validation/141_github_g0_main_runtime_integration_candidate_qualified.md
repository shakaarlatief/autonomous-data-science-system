# Validation 141: GitHub G0 Main-Runtime Integration Candidate Qualified

**Date:** 2026-09-08
**Status:** PASS / MAIN-RUNTIME SOURCE INTEGRATION CANDIDATE QUALIFIED / DEPENDENCY PROVISIONING BLOCKS LIVE RELEASE
**Research:** Research 123
**Scope:** Compose the qualified GitHub G0 kernel into the current Codexless public-runtime construction while preserving the existing public tool surface, lazy/no-network startup, and explicit dependency-packaging boundary.

## 1. Private implementation result

The integration candidate is preserved in the private local-runtime repository at:

```text
6ce0da8818a455731acc10ba231ef9f52c0c8206
```

Candidate root:

```text
.ads-private/codexless/github-g0-runtime-integration-candidate/
```

It contains the previously qualified G0 modules plus:

```text
src/github-runtime-kernel.mjs
src/codexless-runtime.mjs
test/github-g0-runtime-integration.mjs
README.md
```

Private publication passed the normal integrity policy:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

## 2. Runtime composition

The candidate adds `createGitHubRuntimeKernel` to public-preview runtime construction. The kernel is deliberately lazy.

Ordinary Codexless startup with no GitHub App client ID:

```text
keyring import       0
credential read      0
GitHub network call  0
public github tools  0
```

A configured future internal caller may resolve services lazily. Only then is the exact protected-store adapter imported and token/device-flow/REST/GraphQL/authority services constructed.

The runtime metadata contains only non-secret facts:

```text
configured
initialized
authMode = github-app-user-token-device-flow
host = github.com
restApiVersion = 2026-03-10
protectedStorePackage = @napi-rs/keyring
protectedStoreVersion = 2.0.0
publicActionsRegistered = 0
```

The client ID itself, device code, token values and keyring contents are not exposed by this metadata.

## 3. Public-surface invariant

The candidate intentionally does not replace `surface-contracts.mjs` or `mcp-server-factory.mjs`.

Therefore:

```text
current public tool count  63
new github.* actions        0
```

This is an internal-kernel integration only. It does not claim G1 or action-level parity.

## 4. Focused integration regressions

Final candidate checks:

```text
source syntax             9 / 9 PASS
integration tests         4 / 4 PASS
secret-scanner matches    0
real GitHub requests      0
real credential writes    0
```

The four integration cases prove:

```text
unconfigured startup is lazy and performs no keyring/network work
configured services initialize once without contacting GitHub
missing keyring fails explicitly with no plaintext fallback
runtime composition adds no public GitHub tool registration
```

## 5. Release-v1 dependency blocker

Inspection of the currently qualified Runtime Release v1 implementation establishes:

```text
allowed release target roots = src / test / scripts / config
root package.json target      = not allowed
package-lock target           = not allowed
node_modules target           = not allowed
release publisher             = source-file replacement/add only
regression NODE_PATH          = live install node_modules
```

The exact `@napi-rs/keyring@2.0.0` package is not already available in the live runtime dependency tree; its prior host qualification used temporary staging that was removed afterward.

Therefore a live G0 publication now would be incomplete. The source can be published, but the first configured GitHub action would fail when the lazy keyring import is reached.

This is a **deployment dependency-provisioning gap**, not a G0 logic or Windows compatibility gap.

## 6. Correct next step

Do not commit native `node_modules` binaries to Git, do not smuggle them through a source-file release, and do not add runtime self-install/network behavior on first credential access.

The next work is to design and qualify a bounded dependency provisioning/rollback extension to the Runtime Release architecture. It must preserve exact package identity/version/integrity, deterministic staging, rollback, no caller-selected package authority, and no arbitrary install command.

```text
VALIDATION141=PASS
G0_MAIN_RUNTIME_SOURCE_INTEGRATION=QUALIFIED
PRIVATE_RUNTIME_HEAD=6ce0da8818a455731acc10ba231ef9f52c0c8206
INTEGRATION_TESTS=4_OF_4_PASS
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
LIVE_G0_RELEASE=BLOCKED_BY_DEPENDENCY_PROVISIONING
RUNTIME_RELEASE_V1_PACKAGE_PROVISIONING=NOT_SUPPORTED
NEXT=DESIGN_BOUNDED_RUNTIME_DEPENDENCY_PROVISIONING
```
