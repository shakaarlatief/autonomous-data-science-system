# GitHub App Extended Permission Review

**Date:** 2026-09-08
**Status:** ACTIVE / PARITY-ONLY MANIFEST PAUSED / EXTENDED GITHUB CAPABILITY REVIEW
**Research:** Research 123
**Purpose:** Re-open the Checkpoint 391 seven-permission parity-only GitHub App manifest before App creation because the project owner explicitly wants Codexless Runtime Bridge to exceed the native ChatGPT GitHub connector where useful, including repository creation/administration and other GitHub capabilities that the native connector does not expose.

## 1. Why this review exists

The original seven-permission manifest was intentionally derived only from the observed 89-action native GitHub connector parity target. That was correct for parity, but it is too narrow for the newly clarified product goal:

```text
Codexless Runtime Bridge GitHub layer
= native-connector parity
+ deliberately selected GitHub capabilities beyond the connector
```

The GitHub App has not yet been created, so this is the correct time to expand the authority model once rather than immediately requesting permission changes after installation.

## 2. Important distinction from the native ChatGPT GitHub app

The existing ChatGPT GitHub integration is provider-owned. Its exposed actions and GitHub-side permissions are not under this project's control. Packaging or orchestrating that app together with Codexless would not let Codexless add new GitHub API authority to the provider-owned app.

The dedicated GitHub App behind Codexless is different: this project controls its requested permissions and the bounded Runtime Bridge actions implemented on top of them. That is what makes repository creation, administration, checks, deployments, security automation, Codespaces management, Copilot/agent operations, and other extensions possible.

## 3. Current official permission families

GitHub classifies App permissions into repository, organization, account/user, and enterprise families. The current main permission reference enumerates 31 established repository permission headings, 31 organization headings, 14 user headings, and 2 enterprise headings. The live GitHub registration UI also exposes newer preview permissions such as **Agent tasks**, which GitHub documents separately and currently supports only with user access tokens for its task endpoints.

### 3.1 Established repository permission headings

```text
Actions
Administration
Agent secrets
Agent variables
Artifact metadata
Attestations
Checks
Code quality
Code scanning alerts
Codespaces lifecycle admin
Codespaces metadata
Codespaces secrets
Codespaces
Commit statuses
Contents
Copilot agent settings
Custom properties
Dependabot alerts
Dependabot secrets
Deployments
Environments
Issues
Metadata
Pages
Pull requests
Repository security advisories
Secret scanning alerts
Secrets
Variables
Webhooks
Workflows
```

### 3.2 Live/newer repository permission surface to track

```text
Agent tasks  (public preview; user access token supported; installation token not supported)
```

GitHub's broader token/App permission schema also contains permission identifiers for resource families such as Discussions, Merge queues, Packages, repository projects/hooks, and related compatibility permissions. These must be reconciled against the actual live registration UI before final selection because availability can depend on product surface, account features, and API support.

### 3.3 Organization permission headings

```text
API Insights
Administration
Agent secrets
Agent variables
Blocking users
Campaigns
Copilot Spaces
Copilot agent settings
Copilot content exclusion
Custom organization roles
Custom properties
Events
GitHub Copilot Business
Hosted runner custom images
Issue Fields
Issue Types
Members
Network configurations
Organization Copilot metrics
Organization codespaces secrets
Organization codespaces settings
Organization codespaces
Organization dependabot secrets
Organization private registries
Personal access token requests
Personal access tokens
Projects
Secrets
Self-hosted runners
Variables
Webhooks
```

### 3.4 Account/user permission headings

```text
Block another user
Codespaces user secrets
Email addresses
Followers
GPG keys
Gists
Git SSH keys
Interaction limits
Plan
Private repository invitations
Profile
SSH signing keys
Starring
Watching
```

### 3.5 Enterprise permission headings

```text
Enterprise Copilot metrics
Enterprise teams
```

## 4. High-value extension capabilities beyond the 89-action connector

The following permission families correspond to capabilities that materially improve a professional GitHub development agent and are not merely duplicates of the parity target.

### 4.1 Repository Administration: strongest immediate extension

**Recommended candidate: `Administration = Read & write`.**

GitHub documents this permission as covering repository creation/deletion/settings/teams/collaborators and many administration endpoints. It enables capabilities such as:

