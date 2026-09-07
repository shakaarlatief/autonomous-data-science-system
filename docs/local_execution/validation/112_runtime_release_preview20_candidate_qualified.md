# Validation 112: Runtime Release Preview.20 Candidate Qualified

**Date:** 2026-09-07
**Status:** PASS / SEMANTIC RUNTIME RELEASE CANDIDATE QUALIFIED WITHOUT LIVE MUTATION
**Research:** Research 122
**Private implementation head:** `00355fa8354147a8c62dfd40521c122dede5530b`
**Scope:** Validate the preview.20 `codex.runtime_release` authority boundary, release preparation/publication/verification/rollback semantics, release-aware restart activation/recovery, chained managed-release history, and compatibility with the existing preview.19 lifecycle architecture.

## 1. Public surface contract

Preview.20 proposes:

```text
0.1.1-preview.20-runtime-release
codexless-public-preview-v2
63 tools
```

The added tool is:

```text
codex.runtime_release
```

Its strict top-level schema accepts only:

```text
action              prepare | publish | verify | rollback | status
releaseId           ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
requestId           ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
expectedSourceHead  ^[0-9a-f]{40}$
```

The wire-level initialize/tools-list regression proves a flat top-level object, all four fields required, the exact action enum and `additionalProperties: false`. It contains no top-level `oneOf` and therefore preserves the host-schema lesson learned from preview.18.

Forbidden caller authority was explicitly regression-tested, including PID, path, install root, destination, command, argv, executable, cwd, environment, URL, tunnel ID, credentials, permission profile, sandbox, regression list and workspace ID.

## 2. Release-source authority

The release reader has one server-owned source workspace identity: `ads-local-runtime`. A caller cannot choose another workspace or path.

For `prepare`, it requires:

```text
local HEAD == expectedSourceHead
upstream HEAD == expectedSourceHead
git status --porcelain --untracked-files=all == empty
integrityPolicyId == runtime-private-bootstrap
release manifest located only in the fixed private release namespace
canonical bounded manifest
payload path contained by the fixed release root
regular non-symlink payload files
per-file SHA-256 equality
bounded file count, per-file size and aggregate size
```

Only after these checks are complete are exact payload bytes copied to a server-owned prepared-release store.

## 3. Installed-runtime publication semantics

A prepared release carries exact current and target hashes. Publication performs:

```text
pending-activation exclusion
managed-active/previous-contract consistency check
exact installed baseline hashes
staged source overlay
staged regression execution
durable rollback snapshot
bounded atomic replacement
live-disk regression execution
exact target hash verification
pending activation write
```

Any caught publication/regression failure restores the exact snapshot before returning failure. The tool does not restart Codexless while its publication request is in flight.

The same runtime-maintenance state root owns prepared payloads, snapshots, release operations and the shared mutation lock. Runtime release mutation and runtime restart therefore cannot concurrently own destructive lifecycle work.

## 4. Activation and recovery coupling

A pending release is activated only by the already-qualified `codex.runtime_maintenance restart_codexless` path. The one-shot supervisor detects pending release state and selects the expected runtime contract from it.

The forward functional probe passed both directions:

```text
successful target activation
    operationStatus=succeeded
    target source retained=true
    target runtime healthy=true
    active release recorded=true
    pending cleared=true

synthetic target-contract mismatch
    operationStatus=failed
    errorCode=RUNTIME_REPLACEMENT_CONTRACT_MISMATCH
    recoveryAttempted=true
    recoverySucceeded=true
    previous source restored=true
    previous runtime healthy=true
    pending cleared=true
```

The rollback functional probe also passed both directions:

```text
successful rollback activation
    operationStatus=succeeded
    previous source restored=true
    previous runtime healthy=true
    active release cleared for bootstrap predecessor=true
    pending cleared=true

synthetic rollback target-contract mismatch
    operationStatus=failed
    recoveryAttempted=true
    recoverySucceeded=true
    released target source reapplied=true
    released target runtime healthy=true
    active release preserved=true
    pending cleared=true
```

These probes used real isolated loopback Codexless-style workers with private runtime identities, authenticated graceful shutdown and replacement health checks. They did not mutate the production listener or tunnel.

## 5. Chained managed-release correction

Qualification identified and corrected an important first-draft defect: a forward activation failure or later rollback could incorrectly erase the active managed-release pointer when another managed release preceded the current release.

The final candidate uses immutable activation-history records keyed by the publication snapshot operation. A newly activated release stores its predecessor operation ID. Rolling back release B restores release A from immutable history; rolling back release A to the unmanaged bootstrap baseline removes the active pointer. Forward activation recovery leaves the predecessor active pointer unchanged. Rollback activation recovery preserves the current released target.

The focused regression now proves this chain explicitly:

```text
A activates
B activates with predecessor A
B rollback restores A as active
A rollback restores unmanaged baseline
```

## 6. Regression evidence

Final candidate and staged results:

```text
PREVIEW20_ALL_SYNTAX=PASS
RUNTIME_RELEASE_REGRESSION=PASS tests=11
PREVIEW20_STAGED_PUBLIC_REGRESSIONS=PASS scripts=9

RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6

existing one-shot exact-instance functional probe PASS
existing direct-dispatch/replay functional probe PASS
existing authenticated HTTP shutdown functional probe PASS
PREVIEW20_RELEASE_AWARE_RESTART_FUNCTIONAL=PASS scenarios=2
PREVIEW20_RELEASE_AWARE_ROLLBACK_FUNCTIONAL=PASS scenarios=2

RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS
RUNTIME_RELEASE_WIRE_SCHEMA=PASS
PUBLIC_SURFACE_REGISTRATION=PASS tools=63
```

The staged public set also preserves bounded semantic Git, Office whole-file handoff, PDF file/read/resource/render paths and local image regression coverage.

## 7. Preservation and live boundary

The complete 25-file preview.20 candidate was committed and pushed through bounded semantic Git:

```text
private head  00355fa8354147a8c62dfd40521c122dede5530b
parent        ac3e05de0ebd9553eafb322ce19ec17539f1c09d
integrity     RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflight    exact local/remote equality + clean tracked tree
```

Production was not changed. Preview.19 / 62 tools and its qualified `codex.runtime_maintenance` self-restart remain the live authority.

## 8. Next gate

Build one guarded ordinary-host bootstrap publication helper for preview.20. It must:

```text
bind exact private head 00355fa...
require exact preview.19 process/tool/surface baseline
require exact old installed hashes and target candidate hashes
stage the complete target source/test overlay
run all public/lifecycle/release regressions
exercise the exact Windows forward/rollback primitive
support no-publish qualification mode
perform source-only publication with timestamped backups and fail-closed rollback
perform no restart
```

After source-only publication passes and independent installed hashes match, activation may use the already-live `codex.runtime_maintenance` path rather than another manual Codexless restart.

```text
RUNTIME_RELEASE_PREVIEW20_CANDIDATE=PASS
LIVE_INSTALL_MUTATION=false
LIVE_RESTART=false
NEXT=PREVIEW20_BOOTSTRAP_PUBLICATION_PREFLIGHT
```
