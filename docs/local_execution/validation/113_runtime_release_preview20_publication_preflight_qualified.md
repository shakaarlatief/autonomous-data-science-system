# Validation 113: Runtime Release Preview.20 Publication Preflight Qualified

**Date:** 2026-09-07
**Status:** PASS / CORRECTED BOOTSTRAP + GUARDED SOURCE-PUBLICATION PACKAGE QUALIFIED
**Research:** Research 122
**Private implementation head:** `77e13dc69aec8e2fdc7ffa8379cccf039046785e`
**Protected helper SHA-256:** `c88c3085a14024e57d738ee8110a332bbfc5e0dbe908c8574410ca8598d52a0c`
**Scope:** Verify the final preview.20 candidate after bootstrap-activation hardening and qualify the exact ordinary-host source-publication helper in no-publish mode.

## 1. Bootstrap compatibility problem discovered before publication

Preview.19 is already live and its `codex.runtime_maintenance` service was initialized with the preview.19 contract:

```text
version    0.1.1-preview.19-runtime-maintenance-schema
toolCount  62
surface    codexless-public-preview-v2
```

Preview.20 source publication changes the on-disk supervisor before the running preview.19 process is replaced. The preview.19 service can therefore launch the newly installed supervisor, but its inherited environment does not contain the preview.20-only `CODEXLESS_RUNTIME_INSTALL_ROOT` field and still contains preview.19 expected version/tool-count values.

Requiring that new field unconditionally, or trusting those stale expected values unconditionally, would make the one-time preview.19 -> preview.20 semantic self-restart fail after otherwise successful source publication.

The final supervisor contract is therefore:

```text
CODEXLESS_RUNTIME_INSTALL_ROOT present
    normal preview.20+ restart
    use explicit fixed install root
    use process-bound expected version/surface/tool count

CODEXLESS_RUNTIME_INSTALL_ROOT absent
    one-time source-activation bootstrap compatibility
    derive fixed install root from newly installed supervisor module location
    derive replacement version/surface/tool count from newly installed surface-contracts.mjs
```

The caller still controls none of those fields. Both paths are server-owned configuration.

## 2. Exact bootstrap functional qualification

A dedicated isolated probe launched an old-style maintenance service with intentionally no `CODEXLESS_RUNTIME_INSTALL_ROOT`, exactly matching the preview.19 launcher shape. The service returned `armed`, the detached newly installed supervisor consumed the preview.20 source contract, replaced the isolated preview.19-style worker with preview.20 / 63, and released the durable mutation lock.

Result:

```json
{
  "probe": "r122-preview20-bootstrap-preview19-restart-compat",
  "installRootEnvProvided": false,
  "armedBeforeRestart": true,
  "terminalStatus": "succeeded",
  "replacementVersion": "0.1.1-preview.20-runtime-release",
  "replacementToolCount": 63,
  "instanceChanged": true,
  "activeLockReleased": true
}
```

```text
PREVIEW20_BOOTSTRAP_PREVIEW19_RESTART_COMPAT=PASS
```

No production process or tunnel was involved.

## 3. Final candidate regression rerun

After the bootstrap correction, the staged 63-tool public matrix passed:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=63
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=63
FILE_LINK_REGRESSION=PASS tests=10
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS
RUNTIME_RELEASE_WIRE_SCHEMA=PASS
PUBLIC_SURFACE_REGISTRATION=PASS tools=63
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
RUNTIME_RELEASE_REGRESSION=PASS tests=11
PREVIEW20_FINAL_STAGED_PUBLIC_REGRESSIONS=PASS scripts=9
```

Lifecycle/recovery compatibility passed:

```text
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
PREVIEW20_EXISTING_LIFECYCLE_FUNCTIONALS=PASS probes=3
PREVIEW20_RELEASE_AWARE_RESTART_FUNCTIONAL=PASS scenarios=2
PREVIEW20_RELEASE_AWARE_ROLLBACK_FUNCTIONAL=PASS scenarios=2
PREVIEW20_BOOTSTRAP_PREVIEW19_RESTART_COMPAT=PASS
```

The corrected private candidate was then committed and pushed through bounded semantic Git:

```text
head       77e13dc69aec8e2fdc7ffa8379cccf039046785e
parent     00355fa8354147a8c62dfd40521c122dede5530b
integrity  RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflight exact local/remote equality + clean tracked tree
```

## 4. Exact publication target set

The helper is hash-bound to 16 installation targets:

```text
12 source targets
    5 exact replacements
    7 exact previously absent additions

