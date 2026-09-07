# Checkpoint 340: Runtime Lifecycle and Device Access Research Opened

**Date:** 2026-09-07
**Status:** RESEARCH 122 ACTIVE / RUNTIME-MAINTENANCE + PHONE ACCESS BASELINE OPENED
**Checkpoint class:** ARCHITECTURE / LOCAL EXECUTION / CROSS-DEVICE ACCESS
**Project stage:** Post-document direct-access infrastructure hardening
**Scope:** Opens the next project-owner-selected stage after Research 120/121 completion. It activates the previously preserved narrow runtime-maintenance authority and device-independent connector gaps, records the current self-restart dependency, captures new official tunnel-client managed-runtime evidence, and reframes the phone problem against current OpenAI mobile support.
**Authority:** Research 122 governs this stage; Validation 098 contains the initial evidence baseline; AB-001, AB-002, AB-006 and AB-017 remain the linked backlog owners.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The repository already preserved both user-requested directions. AB-002/AB-017 cover narrow `%LOCALAPPDATA%` runtime publication and lifecycle authority without ordinary whole-profile access. AB-001 records the earlier phone failure `401 tunnel_active_organization_required` while the laptop/tunnel remained running, and AB-006 separately owns task recovery across caller/tunnel/device interruption.

Initial evidence materially changes the implementation direction. The exact installed tunnel-client v0.0.13 exposes native `runtimes connect/list/status/stop/rm/cleanup` commands, and current upstream OpenAI documentation explicitly recommends `runtimes connect` for long-lived local runtimes managed by Codex. A read-only local probe confirms those commands exist. A second probe shows that the current ordinary ADS command sandbox cannot initialize tunnel-client's default user-profile state directory, while the same managed-runtime command succeeds when `TUNNEL_CLIENT_STATE_DIR` is redirected to a bounded workspace-local temporary root. The active seam is therefore a dedicated host-runtime state/credential/lifecycle authority class, not missing tunnel lifecycle functionality.

The current self-restart limitation is also preserved explicitly: an action served only by Codexless cannot safely stop Codexless or the tunnel carrying its own request and still synchronously guarantee a response. The candidate architecture must therefore use a separately owned lifecycle mechanism that accepts a bounded job before destructive restart begins and can complete recovery independently.

Current official OpenAI Help Center documentation now states that MCP apps are not available on mobile and are web-only. Therefore the historical native-phone failure is not treated as a purely local tunnel defect. The first phone experiment in this stage will distinguish native mobile app from mobile browser web access before any custom remote-control surface is designed.

```text
CHECKPOINT_340 = RUNTIME_LIFECYCLE_DEVICE_ACCESS_RESEARCH_OPENED
NEXT = QUALIFY_MANAGED_TUNNEL_RUNTIME + DESIGN_NARROW_SUPERVISOR + PHONE_SURFACE_MATRIX
```
