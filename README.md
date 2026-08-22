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

> **Create the best data-science process for the particular project, where what "best" means is configurable according to the project's goals, constraints, required outputs, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective.

## Current development stage

**Prototype V0 is complete. The project is now in bounded V1 implementation and integration.**

V0 compared:

```text
B0 = strong LLM + Python + project artifacts + strong generic data-science instructions

B1 = B0 + four methodological concepts supplied statically

P0 = same strong LLM + typed project state + structured knowledge activation
     + prospective safeguards + state-derived action selection
     + dependency-aware repair
```

### V0 result

**The current P0 design received a strong falsification signal.**

```text
                         B0          B1          P0
Targeted mean           1.47        1.73        1.78
Strong targeted pass    0/10        0/10        0/10
Critical failure runs   0/10        0/10        0/10
Completed in budget    10/10       10/10        3/10
Budget exhausted        0/10        0/10        7/10
Median total tokens  122,544.5   120,564.5   260,370.0
```

P0 improved the targeted semantic score over B1 by only `+0.05`, while using `2.160x` B1's median tokens and completing only `3/10` runs within budget.

The strongest architectural lesson is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

The result does **not** falsify persistent project memory, reusable methodological knowledge, provenance, or the broader Autonomous Data Science System vision. It does falsify carrying P0's large always-on state/context, path-sensitive activation, generic recursive reopening, and full frontier machinery forward unchanged.

Detailed evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
```

## Current V1 architecture

The post-V0 design has several connected but deliberately bounded tracks.

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

A potentially large global knowledge universe is narrowed into a bounded project-specific **MethodologicalHorizon** before selective reasoning context is assembled.

Primary sources:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/foundations/019_methodological_navigation_brain_and_relevance_architecture.md
docs/foundations/020_reusable_methodological_knowledge_representation_architecture.md
```

### Accepted V1 persistence and interchange

Accepted decisions currently include:

```text
D-028
SQLite-centered local-first operational architecture

D-029 + Specification 002 v1.1
SQLAlchemy Core 2.0 + Alembic 1.x
PostgreSQL identifier portability
unique Alembic revision IDs <= 32 chars while the default version table remains

D-030
pyproject.toml + uv + committed uv.lock + uv_build

D-031
JSON + JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic reusable-knowledge serialization
```

The richer governed reusable-knowledge persistence/interchange seam is **closed across all required environments**.

```text
V1 governed knowledge roundtrip closure gate
run 32496856945

SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS
```

Validated behavior includes candidate import, explicit acceptance, accepted-current pointers, accepted snapshot export, provenance, relation governance, collections, migration compatibility, and historical project revision pinning across later knowledge acceptance.

Primary sources:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

### Selected V1 reasoning runtime

Runtime infrastructure is replaceable infrastructure, not ADS domain authority.

After an executable three-way bakeoff, D-032 selects:

```text
OpenAI Agents SDK
    behind an ADS-owned ReasoningRuntime port

validated starting package
    openai-agents==0.19.4
```

Direct model calls remain a fallback/reference escape path. LangGraph remains a future escalation path if materially stronger long-running workflow durability becomes necessary. No final LLM provider/model or multi-agent architecture is selected.

Primary sources:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
```

### Production retrieval and MethodologicalHorizon track

Research 016 and Specification 009 define the current retrieval/Horizon evaluation decomposition:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

#### 1. Production lexical retrieval

The first production retrieval channel is implemented behind a storage-neutral application port:

```text
KnowledgeRetrievalPort
KnowledgeRetrievalHit
    -> SqliteFtsKnowledgeRetrieval
    -> rebuildable accepted-current FTS5 projection
```

Checkpoint 135 validates:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
```

The one lexical semantic miss is RH-S01 `class-imbalance`.

#### 2. Exact dense semantic comparator

Specification 010 / Checkpoint 137 tested FastEmbed 0.8.0 with `BAAI/bge-small-en-v1.5` as an experiment-only exact in-process dense channel.

Observed:

```text
RH-L Recall@3            1.00
RH-L MRR                 1.00
RH-S Recall@3            0.75
RH-S MRR                 0.75
```

Dense retrieval recovered the lexical `class-imbalance` miss at rank 1, but displaced RH-S04 `ecdf` from the semantic top 3. Dense-only therefore did not earn replacement of lexical retrieval.

#### 3. Complementary rank fusion

Because the two channels made complementary misses, Specification 011 preregistered the smallest score-scale-independent fusion comparator: equal-weight Reciprocal Rank Fusion over the unchanged lexical and dense top-three rankings.

Checkpoint 139 / workflow run `32561118325` passed on Ubuntu and Windows:

```text
RH-S Recall@3            1.00
RH-S MRR                 0.875
RH-S critical omissions  0 / 4
RH-L Recall@3            1.00
RH-L MRR                 1.00
```

`class-imbalance` survives through the dense channel and `ecdf` survives through the lexical channel.

This makes hybrid lexical + exact semantic retrieval the leading V1 retrieval hypothesis for this benchmark. It does **not** permanently select FastEmbed, BGE, RRF `k=60`, vector persistence, ANN, or a vector database.

