# GitHub Connector 89-Action Native Schema Capture

**Date:** 2026-09-08
**Status:** BATCH 2 PRESERVED / 30 OF 89 CONTRACTS CAPTURED / BATCH 3 NEXT
**Research:** Research 123
**Purpose:** Capture the exact native GitHub connector action contracts from one fixed fresh 89-action projection without invoking any GitHub action.

## Fixed projection evidence

The fresh GitHub-only schema-capture conversation completed its inventory phase with exactly 89 projected actions and zero action invocations. The count matches Validation 128.

Comparison against the Checkpoint 372 reconstructed inventory exposed one exact-name reconstruction defect while leaving the count unchanged:

```text
fresh projection contains      GitHub.download_user_content
Checkpoint 372 reconstruction  GitHub.add_issue_comment

fresh projection also contains GitHub.add_comment_to_issue
fresh projection does not contain GitHub.add_issue_comment
```

Because Validation 128 did not publicly preserve all exact action names, this is classified as `RECONSTRUCTION_DEFECT_NOT_CONNECTOR_DRIFT`. The exact fresh projected order is now canonical in `github_connector_89_action_inventory.json`.

Continue all remaining schema batches in this same GitHub-only conversation so every schema is captured from one fixed host projection.

## Qualification rules

Use one fresh GitHub-only conversation and keep the projection fixed for all batches.

```text
GitHub connector only
no Runtime Bridge / developer MCP
no Browser
no web search
no shell
no Codex Agent
no repository mutation
no issue/PR/review/Actions mutation
no generic fetch invocation merely to probe an endpoint
```

Tool/action discovery and schema inspection are sufficient. Do not invoke mutating actions.

The inventory phase is complete. For every remaining requested action capture:

```text
exact action name
title and full description
complete input schema
required fields
optional fields
enum values
validation constraints / limits
pagination / cursor / continuation / limit semantics visible in the contract
whether read-only or mutating
GitHub resource/object scope
visible result-shape and error-contract notes
```

Do not infer undocumented fields. If the host projection genericizes, truncates or omits anything, report that exact limitation.

## Batch 1: projected actions 1-15

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Do not use Browser, web search, shell, ADS/Runtime Bridge, or another connector.

For each action below, report the complete contract fields defined above.

GitHub.add_comment_to_issue
GitHub.add_issue_assignees
GitHub.add_issue_labels
GitHub.add_reaction_to_issue_comment
GitHub.add_reaction_to_pr
GitHub.add_reaction_to_pr_review_comment
GitHub.add_review_to_pr
GitHub.compare_commits
GitHub.convert_pull_request_to_draft
GitHub.create_blob
GitHub.create_branch
GitHub.create_commit
GitHub.create_file
GitHub.create_issue
GitHub.create_pull_request

After these actions, stop. Do not continue into the next batch.
```

### Batch 1 preservation result

Batch 1 completed with zero GitHub action invocations and is preserved by Validation 131 / Checkpoint 374 plus `github_connector_native_schema_capture.json`.

```text
captured contracts                         15 / 89
separate action title metadata exposed      0 / 15
projected return type                       any for 15 / 15
machine-readable output schemas exposed     0 / 15
structured error schemas exposed            0 / 15
pagination-bearing inputs exposed            0 / 15
```

Exact enums observed in this batch are `add_review_to_pr.action = COMMENT | APPROVE | REQUEST_CHANGES` and `create_blob.encoding = utf-8 | base64` with default `utf-8`. Several conditional constraints are descriptive rather than structurally encoded. Final parity reconciliation must preserve this distinction and determine whether additional live-result evidence is needed for exact normalized output shapes.

## Batch 2: projected actions 16-30

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Capture the same complete contract fields for:

GitHub.create_tree
GitHub.delete_file
GitHub.dismiss_pull_request_review
GitHub.download_user_content
GitHub.download_workflow_artifact
GitHub.enable_auto_merge
GitHub.fetch
GitHub.fetch_blob
GitHub.fetch_commit
GitHub.fetch_commit_workflow_runs
GitHub.fetch_file
GitHub.fetch_issue
GitHub.fetch_issue_comments
GitHub.fetch_pr
GitHub.fetch_pr_comments

After these actions, stop. Do not continue into the next batch.
```

### Batch 2 preservation result

Validation 132 / Checkpoint 375 preserve cumulative schema capture at `30 / 89` with zero GitHub action invocations. Batch 2 confirms action-specific pagination and a stronger host genericization:

