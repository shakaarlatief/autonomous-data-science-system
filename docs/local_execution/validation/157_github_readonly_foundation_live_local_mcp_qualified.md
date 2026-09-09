# Validation 157: GitHub Read-Only Foundation Live Local MCP Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.28 LIVE / FOUR READ-ONLY GITHUB TOOLS LIVE LOCALLY / FRESH-HOST PROJECTION NEXT
**Research:** Research 123
**Scope:** Migrate the stale zero-public-action G0 regression, publish and activate the first bounded `github.*` read-only foundation, live-qualify authenticated identity plus installation-derived repository scope through the active MCP server, and preserve the remaining fresh-ChatGPT-host projection boundary without claiming full 89-action parity.

## 1. Starting boundary

Checkpoint 399 had already established:

```text
GitHub App registered                 true
GitHub App installed                  true
personal installation scope          All repositories
correct Client ID configured          true
device-flow user authorization        true
protected authorization stored        true
access authorization expired          false
refresh authorization expired         false
public github.* tools                 0
```

The next gate was intentionally read-only: prove authenticated identity, installation scope, bounded REST/GraphQL transport, and the first public `github.*` surface before any remote GitHub mutation is published.

## 2. First read-only foundation surface

The new server-owned bundle publishes exactly four `github.*` tools:

```text
github.get_profile
github.get_user_login
github.list_installations
github.list_repositories_by_installation
```

The surface deliberately exposes no caller-selected:

```text
access token
refresh token
client secret
private device code
GitHub host
REST endpoint
GraphQL document
HTTP method
HTTP headers
permission profile
arbitrary transport authority
```

`github.get_profile` and `github.get_user_login` use a fixed server-registered GraphQL viewer query. Installation and repository enumeration use the fixed github.com REST transport plus the protected user token and installation-derived authority.

## 3. Regression migration and immutable release evidence

The first publication attempt exposed stale historical regression assumptions that the G0 kernel must always report zero public GitHub actions. The active design intentionally advances that count to four, so the old assertion was no longer a valid invariant.

The final migrated G0 regression preserves the important parts of the old contract:

```text
unconfigured startup remains lazy
no keyring import before protected services are needed
no GitHub network request during construction
failed keyring initialization remains explicit and retryable
runtime construction still delegates tool registration to the MCP server factory
```

while updating only the now-obsolete public-action-count expectation from `0` to `4`.

The successful immutable private-runtime source head is:

```text
a18983d2b2199f350d07664cfe91dbf013e2df3c
```

The final release is:

```text
releaseId               github-readonly-foundation-v3
targetVersion           0.1.1-preview.28-github-readonly-foundation
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         68
fileCount               8
runtimeDependencyCount  1
manifestSha256          41ebfb14993a81d6b97be3113f9167cb108e9d6dd68077ab73eba0ca942f64a8
```

Publication operation:

```text
operationId   rm_d607e555f858e60d7ae5c253fcc71215
requestId     r123.github-readonly-v3.publish.20260909.01
status        succeeded
errorCode     null
recovery      not attempted
```

Activation operation:

```text
operationId        rm_86a5699c3cf0160932348716698b4230
requestId          r123.github-readonly-v3.restart.20260909.01
status             succeeded
errorCode           null
recoveryAttempted   false
```

Fresh postactivation release verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.28-github-readonly-foundation
targetToolCount          68
fileCount                8
runtimeDependencyCount   1
mismatchCount            0
```

## 4. Live process and tunnel health

Direct local health after activation returned:

```text
ok             true
service        codexless-public
transport      streamable-http
version        0.1.1-preview.28-github-readonly-foundation
toolCount      68
surfaceVersion codexless-public-preview-v2
```

The already-running managed tunnel remained healthy:

```text
/healthz  HTTP 200 / live
/readyz   HTTP 200 / ready
```

No tunnel restart was required.

## 5. Protected authorization survived activation

A postrestart `codex.github_authorization metadata` read returned:

```text
configured           true
initialized          false
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
authMode             github-app-user-token-device-flow
host                 github.com
restApiVersion       2026-03-10
```

`initialized=false` is healthy after a new worker start because the GitHub runtime remains lazy until one read-only action first requests services. Protected token storage survived the restart without exposing credential values.

## 6. Live local MCP tools/list qualification

A fresh stateless initialize against the active loopback MCP endpoint returned exactly 68 tools and contained all four new names.

The serialized input contracts are:

```text
github.get_profile
    strict empty object

github.get_user_login
    strict empty object

github.list_installations
    manageable_only: boolean = false
    no additional properties

