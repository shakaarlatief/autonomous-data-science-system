# Research 001: 2026 Agentic Ecosystem and Integration Architecture Audit

**Date:** 2026-08-20  
**Status:** Current external-ecosystem research and architecture assessment  
**Scope:** MCP, agent runtimes, durable execution, human approval, A2A, AG-UI, observability, and implications for the Autonomous Data Science System  
**Authority:** Research evidence and current architecture guidance. Rapidly changing external technology claims should be rechecked before implementation decisions. Foundations 013, 017-020 and accepted project decisions remain authoritative for product/domain semantics.  
**Design session:** 02  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 02 - Methodological Brain & Knowledge Units

## 1. Why this audit exists

The project has deliberately delayed selecting an agent framework, orchestration runtime, LLM provider, frontend-agent protocol, or multi-agent architecture.

That delay is now useful. By August 2026, the agent ecosystem contains increasingly mature standards and runtimes that solve infrastructure problems we should not rebuild without evidence.

The question is therefore not:

```text
Which agent framework is most popular?
```

It is:

> Which parts of the Autonomous Data Science System are durable domain/product semantics that we must own, and which parts are commodity or emerging infrastructure that should be adopted behind replaceable boundaries?

This audit specifically tests whether the current work on methodological knowledge, project objects, provenance, revision history, governance, and selective context is redundant given modern agent technology.

The conclusion is no. Those concepts belong to a different architectural layer. However, several major future implementation areas should preferentially use standards or existing runtimes rather than custom infrastructure.

---

## 2. Layer map

The current ecosystem becomes clearer when separated by responsibility.

```text
PRODUCT / DOMAIN SEMANTICS
    ADS project objects
    methodological knowledge
    provenance and governance
    Questions / Evidence / Findings / Claims / Decisions
    methodological horizon semantics
    user-facing project workflows
            |
            v
REASONING / AGENT RUNTIME
    model loop
    tool dispatch
    handoffs / agents-as-tools where justified
    runtime interrupts
    run-local state
            |
      +-----+-------------------+
      |                         |
      v                         v
TOOL / RESOURCE INTEROP      REMOTE AGENT INTEROP
MCP                         A2A
      |                         |
      +------------+------------+
                   |
                   v
EXECUTION / EXTERNAL SYSTEMS
    Python / SQL / code execution
    GitHub / files / databases / APIs
    local / container / remote compute

FRONTEND INTERACTION PROTOCOL
    possible AG-UI adapter
    streaming / approvals / run events / UI intents

OBSERVABILITY
    application events
    OpenTelemetry-compatible traces/metrics where useful
    framework-native traces as supplementary views
```

The essential architectural rule is:

```text
protocol/runtime state
    !=
ADS project state
```

An agent runtime may remember how one agent execution should resume. It should not become the authority for what a Finding, Decision, Question, accepted knowledge revision, or project history means.

---

## 3. MCP

### 3.1 What MCP is

The Model Context Protocol is an interoperability protocol between AI applications and external capabilities. Current MCP servers expose capabilities such as tools, resources, and prompts.

For ADS, MCP is potentially valuable for integrations such as:

```text
GitHub
filesystems
databases and warehouses
documentation systems
cloud services
external APIs
execution services
specialized analytical services
```

MCP can also eventually make selected ADS capabilities available to other AI hosts.

### 3.2 Important 2026 protocol change

The 2026-07-28 MCP specification changed the architecture substantially. The protocol core is now stateless. It added Multi Round-Trip Requests, header-based routing, cacheable list results, an extensions framework, authorization hardening, and a Tasks extension.

The same release formally deprecated:

```text
Roots
Sampling
Logging
legacy HTTP + SSE transport
```

New ADS code should not build on those deprecated features.

Sampling should not be used as our model-provider abstraction. Direct provider/runtime integration is the recommended direction. Workspace roots should be explicit tool parameters, resource URIs, or server configuration rather than a core architectural assumption.

### 3.3 ADS conclusion for MCP

MCP should be treated as a first-class interoperability boundary, but not as an internal application bus.

Use direct Python/application calls where the capability is already an in-process ADS service. Introduce MCP where a standardized external integration boundary reduces bespoke coupling.

Candidate future direction:

```text
ADS ToolGateway
    direct function tools
    MCP client adapter
    other provider-specific hosted tools where justified
```

Potential later direction:

```text
ADS MCP server
    carefully scoped tools/resources
    explicit authorization
    no exposure of privileged project state merely because it is easy to serve
```

MCP does not replace methodological knowledge, project memory, governance, revision history, or the project object model.

