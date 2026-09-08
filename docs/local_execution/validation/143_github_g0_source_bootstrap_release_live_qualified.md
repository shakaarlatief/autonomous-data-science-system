# Validation 143: GitHub G0 Source Bootstrap Release Live Qualified

**Date:** 2026-09-08
**Status:** PASS / SOURCE-ONLY BOOTSTRAP LIVE / DEPENDENCY BINDING EMPTY / V2 ACTIVATION NEXT
**Research:** Research 123
**Scope:** Qualify the source-only Runtime Release v1 bootstrap that installs the dependency-aware release engine, immutable dependency resolver and internal G0 source integration without activating the keyring generation or exposing public GitHub actions.

## 1. Private release bundle

The private local-runtime repository preserves the bootstrap release at:

```text
private source HEAD   21b8597abde893a2b6e6b9b91d3488de0fe8aa16
releaseId             github-g0-dependency-bootstrap-v1
manifest schema       codexless.runtime-release-bundle.v1
target version        0.1.1-preview.22-github-g0-bootstrap
target surface        codexless-public-preview-v2
target tool count     63
file count            26
regression count      14
manifest SHA-256      77dde3e241d422ba2d7e8e66edb3d9dbe89383fb57f1bd48209294f158a30fe2
```

The release deliberately uses v1 because the pre-bootstrap live engine could not yet consume v2 dependency manifests. It installs the v2-capable source machinery while retaining an empty runtime dependency binding.

The private release-bundle commit is:

```text
21b8597abde893a2b6e6b9b91d3488de0fe8aa16
Add GitHub G0 dependency bootstrap release
```

Its private push passed:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

## 2. Prepublication qualification

Before publication:

```text
current v1 manifest parser              PASS
manifest file count                     26
manifest regression count               14
focused staged regressions              22 / 22 PASS
focused secret scanner                  0 matches
```

The staged regressions cover the immutable package-generation subsystem, Runtime Release v2 compatibility/state transitions, G0 runtime integration and exact-generation keyring routing without performing live GitHub authorization.

`codex.runtime_release prepare` then succeeded through the still-live v1 engine:

```text
status                  prepared
fileCount               26
manifestSha256          77dde3e241d422ba2d7e8e66edb3d9dbe89383fb57f1bd48209294f158a30fe2
```

The prepublication verification correctly reported all 26 target files as not yet installed:

```text
status          verification_failed
mismatchCount   26
```

## 3. Publication

One bounded publication operation was submitted:

```text
operationId   rm_92d5a1cdf16ee979cabda34918b5c686
requestId     r123.g0.bootstrap.publish.20260908.01
action        publish_release
status        succeeded
errorCode     null
```

The old v1 release engine staged and ran the declared regressions before writing the exact payload. Publication completed without rollback or recovery.

Postpublication source verification, before restart, returned:

```text
status          verified
mismatchCount   0
```

## 4. Activation

The existing bounded restart surface activated the published source:

```text
operationId        rm_1dcf2e517515a89eee1c5c651bc440ef
requestId          r123.g0.bootstrap.activate.20260908.01
action             restart_codexless
status             succeeded
errorCode          null
recoveryAttempted  false
```

This proves that the newly installed maintenance/release supervisor source could consume the pending v1 activation record, launch the replacement worker and satisfy the exact target runtime contract.

## 5. Postactivation evidence

A fresh postactivation release verification succeeded and, importantly, returned the new dependency-aware result field:

```text
status                   verified
targetVersion            0.1.1-preview.22-github-g0-bootstrap
targetSurfaceVersion     codexless-public-preview-v2
targetToolCount          63
fileCount                26
runtimeDependencyCount   0
mismatchCount            0
```

`runtimeDependencyCount = 0` is the intended bootstrap state. The dependency-aware engine is live, but no keyring generation has yet been activated.

The restart health contract also preserved the public tool count at 63. The G0 source integration does not register any `github.*` tool, and no live GitHub authorization was started.

## 6. Next boundary

The live runtime can now consume Runtime Release v2. The next bounded step is a v2 activation release that:

```text
- declares only server-owned dependency id github-keyring-win32-x64;
- freezes the exact prepared keyring generation at prepare time;
- advances the runtime version while leaving the public surface at 63 tools;
- keeps public github.* actions at zero;
- performs no GitHub authorization or GitHub API request;
- restarts the worker with the exact immutable dependency binding;
- verifies runtimeDependencyCount = 1 after activation.
```

```text
VALIDATION143=PASS
SOURCE_BOOTSTRAP_RELEASE=LIVE
PRIVATE_RUNTIME_HEAD=21b8597abde893a2b6e6b9b91d3488de0fe8aa16
BOOTSTRAP_RELEASE_ID=github-g0-dependency-bootstrap-v1
BOOTSTRAP_MANIFEST_SHA256=77dde3e241d422ba2d7e8e66edb3d9dbe89383fb57f1bd48209294f158a30fe2
LIVE_RUNTIME_VERSION=0.1.1-preview.22-github-g0-bootstrap
LIVE_RUNTIME_RELEASE_ENGINE=V2_CAPABLE
RUNTIME_DEPENDENCY_COUNT=0
PUBLIC_TOOL_COUNT=63
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
NEXT=BUILD_AND_ACTIVATE_GITHUB_KEYRING_RELEASE_V2
```
