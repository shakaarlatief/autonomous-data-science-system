# Foundation 018: Project Object Model and Professional Developer Workflow Integration

**Date:** 2026-08-19  
**Status:** Foundational product-model and workflow-integration direction  
**Scope:** Long-term Autonomous Data Science System. This document defines product concepts and strong design requirements, not a finalized database schema, execution backend, frontend stack, or V1 implementation.

## Purpose

Foundation 017 made the desired product concrete as a professional interactive data-science workspace with a methodological-navigation brain. The next design discussion clarified two further questions:

1. **What kinds of things should exist inside a project from the product and reasoning perspective?**
2. **How should this system integrate with the professional code-development workflow that already exists around VS Code, Git, GitHub, local Python environments, notebooks, scripts, and reproducible execution?**

The goal is to derive the system model from the desired project experience rather than beginning with a storage ontology or orchestration framework and hoping the product emerges from it.

The central ideas are:

> **The project workspace should be the control and understanding layer for the data-science process, while professional code editing, execution, and version control remain first-class interoperable environments rather than being replaced.**

and:

> **The objects the system persists are not the same as the views the user sees, and neither is the same as the context supplied to an LLM.**

This foundation remains consistent with the V0 lesson that persistent project memory may be valuable even when repeatedly serializing large state into every model call is not.

---

## 1. Four conceptual structures: objects, relations, events, and views

The product should not begin with one giant ontology.

A cleaner conceptual separation is:

```text
OBJECTS
    what exists in the project

RELATIONS
    how those things are connected

EVENTS
    what happened over time

VIEWS
    how the user sees and works with the underlying project
```

This is important because many familiar data-science stages should probably be **views**, not fundamental state objects.

For example:

```text
EDA
Validation
Features
Models
Evaluation
```

are useful workspace sections, but each can be constructed from the same underlying questions, methods, proposals, investigations, runs, evidence, findings, claims, and decisions.

This permits an iterative scientific process without forcing the backend into a rigid pipeline.

---

## 2. Four knowledge worlds should remain distinct

The finished system should conceptually separate at least four kinds of information:

```text
GLOBAL METHODOLOGICAL KNOWLEDGE
    what the system knows about data science generally

PROJECT KNOWLEDGE
    what is known, inferred, assumed, unresolved, or decided for this project

WORK / EXECUTION
    what analyses, experiments, commands, and tool actions were proposed or performed

PRESENTATION
    how project knowledge and work are exposed to the user and assembled into deliverables
```

Conversation is another interaction stream and provenance source, but it should not be the primary storage substrate for these four worlds.

This distinction sharpens the product-level statement:

```text
project workspace = the project
chat = one interface into the project
```

---

## 3. Project constitution objects

### 3.1 Project

`Project` is the top-level identity and container.

It may contain operational metadata such as:

```text
name
creation time
current status
project configuration
linked repository
linked execution environment
participants
```

Important project meaning should not be compressed into unstructured project metadata.

### 3.2 IntentItem

A useful conceptual family is `IntentItem`, with candidate subtypes:

```text
Objective
Constraint
Deliverable
HumanPreference
Definition
```

#### Objective

What the project is trying to achieve.

Examples:

```text
predict churn during the next 30 days
produce the most accurate defensible forecast possible
maximize learning breadth for a portfolio reference project
```

#### Constraint

A boundary the process must respect.

Examples:

```text
final test may be used only after development is locked
training must finish inside a compute limit
certain data cannot appear in reports
only specified tools may be used
```

#### Deliverable

An output that must eventually exist.

Examples:

```text
prediction file
technical report
trained model
presentation
API
GitHub repository
```

#### HumanPreference

Project-specific preferences concerning interaction and process depth.

Examples:

```text
autonomy level
learning breadth
report detail
analysis depth
compute budget
how often the system should ask before acting
```

#### Definition

Semantic definitions that establish what the project means.

Examples:

```text
target definition
prediction unit
prediction moment
forecast horizon
positive class
population of interest
```

These distinctions support the broader project-relative definition of "best" already established in the project vision.

---

## 4. Project material objects

### 4.1 Artifact

`Artifact` is the general representation of material entering, existing within, or leaving the project.

Examples:

