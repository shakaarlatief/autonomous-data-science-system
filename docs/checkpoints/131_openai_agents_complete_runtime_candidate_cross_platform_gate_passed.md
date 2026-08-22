# Checkpoint 131: OpenAI Agents complete runtime candidate cross-platform gate passed

**Date:** 2026-08-22  
**Status:** Historical experiment-verification record; runtime selection remains open  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Post-V0 V1 bounded runtime evaluation  
**Scope:** Preserves the complete OpenAI Agents SDK 0.19.4 candidate after all Specification 005 mandatory gates passed on Ubuntu and Windows.  
**Authority:** Historical runtime-bakeoff evidence. Specification 005 remains the evaluation contract; this checkpoint does not select a runtime.  
**Active branch:** `v1-runtime-bakeoff`  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this checkpoint exists

Checkpoint 129 established a viable ADS-owned direct model-call control. Checkpoint 130 preserved a bounded post-promotion Cockpit polish gate while the runtime track remained primary.

The OpenAI Agents SDK candidate had already passed a core subgate for domain isolation, the single-agent tool loop, approval interruption, `RunState` serialization/resume, external ADS authority, context transparency, structured output, and deterministic provider substitution.

The remaining mandatory Specification 005 gates were:

```text
AR-03  MCP integration
AR-08  cancellation and bounded timeout
AR-09  failure/retry behavior
AR-11  normalized observability
```

Those gates are now implemented and validated.

---

## 2. Complete candidate implementation

Candidate implementation remains isolated under:

```text
experiments/runtime_bakeoff/candidates/openai_agents/
```

No OpenAI Agents type has been promoted into ADS domain/project/methodological authority.

New bounded evidence includes:

```text
local_mcp_server.py
    side-effect-free FastMCP stdio reference server

advanced.py
    ADS-normalized SDK lifecycle hooks
    application-owned cancellation
    SDK function-tool timeout probe
    real MCPServerStdio candidate path

test_advanced.py
    executable AR-03 / AR-08 / AR-09 / AR-11 gates
```

`openai-agents==0.19.4` remains an experiment-only ephemeral workflow dependency rather than an unconditional production dependency.

---

## 3. Cross-platform validation

Validated implementation commit:

```text
08c1c41246d8ece21e443d938ed477176505e40f
```

Workflow:

```text
V1 runtime bakeoff
```

Run:

```text
32555526773
```

Final result:

```text
Ubuntu
    deterministic direct-call/control harness PASS
    existing Python suite PASS
    OpenAI Agents complete candidate PASS

Windows
    deterministic direct-call/control harness PASS
    existing Python suite PASS
    OpenAI Agents complete candidate PASS
```

Primary result artifact:

```text
experiments/runtime_bakeoff/candidates/openai_agents/COMPLETE_RESULT.md
```

Interpretive evidence:

```text
docs/research/011_openai_agents_0_19_4_released_api_compatibility_findings.md
docs/research/013_openai_agents_complete_candidate_evidence_and_direct_call_comparison.md
```

---

## 4. Mandatory gate result

```text
AR-01  PASS  domain isolation
AR-02  PASS  single principal-agent tool loop
AR-03  PASS  real local stdio MCP integration
AR-04  PASS  approval interrupt before authoritative side effect
AR-05  PASS  serialized RunState process-boundary resume
AR-06  PASS  ADS project-state authority remains external
AR-07  PASS  exact context-pack/revision transparency
AR-08  PASS  application cancellation + bounded function-tool timeout
AR-09  PASS  controlled read retry + ADS-owned side-effect idempotency
AR-10  PASS  ADS-owned structured result validation
AR-11  PASS  normalized ADS observability
AR-12  PASS  deterministic provider-free model substitution
```

OpenAI Agents SDK 0.19.4 is therefore a technically viable complete candidate under the current Specification 005 workload.

---

## 5. Important architectural evidence

### MCP remains interoperability

The candidate launches a real local stdio MCP subprocess using released `MCPServerStdio`. The principal reasoner discovers and invokes the methodological-reference MCP tool.

This does not make MCP project memory or an ADS internal application bus.

### Cancellation remains application policy

ADS registers the active run behind the adapter and cancels it by ADS `run_id`. The SDK run receives normal asynchronous cancellation. The normalized result is `CANCELLED` and the ADS trace records the application-requested cancellation.

### Timeout can use SDK infrastructure

A bounded async function tool configured with released SDK timeout behavior raises `ToolTimeoutError`, which is normalized into ADS evidence.

### Retry does not own exactly-once meaning

A read-only tool fails once and succeeds after model retry. The approval-gated project proposal remains protected by the ADS `ProposalLedger`.

Repeated approved resume execution yields:

```text
execution attempts > 1
created authoritative proposal = 1
```

The durable principle remains:

```text
runtime retry/replay
    !=
ADS domain idempotency / exactly-once meaning
```

### Observability remains ADS-owned

SDK hooks provide useful lifecycle signals, but stable run/project/context/revision/tool/error/latency evidence is normalized into `RuntimeTrace`. Vendor tracing is disabled in the deterministic gate.

---

## 6. Comparison with direct calls

The direct-call control remains viable.

OpenAI Agents SDK removes meaningful custom plumbing around:

```text
model/tool iteration
function-tool schema/dispatch
approval interruption representation
RunState serialization/restoration
structured-output validation
native local MCP integration
function-tool timeout behavior
lifecycle hooks
```

ADS still must own:

```text
project/methodological semantics
bounded context construction and digest
exact knowledge revision provenance
stale-context rejection
human-control and cancellation policy
side-effect idempotency/domain events
stable normalized trace
framework-state compatibility
adapter translation
```

The complete PASS therefore establishes technical viability, not automatic architectural superiority.

---

## 7. Released-version compatibility cost remains evidence

Research 011 remains valid:

```text
current docs advertised agents.testing.ScriptedModel
published openai-agents==0.19.4 did not ship agents.testing
```

Deterministic testing required an experiment-local fake at the released public `Model` boundary.

This is a real API-maturity/testability cost even though all mandatory gates now pass.

---

## 8. Decision status

No runtime is selected.

Current evidence set:

```text
Direct model calls
    viable
    smallest dependency surface
    largest explicit custom orchestration burden

OpenAI Agents SDK 0.19.4
    viable complete candidate
    meaningful reduction in runtime plumbing
    non-zero adapter/version coupling
    released docs/package drift observed
```

LangGraph remains decision-relevant because durability/checkpoint semantics are the strongest unresolved differentiator.

Microsoft Agent Framework and Google ADK 2.0 remain conditional candidates rather than mandatory implementations unless the direct/OpenAI/LangGraph evidence leaves a material decision gap they could plausibly resolve.

---

## 9. Exact continuation

Next:

```text
1. audit the currently released LangGraph package/API surface
2. implement an isolated deterministic LangGraph durability comparator
3. use the same ADS workload, provenance, approval and ProposalLedger authority
4. explicitly test interrupt/checkpoint replay semantics across a process boundary
5. test the consequence that resumed interrupts may restart node execution
6. complete AR-01 through AR-12 if LangGraph remains technically viable
7. compare direct calls vs OpenAI vs LangGraph on capability, durability,
   custom machinery, coupling, maturity, testability and operational burden
8. decide whether Microsoft/Google could still change the selection outcome
9. make an explicit runtime/no-runtime promotion decision only from evidence
```
