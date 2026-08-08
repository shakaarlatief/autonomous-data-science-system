# Current State

## Checkpoint

**Checkpoint:** 5  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, depth, speed, or low cost are project-dependent objectives rather than universal goals.

## Current project-constitution hypothesis

The current conceptual hierarchy remains:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

The five candidate epistemic invariants remain:

1. semantic validity;
2. information legitimacy;
3. evidence validity;
4. claim validity;
5. traceability and dependency integrity.

These remain strong design hypotheses rather than finalized requirements.

## Checkpoint 3: admissibility, risk, and assurance

The project currently hypothesizes that admissibility should be action-specific and authority-aware, risk should be represented through failure scenarios rather than one unexplained project-level label, inherent and residual risk should be distinguished, controls should be credible, and risk should dynamically affect assurance, autonomy, review, monitoring, and human gates.

Detailed reasoning:

`docs/foundations/003_admissibility_risk_and_assurance.md`

## Checkpoint 4: project state and state-driven orchestration

The central Checkpoint 4 hypothesis remains:

> **Project state should not be passive memory. It should represent the evolving epistemic and operational situation strongly enough to determine what the system is still entitled to believe, what is stale or invalid, what obligations exist, and what should happen next.**

Candidate first-class state objects include:

```text
PROJECT INTENT
FACT
ASSUMPTION
QUESTION
INVESTIGATION
EVIDENCE
CLAIM
DECISION
RISK
CONTROL
APPROVAL
CONSTRAINT / RULE
ACTION
ARTIFACT
```

Typed dependency relationships may include meanings such as support, contradiction, hard dependency, derivation, information influence, blocking, invalidation, supersession, requirement, mitigation, and approval.

Important current hypotheses from Checkpoint 4 include:

- separate validity from currency;
- preserve both current state and meaningful history;
- perform impact analysis when consequential upstream state changes;
- reopen questions and decisions when their support changes;
- treat invalidation as creating new obligations rather than merely changing a status label;
- track information lineage in addition to computational lineage;
- detect high-leverage fragile assumptions and epistemic single points of failure;
- derive plans from state rather than treating plans as the deepest source of truth;
- maintain a runnable frontier of useful executable actions;
- separate mandatory integrity/admissibility/assurance obligations from optional value-improving work;
- select optional actions using expected project value, information value, dependency leverage, risk reduction, cost, and project intent.

Detailed reasoning:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

## Major development since Checkpoint 4: project initialization

Checkpoint 5 addresses how a project enters the system before a rich project state already exists.

The strongest current formulation is:

> **A new project should enter the system through progressive state construction rather than one-shot problem definition. Initial requests, documentation, code, data, and external information should be registered with provenance, converted into provisional facts, assumptions, questions, constraints, and candidate interpretations, and continuously reconciled as evidence accumulates.**

The initial user request should therefore be treated as source material about the project rather than automatically converted into ground truth.

The project now distinguishes conceptually:

```text
ORIGINAL PROJECT INPUT
what a source actually stated

CURRENT PROJECT INTERPRETATION
what the system currently believes the project means
```

Material disagreement between sources should become explicit state rather than being silently resolved.

## Source-aware project entry

A new project may include user requests, datasets, schemas, READMEs, data dictionaries, notebooks, code, saved models, configuration, deployment descriptions, reports, and external requirements.

The bootstrap should first register what sources exist before relying on them.

A strong current hypothesis is:

> **Authority is question-specific.**

The user may be authoritative about desired project intent, while a production system owner or deployment specification may be more authoritative about operational feature availability. Direct data inspection is authoritative about what is present in a file but does not by itself determine business semantics.

No universal source-precedence model has been selected.

## Progressive semantic commitment

Different actions require different semantic prerequisites.

The system should therefore avoid both blindly modelling from an incomplete initial request and requiring exhaustive project understanding before any useful work can begin.

The emerging rule is:

> **Require only the semantic information necessary for the next action, while preventing actions whose material semantic prerequisites remain unresolved.**

Project understanding remains revisable throughout the project.

## Universal bootstrap inspection

A major Checkpoint 5 hypothesis is that the fixed project-entry process may be much smaller than a complete universal data-science workflow.

The bootstrap should remain:

```text
broadly relevant
low semantic commitment
low risk
high trigger value
relatively cheap
non-destructive
provenance-preserving
reversible
```

Its purpose is not to complete EDA or choose modelling strategy.

Its purpose is to create enough trustworthy structural state for specialized reasoning to activate.

A concise behavioral rule is:

> **Observe broadly, infer cautiously.**

## Information boundaries apply during bootstrap

The bootstrap itself must obey information legitimacy.

Before deeply inspecting a source, the system should determine its likely role and what information is legitimate to consume.

This is especially important for final test or holdout data. Structural metadata may be legitimate to inspect while target values or outcome associations remain protected from development.

A future execution environment may need enforceable information barriers, but no implementation has been selected.

## Candidate bootstrap observations

High-value structural observations may include:

- available sources, files, and versions;
- dataset shape and schema;
- physical data types;
- candidate identifiers and cardinality;
- timestamps or ordering variables;
- candidate target structure where legitimate;
- missingness presence and approximate rates;
- duplicate or repeated-entity structure;
- data partitions;
- entity and temporal overlap across partitions;
- obvious structural inconsistencies;
- existing implementation and environment structure;
- executability and resource availability;
- obvious governance-relevant facts or hard restrictions.

These observations should create facts, conflicts, hypotheses, and triggers rather than immediately dictate downstream responses.

