# Validation 152: GitHub Extended Permission Manifest and Registration Prefill Frozen

**Date:** 2026-09-09
**Status:** PASS / 74-PERMISSION DEVELOPER SUPERSET FROZEN / OWNER APP CREATION READY
**Research:** Research 123
**Scope:** Convert the complete 118-row live GitHub permission inventory into the first frozen broader-than-native Codexless GitHub App permission manifest, preserve exact selected access levels, generate the safest reproducible registration prefill possible without guessing undocumented parameters, and freeze the owner creation/install sequence.

## 1. Frozen extended authority

The final initial App profile selects 74 of the 118 current live permission rows:

```text
repository selected/read   34 / 40
organization selected/read 30 / 42
account selected/read      10 / 19
enterprise selected         0 / 17
total selected/read        74 / 118
```

The 89-action native connector parity authority remains a strict subset. The extended profile additionally includes repository creation/administration, checks/status publication, deployments/environments, Codespaces, discussions, packages, projects, security management, Agent/Copilot surfaces and selected organization/account administration.

Repository `Administration=write` is now frozen, directly enabling later bounded repository creation/settings/collaborator capabilities that the provider-owned native ChatGPT GitHub connector did not expose.

## 2. Exact repository No-access boundary

Only six live repository permission rows remain off:

```text
Agent secrets
Codespaces secrets
Dependabot secrets
Secrets
Single file
Webhooks
```

The secret-value families are deferred until Runtime Bridge owns a secure secret-value input/encryption/mutation contract. `Single file` is redundant with broader Contents authority. Webhooks remain off until external destinations are explicitly bounded.

## 3. Organization/account/enterprise boundary

Organization capability is broad but excludes 12 credential/secret/PAT/webhook/unrelated-governance families. Account capability is limited to ten developer-oriented rows and excludes nine personal-control/context/secret rows. All 17 enterprise permission rows remain No access because no enterprise target is established.

High-consequence permissions that *are* selected, such as repository/organization Administration, member administration, security-advisory mutation, bypass/dismissal review and runner administration, remain subject to future bounded semantic Runtime Bridge tool contracts. App-level authority does not imply arbitrary API passthrough.

## 4. Exact access-level changes

The old parity-only seven-permission set is preserved as a subset, with Commit statuses deliberately upgraded from read to write:

```text
Actions          write
Contents         write
Issues           write
Metadata         read
Pull requests    write
Commit statuses  write
Workflows        write
```

Repository Projects and organization Projects are set to `admin`; organization Custom properties is also `admin`, because current GitHub permission documentation explicitly supports that highest level for those permission families.

## 5. Registration prefill is reproducible but does not guess

GitHub documents that App registration URLs use permission names as query parameters and `read`, `write`, or where supported `admin` as values.

The extended prefill therefore includes:

```text
56 independently documented permission parameters
+ App identity
+ public=true / Any-account visibility
+ request_oauth_on_install=false
+ webhook_active=false
```

There are 18 current live/newer selected permission rows whose registration parameter names were not independently verified from the current official parameter surfaces. They remain explicit **manual UI selections** rather than guessed URL parameters:

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

This preserves reproducibility without asserting undocumented query keys.

## 6. Registration settings remain bounded

```text
owner                         shakaarlatief
App name                      Codexless Runtime Bridge
visibility                    Any account / public
Enable Device Flow            ON
Expire user authorization     ON
Request OAuth during install  OFF
Callback URL                  blank
Setup URL                     blank
Webhook Active                OFF
private-key bootstrap         NOT USED
```

Device Flow and expiring-user-token settings remain manual confirmations because GitHub's documented registration URL parameter table does not expose those switches.

## 7. Personal installation scope

The owner's clarified target is frozen as:

```text
personal account   shakaarlatief
repository access  All repositories
```

Organization repositories still require installing/approving the same public App on each relevant organization. Effective user-token authority remains user access intersected with installation scope and App permissions.

## 8. Validator

```text
GITHUB_APP_EXTENDED_PERMISSION_MANIFEST=PASS
GITHUB_APP_EXTENDED_SELECTED_PERMISSION_COUNT=74
GITHUB_APP_EXTENDED_DOCUMENTED_PREFILL_COUNT=56
GITHUB_APP_EXTENDED_MANUAL_PERMISSION_COUNT=18
GITHUB_APP_EXTENDED_PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
```

The validator also proves the old parity set remains covered, Administration(write) is present, selected/no-access counts match the 118-row live inventory, no repository/organization webhook permission enters the URL, registration settings are exact, and the prefill contains precisely the 56 independently documented permission parameters.

## 9. Mutation boundary

No GitHub App has been created. No Client ID, client secret, private key, token, device code or installation exists yet. No GitHub authorization has started.

The next step is owner-performed creation from the extended registration prefill, completion of the 18 manual permission rows/settings, and installation on the personal account with **All repositories**.

```text
VALIDATION152=PASS
EXTENDED_GITHUB_APP_PERMISSION_MANIFEST=FROZEN
SELECTED_PERMISSION_COUNT=74
DOCUMENTED_PREFILL_PERMISSION_COUNT=56
MANUAL_PERMISSION_SELECTION_COUNT=18
REPOSITORY_ADMINISTRATION=WRITE
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
GITHUB_APP_REGISTERED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=OWNER_CREATE_EXTENDED_GITHUB_APP_AND_INSTALL_ALL_PERSONAL_REPOSITORIES
```
