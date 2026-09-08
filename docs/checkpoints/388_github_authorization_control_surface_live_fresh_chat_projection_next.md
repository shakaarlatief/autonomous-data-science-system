# Checkpoint 388: GitHub Authorization Control Surface Live, Fresh-Chat Projection Next

**Date:** 2026-09-08
**Status:** PASS / 64-TOOL AUTHORIZATION SUPPORT LIVE / SAME-CHAT PROJECTION STALE / FRESH-CHAT METADATA GATE NEXT
**Checkpoint class:** LIVE RUNTIME SUPPORT-SURFACE QUALIFICATION
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve successful publication and activation of the bounded GitHub authorization-control support tool, its live local MCP schema and metadata-only result, and the same-conversation ChatGPT projection limitation before any actual GitHub authorization begins.
**Authority:** Validation 145 owns detailed release/schema/metadata evidence; private local-runtime head `d63bb48112985fd05e4a32925b83e75214dd2a4a` owns the corrected implementation and release bytes.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Authorization support is now live

Runtime Release v2 successfully published and activated:

```text
releaseId               github-auth-control-v2-fix2
private runtime head    d63bb48112985fd05e4a32925b83e75214dd2a4a
manifest SHA-256        92554d6da7418885fcb491f1c16a2527517ca09d6c230d0d8a5dc54e1421a7be
runtime version         0.1.1-preview.24-github-auth-control
public tool count       64
runtime dependency      1
source mismatches       0
```

Publication operation `rm_137444f8dda39d01c282b2c1d47a9356` and activation operation `rm_91321739c5b2287e638719a37c2de0b3` both reached `succeeded` without recovery.

## 2. Public support tool is separate from 89-action parity

The active local MCP tool inventory contains exactly one new GitHub support action:

```text
codex.github_authorization
```

It manages metadata/begin/status/poll/cancel/clear for GitHub App device flow. It is infrastructure and does not increment the fixed native GitHub parity count.

```text
public github.* parity actions = 0 / 89
```

## 3. Live metadata-only qualification passed

A direct active local MCP `metadata` call returned:

```text
configured             false
initialized            false
authorized             false
storedAuthorization    false
authMode               github-app-user-token-device-flow
host                   github.com
restApiVersion         2026-03-10
```

No device flow, GitHub token creation, credential clearing or GitHub API/OAuth request occurred.

## 4. Release failures strengthened the release contract

The original release and first immutable retry both failed their regression gates. The original prepared release then correctly refused changed bytes under the same release ID. `fix2` resolved the actual regressions rather than weakening them and was the first publication to succeed.

That history remains preserved as negative evidence for immutable prepared-release identity and fail-closed regression publication.

## 5. Same-chat projection is stale

The active local MCP `tools/list` contains the new support action and the runtime is healthy at 64 tools, but this existing persistent ChatGPT conversation still does not project `codex.github_authorization` as a normal callable tool.

This is an AB-008 host-projection lifecycle reproduction, not a server publication failure.

## 6. Next boundary

Use a refreshed fresh disposable ChatGPT conversation to discover the new support action, capture the actual host-visible schema, and invoke **metadata only** once. Do not begin or poll device flow in that host-projection qualification.

Current authorization state is deliberately empty:

```text
GitHub App client ID configured  false
stored authorization             false
live GitHub auth                  NOT STARTED
public github.* actions           0 / 89
```

Actual GitHub App registration/client-ID configuration and device-flow user authorization come only after this fresh-host support-tool gate is closed.

```text
CHECKPOINT388=GITHUB_AUTHORIZATION_CONTROL_LIVE
LIVE_RUNTIME_VERSION=0.1.1-preview.24-github-auth-control
PUBLIC_TOOL_COUNT=64
RUNTIME_DEPENDENCY_COUNT=1
AUTH_SUPPORT_TOOL=codex.github_authorization
LIVE_LOCAL_METADATA=PASS
SAME_CHAT_TOOL_PROJECTION=STALE
LIVE_GITHUB_AUTH=NOT_STARTED
PUBLIC_GITHUB_ACTIONS=0
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=FRESH_CHAT_GITHUB_AUTHORIZATION_SCHEMA_AND_METADATA_QUALIFICATION
```
