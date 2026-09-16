# Checkpoint 532: Browser Lifecycle Boundary Localized, Genuine-Turn Qualification Deferred, G009 Route Preserved

**Date:** 2026-09-16
**Status:** BROWSER LIFECYCLE ROOT CAUSE LOCALIZED / MODEL-FREE CLAIM PATH REMAINS FAIL-CLOSED / GENUINE-TURN EXPERIMENT DEFERRED / G009 REMAINS NEXT
**Checkpoint class:** LOCAL_EXECUTION / RUNTIME_SUPPORT / ARCHITECTURE VALIDATION
**Project stage:** Candidate 01 W0 implementation with bounded Browser lifecycle side investigation
**Scope:** Preserve the exact current Browser cleanup mechanism and the supported boundary between out-of-band model-free MCP calls and genuine Codex turns without changing the active Runtime Bridge or project-knowledge route.
**Authority:** Validation 208 is the detailed execution evidence. Research 117 / Research 118 remain the governing Browser/document architecture evidence. Current official OpenAI Codex App Server/core source provides upstream implementation evidence. Specification 028 and Research 179 remain governing for Candidate 01 W0.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** chatgpt-25
**Conversation title:** 25 - Identity Transition Semantics and G006 Repair
**Primary collaborator:** ChatGPT

After Checkpoint 531 restored current Browser/Chrome discovery and live tab inventory, the remaining existing-tab lifecycle boundary was investigated model-free against the exact current Browser bundle, active Codexless executor and current official OpenAI Codex source.

The current Browser service's maintained documentation states that unmarked claimed external user tabs are released and left open when the Codex turn ends. Source inspection localized the mechanism: Browser session requests are tracked by `{session_id, turn_id}` through a Node REPL turn-ended tracker, which invokes Browser `turnEnded(...)` cleanup when the matching genuine turn terminates. The current node_repl runtime exposes the corresponding maintained `turn_ended` lifecycle tool.

The current Codexless direct Browser path, however, executes `node_repl/js` through App Server `mcpServer/tool/call` and supplies locally generated synthetic turn/session metadata. Current official Codex source confirms `mcpServer/tool/call` dispatches directly through `CodexThread::call_mcp_tool(...)`; it does not perform `turn/start`. A genuine `turn/start` is a model generation turn and ends through the normal `turn/completed` lifecycle.

No public `releaseTab`, `unclaimTab`, `unclaim`, or current `Tabs.finalize` operation exists in the installed Browser build. Therefore no supported model-free release primitive was missed.

The following apparent workarounds remain explicitly rejected:

```text
manual node_repl turn_ended after direct call     lifecycle fabrication
synthetic turn metadata as ownership proof        unsupported
markDeliverable / markHandoff as release          wrong semantics
closing user tab as cleanup                       destructive substitute
runtime/process teardown as release               no exact supported receipt
private backend cleanup calls                     authority/API violation
```

The accepted direct-path disposition is therefore unchanged but now more strongly grounded:

```text
status / tab inventory                  LIVE-QUALIFIED
existing-tab claim-requiring actions    BLOCK BEFORE CLAIM
new-tab direct lifecycle                 DEFERRED / UNPROVEN
direct model-free cleanup repair         NO SUPPORTED CURRENT PATH FOUND
genuine-turn Browser lifecycle           UPSTREAM NORMAL MODEL EXISTS
ADS genuine-turn integration             NOT YET QUALIFIED
```

A future Browser-operation experiment should use one real Codex turn and verify normal claim cleanup plus interruption/failure semantics. That is a separate metered/model-mediated capability and must not be smuggled into the deterministic direct Browser API by forging turn completion. No Codex model turn was started and no Runtime Bridge source mutation was made by this checkpoint.

The Browser upload implementation remains preserved but not live-qualified for existing user tabs. No PDF upload was attempted.

Project-development routing remains unchanged:

```text
PKA-G001..PKA-G008   PASS
PKA-G009..PKA-G017   PENDING
next W0 task          PKA-G009 derived-view framework
W1                    NOT STARTED
operational authority current continuity architecture
authority switch      NOT ALLOWED
```

```text
CHECKPOINT532=BROWSER_LIFECYCLE_BOUNDARY_LOCALIZED
VALIDATION208=PASS
MODEL_FREE_EXISTING_TAB_CLAIM=BLOCKED_CORRECTLY
SUPPORTED_DIRECT_RELEASE_API=NONE_FOUND_CURRENT_BUILD
GENUINE_TURN_BROWSER_QUALIFICATION=DEFERRED
RUNTIME_VERSION=0.1.1-preview.47-browser-current-plugin-compat-public
RUNTIME_MUTATION=NONE
NEXT=PKA_G009_DERIVED_VIEW_FRAMEWORK
AUTHORITY_SWITCH_ALLOWED=false
```
