# Validation 198: GitHub Delete Branch Preview.43 Live Local Qualification

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.43 ACTIVE / 169 PUBLIC TOOLS / 105 GITHUB TOOLS / DELETE-BRANCH WIRE SCHEMA PASS / TWO NO-WRITE GUARDS PASS / ZERO BRANCH DELETIONS
**Scope:** Implement, publish, activate, and locally qualify the one-action Git Reference Lifecycle foundation frozen by Validation 197 without deleting any GitHub branch.
**Research:** Research 123

## 1. Implementation and immutable release

The new action is:

```text
github.delete_branch
```

Private local-runtime source head:

```text
7b426a4844d4d26f995fd2c4964397eb97753533
```

Immutable Runtime Release:

```text
releaseId           github-git-reference-lifecycle-v1
targetVersion       0.1.1-preview.43-github-git-reference-lifecycle
targetSurface       codexless-public-preview-v2
targetToolCount     169
fileCount           10
runtimeDependencies 1
manifestSha256      859bd5e339eda29cc151359b4efd41fd11cbbf97651d64d0bef9b98b7577da4f
```

The dedicated fake-dependency suite passed:

```text
tests      9
pass       9
fail       0
```

It covers the exact action declaration, positive fake deletion, malformed branch rejection, default-branch rejection, protected-branch rejection, stale-head rejection, destructive-state drift during serialized revalidation, definite 404/409/422 propagation, and mutation uncertainty after exactly one DELETE with zero replay.

All candidate JavaScript files passed `node --check`, and all ten release payload hashes matched the manifest before publication.

## 2. Publication and activation

Release preparation succeeded for source head `7b426a4844d4d26f995fd2c4964397eb97753533`.

Prepublication verification correctly returned:

```text
status         verification_failed
mismatchCount  10
```

because preview.42 did not yet contain the preview.43 release files.

Publication operation:

```text
operationId       rm_98203fc3f6c56b4dfa47b8c66b8448dc
final status      succeeded
recoveryAttempted false
```

Activation restart:

```text
operationId       rm_1805cfa7fb1fc24e5f23c49c5d36f6e7
final status      succeeded
recoveryAttempted false
```

Postactivation verification returned:

```text
status         verified
mismatchCount  0
```

## 3. Active runtime and wire contract

Fresh `/healthz` reports:

```text
ok              true
service         codexless-public
version         0.1.1-preview.43-github-git-reference-lifecycle
surfaceVersion  codexless-public-preview-v2
toolCount       169
```

Fresh stateless MCP `tools/list` reports:

```text
public tools       169
GitHub tools       105
github.delete_branch present
```

The exact wire contract is:

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hex string 7..64
additionalProperties  false
```

Visible annotations are:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

The tool description confirms branches-only server-owned ref construction, exact expected-head validation, repeated default/protection/head checks inside the destructive serialized boundary, no force/policy bypass, and no automatic retry after uncertain deletion.

## 4. Local-live deterministic no-write guards

Two real GitHub branch identities were read before guard calls:

```text
main
    head      3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
    protected false

v1-source-vault-bootstrap-resume
    head      12f89b1d01d532798003091a6df8fbfd500d5ae4
    protected false
```

### Guard 1: default branch

`github.delete_branch` was invoked through a fresh stateless local MCP call with:

```text
branch_name        main
expected_head_sha  3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
```

It failed closed before DELETE:

```text
errorCode          GITHUB_DEFAULT_BRANCH_DELETE_FORBIDDEN
operation          github.delete_branch
status             null
retryable          false
mutationUncertain  false
githubRequestId    null
```

### Guard 2: stale head

`github.delete_branch` was invoked against the active development branch with deliberately stale:

```text
expected_head_sha  0000000
```

It failed closed before DELETE:

```text
errorCode          GITHUB_BRANCH_HEAD_CHANGED
operation          github.delete_branch
status             null
retryable          false
mutationUncertain  false
githubRequestId    null
```

Read-only postflight then returned both branches at their original exact heads. Therefore:

```text
positive branch deletions   0
mutation retries            0
mutation-uncertain results  0
branch state changes        0
```

A live protected-branch guard was not manufactured because the canonical repository currently has no protected branch fixture. The protected-branch behavior remains covered by the 9/9 fake-dependency suite and must fail closed locally before DELETE.

## 5. Authorization and host projection

Protected GitHub authorization remains healthy after activation and qualification:

```text
configured          true
initialized         true
authorized          true
storedAuthorization true
accessExpired       false
refreshExpired      false
refreshRecommended  false
```

The already-open persistent `chatgpt-22` Plugin projection does not expose `github.delete_branch` as a direct host tool after runtime activation, while fresh stateless MCP discovery proves it is live. This is the established same-conversation projection-staleness class rather than a runtime failure.

The next gate is therefore one fresh disposable ChatGPT-host qualification after Plugin refresh/rescan. That gate must capture the exact projected schema and run deterministic invalid no-write guards only. No positive branch deletion is authorized until that gate passes and a new disposable positive fixture is frozen.

## 6. Disposition

```text
VALIDATION198=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.43-github-git-reference-lifecycle
LIVE_PUBLIC_TOOL_COUNT=169
LIVE_GITHUB_TOOL_COUNT=105
GITHUB_DELETE_BRANCH_WIRE_SCHEMA=PASS_1_OF_1
GITHUB_DELETE_BRANCH_FAKE_TESTS=PASS_9_OF_9
GITHUB_DELETE_BRANCH_LOCAL_NO_WRITE_GUARDS=PASS_2_OF_2
GITHUB_DELETE_BRANCH_POSITIVE_WRITES=0_OF_1
GITHUB_DELETE_BRANCH_MUTATION_RETRIES=0
GITHUB_DELETE_BRANCH_MUTATION_UNCERTAIN_RESULTS=0
POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
PROTECTED_GITHUB_AUTHORIZATION=HEALTHY
HISTORICAL_BRANCH_CLEANUP=NOT_AUTHORIZED
AB030=PARKED_UNCHANGED
NEXT=FRESH_CHAT_GITHUB_DELETE_BRANCH_SCHEMA_GUARD_QUALIFICATION
```
