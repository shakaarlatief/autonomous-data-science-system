# GitHub App Live Permission Reconciliation and Broad Superset Candidate

**Date:** 2026-09-09
**Status:** LIVE UI CAPTURE COMPLETE / 118 OPTIONS RECONCILED / BROAD DEVELOPER-SUPERSET CANDIDATE
**Research:** Research 123
**Machine artifact:** `docs/research/github_app_live_permission_inventory_20260909.json`

## 1. Live UI authority

The project owner supplied a complete scrolling capture of the current personal-account GitHub App registration page. The live UI exposes:

```text
Repository permissions   40
Organization permissions 42
Account permissions      19
Enterprise permissions   17
Total visible options    118
```

This live surface is materially broader than the consolidated public permission index alone. It includes newer/preview or differently surfaced capabilities such as Agent tasks, Discussions, License compliance alerts, Merge queues, Packages, Projects, secret-scanning request families, Single file, Copilot Chat/Editor Context, Models, multiple organization security/Copilot/credentials families, and a much broader enterprise-preview list. The live GitHub UI is therefore the authority for what can actually be selected on this account today, while official API documentation remains authority for endpoint semantics and token support.

## 2. Selection policy

The product goal is **maximum useful professional developer capability**, not maximum unchecked permission count. The initial App should therefore request broad repository development/admin/security capability, useful organization-level developer administration, selected user-level developer conveniences, and no enterprise authority until a real enterprise target exists.

Secret-value families and arbitrary webhook-management authority remain deferred because they need dedicated secure-value/external-destination contracts. `Single file` is not useful when broader `Contents` authority is already present.

## 3. Repository permissions

| Permission | Recommendation |
| --- | --- |
| Actions | Highest available (normally Read & write) |
| Administration | Highest available (normally Read & write) |
| Agent secrets | No access |
| Agent tasks | Highest available (normally Read & write) |
| Agent variables | Highest available (normally Read & write) |
| Artifact metadata | Highest available (normally Read & write) |
| Attestations | Highest available (normally Read & write) |
| Checks | Highest available (normally Read & write) |
| Code quality | Read-only |
| Code scanning alerts | Highest available (normally Read & write) |
| Codespaces | Highest available (normally Read & write) |
| Codespaces lifecycle admin | Highest available (normally Read & write) |
| Codespaces metadata | Read-only |
| Codespaces secrets | No access |
| Commit statuses | Highest available (normally Read & write) |
| Contents | Highest available (normally Read & write) |
| Copilot agent settings | Highest available (normally Read & write) |
| Custom properties | Highest available (normally Read & write) |
| Dependabot alerts | Highest available (normally Read & write) |
| Dependabot secrets | No access |
| Deployments | Highest available (normally Read & write) |
| Discussions | Highest available (normally Read & write) |
| Environments | Highest available (normally Read & write) |
| Issues | Highest available (normally Read & write) |
| License compliance alerts | Read-only |
| Merge queues | Highest available (normally Read & write) |
| Metadata | Read-only |
| Packages | Highest available (normally Read & write) |
| Pages | Highest available (normally Read & write) |
| Projects | Highest available (normally Read & write) |
| Pull requests | Highest available (normally Read & write) |
| Repository security advisories | Highest available (normally Read & write) |
| Secret scanning alert dismissal requests | Highest available (normally Read & write) |
| Secret scanning alerts | Highest available (normally Read & write) |
| Secret scanning push protection bypass requests | Highest available (normally Read & write) |
| Secrets | No access |
| Single file | No access |
| Variables | Highest available (normally Read & write) |
| Webhooks | No access |
| Workflows | Highest available (normally Read & write) |

Repository result:

```text
Enable now / highest available    30
Enable now / read-only             4
Defer or exclude                    6
Total                              40
```

The six repository exclusions are intentionally narrow: Agent secrets, Codespaces secrets, Dependabot secrets, Actions Secrets, Single file, and Webhooks. The first four are secret-value management surfaces; Single file is redundant with Contents; Webhooks can create arbitrary external destinations.

High-consequence repository capabilities such as Administration, security-advisory mutation, and secret-scanning bypass review may be selected at the App layer but must later be exposed only through bounded semantic Runtime Bridge actions with explicit confirmation where appropriate.

## 4. Organization permissions

| Permission | Recommendation |
| --- | --- |
| API Insights | Read-only |
| Administration | Highest available (normally Read & write) |
| Agent secrets | No access |
| Agent variables | Highest available (normally Read & write) |
| Blocking users | No access |
| Campaigns | Highest available (normally Read & write) |
| Copilot Spaces | Highest available (normally Read & write) |
| Copilot agent settings | Highest available (normally Read & write) |
| Copilot content exclusion | Highest available (normally Read & write) |
| Custom organization roles | Highest available (normally Read & write) |
| Custom properties | Highest available (normally Read & write) |
| Custom properties for organizations | Highest available (normally Read & write) |
| Custom repository roles | Highest available (normally Read & write) |
| Events | Read-only |
| GitHub Copilot Business | No access |
| Hosted runner custom images | Highest available (normally Read & write) |
| Issue Fields | Highest available (normally Read & write) |
| Issue Types | Highest available (normally Read & write) |
| Members | Highest available (normally Read & write) |
| Models | Highest available (normally Read & write) |
| Network configurations | Highest available (normally Read & write) |
| Organization Copilot metrics | Read-only |
| Organization announcement banners | No access |
| Organization bypass requests for secret scanning | Highest available (normally Read & write) |
| Organization codespaces | Highest available (normally Read & write) |
| Organization codespaces secrets | No access |
| Organization codespaces settings | Highest available (normally Read & write) |
| Organization credentials | No access |
| Organization dependabot secrets | No access |
| Organization dismissal requests for Dependabot | Highest available (normally Read & write) |
| Organization dismissal requests for code scanning | Highest available (normally Read & write) |
| Organization innersource vulnerabilities | Highest available (normally Read & write) |
| Organization private registries | No access |
| Personal access token requests | No access |
| Personal access tokens | No access |
| Plan | Read-only |
| Projects | Highest available (normally Read & write) |
| Secret scanning alert dismissal requests | Highest available (normally Read & write) |
| Secrets | No access |
| Self-hosted runners | Highest available (normally Read & write) |
| Variables | Highest available (normally Read & write) |
| Webhooks | No access |

