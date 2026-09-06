# Validation 081: Hybrid PDF Direct-Render Serialization Candidate Qualified

**Date:** 2026-09-06
**Status:** PASS / PRIVATE CANDIDATE 51/51 / GUARDED LIVE PUBLICATION NEXT
**Research:** Research 120
**Scope:** Qualify the smallest implementation correction for the Checkpoint 322 multi-page direct-render transport failure without changing the public PDF intent contract, widening authority, or adopting the previously unqualified loopback transport.

## 1. Defect boundary

Checkpoint 322 / Validation 080 established that source pages 16 and 49 of `51.Deep Learning2.annotated.pdf` fail when sent together through `codex.document_render` but pass individually with the already-qualified Checkpoint 321 hashes. The current renderer sends all selected PNG base64 through one App Server `command/exec` stdout JSON protocol, matching the previously documented Windows buffered-capture ceiling.

The accepted correction is therefore internal serialization rather than semantic rerouting:

```text
public request
    pages: 1..4 ordered unique source pages

internal direct renderer
    -> one read-only sandbox execution per selected page
    -> validate each one-page child protocol
    -> require consistent source pageCount
    -> preserve requested order
    -> combine validated page records
    -> reapply existing 4 MiB per-page / 8 MiB aggregate limits
    -> revalidate source identity after rendering
```

No public tool schema, intent policy, source authority, renderer dependency, DPI, cache policy, or OCR behavior changed.

## 2. Candidate implementation

The private runtime candidate modified only:

```text
.ads-private/codexless/hybrid-pdf-routing-candidate/src/document-renderer.mjs
```

The candidate renderer SHA-256 after the correction is:

```text
42199fca624f931f0076a502dbe4c4710f26f0769db50a64a2ac2174b6899b43
```

The implementation executes one `authorityExecutor.exec` per requested source page with:

```text
access      readOnly
capability  read
page batch  [one page]
```

and fails closed on truncation, non-zero child exit, invalid JSON, child-level failure, invalid page count, inconsistent page counts across serialized executions, malformed PNGs, provenance mismatches, aggregate image limit violations, or source drift.

## 3. Regression evidence

Two focused regression cases were added:

```text
multi-page request
    -> exactly one sandbox execution per selected page
    -> ordered recombination
    -> permission/profile preservation
    -> diagnostics aggregation
    -> PASS

inconsistent pageCount across serialized executions
    -> DOCUMENT_RENDER_PROTOCOL_ERROR
    -> PASS / fail closed
```

The full hybrid PDF candidate suite then passed:

```text
tests       51
pass        51
fail        0
cancelled   0
skipped     0
```

Existing routing, facade projection, native splitting, cache lifecycle, source drift, artifact text/render/resource, render-equivalence, and >192 MiB isolation tests remained green.

## 4. Private preservation and integrity-boundary observation

The first private candidate commit was:

```text
96154261b275dbe3e8f66bf8fd5822b9f16b2dc5
Qualify multi-page PDF render serialization fix
```

Its first semantic push failed closed with:

```text
RUNTIME_BOOTSTRAP_INTEGRITY_UNCERTAIN
tracked-file enumeration was truncated
```

Direct read-only measurement showed the tracked NUL-delimited path enumeration had reached 32,841 bytes for 412 files, just above the generic 32 KiB command-output envelope. This is the concrete scaling edge already anticipated by AB-020. The integrity gate was not weakened and the push was not bypassed.

The two new renderer regression cases were instead folded into an existing tracked candidate test file, preserving all 51 tests while removing the additional tracked pathname. The deterministic tracked-path enumeration then measured:

```text
32,753 bytes
411 files
```

inside the existing gate. The follow-up private commit was:

```text
ad61a5619165ec5675e75daecdb4fdb29ea6f19a
Keep PDF render regression within bounded private gate
```

The bounded semantic push then passed:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
local HEAD == origin/main
tracked working tree clean
postflightOk=true
```

This is a bounded preservation workaround, not a claim that AB-020 is architecturally solved. The repository-size/path-enumeration coupling remains a real future runtime-integrity refinement target.

## 5. Live boundary

The installed Codexless runtime has not yet been modified by this candidate qualification. The active process remains the previously qualified preview.16 / 60-tool runtime with the old multi-page renderer behavior.

Therefore:

```text
CANDIDATE_RENDERER_SERIALIZATION   PASS
FOCUSED_REGRESSION                 PASS 2/2
FULL_PRIVATE_CANDIDATE_SUITE       PASS 51/51
PRIVATE_PRESERVATION               PASS
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY   PASS
LIVE_RENDERER_PUBLICATION          NOT YET PERFORMED
LIVE_RESTART                       NOT YET PERFORMED
FRESH_HOST_INTENT_RETEST           NOT YET PERFORMED
```

The next legitimate step is a renderer-only guarded publication against the exact installed preview.16 baseline, followed by the repository-authoritative controlled restart procedure and a fresh disposable intent-matrix requalification.
