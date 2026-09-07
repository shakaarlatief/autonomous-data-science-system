# Checkpoint 348: Runtime Maintenance Preview.19 Flat Schema Candidate Qualified

**Date:** 2026-09-07
**Status:** PASS / FLAT HOST-COMPATIBLE SCHEMA CANDIDATE QUALIFIED / GUARDED PUBLICATION NEXT
**Checkpoint class:** ARCHITECTURE / HOST COMPATIBILITY / LIFECYCLE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the preview.19 schema-only compatibility candidate that replaces the top-level runtime-maintenance discriminated union with one strict top-level object, adds actual MCP wire-schema regression coverage, and preserves the previously qualified lifecycle behavior and 62-tool surface.
**Authority:** Research 122 governs the architecture; Validation 106 owns the detailed candidate evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The private runtime candidate is durably synchronized at:

```text
ac3e05de0ebd9553eafb322ce19ec17539f1c09d
```

The proposed corrected runtime is:

```text
version    0.1.1-preview.19-runtime-maintenance-schema
surface    codexless-public-preview-v2
toolCount  62
```

Relative to the preview.18 integration candidate, only three integration files differ:

```text
src/mcp-server-factory.mjs
src/surface-contracts.mjs
test/public-surface-registration.mjs
```

The runtime-maintenance schema is now one ordinary strict object:

```text
type                    object
properties              action, requestId
required                action, requestId
action enum             restart_codexless, status
additionalProperties    false
top-level oneOf         absent
```

The regression suite now tests the actual MCP wire definition, not only the in-process Zod parser. It connects the real `McpServer` to linked MCP transports, sends `initialize`, `notifications/initialized`, and `tools/list`, then verifies the serialized `codex.runtime_maintenance.inputSchema` field-by-field.

The wire regression passes together with the eight staged public compatibility scripts and all previously qualified lifecycle suites/probes. Production remains preview.18 / 62 tools and the tunnel remains live/ready. No production source or process was changed by this candidate qualification.

```text
CHECKPOINT_348=RUNTIME_MAINTENANCE_PREVIEW19_FLAT_SCHEMA_CANDIDATE_QUALIFIED
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS
LIVE_MUTATION=false
NEXT=GUARDED_PREVIEW19_PUBLICATION_PREFLIGHT
```
