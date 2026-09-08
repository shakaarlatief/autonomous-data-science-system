# Validation 147: GitHub Authorization Flat Fresh Host and Live Plugin Name Qualified

**Date:** 2026-09-08
**Status:** PASS / FRESH-HOST FLAT SCHEMA + METADATA LIVE / LIVE PLUGIN DISPLAY NAME CONFIRMED / APP PERMISSION MANIFEST NEXT
**Research:** Research 123
**Scope:** Preserve the fresh disposable ChatGPT qualification of preview.25 `codex.github_authorization`, close the preview.24 union-genericization discriminator, and qualify the current live ChatGPT Plugin display name before GitHub App registration/device-flow work.

## 1. Live ChatGPT Plugin display name

The project owner supplied a ChatGPT UI screenshot showing the connected custom Plugin under the display name:

```text
Codexless Runtime Bridge
```

This matches the canonical forward-looking name selected at Checkpoint 370. The screenshot is direct current UI evidence that the live ChatGPT Plugin/display name has now been renamed from the historical `ADS Codexless Local Bridge` label.

Historical evidence that recorded the old exact label remains valid and is not rewritten. `ADS` remains the name of the complete Autonomous Data Science System, while `Codexless Runtime Bridge` is the custom connector/Plugin name.

This validation qualifies the **ChatGPT Plugin display name**. It does not imply that every historical package identifier, tunnel identifier, internal compatibility string or repository artifact has been renamed, and it does not rewrite identifiers whose exact historical spelling is part of evidence.

## 2. Fresh-host tool discovery

After refreshing the renamed Plugin and opening a fresh disposable ChatGPT conversation, the host projected:

```text
codex.github_authorization
```

The exact tool name and full description were visible. A separate action title and MCP annotation block were not visible in the host projection.

## 3. Preview.25 host schema is structured and flat

The fresh host projected one flat bounded object rather than the preview.24 generic map.

Host-visible schema:

```text
action
    required
    enum:
        metadata
        begin
        status
        poll
        cancel
        clear

requestId
    optional string
    minLength 1
    maxLength 128
    pattern ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$

authorizationRef
    optional string
    pattern ^gha_[0-9a-f]{48}$

confirmClear
    optional literal true
```

The fresh host exposed:

```text
no top-level oneOf
no top-level anyOf
no discriminated union
no generic { [key: string]: any } index signature
```

The host rendering did not separately print an `additionalProperties: false` keyword. It nevertheless presented only the bounded named properties above and no arbitrary-property/index-signature surface. Therefore this validation records the exact host observation without claiming a separately rendered `additionalProperties` keyword.

Local MCP wire qualification at Validation 146 remains authority that the active server schema itself has `additionalProperties=false`.

## 4. Machine constraints versus semantic cross-field rules

The flat host schema intentionally makes every accepted field visible while not encoding action-specific combinations as a top-level union.

The tool description supplies semantic rules such as:

```text
metadata            reads non-secret authorization metadata only
begin               uses server-configured client ID; same-runtime requestId reuse is idempotent
status              operates on one exact in-memory authorizationRef
poll                contacts only the fixed GitHub OAuth token endpoint for that ref
cancel              invalidates one exact pending local ref
clear               requires explicit disconnect intent and confirmClear=true
```

The active Runtime Bridge additionally enforces exact action/field combinations server-side with `GITHUB_AUTHORIZATION_INPUT_INVALID`, as qualified by Validation 146.

## 5. No caller-controlled credential or transport authority

The fresh-host schema exposes none of:

```text
GitHub client ID
client secret
access token
refresh token
device_code
OAuth scope
arbitrary URL
HTTP method
HTTP headers
keyring payload
package selector/path
filesystem path
command/process authority
arbitrary GitHub API authority
arbitrary transport authority
```

The description explicitly reinforces that credential-bearing and transport-authority inputs remain server-owned.

## 6. Exactly one metadata invocation

The fresh disposable conversation invoked `codex.github_authorization` exactly once with:

```text
action = metadata
```

No `begin`, `status`, `poll`, `cancel`, `clear`, or `github.*` parity action was invoked.

The complete returned result was:

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

The metadata call reached Runtime Bridge successfully and was not blocked by host safety controls.

## 7. Side-effect boundary

The metadata result contained no:

```text
user code
verification URI
authorizationRef
device_code
access token
refresh token
credential receipt
```

Under the qualified metadata contract, the call performs only non-secret protected-store/configuration metadata readback. It did not begin device flow, poll OAuth, create/delete credentials, issue a GitHub API request, or expose token material.

Current live authorization state remains:

```text
GitHub App client ID configured  false
stored authorization             false
live GitHub authorization        NOT STARTED
```

## 8. Preview.24 -> preview.25 discriminator closes

The exact host discriminator is now:

```text
preview.24 local strict top-level union
    -> fresh host generic map
    -> metadata host-safety-blocked

preview.25 local strict flat object
    -> fresh host structured bounded flat object
    -> metadata successfully dispatched and returned
```

This strongly supports the already preserved AB-008 design rule for mutation-sensitive developer-MCP actions: prefer one bounded flat top-level object when the ChatGPT host genericizes top-level unions.

The evidence does not require a stronger universal claim about every possible host safety classification. It establishes that the flat correction resolved this concrete authorization-support qualification failure.

## 9. Next gate: exact GitHub App permission manifest

The authorization support surface is now host-qualified. Actual GitHub authorization must still not begin because metadata confirms that no server-owned GitHub App client ID is configured.

Before registering/configuring the GitHub App, the canonical Research 123 architecture requires the exact permission manifest to be mechanically derived from official endpoint requirements for the observed parity surface. The next work is therefore:

```text
- derive repository / organization / account permission requirements for the 89-action target;
- identify actions requiring no explicit App permission beyond user/install access;
- distinguish read vs write levels;
- preserve endpoint-specific permission evidence and conflicts;
- freeze the minimal superset needed for practical parity;
- only then register/configure the dedicated GitHub App and enable device flow.
```

No client ID, secret or token belongs in ordinary Git. When configuration begins, only the non-secret client ID may enter the fixed server-owned runtime configuration path; token material remains protected-store only.

```text
VALIDATION147=PASS
LIVE_PLUGIN_DISPLAY_NAME=Codexless Runtime Bridge
PLUGIN_DISPLAY_RENAME=QUALIFIED
FRESH_PREVIEW25_HOST_SCHEMA=STRUCTURED_FLAT
FRESH_PREVIEW25_METADATA=PASS
GITHUB_APP_CLIENT_ID_CONFIGURED=false
STORED_GITHUB_AUTHORIZATION=false
LIVE_GITHUB_AUTH=NOT_STARTED
PUBLIC_GITHUB_ACTIONS=0
NEXT=DERIVE_AND_FREEZE_GITHUB_APP_PERMISSION_MANIFEST
```
