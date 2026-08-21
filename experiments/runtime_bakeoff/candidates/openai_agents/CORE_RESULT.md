# OpenAI Agents SDK 0.19.4 Core Candidate Result

**Status:** PASS  
**Date:** 2026-08-21  
**Candidate:** OpenAI Agents SDK 0.19.4  
**Scope:** First bounded Specification 005 core subgate, excluding MCP, cancellation/timeout, detailed retry/failure, and normalized observability completion  
**Validation workflow:** `V1 runtime bakeoff`  
**Workflow run:** `32501907783`  
**Validated commit:** `6483563e95cf3b88a9c342b665f606c742ac24cf`

## Cross-platform result

```text
Ubuntu
    OpenAI Agents core candidate PASS
    direct-call controls PASS
    existing Python suite PASS

Windows
    OpenAI Agents core candidate PASS
    direct-call controls PASS
    existing Python suite PASS
```

## Core gates exercised

```text
AR-01  PASS
    candidate framework imports remain under experiments/runtime_bakeoff
    src/ads_system imports no `agents` package

AR-02  PASS
    one principal Agent completed the representative tool loop

AR-04  PASS
    @tool(needs_approval=True) interrupted before ProposalLedger execution

AR-05  PASS for the bounded serialized-RunState scenario
    RunState serialized to JSON-compatible state
    a fresh adapter/Agent/model restored it after a process boundary
    completed read-only reference work was not replayed
    approved proposal executed through ADS at most once

AR-06  PASS
    SDK state remained runtime execution state
    ADS Project/Finding/Decision authority was not moved into the framework

AR-07  PASS
    exact MethodologicalContextPack id/digest and exact knowledge revision ids
    were supplied explicitly and retained through the resumable state
    raw project fact values were obtained only through the explicit project-fact tool

AR-10  PASS
    Agent output was schema validated into ADS RuntimeRecommendation
    ADS then separately verified that referenced revisions were contained in the supplied context pack

AR-12  PASS with release-specific caveat
    no live model/API call or API key was required
    deterministic testing used the released public Model interface
```

## Release/docs compatibility finding

The current OpenAI Agents SDK documentation describes:

```text
agents.testing.ScriptedModel
agents.testing.assistant_message
agents.testing.function_call
```

The current published `openai-agents==0.19.4` package does not ship `agents.testing`.

The first candidate CI therefore failed at import collection even though package installation succeeded.

The released 0.19.4 repository exposes a public `agents.models.interface.Model` boundary and uses its own repository-local `tests/fake_model.py` for deterministic tests. The ADS candidate was corrected to the actual released API by implementing a small experiment-local `ReleaseScriptedModel(Model)`.

This is not a runtime correctness failure, but it is real maturity/testability evidence:

```text
current docs/main testing surface
    ahead of
current PyPI 0.19.4 testing surface
```

The custom fake is additional candidate-specific glue that should count against the framework until a released first-class testing package removes it.

## Structured-output compatibility finding

`RuntimeRecommendation` is an ADS dataclass, not a Pydantic BaseModel or dict subclass.

OpenAI Agents SDK 0.19.4 therefore exposes its strict output schema under:

```text
{"response": <RuntimeRecommendation schema>}
```

and unwraps `response` after validation.

The deterministic model fixture must emit that SDK-requested schema. ADS still receives and validates the original RuntimeRecommendation after SDK parsing.

## Complexity comparison so far

Relative to the direct-call control, the SDK already removes meaningful custom machinery around:

```text
model/tool iteration
function-tool schema/dispatch plumbing
approval interruption representation
RunState construction
RunState JSON serialization/restoration
structured-output schema validation
```

ADS still must own:

```text
project/context authority
context-pack construction and digest
knowledge revision provenance
stale-authoritative-context validation
application side-effect idempotency
normalized ADS trace/provenance
framework-state version compatibility
adapter translation
```

Candidate-specific glue currently also includes the 0.19.4 deterministic Model fake because the documented `agents.testing` package is not released.

## Not yet passed

Do not interpret this core result as a full Specification 005 PASS.

Still required for this candidate:

```text
AR-03  current MCP client integration
AR-08  cancellation and bounded timeout semantics
AR-09  controlled failure/retry behavior
AR-11  complete normalized observability evidence
```

Provider coupling and operational/dependency burden must also be compared against the direct-call control and LangGraph before any runtime selection.
