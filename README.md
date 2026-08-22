# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that can own project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project does not assume that more orchestration is automatically better. Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

The current active branch is:

```text
v1-reasoning-context-value
```

Active promotion PR:

```text
#12 -> v1-frontend-spike
```

The promoted V1 integration branch currently ends at the PR #11 selective-context merge:

```text
fd33184fbff588c6737d77af751bc5def0e31954
```

Current checkpoint:

```text
145
```

The immediate boundary is **pre-live**. The first real reasoning experiment has been preregistered and implemented provider-free, but no live Specification 014 reasoner/judge call has been executed yet.

See:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

for the exact current continuation.

---

## Prototype V0 result and durable architectural constraint

Prototype V0 compared:

```text
B0 = strong LLM + Python + project artifacts + strong generic data-science instructions

B1 = B0 + four methodological concepts supplied statically

P0 = same strong LLM + typed project state + structured knowledge activation
     + prospective safeguards + state-derived action selection
     + dependency-aware repair
```

Final pooled evidence:

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

Final classification:

> **STRONG FALSIFICATION OF THE CURRENT P0 DESIGN**

The strongest scaling lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

This result did not reject persistent project memory, reusable methodological knowledge, provenance, or the broader ADS vision. It rejected carrying P0's large always-on state/context, path-sensitive activation, generic recursive reopening, and full frontier machinery forward unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project and methodological semantics

The project object model distinguishes:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

with important separations including:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

Methodological navigation follows:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The current scaling path is:

```text
large reusable methodological knowledge universe
    -> high-recall retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> relevance / prioritization
    -> selective task-specific MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> reasoning / recommendation evidence
```

Primary foundations:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

### Accepted persistence and interchange

Accepted V1 decisions include:

```text
D-028
    SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
    SQLAlchemy Core 2.0 + Alembic 1.x

D-030
    pyproject.toml + uv + committed uv.lock + uv_build

D-031
    JSON + JSON Schema Draft 2020-12
    semantic validation
    deterministic reusable-knowledge normalization/serialization
```

The governed reusable-knowledge persistence/interchange seam is closed across:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
```

Primary evidence:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

### Selected initial reasoning runtime infrastructure

D-032 selects:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port

validated starting package
    openai-agents==0.19.4
```

Direct model calls remain the fallback/reference path. LangGraph remains a possible future stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

Primary evidence:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

### Project Cockpit

Specification 008 promotes the Project Cockpit as the primary immersive V1 active-work interaction model while direct specialist views remain alternative entry, inspection, and record paths.

The accepted interaction architecture includes 2D project navigation and recovery, bounded zoom, native laptop pinch capability, viewport-aware stage orientation, scalable Jump/search, compact immersive chrome, collision-safe floating surfaces, true fullscreen, URL-addressable focus state, keyboard accessibility, reduced-motion support, and restrained world-owned ambient depth.

Primary source:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

---

## Retrieval and MethodologicalHorizon progression

The first bounded methodological-navigation program is decomposed as:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational Horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

Current evidence:

```text
Checkpoint 135
    production lexical retrieval
    RH-L Recall@3 = 1.00
    RH-L MRR      = 1.00

Checkpoint 137
    exact dense semantic comparator
    recovered class-imbalance but lost ecdf
    dense-only did not replace lexical

Checkpoint 139
    complementary equal-weight RRF comparator
    RH-S Recall@3 = 1.00
    RH-S MRR      = 0.875

Specification 012 v1.0 / Checkpoint 141
    accepted-current one-hop relation expansion
    TRUE / FALSE / UNKNOWN applicability
    POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    explained MethodologicalHorizon
```

The key semantic invariant is:

```text
unknown != false
```

The hybrid result is evidence for lexical+dense complementarity. It does not permanently select FastEmbed, BGE, RRF `k=60`, embedding persistence, ANN, or a vector database.

---

## Accepted selective MethodologicalContextPack seam

Research 020 and Specification 013 tested the first deterministic RH-C policy:

```text
explicit requested reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact context reads
    -> MethodologicalContextPack
```

The system/model boundary is explicit:

```text
SYSTEM
    retains Horizon
    retains selection/omission decisions and reasons

MODEL-FACING PACK
    contains selected methodological knowledge only
```

On the deliberately wide ten-asset Horizon:

```text
              selected     full bytes   selective   ratio
RH-C01        2 / 10         10,744       2,151     0.2002
RH-C02        2 / 10         10,752       1,770     0.1646
RH-C03        3 / 10         10,752       3,724     0.3464
RH-C04        2 / 10         10,754       3,035     0.2822
```