#### 4. First real MethodologicalHorizon

Specification 012 v1.0 / Checkpoint 141 validate the first production-facing Horizon seam:

```text
stable/revision-transparent direct candidates
    -> accepted-current KnowledgeNavigationRepository reads
    -> outbound one-hop accepted relation expansion
    -> deterministic TRUE / FALSE / UNKNOWN applicability evaluation
    -> POSSIBLY_APPLICABLE / INAPPLICABLE / MISSING_CONTEXT
    -> explained included/excluded MethodologicalHorizon
```

Cross-platform gate:

```text
V1 first MethodologicalHorizon builder
run 32561727632

Ubuntu PASS
Windows PASS
RH-R relation cases       4 / 4 PASS
RH-A applicability cases  5 / 5 PASS
authoritative knowledge   unchanged
39 passed, 2 skipped on each OS
```

Validated examples include:

```text
random-forest
    -> bagging
    -> gradient-boosted-trees

temporal-validation
    -> prediction-moment

prediction-time-feature-eligibility
    -> prediction-moment

histogram
    -> ecdf
```

and the key applicability distinction:

```text
known false supervision context
    -> random-forest INAPPLICABLE

missing required context
    -> MISSING_CONTEXT, not false
```

The executable semantic invariant is:

```text
unknown != false
```

Primary sources:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/research/017_exact_semantic_retrieval_comparator_selection.md
docs/research/018_dense_semantic_failure_complementarity_and_rrf_fusion_rationale.md
docs/research/019_first_methodological_horizon_application_seam.md

docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/specifications/010_v1_exact_semantic_retrieval_comparator.md
docs/specifications/011_v1_rrf_hybrid_retrieval_comparator.md
docs/specifications/012_v1_first_methodological_horizon_builder.md

docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
docs/checkpoints/137_dense_semantic_retrieval_comparator_cross_platform_result_preserved.md
docs/checkpoints/139_rrf_hybrid_retrieval_cross_platform_gate_passed.md
docs/checkpoints/141_first_methodological_horizon_cross_platform_gate_passed.md

experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
experiments/retrieval/V1_RRF_HYBRID_RETRIEVAL_RESULT.md
experiments/retrieval/V1_METHODOLOGICAL_HORIZON_RESULT.md
```

### Professional frontend and Project Cockpit

The frontend is a first-class reasoning, control, and quality surface rather than an end-stage presentation layer.

The Project Cockpit is a **promoted V1 interaction architecture** after seven real-browser human review cycles and repeated executable gates.

Current authoritative interaction contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promoted model:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process projection
    native system interaction
    spatial navigation
    smooth focus into real analytical workspaces

Direct specialist views
    alternative inspection / entry / record paths
    reuse the same substantive analytical modules and project state
```

The accepted interaction architecture includes:

```text
meaningful work units rather than every persisted object
spatial focus into reusable specialist workspaces
reachability != simultaneous mounting
FiniteNavigableGridWorld != SemanticProjectPlane
2D project navigation and recovery
bounded geometric zoom and native laptop pinch
viewport-aware semantic stage orientation
scalable Jump/search
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility and reduced-motion support
world-owned restrained ambient depth
```

Checkpoint 130 records later bounded polish for normal-window Jump/composer collision safety and faster anchored pinch. The subsequent real-browser/hardware retest accepted the repaired behavior as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish.

Promotion deliberately does **not** freeze graph/canvas or gesture libraries, auto-layout, semantic zoom, minimap, final pinch/zoom constants, production project-search backend, final stage taxonomy, final stage-ruler visual treatment, permanent tool-rail styling, final visual identity, or a canonical Cockpit screenshot baseline.

## Immediate active track

The next methodological question is no longer whether the first Horizon can retrieve and classify the ten-asset benchmark. That boundary has passed.

The immediate next gate is:

```text
explained MethodologicalHorizon
    -> relevance / prioritization
    -> selective task-specific context
    -> exact required revision coverage
    -> irrelevant-context cost
    -> serialized size / token burden
    -> explicit omission reasons
```

Execution order:

```text
1. finish final PR #10 reconciliation and validate its exact head
2. merge the green retrieval/Horizon promotion into v1-frontend-spike
3. branch from that promoted boundary
4. freeze RH-C relevance/selective-context scenarios before implementation
5. implement the smallest bounded selection policy that can falsify the design
6. measure revision coverage, irrelevant context, size/token burden, and omission quality
7. only then connect a real MethodologicalContextPack to the selected ReasoningRuntime adapter
```

Do not keep tuning retrieval simply because it can be tuned. Do not introduce an LLM relevance judge, reranker, ANN service, vector database, or large context policy before evidence shows that the simpler boundary is insufficient.

## Active branch and continuation

Current retrieval / MethodologicalHorizon promotion work lives on:

```text
v1-semantic-retrieval
PR #10 -> v1-frontend-spike
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

> **Build only the system mechanisms that demonstrably improve the reliability, coverage, efficiency, reuse, traceability, professional usability, or human-navigation burden of real data-science work beyond what strong simpler workflows already achieve.**
