# Validation 173: GitHub PR/Review Mutation Preview.36 Live Surface Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.36 LIVE / NINETEEN PR-REVIEW MUTATION TOOLS LIVE / NO PR-REVIEW WRITE / FRESH-HOST PR-REVIEW SCHEMA GATE NEXT
**Research:** Research 123
**Scope:** Preserve implementation, immutable release publication/activation, local MCP wire qualification and fail-closed no-write guard evidence for the nineteen captured native GitHub pull-request/review mutation actions.

## 1. Starting boundary

Validation 172 / Checkpoint 415 closed the second native write family by positive-live qualifying all twelve issue mutation actions on dedicated qualification issue #83. The next family contains exactly nineteen pull-request/review mutations:

```text
github.add_reaction_to_pr
github.add_reaction_to_pr_review_comment
github.add_review_to_pr
github.convert_pull_request_to_draft
github.create_pull_request
github.dismiss_pull_request_review
github.enable_auto_merge
github.label_pr
github.mark_pull_request_ready_for_review
github.merge_pull_request
github.remove_pull_request_reviewers
github.remove_reaction_from_pr
github.remove_reaction_from_pr_review_comment
github.reply_to_review_comment
github.request_pull_request_reviewers
github.resolve_review_thread
github.unresolve_review_thread
github.update_pull_request
github.update_review_comment
```

This validation implements and activates all nineteen actions, but does not authorize or perform a positive pull-request/review mutation.

## 2. Implementation contract

The PR/review mutation service binds repository-specific writes to GitHub App installation-derived repository authority and fixed server-owned REST or GraphQL operations. Mutation-aware transport remains single-attempt: an uncertain mutation result is surfaced and is never automatically replayed. Same-pull-request and same-review-comment mutation sequences are serialized server-side.

The public caller surface is deliberately narrower than the captured native wrapper wherever hidden precedence or destructive concurrency would otherwise be ambiguous:

```text
reaction enum              +1 / -1 / laugh / confused / heart / hooray / rocket / eyes
review event enum          COMMENT / APPROVE / REQUEST_CHANGES
PR state enum              open / closed
merge method enum          merge / squash / rebase
review comment side        LEFT / RIGHT
review/file-comment cap    100 entries
reviewer/team cap          100 entries per list
body/comment max           65,536 characters
title max                     256 characters
```

`github.merge_pull_request` requires `expected_head_sha` even though the captured native projection makes that field optional. Runtime Bridge rereads the live pull request immediately before merge and refuses the mutation if the current head differs. This is an intentional optimistic-concurrency narrowing and is not presented as exact native wrapper parity.

`github.create_pull_request` supports same-repository head branches in this initial qualified surface. Conflicting `head`/`head_branch` or `base`/`base_branch` aliases fail closed, simultaneous `issue` plus `title` is rejected because native precedence is hidden, and cross-repository head authority is not inferred.

GraphQL node-ID operations such as review dismissal and review-thread resolve/unresolve first run a fixed server-owned scope query, derive the owning repository and pull-request number, and require that repository to be installation-authorized before dispatching the fixed mutation. Callers cannot provide arbitrary GraphQL documents.

`github.add_review_to_pr` requires a non-empty review body for COMMENT and REQUEST_CHANGES. Optional inline review comments must use bounded repository-relative paths and either position coordinates or explicit line/side coordinates. `github.request_pull_request_reviewers` and `github.remove_pull_request_reviewers` require at least one user or team reviewer.

No PR/review tool exposes caller-selected GitHub credentials/tokens, Authorization headers, host, arbitrary URL/endpoint, HTTP method/header, GraphQL document, permission profile, transport implementation, filesystem path, shell command or open-ended host authority.

## 3. Focused and reconstructed regression qualification

The focused PR/review mutation integration suite passed all four cases:

```text
all 19 fixed REST/GraphQL routes plus normalized outputs      PASS
semantic guards fail before write dispatch                   PASS
merge expected-head stale-object guard                       PASS
uncertain mutation single-attempt behavior                    PASS
```

The semantic guard coverage includes unsupported reaction input, an empty reviewer request, conflicting create-PR branch aliases and a COMMENT review without a review body. The merge guard verifies that a stale `expected_head_sha` causes rejection before the merge mutation.

A reconstructed broad current-source stage passed:

```text
GITHUB_READONLY_WIRE_SCHEMA=PASS tools=48
GITHUB_REPOSITORY_GIT_MUTATION_WIRE_SCHEMA=PASS tools=8
GITHUB_ISSUE_MUTATION_WIRE_SCHEMA=PASS tools=12
GITHUB_PR_REVIEW_MUTATION_WIRE_SCHEMA=PASS tools=19
PUBLIC_SURFACE_REGISTRATION=PASS tools=151
PR/review mutation regression PASS
issue mutation regression PASS
repository Git mutation regression PASS
all-read regression PASS
G0 regression PASS
read-only foundation PASS
bounded semantic Git count guards PASS tools=151
```

Local public-wire qualification confirms strict object schemas with `additionalProperties=false`, required-field sets, bounded enums/defaults, mutation annotations and the Runtime Bridge-only required merge concurrency SHA.

## 4. Immutable preview.36 release

Private local-runtime source head:

```text
70dd9d028e20d607e58aa1012b1b961125e6213e
```

preserves immutable release:

