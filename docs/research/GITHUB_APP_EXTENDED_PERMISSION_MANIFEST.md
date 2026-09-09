# Extended GitHub App Permission Manifest

**Date:** 2026-09-09
**Status:** FROZEN / BROAD DEVELOPER-SUPERSET / APP CREATION READY AFTER REGISTRATION CHECKLIST
**Research:** Research 123
**Machine authority:** `docs/research/github_app_extended_permission_manifest.json`
**Live UI authority:** `docs/research/github_app_live_permission_inventory_20260909.json`

## Purpose

Freeze the first intentionally broader-than-native GitHub App permission profile for Codexless Runtime Bridge. The profile keeps 89-action connector parity as a subset, then adds repository administration, checks/status publication, deployments/environments, Codespaces, discussions, packages, projects, security management, agent/Copilot surfaces and selected organization/account capabilities.

The design target is **maximum useful professional development capability with bounded runtime actions**, not maximum checkbox count. The App-level permission can be broad while Runtime Bridge still exposes only semantic, validated operations and requires explicit confirmation for high-consequence mutations.

## Live UI baseline

```text
repository permission options   40
organization permission options 42
account permission options      19
enterprise permission options   17
total live options             118
```

Frozen selected profile:

```text
repository selected/read   34 / 40
organization selected/read 30 / 42
account selected/read      10 / 19
enterprise selected         0 / 17
total selected/read        74 / 118
```

## Repository permissions

| Permission | Access | Prefill |
| --- | --- | --- |
| Actions | write | actions |
| Administration | write | administration |
| Agent tasks | write | manual UI |
| Agent variables | write | manual UI |
| Artifact metadata | write | artifact_metadata |
| Attestations | write | attestations |
| Checks | write | checks |
| Code quality | write | code_quality |
| Code scanning alerts | write | security_events |
| Codespaces | write | codespaces |
| Codespaces lifecycle admin | write | codespaces_lifecycle_admin |
| Codespaces metadata | read | codespaces_metadata |
| Commit statuses | write | statuses |
| Contents | write | contents |
| Copilot agent settings | read | manual UI |
| Custom properties | write | repository_custom_properties |
| Dependabot alerts | write | vulnerability_alerts |
| Deployments | write | deployments |
| Discussions | write | discussions |
| Environments | write | environments |
| Issues | write | issues |
| License compliance alerts | read | manual UI |
| Merge queues | write | merge_queues |
| Metadata | read | metadata |
| Packages | write | packages |
| Pages | write | pages |
| Projects | admin | repository_projects |
| Pull requests | write | pull_requests |
| Repository security advisories | write | repository_advisories |
| Secret scanning alert dismissal requests | write | manual UI |
| Secret scanning alerts | write | secret_scanning_alerts |
| Secret scanning push protection bypass requests | write | manual UI |
| Variables | write | actions_variables |
| Workflows | write | workflows |

Explicit repository No access:

```text
Agent secrets
Codespaces secrets
Dependabot secrets
Secrets
Single file
Webhooks
```

Key changes relative to the old parity-only profile include `Administration=write`, `Checks=write`, `Commit statuses=write`, deployments/environments, Codespaces, discussions, merge queues, packages, Pages/projects, security alert/advisory management, Attestations, Agent tasks/variables, and other development extensions.

`Administration=write` is deliberately selected because the owner explicitly wants Codexless to be able to create/manage repositories. GitHub documents repository Administration as covering repository creation/deletion/settings/teams/collaborators. Destructive repository deletion/transfer/settings actions must still be separately bounded in Runtime Bridge.

## Organization permissions

| Permission | Access | Prefill |
| --- | --- | --- |
| API Insights | read | organization_api_insights |
| Administration | write | organization_administration |
| Agent variables | write | manual UI |
| Campaigns | write | organization_campaigns |
| Copilot Spaces | write | manual UI |
| Copilot agent settings | write | organization_copilot_agent_settings |
| Copilot content exclusion | write | manual UI |
| Custom organization roles | write | organization_custom_org_roles |
| Custom properties | admin | organization_custom_properties |
| Custom properties for organizations | write | custom_properties_for_organizations |
| Custom repository roles | write | organization_custom_roles |
| Events | read | organization_events |
| Hosted runner custom images | read | manual UI |
| Issue Fields | write | manual UI |
| Issue Types | write | issue_types |
| Members | write | members |
| Models | read | organization_models |
| Network configurations | write | organization_network_configurations |
| Organization Copilot metrics | read | manual UI |
| Organization bypass requests for secret scanning | write | manual UI |
| Organization codespaces | write | organization_codespaces |
| Organization codespaces settings | write | organization_codespaces_settings |
| Organization dismissal requests for Dependabot | write | manual UI |
| Organization dismissal requests for code scanning | write | organization_code_scanning_dismissal_requests |
| Organization innersource vulnerabilities | write | manual UI |
| Plan | read | organization_plan |
| Projects | admin | organization_projects |
| Secret scanning alert dismissal requests | write | manual UI |
| Self-hosted runners | write | organization_self_hosted_runners |
| Variables | write | organization_actions_variables |

Explicit organization No access:

