# Checkpoint 397: GitHub App Registered, Private-Key Install Gate Next

**Date:** 2026-09-09
**Status:** PASS / LIVE APP REGISTERED / INSTALLATION NOT YET COMPLETE
**Checkpoint class:** GITHUB APP REGISTRATION
**Project stage:** Research 123 GitHub parity plus Codexless extensions
**Scope:** Preserve successful creation of the extended GitHub App and the newly observed GitHub requirement to generate a private key before installation.
**Authority:** Validation 154 and `github_app_live_registration_20260909.json` own the live registration evidence and corrected bootstrap boundary.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

```text
App name   Codexless Runtime Bridge
Owner      shakaarlatief
App ID     4881901
Client ID  Iv23lirgmw82wV0SGTWn
Slug       codexless-runtime-bridge
Registered true
Installed  false
```

GitHub's live UI requires a private key before installation. The key is not part of Runtime Bridge's selected user-token/device-flow runtime authority. Generate one only to satisfy the install gate, never expose it, install with All repositories, then destroy the downloaded local PEM.

```text
CHECKPOINT397=GITHUB_APP_REGISTERED_PRIVATE_KEY_INSTALL_GATE
GITHUB_APP_REGISTERED=true
GITHUB_APP_INSTALLED=false
CLIENT_SECRET_GENERATED=false
PRIVATE_KEY_GENERATED=false
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=GENERATE_ONE_PRIVATE_KEY_INSTALL_ALL_REPOSITORIES_DESTROY_LOCAL_PEM
```
