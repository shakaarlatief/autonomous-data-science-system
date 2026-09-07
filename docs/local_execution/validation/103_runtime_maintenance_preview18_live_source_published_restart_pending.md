# Validation 103: Runtime Maintenance Preview.18 Live Source Published, Restart Pending

**Date:** 2026-09-07
**Status:** PASS / SOURCE PUBLICATION + INDEPENDENT INSTALLED-HASH VERIFICATION / ACTIVE PROCESS STILL PREVIEW.17
**Research:** Research 122
**Scope:** Preserve the successful ordinary-host preview.18 publication, exact installed bytes, rollback backups, unchanged semantic-Git source, and explicit pre-restart process/tunnel boundary.

## 1. Publication result

The user ran the exact Checkpoint 344 helper with `-Publish` and approved only the qualified publication operation. The helper reran the full preflight and then completed publication.

Terminal result:

```text
RUNTIME_MAINTENANCE_PREVIEW18_PUBLICATION_RESULT=PASS
CANDIDATE_VERSION=0.1.1-preview.18-runtime-maintenance
CANDIDATE_TOOL_COUNT=62
LIVE_DISK_PUBLIC_REGRESSIONS=PASS scripts=8
LIVE_DISK_LIFECYCLE_REGRESSIONS=PASS suites=3 probes=3
SEMANTIC_GIT_PRESERVED=true
RUNNING_PROCESS_STILL=0.1.1-preview.17-office-file-link/61
TUNNEL_STILL=live/ready
RESTART_PERFORMED=false
```

The publication created timestamped backups of every replaced existing source/test target before accepting the new bytes.

## 2. Independent installed-source verification

A separate read-only ADS call after publication rehashed the installed runtime directly.

Installed preview.18 source hashes:

```text
src/codexless-one-shot-supervisor.mjs
  63649587bca0158d0bc942860ff9c1d5bed519ce359225022e0b41f98dc08595
src/codexless-runtime.mjs
  566ba74a6c3dd4cfa169f5d56f835fc08cf27a64f8341cbcbd5177b88fd3050f
src/detached-runtime-maintenance-launcher.mjs
  daef87a56946da819a0bd290733dd6553d3656a8cf64bb960827a7a0d935bb80
src/file-runtime-maintenance-ledger.mjs
  6fe0ef542d7377febca738df2e98238e91ecd52d3cc863cc4ca7b2d8b59d1a50
src/fixed-runtime-worker-launcher.mjs
  18800411d2b5fc64e84fe566731d16c98c0490b7b8907970e5b0d3fa4479601c
src/mcp-http-public.mjs
  bf63ea413f42259da5d1abd523a42ee8aad2bcdbd8e2a1ffce03fafe0ada1918
src/mcp-server-factory.mjs
  8e3ff7054cd06599fc5632aa3f02ed17397b6dd94cf7050faa757c87b8f4a27a
src/runtime-instance-contract.mjs
  bf7e7366ede0f2298aad4a4f062b593772ab3092cff227aa606131be2d18983a
src/runtime-maintenance-service.mjs
  dc3b9666b1f95d7f40d58bb7e88645767d803d08ea6cc7f29f20746d7f0028b8
src/runtime-maintenance-supervisor.mjs
  00c30ec8b560189155aed0cb43d4636f3caf8a6799b0ab6750dec701b124b278
src/surface-contracts.mjs
  0f99e3f883df7ab3c190d31c6a544289e25da3d05a0e1c83246742942dfca335
```

Every value exactly matches Validation 101/102's qualified private candidate.

## 3. Independent installed-regression verification

Replaced preview.18 regression hashes:

```text
test/bounded-git-fetch-origin.mjs
  72b6cdc0ade82c83f15c677dc997b6c491509f1b0563d3cb1601c8f88c0cf0d7
test/bounded-git-pull-ff-only.mjs
  4b87033b505cb345dcf8c711871259184f9f0508e27f2575151d72f0b6fa9138
test/public-surface-registration.mjs
  4e55dc32a94ef0fb3025dda4d6896d3eb5b9fb06e34112aba09f7d473e061227
```

Preserved existing regression hashes remained unchanged:

```text
test/file-link-regression.mjs
  d378c7109ffaef4be58c68d26abef863e5cb4a59bc245a33aa1febc8250d5db6
test/document-file-read-regression.mjs
  7cd4bca0ea2a85212315c5ea8d5f7f08b1da4a635a964fbc8c4bb4d646de35a5
test/document-resource-link-regression.mjs
  d47b353850cb297de5acec3fe678edd4ce18e25aa64ff1d3ab1b8632f1897fac
test/document-render-regression.mjs
  3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
test/image-read-regression.mjs
  6eaf3a2b9f0294e8684b45be8fd8330ba5a6b213271d1f6078601effd0bebc61
```

## 4. AB-020 semantic-Git preservation

Independent installed hash:

```text
src/semantic-git.mjs
  3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

This is exactly the previously live-qualified bounded private-integrity correction. Preview.18 publication did not alter it.

## 5. Explicit pre-restart runtime boundary

Independent health verification after source publication:

```text
version       0.1.1-preview.17-office-file-link
toolCount     61
surface       codexless-public-preview-v2
tunnelHealth  live
tunnelReady   ready
```

This is expected. The active Node process still has preview.17 code loaded. Installed preview.18 bytes are not yet active runtime evidence.

No claim is made yet that:

```text
codex.runtime_maintenance is projected live
production exact-instance identity is active
production self-restart works
ChatGPT has discovered the 62-tool surface
```

## 6. Next evidence boundary

The next step must follow the current operational authority in `docs/local_execution/OPERATIONS.md`. Because this publication changes Codexless code/tool registration, use the full controlled restart order for this one bootstrap activation. After local preview.18 / 62-tool health and tunnel 200/200 are established, refresh the ChatGPT developer MCP app and use a fresh disposable chat for discovery before the first live `codex.runtime_maintenance` mutation qualification.

```text
PREVIEW18_SOURCE_PUBLICATION=PASS
INSTALLED_HASH_VERIFICATION=PASS
ACTIVE_PREVIEW18=false
RESTART_PENDING=true
```
