# Validation 117: Preview.21 Semantic Release Bundle Qualified

**Date:** 2026-09-07
**Status:** PASS / RELEASE SOURCE, BASELINE HASHES, TARGET HASHES AND STAGED REGRESSIONS QUALIFIED
**Research:** Research 122
**Private source head:** `7aa303f4f362f7d4a3ae9b4d492679751c5e892b`
**Release ID:** `preview21-semantic-release-e2e`
**Scope:** Qualify the first real next-version bundle intended for the live `codex.runtime_release` path.

## 1. Release design

Target contract:

```text
version       0.1.1-preview.21-semantic-release-e2e
surface       codexless-public-preview-v2
toolCount     63
```

The release is purposefully minimal. It changes the public version compatibility ID and the matching exact-version regression only. No runtime authority, lifecycle, transport, document, Git, Browser, agent or schema behavior changes. This isolates the first live semantic-publication qualification from unrelated feature risk.

## 2. Fixed namespace

The bundle is committed under the server-owned namespace expected by `RuntimeReleaseBundleReader`:

```text
.ads-private/codexless/runtime-releases/preview21-semantic-release-e2e/
    release.json
    payload/src/surface-contracts.mjs
    payload/test/public-surface-registration.mjs
```

The remote caller still supplies no filesystem path. `releaseId` resolves this fixed namespace server-side.

## 3. Manifest and exact hashes

Final manifest SHA-256:

```text
bb00583fd32fc7e512a16b7197b9e4ae9aed41bd1b5649c6015c1af47e20ca60
```

Entries:

```text
src/surface-contracts.mjs
    mode                   replace
    expected current       9286d3838d227055f4591a75dbc2c76ef3c107a8fd99168197892c4d9b4db76b
    target                 09d2f19c0b3a86f1a8e11be9b360f455913d1acfb106ce672abb43d33b0d4f4a

test/public-surface-registration.mjs
    mode                   replace
    expected current       b5b5781d71343fea66102fd27a652131b90913191b9f5179839dc81042ec9bb2
    target                 a11d663baa88f3df7df5f92faad1c5abca67eb475860fadc5d1e8afc05d91bee
```

Independent read-only comparison after private preservation confirmed both live hashes still equal the exact expected-current values and both payload hashes equal the exact target values.

## 4. Manifest parser qualification

The actual preview.20 `validateManifest` implementation accepted the manifest. The file also passed the implementation's exact canonical-JSON requirement after LF-only canonicalization. This caught and corrected an initial Windows newline mismatch before preservation; no live state was involved.

## 5. Staged regression qualification

A staging tree was built from the exact live preview.20 install and overlaid with only the two release payload files. The complete declared regression set passed:

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

The modified registration regression directly asserts:

```text
PUBLIC_SERVER_VERSION == 0.1.1-preview.21-semantic-release-e2e
PUBLIC_SOURCE_TOOL_COUNT == 63
```

## 6. Private preservation

The three release files were committed and pushed using bounded semantic Git:

```text
head       7aa303f4f362f7d4a3ae9b4d492679751c5e892b
parent     77e13dc69aec8e2fdc7ffa8379cccf039046785e
integrity  RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflight exact local/remote equality + clean tracked tree
```

Temporary preview.20 publication scratch had already become superseded by Checkpoints 356-358 and was deliberately removed before this release was committed, so the private working tree is now clean enough for the live release reader's strict `--untracked-files=all` gate.

## 7. Next live discriminator

The first live use should not publish immediately. In one fresh chat with the qualified host schema:

```text
1. prepare releaseId preview21-semantic-release-e2e at exact HEAD 7aa303f...
2. verify the same prepared release before publication
3. stop
```

Expected interpretation:

```text
prepare -> prepared
verify before publication -> verification_failed with mismatchCount 2
```

The second result is expected proof that verification sees the still-installed preview.20 baseline, not a release failure. No `publish`, `rollback` or runtime restart should occur in that turn.

```text
PREVIEW21_RELEASE_BUNDLE=PASS
LIVE_INSTALL_MUTATION=false
NEXT=PREPARE_AND_PREPUBLICATION_VERIFY
```
