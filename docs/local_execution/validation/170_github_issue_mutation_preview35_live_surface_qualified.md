# Validation 170: GitHub Issue Mutation Preview.35 Live Surface Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.35 LIVE / TWELVE ISSUE MUTATION TOOLS LIVE / NO ISSUE WRITE / FRESH-HOST ISSUE SCHEMA GATE NEXT
**Research:** Research 123
**Scope:** Preserve implementation, publication/activation, local MCP wire qualification and fail-closed no-write guard evidence for the twelve captured native GitHub issue mutation actions.

## 1. Starting boundary

Validation 169 / Checkpoint 412 closed the first native write family by positive-live qualifying all eight repository Git/content mutation actions on a disposable branch. The next family contains exactly twelve issue mutations:

```text
github.add_comment_to_issue
github.add_issue_assignees
github.add_issue_labels
github.add_reaction_to_issue_comment
github.create_issue
github.lock_issue_conversation
github.remove_issue_assignees
github.remove_issue_label
github.remove_reaction_from_issue_comment
github.unlock_issue_conversation
github.update_issue
github.update_issue_comment
```

This validation implements and activates those actions, but does not authorize or perform a positive issue mutation.

## 2. Implementation contract

The issue-mutation service binds repository-specific writes to GitHub App installation-derived repository authority and fixed server-owned REST endpoints. Actual writes use the existing mutation-aware transport with `mutation=true`; transport uncertainty remains fail-visible and is never automatically retried. Same-issue and same-comment mutation sequences are serialized server-side.

Caller envelopes are bounded beyond the generic native projection where GitHub platform rules are known:

```text
comment/body max length          65,536 characters
issue title max length              256 characters
add assignees max                    10 entries
remove assignees max                100 entries (conservative Runtime Bridge envelope)
labels max                           100 entries
reaction enum                         +1 / -1 / laugh / confused / heart / hooray / rocket / eyes
lock_reason enum                      off-topic / too heated / resolved / spam
state enum                            open / closed
state_reason enum                     completed / not_planned / duplicate / reopened
```

`update_issue` preserves native replacement-set semantics for assignees and labels. `state_reason` requires an explicit `state` in the same Runtime Bridge request. Null optional values are omitted rather than silently inventing clearing semantics. The captured native wrapper does not expose an explicit milestone-clear operation, so Runtime Bridge does not invent one.

No issue tool exposes caller-selected GitHub credentials/tokens, Authorization headers, GitHub host, arbitrary URL/endpoint, HTTP method/header, GraphQL document, permission profile, transport implementation, filesystem path, shell command or other open-ended host authority.

## 3. Focused and reconstructed regression qualification

The focused issue mutation integration test passed all four cases:

```text
fixed installation-scoped REST operations / normalized results   PASS
fail-closed issue mutation guards before mutation transport      PASS
same-issue serialization                                         PASS
uncertain mutation single-attempt behavior                       PASS
```

The guard cases include invalid reaction, invalid lock reason, `state_reason` without state, and an eleven-assignee add request. No mutation transport call occurs for those guard failures.

A reconstructed broad current-source stage also passed:

```text
GITHUB_READONLY_WIRE_SCHEMA=PASS tools=48
GITHUB_REPOSITORY_GIT_MUTATION_WIRE_SCHEMA=PASS tools=8
GITHUB_ISSUE_MUTATION_WIRE_SCHEMA=PASS tools=12
PUBLIC_SURFACE_REGISTRATION=PASS tools=132
repository Git mutation regression PASS
all-read regression PASS
G0 regression PASS
read-only foundation PASS
bounded semantic Git count guards PASS tools=132
```

A manual attempt to extend the reconstructed stage to every release regression later encountered an unchanged historical test path absent from that temporary reconstruction. That is a local stage-assembly incompleteness, not a candidate regression failure. Runtime Release `prepare` is the authoritative complete release-regression gate.

## 4. Immutable preview.35 release

Private local-runtime source head:

```text
6f1651a0c5258f1d9185962798f43babdf7ba018
```

preserves immutable release:

```text
releaseId               github-issue-mutations-v1
targetVersion           0.1.1-preview.35-github-issue-mutations
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         132
fileCount               10
regressionCount         16
runtimeDependencyCount  1
manifestSha256          66802022e3e8375b0eab14b395d74462de6f8e067c4996ee14d190d642c354ea
```

