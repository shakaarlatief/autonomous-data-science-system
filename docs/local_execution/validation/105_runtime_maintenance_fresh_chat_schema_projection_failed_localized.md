# Validation 105: Runtime Maintenance Fresh-Chat Schema Projection Failure Localized

**Date:** 2026-09-07
**Status:** FAIL / CHATGPT HOST GENERICIZED TOP-LEVEL UNION SCHEMA / NO MUTATION
**Research:** Research 122
**Scope:** Determine whether a refreshed fresh ChatGPT conversation preserves the narrow live preview.18 runtime-maintenance schema strongly enough to authorize the first production self-restart qualification.

## 1. Fresh-host procedure

The user refreshed the existing ADS developer MCP app, opened a completely fresh disposable conversation, and requested discovery only. The prompt explicitly forbade invoking `codex.runtime_maintenance`, `command_exec`, or any other ADS tool.

The fresh conversation reported `codex.runtime_maintenance` as exposed. Therefore AB-008's stale-same-chat projection issue did not block discovery in this new conversation.

## 2. Host-projected schema

The callable definition visible to the fresh ChatGPT conversation was:

```text
type codex.runtime_maintenance = (_: {
  [key: string]: any
}) => any;
```

Consequences at the host projection layer:

```text
tool presence                              PASS
action enum structurally projected         FAIL
requestId structurally marked required     FAIL
additionalProperties=false visible         FAIL
arbitrary-key rejection host-certifiable   FAIL
```

The description still stated that the tool accepts only a stable `requestId` and the bounded restart/status semantics, but descriptive prose is not a substitute for a mutation-sensitive callable schema.

The fresh chat therefore correctly finished with:

```text
RUNTIME_MAINTENANCE_FRESH_CHAT_DISCOVERY=FAIL
```

## 3. Server-side contract remains narrow

Before this fresh-host test, Validation 104 independently queried the active local MCP server and observed the exact `tools/list` schema. Preview.18 serializes a closed top-level `oneOf` with two strict branches:

```text
{ action: restart_codexless, requestId }
{ action: status,            requestId }
```

Each branch requires both fields and has `additionalProperties: false`. No production runtime source changed during the fresh-host discovery.

Therefore the evidence classifies the failure as:

```text
server validation / MCP wire schema     NARROW / PASS
ChatGPT host callable projection         GENERICIZED / FAIL
runtime-maintenance mutation             NOT ATTEMPTED
```

## 4. Corroborating projection pattern

The current ChatGPT projection also exposes the older `codex.workspace_authority` as:

```text
type codex.workspace_authority = (_: { [key: string]: any }) => any;
```

That server tool is likewise backed by a top-level `z.discriminatedUnion(...)`. In contrast, ordinary `z.object(...).strict()` tools such as `codex.command_exec` and `codex.document_read` retain structured host-visible arguments.

This is sufficient to justify a compatibility correction without claiming a universal host implementation rule. For the current observed host, a top-level union/`oneOf` is not accepted as a safe projection shape for this mutation-sensitive tool when an equivalent flat object can express the contract.

## 5. Safety decision

The first live `restart_codexless` qualification is blocked. The server could still reject unknown input at execution time, but Research 122 requires the ChatGPT-facing callable surface itself to be narrow enough to inspect before granting the new lifecycle authority.

The correction must preserve the same server semantics using one strict top-level object with:

```text
action     enum [restart_codexless, status]
requestId  required bounded string
additionalProperties false
```

No live restart or other mutation was invoked in this qualification.

```text
FRESH_CHAT_TOOL_DISCOVERY=PASS
FRESH_CHAT_SCHEMA_FIDELITY=FAIL
SERVER_AUTHORITY_WIDENED=false
LIVE_MUTATION=false
NEXT=PREVIEW19_FLAT_SCHEMA_QUALIFICATION
```
