# Validation 156: GitHub Device Flow Client-ID Correction and User Authorization Qualified

**Date:** 2026-09-09
**Status:** PASS / ROOT CAUSE LOCALIZED / USER AUTHORIZATION STORED
**Research:** Research 123
**Scope:** Preserve the interrupted authorization-bootstrap recovery, exact GitHub App Client-ID correction, live device-flow success, and protected user-token storage without exposing credentials.

## 1. Owner-side Device Flow setting ruled out

The project owner supplied a current GitHub App General-settings screenshot showing:

```text
Request user authorization (OAuth) during installation  OFF
Enable Device Flow                                      ON
```

This rules out the previously suspected disabled-Device-Flow setting.

## 2. Exact Client-ID root cause

The first Runtime Bridge device-code request had returned HTTP 404 with JSON `{"error":"Not Found"}` before GitHub supplied any device/user code or token.

A public GitHub App lookup for slug `codexless-runtime-bridge` then returned the live App identity:

```text
App ID      4881901
Owner       shakaarlatief
Slug        codexless-runtime-bridge
Client ID   Iv23lirgmw82wV0SGTWn
```

The previously preserved/configured Client ID contained a transcription error. Direct non-secret transport discrimination established:

```text
previous value -> POST /login/device/code -> HTTP 404 / Not Found
live App value -> POST /login/device/code -> HTTP 200 / required device-flow fields present
```

No access token, refresh token or private device code was printed by these diagnostics.

The corrected non-secret Client ID is now the canonical public value. Earlier public occurrences were repaired as a factual identifier correction; Git history preserves the superseded transcription.

## 3. Immutable Runtime Bridge correction

Private local-runtime repository head:

```text
6d641881423ea50e0fdf1329782dd2489735d551
```

Release `github-client-config-v3` corrected the configuration but its first restart exposed a release-contract defect: the target version was advanced without carrying a matching `surface-contracts.mjs` version update. The bounded restart failed visibly and automatic recovery restored the previous healthy runtime.

A new immutable release corrected both the Client ID and runtime identity contract:

```text
releaseId            github-client-config-v4
targetVersion        0.1.1-preview.27-github-client-id-correction
targetToolCount      64
runtimeDependencies  1
```

Publication succeeded, restart succeeded without recovery, and postactivation verification returned:

```text
status         verified
mismatchCount  0
```

The authorization-control regression was also hardened so it proves the status/result surface contains no `clientId` field rather than embedding the concrete Client ID as a test literal.

## 4. Live device authorization

Before the corrected begin call, live metadata returned:

```text
configured           true
initialized          false
authorized           false
storedAuthorization  false
```

Exactly one corrected Runtime Bridge `begin` call then succeeded and returned a pending authorization attempt with a GitHub verification URI and user code while retaining the private `device_code` inside the runtime.

After the project owner completed GitHub authorization, exactly one poll of that same authorization reference returned:

```text
status  authorized
```

The subsequent metadata read returned:

```text
configured           true
initialized          true
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
authMode             github-app-user-token-device-flow
host                 github.com
restApiVersion       2026-03-10
```

A status read of the consumed authorization reference then returned `GITHUB_DEVICE_FLOW_REF_UNKNOWN`, confirming the in-memory pending device-flow session was removed after successful token storage.

No access token or refresh token value was exposed in the MCP result or committed to Git.

## 5. Security/bootstrap state

The owner had already confirmed deletion of the locally downloaded GitHub App PEM before live authorization proceeded. Runtime Bridge still uses no App private-key/JWT authority and no Client secret was generated.

```text
VALIDATION156=PASS
DEVICE_FLOW_SETTING=ON
CLIENT_ID_TRANSCRIPTION_DEFECT=CORRECTED
RUNTIME_VERSION=0.1.1-preview.27-github-client-id-correction
RUNTIME_RELEASE_VERIFY=PASS
GITHUB_USER_AUTHORIZED=true
PROTECTED_AUTHORIZATION_STORED=true
ACCESS_TOKEN_EXPOSED=false
REFRESH_TOKEN_EXPOSED=false
CLIENT_SECRET_GENERATED=false
LOCAL_PEM_DELETION=CONFIRMED_BY_OWNER
NEXT=QUALIFY_AUTHENTICATED_IDENTITY_INSTALLATION_SCOPE_AND_FIRST_READ_ONLY_GITHUB_ACTIONS
```
