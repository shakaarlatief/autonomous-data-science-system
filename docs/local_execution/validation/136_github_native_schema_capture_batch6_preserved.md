# Validation 136: GitHub Native Schema Capture Batch 6 Preserved

**Date:** 2026-09-08
**Status:** PASS / 89 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / FINAL RECONCILIATION NEXT
**Research:** Research 123
**Scope:** Preserve projected GitHub connector contracts 76-89 from the same fixed fresh 89-action GitHub-only conversation, complete the discovery-only native contract capture, and retain the final search/update/ref semantics without invoking any GitHub action.

## 1. Qualification conditions

```text
projected GitHub action count      89
schema batch                        6
projected ordinals                  76-89
cumulative captured contracts       89 / 89
GitHub actions invoked               0
Browser / web / shell / ADS          not used
```

The batch begins with `GitHub.search_commits` and ends with `GitHub.update_review_comment`, exactly matching canonical inventory ordinals 76-89.

## 2. Discovery capture is complete but not yet reconciled

All 89 native projected action contracts are now represented in the machine schema artifact. The status deliberately remains:

```text
CAPTURED_89_OF_89_PENDING_FINAL_RECONCILIATION
```

because the final same-conversation reconciliation has not yet been performed. Completion of six batches is not silently promoted to a fully reconciled parity contract.

## 3. Search pagination adds three more distinct models

Batch 6 captures:

```text
GitHub.search_installed_repositories_streaming
    opaque next_token
    limit default 10
    next-token output field hidden behind any

GitHub.search_installed_repositories_v2
    1-based page
    limit default 10
    optional installation_ids

GitHub.search_repositories
    1-based page
    per_page
    topn alias for per_page
    no conflict/precedence rule when both supplied

GitHub.search_commits / search_issues / search_prs
    final topn
    no continuation interface projected
```

This further confirms that search/list parity requires action-specific continuation behavior.

## 4. Commit search exposes qualifier-only rejection plus a narrow empty-query exception

`GitHub.search_commits` exposes genuine enums:

```text
sort
    best-match
    author-date
    committer-date

order
    desc
    asc
```

Its description states that GitHub rejects qualifier-only commit queries. It also documents a narrow special case for listing recent commits: an empty query may be used with `repository_full_name`, using default descending ordering.

No selector-combination rule is projected for repository_full_name / repository_id / repository_url / org.

## 5. Issue and PR search contracts differ

`GitHub.search_issues` explicitly allows **at most one repository-selector family**. Empty selector lists mean no repository filter, and `repo:owner/name` may be embedded directly in the query.

`GitHub.search_prs` exposes the same scalar-or-array repository selector families but does **not** describe a mutual-exclusion rule, so none is inferred.

Exact enums include:

```text
search_issues.state
    open | closed

search_prs.state
    open | closed | all
```

Both expose `best-match | created | updated | comments | reactions | interactions` sort enums and `desc | asc` order enums.

## 6. Sequential file-write semantics are explicit

`GitHub.update_file` requires the current blob SHA and explicitly says:

```text
do not run update/delete writes for the same path in parallel
```

The description also exposes two semantic result values despite return type `any`:

```text
resulting commit SHA
content blob SHA
```

and names the content-blob result field `content_sha` for use in a subsequent sequential update.

This is direct evidence for a per-path sequential mutation guard in Runtime Bridge parity.

## 7. Issue-update replacement semantics and milestone gap are explicit

`GitHub.update_issue` exposes:

```text
state
    open | closed

state_reason
    completed | not_planned | duplicate | reopened
```

`assignees` and `labels` are the **full replacement sets**, not additive deltas.

The projected wrapper explicitly does **not** expose a way to clear an existing milestone. That limitation must be preserved rather than silently adding a stronger parity capability.

No at-least-one patch-field requirement is projected.

## 8. `update_ref` remains branch-oriented

`GitHub.update_ref` exposes:

```text
repository_full_name
branch_name
sha
force = false
```

`force=true` permits a forced update; default behavior is non-forced. The action-level contract is branch-oriented and exposes no tag selector or broader Git ref namespace.

The field description says the branch may be created or updated, but this does not establish general tag/ref mutation capability.

## 9. Review-comment update differs from reply creation

`GitHub.update_review_comment` applies to both an inline review comment and a reply.

This differs from `reply_to_review_comment`, whose creation contract only permits replying to a thread's top-level inline review comment and rejects replies-to-replies.

That asymmetry is preserved explicitly.

## 10. Machine-readable preservation

`docs/research/github_connector_native_schema_capture.json` now records:

```text
status               CAPTURED_89_OF_89_PENDING_FINAL_RECONCILIATION
capturedCount        89
batchesCompleted     [1, 2, 3, 4, 5, 6]
nextOrdinal          null
```

The validator now guards all Batch 6 action order and key semantics, including:

```text
search_commits sort/order enums + qualifier-only rule
streaming opaque next_token continuation
installed-repository-v2 1-based paging
search_issues selector-family constraint + state enum
search_prs state enum
search_repositories page + topn/per_page alias
update_file content_sha + sequential same-path write rule
update_issue state_reason enum + milestone-clear gap
update_pull_request state enum
update_ref force=false + branch-only scope
update_review_comment reply-support distinction
Batch 6 6-read / 8-mutation distribution
```

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=89_OF_89
```

## 11. Exact continuation

Return to the same fixed GitHub-only conversation and run the already-preserved final reconciliation message. No GitHub action should be invoked.

The reconciliation must determine whether all 89 host-visible contracts were sufficiently captured, list every remaining genericized/truncated/ambiguous contract, and decide whether stronger result/output evidence is required before implementation.

```text
VALIDATION136=PASS
NATIVE_SCHEMA_CAPTURE=89_OF_89
BATCH6=PASS
ACTIONS_INVOKED=0
FULL_DISCOVERY_CAPTURE=COMPLETE
FINAL_RECONCILIATION=PENDING
SEARCH_PAGINATION=FURTHER_DIFFERENTIATED
UPDATE_FILE_SEQUENTIAL_GUARD=CAPTURED
UPDATE_ISSUE_MILESTONE_CLEAR=NOT_EXPOSED
UPDATE_REF_SCOPE=BRANCH_ORIENTED
IMPLEMENTATION=NOT_STARTED
NEXT=FINAL_89_ACTION_SCHEMA_RECONCILIATION
```
