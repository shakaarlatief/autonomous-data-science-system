# Research 110: Durable Bidirectional Codex Thread Handoff and Cooperative Release

**Status:** CORE BIDIRECTIONAL HANDOFF VERIFIED / COOPERATIVE DESKTOP RELEASE INVESTIGATION NEXT  
**Date:** 2026-09-02  
**Opened:** 2026-09-02  
**Scope:** Preserve the post-Research-109 work that activated H6, characterized Desktop catalog and writer ownership more precisely, introduced model-free durable thread binding, verified restart rehydration and same-thread ChatGPT reacquisition, and defines the next supported investigation: a Desktop-side cooperative release path suitable for a future `Proceed in Chat` experience.  
**Authority:** Bounded local-execution and integration research. The public ADS repository remains sole project-development authority. This record does not authorize private Codex database edits, forced writer takeover, or platform-safety evasion.

## 1. Objective

Research 109 established that ADS creates genuine Codex threads, H4 can release completed ChatGPT/Codexless ownership, and exact Desktop deeplinks are a stronger deterministic handoff seam than immediate sidebar registration.

The next goal was bidirectional continuity:

```text
ChatGPT starts/continues a Codex thread
-> ChatGPT releases it
-> Desktop opens and continues the exact same thread
-> Desktop releases it
-> ChatGPT reacquires that exact persisted thread
```

The design target is not simultaneous writers. It is one durable thread identity with cooperative ownership transfer between clients.

## 2. H6 activation and live Desktop handoff

The preflighted H6 candidate was activated. It retained H4 release behavior, removed the falsified `threadSource="user"` override, exposed `threadId`, derived `desktopThreadUrl = codex://threads/<threadId>`, and rendered `Open in Codex Desktop`.

A fresh formal acceptance task completed with marker:

```text
DESKTOP_DEEPLINK_FINAL_TEST_COMPLETE
```

The Rich Card opened the exact persisted thread in Desktop. Desktop then accepted and returned:

```text
DESKTOP_DEEPLINK_FINAL_CONTINUATION_COMPLETE
```

This closed H6 as a live pass.

## 3. Desktop catalog and sidebar findings

Post-H6 work sharpened the distinction between direct thread visibility and durable Desktop catalog adoption.

A deeplink-opened external thread could appear transiently in Desktop `Recent` even while read-only catalog inspection showed no durable `local_thread_catalog` row and no synchronization-watermark advance.

Manual Desktop pinning (`Vastzetten`) triggered broader Desktop-owned reconciliation. The target and other genuine missing threads were imported. Manual unpinning then left the target durable in ordinary `Recent`.

Therefore:

```text
transient Recent visibility != durable local catalog adoption
manual pin can trigger broad Desktop catalog reconciliation
manual unpin can leave a reconciled thread durable in normal Recent
```

The official protocol concept `thread/section/move` was identified conceptually, but no bounded ADS public section-move tool was live-verified. Programmatic pin/unpin remains unresolved and is not required for core same-thread handoff.

## 4. Writer ownership is upstream Codex behavior

The single active writer constraint is enforced by Codex/App Server, not invented by ADS.

Earlier real attempts to resume a thread while Desktop retained writer ownership returned an `already has an active writer` failure.

ADS's contribution is lifecycle hygiene around that upstream constraint: release its own subscription/process when safe, preserve durable thread identity, and reacquire only through supported official thread lifecycle calls.

## 5. Desktop writer-release ladder

A bounded release ladder tested what actually relinquishes Desktop ownership on the current Windows build:

```text
switch away from target thread / go home      NO RELEASE
close Desktop window                          NO RELEASE
fully quit Desktop with Ctrl+Q                RELEASE
```

This means a polished Desktop-to-Chat return path cannot currently assume that navigation or ordinary window closure relinquishes writer ownership.

## 6. Durable identity design

The durable cross-client identifier is:

```text
threadId
```

A Codexless `agentRef` is deliberately ephemeral runtime state.

The accepted design introduced model-free:

```text
codex.agent_bind(threadId, optional cwd)
```

Its contract is:

```text
resolve current ADS authority for cwd
-> official thread/read of persisted thread
-> require persisted thread cwd == authority-resolved cwd
-> create fresh runtime agentRef
-> do not resume thread
-> do not subscribe/take writer
-> do not start model turn
-> recycle bound-only App Server client
```

A later `codex.agent_send` performs the actual `thread/resume` and must fail visibly if another client still owns the writer.

The bind path cannot choose a permission profile. Later send verifies the returned thread/cwd/permission context before starting a turn and fails closed on authority drift.

## 7. Deterministic regression

The private ignored candidate regression passed:

```text
BIDIRECTIONAL_HANDOFF_EXECUTOR_REGRESSION=PASS
BIDIRECTIONAL_HANDOFF_CANDIDATE=PASS
```

Covered cases included non-owning bind, wrong-cwd rejection, duplicate exact bind reuse, active-writer rejection without `turn/start`, successful resume authority binding, and wrong-permission cleanup.

