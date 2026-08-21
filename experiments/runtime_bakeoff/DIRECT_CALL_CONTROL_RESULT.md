# V1 Runtime Bakeoff Direct Model-Call Control Result

**Status:** PASS  
**Date:** 2026-08-21  
**Scope:** Deterministic no-framework control for the Specification 005 representative runtime workload  
**Validation workflow:** `V1 runtime bakeoff`  
**Workflow run:** `32500521858`  
**Validated commit:** `366d15357205b4deed101e94fc684951f897cf34`

## Result

```text
Ubuntu / Python 3.13
    direct-call control tests PASS
    existing Python test suite PASS

Windows / Python 3.13
    direct-call control tests PASS
    existing Python test suite PASS
```

The control uses an ADS-owned model/tool loop with a deterministic scripted model. It deliberately does not use an agent framework or a live provider call.

## Behavior exercised

The direct-call control demonstrates that the representative workload can be implemented while ADS retains ownership of:

```text
bounded model input construction
exact MethodologicalContextPack identity and digest
exact knowledge revision provenance
normal Python/read-only tool dispatch
controlled model retry
controlled methodological-reference retry
approval interruption before authoritative project-state creation
serializable process-boundary resume state
stale authoritative-context detection on resume
at-most-once proposal creation through the ADS ProposalLedger
cancellation before the approved side effect executes
ADS-owned structured RuntimeRecommendation validation
normalized ADS RuntimeTrace
```

The process-boundary resume test creates a new runtime instance and a new scripted model after interruption. Completed read-only work is recovered from the serialized execution state rather than replayed. The approval-gated proposal remains external ADS authority and is created at most once even if the same pre-execution resume token is approved more than once.

## Direct-call implementation burden exposed

The control also makes the no-framework cost explicit. ADS currently owns code for:

```text
model-turn loop
model/tool request normalization
tool-call dispatch
retry policy
approval state machine
resume-token construction
serialization of model messages and pending tool state
trace reconstruction after process boundary
cancellation checks
stale-context validation
side-effect idempotency boundary
structured-output provenance validation
turn-limit failure handling
```

This burden is evidence for the bakeoff. A framework only earns adoption if it removes meaningful parts of this machinery without taking authority over ADS project/domain/methodological state or introducing larger operational/coupling costs.

## What this result does not prove

This deterministic control does not yet validate:

```text
live model-provider behavior
provider-specific Responses/API translation
MCP protocol integration
network timeout behavior under a real provider
streaming
production observability backend
multi-process persistence backend
concurrent cancellation
multi-agent behavior
```

Those are separate runtime-evaluation concerns. A live provider call is not required to prove the infrastructure semantics exercised here.

## Interpretation

The direct-call path remains a credible V1 outcome. It is not free: ADS must own a small but real orchestration layer to provide approval, durability, retries, cancellation, and provenance.

No runtime is selected by this PASS.

The next candidate is the OpenAI Agents SDK, evaluated against the same ADS-owned workload and normalized result/trace semantics using deterministic provider-neutral test machinery first. LangGraph remains the planned durability comparator if still decision-relevant after the first framework candidate.
