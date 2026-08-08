# Current State

## Checkpoint

**Checkpoint:** 6  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Primary purpose

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, autonomy, depth, speed, or low cost are project-dependent objectives rather than universal goals.

## Current project-constitution hypothesis

The conceptual hierarchy remains:

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

Project state is now treated conceptually as a living representation of what the system is currently entitled to believe and do rather than passive memory.

Candidate state objects include:

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

Strong hypotheses include typed dependencies, separate validity and currency, impact analysis, reopening of questions and decisions, information lineage in addition to computational lineage, a runnable frontier, hard obligations separated from optional value-improving work, and state-driven rather than plan-driven orchestration.

Detailed reasoning:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

## Checkpoint 5: project initialization and universal bootstrap

A new project should enter through progressive state construction rather than one-shot problem definition.

Initial requests, documentation, code, data, and external information should enter project state with provenance and should remain revisable.

The fixed project-entry process may be much smaller than a complete universal workflow:

```text
SMALL UNIVERSAL BOOTSTRAP
        +
ADAPTIVE STATE-DRIVEN REASONING
```

The six candidate bootstrap responsibilities are:

1. register sources and information boundaries;
2. establish structural facts;
3. compare sources for consistency;
4. generate project-characterization hypotheses;
5. emit triggers and questions;
6. construct the first runnable frontier.

A concise bootstrap rule remains:

> **Observe broadly, infer cautiously.**

Detailed reasoning:

`docs/foundations/005_project_initialization_and_universal_bootstrap.md`

## Major development since Checkpoint 5: knowledge activation

Checkpoint 6 develops the first coherent conceptual model for how reusable data-science knowledge becomes relevant to a live project.

The central hypothesis is:

> **Reusable data-science knowledge should be activated from patterns in project state and should contribute structured questions, obligations, safeguards, evidence requirements, review needs, and candidate actions back into that state rather than directly controlling one fixed workflow.**

This is intended to avoid both one enormous centralized decision tree and a design in which one LLM must remember the entire universe of data-science concerns at every step.

## Knowledge, capability, and actor are conceptually separate

The project now strongly distinguishes:

```text
KNOWLEDGE
What should be considered?

CAPABILITY
How can it be investigated or enforced?

ACTOR
Who or what performs the work?
```

A missing-data knowledge unit is therefore not inherently a `MissingDataAgent`. The same knowledge may be used by a general reasoning model, deterministic validator, code executor, specialist reviewer, or human-facing clarification flow.

## Reusable definitions versus project-specific instances

The system-level knowledge library should contain reusable definitions.

A project should create scoped instances when that knowledge becomes relevant to particular facts, questions, datasets, features, actions, claims, models, decisions, or deployment contexts.

Project-specific instances can then be resolved, reopened, or revised without changing the reusable definition itself.

## Activation is not execution

A trigger means that current state has created sufficient reason for a concern to be represented or considered.

Actual work still competes on the runnable frontier.

The project therefore distinguishes:

```text
ACTIVATION PRIORITY
What knowledge is relevant?

EXECUTION PRIORITY
What work should happen now?
```

## Candidate activation strengths

A useful conceptual distinction is:

```text
ENFORCE
A sufficiently established condition creates a mandatory requirement.

INVESTIGATE
Applicability or consequences need to be established.

CONSIDER
Potentially useful but not currently mandatory.
```

The exact labels and status model remain open.

## Hybrid activation mechanisms

The current direction combines:

1. **deterministic activation** for precise hard safeguards;
2. **interpretive activation** for state patterns whose relevance requires reasoning;
3. **open-ended discovery** for novel concerns not represented by the current knowledge library.

No rule engine, retrieval technology, or LLM routing architecture has been selected.

## Trigger sources are broader than data observations

Checkpoint 6 substantially expands the original fact-trigger concept.

Knowledge may activate because of:

- an observed fact;
- a combination of facts;
- a requested analytical objective;
- a desired claim type or strength;
- a proposed action;
- a proposed method;
- a proposed decision;
- a proposed claim;
- a missing prerequisite;
- a contradiction;
- risk or governance state;
- a dependency revision;
- a novel concern proposed through open-ended reasoning.

