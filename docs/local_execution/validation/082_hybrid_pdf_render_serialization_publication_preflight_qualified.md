# Validation 082: Hybrid PDF Render Serialization Publication Preflight Qualified

**Date:** 2026-09-06
**Status:** PASS / GUARDED LIVE PUBLICATION READY / NO LIVE FILES MODIFIED
**Research:** Research 120
**Scope:** Qualify the exact renderer-only live-publication package for the Checkpoint 323 direct-render serialization correction, including the matching installed render-regression expectation, without modifying the installed Codexless runtime or restarting any process.

## 1. Starting boundary

Checkpoint 323 / Validation 081 qualified the private `DocumentRenderer` correction at:

```text
private HEAD
ad61a5619165ec5675e75daecdb4fdb29ea6f19a

candidate renderer SHA-256
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43

private hybrid-PDF suite
51 / 51 PASS
```

The running and installed preview.16 runtime remained on the old direct-render batching implementation:

```text
version       0.1.1-preview.16-hybrid-pdf-access
toolCount     60
surface       codexless-public-preview-v2
tunnel health 200
tunnel ready  200

installed renderer SHA-256
f7f057b70341531d1f3c07853c0741c8668efed3473d33e9c355917fdd2297ef
```

## 2. First staged publication attempt exposed one stale regression expectation

The first guarded preflight copied the installed runtime into a repository-local protected scratch stage, overlaid only the qualified renderer candidate, reran the 51-test private suite, and then executed the existing seven public regression scripts.

The private suite passed 51/51. Six public regressions passed. The staged `document-render-regression.mjs` failed one assertion because the previously installed test still encoded the old batching contract:

```text
expected authority.execCalls.length = 1
actual                              = 2
```

The same old test also expected one child invocation containing:

```text
[2,1]
```

The qualified renderer intentionally performs:

```text
[2]
[1]
```

in two separate read-only sandbox executions. No live file had been modified.

This was therefore a stale test expectation created by the intentional implementation change, not evidence that the serialization implementation had regressed the public contract.

## 3. Matching public regression adaptation

The installed render regression was copied into protected repository-local scratch and changed only at the intentional transport expectation.

Old installed regression SHA-256:

```text
24581331f7442bd44af37dbe3d559135117bbe48f69bc215e98822b825e7feb6
```

Prepared adapted regression SHA-256:

```text
3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
```

The adapted assertion requires:

```text
execCalls.length == 2
child page selections == [[2],[1]]
```

and preserves the existing checks that every child execution uses:

```text
access          readOnly
capability      read
outputBytesCap  INTERNAL_RENDER_STDOUT_BYTES
executable      node.exe
child           document-render-child.mjs
```

No source behavior, authority, limit, dependency, tool schema, or semantic routing policy was changed by the regression adaptation.

## 4. Guarded publication helper

A temporary publication helper was prepared only under protected private-repository `.tmp`:

```text
.tmp/hybrid-pdf-render-serialization-publication/activate-render-serialization-publication.ps1
```

Helper SHA-256:

```text
a05578345be3b5652f5319280d525ac696e60d0c8462a33b8ebdcae8877ad58b
```

The helper binds all four exact old/new hashes:

```text
live renderer before
f7f057b70341531d1f3c07853c0741c8668efed3473d33e9c355917fdd2297ef

candidate renderer after
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43

live render regression before
24581331f7442bd44af37dbe3d559135117bbe48f69bc215e98822b825e7feb6

adapted render regression after
3e60f761ebf5d68dcf4b05969e62dc3cf3d6931aebe4ab7403b66fc37ac4b725
```

Before any publication it also requires the expected live preview.16 version, surface and 60-tool count, reruns the complete 51-test private suite, builds a clean staged installed-runtime mirror, overlays exactly the renderer and adapted regression, checks syntax, and executes the complete seven-script public regression set.

With `-Publish`, it uses same-directory atomic replacement for exactly those two installed files, creates timestamped backups, verifies exact post-write hashes, reruns the seven live-disk regressions, and rolls back every completed replacement in reverse order if a subsequent publication gate fails. It deliberately does not restart Codexless.

## 5. Final preflight result

The corrected publication package passed without `-Publish`:

```text
CANDIDATE_CORE_TESTS=PASS tests=51
STAGED_PUBLIC_REGRESSIONS=PASS scripts=7

BOUNDED_GIT_FETCH_ORIGIN=PASS tools=60
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=60
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RENDER_REGRESSION=PASS tests=10
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=60

HYBRID_PDF_RENDER_SERIALIZATION_PUBLICATION_PREFLIGHT=PASS
NO_LIVE_FILES_MODIFIED=true
```

The exact expected live runtime remained:

```text
0.1.1-preview.16-hybrid-pdf-access
codexless-public-preview-v2
60 tools
```

## 6. Authority and mutation boundary

The normal `ads-local-runtime` workspace authority does not own `%LOCALAPPDATA%\Codexless`, and this qualification did not widen that authority. The preflight performed no live-install mutation.

The already accepted operational pattern remains a guarded ordinary-host PowerShell publication of exact qualified bytes. Restart is a separate step governed by `docs/local_execution/OPERATIONS.md`.

## 7. Result

```text
PRIVATE_CANDIDATE                         PASS 51/51
FIRST_STAGE_STALE_TEST_EXPECTATION        FOUND / NO LIVE MUTATION
ADAPTED_RENDER_REGRESSION                 PASS
FINAL_STAGED_PUBLIC_REGRESSION            PASS 7/7
EXACT_LIVE_BASELINE_BOUND                 YES
EXACT_CANDIDATE_HASHES_BOUND              YES
ATOMIC_BACKUP_ROLLBACK                    PREPARED
LIVE_FILES_MODIFIED                       NO
LIVE_PROCESS_RESTARTED                    NO
NEXT                                      ORDINARY_HOST_POWERSHELL_PUBLISH
```

The next action is to run the exact qualified helper from ordinary host PowerShell with `-Publish`. If publication reports PASS, independently verify the two installed hashes before entering the controlled restart sequence.
