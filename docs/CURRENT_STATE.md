# Current State

**Checkpoint:** 98  
**Date:** 2026-08-19  
**Development stage:** Prototype V0 complete; post-V0 product/system vision, candidate project object model, and professional developer-workflow integration now concretized before next architecture design  
**Final V0 classification:** STRONG FALSIFICATION OF THE CURRENT P0 DESIGN  
**Execution mode:** Prototype V0 is closed; no further B0/B1/P0 treatment or V0 semantic-judge inference is authorized

## Current project goal

The broader Autonomous Data Science System still aims to create the best defensible data-science process for a project's objectives, constraints, deliverables, and desired human involvement.

The intended destination is **not** a single prompt that returns a completed project.

The current product vision is a professional interactive data-science environment in which the system itself carries much of the methodological memory, project memory, option generation, process navigation, execution discipline, provenance, and reporting burden that otherwise has to be repeatedly supplied by the human through prompts.

The user should remain able to inspect, discuss, select, override, and guide the work interactively.

Core product vision:

```text
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
```

System/LLM/human boundary:

```text
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
```

## Prototype V0 constraint

Prototype V0 strongly falsified the **current P0 implementation strategy on the churn benchmark family**.

Primary result:

```text
B1 targeted mean: 1.73
P0 targeted mean: 1.78
incremental P0 gain: +0.05

B1 completed within budget: 10/10
P0 completed within budget: 3/10

P0/B1 median token ratio: 2.160
```

This does not falsify the broader system vision or persistent project memory.

One of the strongest V0 lessons is:

```text
what the SYSTEM should remember
    !=
what the LLM should receive on every reasoning call
```

Do not carry forward P0's large always-on state/context representation unchanged.

Final V0 evidence:

```text
docs/experiments/prototype_v0/FINAL_RESULTS.md
```

## Professional interactive workspace

A new project should eventually begin by providing available sources such as:

```text
assignment / project brief
datasets
README / documentation
existing notebooks or baseline code
business/domain documents
other relevant artifacts
```

The system should initialize a professional project workspace rather than immediately trying to produce a final answer.

Useful user-facing areas may include:

```text
Overview
Data
EDA
Validation
Features
Models
Experiments
Evaluation
Findings
Decisions
Report
History
```

These are navigation/views, not a rigid analytical pipeline.

The underlying process remains iterative and should be able to revisit earlier work when findings, requirements, evidence, assumptions, or code change.

## Methodological-navigation brain

The system should maintain a broad, evolving, inspectable catalog of data-science process knowledge rather than depending solely on an LLM recalling an arbitrary subset on each run.

A useful product separation is:

```text
RECOMMENDED
    what currently deserves attention

RELEVANT OPTION SPACE
    everything currently judged applicable

FULL KNOWLEDGE CATALOG
    everything the system knows, browsable/searchable even when not recommended
```

EDA remains the concrete reference example: basic orientation should happen automatically, while the system should know and organize the wider space of possible descriptive statistics, visualizations, data-quality checks, missingness analyses, relationships, temporal analyses, diagnostics, and follow-up investigations.

The goal is to reduce the need for the human to repeatedly remember and prompt for every useful next analysis.

## Candidate product object model

The latest discussion derived a candidate project model from the desired user experience rather than from a backend schema.

The core conceptual separation is:

```text
OBJECTS
RELATIONS
EVENTS
VIEWS
```

Candidate objects:

```text
PROJECT CONSTITUTION
Project
IntentItem
    Objective
    Constraint
    Deliverable
    HumanPreference
    Definition

PROJECT MATERIAL
Artifact
Dataset
Variable

PROJECT EPISTEMIC STATE
Question
Assumption
Finding
Claim

GLOBAL SYSTEM KNOWLEDGE
Method
MethodFamily / MethodKnowledge

WORK AND CHOICE
Proposal
Investigation
Run
Evidence
Decision

PRESENTATION
Report
ReportSection

HISTORY / CONNECTIVITY
Event
Relation
```

Important distinctions include:

```text
Investigation != Run
Evidence != Finding
Finding != Claim
Claim != Decision
current state != event history
persisted object != derived recommendation
workspace section != fundamental object
```

This is a candidate **product model**, not a frozen database ontology.

Detailed reasoning:

```text
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
```

## Professional developer workflow

The system should **complement VS Code rather than replace it**.

Current conceptual separation:

```text
AUTONOMOUS DATA SCIENCE SYSTEM
    project/process control plane

VS CODE
    developer workbench

PYTHON / DOCKER / LOCAL OR REMOTE COMPUTE
    execution plane

GIT + GITHUB
    source versioning, collaboration, and code provenance
```