```text
PDF
CSV
Parquet dataset
Python module
notebook
plot
table
trained model
configuration
prediction file
report
```

Candidate artifact roles include:

```text
INPUT_SOURCE
GENERATED_OUTPUT
INTERMEDIATE
REFERENCE
PROTECTED_EVALUATION
FINAL_DELIVERABLE
```

Artifacts should retain provenance and version identity.

### 4.2 Dataset

A `Dataset` is a richer interpretation of a data-bearing artifact.

Useful conceptual fields include:

```text
rows
columns
schema
storage format
dataset role
row-unit interpretation
primary key candidates
time range
target when established
known partitions
```

Dataset roles may include:

```text
training
validation
final test
reference
external enrichment
predictions
```

### 4.3 Variable

A `Variable` is important enough to deserve project-level identity because many methodological judgments attach directly to variables.

Candidate information includes:

```text
name
source dataset
stored dtype
inferred semantic type
role
missingness
cardinality
units
description
prediction-time availability
potential leakage concerns
transformations
derivation history
```

The system should preserve the distinction:

```text
stored dtype != semantic type
```

For example, an integer column may semantically be an identifier or category rather than a continuous numeric variable.

---

## 5. Project epistemic objects

### 5.1 Question

`Question` is a central project object.

Examples:

```text
What does one row represent?
Is feature X available at prediction time?
Does missingness change through time?
What validation regime represents deployment?
Why does the model perform poorly for new customers?
```

Questions organize the process around unresolved meaning and evidence rather than around a rigid stage sequence.

Candidate statuses may eventually include:

```text
OPEN
ANSWERED
BLOCKED
DEFERRED
INCONCLUSIVE
SUPERSEDED
```

Exact statuses remain an implementation-design question.

### 5.2 Assumption

`Assumption` represents a proposition the project is temporarily relying on without treating it as fully established.

Example:

```text
Question:
Is this CRM field available at scoring time?

Assumption:
Until stronger evidence appears, provisionally rely on the current documentation that says it is available.
```

This distinction remains useful beyond P0, but it does not imply that every assumption must be included in every LLM call.

### 5.3 Finding

`Finding` is a project-specific interpretation grounded in evidence.

Example:

```text
Evidence:
missingness-by-month table

Finding:
income missingness rises sharply after March
```

### 5.4 Claim

`Claim` is a proposition the project intends to rely on or communicate.

The distinction is:

```text
Finding
    what the evidence appears to show

Claim
    what the project is willing to assert based on that evidence
```

For example:

```text
Finding:
validation AUC = 0.84

Claim:
expected deployment AUC is approximately 0.84
```

The second statement depends on additional assumptions about representativeness and generalization.

---

## 6. Global methodological object

### Method

`Method` belongs primarily to the global methodological knowledge layer rather than being duplicated into every project.

Examples:

```text
Histogram
ECDF
Pearson correlation
Mutual information
Rolling-origin validation
Logistic Regression
Random Forest
RFECV
SHAP
Isotonic calibration
```

A mature Method representation may include:

```text
name
family
purpose
applicability
required inputs
assumptions
parameters
strengths
limitations
common misuse
alternatives
complements
cost
possible outputs
follow-up methods
references / provenance
```

A project should reference the global Method while storing project-specific decisions and applications separately.

For example:

```text
Global method:
Rolling-origin validation

Project-specific proposal:
Use rolling-origin validation for the current forecasting project.
```

This distinction is central to reusable process intelligence.

---

## 7. Work and choice objects

### 7.1 Proposal

`Proposal` is a candidate action, analysis, clarification, decision, or stopping recommendation.

Examples:

```text
run missingness-through-time analysis
use temporal validation
compare logistic regression and gradient boosting
exclude feature X
ask the user to clarify the prediction horizon
stop additional model search
```

A proposal may expose:

```text
why proposed
priority
estimated cost
expected value
supporting project facts
alternatives considered
confidence
```

The user or system may then accept, reject, modify, defer, or discuss it according to the configured interaction mode.

### 7.2 Investigation

`Investigation` represents an analytical activity with a purpose.

It answers the question:

> Why are we doing this work?

Examples:

```text
investigate target distribution
investigate whether missingness changes through time
compare validation designs
investigate poor performance for new customers
```

