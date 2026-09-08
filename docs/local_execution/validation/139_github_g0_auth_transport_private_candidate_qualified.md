# Validation 139: GitHub G0 Auth/Transport Private Candidate Qualified

**Date:** 2026-09-08
**Status:** PASS / PRIVATE G0 CANDIDATE IMPLEMENTED + TESTED + PRESERVED / NO LIVE GITHUB AUTH OR ACTION PUBLICATION
**Research:** Research 123
**Scope:** Implement the first internal GitHub G0 authority/authentication/transport kernel in the private local-runtime repository, qualify it with deterministic fake HTTP/keyring regressions, preserve it through the normal private integrity gate, and keep live GitHub credentials plus public `github.*` actions explicitly out of scope.

## 1. Candidate boundary

The candidate is preserved in the private local-runtime repository at exact head:

```text
3c5f3688ec578c0817953890dc69ecb7ce679153
```

Candidate root:

```text
.ads-private/codexless/github-g0-candidate/
```

Implemented modules:

```text
github-errors.mjs
github-token-store.mjs
github-device-flow.mjs
github-token-manager.mjs
github-rest-transport.mjs
github-graphql-transport.mjs
github-authority.mjs
```

Supporting evidence:

```text
README.md
DEPENDENCY_REVIEW.md
package.json
test/github-g0.test.mjs
```

No candidate byte has been published into the live Codexless installation.

## 2. Protected credential-store design

The candidate uses an injected protected-token-store abstraction with one production adapter boundary for `@napi-rs/keyring` 2.0.0.

Accepted safety rules:

```text
OS-backed keyring only
no plaintext fallback
no custom cryptography
no token values in ordinary logs/errors/results
one fixed service/account identity boundary
access + refresh tokens stored as one serialized credential
same-entry keyring operations serialized
keyring package dynamically imported and failure is explicit
```

The candidate does not perform a real Windows Credential Manager write during this validation. Package installation/import plus one bounded OS-store round trip remains a separate next qualification.

## 3. Device flow

`GitHubDeviceFlow` implements the source-backed headless device authorization state machine:

```text
server-owned client ID
server-owned device_code kept only in memory
user-visible user_code + verification_uri
opaque authorizationRef
bounded expiry
interval-aware polling
slow_down adds five seconds to the polling interval
terminal OAuth error classification
successful access/refresh pair written atomically to protected storage
no client secret input or transport
```

The user-visible authorization result never returns access token, refresh token or device code.

## 4. Token lifecycle

`GitHubTokenManager` implements:

```text
read current protected credential
return still-valid access token internally only
refresh before expiry using a bounded skew
single-flight refresh so concurrent callers do not rotate the same refresh token twice
client-id + refresh-token device-flow refresh without client secret
atomic replacement of access + refresh token pair
explicit reauthorization-required state after refresh expiry
metadata surface that excludes token values
```

## 5. REST transport

The first github.com transport is intentionally fixed:

```text
base URL                 https://api.github.com
Accept                   application/vnd.github+json
X-GitHub-Api-Version     2026-03-10
User-Agent               fixed Codexless Runtime Bridge identity
Authorization            server-owned Bearer user token
methods                   GET / POST / PATCH / PUT / DELETE
JSON response ceiling    8 MiB default, bounded maximum 32 MiB
request timeout           30 seconds default, bounded maximum 120 seconds
```

Caller-selected absolute URLs, query strings embedded in the path, URL fragments, traversal segments and arbitrary headers are rejected. The internal request helper does not auto-retry.

Network failure on a mutation is classified as `GITHUB_MUTATION_RESULT_UNCERTAIN`; equivalent read transport failure remains retryable. HTTP responses are classified separately, including 401, 404/inaccessible, 409, 422, rate limits and upstream 5xx.

Safe metadata includes GitHub request ID, retry-after/rate-limit fields and accepted-permissions hints. Credential material is not included.

## 6. GraphQL transport

GraphQL is not exposed as arbitrary query authority. `GitHubGraphqlTransport` accepts only server-registered operation IDs whose query/mutation documents are fixed by the implementation.

Unknown operation IDs and caller-supplied raw GraphQL documents are rejected. GraphQL error arrays fail visibly; mutation GraphQL errors preserve mutation uncertainty rather than pretending success.

## 7. Installation-derived authority

`GitHubAuthority` implements bounded current-user GitHub App installation discovery plus installation repository enumeration with `per_page=100`, a server-side maximum page bound and normalized repository identity.

Repository resolution succeeds only when the requested owner/name appears through the authenticated user's app-installation scope. No caller remote URL, PAT, OAuth scope, authorization header or installation-token substitution is accepted.

Public-repository unauthenticated read parity remains action-specific future work and is not misclassified as installation authority.

## 8. Deterministic regression result

The candidate passed syntax validation and the focused G0 suite twice after final correction.

Final test result:

```text
npm run check   PASS
npm test        PASS

tests           12
pass            12
fail             0
network calls    0 real GitHub calls
OS keyring writes 0 real credential writes
```

The 12 cases cover protected-store serialization, fail-closed missing keyring, device-flow privacy/polling/slow-down/token write, no-refresh valid-token reads, single-flight refresh, fixed REST host/version/headers, no arbitrary URL routing, rate-limit normalization/no retry, mutation uncertainty, GraphQL registry/error behavior, installation pagination/scope resolution and token-like error redaction.

## 9. Integrity-gate failure and correction

The first semantic push attempt failed closed with:

```text
GIT_PUSH_FF_ONLY_INTEGRITY_FAILED
obvious secret-like material rejected in tracked file:
.ads-private/codexless/github-g0-candidate/src/github-device-flow.mjs
```

Read-only diagnosis reproduced the existing `runtime-private-bootstrap` scanner and showed **false-positive code syntax**, not a leaked credential. Examples such as `accessToken: body.access_token` matched the intentionally conservative generic secret-assignment pattern.

The validator was **not weakened or bypassed**. The candidate was rewritten to avoid secret-like assignment syntax and tests were converted to scanner-safe synthetic fixture values. A direct re-scan using the exact scanner patterns returned zero hits, all 12 tests still passed, and the subsequent normal semantic push succeeded.

Final private push evidence:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
local head = remote tracking head
3c5f3688ec578c0817953890dc69ecb7ce679153
```

## 10. Dependency status

Current upstream evidence supports `@napi-rs/keyring` 2.0.0 as the candidate Node keyring adapter and the Windows backend is based on Windows Credential Manager. The underlying Windows store warns that simultaneous same-entry operations may not be ordered, which is why the candidate serializes those operations.

This validation does not claim the package is installed in the live Codexless runtime. Dependency import/package provenance plus a no-GitHub-token Windows Credential Manager round trip remain the next local qualification.

## 11. Current boundary

```text
VALIDATION139=PASS
G0_INTERNAL_CANDIDATE=IMPLEMENTED
G0_CANDIDATE_PRIVATE_HEAD=3c5f3688ec578c0817953890dc69ecb7ce679153
G0_FOCUSED_TESTS=12_OF_12_PASS
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
LIVE_GITHUB_CREDENTIAL=NOT_USED
REAL_GITHUB_NETWORK_CALL=NOT_PERFORMED
REAL_OS_CREDENTIAL_WRITE=NOT_PERFORMED
PUBLIC_GITHUB_ACTIONS=NOT_REGISTERED
LIVE_CODEXLESS_INSTALL=UNCHANGED
NEXT=QUALIFY_NAPI_KEYRING_WINDOWS_IMPORT_AND_BOUNDED_OS_CREDENTIAL_ROUNDTRIP
```