---

## 4. Agent runtimes

Four current ecosystems deserve serious evaluation for V1 runtime/orchestration work.

### 4.1 OpenAI Agents SDK

Current capabilities include:

```text
agent loop
function and hosted tools
MCP tools
handoffs
agents-as-tools
sessions
streaming
human approval interruptions
serializable RunState
tracing
run hooks and guardrails
```

The SDK's runner loops model calls, tool calls, and handoffs until final output or an explicit limit. Current documentation also provides durable execution integration paths through Dapr, Temporal, Restate, and DBOS.

Strengths for ADS:

```text
small conceptual surface
very direct Python integration
strong single-agent/tool workflow
MCP support
built-in approval/resume support
useful tracing
agents-as-tools available without forcing decentralized multi-agent design
```

Risks/questions:

```text
OpenAI-centered default runtime/provider path
long-running durability is partly delegated to integrations
must prevent SDK sessions/run state from becoming project authority
must verify provider substitution requirements empirically
```

This is a strong V1 candidate, especially if the initial ADS reasoning loop remains deliberately small.

### 4.2 LangGraph

LangGraph is a low-level stateful agent/workflow runtime with explicit persistence. Its checkpointers save workflow state at execution steps and support:

```text
human-in-the-loop
pause/resume
fault tolerance
memory
replay/time travel
streaming
retryable tasks
```

The Functional API is particularly relevant because it can add persistence, tasks, interrupts, and streaming to ordinary Python control flow without forcing the entire ADS application into a graph-shaped domain model.

Strengths for ADS:

```text
strong durable execution model
mature interruption/resume semantics
provider-neutral orientation
Functional API reduces graph-framework intrusion
well suited to long analytical runs and approvals
```

Risks/questions:

```text
its checkpoint state could duplicate ADS project state if boundaries are weak
additional runtime concepts and persistence infrastructure
must prove that durability benefits justify framework complexity for V1
```

This is probably the strongest candidate if durable pause/resume and fault recovery become central early V1 requirements.

### 4.3 Microsoft Agent Framework

Current Agent Framework separates:

```text
Agents
Harness
Workflows
```

and supports multiple providers, MCP clients, workflow checkpointing, human-in-the-loop, and integrations including A2A and AG-UI.

Its current documentation makes a useful architectural recommendation:

> If a task can be handled as a normal function, use a function instead of an AI agent.

This aligns strongly with ADS's hybrid reasoning architecture.

Strengths for ADS:

```text
explicit agent-versus-workflow separation
multi-provider support
checkpointing and HITL
MCP / A2A / AG-UI integration surface
strong enterprise observability/type-safety orientation
```

Risks/questions:

```text
broad framework surface
rapidly evolving ecosystem
some Python workflow surfaces are still experimental
could be more infrastructure than the first V1 slice needs
```

It remains a credible bakeoff candidate rather than an automatic default.

### 4.4 Google Agent Development Kit 2.0

ADK 2.0 combines simple agents with graph workflows and multi-agent workflows. Current documentation emphasizes explicit graph paths that combine deterministic code with adaptive reasoning. It also supports MCP/A2A ecosystem integration and context compaction.

Strengths for ADS:

```text
deterministic + adaptive workflow philosophy
single-agent to graph/multi-agent growth path
MCP and A2A integration
context compaction aligns with V0 token lessons
multi-language ecosystem
```

Risks/questions:

```text
ADK 2.0 is relatively new
must assess Python maturity and local-first fit
must avoid binding ADS domain semantics to an ADK graph
some capabilities may be more Google-platform-oriented than V1 requires
```

It is a credible candidate, but adoption should follow workload-specific tests.

### 4.5 Pydantic AI / Pydantic Graph watchlist

Pydantic AI remains relevant because ADS is a typed Python application and Pydantic's evaluation/validation ecosystem is attractive. Current graph APIs include typed branching/workflow primitives, but parts of the graph surface remain explicitly beta.

It should remain on the watchlist. The first runtime bakeoff should prioritize the four candidates above unless later research shows a Pydantic AI capability that materially changes the comparison.

---

## 5. Single agent before multi-agent

Current OpenAI guidance recommends maximizing one agent before adding multiple agents because additional agents increase orchestration complexity and maintenance overhead.

This is consistent with our own Prototype V0 result. P0 showed that adding explicit machinery without sufficient incremental behavioral value can produce large cost increases.

ADS should therefore begin with the hypothesis:

```text
one capable reasoning runtime
    + bounded methodological horizon
    + explicit project state
    + well-defined tools
    + deterministic services and safeguards
```

