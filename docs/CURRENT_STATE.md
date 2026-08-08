# Current State

## Checkpoint

**Checkpoint:** 1  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Working project definition

The Autonomous Data Science System is intended to become a rigorous, adaptive, semi-autonomous system for carrying out data science projects with the help of multiple reasoning roles, executable tools, persistent knowledge, explicit review processes, empirical evidence, and human judgment.

The system should eventually be able to begin with a new data project, understand the problem, inspect and characterize the data, determine which questions and risks are relevant, plan investigations, execute code, evaluate evidence, compare alternatives, revisit earlier assumptions when necessary, involve the human at appropriate decision points, preserve project state, and produce reproducible analytical and reporting artifacts.

The primary purpose is now defined more precisely:

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

This means maximum automation, maximum predictive performance, maximum analytical depth, minimum cost, or maximum speed are not universal objectives. They are project-dependent priorities or means that should serve the broader project intent.

The next stage is to determine which methodological standards must remain invariant across project profiles and which aspects of the process can safely be configured.

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
13. The meaning of a good project is project-relative. The process should adapt to project goals, constraints, required outputs, and desired human involvement rather than optimize one universal objective.

## Accepted decisions added since Checkpoint 0

The primary-purpose question has been partially resolved.

The project now explicitly accepts that:

- the system should optimize the data-science process relative to project intent;
- maximum autonomy is not the universal goal;
- maximum predictive performance is not the universal goal;
- different projects can legitimately prioritize different combinations of rigor, learning value, interpretability, speed, cost, production readiness, reporting depth, and other dimensions.

See `DECISIONS.md`, especially D-017.

## Strong design hypotheses, not yet validated architecture

Several ideas appear promising but are **not yet final architectural decisions**:

- reusable decision or knowledge modules for topics such as missing data, leakage, class imbalance, validation, outliers, metric selection, calibration, and temporal structure;
- a trigger mechanism that activates relevant modules when project facts are discovered;
- a project reasoning graph in which observations create facts, facts trigger investigations, evidence produces decisions, and decisions can create new facts and investigations;
- specialized responsibilities such as problem understanding, data analysis, experiment planning, execution, statistical review, leakage review, model review, and decision synthesis;
- proposer-reviewer separation for consequential analytical choices;
- independent replication for selected high-risk findings;
- configurable analysis depth or resource budgets;
- explicit state records for decisions, rejected ideas, assumptions, experiments, evidence, confidence, and unresolved questions;
- a non-negotiable methodological quality floor that remains protected even when project priorities favor speed, low cost, or limited depth;
- a project-intent representation that distinguishes objectives, constraints, deliverables, and human-control preferences;
- treating named modes such as Quick, Standard, or Research as presets over a richer project-intent representation rather than as fundamental architecture;
- distinguishing project-level, model-level, and operational objectives;
- and allocating additional analytical effort where expected value, risk reduction, uncertainty reduction, and downstream impact justify it.

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
- exact evaluation framework for the system itself;
- exact contents of the non-negotiable methodological quality floor;
- exact project-intent schema;
- whether named project modes will exist;
- how project, model, and operational objectives will be represented;
- how analytical effort will be prioritized or scored.

## Current view of project intent

The project now has a stronger working concept of what information may be needed before an appropriate process can be planned.

A promising decomposition is:

1. **Objectives** - what the project should prioritize or maximize.
2. **Constraints** - limits the project must operate under.
3. **Deliverables** - outputs the project must produce.
4. **Human-control preferences** - how and when the system should involve the user.

This decomposition is not yet a finalized schema.

A second promising distinction is between:

- the **project-level objective**, which defines what makes the overall project valuable;
- the **model-level objective**, which defines the predictive or inferential task;
- the **operational objective**, which defines how outputs will be used in the real setting.

These distinctions may be important because improvements at one level do not automatically improve the others.

## Current view of configurable depth

Different projects should be allowed to consume different amounts of analytical effort.

A learning- or research-focused project may justify broad model comparison, theoretical explanation, ablations, robustness analysis, specialized review, and detailed reporting. A speed-focused project may justify a strong baseline, a few high-value alternatives, appropriate validation, and concise reporting.

The emerging principle is that selective depth should change the amount of work, not the validity of the work.

An additional hypothesis is that the system should allocate effort where additional analysis has the highest expected analytical value, rather than simply performing more experiments because resources remain available.

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

The highest-priority conceptual question is now:

> **What belongs in the non-negotiable methodological quality floor, and what should remain configurable according to project intent?**

This question follows directly from the accepted primary purpose. The system cannot safely optimize differently for different projects until it knows which standards may vary and which standards must remain protected.

Important subquestions include:

- Which methodological requirements must hold for every project?
- Which requirements depend on project type or intended deployment?
- Which aspects of depth, review, explanation, experimentation, and reporting can legitimately vary?
- Can a quality floor be expressed as universal principles, conditional invariants, or both?
- How should conflicts between project constraints and methodological validity be handled?
- When should the system refuse, pause, or escalate because a minimum standard cannot be satisfied?

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

Relevant historical checkpoints are:

10. `docs/checkpoints/000_checkpoint_0.md`
11. `docs/checkpoints/001_primary_purpose_and_project_intent.md`

## Next step

Define the first rigorous version of the non-negotiable methodological quality floor and distinguish it from project-configurable objectives, constraints, deliverables, depth, and human-control preferences.
