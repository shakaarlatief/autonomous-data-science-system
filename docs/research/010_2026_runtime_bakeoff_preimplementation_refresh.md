# Research 010: 2026 Runtime Bakeoff Pre-implementation Refresh

**Date:** 2026-08-21  
**Status:** Current external-ecosystem implementation research  
**Scope:** Fresh official-source audit of Specification 005 candidates immediately before executable runtime-bakeoff implementation  
**Authority:** Current implementation guidance only. Specification 005 remains the candidate evaluation contract; no runtime is selected by this memo. Rapidly changing external API details must be rechecked when adapter code is written.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why refresh the ecosystem research now

Research 001 was intentionally written as a rapidly changing ecosystem audit. The project has since completed two major V1 boundaries:

```text
Project Cockpit interaction architecture
    -> promoted through Specification 008 / Checkpoint 126

governed reusable-knowledge persistence/interchange
    -> closed across SQLite/Linux, SQLite/Windows, PostgreSQL 18
    -> Checkpoint 127
```

Specification 005 is therefore now the immediate execution track.

Before adding runtime dependencies, its external claims were refreshed against current official documentation on 2026-08-21.

The purpose of this memo is not to pick a framework from documentation. It is to determine:

```text
which candidates are mature enough to implement first
which Specification 005 gates have direct current support
which risks need executable tests rather than assumptions
how to keep the bakeoff framework-neutral
```

---

## 2. Current MCP protocol baseline

The final MCP specification `2026-07-28` is now published.

Current official protocol direction includes:

```text
stateless core
no required initialize/initialized handshake
no protocol-level session identifier
server/discover optional capability discovery
self-describing requests
header-based routing
cacheable deterministic list results
Multi Round-Trip Requests
extensions framework
Tasks extension
authorization hardening
```

Roots, Sampling, and Logging are formally deprecated under SEP-2577. They remain temporarily supported for compatibility, but new implementations should not depend on them.

ADS implication:

```text
runtime bakeoff MCP server/client
    -> local and side-effect-free
    -> current tool/resource interoperability only
    -> no architectural dependency on Roots
    -> no model-provider abstraction through Sampling
    -> no observability dependency on MCP Logging
```

This confirms Specification 005's MCP direction rather than changing it.

Official sources checked:

```text
https://blog.modelcontextprotocol.io/posts/2026-07-28/
https://modelcontextprotocol.io/seps/2577-deprecate-roots-sampling-and-logging
https://py.sdk.modelcontextprotocol.io/v2/handlers/sampling-and-roots/
```

---

## 3. OpenAI Agents SDK

### 3.1 Current shape

The Python Agents SDK remains deliberately small around:

```text
Agent
Runner
function tools
MCP tools
sessions
human approval
RunState
tracing
structured output
```

The SDK uses the Responses API by default for OpenAI models but explicitly documents direct Responses API use as preferable when the application wants to own its own loop/tool/state handling.

That distinction is useful for this bakeoff because direct model calls remain the control, not a strawman.

### 3.2 Specification 005 support visible in current official docs

Strong direct evidence exists for:

```text
AR-02 single-agent tool loop
    Runner owns model/tool loop

AR-03 MCP
    local stdio and Streamable HTTP MCP support
    tool filtering and structured content support

AR-04 approval interrupt
    function tools can declare needs_approval
    pending calls surface as structured interruptions

AR-05 durable resume
    RunResult -> RunState
    RunState serializes to JSON/string
    paused state can be recreated and resumed

AR-07 context transparency
    explicit run context remains application-supplied
    serialized context behavior is documented

AR-08 timeouts
    per-model-call timeout
    per-async-function-tool timeout

AR-09 retries
    opt-in runner-managed model retry policies
    replay-safety metadata exposed to retry policy

AR-10 structured output
    Agent output types are schema validated

AR-11 observability
    built-in tracing plus usage/run information

AR-12 deterministic testing
    current testing package includes ScriptedModel and provider-neutral in-memory utilities
    no live API request required for orchestration tests
```

