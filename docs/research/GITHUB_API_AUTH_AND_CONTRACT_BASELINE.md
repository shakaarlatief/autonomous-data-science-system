# GitHub API Auth and Contract Baseline

**Date:** 2026-09-08
**Status:** AUTHORITATIVE PLATFORM BASELINE / G0 CONTRACT READY / FIRST REQUEST GAPS CLOSED
**Research:** Research 123
**Scope:** Current official GitHub documentation used to turn the reconciled native connector surface into an implementation-grade GitHub App/auth/REST baseline without inferring hidden native-wrapper wire formats.

## Sources

Current GitHub documentation inspected on 2026-09-08:

```text
https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/about-authentication-with-a-github-app
https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens
https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/best-practices-for-creating-a-github-app
https://docs.github.com/en/rest/apps/installations
https://docs.github.com/en/rest/about-the-rest-api/api-versions
https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api
https://docs.github.com/en/rest/using-the-rest-api/best-practices-for-using-the-rest-api
https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
https://docs.github.com/en/rest/git/trees
https://docs.github.com/en/rest/pulls/pulls
https://docs.github.com/en/rest/repos/contents
```

This artifact records GitHub platform behavior, not hidden native connector wrapper behavior.

## 1. Authentication mode is now implementation-grade

The selected model remains a **GitHub App acting on behalf of the user with a GitHub App user access token**.

Official GitHub guidance distinguishes app, installation and user authentication. For actions taken on behalf of a user, GitHub recommends a user access token because its effective authority is the intersection of:

```text
GitHub App permissions/access
AND
user permissions/access
```

A user access token can access only resources visible to both the installed app and the user. This matches the Research 123 objective better than an installation token for interactive ChatGPT-directed user actions.

The first implementation target therefore does not need a personal access token and should not silently substitute one.

## 2. Device flow contract

For a headless/CLI-style application, GitHub App user access tokens support OAuth 2.0 Device Authorization Grant after device flow is enabled on the GitHub App.

Server flow:

```text
POST https://github.com/login/device/code
    client_id

response
    device_code
    user_code
    verification_uri
    expires_in
    interval

user visits
    https://github.com/login/device

poll
POST https://github.com/login/oauth/access_token
    client_id
    device_code
    grant_type = urn:ietf:params:oauth:grant-type:device_code
```

The documented default device/user-code lifetime is 900 seconds and the example/default polling interval is 5 seconds. Polling faster than the supplied interval yields `slow_down`; GitHub documents `authorization_pending`, `slow_down`, `expired_token`, `unsupported_grant_type`, `incorrect_client_credentials`, `incorrect_device_code`, `access_denied` and `device_flow_disabled` device-flow error codes.

The device flow does not require the client secret for token generation. This supports a narrower G0 configuration surface: the GitHub App **client ID** is required for device authorization, while no client secret needs to be exposed to ChatGPT or stored merely to complete device flow.

## 3. Expiring user-token lifecycle

GitHub recommends expiring user access tokens. Current documented values are:

```text
user access token
    prefix      ghu_
    lifetime    28,800 seconds / 8 hours

refresh token
    prefix      ghr_
    lifetime    15,897,600 seconds / 6 months
```

Using a refresh token invalidates the old refresh token and old user access token. Refresh returns a new access token and refresh token.

For a user token originally generated with device flow, GitHub's refresh documentation explicitly says the client secret is **not required** for refresh. G0 should therefore keep the credential set minimal and rotate both access/refresh tokens atomically.

No token value belongs in tool arguments, logs, ordinary repository files or user-visible error details.

## 4. Installation-derived repository scope is directly supported

With a GitHub App user access token:

```text
GET /user/installations
```

lists installations the authenticated user has explicit permission to access. The endpoint requires a GitHub App user access token and no additional GitHub App permission. GitHub documents page/per_page pagination, with `per_page` maximum 100 and defaults of 30/page 1.

