# Validation 202: Repository Branch-Safety Preview.44 Live Local Qualification

**Date:** 2026-09-10
**Status:** PASS / PREVIEW.44 ACTIVE / 172 PUBLIC TOOLS / 108 GITHUB TOOLS / THREE-ACTION WIRE PASS / LOCAL NO-WRITE GUARDS PASS
**Scope:** Implement, publish, activate, and locally qualify the three-action Repository Branch-Safety Governance foundation frozen by Validation 201 without changing live branch protection.
**Research:** Research 123

## 1. Implementation

The fifth and intended-final important beyond-parity GitHub family contains exactly:

```text
github.get_branch_protection
github.create_branch_safety_protection
github.delete_branch_safety_protection
```

Private local-runtime source head:

```text
4e02b105e698265b72e449b8211a20aa20a22b14
```

The implementation uses the server-owned profile:

```text
codexless.branch-safety-baseline.v1
```

with ordinary fast-forward pushes left available while force pushes and branch deletion are disabled and administrator enforcement is enabled. Required PR reviews, required status checks, branch locking and other broad governance settings are not exposed.

Two implementation hardenings preserve the design's fail-closed intent:

```text
1. if the exact branch reports protected=true while the classic protection endpoint is absent,
   Runtime Bridge treats the branch as externally protected and refuses create;
2. signed-commit protection is included in baseline comparison, so a stronger signed-commit
   policy cannot be mistaken for the removable Codexless baseline.
```

The dedicated fake-dependency integration suite passes:

```text
tests  13
pass   13
fail   0
```

Coverage includes exact action declaration, absent/classic/external protection reads, baseline normalization, exact create, stale-head and existing-protection create guards, serialized create drift, post-write policy verification, exact baseline removal, absent/stronger/signed/stale removal guards, serialized delete drift, definite transport errors, and mutation uncertainty after exactly one mutation with zero replay.

## 2. Immutable release

```text
releaseId           github-repository-branch-safety-governance-v1
targetVersion       0.1.1-preview.44-github-repository-branch-safety-governance
targetSurface       codexless-public-preview-v2
targetToolCount     172
fileCount           10
runtimeDependencies 1
manifestSha256      7d9c84c5aef0994f8515f43d256b0c9836d4970b461207f189a8e81e74037ba3
```

The release manifest is exact canonical JSON. All ten payload hashes match the manifest and every replacement baseline hash chains to the previously active preview.43 release.

Release preparation succeeded at source head `4e02b105e698265b72e449b8211a20aa20a22b14`.

A prepublication verify returned ten mismatches, as expected because the ten preview.44 targets had not yet been installed. Publication then completed successfully:

```text
operationId       rm_19ab2a2cf09ca4dedc9b588d5c8a9476
final status      succeeded
recoveryAttempted false
```

Postpublication verification returned:

```text
status         verified
mismatchCount  0
```

Activation restart completed successfully:

```text
operationId       rm_d09b14aec98ef81cc2ca587d14170268
final status      succeeded
recoveryAttempted false
```

A second postactivation release verification again returned zero mismatches.

## 3. Active runtime

Fresh local health and readiness both report:

```text
ok              true
service         codexless-public
version         0.1.1-preview.44-github-repository-branch-safety-governance
surfaceVersion  codexless-public-preview-v2
toolCount       172
```

Fresh stateless MCP `tools/list` reports:

```text
public tools  172
GitHub tools  108
```

All three new actions are present.

## 4. Wire contracts

