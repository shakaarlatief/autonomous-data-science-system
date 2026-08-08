# Current State

## Checkpoint

**Checkpoint:** 3  
**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Working project definition

The Autonomous Data Science System is intended to become a rigorous, adaptive, semi-autonomous system for carrying out data science projects through a combination of structured reasoning, executable tools, persistent project state, empirical evidence, review, reusable knowledge, governance constraints, and human judgment.

The accepted primary purpose remains:

> **The system should create the best data-science process for the particular project, where what "best" means depends on the project's goals, constraints, required outputs, and desired level of human involvement.**

Maximum predictive performance, maximum autonomy, maximum analytical depth, minimum cost, or maximum speed are therefore not universal goals. They are project-dependent objectives or means.

## Current project-constitution hypothesis

The project has moved beyond a single flat methodological quality floor.

A strong current conceptual hierarchy is:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

A more detailed interpretation is:

```text
PROPOSED ACTION / INTENDED USE
        |
        v
ADMISSIBILITY
Is this action permitted?
        |
        v
EPISTEMIC INTEGRITY
Is the reasoning and evidence defensible?
        |
        v
RISK ASSESSMENT
What could fail, with what consequence and uncertainty?
        |
        v
ASSURANCE REQUIREMENTS
What evidence, review, controls, approvals, monitoring,
and recovery mechanisms are required?
        |
        v
RESIDUAL-RISK ACCEPTANCE
Who is authorized to accept what remains?
        |
        v
PROJECT OPTIMIZATION
Which defensible and admissible path best serves project intent?
```

This remains a **strong design hypothesis**, not a selected implementation architecture or final workflow.

## Candidate epistemic core

The five-invariant epistemic framework from Checkpoint 2 remains active:

1. **Semantic validity** - are we answering the right question?
2. **Information legitimacy** - did each step use only information legitimate for its role and represented conditions?
3. **Evidence validity** - did the design, assumptions, execution, and uncertainty treatment validly generate evidence about the question?
4. **Claim validity** - are conclusions limited to what the evidence and assumptions justify?
5. **Traceability and dependency integrity** - can consequential conclusions be reconstructed, and can downstream dependencies be identified when upstream state changes?

The framework has survived conceptual stress tests across several project types but has not yet been validated through heterogeneous real-project tests or formalized into system requirements.

Detailed reasoning is preserved in:

`docs/foundations/002_epistemic_integrity_and_project_constitution.md`

## Major development since Checkpoint 2: admissibility

The project has substantially refined the admissibility layer.

A central distinction is:

```text
VALIDITY
Can the conclusion be justified?

ADMISSIBILITY
May the action, data use, output, or intended application occur?
```

An analysis may be epistemically excellent while still being impermissible because of privacy, security, contractual, legal, policy, ethical, fairness, organizational, or operational constraints.

### Reasoning versus authority

A strong current hypothesis is that the system may reason about admissibility without automatically having authority to approve it.

The system may detect issues, retrieve or interpret available rules, identify missing facts, map actions to constraints, propose controls, generate safer alternatives, and prepare questions for experts or decision authorities.

Material ambiguity about permission should not be silently converted into permission merely because an LLM can produce a plausible interpretation.

### Source and authority awareness

Admissibility constraints may originate from different sources, including system rules, law, contracts, data-use permissions, organizational policy, project-owner requirements, stakeholder decisions, or user instructions.

The exact precedence model remains unresolved, but a strong hypothesis is that constraints should eventually preserve their source, scope, authority, status, and relevant version or exception authority.

### Action-specific admissibility

Admissibility should likely attach to proposed actions rather than one project-level boolean.

Examples include reading or transferring data, joining external information, transforming sensitive fields, training models, generating individual predictions, exporting artifacts, reporting, deployment, and retention.

A project can be admissible overall while a particular operation is prohibited or requires controls.

### Candidate admissibility statuses

The following are currently exploratory:

```text
PERMITTED
PERMITTED WITH CONTROLS
APPROVAL REQUIRED
UNRESOLVED
PROHIBITED
```

These are not yet a finalized state machine.

### Safe alternatives

A constrained or prohibited action should not automatically terminate a project when an admissible alternative can still serve the objective.

Examples include local execution instead of external transfer, aggregate reporting instead of row-level disclosure, excluding a restricted feature, or preparing a deployment artifact instead of automatically deploying it.