GitHub also documents repository enumeration within an installation through the user-access-token installation repository endpoint. This validates the planned server-owned scope derivation:

```text
user authorization
    -> installations accessible to user + app
    -> repositories accessible within chosen installation
    -> semantic github.* action authority
```

The Runtime Bridge should derive repository authority from GitHub's installation/user intersection rather than inventing a second caller-controlled remote whitelist.

## 5. GitHub App permission model

GitHub App permissions are fine-grained. User-access-token requests succeed only when both the app and user have sufficient access. Official GitHub guidance says to request minimum necessary permissions and endpoint documentation states required permissions.

G0 should therefore represent permissions as server-owned app-registration/configuration facts and fail visibly on insufficient permissions. It should not ask ChatGPT for OAuth scopes, arbitrary token permissions or caller-selected authorization headers.

For REST requests, GitHub may return `X-Accepted-GitHub-Permissions`, which can inform diagnostics without exposing secrets.

## 6. github.com REST transport baseline

GitHub REST is explicitly versioned. As of 2026-09-08 the supported github.com versions are:

```text
2026-03-10    current, no end-of-support scheduled
2022-11-28    supported through 2028-03-10
```

G0 should pin the current github.com target explicitly:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2026-03-10
User-Agent: <fixed Codexless Runtime Bridge application identity>
Authorization: Bearer <server-owned user access token>
```

GitHub requires a valid `User-Agent`; requests without one are rejected. API-version pinning avoids relying on the unversioned default and gives the project a deliberate future upgrade boundary.

This pin is for the first github.com target. GitHub Enterprise Server versions may support a different REST API-version set, so Enterprise support remains a separate qualified target rather than inheriting the github.com version header blindly.

## 7. Transport/rate-limit/error baseline

GitHub's current REST guidance establishes:

```text
primary/secondary rate-limit failures
    HTTP 403 or 429

if Retry-After present
    wait at least that duration

if X-RateLimit-Remaining = 0
    wait until X-RateLimit-Reset

otherwise secondary-limit retry
    wait at least one minute, then exponential backoff if repeated

invalid credentials
    initially 401

private/inaccessible resource with insufficient auth
    may appear as 404
```

GitHub also recommends avoiding concurrent API requests and pausing at least one second between large numbers of mutative requests to reduce secondary rate limits.

Runtime Bridge policy remains stricter for uncertain mutations: **do not blindly auto-retry accepted-or-uncertain writes**. Rate-limit guidance may schedule a new deliberate attempt only when the prior write is known not to have been accepted or when action-specific idempotency/reconciliation proves safety.

## 8. `create_tree` genericized input gap is closed at GitHub-platform level

Official `POST /repos/{owner}/{repo}/git/trees` documentation defines each tree entry as:

```text
path: string
mode: one of
    100644  regular file blob
    100755  executable blob
    040000  tree/subdirectory
    160000  submodule commit
    120000  symlink blob

type: one of
    blob
    tree
    commit

sha: string | null
content: string
```

Rules:

```text
use sha OR content for entry contents, not both
sha = null deletes the path
base_tree optionally selects the existing base tree
entries overwrite same-path entries from base_tree
deleting a nonexistent file returns an error
```

The endpoint requires repository Contents permission at write level for fine-grained/GitHub App tokens and documents status codes 201, 403, 404, 409 and 422.

Runtime mapping:

```text
native base_tree_sha -> GitHub body base_tree
native tree_elements -> validated GitHub tree[] entries above
```

The missing host nested schema is therefore no longer a GitHub-platform blocker. The Runtime Bridge may expose an explicit strict nested schema instead of copying the native host's generic map.

## 9. `create_pull_request` source/target platform rules are closed

Official GitHub create-PR documentation establishes:

```text
head    required
base    required
title   required unless issue supplied
issue   required unless title supplied
head_repo required for cross-repository PRs when both repositories are owned by the same organization
```

`base` must be an existing branch in the current repository; the endpoint cannot create a PR whose base lives in another repository. Cross-repository head may be namespaced `username:branch` where appropriate.

The native connector exposes compatibility aliases `head_branch`/`head` and `base_branch`/`base` but does not project precedence when both forms are supplied. Runtime Bridge should therefore adopt a deliberate fail-closed normalization rule:

```text
for each alias pair
    one supplied                  -> use it
    both supplied and equal       -> use value
    both supplied and different   -> reject AMBIGUOUS_ALIAS_INPUT