No private Codex database/session/index fabrication was used.

## 8. Publication-layer correction

The first live restart did not publish `codex.agent_bind` because the public surface allowlist still reflected the old tool set. The implementation existed but the registration gate silently excluded it.

A narrow publication fix added the tool to the public and household technical-preview allowlists.

After restart:

```text
Codexless health toolCount   45
raw local MCP tools/list     45
codex.agent_bind             present
```

The ChatGPT developer MCP app was refreshed through the repository-owned `Vernieuwen` procedure. A fresh disposable chat discovered the new action. The canonical already-open chat retained a stale callable snapshot, which is consistent with the runbook's fresh-chat discovery rule.

## 9. Live bind acceptance

A fresh disposable ChatGPT conversation bound persisted target thread:

```text
01a0616f-f3e4-7b10-bb82-267a974c16b3
```

The returned state showed:

```text
same threadId
fresh agentRef
boundThread = true
turnId = null
status = idle
canSend = true
thread/bound
app-server/released
```

No model turn or approval was involved. This is a live pass for non-owning durable binding.

## 10. Rehydration after Codexless restart

Codexless was deliberately restarted, destroying its in-memory runtime-agent map. The same persisted `threadId` was bound again and returned a new fresh `agentRef`.

That proves the intended durability split:

```text
durable across processes: threadId
ephemeral per Codexless runtime: agentRef
```

## 11. Live same-thread reacquisition

After Desktop was fully quit, the newly rebound runtime agent sent a new approved turn with exact requested result:

```text
DURABLE_THREAD_BIND_REACQUIRE_COMPLETE
```

The final agent state remained on the same persisted thread and exposed:

```text
turn/completed
resource-receipt/ready
thread/released / unsubscribed
app-server/released
```

This is the live end-to-end pass:

```text
durable threadId
-> model-free bind
-> fresh ephemeral agentRef
-> Codexless restart
-> same threadId rebound to another fresh agentRef
-> approved agent_send after Desktop release
-> same persisted thread
-> exact result
-> terminal release
```

The bounded event tail did not explicitly expose a `thread/resumed` event or a separately named authority-verification event. Those exact observable events are therefore not claimed. The fail-closed authority checks are additionally covered by deterministic regression.

## 12. Final combined active-writer discriminant

A final live safety discriminator was prepared:

```text
Desktop intentionally owns target thread
-> non-owning codex.agent_bind should still succeed
-> bound agent_send should fail at thread/resume
-> no new turn should start
```

The platform safety layer blocked Step 1 before Codexless execution. Exact result:

```text
Deze toolaanroep is geblokkeerd door de veiligheidscontroles van OpenAI. Controleer nogmaals wat je verzendt.
```

No bind, runtime agent, resume, approval card, Codex turn, retry, wrapper, or workaround occurred.

Correct classification:

```text
COMBINED LIVE DISCRIMINANT = INCOMPLETE
REASON                      = BLOCKED_BY_PLATFORM_SAFETY
```

This is not an implementation FAIL and not a safety PASS. Existing deterministic and earlier live active-writer evidence remain valid within their own scopes.

## 13. What is now achieved

The core user goal is achieved live:

```text
ChatGPT -> exact Codex thread -> Desktop
Desktop -> same exact Codex thread -> ChatGPT after Desktop release
```

The system can recover the durable thread even after a Codexless restart. No transcript copy, replacement thread, private database fabrication, or forced ownership takeover is required.

## 14. Remaining UX problem: cooperative Desktop release

The remaining friction is Desktop-to-ChatGPT release. Today the verified cooperative release primitive is full Desktop quit (`Ctrl+Q`).

The desired professional interaction is conceptually:

```text
Open in Codex Desktop
-> work normally
-> Proceed in Chat
-> Desktop voluntarily releases its writer
-> ChatGPT binds/reacquires the same threadId
```

The next investigation must determine whether current Codex Desktop exposes a supported per-thread release/unsubscribe action or another official lifecycle primitive that Desktop itself can invoke without terminating the whole application.

Important constraint:

```text
client A may release client A's own ownership
client B must not forcibly unsubscribe client A's connection
```

Therefore ChatGPT/Codexless should not attempt to issue a remote unsubscribe on Desktop's behalf, force-kill Desktop, mutate private state, or bypass the upstream single-writer contract.

## 15. Exact next investigation

The next legitimate bounded work is:

```text
1. inspect current repository and accepted Codex/App Server/Desktop lifecycle evidence
2. research supported Desktop-originated release/unsubscribe mechanisms
3. distinguish protocol capability from Desktop-exposed UI/control capability
4. design the smallest non-destructive discriminator
5. prefer read-only/static discovery before any live ownership mutation
6. if a supported Desktop-side release exists, validate it on a harmless test thread
7. only then design a user-facing Proceed in Chat handoff
8. preserve negative evidence if no supported release exists
```

Do not begin this next experiment by modifying Codex private DB/session/catalog state or by routing around platform safety.
