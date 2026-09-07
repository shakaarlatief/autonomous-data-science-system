# Checkpoint 358: Runtime Release Preview.20 Fresh-Chat Schema Qualified

**Date:** 2026-09-07
**Status:** PASS / FRESH-HOST `codex.runtime_release` SCHEMA QUALIFIED / FIRST LIVE RELEASE OPERATION NEXT
**Checkpoint class:** FRESH-HOST TOOL-PROJECTION QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the refreshed disposable-chat host projection of the live preview.20 semantic runtime-release surface without invoking any ADS tool in that qualification chat.
**Authority:** Research 122 governs the architecture; Validation 116 owns detailed host evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

A refreshed disposable ChatGPT conversation exposed `codex.runtime_release` successfully. The fresh-chat qualification invoked no ADS tool.

The host-projected callable schema was:

```text
type codex.runtime_release = (_: {
  action: "prepare" | "publish" | "verify" | "rollback" | "status",
  releaseId: string, // minLength: 1, maxLength: 128, pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
  requestId: string, // minLength: 1, maxLength: 128, pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
  expectedSourceHead: string, // pattern: /^[0-9a-f]{40}$/
}) => any;
```

The host therefore preserves the mutation-sensitive preview.20 surface as one named structured object rather than the generic `{ [key: string]: any }` projection that previously blocked preview.18 runtime-maintenance qualification. Exactly four caller-visible fields are present, all are required, the exact five-action enum is structurally visible, release/request identifiers retain bounded patterns, and `expectedSourceHead` is structurally constrained to exactly 40 lowercase hexadecimal characters.

The rendered callable definition does not print a literal `additionalProperties: false` line, so that exact JSON-Schema keyword is not claimed as host-visible. However, the host surface exposes no index signature/catch-all property and exposes only the four named fields above.

No caller field exposes filesystem path, install root, destination, workspace selector, PID, executable, shell command, argv, cwd, environment, URL, tunnel identity, credential, permission profile, sandbox, regression command/list, or arbitrary host-process/filesystem authority. No separate MCP annotation object was visible in the host projection.

The persistent project conversation remains an older projection and is not used as fresh-host evidence. Independently after receiving the disposable-chat result, the live server was still verified as:

```text
version   0.1.1-preview.20-runtime-release
tools     63
surface   codexless-public-preview-v2
tunnel    live / ready
```

This closes the fresh-host schema gate. The next work is not to immediately mutate the installed runtime. First construct and preserve one genuine next-version release bundle in the fixed private `runtime-releases/<releaseId>` namespace, qualify it completely against the live preview.20 baseline, and then use the fresh-host semantic surface to prove `prepare`, publication, activation, verification/status and rollback/recovery semantics without another ordinary-host `%LOCALAPPDATA%` helper.

```text
CHECKPOINT_358=RUNTIME_RELEASE_PREVIEW20_FRESH_CHAT_SCHEMA_QUALIFIED
HOST_SCHEMA=PASS
LIVE_VERSION=0.1.1-preview.20-runtime-release
LIVE_TOOL_COUNT=63
TOOL_INVOKED_IN_FRESH_CHAT=false
NEXT=BUILD_AND_QUALIFY_FIRST_SEMANTIC_RELEASE_BUNDLE
```
