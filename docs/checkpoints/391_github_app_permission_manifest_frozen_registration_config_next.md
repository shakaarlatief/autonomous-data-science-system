# Checkpoint 391: GitHub App Permission Manifest Frozen, Registration Configuration Next

**Date:** 2026-09-08
**Status:** PASS / 89-ACTION PERMISSION MAPPING COMPLETE / SEVEN REPOSITORY PERMISSIONS FROZEN / GRAPHQL LIVE PROBE REQUIRED
**Checkpoint class:** GITHUB APP AUTHORITY MANIFEST
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the exact REST-derived GitHub App permission manifest for the 89-action parity target while explicitly retaining GraphQL permission sufficiency as an empirical post-registration gate.
**Authority:** Validation 148 and `github_app_permission_manifest.json` own the permission evidence/mapping; Validation 147 / Checkpoint 390 own the fresh-host authorization-support and live Plugin-name qualification.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Frozen initial App permissions

```text
Actions          write
Contents         write
Issues           write
Metadata         read
Pull requests    write
Commit statuses  read
Workflows        write
```

No organization, account, enterprise or webhook permissions are requested.

Administration, Checks and Members remain explicitly absent.

## 2. Every native action is mapped

The new machine artifact maps all 89 exact actions in exact inventory order and the validator passes:

```text
GITHUB_APP_PERMISSION_MANIFEST=PASS
GITHUB_APP_PERMISSION_MANIFEST_ACTION_COUNT=89
GITHUB_APP_PERMISSION_MANIFEST_REPOSITORY_PERMISSION_COUNT=7
GITHUB_APP_GRAPHQL_PERMISSION_SUFFICIENCY=LIVE_PROBE_REQUIRED
```

## 3. Exact GraphQL permission sufficiency is not documentation-resolvable

GitHub publishes REST endpoint permission requirements, but its current GitHub App guidance instructs developers to **test** GraphQL queries/mutations for permission sufficiency rather than publishing an exact GraphQL permission table.

Eight native actions require GraphQL or GraphQL-node handling. All are PR/review resources, so the frozen App already carries `Pull requests(write)` without adding any speculative permission. Live sufficiency must be tested after App registration.

## 4. No authorization has started

```text
GitHub App registered             false
GitHub App client ID configured  false
stored authorization             false
live GitHub authorization        NOT STARTED
public github.* actions           0 / 89
```

## 5. Next boundary

Freeze the exact non-secret GitHub App registration configuration around this seven-permission manifest before asking the owner to create/install the App in GitHub's account UI.

The registration configuration must keep webhooks disabled, enable device flow, choose installability/owner/repository-selection policy deliberately, and introduce no extra permissions.

```text
CHECKPOINT391=GITHUB_APP_PERMISSION_MANIFEST_FROZEN
PERMISSION_ACTION_MAPPING=89_OF_89
REPOSITORY_PERMISSION_COUNT=7
GRAPHQL_PERMISSION_SUFFICIENCY=LIVE_PROBE_REQUIRED
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=FREEZE_GITHUB_APP_REGISTRATION_CONFIGURATION
```
