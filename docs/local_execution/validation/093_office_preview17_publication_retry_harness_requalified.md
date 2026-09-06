# Validation 093: Office Preview.17 Publication Retry Harness Requalified

**Date:** 2026-09-06
**Status:** PASS / FAILED HOST ATTEMPT CONTAINED / WINDOWS CLEANUP HARNESS HARDENED / PUBLICATION RETRY QUALIFIED
**Research:** Research 121
**Scope:** Preserve the first ordinary-host `-Publish` attempt, prove that it stopped before any live preview.17 mutation, localize the failure to Windows temporary-directory cleanup in the AB-020 regression harness, harden that cleanup without changing product behavior, and requalify the exact guarded publication helper before retry.

## 1. First host publication attempt

The ordinary-host publication command reran the staged 61-tool Office regression package successfully through:

```text
FILE_LINK_REGRESSION=PASS tests=10
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=61
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=61
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=61
```

The final AB-020 regression suite then failed one test only during its `finally` cleanup:

```text
FAIL runtime-private-bootstrap deterministically rejects obvious tracked secret material
EBUSY: resource busy or locked, rmdir ...\codexless-runtime-policy-...\repo-runtime-policy
FLEXIBLE_AUTHORITY_REGRESSION=FAIL failures=1
```

The test body had already exercised the expected secret-material rejection. The failure was the Windows removal of its temporary Git fixture, not a semantic-Git assertion, integrity-policy failure, Office candidate failure, or live publication failure.

## 2. No live mutation occurred

The helper executes all preflight suites before `ShouldProcess` and before replacing any installed file. The failed attempt never reached the confirmation prompt or publication block.

A separate read-only inspection after the failure proved:

```text
running version  0.1.1-preview.16-hybrid-pdf-access
toolCount        60
surface          codexless-public-preview-v2
semantic-git     3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

All six existing files in the Office publication package still matched their exact preview.16 baseline hashes, and all three new preview.17 files remained absent. Therefore:

```text
LIVE_PREVIEW17_FILES_MODIFIED=false
ROLLBACK_REQUIRED=false
RESTART_REQUIRED=false
```

## 3. Harness correction

The private AB-020 regression already used retrying Windows cleanup for its large tracked-set case, but six earlier fixture cleanups still used one-shot recursive `rm`. Those six cleanup calls were normalized to the same bounded Node cleanup policy:

```text
recursive: true
force: true
maxRetries: 8
retryDelay: 100 ms
```

This changes test-fixture teardown only. It does not modify `semantic-git.mjs`, the bounded integrity scanner, the Office candidate, the public tool surface, authority, source ceilings, or publication payload.

The hardened regression passed again under the same repository-local TEMP layout used by the publication preflight. The private correction was committed and pushed at:

```text
386813d1a31afd6748ad829c2f1dab3ea1bb89f4
```

with:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

Hardened regression SHA-256:

```text
5a663903a4e5df4cc470cc52d1bf7776391af88b170532e1aaf5e0ad3dafed25
```

## 4. Requalified publication helper

The helper was rebound to private head `386813d1a31afd6748ad829c2f1dab3ea1bb89f4` and rerun twice without `-Publish`. Both complete preflights passed, including all 8/8 AB-020 regressions.

Current helper SHA-256:

```text
b2e73646922851682c855739eecb539ef73e7d3fc75e278967e66a4829b44ba9
```

Each requalification ended with:

```text
OFFICE_FILE_LINK_PUBLICATION_PREFLIGHT=PASS
PRIVATE_CANDIDATE_HEAD=386813d1a31afd6748ad829c2f1dab3ea1bb89f4
CANDIDATE_VERSION=0.1.1-preview.17-office-file-link
CANDIDATE_TOOL_COUNT=61
FILE_LINK_REGRESSION=PASS tests=10
STAGED_PUBLIC_REGRESSIONS=PASS scripts=7
AB020_FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

## 5. Result

```text
FIRST_PUBLICATION_ATTEMPT              STOPPED_IN_PREFLIGHT
LIVE_PREVIEW17_MUTATION                NO
FAILURE_CLASS                          WINDOWS_TEMP_CLEANUP_EBUSY
PRODUCT_CODE_FAILURE                   NO
HARNESS_CLEANUP_RETRIES_HARDENED       PASS
PRIVATE_HARDENING_PUSHED               PASS
REQUALIFIED_PREFLIGHT_RUNS             2/2 PASS
NEXT                                   RETRY ORDINARY-HOST -Publish
```
