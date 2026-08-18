# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project explores how to build a rigorous, adaptive, semi-autonomous system for carrying out data-science projects from problem understanding through analysis, experimentation, modelling, evaluation, reporting, and delivery.

Modern LLMs can already perform substantial portions of a data project. That capability does not imply that one long end-to-end conversation reliably produces the best possible process for every project.

The project therefore studies a higher-level question:

> How much of the process navigation, methodological memory, state maintenance, evidence discipline, repair, and selective human involvement that currently lives in a skilled human-LLM workflow should be made explicit and reusable in a wider system?

The LLM is treated as a powerful reasoning component inside that wider system, not as the system itself.

The project also takes the opposite risk seriously: explicit architecture is not automatically valuable. Every mechanism should earn its complexity through evidence.

## Working purpose

The current working purpose is:

> **Create the best data-science process for the particular project, where what "best" means is configurable according to the project's goals, constraints, required outputs, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective.

## Current stage

The project is currently running **Prototype V0**, the first falsification-oriented implementation experiment.

Prototype V0 asks whether a small explicit semantic architecture around the same strong LLM provides meaningful value beyond strong simpler workflows.

The three conditions are:

```text
B0 = strong LLM + Python + project artifacts + strong generic data-science instructions

B1 = B0 + the same four methodological concepts supplied statically in the prompt

P0 = same strong LLM + minimal typed state + structured knowledge activation
     + a prospective safeguard + state-derived action selection
     + dependency-aware repair
```

B1 is the primary architectural control. If B1 matches P0 reliably with less cost or friction, the tested P0 machinery is not justified for this benchmark.

The held-out experiment is preregistered and currently executing. The treatment architecture, prompts, benchmark bundles, budgets, semantic rubric, provider/model configuration, and run order are frozen during execution.

For a short explanation of V0, start with:

```text
prototype_v0/README.md
```

For exact current execution status, use:

```text
docs/CURRENT_STATE.md
docs/experiments/prototype_v0/HELD_OUT_STATUS.md
```

## System-level vision versus Prototype V0

Prototype V0 tests a narrow local question. It does not define the final system architecture.

The broader system-level distinction is:

```text
1. human-executed data-science project
2. human + interactive LLM project
3. system-mediated data-science project
```

The long-term question is whether a system can make high-quality project navigation, methodological coverage, state maintenance, repair, and knowledge reuse less dependent on the user remembering and supplying the right reasoning at the right time.

The best current synthesis is:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The preservation architecture deliberately distinguishes:

```text
canonical current documents
foundational design memos
checkpoints / historical provenance
experiment-specific status ledgers
routing/index knowledge
Git history
```

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

But preservation now includes not only durability, but also discoverability, promotion, authority, and reconciliation.

## Start here

The main project-level documents are:

```text
docs/CURRENT_STATE.md
    Concise current state, exact current priority, and next step.

docs/KNOWLEDGE_MAP.md
    Routing layer showing where important knowledge lives.

docs/VISION.md
    Current system vision and purpose.

docs/PRINCIPLES.md
    Current high-level design principles.

docs/DECISIONS.md
    Accepted project-level decisions.

docs/OPEN_QUESTIONS.md
    Important unresolved questions.

docs/DEVELOPMENT_METHOD.md
    Current method for developing and preserving the project.

docs/CONTINUITY.md
    Procedure for reliable continuation across chats and models.

docs/MAJOR_CHANGES.md
    Selective history of major architectural and methodological changes.

docs/foundations/
    Detailed durable reasoning and specifications.

docs/checkpoints/
    Historical snapshots and milestone records.
```

If you are looking for a topic and do not know which document contains it, use:

```text
docs/KNOWLEDGE_MAP.md
```

## Knowledge preservation architecture

Development Method version 0.3 introduced a stronger preservation lifecycle after actual use exposed the risk that historically safe knowledge can still become conceptually buried.

The current flow is:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> knowledge-map routing update when warranted
    -> periodic knowledge reconciliation
```

Important changes include:

```text
explicit checkpoint promotion audits;
KNOWLEDGE_MAP as a routing layer;
periodic reconciliation of stale/duplicated knowledge;
lightweight document authority/maturity metadata;
separation of concise CURRENT_STATE from detailed experiment ledgers;
MAJOR_CHANGES as a selective structural history.
```

Detailed rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

The current storage foundation remains Git + Markdown. Graph databases, vector retrieval, automatic summarization, generated dependency graphs, and similar advanced preservation infrastructure are deliberately deferred until demonstrated scale, retrieval, consistency, dependency, or automation problems justify them.

## Prototype V0 repository area

The executable experiment lives under:

```text
prototype_v0/
```

Key locations:

```text
prototype_v0/README.md
    Current simple conceptual and operational V0 overview.

prototype_v0/src/ads_v0/
    Executable implementation.

prototype_v0/tests/
    Prototype tests.

prototype_v0/configs/
    Frozen experiment configuration.

docs/foundations/010_minimum_falsification_prototype_and_experimental_contract.md
    V0 conceptual and benchmark contract.

docs/foundations/011_prototype_v0_technical_specification.md
    V0 technical specification.

docs/foundations/012_preregistered_held_out_evaluation_protocol.md
    Frozen held-out experiment protocol.

docs/experiments/prototype_v0/HELD_OUT_STATUS.md
    Detailed current held-out execution ledger.
```

## Relationship to individual data projects

This repository is intentionally separate from repositories or folders containing individual data-science projects.

Individual projects can serve as coverage tests and development environments for the system.

The relationship is:

```text
Autonomous Data Science System
        |
        | designs, guides, reviews, and learns from
        v
Individual Data Projects
```

When a project reveals a generalizable weakness, the lesson should be extracted into reusable system knowledge, decision frameworks, behavioral regression tests, or architectural changes rather than patched only locally.

## Current development philosophy

The project intentionally resists two opposite mistakes:

```text
Mistake 1:
Assume that because a strong LLM can already do impressive data-science reasoning,
there is no value in system-level process machinery.

Mistake 2:
Assume that because the long-term vision is broader than one LLM conversation,
every piece of orchestration machinery is automatically justified.
```

The current stance is empirical:

> **Build only the system mechanisms that demonstrably improve the reliability, coverage, efficiency, reuse, or human-navigation burden of real data-science work beyond what strong simpler workflows already achieve.**

See `docs/CURRENT_STATE.md` for the exact current continuation point.
