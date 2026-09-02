# Durable Codex thread bind, restart rehydration, and same-thread reacquisition verified

**Date:** 2026-09-02  
**Status:** `DURABLE_THREAD_BIND_RESTART_REACQUISITION_PASS`  
**Scope:** Preserve the live acceptance of model-free durable `threadId` binding, fresh runtime-agent rehydration after Codexless restart, and a later approved same-thread Codex continuation after Desktop released the writer.  
**Authority:** Bounded local-execution evidence for the tested Codexless implementation. It verifies the public behavior observed live and keeps unobserved internal event claims out of scope.

## Accepted design

The durable cross-client identity is the Codex `threadId`, not a Codexless runtime `agentRef`.

The public `codex.agent_bind` operation is model-free and non-owning. It uses official `thread/read` under currently resolved ADS authority, requires the persisted thread cwd to match the resolved cwd, creates a fresh runtime `agentRef`, and does not call `thread/resume` or start a model turn. A later `codex.agent_send` performs actual reacquisition.

Focused deterministic regression covered:

```text
non-owning bind                               PASS
wrong-cwd rejection                          PASS
duplicate exact bind reuse in one runtime    PASS
active-writer resume rejection               PASS
no turn/start after rejected resume           PASS
successful resume authority binding          PASS
wrong permission-profile fail-closed cleanup PASS
```

## Publication and discovery

The new tool initially existed in implementation but was absent from the public surface because the public/household allowlists had not been updated. The publication-layer fix added `codex.agent_bind` to the accepted technical-preview allowlists.

After controlled Codexless/tunnel restart and ChatGPT developer-app refresh:

```text
Codexless health toolCount    45
raw local MCP tools/list      45
codex.agent_bind present      PASS
fresh ChatGPT discovery       PASS
```

The already-open canonical chat retained a stale callable-tool snapshot, so live acceptance was performed in a fresh disposable ChatGPT conversation as required by the operations runbook.

## First live bind

Binding persisted thread:

```text
01a0616f-f3e4-7b10-bb82-267a974c16b3
```

produced a fresh runtime agent with:

```text
same threadId          PASS
boundThread            true
turnId                 null
status                 idle
canSend                true
no model turn          PASS
thread/bound event     PASS
app-server/released    PASS
```

## Rebind after Codexless restart

Codexless was deliberately restarted so its in-memory agent state was lost. Binding the same durable thread again returned a different fresh `agentRef` while preserving the exact `threadId` and the same non-owning idle state.

Therefore:

```text
within one Codexless lifetime:
threadId -> runtime agentRef

across Codexless lifetimes:
same durable threadId -> new fresh runtime agentRef
```

## Same-thread reacquisition after Desktop full quit

Codex Desktop was fully quit, satisfying the empirically verified release condition. An approved `codex.agent_send` on the newly rebound runtime agent requested exact marker:

```text
DURABLE_THREAD_BIND_REACQUIRE_COMPLETE
```

The turn completed on the same persisted thread and returned that exact marker.

The bounded final state exposed:

```text
threadId             same persisted thread
finalResult          DURABLE_THREAD_BIND_REACQUIRE_COMPLETE
status               idle
canSend              true
latestError          null
turn/completed       observed
resource receipt     observed
thread/released      observed / unsubscribed
app-server/released  observed
```

The task card showed the ADS repository cwd and `ads-direct-git` permission profile.

## Claim-scope caveat

The returned bounded event tail did not explicitly expose a `thread/resumed` event or a separately named authority-verification event. Therefore this validation does not claim those exact observable events occurred.

What is live-observed is that the approved send completed on the same persisted thread under the task card's ADS cwd/profile with no authority error. The fail-closed authority checks before `turn/start` are additionally covered by deterministic regression.

## Classification

```text
model-free durable bind                     PASS
bind does not start a turn                  PASS
bind survives as durable thread identity    PASS
restart -> new agentRef / same threadId      PASS
same-thread approved reacquisition           PASS
exact marker                                 PASS
terminal H4 release retained                 PASS
explicit thread/resumed event observed       NOT CLAIMED
explicit authority-verification event        NOT CLAIMED
```

Detailed synthesis: `docs/research/110_durable_bidirectional_codex_thread_handoff_and_cooperative_release.md`.