```text
releaseId               github-pr-review-mutations-v1
targetVersion           0.1.1-preview.36-github-pr-review-mutations
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         151
fileCount               10
regressionCount         16
runtimeDependencyCount  1
manifestSha256          ea3addeb85c89704a451285f0e6a2767f85a246bc410e502595c0722a974394b
```

The release bundle hash binding passed before commit. Syntax checks passed for all candidate source/test modules, the local-runtime repository was clean and synchronized after commit/push, and Runtime Release `prepare` succeeded.

Publication operation:

```text
rm_94f667f33c1350fae18a5a0214a0795d
```

succeeded with `errorCode=null` and no recovery. Restart operation:

```text
rm_8656dfe9141c9aa51ab1cba699063d34
```

then succeeded with no recovery. Postactivation verification returned:

```text
status                   verified
targetVersion            0.1.1-preview.36-github-pr-review-mutations
targetToolCount          151
fileCount                10
runtimeDependencyCount   1
manifestSha256           ea3addeb85c89704a451285f0e6a2767f85a246bc410e502595c0722a974394b
mismatchCount            0
```

No rollback or recovery path was required.

## 5. Live local MCP projection

Direct loopback health after activation returned:

```text
ok              true
version         0.1.1-preview.36-github-pr-review-mutations
surfaceVersion  codexless-public-preview-v2
toolCount       151
```

A stateless local MCP `tools/list` returned exactly:

```text
total public tools          151
GitHub tools                 87
GitHub read tools            48
repository Git writes         8
issue writes                 12
PR/review writes             19
```

All nineteen exact PR/review mutation names are present on the live Runtime Bridge.

## 6. Live no-write guard probes

Two live MCP calls deliberately failed during input validation before any PR/review handler or GitHub mutation dispatch:

1. `github.add_reaction_to_pr` with unsupported reaction `party` was rejected against the exact eight-value reaction enum.
2. `github.request_pull_request_reviewers` with both reviewer arrays empty was rejected with `at least one reviewer or team reviewer is required`.

These are deterministic no-write schema failures. No pull request, review, review comment, reaction, reviewer set, label, merge state, auto-merge state, draft state or review-thread state changed.

## 7. Authorization continuity

Immediately after preview.36 activation, protected authorization metadata reported:

```text
configured           true
initialized          false
authorized           true
storedAuthorization  true
accessExpired        false
refreshExpired       false
refreshRecommended   false
authMode             github-app-user-token-device-flow
host                 github.com
restApiVersion       2026-03-10
```

`initialized=false` is expected lazy post-restart state while protected authorization is durably stored. No authorization reset, clear, reconnect or device-flow mutation was performed, and no credential secret appeared.

## 8. Next boundary

This persistent `chatgpt-21` conversation predates preview.36 tool projection and is not authoritative for fresh-host availability of the nineteen new mutation actions. Direct local MCP proves the runtime itself is live at 151 tools / 87 GitHub actions, but host projection must be qualified in a refreshed disposable ChatGPT conversation.

The next gate is therefore one fresh-host schema/guard qualification that:

- verifies all nineteen exact PR/review action names project simultaneously;
- captures their host-visible descriptions/schemas/required fields/defaults/enums/constraints;
- checks that no caller-selected credential, token, GitHub host, arbitrary endpoint/method/header, GraphQL document, permission-profile, transport or host-process authority appears;
- exercises only deterministic invalid no-write guards;
- performs no positive PR/review mutation.

Positive-live PR/review mutation remains `0 / 19`. A later positive qualification requires a deliberately prepared disposable branch/pull-request/review fixture and must derive every PR/review/comment/reaction/thread ID from actual returned results. Destructive merge must remain separately controlled with exact expected-head binding rather than being mixed casually into general schema qualification.

Runtime Bridge now implements 39 of 41 captured native write action names and 87 of 89 captured native GitHub action names overall. Only the two Actions rerun mutations remain unimplemented. Exact native-wrapper parity remains conservatively `0 / 89` because hidden native output envelopes and unresolved native wrapper semantics are still explicit gaps.

```text
VALIDATION173=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.36-github-pr-review-mutations
LIVE_PUBLIC_TOOL_COUNT=151
LIVE_GITHUB_TOOL_COUNT=87
LIVE_GITHUB_READONLY_TOOLS=48
LIVE_GITHUB_REPOSITORY_GIT_MUTATION_TOOLS=8
LIVE_GITHUB_ISSUE_MUTATION_TOOLS=12
LIVE_GITHUB_PR_REVIEW_MUTATION_TOOLS=19
PR_REVIEW_MUTATION_WIRE_SCHEMA=PASS_19_OF_19
PR_REVIEW_MUTATION_POSITIVE_LIVE=0_OF_19
PR_REVIEW_GUARD_INVALID_REACTION=PASS_EXPECTED_REJECTION
PR_REVIEW_GUARD_EMPTY_REVIEWERS=PASS_EXPECTED_REJECTION
PR_REVIEW_MUTATION_OCCURRED=false
PROTECTED_AUTHORIZATION_PRESERVED=true
LOCAL_RUNTIME_SOURCE_HEAD=70dd9d028e20d607e58aa1012b1b961125e6213e
NATIVE_WRITE_ACTIONS_IMPLEMENTED=39
NATIVE_WRITE_ACTIONS_UNIMPLEMENTED=2
NATIVE_ACTION_NAMES_IMPLEMENTED=87_OF_89
EXACT_NATIVE_PARITY_ROWS_CLOSED=0
NEXT=FRESH_CHAT_PR_REVIEW_MUTATION_SCHEMA_QUALIFICATION
```
