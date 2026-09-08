# Checkpoint 392: GitHub App Registration Configuration Frozen, Owner Creation Next

**Date:** 2026-09-08
**Status:** PASS / REGISTRATION CONFIGURATION FROZEN / OWNER GITHUB UI CREATION REQUIRED
**Checkpoint class:** GITHUB APP REGISTRATION PREFLIGHT
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the exact non-secret GitHub App registration and first-installation configuration before the account-bound owner creation step.
**Authority:** Validation 149 and `github_app_registration_configuration.json` own the registration configuration; Validation 148 / Checkpoint 391 own the permission manifest.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Frozen registration

```text
owner               shakaarlatief (personal account)
name                Codexless Runtime Bridge
visibility          Any account / public
homepage            public ADS repository
callback URL        none
request OAuth install OFF
device flow         ON
expire user tokens  ON
setup URL           none
webhooks            OFF
private key         not used/generated
```

The seven repository permissions from Checkpoint 391 are reused exactly with no organization/account/enterprise permissions.

## 2. Initial installation

```text
account              shakaarlatief
repository access    Only select repositories
selected repository  shakaarlatief/autonomous-data-science-system
```

This is a staged G0 qualification scope, not the final parity scope.

## 3. Owner action required

The current Runtime Bridge cannot create a GitHub App through account UI. The owner must create the App using the frozen prefill/checklist and then install it on the one selected repository.

Return only non-secret identifiers/state such as App ID, Client ID, installation ID and screenshots/settings confirmation. Never paste a client secret, private key, access token, refresh token or device code.

## 4. Next boundary

After creation/install, preserve the actual registration evidence, then implement/configure the fixed server-owned non-secret Client ID path and require metadata to show:

```text
configured          true
storedAuthorization false
```

Only then begin one explicit device authorization.

```text
CHECKPOINT392=GITHUB_APP_REGISTRATION_CONFIGURATION_FROZEN
GITHUB_APP_REGISTERED=false
GITHUB_APP_CLIENT_ID_CONFIGURED=false
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=OWNER_CREATE_AND_INSTALL_GITHUB_APP
```
