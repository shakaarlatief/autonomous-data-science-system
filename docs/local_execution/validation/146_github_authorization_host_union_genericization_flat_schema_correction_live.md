# Validation 146: GitHub Authorization Host Union Genericization Reproduced, Flat Schema Correction Live

**Date:** 2026-09-08
**Status:** PASS / FRESH-HOST FAILURE EXPLAINED TO THE CURRENT EVIDENCE BOUNDARY / FLAT SCHEMA LIVE / FRESH-CHAT REQUALIFICATION NEXT
**Research:** Research 123
**Scope:** Preserve the fresh-chat host projection and safety-block result for `codex.github_authorization`, reproduce the local-vs-host schema discrepancy, apply the previously qualified AB-008 flat-object correction, and live-qualify preview.25 without beginning GitHub authorization.

## 1. Fresh-chat host result from preview.24

A refreshed fresh disposable ChatGPT conversation projected:

```text
codex.github_authorization
```

The action name and full description were visible, but no separate title or MCP annotations were visible in the host projection.

The decisive host-visible input schema was genericized to:

```text
{
  [key: string]: any
}
```

The host therefore did not expose the locally declared:

```text
action enum
requestId field / bounds / regex
authorizationRef field / regex
confirmClear literal
required fields
additionalProperties=false
top-level branch structure
```

The six semantic operations remained recoverable only from the tool description:

```text
metadata
begin
status
poll
cancel
clear
```

No GitHub action or other connector/tool was invoked in that fresh-chat discovery except the one permitted metadata attempt.

## 2. Host safety block

The fresh chat invoked `codex.github_authorization` exactly once with:

```text
action = metadata
```

The host returned only:

```text
Deze toolaanroep is geblokkeerd door de veiligheidscontroles van OpenAI. Controleer nogmaals wat je verzendt.
```

No Runtime Bridge metadata payload was returned.

Therefore the following actual values were **not** observable through that fresh-host call:

```text
configured
initialized
authorized
storedAuthorization
authMode
host
restApiVersion
```

The blocked attempt returned no user code, verification URI, token material, credential receipt, or device-flow state. There is no evidence that the Runtime Bridge handler was dispatched.

The evidence establishes co-occurrence of:

```text
host-genericized top-level union schema
host safety block before tool result
```

It does **not**, by itself, prove that schema genericization was the sole cause of the safety block.

## 3. Local MCP wire schema remained strict

Direct read-only inspection of the active preview.24 MCP `tools/list` showed that the server itself was not genericized. Its exact live input schema was a top-level JSON Schema `oneOf` containing six closed objects, each with `additionalProperties=false` and action-specific required fields.

For example:

```text
metadata -> required action only
begin -> required action + requestId
status/poll/cancel -> required action + authorizationRef
clear -> required action + confirmClear=true
```

This reproduces the earlier AB-008 discriminator from Runtime Maintenance:

```text
strict local top-level union
-> ChatGPT host generic map
```

rather than a server-side validation failure.

## 4. Chosen correction

The previously qualified Research 122 / AB-008 correction was reused instead of inventing a new host workaround.

The public GitHub authorization schema is now one strict flat top-level object:

```text
action            required enum(metadata, begin, status, poll, cancel, clear)
requestId         optional string, min 1, max 128,
                  ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
authorizationRef  optional string, ^gha_[0-9a-f]{48}$
confirmClear      optional literal true
additionalProperties = false
```

No top-level `oneOf`, `anyOf`, or discriminated union remains.

Exact per-action cross-field rules remain server enforced:

```text
metadata            no optional control fields
begin               requestId only
status/poll/cancel  authorizationRef only
clear               confirmClear=true only
```

Invalid cross-field combinations return:

```text
GITHUB_AUTHORIZATION_INPUT_INVALID
```

This preserves the bounded authority contract while making every accepted caller field visible at the host projection layer.

## 5. Candidate qualification

Private candidate / release source is preserved at:

```text
ad10aa30342503d303b6a22629fe56dc914f0fa2
Flatten GitHub authorization host schema
```

Private push integrity:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

Focused candidate checks passed:

```text
source/test syntax                       8 / 8 PASS
authorization integration               4 / 4 PASS
public surface registration             PASS / tools=64
GitHub auth flat MCP wire schema         PASS
full staged release regression set      16 / 16 PASS
secret scanner                          0 matches
```

