# Checkpoint 132: LangGraph durability comparator cross-platform gate passed

**Date:** 2026-08-22  
**Status:** Historical experiment-verification record  
**Checkpoint class:** EXPERIMENT_VERIFICATION  
**Project stage:** Post-V0 V1 bounded runtime evaluation  
**Scope:** Preserves the complete LangGraph 1.2.10 durability comparator after Ubuntu and Windows validation.  
**Authority:** Historical runtime-bakeoff evidence. Runtime selection is a separate promotion decision.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this checkpoint exists

Checkpoint 131 established that OpenAI Agents SDK 0.19.4 passed all Specification 005 mandatory gates. LangGraph remained decision-relevant because its persisted execution/checkpoint semantics could plausibly justify a larger runtime surface.

The comparator is now complete.

## 2. Validated package boundary

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
Python 3.13
```

The MCP pin is deliberate. The released LangChain MCP adapter allowed a later incompatible MCP v2 generation through its dependency range. Pinning the verified v1 line restored the API generation the adapter actually supports and is preserved as dependency-maturity evidence.

## 3. Validation

Validated implementation head:

```text
c7f9f8bcb4ec367a3d30e5d2831db14a2aed8e53
```

Workflow:

```text
V1 runtime bakeoff
run 43
32556382248
```

Result:

```text
Ubuntu / Python 3.13
    LangGraph durability comparator        PASS
    9 tests passed
    direct/control + full Python suite     PASS
    OpenAI complete candidate              PASS

Windows / Python 3.13
    LangGraph durability comparator        PASS
    9 tests passed in 4.97s
    direct/control + full Python suite     PASS
    OpenAI complete candidate              PASS
```

## 4. Mandatory gate result

The comparator provides executable PASS evidence for:

```text
AR-01  domain isolation
AR-02  single-principal-reasoner tool loop
AR-03  MCP integration
AR-04  approval interrupt
AR-05  durable process-boundary resume
AR-06  external ADS project-state authority
AR-07  context/revision transparency
AR-08  cancellation and timeout
AR-09  controlled failure/retry behavior
AR-10  ADS-owned structured output
AR-11  normalized observability
AR-12  deterministic provider substitution
```

## 5. Durability finding

The important result is not merely that resume works.

The tested execution semantics are:

```text
earlier completed read-only nodes
    -> persisted and not repeated on the tested resume path

node containing interrupt()
    -> restarts from the beginning when resumed
```

The same pre-approval checkpoint was deliberately resumed repeatedly.

Observed authoritative behavior:

```text
completed methodological-reference gateway calls = 1
proposal execution attempts                      = 2
ADS proposals created                            = 1
```

The ADS `ProposalLedger` therefore remains the exactly-once project-meaning boundary.

LangGraph durability does not replace ADS side-effect governance.

## 6. Other validated behavior

The complete comparator also validates:

```text
human rejection without project-state creation
stale project/context rejection before approved execution
RetryPolicy on a transient side-effect-free read
bounded async-node timeout surfaced as NodeTimeoutError
application cancellation by ADS run identity
real local stdio MCP reference lookup
ADS-normalized run/context/revision/tool/interrupt/checkpoint/retry/latency trace
```

## 7. Comparison significance

LangGraph demonstrates a real advantage over the smaller OpenAI runtime in persisted workflow/checkpoint machinery.

It also demonstrates additional cost:

```text
separate checkpointer package
separate MCP adapter package
explicit MCP v1 compatibility pin
checkpoint database lifecycle
thread/checkpoint runtime identifiers
interrupt-node replay semantics
more explicit workflow topology
```

Those costs are now empirical rather than hypothetical.

## 8. Promotion audit

Promotion is warranted.

Created/promoted evidence:

```text
experiments/runtime_bakeoff/candidates/langgraph_runtime/COMPLETE_RESULT.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
```

No runtime is selected by this checkpoint itself.

No Foundation is required because the durable architectural principle already exists: runtime/checkpoint infrastructure is not ADS project authority.

## 9. Exact continuation

The next step is no longer another LangGraph implementation.

Use the now-complete evidence to make an explicit V1 runtime/no-runtime promotion decision across:

```text
ADS-owned direct model calls
OpenAI Agents SDK 0.19.4
LangGraph 1.2.10
```

Only implement Microsoft Agent Framework or Google ADK 2.0 if Research 015's stop-rule analysis is overturned by a concrete current requirement that could plausibly change the selection.