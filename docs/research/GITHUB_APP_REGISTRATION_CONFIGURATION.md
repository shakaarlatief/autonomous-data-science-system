# GitHub App Registration Configuration

**Date:** 2026-09-08
**Status:** FROZEN / OWNER UI CREATION + FIRST INSTALLATION REQUIRED
**Research:** Research 123
**Machine authority:** `docs/research/github_app_registration_configuration.json`
**Permission authority:** `docs/research/github_app_permission_manifest.json`

## Purpose

Freeze every non-secret registration and first-installation choice that should be made in GitHub before the project owner performs the account-bound GitHub App creation. The goal is to avoid making security/authority decisions ad hoc in the GitHub UI and to preserve the practical-parity architecture without starting authorization prematurely.

## Registration owner and identity

```text
owner account type   personal
owner login          shakaarlatief
GitHub App name      Codexless Runtime Bridge
description          GitHub capability layer for the Autonomous Data Science System through Codexless Runtime Bridge.
homepage             https://github.com/shakaarlatief/autonomous-data-science-system
```

The personal owner is the same account that owns the canonical public ADS repository. The App is registered as **Any account / public** so this one registration can later be installed on the owner account and on user-controlled organizations without transferring/recreating the App. A private personal-account App would be installable only on its owner account and would therefore prevent the multi-installation parity target.

Public App visibility does **not** grant repository access by itself. Each installation still requires explicit approval and repository selection, and Runtime Bridge remains bounded by the user + App installation intersection. The App is not being listed in GitHub Marketplace as part of this work.

GitHub requires an App name to be unique and no longer than 34 characters. `Codexless Runtime Bridge` is 24 characters. GitHub itself remains the authority on availability at creation time. If it reports a name conflict, stop and return that evidence rather than silently choosing another identity.

## Authorization settings

```text
Enable Device Flow                         ON
Request user authorization during install  OFF
Expire user authorization tokens           ON
Callback URL                               blank
Setup URL                                  blank
Redirect on update                         OFF
Client secret needed by selected flow      NO
Generate/use private key for bootstrap      NO
```

The selected Runtime Bridge contract uses OAuth device flow, not the web application flow. GitHub documentation says callback URLs are ignored for device flow, so no callback URL should be invented. GitHub strongly recommends expiring user access tokens; this is also required by the already-qualified eight-hour access / six-month refresh lifecycle.

Authorization is deliberately **not** requested automatically during installation. User authorization must remain an explicit Runtime Bridge `begin` action after installation and server-owned client-ID configuration. This keeps installation and user authorization as independently qualified gates.

## Webhooks

```text
Active          OFF
Webhook URL     none
Webhook secret  none
Events          none
```

The current parity target is request-driven and has no webhook-dependent action. Leaving webhooks off avoids introducing an unrelated inbound network/secret surface.

## Frozen repository permissions

```text
Actions          write
Contents         write
Issues           write
Metadata         read
Pull requests    write
Commit statuses  read
Workflows        write
```

No organization, account or enterprise permissions are configured. Administration, Checks and Members remain no-access. See `GITHUB_APP_PERMISSION_MANIFEST.md` for the exact 89-action mapping and the separate GraphQL sufficiency boundary.

## Installability and first installation

GitHub registration setting:

```text
Where can this GitHub App be installed?  Any account
```

Initial qualification installation:

```text
account             shakaarlatief
repository access   Only select repositories
selected repository shakaarlatief/autonomous-data-science-system
```

This initial one-repository installation minimizes live blast radius while still allowing the project to qualify device authorization, installation/repository derivation, and read-only GraphQL sufficiency against the canonical ADS development repository. It is a staged qualification boundary, not the final parity scope.

After G0 is proven, additional installations and broader repository selection may be granted explicitly. Runtime Bridge must never invent or widen repository access beyond GitHub installation scope.

## Frozen GitHub registration prefill

GitHub supports URL parameters for the identity, visibility, webhook state and permission fields. The frozen personal-account prefill URL is preserved in the machine artifact. It preselects:

```text
name
description
homepage URL
request_oauth_on_install=false
public=true
webhook_active=false
seven repository permissions
```

Two critical settings are **not** represented in GitHub's documented registration URL parameter table and must be checked manually:

```text
Enable Device Flow                ON
Expire user authorization tokens  ON
```

Repository selection also occurs later during installation rather than registration.

## Owner creation checklist

1. Open the frozen personal-account prefill URL.
2. Confirm GitHub App name is Codexless Runtime Bridge; if GitHub reports a uniqueness conflict, stop and report it rather than silently renaming.
3. Confirm homepage and description exactly match this artifact.
4. Leave Callback URL blank.
5. Leave Request user authorization (OAuth) during installation unchecked.
6. Leave Expire user authorization tokens enabled.
7. Enable Device Flow.
8. Leave Setup URL blank and Redirect on update disabled.
9. Disable Webhook Active; no webhook URL, secret or events.
10. Confirm exactly the seven repository permissions from the frozen manifest and no other permission families.
11. Select Any account for installability.
12. Create the GitHub App.
13. Do not generate a private key.
14. Record App ID and Client ID as non-secret identifiers; do not copy Client secret into chat/repository.
15. Install the App on the personal owner account with Only select repositories and select only shakaarlatief/autonomous-data-science-system for the first qualification.

## Post-creation evidence to return

After creation and the first limited installation, preserve only non-secret identifiers/state:

```text
App name
App slug / settings URL if visible
App ID
Client ID
owner account
visibility / Any account
device flow enabled
expiring user tokens enabled
webhook inactive
seven permission selections
installation ID (non-secret)
selected repository identity
```

**Do not paste or store:** client secret, private key, access token, refresh token, device code, webhook secret. No private key should be generated for this selected user-token/device-flow bootstrap.

## Next boundary

Once the App exists and the first selected-repository installation is verified, the Runtime Bridge needs a bounded server-owned configuration path for the **non-secret Client ID**. Metadata must then move from `configured=false` to `configured=true` while `storedAuthorization=false`. Only after that read-only configuration gate passes should the owner explicitly begin one device authorization.

The first device-flow qualification will then establish protected token storage and installation/repository scope before the eight GraphQL permission probes and before any public `github.*` parity action is published.

```text
GITHUB_APP_REGISTRATION_CONFIGURATION=FROZEN
GITHUB_APP_OWNER=shakaarlatief
GITHUB_APP_NAME=Codexless Runtime Bridge
GITHUB_APP_VISIBILITY=ANY_ACCOUNT_PUBLIC
DEVICE_FLOW=ENABLED
REQUEST_OAUTH_ON_INSTALL=DISABLED
EXPIRE_USER_AUTH_TOKENS=ENABLED
CALLBACK_URL=NONE
SETUP_URL=NONE
WEBHOOKS=DISABLED
REPOSITORY_PERMISSION_COUNT=7
INITIAL_INSTALL_SCOPE=ONLY_SELECTED_REPOSITORIES
INITIAL_SELECTED_REPOSITORY=shakaarlatief/autonomous-data-science-system
PRIVATE_KEY_BOOTSTRAP=NOT_USED
GITHUB_APP_REGISTERED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_CREATE_AND_INSTALL_GITHUB_APP
```

## Official GitHub sources

- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app
- https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/making-a-github-app-public-or-private
- https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/generating-a-user-access-token-for-a-github-app
- https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/refreshing-user-access-tokens
- https://docs.github.com/en/apps/sharing-github-apps/registering-a-github-app-using-url-parameters
