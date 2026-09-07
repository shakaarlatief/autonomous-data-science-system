# Validation 108: Runtime Maintenance Preview.19 Live Source Published, Restart Pending

**Date:** 2026-09-07
**Status:** PASS / EXACT PREVIEW.19 LIVE-DISK BYTES VERIFIED / ACTIVE PROCESS STILL PREVIEW.18
**Research:** Research 122
**Scope:** Verify the source-only preview.19 publication independently before any activation restart.

## 1. User-observed publication result

The guarded publication helper completed successfully with:

```text
RUNTIME_MAINTENANCE_PREVIEW19_PUBLICATION_RESULT=PASS
CANDIDATE_VERSION=0.1.1-preview.19-runtime-maintenance-schema
TOOL_COUNT=62
LIVE_DISK_PUBLIC_REGRESSIONS=PASS scripts=8
LIVE_DISK_LIFECYCLE_COMPATIBILITY=PASS suites=3 probes=3
SEMANTIC_GIT_PRESERVED=true
RUNNING_PROCESS_STILL=0.1.1-preview.18-runtime-maintenance/62
TUNNEL_STILL=live/ready
RESTART_PERFORMED=false
```

The helper created one timestamped backup for each replaced file and changed exactly three installed files.

## 2. Independent installed-hash verification

A separate read-only ADS command rehashed the installed files after publication. Every candidate hash matched exactly:

```text
src/mcp-server-factory.mjs
expected 90b93ef7e8c384c441d53cf745537902ff8bd6cd2311af8efb0065565021adc8
actual   90b93ef7e8c384c441d53cf745537902ff8bd6cd2311af8efb0065565021adc8
match    true

src/surface-contracts.mjs
expected 9d5dc53098f843e7073f5c7c26fd10d4e2aa57dddb17c5458002138d295dc5f0
actual   9d5dc53098f843e7073f5c7c26fd10d4e2aa57dddb17c5458002138d295dc5f0
match    true

test/public-surface-registration.mjs
expected a7450e461539ea2ff778fca8d23a3b2c084d98c93a19594c94af8e28450213ce
actual   a7450e461539ea2ff778fca8d23a3b2c084d98c93a19594c94af8e28450213ce
match    true
```

The aggregate result was `AllHashesMatch=true`.

## 3. Preserved safety boundary

The same read-only verification confirmed:

```text
semantic-git SHA256
  3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
semantic-git match  true

running version     0.1.1-preview.18-runtime-maintenance
running tool count  62
running surface     codexless-public-preview-v2
tunnel health       live
tunnel ready        ready
```

Therefore source publication did not alter the active process or tunnel. The corrected bytes are installed but not process-live yet.

## 4. Activation decision

Because Validation 105 rejected the preview.18 ChatGPT host schema projection for mutation use, the project will not call `restart_codexless` from preview.18 to activate preview.19. The next action is one manual runbook-controlled bootstrap restart.

After activation, require:

```text
0.1.1-preview.19-runtime-maintenance-schema
62 tools
codexless-public-preview-v2
tunnel live/ready
```

Then refresh the existing developer MCP app and use a new disposable chat to verify that `codex.runtime_maintenance` now projects as the structured flat schema before the first live self-restart call.

```text
PREVIEW19_SOURCE_PUBLICATION=PASS
INDEPENDENT_INSTALLED_HASH_VERIFICATION=PASS
ACTIVE_PREVIEW19=false
LIVE_SELF_RESTART=false
NEXT=MANUAL_ACTIVATION_RESTART
```
