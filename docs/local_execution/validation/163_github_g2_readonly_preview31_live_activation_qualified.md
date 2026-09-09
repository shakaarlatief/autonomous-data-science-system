# Validation 163: GitHub G2 Read-Only Preview.31 Live Activation Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.31 LIVE / G2 HOST QUALIFICATION NEXT
**Research:** Research 123
**Scope:** Preserve the implementation, release qualification, live activation and same-chat projection result for the eleven-action G2 read-only repository fetch/search/branch/commit/file/blob/compare slice.

## 1. Starting boundary

Validation 162 / Checkpoint 405 closed G1 fresh-host coverage at 7/7 and opened G2 read-only implementation. Live runtime before this work was:

```text
version             0.1.1-preview.30-github-g1-readonly
public tools        75
github.* tools      11
protected auth      authorized / stored / non-expired
exact native rows   0 / 89
```

## 2. G2 action surface

The new read-only slice adds exactly eleven actions:

```text
github.compare_commits
github.fetch
github.fetch_blob
github.fetch_commit
github.fetch_file
github.search
github.search_branches
github.search_commits
github.search_installed_repositories_streaming
github.search_installed_repositories_v2
github.search_repositories
```

The implementation keeps repository authority installation-derived and exposes no caller-selected GitHub credential, arbitrary HTTP method/header, arbitrary GraphQL document or non-GitHub host authority. The generic `github.fetch` path is GET-only and allowlisted; search remains on explicit semantic actions.

Known hidden native semantics remain fail-closed rather than guessed. In particular, search-index enrichment is not claimed, Enterprise repository URL routing remains separate, and conflicting `per_page`/`topn` repository-search aliases are rejected instead of inventing precedence.

## 3. Candidate qualification and first failed immutable release

Private local-runtime release `github-g2-readonly-expansion-v1` targeted:

```text
version                0.1.1-preview.31-github-g2-readonly
public tools           86
github.* read tools    22
release files          10
runtime dependencies  1
```

The first manifest declared 17 regressions and was correctly rejected by the existing Runtime Release v2 maximum of 16. The bound was not widened. The corrected v1 manifest used sixteen regressions, prepared successfully and showed the expected ten prepublication mismatches against preview.30.

Its first publication then failed safely with:

```text
errorCode  RUNTIME_RELEASE_REGRESSION_FAILED
```

No live source mutation occurred. A reconstructed current-source test stage localized the failure to the new public MCP wire-schema regression: the test incorrectly expected no serialized enum for nullable commit-search `sort`, while the real Zod-to-MCP schema correctly serialized `best-match | author-date | committer-date` plus null. The product schema was correct; the test assertion was repaired.

Because the failed v1 release ID was already immutably bound to its earlier manifest, re-preparation with changed bytes correctly returned `RUNTIME_RELEASE_PREPARED_CONFLICT`. The correction therefore moved to a new immutable release ID rather than rewriting prepared state.

## 4. Corrected immutable release v2

Private local-runtime head:

```text
b446a3fc2ff480e66acc81ddad56f12bb871feca
```

Release:

```text
github-g2-readonly-expansion-v2
```

Target:

```text
0.1.1-preview.31-github-g2-readonly
codexless-public-preview-v2
86 public tools
10 release files
16 regressions
1 runtime dependency
manifest SHA-256 634212f05c78e62761c6b5e0214c3408eb23c33cd66105b1d4a407329e9cbace
```

Focused reconstructed-stage qualification passed for:

```text
bounded Git fetch/pull count guards
public MCP registration / wire schema   PASS / tools=86 / github read tools=22
GitHub G0 runtime integration            PASS
GitHub read-only foundation integration PASS
combined G1 + G2 integration            PASS
```

The combined G2 integration exercises compare, bounded fetch, blob/commit/file reads, code search, opaque branch continuation, commit search and both installed-repository search models while enforcing installation scope, GET-only GitHub API traffic and secret non-disclosure.

## 5. Publication and activation

Corrected v2 preparation succeeded. Prepublication verification returned the expected ten mismatches against live preview.30. Publication operation:

```text
rm_59bfec18a65b6d64e35b5ad003f7463d
```

completed `succeeded` with no recovery. All release regressions passed.

Restart operation:

```text
rm_ad739f5850d15cd2b7eb267d6ca25c0b
```

then activated preview.31 successfully with no recovery. One immediate status read crossed the deliberate restart window and returned host HTTP 502; retrying the same read-only status after the runtime returned reported the durable operation as `succeeded`. The restart itself was never replayed.

Fresh postactivation release verification returned:

```text
status                  verified
targetVersion           0.1.1-preview.31-github-g2-readonly
targetToolCount         86
fileCount               10
runtimeDependencyCount  1
mismatchCount           0
```

## 6. Authorization continuity

Postactivation `codex.github_authorization metadata` remains healthy:

```text
configured           true
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
authMode             github-app-user-token-device-flow
host                 github.com
restApiVersion       2026-03-10
```

No credential value, Authorization header, device code, client secret or keyring payload was exposed. No GitHub mutation occurred.

## 7. Same-chat host projection

After activation, targeted Runtime Bridge tool rediscovery in the existing persistent `chatgpt-21` conversation still returned only the already projected G1 GitHub tools. The new G2 names were not projected into this existing host conversation. This reproduces the established AB-008 same-chat projection staleness and does not contradict the verified live 86-tool source contract.

Therefore no real G2 GitHub read was forced through a stale host. The next evidence gate is a fresh disposable ChatGPT conversation that must discover the eleven G2 actions, capture their bounded host schemas and execute a bounded read-only qualification set against live GitHub.

## 8. Disposition

```text
VALIDATION163=PASS
G2_IMPLEMENTATION=PASS
G2_RELEASE_V1_MANIFEST_COUNT_REJECTION=PRESERVED
G2_RELEASE_V1_REGRESSION_FAILURE=PRESERVED
G2_RELEASE_V2_PREPARE=PASS
G2_RELEASE_V2_PUBLISH=PASS
G2_RELEASE_V2_RESTART=PASS
G2_POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
LIVE_RUNTIME_VERSION=0.1.1-preview.31-github-g2-readonly
LIVE_PUBLIC_TOOL_COUNT=86
LIVE_GITHUB_READONLY_TOOL_COUNT=22
G2_NEW_TOOL_COUNT=11
PROTECTED_AUTHORIZATION_HEALTHY=true
SAME_CHAT_G2_PROJECTION=STALE
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_G2_SCHEMA_AND_LIVE_READ_QUALIFICATION
```