## Major development since Checkpoint 2: risk and assurance

The project now has a clearer distinction between risk and assurance.

> **Admissibility asks whether an action is allowed. Assurance asks how much justified confidence and operational control are required before an allowed action proceeds.**

A strong hypothesis is that risk primarily changes assurance intensity rather than the meaning of valid evidence.

### Risk attaches to intended use and action

The same model can have very different risk depending on whether it supports offline exploration, an optional human decision, or a fully automated consequential action.

The primary risk-bearing object should therefore likely be an intended use, decision, action, or consequential claim rather than a model alone.

### Scenario-based risk

The project currently rejects an unexplained project-level label such as `risk = high` as the primary representation.

A stronger direction is:

```text
intended action
    -> plausible failure scenario
    -> affected entity / population / system
    -> consequence
    -> likelihood or uncertainty
    -> controls
    -> residual exposure
```

Aggregate categories may later help routing, but should remain traceable to their underlying scenarios and evidence.

### Candidate risk drivers

Current candidate dimensions include:

- consequence severity;
- exposure or scale;
- likelihood;
- uncertainty;
- reversibility;
- detectability and time to detection;
- human control and override ability;
- degree of automation;
- distribution-shift exposure;
- population sensitivity;
- operational coupling;
- fallback quality;
- governance sensitivity.

This set is exploratory rather than final.

### Unknown consequential risk

Unknown risk should remain explicit rather than silently becoming low risk. Where possible consequences are substantial or difficult to reverse, uncertainty may itself justify stronger investigation, assurance, or escalation.

### Inherent and residual risk

The project distinguishes conceptually:

```text
inherent risk
    -> controls
    -> residual risk
```

Controls should not count merely because they are mentioned. Human review, monitoring, rollback, abstention, and similar safeguards need to be credible in the actual operating process.

### Residual-risk acceptance

The system may generate evidence about risk without necessarily having authority to accept the remaining risk.

A strong hypothesis is that residual-risk acceptance should identify an appropriate decision authority and should use authoritative thresholds or requirements where available.

## Assurance is broader than model validation

Risk-sensitive assurance may include:

- stronger validation and robustness analysis;
- subgroup analysis;
- implementation and reproducibility tests;
- independent methodological or code review;
- independent replication;
- staged rollout or shadow deployment;
- human approval;
- monitoring and drift detection;
- rollback and fallback mechanisms;
- abstention and escalation rules;
- stronger auditability and governance documentation.

The correct assurance mechanisms should respond to particular failure scenarios rather than to a universal high-risk checklist.

## Dynamic risk, autonomy, and human involvement

Risk and assurance requirements should be revisable when project state or intended use changes.

For example:

```text
offline exploratory model
    -> proposed production automation
    -> operational risk changes
    -> additional assurance obligations activate
```

This produces an important current hypothesis: autonomy should probably be conditional rather than one fixed project-wide level.

The project now conceptually distinguishes:

- **preferred human involvement**, expressing the user's desired interaction style;
- **required human involvement**, activated by epistemic validity, admissibility, risk, uncertainty, or authority requirements.

A preference for minimal interruption should not override a mandatory approval gate.

## Unmet assurance requirements

A model or artifact may be valid for one purpose without being ready for a more consequential use.

The discussion introduced the concept of unfulfilled assurance requirements, informally called `assurance debt`, for additional validation, monitoring, review, controls, or approval that must be satisfied before intended use expands.

The terminology is not final.

## Dependency-aware governance and risk

Risk, controls, admissibility, approvals, and assurance should likely participate in the same dependency-aware project state as evidence and claims.

For example:

```text
population-stability assumption invalidated
    -> generalization evidence weakens
    -> uncertainty increases
    -> residual risk increases
    -> assurance requirements change
    -> deployment approval becomes stale
```

This observation creates the transition to the next major design problem.

Detailed reasoning for the current checkpoint is preserved in:

`docs/foundations/003_admissibility_risk_and_assurance.md`

Historical snapshot:

`docs/checkpoints/003_admissibility_risk_and_assurance.md`

## Established working principles

The following continue to have strong support. Detailed formulations are maintained in `PRINCIPLES.md`.

