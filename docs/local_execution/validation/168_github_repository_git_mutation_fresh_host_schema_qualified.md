# Validation 168: Repository Git Mutation Fresh-Host Schema Qualified

**Date:** 2026-09-09
**Status:** PASS / EIGHT REPOSITORY-GIT MUTATIONS FRESH-HOST PROJECTED / TWO NON-WRITING GUARDS PASS / POSITIVE LIVE MUTATION STILL UNAUTHORIZED
**Research:** Research 123
**Scope:** Preserve the owner-supplied fresh ChatGPT host qualification of the first eight preview.34 repository Git/content mutation actions.

## 1. Starting boundary

Validation 167 / Checkpoint 410 established preview.34 live locally at 120 public tools / 56 GitHub tools and locally qualified all eight repository Git/content mutation schemas plus two fail-closed guard probes without dispatching a GitHub write. The remaining gate was a refreshed disposable ChatGPT host projection of those eight mutation-sensitive actions.

## 2. Owner-supplied fresh-host result

The owner supplied a completed disposable-chat result ending exactly:

```text
GITHUB_REPOSITORY_GIT_MUTATION_FRESH_HOST_SCHEMA=PASS
```

All eight exact actions projected:

```text
github.create_blob
github.create_branch
github.create_commit
github.create_file
github.create_tree
github.delete_file
github.update_file
github.update_ref
```

The owner reports every host-visible caller schema was bounded and none was genericized or truncated enough to prevent establishing caller authority. Some semantic cross-field rules remained descriptive rather than separately rendered as machine-readable `oneOf` or `additionalProperties` keywords. That distinction is preserved rather than upgraded into a stronger host-schema claim.

No projected schema exposed caller-selected GitHub credentials/tokens, Authorization headers, GitHub hosts, arbitrary URLs/endpoints, GraphQL documents, HTTP methods/headers, arbitrary Git ref namespaces, permission profiles, transport implementations, host filesystem paths, shell commands or equivalent arbitrary authority.

The full field-by-field Part A transcript was not recopied into this persistent conversation. Validation 167 remains the exact local MCP wire-schema authority; Validation 168 establishes fresh-host projection/boundedness and guard behavior without fabricating field details that were not supplied here.

## 3. Fresh-host non-writing guard Call 1

Exactly one `github.create_branch` call used the canonical public repository and deliberately supplied both source selectors. The result was:

```text
error: Exactly one of sha or base_ref must be supplied
errorCode: GITHUB_BRANCH_BASE_INVALID
source: runtime-bridge
operation: github.create_branch
status: null
retryable: false
mutationUncertain: false
githubRequestId: null
retryAfterMs: null
rateLimitResetAtMs: null
acceptedPermissions: null
documentationUrl: null
surfaceVersion: codexless-public-preview-v2
is_error: true
```

This exactly matches the intended fail-closed XOR guard. No retry occurred.

## 4. Fresh-host non-writing guard Call 2

Exactly one `github.update_ref` call targeted branch `main` with `force=true`. The result was:

```text
error: force=true remains fail-closed until destructive ref movement receives a dedicated qualification
errorCode: GITHUB_FORCE_REF_UPDATE_NOT_QUALIFIED
source: runtime-bridge
operation: github.update_ref
status: null
retryable: false
mutationUncertain: false
githubRequestId: null
retryAfterMs: null
rateLimitResetAtMs: null
acceptedPermissions: null
documentationUrl: null
surfaceVersion: codexless-public-preview-v2
is_error: true
```

This exactly matches the intended force guard. No retry occurred.

## 5. Mutation-certainty and external-effect result

Neither call was mutation-uncertain. Both returned `githubRequestId=null`, which is consistent with termination at Runtime Bridge application guards before intended GitHub write dispatch. The owner observed no branch, blob, tree, commit, file, deletion, update or ref movement.

This validation therefore preserves:

```text
FRESH_HOST_PROJECTION=PASS_8_OF_8
FRESH_HOST_CALLER_AUTHORITY=BOUNDED_8_OF_8
CREATE_BRANCH_XOR_GUARD=PASS_EXPECTED_REJECTION
UPDATE_REF_FORCE_TRUE_GUARD=PASS_EXPECTED_REJECTION
MUTATION_UNCERTAIN=false
GITHUB_REQUEST_ID=null_for_both_guard_calls
GITHUB_MUTATION_OCCURRED=false
```

## 6. Positive-live boundary

No positive GitHub write path was exercised or qualified. The project must not reinterpret this schema/guard qualification as positive mutation parity.

The next legitimate gate is a separately authorized disposable positive-mutation qualification. It should use one dedicated disposable branch and a deterministic test path, avoid `main`, use `force=false` only, bind sequential file updates/deletion to returned content SHAs, preserve every returned object SHA, and never retry any uncertain mutation.

Because the native connector exposes no branch-delete action in the 89-action baseline, the qualification design must decide in advance whether the disposable branch may remain as an explicit test artifact or whether cleanup will use a separately authorized non-parity capability. Cleanup authority must not be smuggled into the parity test.

Exact native-wrapper parity remains conservatively `0 / 89` because hidden output envelopes and unresolved wrapper semantics remain explicit gaps.

```text
VALIDATION168=PASS
GITHUB_REPOSITORY_GIT_MUTATION_FRESH_HOST_SCHEMA=PASS
REPOSITORY_GIT_MUTATION_FRESH_HOST_PROJECTION=PASS_8_OF_8
REPOSITORY_GIT_MUTATION_FRESH_HOST_BOUNDEDNESS=PASS_8_OF_8
CREATE_BRANCH_XOR_GUARD=PASS_EXPECTED_REJECTION
UPDATE_REF_FORCE_TRUE_GUARD=PASS_EXPECTED_REJECTION
REPOSITORY_GIT_MUTATION_POSITIVE_LIVE=0_OF_8
GITHUB_MUTATION_OCCURRED=false
LIVE_RUNTIME_VERSION=0.1.1-preview.34-github-repository-git-mutations
LIVE_PUBLIC_TOOL_COUNT=120
LIVE_GITHUB_TOOL_COUNT=56
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=DISPOSABLE_REPOSITORY_GIT_POSITIVE_MUTATION_QUALIFICATION
```
