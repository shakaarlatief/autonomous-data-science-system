# Checkpoint 133: V1 reasoning runtime selected and bakeoff closed

**Date:** 2026-08-22  
**Status:** Architecture promotion completed  
**Checkpoint class:** ARCHITECTURE_PROMOTION  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Promotes the initial V1 reasoning-runtime selection after the complete direct-call, OpenAI Agents SDK, and LangGraph evidence and closes Specification 005 for the current selection question.  
**Authority:** Promotion record. D-032 is the accepted runtime decision and Specification 005 v0.2 is the executed evaluation contract for this scope.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Promotion

D-032 is now accepted:

```text
Initial V1 reasoning runtime
    OpenAI Agents SDK

Validated starting package
    openai-agents==0.19.4

Architecture boundary
    ADS-owned ReasoningRuntime port
        -> OpenAI Agents adapter
        -> SDK runtime infrastructure
```

The package version is a validated baseline, not a permanent freeze.

## 2. Evidence used

The selection is based on executable ADS-shaped evidence rather than framework feature lists.

### Direct model-call control

```text
Checkpoint 129
workflow 32500521858
Ubuntu PASS
Windows PASS
```

The control proves that ADS can remain framework-independent, but it also exposes the generic runtime machinery ADS would otherwise have to own.

### OpenAI Agents SDK 0.19.4

```text
Checkpoint 131
workflow 32555526773
AR-01 through AR-12 PASS
Ubuntu PASS
Windows PASS
```

The candidate removes meaningful generic plumbing around model/tool iteration, tool schemas/dispatch, approval interruption, serializable/restorable RunState, structured output, stdio MCP, function-tool timeout, and lifecycle hooks while ADS retains semantic and authoritative state.

### LangGraph 1.2.10

Validated package set:

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
```

Validation:

```text
Checkpoint 132
workflow 32556382248
Ubuntu PASS, 9 comparator tests
Windows PASS, 9 comparator tests
```

LangGraph demonstrates a real durability advantage through explicit persistent checkpoints and replay-capable execution. It also requires a larger dependency/operational surface and preserves an explicit interrupt-node restart semantic that still requires ADS-owned side-effect idempotency.

## 3. Why OpenAI is selected

The current V1 need is primarily:

```text
one principal reasoner
bounded context
tool use
human approval
resume
structured recommendation
stable provenance
```

It does not yet require a general durable workflow engine, time-travel capability, many independently durable graph stages, or distributed multi-agent execution.

The OpenAI candidate is therefore the smallest complete framework candidate that removes substantial generic runtime burden without taking ownership of ADS project, methodological, governance, provenance, or authoritative side-effect semantics.

The direct-call control is too infrastructure-heavy for the preferred V1 path. LangGraph is stronger than currently necessary.

## 4. Stop rule for additional candidates

Research 015 concludes that Microsoft Agent Framework and Google ADK 2.0 do not currently expose a differentiator likely to overturn the three-way result.

They are therefore not implemented in this bakeoff.

This is not permanent rejection. Reopen if a future first-order requirement appears around:

```text
provider portability
stronger distributed/long-running workflow durability
empirically justified multi-agent collaboration
independently deployed agent systems
material selected-runtime maturity/API problems
```

## 5. Authority boundary remains unchanged

D-032 does not make the runtime the ADS brain or source of truth.

ADS still owns:

```text
Project/domain semantics
methodological knowledge and revisions
MethodologicalContextPack construction
context-pack digest and provenance
stale-context rejection
human-control and approval policy
application cancellation policy
authoritative side-effect idempotency and domain events
stable RuntimeTrace / operational provenance
runtime-state compatibility policy
```

Framework runtime state remains execution state.

MCP remains an external tool/resource interoperability boundary, not project memory or an internal ADS application bus.

## 6. Deliberate non-selections

This checkpoint does not select:

```text
final LLM provider
final model
multi-agent architecture
number of agents beyond single-principal-reasoner first
production durable runtime-state persistence schema
production MCP server/tool catalog
A2A
AG-UI final role
telemetry backend
cloud deployment
```

## 7. Specification closure

Specification 005 is updated to v0.2 and marked completed for the current V1 selection question.

Historical experiment evidence remains in:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
```

Detailed comparison and stop-rule reasoning remains in Research 015.

## 8. Promotion audit

Promoted/current layers:

```text
D-032
    accepted initial V1 reasoning runtime

Specification 005 v0.2
    executed and closed evaluation contract

OPEN_QUESTIONS.md
    Q-046 closed
    Q-009 and Q-021 reframed around the accepted runtime boundary
    Q-044 / Q-045 now immediate methodological priorities
```

No new Foundation is required. The architectural principle that runtime infrastructure is subordinate to ADS semantic authority was already established and is now concretely instantiated.

The runtime-bakeoff experiment code remains valuable as regression/compatibility evidence rather than being promoted wholesale into production architecture.

## 9. Exact continuation

The next highest-value V1 track is no longer another runtime adapter.

Proceed to:

```text
production retrieval / MethodologicalHorizon benchmark
    Q-044
    Q-045

1. inspect current production retrieval/persistence capabilities
2. define retrieval-quality fixtures and omission/relevance metrics
3. implement/evaluate lexical retrieval first
4. evaluate semantic retrieval as a candidate, not an assumption
5. use fusion/reranking only if measured evidence justifies it
6. construct the first bounded real MethodologicalHorizon
7. measure selective LLM context quality and cost
```

Do not select an embedding model, reranker, ANN service, or vector database from intuition.

Before starting that track, reconcile current routing and merge the completed `v1-runtime-bakeoff` branch into the promoted V1 branch after CI is green.