# Validation 116: Runtime Release Preview.20 Fresh-Chat Schema Qualified

**Date:** 2026-09-07
**Status:** PASS / HOST PROJECTION PRESERVES STRICT SEMANTIC RELEASE INPUT SHAPE
**Research:** Research 122
**Scope:** Record fresh ChatGPT host discovery of the live preview.20 `codex.runtime_release` tool and distinguish host-visible structural facts from description-only claims.

## 1. Fresh-chat result

The disposable qualification chat exposed `codex.runtime_release` and invoked no ADS tool.

Projected callable schema:

```text
type codex.runtime_release = (_: {
  action: "prepare" | "publish" | "verify" | "rollback" | "status",
  releaseId: string, // minLength: 1, maxLength: 128, pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
  requestId: string, // minLength: 1, maxLength: 128, pattern: /^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$/
  expectedSourceHead: string, // pattern: /^[0-9a-f]{40}$/
}) => any;
```

## 2. Structural findings

The host projection establishes:

```text
top-level form        structured named object
properties            action, releaseId, requestId, expectedSourceHead
all required          yes
action enum           prepare | publish | verify | rollback | status
releaseId             string, length 1..128, bounded identifier regex
requestId             string, length 1..128, bounded identifier regex
expectedSourceHead    string, exact lowercase 40-hex regex
generic map           absent
catch-all/index field absent
```

The rendered callable syntax does not separately expose the literal JSON-Schema keyword `additionalProperties: false`; that exact keyword is therefore not asserted from host discovery alone. The server-side wire regression from Validation 112 remains the evidence for that literal wire-schema property.

## 3. Authority surface

No structural caller field exists for:

```text
filesystem path or install root
destination
workspace selection
PID / arbitrary process selection
executable / command / argv
cwd / environment
URL / tunnel identity
credentials
permission profile / sandbox
regression command or list
arbitrary host-process/filesystem authority
```

The host-visible description independently describes the same narrow design, but description text is not substituted for structural schema evidence.

## 4. Annotations

No separate host-visible MCP annotations object was exposed. This is a statement about the ChatGPT projection, not proof that the server lacks internal annotations.

## 5. Live process cross-check

After the fresh-chat evidence was returned to the project conversation, direct local health still reported:

```text
version     0.1.1-preview.20-runtime-release
toolCount   63
surface     codexless-public-preview-v2
PID         41548
instanceId  ri_c8620c8dc49e8af26a2d0d7480c3cae1
tunnel      live / ready
```

## 6. Disposition

The host-schema blocker is closed for preview.20. The next qualification should use a real, separately preserved next-version release bundle rather than perform a synthetic mutation of preview.20 itself. That preserves the actual objective: demonstrate a normal future Codexless update end to end through the semantic release + semantic restart surfaces with no ordinary-host install helper.

```text
RUNTIME_RELEASE_PREVIEW20_FRESH_CHAT_SCHEMA=PASS
LIVE_MUTATION=false
NEXT=FIRST_SEMANTIC_RELEASE_BUNDLE
```
