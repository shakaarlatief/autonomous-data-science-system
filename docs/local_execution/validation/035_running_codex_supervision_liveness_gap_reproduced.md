# Running Codex supervision liveness gap reproduced

**Date:** 2026-09-03
**Status:** `REPRODUCED / ARCHITECTURE GAP`
**Scope:** Preserve a concrete reproduction where a Codexless-owned running Codex turn reached a later approval after the calling ChatGPT assistant turn had ended, leaving the Codex turn blocked until the user sent another message. Also records the related need to study live writer-ownership transfer/reacquisition while a turn is active.
**Authority:** Local integration/liveness evidence. This proves the observed host behavior in the tested ChatGPT + Codexless workflow; it does not by itself prove that no future ChatGPT or Codex App mechanism can provide background wakeups or live ownership transfer.
**Declared references:** `research:116`, `checkpoint:277`, `path:docs/local_execution/validation/034_chatgpt_tool_projection_refresh_and_connector_coexistence_observations.md`, `path:docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`, `path:docs/research/112_guided_proceed_in_chat_shared_ready_and_repeatable_roundtrip.md`

## Reproduction

A formal Research 116 Codex task was started from canonical interaction `chatgpt-16` and mounted in the live Rich Task Card.

The first later in-turn command approval concerned a bounded disposable `%TEMP%` staging test with guarded recursive cleanup. The user noticed the card's `Action required` state and explicitly asked about it because no approval control appeared in Codex Desktop. ChatGPT inspected the agent, explained that Codexless/ChatGPT still owned the writer, and obtained explicit approval.

After approval request `0` was resolved, Codex resumed, discovered a harmless temporary test-layout/import mistake, corrected the staging command, and then reached a second approval request for the corrected disposable staging command.

Exact later state observed only after the user sent another ChatGPT message:

```text
status: awaitingApproval
pendingApproval.requestId: 1
method: item/commandExecution/requestApproval
```

The second request had been pending since shortly after the first approval. ChatGPT had not autonomously resumed to inspect it because the prior assistant turn had already ended.

## Important distinction

The Rich Task Card can update independently enough for the user to notice `Action required`, but the calling ChatGPT assistant does not currently receive an autonomous wakeup that causes another reasoning/tool turn after its previous response has ended.

Observed effective flow:

```text
ChatGPT starts/supervises Codex
    -> assistant response ends
    -> Codex keeps running
    -> Codex reaches approval/error/completion
    -> Rich Card may reflect the new state
    -> ChatGPT itself does not automatically execute agent_show/approve/follow-up
    -> Codex can remain blocked until the user sends another message
```

This creates a liveness gap between the **intended** Call Profile supervision policy and the actual host scheduling/wakeup model.

## Why this matters

The Call Profile says the calling AI should remain responsible for running Codex work and revisit it often enough that approvals/errors do not sit unattended. A profile instruction can guide the assistant while it is executing, but it cannot itself schedule a future assistant turn after the current response has ended.

Without another mechanism, a task can therefore wait for:

```text
minutes
hours
or indefinitely
```

if the user does not happen to notice the Rich Card state and send a message.

This is not acceptable as the long-term supervision model for professional long-running ADS work.

## Related writer-ownership issue

During the same reproduction, Codex Desktop showed the thread but indicated that it was opened/owned in another app. Desktop therefore did not present the pending approval UI for the Codexless-owned active turn.

The project owner explicitly wants the architecture to investigate not only passive live viewing, but also whether writer authority can be cooperatively transferred or reacquired **during a running turn**, rather than only through the currently validated idle archive/unarchive/rebind handoff.

Research questions now include:

```text
Can a running Codexless-owned turn publish a durable host notification/wakeup that causes ChatGPT to resume supervision?
Can an MCP App action or other ChatGPT mechanism create a genuine follow-up assistant execution without user prompting?
Can Codexless itself safely auto-handle only profile-approved low-risk approvals server-side while leaving ambiguous/high-risk actions for the user?
Can an external supervisor/daemon monitor task state and notify the user or ChatGPT when approval is needed?
Can writer ownership be cooperatively transferred to Codex Desktop while the turn is active without interrupting/replaying work?
If active transfer is unsupported, can the running turn be safely interrupted/released and resumed under Desktop with exact continuity guarantees?
Can the companion Rich Task Card expose a prominent actionable approval surface even when Desktop is non-owning?
What are the official App Server semantics around approval routing, subscriptions, active writer ownership, turn interruption, and same-turn steering that constrain these options?
```

## Current bounded conclusion

```text
live card state update                         WORKS
Codex continues after assistant response ends  WORKS
ChatGPT autonomous follow-up supervision        NOT OBSERVED / GAP
approval can remain pending silently to AI      REPRODUCED
Desktop approval while non-owning               NOT AVAILABLE IN TESTED STATE
idle cooperative handoff                        PREVIOUSLY VERIFIED
active-turn writer transfer                     OPEN RESEARCH QUESTION
```

## Immediate handling rule

Until a better mechanism is implemented, do not assume that mounting a running Rich Task Card means ChatGPT will automatically return when the task later needs attention.

For important long-running tasks, either:

```text
keep the current assistant turn actively checking while tools permit,
use deliberately bounded Codex work units,
or warn that later approvals may require user re-entry.
```

This is a temporary operational mitigation, not the desired final architecture.

## Research routing

This finding belongs to the broader Codex/Codexless upstream research and should be compared against:

```text
App Server subscription/status semantics
approval reviewer/auto_review
turn/steer
turn/interrupt
thread ownership constraints
Desktop/App multi-client behavior
possible ChatGPT MCP App notification/wakeup capabilities
external task-supervisor/automation possibilities
```

It should be included in the eventual repository-wide Codexless coherence/reconciliation audit and must not be lost when Chat 17 opens.