The wire regression explicitly proves:

```text
type = object
no top-level oneOf
properties = action, authorizationRef, confirmClear, requestId
required = [action]
action enum = metadata/begin/status/poll/cancel/clear
requestId bounds/pattern preserved
authorizationRef pattern preserved
confirmClear const=true preserved
additionalProperties=false
```

## 6. Live Runtime Release

The corrected immutable release is:

```text
releaseId               github-auth-control-flat-v2
manifest schema         codexless.runtime-release-bundle.v2
target version          0.1.1-preview.25-github-auth-flat
target surface          codexless-public-preview-v2
target tool count       64
file count              3
regression count        16
runtime dependency      github-keyring-win32-x64
manifest SHA-256        a71dda9a430b292ca7fd0c16d2db95dc31e577b23f474dc83590c145032e5447
```

Live preparation returned:

```text
status                   prepared
runtimeDependencyCount   1
fileCount                3
```

Prepublication verification correctly returned three mismatches because the target source was not installed yet.

Publication operation:

```text
operationId   rm_6215ff67fd5ca530af3ca953b0cad03a
requestId     r123.github.auth.flat.publish.20260908.01
status        succeeded
errorCode     null
recovery      not attempted
```

Postpublication verification returned zero mismatches.

Activation operation:

```text
operationId        rm_accbd4edacc46458cae81dd493173feb
requestId          r123.github.auth.flat.activate.20260908.01
status             succeeded
errorCode          null
recoveryAttempted  false
```

Fresh postactivation verification returned:

```text
targetVersion            0.1.1-preview.25-github-auth-flat
targetToolCount          64
runtimeDependencyCount   1
mismatchCount            0
```

## 7. Live local schema and metadata after correction

A fresh direct local MCP `tools/list` now returns the flat schema exactly as intended:

```text
type                 object
required             [action]
additionalProperties false
action.enum          metadata, begin, status, poll, cancel, clear
requestId            bounded optional string
authorizationRef     bounded optional string
confirmClear         optional const true
oneOf                absent
```

A direct local metadata-only call still returns:

```text
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

No device flow, credential write, token creation or GitHub OAuth/API request was started.

## 8. Current interpretation

The host union-genericization portion is now a direct reproduction of the same class already qualified for `codex.runtime_maintenance`:

```text
preview.18 union -> generic host map
preview.19 flat object -> structured host projection
preview.24 auth union -> generic host map
preview.25 auth flat object -> fresh-host requalification pending
```

The metadata safety block may be downstream of the genericized authority surface, but that causal link is not yet proven. The preview.25 fresh-host test is the correct discriminator.

## 9. Next gate

Refresh the current renamed developer-MCP Plugin and open a fresh disposable ChatGPT conversation.

Discovery-only first:

```text
confirm codex.github_authorization is projected
capture its complete host-visible schema
require a structured flat object, not a generic map
```

The expected host-visible machine schema is now:

```text
action required, six-value enum
requestId optional, 1..128 + regex
authorizationRef optional + regex
confirmClear optional const true
additionalProperties=false
no top-level union
```

Then invoke exactly once:

```text
action = metadata
```

Do not begin/poll/cancel/clear device flow in that test.

A PASS requires both:

```text
structured flat host schema
metadata call reaches Runtime Bridge and returns non-secret current state
```

```text
VALIDATION146=PASS
FRESH_PREVIEW24_HOST_SCHEMA=GENERIC_MAP
FRESH_PREVIEW24_METADATA_CALL=HOST_SAFETY_BLOCKED
RUNTIME_HANDLER_DISPATCH=NOT_ESTABLISHED
LOCAL_PREVIEW24_UNION_SCHEMA=STRICT
AB008_UNION_GENERICIZATION=REPRODUCED
PRIVATE_RUNTIME_HEAD=ad10aa30342503d303b6a22629fe56dc914f0fa2
LIVE_RUNTIME_VERSION=0.1.1-preview.25-github-auth-flat
PUBLIC_TOOL_COUNT=64
RUNTIME_DEPENDENCY_COUNT=1
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=FRESH_CHAT_GITHUB_AUTHORIZATION_FLAT_SCHEMA_AND_METADATA_REQUALIFICATION
```
