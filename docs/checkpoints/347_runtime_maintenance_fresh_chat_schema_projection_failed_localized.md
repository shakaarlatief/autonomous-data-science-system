# Checkpoint 347: Runtime Maintenance Fresh-Chat Schema Projection Failure Localized

**Date:** 2026-09-07
**Status:** FAIL AT CHATGPT HOST SCHEMA FIDELITY / TOOL DISCOVERED / NO MUTATION INVOKED
**Checkpoint class:** HOST INTEGRATION / SAFETY QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Preserves the first fresh-chat ChatGPT host discovery of live `codex.runtime_maintenance`, distinguishes successful tool discovery from failed schema fidelity, and blocks the first production self-restart until the host-facing schema is structurally narrow.
**Authority:** Research 122 governs the architecture; Validation 105 owns the detailed host-projection evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

After refreshing the developer MCP app, a fresh disposable ChatGPT conversation successfully discovered `codex.runtime_maintenance`. The fresh chat did not invoke that tool or any other ADS tool.

The host-projected callable definition, however, exposed the input as a generic map:

```text
type codex.runtime_maintenance = (_: {
  [key: string]: any
}) => any;
```

The intended server contract was still visible in the description, but the host projection did not preserve the action enum, required `requestId`, or `additionalProperties: false` as callable schema structure. Therefore discovery presence passed while mutation-sensitive schema fidelity failed.

This is not evidence of server-side authority widening. Direct local MCP `tools/list` on the active preview.18 runtime still serializes the exact restrictive top-level `oneOf` where both branches require `action` and `requestId` and reject additional properties. The first live restart was deliberately not attempted.

A corroborating host-side observation is that the older `codex.workspace_authority`, also implemented as a top-level discriminated union, is projected in the current ChatGPT tool surface as the same generic `{ [key: string]: any }` shape, while ordinary top-level object tools preserve structured fields. This localizes the compatibility problem to the current host projection of top-level union/`oneOf` schemas rather than the runtime-maintenance service semantics.

```text
CHECKPOINT_347=RUNTIME_MAINTENANCE_FRESH_CHAT_SCHEMA_PROJECTION_FAILED_LOCALIZED
TOOL_DISCOVERED=true
HOST_SCHEMA_FIDELITY=false
SERVER_VALIDATION_STILL_NARROW=true
LIVE_SELF_RESTART_INVOKED=false
NEXT=FLAT_TOP_LEVEL_SCHEMA_CANDIDATE
```
