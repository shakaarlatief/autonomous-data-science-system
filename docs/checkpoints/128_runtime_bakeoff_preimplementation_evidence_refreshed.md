# Checkpoint 128: Runtime Bakeoff Pre-implementation Evidence Refreshed

**Date:** 2026-08-21  
**Status:** Historical design/evaluation checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Post-V0 V1 bounded implementation and integration  
**Scope:** Records the fresh official-source runtime/MCP audit immediately before Specification 005 implementation and establishes the evidence-based first implementation order without selecting a runtime.  
**Authority:** Historical provenance. Research 010 contains the detailed refreshed ecosystem evidence; Specification 005 remains the candidate evaluation contract and no runtime is accepted by this checkpoint.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Transition into the runtime bakeoff

Checkpoint 127 closed the governed reusable-knowledge persistence/interchange seam. The immediate project priority therefore moved to Specification 005.

Because runtime/framework APIs are fast-moving, Research 001 was refreshed against current official documentation before executable implementation.

Detailed source:

```text
docs/research/010_2026_runtime_bakeoff_preimplementation_refresh.md
```

---

## 2. MCP baseline reconfirmed

The final MCP `2026-07-28` specification is now published.

Current direction remains compatible with Specification 005:

```text
stateless protocol core
current request/response tool interoperability
no new dependency on deprecated Roots
no model-provider abstraction through deprecated Sampling
no observability architecture built on deprecated MCP Logging
```

The runtime bakeoff should use a local side-effect-free MCP server and evaluate MCP as an external tool/resource interoperability seam.

---

## 3. First implementation order

The refreshed evidence justifies implementation ordering, not runtime selection:

```text
CONTROL
    ADS-owned direct model-call runtime

FIRST FRAMEWORK CANDIDATE
    OpenAI Agents SDK

SECOND FRAMEWORK CANDIDATE
    LangGraph

SECONDARY / CONDITIONAL EXECUTABLE CANDIDATES
    Microsoft Agent Framework
    Google ADK 2.0
```

Reasoning:

```text
OpenAI Agents SDK
    current native approval interruptions
    serializable RunState
    MCP integration
    model/tool timeouts and retry controls
    deterministic provider-neutral ScriptedModel testing
    relatively small runtime surface

LangGraph
    strongest durability/checkpoint comparator
    explicit persistence and interrupt semantics
    Functional API can minimize graph intrusion
    side-effect/replay semantics must be tested carefully

Microsoft Agent Framework
    credible provider/MCP/HITL/checkpoint surface
    Python Functional Workflow API currently experimental

Google ADK 2.0
    GA workflow framework and MCP/session support
    Tool Confirmation currently experimental
    resumability documented as best-effort / at-least-once
```

Specification 005 already permits early elimination/deprioritization and does not require equal implementation effort.

---

## 4. No framework is selected

This checkpoint does not accept:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK
any multi-agent architecture
any LLM provider/model
any durable runtime backend
```

Direct model calls remain an explicit control and valid final architecture outcome.

---

## 5. ADS-owned harness first

Before framework adapters, the executable bakeoff should define an experiment-level ADS-owned contract for:

```text
canonical workload input
bounded project/context snapshot
bounded methodological context pack
exact knowledge revision IDs
structured recommendation/result
approval interruption
resume token
normalized trace
at-most-once proposal side-effect ledger
fake deterministic model behavior
local MCP reference lookup
AR-01 through AR-12 evidence
```

Framework-specific types must stay below adapter boundaries and outside `ads_system.domain`.

These experiment types do not automatically become the final production `ReasoningRuntime` interface.

---

## 6. Promotion audit

### Durable research

Research 010 is warranted because it updates rapidly changing ecosystem facts immediately before implementation.

### No Specification 005 promotion yet

The existing mandatory AR-01 through AR-12 gates remain appropriate. The refreshed research changes implementation order and current API assumptions, not the core evaluation question.

### No D-series decision

No runtime or provider has been selected.

### No foundation change

The existing ADS/domain versus runtime-infrastructure boundary remains intact.

---

## 7. Exact continuation

```text
1. create an isolated runtime-bakeoff implementation branch
2. implement ADS-owned deterministic harness and fixtures
3. implement direct-call control
4. implement OpenAI Agents SDK adapter with fake-model infrastructure first
5. test AR-01 through AR-12 where possible without paid calls
6. implement LangGraph durability comparator unless evidence already falsifies the path
7. decide from evidence whether Microsoft/Google executable adapters are still decision-relevant
8. use live provider calls only for behavior that deterministic infrastructure cannot establish
9. preserve a direct-call/no-framework outcome as legitimate
```
