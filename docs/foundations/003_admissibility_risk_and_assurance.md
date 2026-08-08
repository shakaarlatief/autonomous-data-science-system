# Foundation 003: Admissibility, Risk, and Assurance

**Date:** 2026-08-08  
**Status:** Foundational design reasoning  
**Maturity:** Strong design hypotheses, not final architecture

## Purpose

This memo preserves the reasoning that followed the epistemic-integrity work in Foundation 002. The discussion explored the second major part of the emerging project constitution: whether actions are permitted, how risk should be understood, how much assurance should be required before consequential actions proceed, and who has authority to accept unresolved or residual risk.

The material in this document is deliberately richer than the canonical current-state summary. It should be used as rationale and design context, not treated as a finalized specification.

## Starting point: validity is not enough

The project had already separated epistemic integrity from project optimization. The next observation was that an analysis can be methodologically excellent and still be impermissible.

For example, an analysis can be semantically correct, leakage-free, appropriately validated, statistically sound, and reproducible while still violating:

- privacy restrictions;
- data-use permissions;
- organizational policy;
- contractual restrictions;
- security requirements;
- legal obligations;
- ethical or fairness requirements;
- operational safety constraints;
- deployment approval rules.

This led to a central distinction:

```text
VALIDITY
Can the reasoning and evidence justify the conclusion?

ADMISSIBILITY
Is the proposed action, data use, analysis, output, or deployment permitted?
```

These should not be collapsed into one generic quality score.

## Reasoning about admissibility is not the same as authorizing it

A major concern is avoiding a system that asks an LLM to decide whether a project is legally or ethically acceptable and then treats that judgment as permission.

The system may be useful for:

- detecting that an admissibility issue exists;
- identifying relevant project facts;
- retrieving or interpreting available policies;
- identifying missing information;
- mapping a proposed action to applicable constraints;
- explaining ambiguity;
- generating safer alternatives;
- preparing questions for an expert or authority;
- operationalizing a rule once it is established.

But this is different from having authority to approve the action.

A recurring candidate principle is therefore:

> **Empirical or reasoning capability does not create normative, legal, policy, or organizational authority.**

Material uncertainty about permission should not be converted into invented permission.

## Constraint provenance and authority

Admissibility constraints can come from different sources, including:

- platform or system safety rules;
- applicable law or regulation;
- contracts and data-use agreements;
- organizational governance and security policy;
- project-owner requirements;
- domain or stakeholder decisions;
- explicit user instructions.

These sources may have different authority and may conflict.

A useful conceptual implication is that a constraint may need provenance similar to an empirical claim. A future representation might include concepts such as:

```text
constraint
source
scope
authority
status
required controls
exception authority
effective version
```

No schema has been selected.

The exact precedence hierarchy between legal, contractual, organizational, project-owner, and user-level rules remains an open question. The important current hypothesis is simply that lower-authority preferences should not silently override binding higher-authority constraints.

## Admissibility is action-specific

Another important refinement is that admissibility should generally attach to proposed actions rather than only to the project as a whole.

Examples of actions include:

```text
read a dataset
join an external dataset
send records to an external API
transform a sensitive field
train a model
generate individual predictions
export an artifact
produce a report
deploy a model
store outputs
```

A project can be admissible overall while one particular operation is prohibited.

Privacy illustrates this well. Different questions apply to collection, access, processing, transfer, retention, derived information, reporting, and deployment. A single `privacy_ok = true` flag would hide too much.

## Candidate admissibility statuses

A richer conceptual status model was proposed:

- **Permitted**: applicable constraints are sufficiently established and satisfied.
- **Permitted with controls**: action may proceed only while specified safeguards are satisfied.
- **Approval required**: an appropriate authority must explicitly authorize continuation.
- **Unresolved**: material information or authoritative interpretation is missing.
- **Prohibited**: an applicable binding constraint disallows the action or no acceptable safe path exists.

These are design hypotheses, not a finalized state machine.

## Detect, resolve, enforce

The admissibility layer may eventually have three conceptual responsibilities:

### Detect

Recognize that a proposed action may have governance, privacy, ethical, legal, contractual, security, or policy implications.

### Resolve

Determine whether project facts and authoritative constraints are sufficient to establish an admissibility status. Where interpretation is material and authority is missing, escalate rather than guess.

### Enforce

Once a binding rule is established, prevent prohibited actions, apply required controls, or require the relevant approval before execution.

This is intentionally stronger than a generic `ethics reviewer` agent. Some controls should become deterministic once their conditions are known.

## Safe alternative generation

A prohibited or constrained action does not necessarily imply that the entire project must stop.

The system should often search for an admissible alternative, for example:

```text
raw data cannot leave local environment
    -> run analysis locally

sensitive feature cannot be used
    -> evaluate alternatives without it

row-level examples cannot be exposed
    -> use aggregated reporting

automatic deployment is prohibited
    -> produce a deployment package for human approval
```

This generalizes an earlier idea from epistemic integrity:

> When a requested solution conflicts with hard constraints, alter or narrow the solution rather than silently violate the constraint.

