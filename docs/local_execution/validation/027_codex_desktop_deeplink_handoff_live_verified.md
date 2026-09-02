# Codex Desktop deeplink handoff live verified

**Date:** 2026-09-02
**Status:** `H6_LIVE_ACCEPTANCE_PASS`
**Scope:** Preserve the live H6 activation and acceptance proving that a completed ADS formal Codex task exposes the exact persisted thread identity and an `Open in Codex Desktop` handoff that continues the same thread.
**Authority:** Bounded local-execution/UI integration evidence. It verifies exact-thread handoff on the tested Codex/Codexless build and does not imply automatic Desktop sidebar registration.

## Live result

The preflighted H6 candidate was activated through the fail-closed local procedure. The activated implementation retained H4 terminal release behavior, removed the falsified `threadSource="user"` override, exposed the public `threadId`, derived `desktopThreadUrl = codex://threads/<threadId>`, and rendered `Open in Codex Desktop` on the task card.

A fresh formal Codex acceptance task completed with exact marker:

```text
DESKTOP_DEEPLINK_FINAL_TEST_COMPLETE
```

Observed acceptance evidence:

```text
formal Codex task completed                 PASS
public threadId exposed                     PASS
desktopThreadUrl exposed                    PASS
Rich Card Open in Codex Desktop             PASS
thread/released after terminal completion   PASS
app-server/released                         PASS
```

The user opened the exact thread from the Rich Card in Codex Desktop and sent:

```text
DESKTOP_DEEPLINK_FINAL_CONTINUATION_COMPLETE
```

Desktop returned that exact marker in the same visible conversation. The composer was writable and no ownership-lock banner remained.

## Classification

```text
H6 activation                                  PASS
ChatGPT -> Desktop exact-thread handoff         PASS
same-thread Desktop continuation                PASS
H4 terminal release retained                    PASS
immediate persistent Desktop Recent adoption    NOT REQUIRED / NOT CLAIMED
```

Detailed continuation research is preserved in `docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md`.