```text
create repository for authenticated user
create organization repository when user/org policy allows
rename/update repository settings
change visibility where GitHub/user policy allows
transfer repository
manage collaborators / invitations
manage deploy keys and repository autolinks
manage branch protection / rulesets / repository Actions policy settings
manage repository topics and other settings
manage automated security-fix configuration
read traffic and other admin metadata
delete repository (must be separately guarded at Runtime Bridge tool level)
```

This is the key permission required for the project owner's explicit request that Codexless can create/manage repositories.

**Tradeoff:** requesting repository Administration means installation in an organization normally requires organization-owner approval; repository admins alone cannot install an App that requests repository Administration. This may reduce portability into organizations where the user is not an owner.

### 4.2 Checks

**Recommended candidate: `Checks = Read & write`.**

Adds first-class check-run/check-suite creation, updates, reruns, annotations and result reading. This is useful for a professional autonomous development system that may publish validation/status evidence independently of GitHub Actions.

### 4.3 Commit statuses

**Recommended change: upgrade `Commit statuses` from Read-only to Read & write.**

The parity target only required reading combined statuses, but extension capability benefits from publishing bounded commit-status results.

### 4.4 Deployments and Environments

**Recommended candidates: `Deployments = Read & write`, `Environments = Read & write`.**

These enable creation/management of deployments, deployment statuses, environments, protection/configuration state, environment variables and environment secrets metadata/management where the API supports it. They are valuable for CI/CD and release automation beyond connector parity.

### 4.5 Pages

**Recommended candidate: `Pages = Read & write` if GitHub Pages automation is desired.**

Allows reading/updating Pages configuration and triggering builds. Useful but not foundational to ordinary repository development.

### 4.6 Code security and quality

Strong candidates for a comprehensive development/security layer:

```text
Code quality            Read-only where the current endpoint family is read-only
Code scanning alerts    Read & write
Dependabot alerts       Read & write
Secret scanning alerts  Read & write, with explicit destructive/dismissal guards
Attestations             Read & write
Repository security advisories  candidate, but high-sensitivity workflow
```

These permit Codexless to inspect and, where appropriate, manage security findings rather than only manipulate source code.

### 4.7 Agent/Copilot repository capabilities

Candidate families:

```text
Agent tasks              Read & write (public preview)
Agent variables          Read & write
Copilot agent settings   Read & write if available/needed
Agent secrets            high-risk; defer until secure secret-value transport exists
```

`Agent tasks` is particularly interesting because GitHub's current API can start/manage Copilot cloud-agent tasks and supports GitHub App **user access tokens**, matching the user-token architecture already selected for Codexless.

### 4.8 Codespaces

Potential comprehensive cloud-development capability:

```text
Codespaces lifecycle admin   Read & write
Codespaces metadata          Read-only
Codespaces                   Read & write
Codespaces secrets           high-risk; defer until secure secret-value transport exists
```

This would let Codexless create/start/stop/delete/publish Codespaces and inspect machine/devcontainer metadata. It is valuable if Codespaces is part of the intended development workflow, but not necessary for local Codexless operation.

### 4.9 Variables

**Recommended candidate: `Variables = Read & write`.**

Repository variables are non-secret configuration and are useful for CI/CD automation with much lower sensitivity than secret values.

### 4.10 Webhooks

**Do not enable merely for comprehensiveness.**

Repository Webhooks(write) would let Codexless create external post-receive hooks, which introduces arbitrary outbound destinations and a potential data-exfiltration path. The current architecture is polling/request-driven and deliberately has the App's own webhook receiver disabled. Add this only if a concrete webhook-management feature is designed with destination allowlisting and explicit user confirmation.

### 4.11 Secret-bearing permission families

High-risk families:

```text
Secrets
Dependabot secrets
Codespaces secrets
Agent secrets
organization secrets
organization agent secrets
organization Codespaces secrets
organization Dependabot secrets
```

These APIs generally do not reveal plaintext secret values, but write access can replace/delete encrypted secret material. Codexless currently has no dedicated secure user-to-GitHub secret-value transport contract. Therefore these should remain **No access for initial extended App creation** unless that secure secret-management architecture is deliberately built first.

## 5. Broader permission selection profiles

