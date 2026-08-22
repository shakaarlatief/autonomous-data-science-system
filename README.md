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

This closes the governed persistence/interchange implementation gate. It does not validate retrieval quality, embeddings, reranking, MethodologicalHorizon construction, selective LLM context quality, external-source ingestion, or knowledge-authoring UX.

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

The bakeoff compared:

```text
Direct model calls
    minimum dependency surface
    maximum explicit control
    more ADS-owned generic orchestration

OpenAI Agents SDK 0.19.4
    AR-01 through AR-12 PASS
    smaller complete runtime surface
    native approval / RunState / MCP / structured-output / timeout infrastructure

LangGraph 1.2.10
    complete ADS-shaped capability PASS
    stronger explicit persisted checkpoint/replay machinery
    larger dependency/operational/topology surface
```

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

`Agent != Project`, `RunState != project memory`, and framework tracing/checkpoints do not become authoritative ADS state.

Direct model calls remain a fallback/reference escape path. LangGraph remains a future escalation path if materially stronger long-running workflow durability becomes necessary. Microsoft Agent Framework and Google ADK 2.0 were not implemented after the Specification 005 stop rule found no current differentiator likely to overturn the selection.

No final LLM provider/model or multi-agent architecture is selected.

Primary sources:

```text
docs/DECISIONS.md, D-032
docs/specifications/005_v1_agent_runtime_and_interoperability_bakeoff.md
docs/research/015_langgraph_complete_candidate_three_way_runtime_comparison_and_stop_rule.md
docs/checkpoints/129_direct_model_call_runtime_control_cross_platform_gate_passed.md
docs/checkpoints/131_openai_agents_complete_runtime_candidate_cross_platform_gate_passed.md
docs/checkpoints/132_langgraph_durability_comparator_cross_platform_gate_passed.md
docs/checkpoints/133_v1_reasoning_runtime_selected_and_bakeoff_closed.md
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

Checkpoint 130 records later bounded polish for normal-window Jump/composer collision safety and faster anchored pinch.

```text
head ae83e920b3fa43ee8242bdb1ca2640d23a474c71
run 167 / 32503861255

Ubuntu build + unit tests                  PASS
Windows build + unit tests                 PASS
Chromium interaction/accessibility         PASS
controlled direct-view visual regression   PASS
normal-window Jump re-clamp regression      PASS
faster anchored pinch regression            PASS
```

The subsequent real-browser/hardware retest accepted the repaired behavior as good enough to continue. The tiny occasional pinch hitch remains deferred non-blocking polish, and exact pinch constants remain unfrozen.

Primary latest sources:

```text
docs/research/012_post_promotion_cockpit_normal_window_and_pinch_sensitivity_review.md
docs/checkpoints/130_post_promotion_cockpit_normal_window_and_pinch_polish_gate_passed.md
```

Promotion deliberately does **not** freeze graph/canvas or gesture libraries, auto-layout, semantic zoom, minimap, final pinch/zoom constants, production project-search backend, final stage taxonomy, final stage-ruler visual treatment, permanent tool-rail styling, final visual identity, or a canonical Cockpit screenshot baseline.

## Immediate active track

The runtime selection question is closed for initial V1. The highest-value methodological track is now production retrieval and MethodologicalHorizon construction.

```text
Q-044
    production retrieval / MethodologicalHorizon construction

Q-045
    recommendation quality separated from catalog/retrieval coverage
```

The next benchmark should evaluate:

```text
retrieval-quality fixtures
production lexical retrieval
semantic retrieval as an empirical candidate
lexical/semantic fusion only if justified
ranking and omission quality
first bounded real MethodologicalHorizon
selective LLM context quality and cost
```

Do not select an embedding model, reranker, ANN service, or vector database from intuition.

## Current execution order

```text
1. finish runtime-branch reconciliation, CI and merge into v1-frontend-spike
2. inspect current production retrieval/persistence surfaces
3. define retrieval / MethodologicalHorizon benchmark fixtures and acceptance criteria
4. implement and evaluate lexical retrieval first
5. evaluate semantic retrieval and fusion/reranking only if evidence justifies them
6. build the first bounded real MethodologicalHorizon and selective context assembly
7. integrate the selected runtime behind an ADS-owned production port when a real reasoning vertical slice needs it
```

## Active branch and continuation

Current runtime-selection reconciliation lives on:

```text
v1-runtime-bakeoff
```

The promoted frontend/V1 boundary is preserved on:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails current V1 work. New sessions must reconstruct current execution from the canonical routing documents and the active promoted branch rather than assuming `main` is current.

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