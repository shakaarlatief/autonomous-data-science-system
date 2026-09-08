# GitHub App Permission Manifest for 89-Action Parity

**Date:** 2026-09-08
**Status:** REST-DERIVED REGISTRATION MANIFEST FROZEN / GRAPHQL SUFFICIENCY LIVE PROBE REQUIRED
**Research:** Research 123
**Machine authority:** `docs/research/github_app_permission_manifest.json`
**Validator:** `scripts/check_github_app_permission_manifest.py`

## Purpose

Freeze the smallest GitHub App permission superset justified by the observed 89-action native connector parity target before GitHub App registration, client-ID configuration, or user device authorization begins. This artifact maps every exact native action to current official GitHub endpoint permission evidence while refusing to invent permissions for undocumented wrapper behavior.

The selected authorization model remains a GitHub App **user access token** obtained through device flow. Effective authority is the intersection of app permissions, installation repository access, and the authorizing user's own access. No token value belongs in this repository.

## Frozen registration manifest

Repository permissions:

```text
Actions          Read & write   (actions=write)
Contents         Read & write   (contents=write)
Issues           Read & write   (issues=write)
Metadata         Read-only      (metadata=read)
Pull requests    Read & write   (pull_requests=write)
Commit statuses  Read-only      (statuses=read)
Workflows        Read & write   (workflows=write)
```

Other permission families:

```text
Organization permissions   none
Account/user permissions   none
Enterprise permissions     none
Webhooks                    disabled / no subscriptions
Administration              no access
Checks                      no access
Members                     no access
```

This is a seven-permission repository manifest. Write level is selected only where at least one observed parity mutation requires it; that same level subsumes the read operations in that resource family. `Commit statuses` remains read-only because the observed target only reads combined/status checks.

## Why each permission is present

| Permission | Frozen level | Necessity |
| --- | --- | --- |
| Actions | write | The native target includes rerunning failed workflow-run jobs and rerunning one workflow job. Actions write also covers workflow/job/log/artifact reads. |
| Contents | write | Required by raw Git blob/tree/commit/ref creation, file create/update/delete, and pull-request merge; also covers repository contents/commit/branch reads. |
| Issues | write | Required by issue creation/update and issue/issue-comment reaction mutations; also covers issue reads. |
| Metadata | read | Required by repository metadata, collaborator-permission lookup, authenticated-user repository listing, and installation repository enumeration. |
| Pull requests | write | Required by PR create/update, reviews, review comments, reviewer requests/removal and review-comment reactions. It is also the least-privilege candidate for the observed GraphQL PR/review-thread operations. |
| Commit statuses | read | Required by `get_commit_combined_status`; no observed parity action creates commit statuses. |
| Workflows | write | GitHub conditionally requires this in addition to Contents write when file/ref operations affect `.github/workflows`. Native file/ref actions accept arbitrary targets, so practical parity cannot omit it. |

## Explicit non-permissions

`Administration` is intentionally excluded. The captured native `fetch` contract already states that the managed GitHub App does not expose administration-only endpoint families; practical parity must reject those endpoints rather than broaden authority. No observed action needs repository administration, branch-protection administration, runner administration, repository deletion/creation, or similar authority.

`Checks` is intentionally excluded. The target reads commit statuses through the **Commit statuses** permission and GitHub Actions workflow/job data through **Actions**. No observed action creates or updates check runs/suites.

`Members` organization permission is intentionally excluded. The exact native account actions can use user-access-token endpoints that require no App permission for listing the authenticated user's organization memberships, and `list_user_orgs` likewise adds no App permission.

No webhook permission/subscription is needed for the current parity target. Device authorization uses the explicit bounded support tool and polling contract already qualified; parity actions are request-driven.

## GraphQL boundary: official permission table is not exact

GitHub's current official GitHub App guidance gives exact permission requirements for REST endpoints, but for GraphQL it explicitly instructs app developers to **test the app** for the queries/mutations they intend to make; insufficient permission returns HTTP 401. Therefore an honest “exact permission manifest derived entirely from documentation” is impossible for the GraphQL subset.

The observed GraphQL/native operations are all pull-request/review resources:

```text
GitHub.convert_pull_request_to_draft
GitHub.dismiss_pull_request_review
GitHub.enable_auto_merge
GitHub.list_pull_request_review_threads
GitHub.list_pull_request_reviews
GitHub.mark_pull_request_ready_for_review
GitHub.resolve_review_thread
GitHub.unresolve_review_thread
```