Specialist agents should be introduced only when evaluations show a concrete failure mode such as:

```text
prompt/instruction complexity becomes unmanageable
tool selection quality degrades due to overlapping tools
specialized context materially improves quality/cost
independent reviewer separation is empirically useful
independent remote-agent interoperability becomes a real requirement
```

Even then, an `agent as tool` manager pattern may be preferable to decentralized handoffs because it preserves one user-facing coordinator.

The number of agents is an implementation outcome, not a product objective.

---

## 6. A2A

A2A 1.0 is now a stable open protocol for communication between independent, potentially opaque agent systems built with different frameworks, languages, or vendors.

Its role is distinct from MCP:

```text
MCP
    AI app/agent <-> tools/resources/context services

A2A
    independent agent system <-> independent agent system
```

A2A supports capability discovery, modality negotiation, collaborative task management, and communication without requiring access to another agent's internal memory/tools.

### ADS conclusion

Do not introduce A2A in the first V1 runtime solely because we may eventually have multiple agents.

Internal specialist agents inside one runtime do not need a remote interoperability protocol.

A2A becomes justified when ADS needs to consume or expose independently deployed agent services across process, framework, language, organizational, or trust boundaries.

Until then:

```text
A2A = extension path, not V1 core dependency
```

---

## 7. AG-UI and the frontend-agent seam

AG-UI is an open event-based protocol for bidirectional interaction between user-facing applications and agentic backends. It standardizes categories such as:

```text
messages
agent/run state
streamed events
tool activity
user interactions
approval workflows
UI intents
```

This is highly relevant because ADS requires a rich application interface, not just request/response chat.

Microsoft Agent Framework already documents AG-UI integration for remote HTTP clients, streaming, bidirectional state synchronization, approvals, and tool-based UI rendering.

### ADS conclusion

AG-UI should be evaluated before ADS invents a large custom frontend-agent event protocol.

However, the protocol is still evolving. It should not become the domain event model.

Preferred boundary:

```text
ADS application InteractionEvent / RunEvent model
            |
            +-> native web transport
            |
            +-> AG-UI adapter if the protocol passes the frontend spike
```

This protects the product from protocol churn while preserving interoperability.

AG-UI also should not determine what a Question, Finding, Evidence object, Decision, or methodological recommendation means. It transports interaction state; it does not define ADS domain semantics.

---

## 8. Durable execution and project state must remain separate

Modern runtimes can persist run state. ADS also has durable project state. These must not be collapsed.

The clean separation is:

```text
ADS project state
    current/historical analytical meaning
    Findings, Questions, Evidence, Decisions
    exact knowledge revision references
    artifacts/provenance

runtime execution state
    where this specific reasoning/workflow run paused
    tool results needed for resume
    approval interruption state
    retry/checkpoint information
    runtime-local conversation/agent state
```

A durable runtime checkpoint should reference the ADS project/context snapshot it used. It should not silently mutate or replace the project truth.

For long-lived pauses, resume logic should be able to detect that relevant authoritative project state changed while the run was suspended and decide whether to resume, refresh context, request review, or invalidate the stale run.

This is a stronger architecture than either:

```text
put all project state in the agent framework
```

or:

```text
rebuild durable agent execution ourselves inside project tables
```

---

## 9. Observability

Framework-native tracing is useful but should not be the only observability contract.

OpenTelemetry's 2026 GenAI semantic-convention work standardizes model calls, token usage, agent invocation, tool execution, retrieval, and related telemetry. The current MCP specification also points structured logging toward OpenTelemetry rather than maintaining MCP protocol logging.

ADS should therefore design an observability seam that can preserve project-specific provenance while exporting conventional operational telemetry.

Conceptually:

```text
ADS authoritative events/provenance
    exact knowledge/context/project references
            |
            +-> product history / audit views
            |
            +-> OpenTelemetry traces/metrics where useful
            |
            +-> framework-native trace viewers as supplementary tooling
```

Prompt/tool/result contents may contain sensitive project data and should be opt-in for telemetry rather than indiscriminately exported.

---

## 10. What ADS should own versus adopt

### ADS should own

```text
project object semantics
methodological knowledge semantics
knowledge governance and revisions
project Findings / Claims / Decisions
methodological horizon semantics
context-pack selection contract
information-legitimacy and validity concepts
project-to-knowledge provenance
user-facing methodological workflow semantics
```

### ADS should preferentially adopt or integrate

