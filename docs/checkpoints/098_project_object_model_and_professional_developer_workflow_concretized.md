# Checkpoint 098: Project Object Model and Professional Developer Workflow Concretized

**Date:** 2026-08-19  
**Status:** Historical checkpoint with promoted foundational conclusions

## Context

After Prototype V0 was closed and the post-V0 product vision was promoted into Foundation 017, the design discussion continued from the desired user experience rather than from a new backend architecture.

Two areas became materially clearer:

1. the kinds of conceptual objects that should exist inside an interactive data-science project;
2. how the future system should coexist with VS Code, local execution, Git, and GitHub rather than attempting to replace the professional developer workflow.

This reasoning is important enough that the stable content has been promoted into Foundation 018 rather than remaining only in conversation history.

## Main product-model insight

The system should distinguish:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

User-facing sections such as EDA, Validation, Features, and Models should normally be treated as **views over shared project objects**, not as independent backend silos or a rigid pipeline.

A candidate product-level object family was developed:

```text
Project
IntentItem
    Objective
    Constraint
    Deliverable
    HumanPreference
    Definition

Artifact
Dataset
Variable

Question
Assumption
Finding
Claim

Method

Proposal
Investigation
Run
Evidence
Decision

Report
ReportSection

Event
Relation
```

Important distinctions include:

```text
Investigation != Run
Finding != Evidence
Finding != Claim
Claim != Decision
current state != event history
persisted project object != derived UI recommendation
```

The model is intentionally a product concept rather than a frozen storage ontology.

## Professional developer-workflow insight

The intended system should not attempt to replace VS Code.

A strong current conceptual split is:

```text
Autonomous Data Science System
    project/process control plane

VS Code
    developer workbench

Python / Docker / local or remote compute
    execution plane

Git + GitHub
    source versioning, collaboration, and code provenance
```

The system and VS Code should operate on the same project rather than maintaining unrelated project copies.

Generated code should remain normal, professional, independently runnable project code.

A UI-triggered execution and a user-triggered VS Code execution should ideally share the same reproducible command/configuration contract so that the system does not hide analytical logic behind proprietary execution paths.

GitHub should be deeply integrated, but Git is not intended to store every large dataset, model, or intermediate artifact. The system should track artifact provenance separately from source-code versioning.

## Local-first versus remote execution

Local-first execution is currently a strong product hypothesis for the user's typical workflow because it naturally supports:

```text
same working tree
immediate VS Code visibility
local Python / Docker execution
Git versioning
GitHub synchronization
```

However, it has **not** been promoted into a universal architecture commitment. The eventual execution abstraction should remain compatible with local GPU, remote GPU, cloud, cluster, or organizational infrastructure.

## Execution maturity levels

Not every exploratory action should become permanent source code.

A useful conceptual distinction emerged:

```text
EPHEMERAL ANALYSIS
REPRODUCIBLE INVESTIGATION
PROJECT / FINAL CODE
```

Consequential exploration can be promoted into reproducible code and experiment provenance without creating permanent scripts for every tiny interactive action.

Notebooks and modules can coexist according to purpose.

## Additional architectural separations

The discussion reinforced several important boundaries:

```text
system memory != LLM context
project workspace != code editor
project orchestration != execution environment
Git/GitHub provenance != full artifact storage
workspace section != fundamental object
investigation purpose != concrete execution
```

These separations should reduce responsibility conflation in future prototypes.

## Promotion audit

### Promoted to foundation

The stable object-model and developer-workflow reasoning was promoted into:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

### Canonical principles

Two principles are suitable for promotion:

```text
The system should complement the professional developer workbench rather than replace it.
Generated project code should remain independently runnable and professionally maintainable.
```

### Current-state/routing updates

`CURRENT_STATE.md` and `KNOWLEDGE_MAP.md` should route future sessions to Foundation 018 and make the methodological-navigation brain the next design topic.

### Not promoted as settled architecture

The following remain open:

```text
exact object schema
statuses and relations
storage technology
frontend/backend stack
local-first as universal architecture
one versus multiple LLM roles
GitHub write policy
remote-compute design
```

## Next step

Continue product/system reasoning rather than implementation.

The next major question is:

> How should the methodological-navigation brain represent broad reusable data-science knowledge and decide what is known, applicable, relevant, recommended, required, or inapplicable for the current project?

That question should be developed before selecting a V1 storage, retrieval, orchestration, or execution architecture.