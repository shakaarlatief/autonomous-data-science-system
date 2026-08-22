# Research 011: OpenAI Agents SDK 0.19.4 Released-API Compatibility Findings

**Date:** 2026-08-21  
**Status:** Current implementation research / correction to pre-implementation assumptions  
**Scope:** Differences between the current OpenAI Agents SDK documentation/main branch and the actual `openai-agents==0.19.4` PyPI release encountered during the Specification 005 executable bakeoff  
**Authority:** Current candidate-implementation evidence. This memo refines Research 010 where released-package evidence is stronger than documentation-only assumptions. It does not select a runtime.  
**Design session:** 03  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 03 - Project Cockpit & V1 Integration

## 1. Why this memo exists

Research 010 refreshed Specification 005 against current official documentation immediately before implementation.

The executable OpenAI Agents SDK candidate then exposed an important distinction:

```text
current documentation / repository main
    !=
current published package surface
```

This is exactly the kind of evidence the project uses implementation spikes to uncover.

Research 010 remains useful for current ecosystem direction, but its statement that deterministic testing support is available through the current released `agents.testing.ScriptedModel` surface was too strong.

---

## 2. Published candidate version

The bakeoff pins:

```text
openai-agents==0.19.4
```

The package installs successfully on the current Ubuntu and Windows CI environments with Python 3.13.

The framework is installed only inside the candidate CI job using `uv --with`; it is not yet an unconditional ADS project dependency.

---

## 3. `agents.testing` documentation/release mismatch

Current OpenAI Agents SDK documentation describes a public deterministic testing surface including:

```text
agents.testing.ScriptedModel
agents.testing.assistant_message
agents.testing.function_call
```

The first executable candidate used that documented import path.

CI failed during test collection with:

```text
ModuleNotFoundError: No module named 'agents.testing'
```

Inspection of the tagged 0.19.4 source confirmed:

```text
src/agents/testing/
    absent from the release tag/package

tests/fake_model.py
    present in the SDK repository
    not part of the installed package API
```

The current repository `main` branch does contain `src/agents/testing/model.py`, so the documentation describes a real newer surface, but one that is ahead of the current published release used by the bakeoff.

---

## 4. Released deterministic-testing seam

OpenAI Agents SDK 0.19.4 does expose the public abstract model boundary:

```text
agents.models.interface.Model
```

with provider-neutral methods including:

```text
get_response(...)
stream_response(...)
```

The release's own repository test suite subclasses that public `Model` boundary in `tests/fake_model.py`.

ADS therefore implemented a deliberately small experiment-local:

```text
ReleaseScriptedModel(Model)
```

that supports only the non-streaming FIFO outputs required by the representative workload.

This preserves AR-12's important behavioral requirement:

```text
no live paid/provider model call required for infrastructure tests
```

but it changes the maturity assessment:

```text
AR-12 behavior
    achievable on 0.19.4

first-class released testing ergonomics
    weaker than current docs imply
```

The extra custom fake is candidate-specific glue and must count in the runtime comparison.

---

## 5. Structured-output wrapper behavior

A second released-API detail was discovered during the core gate.

ADS uses the dataclass:

```text
RuntimeRecommendation
```

as the structured output type.

OpenAI Agents SDK 0.19.4 wraps output types that are not Pydantic `BaseModel` subclasses or dict subclasses under:

```text
{"response": ...}
```

for strict JSON-schema validation, then unwraps the value before returning the requested type.

The initial deterministic final-model fixture emitted the raw dataclass JSON and failed strict SDK validation with:

```text
response
    Field required
```

The fixture was corrected to emit the schema the SDK actually supplied to the model. No ADS output requirement was weakened.

This behavior is acceptable but should remain documented because adapter/test doubles need to use the runtime's actual requested schema rather than assuming that a Python dataclass maps directly to the root JSON object.

---

## 6. Core candidate evidence after corrections

After pinning tests to the released 0.19.4 API surface, the core candidate passed on both Ubuntu and Windows.

Validated core behavior includes:

```text
single principal Agent tool loop
native approval interruption before authoritative side effect
RunState JSON serialization/restoration across a process boundary
no replay of completed read-only reference lookup in the tested resume path
ADS ProposalLedger at-most-once authority under repeated resume
approval rejection without project-state creation
exact context-pack/revision transparency
stale ADS project-snapshot rejection before resume
ADS-owned structured RuntimeRecommendation
production package isolation from candidate framework imports
```

Final core result:

```text
experiments/runtime_bakeoff/candidates/openai_agents/CORE_RESULT.md
```

---

## 7. Implication for runtime evaluation method

Rapidly changing runtime ecosystems should be evaluated against three distinct evidence layers:

```text
current documentation
    indicates intended/current direction

latest published package
    determines what ADS can actually depend on today

executable ADS-shaped gate
    determines whether the released behavior satisfies our requirements
```

A documented capability should not be credited as released implementation evidence until the candidate environment imports and executes it successfully.

This lesson applies to all remaining runtime candidates, not only OpenAI Agents SDK.

---

## 8. Current interpretation

The release/docs mismatch is not enough to reject OpenAI Agents SDK.

The core gate shows meaningful native value around:

```text
tool-loop orchestration
approval interruptions
serialized RunState
structured output
```

But API maturity/testability should receive a real caveat because ADS currently needs a custom deterministic model double that the documentation suggests should already be first-class.

No runtime selection follows from this memo.
