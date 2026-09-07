# Validation 094: Office Preview.17 Atomic Replacement Publication Harness Requalified

**Date:** 2026-09-07
**Status:** PASS / SECOND HOST ATTEMPT ROLLED BACK / ATOMIC REPLACEMENT HARNESS FIXED / PUBLICATION RETRY QUALIFIED
**Research:** Research 121
**Scope:** Preserve the second ordinary-host preview.17 publication attempt, independently verify exact rollback to preview.16, localize the failure to the publication helper's Windows `File.Replace` invocation, correct both forward replacement and rollback primitives, and requalify the complete publication package before another host retry.

## 1. Second host publication attempt

The retry passed every staged preflight and reached the explicit host confirmation step. After approval, the first existing-file replacement failed with:

```text
Exception calling "Replace" with "4" argument(s): "Het pad heeft een ongeldige indeling."
```

The helper caught the exception and reported that completed replacements were rolled back. The failure occurred because the Windows PowerShell/.NET `System.IO.File.Replace` four-argument overload was called with a null backup-file argument. That invocation is not accepted in this host runtime. The defect was in the guarded publication helper, not in the Office candidate source, MCP contracts, semantic-Git integrity code, or staged regressions.

## 2. Independent rollback verification

A separate read-only probe after the failure re-read the installed runtime. The running surface remained:

```text
version        0.1.1-preview.16-hybrid-pdf-access
surface        codexless-public-preview-v2
toolCount      60
```

All six existing publication targets matched their exact preview.16 baseline hashes again:

```text
src/mcp-server-factory.mjs          1dfbf8edb46a6c88149c759794d389c77fc3df7d5886622ddaa93d90fb1f7d75
src/codexless-runtime.mjs           0bcddb93f3b2de6b05e9c8ce8b904ba66154aae896211ee3e761dd3b371f6755
src/surface-contracts.mjs           b466db1f85ae71e6dc4c2f7275dd37853ad1371043cb6e358bb44282a5e2d7a8
test/public-surface-registration.mjs e9a8e0f2463c6595a176d74bd6101c0b1628f2a426b1ed9d19a7b183d8e51284
test/bounded-git-fetch-origin.mjs    e65c7d0810441ecbe5d48c1c9d4a7717431a4ca652a7b5ec7bf39fb732ce2bef
test/bounded-git-pull-ff-only.mjs    e3d70bbf61e08b34463acbd6d5f4951ca3972f28345a1ec65c2fc135e09ee320
```

All three new preview.17 files were absent:

```text
src/file-link-reader.mjs      absent
src/file-resource-store.mjs   absent
test/file-link-regression.mjs absent
```

The AB-020-qualified semantic-Git source remained unchanged at:

```text
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

Two timestamped backup copies of the first existing target remain from the contained failed attempts; both hash exactly to the same preview.16 baseline and are not active runtime files. No restart is required.

## 3. Atomic replacement correction

The helper now uses the Windows-supported atomic replacement form for existing files:

```text
File.Replace(candidateTemp, livePath, timestampedBackupPath, true)
```

The backup is created by the same atomic replacement call and immediately hash-verified against the exact old baseline. The helper no longer pre-copies a backup and then passes null to `File.Replace`.

Rollback was also hardened. For a completed existing-file replacement, rollback now:

```text
copy exact timestamped backup -> bounded rollback temp
verify rollback-temp old hash
File.Replace(rollbackTemp, livePath, displacedTempBackup, true)
verify restored live old hash
delete displaced temporary copy
```

New preview.17 files remain rollback-safe by exact removal when needed.

## 4. Publication-primitive smoke test

The no-publish preflight now directly exercises the same Windows atomic replacement primitive on a bounded scratch fixture before declaring the publication package qualified. It requires:

```text
old destination -> new destination
old destination preserved at backup path
candidate temp consumed
```

and reports:

```text
OFFICE_FILE_REPLACE_PRIMITIVE=PASS
```

This closes the specific test gap that allowed the second host attempt to reach an unexercised `File.Replace` call.

## 5. Requalification

The corrected helper was run twice without `-Publish`. Both complete runs passed:

```text
FILE_LINK_REGRESSION=PASS tests=10
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=61
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=61
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
PUBLIC_SURFACE_REGISTRATION=PASS tools=61
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
OFFICE_FILE_REPLACE_PRIMITIVE=PASS
OFFICE_FILE_LINK_PUBLICATION_PREFLIGHT=PASS
NO_LIVE_FILES_MODIFIED=true
RESTART_PERFORMED=false
```

The private durable candidate remains at:

```text
386813d1a31afd6748ad829c2f1dab3ea1bb89f4
```

Current corrected helper SHA-256:

```text
05839717f1b09360c514d86985180b57dd029b088b1b09a0bdc129f9b54a5ee5
```

## 6. Result

```text
SECOND_HOST_ATTEMPT                     REACHED_MUTATION_BLOCK
FAILURE_CLASS                           WINDOWS_FILE_REPLACE_NULL_BACKUP
ROLLBACK_VERIFIED                       PASS
LIVE_PREVIEW17_ACTIVE                   NO
OFFICE_PRODUCT_CODE_FAILURE             NO
ATOMIC_FORWARD_REPLACEMENT_FIXED        PASS
ATOMIC_ROLLBACK_REPLACEMENT_FIXED       PASS
PUBLICATION_PRIMITIVE_SMOKE_TEST        PASS
REQUALIFIED_PREFLIGHT_RUNS              2/2 PASS
NEXT                                    RETRY ORDINARY-HOST -Publish
```
