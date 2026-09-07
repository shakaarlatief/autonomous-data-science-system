# Validation 106: Runtime Maintenance Preview.19 Flat Schema Candidate Qualified

**Date:** 2026-09-07
**Status:** PASS / FLAT TOP-LEVEL MCP SCHEMA + EXISTING LIFECYCLE COMPATIBILITY QUALIFIED / NO LIVE MUTATION
**Research:** Research 122
**Scope:** Qualify the minimum correction for Validation 105's ChatGPT host schema-projection failure before any production runtime-maintenance mutation is allowed.

## 1. Private durable boundary

The candidate and rationale are committed/pushed in the private runtime repository:

```text
private head  ac3e05de0ebd9553eafb322ce19ec17539f1c09d
private push  RUNTIME_PRIVATE_BOOTSTRAP_SAFETY=PASS
postflight    clean / local=origin/main
```

Preview.19 candidate:

```text
0.1.1-preview.19-runtime-maintenance-schema
codexless-public-preview-v2
62 tools
```

## 2. Minimal delta from preview.18

Only three integration files differ from the qualified preview.18 integration candidate:

```text
src/mcp-server-factory.mjs
  8e3ff7054cd06599fc5632aa3f02ed17397b6dd94cf7050faa757c87b8f4a27a
  -> 90b93ef7e8c384c441d53cf745537902ff8bd6cd2311af8efb0065565021adc8

src/surface-contracts.mjs
  0f99e3f883df7ab3c190d31c6a544289e25da3d05a0e1c83246742942dfca335
  -> 9d5dc53098f843e7073f5c7c26fd10d4e2aa57dddb17c5458002138d295dc5f0

test/public-surface-registration.mjs
  4e55dc32a94ef0fb3025dda4d6896d3eb5b9fb06e34112aba09f7d473e061227
  -> a7450e461539ea2ff778fca8d23a3b2c084d98c93a19594c94af8e28450213ce
```

Every other integration source/test file is byte-identical to preview.18. The surface-contract change is only the preview.19 version marker.

## 3. Schema correction

Preview.18 used a top-level Zod discriminated union because there were two actions. Both actions, however, intentionally have the same field set. Preview.19 therefore expresses the exact same semantic authority as one strict object:

```text
action     enum [restart_codexless, status]
requestId  string, min 1, max 128, stable-id regex
strict     true
```

This removes the top-level `oneOf` without adding any caller field or action.

## 4. Actual MCP wire-schema regression

`public-surface-registration.mjs` now creates the actual MCP server, attaches linked `InMemoryTransport` endpoints from the installed MCP SDK, and sends:

```text
initialize
notifications/initialized
tools/list
```

It then reads the serialized `codex.runtime_maintenance.inputSchema` and requires:

```text
type == object
no top-level oneOf
properties == [action, requestId]
required == [action, requestId]
additionalProperties == false
action.enum == [restart_codexless, status]
requestId.type == string
requestId.minLength == 1
requestId.maxLength == 128
requestId.pattern == ^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$
```

Observed result:

```text
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS flat-object-required-enum-additionalProperties-false
```

This closes a test gap in preview.18: the previous registration test proved server-side Zod strictness but did not assert the shape serialized through MCP `tools/list`.

## 5. Staged public compatibility regressions

A complete preview.19 staging tree was made from the active preview.18 installed source/config/tests and overlaid with the candidate. Syntax checks passed, followed by:

```text
BOUNDED_GIT_FETCH_ORIGIN=PASS tools=62
BOUNDED_GIT_PULL_FF_ONLY=PASS tools=62
FILE_LINK_REGRESSION=PASS tests=10
RUNTIME_MAINTENANCE_WIRE_SCHEMA=PASS flat-object-required-enum-additionalProperties-false
PUBLIC_SURFACE_REGISTRATION=PASS tools=62
DOCUMENT_FILE_READ_REGRESSION=PASS tests=7
DOCUMENT_RESOURCE_LINK_REGRESSION=PASS tests=9
DOCUMENT_RENDER_REGRESSION=PASS tests=10
IMAGE_READ_REGRESSION=PASS tests=7
PREVIEW19_STAGED_CORE_REGRESSIONS=PASS scripts=8
```

## 6. Lifecycle compatibility

The schema-only candidate leaves runtime semantics unchanged. The existing lifecycle evidence was rerun successfully:

```text
RUNTIME_MAINTENANCE_REGRESSION=PASS tests=12
DETACHED_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=7
ONE_SHOT_RUNTIME_MAINTENANCE_REGRESSION=PASS tests=6
PREVIEW19_LIFECYCLE_COMPATIBILITY=PASS suites=3 probes=3
```

The three functional probes again qualified exact-instance replacement, direct pre-restart acceptance/idempotency, and private authenticated graceful shutdown behavior.

## 7. Production non-mutation boundary

After qualification:

```text
live version     0.1.1-preview.18-runtime-maintenance
live toolCount   62
live surface     codexless-public-preview-v2
tunnel health    live
tunnel ready     ready
```

No live source publication, restart, or `codex.runtime_maintenance` mutation occurred.

The next gate is a guarded preview.19 publication preflight. After publication/activation, a refreshed fresh ChatGPT conversation must prove that the flat schema is now projected structurally before the first live self-restart is attempted.

```text
PREVIEW19_FLAT_SCHEMA_CANDIDATE=PASS
WIRE_SCHEMA=PASS
LIVE_MUTATION=false
NEXT=GUARDED_PUBLICATION_PREFLIGHT
```
