# Completed Codex thread writer handoff verified

**Date:** 2026-09-02  
**Status:** `COMPLETED_THREAD_HANDOFF_VERIFIED / SAME_THREAD_CONTINUATION_PASS`  
**Scope:** Preserve the H3/H4 lifecycle experiments that released ADS ownership of completed formal Codex threads and proved that another Codex client could later continue the same thread.  
**Authority:** Bounded local-execution evidence. This record verifies post-completion handoff on the tested Codex/Codexless build; it does not imply simultaneous multi-client writer support.

## H3 result

Codexless was changed so a terminal formal-agent thread is unsubscribed only after its final result and resource receipt are frozen. Later status reads serve the frozen terminal state and do not resume the thread. An explicit later ADS follow-up may resume it.

Focused regression:

```text
THREAD_RELEASE_REGRESSION=PASS
```

However, `thread/unsubscribe` alone did not immediately remove the external-client writer lock on the tested build.

## H4 result

The formal-agent App Server lifecycle was then changed so, after all known ADS formal-agent threads are terminal, receipt-complete, approval-free and unsubscribed, only the formal-agent App Server process is recycled.

Focused regression:

```text
PROCESS_RELEASE_REGRESSION=PASS
```

A real acceptance turn then produced:

```text
turn completed             PASS
resource-receipt/ready     PASS
thread/released            PASS / unsubscribed
app-server/released        PASS
post-release status read   PASS / no reclaim
```

The user subsequently continued the released thread from the Codex IDE surface. Read-only persistence inspection confirmed the follow-up advanced the same underlying thread identity rather than creating a replacement conversation.

## Classification

```text
ADS formal turn completion                  PASS
terminal result/usage preservation          PASS
thread subscription release                 PASS
formal-agent process release                PASS
external-client writer handoff              PASS
same-thread later continuation              PASS
read-only ADS status does not reclaim       PASS
simultaneous multi-client writing           NOT CLAIMED
```

This is the accepted live handoff behavior before H6.

Detailed synthesis: `docs/research/109_codex_desktop_thread_handoff_and_catalog_reconciliation.md`.
