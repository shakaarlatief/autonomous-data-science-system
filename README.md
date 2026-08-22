# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project explores how to build a rigorous, adaptive, semi-autonomous system for carrying out data-science projects from problem understanding through analysis, experimentation, modelling, evaluation, reporting, and delivery.

Modern LLMs can already perform substantial portions of a data project. That does not imply that one long end-to-end conversation reliably produces the best process for every project.

The higher-level question is:

> How much of the process navigation, methodological memory, project memory, evidence discipline, repair, execution control, provenance, and selective human involvement that currently lives in a skilled human-LLM workflow should be made explicit and reusable in a wider system?

The LLM is treated as a powerful reasoning component inside that wider system, not as the system itself. Explicit architecture is not automatically valuable either; every mechanism should earn its complexity through evidence.

## Working purpose

The current working purpose is:

> **Create the best defensible data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, risk, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective.

---

## Current development stage

**Prototype V0 is complete. The project is now in bounded V1 implementation and integration.**

### Prototype V0 result

V0 compared:

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

The strongest architectural lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The result does **not** falsify persistent project memory, reusable methodological knowledge, provenance, or the broader ADS vision. It falsifies carrying P0's large always-on state/context, path-sensitive activation, generic recursive reopening, and full frontier machinery forward unchanged.

Primary evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

---

## Current V1 architecture

### Project and methodological semantics

The current foundations distinguish:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

and preserve distinctions such as:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

The methodological-navigation brain uses:

```text
KNOWN
    -> APPLICABLE
    -> RELEVANT
    -> RECOMMENDED
    -> REQUIRED / BLOCKING
```

The intended scaling path is:

```text
large global methodological knowledge universe
    -> high-recall retrieval
    -> bounded explained MethodologicalHorizon
    -> applicability / missing-context handling
    -> relevance / prioritization
    -> selective task-specific methodological context
    -> LLM reasoning
```

Primary sources:

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
+ semantic validation
+ deterministic reusable-knowledge serialization
```

The governed reusable-knowledge persistence/interchange seam is closed across:

```text
SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS
```

Primary evidence:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

### Selected V1 reasoning runtime

D-032 selects:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port

validated starting package
    openai-agents==0.19.4
```

Direct model calls remain the fallback/reference path. LangGraph remains a future escalation path if materially stronger long-running workflow durability becomes necessary. No final LLM provider/model or multi-agent architecture is selected.

Primary evidence:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

### Promoted Project Cockpit interaction architecture

The frontend is treated as a first-class reasoning, control, and quality surface rather than an end-stage presentation layer.

Specification 008 promotes the Project Cockpit as the primary immersive V1 active-work model:

```text
Project Cockpit
    living project-process projection
    native system interaction
    spatial navigation
    smooth focus into real analytical workspaces

Direct specialist views
    alternative inspection / entry / record paths
    reuse the same substantive analytical modules and project state
```

The accepted interaction architecture includes bounded 2D navigation, zoom/recovery, native pinch capability, scalable Jump/search, compact immersive chrome, collision-safe floating surfaces, true fullscreen, URL-addressable focus state, keyboard accessibility, reduced-motion support, and restrained world-owned ambient depth.

The later normal-window/pinch repair at Checkpoint 130 is accepted as good enough to continue. Final frontend stack promotion, chart library, graph/canvas dependencies, auto-layout, semantic zoom, minimap, stage taxonomy, URL contract, and final visual identity remain open.

Primary source:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

---

## Production retrieval and MethodologicalHorizon progression

Research 016 and Specification 009 decompose the current benchmark into:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

### 1. Production lexical retrieval

Checkpoint 135 validates the first production lexical retriever behind a storage-neutral application port:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

The one lexical semantic miss is `class-imbalance`.

### 2. Exact dense semantic comparator

Checkpoint 137 tested FastEmbed 0.8.0 with `BAAI/bge-small-en-v1.5` as an experiment-only exact dense channel.

Dense retrieval recovered `class-imbalance` but displaced `ecdf` from the semantic top three. Dense-only therefore did not earn replacement of lexical retrieval.

### 3. Complementary hybrid comparator

Specification 011 / Checkpoint 139 tested equal-weight Reciprocal Rank Fusion over the unchanged lexical and dense top-three rankings.

Observed:

```text
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

This is evidence for lexical+dense complementarity, not permanent selection of FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, or a vector database.

### 4. First explained MethodologicalHorizon

Specification 012 v1.0 / Checkpoint 141 validate:

```text
stable/revision-transparent candidates
    -> accepted-current KnowledgeNavigationRepository reads
    -> outbound one-hop accepted relation expansion
    -> deterministic TRUE / FALSE / UNKNOWN applicability
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained MethodologicalHorizon
```

The key semantic invariant is:

```text
unknown != false
```

PR #10 containing the dense-complementarity, hybrid-retrieval, and first-Horizon slice was merged into `v1-frontend-spike` at:

```text
9319ed9b0a401efa1be85c27a9ce4424a8ce5e1e
```

---

## First selective MethodologicalContextPack seam

Research 020 and Specification 013 froze the next RH-C experiment before implementation.

The first deterministic hypothesis was:

```text
explicit requested reasoning functions
    -> primary Horizon matches
    -> bounded REQUIRES_CONCEPT support
    -> hard max_assets budget
    -> exact accepted-current compact context reads
    -> MethodologicalContextPack
