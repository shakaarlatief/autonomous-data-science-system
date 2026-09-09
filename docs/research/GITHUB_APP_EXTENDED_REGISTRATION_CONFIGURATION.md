# Extended GitHub App Registration Configuration

**Date:** 2026-09-09
**Status:** FROZEN / OWNER CREATION READY
**Research:** Research 123
**Machine authority:** `docs/research/github_app_extended_registration_configuration.json`
**Permission authority:** `docs/research/github_app_extended_permission_manifest.json`

## Frozen identity and registration settings

```text
owner               shakaarlatief
name                Codexless Runtime Bridge
visibility          Any account / public
homepage            https://github.com/shakaarlatief/autonomous-data-science-system
request OAuth install OFF
Device Flow          ON
expire user tokens   ON
callback URL         none
setup URL            none
redirect on update   OFF
webhooks             OFF
private key          do not generate/use
```

This preserves the qualified Runtime Bridge device-flow architecture while changing the permission profile from the historical seven-permission parity baseline to the frozen 74-row GitHub developer superset.

## Permission selection totals

```text
repository selected/read   34 / 40
organization selected/read 30 / 42
account selected/read      10 / 19
enterprise selected         0 / 17
total selected/read        74 / 118
```

The exact levels are owned by `GITHUB_APP_EXTENDED_PERMISSION_MANIFEST.md`.

## Prefill behavior

The frozen GitHub registration URL contains 56 permission selections whose parameter names were independently documented, plus the identity/visibility/webhook/install-OAuth settings.

The remaining 18 current live permission rows are **manual UI selections** because their registration query parameter names were not independently verified. They are intentionally not guessed.

Manual permission rows:

```text
repository: Agent tasks -> write
repository: Agent variables -> write
repository: Copilot agent settings -> read
repository: License compliance alerts -> read
repository: Secret scanning alert dismissal requests -> write
repository: Secret scanning push protection bypass requests -> write
organization: Agent variables -> write
organization: Copilot Spaces -> write
organization: Copilot content exclusion -> write
organization: Hosted runner custom images -> read
organization: Issue Fields -> write
organization: Organization Copilot metrics -> read
organization: Organization bypass requests for secret scanning -> write
organization: Organization dismissal requests for Dependabot -> write
organization: Organization innersource vulnerabilities -> write
organization: Secret scanning alert dismissal requests -> write
account: Issue Fields -> write
account: Issue Types -> write
```

## Required manual configuration after opening the prefill

In addition to those 18 permission rows, explicitly verify:

```text
Expire user authorization tokens  ON
Enable Device Flow                ON
Where can this GitHub App be installed?  Any account
Callback URL                      blank
Setup URL                         blank
Webhook Active                    OFF
```

These settings are not all representable through GitHub's documented registration URL parameters.

## Explicit No-access boundary

Keep the following repository permissions at No access:

```text
Agent secrets
Codespaces secrets
Dependabot secrets
Secrets
Single file
Webhooks
```

Keep the following organization permissions at No access:

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

Keep the following account permissions at No access:

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

Keep all 17 Enterprise permissions at No access.

## Creation and installation sequence

1. Open the extended prefill URL from this artifact.
2. Confirm App name exactly Codexless Runtime Bridge. If GitHub reports a uniqueness conflict, stop and return that evidence rather than silently renaming.
3. Confirm homepage and description exactly match the artifact.
4. Confirm Request user authorization during installation is OFF.
5. Confirm Callback URL and Setup URL are blank; redirect-on-update remains OFF.
6. Confirm Expire user authorization tokens is ON.
7. Confirm Enable Device Flow is ON.
8. Confirm webhook Active is OFF and no webhook URL/secret/events are configured.
9. Confirm Where can this GitHub App be installed? is Any account.
10. Verify the prefill-selected permission rows against the frozen manifest.
11. Manually set each of the 18 live/newer permission rows listed in this artifact because their URL parameter names were not independently verified.
12. Confirm the six repository No-access rows, twelve organization No-access rows, nine account No-access rows, and all seventeen enterprise rows remain No access.
13. Create the GitHub App. Do not generate a private key.
14. Install it on personal account shakaarlatief with All repositories.
15. Return only non-secret App ID, Client ID, installation ID, App slug/settings URL and screenshots/settings confirmation. Do not paste client secret, private key, access token, refresh token, device_code, webhook secret or any other credential.

## Personal installation scope

After creation, install the App on the personal owner account with:

```text
Repository access: All repositories
```

This is the owner's clarified target. It allows the App installation to cover current and future repositories under that personal account, still subject to the authorizing user and App permission intersection. Organization repositories require separate installation/approval of the same public App on each relevant organization.

## Credential boundary

After creation, **App ID, Client ID, App slug and installation ID are non-secret identifiers** and may be returned for qualification. Do not paste/store client secret, private key, access token, refresh token, device code or webhook secret. No private key is needed for the current user-token/device-flow bootstrap.

## Frozen prefill URL

The machine artifact contains the exact URL. It is intentionally long because it preselects 56 independently documented permission parameters.

## Next boundary

The next action is owner-performed App creation from the extended prefill, manual completion of the 18 live-only permission selections and settings verification, followed by installation on `shakaarlatief` with **All repositories**.

After that evidence returns, preserve the actual App identity/settings, configure only the non-secret Client ID into fixed server-owned Runtime Bridge configuration, require `metadata` to change to `configured=true` while `storedAuthorization=false`, and only then begin one explicit device authorization.

```text
EXTENDED_GITHUB_APP_REGISTRATION=FROZEN
APP_NAME=Codexless Runtime Bridge
APP_VISIBILITY=ANY_ACCOUNT_PUBLIC
SELECTED_PERMISSION_COUNT=74
DOCUMENTED_PREFILL_PERMISSION_COUNT=56
MANUAL_PERMISSION_SELECTION_COUNT=18
DEVICE_FLOW=ON
EXPIRE_USER_TOKENS=ON
REQUEST_OAUTH_ON_INSTALL=OFF
WEBHOOKS=OFF
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
GITHUB_APP_REGISTERED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_CREATE_EXTENDED_GITHUB_APP_AND_INSTALL_ALL_PERSONAL_REPOSITORIES
```