1. The repository is the persistent source of truth.
2. Important reasoning should be preserved at multiple levels of detail.
3. Empirical evidence should dominate unsupported LLM judgment when a question is testable.
4. The workflow should be adaptive and revisitable rather than globally linear.
5. The system should combine hard constraints, explicit decision frameworks, and open-ended reasoning.
6. Relevant investigations should activate from project facts.
7. Important decisions should expose assumptions, evidence, uncertainty, and alternatives.
8. Human attention should be used where human judgment creates value.
9. Important conclusions should be challengeable through review or replication where justified.
10. Real projects should act as coverage tests for the evolving system.
11. Generalizable project lessons should become reusable system knowledge.
12. Both the target system and the development method should remain evolvable.
13. The meaning of a good project is project-relative.

## Strong design hypotheses currently active

Important hypotheses now include:

- reusable decision or knowledge modules;
- fact-triggered activation of relevant investigations;
- a revisitable reasoning graph;
- analytical questions and claims as primary orchestration objects;
- explicit question states and dependencies;
- five candidate epistemic invariants;
- a project constitution separating admissibility, epistemic integrity, assurance, and optimization;
- action-specific, source-aware, authority-aware admissibility;
- scenario-based multidimensional risk rather than unexplained aggregate labels;
- inherent risk, controls, and residual risk;
- risk-sensitive assurance;
- required versus preferred human involvement;
- dynamic autonomy based on project state, risk, and admissibility;
- dependency-aware risk, approvals, claims, and controls;
- allocation of analytical effort according to expected value, uncertainty reduction, risk, and downstream impact;
- reducing scope or changing route rather than silently lowering integrity when hard constraints conflict with project objectives.

These remain hypotheses to test and refine.

## Explicit non-decisions

The project has **not** selected:

- agent count or permanent role structure;
- LLM provider strategy;
- orchestration framework;
- workflow engine;
- database, knowledge graph, or rule-engine technology;
- exact decision-module representation;
- execution sandbox architecture;
- experiment-tracking platform;
- deployment or UI architecture;
- final project-type taxonomy;
- final project-intent schema;
- final epistemic invariant set;
- exact analytical-question schema or state machine;
- final admissibility rule architecture;
- legal, fairness, privacy, or governance decision framework;
- authority precedence model;
- risk-scoring method;
- final risk taxonomy;
- formal assurance levels;
- control-effectiveness model;
- residual-risk acceptance workflow;
- final autonomy model or human gates;
- project-state storage representation;
- completion rule;
- system-evaluation framework.

## Project-development method

The repository continues to use layered preservation:

1. canonical current documents;
2. detailed foundational design memos;
3. historical checkpoints and session records;
4. raw conversation material, if later archived, as provenance rather than authority.

The AI design collaborator is responsible for recognizing natural repository checkpoints proactively rather than requiring the user to request each update.

## Current focus

The next major conceptual question is:

> **How should the system represent and manage analytical questions, project facts, assumptions, evidence, claims, decisions, risks, controls, approvals, dependencies, unresolved issues, and next actions as the core persistent project state?**

This question is now the major bottleneck because the project has accumulated many interacting conceptual objects but has not yet defined how they relate as one coherent state model.

Important subquestions include:

- Which concepts deserve first-class project-state objects?
- What is the difference between a fact, observation, assumption, evidence item, claim, and decision?
- How should analytical questions generate investigations and claims?
- How should evidence support or contradict claims?
- How should decisions depend on claims, objectives, and constraints?
- How should risks, controls, approvals, and assurance obligations connect to actions?
- How should invalidation propagate through dependencies?
- Which state is canonical and which material is merely historical?
- How should unresolved issues and blockers be represented?
- How should the system determine the next action from current state?

This should remain conceptual before selecting database, graph, workflow, or agent technology.

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

For detailed reasoning, also read:

9. `docs/foundations/001_initial_vision_and_reasoning.md`
10. `docs/foundations/002_epistemic_integrity_and_project_constitution.md`
11. `docs/foundations/003_admissibility_risk_and_assurance.md`

Relevant historical checkpoints are:

12. `docs/checkpoints/000_checkpoint_0.md`
13. `docs/checkpoints/001_primary_purpose_and_project_intent.md`
14. `docs/checkpoints/002_epistemic_integrity_and_project_constitution.md`
15. `docs/checkpoints/003_admissibility_risk_and_assurance.md`

## Next step

Develop the first conceptual model of persistent project state and the relationships between questions, facts, assumptions, evidence, claims, decisions, risks, controls, approvals, dependencies, unresolved issues, and actions before discussing storage or orchestration technology.