### Profile A: parity-only

The Checkpoint 391 seven-permission set. No longer preferred given the clarified product goal.

### Profile B: broad professional developer superset

**Current recommended direction.** Keep the parity permissions and add high-value repository development/admin/security/CI capabilities while excluding secret-value and arbitrary-webhook authority until purpose-built safeguards exist.

Likely additions/upgrades:

```text
Administration          write
Checks                  write
Commit statuses         write  (upgrade)
Deployments             write
Environments            write
Variables               write
Code quality            read
Code scanning alerts    write
Dependabot alerts       write
Secret scanning alerts  write
Attestations            write
Agent tasks              write   if live UI/account supports it
Agent variables          write   if intended
Copilot agent settings   write   if intended
Codespaces lifecycle admin write if intended
Codespaces metadata      read    if intended
Codespaces               write   if intended
Pages                    write   if intended
Custom properties        write   if intended
```

Keep initially off:

```text
Secrets / secret-value families
Webhooks
Repository security advisories unless a vulnerability-publication workflow is explicitly wanted
organization-wide destructive/admin permissions
enterprise permissions
personal-account mutation permissions unrelated to development
```

### Profile C: literal maximum authority

Selecting nearly every write permission is technically possible in many cases but is **not recommended**. It would greatly increase token-compromise blast radius, make organization installation/approval harder, add unrelated personal/organization authority, and force Runtime Bridge to secure many destructive APIs that the user may never need.

The project goal should be **maximum useful development capability**, not maximum unchecked permission count.

## 6. Organization-level tradeoff

Organization permissions can add powerful capabilities such as members/teams, projects, Actions runners, org variables/secrets, custom properties and org settings. However, they also make installation dependent on organization-owner approval and broaden authority beyond repository scope.

For the first App version, the recommended architecture is:

```text
repository-level developer/admin superset  broad
organization permissions                   add only concrete developer-management families
account/user permissions                    add only concrete user workflows
enterprise permissions                      none unless an enterprise target exists
```

If organization portability becomes more important than full administration, a future second lower-authority GitHub App profile could be considered without creating a second ChatGPT Plugin. Codexless Runtime Bridge can conceptually host more than one server-owned GitHub credential profile, but that complexity is not justified yet.

## 7. Repository scope remains independent of permission breadth

App permission breadth and installation repository scope are separate. For the owner's personal installation, the clarified target is **All repositories**, not the earlier one-repository-only qualification scope. GitHub explicitly allows All repositories or Only select repositories, and repositories created by an installed App are automatically added to that installation's accessible repositories.

Organization repositories require installing the same public App on the relevant organization/account and remain bounded by installation approval plus the authorizing user's own permissions.

## 8. Current recommendation before GitHub App creation

Do **not** create the App from the Checkpoint 392 seven-permission prefill yet.

Next:

```text
1. inventory every live registration permission visible for this account;
2. reconcile established docs + preview/live-only permission families;
3. freeze a broad developer-superset permission profile;
4. update the registration prefill/checklist;
5. then create the App once with the intended initial authority.
```

Checkpoint 391/392 remain valid historical parity/preflight evidence, but their seven-permission creation instruction is superseded pending this review.

## 9. Official GitHub sources

- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/choosing-permissions-for-a-github-app
- https://docs.github.com/en/rest/authentication/permissions-required-for-github-apps
- https://docs.github.com/en/rest/authentication/endpoints-available-for-github-app-user-access-tokens
- https://docs.github.com/en/rest/apps/apps
- https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters
- https://docs.github.com/en/rest/agent-tasks/agent-tasks
- https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party
- https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps

```text
EXTENDED_PERMISSION_REVIEW=ACTIVE
PARITY_ONLY_7_PERMISSION_CREATION=PAUSED
TARGET=MAXIMUM_USEFUL_DEVELOPER_CAPABILITY
REPOSITORY_ADMINISTRATION=STRONG_RECOMMENDATION
SECRET_VALUE_PERMISSIONS=DEFER_PENDING_SECURE_TRANSPORT
WEBHOOK_MANAGEMENT=DEFER_PENDING_BOUNDED_DESIGN
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
NEXT=CAPTURE_AND_RECONCILE_COMPLETE_LIVE_PERMISSION_UI
```
