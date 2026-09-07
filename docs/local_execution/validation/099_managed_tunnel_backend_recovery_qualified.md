# Validation 099: Managed Tunnel Backend Recovery Qualified

**Date:** 2026-09-07
**Status:** PASS
**Scope:** Determine whether the official managed tunnel runtime can stay alive while its local MCP target disappears and later recovers, without touching the production tunnel.

## Isolation

The probe used:

```text
exact installed tunnel-client v0.0.13
private-workspace temporary state/profile roots
fake loopback control plane implementing published poll/response routes
dummy runtime-key reference
temporary loopback proxy to the already-running local Codexless MCP
fabricated non-production tunnel id
```

It did not use the production tunnel key/id, mutate remote tunnel state, stop/restart production Codexless, or change the installed runtime.

## Functional sequence

```text
pre-outage initialize                      PASS
pre-outage tools/list                      PASS / 61 tools
remove local MCP path                      DONE
queued tools/list during outage            HTTP-style 502
managed tunnel process after failure       RUNNING
restore same local MCP endpoint            DONE
new initialize through same tunnel         PASS
post-recovery tools/list                   PASS / 61 tools
explicit tunnel reconnect between stages   NO
```

Compact result:

```text
preOutageToolsList=true
outageFailureObserved=true
outageRespCode=502
postRecoveryNewInitialize=true
postRecoveryToolsList=true
tunnelProcessRunning=true
tunnelHealthy=true
tunnelReady=true
sameManagedRuntimeStayedUp=true
beforeToolCount=61
afterToolCount=61
```

Cleanup verification found no isolated managed-runtime alias remaining. The production runtime remained `0.1.1-preview.17-office-file-link` / 61 tools and the production tunnel remained `live` / `ready`.

## Interpretation

This proves functional recovery, not merely process liveness. A normal Codexless restart does not require stopping the managed tunnel first. The future external helper can return/record an accepted operation, restart only Codexless, verify the new local service, and rely on a new MCP initialization through the still-running managed tunnel.

The test also exposed that a previously healthy managed tunnel can continue reporting nominal readiness while the local target is absent. Therefore `/readyz` alone must not be used as the proof of backend recovery in the future maintenance contract.

Private probe source SHA-256 before its next private preservation commit:

```text
422905f509466f56ddf3dc00b8c352a0fe6fa40d30bafcea96718db2854d9995
```
