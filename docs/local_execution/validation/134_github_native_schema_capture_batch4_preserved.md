# Validation 134: GitHub Native Schema Capture Batch 4 Preserved

**Date:** 2026-09-08
**Status:** PASS / 60 OF 89 HOST-VISIBLE CONTRACTS PRESERVED / DISCOVERY-ONLY / BATCH 5 NEXT
**Research:** Research 123
**Scope:** Preserve projected GitHub connector contracts 46-60 from the same fixed fresh 89-action GitHub-only conversation, including identity, installation/account discovery, repository pagination, PR-review listing semantics, recent-PR/issues internal pagination, organization listing ambiguity, and conversation-lock enum behavior, without invoking any GitHub action.

## 1. Qualification conditions

```text
projected GitHub action count      89
schema batch                        4
projected ordinals                  46-60
cumulative captured contracts       60 / 89
GitHub actions invoked               0
Browser / web / shell / ADS          not used
```

The batch begins with `GitHub.get_user_login` and ends with `GitHub.lock_issue_conversation`, exactly matching canonical inventory ordinals 46-60.

## 2. Projection-wide limitations remain stable

All fifteen actions continue the same host-projection pattern:

```text
separate action title metadata                 0 / 15 exposed
projected return type                         any for 15 / 15
machine-readable output schema                0 / 15 exposed
structured error schema                       0 / 15 exposed
```

Input contracts and descriptive behavior remain materially stronger than projected output/error contracts.

## 3. Four zero-argument actions are now explicit

Batch 4 confirms true zero-argument contracts for:

```text
GitHub.get_user_login
GitHub.list_installed_accounts
GitHub.list_user_org_memberships
GitHub.list_user_orgs
```

`get_user_login` semantically returns the authenticated login, but the projection does not reveal whether that is a raw string or wrapped object. The three listing actions project no paging controls or explicit continuation mechanism.

## 4. Installation/account discovery remains intentionally descriptive

`GitHub.list_installations` exposes only:

```text
manageable_only?: boolean = false
```

The description says this can limit results to managed setup account types, but the exact account-type set is not projected.

`GitHub.list_installed_accounts` says it lists **all** accounts on which the user installed the GitHub app, but no implementation-level all-pages/pagination mechanism is projected. That semantic word is preserved without inventing an internal paging algorithm.

## 5. Internal pagination and zero-based offset pagination coexist

Batch 4 adds several distinct pagination forms:

```text
GitHub.get_users_recent_prs_in_repo
    limit default 20
    limit is final result count
    internal pagination of GitHub search endpoint
    state examples open / closed / all are NOT an enum

GitHub.list_pr_changed_filenames
    ALL paginated file-list pages internally
    no caller page/cursor/limit inputs

GitHub.list_recent_issues
    top_k default 20
    internally paginate until top_k reached OR no more pages

GitHub.list_repositories
    page_size default 20
    page_offset default 0
    zero-based offset

GitHub.list_repositories_by_affiliation
    page_size default 100
    page_offset default 0
    affiliation examples owner / collaborator / organization_member are NOT an enum

GitHub.list_repositories_by_installation
    installation_id required
    page_size default 20
    page_offset default 0
```

This further confirms that parity requires per-action pagination semantics rather than translating all list operations into a single page/cursor model.

## 6. Review-thread/review pagination remains unspecified

`GitHub.list_pull_request_review_threads` semantically returns GraphQL review-thread nodes including comment bodies and resolution metadata.

`GitHub.list_pull_request_reviews` semantically returns GraphQL review nodes normalized into the connector review model.

For both actions:

```text
no page input
no cursor input
no continuation token
no explicit all-pages guarantee
return type any
```

The Runtime Bridge must not invent automatic full pagination from generic GraphQL expectations.

## 7. PR/repository listing semantics

`GitHub.get_users_recent_prs_in_repo` optionally includes diffs and comments in each result. The host still does not expose the resulting PR collection schema or size limits for included diff/comment content.

`GitHub.list_repositories` can optionally enrich each repository with code-search-index availability metadata through `include_search_index_status`, but those enrichment fields remain unprojected.

`GitHub.list_repositories_by_installation` confirms installation ID as a first-class repository-discovery selector, reinforcing the selected GitHub App installation-aware authority architecture.

## 8. Genuine lock-reason enum captured

Unlike the descriptive string examples for PR state and repository affiliation, `GitHub.lock_issue_conversation.lock_reason` is a true projected enum:

```text
off-topic
too heated
resolved
spam
```

The field is nullable and defaults to `null`.

This action mutates the conversation-lock state of either an issue or a pull request through GitHub's shared issue/conversation model. The projected return remains `any`.

## 9. Machine-readable preservation

`docs/research/github_connector_native_schema_capture.json` now records:

```text
status               PARTIAL_60_OF_89
capturedCount        60
batchesCompleted     [1, 2, 3, 4]
nextOrdinal          61
```

The validator now additionally guards:

```text
Batch 4 zero-argument contracts
recent-PR internal final-limit pagination
state examples remaining non-enum
all-pages changed-filename listing
top_k until-limit-or-exhaustion issue pagination
zero-based repository-list offset pagination
affiliation examples remaining non-enum
lock_reason exact four-value enum + null default
```

Observed result:

```text
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE=PASS
GITHUB_CONNECTOR_NATIVE_SCHEMA_CAPTURE_COUNT=60_OF_89
```

## 10. Exact continuation

Continue the same fixed GitHub-only conversation with projected ordinals 61-75, beginning with `GitHub.mark_pull_request_ready_for_review` and ending with `GitHub.search_branches`.

No GitHub action is to be invoked.

```text
VALIDATION134=PASS
NATIVE_SCHEMA_CAPTURE=60_OF_89
BATCH4=PASS
ACTIONS_INVOKED=0
INSTALLATION_AWARE_DISCOVERY=FURTHER_CONFIRMED
PAGINATION_POLICY=FURTHER_DIFFERENTIATED
ZERO_BASED_REPOSITORY_OFFSET=CONFIRMED
REVIEW_LIST_PAGINATION=UNSPECIFIED
LOCK_REASON_ENUM=EXACTLY_FOUR_VALUES
IMPLEMENTATION=NOT_STARTED
NEXT=SCHEMA_CAPTURE_BATCH_5_ORDINALS_61_75
```