## Bootstrap detects conditions; specialized knowledge reasons about responses

Examples:

```text
42% missingness detected
    -> activate missing-data reasoning
    -> do not automatically median-impute
```

```text
timestamp detected
    -> activate temporal-structure reasoning
    -> do not automatically fit a time-series model
```

```text
2% positive class detected
    -> activate imbalance / metric / threshold reasoning
    -> do not automatically apply SMOTE
```

This separation is central to keeping the universal process small while preserving project-specific methodological depth.

## Multidimensional project characterization

The project should probably be characterized by multiple structural properties rather than one exclusive project-type label.

For example, one task may simultaneously be:

```text
supervised
binary classification
temporal
grouped
forward-looking
sequence-derived
imbalanced
```

Those properties can activate different reasoning modules.

The exact representation remains open.

## Intended use remains high leverage

Intended use affects validation, feature legitimacy, metrics, interpretation, risk, admissibility, monitoring, and human gates.

The system should try to establish intended use relatively early while keeping it revisable.

A later transition from exploratory analysis to operational deployment should trigger impact analysis and new assurance obligations rather than acting like a harmless metadata edit.

## Selective human clarification

The system should not start every project with a large questionnaire.

It should first use available data, documentation, schemas, code, and authoritative sources when they can resolve a question cheaply and reliably.

Human clarification becomes a first-class action when a material semantic, normative, authority-dependent, or blocking question cannot be resolved reliably from existing evidence.

A derived human-facing **Current Project Interpretation** may eventually help users correct high-leverage misunderstandings efficiently without making the summary itself the source of truth.

## Initialization stopping condition

Checkpoint 5 introduces the following strong hypothesis:

> **Initialization is sufficiently advanced once at least one useful, admissible, methodologically legitimate action can proceed, while important unresolved questions and blockers are explicitly represented.**

Initialization therefore does not require complete certainty about every future project decision.

Blocking is relative to actions and milestones rather than one project-wide yes/no flag.

## Six candidate universal bootstrap responsibilities

The current bootstrap can be compressed conceptually into six responsibilities:

1. **Register sources and information boundaries.**
2. **Establish structural facts.**
3. **Compare sources for consistency.**
4. **Generate project-characterization hypotheses.**
5. **Emit triggers and questions.**
6. **Construct the first runnable frontier.**

This is a conceptual protocol, not a selected implementation workflow.

## Major simplification

One of the strongest simplifications found so far is:

```text
SMALL UNIVERSAL BOOTSTRAP PROTOCOL
                +
ADAPTIVE STATE-DRIVEN REASONING
```

rather than one complete universal data-science pipeline.

Conceptually:

```text
NEW PROJECT
    -> source registration
    -> provisional interpretation
    -> information-boundary determination
    -> universal bootstrap inspection
    -> structural facts and conflicts
    -> characterization hypotheses
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

Detailed reasoning is preserved in:

`docs/foundations/005_project_initialization_and_universal_bootstrap.md`

Historical snapshot:

`docs/checkpoints/005_project_initialization_and_universal_bootstrap.md`

## Strong design hypotheses currently active

Important active hypotheses include:

- five candidate epistemic invariants;
- a project constitution separating admissibility, epistemic integrity, risk-sensitive assurance, and optimization;
- typed dependency-aware project state;
- questions and claims as important orchestration objects;
- impact analysis and change propagation;
- information lineage in addition to computational lineage;
- a runnable frontier;
- separation of mandatory obligations from optional prioritization;
- state-driven rather than plan-driven orchestration;
- source-aware progressive project initialization;
- question-specific authority;
- explicit representation of source conflicts;
- progressive semantic commitment;
- a small universal bootstrap protocol;
- trigger-oriented structural inspection;
- multidimensional project characterization;
- initialization completion based on a legitimate runnable frontier.

## Explicit non-decisions

The project has not selected agent count, LLM providers, orchestration framework, workflow engine, database, graph technology, event-log architecture, exact project-state schemas, source schema, authority model, exact bootstrap checklist, project-characterization schema, information-barrier implementation, trigger representation, module representation, rule engine, exact status machines, materiality model, priority formula, parallel scheduler, execution sandbox, final autonomy model, final completion rule, or system-evaluation framework.

## Current focus

The next major conceptual question is:

> **How should discovered project facts, conflicts, questions, and characterization properties activate the correct reusable knowledge modules, rules, reviewers, or open-ended reasoning without creating one impossibly large centralized decision tree?**

This is the **knowledge-activation problem**.

Important subquestions include:

- What exactly is a trigger?
- What should a reusable knowledge module receive and produce?
- Should modules subscribe to state patterns rather than call each other directly?
- Can multiple modules activate from the same fact?
- Can modules activate further modules through new state changes?
- Which activations should be deterministic versus proposed by an LLM?
- How should missed activations be detected?
- How should the system avoid over-activation and irrelevant work?
- How should reviewers and open-ended reasoning participate in the same activation mechanism?
- How should activations create questions, obligations, or candidate actions on the runnable frontier?

This should remain conceptual before choosing a rule engine, graph system, workflow framework, or agent architecture.

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

For detailed reasoning, also read the five files currently under `docs/foundations/`.

Relevant historical checkpoints are Checkpoints 0 through 5 under `docs/checkpoints/`.

## Next step

Develop the conceptual knowledge-activation mechanism linking project-state facts and questions to reusable modules, rules, reviewers, and open-ended reasoning before choosing implementation technology.