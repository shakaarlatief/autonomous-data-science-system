# Current State

## Checkpoint

**Checkpoint:** 4  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, depth, speed, or low cost are therefore project-dependent objectives rather than universal goals.

## Current project-constitution hypothesis

The current conceptual hierarchy is:

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

## Admissibility, risk, and assurance

Checkpoint 3 established strong hypotheses that admissibility should be action-specific and authority-aware, risk should be scenario-based rather than one unexplained label, inherent and residual risk should be distinguished, controls should be credible, and risk should dynamically affect assurance, autonomy, and human gates.

Detailed reasoning is preserved in:

`docs/foundations/003_admissibility_risk_and_assurance.md`

## Major development since Checkpoint 3: project state

The central new hypothesis is:

> **Project state should not be passive memory. It should represent the evolving epistemic and operational situation strongly enough to determine what the system is still entitled to believe, what is stale or invalid, what obligations exist, and what should happen next.**

### Candidate state objects

The current minimal conceptual vocabulary is:

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

This is not a finalized ontology or schema.

The important distinction is epistemic role. Facts, assumptions, evidence, claims, decisions, approvals, risks, and controls should not collapse into one narrative record.

## Questions as a likely orchestration backbone

The hypothesis that analytical questions are more fundamental than pipeline stages has strengthened.

Questions may differ by purpose, blocking power, importance, evidence requirements, and current resolution state. A question can be sufficiently resolved even when the result is inconclusive if the remaining uncertainty is acceptable for the current decision.

## Evidence, claims, and decisions

The current reasoning structure distinguishes:

```text
question
    -> investigation
    -> evidence
    -> claim
    -> decision
```

while allowing later evidence to reopen questions, claims, or decisions.

Evidence should preserve how it was produced. Claims should preserve support and assumptions. Decisions should preserve rationale, alternatives, and dependencies.

## State and history

The system needs both:

1. a usable current view of what should be believed and acted upon now; and
2. historical preservation of how important state changed.

Important state should not simply be overwritten. No event-sourcing or storage architecture has been selected.

## Validity and currency

The project now distinguishes whether an object is valid from whether it is current.

Examples include valid but stale, invalid, valid but superseded, and under review.

## Dependency-aware state

A major hypothesis is that state objects should have typed relationships with enough semantic meaning to support change propagation.

Candidate relationship meanings include:

```text
supports
contradicts
hard_depends_on
derived_from
informed_by
answers
motivates
blocks
invalidates
supersedes
requires
implements
mitigates
approves
generated_by
```

The exact vocabulary remains open.

Different dependency types should propagate differently. Hard validity dependencies may invalidate downstream work. Loss of one evidence item may only require claim reassessment. New source versions may create staleness. Missing approvals may block actions. Failed controls may reopen risk.

## Impact analysis and self-correction

A consequential state change should trigger impact analysis:

```text
new fact / revision / invalidation / new version
        -> identify changed object
        -> traverse typed dependencies
        -> determine impact
        -> apply deterministic effects
        -> mark ambiguous dependents for reassessment
        -> reopen affected questions or decisions
        -> generate new obligations
        -> prioritize repair, review, rerun, or clarification
```

This is a central candidate mechanism for making the future system self-correcting.

Invalidation should therefore create obligations rather than merely change a status label.

## Materiality and repair priority

Not every affected object should be repaired immediately.

The system should distinguish what is affected from what must be repaired now. Priority may depend on materiality, downstream importance, risk, deliverable relevance, cost, and expected value.

The exact materiality model remains open.

## Computational lineage versus information lineage

File and code lineage are insufficient because human or LLM reasoning can create indirect information dependencies.

The project now distinguishes conceptually:

```text
computational / provenance lineage
    dataset -> transformation -> model -> prediction

epistemic / information lineage
    fact -> question -> evidence -> claim -> decision -> action

governance lineage
    constraint -> control -> approval -> action
```

This may be important for leakage auditing, reviewer independence, and reasoning provenance.

## Fragility and epistemic single points of failure

Dependency structure could reveal claims with one support path, apparently independent experiments sharing one flawed ancestor, high-leverage assumptions with large downstream effects, circular support, and unresolved questions that gate much of the project.

The project currently refers to such high-leverage fragile nodes conceptually as **epistemic single points of failure**.

## Major development since Checkpoint 3: state-driven orchestration

Plans should likely be derived from project state rather than act as the deepest source of truth.

Every consequential next action should ideally be traceable to an unresolved question, obligation, risk, constraint, deliverable need, repair requirement, or accepted decision.

### Runnable frontier

The discussion introduced the conceptual **runnable frontier**: currently useful candidate actions whose prerequisites are satisfied and which are not blocked by admissibility, approval, dependencies, resources, or required independence.

