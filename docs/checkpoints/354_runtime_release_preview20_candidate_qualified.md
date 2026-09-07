# Checkpoint 354: Runtime Release Preview.20 Candidate Qualified

**Date:** 2026-09-07
**Status:** PASS / PREVIEW.20 SEMANTIC PUBLICATION-VERIFY-ROLLBACK CANDIDATE QUALIFIED IN ISOLATION
**Checkpoint class:** PRIVATE CANDIDATE + STAGED PUBLIC SURFACE QUALIFICATION
**Project stage:** Research 122 runtime self-maintenance and device-independent access
**Scope:** Qualifies the narrow semantic runtime-release architecture, its public MCP schema, staged publication and rollback semantics, activation coupling to the already-qualified self-restart path, and automatic recovery behavior without mutating the live Codexless installation.
**Authority:** Research 122 governs the architecture; Validation 112 owns the detailed qualification evidence.
**Interaction environment:** ChatGPT
**Project / workspace:** Autonomous Data Science System
**Interaction session:** `chatgpt-19`
**Conversation title:** `19 - Hybrid PDF Intent Matrix and Isolation Qualification`
**Primary collaborator:** ChatGPT

The private runtime repository now preserves the complete preview.20 candidate at:

```text
00355fa8354147a8c62dfd40521c122dede5530b
```

The candidate proposes:

```text
version      0.1.1-preview.20-runtime-release
surface      codexless-public-preview-v2
toolCount    63
new tool     codex.runtime_release
```

The public tool is one strict flat object with exactly four caller fields:

```text
action              prepare | publish | verify | rollback | status
releaseId           bounded stable release identifier
requestId           bounded stable idempotency identifier
expectedSourceHead  exact lowercase 40-hex private-runtime Git HEAD
```

It exposes no caller-selected install path, destination, PID, executable, shell command, argv, cwd, environment, URL, tunnel identity, credentials, permission profile, sandbox, workspace selector, regression command, or arbitrary host-process/filesystem authority.

Release source is fixed server-side to a committed release-bundle namespace in the registered `ads-local-runtime` private repository. Preparation requires the exact declared source HEAD to equal both local HEAD and upstream, requires a clean working tree, validates a canonical bounded manifest, verifies every payload SHA-256, and copies the release into server-owned runtime-maintenance state before any installed-runtime mutation.

Publication is separately bounded by exact current installed hashes, staged regressions, a durable rollback snapshot, bounded atomic file replacement, live-disk regressions and post-write hashes. Publication creates a pending activation rather than restarting itself. Activation is delegated to the already-live `codex.runtime_maintenance restart_codexless` path.

The restart supervisor is release-aware. A successful forward activation verifies the exact target version/surface/tool-count contract and records immutable managed activation history. A failed target activation restores the previous source snapshot, launches the previous runtime contract and clears pending state only after recovery succeeds. Rollback uses the inverse path. Chained managed releases retain predecessor activation history so rolling back release B restores release A as the active managed release rather than incorrectly erasing the chain.

Focused qualification passes:

```text
RUNTIME_RELEASE_REGRESSION=PASS tests=11
PREVIEW20_RELEASE_AWARE_RESTART_FUNCTIONAL=PASS scenarios=2
PREVIEW20_RELEASE_AWARE_ROLLBACK_FUNCTIONAL=PASS scenarios=2
```

The two release-aware functional probes cover four real isolated worker transitions:

```text
forward activation success
forward activation target-contract failure -> previous source/runtime recovery
rollback activation success
rollback activation target-contract failure -> released source/runtime reapplication
```

All preserved public and lifecycle compatibility gates also pass:

```text
PREVIEW20_STAGED_PUBLIC_REGRESSIONS=PASS scripts=9
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
three existing lifecycle functional probes PASS
```

The actual MCP wire regression confirms both mutation-sensitive tools serialize as flat required object schemas with `additionalProperties: false`:

```text
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS
RUNTIME_RELEASE_WIRE_SCHEMA=PASS
PUBLIC_SURFACE_REGISTRATION=PASS tools=63
```

No live `%LOCALAPPDATA%` source file, active Codexless process or production tunnel was mutated during this candidate qualification. Production therefore remains preview.19 / 62 tools with the already-qualified self-restart path.

The next gate is an exact guarded one-time preview.20 bootstrap publication package. It must be bound to the current preview.19 installed hashes and private head above, run the staged/public/lifecycle/release qualification set without publication, prove the Windows replacement/rollback primitive, and perform no restart. Only after that preflight passes may ordinary-host source publication be requested.

```text
CHECKPOINT_354=RUNTIME_RELEASE_PREVIEW20_CANDIDATE_QUALIFIED
PRIVATE_CANDIDATE_HEAD=00355fa8354147a8c62dfd40521c122dede5530b
PUBLIC_TARGET_VERSION=0.1.1-preview.20-runtime-release
PUBLIC_TARGET_TOOL_COUNT=63
LIVE_PUBLICATION_PERFORMED=false
LIVE_RESTART_PERFORMED=false
NEXT=GUARDED_PREVIEW20_BOOTSTRAP_PUBLICATION_PREFLIGHT
```
