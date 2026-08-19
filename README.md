# Autonomous Data Science System

## Overview

This repository is the persistent home of the Autonomous Data Science System project.

The project explores how to build a rigorous, adaptive, semi-autonomous system for carrying out data-science projects from problem understanding through analysis, experimentation, modelling, evaluation, reporting, and delivery.

Modern LLMs can already perform substantial portions of a data project. That does not imply that one long end-to-end conversation reliably produces the best possible process for every project.

The project therefore studies a higher-level question:

> How much of the process navigation, methodological memory, state maintenance, evidence discipline, repair, and selective human involvement that currently lives in a skilled human-LLM workflow should be made explicit and reusable in a wider system?

The LLM is treated as a powerful reasoning component inside that wider system, not as the system itself.

The opposite risk matters just as much: explicit architecture is not automatically valuable. Every mechanism should earn its complexity through evidence.

## Working purpose

The current working purpose is:

> **Create the best data-science process for the particular project, where what "best" means is configurable according to the project's goals, constraints, required outputs, and desired human involvement, while maintaining non-negotiable methodological integrity.**

The project therefore does not define maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed as the universal objective.

## Current stage

**Prototype V0 is complete.**

V0 was the first preregistered falsification experiment. It compared:

```text
B0 = strong LLM + Python + project artifacts + strong generic data-science instructions

B1 = B0 + four methodological concepts supplied statically

P0 = same strong LLM + typed project state + structured knowledge activation
     + prospective safeguards + state-derived action selection
     + dependency-aware repair
```

The experiment asked whether the extra P0 architecture materially improves reliability beyond B1 at acceptable cost.

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

P0 improved the targeted semantic score over B1 by only `+0.05`. The preregistered material-reliability threshold required `+0.30` together with at least two additional strong-targeted passes, or at least two fewer critical failures.

P0 and B1 had identical critical-failure and strong-pass counts, while P0 used `2.160x` B1's median tokens and completed only `3/10` runs within budget.

Most of the semantic gain over the generic baseline came from the simpler B1 intervention: make the relevant methodological knowledge explicitly available to the strong LLM.

Detailed result:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

Quick V0 overview:

```text
prototype_v0/README.md
```

The next stage is not to tune P0 until it passes the completed benchmark. The project is now reconciling what V0 taught and designing the smallest lower-overhead successor architecture that can be tested against B1 on a harder problem.

## What V0 changed

The V0 result does **not** falsify the broader Autonomous Data Science System vision.

It does falsify the assumption that more explicit state and orchestration machinery should be preserved merely because it looks systematic.

The current evidence favors keeping:

```text
one strong LLM reasoner
compact explicit methodological guidance
instrumented execution and traceability
precise deterministic boundaries where justified
append-only experiment provenance
external mechanical verification
read-only observability separated from execution
```

The current P0 mechanisms should not be carried forward unchanged:

```text
full typed project state resent every reasoning cycle
large always-on object/relation context
generic support-reassessment propagation
path-sensitive tag-trigger knowledge activation
universal dependency reopening machinery
full state-derived frontier representation
```

Potential successors such as compact question/claim memory, incremental state deltas, selective retrieval, event-driven repair, and lightweight blocker/frontier representations remain hypotheses for the next design stage.

## System-level vision versus Prototype V0

Prototype V0 tested a narrow local architecture. It does not define the final system.

The broader system-level distinction remains:

```text
1. human-executed data-science project
2. human + interactive LLM project
3. system-mediated data-science project
```

The long-term question is whether a system can make high-quality project navigation, methodological coverage, state maintenance, repair, and knowledge reuse less dependent on the human remembering and supplying the right reasoning at the right time.

The best current synthesis is:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

## Repository role

This repository is the project's durable source of truth.

Chat conversations are used for exploration, reasoning, criticism, and design work. Stable knowledge is extracted into repository artifacts so the project does not depend on conversational memory or any single chat remaining available.

The preservation architecture distinguishes:

```text
canonical current documents
foundational design memos
checkpoints and historical provenance
experiment-specific ledgers
routing/index knowledge
Git history
```

The core maxim remains:

> **The chat is where we think. The repository is where the system remembers.**

Preservation includes not only durability, but also discoverability, promotion, authority, and reconciliation.

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
    Important unresolved questions.

docs/DEVELOPMENT_METHOD.md
    Method for developing and preserving the project.

docs/CONTINUITY.md
    Procedure for reliable continuation across chats and models.

docs/MAJOR_CHANGES.md
    Selective history of major architectural and methodological changes.

docs/foundations/
    Detailed durable reasoning and specifications.

docs/checkpoints/
    Historical snapshots and milestone records.
```

For the completed V0 experiment specifically:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
prototype_v0/README.md
docs/foundations/012_preregistered_held_out_evaluation_protocol.md
```

## Knowledge preservation architecture

Development Method v0.3 uses the lifecycle:

```text
discussion
    -> checkpoint
    -> promotion audit
    -> canonical/foundational/specification update when warranted
    -> knowledge-map routing update when warranted
    -> periodic knowledge reconciliation
```

Detailed rationale:

```text
docs/foundations/014_knowledge_preservation_architecture_and_evolution.md
```

The current preservation substrate remains Git + Markdown. More advanced infrastructure is deferred until observed retrieval, dependency, consistency, concurrency, or automation problems justify it.

## Execution and observability

A system-level lesson discovered while running V0 is that execution and human-facing observability should be separated:

```text
execution / reasoning
    -> persisted structured state or events
    -> read-only observability
    -> human interface
```

This allows monitors, dashboards, timestamps, heartbeats, and progress displays to evolve without modifying the trusted execution path.

Deep rationale:

```text
docs/foundations/016_execution_observability_separation.md
```

## Relationship to individual data projects

This repository is intentionally separate from repositories containing individual data-science projects.

Individual projects can serve as coverage tests and development environments for the system.

```text
Autonomous Data Science System
        |
        | designs, guides, reviews, and learns from
        v
Individual Data Projects
```

When a project reveals a generalizable weakness, the lesson should become reusable system knowledge, a decision framework, a behavioral regression test, or an architectural revision rather than remaining a local patch.

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

> **Build only the system mechanisms that demonstrably improve the reliability, coverage, efficiency, reuse, or human-navigation burden of real data-science work beyond what strong simpler workflows already achieve.**

Prototype V0 is the first concrete example of that philosophy: a more elaborate treatment was allowed to lose, and the result is now an architectural constraint for what comes next.
