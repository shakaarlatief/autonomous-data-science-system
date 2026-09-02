# Checkpoint 273: Durable Bidirectional Codex Thread Handoff Verified, Cooperative Release Next

**Date:** 2026-09-02
**Status:** Verified infrastructure/continuity checkpoint; cooperative Desktop release investigation remains open
**Checkpoint class:** INFRASTRUCTURE
**Project stage:** Post-Checkpoint-272 Codex thread-handoff integration; H6 live, durable bind/restart rehydration/same-thread reacquisition verified, Desktop cooperative release UX next
**Scope:** Records the live H6 acceptance, refined Desktop catalog and writer-ownership behavior, the model-free durable `codex.agent_bind` design and publication fix, restart rehydration to a fresh runtime `agentRef`, same-thread ChatGPT reacquisition after Desktop release, and the final combined active-writer live discriminator being blocked by platform safety before Codexless execution.
**Authority:** Historical verification and continuity provenance. Research 110 and Validations 027-030 govern detailed evidence. Current continuation is governed by `docs/CURRENT_STATE.md` and `docs/current_routing.json`. The combined active-writer live discriminator remains incomplete and must not be reported as PASS or FAIL.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-15`
**Conversation title:** `15 - Codex Desktop Thread Handoff and Source Vault Continuation`
**Primary collaborator:** ChatGPT
**Branch:** `v1-source-vault-bootstrap-resume`

## Meaningful state transition

Checkpoint 272 froze H4 writer/process release and an H6 Desktop-deeplink candidate before activation.

This checkpoint closes that prepared H6 gate and advances the integration architecture to a durable bidirectional same-thread model.

The central result is:

```text
ChatGPT -> same persisted Codex thread -> Desktop     PASS
Desktop -> same persisted Codex thread -> ChatGPT     PASS after Desktop releases writer
Codexless restart -> same threadId -> fresh agentRef  PASS
```

No transcript-copy handoff, replacement conversation, private Codex database fabrication, or forced writer takeover is required.

## H6 became live

The H6 candidate was activated and a fresh acceptance task returned:

```text
DESKTOP_DEEPLINK_FINAL_TEST_COMPLETE
```

The completed task exposed the exact persisted `threadId` and `codex://threads/<threadId>` handoff. The Rich Card's `Open in Codex Desktop` opened the exact thread, and Desktop continued it with:

```text
DESKTOP_DEEPLINK_FINAL_CONTINUATION_COMPLETE
```

H4 `thread/released` and `app-server/released` terminal behavior remained intact.

## Desktop catalog behavior was refined

A deeplink-opened external thread may appear transiently in Desktop `Recent` without a durable `local_thread_catalog` row or catalog synchronization advance.

Manual pinning (`Vastzetten`) triggered broad Desktop-owned reconciliation. Unpinning afterward left the reconciled target durable in ordinary `Recent`.

This proves that transient UI appearance and persistent Desktop catalog adoption are separate states.

The protocol concept `thread/section/move` was identified, but no bounded ADS programmatic section-move route was accepted or live-verified.

## Desktop writer-release ladder

The tested Windows Desktop build retained writer ownership across:

```text
switch away / home / New Chat navigation   NO RELEASE
close Desktop window                        NO RELEASE
full Desktop quit with Ctrl+Q               RELEASE
```

After full quit, ChatGPT could reacquire and continue the exact same persisted thread.

## Durable `threadId` bind architecture

The accepted model treats:

```text
threadId   durable cross-client identity
agentRef   ephemeral Codexless runtime handle
```

The new `codex.agent_bind` is model-free and non-owning. It reads the persisted thread under current authority, verifies cwd identity, creates a fresh runtime agent handle, does not resume or subscribe to the thread, does not start a turn, and releases its bound-only App Server client.

A later `agent_send` performs actual resume/reacquisition and carries the authority fail-closed checks.

Deterministic regression passed for non-owning bind, wrong-cwd rejection, duplicate binding, active-writer rejection/no turn start, successful authority binding, and wrong-permission cleanup.

## Publication-layer fix

The implementation initially failed to appear publicly because the tool allowlists still reflected the old surface. The public and household technical-preview allowlists were updated to publish `codex.agent_bind`.

After controlled restart and app refresh:

```text
Codexless public toolCount  45
raw MCP tools/list          45
codex.agent_bind            discovered in fresh ChatGPT conversation
```

The canonical already-open chat retained a stale tool snapshot, so live acceptance correctly used a fresh disposable conversation.

## Restart rehydration and same-thread reacquisition

A first live `codex.agent_bind` on persisted thread:

```text
01a0616f-f3e4-7b10-bb82-267a974c16b3
```

returned a fresh idle/sendable bound agent with no turn.

Codexless was then deliberately restarted, erasing its in-memory runtime map. Binding the same `threadId` again returned a different fresh `agentRef` while preserving the exact thread identity.

After Codex Desktop was fully quit, an approved send on that rebound agent completed on the same persisted thread with exact result:

```text
DURABLE_THREAD_BIND_REACQUIRE_COMPLETE
```

The terminal event tail showed completion, resource receipt, `thread/released`/unsubscribed, and `app-server/released`.

The bounded returned tail did not explicitly expose a `thread/resumed` event or a separately named authority-verification event. Those exact event claims are not made. The authority fail-closed behavior is additionally covered by deterministic regression.

## Final combined safety discriminator remained incomplete

The final planned test intentionally left Desktop as active writer, then attempted:

```text
codex.agent_bind
-> codex.agent_send
-> expected official active-writer rejection before any new turn
```

The platform safety layer blocked Step 1 before Codexless executed it.

Therefore:

```text
combined live discriminator   INCOMPLETE
classification                BLOCKED_BY_PLATFORM_SAFETY
implementation FAIL           NOT ESTABLISHED
safety PASS                   NOT ESTABLISHED
retry/evasion                 NOT ATTEMPTED
```

Earlier real `thread/resume` active-writer rejection evidence and the deterministic new-bind regression remain valid within their scopes.

## Current UX boundary

The core handoff capability is achieved. The remaining usability friction is how Desktop voluntarily relinquishes writer ownership without requiring full application quit.

The desired future UX is:

```text
[ Open in Codex Desktop ]
-> Desktop works on same thread
-> [ Proceed in Chat ]
-> Desktop voluntarily releases its own writer
-> ChatGPT binds/reacquires same threadId
```

This is a cooperative ownership-transfer problem, not a reason to remove or bypass Codex's upstream single-writer invariant.

## Exact continuation

The next bounded integration investigation is to determine whether current Codex Desktop exposes a supported per-thread release/unsubscribe mechanism, or another official Desktop-originated lifecycle action, that can release its own writer without terminating the whole application.

Constraints:

```text
no private Codex DB/session/catalog writes
no forced process termination as product UX
no cross-client forced unsubscribe
no platform-safety workaround
read-only/static discovery first
smallest supported live discriminator only after discovery
```

After this integration question is deliberately closed, the unchanged substantive ADS route remains Source Vault reviewed ingestion of the frozen 20-entry corpus.

## Durable evidence route

```text
docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md
docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md
docs/local_execution/validation/027_codex_desktop_deeplink_handoff_live_verified.md
docs/local_execution/validation/028_codex_desktop_catalog_writer_ownership_followup.md
docs/local_execution/validation/029_durable_thread_bind_restart_reacquisition_verified.md
docs/local_execution/validation/030_bound_active_writer_combined_live_test_blocked_by_platform_safety.md
```
