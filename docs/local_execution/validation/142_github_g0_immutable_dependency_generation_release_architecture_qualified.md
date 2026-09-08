# Validation 142: GitHub G0 Immutable Dependency-Generation Release Architecture Qualified

**Date:** 2026-09-08
**Status:** PASS / IMMUTABLE NATIVE DEPENDENCY GENERATIONS QUALIFIED / SOURCE-ONLY BOOTSTRAP RELEASE NEXT
**Research:** Research 123
**Scope:** Close the Runtime Release dependency-provisioning design blocker by qualifying exact package preparation, immutable generation binding, release activation/rollback selection, restart persistence, recovery, and G0 keyring loading without live `node_modules` mutation.

## 1. Private implementation result

The private local-runtime repository now preserves the integrated implementation at:

```text
5b63371536fa2f09bb122ed09470ec5204f18d9b
```

Commit:

```text
Integrate immutable runtime dependency generations
```

The private semantic publication passed:

```text
RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

The implementation spans three deliberately separated candidate layers:

```text
runtime-dependency-provisioning-candidate
runtime-release-dependency-integration-candidate
github-g0-runtime-integration-candidate
```

The final G0 candidate composes the release/dependency changes into the same main-runtime source candidate rather than depending on ambient package installation.

## 2. Exact dependency identity remains server-owned

The only currently accepted dependency id is:

```text
github-keyring-win32-x64
```

It resolves server-side to exactly:

```text
@napi-rs/keyring@2.0.0
@napi-rs/keyring-win32-x64-msvc@2.0.0
platform = win32
arch = x64
registry = https://registry.npmjs.org/
install scripts = disabled
```

Both npm SHA-512 integrity values remain fixed in the implementation. Remote release callers do not choose package names, versions, registry URLs, integrity strings, install commands, destination paths, platform packages, npm environment, or package authority.

## 3. Real package preparation and loading

The exact dependency provisioner was exercised again against the real npm packages. The prepared generation was:

```text
fileCount  = 10
totalBytes = 1,971,364
treeSha256 = abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
```

A child process then resolved `@napi-rs/keyring` through the immutable generation binding and observed:

```text
Entry type = function
bindingCount = 1
```

No credential operation was performed by this package-loading qualification. The temporary prepared state was removed successfully after the child process exited.

A separate real Runtime Release v2 preparation also succeeded using the same real npm dependency and produced:

```text
prepared schema          codexless.runtime-release-prepared.v2
dependencyCount          1
dependencyFiles          10
dependencyBytes          1,971,364
treeSha256               abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
```

Its scratch state was likewise removed afterward.

## 4. Why immutable generations replace live node_modules mutation

A discriminating Windows probe loaded the real native keyring package from one prepared generation and then attempted to delete that generation before the loading Node process exited.

The import itself succeeded, but same-process removal failed with Windows `EPERM`. After the Node process terminated, separate cleanup removed the same scratch tree successfully.

This is direct evidence that a loaded native `.node` generation may remain file-locked for the process lifetime. Runtime Release must therefore not model native dependency rollback as "replace/delete live node_modules while the worker may still hold the module open."

The qualified model is instead:

```text
prepare exact immutable generation
-> bind worker to { dependencyId, treeSha256 }
-> keep generation immutable for worker lifetime
-> release activation switches worker binding
-> rollback switches worker binding back
-> retain old generations
-> garbage collect only in a later separately qualified lifecycle
```

## 5. Runtime Release v2 dependency contract

`codexless.runtime-release-bundle.v2` adds one bounded `runtimeDependencies` array containing only server-owned dependency ids. Historical v1 manifests remain accepted and normalize to an empty dependency list.

During `prepare`, each dependency id is resolved through the bounded provisioner and the prepared release stores exact refs:

```text
{ dependencyId, treeSha256 }
```

Runtime Release state now preserves:

```text
prepared release:
    runtimeDependencies
    runtimeDependencyFileCount
    runtimeDependencyTotalBytes