```text
GitHub.create_tree.tree_elements        { [key: string]: any }[]
GitHub.fetch_commit_workflow_runs       FIRST PAGE ONLY
GitHub.fetch_issue_comments             ALL PAGES internally
GitHub.fetch_pr_comments                 pagination unspecified
GitHub.download_user_content             private-user-images.githubusercontent.com only
GitHub.download_workflow_artifact        reusable file reference after redirect
```

`fetch_issue.repository_url` also explicitly documents GitHub Enterprise Server custom hostnames and GHE.com API hosts, which is now an architecture follow-up rather than an assumed global host capability.

## Batch 3: projected actions 31-45

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Capture the same complete contract fields for:

GitHub.fetch_pr_file_patch
GitHub.fetch_pr_patch
GitHub.fetch_workflow_job_logs
GitHub.fetch_workflow_job_steps
GitHub.fetch_workflow_run_artifacts
GitHub.fetch_workflow_run_jobs
GitHub.get_commit_combined_status
GitHub.get_issue_comment_reactions
GitHub.get_pr_diff
GitHub.get_pr_info
GitHub.get_pr_reactions
GitHub.get_pr_review_comment_reactions
GitHub.get_profile
GitHub.get_repo
GitHub.get_repo_collaborator_permission

After these actions, stop. Do not continue into the next batch.
```

## Batch 4: projected actions 46-60

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Capture the same complete contract fields for:

GitHub.get_user_login
GitHub.get_users_recent_prs_in_repo
GitHub.label_pr
GitHub.list_installations
GitHub.list_installed_accounts
GitHub.list_pr_changed_filenames
GitHub.list_pull_request_review_threads
GitHub.list_pull_request_reviews
GitHub.list_recent_issues
GitHub.list_repositories
GitHub.list_repositories_by_affiliation
GitHub.list_repositories_by_installation
GitHub.list_user_org_memberships
GitHub.list_user_orgs
GitHub.lock_issue_conversation

After these actions, stop. Do not continue into the next batch.
```

## Batch 5: projected actions 61-75

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Capture the same complete contract fields for:

GitHub.mark_pull_request_ready_for_review
GitHub.merge_pull_request
GitHub.remove_issue_assignees
GitHub.remove_issue_label
GitHub.remove_pull_request_reviewers
GitHub.remove_reaction_from_issue_comment
GitHub.remove_reaction_from_pr
GitHub.remove_reaction_from_pr_review_comment
GitHub.reply_to_review_comment
GitHub.request_pull_request_reviewers
GitHub.rerun_failed_workflow_run_jobs
GitHub.rerun_workflow_job
GitHub.resolve_review_thread
GitHub.search
GitHub.search_branches

After these actions, stop. Do not continue into the next batch.
```

## Batch 6: projected actions 76-89

```text
Continue the Research 123 discovery-only schema capture in this same GitHub-only conversation.

Do not invoke any GitHub action. Capture the same complete contract fields for:

GitHub.search_commits
GitHub.search_installed_repositories_streaming
GitHub.search_installed_repositories_v2
GitHub.search_issues
GitHub.search_prs
GitHub.search_repositories
GitHub.unlock_issue_conversation
GitHub.unresolve_review_thread
GitHub.update_file
GitHub.update_issue
GitHub.update_issue_comment
GitHub.update_pull_request
GitHub.update_ref
GitHub.update_review_comment

After these actions, stop.
```

## Final reconciliation message

```text
Without invoking any GitHub action, reconcile the six completed schema-capture batches against the exact 89-action projection from the opening inventory.

Report:
1. projected action count;
2. number of exact projected actions whose full host-visible schema was captured;
3. any action whose schema was genericized, truncated or unavailable;
4. any projected action not captured;
5. any schema-level ambiguity that would prevent faithful Runtime Bridge implementation;
6. whether all 89 exact projected contracts are sufficiently captured for implementation mapping.

Finish with exactly one:
GITHUB_89_SCHEMA_CAPTURE=PASS
or
GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE
```

## Preservation rule

The historical two 89-action qualifications in Validation 128 remain valid count/capability evidence. Checkpoint 372 remains historical evidence of the first mapping attempt, but its exact-name reconstruction is superseded by Validation 130 / Checkpoint 373 and the fresh projection preserved in `github_connector_89_action_inventory.json`. Do not rewrite the historical checkpoint as if the error had never occurred.