Equivalent methodology-only context reduction was approximately **65% to 84%** while preserving:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
selected assets                    <= 3
unexplained omissions              0
```

Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

Primary sources:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

The result does not prove that reasoning functions solve general semantic relevance, that `max_assets = 3` is a universal budget, or that selective context improves downstream reasoning.

---

## Active experiment: does selective context help real reasoning?

Research 021, Specification 014 v0.1, the frozen reasoning fixture, and Checkpoint 144 preregister the first downstream real-model comparison.

Conditions:

```text
SELECTIVE
    accepted Specification 013 context
    2-3 exact task-specific revisions

FULL_HORIZON
    all 10 exact included Horizon revisions
    same compact reasoning projection
    same task envelope
```

Frozen reasoner:

```text
OpenAI Agents SDK behind ADS-owned ReasoningRuntime
openai-agents==0.19.4
gpt-5.6-sol
reasoning effort medium
verbosity low
max output tokens 4000
no tools
no previous-response state
```

Frozen blinded judge:

```text
gpt-5.6-sol
reasoning effort high
verbosity low
max output tokens 4000
condition hidden
```

Frozen plan:

```text
4 task classes
2 context conditions
3 repetitions
24 reasoner outputs
24 blinded judge outputs
48 planned successful provider calls
maximum 60 provider attempts
```

Quality gates:

```text
aggregate SELECTIVE >= FULL_HORIZON - 0.05
per-case SELECTIVE >= FULL_HORIZON - 0.10
no reproducible selective-only critical-obligation regression
```

Efficiency gates:

```text
SELECTIVE input tokens < FULL_HORIZON input tokens in every matched pair
per-case mean SELECTIVE/FULL_HORIZON <= 0.80
aggregate mean SELECTIVE/FULL_HORIZON <= 0.80
```

Provider-free implementation is now complete. The first production-facing runtime seam exists under `src/ads_system`, deterministic experiment/environment/runner infrastructure exists under `experiments/reasoning_context_value`, ordinary CI is explicitly live-API-free, and the secret-gated live workflow exists separately.

Checkpoint 145 records the first provider-free implementation gate:

```text
source head aadf425fdb24db2512e2171f4a99be3c87d8cb80
workflow    V1 reasoning context value / 32568052820
Ubuntu      PASS
Windows     PASS
```

No live Specification 014 model call has occurred yet.

Primary active sources:

```text
docs/research/021_first_reasoning_context_value_vertical_slice_design.md
docs/specifications/014_v1_reasoning_context_value_vertical_slice.md
tests/fixtures/reasoning/context_value_v1.json
docs/checkpoints/144_first_reasoning_context_value_contract_frozen.md
docs/checkpoints/145_reasoning_context_value_implementation_gate_cross_platform_passed.md
```

---

## Exact continuation

Before live execution:

```text
1. finish PR #12 reconciliation
2. validate the exact reconciled head cross-platform
```

Then manually dispatch:

```text
.github/workflows/v1-reasoning-context-value-live.yml
```

from:

```text
v1-reasoning-context-value
```

with confirmation:

```text
RUN_SPEC_014_FROZEN
```

and repository secret `OPENAI_API_KEY` available.

The live result must be preserved before changing any frozen model, prompt, fixture, rubric, threshold, repetition count, retry policy, or context condition.

---

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The preservation model distinguishes:

```text
canonical current documents
foundational design memos
current specifications and evaluation contracts
checkpoints and historical provenance
experiment-specific result ledgers
routing/index knowledge
Git history
```

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

## Start here

```text
docs/CURRENT_STATE.md
    concise present state and exact next step

docs/KNOWLEDGE_MAP.md
    routing layer

docs/VISION.md
    current high-level product/system direction

docs/PRINCIPLES.md
    accepted high-level design principles

docs/DECISIONS.md
    accepted project-level decisions

docs/OPEN_QUESTIONS.md
    current unresolved questions

docs/DEVELOPMENT_METHOD.md
    development and preservation method

docs/CONTINUITY.md
    continuation procedure

docs/MAJOR_CHANGES.md
    selective structural history
```

## Development philosophy

The project deliberately resists two opposite mistakes:

```text
Mistake 1:
Assume that because a strong LLM can already do impressive data-science reasoning,
there is no value in system-level process machinery.

Mistake 2:
Assume that because the long-term vision is broader than one LLM conversation,
every piece of orchestration machinery is automatically justified.
```

The current stance is empirical:

> **Build the smallest mechanism that can test the architectural hypothesis, preregister what success means when possible, preserve failures as evidence, and promote only what earns its complexity.**