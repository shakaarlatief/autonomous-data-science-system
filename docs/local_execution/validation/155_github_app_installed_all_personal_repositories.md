# Validation 155: GitHub App Installed on All Personal Repositories

**Date:** 2026-09-09
**Status:** PASS / APP INSTALLED / ALL PERSONAL REPOSITORIES / LOCAL PRIVATE-KEY DELETION PENDING
**Research:** Research 123
**Scope:** Preserve owner-supplied live evidence that the extended `Codexless Runtime Bridge` GitHub App is installed on the personal account with `All repositories` selected.

## 1. Live installation evidence

The owner supplied the post-installation GitHub page. It visibly shows:

```text
Codexless Runtime Bridge
Installed now
Developed by shakaarlatief
```

The same page shows the repository-access selector with:

```text
All repositories = selected
```

GitHub's explanatory text states that this applies to all current and future repositories owned by the resource owner, with public repositories also included read-only according to GitHub's installation UI.

## 2. Permission summary remains consistent

The installation page visibly summarizes repository access including:

```text
Read access
    License compliance alerts
    Codespaces metadata
    Copilot agent settings
    Metadata

Read and write access
    Dependabot alerts
    Actions
    Actions variables
    Administration
    Agent tasks
    Agent variables
    Artifact metadata API
    Checks
    Code / Contents-related authority
    Code quality
    Codespaces
    Codespaces lifecycle admin
    Commit statuses
    Repository custom properties
    Deployments
    Discussions
    Environments
    Issues
    Merge queues
    Packages
    Pages
    Pull requests
    Repository advisories
    Secret-scanning dismissal/bypass/alerts
    Security events
    Workflows

Admin access
    Repository projects
```

This is consistent with the frozen extended repository-permission profile from Checkpoint 395/396.

## 3. Installation state

```text
GitHub App registered   true
GitHub App installed    true
installation account    shakaarlatief
repository scope        All repositories
installation ID         not yet captured
```

The private key had to be generated because GitHub's live UI required one before installation. Runtime Bridge does not use that key in its selected user-token/device-flow architecture.

## 4. Immediate security cleanup

The downloaded local `.pem` private-key file must now be securely deleted before Runtime Bridge authorization proceeds.

Do not paste, upload, commit, copy into a repository, or otherwise expose that PEM. The corresponding GitHub-side public key registration may remain because the runtime does not need the private half.

No Client secret should be generated.

## 5. Next boundary

After the owner confirms local PEM deletion, configure only the non-secret Client ID:

```text
Iv23ligrmw82wVOSGTWn
```

into the fixed server-owned Runtime Bridge GitHub authorization configuration. Then qualify:

```text
configured          true
storedAuthorization false
```

through `codex.github_authorization metadata` before starting one explicit device authorization.

```text
VALIDATION155=PASS
GITHUB_APP_REGISTERED=true
GITHUB_APP_INSTALLED=true
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
INSTALLATION_ID=NOT_YET_CAPTURED
PRIVATE_KEY_GENERATED=true
LOCAL_PRIVATE_KEY_DELETION=PENDING_USER_CONFIRMATION
CLIENT_SECRET_GENERATED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_DELETE_DOWNLOADED_PRIVATE_KEY_PEM_THEN_CONFIGURE_NON_SECRET_CLIENT_ID
```