Organization result:

```text
Enable now / highest available    26
Enable now / read-only             4
Defer or exclude                   12
Total                              42
```

The broad organization selection is justified only because the owner wants Codexless to become a GitHub capability superset and repository Administration already means organization-owner approval will generally be required for organization installations. Nevertheless, credential/secret families, PAT governance, billing/seat-management, blocking users, announcement banners, private registries and webhooks remain excluded until concrete workflows justify them.

## 5. Account permissions

| Permission | Recommendation |
| --- | --- |
| Block another user | No access |
| Codespaces user secrets | No access |
| Copilot Chat | No access |
| Copilot Editor Context | No access |
| Email addresses | No access |
| Events | Read-only |
| Followers | No access |
| GPG keys | Read-only |
| Gists | Highest available |
| Git SSH keys | Read-only |
| Interaction limits | No access |
| Issue Fields | Highest available |
| Issue Types | Highest available |
| Models | Highest available |
| Plan | No access |
| Profile | No access |
| SSH signing keys | Read-only |
| Starring | Highest available |
| Watching | Highest available |

Account result:

```text
Enable now / highest available     6
Enable now / read-only             4
Defer or exclude                    9
Total                              19
```

The selected account capabilities are limited to developer-oriented features such as Gists, issue-field/type/model access and repository starring/watching, plus read-only event/key visibility. Copilot Chat and Copilot Editor Context are Copilot Extension context permissions rather than prerequisites for Codexless GitHub API access and remain off. Personal profile/email/follower/blocking/interaction mutation and Codespaces user secrets remain off.

## 6. Enterprise permissions

All 17 live enterprise permissions remain **No access** for the initial App. No concrete enterprise owner/tenant target is established, and GitHub explicitly documents that requesting `Enterprise organization installations` or `Enterprise organization installation repositories` restricts cross-enterprise installability. Enterprise authority can be added later if a real enterprise deployment is in scope.

## 7. Important current GitHub evidence

GitHub confirms that App permissions determine API authority and that user-access-token requests are further limited by the authorizing user's own permissions. REST endpoints document exact permission requirements and return `X-Accepted-GitHub-Permissions` on insufficient permission; GraphQL still requires empirical permission testing.

Repository `Administration(write)` is confirmed to support creating repositories for the authenticated user and creating organization repositories, subject to the user/org policy boundary. It also unlocks broad repository administration.

GitHub's current App-token permission schema explicitly includes live families such as Discussions, Merge queues, Packages and many newer organization/user/enterprise permission identifiers even when the consolidated human-readable permission index lags the registration UI.

Agent tasks are in public preview and support GitHub App **user access tokens** for listing/starting/managing Copilot cloud-agent tasks, matching the selected user-token authorization architecture.

## 8. Installation scope

The intended personal installation is now:

```text
owner: shakaarlatief
repository access: All repositories
```

This is independent of permission breadth. Organization repositories remain available only after the same public App is explicitly installed/approved on the relevant organization, and effective user-token authority remains the intersection of user access, installation scope, and App permissions.

## 9. Registration disposition

The old seven-permission Checkpoint 392 prefill must not be used unchanged. A new extended registration prefill/checklist should be generated only after this broad candidate is frozen.

The recommended immediate profile is intentionally very broad at repository scope, broad at organization scope, selective at account scope, and empty at enterprise scope. It keeps only six repository permissions off. This is a substantial expansion beyond native ChatGPT GitHub connector parity while preserving explicit boundaries around secret values, arbitrary webhooks, personal account control, and enterprise administration.

## 10. Official sources

- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/enterprise-cloud@latest/rest/authentication/permissions-required-for-github-apps?apiVersion=2026-03-10
- https://docs.github.com/en/rest/apps/apps
- https://docs.github.com/en/rest/agent-tasks/agent-tasks
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app

```text
LIVE_PERMISSION_UI_CAPTURE=COMPLETE
LIVE_PERMISSION_OPTION_COUNT=118
REPOSITORY_OPTIONS=40
ORGANIZATION_OPTIONS=42
ACCOUNT_OPTIONS=19
ENTERPRISE_OPTIONS=17
BROAD_SUPERSET_CANDIDATE=READY
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
SECRET_VALUE_PERMISSIONS=DEFER
WEBHOOK_MANAGEMENT=DEFER
ENTERPRISE_PERMISSIONS=NONE
NEXT=FREEZE_EXTENDED_PERMISSION_MANIFEST_AND_REBUILD_REGISTRATION_PREFILL
```
