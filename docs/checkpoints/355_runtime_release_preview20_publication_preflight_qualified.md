# Checkpoint 355: Runtime Release Preview.20 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / GUARDED PREVIEW.20 SOURCE-PUBLICATION PACKAGE QUALIFIED / LIVE PUBLICATION NEXT
**Checkpoint class:** PUBLICATION PREFLIGHT
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the corrected preview.20 bootstrap activation contract and the exact one-time guarded ordinary-host source-publication helper without mutating the live Codexless install or restarting production.
**Authority:** Research 122 governs the architecture; Validation 113 owns detailed qualification evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

Checkpoint 354 qualified the first complete preview.20 semantic runtime-release candidate, but qualification then exposed one bootstrap-specific compatibility requirement before source publication: the already-running preview.19 process launches the maintenance supervisor with preview.19 expected version/tool-count environment values. After preview.20 source is installed, that old process must still be able to invoke the newly installed supervisor and restart into preview.20 / 63 tools rather than incorrectly insisting on preview.19 / 62.

The corrected private candidate is now preserved and synchronized at:

```text
77e13dc69aec8e2fdc7ffa8379cccf039046785e
```

The corrected supervisor distinguishes the one-time source-activation bootstrap from normal post-preview.20 restarts. When the new preview.20 install-root environment field is absent, which reproduces the environment inherited from preview.19, the newly installed supervisor derives its own fixed installation root from `import.meta.url` and derives the replacement version/surface/tool-count contract from the newly installed server-owned `surface-contracts.mjs`. When preview.20 itself launches later maintenance operations, it supplies the explicit install root and normal process-bound expected contract.

A dedicated functional probe reproduced the exact bootstrap shape with no `CODEXLESS_RUNTIME_INSTALL_ROOT` in the launcher environment and passed:

```text
PREVIEW20_BOOTSTRAP_PREVIEW19_RESTART_COMPAT=PASS
installRootEnvProvided=false
armedBeforeRestart=true
terminalStatus=succeeded
replacementVersion=0.1.1-preview.20-runtime-release
replacementToolCount=63
instanceChanged=true
activeLockReleased=true
```

The complete final candidate matrix was rerun after the correction:

```text
PREVIEW20_FINAL_STAGED_PUBLIC_REGRESSIONS=PASS scripts=9
RUNTIME_RELEASE_REGRESSION=PASS tests=11
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
PREVIEW20_EXISTING_LIFECYCLE_FUNCTIONALS=PASS probes=3
PREVIEW20_RELEASE_AWARE_RESTART_FUNCTIONAL=PASS scenarios=2
PREVIEW20_RELEASE_AWARE_ROLLBACK_FUNCTIONAL=PASS scenarios=2
PREVIEW20_BOOTSTRAP_PREVIEW19_RESTART_COMPAT=PASS
```

A protected one-time helper now exists only in private/untracked local-runtime scratch at:

```text
.tmp/runtime-release-preview20-publication/activate-preview20-runtime-release.ps1
```

Its SHA-256 is:

```text
c88c3085a14024e57d738ee8110a332bbfc5e0dbe908c8574410ca8598d52a0c
```

The helper is bound to private head `77e13dc...`, exact preview.19 / 62-tool live source hashes, exact preview.20 target hashes, absent new source paths, live preview.19 process identity contract, and tunnel `live/ready`. It stages the complete target overlay, runs nine public regressions plus the full lifecycle/release probe set, and exercises both Windows atomic replacement and add/remove rollback primitives before publication is allowed.

Two complete default no-publish runs passed independently. Each ended with:

```text
RUNTIME_RELEASE_PREVIEW20_PUBLICATION_PREFLIGHT=PASS
CANDIDATE_HEAD=77e13dc69aec8e2fdc7ffa8379cccf039046785e
TARGET_VERSION=0.1.1-preview.20-runtime-release
TARGET_TOOL_COUNT=63
STAGED_PUBLIC_REGRESSIONS=PASS scripts=9
LIFECYCLE_REGRESSIONS=PASS suites=3 probes=6
WINDOWS_ATOMIC_REPLACE_ADD_ROLLBACK=PASS
PUBLICATION_PERFORMED=false
RESTART_PERFORMED=false
RUNNING_PROCESS_STILL=0.1.1-preview.19-runtime-maintenance-schema/62
TUNNEL_STILL=live/ready
```

The publication mode is source-only. It requires an explicit high-impact PowerShell confirmation, re-runs the same preflight first, replaces only exact hash-bound targets, adds only exact previously absent release modules/tests, creates timestamped backups for every replacement, verifies each write, runs all nine live-disk public regressions, and rolls all applied targets back on any caught publication/regression failure. It deliberately does not restart Codexless.

After successful source publication, independent installed-hash verification is required before activation. Unlike preview.18/19 bootstrap, preview.20 activation should then use the already-live preview.19 `codex.runtime_maintenance restart_codexless` surface. The new bootstrap-compatibility probe is the isolated proof that this transition can consume newly installed preview.20 source while the request is dispatched by the still-running preview.19 process.

```text
CHECKPOINT_355=RUNTIME_RELEASE_PREVIEW20_PUBLICATION_PREFLIGHT_QUALIFIED
PRIVATE_CANDIDATE_HEAD=77e13dc69aec8e2fdc7ffa8379cccf039046785e
HELPER_SHA256=c88c3085a14024e57d738ee8110a332bbfc5e0dbe908c8574410ca8598d52a0c
LIVE_PUBLICATION_PERFORMED=false
LIVE_RESTART_PERFORMED=false
NEXT=ORDINARY_HOST_PREVIEW20_SOURCE_PUBLICATION
```