### `github.get_branch_protection`

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
additionalProperties  false
```

Annotations:

```text
readOnlyHint     true
destructiveHint  false
idempotentHint   true
openWorldHint    true
```

### `github.create_branch_safety_protection`

```text
repository_full_name  required string 3..512
branch_name           required string 1..512
expected_head_sha     required hexadecimal string 7..64
additionalProperties  false
```

Annotations:

```text
readOnlyHint     false
destructiveHint  false
idempotentHint   false
openWorldHint    true
```

### `github.delete_branch_safety_protection`

The input schema is the same bounded three-field optimistic-concurrency contract as create.

Annotations:

```text
readOnlyHint     false
destructiveHint  true
idempotentHint   false
openWorldHint    true
```

No caller-selected protection body, required check/review, bypass actor, branch pattern, ruleset, force/deletion allowance, credential, GitHub host/endpoint, method/header, GraphQL document, transport, filesystem path or process authority is exposed.

## 5. Live read-only qualification

The two durable canonical branches currently read as:

```text
main
    head                     3c7bcc51b10bfac787aee4b12cc3cd0f6b553400
    protected                false
    codexlessSafetyBaseline  false

v1-frontend-spike
    head                     2480109fadeee1e480ef03b82e335aacdf9adf91
    protected                false
    codexlessSafetyBaseline  false
```

No protection mutation was needed to establish these reads.

## 6. Deterministic local no-write guards

### Guard 1: stale-head create

`github.create_branch_safety_protection` was called against exact branch `main` with deliberately stale:

```text
expected_head_sha  0000000
```

It failed before PUT with:

```text
errorCode          GITHUB_BRANCH_HEAD_CHANGED
retryable          false
mutationUncertain  false
githubRequestId    null
```

### Guard 2: remove absent protection

`github.delete_branch_safety_protection` was called against exact `main` using its real current SHA while protection was absent.

It failed before DELETE with:

```text
errorCode          GITHUB_BRANCH_SAFETY_PROTECTION_NOT_FOUND
retryable          false
mutationUncertain  false
githubRequestId    null
```

Read-only postflight then returned the same exact SHAs and `protected=false` for both `main` and `v1-frontend-spike`.

Therefore:

```text
positive branch-protection PUTs      0
positive branch-protection DELETEs   0
mutation retries                     0
mutation-uncertain results           0
canonical branch state changes       0
```

## 7. Authorization and next gate

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

The already-open persistent `chatgpt-22` host projection is expected to remain stale for newly activated preview.44 tools. The next gate is therefore a fresh disposable ChatGPT-host qualification of all three exact actions.

That fresh-host gate must capture the visible contracts, perform positive reads only, and run deterministic invalid no-write guards. No positive branch-protection mutation is authorized by this validation.

After the fresh-host gate passes, positive capability qualification may use only the frozen disposable branch family. Permanent protection of `main` and `v1-frontend-spike` remains a separate owner authorization after the tool family itself is proven end to end.

AB-030 remains parked unchanged.

## 8. Disposition

```text
VALIDATION202=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.44-github-repository-branch-safety-governance
LIVE_PUBLIC_TOOL_COUNT=172
LIVE_GITHUB_TOOL_COUNT=108
REPOSITORY_BRANCH_SAFETY_FAKE_TESTS=PASS_13_OF_13
REPOSITORY_BRANCH_SAFETY_WIRE_SCHEMA=PASS_3_OF_3
REPOSITORY_BRANCH_SAFETY_LOCAL_READS=PASS_2_OF_2
REPOSITORY_BRANCH_SAFETY_LOCAL_NO_WRITE_GUARDS=PASS_2_OF_2
REPOSITORY_BRANCH_SAFETY_POSITIVE_WRITES=0
REPOSITORY_BRANCH_SAFETY_MUTATION_RETRIES=0
REPOSITORY_BRANCH_SAFETY_MUTATION_UNCERTAIN_RESULTS=0
POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
PROTECTED_GITHUB_AUTHORIZATION=HEALTHY
CANONICAL_BRANCH_PROTECTION_MUTATION=NOT_AUTHORIZED
AB030=PARKED_UNCHANGED
NEXT=FRESH_CHAT_REPOSITORY_BRANCH_SAFETY_SCHEMA_GUARD_QUALIFICATION
```