The current testing documentation is especially important. It materially reduces the risk that infrastructure testing requires paid model calls.

### 3.3 Durable-resume caution

`RunState` is a runtime state object and may include SDK-managed metadata, approvals, usage, tool input, nested-agent resumptions, trace metadata, and application context.

ADS must therefore persist it, if used, only as runtime execution state:

```text
runtime checkpoint
    references ADS run/project/context identities
    !=
ADS Project / Finding / Decision authority
```

Longer-lived durability can additionally use documented integrations such as Dapr, Temporal, Restate, or DBOS, but those must not enter the first bakeoff unless plain serialized `RunState` cannot satisfy AR-05.

### 3.4 Current implementation assessment

```text
First-round implementation priority: HIGH
Reason:
    smallest direct path across most mandatory gates
    strongest current deterministic test support
    native approval + resumable state + MCP in one Python runtime
```

This is implementation ordering, not selection.

Official sources checked:

```text
https://openai.github.io/openai-agents-python/
https://openai.github.io/openai-agents-python/human_in_the_loop/
https://openai.github.io/openai-agents-python/ref/run_state/
https://openai.github.io/openai-agents-python/mcp/
https://openai.github.io/openai-agents-python/models/
https://openai.github.io/openai-agents-python/tools/
https://openai.github.io/openai-agents-python/testing/
```

---

## 4. LangGraph

### 4.1 Current shape

LangGraph remains explicitly persistence-oriented.

Its checkpointer saves state at execution boundaries and supports:

```text
human-in-the-loop
pause/resume
fault tolerance
pending writes
replay/time travel
thread-scoped history
```

The Functional API remains particularly relevant for ADS because it can express durable execution around ordinary Python functions/tasks rather than forcing the ADS domain into a graph ontology.

### 4.2 Specification 005 support visible in current official docs

Strong direct evidence exists for:

```text
AR-04 approval/HITL
    interrupt() pauses and surfaces JSON-serializable payload

AR-05 durable resume
    persistent checkpointers + thread_id
    task outputs persisted and reused on resume

AR-08 timeout
    async task/entrypoint timeout support documented

AR-09 retry/failure
    retry policies and fault-tolerance mechanisms

AR-03 MCP
    official LangChain MCP adapters expose MCP tools to agents/workflows

AR-10 structured output
    structured-response schemas through LangChain agents/models
```

### 4.3 Critical replay/idempotency behavior

LangGraph's interrupt semantics are especially important for AR-05 and AR-09:

```text
interrupt occurs inside a node
    -> node is restarted from the beginning on resume
```

Therefore code executed before the interrupt may execute again.

Official guidance explicitly requires side effects before an interrupt to be idempotent.

The Functional API's persisted `@task` results can avoid recomputing completed work when the same resumable sequence is replayed, but side-effecting tasks must still be designed carefully.

For ADS this is not necessarily a defect. It is a concrete semantic constraint that the bakeoff must test against:

```text
approval-gated proposal creation
    -> executes at most once
```

### 4.4 Maturity caution

Some newer node-level fault-tolerance surfaces in current LangGraph documentation are marked as requiring `langgraph>=1.2`, currently alpha. The bakeoff should distinguish stable functionality needed by AR-01 through AR-12 from optional alpha conveniences.

### 4.5 Current implementation assessment

```text
First-round implementation priority: HIGH
Reason:
    strongest durability comparator
    explicit persisted-task semantics
    provider-neutral runtime shape
    useful contrast against smaller agent-loop SDK
```

Official sources checked:

```text
https://docs.langchain.com/oss/python/langgraph/persistence
https://docs.langchain.com/oss/python/langgraph/interrupts
https://docs.langchain.com/oss/python/langgraph/functional-api
https://docs.langchain.com/oss/python/langgraph/use-functional-api
https://docs.langchain.com/oss/python/langgraph/fault-tolerance
https://docs.langchain.com/oss/python/langchain/mcp
https://docs.langchain.com/oss/python/langchain/structured-output
```

---

## 5. Microsoft Agent Framework

### 5.1 Current shape

