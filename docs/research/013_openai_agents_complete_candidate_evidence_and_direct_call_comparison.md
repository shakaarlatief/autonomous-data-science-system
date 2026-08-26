# Research 013: OpenAI Agents SDK 0.19.4 complete candidate evidence and direct-call comparison

**Date:** 2026-08-22  
**Status:** Current runtime-bakeoff evidence; no runtime selection  
**Scope:** Interprets the complete executable OpenAI Agents SDK 0.19.4 candidate against the previously validated direct model-call control under Specification 005.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Question

The relevant question is not whether OpenAI Agents SDK can run an agent.

The ADS-shaped question is:

> Does the SDK remove enough runtime-control burden or add enough durable interoperability/testability value to justify its dependency and coupling cost while ADS retains project, methodological, governance, provenance, and side-effect authority?

Specification 005 therefore compares the framework against an executable no-framework control rather than against an abstract baseline.

## 2. Evidence boundary

Direct model-call control:

```text
Checkpoint 129
workflow 32500521858
Ubuntu PASS
Windows PASS
```

Complete OpenAI candidate:

```text
openai-agents==0.19.4
validated commit 08c1c41246d8ece21e443d938ed477176505e40f
workflow 32555526773
Ubuntu complete candidate PASS
Windows complete candidate PASS
control/full Python suite PASS in the same run
```

Primary executable result:

```text
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
```

Research 011 remains the source for released-package/documentation compatibility findings discovered during implementation.

## 3. Mandatory Specification 005 result

The OpenAI 0.19.4 candidate now has executable PASS evidence for all mandatory gates:

```text
AR-01  domain isolation                         PASS
AR-02  single-principal-agent tool loop         PASS
AR-03  current MCP integration                  PASS
AR-04  human approval interrupt                 PASS
AR-05  process-boundary durable resume          PASS
AR-06  external ADS project-state authority     PASS
AR-07  context/revision transparency            PASS
AR-08  cancellation and bounded timeout         PASS
AR-09  controlled failure/retry behavior        PASS
AR-10  ADS-owned structured output              PASS
AR-11  normalized observability                 PASS
AR-12  deterministic provider substitution      PASS
```

The new evidence beyond the earlier core subgate is especially important.

### MCP

A real local stdio MCP subprocess is launched through the released `MCPServerStdio` integration. The principal agent discovers and calls the MCP methodological-reference tool. MCP remains an external interoperability boundary, not project memory or an internal ADS application bus.

### Cancellation and timeout

Application cancellation remains ADS-owned: an active SDK run is registered behind the experiment adapter and cancelled by ADS run identity. Separately, released SDK function-tool timeout behavior is exercised with a bounded async tool and `ToolTimeoutError`.

### Retry and replay

A side-effect-free read tool fails once and is retried by the model after the SDK exposes the failure as tool output. The authoritative proposal remains behind the ADS `ProposalLedger`. Repeated approved resume execution produces multiple execution attempts but one created proposal.

This preserves the durable rule:

```text
runtime replay semantics
    !=
authoritative exactly-once project meaning
```

### Observability

SDK lifecycle hooks are translated into the stable ADS `RuntimeTrace`. SDK/vendor tracing is disabled in the deterministic gate. Stable ADS provenance therefore does not depend on a framework-specific telemetry backend.

## 4. What OpenAI Agents SDK removes compared with direct calls

The executable comparison shows meaningful framework value around:

```text
model/tool iteration
function-tool schema generation and dispatch
approval interruption representation
serializable/restorable RunState
structured-output schema validation
native local MCP server exposure
function-tool timeout behavior
lifecycle hooks
```

The no-framework control can implement these behaviors, but it must own more orchestration machinery explicitly.

## 5. What the SDK does not remove

ADS must still own:

```text
project/domain/methodological semantics
bounded MethodologicalContextPack construction
context-pack digest and exact knowledge revisions
stale authoritative-context rejection
human-control policy
application cancellation policy
side-effect idempotency and domain-event persistence
stable normalized runtime trace/provenance
framework-state compatibility/version migration policy
adapter translation
```

Therefore the SDK is infrastructure, not the ADS brain or source of truth.

## 6. Costs and maturity evidence

The complete PASS does not erase costs observed during implementation.

Released `openai-agents==0.19.4` did not contain `agents.testing.ScriptedModel` even though current documentation advertised that surface. Deterministic testing required an experiment-local fake against the released public `Model` interface.

The released SDK also wraps the dataclass structured-output schema under a top-level `response` key before strict validation/unwrapping.

These are manageable costs, but they matter to dependency/API-maturity scoring.

## 7. Current comparison

```text
DIRECT CALL CONTROL
    smallest dependency surface
    maximum explicit control
    strong deterministic testability
    significant custom runtime machinery

OPENAI AGENTS SDK 0.19.4
    complete AR-01..AR-12 technical viability
    meaningful reduction in tool/approval/resume/MCP/timeout plumbing
    still requires ADS adapter/authority boundaries
    released API/documentation drift observed
```

Neither result alone answers the runtime selection question.

## 8. Why LangGraph remains decision-relevant

The strongest unresolved differentiator is durability/checkpoint semantics under interruption and replay.

LangGraph remains the planned comparator because it is specifically strong in persisted execution/checkpointing. Its interrupt semantics may restart an interrupted node, so the bakeoff must test whether that durability model is materially better for ADS and what idempotency/replay burden it creates.

The next candidate should therefore emphasize:

```text
process-boundary checkpoint/resume
interrupt/replay semantics
side-effect placement and idempotency
state ownership boundaries
provider-neutral deterministic testing
normalized ADS trace/provenance
```

If LangGraph does not produce a meaningful durability advantage, the remaining Microsoft/Google candidates should only be implemented if current evidence suggests they could plausibly change the final decision.

## 9. Current conclusion

OpenAI Agents SDK 0.19.4 is a **technically viable complete V1 runtime candidate**.

It is not selected.

The direct-call control is also viable. The next legitimate step is the LangGraph durability comparator, followed by an explicit evidence-based runtime/no-runtime decision or a bounded justification for testing additional candidates.
