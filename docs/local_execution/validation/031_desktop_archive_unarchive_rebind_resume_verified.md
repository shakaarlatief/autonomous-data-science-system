# Desktop archive, unarchive, rebind, and resume verified

**Date:** 2026-09-02
**Status:** `PASS / CODEX_HANDOFF_INTEGRATION_CLOSED_FOR_CURRENT_SCOPE`
**Scope:** Preserve the completed live cooperative Codex Desktop handoff discriminator on a disposable ADS-root thread: Desktop-originated archive while Desktop remained running, official model-free unarchive, fresh model-free bind, and normally approved same-thread resume to an exact terminal result.
**Authority:** Bounded live integration evidence. This record proves the observed end-to-end sequence and its returned identities/results. It does not identify an unobserved internal instant at which the Codex writer lease was released.

## Live target and sequence

Disposable ADS-root thread:

```text
01a060d7-7249-78b2-b4a0-61cc4376da4f
```

The thread was continued in Codex Desktop and then archived through the supported Desktop UI while Codex Desktop remained running.

The newly published model-free surface then performed the official lifecycle sequence:

```text
codex.thread_unarchive
    official thread/read + thread/unarchive
    no model turn

codex.agent_bind
    same durable threadId
    fresh agentRef agent_7d5d070f-24c0-470b-9164-2ca7db2623a4
    no model turn

codex.agent_send
    normal metered user approval
    same persisted thread resumed
    turn 01a0628f-8415-77d3-9a8d-2ab29f204c53
    exact result ARCHIVE_UNARCHIVE_REACQUIRE_COMPLETE
```

## Operational classifications

```text
UNARCHIVE_PATH                         PASS
POST_UNARCHIVE_BIND                    PASS
ARCHIVE_RELEASES_DESKTOP_WRITER        PASS
end-to-end Archive -> Unarchive
    -> Bind -> Resume                  PASS
```

`ARCHIVE_RELEASES_DESKTOP_WRITER=PASS` is scoped to the operational outcome: after the Desktop-originated archive, the supported unarchive/bind/resume sequence succeeded without quitting Desktop. It does not claim telemetry for the precise internal instant or mechanism by which the writer lease became available.

## Runtime and publication evidence

The new tool was published through official `thread/read` plus `thread/unarchive` and required no model selection or model turn.

After the controlled Codexless restart, live health reported:

```text
toolCount     46
tunnel        ready / HTTP 200
```

Codex Desktop remained running throughout the archive-to-resume handoff.

## Safety and authority boundary

The live result used none of the following:

```text
private Codex DB/session/catalog write
forced process termination
Codex Desktop quit
permission widening
cross-client forced unsubscribe
platform-safety workaround
```

The resume required the normal metered user approval. The result therefore preserves the existing authority and consent boundary rather than creating an unmetered execution route.

## Conclusion

The supported sequence is verified end to end:

```text
Desktop archive
-> official model-free unarchive
-> model-free fresh bind
-> normally approved resume
-> exact same-thread terminal result
```

This closes the Codex Desktop handoff integration for the current scope. The active ADS boundary returns to reviewed Source Vault ingestion of the frozen 20-entry first corpus.
