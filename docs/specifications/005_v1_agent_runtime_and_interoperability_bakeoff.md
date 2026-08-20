# Specification 005: V1 Agent Runtime and Interoperability Bakeoff

**Date:** 2026-08-20  
**Status:** Candidate V1 evaluation specification v0.1  
**Scope:** Empirical selection of the first V1 reasoning/agent runtime and validation of MCP/HITL/durability/domain-isolation boundaries  
**Authority:** Candidate evaluation contract. No agent framework is accepted by this specification until the bakeoff is executed and promoted explicitly.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Purpose

The 2026 agent ecosystem now provides mature enough infrastructure that ADS should not build a generic agent loop, durable workflow engine, human-approval runtime, or external tool protocol without testing existing options first.

At the same time, selecting a framework from marketing feature lists would violate P-019 and the development method used successfully for the persistence architecture.

This specification defines a small ADS-shaped bakeoff.

The goal is:

> Select the smallest runtime that cleanly supports the reasoning/execution behavior V1 actually needs while keeping ADS domain/project state independent and replaceable.

---

## 2. Candidate set

Initial candidates:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google Agent Development Kit 2.0
```

The first implementation pass may eliminate a candidate early if basic installation/API maturity or a mandatory requirement clearly fails. Equal implementation effort is not required for dominated candidates.

Pydantic AI / Pydantic Graph remains a watchlist candidate rather than a mandatory first-round implementation because its current graph surface is still partly beta and the four candidates above cover the immediate runtime design space more directly.

---

## 3. Non-negotiable architecture boundary

No candidate may become the domain model.

Production ADS code should preserve a boundary conceptually similar to:

```text
ADS domain/application services
        |
        v
ReasoningRuntime port
        |
        +-> OpenAI Agents adapter
        +-> LangGraph adapter
        +-> Microsoft Agent Framework adapter
        +-> Google ADK adapter
```

The exact interface may change during the spike, but the following are forbidden as foundational coupling:

```text
framework Agent object stored as Project state
framework Session/Thread as Project identity
framework checkpoint replacing Finding/Decision history
framework message transcript becoming authoritative project memory
framework Graph node types leaking into methodological knowledge
framework tool definition becoming the only definition of an ADS execution capability
```

Runtime execution state is allowed and expected. It remains execution state.

---

## 4. Representative ADS workload

Every surviving candidate should implement the same logical workload.

### Input

```text
ProjectContextSnapshot
    project_id
    objective
    current relevant project facts
    unresolved Questions
    selected Findings

MethodologicalContextPack
    bounded candidate knowledge revisions
    exact revision identifiers
    retrieval/application rationale
    explicit hard constraints

UserIntent
    "What should we investigate next about missingness and validation?"
```

The test context should be small enough to inspect manually and should use the existing representative methodological corpus rather than arbitrary customer-support examples.

### Available capabilities

The reasoner receives:

```text
1 direct deterministic Python tool
    inspect_project_fact(key)

1 side-effect-free MCP tool
    lookup_methodological_reference(query)

1 approval-gated tool
    create_investigation_proposal(...)
