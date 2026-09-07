# Validation 100: Detached Runtime Helper Survival Qualified

**Date:** 2026-09-07
**Status:** PASS / ISOLATED DETACHED HELPER SURVIVAL; COMMAND_EXEC LAUNCH RESPONSE NOT CLEAN
**Scope:** Qualify durable runtime-maintenance state and prove that a one-shot helper can continue after the invoking wrapper ends/fails, without touching production Codexless or the production tunnel.

## Private candidate

Private head:

```text
22773bb9d39f29f091b06f90f970730e01bd46d9
```

Focused tests:

```text
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
```

New candidate hashes:

```text
file-runtime-maintenance-ledger.mjs
  e272f5de2a4513165f7136a4f9bc5105301f404a2c70f88e2a02b301a360e7f1

detached-runtime-maintenance-launcher.mjs
  4d7b50975ab043f76923f488ef5ee4969904c5e2b179bb1d69cef8589ed24d86

detached-runtime-maintenance-regression.mjs
  a1c5ce78d00a7e3b5a99257e88619c4e493a3edc8da7fd37e7c8bbbe3d811206

detached-helper-dummy-restart.mjs
  30467cf61dae087b0c76b0af2a879f38d5e5adad49232eb10e059d14d441f52f

managed-tunnel-backend-recovery.mjs final preserved hash
  e3707abc0ff49864d8217b92c03300b74effba9f718ab85bb388bcc234881648
```

## Durable ledger properties

The new file-backed ledger demonstrated:

```text
independent-instance readback                 PASS
request id hashed before filesystem naming    PASS
unexpected host-shaped fields rejected        PASS
malformed JSON rejected                       PASS
request id cannot bind to a second operation  PASS
atomic same-directory JSON replacement        IMPLEMENTED
```

## Detached launch contract

The launcher regression demonstrated that the only variable argv value is the opaque operation ID. Executable, supervisor script, working directory, state root and environment remain constructor-owned server configuration. Detached mode, hidden window, ignored stdio and unref are fixed.

## Real dummy-service survival probe

The probe used only a temporary local HTTP service. Generation A was healthy before helper dispatch. The helper was configured to wait, terminate A, start generation B on the same endpoint, wait for B health and write a durable receipt.

The `command_exec` invocation that launched this process tree timed out, so no clean synchronous launch receipt is claimed from that wrapper. A separate later invocation directly observed:

```text
receiptStatus=succeeded
replacementGeneration=B
replacementHealthy=true
replacementProcessAlive=true
```

Cleanup then removed the dummy process/listener/state. Production verification remained:

```text
Codexless ok=true
toolCount=61
production tunnel ready
```

## Interpretation

This is a PASS for the architecture question “can a one-shot helper survive the invoking wrapper and complete/recover state?” It is deliberately not a PASS for “can generic command_exec return cleanly after launching detached work?” The latter timed out and is not the target architecture.

The production semantic runtime-maintenance action must launch the helper directly from Codexless, before stopping anything, and expose durable requestId/operationId status so uncertain transport delivery never causes mutation replay.