An investigation may contain several concrete executions and may use several methods.

### 7.3 Run

`Run` is a concrete reproducible execution.

It answers:

> What exactly ran?

Candidate information includes:

```text
method
code version
input artifact versions
configuration
parameters
random seed
environment
start/end time
outputs
logs
resource use
status
```

This gives the important distinction:

```text
Investigation != Run
```

The investigation captures purpose; the run captures execution.

### 7.4 Evidence

`Evidence` is information capable of supporting or challenging a finding or claim.

Evidence may be numerical, visual, documentary, computational, or authoritative human/domain input.

Examples:

```text
AUC = 0.814
residual ACF shows lag-1 dependence
timing notice states feature X is populated after outcome
plot shows target distribution changed after March
```

Evidence should retain provenance automatically whenever possible.

### 7.5 Decision

`Decision` represents a selected course of action.

Examples:

```text
use chronological validation
exclude feature X
select Gradient Boosting
stop hyperparameter tuning
use median imputation
```

A decision should retain the alternatives considered, supporting findings/evidence, relevant constraints, rationale, provenance, and current status.

A decision is distinct from a claim:

```text
Claim:
Gradient Boosting performs best under the accepted validation design.

Decision:
Use Gradient Boosting as the selected model.
```

---

## 8. Reporting objects

### Report and ReportSection

Reporting should be a living projection of accepted project knowledge, not a one-time reconstruction from conversation history.

Conceptually:

```text
Report
    -> ReportSection
        -> Claim
            -> Finding
                -> Evidence
                    -> Run / Artifact
```

If upstream evidence becomes invalid or stale, downstream report content can be flagged rather than silently remaining current.

This supports traceable professional reporting and aligns with Principle P-015.

---

## 9. Human input is primarily event/provenance, not a separate semantic universe

Human clarification and approval are important, but they do not necessarily require a large standalone `HumanInput` object hierarchy.

A human action can be captured as an event and provenance source that creates or changes project objects.

Examples:

```text
User clarified the target definition.
User rejected Proposal P-013.
User approved Decision D-008.
User stated that false negatives are twice as costly.
```

The resulting persistent change may be a Definition, Constraint, Decision, Assumption, or resolved Question.

---

## 10. Events should preserve how the project evolved

Current state answers:

> What is true now?

Events answer:

> How did we get here?

Candidate event types include:

```text
ArtifactUploaded
DatasetProfiled
QuestionOpened
ProposalCreated
ProposalAccepted
InvestigationStarted
RunCompleted
FindingCreated
AssumptionInvalidated
DecisionChanged
HumanClarificationReceived
ReportSectionUpdated
ExternalCodeChanged
GitCommitRecorded
```

Events are useful for:

```text
audit
project timeline
provenance
debugging
reconstruction
learning from projects
```

The complete event stream should usually remain outside the LLM context unless a specific reasoning task requires part of it.

---

## 11. Relations should remain compact and useful

A future project model may need relations such as:

```text
ABOUT
DERIVED_FROM
USES
PRODUCES
SUPPORTS
CONTRADICTS
DEPENDS_ON
ANSWERS
MOTIVATES
SELECTS
SUPERSEDES
APPEARS_IN
```

The project should resist creating a large relation taxonomy prematurely.

The value is in answering practical questions such as:

```text
Which evidence supports this claim?
Which runs produced this evidence?
Which artifact version did this run use?
Which decisions depend on this finding?
Which report sections rely on this claim?
```

The persisted project network may be large while the reasoning context remains selective.

---

## 12. User-facing workspaces are views, not silos

The user should not navigate ontology types directly.

Instead, the product exposes workspaces such as:

```text
Overview
Data
EDA
Validation
Features
Models
Experiments
Findings
Decisions
Report
History
```

Each is a view over the relevant underlying objects.

For example:

```text
EDA
    Questions
    Methods
    Proposals
    Investigations
    Evidence
    Findings

Validation
    Questions
    Methods
    Proposals
    Investigations
    Evidence
    Decisions

Models
    Methods
    Investigations
    Runs
    Evidence
    Findings
    Decisions
```

This keeps the user experience intuitive without making the scientific process rigidly stage-based.

---