The immutable bundle uses the rollback-compatible sixteen-regression matrix already established by preview.34 v2. The new add-mode focused issue-mutation test remains preserved and independently qualified but is deliberately not in the release rollback matrix, avoiding the target-only regression-path hazard found during preview.34 v1.

Preparation succeeded. Prepublication verification returned the expected ten target mismatches. Publication operation:

```text
rm_cfe9e661da3d6035b6f4f7273089a304
```

succeeded with `errorCode=null` and no recovery. Restart operation:

```text
rm_0fc4891d51a6ec8c18932ed772000b9d
```

then succeeded with no recovery. Postactivation verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.35-github-issue-mutations
targetToolCount          132
fileCount                10
runtimeDependencyCount   1
mismatchCount            0
```

## 5. Live local MCP projection

Direct loopback health after activation returned HTTP 200 with:

```text
version        0.1.1-preview.35-github-issue-mutations
surfaceVersion codexless-public-preview-v2
toolCount      132
```

A fresh stateless MCP `tools/list` returned exactly:

```text
total public tools      132
GitHub tools             68
GitHub read tools        48
repository Git writes     8
issue writes             12
```

All twelve exact issue mutation names are present. Local wire tests establish strict `additionalProperties=false` object schemas and the declared bounded/default/enum constraints.

## 6. Live no-write guard probes

Two live MCP calls deliberately fail at schema validation before any handler or GitHub mutation dispatch.

`github.add_reaction_to_issue_comment` with reaction `party` returned an input-validation error stating that reaction must be one of the eight bounded platform values.

`github.update_issue` with `state_reason=completed` but `state=null` returned an input-validation error:

```text
state_reason requires state
```

These are host/MCP schema-level fail-closed rejections, not uncertain mutation attempts. No issue, comment, reaction, label, assignee or lock state was changed.

## 7. Authorization continuity

Immediately after restart, protected authorization metadata reported the stored access token as expired but the refresh token valid, with authorization still true and refresh recommended. A single safe read-only `github.get_user_login` call then exercised normal token-manager refresh. The read succeeded for `shakaarlatief`. Subsequent metadata reported:

```text
configured           true
initialized          true
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
```

No authorization reset, clear, reconnect or new device flow was used. No credential secret appeared.

## 8. Next boundary

This persistent `chatgpt-21` conversation predates preview.35 projection and must not be used to infer fresh-host availability of the twelve new mutation actions. The next gate is one refreshed disposable ChatGPT conversation that verifies all twelve exact issue mutation names and their bounded caller schemas, then performs only fail-closed non-writing guard calls.

Positive-live issue mutation remains `0 / 12`. A later positive qualification should create one dedicated disposable issue and derive all comment/reaction IDs from returned results. Because the captured native surface exposes no issue-delete action, the final test issue should be closed and retained as an explicit qualification artifact rather than silently cleaned up with non-parity authority.

The native write inventory now has twenty implemented mutation actions in Runtime Bridge, while twenty-one remain unimplemented: nineteen PR/review actions and two Actions rerun actions. Exact native-wrapper parity remains conservatively `0 / 89` because hidden native output schemas and unresolved native wrapper semantics are still not inferred.

```text
VALIDATION170=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.35-github-issue-mutations
LIVE_PUBLIC_TOOL_COUNT=132
LIVE_GITHUB_TOOL_COUNT=68
LIVE_GITHUB_READONLY_TOOLS=48
LIVE_GITHUB_REPOSITORY_GIT_MUTATION_TOOLS=8
LIVE_GITHUB_ISSUE_MUTATION_TOOLS=12
ISSUE_MUTATION_WIRE_SCHEMA=PASS_12_OF_12
ISSUE_MUTATION_POSITIVE_LIVE=0_OF_12
ISSUE_MUTATION_GUARD_INVALID_REACTION=PASS_EXPECTED_REJECTION
ISSUE_MUTATION_GUARD_STATE_REASON_REQUIRES_STATE=PASS_EXPECTED_REJECTION
ISSUE_MUTATION_OCCURRED=false
PROTECTED_AUTHORIZATION_PRESERVED=true
LOCAL_RUNTIME_SOURCE_HEAD=6f1651a0c5258f1d9185962798f43babdf7ba018
NATIVE_WRITE_ACTIONS_IMPLEMENTED=20
NATIVE_WRITE_ACTIONS_UNIMPLEMENTED=21
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_ISSUE_MUTATION_SCHEMA_QUALIFICATION
```
