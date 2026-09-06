# Validation 091: AB-020 Live Qualification and Office Candidate Durable Preservation

**Date:** 2026-09-06
**Status:** PASS / AB-020 LIVE-QUALIFIED / OFFICE CANDIDATE DURABLY PRESERVED
**Research:** Research 121
**Scope:** Preserve the post-restart live proof that the private semantic-Git integrity gate now handles tracked-path enumerations above the old 32 KiB outer command-response ceiling, then preserve the already-qualified Office file-link candidate in durable private Git without weakening the integrity policy.

## 1. Restarted live baseline

After the Checkpoint 332 publication/restart boundary, the restarted Codexless runtime reported:

```text
ok             true
version        0.1.1-preview.16-hybrid-pdf-access
surfaceVersion codexless-public-preview-v2
toolCount      60
```

The tunnel returned HTTP 200 for both `/healthz` and `/readyz`. The installed `semantic-git.mjs` remained at the independently qualified SHA-256:

```text
3b2ddbbe00339045b81044bb3e1e39c314a461a7e0f8e4e608b79b4b0f37de02
```

## 2. Real above-32-KiB semantic-push proof

The private runtime repository initially had 411 tracked files and a complete NUL-delimited tracked-path enumeration of 32,753 bytes. One new tracked Office-candidate README path was committed, producing exactly:

```text
tracked files          412
tracked-path bytes     32,813
above old 32 KiB cap   yes
private head           06d315057284a7c59151f9a691df6159f5c8e810
```

`codex.git_push_ff_only` then ran through the restarted live semantic-Git implementation and reported:

```text
integrityPolicyId = runtime-private-bootstrap
integrity         = RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk      = true
remote head       = 06d315057284a7c59151f9a691df6159f5c8e810
```

This is the direct live discriminator that was missing from Checkpoint 332. The private integrity gate now succeeds while the tracked-path enumeration exceeds the old generic 32 KiB response envelope, so AB-020's concrete scaling defect is closed for the accepted bounded-scanner design.

## 3. Office candidate durable preservation

After the live proof, the complete already-qualified Office file-link candidate was moved from protected scratch into the private runtime repository. The durable candidate contains the full candidate source/config snapshot, the deterministic host-fixture generator, focused `codex.file_link` regression, and the public-surface/bounded-Git tests required to qualify the intentional 60 -> 61 tool transition. Temporary installed-runtime `.bak` files were explicitly excluded.

The candidate's `semantic-git.mjs` was refreshed to the live AB-020-qualified source before preservation, so the Office candidate does not regress the newly closed integrity fix.

Durable candidate regressions passed before commit:

```text
FILE_LINK_REGRESSION=PASS tests=10
PUBLIC_SURFACE_REGISTRATION=PASS tools=61
FLEXIBLE_AUTHORITY_REGRESSION=PASS tests=8
```

The candidate was then committed and pushed to private head:

```text
fa5cc2a6c3e6d47f45961ab475c2ac66c24aff0b
```

The second push again reported:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflightOk=true
```

At this durable boundary the private repository has:

```text
tracked files          503
tracked-path bytes     40,013
above old 32 KiB cap   yes
tracked tree           clean
untracked              protected .tmp only
```

## 4. Result

```text
AB020_RESTARTED_LIVE_CODE                PASS
AB020_REAL_PUSH_ABOVE_32KIB              PASS
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY         PASS
AB020_ACCEPTED_SCALING_DEFECT            CLOSED
OFFICE_CANDIDATE_PRIVATE_PRESERVATION    PASS
OFFICE_CANDIDATE_PRIVATE_HEAD            fa5cc2a6c3e6d47f45961ab475c2ac66c24aff0b
NEXT                                     GUARDED PREVIEW.17 PUBLICATION
```
