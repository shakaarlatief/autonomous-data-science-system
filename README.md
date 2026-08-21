# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project explores how to build a rigorous, adaptive, semi-autonomous system for carrying out data-science projects from problem understanding through analysis, experimentation, modelling, evaluation, reporting, and delivery.

Modern LLMs can already perform substantial portions of a data project. That does not imply that one long end-to-end conversation reliably produces the best possible process for every project.

The higher-level question is:

> How much of the process navigation, methodological memory, project memory, evidence discipline, repair, execution control, provenance, and selective human involvement that currently lives in a skilled human-LLM workflow should be made explicit and reusable in a wider system?

The LLM is treated as a powerful reasoning component inside that wider system, not as the system itself. The opposite risk matters just as much: explicit architecture is not automatically valuable, and every mechanism should earn its complexity through evidence.

## Working purpose

The current working purpose is:

> **Create the best data-science process for the particular project, where what "best" means is configurable according to the project's goals, constraints, required outputs, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective.

## Current development stage

**Prototype V0 is complete. The project is now in bounded V1 implementation and product validation.**

V0 was the first preregistered falsification experiment. It compared:

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

The methodological-navigation brain uses the staged relevance model:

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

Accepted V1 decisions currently include:

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

The richer governed knowledge import/accept/export round-trip is implemented but is **not yet closed**: SQLite passes, while the last persisted PostgreSQL 18 round-trip status remains failed after an identifier-length portability defect. The defect was fixed and revalidation was triggered, but a corrected PostgreSQL PASS has not yet been persisted.

### Agent/runtime boundary

Agent frameworks and interoperability protocols are treated as replaceable infrastructure, not ADS domain authority.

No agent runtime, LLM provider, or multi-agent architecture is accepted yet. Specification 005 defines an empirical bakeoff among current runtime candidates, beginning with one principal reasoner and allowing a simple direct-model-call result if no framework earns its complexity.

### Professional frontend and Project Cockpit

The frontend is a first-class reasoning, control, and quality surface rather than an end-stage presentation layer.

A conventional project-view shell exists for Overview, Data, EDA, Decisions & History, methodological guidance, run state, approvals, themes, accessibility, and visual regression.

Human review established the stronger **Project Cockpit** direction:

```text
Project Cockpit
    primary immersive active-work environment
    living project-process map
    native system interaction
    smooth focus into real analytical workspaces

Direct specialist views
    alternative inspection and entry paths
    reuse the same substantive analytical modules
```

The Cockpit has progressed through several real-browser and executable gates:

```text
Checkpoint 117
    unified deep-work interaction confirmed

Checkpoint 118
    first executable Cockpit gate passed

Checkpoint 119
    stage-zone visual grammar accepted
    2D scale / chrome / fullscreen requirements identified

Checkpoint 121
    immersive-scale 2D/fullscreen automated gate passed

Checkpoint 122
    third human review refined zoom, navigation and canvas dominance
    revised automated gate passed
```

The current Specification 007 candidate v0.3 Cockpit demonstrates:

```text
large two-dimensional project space
horizontal + vertical trackpad/scroll navigation
Arrow / Shift+Arrow / Home keyboard recovery

geometric zoom
    explicit zoom out / percentage / zoom in
    100% reset
    fit project
    keyboard zoom equivalents
    trackpad pinch zoom around the gesture anchor

scalable project navigation
    Jump to quick semantic destinations
        Active work
        Blocker
        Investigation
        Evaluation
    searchable meaningful project work

canvas-dominant composition
    one compact fold-away top HUD
    stage strip attached to project space
    floating project controls
    floating project details
    floating System Focus
    system composer floating over continuous project canvas
    lower/right recovery margin so overlays do not trap work

shared Data / EDA / Production Missingness focus workspaces
URL-addressable focus state
browser Back restoration
reduced-motion handling
true browser fullscreen with graceful fallback
```

Current governing sources:

```text
docs/research/002_primary_project_cockpit_interface_concept.md
docs/research/003_unified_cockpit_workspace_and_spatial_focus_architecture.md
docs/research/004_cockpit_spatial_scalability_immersive_chrome_and_fullscreen.md
docs/research/005_cockpit_canvas_dominance_zoom_and_scalable_project_navigation.md
docs/specifications/007_v1_unified_project_cockpit_interaction_spike.md
docs/checkpoints/122_third_cockpit_review_zoom_canvas_dominance_and_scalable_navigation_gate_passed.md
```

The current revised automated gate passes on Linux, Windows, Chromium interaction/accessibility, and controlled direct-project visual regression.

No graph/canvas library, auto-layout algorithm, final semantic-zoom implementation, minimap, final geometric zoom range, project-search backend, final stage taxonomy, final Cockpit visual identity, or canonical Cockpit screenshot baseline has been selected.

The immediate frontend step is another real-browser human product gate on the current v0.3 implementation.

## Active branch and continuation

The current frontend/Cockpit work is being developed on:

```text
v1-frontend-spike
```

The default `main` branch intentionally trails this active feature branch. New sessions working on the current Cockpit state must reconstruct from `v1-frontend-spike` rather than assuming `main` contains the latest frontend checkpoints.

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
