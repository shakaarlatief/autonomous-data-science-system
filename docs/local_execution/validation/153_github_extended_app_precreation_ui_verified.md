# Validation 153: GitHub Extended App Pre-Creation UI Verified

**Date:** 2026-09-09
**Status:** PASS / OWNER UI PRE-CREATION STATE MATCHES CHECKPOINT 395
**Research:** Research 123
**Scope:** Verify the manually completed GitHub App registration form against the frozen extended permission and registration configuration immediately before the owner creates the App.

## 1. Owner-supplied live UI evidence

The owner supplied current GitHub registration screenshots after completing the manual settings and permission additions from Checkpoint 395.

The authorization section visibly confirms:

```text
Homepage URL                         https://github.com/shakaarlatief/autonomous-data-science-system
Redirect URI                         blank
Allow wildcard matching              OFF
Expire user authorization tokens     ON
Request user authorization (OAuth)
  during installation                OFF
Enable Device Flow                   ON
Setup URL                            blank
Redirect on update                   OFF
Webhook Active                       OFF
Webhook URL                          blank
Webhook Secret                       blank
```

These values match the frozen extended registration configuration.

## 2. Permission counts match exactly

The collapsed live permission headers show:

```text
Repository permissions   33 selected + 1 mandatory = 34 total
Organization permissions 30 selected
Account permissions      10 selected
Enterprise permissions    0 selected
```

This matches the frozen 74-row extended profile exactly:

```text
34 + 30 + 10 + 0 = 74
```

No count drift remains between the owner-completed GitHub UI and `github_app_extended_permission_manifest.json`.

## 3. Installability matches exactly

The owner screenshot visibly shows:

```text
Where can this GitHub App be installed?
    Any account = SELECTED
    Only on this account = NOT SELECTED
```

This closes the pre-creation installability check that the registration URL itself did not reliably set.

## 4. Pre-creation gate

The owner has not yet clicked `Create GitHub App` in the supplied evidence. Therefore:

```text
GitHub App registered             false
GitHub App client ID configured  false
stored authorization             false
live GitHub authorization        NOT STARTED
```

The registration form is now qualified as ready for creation.

## 5. Next action

The owner may now click `Create GitHub App`.

After creation:

```text
- do not generate a private key;
- install the App on personal account shakaarlatief;
- choose All repositories;
- return only non-secret App ID, Client ID, App slug/settings URL, installation ID and setting/install screenshots;
- do not return client secret, private key, access token, refresh token, device code or webhook secret.
```

```text
VALIDATION153=PASS
EXTENDED_APP_PRECREATION_UI=VERIFIED
SELECTED_PERMISSION_COUNT=74
DEVICE_FLOW=ON
EXPIRE_USER_TOKENS=ON
REQUEST_OAUTH_ON_INSTALL=OFF
WEBHOOKS=OFF
APP_VISIBILITY=ANY_ACCOUNT_PUBLIC
GITHUB_APP_REGISTERED=false
NEXT=OWNER_CLICK_CREATE_AND_INSTALL_ALL_PERSONAL_REPOSITORIES
```