The frozen registration manifest uses `pull_requests=write` because that permission is already independently required by ordinary REST parity mutations and is the least-privilege semantic family for all eight GraphQL operations. **No extra permission is added speculatively.** A live GraphQL sufficiency probe is mandatory after App registration and before broad device-flow/parity qualification. If GitHub returns 401 or otherwise demonstrates a missing permission, the project must capture the exact observed requirement before changing the manifest.

## Search and generic fetch do not create new permission families

GitHub App user access tokens can call the GitHub search endpoints, but GitHub exposes no standalone `Search` App permission. Private result visibility remains bounded by the App/user/repository intersection and the underlying resource families. The parity mapping therefore uses existing Contents, Issues, Pull requests and Metadata permissions rather than inventing a search permission.

The native bounded `fetch` action likewise adds no permission. It is a GET-only facade over approved GitHub repository resource families. Runtime Bridge must keep it inside this fixed manifest and reject unlisted or permission-incompatible endpoint families, including Administration-only resources.

## Permission mapping for all 89 actions

| # | Native action | Mapping | Permission requirement | GraphQL probe |
| ---: | --- | --- | --- | :---: |
| 1 | `GitHub.add_comment_to_issue` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 2 | `GitHub.add_issue_assignees` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 3 | `GitHub.add_issue_labels` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 4 | `GitHub.add_reaction_to_issue_comment` | rest_exact | Issues(write) |  |
| 5 | `GitHub.add_reaction_to_pr` | rest_exact | Issues(write) |  |
| 6 | `GitHub.add_reaction_to_pr_review_comment` | rest_exact | Pull requests(write) |  |
| 7 | `GitHub.add_review_to_pr` | rest_exact | Pull requests(write) |  |
| 8 | `GitHub.compare_commits` | rest_exact | Contents(read) |  |
| 9 | `GitHub.convert_pull_request_to_draft` | graphql_empirical | Pull requests(write) | YES |
| 10 | `GitHub.create_blob` | rest_exact | Contents(write) |  |
| 11 | `GitHub.create_branch` | rest_conditional_workflows | Contents(write) OR Contents(write) + Workflows(write) |  |
| 12 | `GitHub.create_commit` | rest_exact | Contents(write) |  |
| 13 | `GitHub.create_file` | rest_conditional_workflows | Contents(write) OR Contents(write) + Workflows(write) |  |
| 14 | `GitHub.create_issue` | rest_exact | Issues(write) |  |
| 15 | `GitHub.create_pull_request` | rest_exact | Pull requests(write) |  |
| 16 | `GitHub.create_tree` | rest_exact | Contents(write) |  |
| 17 | `GitHub.delete_file` | rest_conditional_workflows | Contents(write) OR Contents(write) + Workflows(write) |  |
| 18 | `GitHub.dismiss_pull_request_review` | graphql_empirical | Pull requests(write) | YES |
| 19 | `GitHub.download_user_content` | no_independent_permission | No independent permission |  |
| 20 | `GitHub.download_workflow_artifact` | rest_exact | Actions(read) |  |
| 21 | `GitHub.enable_auto_merge` | graphql_empirical | Pull requests(write) | YES |
| 22 | `GitHub.fetch` | resource_dependent_allowlist | Resource-dependent; fixed manifest only |  |
| 23 | `GitHub.fetch_blob` | rest_exact | Contents(read) |  |
| 24 | `GitHub.fetch_commit` | rest_exact | Contents(read) |  |
| 25 | `GitHub.fetch_commit_workflow_runs` | rest_exact | Actions(read) |  |
| 26 | `GitHub.fetch_file` | rest_exact | Contents(read) |  |
| 27 | `GitHub.fetch_issue` | rest_alternative_permissions | Issues(read) OR Pull requests(read) |  |
| 28 | `GitHub.fetch_issue_comments` | rest_alternative_permissions | Issues(read) OR Pull requests(read) |  |
| 29 | `GitHub.fetch_pr` | rest_exact | Pull requests(read) |  |
| 30 | `GitHub.fetch_pr_comments` | composite_rest | Pull requests(read) + Issues(read) |  |
| 31 | `GitHub.fetch_pr_file_patch` | rest_exact | Pull requests(read) |  |
| 32 | `GitHub.fetch_pr_patch` | rest_exact | Pull requests(read) |  |
| 33 | `GitHub.fetch_workflow_job_logs` | rest_exact | Actions(read) |  |
| 34 | `GitHub.fetch_workflow_job_steps` | rest_exact | Actions(read) |  |
| 35 | `GitHub.fetch_workflow_run_artifacts` | rest_exact | Actions(read) |  |
| 36 | `GitHub.fetch_workflow_run_jobs` | rest_exact | Actions(read) |  |
| 37 | `GitHub.get_commit_combined_status` | rest_exact | Commit statuses(read) |  |
| 38 | `GitHub.get_issue_comment_reactions` | rest_exact | Issues(read) |  |
| 39 | `GitHub.get_pr_diff` | rest_exact | Pull requests(read) |  |
| 40 | `GitHub.get_pr_info` | rest_exact | Pull requests(read) |  |
| 41 | `GitHub.get_pr_reactions` | rest_exact | Issues(read) |  |
| 42 | `GitHub.get_pr_review_comment_reactions` | rest_exact | Pull requests(read) |  |
| 43 | `GitHub.get_profile` | rest_no_permission | No App permission |  |
| 44 | `GitHub.get_repo` | rest_exact | Metadata(read) |  |
| 45 | `GitHub.get_repo_collaborator_permission` | rest_exact | Metadata(read) |  |
| 46 | `GitHub.get_user_login` | rest_no_permission | No App permission |  |
| 47 | `GitHub.get_users_recent_prs_in_repo` | composite_search | Pull requests(read) + Issues(read) |  |
| 48 | `GitHub.label_pr` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 49 | `GitHub.list_installations` | rest_no_permission | No App permission |  |
| 50 | `GitHub.list_installed_accounts` | rest_no_permission | No App permission |  |
| 51 | `GitHub.list_pr_changed_filenames` | rest_exact | Pull requests(read) |  |
| 52 | `GitHub.list_pull_request_review_threads` | graphql_empirical | Pull requests(read) | YES |
| 53 | `GitHub.list_pull_request_reviews` | graphql_empirical | Pull requests(read) | YES |
| 54 | `GitHub.list_recent_issues` | rest_no_permission | No App permission |  |
| 55 | `GitHub.list_repositories` | rest_exact | Metadata(read) |  |
| 56 | `GitHub.list_repositories_by_affiliation` | rest_exact | Metadata(read) |  |
| 57 | `GitHub.list_repositories_by_installation` | rest_exact | Metadata(read) |  |
| 58 | `GitHub.list_user_org_memberships` | rest_no_permission | No App permission |  |
| 59 | `GitHub.list_user_orgs` | rest_no_permission | No App permission |  |
| 60 | `GitHub.lock_issue_conversation` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 61 | `GitHub.mark_pull_request_ready_for_review` | graphql_empirical | Pull requests(write) | YES |
| 62 | `GitHub.merge_pull_request` | rest_exact | Contents(write) |  |
| 63 | `GitHub.remove_issue_assignees` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 64 | `GitHub.remove_issue_label` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 65 | `GitHub.remove_pull_request_reviewers` | rest_exact | Pull requests(write) |  |
| 66 | `GitHub.remove_reaction_from_issue_comment` | rest_exact | Issues(write) |  |
| 67 | `GitHub.remove_reaction_from_pr` | rest_exact | Issues(write) |  |
| 68 | `GitHub.remove_reaction_from_pr_review_comment` | rest_exact | Pull requests(write) |  |
| 69 | `GitHub.reply_to_review_comment` | rest_exact | Pull requests(write) |  |
| 70 | `GitHub.request_pull_request_reviewers` | rest_exact | Pull requests(write) |  |
| 71 | `GitHub.rerun_failed_workflow_run_jobs` | rest_exact | Actions(write) |  |
| 72 | `GitHub.rerun_workflow_job` | rest_exact | Actions(write) |  |
| 73 | `GitHub.resolve_review_thread` | graphql_empirical | Pull requests(write) | YES |
| 74 | `GitHub.search` | search_visibility | Contents(read) |  |
| 75 | `GitHub.search_branches` | rest_exact | Contents(read) |  |
| 76 | `GitHub.search_commits` | search_visibility | Contents(read) |  |
| 77 | `GitHub.search_installed_repositories_streaming` | rest_exact | Metadata(read) |  |
| 78 | `GitHub.search_installed_repositories_v2` | rest_exact | Metadata(read) |  |
| 79 | `GitHub.search_issues` | search_visibility | Issues(read) |  |
| 80 | `GitHub.search_prs` | search_visibility | Pull requests(read) |  |
| 81 | `GitHub.search_repositories` | search_visibility | Metadata(read) |  |
| 82 | `GitHub.unlock_issue_conversation` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 83 | `GitHub.unresolve_review_thread` | graphql_empirical | Pull requests(write) | YES |
| 84 | `GitHub.update_file` | rest_conditional_workflows | Contents(write) OR Contents(write) + Workflows(write) |  |
| 85 | `GitHub.update_issue` | rest_exact | Issues(write) |  |
| 86 | `GitHub.update_issue_comment` | rest_alternative_permissions | Issues(write) OR Pull requests(write) |  |
| 87 | `GitHub.update_pull_request` | rest_exact | Pull requests(write) |  |
| 88 | `GitHub.update_ref` | rest_conditional_workflows | Contents(write) OR Contents(write) + Workflows(write) |  |
| 89 | `GitHub.update_review_comment` | rest_exact | Pull requests(write) |  |

