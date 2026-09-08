# GitHub Connector 89-Action Native Schema Capture

**Date:** 2026-09-08
**Status:** READY / DISCOVERY-ONLY PREIMPLEMENTATION QUALIFICATION
**Research:** Research 123
**Purpose:** Recover the exact native GitHub connector action contracts that Validation 128 did not reproduce in full, without performing any GitHub mutation.

## Why this capture is required

The public repository now durably owns the exact 89 action names through `github_connector_89_action_inventory.json`, but the complete native schemas remain missing from durable evidence. Practical parity requires exact fields, enums, limits and pagination semantics rather than plausible approximations.

The capture must use a fresh GitHub-only ChatGPT conversation because the current persistent Runtime Bridge conversation does not reliably co-project the native GitHub connector.

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

At the start, report the complete projected GitHub action count. If it is not exactly 89, preserve the observed count and differences instead of forcing the old conclusion.

For every requested action report:

```text
exact action name
title
full description
complete input schema
required fields
optional fields
enum values
validation constraints / limits
pagination / cursor / limit semantics visible in the contract
whether read-only or mutating
resource/object operated on
result-shape notes visible from the action contract
```

Do not infer undocumented fields. If a property is genericized or omitted by the host projection, report that exact limitation.

## Initial message for the fresh GitHub-only conversation

Copy this first:

```text
@GitHub

This is the Research 123 read-only native GitHub schema-capture qualification.

Do not invoke any GitHub action. Discovery/schema inspection only.
Do not use Browser, web search, shell, Codex Agent, ADS/Runtime Bridge, or any other connector.

First inspect the GitHub actions actually projected in this fresh conversation.
Report the exact projected action count and the exact ordered action names.

The preserved 2026-09-08 baseline expected 89 actions. Do not force that result: if this fresh projection differs, report the new count and exact added/missing names.

After reporting the inventory, stop. I will send schema-capture batches in follow-up messages in this same conversation.
```

## Batch 1: repository / installation / Git, actions 1-15

```text
Continue discovery only. Do not invoke any action.

For each action below, report its exact title, description, complete input schema, required/optional fields, enums, validation constraints, pagination/cursor/limit behavior visible in the schema, read/mutation classification, and resource scope.

GitHub.get_user_login
GitHub.get_profile
GitHub.list_installations
GitHub.list_installed_accounts
GitHub.list_user_orgs
GitHub.list_user_org_memberships
GitHub.list_repositories
GitHub.list_repositories_by_affiliation
GitHub.list_repositories_by_installation
GitHub.search_installed_repositories_streaming
GitHub.search_installed_repositories_v2
GitHub.search_repositories
GitHub.get_repo
GitHub.fetch
GitHub.search
```

## Batch 2: repository / Git, actions 16-29

```text
Continue discovery only. Do not invoke any action.

Capture the same complete contract fields for:

GitHub.search_branches
GitHub.search_commits
GitHub.fetch_file
GitHub.fetch_blob
GitHub.fetch_commit
GitHub.compare_commits
GitHub.create_blob
GitHub.create_tree
GitHub.create_commit
GitHub.create_branch
GitHub.create_file
GitHub.update_file
GitHub.delete_file
GitHub.update_ref
```

## Batch 3: issues, actions 30-46

```text
Continue discovery only. Do not invoke any action.

Capture the same complete contract fields for:

GitHub.create_issue
GitHub.fetch_issue
GitHub.search_issues
GitHub.list_recent_issues
GitHub.fetch_issue_comments
GitHub.update_issue
GitHub.add_issue_assignees
GitHub.remove_issue_assignees
GitHub.add_issue_labels
GitHub.remove_issue_label
GitHub.add_issue_comment
GitHub.update_issue_comment
GitHub.add_reaction_to_issue_comment
GitHub.get_issue_comment_reactions
GitHub.remove_reaction_from_issue_comment
GitHub.lock_issue_conversation
GitHub.unlock_issue_conversation
```

## Batch 4: Actions / CI, actions 47-55

```text
Continue discovery only. Do not invoke any action.

Capture the same complete contract fields for:

GitHub.fetch_commit_workflow_runs
GitHub.fetch_workflow_run_jobs
GitHub.fetch_workflow_job_steps
GitHub.fetch_workflow_job_logs
GitHub.fetch_workflow_run_artifacts
GitHub.download_workflow_artifact
GitHub.get_commit_combined_status
GitHub.rerun_failed_workflow_run_jobs
GitHub.rerun_workflow_job
```

## Batch 5: pull requests / reviews, actions 56-72

```text
Continue discovery only. Do not invoke any action.

Capture the same complete contract fields for:

GitHub.add_comment_to_issue
GitHub.add_reaction_to_pr
GitHub.add_reaction_to_pr_review_comment
GitHub.add_review_to_pr
GitHub.convert_pull_request_to_draft
GitHub.create_pull_request
GitHub.dismiss_pull_request_review
GitHub.enable_auto_merge
GitHub.fetch_pr
GitHub.fetch_pr_comments
GitHub.fetch_pr_file_patch
GitHub.fetch_pr_patch
GitHub.get_pr_diff
GitHub.get_pr_info
GitHub.get_pr_reactions
GitHub.get_pr_review_comment_reactions
GitHub.get_users_recent_prs_in_repo
```

## Batch 6: pull requests / reviews + permission, actions 73-89

```text
Continue discovery only. Do not invoke any action.

Capture the same complete contract fields for:

GitHub.label_pr
GitHub.list_pr_changed_filenames
GitHub.list_pull_request_review_threads
GitHub.list_pull_request_reviews
GitHub.mark_pull_request_ready_for_review
GitHub.merge_pull_request
GitHub.remove_reaction_from_pr
GitHub.remove_reaction_from_pr_review_comment
GitHub.reply_to_review_comment
GitHub.request_pull_request_reviewers
GitHub.resolve_review_thread
GitHub.search_prs
GitHub.unresolve_review_thread
GitHub.update_pull_request
GitHub.update_review_comment
GitHub.remove_pull_request_reviewers
GitHub.get_repo_collaborator_permission
```

## Final reconciliation message

```text
Without invoking any GitHub action, reconcile the six schema-capture batches.

Report:
1. projected action count;
2. number of exact baseline actions whose full schema was captured;
3. any action whose host schema was genericized, truncated or unavailable;
4. any baseline action missing from this projection;
5. any new projected action not in the 89-action baseline;
6. whether all 89 exact baseline contracts are now sufficiently captured for implementation mapping.

Finish with exactly one:
GITHUB_89_SCHEMA_CAPTURE=PASS
or
GITHUB_89_SCHEMA_CAPTURE=INCOMPLETE
```

## Preservation rule

Do not treat a changed future projection as corruption of the 2026-09-08 baseline. The baseline remains historical evidence. If the fresh projection changes, preserve both the historical 89-action parity target and the newly observed surface, then decide explicitly whether Research 123 parity should target the historical baseline, the new superset, or both.
