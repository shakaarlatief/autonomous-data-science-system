# Checkpoint 395: GitHub Extended Permission Manifest Frozen, Owner Creation Next

**Date:** 2026-09-09
**Status:** PASS / 74-ROW EXTENDED PROFILE FROZEN / OWNER CREATION READY
**Checkpoint class:** GITHUB APP EXTENDED AUTHORITY + REGISTRATION FREEZE
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve the final initial extended GitHub App permission profile and reproducible registration configuration after complete 118-row live UI capture.
**Authority:** Validation 152 and `github_app_extended_permission_manifest.json` own the 74-row authority profile; `github_app_extended_registration_configuration.json` owns creation/install settings; Validation 151 owns the 118-row live inventory.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Final initial permission profile

```text
repository selected/read   34 / 40
organization selected/read 30 / 42
account selected/read      10 / 19
enterprise selected         0 / 17
total selected/read        74 / 118
```

The old seven-permission parity baseline remains contained inside this profile but is no longer the App-creation target.

Repository Administration(write) is included so Codexless can later expose bounded repository creation/administration beyond native connector parity.

## 2. Registration prefill

The new registration prefill embeds 56 permission selections using independently documented parameter names. Eighteen current live/newer permission rows remain manual UI selections rather than guessed query keys.

Device Flow ON, expiring user authorization tokens ON, install-time OAuth OFF, webhooks OFF, and Any-account/public visibility remain frozen.

## 3. Installation scope

```text
personal account   shakaarlatief
repository access  All repositories
```

Organization installations remain explicit and separately approved.

## 4. No live GitHub mutation yet

```text
GitHub App registered             false
GitHub App client ID configured  false
stored authorization             false
live GitHub authorization        NOT STARTED
public github.* actions           0 / 89
```

## 5. Next boundary

The owner can now create the App from the extended prefill, manually complete the 18 live-only permission rows and manual settings, select **Any account**, then install the App on `shakaarlatief` with **All repositories**.

Return only non-secret App ID, Client ID, App slug/settings URL, installation ID and setting confirmation. Do not paste client secret, private key, access token, refresh token, device code or webhook secret.

```text
CHECKPOINT395=EXTENDED_GITHUB_APP_PERMISSION_MANIFEST_FROZEN
SELECTED_PERMISSION_COUNT=74
DOCUMENTED_PREFILL_PERMISSION_COUNT=56
MANUAL_PERMISSION_SELECTION_COUNT=18
REPOSITORY_ADMINISTRATION=WRITE
PERSONAL_INSTALL_SCOPE=ALL_REPOSITORIES
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
SOURCE_VAULT=PAUSED
NEXT=OWNER_CREATE_EXTENDED_GITHUB_APP_AND_INSTALL_ALL_PERSONAL_REPOSITORIES
```
