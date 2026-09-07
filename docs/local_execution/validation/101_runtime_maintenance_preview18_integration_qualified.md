# Validation 101: Runtime Maintenance Preview.18 Integration Qualified

**Date:** 2026-09-07
**Status:** PASS / PRODUCTION-SHAPED RESTART CHAIN + 62-TOOL PRIVATE INTEGRATION QUALIFIED / NO LIVE MUTATION
**Research:** Research 122
**Scope:** Qualify exact runtime identity, direct pre-restart semantic dispatch, detached one-shot graceful restart, durable status/idempotency, and the preview.18 public integration candidate without touching the production Codexless process or tunnel.

## 1. Durable private boundary

Private runtime repository:

```text
head      610fb6c1480012b0db80965239493348e5de5a58
upstream  610fb6c1480012b0db80965239493348e5de5a58
status    clean
push      RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

Key current hashes:

```text
file-runtime-maintenance-ledger.mjs        6fe0ef542d7377febca738df2e98238e91ecd52d3cc863cc4ca7b2d8b59d1a50
detached-runtime-maintenance-launcher.mjs  daef87a56946da819a0bd290733dd6553d3656a8cf64bb960827a7a0d935bb80
fixed-runtime-worker-launcher.mjs           18800411d2b5fc64e84fe566731d16c98c0490b7b8907970e5b0d3fa4479601c
runtime-instance-contract.mjs               bf7e7366ede0f2298aad4a4f062b593772ab3092cff227aa606131be2d18983a
runtime-maintenance-service.mjs              dc3b9666b1f95d7f40d58bb7e88645767d803d08ea6cc7f29f20746d7f0028b8
codexless-one-shot-supervisor.mjs            63649587bca0158d0bc942860ff9c1d5bed519ce359225022e0b41f98dc08595
runtime-maintenance-supervisor.mjs           0ec3916ab6d37d3e0ae27dd94aee2a4a6cf520cc60cbb9850a78f1a281dd2725
detached-runtime-maintenance-regression.mjs  ecef0799651a8f03ac9b7a2760af93caf8014625cc6d2d75f0ab8bfa2d006212
one-shot-runtime-maintenance-regression.mjs  dcbd3821189789bb9d526204c83efbe9acbc3a32974cb77232346be31a5ceac1
direct-dispatch-one-shot-functional.mjs      be8fca6a06240d1dead3e12e093df46c545f41ca2bbcf7912a049e0e1d2a835e
http-runtime-maintenance-entrypoint-functional.mjs
                                            f0cacc471e0588b6c0e1cbb7fc8b1cd2ae5665e559a4efa074b82678afb17f54
