# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that owns project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

```text
checkpoint            158
active branch         v1-recommendation-action-value-relation-backed
active PR             #16 -> v1-frontend-spike
promoted V1 head      6bda0c1efcf078476859b2c2c64fb0586964899d
current boundary      Specification 017 provider-free implementation green;
                      explicit live boundary frozen; final pre-live CI pending
```

Current progression:

```text
Prototype V0
    strong falsification of the original P0 design

Specification 013
    accepted selective exact-revision MethodologicalContextPack

Specification 014
    real-model selective context preserved frozen reasoning quality
    while reducing provider input tokens by 66.56%

Specification 015
    first recommendation/action-value experiment
    frozen result FAIL
    failed implementation rejected
    negative evidence preserved separately

Specification 016
    isolated dependency-backed DEFER-vs-NOT_NOW construct validity
    all frozen live gates passed
    outcome DISPOSITION_BOUNDARY_SUPPORTED
    promoted at 6bda0c1efcf078476859b2c2c64fb0586964899d

Specification 017 [active]
    second recommendation/action-value experiment
    GENERIC vs SELECTIVE vs FULL_HORIZON
    explicit relation-backed defer pointers
    provider-free implementation passed Ubuntu + Windows
    manual secret-gated live workflow frozen
    no live Specification 017 call yet
```

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/research/024_relation_backed_recommendation_action_value_design.md
docs/specifications/017_v1_relation_backed_recommendation_action_value_vertical_slice.md
docs/checkpoints/156_relation_backed_recommendation_action_value_contract_frozen.md
docs/checkpoints/157_relation_backed_recommendation_action_provider_free_gate_cross_platform_passed.md
docs/checkpoints/158_specification_017_live_boundary_frozen.md
```

---

## Durable post-V0 constraint

Prototype V0 strongly falsified the current P0 design. The broader ADS vision survived, but the original orchestration machinery did not earn its complexity.

The strongest scaling lesson remains:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not restore large always-on project/methodological context, narrow path-sensitive activation, generic recursive reopening, or full frontier machinery unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project semantics

Foundation 018 distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

### Methodological navigation

Foundation 019 establishes:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The bounded executable path currently reaches:

```text
reusable methodological knowledge
    -> retrieval
    -> explained MethodologicalHorizon
    -> applicability / missing context
    -> selective exact-revision MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> measured real reasoning
    -> relation-backed recommendation/action evaluation [active]
```

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

---

## Accepted infrastructure and interaction boundaries

```text
D-028  SQLite-centered local-first operational architecture
D-029  SQLAlchemy Core 2.0 + Alembic 1.x
D-030  pyproject.toml + uv + committed uv.lock + uv_build
D-031  governed deterministic JSON / JSON Schema knowledge interchange
D-032  OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
```

The governed reusable-knowledge round-trip is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Specification 008 promotes the **Project Cockpit** as the V1 primary immersive active-work interaction model. It remains the intended user-facing environment for chat, project navigation, analytical workspaces, evidence, recommendations, decisions, and project state. Final frontend/chart/canvas choices and production backend/API architecture remain open.

---

## Accepted selective-context evidence

Specification 013 accepted a bounded selector that reduces a deliberately wide ten-asset MethodologicalHorizon to 2-3 exact current revisions per task while retaining explicit omission evidence.

Specification 014 then tested the downstream real-model consequence:

```text
reasoner outputs        24 / 24
judge outputs           24 / 24
retries                 0
SELECTIVE quality       1.000000
FULL_HORIZON quality    1.000000
SELECTIVE/FULL input    0.334379
input-token reduction   66.56%
critical regressions    none
```

Supported conclusion:

> Selective exact-revision methodological context preserved every frozen reasoning obligation while materially reducing real provider input burden on the bounded benchmark.

This does not establish a universal context budget or final provider/model.

Primary evidence:

```text
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
docs/checkpoints/146_first_real_reasoning_context_value_gate_passed.md
experiments/reasoning_context_value/V1_REASONING_CONTEXT_VALUE_RESULT.md
```

---

## Recommendation/action evidence so far

Specification 015 was the first three-condition recommendation/action-value test. The workflow completed, but the frozen advancement result was `FAIL`. Fourteen of fifteen gates passed; the single failed gate was an exact `DEFER` versus `NOT_NOW` distinction for two noncritical RA-02 actions. The failed implementation was not promoted.

Specification 016 isolated that semantic boundary prospectively. With DEFER represented as an already-justified action waiting on one exact activating trigger, the live diagnostic produced:

```text
36 / 36 exact dispositions correct
18 / 18 DEFER pointers exact
18 / 18 NOT_NOW pointers null
0 retries
DISPOSITION_BOUNDARY_SUPPORTED
```

The bounded lesson is not that DEFER/NOT_NOW are final production enums. It is that sequencing should carry an explicit dependency relation when deterministic separation from absence of current justification is expected.

---

## Active Specification 017 boundary

Specification 017 returns to the downstream system-value question without rewriting Specification 015.

Frozen conditions:

```text
GENERIC
    project/task/action evidence only

SELECTIVE
    same evidence + accepted task-specific exact methodological revisions

FULL_HORIZON
    same evidence + all ten compact exact Horizon revisions
```

Frozen result shape adds a machine-checkable sequencing pointer:

```text
action_id
disposition
defer_until_id
rationale
```

Every expected DEFER action is prospectively relation-backed. Other dispositions require a null defer pointer.

Frozen outcomes:

```text
PROMOTE_RELATION_BACKED_RECOMMENDATION_SEAM
SAFE_BUT_NOT_DIFFERENTIATED
FAIL
```

Promotion requires all safety/non-regression/expansion gates **and** at least one preregistered positive value signal. A perfect three-condition tie is intentionally `SAFE_BUT_NOT_DIFFERENTIATED`.

Provider-free implementation evidence at head `07da2a091b5686b0378c7f8114495fe1d0b29c32`:

```text
workflow 32655457836
Ubuntu targeted       13 passed
Windows targeted      13 passed
Ubuntu full suite     71 passed, 2 skipped
Windows full suite    71 passed, 2 skipped
```

The complete fake design executes 36 reasoner and 36 judge outputs through real persistence/context construction, preserves attempt ledgers, validates all pointer/basis/menu invariants, and verifies authoritative-state isolation.

Checkpoint 158 freezes the explicit manual live workflow. The final reconciled PR #16 head must still pass ordinary provider-free CI before any live call.

---

## Exact continuation

```text
1. validate the exact final Checkpoint 158 PR #16 head
2. require the Specification 017, reasoning-context, disposition-semantics,
   and checkpoint-metadata workflows all to pass
3. after that exact head is green, make no further experiment-branch commits
4. expose only the identical Specification 017 live workflow on main
5. manually dispatch the workflow from v1-recommendation-action-value-relation-backed
6. enter RUN_SPEC_017_FROZEN
7. preserve the complete live artifact before interpretation
```

No Specification 017 live provider call has occurred.

---

## Repository role

This repository is the project's durable source of truth.

> **The chat is where we think. The repository is where the system remembers.**

The project continues to follow one empirical rule: build the smallest mechanism that can test the architectural hypothesis, preregister what success means where possible, preserve failures as evidence, and promote only what earns its complexity.
