# Validation 148: GitHub App REST Permission Manifest Frozen, GraphQL Probe Required

**Date:** 2026-09-08
**Status:** PASS / 89-ACTION PERMISSION MAPPING COMPLETE / REST-DERIVED REGISTRATION MANIFEST FROZEN / GRAPHQL SUFFICIENCY EMPIRICAL
**Research:** Research 123
**Scope:** Derive the smallest GitHub App permission superset justified by the exact 89-action parity target from current official GitHub endpoint documentation, preserve an action-by-action machine mapping, and isolate the one permission-evidence class that GitHub explicitly requires developers to test rather than documenting exactly: GraphQL.

## 1. Inputs

Canonical project inputs:

```text
docs/research/github_connector_89_action_inventory.json
docs/research/github_connector_native_schema_capture.json
docs/research/GITHUB_CONNECTOR_PARITY_MATRIX.md
docs/research/GITHUB_API_AUTH_AND_CONTRACT_BASELINE.md
```

New permission artifacts:

```text
docs/research/GITHUB_APP_PERMISSION_MANIFEST.md
docs/research/github_app_permission_manifest.json
scripts/check_github_app_permission_manifest.py
```

Current GitHub documentation was rechecked on 2026-09-08, including:

```text
GitHub App permission selection guidance
permissions required for GitHub Apps
REST troubleshooting / X-Accepted-GitHub-Permissions
repository contents
Git refs and Git commits
branches
pull requests, reviews, review comments and review requests
issues, comments, labels and assignees
reactions
Actions artifacts and workflow runs
commit statuses
GitHub App user-token installations/repositories
repositories
users
organization memberships / organizations
endpoints available to GitHub App user access tokens
```

Exact source URLs are preserved in `github_app_permission_manifest.json` and `GITHUB_APP_PERMISSION_MANIFEST.md`.

## 2. Frozen repository permission set

The minimal REST-derived registration manifest is:

```text
Actions          write   actions=write
Contents         write   contents=write
Issues           write   issues=write
Metadata         read    metadata=read
Pull requests    write   pull_requests=write
Commit statuses  read    statuses=read
Workflows        write   workflows=write
```

Count:

```text
repository permission families = 7
organization permissions        = 0
account/user permissions        = 0
enterprise permissions          = 0
webhook subscriptions           = 0
```

The selected write levels are forced by observed parity mutations and then cover the corresponding reads. `Commit statuses` remains read-only because the 89-action target contains status reads but no status mutation.

## 3. Why Workflows write is not optional for practical parity

Official GitHub content and Git-reference documentation defines conditional permission sets:

```text
Contents(write)
OR
Contents(write) + Workflows(write)
```

when content/ref operations affect Actions workflow files. The native connector actions:

```text
GitHub.create_branch
GitHub.create_file
GitHub.delete_file
GitHub.update_file
GitHub.update_ref
```

accept arbitrary repository paths/refs rather than excluding `.github/workflows` changes. Therefore a parity App that omits Workflows(write) would intentionally lose observed mutation capability. The permission is retained for capability parity, not general Actions administration.

## 4. Explicitly excluded authority

The frozen manifest gives **no access** to:

```text
Administration
Checks
Members (organization)
Repository webhooks
Deployments
Environments
Secrets
Variables
Pages
security-advisory families
all account permission families
all organization permission families
all enterprise permission families
```

`Administration` is especially important. The captured native `GitHub.fetch` contract already says the managed GitHub App does not have Administration access for endpoints that require it. Runtime Bridge must preserve that limitation by rejecting permission-incompatible endpoints, not by broadening the App.

`Checks` is not needed because the target uses `Commit statuses(read)` for combined statuses and `Actions` for workflow/job/run evidence. No native parity action creates or updates a check run/suite.

`Members` is not needed because the exact authenticated-user organization membership listing used by the target requires no GitHub App permission.

## 5. Exact 89-action mapping is machine preserved

`github_app_permission_manifest.json` contains one row for every exact native action in exact inventory order. Mapping classes include:

