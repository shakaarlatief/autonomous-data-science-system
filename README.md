# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project explores how to build a rigorous, adaptive, semi-autonomous system for carrying out data science projects from initial problem understanding through analysis, experimentation, modelling, evaluation, reporting, and final delivery.

The central motivation is that a single large language model can often complete an entire data project, but a one-dimensional workflow is fragile. Important decisions can be made too quickly, assumptions can remain implicit, project-specific considerations can be missed, alternatives may not be explored, and apparently reasonable choices may not be adequately challenged or tested.

The long-term goal is therefore not merely to create an "AI data scientist." The goal is to design an AI-managed scientific process for data projects that can combine:

- large language model reasoning;
- executable code and empirical experiments;
- reusable data science knowledge;
- explicit decision frameworks;
- independent review and criticism;
- persistent project state;
- reproducibility and provenance;
- uncertainty tracking;
- configurable depth and efficiency;
- and human judgment where it materially improves the outcome.

## Current stage

The project is currently in the **conceptual research and system-definition stage**.

No final software architecture, agent framework, orchestration technology, knowledge representation, or implementation stack has been selected.

This is deliberate. The project is first defining what the system should accomplish, how it should reason, how it should adapt across different kinds of data projects, how knowledge should be represented and preserved, how humans should be involved, and how the system itself should be developed and evaluated.

## Repository role

This repository is the project's long-term source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable conclusions, current state, decisions, open questions, and important long-form reasoning are extracted into this repository so that the project does not depend on conversational memory or any single chat remaining available.

The repository intentionally preserves both:

1. concise canonical knowledge that can be read quickly; and
2. detailed foundational reasoning that explains why important ideas were introduced.

Historical material is useful for provenance, but current canonical documents take precedence when earlier discussions conflict with later accepted decisions.

## Initial documentation

- `docs/CURRENT_STATE.md` - concise snapshot of where the project currently stands and what should happen next.
- `docs/VISION.md` - working definition of the system we are trying to create and the problem it is intended to solve.
- `docs/PRINCIPLES.md` - current high-level principles that guide the design.
- `docs/DECISIONS.md` - explicit decisions already made, including their rationale and status.
- `docs/OPEN_QUESTIONS.md` - important unresolved questions that must not be silently treated as settled.
- `docs/DEVELOPMENT_METHOD.md` - how the system itself will be designed, tested, documented, and evolved.
- `docs/CONTINUITY.md` - procedure for ending one chat or design session and resuming correctly in another.
- `docs/foundations/001_initial_vision_and_reasoning.md` - detailed reconstruction of the foundational reasoning from the first design discussion.
- `docs/checkpoints/000_checkpoint_0.md` - historical snapshot of the project at the first formal checkpoint.

## Relationship to individual data projects

This repository is intentionally separate from repositories or folders containing individual data science projects.

Individual projects such as tabular classification, regression, forecasting, sequence modelling, recommender systems, and other future cases can later serve as **coverage tests and development environments** for the Autonomous Data Science System.

The relationship is therefore:

```text
Autonomous Data Science System
        |
        | designs, guides, reviews, and learns from
        v
Individual Data Projects
```

Lessons discovered in one project should not remain isolated patches when they are generalizable. They should be extracted into reusable system knowledge, decision frameworks, tests, or capabilities where appropriate.

## Immediate next step

The next major task is to define the system more precisely before selecting implementation architecture.

The project must clarify:

- what the system is ultimately expected to accomplish;
- what degree of autonomy is desirable;
- what role the human should play;
- what "high quality" means across different project types;
- which properties are mandatory for success;
- how the system should be evaluated against a strong single-LLM workflow;
- and how quality, efficiency, learning value, reproducibility, and general applicability should be balanced.

See `docs/CURRENT_STATE.md` for the current working state and the exact continuation point.

## Status of this structure

The current repository and documentation structure is **version 0.1 of the project-development methodology**.

It exists to prevent knowledge loss and support disciplined iteration. It should not be treated as the final documentation architecture. Problems discovered while using it should lead to revisions of the methodology itself.
