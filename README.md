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

D-029
SQLAlchemy Core 2.0 + Alembic 1.x

D-030
pyproject.toml + uv + committed uv.lock + uv_build

D-031
JSON + JSON Schema Draft 2020-12
+ application semantic validation
+ deterministic reusable-knowledge serialization
```

The first production persistence vertical slice passed on SQLite/Linux, SQLite/Windows, and PostgreSQL 18 and proves exact historical project-to-knowledge revision pinning.

The richer governed reusable-knowledge persistence/interchange seam is now also **closed across all required environments**.

Final governed round-trip evidence:

```text
V1 governed knowledge roundtrip closure gate
run 32496856945

SQLite / Ubuntu     PASS
SQLite / Windows    PASS
PostgreSQL 18       PASS
Alembic revision-ID portability guard PASS on all three jobs
```

Validated governed behavior includes candidate import, explicit acceptance, accepted-current pointers, accepted snapshot export, provenance, relation governance, collections, migration 0002, and historical project revision pinning across later knowledge acceptance.

Two PostgreSQL portability defects were found and repaired before closure:

```text
1. a manually named migration constraint exceeded PostgreSQL's 63-byte identifier limit
2. the Alembic revision identity `0002_reusable_knowledge_interchange`
   exceeded the default `alembic_version.version_num VARCHAR(32)` envelope
```

Migration 0002 now uses:

```text
revision = "0002_knowledge_interchange"
down_revision = "0001_v1_persistence_core"
```

A deterministic regression test now enforces unique Alembic revision IDs whose length does not exceed 32 characters.

Primary closure sources:

```text
experiments/architecture_spikes/V1_KNOWLEDGE_ROUNDTRIP_RESULT.md
docs/checkpoints/127_governed_knowledge_roundtrip_closed_across_sqlite_and_postgresql.md
```

This closes the governed persistence/interchange implementation gate. It does not validate retrieval quality, embeddings, reranking, MethodologicalHorizon construction, selective LLM context quality, external-source ingestion, or knowledge-authoring UX.

### Agent/runtime boundary

Agent frameworks and interoperability protocols are treated as replaceable infrastructure, not ADS domain authority.

No agent runtime, LLM provider, or multi-agent architecture is accepted yet. Specification 005 defines an empirical bakeoff among current runtime candidates, beginning with one principal reasoner and allowing a simple direct-model-call result if no framework earns its complexity.

This bakeoff is now the immediate bounded execution track.

### Professional frontend and Project Cockpit

The frontend is a first-class reasoning, control, and quality surface rather than an end-stage presentation layer.

The Project Cockpit has moved from candidate interaction spike to a **promoted V1 interaction architecture** after seven real-browser human review cycles and repeated executable gates.

Current authoritative interaction contract:

```text
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
```

Promoted product model:

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

The promoted interaction architecture includes:

```text
meaningful work units rather than every persisted object
spatial focus into reusable specialist workspaces
reachability != simultaneous mounting

FiniteNavigableGridWorld != SemanticProjectPlane
    continuous grid through surrounding reserve
    symmetric navigation/recovery
    semantic stage space kept distinct from neutral reserve
    world-owned restrained ambient depth

two-dimensional navigation
bounded geometric zoom
native laptop pinch capability
viewport-aware stage orientation
scalable Jump/search
compact/fold-away immersive chrome
collision-safe floating surfaces
true fullscreen with graceful fallback
URL-addressable focus/deep-work state
keyboard accessibility
reduced-motion support
```

Final validated Cockpit promotion head:

```text
2c3b522e2416d73c015ce5ec2a4560a227524dd9
```

Final gate:

```text
V1 frontend spike
run 155 / 32492536072

Ubuntu build + unit tests                 PASS
Windows build + unit tests                PASS
Chromium interaction/accessibility        PASS
controlled direct-view visual regression  PASS
```

Key promotion sources:

```text
docs/research/009_seventh_cockpit_human_review_pinch_responsiveness_and_interaction_promotion.md
docs/specifications/008_v1_project_cockpit_interaction_architecture.md
docs/checkpoints/126_seventh_cockpit_review_validated_and_interaction_architecture_promoted.md
```

Promotion deliberately does **not** freeze a graph/canvas library, gesture library, auto-layout algorithm, semantic zoom, minimap, final native-pinch constants, final geometric zoom range, production project-search backend, final stage taxonomy, final stage-ruler visual treatment, permanent tool-rail styling, final visual identity, or canonical Cockpit screenshot baseline.

The tiny remaining pinch hitch is preserved as deferred product polish, not as a blocker for the interaction architecture.

## Current execution order

```text
1. Specification 005 one-principal-reasoner agent-runtime bakeoff
2. production retrieval / MethodologicalHorizon benchmark
3. future Cockpit capability and polish on top of Specification 008
```

The runtime bakeoff must preserve a simpler direct-model-call architecture as a valid outcome if no framework earns its complexity.

The retrieval/horizon benchmark should evaluate omission quality, relevance, and context cost before selecting embeddings, rerankers, ANN services, or vector infrastructure.

## Active branch and continuation

The current V1/frontend work is being developed on:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails this active branch. New sessions working on the current V1 state must reconstruct from `v1-frontend-spike` rather than assuming `main` contains the latest checkpoints and promoted contracts.

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
    Accepted or candidate implementation/evaluation contracts.

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
