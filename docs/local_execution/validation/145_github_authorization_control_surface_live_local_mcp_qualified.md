# Validation 145: GitHub Authorization Control Surface Live and Local MCP Qualified

**Date:** 2026-09-08
**Status:** PASS / 64-TOOL AUTHORIZATION SUPPORT SURFACE LIVE / LOCAL METADATA QUALIFIED / FRESH CHAT PROJECTION NEXT
**Research:** Research 123
**Scope:** Qualify the explicit GitHub App authorization-control support surface through Runtime Release v2, preserve failed immutable release attempts as evidence, prove the live local MCP schema and metadata-only operation, and keep actual GitHub authorization and all 89 parity actions unstarted.

## 1. Final private implementation boundary

The corrected authorization-control implementation is preserved in the private local-runtime repository at:

```text
private source HEAD   d63bb48112985fd05e4a32925b83e75214dd2a4a
commit                Add GitHub authorization release fix2
private integrity     RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

The support surface adds exactly one public infrastructure tool:

```text
codex.github_authorization
```

This tool is not one of the native connector's fixed 89 parity actions. The remote GitHub parity count therefore remains:

```text
published github.* parity actions = 0 / 89
```

## 2. Bounded authorization-control contract

The live support tool exposes only these semantic operations:

```text
metadata
begin    + requestId
status   + authorizationRef
poll     + authorizationRef
cancel   + authorizationRef
clear    + confirmClear=true
```

`authorizationRef` is an opaque runtime-owned reference with exact shape:

```text
^gha_[0-9a-f]{48}$
```

`begin.requestId` reuses the established bounded request-id contract. The schema exposes no caller-selected:

```text
client id
client secret
access token
refresh token
device_code
OAuth scope
URL
HTTP method
HTTP headers
keyring payload
package id/path
arbitrary transport or host-process authority
```

The server-configured GitHub App client ID remains outside caller arguments. GitHub's device code remains private runtime state. A successful poll may write only the resulting access/refresh pair to the qualified protected OS credential store, never to the MCP result.

## 3. Candidate and release regression evidence

Before live publication, the implementation passed:

```text
authorization-control source syntax      6 / 6 PASS
authorization integration                4 / 4 PASS
combined staged G0/auth focused suite   11 / 11 PASS
public surface registration              PASS / tools=64
secret scanner                           0 matches
```

The integration tests prove:

```text
metadata is non-secret and network-free
metadata can inspect protected-store state even when the GitHub App client ID is absent
begin is same-runtime idempotent by stable requestId
begin exposes userCode / verificationUri / timing but never device_code
status/cancel/poll require one exact runtime authorizationRef
successful fake OAuth polling persists token material only in protected storage
clear removes stored authorization and cancels locally tracked pending attempts
malformed request/reference authority fails closed
```

## 4. Failed immutable release attempts are preserved evidence

Two earlier publication attempts failed for real regression reasons and were not rewritten in place.

### Original `github-auth-control-v2`

The first prepared release was immutable at manifest SHA-256:

```text
01eab65d0af5a578077ce95b30b9db697dc47f0a40740d7aeaebfe72dfb0a74d
```

Publication operation:

```text
rm_477f3feeea2aef0f7b14b9459c55ff58
```

failed with:

```text
RUNTIME_RELEASE_REGRESSION_FAILED
```

The failing public-surface assertion did not yet exclude the newly added support tool from the exact preserved-old-tools comparison.

After that test was corrected, attempting to prepare changed bytes under the same release ID failed closed with the intended immutable-release conflict rather than rebinding the old prepared identity.

### `github-auth-control-v2-fix1`

A new release ID preserved the corrected bytes. Publication operation:

```text
rm_5a9311dad33e4d7203b60630aacc2020
```

again failed `RUNTIME_RELEASE_REGRESSION_FAILED`. Direct reproduction localized two older semantic-Git regressions that still asserted the historical 63-tool public count.

These failures are accepted evidence that:

```text
prepared release identity is immutable
failed regressions prevent publication
support-surface expansion must reconcile every exact tool-count regression
failed releases are preserved rather than silently edited/replayed
```

## 5. Corrected immutable release

The final release is:

```text
releaseId               github-auth-control-v2-fix2
manifest schema         codexless.runtime-release-bundle.v2
target version          0.1.1-preview.24-github-auth-control
target surface          codexless-public-preview-v2
target tool count       64
file count              8
regression count        16
runtime dependencies    [github-keyring-win32-x64]
manifest SHA-256        92554d6da7418885fcb491f1c16a2527517ca09d6c230d0d8a5dc54e1421a7be
```

The exact immutable keyring generation remains:

```text
abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
```

Preparation succeeded with `runtimeDependencyCount=1`. Prepublication verification correctly returned eight source mismatches because the new payload was not yet installed.

## 6. Live publication and activation

Final publication operation:

```text
operationId   rm_137444f8dda39d01c282b2c1d47a9356
requestId     r123.github.auth.control.fix2.publish.20260908.01
action        publish_release
status        succeeded
errorCode     null
recovery      not attempted
```

Postpublication verification returned:

```text
status                   verified
mismatchCount            0
runtimeDependencyCount   1
targetToolCount          64
```

Activation used the bounded runtime-maintenance surface:

```text
operationId        rm_91321739c5b2287e638719a37c2de0b3
requestId          r123.github.auth.control.fix2.activate.20260908.01
action             restart_codexless
status             succeeded
errorCode           null
recoveryAttempted   false
```

Fresh postactivation release verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.24-github-auth-control
targetSurfaceVersion     codexless-public-preview-v2
targetToolCount          64
fileCount                8
runtimeDependencyCount   1
mismatchCount            0
```

