# Validation 138: GitHub Official API Auth and First Contract Gaps Resolved

**Date:** 2026-09-08
**Status:** PASS / G0 AUTH-TRANSPORT CONTRACT READY / CREATE-TREE + CREATE-PR + CONTENTS SERIALIZATION PLATFORM GAPS RESOLVED
**Research:** Research 123
**Scope:** Use current official GitHub documentation to validate the selected GitHub App/user-token/device-flow architecture, pin the first github.com REST transport contract, and close the most important GitHub-platform request gaps without invoking GitHub actions or exposing credentials.

## 1. Official-source qualification

Current GitHub documentation was inspected directly for:

```text
GitHub App authentication modes
GitHub App user access tokens
device-flow user authorization
refresh-token lifecycle
GitHub App registration/permissions
user-accessible app installations
REST API versioning/request headers
REST rate-limit/error best practices
Git Trees create-tree contract
Pull Request create contract
Repository Contents create/update/delete concurrency
```

The detailed source index is preserved in `docs/research/GITHUB_API_AUTH_AND_CONTRACT_BASELINE.md`.

## 2. Authentication architecture confirmed

GitHub's current guidance confirms that user-directed activity should use a GitHub App user access token when the action should be bounded by both the user's authority and the app's authority. The user token can access only resources available to both the installed app and the user.

This directly supports Research 123's selected authority chain:

```text
ChatGPT semantic action
    -> server-owned GitHub App user authorization
    -> installation/user intersection
    -> bounded GitHub REST/GraphQL operation
```

No PAT fallback is justified for this parity target.

## 3. Device flow and token rotation confirmed

The GitHub App device flow requires the app client ID but not a client secret. The device code/user code expire on the documented 900-second default window, with interval-aware polling and explicit device-flow error codes.

Current expiring user-token values are:

```text
access token     8 hours
refresh token    6 months
```

GitHub explicitly allows refresh without the client secret when the user access token was generated through device flow. Atomic access/refresh rotation is therefore the accepted G0 token-lifecycle contract.

## 4. Installation-derived scope confirmed

`GET /user/installations` works specifically with a GitHub App user access token and lists app installations accessible to the authenticated user. GitHub documents page/per_page pagination with a maximum per_page of 100.

This confirms that Runtime Bridge repository scope should be derived from GitHub installation/user authority instead of a caller-provided remote URL/token/permission surface.

## 5. github.com REST transport pin confirmed

GitHub currently supports REST versions `2026-03-10` and `2022-11-28`, with 2022 support ending 2028-03-10. The current first github.com target is pinned to:

```text
Accept: application/vnd.github+json
X-GitHub-Api-Version: 2026-03-10
User-Agent: fixed Codexless Runtime Bridge identity
Authorization: Bearer <server-owned user token>
```

GitHub requires a valid User-Agent. Enterprise Server API-version support is treated separately and must not inherit the github.com pin automatically.

## 6. Error/rate-limit transport behavior established

Official guidance establishes 403/429 rate-limit behavior, `Retry-After`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, secondary-limit backoff, initial 401 for invalid credentials and possible 404 masking for inaccessible private resources.

These facts justify a stable Codexless transport/error envelope, while accepted-or-uncertain mutations continue to follow the stricter ADS rule: never blindly retry an uncertain write.

## 7. `create_tree` platform gap resolved

Official Git Tree documentation closes the genericized nested host schema:

```text
path
mode = 100644 | 100755 | 040000 | 160000 | 120000
type = blob | tree | commit
sha: string | null
content: string
```

Use `sha` or `content`, not both. `sha=null` deletes the path. `base_tree` supplies the existing base tree. The endpoint requires Contents write permission and documents 201/403/404/409/422 statuses.

Runtime mapping is explicit:

```text
base_tree_sha -> base_tree
tree_elements -> validated GitHub tree entries
```

## 8. `create_pull_request` platform requirements resolved

Official create-PR documentation establishes `head` and `base` as required, plus title/issue conditional requirements and `head_repo` for specific same-organization cross-repository cases.

Because native aliases do not project conflict precedence, Codexless will fail closed on conflicting alias/canonical values and require normalized head/base before transport.

## 9. Contents-write serialization confirmed

GitHub's Contents API explicitly warns that create/update and delete operations conflict when run concurrently and must be used serially. This independently supports a per-repository/path Contents mutation serialization guard.

## 10. Exact next boundary

The first G0 implementation contract is now ready. The only major G0 local design choice still open is the concrete protected Windows token-store implementation. It should use a maintained OS protection mechanism where practical and must not invent custom cryptography.

```text
VALIDATION138=PASS
GITHUB_APP_USER_TOKEN_ARCHITECTURE=CONFIRMED
DEVICE_FLOW_NO_CLIENT_SECRET=CONFIRMED
REFRESH_NO_CLIENT_SECRET_AFTER_DEVICE_FLOW=CONFIRMED
INSTALLATION_USER_SCOPE=CONFIRMED
GITHUB_COM_REST_VERSION=2026-03-10
CREATE_TREE_PLATFORM_GAP=CLOSED
CREATE_PR_PLATFORM_REQUIREMENTS=CLOSED
CONTENTS_SERIALIZATION=CONFIRMED
G0_CONTRACT=READY
NEXT=G0_PROTECTED_TOKEN_STORE_AND_AUTH_TRANSPORT_IMPLEMENTATION
```
