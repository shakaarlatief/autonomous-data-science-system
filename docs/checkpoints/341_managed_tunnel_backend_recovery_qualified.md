# Checkpoint 341: Managed Tunnel Backend Recovery Qualified

**Date:** 2026-09-07
**Status:** PASS / SAME MANAGED TUNNEL RECOVERS AFTER LOCAL MCP TARGET OUTAGE
**Checkpoint class:** ARCHITECTURE / LOCAL EXECUTION / LIFECYCLE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies exact installed managed-tunnel behavior across a real local MCP target outage and recovery without touching the production tunnel, establishing tunnel-preserving Codexless-only restart as the preferred normal lifecycle direction.
**Authority:** Research 122 governs the architecture; Validation 099 owns the detailed functional evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT
**Research:** Research 122
**Validation:** Validation 099

An isolated managed tunnel created by the exact installed OpenAI tunnel-client v0.0.13 successfully forwarded a real MCP initialize and tools/list to the live local Codexless backend through a temporary proxy, observed a real 502 when that local MCP path was removed, remained running, and then forwarded a new initialize and tools/list after the local path returned without any tunnel reconnect/restart. Both successful tools/list calls returned the live 61-tool surface.

The production tunnel and live Codexless process were not mutated and remained healthy afterward.

Architecture consequence: ordinary Codexless publication/restart should keep the managed tunnel running and restart only Codexless through a separately owned deferred helper. Full tunnel restart is reserved for tunnel-specific changes/failure. Tunnel readiness alone is not sufficient outage/recovery evidence because the managed runtime can remain nominally ready while a formerly healthy local target is absent; use real backend health and command/reinitialize evidence.

```text
CHECKPOINT_341=MANAGED_TUNNEL_BACKEND_RECOVERY_QUALIFIED
NEXT=DETACHED_ONE_SHOT_CODEXLESS_RESTART_HELPER_CANDIDATE
```
