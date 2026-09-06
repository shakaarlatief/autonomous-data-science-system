# Validation 083: Hybrid PDF Render Serialization Live Source Published / Restart Pending

**Date:** 2026-09-06
**Status:** PASS / LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Research:** Research 120
**Scope:** Preserve the successful ordinary-host publication of the qualified serialized-page `DocumentRenderer` correction and its matching public regression expectation into the installed Codexless preview.16 tree, independently verify the exact installed hashes, and stop before process restart.

## 1. Publication receipt

The qualified Checkpoint 324 helper was run from ordinary host PowerShell with `-Publish`. The user explicitly confirmed the `ShouldProcess` prompt for target `%LOCALAPPDATA%\\Codexless`.

The helper reran the live-disk regression set and reported:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=60
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=60
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=60
HYBRID_PDF_RENDER_SERIALIZATION_PUBLICATION_RESULT=PASS
LIVE_DISK_REGRESSIONS=PASS scripts=7
RESTART_PERFORMED=false
```

## 2. Installed bytes reported by the publication helper

```text
renderer
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43

render regression
3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
```

The helper created timestamped pre-publication backups for both modified files under the installed Codexless tree.

## 3. Independent post-publication verification

A separate read-only ADS-side PowerShell probe independently re-read the installed files after the host publication and produced the same exact SHA-256 values:

```text
renderer
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43

render regression
3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
```

This closes the exact-byte publication claim for the two intended files.

## 4. Process state remains intentionally old

The independent probe also verified that the currently running process and tunnel remained healthy before restart:

```text
version        0.1.1-preview.16-hybrid-pdf-access
toolCount      60
surfaceVersion codexless-public-preview-v2
tunnel health  HTTP 200
tunnel ready   HTTP 200
```

These health values do not prove the new renderer code is active because the process has not been restarted. The publication helper explicitly reported:

```text
RESTART_PERFORMED=false
```

Therefore this boundary is source-published / restart-pending, not live-qualified behavior.

## 5. Operational authority

`docs/local_execution/OPERATIONS.md` was re-read before restart guidance. Its authoritative full controlled restart order is:

```text
1. stop tunnel-client with Ctrl+C, keep the Git Bash shell open;
2. stop Codexless HTTP with Ctrl+C;
3. restart Codexless from %LOCALAPPDATA%\\Codexless\\bin\\codexless-http.cmd;
4. verify Codexless /healthz and expected toolCount;
5. in Git Bash verify tunnel variables are SET without printing values;
6. optionally run tunnel doctor when needed;
7. start the tunnel client;
8. verify tunnel /healthz HTTP 200;
9. verify tunnel /readyz HTTP 200;
10. only after both layers are healthy, refresh the ChatGPT developer MCP app if required;
11. use a fresh disposable chat for discovery/qualification.
```

The tool surface itself remains 60 tools, so the restart is required to load changed implementation bytes, while an app refresh is not intrinsically required by a schema-count change. A fresh disposable chat remains required for the qualification because AB-008 preserves same-chat projection staleness risk.

## 6. Result

```text
HOST_PUBLICATION                       PASS
LIVE_DISK_REGRESSIONS                  PASS 7/7
INSTALLED_RENDERER_HASH                VERIFIED
INSTALLED_RENDER_REGRESSION_HASH       VERIFIED
RUNNING_PROCESS_RESTARTED              NO
TUNNEL_BEFORE_RESTART                  HEALTHY / READY
BOUNDARY                               SOURCE_PUBLISHED_RESTART_PENDING
NEXT                                   FULL_CONTROLLED_RESTART
```