normalized head and base
    both required before transport
```

This is an explicit Codexless safety contract, not a claim about hidden native-wrapper precedence.

## 10. Same-path Contents mutations must be serialized

Official GitHub Contents API documentation independently confirms that create/update-file and delete-file requests conflict when run concurrently and must be used serially.

This supports the native `update_file` descriptive rule and justifies a Runtime Bridge per-repository/path mutation serialization guard for Contents writes.

The endpoint works with GitHub App user access tokens and requires Contents write permission; modifying `.github/workflows` additionally requires Workflows write permission.

## 11. First G0 implementation contract

The now-accepted first implementation boundary is:

```text
GitHubAuthority
    user-access-token authentication only for user-directed parity actions
    derive installation/repository scope from GitHub
    no PAT fallback
    no caller token/header/scope inputs

GitHubDeviceFlow
    begin authorization
    expose only user_code / verification_uri / expiry/status metadata
    server owns device_code
    interval-aware polling
    typed device-flow errors

GitHubTokenStore
    server-owned protected storage abstraction
    atomic access+refresh token rotation
    expiration-aware refresh
    never logs token values

GitHubRestTransport
    github.com first target
    API version 2026-03-10
    fixed Accept + User-Agent
    Bearer user access token
    bounded endpoint construction, never arbitrary caller URL/method/header
    response status/headers/body captured internally
    rate-limit metadata normalized
    uncertain writes never blindly retried

GitHubGraphqlTransport
    same user authorization boundary
    explicit query/mutation operations owned by semantic actions
    never caller-supplied arbitrary GraphQL documents
