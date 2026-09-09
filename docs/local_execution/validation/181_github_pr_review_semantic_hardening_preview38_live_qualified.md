# Validation 181: GitHub PR/Review Semantic Hardening Preview.38 Live Qualified

**Date:** 2026-09-09
**Status:** PASS / PREVIEW.38 LIVE / DISMISSAL AND AUTO-MERGE PRECONDITIONS FAIL CLOSED / ZERO NEW GITHUB MUTATIONS
**Research:** Research 123

## 1. Starting boundary

Validation 180 / Checkpoint 423 classified the six remaining PR/review positive-live gaps. Two actions, `github.update_pull_request` and `github.merge_pull_request`, are independently isolatable. Four actions are environment-gated. The same design identified two Runtime Bridge semantic preflight gaps that should be corrected before any further dismissal or auto-merge testing:

- COMMENTED/non-dismissible reviews should fail before dismissal mutation dispatch;
- repositories with `allow_auto_merge=false` should fail before auto-merge GraphQL mutation dispatch.

This validation implements and activates those corrections without changing the public tool schemas and without performing a new positive GitHub mutation.

## 2. Dismiss-review hardening

The fixed `node.pull_request_review_scope` query now resolves:

```text
id
databaseId
state
pull-request number
repository owner/name
```

`github.dismiss_pull_request_review` now:

1. resolves the caller-supplied GraphQL review node ID through that fixed query;
2. rejects before mutation unless review state is `APPROVED` or `CHANGES_REQUESTED`;
3. serializes by the owning PR;
4. re-resolves the same node immediately before mutation and verifies repository, PR number and database ID have not drifted;
5. rechecks dismissible state;
6. dispatches GitHub's fixed REST review-dismissal endpoint with the resolved database ID and body `{message, event: DISMISS}`;
7. keeps the existing caller-visible GraphQL node-ID input contract unchanged.

Using the fixed REST endpoint means a GitHub HTTP validation response such as 422 is a classified response with `mutationUncertain=false`; only transport failure before a classifiable response remains uncertain.

## 3. Auto-merge hardening

`github.enable_auto_merge` already preflights the PR and repository metadata. Preview.38 adds a deterministic guard:

```text
repository allow_auto_merge must be exactly true
```

If repository auto-merge is disabled, Runtime Bridge returns `GITHUB_AUTO_MERGE_DISABLED` before any GraphQL mutation. Merge-method inference remains server-owned and unchanged for repositories where auto-merge is enabled.

## 4. Regression qualification

Focused PR/review integration passes 4/4 after the hardening. The semantic guard test now verifies both new guards produce no mutation transport call. The positive fixture test verifies dismissal uses the fixed REST endpoint and still normalizes `DISMISSED` review output.

A manual reconstructed broad stage reached the bounded command sandbox timeout while installing dependencies; a subsequent attempt inherited an incomplete `node_modules` and failed on missing `zod/v4`. This was stage-assembly incompleteness rather than a source/test regression. Runtime Release `prepare` is the authoritative complete release-regression gate and succeeded for this exact hash-bound release.

Candidate syntax checks, manifest hash binding and focused tests all passed before release preparation.

## 5. Immutable preview.38 release

Private local-runtime source head:

```text
7eda5dbce805dd4452d4ec6a667ee39e4e45fc74
```

Immutable release:

```text
releaseId               github-pr-review-semantic-hardening-v1
targetVersion           0.1.1-preview.38-github-pr-review-semantic-hardening
targetSurfaceVersion    codexless-public-preview-v2
targetToolCount         153
fileCount               4
regressionCount         16
runtimeDependencyCount  1
manifestSha256          7edebf36973d619e808773b74ddc5a37c96c79830db5dd7ebb411b219892cb0c
```

`prepare` succeeded. Prepublication verify returned the expected four target mismatches because preview.38 was not yet installed. Publication operation `rm_0f90c312dbeef95f087c33e36b70282f` succeeded without recovery. Restart operation `rm_2c63a4ae62bf7a60cda02c1486c7f88e` succeeded without recovery. Postactivation verification returned `status=verified`, `targetToolCount=153` and `mismatchCount=0`.

## 6. Live no-write qualification

Live loopback health after activation reports:

```text
version         0.1.1-preview.38-github-pr-review-semantic-hardening
surfaceVersion  codexless-public-preview-v2
toolCount       153
GitHub tools     89
```

Two local-live calls intentionally targeted the known gated PR #84 state.

### COMMENTED review dismissal

`github.dismiss_pull_request_review` on review node `PRR_kwDOTxqesM8AAAABM3Ccrw` returned:

```text
error                 GitHub pull-request review must be APPROVED or CHANGES_REQUESTED before dismissal
errorCode             GITHUB_PR_REVIEW_NOT_DISMISSIBLE
source                runtime-bridge
retryable             false
mutationUncertain     false
```

The rejection occurs after read-only scope resolution and before dismissal mutation dispatch. The previous COMMENTED-review uncertainty condition is therefore removed from the live runtime. No replay of the Validation 175 dismissal mutation occurred.

### Repository auto-merge disabled

`github.enable_auto_merge` on PR #84 returned:

```text
error                 GitHub repository does not allow pull-request auto-merge
errorCode             GITHUB_AUTO_MERGE_DISABLED
source                runtime-bridge
retryable             false
mutationUncertain     false
```

This rejection occurs after read-only PR/repository preflight and before GraphQL mutation dispatch.

No GitHub PR/review state changed during either guard qualification. Protected GitHub authorization remains configured, stored, authorized, non-expired and not recommended for refresh.

## 7. Remaining positive-live boundary

The hardening changes failure certainty, not fixture availability. Current positive-live write coverage remains 35/41.

The six remaining actions remain classified:

```text
github.update_pull_request
    READY_FOR_ISOLATED_POSITIVE_FIXTURE

github.merge_pull_request
    READY_FOR_ISOLATED_POSITIVE_FIXTURE

github.dismiss_pull_request_review
    SECOND_REVIEWER_FIXTURE_GATED

github.enable_auto_merge
    REPOSITORY_CONFIGURATION_GATED

github.request_pull_request_reviewers
    SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED

github.remove_pull_request_reviewers
    SECOND_REVIEWER_OR_TEAM_FIXTURE_GATED
```

The current environment can reach 37/41 by qualifying update+merge on a fresh isolated disposable PR. That sequence requires separate explicit owner authorization because it creates new GitHub branches/file/PR metadata and merges into a disposable base branch.

```text
VALIDATION181=PASS
LIVE_RUNTIME_VERSION=0.1.1-preview.38-github-pr-review-semantic-hardening
LIVE_PUBLIC_TOOL_COUNT=153
LIVE_GITHUB_TOOL_COUNT=89
DISMISS_REVIEW_COMMENTED_GUARD=PASS_NO_WRITE
DISMISS_REVIEW_COMMENTED_MUTATION_UNCERTAIN=false
AUTO_MERGE_DISABLED_GUARD=PASS_NO_WRITE
AUTO_MERGE_DISABLED_MUTATION_UNCERTAIN=false
PR_REVIEW_HARDENING_GITHUB_MUTATION_OCCURRED=false
NATIVE_WRITE_POSITIVE_LIVE=35_OF_41
NATIVE_WRITE_POSITIVE_REMAINING=6
CURRENT_ENVIRONMENT_MAX_POSITIVE_LIVE=37_OF_41
PR84_MUTATION_REPLAY_AFTER_UNCERTAINTY=0
NEXT=EXPLICIT_OWNER_AUTHORIZATION_FOR_ISOLATED_UPDATE_AND_MERGE_PR_FIXTURE
```