4 regression targets
    3 exact replacements
    1 exact previously absent addition
```

Existing unchanged lifecycle, HTTP entrypoint, instance-identity, maintenance-service and worker-launcher files are not rewritten merely to make the package larger.

The five source replacements are the release-aware one-shot supervisor, runtime integration, MCP factory, bootstrap-compatible maintenance supervisor and surface contracts. The seven source additions are the bounded runtime-release reader/store/ledger/publisher/service/detached launcher/supervisor modules.

## 5. Publication helper authority

The protected helper exists only in private local scratch:

```text
.tmp/runtime-release-preview20-publication/activate-preview20-runtime-release.ps1
```

SHA-256:

```text
c88c3085a14024e57d738ee8110a332bbfc5e0dbe908c8574410ca8598d52a0c
```

It accepts only one optional switch:

```text
-Publish
```

Without it, the helper cannot mutate the live installation. With it, PowerShell `SupportsShouldProcess` requires explicit high-impact confirmation before any live replacement.

It does not accept a caller-selected live path, candidate path, file list, hash, command, executable, regression list, PID, process, tunnel identity, environment, credential, permission profile or sandbox.

The helper derives:

```text
private repository root from its own location
candidate root from one fixed repository-relative path
live install from %LOCALAPPDATA%\Codexless
health endpoints from fixed loopback addresses
exact target list/hashes from embedded qualified constants
```

## 6. No-publish preflight behavior

Before publication could become reachable, each run required:

```text
private HEAD == 77e13dc...
upstream == 77e13dc...
tracked working tree clean
live preview.19 / 62 / expected surface
production tunnel live / ready
all candidate target hashes exact
all replacement baseline hashes exact
all addition targets absent
complete target stage overlay
nine staged public regressions
three lifecycle regression suites
three established lifecycle functional probes
forward release activation + recovery probe
rollback activation + recovery probe
preview.19 -> preview.20 bootstrap compatibility probe
Windows File.Replace forward/backup/restore smoke
Windows same-volume add/remove smoke
live baseline/tunnel recheck after qualification
```

Two complete no-publish executions independently passed this entire sequence.

Terminal receipt both times:

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

## 7. Publication and rollback semantics

If explicitly rerun with `-Publish`, the helper first repeats the entire preflight. Only after high-impact confirmation does it mutate source.

For each replacement it:

```text
copies exact candidate bytes to a same-directory temporary file
rehashes the temporary file
uses Windows File.Replace
creates a timestamped original-file backup
rehashes installed target immediately
```

For each addition it:

```text
requires target absence in preflight
copies exact candidate bytes to a same-directory temporary file
rehashes the temporary file
uses same-volume File.Move to create the target
rehashes installed target immediately
```

After all writes it verifies all 16 target hashes and runs all nine public regressions directly from the installed tree. The running preview.19 process and production tunnel must still remain healthy because publication itself performs no restart.

Any caught write/post-write/regression failure invokes reverse-order rollback. Replacement backups are restored with the same Windows replacement primitive, additions are removed, and every old hash/absence postcondition is rechecked before the original failure is surfaced.

## 8. Activation boundary after source publication

A successful source-only publication is not enough to call preview.20 live. The required sequence is:

```text
ordinary-host helper source publication
-> independent ChatGPT-side installed hash verification
-> preserve source-published / activation-pending boundary
-> invoke current live preview.19 codex.runtime_maintenance restart_codexless once
-> detached newly installed supervisor derives preview.20 bootstrap replacement contract
-> verify preview.20 / 63 and same managed tunnel
-> recover durable restart status
-> refresh developer MCP app
-> fresh-chat codex.runtime_release schema discovery
-> only then perform first live semantic release operation qualification
```

Production was not changed during Validation 113.

```text
RUNTIME_RELEASE_PREVIEW20_PUBLICATION_PREFLIGHT=PASS
HELPER_REPEATABILITY=PASS runs=2
LIVE_SOURCE_MUTATION=false
LIVE_RESTART=false
NEXT=ORDINARY_HOST_SOURCE_PUBLICATION
```