pending activation:
    previousDependencies
    targetDependencies

active release:
    previousDependencies
    targetDependencies
```

The public `codex.runtime_release` input schema is unchanged. No package selector or dependency field is exposed to the remote caller.

## 6. Activation, restart, rollback and recovery

The fixed worker launcher now overwrites the server-owned dependency-binding environment for every launch, including canonical `[]`. This prevents an inherited stale generation from surviving an ordinary restart.

The selected binding is:

```text
forward activation   -> targetDependencies
rollback activation  -> previousDependencies
ordinary restart     -> active targetDependencies
forward recovery     -> previousDependencies
rollback recovery    -> targetDependencies
```

Source rollback remains handled by the existing exact source snapshot. Package rollback does not rewrite package bytes; it changes only the immutable generation selected for the replacement worker.

Runtime startup parses the canonical binding and revalidates every exact prepared generation before returning a resolver. Missing or digest-drifted generations fail closed.

## 7. G0 integration

The G0 runtime no longer imports keyring from ambient live `node_modules`. The keyring importer is injected from the exact runtime dependency resolver.

When no keyring generation is bound, a configured G0 kernel has no ambient fallback. Initialization fails through the protected-store error path with an underlying `RUNTIME_DEPENDENCY_NOT_BOUND` condition, before any GitHub request.

When the exact generation is bound, the keyring module resolves from that immutable generation. Ordinary unconfigured runtime startup remains lazy and performs no GitHub credential read or GitHub request.

## 8. Regression result

The final combined focused run passed:

```text
22 tests
22 pass
0 fail
```

Coverage includes:

```text
server-owned dependency id/platform authority
exact npm integrity and installed-package-set validation
idempotent prepared state
digest-drift and missing-generation failure
canonical duplicate-free worker binding
root-package-only importer
Runtime Release v1 compatibility
Runtime Release v2 dependency preparation
publish/rollback dependency switching
zero live node_modules mutation
stale inherited binding overwrite
startup prepared-generation revalidation
ordinary restart active-binding preservation
forward activation failure recovery to previous binding
G0 exact-generation keyring resolution
G0 no-ambient-fallback behavior
```

Additional source syntax checks passed:

```text
G0 combined candidate                  21 / 21
release dependency integration        15 / 15
```

The focused secret scanner reported:

```text
0 matches
```

## 9. Remaining deployment boundary

The current live Codexless runtime still runs the already-qualified Runtime Release v1 engine. It cannot consume a v2 manifest until the new source implementation itself is installed.

This creates a bounded bootstrap sequence rather than a design blocker:

```text
current live Runtime Release v1
-> source-only v1 bootstrap release
   - install dependency-aware release engine
   - install immutable dependency resolver
   - install G0 source integration
   - keep runtime dependency binding empty
   - keep public github.* count at zero
-> restart and qualify new source runtime
-> use live Runtime Release v2 for exact keyring-generation activation
-> only then open live GitHub authorization / public-action gates
```

```text
VALIDATION142=PASS
PRIVATE_RUNTIME_HEAD=5b63371536fa2f09bb122ed09470ec5204f18d9b
IMMUTABLE_DEPENDENCY_GENERATIONS=QUALIFIED
REAL_KEYRING_GENERATION_TREE=abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
REAL_KEYRING_GENERATION_FILES=10
REAL_KEYRING_GENERATION_BYTES=1971364
RUNTIME_RELEASE_V2_DEPENDENCY_PREPARE=PASS
COMBINED_FOCUSED_TESTS=22_OF_22_PASS
PUBLIC_GITHUB_ACTIONS=0
LIVE_GITHUB_AUTH=NOT_STARTED
LIVE_RUNTIME_RELEASE_ENGINE=V1
NEXT=BUILD_SOURCE_ONLY_G0_DEPENDENCY_BOOTSTRAP_RELEASE_V1
```