```text
49  rest_exact
11  rest_alternative_permissions
 8  graphql_empirical
 7  rest_no_permission
 5  rest_conditional_workflows
 5  search_visibility
 1  no_independent_permission
 1  resource_dependent_allowlist
 1  composite_rest
 1  composite_search
--
89
```

The validator verifies:

```text
exact inventory order and names           89 / 89
repository permission families            exactly 7
all declared action requirements          covered by frozen manifest
conditional Workflows actions             exact expected five
graphQL empirical actions                 exact expected eight
no-permission action set                   exact expected seven
Administration / Checks / Members         absent
organization/account/enterprise perms     absent
webhooks                                  disabled
```

Validator result:

```text
GITHUB_APP_PERMISSION_MANIFEST=PASS
GITHUB_APP_PERMISSION_MANIFEST_ACTION_COUNT=89
GITHUB_APP_PERMISSION_MANIFEST_REPOSITORY_PERMISSION_COUNT=7
GITHUB_APP_GRAPHQL_PERMISSION_SUFFICIENCY=LIVE_PROBE_REQUIRED
```

## 6. Search adds no invented permission

GitHub documents GitHub App user access token availability for the search endpoints but exposes no standalone GitHub App `Search` permission. The action mapping therefore does not invent one.

Private search result authority remains constrained by the App/user/repository intersection and the relevant resource permissions already in the manifest:

```text
code / commit       Contents
issues              Issues
pull requests       Pull requests
repositories        Metadata
```

## 7. GraphQL is the deliberate evidence exception

GitHub's current App guidance is asymmetric:

```text
REST
    endpoint reference documents permission requirements
    insufficient permission -> 403
    X-Accepted-GitHub-Permissions can identify accepted sets

GraphQL
    GitHub tells developers to test their app for required permissions
    insufficient permission -> 401
    exact query/mutation permission table is not published
```

Eight observed native actions are GraphQL-dependent or GraphQL-node-dependent:

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

All eight operate on pull-request/review resources. `pull_requests=write` is therefore the minimal semantic candidate, and it is already independently required by ordinary REST parity mutations. **No new permission is added speculatively.**

However, Research 123 must not claim exact GraphQL permission sufficiency before live testing. A bounded live GraphQL probe after App registration is mandatory. If a probe returns 401 or an explicit permission failure, preserve that evidence and revise the manifest only to the demonstrated minimum.

## 8. Registration disposition

The REST-derived registration permission set is now frozen and ready to use as the initial dedicated GitHub App configuration:

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

No GitHub App has been registered/configured by this validation. No client ID, client secret, access token, refresh token or device code was created or stored.

## 9. Next boundary

The next step is to freeze the non-secret GitHub App **registration configuration** around this permission manifest and then have the project owner create/install the dedicated App through GitHub's UI because that account-bound operation is not available through the current Runtime Bridge tool surface.

That configuration must determine, without widening authority:

```text
canonical App name / description / homepage
owner account for registration
private-vs-public installability
webhook disabled
no callback URL unless GitHub requires one for the chosen device-flow setting
device flow enabled
exact seven repository permissions
no organization/account/enterprise permissions
repository installation selection policy
```

After the App exists, configure only the **non-secret client ID** in the fixed server-owned Runtime Bridge configuration. Then qualify metadata -> device begin -> user completion -> protected token storage -> installation/repository derivation -> minimal GraphQL permission probes before publishing the first read-only `github.*` bundle.

```text
VALIDATION148=PASS
PERMISSION_ACTION_MAPPING=89_OF_89
REST_DERIVED_PERMISSION_MANIFEST=FROZEN
REPOSITORY_PERMISSION_COUNT=7
ORGANIZATION_PERMISSIONS=NONE
ACCOUNT_PERMISSIONS=NONE
ENTERPRISE_PERMISSIONS=NONE
WEBHOOKS=DISABLED
ADMINISTRATION=NO_ACCESS
CHECKS=NO_ACCESS
MEMBERS=NO_ACCESS
GRAPHQL_PERMISSION_SUFFICIENCY=LIVE_PROBE_REQUIRED
GITHUB_APP_REGISTERED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=FREEZE_GITHUB_APP_REGISTRATION_CONFIGURATION
```