## Ethics and fairness require separation of empirical and normative questions

The project should avoid treating ethical questions as if they were merely statistical.

For fairness, for example:

- measuring false-negative-rate differences is empirical;
- quantifying uncertainty around those differences is epistemic;
- choosing which fairness criterion is appropriate may be normative or policy-driven;
- determining whether the result satisfies an authoritative requirement is an admissibility question;
- accepting a residual trade-off may require an authorized human or institution.

The system can generate evidence and expose trade-offs without pretending that the data determine the correct normative objective.

## Legal and policy reasoning should use a conservative authority boundary

The working direction is not to ignore legal or policy questions, but also not to allow LLM interpretation to create authority.

A useful candidate policy is:

> **The system may identify, retrieve, summarize, compare, and operationalize authoritative rules, but material uncertainty in legal, contractual, privacy, policy, or normative interpretation should be escalated to the appropriate authority rather than treated as autonomously settled.**

Straightforward established rules can be enforced automatically. Ambiguous rules may require expert or human resolution.

## Admissibility versus assurance

The next distinction was between whether an action is permitted and how much confidence or control is required before a permitted action proceeds.

Working definitions:

> **Admissibility asks whether an action belongs inside the set of actions the project is permitted to take.**

> **Assurance asks how much justified confidence and operational control are required before an admissible action may proceed.**

For example, using a dataset without authorization is an admissibility issue. Using an authorized model in a consequential setting may be permitted but require extensive review, monitoring, human oversight, rollback, and validation. That is an assurance issue.

## Risk should primarily determine assurance intensity

A strong hypothesis emerged:

> **Risk does not normally redefine what valid evidence means. It changes how much assurance is required before relying on that evidence or taking action.**

The same epistemic principles can apply to a movie recommender and a consequential decision-support system, while the amount of review, replication, testing, monitoring, approval, and fallback planning differs substantially.

## Risk attaches to intended use and action, not the model alone

Exactly the same model can have very different risk depending on how its output is used.

For example:

```text
model output -> offline analyst review
model output -> optional marketing intervention
model output -> fully automated consequential action
```

The dataset and model may be identical while operational risk changes dramatically.

Therefore a primary risk-bearing object should be closer to a proposed use, decision, action, or consequential claim than a model in isolation.

## Risk should be scenario-based

The project rejected the idea that a generic LLM should simply assign `risk = low / medium / high` and route the project from that label.

A stronger direction is to identify plausible failure scenarios:

```text
intended action
    -> plausible failure
    -> affected entity / population / system
    -> consequence
    -> likelihood or uncertainty
    -> current controls
    -> residual exposure
```

This exposes why a project is risky and creates concrete objects for analysis and mitigation.

## Candidate risk dimensions

A strong but non-final set of risk drivers includes:

- consequence severity;
- exposure or scale;
- failure likelihood;
- uncertainty about likelihood or impact;
- reversibility;
- detectability;
- time to detection;
- human control and override ability;
- degree of automation;
- distribution-shift exposure;
- population sensitivity;
- operational coupling and propagation;
- fallback quality;
- governance sensitivity.

Some of these can be inferred from project facts, some estimated empirically, and some require domain or human input.

The system should not pretend that all risk is visible in the dataframe.

## Avoid false precision

The project should be cautious about collapsing multidimensional risk immediately into an arbitrary numeric score such as `72.4`.

A structured risk profile may be more informative:

```text
severity: very high
exposure: moderate
reversibility: low
detectability: poor
automation: high
uncertainty: high
human override: absent
```

Aggregate categories may later be useful for routing, but they should remain traceable to explicit underlying reasons.

## Risk assessment can itself trigger investigation

Risk should not be only a static questionnaire.

For example, distribution-shift risk may be investigated using temporal comparisons, historical validation, stress testing, or deployment-context research. Failure likelihood may be estimated from validation errors or simulations.

This creates another adaptive loop:

```text
potential risk detected
    -> risk question
    -> investigation
    -> evidence
    -> updated risk profile
    -> revised assurance requirements
```

Risk objects can therefore participate in the same question/evidence/state system being explored elsewhere in the project.

## Unknown consequential risk should remain visible

Unknown risk should not silently become low risk.

If uncertainty is high and consequences could be substantial or irreversible, that uncertainty may itself justify stronger assurance, additional investigation, or human escalation.

This is not a universal rule that all unknowns are dangerous. It is a requirement that consequential uncertainty not be averaged away or ignored.

## Inherent and residual risk

The discussion distinguished:

- **inherent risk**, before additional safeguards;
- **controls**, intended to reduce risk;
- **residual risk**, remaining after those controls.

Conceptually:

```text
inherent risk
    -> controls
    -> residual risk
```

This permits the system to reason about whether controls make a previously unacceptable use acceptable and what risk remains after mitigation.

## Controls must be credible

A control should not count merely because it is mentioned.

Examples:

- human review may be ineffective if reviewers rubber-stamp thousands of decisions;
- monitoring may be ineffective if alerts are never acted on;
- rollback may be ineffective if recovery takes weeks;
- an abstention mechanism may be ineffective if thresholds are badly configured.