```

The implementation preserves the critical boundary:

```text
SYSTEM
    retains MethodologicalHorizon
    retains selection and omission decisions
    retains omission reasons and diagnostics

MODEL-FACING PACK
    contains selected methodological knowledge only
```

The frozen gate passed on Ubuntu and Windows without changing targets or thresholds.

Observed on the deliberately wide ten-asset Horizon:

```text
              selected     full bytes   selective   ratio
RH-C01        2 / 10         10,744       2,151     0.2002
RH-C02        2 / 10         10,752       1,770     0.1646
RH-C03        3 / 10         10,752       3,724     0.3464
RH-C04        2 / 10         10,754       3,035     0.2822
```

Equivalent context reduction was approximately **65% to 84%** while preserving:

```text
required stable-key coverage       1.00
required exact-revision coverage   1.00
irrelevant selected assets         0
selected assets                    <= 3
unexplained omissions              0
```

The full suite passed:

```text
Ubuntu   42 passed, 2 skipped
Windows  42 passed, 2 skipped
```

Additional validated behavior includes stale-revision fail-closed reads, explicit `BUDGET_LIMIT`, post-budget full-context materialization, deterministic canonical serialization, cross-platform identical digests, retained `MISSING_CONTEXT`, and omission of retrieval metadata from model-facing context.

Checkpoint 143 promotes Specification 013 to accepted bounded v1.0.

Primary sources:

```text
docs/research/020_first_horizon_relevance_and_selective_context_gate_design.md
docs/specifications/013_v1_horizon_relevance_and_selective_context.md
docs/checkpoints/142_relevance_and_selective_context_contract_frozen.md
docs/checkpoints/143_selective_methodological_context_gate_passed_and_promotion_authorized.md
experiments/retrieval/V1_SELECTIVE_CONTEXT_RESULT.md
```

The result does **not** prove that reasoning functions solve general semantic relevance, that `max_assets = 3` is a universal budget, or that selective context improves downstream model reasoning. Those remain later questions.

---

## Immediate active track

The immediate work is the final promotion of PR #11:

```text
1. complete canonical/routing reconciliation
2. update PR #11 with the measured RH-C result
3. validate the exact reconciled PR head
4. merge exactly that green head into v1-frontend-spike
```

After that, the next experiment should **not** be more retrieval or selector tuning.

The next justified boundary is a real reasoning vertical slice:

```text
same frozen project/task evidence
    -> selective MethodologicalContextPack
    -> ADS-owned ReasoningRuntime
    -> one concrete model configuration

versus

same frozen project/task evidence
    -> strong full-Horizon/simple context control
    -> same ReasoningRuntime
    -> same concrete model configuration
```

The experiment should be preregistered before model calls and should measure reasoning quality against frozen obligations, critical methodological omissions, exact supplied knowledge revisions, exact provider/model tokens, latency/cost where observable, and whether context reduction helps or harms real reasoning.

---

## Active branch and continuation

Current selective-context promotion work lives on:

```text
v1-relevance-selective-context
PR #11 -> v1-frontend-spike
```

The promoted V1 integration branch is:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails current V1 work. New sessions must reconstruct current execution from the canonical routing documents and the active branch rather than assuming `main` is current.

Current continuity and exact next action are maintained in:

```text
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
```

---

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The preservation architecture distinguishes:

```text
canonical current documents
foundational design memos
current specifications and evaluation contracts
checkpoints and historical provenance
experiment-specific ledgers
routing/index knowledge
Git history
```

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

Preservation includes not only durability, but also discoverability, promotion, authority, reconciliation, and recovery after unexpected session boundaries.

---

## Start here

```text
docs/CURRENT_STATE.md
    Concise current state, exact priority, and next step.

docs/KNOWLEDGE_MAP.md
    Routing layer showing where important knowledge lives.

docs/VISION.md
    Current system vision and purpose.

docs/PRINCIPLES.md
    Current high-level design principles.

docs/DECISIONS.md
    Accepted project-level decisions.

docs/OPEN_QUESTIONS.md
    Current unresolved questions.

docs/DEVELOPMENT_METHOD.md
    Method for developing and preserving the project.

docs/CONTINUITY.md
    Procedure for reliable continuation across chats and models.

docs/MAJOR_CHANGES.md
    Selective history of major architectural and methodological changes.

docs/foundations/
    Detailed durable reasoning.

docs/research/
    Current bounded design and ecosystem research.

docs/specifications/
    Accepted, completed, or candidate implementation/evaluation contracts.

docs/checkpoints/
    Historical snapshots and milestone records.
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
