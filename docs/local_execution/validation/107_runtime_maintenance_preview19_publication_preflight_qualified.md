# Validation 107: Runtime Maintenance Preview.19 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / EXACT THREE-FILE SCHEMA-CORRECTION PUBLICATION PACKAGE QUALIFIED / LIVE MUTATION NOT YET PERFORMED
**Research:** Research 122
**Scope:** Qualify the exact ordinary-host helper that will publish preview.19 while preserving the separation between source publication, activation restart, fresh-host schema verification, and the eventual first live self-restart.

## 1. Durable candidate and helper

```text
private head   ac3e05de0ebd9553eafb322ce19ec17539f1c09d
private push   RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
tracked tree   clean
helper SHA256  3ce8d4561886a8101525666cc6c084ed94b2f9607d36ec5a7ea797961b2be165
```

## 2. Exact live preview.18 baseline

The helper requires:

```text
version    0.1.1-preview.18-runtime-maintenance
toolCount  62
surface    codexless-public-preview-v2
tunnel     live / ready
```

Exact old hashes:

```text
src/mcp-server-factory.mjs
  8e3ff7054cd06599fc5632aa3f02ed17397b6dd94cf7050faa757c87b8f4a27a
src/surface-contracts.mjs
  0f99e3f883df7ab3c190d31c6a544289e25da3d05a0e1c83246742942dfca335
test/public-surface-registration.mjs
  4e55dc32a94ef0fb3025dda4d6896d3eb5b9fb06e34112aba09f7d473e061227
```

AB-020 semantic-Git must remain:

```text
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

## 3. Exact preview.19 publication bytes

```text
src/mcp-server-factory.mjs
  90b93ef7e8c384c441d53cf745537902ff8bd6cd2311af8efb0065565021adc8
src/surface-contracts.mjs
  9d5dc53098f843e7073f5c7c26fd10d4e2aa57dddb17c5458002138d295dc5f0
test/public-surface-registration.mjs
  a7450e461539ea2ff778fca8d23a3b2c084d98c93a19594c94af8e28450213ce
```

The target version is `0.1.1-preview.19-runtime-maintenance-schema`. Tool count and surface remain 62 / `codexless-public-preview-v2`.

## 4. Guarded helper behavior

Before any mutation the helper requires the exact private head, clean tracked/index state, exact live/candidate hashes, exact running version/tool count/surface, unchanged semantic-Git, preserved document/Git regression hashes, and a live/ready tunnel.

It creates a protected staging mirror of live source/test/config, overlays only the three candidate files, checks changed source syntax, runs the eight public regressions, then reruns all lifecycle suites/probes. It separately exercises the same Windows atomic forward/rollback primitive used for live replacement.

On `-Publish`, each existing file is replaced using a same-directory candidate temp plus:

```text
File.Replace(candidateTemp, livePath, timestampedBackup, true)
```

with exact old-backup and new-live hash checks. Any failure rolls completed replacements back in reverse from verified backups. The helper then reruns public/lifecycle regressions against live disk and requires the process/tunnel to remain preview.18 / 62 and live/ready because it intentionally performs no restart.

## 5. Two complete no-publish preflights

Both runs produced:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=62
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=62
FILE_LINK_REGRESSION=PASS tests=10
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS flat-object-required-enum-additionalProperties-false
PUBLIC_SURFACE_REGISTRATION=PASS tools=62
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
RUNTIME_MAINTENANCE_PREVIEW19_FILE_REPLACE_PRIMITIVE=PASS
RUNTIME_MAINTENANCE_PREVIEW19_PUBLICATION_PREFLIGHT=PASS
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS
STAGED_PUBLIC_REGRESSIONS=PASS scripts=8
LIFECYCLE_COMPATIBILITY=PASS suites=3 probes=3
LIVE_BASELINE_VERIFIED=true
CANDIDATE_HASHES_VERIFIED=true
SEMANTIC_GIT_PRESERVED=true
TUNNEL_BASELINE=live/ready
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

## 6. Activation boundary

Preview.18's server validator remains narrow, but Validation 105 rejected its generic ChatGPT host projection for mutation use. Therefore the preview.18 `codex.runtime_maintenance` action will not be used to activate preview.19. After source publication and independent installed-hash verification, perform a manual runbook-controlled activation restart. Then refresh the app and require a new fresh-chat discovery PASS for the flat schema before any self-restart call.

```text
PREVIEW19_PUBLICATION_PREFLIGHT=PASS
PREFLIGHT_RUNS=2/2
LIVE_MUTATION=false
NEXT=ORDINARY_HOST_PUBLISH
```
