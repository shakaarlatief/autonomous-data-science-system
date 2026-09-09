# Validation 167: Repository Git Mutation Preview.34 Live Surface Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.34 LIVE / EIGHT REPOSITORY-GIT MUTATION TOOLS LIVE / NO LIVE GITHUB MUTATION / FRESH-HOST GATE NEXT
**Research:** Research 123
**Scope:** Preserve implementation, release publication/activation, local MCP projection and fail-closed live guard qualification for the first eight GitHub mutation actions without dispatching any GitHub write.

## 1. Starting boundary

Validation 166 / Checkpoint 409 closed the complete 48-action GitHub read phase and opened implementation of the first mutation family. The selected family contains exactly eight repository Git/content actions:

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

Checkpoint 409 authorized implementation and synthetic/non-network qualification, but explicitly did not authorize a live GitHub mutation. This validation therefore activates and inspects the mutation surface while keeping `GITHUB_MUTATION_OCCURRED=false`.

## 2. Mutation safety contract

The preview.34 implementation preserves installation-derived repository authority before repository-specific operations and exposes only fixed semantic GitHub operations. No caller can select a credential, token, GitHub host, REST endpoint, HTTP method/header, arbitrary GraphQL document, ref namespace, permission profile or transport implementation.

The mutation service marks every actual write request as `mutation=true` at the fixed GitHub REST transport boundary. Transport uncertainty remains fail-visible as `GITHUB_MUTATION_RESULT_UNCERTAIN`, with `mutationUncertain=true` and no automatic retry.

Additional guards are:

```text
create_branch
    exactly one of sha or base_ref
    branch-only refs/heads namespace

create_file / update_file / delete_file
    same repository/branch/path writes serialized server-side
    update/delete require current content blob SHA

create_tree
    strict platform-backed nested entry schema
    mode enum 100644 / 100755 / 040000 / 160000 / 120000
    type enum blob / tree / commit
    exactly one of sha or content
    sha=null permitted for deletion semantics

update_ref
    branch-only refs/heads namespace
    force defaults false
    force=true fails closed as GITHUB_FORCE_REF_UPDATE_NOT_QUALIFIED
```

The service bounds UTF-8 mutation content to 2 MiB, tree entry count to 1,000, additional commit parents to 16, and branch/path/message/object selectors to explicit envelopes.

## 3. Candidate synthetic qualification

Before publication, the candidate passed focused fake/server-owned transport qualification. Evidence included:

```text
GITHUB_READONLY_WIRE_SCHEMA=PASS tools=48
GITHUB_REPOSITORY_GIT_MUTATION_WIRE_SCHEMA=PASS tools=8
PUBLIC_SURFACE_REGISTRATION=PASS tools=120

repository mutation focused tests
    fixed scoped REST and normalized results   PASS
    fail-closed mutation input guards          PASS
    same-path Contents serialization           PASS
    uncertain mutation single-attempt behavior PASS
```

Existing all-read, G0, read-only-foundation and bounded semantic-Git regressions also remained green in the reconstructed candidate stage. No external GitHub mutation was used for these tests.

## 4. First immutable release v1 and abnormal publication failure

Private local-runtime head:

```text
8f80ae324023bf21405a3cd9c1d222adf9247f1d
```

first preserved release:

```text
releaseId               github-repository-git-mutations-v1
targetVersion           0.1.1-preview.34-github-repository-git-mutations
targetToolCount         120
fileCount               10
regressionCount         16
runtimeDependencyCount  1
manifestSha256          bb23fd21f0efe6081a9e3c2176eae9d1e522f5218637aafcedd6fe9b12b613b1
```

Preparation succeeded and prepublication verification produced the expected ten mismatches against live preview.33. Publication operation `rm_7b4a4beac959311db574b75268cde9ba` later terminated with:

```text
status     failed
errorCode  RUNTIME_RELEASE_PUBLICATION_ROLLBACK_FAILED
```

The public operation receipt does not expose the original forward-publication failure that entered the publisher's recovery path. This validation therefore does not invent that cause.

A structural release-engine weakness was nevertheless identified independently from the publisher contract. Runtime Release v2 reruns the target release's regression list after restoring the previous source snapshot. The v1 matrix included the new add-mode path `test/github-repository-git-mutations-integration.mjs`. Correct restoration removes that target-only file, so the same target regression matrix is not rollback-compatible and can itself make rollback validation fail. This explains the wrapped rollback failure mode but does not establish the hidden original forward trigger.

A post-failure release verification returned ten target mismatches, showing that preview.34 was not left installed across any declared release target. The later successful v2 publication necessarily passed Runtime Release's exact expected-current baseline verification, which establishes the expected preview.33 baseline immediately before the corrected target was applied. GitHub authorization also remained healthy.

## 5. Rollback-compatible immutable v2 release

The correction did not weaken Runtime Release and did not rewrite the already-prepared v1 release. A new immutable release was created at private local-runtime head:

```text
fc86cdc827d8c6850539e3f94052d6209f4152f4
```

with:

```text
releaseId               github-repository-git-mutations-v2
targetVersion           0.1.1-preview.34-github-repository-git-mutations
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         120
fileCount               10
regressionCount         16
runtimeDependencyCount  1
manifestSha256          e1cd6cc585cbd6b38bf0a90a364cd484d71fbe485168d28621948db56d086960
```

The focused mutation integration test remains preserved in the immutable bundle and had already passed independently, but it is no longer a Runtime Release rollback regression. The sixteen release regressions instead use paths that exist on both target and restored previous source, including the prior `github-all-readonly-integration` regression.