### Hard gates versus prioritization

Mandatory validity, admissibility, and assurance obligations should not compete as ordinary weighted preferences with optional optimization work.

A candidate policy is:

1. identify hard blockers and mandatory obligations;
2. filter actions that are not currently executable;
3. satisfy prerequisites needed to unlock consequential work;
4. prioritize remaining runnable actions according to expected project value.

### Candidate prioritization factors

Current candidate factors include blocking power, validity importance, risk reduction, probability of changing an important decision, uncertainty reduction, downstream dependency leverage, deliverable relevance, urgency, compute and human cost, reversibility, parallelizability, and project objectives.

No weighted formula has been selected.

A useful qualitative value-of-information intuition is:

```text
value of investigation
    ~ probability it changes an important decision
      x importance of that decision
      - cost of obtaining the information
```

## Parallelism and human clarification

Dependency structure can determine what can run in parallel, what must wait, and what should remain isolated for independent review.

Asking the human is also a first-class candidate action when a high-impact semantic, normative, domain, or authority question cannot be resolved reliably from available evidence.

## Stopping and completion

The current direction distinguishes local stopping from project completion.

A question may stop when evidence is sufficient for the current decision, remaining uncertainty is decision-irrelevant, further work has low expected value, or available data cannot discriminate alternatives.

A project may be complete when mandatory epistemic, admissibility, assurance, approval, and deliverable obligations are sufficiently resolved, critical state is internally consistent, no important current output depends on known invalid state, and remaining optional work has insufficient expected value for the project's intent and budget.

The final completion rule remains open.

## Current control-loop hypothesis

```text
CURRENT PROJECT STATE
        -> identify unresolved questions, obligations, risks,
           stale/invalid objects, approvals, deliverable needs
        -> generate candidate actions
        -> filter by prerequisites and constraints
        -> identify mandatory blockers
        -> prioritize remaining runnable candidates
        -> execute one action or compatible parallel set
        -> update evidence, artifacts, decisions, approvals, or revisions
        -> perform impact analysis
        -> recompute state and runnable frontier
```

This is a behavioral hypothesis, not an implementation commitment.

## Project state may be more fundamental than the orchestrator

A conceptual shift has occurred: the durable core may be project state, with reasoning, execution, review, and orchestration acting on that state.

No database, graph, workflow, agent, or event-log technology has been selected.

Detailed reasoning is preserved in:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

Historical snapshot:

`docs/checkpoints/004_project_state_and_state_driven_orchestration.md`

## Strong design hypotheses currently active

Important active hypotheses include:

- fact-triggered investigations and reusable knowledge modules;
- five candidate epistemic invariants;
- the project-constitution model;
- action-specific admissibility and scenario-based risk;
- dynamic autonomy and required versus preferred human involvement;
- typed persistent project-state objects;
- analytical questions as an orchestration backbone;
- typed dependency relationships;
- separate validity and currency;
- impact analysis and change propagation;
- information lineage in addition to computational lineage;
- epistemic single points of failure;
- plans as derived views;
- a runnable frontier;
- separation of hard obligations from optional prioritization;
- dependency-aware value-of-information action selection;
- dynamic stopping based on unresolved obligations rather than fixed pipeline stages.

## Explicit non-decisions

The project has not selected agent count, LLM providers, orchestration framework, workflow engine, database, graph technology, event-log architecture, exact project-state schemas, exact relationship vocabulary, exact status machines, materiality model, priority formula, parallel scheduler, execution sandbox, final autonomy model, final completion rule, or system-evaluation framework.

## Current focus

The next major conceptual question is:

> **How should a new project enter the system and be initialized into the project-state model when the user's initial request, data, documentation, constraints, and intended use may be incomplete or partially wrong?**

Important subquestions include:

- What should be extracted from the initial request before inspecting data?
- What should be inferred from files, documentation, repository context, and early data inspection?
- What should the system ask the human immediately versus investigate itself first?
- How should project intent be initialized?
- How should the analytical object, population, time, prediction point, intended use, and desired claim strength be established?
- When should admissibility and initial risk assessment begin?
- Which missing facts should block modelling?
- How should the system avoid overwhelming the user with unnecessary questions?
- How does initial inspection create the first runnable frontier?

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

For detailed reasoning, also read the four files currently under `docs/foundations/`.

Relevant historical checkpoints are Checkpoints 0 through 4 under `docs/checkpoints/`.

## Next step

Develop the conceptual project-initialization process: how an incomplete real-world request becomes a sufficiently specified initial project state and first runnable frontier without assuming that the initial framing is complete, valid, or operationally sufficient.