```

The protected-store concrete Windows implementation remains the main G0 implementation design choice still to resolve locally. It should reuse a maintained OS protection mechanism where practical rather than invent custom cryptography.

## 12. G0 private candidate implementation

Validation 139 / Checkpoint 382 implement the source-backed contract at private head `3c5f3688ec578c0817953890dc69ecb7ce679153`. Syntax validation and 12 focused fake-transport/keyring regressions pass. The implementation preserves no-plaintext-fallback protected storage, private device codes, single-flight refresh, fixed github.com REST routing/version/headers, no automatic mutation retry, server-owned GraphQL documents and installation-derived repository scope.

The production keyring adapter is intentionally still a boundary rather than a live claim. Exact package import/API behavior plus a synthetic Windows Credential Manager round trip must pass before runtime integration.

## 13. Windows protected-store qualification

Validation 140 / Checkpoint 383 qualify the exact `@napi-rs/keyring@2.0.0` adapter on Windows x64. The package imports with the expected entry API, and one bounded normal-user-session synthetic Credential Manager lifecycle completed set/read-match/delete/verified-absence successfully. No GitHub credential was used. The earlier sandbox `ERROR_NO_SUCH_LOGON_SESSION` is classified as execution-context evidence rather than package incompatibility.

## 14. Main-runtime integration and dependency boundary

Validation 141 / Checkpoint 384 integrate the internal G0 kernel into a main-runtime candidate with lazy startup and no public GitHub action registration. The source integration is qualified, but the current Runtime Release v1 mechanism cannot provision the exact native keyring package into the installed runtime because package manifests and `node_modules` are outside its bounded target roots. This deployment gap must close before a live configured G0 release.

## 15. Immutable keyring dependency generation

Validation 142 / Checkpoint 385 close the package-deployment architecture gap. The exact Windows keyring packages are prepared into an immutable server-owned generation, identified to workers only by `{dependencyId, treeSha256}`. Runtime Release v2 carries server-owned dependency ids at manifest level, freezes exact tree refs at prepare time, preserves previous/target refs through pending and active release state, and switches those refs across activation, rollback, ordinary restart and recovery. The G0 keyring importer resolves only from the bound generation, with no ambient package fallback.

A real package load and real v2 release prepare both reproduced tree `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858`. Native Windows file locking prevents safe same-process generation deletion after load, so generation garbage collection is deliberately separated from release rollback.

## 16. Live dependency-aware runtime and exact keyring activation

Validation 143 / Checkpoint 386 first live-qualify the source-only bootstrap to `0.1.1-preview.22-github-g0-bootstrap`, proving that the old v1 engine can install the dependency-aware v2 implementation and restart with an empty dependency binding. Validation 144 / Checkpoint 387 then use that live v2 engine to prepare and activate the fixed `github-keyring-win32-x64` dependency under target version `0.1.1-preview.23-github-g0-keyring`. Postactivation verification reports one runtime dependency and zero source mismatches while the public surface remains 63 tools with no `github.*` action.

The exact generation has independently and during release regression loaded `@napi-rs/keyring` from tree `abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858`. No GitHub credential was created by the package activation. The remaining G0 boundary is now the explicit device-flow/control surface rather than storage or deployment.

## 17. Live authorization-control support surface

Validation 145 / Checkpoint 388 move the authorization-control contract from design into the active 64-tool runtime. `codex.github_authorization` is a support tool outside the native 89-action parity count. Its strict semantic operations are metadata, begin, status, poll, cancel and explicit clear. Secret-bearing and transport-authority fields remain absent from its caller schema.

The final live release `github-auth-control-v2-fix2` preserves one exact `github-keyring-win32-x64` dependency and passed all release regressions. Direct local MCP discovery shows the complete support schema. A metadata-only live invocation reports no configured GitHub App client ID and no stored authorization; no device-flow or GitHub request has been initiated.

The current persistent ChatGPT conversation retains a stale callable projection, so fresh-chat host schema/metadata qualification remains required before actual user authorization is attempted.

## 18. Host projection correction for authorization support

Validation 146 / Checkpoint 389 reproduce the known developer-MCP top-level-union projection defect on the live GitHub authorization support tool. The strict local preview.24 `oneOf` is projected by a fresh ChatGPT host only as `{ [key: string]: any }`, after which the single metadata attempt is blocked by host safety controls before any Runtime Bridge payload returns. That ordering does not prove the generic schema caused the safety block, but it is sufficient to reject the union shape for a mutation-sensitive authorization tool.

Preview.25 therefore applies the already qualified flat-schema pattern. The live schema now structurally exposes required six-value `action`, bounded optional `requestId`, bounded optional `authorizationRef`, optional literal `confirmClear=true`, and `additionalProperties=false`. Server-side cross-field validation preserves exact action semantics. The 16-regression release and activation pass; direct local metadata remains unconfigured/unauthorized and no GitHub request has started.

## 19. Fresh-host authorization support and live Plugin-name qualification

Validation 147 / Checkpoint 390 close the fresh-host support-surface gate. Preview.25 projects as a structured flat bounded object in a fresh ChatGPT conversation and exactly one `metadata` call reaches Runtime Bridge successfully. The returned state remains unconfigured and unauthorized, with no stored credential. The host does not separately render `additionalProperties=false`, so that exact keyword remains local-wire evidence rather than a host-visible claim.

The owner also supplied current ChatGPT UI evidence showing the Plugin display name `Codexless Runtime Bridge`. This closes the live Plugin display-name rename that had remained open since Checkpoint 370 while preserving historical exact labels as evidence.

The next platform gate is now the exact GitHub App permission manifest required by the 89-action parity target. Device flow remains disabled in practice until the dedicated App exists, has the frozen minimal permission superset, and its non-secret client ID is installed in server-owned configuration.

## 20. Frozen GitHub App permission manifest

Validation 148 / Checkpoint 391 derive every exact native action against current GitHub endpoint permission evidence and freeze the initial dedicated App manifest at seven repository permissions: `actions=write`, `contents=write`, `issues=write`, `metadata=read`, `pull_requests=write`, `statuses=read`, and `workflows=write`. Organization, account and enterprise permissions remain empty; webhooks remain disabled; Administration, Checks and Members remain no-access.

This is exact at the REST documentation layer. GitHub's own App guidance does not publish an exact GraphQL permission matrix and explicitly tells developers to test their intended GraphQL operations. Eight observed PR/review operations therefore remain an empirical sufficiency check under the already-required `pull_requests=write`; no speculative extra permission is added.

## 21. Frozen registration and first-installation configuration

Validation 149 / Checkpoint 392 freeze the account-bound GitHub App creation choices before any live registration occurs. The App is to be owned by personal account `shakaarlatief`, request the canonical name `Codexless Runtime Bridge`, use the public ADS repository as homepage, remain installable on Any account, keep webhooks off, enable device flow and expiring user access tokens, avoid install-time OAuth authorization, and use no callback/setup URL or private-key bootstrap.

The first installation is intentionally limited to `Only select repositories` with the canonical public ADS repository. That scope is sufficient for authorization, installation-intersection and read-only GraphQL sufficiency qualification while minimizing first-live blast radius. It does not alter the final installation-derived parity model.

## 22. Extended App authority supersedes parity-only registration

Validation 150-152 / Checkpoints 393-395 reopen and then refreeze the GitHub App authority because Codexless is now explicitly intended to exceed the provider-owned native connector where useful. Owner-supplied live UI evidence exposes 118 permission rows. The initial extended profile selects 74: 34 repository, 30 organization, 10 account and no enterprise permissions. Repository Administration(write) is included for later bounded repository creation/administration; secret-value and Webhook permission families remain excluded pending purpose-built safety contracts.

The registration prefill contains 56 independently documented permission parameters. Eighteen current live/newer rows remain manual rather than using guessed query keys. Personal installation scope is All repositories. This extended profile, not the historical seven-permission baseline, is now the creation authority.

## 23. Current disposition

```text
GITHUB_APP_USER_ACCESS_TOKEN_MODEL=CONFIRMED
DEVICE_FLOW_WITHOUT_CLIENT_SECRET=CONFIRMED
DEVICE_FLOW_REFRESH_WITHOUT_CLIENT_SECRET=CONFIRMED
USER_TOKEN_LIFETIME=8_HOURS
REFRESH_TOKEN_LIFETIME=6_MONTHS
INSTALLATION_DERIVED_USER_SCOPE=CONFIRMED
REST_GITHUB_COM_API_VERSION=2026-03-10
REST_USER_AGENT_REQUIRED=CONFIRMED
CREATE_TREE_PLATFORM_SCHEMA=RESOLVED
CREATE_PULL_REQUEST_PLATFORM_REQUIREMENTS=RESOLVED
CONTENTS_SAME_PATH_SERIALIZATION=CONFIRMED
G0_IMPLEMENTATION_CONTRACT=READY
LIVE_RUNTIME_RELEASE_ENGINE=V2_CAPABLE
RUNTIME_DEPENDENCY_COUNT=1
KEYRING_GENERATION_ACTIVE=YES
AUTHORIZATION_SUPPORT_SURFACE=LIVE_LOCAL_MCP
PUBLIC_TOOL_COUNT=64
GITHUB_APP_CLIENT_ID_CONFIGURED=false
STORED_GITHUB_AUTHORIZATION=false
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_CREATE_EXTENDED_GITHUB_APP_AND_INSTALL_ALL_PERSONAL_REPOSITORIES
```