The first v2 prepare attempt rejected a noncanonical working-tree JSON encoding with `RUNTIME_RELEASE_MANIFEST_NONCANONICAL`. The manifest was normalized to Runtime Release's exact `JSON.stringify(..., null, 2) + newline` contract. Git observed no semantic content change to commit; the next prepare used the same clean source head and succeeded.

Prepublication verification again produced the expected ten mismatches. Publication operation:

```text
rm_de22ee201cfe489bc97f4b795841b6dc
```

completed successfully with `errorCode=null` and no recovery.

Restart operation:

```text
rm_0ddd5b6891b5c60ac2e667964363460d
```

then activated preview.34 successfully with no recovery. Postactivation verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.34-github-repository-git-mutations
targetToolCount          120
fileCount                10
runtimeDependencyCount   1
mismatchCount            0
```

## 6. Live process, authorization and MCP projection

Direct loopback health after activation returned:

```text
ok             true
service        codexless-public
transport      streamable-http
version        0.1.1-preview.34-github-repository-git-mutations
surfaceVersion codexless-public-preview-v2
toolCount      120
```

Protected GitHub authorization remained:

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

A fresh stateless loopback MCP `initialize -> tools/list` returned exactly:

```text
serverVersion    0.1.1-preview.34-github-repository-git-mutations
totalToolCount   120
githubToolCount  56
read tools        48
mutation tools     8
```

All eight exact mutation names were present. Their serialized wire schemas were strict objects with `additionalProperties=false`. All eight report `readOnlyHint=false`, `idempotentHint=false` and `openWorldHint=true`. Create-object/create-branch/create-file/create-tree actions report `destructiveHint=false`; delete/update-file/update-ref report `destructiveHint=true`.

The live schemas preserve the bounded contracts above. `create_blob` exposes only repository, bounded content and `utf-8|base64`; `create_branch` exposes branch plus nullable SHA/base-ref inputs; commit parents are bounded; Contents writes expose bounded paths/content/messages and optional branch; the tree nested object is strict; and update-ref exposes only repository, branch, SHA and boolean force defaulting false.

## 7. Live fail-closed guard probes without GitHub writes

Two live MCP calls were made specifically to prove mutation guards while preventing write dispatch. Both may perform installation-authority reads before reaching the action guard, but neither dispatched a GitHub mutation.

`github.create_branch` was called with both `sha` and `base_ref`. It returned:

```text
isError            true
errorCode          GITHUB_BRANCH_BASE_INVALID
retryable          false
mutationUncertain  false
status             null
githubRequestId    null
```

`github.update_ref` was called with `force=true`. It returned:

```text
isError            true
errorCode          GITHUB_FORCE_REF_UPDATE_NOT_QUALIFIED
retryable          false
mutationUncertain  false
status             null
githubRequestId    null
```

These are pre-mutation semantic rejections, not uncertain external writes. No branch, blob, tree, commit or repository content was created, updated or deleted.

## 8. Host projection and next gate

The already-open persistent `chatgpt-21` host remains stale for the eight newly activated mutation names, consistent with prior AB-008 evidence. Targeted tool rediscovery does not expose the new mutation definitions in this existing conversation, while fresh local MCP projection proves the 120-tool source is live.

Because these are mutation-sensitive actions, the next gate is a refreshed disposable ChatGPT conversation that performs discovery/schema qualification of exactly the eight new mutation tools before any positive live GitHub write is authorized. The fresh-host qualification should verify bounded fields and authority, and may use only fail-closed non-writing guard calls unless a later checkpoint explicitly opens a disposable live-mutation fixture.

The project still has 41 native write action names total. Eight are now implemented/live at the Runtime Bridge surface but have not yet been positively live-mutated. Exact native-wrapper parity remains conservatively `0 / 89` because hidden native output envelopes and unresolved wrapper semantics remain unclaimed.

```text
VALIDATION167=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.34-github-repository-git-mutations
LIVE_PUBLIC_TOOL_COUNT=120
LIVE_GITHUB_READONLY_TOOLS=48
LIVE_GITHUB_REPOSITORY_GIT_MUTATION_TOOLS=8
LIVE_GITHUB_TOOL_COUNT=56
REPOSITORY_GIT_MUTATION_WIRE_SCHEMA=PASS_8_OF_8
REPOSITORY_GIT_MUTATION_POSITIVE_LIVE=0_OF_8
CREATE_BRANCH_XOR_GUARD=PASS_EXPECTED_REJECTION
UPDATE_REF_FORCE_TRUE_GUARD=PASS_EXPECTED_REJECTION
V1_PUBLICATION=FAIL_ROLLBACK_WRAPPED
V1_FORWARD_FAILURE_CAUSE=UNOBSERVED
V1_POSTFAIL_SOURCE_BASELINE_RESTORED=true
V2_ROLLBACK_COMPATIBLE_MATRIX=true
V2_PUBLICATION=PASS
V2_ACTIVATION=PASS
V2_POSTACTIVATION_VERIFY=PASS_ZERO_MISMATCH
PROTECTED_AUTHORIZATION_PRESERVED=true
SECRETS_EXPOSED=false
GITHUB_MUTATION_OCCURRED=false
NATIVE_WRITE_ACTIONS_REMAINING=41
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_REPOSITORY_GIT_MUTATION_SCHEMA_QUALIFICATION
```