```

The proposal tool does not silently run the investigation. It creates an ADS Proposal/Investigation candidate through an application boundary.

### Expected reasoning behavior

The runtime should be able to:

```text
reason over the bounded context
call one or more tools if useful
surface an approval interruption when required
resume after approval
return a structured recommendation/result
preserve enough trace information to reconstruct what context and knowledge revisions were used
```

---

## 5. Bakeoff gates

### AR-01: Domain isolation

Framework-specific types must remain beneath the runtime adapter boundary.

Pass criterion:

```text
ADS domain models and core application contracts import no candidate framework package.
```

### AR-02: Single-agent tool loop

One principal reasoner must complete the representative workload with normal function tools.

This gate is intentionally single-agent first.

### AR-03: Current MCP client integration

The candidate must call a test MCP server through either native integration or a narrow ADS MCP adapter compatible with the current protocol direction.

The implementation must not depend on MCP Roots, Sampling, or Logging, which are deprecated in the 2026-07-28 specification.

### AR-04: Human approval interrupt

An approval-gated tool call must pause without executing the side effect.

The caller must receive structured information sufficient to render an approval UI.

### AR-05: Durable resume after process boundary

The interrupted run must be serializable/checkpointable so it can be resumed after recreating the application process/runtime.

A candidate may use its native persistence or an officially supported durable integration.

Pass criterion:

```text
approved tool executes at most once
prior completed deterministic/random external work is not accidentally repeated
run continues to a correct final result
```

### AR-06: Project-state authority remains external

Pausing/resuming runtime state must not require moving ADS Findings/Questions/Decisions into the framework's authoritative store.

The runtime checkpoint may reference ADS IDs/revisions.

### AR-07: Context transparency

The test must record the exact context-pack identity or digest and exact knowledge revision IDs supplied to the model.

The framework must not silently append the complete project history merely because a session exists.

### AR-08: Cancellation and timeout

The application must be able to request cancellation and configure a bounded run/tool timeout behavior.

The exact semantics may differ by runtime but must be observable and testable.

### AR-09: Failure/retry behavior

A controlled tool failure must produce inspectable behavior.

Retry behavior must not duplicate an externally visible side effect.

### AR-10: Structured output

The result must be validated into an ADS-owned structured result type rather than parsed from unconstrained final prose.

### AR-11: Observability

At minimum, capture:

```text
run ID
model/provider identity
context-pack identity
knowledge revision references
tool calls and outcomes
approval interrupt/resume
input/output token usage where provider exposes it
latency
errors/retries
```

Framework-native tracing may be used, but the application must be able to preserve its own stable identifiers and eventually export operational telemetry independently.

### AR-12: Provider/test substitution

The architecture must permit deterministic/fake-model testing and must not require live paid model calls for every infrastructure test.

Provider portability should be assessed explicitly. Full provider equivalence is not required if a candidate clearly offers the best V1 runtime and remains isolated behind the port.

---

## 6. Optional multi-agent challenge

Do not start here.

Only after AR-01 through AR-12 pass for a candidate, add one optional specialist as a callable tool or subagent:

```text
Validation Specialist
```

The main reasoner should retain user-facing control and synthesis.

Purpose:

```text
measure integration complexity
measure context duplication
measure trace/provenance clarity
verify that specialist separation is possible without committing to it
```

This is not evidence that ADS should use multiple agents in production.

---

## 7. Comparison dimensions

Use qualitative evidence plus measured implementation/runtime facts.

```text
Domain isolation
API maturity/stability
Python ergonomics
Single-agent simplicity
Durable resume
HITL semantics
MCP compatibility
Context transparency
Structured outputs
Failure/retry control
Cancellation
Observability
Provider coupling
Local-first operation
Testability
Dependency/operational burden
Multi-agent escape hatch
Documentation quality
```

Avoid false precision. A small number of clearly explained categories is preferred to a meaningless 8.73 versus 8.61 score.

---

## 8. Expected likely contenders

Current research suggests two especially strong shapes:

```text
OpenAI Agents SDK
    smaller agent-loop integration surface
    strong tools / MCP / HITL / tracing
    durable execution available through supported integrations

LangGraph
    strongest built-in durable workflow/checkpoint model
    strong HITL / replay / recovery
    Functional API can preserve ordinary Python control flow
```

Microsoft Agent Framework and Google ADK remain credible. They should not be rejected from documentation alone because their explicit function/workflow/agent separation aligns well with ADS.

The bakeoff should be willing to stop early if evidence makes one option clearly preferable.

---

## 9. MCP-specific requirements

MCP is evaluated as a tool/resource interoperability seam, not as agent memory.

The test server should be local and side-effect-free.

V1 integration should follow the current 2026-07-28 direction:

```text
stateless protocol core
explicit request/response semantics
current Streamable HTTP or stdio support as appropriate
no dependency on deprecated sampling
no dependency on deprecated roots
no dependency on deprecated MCP logging
```

If a candidate framework lags the newest protocol, determine whether a narrow official MCP SDK adapter resolves the gap cleanly before rejecting the runtime.

---

## 10. AG-UI and A2A are outside the runtime winner gate

AG-UI belongs to the frontend-interaction spike and may be tested against the winning or leading runtime adapter.

A2A is intentionally not a selection requirement because ADS does not yet need independently deployed agent services.

A runtime does not receive extra credit simply for supporting A2A today.

---

## 11. No framework-specific project schema

The bakeoff must not add production project tables whose only purpose is to mirror a candidate runtime.

If durable runtime state requires persistence, use:

```text
runtime-specific execution store/projection
    or
narrow generic execution-state records
```

behind the runtime adapter.

Any project-level semantic result produced by the run enters the existing ADS application/domain path explicitly.

---

## 12. Promotion criterion

Select a V1 runtime only after at least one candidate passes the mandatory workload and the comparison demonstrates that its additional complexity is justified.

A valid outcome is:

```text
Use direct model/Responses-style calls for the first V1 slice because none of the runtimes adds enough value yet.
```

That outcome should remain possible. The bakeoff is designed to prevent framework adoption from becoming a foregone conclusion.

---

## 13. Current non-decisions

This specification does not yet choose:

```text
agent runtime
number of agents
LLM provider
model
MCP server catalog
durable runtime backend
A2A
AG-UI
telemetry backend
cloud deployment
```

The purpose of the bakeoff is to reduce these uncertainties with direct evidence.