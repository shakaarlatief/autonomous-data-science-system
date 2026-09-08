# Validation 135: GitHub Native Schema Capture Batch 5 Preserved

**Date:** 2026-09-08
**Status:** PASS / 75 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / FINAL BATCH NEXT
**Research:** Research 123
**Scope:** Preserve projected GitHub connector contracts 61-75 from the same fixed fresh 89-action GitHub-only conversation, including PR readiness/merge concurrency, reviewer mutations, reaction removals, inline review reply constraints, Actions rerun permissions, thread resolution, code search, and branch cursor semantics, without invoking any GitHub action.

## 1. Qualification conditions

```text
projected GitHub action count      89
schema batch                        5
projected ordinals                  61-75
cumulative captured contracts       75 / 89
GitHub actions invoked               0
Browser / web / shell / ADS          not used
```

The batch begins with `GitHub.mark_pull_request_ready_for_review` and ends with `GitHub.search_branches`, exactly matching canonical inventory ordinals 61-75.

## 2. Projection-wide limitations remain stable

All fifteen actions retain the established host-projection limitation:

```text
separate action title metadata                 0 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schema                0 / 15 exposed
structured error schema                       0 / 15 exposed
```

Batch 5 nevertheless exposes unusually strong descriptive mutation/concurrency semantics.

## 3. Pull-request merge concurrency is explicit

`GitHub.merge_pull_request` exposes:

```text
merge_method?: merge | squash | rebase | null
commit_title?: string | null
commit_message?: string | null
expected_head_sha?: string | null
```

`merge_method` is a genuine projected enum.

Most importantly, `expected_head_sha` is an explicit optimistic-concurrency guard: GitHub rejects the merge when the pull-request head moved after the caller's expected SHA.

The description identifies GitHub's merge result payload as:

```text
sha
merged
message
```

but the field types remain hidden behind `any`.

This directly supports the Research 123 requirement that Runtime Bridge merge parity preserve expected-head concurrency rather than silently merging a newer PR head.

## 4. Reviewer mutation ambiguity is preserved, not invented away

Both reviewer-request mutations expose optional arrays:

```text
reviewers?: string[] | null
team_reviewers?: string[] | null
```

For both `request_pull_request_reviewers` and `remove_pull_request_reviewers`:

```text
no array limits projected
no username/team-slug pattern projected
no at-least-one requirement projected
no XOR or other array relationship projected
```

The Runtime Bridge contract must not invent an at-least-one rule merely because the underlying GitHub API may behave that way in some cases.

## 5. Inline review reply constraint is exact

`GitHub.reply_to_review_comment` requires:

```text
comment_id = top-level inline review comment ID for the thread
```

and explicitly states:

```text
replies-to-replies are not supported by the API
```

This is a descriptive unsupported-input constraint that must be preserved even though the host projects no structured error enum.

## 6. Actions rerun permission and scope are explicit

Both Actions rerun mutations require GitHub Actions **write** permission.

```text
GitHub.rerun_failed_workflow_run_jobs
    rerun failed jobs only
    do not restart successful jobs as a full new attempt

GitHub.rerun_workflow_job
    rerun one specific workflow job
    description frames it for failed or cancelled jobs
```

Neither action exposes a result schema beyond `any`.

## 7. Search contracts diverge again

`GitHub.search` exposes:

```text
query: string
required

topn?: integer = 20
repository_name?: string | string[] | null
org?: string | null
```

Semantic rules include:

```text
plain-text query expected
avoid GitHub flags such as is:pr
empty query -> valid no-results result
code search covers default branch
fetch_file is the full-file retrieval path
topn is the final result limit
no page/cursor/continuation contract projected
```

`repository_name` may be one string or an array. Fully qualified repository names retain their explicit owner even when `org` is supplied.

`GitHub.search_branches`, by contrast, exposes a real cursor model:

```text
owner: string
repo_name: string
query: string
page_size?: integer = 20
cursor?: string | null
```

The cursor is explicitly opaque and comes from a previous branch search. Because the result is `any`, the field carrying the next cursor is not visible and must not be inferred.

## 8. Mutation/read distribution

Batch 5 is mutation-heavy:

```text
mutating actions    13 / 15
read-only actions    2 / 15

read-only:
    GitHub.search
    GitHub.search_branches
```

This is useful for later risk-scaled qualification planning: most Batch 5 parity tests will require disposable fixtures and explicit mutation safeguards.

## 9. Machine-readable preservation

`docs/research/github_connector_native_schema_capture.json` now records:

```text
status               PARTIAL_75_OF_89
capturedCount        75
batchesCompleted     [1, 2, 3, 4, 5]
nextOrdinal          76
```

The validator now additionally guards:

```text
merge_method exact enum
expected_head_sha concurrency rule
reviewer-array ambiguity
reply-to-review top-level-only rule
Actions write-permission requirements
search topn/no-continuation semantics
search empty-query valid-empty behavior
search_branches opaque cursor contract
Batch 5 mutation/read distribution
```

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=75_OF_89
```

## 10. Exact continuation

Continue the same fixed GitHub-only conversation with the final projected ordinals 76-89, beginning with `GitHub.search_commits` and ending with `GitHub.update_review_comment`.

No GitHub action is to be invoked.

```text
VALIDATION135=PASS
NATIVE_SCHEMA_CAPTURE=75_OF_89
BATCH5=PASS
ACTIONS_INVOKED=0
MERGE_EXPECTED_HEAD_CONCURRENCY=CAPTURED
MERGE_METHOD_ENUM=CAPTURED
REVIEWER_ARRAY_AT_LEAST_ONE_RULE=NOT_PROJECTED
INLINE_REVIEW_REPLY_TOP_LEVEL_ONLY=CAPTURED
ACTIONS_RERUN_WRITE_PERMISSION=CAPTURED
SEARCH_EMPTY_QUERY=VALID_EMPTY
BRANCH_SEARCH_CURSOR=OPAQUE_AND_EXPLICIT
IMPLEMENTATION=NOT_STARTED
NEXT=SCHEMA_CAPTURE_BATCH_6_ORDINALS_76_89
```
