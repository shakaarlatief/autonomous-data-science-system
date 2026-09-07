# Checkpoint 359: Preview.21 Semantic Release Bundle Qualified

**Date:** 2026-09-07
**Status:** PASS / FIRST GENUINE POST-PREVIEW.20 SEMANTIC RELEASE BUNDLE QUALIFIED / LIVE PREPARE NEXT
**Checkpoint class:** PRIVATE RELEASE-BUNDLE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies a minimal genuine next-version release bundle against the live preview.20 baseline without modifying the installed runtime.
**Authority:** Research 122 governs the architecture; Validation 117 owns detailed bundle evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The first post-preview.20 release bundle is now durably preserved in the fixed private runtime-release namespace:

```text
releaseId           preview21-semantic-release-e2e
private HEAD        7aa303f4f362f7d4a3ae9b4d492679751c5e892b
target version      0.1.1-preview.21-semantic-release-e2e
target surface      codexless-public-preview-v2
target tool count   63
manifest SHA-256    bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
```

This is intentionally a small but real next-version release. It changes exactly two installed files:

```text
src/surface-contracts.mjs
    preview.20 version string -> preview.21 semantic-release-e2e version string

test/public-surface-registration.mjs
    adds an exact assertion for the preview.21 server version
```

The live preview.20 hashes exactly match both manifest `expectedCurrentSha256` values, and the payload hashes exactly match both manifest target hashes:

```text
src/surface-contracts.mjs
    current  9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b
    target   09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a

test/public-surface-registration.mjs
    current  b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
    target   a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

The manifest passes the actual preview.20 `validateManifest` implementation and canonical LF JSON encoding. A staged overlay of the exact live preview.20 install plus the two payload files passes all nine release-declared regressions:

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
PREVIEW21_STAGED_PUBLIC_REGRESSIONS=PASS scripts=9
```

The private repository push passed `RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS`, exact local/remote equality, clean tracked postflight and `postflightOk=true`. All qualification scratch was removed afterward.

No installed source file, live process, tunnel, prepared release state, or runtime-release mutation operation has been changed by this checkpoint. Production remains preview.20 / 63 tools.

The next gate is deliberately non-destructive to the install: from the refreshed fresh-host surface, call `prepare` for this exact release/source binding and then `verify` before publication. `prepare` should copy the immutable bundle into server-owned prepared state; pre-publication `verify` should report that the two target files are not yet installed. Only after those receipts are qualified should `publish` be invoked.

```text
CHECKPOINT_359=PREVIEW21_SEMANTIC_RELEASE_BUNDLE_QUALIFIED
RELEASE_ID=preview21-semantic-release-e2e
SOURCE_HEAD=7aa303f4f362f7d4a3ae9b4d492679751c5e892b
LIVE_MUTATION=false
NEXT=FRESH_HOST_PREPARE_AND_PREPUBLICATION_VERIFY
```