The system workspace and VS Code should operate on the same coherent project rather than creating unrelated project copies.

Promoted principles:

```text
P-023  The system should complement the professional developer workbench rather than replace it.
P-024  Generated project code should remain independently runnable and professionally maintainable.
```

Generated consequential code should aim to be normal professional project code:

```text
readable
modular
reproducible
configurable
documented
tested where appropriate
version controlled
```

A system-triggered execution and a manual VS Code/terminal execution should preferentially use the same reproducible command/configuration contract.

If code changes after a run, old evidence must keep its original code provenance and a new run should be required for new evidence.

## GitHub and artifact integration

Git/GitHub should be first-class infrastructure for code versioning, collaboration, and experiment provenance.

The system should eventually understand concepts such as:

```text
repository
branch
working-tree state
commit used for a run
remote synchronization
code changes made inside or outside the system
```

Git is **not** intended to store every large data/model artifact.

A likely separation is:

```text
source code / configs / tests / lightweight docs
    -> Git

large datasets / models / prediction arrays / caches
    -> local or external artifact storage
```

The project system should track provenance across both.

## Execution direction

A local-first workflow is currently a strong **hypothesis** for the user's typical projects because the same working tree can be used by the system, VS Code, Git, GitHub synchronization, and local Python/Docker execution.

It is not yet a universal architecture decision.

The execution abstraction should remain compatible with future local GPU, remote GPU, cloud, cluster, or organizational infrastructure.

Useful execution maturity levels may be:

```text
EPHEMERAL ANALYSIS
REPRODUCIBLE INVESTIGATION
PROJECT / FINAL CODE
```

Notebooks and Python modules can coexist according to purpose.

## Human involvement

The target remains interactive, not necessarily black-box autonomous.

A project may support a continuum such as:

```text
GUIDED
system proposes; user selects; system executes

SEMI-AUTONOMOUS
system runs safe/high-confidence work and pauses at important decisions

MORE AUTONOMOUS
system proceeds under an agreed project constitution and escalates where human judgment or authority adds value
```

The desired level of involvement remains a project-intent dimension.

## Evaluation direction

Future evaluation should combine controlled benchmarks with realistic project replay and expert judgment.

Useful measures include:

```text
important-method coverage
recommendation precision
critical omissions
unnecessary recommendations
human reminder burden
human intervention burden
state-recall failures
methodological violations
repeated work
reproducibility
```

Project replay remains a major candidate evaluation method:

```text
completed historical project
    -> restore only original starting inputs
    -> initialize the system from scratch
    -> observe what it surfaces, recommends, remembers, executes, and repairs
    -> compare with known project experience
```

## Current design stage

Do **not** implement V1 yet.

The product/system contract is now substantially clearer in three areas:

```text
1. interactive workspace and methodological-navigation experience
2. candidate product object model
3. integration with VS Code, reproducible execution, Git, and GitHub
```

The next major design problem is the **methodological-navigation brain**:

> How should the system represent a broad universe of data-science knowledge and transform it into known, applicable, relevant, recommended, required, or inapplicable options for the current project?

Questions to resolve next include:

```text
What does a reusable Method/knowledge object contain in practice?
How are applicability conditions represented?
How are relevant options ranked and recommended?
How are alternatives exposed?
How does the system explain why something was or was not recommended?
What role should the LLM play in applicability and ranking?
How should project intent, cost, risk, and human preferences affect priority?
How does knowledge grow from completed projects without overgeneralizing?
How should recommendation quality be evaluated?
```

Only after this product/system reasoning is clearer should the project select the smallest backend architecture worth prototyping.

## Continuity

The standardized new-chat prompt is stored in:

```text
docs/CONTINUITY.md
```

A future session should reconstruct the project from the repository rather than requiring the user to invent a handoff summary.

## Minimum reading for a future session

```text
README.md
docs/CURRENT_STATE.md
docs/KNOWLEDGE_MAP.md
docs/VISION.md
docs/PRINCIPLES.md
docs/foundations/013_system_level_vision_and_llm_system_human_boundary.md
docs/foundations/017_interactive_data_science_workspace_and_methodological_navigation_vision.md
docs/foundations/018_project_object_model_and_professional_developer_workflow_integration.md
docs/experiments/prototype_v0/FINAL_RESULTS.md
docs/CONTINUITY.md
```

## Current priority

**Continue designing the methodological-navigation brain from the product perspective. Do not select a V1 architecture or implementation stack yet. Preserve the V0 constraints, the interactive workspace goal, the product object model, and the professional VS Code/Git/GitHub workflow as separate but interoperable concerns.**