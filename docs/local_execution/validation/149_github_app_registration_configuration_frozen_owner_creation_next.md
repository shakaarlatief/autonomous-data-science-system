# Validation 149: GitHub App Registration Configuration Frozen, Owner Creation Next

**Date:** 2026-09-08
**Status:** PASS / NON-SECRET REGISTRATION CONFIGURATION FROZEN / ACCOUNT-BOUND OWNER CREATION REQUIRED
**Research:** Research 123
**Scope:** Freeze the exact non-secret GitHub App registration and first-installation choices around the seven-permission authority manifest before the owner performs the account-bound GitHub UI creation step.

## 1. Official GitHub registration behavior rechecked

Current GitHub documentation confirms:

```text
- an App may be owned by a personal account or organization;
- App names are limited to 34 characters and must be unique on GitHub;
- a public / Any account App can be installed on other accounts;
- a private / Only on this account App can be installed only on its owner account;
- device flow is an explicit App setting;
- callback URLs are ignored for device flow;
- GitHub strongly recommends expiring user authorization tokens;
- user authorization during installation is optional and distinct from installation;
- webhooks can be disabled when not needed;
- repository scope is selected at installation as All repositories or Only select repositories;
- GitHub supports registration URL parameters for identity, visibility, webhook state and permission choices, but its documented URL-parameter table does not expose the Device Flow or token-expiration toggles.
```

Sources are preserved in `GITHUB_APP_REGISTRATION_CONFIGURATION.md`.

## 2. Frozen registration owner and identity

The canonical public ADS Git remote is owned by:

```text
shakaarlatief
```

The GitHub App registration is therefore frozen under that personal account.

Identity:

```text
GitHub App name  Codexless Runtime Bridge
name length      24 / 34
homepage         https://github.com/shakaarlatief/autonomous-data-science-system
description      GitHub capability layer for the Autonomous Data Science System through Codexless Runtime Bridge.
```

GitHub itself remains authority for global App-name uniqueness at creation time. If the name is unavailable, the owner must stop and return that evidence rather than silently creating a differently named App.

## 3. Visibility is Any account / public

The frozen setting is:

```text
Where can this GitHub App be installed?  Any account
```

This is required by the target architecture rather than chosen for discoverability. The 89-action target includes installation/account discovery and is intended to support personal and organization installations. A private App owned by the personal account could be installed only on that account and would structurally block organization-installation parity.

Public App visibility does not grant repository access by itself. Each installation remains separately approved and repository-scoped. Marketplace publication is not part of this work.

## 4. Authorization configuration

```text
Enable Device Flow                         ON
Request user authorization during install  OFF
Expire user authorization tokens           ON
Callback URL                               blank
Setup URL                                  blank
Redirect on update                         OFF
```

This preserves the already-qualified Runtime Bridge authorization lifecycle:

```text
install first
configure server-owned non-secret Client ID
metadata -> configured=true / storedAuthorization=false
explicit user-intent begin
user completes device code at GitHub
poll -> protected token storage
```

The selected device flow does not require a client secret. The bootstrap also does not require a GitHub App private key/JWT/installation-token path; no private key should be generated during this stage.

## 5. Webhooks remain disabled

```text
Active          OFF
Webhook URL     none
Webhook secret  none
Events          none
```

The parity target is request-driven. No webhook-dependent capability has been observed, so introducing a webhook secret/inbound event surface would widen architecture without evidence.

## 6. Exact permission manifest retained

```text
Actions          write
Contents         write
Issues           write
Metadata         read
Pull requests    write
Commit statuses  read
Workflows        write
```

No organization, account or enterprise permissions are configured. Administration, Checks and Members remain no-access.

The registration configuration reuses `github_app_permission_manifest.json` exactly; no permission decision is duplicated or widened.

## 7. Initial installation scope

After App creation, the first qualification installation is deliberately narrow:

```text
installation account   shakaarlatief
repository access      Only select repositories
selected repository    shakaarlatief/autonomous-data-science-system
```

This minimizes live blast radius while still supporting:

```text
device-flow authorization qualification
user/App installation-intersection derivation
read-only repository metadata qualification
read-only GraphQL PR/review permission sufficiency probes
```

It does not redefine final parity scope. After G0 authorization/GraphQL sufficiency passes, additional repositories/accounts may be explicitly installed/approved. Runtime Bridge must never widen beyond GitHub's installation scope.

## 8. Reproducible prefill

The machine artifact preserves an exact personal-account GitHub registration URL with preselected:

```text
name
description
homepage
public=true
request_oauth_on_install=false
webhook_active=false
actions=write
contents=write
issues=write
metadata=read
pull_requests=write
statuses=read
workflows=write
```

The owner must still manually confirm:

```text
Enable Device Flow = ON
Expire user authorization tokens = ON
```

because those settings are not in GitHub's documented registration-URL parameter table.

## 9. Validator

```text
GITHUB_APP_REGISTRATION_CONFIGURATION=PASS
GITHUB_APP_REGISTRATION_OWNER=shakaarlatief
GITHUB_APP_REGISTRATION_VISIBILITY=ANY_ACCOUNT_PUBLIC
GITHUB_APP_INITIAL_INSTALL_SCOPE=ONE_SELECTED_REPOSITORY
```

The validator also asserts exact equality with the seven-permission manifest and rejects callback/setup/webhook/private-key drift.

## 10. Current mutation boundary

No GitHub App was created or installed by this validation, because the current Runtime Bridge exposes no GitHub account UI/browser action for App registration and the account-bound GitHub confirmation belongs to the owner.

No client ID, client secret, private key, access token, refresh token or device code was created or stored.

The project is now ready for one owner-performed GitHub UI step using the frozen configuration. After creation/install, return only the non-secret evidence requested by the registration artifact. Never paste a client secret, private key or token.

```text
VALIDATION149=PASS
GITHUB_APP_REGISTRATION_CONFIGURATION=FROZEN
GITHUB_APP_OWNER=shakaarlatief
GITHUB_APP_NAME=Codexless Runtime Bridge
GITHUB_APP_VISIBILITY=ANY_ACCOUNT_PUBLIC
DEVICE_FLOW=ENABLED
REQUEST_OAUTH_ON_INSTALL=DISABLED
EXPIRE_USER_AUTH_TOKENS=ENABLED
WEBHOOKS=DISABLED
REPOSITORY_PERMISSION_COUNT=7
INITIAL_INSTALL_SCOPE=ONE_SELECTED_REPOSITORY
PRIVATE_KEY_BOOTSTRAP=NOT_USED
GITHUB_APP_REGISTERED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_CREATE_AND_INSTALL_GITHUB_APP
```
