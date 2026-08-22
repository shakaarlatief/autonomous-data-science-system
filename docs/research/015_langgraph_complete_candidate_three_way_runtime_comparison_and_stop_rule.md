# Research 015: LangGraph complete candidate, three-way runtime comparison, and bakeoff stop rule

**Date:** 2026-08-22  
**Status:** Current runtime-selection evidence  
**Scope:** Interprets the complete LangGraph 1.2.10 comparator alongside the validated direct-call control and OpenAI Agents SDK 0.19.4 candidate, then evaluates whether Microsoft Agent Framework or Google ADK 2.0 remain decision-relevant under Specification 005.  
**Authority:** Selection rationale only until promoted through an explicit decision.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Decision question

Specification 005 did not ask which framework has the largest feature list.

It asked:

> What is the smallest runtime that cleanly supports the V1 reasoning/execution behavior ADS actually needs while keeping project, methodological, governance, provenance, and authoritative side-effect state independent and replaceable?

The executable bakeoff now spans three meaningful points in the design space:

```text
ADS-owned direct model calls
    -> minimum dependency surface / maximum custom runtime ownership

OpenAI Agents SDK 0.19.4
    -> small agent-loop runtime with native approval, resumable state, MCP,
       structured output, timeout and lifecycle infrastructure

LangGraph 1.2.10
    -> stronger explicit persisted execution/checkpoint/replay machinery
       with a larger workflow and dependency surface
```

That is sufficient to evaluate the current V1 need without implementing every ecosystem candidate equally.

---

## 2. Evidence boundary

### Direct model-call control

```text
Checkpoint 129
workflow 32500521858
Ubuntu PASS
Windows PASS
```

Primary result:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
```

### OpenAI Agents SDK

```text
openai-agents==0.19.4
Checkpoint 131
workflow 32555526773
AR-01 through AR-12 PASS
Ubuntu PASS
Windows PASS
```

Primary result:

```text
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
```

### LangGraph

Validated package set:

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
```

Validated implementation head:

```text
c7f9f8bcb4ec367a3d30e5d2831db14a2aed8e53
```

Workflow:

```text
V1 runtime bakeoff
run 43 / 32556382248
```

Result:

```text
Ubuntu LangGraph comparator     PASS, 9 tests
Windows LangGraph comparator    PASS, 9 tests
control/full Python suite       PASS on both
OpenAI complete candidate       PASS on both
```

Primary result:

```text
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
```

---

## 3. Mandatory capability comparison

The two implemented framework candidates both satisfy the mandatory Specification 005 capability envelope.

```text
                                       DIRECT CALLS      OPENAI 0.19.4      LANGGRAPH 1.2.10
ADS domain isolation                   strong            PASS               PASS
single principal reasoner              viable            PASS               PASS
MCP                                    not core control   PASS               PASS
human approval                         ADS-built          PASS               PASS
durable process-boundary resume        ADS-built          PASS               PASS
external ADS project authority         strong            PASS               PASS
context/revision transparency          strong            PASS               PASS
cancellation / timeout                 ADS-built          PASS               PASS
failure / retry                        ADS-built          PASS               PASS
ADS-owned structured result            strong            PASS               PASS
normalized observability               ADS-built          PASS               PASS
deterministic provider-free tests      strong            PASS               PASS
```

The selection therefore turns on burden, durability semantics, maturity, and fit rather than missing feature checkboxes.

---

## 4. Direct calls remain a real option, not a strawman

The direct-call control proves that ADS does not require an agent framework to preserve its architecture.

Advantages:

```text
smallest dependency surface
maximum execution transparency
provider/runtime neutrality
no framework checkpoint ontology
excellent deterministic testing
straightforward preservation of ADS authority
```

But the experiment also demonstrates what ADS would have to maintain itself:

```text
model/tool iteration
request/response normalization
tool dispatch
approval interruption state machine
resume serialization
message/pending-tool checkpoint state
retry policy
cancellation checks
timeout policy
trace reconstruction
turn limits
structured-output provenance validation
```

Those mechanisms are generic runtime infrastructure rather than differentiated ADS methodological capability.

The control is therefore valuable as:

```text
architecture proof
comparison oracle
fallback/escape path
```

but it is not the preferred V1 production path if a small framework removes that machinery without taking domain authority.

---

## 5. OpenAI Agents SDK fit

The complete candidate removes meaningful generic runtime machinery while preserving the ADS boundary.

Framework value demonstrated:

```text
model/tool loop
function-tool schema generation and dispatch
native approval interruption
serializable/restorable RunState
structured-output validation
native local stdio MCP
function-tool timeout
lifecycle hooks
```

ADS still owns all semantically important boundaries:

```text
Project and methodological state
MethodologicalContextPack construction
context digest and exact knowledge revisions
stale-context rejection
human-control policy
application cancellation policy
authoritative side-effect idempotency/domain events
stable RuntimeTrace/provenance
framework-version compatibility
```

The candidate therefore behaves like infrastructure beneath ADS rather than becoming the system's ontology or source of truth.

Observed maturity cost:

```text
released 0.19.4 did not contain the currently documented agents.testing.ScriptedModel
```

The bakeoff handled this through a deterministic fake against the released public `Model` interface. This is real API/documentation drift, but it did not force a domain compromise or an additional runtime subsystem.

---

## 6. LangGraph's real advantage

LangGraph is not redundant with the OpenAI candidate.

Its strongest demonstrated advantage is explicit persisted execution durability:

```text
SQLite checkpointer
stable thread/checkpoint identity
process-boundary resume
persisted completed-node state
replay/time-travel-capable execution model
node retry policy
explicit workflow boundaries
```

The comparator proved that earlier completed read-only work did not replay in the tested resume path.

