# Checkpoint 309: ChatGPT Host Capability Probe Live, Fresh Chat Required

**Date:** 2026-09-06
**Status:** LIVE 59-TOOL DIAGNOSTIC SURFACE / SAME-CHAT PROJECTION STALE / FRESH-CHAT QUALIFICATION READY
**Checkpoint class:** LOCAL EXECUTION / DIRECT CHATGPT FILE ACCESS
**Project stage:** Research 117 / Research 119 direct local-file access
**Scope:** Preserves the live publication and restart of the temporary read-only MCP Apps host-capability probe, successful tunnel readiness verification, same-conversation stale tool-projection reproduction after Plugin refresh, and the exact fresh-chat experiment needed to determine whether ChatGPT advertises `updateModelContext.resourceLink`.
**Authority:** Validation 067 is the detailed evidence. Research 119 remains the governing objective correction.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-18`
**Conversation title:** `18 - Astra Architecture Review and Multimodal Handoff Continuation`
**Primary collaborator:** ChatGPT

Current live surface:

```text
Codexless version   0.1.1-preview.15-host-capability-probe
source tools        59
tunnel readyz       PASS
```

The diagnostic is intentionally model-free and source-free. It reads only the ChatGPT MCP Apps host capability advertisement from the standard `ui/initialize` handshake. It does not read a local document, upload a file, use Browser, or mutate model context during the capability probe itself.

The user refreshed the existing `ADS Codexless Local Bridge` Plugin after the controlled restart. This persistent conversation nevertheless retained its older callable schema and did not expose the three new probe tools. That is classified as same-chat projection staleness, not a live-server publication failure.

The temporary exact-root `codexless-live` workspace admission used for the one-time source publication was removed after verification. The normal durable registry is again revision 7 with four workspaces and no ordinary Codexless runtime-root admission.

The exact next step is a **fresh disposable ChatGPT conversation** using the refreshed Plugin. Its first task is only to run the host-capability probe and read the resulting whitelist receipt.

Decision boundary:

```text
updateModelContext.resourceLink advertised
    -> small direct PDF resourceLink -> model-context qualification

not advertised
    -> stop this route
    -> deterministic multi-PDF resource_link experiment
```

No semantic document worker is part of either path.

```text
CHECKPOINT_309 = HOST_CAPABILITY_PROBE_LIVE_FRESH_CHAT_REQUIRED
```
