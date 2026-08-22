# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project investigates how to build a rigorous, adaptive, semi-autonomous environment for data-science projects in which a strong LLM is one flexible reasoning component inside a wider system that can own project memory, methodological navigation, provenance, execution coordination, deterministic guarantees where justified, and a professional human interaction surface.

The higher-level question is:

> **Which parts of high-quality data-science process navigation should remain flexible LLM reasoning, which should become explicit system-managed memory or deterministic guarantees, which should be reusable across projects, and where should human judgment remain authoritative?**

The working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

Explicit machinery must earn its complexity empirically.

---

## Current development stage

**Prototype V0 is complete. The project is in bounded V1 implementation and integration.**

Current execution state:

```text
checkpoint            145
active branch         v1-reasoning-context-value
active PR             #12 -> v1-frontend-spike
promoted V1 head      fd33184fbff588c6737d77af751bc5def0e31954
current boundary      Specification 014 pre-live reasoning experiment
```

The provider-free implementation, PR reconciliation, and canonical routing reconciliation are complete. The current branch must remain green under the provider-free cross-platform gates, after which the next substantive action is the manually dispatched frozen live experiment.

No live Specification 014 reasoner/judge result has been observed yet.

For exact continuation, start with:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

---

## Prototype V0 result and durable constraint

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

V0 did not reject persistent project memory, reusable methodological knowledge, provenance, or the broader ADS vision. It rejected carrying P0's large always-on state/context, path-sensitive activation, generic recursive reopening, and full frontier machinery forward unchanged.

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

### Accepted persistence, interchange, and runtime boundaries

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

D-032
    OpenAI Agents SDK behind an ADS-owned ReasoningRuntime port
    validated starting package openai-agents==0.19.4
```

The governed reusable-knowledge persistence/interchange seam is closed across SQLite/Ubuntu, SQLite/Windows, and PostgreSQL 18 through Checkpoint 127.

Direct model calls remain the runtime fallback/reference path. LangGraph remains a possible stronger-durability escalation path. No final LLM provider/model or multi-agent architecture is selected.

### Project Cockpit

Specification 008 promotes the Project Cockpit as the primary immersive V1 active-work interaction model while direct specialist views remain alternative entry, inspection, and record paths.

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

This does not prove that reasoning functions solve general semantic relevance, that `max_assets = 3` is universal, or that selective context improves downstream reasoning.

---

## Active experiment: selective context versus compact full-Horizon reasoning

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

Provider-free implementation now includes the ADS-owned production-facing reasoning types/port, infrastructure OpenAI Agents adapter, isolated accepted-current experiment environment, deterministic condition and call-plan construction, blinded judge adapter, complete attempt/result ledger, ordinary live-API-free cross-platform CI, and a separate secret-gated live workflow.

Checkpoint 145 records the first provider-free implementation gate:

```text
source head  aadf425fdb24db2512e2171f4a99be3c87d8cb80
workflow     V1 reasoning context value / 32568052820
Ubuntu       PASS
Windows      PASS
```

A later fully reconciled pre-live head `23cf0c09fadbe11330edfed19c10e7e194f5be18` also passed the reasoning-context workflow on Ubuntu and Windows plus the relevant checkpoint/Horizon/selective-context regressions.

No live Specification 014 model result has occurred yet.

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

Pre-live implementation and repository reconciliation are complete. Confirm the **current** PR head remains green under the provider-free cross-platform workflows, then manually dispatch:

```text
.github/workflows/v1-reasoning-context-value-live.yml
branch: v1-reasoning-context-value
confirmation: RUN_SPEC_014_FROZEN
secret: OPENAI_API_KEY
```

After the workflow completes:

```text
1. inspect the complete uploaded result artifact
2. preserve raw and aggregate results before any tuning
3. create the live-result checkpoint
4. apply Specification 014's frozen advancement rule
5. only then decide promotion, repair, or the next experiment
```

PR #12 must not be merged on provider-free evidence alone.

Do not change the frozen model, prompts, fixture, semantic rubric, thresholds, repetitions, retry policy, or context construction before the live result is preserved.

---

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

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