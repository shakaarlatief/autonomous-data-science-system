# Checkpoint 398: GitHub App Installed on All Repositories, Private-Key Cleanup Next

**Date:** 2026-09-09
**Status:** PASS / LIVE APP INSTALLED / ALL PERSONAL REPOSITORIES / PEM CLEANUP NEXT
**Checkpoint class:** GITHUB APP INSTALLATION
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve live installation of the extended GitHub App on the owner's personal account with All repositories selected.
**Authority:** Validation 155 and `github_app_live_registration_20260909.json` own the installation evidence; Checkpoint 397 owns the private-key installation-gate discovery.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

```text
App name              Codexless Runtime Bridge
Owner                 shakaarlatief
App ID                4881901
Client ID             Iv23ligrmw82wVOSGTWn
Slug                  codexless-runtime-bridge
Registered            true
Installed             true
Personal repo scope   All repositories
Installation ID       not yet captured
```

The private key required by GitHub's install gate was generated, but Runtime Bridge does not use it. The downloaded local PEM must now be deleted before authorization work continues.

```text
CHECKPOINT398=GITHUB_APP_INSTALLED_ALL_REPOSITORIES
PRIVATE_KEY_GENERATED=true
LOCAL_PRIVATE_KEY_DELETION=PENDING_USER_CONFIRMATION
CLIENT_SECRET_GENERATED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=DELETE_LOCAL_PEM_THEN_CONFIGURE_NON_SECRET_CLIENT_ID
```