## Registration disposition

This manifest is **registration-ready for the REST-derived permission set**, with one explicit unresolved evidence item: GraphQL sufficiency. It is not truthful to label that item documentation-complete because GitHub does not publish an exact GraphQL permission matrix.

The registration configuration should therefore begin with exactly:

```text
actions=write
contents=write
issues=write
metadata=read
pull_requests=write
statuses=read
workflows=write
webhook_active=false
```

Do not add Administration, Checks, Members, Secrets, Environments, Deployments, Pages, Variables, Webhooks, account permissions, organization permissions, enterprise permissions, OAuth scopes, or arbitrary caller-selected permissions “just in case.”

## Next qualification

After the dedicated GitHub App is registered with this manifest and **device flow is enabled**, configure only its non-secret client ID in the fixed server-owned Runtime Bridge configuration path. Before broad user authorization/parity work, run a bounded qualification that:

1. confirms metadata now reports `configured=true` while `storedAuthorization=false`;
2. begins one explicit device authorization only with user intent;
3. completes authorization without exposing `device_code` or tokens;
4. derives the accessible installation/repository intersection;
5. runs a minimal read-only GraphQL permission probe for the required PR/review-thread operations;
6. records any 401/permission failure without widening the App automatically;
7. only after GraphQL sufficiency passes, opens the first read-only `github.*` parity-action bundle.