The activation layer should therefore react to meaningful project-state transitions broadly rather than only raw data observations.

## Reactive and prospective activation

The project now distinguishes conceptually:

```text
REACTIVE ACTIVATION
Something material was discovered.

PROSPECTIVE ACTIVATION
Something consequential is about to be claimed,
decided, or executed.
```

Prospective activation is especially important for methodological and governance safeguards.

Examples include protecting a final test set before an agent inspects outcomes, checking target encoding for information leakage before execution, or evaluating a sensitive-data transfer before it occurs.

## Missing prerequisites can activate obligations

Absence of required state can itself be a trigger.

Examples include:

```text
causal claim requested
but identification assumptions absent
```

```text
deployment proposed
but monitoring obligations unsatisfied
```

```text
final model selection proposed
but no accepted validation design exists
```

```text
external transfer proposed
but permission state unresolved
```

This allows the system to generate missing semantic, methodological, evidence, governance, or assurance obligations before unsafe downstream actions occur.

## Module input and output

Activated knowledge should receive a relevant project-state slice rather than the entire conversational history.

A knowledge unit may contribute typed objects such as:

- analytical questions;
- semantic or methodological obligations;
- evidence requirements;
- candidate investigations;
- constraints and safeguards;
- risk scenarios;
- review requests;
- human clarification requests;
- candidate decisions or alternatives;
- conditions for sufficient resolution.

The output should update project state rather than remain an isolated prose response.

## Module interaction through shared state

The preferred conceptual pattern is:

```text
MODULE A
    -> PROJECT STATE UPDATE
    -> activation layer evaluates new state
    -> MODULE B may become relevant
```

rather than direct hard-coded module-to-module calls.

This reduces coupling and makes the reason for cross-activation traceable.

## Shared questions as integration points

Multiple knowledge units may converge on one analytical question.

For example, temporal structure, repeated entities, and leakage concerns may all motivate:

> Does the validation design represent the intended deployment regime?

The project therefore increasingly views shared analytical questions as a mechanism for recombining modular knowledge without creating duplicated workflows.

## Evidence frameworks rather than cookbook rules

Knowledge units should encode distinctions, failure modes, evidence requirements, and conditional strategies rather than unconditional recipes such as:

```text
missing values -> median imputation
imbalance -> SMOTE
```

The response should emerge from project-specific evidence and constraints.

A knowledge unit may contain hard safeguards, explicit decision frameworks, and open-ended reasoning within the same analytical area.

## Scope and applicability

Knowledge instances should likely be scoped to entities such as a project, dataset, partition, feature, target, subgroup, model, claim, decision, action, or deployment environment.

The exact scope representation remains open.

To control over-activation, semantic retrieval may use a two-step process:

```text
candidate relevance
    -> applicability determination
    -> project-specific knowledge instance
```

Precise deterministic rules may not need this interpretive applicability stage.

## Open-world and compositional knowledge

The system should assume its reusable knowledge library is incomplete.

Open-ended reasoning must be able to create novel concerns when no exact module fits.

A complex concern may compose several partial knowledge units rather than mapping to one perfect module.

This means the project has not committed to one homogeneous module granularity or taxonomy.

## Coverage review and omission detection

Because false-negative activation is possible, the system likely needs a residual coverage process asking whether important project facts remain unrepresented by active reasoning, accepted resolution, explicit irrelevance, or acknowledged residual uncertainty.

This produced the concept of an **orphaned material fact**:

> An important project-state fact with no reasoning consequence and no explicit rationale for why it is irrelevant.

The complementary concept is an **orphaned action**:

> Consequential work with no state-based justification such as a question, obligation, objective, risk reduction need, deliverable requirement, or accepted decision.

These are promising general integrity checks.

## Review participates in the same activation model

Independent review, replication, leakage review, privacy review, validation review, or other specialist checks need not form a fixed always-on roster.

They can activate because of risk, weak high-leverage assumptions, evidence fragility, governance state, or assurance requirements.

## Activation quality is itself a system-evaluation target

