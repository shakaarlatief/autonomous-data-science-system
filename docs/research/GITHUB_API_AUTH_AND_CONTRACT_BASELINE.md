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

## 14. Current disposition

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
NEXT=INTEGRATE_G0_INTO_MAIN_CODEXLESS_RUNTIME_CANDIDATE
```
