# OpenAI Agents SDK 0.19.4 Complete Candidate Result

**Status:** PASS for Specification 005 mandatory candidate gates  
**Date:** 2026-08-22  
**Candidate:** OpenAI Agents SDK 0.19.4  
**Validation workflow:** `V1 runtime bakeoff`  
**Workflow run:** `32555526773`  
**Validated commit:** `08c1c41246d8ece21e443d938ed477176505e40f`

## Cross-platform result

```text
Ubuntu
    OpenAI Agents complete candidate PASS
    deterministic direct-call/control harness PASS
    existing Python suite PASS

Windows
    OpenAI Agents complete candidate PASS
    deterministic direct-call/control harness PASS
    existing Python suite PASS
```

## Mandatory gate status

```text
AR-01  PASS  domain isolation
AR-02  PASS  single principal-agent tool loop
AR-03  PASS  real local stdio MCP integration
AR-04  PASS  human approval interrupt before authoritative side effect
AR-05  PASS  serialized RunState resume after process boundary
AR-06  PASS  ADS project-state authority remains external
AR-07  PASS  exact context-pack/revision transparency
AR-08  PASS  application cancellation + bounded function-tool timeout
AR-09  PASS  controlled read failure/retry + ADS-owned side-effect idempotency
AR-10  PASS  ADS-owned structured result validation
AR-11  PASS  normalized ADS observability evidence
AR-12  PASS  deterministic provider-free test substitution
```

## AR-03 MCP evidence

The candidate launches the repository-local side-effect-free methodological reference server as a real stdio MCP subprocess through released `MCPServerStdio`.

The principal agent receives `lookup_methodological_reference` from the MCP server rather than from the in-process pre-MCP gateway. The deterministic model discovers and calls the MCP tool, and ADS-normalized lifecycle hooks record its invocation/outcome.

The test does not depend on deprecated MCP Roots, Sampling, or Logging behavior.

## AR-08 cancellation and timeout evidence

Two distinct controls were exercised:

```text
application cancellation
    active Runner task registered behind the experiment adapter
    application requests cancellation by ADS run_id
    asyncio cancellation reaches the SDK run
    adapter returns RuntimeStatus.CANCELLED
    normalized trace records application-requested cancellation

function-tool timeout
    async tool configured with a small SDK timeout
    timeout_behavior = raise_exception
    released SDK raises ToolTimeoutError
    adapter records timeout/error/latency in ADS trace
```

This demonstrates that cancellation ownership can remain at the ADS application boundary while tool timeout semantics use released SDK infrastructure.

## AR-09 failure/retry evidence

A side-effect-free methodological-reference lookup fails once with a synthetic transient error. The SDK converts the ordinary function-tool failure into model-visible failure output under its released default function-tool failure behavior. The deterministic model retries the same read-only tool and succeeds on attempt two.

ADS-normalized hooks record the repeated tool invocation as retry evidence.

The approval-gated authoritative proposal remains protected by `ProposalLedger.create_once(...)`. Replaying the same approved resume token twice produces two execution attempts but only one created proposal.

Therefore retry/replay behavior does not transfer idempotency authority to the runtime framework.

## AR-11 normalized observability evidence

The experiment-owned `RuntimeTrace` preserves stable ADS identifiers independently of SDK-native tracing:

```text
run_id
project_snapshot_id
context_pack_id
context_pack_digest
knowledge_revision_ids
runtime / SDK identity
model-double identity
model lifecycle and usage where exposed
tool start/end and results
repeated tool attempts / retry signal
approval interruption and resume
cancellation
timeout/error evidence
whole-run latency
structured-output validation
```

SDK tracing remains disabled in the deterministic gate. This proves ADS does not need to make a framework/vendor tracing backend authoritative in order to preserve stable operational provenance.

## Released-API compatibility evidence retained

The earlier core gate established two important release-specific facts:

```text
1. current documentation advertises agents.testing.ScriptedModel,
   but PyPI openai-agents==0.19.4 does not ship agents.testing;
   deterministic testing therefore uses the released public Model interface.

2. a dataclass RuntimeRecommendation is represented by the SDK output schema
   under a top-level `response` wrapper and unwrapped after strict validation.
```

These remain real API-maturity/testability costs and are not erased by the final PASS.

## Complexity compared with the direct-call control

OpenAI Agents SDK removes meaningful custom machinery around:

```text
model/tool iteration
function-tool schema and dispatch plumbing
approval interruption representation
RunState serialization/restoration
structured-output schema validation
native local MCP exposure
function-tool timeout behavior
lifecycle hooks
```

ADS still owns, and must continue to own:

```text
project and methodological semantics
bounded context construction and digest
exact knowledge revision provenance
stale authoritative-context rejection
application cancellation policy
side-effect idempotency
domain event persistence
stable normalized runtime trace/provenance
framework-state version compatibility
adapter translation
```

Candidate-specific glue remains non-zero, particularly the released-version deterministic Model fake and translation from SDK lifecycle/state into ADS-owned contracts.

## Interpretation

This result establishes that OpenAI Agents SDK 0.19.4 is a technically viable V1 runtime candidate for the mandatory workload.

It does **not** select the SDK.

The direct-call control is also viable, and LangGraph remains decision-relevant as the strongest durability/checkpoint comparator. Runtime selection should occur only after comparing the concrete complexity and durability evidence rather than from feature availability alone.
