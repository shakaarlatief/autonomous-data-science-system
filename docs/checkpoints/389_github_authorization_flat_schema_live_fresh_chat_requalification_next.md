# Checkpoint 389: GitHub Authorization Flat Schema Live, Fresh-Chat Requalification Next

**Date:** 2026-09-08
**Status:** PASS / PREVIEW.24 HOST UNION GENERICIZATION REPRODUCED / PREVIEW.25 FLAT CORRECTION LIVE / FRESH-CHAT RETEST NEXT
**Checkpoint class:** HOST-PROJECTION FAILURE + LIVE SCHEMA CORRECTION
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the failed preview.24 fresh-host metadata qualification, the exact local-vs-host union projection discrepancy, and successful live activation of the flat preview.25 correction before any actual GitHub authorization begins.
**Authority:** Validation 146 owns detailed evidence; private local-runtime head `ad10aa30342503d303b6a22629fe56dc914f0fa2` owns the correction/release bytes.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Preview.24 fresh-host qualification failed

The fresh disposable ChatGPT conversation projected `codex.github_authorization`, but its host input schema was only:

```text
{ [key: string]: any }
```

The local live MCP still had a strict six-branch `oneOf`, so this is another AB-008 top-level-union genericization observation.

The exactly one permitted `metadata` call was blocked by OpenAI host safety controls before a Runtime Bridge payload was returned. No device flow or credential activity was observed.

## 2. Correction reuses the qualified flat-schema pattern

Preview.25 replaces the top-level union with one strict flat object:

```text
action            required six-value enum
requestId         optional bounded string
authorizationRef  optional bounded string
confirmClear      optional const true
additionalProperties=false
```

Exact action/field combinations remain enforced server-side with `GITHUB_AUTHORIZATION_INPUT_INVALID`.

## 3. Corrected release is live

```text
private runtime head     ad10aa30342503d303b6a22629fe56dc914f0fa2
releaseId                github-auth-control-flat-v2
manifest SHA-256         a71dda9a430b292ca7fd0c16d2db95dc31e577b23f474dc83590c145032e5447
runtime version          0.1.1-preview.25-github-auth-flat
public tool count        64
runtime dependency       1
source mismatches        0
```

Publication operation `rm_6215ff67fd5ca530af3ca953b0cad03a` and activation operation `rm_accbd4edacc46458cae81dd493173feb` both succeeded without recovery.

The full staged 16-regression release matrix passed before publication, including an explicit flat GitHub-authorization MCP wire-schema assertion.

## 4. Local postactivation check

Direct local MCP discovery now exposes the exact flat schema with no `oneOf`, and metadata still reports:

```text
configured             false
initialized            false
authorized             false
storedAuthorization    false
```

No GitHub authorization has started.

## 5. Next boundary

Refresh the renamed developer-MCP Plugin and use a new disposable ChatGPT conversation to repeat discovery plus exactly one metadata-only call.

The decisive discriminator is whether ChatGPT now projects the flat schema structurally and permits the bounded read-only metadata action to reach Runtime Bridge.

```text
CHECKPOINT389=GITHUB_AUTHORIZATION_FLAT_SCHEMA_LIVE
PREVIEW24_FRESH_HOST=FAIL_GENERIC_SCHEMA_AND_SAFETY_BLOCK
PREVIEW25_LOCAL_FLAT_SCHEMA=PASS
PUBLIC_TOOL_COUNT=64
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=FRESH_CHAT_GITHUB_AUTHORIZATION_FLAT_SCHEMA_AND_METADATA_REQUALIFICATION
```