This is stronger runtime durability infrastructure than the smaller OpenAI `RunState` approach.

---

## 7. Why that advantage does not currently justify selecting LangGraph

The same experiment also makes the cost visible.

### 7.1 ADS does not currently require a general durable workflow engine

V1 is deliberately single-principal-reasoner first.

The current runtime requirement is primarily:

```text
bounded reasoning turn(s)
tool use
human approval
resume
structured recommendation
stable provenance
```

The architecture does not currently require:

```text
large graph-native workflow topology
time-travel as a core user capability
long-running multi-stage agent workflows
framework-owned distributed workflow scheduling
many independently durable agent nodes
```

Selecting the stronger workflow engine before those needs exist would violate the project's evidence-driven complexity discipline.

### 7.2 Interrupt replay remains an application concern

The LangGraph approval node restarts from the beginning on resume.

The comparator intentionally resumed the same pre-approval checkpoint multiple times and observed:

```text
completed read gateway calls       = 1
proposal execution attempts        = 2
authoritative proposals created    = 1
```

The final at-most-once protection still came from ADS `ProposalLedger`.

So the extra durability does not remove the core domain rule:

```text
runtime replay semantics
    !=
authoritative exactly-once ADS meaning
```

### 7.3 Larger dependency and operational surface

The validated LangGraph path required:

```text
langgraph
langgraph-checkpoint-sqlite
langchain-mcp-adapters
mcp v1 pin
checkpoint database lifecycle
thread/checkpoint identifiers
explicit graph topology
```

The MCP adapter also admitted incompatible MCP v2 through its released dependency range, requiring an explicit `mcp==1.28.1` experiment pin.

This is useful maturity evidence because dependency compatibility is part of operational burden.

### 7.4 Provider neutrality is not enough by itself

LangGraph's provider-neutral shape is attractive, but Specification 005 requires framework isolation and deterministic substitution, not universal provider equivalence.

The OpenAI candidate already passes the required isolation/testability boundary. ADS can preserve provider/model choice behind its runtime adapter instead of selecting a larger workflow framework solely to maximize provider abstraction before that becomes a demonstrated project requirement.

---

## 8. Three-way selection result

### Direct calls

```text
Best at:
    dependency minimality
    explicit control
    escape-hatch simplicity

Loses current V1 selection because:
    ADS would own too much generic orchestration code
    framework candidate demonstrably removes that burden without semantic coupling
```

### OpenAI Agents SDK 0.19.4

```text
Best current fit at:
    smallest framework surface that passes every mandatory gate
    native approval + resumable state + MCP + structured output
    low additional operational machinery
    straightforward single-principal-reasoner model

Costs:
    framework dependency
    released API/documentation drift observed
    runtime-state compatibility must be version governed
```

### LangGraph 1.2.10

```text
Best at:
    explicit persisted workflow/checkpoint durability
    replay/fault-tolerance machinery

Loses current V1 selection because:
    stronger durability is not yet required enough
    larger dependency/operational surface
    explicit replay/idempotency constraints remain
    more workflow topology than the current reasoning runtime needs
```

The evidence therefore supports:

> Select OpenAI Agents SDK as the initial V1 reasoning runtime infrastructure, behind an ADS-owned runtime port, while retaining direct model calls as a valid fallback/control and keeping LangGraph as a future escalation path if durable workflow requirements become materially stronger.

---

## 9. Are Microsoft Agent Framework or Google ADK 2.0 still decision-relevant?

Specification 005 explicitly permits early elimination and does not require equal implementation effort.

Research 010 preserved current official-source evidence for both secondary candidates.

### Microsoft Agent Framework

Potential differentiators:

```text
broad provider matrix
workflow checkpoints
HITL
MCP
structured output
```

But the most ADS-shaped functional workflow API was recorded as experimental, while the already-tested candidates bracket the current tradeoff:

```text
OpenAI -> smaller complete runtime
LangGraph -> stronger complete durability comparator
```

There is no preserved Microsoft-specific capability that is currently required by ADS and plausibly beats both boundaries enough to justify another full adapter.

### Google ADK 2.0

Potential differentiators:

```text
GA workflow framework
MCP
multi-agent/workflow breadth
provider adapters
human-input workflow nodes
```

But the relevant audit recorded:

```text
tool confirmation -> experimental
resumability -> best-effort
resume/tool execution -> at-least-once/idempotency discipline
structured-output/tool combinations -> model-dependent limitations
```

Those properties do not improve the current selection problem relative to the two complete candidates.

### Stop rule

Therefore:

```text
Microsoft Agent Framework implementation   NOT REQUIRED for current V1 selection
Google ADK 2.0 implementation              NOT REQUIRED for current V1 selection
```

This is not a permanent rejection.

Reopen either candidate if a future ADS requirement appears that the selected runtime handles poorly, for example:

```text
provider portability becomes a first-order production constraint
workflow durability expands beyond serialized single-agent runtime state
multi-agent collaboration becomes empirically justified
long-running distributed execution becomes necessary
selected-runtime API/maturity degrades materially
```

---

## 10. Recommended promotion

The runtime bakeoff has now produced enough evidence for an explicit V1 architecture decision.

Recommended decision:

```text
Initial V1 reasoning runtime:
    OpenAI Agents SDK

Validated starting package:
    openai-agents==0.19.4

Architecture boundary:
    ADS-owned ReasoningRuntime port
    framework-specific adapter below the port
    ADS domain/project/methodological state remains authoritative

Retain:
    direct-call control as fallback/reference
    LangGraph evidence as future durability escalation path

Do not implement now:
    Microsoft Agent Framework adapter
    Google ADK adapter
    multi-agent architecture
```

The decision should be version-governed rather than interpreted as permanent framework lock-in.