## 13. Durable objects and derived projections should be separated

Not every UI result needs to become permanent state.

Potentially durable information includes:

```text
project meaning
artifacts
questions
assumptions
investigations
runs
evidence
findings
claims
decisions
```

Potentially derived/recomputable information includes:

```text
method rankings
recommendation lists
priority scores
workspace summaries
suggested next actions
```

If the user acts on a recommendation, that action and its consequences should become durable history.

This separation reduces unnecessary state growth and is a direct response to P0's over-persistent representation cost.

---

## 14. The system should complement VS Code rather than replace it

The desired product is a data-science project control and reasoning environment, not a replacement IDE.

VS Code already provides a mature professional environment for:

```text
reading code
editing code
debugging
running terminals
working with notebooks
using extensions
reviewing source control
```

The system should therefore integrate with the developer workbench rather than recreate those capabilities badly inside the frontend.

A useful conceptual separation is:

```text
AUTONOMOUS DATA SCIENCE SYSTEM
    project/process control plane

VS CODE
    developer workbench

LOCAL / REMOTE PYTHON, CONTAINERS, GPU, ETC.
    execution plane

GIT + GITHUB
    code versioning, collaboration, and durable provenance
```

The system workspace and the code editor are different interfaces over the same project.

---

## 15. Generated project code must remain independently runnable

A strong product requirement is:

> **The project code generated or maintained by the system must remain normal, professional, independently runnable code that does not require the Autonomous Data Science System UI to function.**

The code should aim to be:

```text
readable
modular
professionally structured
reproducible
configurable
documented
tested where appropriate
version controlled
```

If the system disappeared, the resulting Git repository should still be a good data-science project.

This prevents the platform from trapping analytical logic behind proprietary UI actions and makes the work inspectable and credible in normal professional environments.

---

## 16. System execution and manual execution should share the same run contract

The system should avoid having one hidden execution path for UI-triggered jobs and a separate unrelated path for manual execution.

A preferred design is:

```text
reproducible command / job specification
        |
        +--> system invokes it
        |
        +--> user invokes the same thing in VS Code / terminal
```

For example:

```text
python -m project.experiments.run --config configs/model_017.yaml
```

The command, configuration, environment, outputs, and provenance should be the same whether launched by the system or by the user.

This supports transparency, debugging, reproducibility, and trust.

---

## 17. Local-first execution is a strong current hypothesis, not yet a fixed architecture

For many individual data-science projects, the most natural initial execution model may be:

```text
professional system UI
        |
local project service
        |
shared local working tree
        |
VS Code + Git + Python / Docker
```

The same project folder could be visible simultaneously to:

```text
the system
VS Code
Git
GitHub synchronization
local execution
```

This avoids unnecessary copies and a repetitive remote-edit/pull loop.

However, **local-first is not yet an accepted universal architecture decision**.

The design should remain compatible with optional future execution on:

```text
local GPU
remote GPU
cloud VM
cluster
company infrastructure
managed notebook or compute platform
```

The methodological brain should ideally operate on an execution abstraction such as:

```text
RUN THIS REPRODUCIBLE JOB
```

while the execution backend determines where it runs.

---

## 18. Git and GitHub should be deeply integrated, but they are not the entire project store

Git/GitHub should be first-class project infrastructure.

The system should eventually understand concepts such as:

```text
repository
branch
working-tree state
commits
remote synchronization
code version used for an experiment
report code version
```

A run can then retain provenance such as:

```text
Run R-044
    code commit: abc123
    config: model_017.yaml
    input dataset version: D-006
```

The UI may eventually support operations such as:

```text
view changes
open repository
commit
push
create branch
open in GitHub
open code in VS Code
```

Exact write permissions and confirmation rules remain a separate product/safety design question.

Git should not be abused as storage for every large generated artifact.

A useful distinction is:

```text
source code / configs / tests / lightweight docs
    -> Git

large datasets / large models / prediction arrays / caches
    -> local or external artifact storage
```

The system can track both through artifact provenance without forcing every byte into Git history.

---

## 19. External code edits should create new project state, not rewrite old evidence

If a user edits code in VS Code after an experiment ran, the system should not silently reinterpret old evidence as if it came from the new code.

Instead:

```text
code changes
    -> new code version / working-tree state
    -> existing runs retain old provenance
    -> rerun required for new evidence
```

The system may detect and surface:

```text
Code changed externally.
The current experiment result was produced before this change.
Create a new run to evaluate the modified implementation.
```

This is a direct application of provenance and evidence integrity.

---

## 20. Not every exploratory action should become permanent production code

The system should support multiple execution/promotion levels.

A useful conceptual distinction is:

```text
EPHEMERAL ANALYSIS
    quick exploration; not necessarily promoted to project source

REPRODUCIBLE INVESTIGATION
    stored code/config/results/provenance

PROJECT / FINAL CODE
    clean maintained implementation, tests, documentation, version control
```

A useful exploratory analysis can be promoted into a reproducible investigation when it becomes important.

This avoids generating thousands of tiny permanent scripts while still preserving consequential work.

---

## 21. Notebooks and scripts can coexist

The system should not force a false choice between notebooks and modules.

A professional workflow may reasonably use:

```text
notebooks / interactive cells
    exploratory investigation and explanation

Python modules
    reusable logic and pipelines

configuration-driven scripts
    experiments and batch execution

tests
    correctness and regression protection
```

The criterion is reproducibility and maintainability, not one universal file style.

---

## 22. Additional architectural separations

The discussion adds several strong distinctions to the project's architectural vocabulary:

```text
what the system remembers
    !=
what the LLM sees

project workspace
    !=
code editor

project orchestration
    !=
execution environment

Git/GitHub provenance
    !=
full project/artifact storage

investigation purpose
    !=
concrete run

current project state
    !=
historical event stream

user-facing workspace section
    !=
fundamental persisted object
```

These separations should help prevent future implementations from conflating responsibilities merely because they are convenient to combine in an early prototype.

---

## 23. Example end-to-end object flow

A simplified example illustrates how the product model and professional workflow can fit together.

```text
User uploads assignment.pdf and train.csv
        |
        v
Artifact + Dataset objects created
        |
        v
Variable profiling discovers repeated customer IDs
        |
        v
Question:
What does one row represent?
        |
        v
Proposal:
Investigate row-unit and temporal/entity structure
        |
        v
Investigation created
        |
        v
Reproducible Run executes locally
using code visible in the project repository
        |
        v
Evidence:
customer IDs repeat
(customer_id, month) is unique
        |
        v
Finding:
rows appear to be customer-month snapshots
        |
        v
Question answered
        |
        v
Validation workspace recomputes relevant options
        |
        v
Proposal:
use chronological validation
        |
        v
User discusses / accepts
        |
        v
Decision recorded
        |
        v
Code/config committed to Git
        |
        v
experiment provenance references commit
```

The same underlying project can be inspected through the system UI, VS Code, Git, and GitHub without creating four different project copies.

---

## 24. What is intentionally not decided here

This foundation does **not** choose:

```text
PostgreSQL schema
graph database versus relational storage
JSON serialization
UUID conventions
exact object statuses
exact relation vocabulary
vector retrieval architecture
LLM provider
one versus multiple reasoning roles
frontend framework
backend framework
local-only versus cloud execution
GitHub write-confirmation policy
job queue technology
```

Those decisions should follow from the product behavior and experimental requirements rather than precede them.

---

## 25. Current candidate core object model

The product-level candidate model can be summarized as:

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

This is a **candidate product model**, not a frozen implementation ontology.

Its value should be evaluated by whether it supports the desired project experience cleanly, not by whether every possible data-science concept can be forced into it.

---

## 26. Next design question

The next major design problem remains the methodological-navigation brain:

> **How should the system represent a broad universe of data-science knowledge and transform it into applicable, relevant, recommended, required, or inapplicable options for the current project?**

That requires clarifying:

```text
what a reusable Method/knowledge object really contains;
how project facts are matched to applicability conditions;
how an LLM contributes without being the only memory;
how recommendation/ranking works;
how alternatives are surfaced;
how the system explains why something was or was not recommended;
how knowledge grows from completed projects;
how cost, risk, project intent, and human preferences affect prioritization;
how recommendations remain auditable and revisable.
```

The product object model and developer-workflow integration defined here provide the conceptual substrate on which that brain can operate.