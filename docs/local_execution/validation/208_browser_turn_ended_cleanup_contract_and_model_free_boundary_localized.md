# Validation 208: Browser Turn-End Cleanup Contract and Model-Free Boundary Localized

**Date:** 2026-09-16
**Status:** PASS / ROOT CAUSE LOCALIZED / MODEL-FREE CLAIM PATH REMAINS CORRECTLY FAIL-CLOSED / GENUINE-TURN QUALIFICATION DEFERRED
**Research:** Research 117 / Research 118 with current OpenAI Codex source reconciliation

## 1. Objective

Validation 207 restored current Browser/Chrome plugin discovery and live Browser inventory on Runtime Bridge preview.47 while intentionally leaving claim-requiring operations blocked. This follow-up isolates the exact cleanup mechanism behind that remaining boundary and asks whether a supported model-free repair exists without inventing a second Browser lifecycle.

No Browser mutation, user-tab claim, screenshot, PDF upload, Codex model turn, upstream plugin change, permission change or live runtime source change was authorized for this investigation.

## 2. Current bundled Browser contract

The exact installed Browser build remains:

```text
chrome   26.908.40834
browser  26.908.40834
```

The maintained Browser documentation embedded in the current bundled Browser service states that agent-created Chrome tabs close automatically when the turn ends unless marked; `markDeliverable()` preserves a user-facing output tab; `markHandoff()` preserves a tab that must continue later; and claimed user tabs that are not marked are released from browser-session control and left open when the turn ends.

The same current implementation contains no public `releaseTab`, `unclaimTab`, `unclaim`, or `Tabs.finalize` operation. `markDeliverable()` and `markHandoff()` classify turn-end survival; they are not public release primitives.

## 3. Exact cleanup mechanism

Read-only inspection of the current bundled Browser service localizes the cleanup mechanism precisely.

Browser session requests are tracked against the current `session_id` and `turn_id`. The Browser transport registers those identities with a turn-ended tracker. That tracker requires the Node REPL runtime to expose `addTurnEndedHandler`; if it is absent, Browser startup fails with the explicit invariant that Browser Use requires Node REPL turn-ended hooks.

When the matching turn ends, the tracker invokes the Browser transport's `turnEnded(...)` path. That path performs turn-owned detach/cleanup and notifies the Browser backend that the matching turn ended.

The current Runtime Bridge node_repl inventory independently preserves the maintained `turn_ended` tool contract with required `hook_event_name`, `session_id` and `turn_id` fields and the description `Notify trusted libraries that a Codex turn ended.` This is lifecycle infrastructure, not caller authority to manufacture a turn completion.

The current cleanup architecture is therefore:

```text
genuine Browser request in a Codex turn
    -> Browser service tracks {session_id, turn_id}
    -> genuine turn reaches its terminal lifecycle
    -> node_repl turn-ended hook fires for the exact pair
    -> Browser service turnEnded(...) runs
    -> unmarked claimed user tab is released and remains open
```

## 4. Current Codexless model-free Browser path

The Runtime Bridge Browser executor does not create a genuine Codex turn for semantic Browser calls. It sends a direct App Server MCP request to `node_repl/js` and supplies locally generated correlation metadata:

```text
session_id = toolwire-browser-<uuid>
turn_id    = toolwire-browser-<uuid>-<sequence>
```

No corresponding `turn/start` is admitted. The current execution shape is:

```text
codex.browser_* direct semantic action
    -> App Server mcpServer/tool/call
    -> node_repl/js
    -> synthetic x-codex-turn-metadata
    -> no genuine turn/start
    -> no legitimate matching turn completion
```

## 5. Official current OpenAI Codex source reconciliation

Current official OpenAI Codex source independently confirms the distinction.

`mcpServer/tool/call` is implemented by App Server as an out-of-band direct tool call. The request processor loads the target thread, checks direct-input eligibility, adds thread identity to MCP metadata and calls `CodexThread::call_mcp_tool(...)`:

```text
https://github.com/openai/codex/blob/main/codex-rs/app-server/src/request_processors/mcp_processor.rs
```

`CodexThread::call_mcp_tool(...)` refreshes MCP state and dispatches directly through the MCP runtime's tool-call path. It does not create a Codex generation turn:

```text
https://github.com/openai/codex/blob/main/codex-rs/core/src/codex_thread.rs
```

By contrast, the official App Server `turn/start` contract begins Codex generation, emits `turn/started`, streams turn/item lifecycle notifications and terminates through `turn/completed`. Current upstream turn-start tests likewise wait for `turn/completed` after a real `TurnStart` request:

```text
https://github.com/openai/codex/blob/main/codex-rs/app-server/README.md
https://github.com/openai/codex/blob/main/codex-rs/app-server/tests/suite/v2/turn_start.rs
```

The local Browser-service evidence and official upstream App Server/core evidence therefore agree: direct MCP execution and genuine Codex turn lifecycle are different mechanisms.

## 6. Rejected pseudo-repairs