Current Microsoft documentation separates simple agents from workflows and offers:

```text
function tools
local and hosted MCP tools
structured output
multiple model providers
HITL request/response
workflow checkpoints
functional and graph workflow APIs
```

The current provider matrix includes OpenAI, Azure OpenAI, Foundry, Anthropic, Ollama, Foundry Local, GitHub Copilot, and custom provider shapes, with capability differences by provider.

### 5.2 Positive Specification 005 evidence

Current docs support:

```text
AR-03 MCP
    local MCP integration in Python

AR-04 HITL
    workflow request/response mechanisms

AR-05 checkpoints
    workflow checkpoints capture executor state, pending messages,
    pending requests/responses, and shared state

AR-10 structured output
    Python supports Pydantic or JSON-schema response formats where provider supports them

AR-12 provider substitution direction
    multiple provider clients and custom provider surface
```

### 5.3 Maturity caution

The current workflow documentation states:

```text
Functional Workflow API (Python)
    experimental

Workflow Builder / graph execution
    supported fixed-topology workflow path
```

For ADS, the Functional API would be conceptually attractive because it minimizes graph-shaped framework intrusion, but its experimental status weakens it as the first candidate to implement when two mature contenders already cover the primary design space.

### 5.4 Current implementation assessment

```text
First-round implementation priority: SECONDARY
Do not eliminate.
Implement after OpenAI Agents SDK / LangGraph if:
    they fail mandatory gates
    or
    Microsoft-specific behavior appears capable of changing the selection
```

Official sources checked:

```text
https://learn.microsoft.com/en-us/agent-framework/
https://learn.microsoft.com/en-us/agent-framework/workflows/
https://learn.microsoft.com/en-us/agent-framework/workflows/checkpoints
https://learn.microsoft.com/en-us/agent-framework/workflows/human-in-the-loop
https://learn.microsoft.com/en-us/agent-framework/agents/providers/
https://learn.microsoft.com/en-us/agent-framework/agents/structured-outputs
https://learn.microsoft.com/en-us/agent-framework/agents/tools/local-mcp-tools
```

---

## 6. Google Agent Development Kit 2.0

### 6.1 Current shape

ADK Python 2.0 reached GA on 2026-05-19.

Its current workflow surface includes:

```text
graph-based workflows
dynamic code-based workflows
collaborative/multi-agent workflows
sessions
persistent DatabaseSessionService
MCP client/server tooling
human-input workflow nodes
model/provider adapters
schema-constrained agent data
```

### 6.2 Positive Specification 005 evidence

Current docs support:

```text
AR-03 MCP
    McpToolset consumes external MCP servers
    stdio / broader MCP integration patterns available

AR-04 human input
    ADK 2.0 workflow RequestInput nodes
    tool-confirmation mechanism also exists

AR-05 persistence/resume direction
    persistent session services
    resumable workflow support

AR-10 structured output
    input/output schema support using Pydantic

AR-12 provider breadth
    direct Google models plus LiteLLM connector / other model integrations
```

### 6.3 Important current limitations for this bakeoff

Two official details matter directly to Specification 005:

```text
Tool Confirmation
    currently marked Experimental

ResumabilityConfig
    documented as best-effort
    resumed tools should be idempotent
    execution semantics are at-least-once
```

The latter is a direct tension with AR-05's test requirement that the approval-gated side effect execute at most once. ADS could add its own idempotency key/application boundary, but the bakeoff must then count that extra application burden rather than attributing exactly-once behavior to ADK.

ADK also warns that `output_schema` plus tools is supported reliably only by specific models, including Gemini 3.0. That makes AR-10 provider-independent structured result handling worth testing carefully instead of assuming it from schema support alone.

### 6.4 Current implementation assessment

```text
First-round implementation priority: SECONDARY
Do not eliminate.
Reason for deferral:
    2.0 itself is GA
    but approval surface is partly experimental
    and documented resume behavior requires explicit at-least-once/idempotency handling
```

Official sources checked:

```text
https://adk.dev/2.0/
https://adk.dev/mcp/
https://adk.dev/tools-custom/confirmation/
https://adk.dev/workflows/human-input/
https://adk.dev/agents/llm-agents/
https://adk.dev/sessions/session/
https://adk.dev/agents/models/litellm/
```

---

## 7. First-round implementation order

The documentation refresh supports the following **evaluation order**, not a runtime decision:

```text
CONTROL
    ADS-owned direct model-call runtime

FIRST IMPLEMENTED FRAMEWORK CANDIDATE
    OpenAI Agents SDK

SECOND IMPLEMENTED FRAMEWORK CANDIDATE
    LangGraph Functional API / minimal durable shape

SECONDARY CANDIDATES
    Microsoft Agent Framework
    Google ADK 2.0
```

Why this is methodologically preferable:

```text
OpenAI Agents SDK
    tests whether a small agent-loop runtime earns its dependency

LangGraph
    tests whether stronger native durability earns a larger runtime surface

Direct-call control
    prevents framework adoption from becoming the default answer

Microsoft / Google
    remain available if leading candidates fail or if a specific capability
    could plausibly change the decision
```

Equal implementation effort is not required by Specification 005.

---

## 8. ADS-owned bakeoff architecture before framework adapters

The first executable slice should define a deliberately narrow ADS-owned test contract before importing any candidate package into production application/domain modules.

Candidate experiment-level types:

```text
ProjectContextSnapshot
MethodologicalContextPack
RuntimeWorkloadInput
RuntimeRecommendation
RuntimeInterrupt
RuntimeTrace
RuntimeResumeToken
RuntimeOutcome
```

Candidate experiment-level runtime interface:

```text
run(workload)
resume(resume_token, approval_decision)
cancel(run_id)
```

The final production `ReasoningRuntime` port is **not** frozen by these names.

The harness should own:

```text
canonical workload fixture
ADS-owned structured expected output
context-pack digest
exact knowledge revision list
at-most-once proposal side-effect ledger
fake deterministic model script
local side-effect-free MCP server
normalized trace/evidence record
AR-01 through AR-12 assertions
```

Candidate framework adapters should own only translation between this contract and framework-specific runtime concepts.

Framework-specific dependencies should initially live in experiment-specific optional dependency groups or isolated experiment environments rather than becoming unconditional ADS runtime dependencies.

---

## 9. Mandatory direct-call control

The direct-call control is not merely a fallback sentence in the final report. It should execute the same representative workload wherever technically meaningful.

Its purpose is to measure what framework infrastructure actually buys us.

The direct-call control may need ADS-owned implementations for:

```text
tool loop
approval state machine
resume token
retry/cancellation policy
MCP adapter
trace normalization
```

That implementation effort is itself evidence.

The control should remain deliberately small rather than recreating a general agent framework.

---

## 10. Evidence to collect per candidate

Do not collapse the bakeoff into one numeric score.

For each candidate record:

```text
mandatory gate
    PASS / FAIL / PARTIAL / NOT TESTED

framework code required
ADS-owned glue required
extra persistence/runtime infrastructure required
framework-specific types crossing the adapter boundary
whether fake-model tests are first-class or improvised
whether approval is native or application-built
whether process-boundary resume replays completed work
how side-effect at-most-once behavior is achieved
how exact context-pack/revision provenance is recovered
provider coupling
MCP protocol compatibility/path
stable versus experimental APIs used
observed dependency and operational burden
```

A framework can pass every feature checkbox and still lose if it requires materially more coupling or operational machinery than the workload needs.

---

## 11. Current conclusion

Fresh official documentation does not justify selecting a runtime yet.

It does justify a narrower implementation plan:

```text
1. build ADS-owned deterministic bakeoff harness
2. implement direct-call control
3. implement OpenAI Agents SDK adapter
4. implement LangGraph adapter if OpenAI does not already fail decisively
5. evaluate the evidence before deciding whether Microsoft/Google need executable adapters
6. preserve "no framework" as a first-class possible result
```

The next repository action should therefore be the executable bakeoff harness, not another generic framework comparison memo.