```text
GITHUB_APP_PERMISSION_MANIFEST=REST_DERIVED_FROZEN
REPOSITORY_PERMISSION_COUNT=7
ORGANIZATION_PERMISSIONS=NONE
ACCOUNT_PERMISSIONS=NONE
ENTERPRISE_PERMISSIONS=NONE
WEBHOOKS=DISABLED
ADMINISTRATION=NO_ACCESS
CHECKS=NO_ACCESS
MEMBERS=NO_ACCESS
GRAPHQL_EXACT_PERMISSION_DOCS=NOT_AVAILABLE
GRAPHQL_CANDIDATE_PERMISSION=pull_requests:write
GRAPHQL_LIVE_SUFFICIENCY_PROBE=REQUIRED
GITHUB_APP_CLIENT_ID_CONFIGURED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=REGISTER_GITHUB_APP_AND_QUALIFY_GRAPHQL_PERMISSION_SUFFICIENCY
```

## Official sources

- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/rest/using-the-rest-api/troubleshooting-the-rest-api
- https://docs.github.com/en/rest/repos/contents
- https://docs.github.com/en/rest/git/refs
- https://docs.github.com/en/rest/git/commits
- https://docs.github.com/en/rest/branches/branches
- https://docs.github.com/en/rest/pulls/pulls
- https://docs.github.com/en/rest/pulls/reviews
- https://docs.github.com/en/rest/pulls/comments
- https://docs.github.com/en/rest/pulls/review-requests
- https://docs.github.com/en/rest/issues/issues
- https://docs.github.com/en/rest/issues/comments
- https://docs.github.com/en/rest/issues/labels
- https://docs.github.com/en/rest/issues/assignees
- https://docs.github.com/en/rest/reactions/reactions
- https://docs.github.com/en/rest/actions/artifacts
- https://docs.github.com/en/rest/actions/workflow-runs
- https://docs.github.com/en/rest/commits/statuses
- https://docs.github.com/en/rest/apps/installations
- https://docs.github.com/en/rest/repos/repos
- https://docs.github.com/en/rest/users/users
- https://docs.github.com/en/rest/orgs/members
- https://docs.github.com/en/rest/orgs/orgs
- https://docs.github.com/en/rest/authentication/endpoints-available-for-github-app-user-access-tokens
