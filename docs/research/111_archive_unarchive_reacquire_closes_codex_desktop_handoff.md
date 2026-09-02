# Research 111: Archive-Unarchive Reacquisition Closes the Codex Desktop Handoff Boundary

**Status:** END-TO-END ARCHIVE / UNARCHIVE / BIND / RESUME VERIFIED; CODEX HANDOFF INTEGRATION CLOSED FOR CURRENT SCOPE
**Date:** 2026-09-02
**Opened:** 2026-09-02
**Scope:** Preserve the supported cooperative release result that followed Research 110: a disposable ADS-root thread was archived in the running Desktop UI, unarchived through a newly published model-free official lifecycle tool, rebound to a fresh runtime agent, and resumed after normal approval on the same persisted thread.
**Authority:** Bounded infrastructure and continuity research. Validation 031 governs the exact live evidence. The public ADS repository remains sole project-development authority.

## 1. Question closed

Research 110 left one UX question open:

```text
Can Codex Desktop voluntarily make a thread available for same-thread ChatGPT
reacquisition through a supported action while Desktop itself remains running?
```

The completed live result answers that bounded question affirmatively through Desktop's supported archive action and the official unarchive lifecycle.

## 2. Supported lifecycle surface

A new model-free public tool was published:

```text
codex.thread_unarchive
```

Its implementation uses official Codex lifecycle calls:

```text
thread/read
thread/unarchive
```

It does not start a model turn. After controlled restart, live Codexless health reported `toolCount 46` and the secure tunnel reported ready with HTTP 200.

## 3. Exact live result

Disposable ADS-root thread:

```text
01a060d7-7249-78b2-b4a0-61cc4376da4f
```

The thread was continued in Codex Desktop. While Desktop remained running, it was archived through the supported Desktop UI.

The model-free unarchive path succeeded, followed by a model-free bind of the same durable thread to fresh runtime handle:

```text
agent_7d5d070f-24c0-470b-9164-2ca7db2623a4
```

After normal metered user approval, the bound agent resumed the same persisted thread. Turn:

```text
01a0628f-8415-77d3-9a8d-2ab29f204c53
```

completed with exact result:

```text
ARCHIVE_UNARCHIVE_REACQUIRE_COMPLETE
```

## 4. Accepted classification

```text
UNARCHIVE_PATH                         PASS
POST_UNARCHIVE_BIND                    PASS
ARCHIVE_RELEASES_DESKTOP_WRITER        PASS
Archive -> Unarchive -> Bind -> Resume PASS
```

The writer classification is operationally scoped. The observable sequence proves that the Desktop-originated archive was followed by successful official unarchive, fresh bind, and resume while Desktop remained running. No instrumentation observed the precise internal instant at which writer ownership was relinquished, so no such instant is asserted.

## 5. Safety properties retained

The result required no private Codex DB/session/catalog mutation, forced process termination, Desktop quit, permission widening, cross-client forced unsubscribe, or platform-safety workaround.

The final send retained the ordinary visible metered approval boundary. Model-free unarchive and bind did not become hidden model-execution routes.

## 6. Architectural meaning

The verified cooperative flow is now:

```text
ChatGPT / Codexless creates or reacquires durable threadId
-> Desktop continues exact thread
-> Desktop archives exact thread through supported UI
-> official model-free thread_unarchive restores archived thread
-> model-free agent_bind creates fresh ephemeral agentRef
-> approved agent_send resumes exact thread
```

This preserves the durable/ephemeral distinction established by Research 110:

```text
threadId   durable cross-client identity
agentRef   ephemeral runtime handle
```

It also replaces full Desktop quit as the only verified operational route for returning the tested thread to ChatGPT/Codexless.

## 7. Current scope closure

The Codex Desktop handoff integration is closed for current ADS scope. This does not claim that archive is a universal product-level ownership-transfer primitive for every Codex client, version, or lifecycle state. It records the exact supported Windows Desktop and Codexless sequence that completed successfully here.

No further Codex handoff experiment is active. The project returns to its substantive boundary:

```text
reviewed Source Vault ingestion of the frozen 20-entry first corpus
```

The existing working-store audit, encrypted backup, clean restore, and restored-audit gates remain unchanged and follow ingestion under the permanent vault procedure.