```

## 2. Exact process/runtime identity contract

The runtime instance contract creates one random private `instanceId` and one random private shutdown token. The identity is written atomically to a server-owned maintenance state root. Public `/healthz` exposes only the non-secret runtime identity information needed for proof, including PID and instance ID; the shutdown token is not returned.

The one-shot supervisor refuses to restart from a PID alone. Before shutdown it requires the private identity and live loopback `/healthz` response to agree on service, instance ID, PID, version, surface and tool count. Shutdown then uses only the fixed loopback internal endpoint and requires both the exact private token and exact instance ID.

The managed runtime itself returns HTTP 202 before closing. The supervisor waits for the old identity/health to disappear, launches exactly one fixed server-owned worker definition, and accepts the replacement only when it has a different instance ID plus the expected version, surface and tool count.

No arbitrary process kill is used by the accepted candidate.

## 3. Direct semantic dispatch and durable operation contract

`RuntimeMaintenanceService` is the intended Codexless request-handler seam. It accepts only:

```text
requestId
action = restart_codexless
```

It writes the durable operation, acquires the durable active-operation lock, marks the operation armed, and dispatches the detached helper. The helper owns a fixed delay before destructive work. A replay with the same `requestId` returns the same operation and does not dispatch a second helper. Launch failure becomes a durable terminal failure and releases the active lock.

The proposed public MCP projection adds a read/status form but still accepts no host-control fields.

## 4. Focused regression evidence

Final private run:

```text
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
```

The detached suite now also proves legitimate server-owned Windows environment names such as `ProgramFiles(x86)` are preserved while malformed pseudo-variable keys fail closed.

## 5. Functional restart evidence

Production-shaped one-shot supervisor probe:

```text
operationStatus=succeeded
oldInstanceDifferent=true
oldPidDifferent=true
replacementHealthy=true
replacementVersion=probe-v2
replacementToolCount=61
gracefulShutdownOnly=true
arbitraryPidKillUsed=false
```

Direct dispatch probe:

```text
acceptedBeforeRestart=true
immediateOldWorkerStillHealthy=true
terminalStatus=succeeded
replacementVersion=direct-v2
replacementToolCount=61
instanceChanged=true
durableActiveLockReleased=true
idempotentReplayNoSecondRestart=true
```

HTTP entrypoint probe:

```text
healthInstanceBound=true
shutdownTokenPrivate=true
wrongTokenRejected=true
validShutdownAccepted=true
gracefulExitCode=0
identityRemovedAfterShutdown=true
```

These are isolated workers only. They do not claim a production self-restart yet.

## 6. Preview.18 integration candidate

Proposed public runtime:

```text
version        0.1.1-preview.18-runtime-maintenance
surface        codexless-public-preview-v2
toolCount      62
new public tool codex.runtime_maintenance
```

Important integration hashes:

```text
codexless-runtime.mjs               566ba74a6c3dd4cfa169f5d56f835fc08cf27a64f8341cbcbd5177b88fd3050f
mcp-http-public.mjs                 bf63ea413f42259da5d1abd523a42ee8aad2bcdbd8e2a1ffce03fafe0ada1918
mcp-server-factory.mjs              8e3ff7054cd06599fc5632aa3f02ed17397b6dd94cf7050faa757c87b8f4a27a
runtime-maintenance-supervisor.mjs  00c30ec8b560189155aed0cb43d4636f3caf8a6799b0ab6750dec701b124b278
surface-contracts.mjs               0f99e3f883df7ab3c190d31c6a544289e25da3d05a0e1c83246742942dfca335
public-surface-registration.mjs     4e55dc32a94ef0fb3025dda4d6896d3eb5b9fb06e34112aba09f7d473e061227
bounded-git-fetch-origin.mjs        72b6cdc0ade82c83f15c677dc997b6c491509f1b0563d3cb1601c8f88c0cf0d7
bounded-git-pull-ff-only.mjs        4b87033b505cb345dcf8c711871259184f9f0508e27f2575151d72f0b6fa9138
```

The public schema accepts exactly:

```text
{ action: restart_codexless, requestId }
{ action: status,            requestId }
```

and rejects PID, path, cwd, executable, command, environment, URL, tunnel ID, credentials, permission profile, sandbox and other caller host-control inputs.

## 7. Staged compatibility evidence

The staged preview.18 overlay passed:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=62
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=62
FILE_LINK_REGRESSION=PASS tests=10
PUBLIC_SURFACE_REGISTRATION=PASS tools=62
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
```

The deeper Research 120 suites also passed against the staged preview.18 overlay, including routing policy, orchestrator, projection, artifact manager/render/text/resource adapters, native fidelity/splitting/source profiling, >192 MiB isolation smoke, and large-source read/render. No accepted PDF route was regressed.

## 8. Production non-mutation proof

After qualification, the real runtime remained:

```text
ok         true
version    0.1.1-preview.17-office-file-link
toolCount  61
surface    codexless-public-preview-v2
tunnel     live / ready
```

No production Codexless source, process, state or tunnel lifecycle was mutated by this qualification.

```text
RUNTIME_MAINTENANCE_PREVIEW18_INTEGRATION=PASS
LIVE_MUTATION=false
NEXT=GUARDED_PUBLICATION_PREFLIGHT
```