```text
Agent secrets
Blocking users
GitHub Copilot Business
Organization announcement banners
Organization codespaces secrets
Organization credentials
Organization dependabot secrets
Organization private registries
Personal access token requests
Personal access tokens
Secrets
Webhooks
```

Organization permissions are broad because repository Administration already places this App in an organization-owner-approval class for many installations. We therefore retain useful organization development/admin surfaces while still excluding secret/credential/PAT/webhook and unrelated user-governance/billing families.

## Account permissions

| Permission | Access | Prefill |
| --- | --- | --- |
| Events | read | user_events |
| GPG keys | read | gpg_keys |
| Gists | write | gists |
| Git SSH keys | read | keys |
| Issue Fields | write | manual UI |
| Issue Types | write | manual UI |
| Models | read | user_models |
| SSH signing keys | read | git_signing_ssh_public_keys |
| Starring | write | starring |
| Watching | write | watching |

Explicit account No access:

```text
Block another user
Codespaces user secrets
Copilot Chat
Copilot Editor Context
Email addresses
Followers
Interaction limits
Plan
Profile
```

Account permissions are intentionally selective. The App can work with Gists, issue metadata, GitHub Models, stars/subscriptions and read key/event metadata, but it does not receive profile/email/follower/blocking/Copilot-context or user-secret authority.

## Enterprise permissions

All 17 live enterprise permission rows remain No access:

```text
Copilot usage records
Custom enterprise roles
Custom properties
Enterprise AI controls
Enterprise Copilot metrics
Enterprise SCIM
Enterprise billing
Enterprise credentials
Enterprise custom organization roles
Enterprise custom properties for organizations
Enterprise innersource vulnerabilities
Enterprise organization installation repositories
Enterprise organization installations
Enterprise organizations
Enterprise people
Enterprise single sign-on
Enterprise teams
```

No enterprise owner/tenant target exists. Enterprise permissions can be designed later without weakening the GitHub.com personal/organization architecture.

## Secret-value and webhook boundary

The first App deliberately does **not** request repository/organization/user secret-value permissions or repository/organization webhook-management permission. These can be added later after Codexless has purpose-built contracts for encrypted secret value input and bounded external destinations. This avoids giving a newly introduced wide GitHub token powers that Runtime Bridge has no safe semantic surface for yet.

## Registration-prefill strategy

GitHub's documented registration URL format can prefill **56 of the 74 selected permission rows** using independently documented parameter names. The remaining **18 live/newer rows** are deliberately manual because no parameter name was independently verified; the project does not guess undocumented URL keys.

Manual rows:

```text
repository: Agent tasks = write
repository: Agent variables = write
repository: Copilot agent settings = read
repository: License compliance alerts = read
repository: Secret scanning alert dismissal requests = write
repository: Secret scanning push protection bypass requests = write
organization: Agent variables = write
organization: Copilot Spaces = write
organization: Copilot content exclusion = write
organization: Hosted runner custom images = read
organization: Issue Fields = write
organization: Organization Copilot metrics = read
organization: Organization bypass requests for secret scanning = write
organization: Organization dismissal requests for Dependabot = write
organization: Organization innersource vulnerabilities = write
organization: Secret scanning alert dismissal requests = write
account: Issue Fields = write
account: Issue Types = write
```

GitHub documents that App registration URLs use the permission name as the query parameter and `read`, `write`, or where supported `admin` as values. The URL also preselects identity, public/Any-account visibility, install-time OAuth off, and webhooks off. Device Flow and expiring user authorization tokens remain manual UI confirmations because GitHub does not expose those switches in its documented registration URL parameter table.

## Installation scope

Personal installation after App creation:

```text
account             shakaarlatief
repository access   All repositories
```

Organization installations use the same public App but require explicit approval/install on each relevant organization. Effective user-token authority remains the intersection of the authorizing user, App installation repository scope, and App permission set.

## GraphQL boundary remains empirical

The original eight PR/review GraphQL operations remain subject to the already-recorded live permission sufficiency probe. The broader App still carries Pull requests(write), so no extra GraphQL permission is invented. GitHub explicitly recommends testing GraphQL queries/mutations because it does not publish a complete exact GraphQL permission matrix.

## Final registration disposition

This 74-row profile supersedes the historical seven-permission Checkpoint 391/392 registration instruction for actual App creation. The old files remain historical evidence of the parity-only baseline.

```text
EXTENDED_GITHUB_APP_PERMISSION_MANIFEST=FROZEN
LIVE_PERMISSION_OPTION_COUNT=118
SELECTED_PERMISSION_COUNT=74
REPOSITORY_SELECTED=34
ORGANIZATION_SELECTED=30
ACCOUNT_SELECTED=10
ENTERPRISE_SELECTED=0
DOCUMENTED_PREFILL_PERMISSION_COUNT=56
MANUAL_LIVE_UI_PERMISSION_COUNT=18
REPOSITORY_ADMINISTRATION=WRITE
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
SECRET_VALUE_PERMISSIONS=NO_ACCESS
WEBHOOK_MANAGEMENT=NO_ACCESS
NEXT=USE_EXTENDED_REGISTRATION_PREFILL_AND_CONFIRM_MANUAL_ROWS
```

## Official sources

- https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/rest/apps/apps
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
- https://docs.github.com/en/rest/agent-tasks/agent-tasks