## 7. Live local MCP schema qualification

A fresh stateless request to the active loopback MCP endpoint returned `tools/list` successfully. The live serialized tool inventory contains:

```text
codex.github_authorization
```

with the complete six-operation closed schema described above. The active installed `surface-contracts.mjs` likewise reports:

```text
PUBLIC_SERVER_VERSION = 0.1.1-preview.24-github-auth-control
PUBLIC_SOURCE_TOOL_COUNT = 64
```

This establishes that the server publication itself is live and correctly serialized.

## 8. Metadata-only live invocation

Because the current persistent ChatGPT conversation retained a stale callable projection, the new support tool was invoked only through the active local stateless MCP endpoint and only with:

```json
{"action":"metadata"}
```

The live result was:

```text
schemaVersion          codexless.github-authorization.v1
configured             false
initialized            false
authorized             false
storedAuthorization    false
accessExpiresAtMs      null
refreshExpiresAtMs     null
accessExpired          null
refreshExpired         null
refreshRecommended     null
authMode               github-app-user-token-device-flow
host                   github.com
restApiVersion         2026-03-10
surfaceVersion         codexless-public-preview-v2
```

This call did not begin device flow, create a GitHub token, clear a credential, or make a GitHub OAuth/API request. It performed only the intended protected-store metadata read.

The result establishes that no GitHub App client ID is configured in the current runtime environment and no protected GitHub user authorization is stored.

## 9. Same-conversation host projection remains stale

After successful activation, ChatGPT's current persistent developer-MCP projection still does not expose `codex.github_authorization` as a callable projected action even though direct active MCP `tools/list` proves the live server contains it.

This reproduces the previously preserved AB-008 lifecycle pattern:

```text
live server updated and healthy
same persistent conversation retains stale callable projection
fresh conversation required to acquire new tool projection
```

The correct next host qualification is therefore a refreshed **fresh disposable ChatGPT conversation**, not repeated mutation of the live runtime.

## 10. Safety boundary and next gate

No live GitHub authorization has started:

```text
GitHub App client ID configured    false
stored GitHub authorization        false
device flow begun                  false
GitHub token created               false
GitHub API request                 false
public github.* parity actions     0 / 89
```

The next gate is discovery-only plus metadata-only in a fresh ChatGPT conversation:

```text
1. refresh the developer MCP app if required by the governing runbook;
2. open a fresh disposable chat;
3. confirm codex.github_authorization is projected;
4. capture its host-visible schema faithfully;
5. invoke exactly action=metadata once;
6. confirm the same non-secret unconfigured/unauthorized state;
7. do not begin/poll device flow in that qualification.
```

Only after that host gate should Research 123 decide the GitHub App registration/client-ID configuration and actual device-flow qualification boundary. The first read-only parity action bundle remains later.

```text
VALIDATION145=PASS
PRIVATE_RUNTIME_HEAD=d63bb48112985fd05e4a32925b83e75214dd2a4a
LIVE_RUNTIME_VERSION=0.1.1-preview.24-github-auth-control
LIVE_PUBLIC_TOOL_COUNT=64
RUNTIME_DEPENDENCY_COUNT=1
AUTHORIZATION_SUPPORT_TOOL=LIVE_LOCAL_MCP
LIVE_AUTH_METADATA=PASS
GITHUB_APP_CLIENT_ID_CONFIGURED=false
STORED_GITHUB_AUTHORIZATION=false
LIVE_GITHUB_AUTH=NOT_STARTED
PUBLIC_GITHUB_ACTIONS=0
SAME_CHAT_TOOL_PROJECTION=STALE
NEXT=FRESH_CHAT_GITHUB_AUTHORIZATION_SCHEMA_AND_METADATA_QUALIFICATION
```