The activation mechanism has symmetrical failure modes:

```text
FALSE POSITIVE
irrelevant concern activated and resources wasted

FALSE NEGATIVE
material concern never represented
```

Future project tests should therefore measure important concerns correctly activated, important concerns missed, irrelevant activations, unnecessary analytical cost, delay before issue discovery, and whether coverage review recovers omissions.

## Stress-test result

The activation abstraction was stress-tested conceptually against:

- missing data;
- temporal structure;
- repeated entities / group dependence;
- target leakage and test-set integrity;
- class imbalance;
- causal inference;
- clustering;
- privacy and admissibility;
- novel domain-specific feedback-loop concerns.

The abstraction remained coherent across these cases but required the refinements documented above.

Detailed reasoning:

`docs/foundations/006_knowledge_activation_and_open_world_reasoning.md`

Historical snapshot:

`docs/checkpoints/006_knowledge_activation_and_open_world_reasoning.md`

## Current conceptual control picture

```text
                         KNOWLEDGE LIBRARY
                               |
                               v
PROJECT STATE ----------> ACTIVATION / APPLICABILITY
     ^                         |
     |                         v
     |                questions / obligations /
     |                safeguards / review needs
     |                         |
     |                         v
     |                   RUNNABLE FRONTIER
     |                         |
     |                         v
     |                    ORCHESTRATION
     |                         |
     |                         v
     +--------- evidence / result / revision
```

Coverage review surrounds this loop to search for missed material concerns.

## Strong design hypotheses currently active

Important active hypotheses now include:

- five candidate epistemic invariants;
- project constitution separating admissibility, epistemic integrity, assurance, and optimization;
- typed dependency-aware project state;
- questions and claims as important orchestration objects;
- impact analysis and information lineage;
- runnable frontier and state-driven orchestration;
- progressive, source-aware project initialization;
- a small universal bootstrap;
- reusable knowledge separate from actors and tools;
- system-level knowledge definitions separate from project-specific instances;
- hybrid deterministic, interpretive, and open-ended activation;
- prospective activation around proposed actions, methods, claims, and decisions;
- missing-prerequisite activation;
- modules consuming relevant state slices and producing typed state contributions;
- indirect module interaction through project state;
- shared questions as integration points;
- evidence frameworks rather than cookbook prescriptions;
- open-world and compositional knowledge;
- coverage review and orphaned-state detection;
- activation quality as an evaluation target.

## Explicit non-decisions

The project has not selected agent count, LLM providers, orchestration framework, workflow engine, database, graph technology, event-log architecture, project-state schemas, trigger language, rule engine, semantic retrieval technology, embedding model, module schema, module taxonomy, activation thresholds, scope representation, deduplication algorithm, coverage-review implementation, execution sandbox, final autonomy model, final completion rule, or system-evaluation framework.

## Current focus

The next conceptual question is:

> **What should a reusable knowledge unit contain internally so that, once activated, it can reliably generate the right questions, safeguards, evidence requirements, candidate investigations, review behavior, resolution criteria, and state transitions across heterogeneous projects?**

This is the internal knowledge-representation problem already foreshadowed by Q-007.

Important subquestions include:

- What fields or semantic components are truly necessary?
- How should activation conditions differ from applicability conditions?
- How should hard invariants coexist with conditional decision logic and open-ended prompts?
- How should a knowledge unit express required evidence rather than preferred methods?
- How should scopes, dependencies, sufficient-resolution conditions, and reopen conditions be represented?
- How should references, rationale, examples, known limitations, version, and maturity be stored?
- How should knowledge units support composition without becoming excessively fragmented?
- Which parts should eventually be executable or machine-checkable?
- How should real-project lessons revise a reusable unit without corrupting historical project records?

This should remain conceptual before selecting YAML, JSON, code, rules, graphs, databases, or another storage representation.

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

For detailed reasoning, also read the six files currently under `docs/foundations/`.

Relevant historical checkpoints are Checkpoints 0 through 6 under `docs/checkpoints/`.

## Next step

Develop the internal semantic structure of reusable knowledge units before selecting their implementation format.