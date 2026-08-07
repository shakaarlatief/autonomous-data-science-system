# Current State

## Checkpoint

**Checkpoint:** 0  
**Date:** 2026-08-07  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Working project definition

The Autonomous Data Science System is intended to become a rigorous, adaptive, semi-autonomous system for carrying out data science projects with the help of multiple reasoning roles, executable tools, persistent knowledge, explicit review processes, empirical evidence, and human judgment.

The system should eventually be able to begin with a new data project, understand the problem, inspect and characterize the data, determine which questions and risks are relevant, plan investigations, execute code, evaluate evidence, compare alternatives, revisit earlier assumptions when necessary, involve the human at appropriate decision points, preserve project state, and produce reproducible analytical and reporting artifacts.

This working definition is intentionally broad. The next stage of the project is to make it precise enough that architecture and implementation decisions can be evaluated against explicit requirements.

## Core problem being addressed

A capable LLM can often perform an entire data science project from end to end. However, a single conversational workflow has important weaknesses:

- decisions may be made prematurely;
- assumptions may remain implicit;
- important project-specific questions may be missed;
- reasonable alternatives may not be explored;
- preprocessing or validation choices may be technically valid but poorly matched to the actual deployment setting;
- interpretations may be accepted without independent criticism;
- LLM agreement can be mistaken for evidence;
- the workflow can become too linear even when later discoveries should cause earlier stages to be revisited;
- knowledge from one project may not be systematically generalized into future projects;
- and the reasoning behind earlier decisions can be lost as conversations become long.

The system is intended to improve the **process**, not merely replace one LLM with several LLMs.

## Established working principles

The following ideas currently have strong support and are treated as working principles. Detailed formulations are maintained in `PRINCIPLES.md`.

1. The repository, not conversational memory, is the persistent source of truth.
2. Important reasoning should be preserved at multiple levels of detail.
3. Empirical evidence should dominate unsupported LLM judgment when a question can be tested.
4. Data science should be represented as an adaptive, revisitable process rather than a globally fixed linear pipeline.
5. The system should combine hard constraints, explicit decision frameworks, and open-ended reasoning.
6. Investigations should activate dynamically according to project facts rather than running every possible check.
7. Important decisions should expose assumptions, evidence, uncertainty, and alternatives.
8. Human involvement should be concentrated where human judgment materially improves the project.
9. Review, criticism, and where useful independent replication should be possible for important conclusions.
10. Real data projects should be used as coverage tests for the evolving system.
11. Generalizable lessons from project failures or omissions should become reusable system knowledge rather than project-specific patches.
12. Both the target system and the methodology used to build it should remain evolvable.

## Strong design hypotheses, not yet validated architecture

Several ideas appear promising but are **not yet final architectural decisions**:

- reusable decision or knowledge modules for topics such as missing data, leakage, class imbalance, validation, outliers, metric selection, calibration, and temporal structure;
- a trigger mechanism that activates relevant modules when project facts are discovered;
- a project reasoning graph in which observations create facts, facts trigger investigations, evidence produces decisions, and decisions can create new facts and investigations;
- specialized responsibilities such as problem understanding, data analysis, experiment planning, execution, statistical review, leakage review, model review, and decision synthesis;
- proposer-reviewer separation for consequential analytical choices;
- independent replication for selected high-risk findings;
- configurable analysis depth or resource budgets;
- and explicit state records for decisions, rejected ideas, assumptions, experiments, evidence, confidence, and unresolved questions.

These are design hypotheses to be tested and refined. The project must not silently treat them as implementation commitments.

## Explicit non-decisions

The following have **not** been decided:

- number of agents;
- whether agents are permanent, dynamic, or both;
- which LLM providers or models will be used;
- whether multiple model providers are necessary;
- orchestration framework;
- agent framework;
- workflow engine;
- database technology;
- knowledge graph technology;
- rule engine technology;
- whether decision modules are stored as Markdown, YAML, code, database records, graph nodes, or another representation;
- experiment tracking platform;
- execution sandbox architecture;
- deployment environment;
- UI architecture;
- final repository structure;
- final taxonomy of data science project types;
- exact level of autonomy;
- exact human approval gates;
- exact evaluation framework for the system itself.

## Current knowledge-preservation approach

The project currently uses several layers:

1. **Canonical documents** for concise, current, intentionally maintained knowledge.
2. **Foundational design memos** for detailed reasoning, examples, motivations, distinctions, and arguments that should not be compressed away.
3. **Checkpoints and later session records** for historical snapshots of what was known or believed at a particular time.
4. **Raw conversational material**, if archived later, as provenance rather than authoritative specification.

The current documentation methodology is provisional and should be revised when real use exposes weaknesses.

## Current external/source material

The ChatGPT project currently contains machine learning and time-series/econometrics material that may help when developing data science knowledge modules and testing reasoning coverage. It also contains an existing `Missing_Data.md` decision tree that has already served as a useful miniature example of explicit conditional data science reasoning.

These materials have **not** yet been copied into this repository. The permanent source architecture has not been decided.

## Relationship to existing data projects

Individual data projects remain separate from this repository. They are expected to become important test environments for the system.

Examples already discussed include:

- tabular binary classification such as customer churn;
- forecasting and time-series problems;
- and future deliberately selected projects that expose different analytical structures and failure modes.

The system should eventually be tested across heterogeneous cases rather than optimized only for one project type.

## Current focus

The next conceptual task is to answer:

> **What exactly are we trying to create, and what properties must it have for us to consider it successful?**

This question should be answered before selecting a software architecture.

Important subquestions include:

- What degree of autonomy is desirable?
- Which decisions should the system make itself?
- Which decisions should involve the human?
- Should project depth be configurable?
- Is the primary objective maximum analytical quality, learning value, professional output quality, speed, cost, generality, or a configurable combination?
- What should this system do better than giving a strong LLM access to a repository and asking it to complete the project?
- How should success be measured across different project types?

## Required context for a new chat

A new design chat should read, at minimum:

1. `README.md`
2. `docs/CURRENT_STATE.md`
3. `docs/VISION.md`
4. `docs/PRINCIPLES.md`
5. `docs/DECISIONS.md`
6. `docs/OPEN_QUESTIONS.md`
7. `docs/DEVELOPMENT_METHOD.md`
8. `docs/CONTINUITY.md`

For the reasoning behind the initial concepts, also read:

9. `docs/foundations/001_initial_vision_and_reasoning.md`

The historical first snapshot is:

10. `docs/checkpoints/000_checkpoint_0.md`

## Next step

Develop a rigorous first version of the system's goals, success criteria, requirements, and boundaries before discussing implementation architecture.
