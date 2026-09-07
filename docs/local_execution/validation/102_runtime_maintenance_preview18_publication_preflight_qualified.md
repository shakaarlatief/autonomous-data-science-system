# Validation 102: Runtime Maintenance Preview.18 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / GUARDED PREVIEW.18 PUBLICATION PREFLIGHT QUALIFIED / LIVE MUTATION NOT YET PERFORMED
**Research:** Research 122
**Scope:** Qualify the exact source/test publication helper that will install the already-qualified preview.18 runtime-maintenance candidate while keeping publication, restart and first live mutation-tool qualification as separate evidence boundaries.

## 1. Bound private candidate

```text
private head  610fb6c1480012b0db80965239493348e5de5a58
private push  RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
tracked tree  clean
```

The helper refuses to run if the tracked private candidate head or tracked/index cleanliness drifts. Untracked protected publication scratch is deliberately outside the private durable candidate.

## 2. Exact live baseline

Running process before publication:

```text
version    0.1.1-preview.17-office-file-link
toolCount  61
surface    codexless-public-preview-v2
tunnel     live / ready
```

Existing live source hashes bound by the helper:

```text
src/codexless-runtime.mjs   3a030c22d974f0fea504dc5f5b024054e4609738489c9920923c39817f78a552
src/mcp-http-public.mjs     491a21b0efdc47dd189f2cf5864bfb5c65edd78991ca0227128ebec55a057cd7
src/mcp-server-factory.mjs  9f6c002c4545ddde7963761c342f91657a0136eaa1954e1358ad49c57288cbdb
src/surface-contracts.mjs   41a4188fa7edf10d3ec1bc79bbd02d2f7f68fdadd5373eba33896ca7f8cfa15c
```

Existing live regression hashes bound by the helper:

```text
test/public-surface-registration.mjs  ff6eba85ad20b99420de706aaa36b86ff7f875a99fd5929fcaeab6a08128bab5
test/bounded-git-fetch-origin.mjs     ccfb937ba4b723b629336410074f9ecd4fe7ba9764bfa07feb94e8a59cdf9f40
test/bounded-git-pull-ff-only.mjs     3949803c97f85bd075b93358964bf0816ca8aeeb18e83b8c254dad9acee64cda
```

AB-020 semantic-Git must remain unchanged:

```text
src/semantic-git.mjs
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

The seven new runtime-maintenance source files are required to be absent before publication.

## 3. Exact publication payload

Existing source replacements:

```text
src/codexless-runtime.mjs
src/mcp-http-public.mjs
src/mcp-server-factory.mjs
src/surface-contracts.mjs
```

New source files:

```text
src/codexless-one-shot-supervisor.mjs
src/detached-runtime-maintenance-launcher.mjs
src/file-runtime-maintenance-ledger.mjs
src/fixed-runtime-worker-launcher.mjs
src/runtime-instance-contract.mjs
src/runtime-maintenance-service.mjs
src/runtime-maintenance-supervisor.mjs
```

Existing regression replacements:

```text
test/bounded-git-fetch-origin.mjs
test/bounded-git-pull-ff-only.mjs
test/public-surface-registration.mjs
```

The target candidate remains:

```text
version        0.1.1-preview.18-runtime-maintenance
surface        codexless-public-preview-v2
toolCount      62
new public tool codex.runtime_maintenance
```

## 4. Helper contract

Protected helper SHA-256:

```text
5c1de81279e4dbf4fb009aa585ca8d832cfd863dbe8765e6139ab75a0542802f
```

The helper:

```text
requires the exact private candidate head
requires tracked private tree/index clean
requires exact preview.17 live source/test hashes
requires all seven new source paths absent
requires exact candidate source/test hashes
requires semantic-git unchanged
requires running preview.17 / 61 tools
requires production tunnel live/ready
stages a complete live source/config/test mirror inside protected private scratch
overlays the exact preview.18 candidate
runs node --check on every candidate source module
runs eight staged public regressions
runs all three lifecycle suites
runs all three isolated lifecycle functional probes
exercises the exact Windows forward+rollback File.Replace primitive before mutation
uses timestamped atomic backups for existing files
uses exact-hash guarded removal for new files on rollback
runs the eight regressions again against live disk after publication
runs lifecycle suites/probes again after publication
requires the running process to remain preview.17 / 61 until restart
requires tunnel to remain live/ready
performs no restart
```

## 5. Two independent complete preflight passes

Both no-publish runs ended with:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=62
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=62
FILE_LINK_REGRESSION=PASS tests=10
PUBLIC_SURFACE_REGISTRATION=PASS tools=62
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
FUNCTIONAL_LIFECYCLE_PROBES=PASS probes=3
RUNTIME_MAINTENANCE_FILE_REPLACE_PRIMITIVE=PASS
RUNTIME_MAINTENANCE_PREVIEW18_PUBLICATION_PREFLIGHT=PASS
LIVE_BASELINE_VERIFIED=true
CANDIDATE_HASHES_VERIFIED=true
SEMANTIC_GIT_PRESERVED=true
TUNNEL_BASELINE=live/ready
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

The helper also cleaned every generated staging directory after each pass; only the helper itself remains in the protected scratch directory.

## 6. Publication/restart separation

A future `-Publish` success is not equivalent to active preview.18 behavior. The evidence sequence remains deliberately separated:

```text
guarded source publication
    -> independent installed hash verification
    -> preserve source-published/restart-pending boundary
    -> one final bootstrap restart using docs/local_execution/OPERATIONS.md
    -> local version/tool-count verification
    -> tunnel verification
    -> ChatGPT app refresh
    -> fresh-chat discovery
    -> first live codex.runtime_maintenance restart qualification
```

Production is untouched at this validation boundary.

```text
RUNTIME_MAINTENANCE_PREVIEW18_PUBLICATION_PREFLIGHT=PASS
PREFLIGHT_RUNS=2/2
LIVE_MUTATION=false
NEXT=ORDINARY_HOST_PUBLISH
```
