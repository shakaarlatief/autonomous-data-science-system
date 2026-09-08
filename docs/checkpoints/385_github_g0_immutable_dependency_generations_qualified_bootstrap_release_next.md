# Checkpoint 385: GitHub G0 Immutable Dependency Generations Qualified, Bootstrap Release Next

**Date:** 2026-09-08
**Status:** PASS / DEPENDENCY PROVISIONING + ACTIVATION ARCHITECTURE QUALIFIED / SOURCE-ONLY BOOTSTRAP RELEASE NEXT
**Checkpoint class:** PRIVATE IMPLEMENTATION + RELEASE ARCHITECTURE QUALIFICATION
**Project stage:** Research 123 GitHub connector capability parity and Codexless Runtime Bridge architecture
**Scope:** Preserve the completed immutable native-dependency generation architecture and open the source-only Runtime Release v1 bootstrap needed before the live runtime can consume dependency-aware v2 releases.
**Authority:** Validation 142 owns the qualification evidence; private local-runtime commit `5b63371536fa2f09bb122ed09470ec5204f18d9b` owns the candidate bytes.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-20`
**Conversation title:** `20 - GitHub Capability Parity and Codexless Runtime Bridge`
**Primary collaborator:** ChatGPT

## 1. Dependency provisioning is no longer an unresolved design blocker

The exact keyring package is now represented as one server-owned immutable prepared generation. Runtime workers select it by exact `{dependencyId, treeSha256}` binding rather than by mutating live `node_modules`.

The real Windows x64 package generation remains:

```text
fileCount  10
totalBytes 1,971,364
treeSha256 abe67a212121747d57d1bb78cd7880e7e7bb29e1f44e2ba8ec5010e5f1e50858
```

Real package loading and real Runtime Release v2 preparation both succeeded and their scratch state was removed afterward.

## 2. Windows native-module lifetime drives the architecture

The real package could be loaded from prepared state, but same-process generation deletion failed with Windows `EPERM`; cleanup succeeded after process exit. Release/rollback therefore switches immutable worker bindings and retains generations rather than replacing/deleting loaded native package directories.

## 3. Release lifecycle is dependency-aware

Runtime Release v2 preserves exact dependency refs in prepared, pending and active state. Forward activation, rollback, ordinary restart and recovery all select the correct generation set. Startup revalidates the bound generation. Missing or drifted prepared state fails closed.

The public runtime-release tool input remains unchanged and exposes no arbitrary package/install authority.

## 4. G0 is wired to the same binding

The G0 keyring importer resolves only through the exact runtime dependency generation. There is no ambient `node_modules` fallback. The public MCP surface remains 63 existing Codexless tools and zero `github.*` actions, and live GitHub authorization remains unstarted.

## 5. Qualification result

```text
private runtime head                  5b63371536fa2f09bb122ed09470ec5204f18d9b
combined focused tests                22 / 22 PASS
G0 combined source syntax             21 / 21 PASS
release dependency source syntax      15 / 15 PASS
secret scanner                        0 matches
private integrity                     RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
```

## 6. Next boundary

The live runtime still has the v1 release engine, so v2 cannot bootstrap itself. Build one source-only v1 release that installs the dependency-aware release engine, immutable resolver and G0 source integration while keeping the worker dependency binding empty and registering no public GitHub action. After that source runtime is live-qualified, use Runtime Release v2 to activate the exact keyring generation.

```text
CHECKPOINT385=IMMUTABLE_DEPENDENCY_GENERATIONS_QUALIFIED
DEPENDENCY_PROVISIONING_DESIGN=QUALIFIED
DEPENDENCY_ACTIVATION_ROLLBACK=QUALIFIED
LIVE_RELEASE_ENGINE=V1
PUBLIC_GITHUB_SURFACE=0_ACTIONS
LIVE_GITHUB_AUTH=NOT_STARTED
RESEARCH123=ACTIVE
RESEARCH113=PAUSED_NOT_CLOSED
SOURCE_VAULT=PAUSED
NEXT=BUILD_SOURCE_ONLY_G0_DEPENDENCY_BOOTSTRAP_RELEASE_V1
```