The investigation rejects all of the following as unsupported lifecycle fabrication or the wrong semantic operation:

```text
manual node_repl turn_ended after a direct Browser call
    REJECTED: would manufacture a turn completion that never occurred

synthetic x-codex-turn-metadata as proof of a real turn
    REJECTED: correlation metadata is not turn ownership

markDeliverable() / markHandoff() as release
    REJECTED: these are turn-end survival classifications

close the user's tab as cleanup
    REJECTED: destructive substitute, not release semantics

runtime/process teardown as release
    REJECTED: no supported exact release receipt

private Browser/backend cleanup calls
    REJECTED: violates the maintained public API boundary
```

These exclusions preserve the `codexless-browser-repair` Skill contract and Research 118's earlier conclusion that direct Browser mutation must not gain a private second cleanup lifecycle merely to make a smoke test pass.

## 7. Genuine-turn route

A genuine Codex turn is the supported lifecycle conceptually, but `turn/start` is a real model turn rather than a model-free tool-only envelope. It consumes model/quota and delegates Browser action selection/execution to the turn. The existing deterministic Runtime Bridge `browser_*` API instead binds exact semantic actions before dispatch.

No supported public API was identified that creates a model-free genuine Browser turn solely to execute one pre-bound direct MCP tool call. Experimental dynamic tools are model-invoked callbacks inside an already-running real turn; they are not an app-client substitute for deterministic out-of-band Browser execution.

A hypothetical hybrid in which Runtime Bridge starts a real turn but independently injects an out-of-band Browser MCP call bearing that turn's identifiers is also not accepted as supported. The direct call is not thereby proven to be causally owned by that turn, and turn-completion races would require semantics not established by the current public contract.

## 8. Accepted boundary

```text
BROWSER_DISCOVERY_AND_INVENTORY
    LIVE_QUALIFIED

MODEL_FREE_EXISTING_TAB_CLAIM
    BLOCKED_BY_REAL_TURN_END_LIFECYCLE_REQUIREMENT

MODEL_FREE_NEW_TAB_LIFECYCLE
    DEFERRED / SAME TURN-END CONTRACT NOT PROVEN

PUBLIC_RELEASE_OR_UNCLAIM_API
    NOT PRESENT IN CURRENT BROWSER BUILD

MANUAL_TURN_ENDED_SIGNAL
    NOT A VALID REPAIR

GENUINE_TURN_BROWSER
    NORMAL UPSTREAM LIFECYCLE EXISTS
    ADS INTEGRATION NOT YET QUALIFIED
```

The current preview.47 preguards are therefore the correct fail-closed behavior for the exact current upstream lifecycle boundary.

## 9. Consequence for file upload

The existing Browser upload implementation remains useful. Its unresolved part is not file selection. `prepare_upload` already binds an authority-bounded local file and exact semantic target, and `browser_upload` already uses the official filechooser/setFiles path. What remains missing is supported Browser ownership and cleanup around the claimed user tab. No PDF-to-ChatGPT Browser upload was performed in this validation.

## 10. Next legitimate experiment

If Browser operation becomes a priority, the next real discriminator is a separately bounded genuine-turn Browser qualification, not a relaxation of the direct-path guard. It should verify one disposable low-risk Browser task through real `turn/start`, observed normal turn completion, proof that a claimed external tab remains open and is no longer controlled afterward, and interruption/failure behavior, with no manual turn-ended fabrication.

Because that route necessarily invokes a Codex model turn and consumes quota, it is a separate explicit experiment rather than part of this model-free diagnosis.

## 11. Preservation

No runtime code change was required or justified by this investigation. Active Runtime Bridge remains:

```text
0.1.1-preview.47-browser-current-plugin-compat-public
codexless-public-preview-v2
172 public tools
```

`codex.browser_status` remains healthy and `codex.browser_tabs` remains live-qualified. Claim-requiring existing-tab actions remain fail-closed before claim.

The Candidate 01 W0 route is unchanged: PKA-G001 through PKA-G008 remain PASS, PKA-G009 through PKA-G017 remain pending, W1 remains not started, PKA-G009 remains next, current continuity remains operational authority, and `authority_switch_allowed=false`.

## 12. Disposition

```text
VALIDATION208=PASS
BROWSER_TURN_END_CLEANUP_MECHANISM=LOCALIZED
DIRECT_MCP_TOOL_CALL_IS_GENUINE_TURN=false
SYNTHETIC_TURN_METADATA_PROVES_OWNERSHIP=false
PUBLIC_EXISTING_TAB_RELEASE_API=ABSENT_CURRENT_BUILD
MANUAL_TURN_ENDED_WORKAROUND=REJECTED
CURRENT_MODEL_FREE_PREGUARD=CORRECT
RUNTIME_MUTATION=NONE
PDF_BROWSER_UPLOAD=NOT_PERFORMED
GENUINE_TURN_BROWSER_QUALIFICATION=DEFERRED_SEPARATE_EXPERIMENT
NEXT_PROJECT_KNOWLEDGE_TASK=PKA_G009
```
