# LangGraph 1.2.10 Complete Durability Comparator Result

**Date:** 2026-08-22  
**Status:** COMPLETE CANDIDATE PASS  
**Scope:** Specification 005 deterministic ADS-shaped runtime bakeoff  
**Selection status:** Technically viable candidate only. This result does not select LangGraph as the ADS V1 runtime.

## Released package boundary

The validated comparator used:

```text
langgraph==1.2.10
langgraph-checkpoint-sqlite==3.1.1
langchain-mcp-adapters==0.3.1
mcp==1.28.1
Python 3.13
```

The MCP v1 pin is deliberate. `langchain-mcp-adapters==0.3.1` permits `mcp>=1.24.0` without a `<2` upper bound, while the subsequently released MCP v2 line is not import-compatible with the adapter surface exercised here. The first unbounded resolver attempt therefore selected an incompatible API generation. The comparator pins the verified v1 release so it tests the released adapter on the protocol generation it actually supports.

This dependency-resolution defect is preserved as ecosystem-maturity evidence rather than hidden as an ADS implementation detail.

## Cross-platform validation

Validated branch head:

```text
c7f9f8bcb4ec367a3d30e5d2831db14a2aed8e53
```

GitHub Actions workflow:

```text
V1 runtime bakeoff
run 43
32556382248
```

Results:

```text
Ubuntu / Python 3.13
    LangGraph durability comparator          PASS
    9 tests passed
    direct-call control/full Python suite    PASS
    OpenAI Agents complete candidate         PASS

Windows / Python 3.13
    LangGraph durability comparator          PASS
    9 tests passed in 4.97s
    direct-call control/full Python suite    PASS
    OpenAI Agents complete candidate         PASS
```

The Windows job executed the exact released-package command:

```text
uv run --python 3.13 --locked \
  --with langgraph==1.2.10 \
  --with langgraph-checkpoint-sqlite==3.1.1 \
  --with langchain-mcp-adapters==0.3.1 \
  --with mcp==1.28.1 \
  python -m pytest \
  experiments/runtime_bakeoff/candidates/langgraph_runtime/test_candidate.py -q
```

## Specification 005 gate result

```text
AR-01  domain isolation                         PASS
AR-02  single-principal-reasoner tool loop      PASS
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

## What the comparator proved

### Persistent runtime state

The candidate uses `AsyncSqliteSaver` as runtime-only checkpoint storage. A stable LangGraph `thread_id` and persisted checkpoint identity are stored inside the ADS-owned resume token. The application process/runtime can be discarded, a new adapter and checkpointer instance can be created, and the interrupted run can continue from the persisted checkpoint.

The checkpoint database is not ADS Project state and does not own Findings, Questions, Decisions, methodological knowledge, or governance history.

### Interrupt and replay semantics

The approval node calls LangGraph `interrupt()`. On resume, that node restarts from the beginning. The comparator records this through harmless test instrumentation.

The executable result establishes both sides of LangGraph durability:

```text
completed earlier read-only nodes
    -> persisted and not replayed during the tested resume path

node containing interrupt()
    -> re-enters from the beginning on resume
```

This is useful durability, but it is not authoritative exactly-once semantics.

### Repeated resume of the same checkpoint

The same serialized pre-approval resume token is intentionally resumed more than once.

Observed invariant:

```text
completed read gateway calls       = 1
approval-node entries              = 3 after two approved resumes
proposal execution attempts        = 2
authoritative proposals created    = 1
```

The final protection comes from the ADS-owned `ProposalLedger`, not from treating the runtime checkpoint as project authority.

Therefore:

```text
LangGraph checkpoint/replay semantics
    !=
authoritative exactly-once ADS project meaning
```

### Human rejection

Rejecting the interrupted proposal resumes the graph to a valid final structured recommendation without creating authoritative project state.

### Stale authoritative context

ADS validates the exact project snapshot, context-pack identity, context-pack digest, and knowledge revision boundary before allowing a persisted runtime checkpoint to resume. A changed authoritative context is rejected before approved side-effect execution.

### Retry behavior

A side-effect-free methodological-reference read fails once. LangGraph `RetryPolicy` retries the node and succeeds on the second attempt. Retry events are translated into ADS-normalized trace evidence.

The authoritative proposal is not placed behind automatic retry as a source of truth. Its at-most-once meaning remains at the ADS application boundary.

### Cancellation and timeout

Application cancellation is requested by ADS run identity and cancels the active graph invocation. The outcome is normalized as `RuntimeStatus.CANCELLED`.

A separate async-node timeout probe exercises bounded LangGraph node execution and surfaces `NodeTimeoutError` into the ADS trace.

### MCP

The comparator launches the local methodological-reference MCP subprocess through the released `langchain-mcp-adapters` client path and invokes the read-only reference tool over stdio before the approval interruption.

MCP remains an external tool/resource interoperability boundary. It is not ADS project memory or the internal application bus.

### Structured output and provenance

The framework-neutral deterministic reasoner returns a payload that is validated into ADS-owned `RuntimeRecommendation`.

The normalized `RuntimeTrace` preserves:

```text
ADS run ID
project snapshot ID
context-pack ID
context-pack digest
exact knowledge revision IDs
model/reasoner identity
tool calls and outcomes
retry evidence
interrupt/checkpoint evidence
resume/replay evidence
cancellation/timeout/errors
latency
```

Stable ADS provenance does not depend on LangGraph/LangSmith becoming the source of truth.

## Framework value demonstrated

Compared with the direct-call control, LangGraph provides substantial runtime infrastructure around:

```text
persistent execution checkpoints
thread-scoped resume identity
interrupt/resume
checkpoint history and replay semantics
node retry policy
async node timeout
explicit graph execution boundaries
```

Its strongest differentiator in this bakeoff is durable persisted execution rather than basic tool calling.

## Costs demonstrated

The complete PASS also exposed real costs:

```text
larger framework/dependency surface than direct calls
separate checkpoint persistence package
separate MCP adapter package
MCP adapter required explicit v1 pin because its released dependency range admitted incompatible MCP v2
interrupt-node restart semantics require side-effect placement/idempotency discipline
runtime thread/checkpoint identity must remain carefully separated from ADS project identity
more explicit workflow topology than the smaller OpenAI Agents candidate
```

These are comparison evidence, not automatic disqualifiers.

## Decision status

LangGraph 1.2.10 is a technically viable complete V1 runtime candidate under Specification 005.

It is not selected by this result.

The next legitimate step is an evidence-based comparison among:

```text
ADS-owned direct model calls
OpenAI Agents SDK 0.19.4
LangGraph 1.2.10
```

Microsoft Agent Framework and Google ADK 2.0 should only be implemented if their remaining differentiators could plausibly change that decision.