github.list_repositories_by_installation
    installation_id: integer, required
    page_size: integer = 20
    page_offset: integer = 0
    no additional properties
```

The public schema deliberately follows the captured native input shape rather than adding speculative machine-readable bounds that the native host never projected. The Runtime Bridge still applies semantic server-side validation, including positive installation IDs, positive page size, and non-negative page offset.

## 7. Live GitHub read-only action qualification

The same local MCP session invoked all four new tools through the running public MCP surface.

Observed bounded results:

```text
github.get_profile
    schemaVersion              codexless.github-readonly.v1
    authenticated login        shakaarlatief
    numeric database id        present
    GraphQL node id            present
    public repository count    12

github.get_user_login
    schemaVersion              codexless.github-readonly.v1
    login                      shakaarlatief

github.list_installations
    manageable_only            false
    installation count         1
    installation id            present, not reproduced here
    repositorySelection        all

github.list_repositories_by_installation
    totalCount                 12
    returnedCount              12
    hasMore                    false
    canonical public ADS repo  present
```

The qualification intentionally did not print the other repository names. No access token, refresh token, private device code, Authorization header or credential-store payload appeared in the MCP results.

The successful `github.get_profile` call also establishes that the server-owned GraphQL transport works against live GitHub with the current App user authorization for this bounded viewer query. It does **not** close the separate empirical permission sufficiency requirement for the eight pull-request/review GraphQL operations preserved by Research 123.

## 8. Explicit partial-parity boundary

The four names are live public Runtime Bridge tools, but Research 123 must not yet claim four fully qualified native-parity rows.

One known native-contract gap remains explicit:

```text
github.list_installations manageable_only=true
    -> GITHUB_PARITY_OPTION_NOT_QUALIFIED
```

The native connector description says this option limits installations to managed setup account types, but the exact account-type/filter semantics were not projected. Runtime Bridge therefore fails closed rather than inventing a filter.

Accordingly:

```text
live public github.* foundation tools     4
full exact 89-action parity rows closed   0
remaining native rows                     89
```

This distinction can be tightened after fresh-host qualification and any targeted native-result evidence needed for the unresolved option.

## 9. Same-conversation ChatGPT projection is stale

The active local server exposes 68 tools and direct MCP `tools/list` contains all four new actions. This persistent `chatgpt-21` conversation, however, still exposes the earlier connector function projection and none of the four new `github.*` names through the ChatGPT connector resource layer.

This reproduces the already accepted AB-008 lifecycle pattern:

```text
live MCP surface changed and verified
same persistent ChatGPT conversation retains old callable projection
fresh conversation required for new action projection
```

The count difference alone is not the stale-projection proof. The decisive evidence is that all four exact expected new names are present in live MCP `tools/list` and absent from the current conversation's callable connector projection.

## 10. Next host qualification

The next gate is a refreshed fresh disposable ChatGPT conversation after the existing `Codexless Runtime Bridge` Plugin is refreshed/rescanned according to `docs/local_execution/OPERATIONS.md`.

That fresh conversation should:

```text
1. discover the four exact new github.* names;
2. capture their host-visible schemas before invocation;
3. invoke github.get_profile once;
4. invoke github.get_user_login once;
5. invoke github.list_installations with manageable_only=false once;
6. use the returned installation id only to invoke
   github.list_repositories_by_installation with page_size=20 and page_offset=0 once;
7. confirm the canonical ADS repository is in scope;
8. perform no GitHub mutation;
9. do not clear or restart authorization.
```

```text
VALIDATION157=PASS
PRIVATE_RUNTIME_HEAD=a18983d2b2199f350d07664cfe91dbf013e2df3c
LIVE_RUNTIME_VERSION=0.1.1-preview.28-github-readonly-foundation
LIVE_MCP_TOOL_COUNT=68
LIVE_GITHUB_FOUNDATION_TOOLS=4
LOCAL_MCP_TOOLS_LIST=PASS
LIVE_PROFILE_READ=PASS
LIVE_LOGIN_READ=PASS
LIVE_INSTALLATION_ENUMERATION=PASS
LIVE_REPOSITORY_SCOPE_ENUMERATION=PASS
PERSONAL_INSTALLATION_REPOSITORY_SELECTION=all
PROTECTED_AUTHORIZATION_PRESERVED=true
GRAPHQL_VIEWER_QUERY=PASS
EXACT_PARITY_ROWS_CLOSED=0
KNOWN_PARTIAL_PARITY_GAP=github.list_installations.manageable_only_true
SAME_CHAT_NEW_TOOL_PROJECTION=STALE
NEXT=FRESH_CHAT_GITHUB_READONLY_FOUNDATION_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
