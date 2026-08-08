# Checkpoint 5: Project Initialization and Universal Bootstrap

**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Purpose of this checkpoint

Checkpoint 4 established a strong hypothesis that the Autonomous Data Science System should maintain typed, dependency-aware project state and derive next actions from that state rather than from one fixed pipeline.

Checkpoint 5 addresses the prior problem: how does a completely new project become a usable project state when the initial user request, data, documentation, code, constraints, and intended use may be incomplete, contradictory, outdated, or wrong?

The current answer is a combination of:

1. **progressive state construction**; and
2. a small **universal bootstrap inspection** that creates initial structural facts, conflicts, questions, and triggers.

Detailed reasoning is preserved in:

`docs/foundations/005_project_initialization_and_universal_bootstrap.md`

---

## Main conceptual result

The strongest current formulation is:

> **A new project should enter the system through progressive state construction rather than one-shot problem definition. Initial requests, documentation, code, data, and external information should be registered with provenance, converted into provisional facts, assumptions, questions, constraints, and candidate interpretations, and continuously reconciled as evidence accumulates.**

A second strong formulation is:

> **The system should begin useful work as soon as a legitimate runnable frontier exists, while preventing actions whose semantic, epistemic, admissibility, or assurance prerequisites remain unresolved.**

These remain design hypotheses rather than finalized requirements.

---

## Initial project input is not automatically truth

The user's request and project documentation should be preserved as source material rather than silently converted into established facts.

The system should distinguish:

```text
ORIGINAL PROJECT INPUT
what a source actually stated

CURRENT PROJECT INTERPRETATION
what the system currently believes the project means
```

If direct inspection conflicts with a reported statement, the disagreement should become explicit project state rather than being silently resolved.

Example:

```text
Reported:
One row represents one customer.

Observed:
Customer IDs repeat.

Result:
Create a material conflict and activate a question about observation unit.
```

---

## Source and authority awareness

A new project may include user requests, data dictionaries, schemas, datasets, notebooks, code, deployment configuration, saved models, reports, and other documentation.

The system should register what sources exist before relying on them.

A strong current hypothesis is:

> **Authority is question-specific.**

For example, the user may be authoritative about intended business objectives while a production schema or system owner may be more authoritative about operational feature availability.

No universal source-precedence model has been selected.

---

## Progressive semantic commitment

The system should not require complete project understanding before every action.

Different actions require different semantic prerequisites.

Basic structural data inspection may be legitimate while operational threshold selection remains blocked by unresolved business trade-offs.

This creates an action-relative interpretation of project understanding:

```text
known enough for structural inspection
not yet known enough for leakage-sensitive feature approval
not yet known enough for operational threshold choice
```

The project should therefore continue refining semantics throughout its lifetime rather than completing all "problem understanding" once at the beginning.

---

## Universal bootstrap inspection

The bootstrap should remain small, cheap, conservative, structural, and trigger-oriented.

Its purpose is not to complete EDA or choose modelling strategy.

It should generate enough trustworthy initial state for specialized reasoning to activate.

Useful criteria for a universal bootstrap action include:

```text
broad relevance
low semantic commitment
low risk
high trigger value
low relative cost
non-destructive behavior
provenance preservation
reversibility
```

A concise behavioral rule is:

> **Observe broadly, infer cautiously.**

---

## Information boundaries apply during bootstrap

The bootstrap must obey information legitimacy.

Before deeply inspecting a source, the system should determine what role it plays and what information is legitimate to consume.

This is especially important for final holdout or test data.

The bootstrap may need structural compatibility information while still protecting restricted outcome information from development.

A future execution architecture may need enforceable information barriers, but no implementation has been selected.

---

## Candidate structural bootstrap observations

High-value early observations may include:

- available project sources and files;
- dataset shapes and schemas;
- physical data types;
- candidate identifiers and their cardinality;
- timestamps or ordering variables;
- target candidate structure where legitimate;
- missingness presence and approximate rates;
- duplicate or repeated-entity structure;
- dataset partitions;
- entity or time overlap across partitions;
- obvious structural inconsistencies;
- existing code/environment structure;
- executability and resource availability;
- obvious governance-relevant facts or constraints.

These observations are intended to create triggers, not to settle all downstream analytical decisions.

---

## Bootstrap detects conditions; specialized modules reason about responses

Examples:

```text
BOOTSTRAP OBSERVATION:
42% missingness in Feature X

TRIGGER:
missing-data reasoning

NOT:
automatically median-impute
```

```text
BOOTSTRAP OBSERVATION:
timestamp column exists

TRIGGER:
temporal-structure reasoning

NOT:
automatically fit a time-series model
```

```text
BOOTSTRAP OBSERVATION:
positive target class is 2%

TRIGGER:
imbalance / metrics / threshold reasoning

NOT:
automatically apply SMOTE
```

This distinction is central to avoiding a brittle hard-coded workflow.

---

## Existing implementation is historical evidence, not accepted methodology