The system may eventually need evidence that a control is operationally meaningful.

## Residual-risk acceptance requires authority

The system may estimate failure rates, quantify uncertainty, compare controls, and characterize possible impact. But deciding that the remaining risk is acceptable may be normative or organizational.

A recurring candidate principle is:

> **The system can analyze risk without automatically having authority to accept it.**

Where possible, acceptable-risk thresholds should be anchored in authoritative sources such as policy, service-level agreements, safety requirements, domain standards, regulatory requirements, historical baselines, or explicit human decisions.

## Assurance extends beyond model validation

High assurance should not be reduced to `more cross-validation`.

Risk-sensitive assurance can involve:

- broader analytical validation;
- robustness and subgroup analysis;
- implementation tests;
- reproducibility checks;
- independent code or methodological review;
- independent replication;
- staged deployment or shadow mode;
- human approval;
- monitoring;
- drift detection;
- fallback or rollback mechanisms;
- abstention and escalation rules;
- stronger audit logging;
- governance documentation.

Assurance concerns how strongly the system must demonstrate, verify, constrain, observe, and recover from behavior before and after action.

## Correctness versus assurance

A useful conceptual distinction is:

- **Correctness**: was the specific conclusion or decision actually sound?
- **Assurance**: how much justified reason do we have to believe it is sound and safe enough to use?

The system cannot guarantee correctness. It can design a process that produces stronger or weaker justified confidence depending on consequence and uncertainty.

## Dynamic risk and assurance

Risk should be recomputed when project state or intended use changes.

An offline exploratory model can become much more consequential when connected to an automated decision process. A change from internal analysis to production deployment may activate entirely new assurance requirements.

Conceptually:

```text
deployment intent discovered
    -> operational risk increases
    -> new assurance obligations activate
```

This fits the broader trigger-based adaptive-system hypothesis.

## Dynamic autonomy and human involvement

A major implication is that autonomy should probably be conditional rather than globally fixed.

Examples:

```text
low-risk reversible exploratory computation
    -> high autonomy

routine expensive training
    -> autonomy with resource controls

consequential methodological decision
    -> autonomous proposal plus review

sensitive data transfer
    -> hard governance check

high-impact operational action
    -> mandatory human approval or restricted autonomy
```

This also distinguishes:

- **preferred human involvement**, set by the project owner;
- **required human involvement**, activated by admissibility, risk, uncertainty, or authority requirements.

A user's preference for minimal interruption should not override a mandatory approval gate.

## Assurance debt / unmet assurance requirements

A model can be valid for one purpose without being ready for a more consequential use.

For example, an exploratory model might have adequate evidence for research discussion but still lack:

- external validation;
- subgroup analysis;
- monitoring design;
- deployment review;
- human approval.

The term `assurance debt` was discussed as a possible way to describe this gap, but the terminology is not final. The deeper concept is important: readiness is use-specific, and transitions to more consequential use should activate additional obligations rather than assume that a good prototype is production-ready.

## Emerging conceptual flow

A useful current decomposition is:

```text
PROPOSED ACTION / INTENDED USE
        |
        v
ADMISSIBILITY
Is the action permitted in principle?
        |
        v
EPISTEMIC INTEGRITY
Is the reasoning/evidence defensible?
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
Who has authority to accept what remains?
        |
        v
PROJECT OPTIMIZATION
Among defensible and admissible paths, which best serves project intent?
```

This should not be mistaken for a final linear workflow. In a mature system, these objects will likely interact and revise each other dynamically.

## Relationship to project state and dependency integrity

Risk and admissibility should likely participate in the same dependency-aware project state as claims and evidence.

For example:

```text
population-stability assumption invalidated
    -> generalization evidence weakens
    -> uncertainty increases
    -> residual risk increases
    -> assurance requirements strengthen
    -> deployment approval reopens
```

This is an important bridge into the next design topic: what project-state objects the autonomous process should actually manage.

## Current status

The following are strong design hypotheses rather than final decisions:

- admissibility is distinct from epistemic validity;
- admissibility should be action-specific, source-aware, authority-aware, and able to require controls or approval;
- system reasoning about rules does not itself create authorization;
- risk should be represented through explicit failure scenarios and structured drivers rather than only a generic label;
- risk is use- and action-dependent;
- inherent and residual risk should be distinguished;
- controls need credible effectiveness;
- residual-risk acceptance needs an appropriate authority;
- risk should drive assurance intensity;
- risk and intended use should dynamically affect autonomy and human gates;
- project state should preserve dependencies between evidence, risk, controls, approvals, and downstream actions.

These ideas still require case-based testing and formalization before promotion into architecture or system requirements.

## Next design transition

The natural next topic is no longer to keep expanding the abstract risk taxonomy. The project now needs to examine the **core project-state model** that could support everything developed so far.

The next major question is:

> **How should the system represent and manage analytical questions, facts, assumptions, evidence, claims, decisions, risks, controls, approvals, dependencies, unresolved issues, and next actions as persistent project state?**

This question should remain conceptual before storage technology or database architecture is selected.
