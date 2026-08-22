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

Two PostgreSQL portability defects were found and repaired before closure: an overlong manually named migration constraint and an Alembic revision identity too long for the default `alembic_version.version_num VARCHAR(32)` envelope. Migration 0002 now uses `0002_knowledge_interchange`, and a deterministic regression guard protects that portability invariant.

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

The package version is a validated baseline, not permanent framework lock-in.

The bakeoff compared direct model calls, OpenAI Agents SDK 0.19.4, and LangGraph 1.2.10 against the same ADS-owned workload and authority boundary.

Cross-platform evidence:

```text
direct-call control
    workflow 32500521858
    Ubuntu PASS
    Windows PASS

OpenAI Agents SDK 0.19.4
    workflow 32555526773
    Ubuntu PASS
    Windows PASS
    AR-01 through AR-12 PASS

LangGraph 1.2.10 durability comparator
    workflow 32556382248
    Ubuntu PASS, 9 tests
    Windows PASS, 9 tests
```

The architecture boundary remains:

```text
ADS owns
    project and methodological semantics
    MethodologicalContextPack construction
    context digests and exact knowledge revisions
    human-control policy
    authoritative side-effect idempotency/domain events
    stable RuntimeTrace/provenance

runtime owns
    replaceable execution mechanics
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

Research 016 and frozen Specification 009 v0.1 now define the first production retrieval/Horizon evaluation boundary:

```text
RH-L    lexical-addressable retrieval
RH-S    semantic/paraphrase retrieval diagnostics
RH-R    relational horizon expansion
RH-A    applicability / required-context behavior
RH-C    selective context construction
```

The first production retrieval channel is now implemented behind a storage-neutral application port:

```text
KnowledgeRetrievalPort
KnowledgeRetrievalHit
    -> SqliteFtsKnowledgeRetrieval
    -> rebuildable accepted-current FTS5 projection
```

Checkpoint 135 validates the frozen lexical baseline cross-platform:

```text
V1 methodological horizon
run 32559177057
source head c462365bf64ebe9d676a0d9ce6402bba61e67279

Ubuntu     PASS
Windows    PASS
```

Observed quality on the ten-asset stress corpus:

```text
indexed accepted-current assets    10
RH-L Recall@3                      1.00
RH-L MRR                           1.00
RH-L critical omissions            0 / 10
RH-L required target rank 1       10 / 10
RH-S diagnostic Recall@3           0.75
```

The frozen lexical-addressable cases are therefore completely covered. The one measured semantic miss is RH-S01:

```text
positive cases are scarce and overall correctness hides failures on them
    -> target class-imbalance
    -> lexical result: no hits
```

The other three frozen RH-S targets are recovered at rank 1 by the lexical channel.

This gives the semantic comparator a concrete measured gap to beat. It does not preselect an embedding model, vector database, ANN service, fusion algorithm, reranker, or final HorizonBuilder.

Primary sources:

```text
docs/research/016_production_retrieval_and_methodological_horizon_benchmark_design.md
docs/specifications/009_v1_retrieval_and_methodological_horizon_benchmark.md
docs/checkpoints/134_retrieval_and_methodological_horizon_benchmark_contract_frozen.md
docs/checkpoints/135_first_production_lexical_retrieval_baseline_cross_platform_passed.md
experiments/retrieval/V1_LEXICAL_RETRIEVAL_RESULT.md
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

Promotion gate:

```text
head 2c3b522e2416d73c015ce5ec2a4560a227524dd9
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-view visual regression  PASS
```

Checkpoint 130 records later bounded polish for normal-window Jump/composer collision safety and faster anchored pinch. The subsequent real-browser/hardware retest accepted the repaired behavior as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish.

Promotion deliberately does **not** freeze graph/canvas or gesture libraries, auto-layout, semantic zoom, minimap, final pinch/zoom constants, production project-search backend, final stage taxonomy, final stage-ruler visual treatment, permanent tool-rail styling, final visual identity, or a canonical Cockpit screenshot baseline.

## Immediate active track

The highest-value methodological track is Q-044/Q-045 production retrieval and MethodologicalHorizon construction.

The lexical baseline is now validated. The immediate next comparison is semantic retrieval against the unchanged RH-S cases.

```text
1. merge the independently validated lexical slice
2. create a bounded semantic-retrieval branch from that merged boundary
3. evaluate the smallest meaningful exact/in-process semantic comparator
4. measure incremental useful recall and irrelevant candidate growth
5. retain fusion only if lexical and semantic channels are materially complementary
6. execute RH-R relation expansion and RH-A applicability/context cases
7. construct the first bounded real MethodologicalHorizon
8. evaluate RH-C selective LLM context quality and cost
```

Do not select an embedding model, vector database, ANN service, fusion algorithm, or reranker from intuition.

## Active branch and continuation

Current retrieval / MethodologicalHorizon work lives on:

```text
v1-methodological-horizon
```

The promoted V1 integration branch is:

```text
v1-frontend-spike
```

Runtime-selection PR #8 has already been merged into that branch at:

```text
de78501c3990bce9657fe02a117c9186c76a7955
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