Inherited code should be inspected as evidence about what the current implementation does.

It should not automatically define what methodology the system should preserve.

For example, code that scales all data before splitting establishes a historical implementation fact and may activate a leakage review.

This creates a useful distinction between:

```text
CURRENT IMPLEMENTATION STATE
```

and

```text
CURRENT ACCEPTED METHODOLOGICAL STATE
```

---

## Project characterization should be multidimensional

The system should avoid one exclusive label such as `classification`, `forecasting`, or `clustering` as the entire project type.

A real project may simultaneously be:

```text
supervised
binary classification
temporal
grouped
forward-looking
sequence-derived
imbalanced
```

Project characterization should therefore likely consist of multiple structural properties that activate different reasoning modules.

The exact representation remains open.

---

## Intended use is a high-leverage state object

Intended use affects validation, feature legitimacy, metrics, calibration, interpretation, risk, admissibility, monitoring, and human-control requirements.

The system should try to establish intended use early but keep it revisable.

A later change from exploratory analysis to production automation should trigger impact analysis and new assurance obligations rather than merely changing one metadata field.

---

## Human interaction during initialization

The system should not begin every project by asking a large questionnaire.

It should first exploit available sources and empirical inspection when they can resolve questions cheaply and reliably.

Human clarification becomes high-value when the issue is semantic, normative, authority-dependent, materially blocking, or otherwise not reliably resolvable from available evidence.

A useful human-facing representation may be a derived **Current Project Interpretation** summarizing the system's present understanding and important uncertainties so that the user can correct high-leverage misunderstandings efficiently.

---

## Initialization stopping condition

Initialization should be considered sufficiently advanced once:

> **At least one useful, admissible, methodologically legitimate action is available, while important unresolved questions and blockers are explicitly represented.**

The system does not need all future project questions answered before work begins.

Blocking is relative to actions and milestones rather than one project-wide yes/no status.

---

## Six bootstrap responsibilities

The current universal bootstrap hypothesis can be compressed into six responsibilities:

1. **Register sources and information boundaries.**
2. **Establish structural facts.**
3. **Compare sources for consistency.**
4. **Generate project-characterization hypotheses.**
5. **Emit triggers and questions.**
6. **Construct the first runnable frontier.**

This is conceptual rather than an implementation workflow.

---

## Major simplification discovered

A significant design simplification is now visible.

The system may not require one universal data-science workflow.

Instead it may require:

```text
A SMALL UNIVERSAL BOOTSTRAP PROTOCOL
                +
ADAPTIVE STATE-DRIVEN REASONING
```

Conceptually:

```text
NEW PROJECT
    -> source registration
    -> provisional interpretation
    -> information-boundary determination
    -> universal bootstrap inspection
    -> structural facts and conflicts
    -> project-characterization hypotheses
    -> triggers
    -> specialized questions / knowledge modules
    -> first runnable frontier
```

Then the Checkpoint 4 control loop takes over:

```text
action
    -> evidence
    -> state update
    -> impact analysis
    -> new obligations
    -> new runnable frontier
```

This offers a more manageable route to broad project coverage than trying to enumerate one complete end-to-end workflow for every data-science project in advance.

---

## Strong hypotheses added or strengthened

Checkpoint 5 strengthens these ideas:

- new project state should be provisional and source-aware;
- original statements and current interpretations should remain distinct;
- source authority is question-specific;
- material contradictions should create explicit conflicts and questions;
- semantic commitment should be progressive and action-relative;
- bootstrap inspection itself must obey information legitimacy;
- universal bootstrap should be structural and trigger-oriented rather than exhaustive;
- bootstrap detects conditions while specialized knowledge decides responses;
- project characterization should be multidimensional;
- intended use should be established early and remain revisable;
- user interruption should be selective and value-sensitive;
- initialization is sufficiently complete when a legitimate runnable frontier exists;
- a small universal bootstrap protocol may be the main fixed entry process before adaptive reasoning takes over.

These are not yet accepted implementation decisions.

---

## Explicit non-decisions

Checkpoint 5 does not select:

- the exact bootstrap checklist;
- source or authority schemas;
- confidence scoring;
- project-characterization representation;
- exact information-barrier mechanism;
- how bootstrap operations are divided between deterministic tools and LLM reasoning;
- knowledge-module storage;
- trigger representation;
- rule engine;
- graph technology;
- workflow engine;
- orchestration framework;
- agent roles or count.

---

## Next continuation point

The next major conceptual question is:

> **How should project facts, conflicts, open questions, and characterization properties activate the correct reusable knowledge modules, rules, reviewers, or open-ended reasoning without creating one centralized decision tree that must enumerate every possible project path?**

This is the **knowledge-activation problem**.

The next discussion should examine trigger semantics, module activation conditions, state subscriptions, deterministic versus LLM-proposed activation, module interactions, false-negative activation, over-activation, and how activation creates questions or candidate actions on the runnable frontier.
