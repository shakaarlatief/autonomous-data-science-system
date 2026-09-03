# Research 112: Guided Proceed in Chat Shared Ready State and Repeatable Round Trip

**Status:** GUIDED PROCEED IN CHAT END TO END AND REPEATED SAME-THREAD ROUND TRIP VERIFIED
**Date:** 2026-09-02
**Opened:** 2026-09-02
**Scope:** Preserves the completed Rich Task Card guided handoff, runtime-lifetime shared Ready resolution across a separate stateless MCP request, ordinary metered continuation, a second visible Desktop/Chat cycle on the same persisted thread, and the bounded Desktop presentation-cache finding.
**Authority:** Bounded infrastructure and continuity research. Validation 032 governs the exact live observations. The public ADS repository remains sole project-development authority.

## 1. Question closed

Research 111 established the supported lifecycle beneath cooperative release. The remaining UX/integration question was whether the Rich Task Card could guide a user through that lifecycle, expose a model-free Ready state to a later independent MCP request, and resume repeatably on the same durable thread without weakening the execution boundary.

The completed evidence answers that question affirmatively for the tested scope.

## 2. Live environment and identity

```text
Codexless public version  0.1.1-preview.7
toolCount                 48
tunnel                    ready / HTTP 200
threadId                  01a063b1-0d21-7011-b17c-514eb0359a15
taskRef                   task_e89b4b3c-0e43-40a2-b3d3-aa32a9fe31e7
```

The first source turn in Chat returned exact marker `PROCEED_IN_CHAT_UI_SOURCE_COMPLETE`.

## 3. Guided card path

The user opened the exact persisted thread in Codex Desktop and selected `Proceed in Chat`. Desktop stayed running while the exact thread was archived through the supported UI. The user then selected `I've archived it — Continue` on the card.

The card reached `Ready in Chat` after model-free verification, official unarchive, and rebound. No model turn had started at Ready.

This preserves the intended authority split:

```text
supported Desktop archive         voluntary writer release
verification / unarchive / bind   model-free lifecycle work
Ready resolution                  model-free status lookup
agent_send                        ordinary metered model turn
```

## 4. Runtime-shared Ready result

A separate stateless MCP request invoked `codex.agent_handoff_resolve` for the exact `taskRef` and returned:

```text
agentRef          agent_645095a6-efa5-4224-a8c1-029da74abea7
threadId          01a063b1-0d21-7011-b17c-514eb0359a15
boundThread       true
status            idle
canSend           true
turnId            null
pendingApproval   null
modelTurnStarted  false
handoffStatus     ready
```

The architectural discriminator is not merely that Ready appeared on the initiating card. A distinct stateless request resolved the same Ready record after guided handoff state moved into the runtime-lifetime shared `agentPreviewState`.

Accepted scope:

```text
shared across distinct MCP requests in one runtime lifetime  VERIFIED
persistent across Codexless process restart                  NOT CLAIMED / intentionally absent
```

## 5. Ordinary continuation result

An ordinary metered `codex.agent_send` resumed the exact persisted thread. Turn `01a063b5-c8d9-7692-b8b1-d23a0a55a7ea` completed with:

```text
PROCEED_IN_CHAT_END_TO_END_COMPLETE
```

The exact `threadId` was unchanged before and after. The observed event sequence included:

```text
thread/reacquired
turn/accepted
turn/started
turn/completed
thread/released
app-server/released
```

This confirms that the model-free Ready path did not itself start a turn and that the later ordinary send exercised the normal metered continuation lifecycle.

## 6. Repeatability discriminator

A second cycle used the same durable persisted thread rather than a replacement thread:

```text
Desktop source      SECOND_DESKTOP_CYCLE_SOURCE
Chat continuation   SECOND_CHAT_CYCLE_COMPLETE
```

The same Desktop conversation visibly showed this ordered history:

```text
PROCEED_IN_CHAT_UI_SOURCE_COMPLETE
PROCEED_IN_CHAT_END_TO_END_COMPLETE
SECOND_DESKTOP_CYCLE_SOURCE
SECOND_CHAT_CYCLE_COMPLETE
```

This rules out the narrow interpretation that the first success was only a one-time recovery trick. For the tested runtime and clients, cooperative handoff was repeatable on one durable thread.

## 7. Desktop cache/synchronization finding

Codex Desktop initially retained stale archived presentation state after Chat had already unarchived and reacquired the thread. The visible `Dearchiveren en openen` action failed. Restarting Codex Desktop and opening the exact `codex://threads/<threadId>` deep link recovered the correct same-thread presentation with both Chat turns visible.

The evidence supports this bounded classification:

```text
backend handoff failure             NO
durable thread identity failure     NO
Desktop UI synchronization/cache    OBSERVED QUIRK
```

The restart was presentation recovery after the handoff, not forced termination used to obtain writer ownership.

## 8. Safety and architectural conclusion

The guided flow retained the previously accepted safety boundary:

```text
no forced writer stealing
no private Codex DB/session/catalog writes
no Desktop forced termination for handoff
no permission widening
no manual raw lifecycle workaround
```

Desktop voluntarily releases by archive. Chat verifies, unarchives, rebinds model-free, and resolves the runtime-shared Ready record. Only an ordinary metered send begins the continuation turn.

The guided `Proceed in Chat` UX and integration are closed for current ADS scope. No new handoff experiment is active. The substantive project route remains reviewed Source Vault ingestion.

## 9. Publication boundary and interruption residue

Checkpoint 274 exists locally at commit `c0b9101` but is not known to be pushed. The direct sandboxed push failed at the configured credential-manager / VS Code askpass boundary, and no authority workaround is permitted.

The Checkpoint 275 preservation set remained uncommitted for a separate reason: its originating reconciliation turn had not cleanly completed. Validation created repository-local `.tmp/pytest-checkpoint-275/` state, after which Codex requested an exact-path-guarded cleanup whose mutation was `Remove-Item -Recurse -Force`. The user approved that pending action, but the outer OpenAI tool-dispatch safety layer blocked the programmatic approval before Codexless received it; the request type did not offer decline as an alternative. The turn remained paused before cleanup and final status verification.

No deletion occurred through the blocked action. A later `git status` warning that `.tmp/pytest-checkpoint-275/` cannot be opened is therefore known interruption residue from this exact sequence. The repository was intentionally not committed or pushed as though the reconciliation had completed.

This event is also the causal origin of the subsequent early-Desktop/live-viewer work: the first proposed recovery was to let the user open the still-running persisted Codex thread in Desktop and service the approval natively. That exposed the missing early `Open in Codex Desktop` control, which then led to the cross-client live-synchronization investigation and companion viewer work. UI work did not precede or independently justify withholding the Checkpoint 275 commit.

