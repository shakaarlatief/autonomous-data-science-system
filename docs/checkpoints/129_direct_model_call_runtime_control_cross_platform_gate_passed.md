# Checkpoint 129: Direct Model-Call Runtime Control Cross-Platform Gate Passed

**Date:** 2026-08-21  
**Status:** Historical experiment-verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Post-V0 V1 bounded runtime evaluation  
**Scope:** Preserves the first executable no-framework control for Specification 005 after deterministic Ubuntu and Windows validation.  
**Authority:** Historical runtime-bakeoff evidence. Specification 005 remains the candidate evaluation contract; no runtime is selected by this checkpoint.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this checkpoint exists

Checkpoint 128 established the refreshed pre-implementation runtime evidence and the evaluation order:

```text
direct model-call control
    -> OpenAI Agents SDK
    -> LangGraph durability comparator if still decision-relevant
    -> Microsoft Agent Framework / Google ADK 2.0 if they could plausibly change the result
```

The first executable bakeoff slice then created a framework-neutral ADS-owned harness before importing any candidate runtime package.

The harness passed its initial cross-platform gate in workflow run:

```text
32499548591
```

That established a stable comparison boundary for:

```text
workload identity
context-pack provenance
approval interruption
resume token
at-most-once side-effect ledger
cancellation
normalized trace
structured result
```

The next required step was not to install a framework immediately. Specification 005 and Research 010 require an actual simpler control so framework adoption does not become the default answer.

Checkpoint 129 records that control.

---

## 2. Direct model-call control

Implementation:

```text
experiments/runtime_bakeoff/direct_call.py
```

The control is deliberately small and provider-neutral at the infrastructure-test layer.

It introduces an ADS-owned direct model-turn abstraction:

```text
DirectModelClient
DirectModelRequest
DirectModelResponse
DirectToolCall
```

with a deterministic fake:

```text
ScriptedDirectModel
```

and the no-framework execution loop:

```text
DirectModelCallRuntime
```

This is experiment code, not a promoted production ReasoningRuntime contract.

---

## 3. Cross-platform validation

Validated commit:

```text
366d15357205b4deed101e94fc684951f897cf34
```

Workflow:

```text
V1 runtime bakeoff
```

Run:

```text
32500521858
```

Result:

```text
Ubuntu / Python 3.13
    direct runtime bakeoff tests PASS
    existing Python suite PASS

Windows / Python 3.13
    direct runtime bakeoff tests PASS
    existing Python suite PASS
```

Final result artifact:

```text
experiments/runtime_bakeoff/DIRECT_CALL_CONTROL_RESULT.md
```

---

## 4. What the control proves

The direct model-call control exercises the representative missingness/validation workload while preserving ADS ownership of:

```text
bounded explicit model context
exact context-pack identity and digest
exact knowledge revision references
normal read-only tool calls
controlled model retry
controlled methodological-reference retry
approval before project-state creation
process-boundary serialization/resume
stale authoritative-context rejection
at-most-once approved proposal creation
cancellation before approved side effect
structured recommendation validation
normalized runtime trace
```

The process-boundary test is important.

The interrupted runtime is discarded. A new runtime instance and new scripted model are created from the serialized resume token. Previously completed read-only work is not repeated. Approval then executes through the ADS ProposalLedger.

Repeated approval of the same pre-execution token results in:

```text
proposal created count = 1
execution attempts = 2
```

This demonstrates that authoritative exactly-once meaning belongs at the ADS application boundary rather than being inferred from runtime replay semantics.

---

## 5. Complexity evidence from the control

The no-framework option is viable but exposes a real implementation burden.

ADS currently owns experiment code for:

```text
model/tool loop
request/response normalization
tool dispatch
retry rules
approval interruption
resume serialization
message/pending-tool checkpoint state
trace reconstruction
cancellation checks
stale-context validation
idempotent side-effect boundary
structured-output provenance checks
turn-limit handling
```

This is now an empirical comparison baseline.

A candidate runtime should not receive credit merely for reproducing this behavior. It must reduce meaningful custom machinery or improve durability/testability/observability/interoperability enough to justify its dependency and coupling cost.

---

## 6. What remains untested in the direct control

The current PASS does not establish:

```text
live provider/API behavior
MCP protocol integration
real network/model timeout behavior
streaming
production telemetry backend
persistent runtime store
concurrent cancellation
multi-agent behavior
```

The infrastructure gate intentionally avoids paid/live model calls.

---

## 7. Decision status

No runtime is selected.

The direct-call control remains a valid possible V1 outcome.

Its current evidence is:

```text
smallest dependency surface
strong domain isolation
fully deterministic infrastructure tests
explicit custom orchestration burden
```

The next implementation must test whether an existing runtime removes enough of that burden while preserving the ADS semantic boundary.

---

## 8. Exact continuation

Next:

```text
OpenAI Agents SDK candidate
    deterministic ScriptedModel first
    no live model/API key required for infrastructure gate
    same ADS workload
    same MethodologicalContextPack provenance
    same ADS ProposalLedger authority
    native approval interruption
    serialize/restore RunState across process boundary
    ADS-owned RuntimeRecommendation output
    framework types contained inside candidate adapter
```

Initial OpenAI candidate subgate should establish the most decision-relevant core requirements before widening to MCP/cancellation/timeout/failure-detail tests:

```text
AR-01 domain isolation
AR-02 single-agent tool loop
AR-04 approval interrupt
AR-05 durable process-boundary resume
AR-06 external project-state authority
AR-07 context transparency
AR-10 structured output
AR-12 deterministic no-live-model testing
```

Then add dedicated evidence for remaining mandatory gates such as MCP, timeout/cancellation, retry/failure semantics, and normalized observability.

LangGraph remains the planned durability comparator if the OpenAI result does not already make another candidate incapable of changing the decision.
