# Validation 090: AB-020 Live Source Published / Controlled Restart Pending

**Date:** 2026-09-06
**Status:** PASS / LIVE SOURCE PUBLISHED / CONTROLLED RESTART PENDING
**Scope:** Preserve successful ordinary-host publication of the qualified AB-020 bounded private-integrity scanner correction into the installed Codexless preview.16 tree, with independent exact-hash verification and no process restart yet.

## Publication receipt

The guarded Checkpoint 330 publication helper completed successfully from ordinary PowerShell with `-Publish`. It reran the complete focused/private and staged/live public regression set and reported:

```text
AB020_PRIVATE_INTEGRITY_PUBLICATION_RESULT=PASS
LIVE_DISK_PUBLIC_REGRESSIONS=PASS scripts=3
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
RESTART_PERFORMED=false
```

The helper created a timestamped backup of the previous installed `semantic-git.mjs`.

## Installed bytes

The helper reported the new live-source SHA-256:

```text
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

A separate read-only ADS probe independently re-read the installed file after publication and returned the same exact SHA-256.

## Running process state before restart

The independent probe also confirmed that the currently running process and tunnel remain healthy before restart:

```text
version        0.1.1-preview.16-hybrid-pdf-access
toolCount      60
surface        codexless-public-preview-v2
tunnel health  HTTP 200
tunnel ready   HTTP 200
```

Those values prove only that the pre-existing process is still healthy. They do not prove the newly published `semantic-git.mjs` is active because the process has not been restarted.

The private repository remains at qualified head:

```text
7e70bd05e4da76ff1ad260b2b1cbdc5c1d65a3fb
```

with only protected `.tmp/` qualification/publication scratch untracked.

## Next action

`docs/local_execution/OPERATIONS.md` was re-read immediately before restart guidance. The next accepted sequence is the full controlled restart: stop tunnel first while keeping its Git Bash shell open, stop/restart Codexless, verify local preview.16 / 60-tool health, restart the tunnel, and verify tunnel liveness/readiness.

After restart, AB-020 is not closed until one real private semantic Git commit/push succeeds while the tracked-path enumeration is actually above the old 32 KiB outer command-response boundary. The already-qualified Office candidate can supply that first new tracked path.

```text
AB020_LIVE_SOURCE_PUBLICATION=PASS
RESTART_PERFORMED=false
NEXT=CONTROLLED_RESTART
```