```text
agent loop/runtime
workflow durability/checkpointing
MCP client/server protocol machinery
A2A if remote independent agents become real
AG-UI if it passes the frontend interaction spike
OpenTelemetry-compatible operational tracing
frontend component/table/chart libraries
sandbox/container/runtime technologies
```

This means the architecture work already completed is not redundant. It defines the stable semantics that allow external infrastructure to remain replaceable.

---

## 11. Proposed application boundaries

Do not immediately add all of these as production interfaces. They are the architectural seams the next spikes should preserve.

```text
ReasoningRuntime
    run/resume/cancel one reasoning task
    receive explicit context pack
    expose structured result/events

ToolGateway
    direct application tools
    MCP tools
    explicit approval/permission metadata

InteractionStream
    normalized application/run events for frontend
    optional AG-UI mapping

RemoteAgentGateway
    absent until A2A is justified

TelemetrySink
    project-safe operational trace/metric export
```

The central requirement is that domain/application logic does not import framework-specific Agent/Graph/Session types.

---

## 12. Agent-runtime bakeoff

A generic feature comparison is insufficient. The bakeoff should execute one ADS-shaped workload through each serious candidate.

Candidate first round:

```text
OpenAI Agents SDK
LangGraph
Microsoft Agent Framework
Google ADK 2.0
```

The workload should test:

```text
bounded MethodologicalHorizon/context pack input
one reasoning turn
normal Python tool call
MCP tool call
human approval interrupt
serialize/persist and resume after process restart
cancellation and timeout
retry/failure semantics
trace exact knowledge revisions/context-pack identity supplied
no silent expansion into full project history
provider substitution or test-model substitution
project state remains external authority
optional specialist as tool, only after single-agent path passes
```

Evaluation dimensions:

```text
semantic/domain isolation
durability and resume correctness
context-control transparency
MCP ergonomics
HITL quality
observability
provider coupling
local-first operation
testability
failure recovery
API maturity
operational burden
amount of framework-specific state we must own
```

Do not award points for multi-agent features we do not need.

The expected result may be that one runtime clearly dominates for V1. If two approaches remain close, prefer the smaller integration surface and better domain isolation.

---

## 13. Current architecture recommendation

As of 2026-08-20:

```text
1. KEEP
   ADS project/domain/methodological architecture.

2. ADOPT AS A DIRECTION
   MCP as a standardized external tool/resource integration boundary.

3. TEST BEFORE SELECTING
   OpenAI Agents SDK vs LangGraph vs Microsoft Agent Framework vs Google ADK.

4. DEFER
   A2A until independently deployed agents become an actual requirement.

5. TEST IN FRONTEND SPIKE
   AG-UI as a frontend-agent interaction adapter.

6. AVOID
   building a bespoke general agent runtime, durable workflow engine,
   remote agent protocol, or large custom agent/frontend event protocol
   before the existing ecosystem has been evaluated against ADS workloads.

7. START SIMPLE
   one principal reasoner with tools, explicit ADS project state,
   and a bounded methodological horizon.
```

This is intentionally anti-lock-in. The agent runtime is infrastructure beneath ADS semantics, not the definition of the product.

---

## 14. External sources reviewed

Current official or primary documentation reviewed on 2026-08-20:

```text
MCP 2026-07-28 specification announcement
https://blog.modelcontextprotocol.io/posts/2026-07-28/

MCP TypeScript SDK migration notes
https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28

OpenAI Agents SDK
https://openai.github.io/openai-agents-python/
https://openai.github.io/openai-agents-python/running_agents/
https://openai.github.io/openai-agents-python/human_in_the_loop/

OpenAI practical guide to building agents
https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/

LangGraph persistence / Functional API / interrupts
https://docs.langchain.com/oss/python/langgraph/persistence
https://docs.langchain.com/oss/python/langgraph/functional-api
https://docs.langchain.com/oss/python/langgraph/interrupts

Microsoft Agent Framework
https://learn.microsoft.com/en-us/agent-framework/overview/
https://learn.microsoft.com/en-us/agent-framework/workflows/
https://learn.microsoft.com/en-us/agent-framework/integrations/ag-ui/

Google Agent Development Kit
https://adk.dev/
https://adk.dev/graphs/routes/
https://adk.dev/context/compaction/

A2A Protocol 1.0
https://a2a-protocol.org/latest/specification/
https://a2a-protocol.org/latest/announcing-1.0/

AG-UI
https://docs.copilotkit.ai/ag-ui/introduction

OpenTelemetry GenAI observability
https://opentelemetry.io/blog/2026/genai-observability/
```

Because this ecosystem is moving quickly, implementation-specific claims in this research note should be revalidated before dependency selection or production integration.