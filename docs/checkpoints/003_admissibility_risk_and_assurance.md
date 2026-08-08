# Checkpoint 003: Admissibility, Risk, and Assurance

**Date:** 2026-08-08  
**Development stage:** Conceptual research and system definition  
**Implementation status:** Not started

## Why this checkpoint exists

Since Checkpoint 2, the project has developed the admissibility and risk-sensitive assurance parts of the emerging project constitution deeply enough to form a coherent conceptual unit.

This checkpoint preserves that unit before the project transitions into a new major design topic: the structure of persistent project state.

## Current project constitution hypothesis

The project continues to use the following conceptual hierarchy as a strong design hypothesis:

```text
Admissibility
    -> Epistemic integrity
    -> Risk-sensitive assurance
    -> Project optimization
```

A more detailed interpretation developed during this checkpoint:

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
What evidence, controls, review, approvals, monitoring,
and recovery mechanisms are required?
        |
        v
RESIDUAL-RISK ACCEPTANCE
Who is authorized to accept what remains?
        |
        v
PROJECT OPTIMIZATION
Which defensible and admissible route best serves project intent?
```

This remains conceptual rather than a final workflow or implementation architecture.

## Admissibility versus validity

The project has strongly reinforced the distinction:

```text
VALIDITY
Can this conclusion be justified?

ADMISSIBILITY
May this action, data use, output, or deployment occur?
```

An analysis may be epistemically valid while still being impermissible because of privacy, legal, policy, contractual, ethical, security, safety, or organizational constraints.

## Reasoning does not create authority

A major current hypothesis is that the system may reason about admissibility without automatically having authority to approve it.

The system may:

- detect possible governance issues;
- identify applicable constraints;
- retrieve and summarize authoritative material;
- identify missing facts;
- map project facts to rules;
- propose controls;
- generate safer alternatives;
- prepare questions for experts or decision authorities.

But material ambiguity about permission should not be turned into invented permission merely because an LLM can produce a plausible interpretation.

## Constraint provenance and authority

Admissibility rules may originate from:

- system or platform rules;
- law and regulation;
- contracts and data-use permissions;
- organizational governance;
- security or privacy policy;
- project-owner requirements;
- domain or stakeholder decisions;
- user instructions.

A strong current hypothesis is that constraints should eventually preserve source, authority, scope, version, and exception information where relevant.

The exact precedence model remains unresolved.

## Action-specific admissibility

Admissibility is better understood as applying to proposed actions than as one project-level boolean.

Potential action types include:

```text
read data
transfer data
join data
transform sensitive variables
train models
generate individual predictions
export artifacts
produce reports
deploy systems
store outputs
```

A project can be admissible overall while one specific action is prohibited.

## Candidate admissibility states

The following state model is a current design hypothesis:

```text
PERMITTED
PERMITTED WITH CONTROLS
APPROVAL REQUIRED
UNRESOLVED
PROHIBITED
```

It is not yet a finalized state machine.

## Safe alternatives

A prohibited action should not automatically terminate the whole project if an admissible path can satisfy the objective.

Examples include local execution instead of external transfer, aggregate reporting instead of row-level exposure, excluding a prohibited feature, or preparing a deployment artifact instead of automatically deploying it.

This extends the broader idea that hard constraints should cause the system to alter scope or route rather than silently violate integrity.

## Risk and assurance are distinct

The project now uses the following working distinction:

> **Admissibility asks whether an action is allowed. Assurance asks how much justified confidence and control are required before an allowed action proceeds.**

Risk appears to primarily determine assurance intensity rather than redefining epistemic validity.

## Risk belongs to use and action

A model is not intrinsically low or high risk independent of use.

The same predictive model may be used for:

- offline exploration;
- optional decision support;
- automated high-impact action.

The risk can differ substantially even if the model and dataset do not change.

Therefore the primary risk-bearing object should likely be an intended use, decision, action, or consequential claim rather than a model alone.

## Scenario-based risk representation

The project rejects a generic pattern in which an LLM assigns one unexplained `low / medium / high` risk label.

A stronger current direction is:

```text
intended action
    -> plausible failure scenario
    -> affected entity / system / population
    -> consequence
    -> likelihood or uncertainty
    -> current controls
    -> residual exposure
```

Aggregate risk levels may later be useful for routing, but should remain traceable to the underlying scenarios and evidence.

## Candidate risk dimensions

Important dimensions currently include:

- consequence severity;
- exposure or scale;
- likelihood;
- uncertainty;
- reversibility;
- detectability;
- time to detection;
- human override;
- degree of automation;
- distribution-shift exposure;
- population sensitivity;
- operational coupling;
- fallback quality;
- governance sensitivity.

This list is exploratory rather than final.

## Unknown risk

Unknown consequential risk should remain explicit rather than being interpreted as low risk.

Where consequences are potentially substantial or irreversible, uncertainty may itself activate additional investigation, stronger assurance, or human escalation.

## Inherent risk, controls, and residual risk

The project now distinguishes conceptually:

```text
inherent risk
    -> controls
    -> residual risk
```

Controls may reduce risk, but they should not count merely because they are named. Human review, monitoring, rollback, abstention, or other safeguards need to be operationally credible.

## Residual-risk acceptance

The system may generate evidence about risk without having authority to accept that risk.

A strong current hypothesis is that residual-risk acceptance should identify an appropriate decision authority and, where possible, use externally anchored thresholds such as policy, service requirements, safety specifications, domain standards, or explicit human decisions.

## Assurance is broader than validation

Risk-sensitive assurance can include:

- stronger validation;
- robustness analysis;
- subgroup analysis;
- implementation and reproducibility checks;
- independent methodological or code review;
- independent replication;
- staged rollout or shadow deployment;
- human approval;
- monitoring;
- drift detection;
- rollback and fallback mechanisms;
- abstention and escalation rules;
- stronger audit logging and governance documentation.

The correct mechanism should depend on the failure scenario and project context rather than on a fixed high-risk checklist.

## Dynamic risk

Risk and assurance obligations should be revisable as intended use changes.

For example:

```text
offline exploratory model
    -> later proposed for production automation
    -> operational risk changes
    -> new assurance obligations activate
```

This fits the broader adaptive trigger hypothesis.

## Dynamic autonomy

An important consequence is that autonomy should probably not be one permanent project-wide setting.

The project now distinguishes:

- **preferred human involvement**, expressing the user's desired interaction style;
- **required human involvement**, activated by validity, admissibility, risk, uncertainty, or authority conditions.

Low-risk reversible work may proceed with high autonomy. A sensitive data transfer may require a hard governance check. A high-impact operational action may require explicit human approval.

This is a strong hypothesis rather than a finalized autonomy model.

## Unmet assurance requirements

A valid exploratory artifact should not automatically be treated as production-ready.

The project discussed the concept of unfulfilled assurance requirements, informally called `assurance debt`, to represent the additional validation, review, monitoring, or approval required before an artifact can be used in a more consequential context.

The terminology is not final, but the concept is important.

## Relationship to dependency integrity

Risk, controls, admissibility, approvals, and assurance requirements should likely be dependency-aware.

For example:

```text
population-stability assumption invalidated
    -> generalization evidence weakens
    -> uncertainty increases
    -> residual risk increases
    -> assurance requirements change
    -> deployment approval becomes stale
```

This provides a direct bridge to the next project-state discussion.

## Maturity status

The ideas preserved here are mostly **strong design hypotheses**.

They have not yet been promoted into a final risk schema, governance architecture, formal rule system, numeric risk model, or implementation technology.

No final decisions have been made about:

- risk scoring;
- assurance levels;
- legal or policy interpretation architecture;
- fairness framework;
- authority hierarchy;
- governance technology;
- approval workflow;
- autonomy-state model;
- control representation;
- risk storage schema.

## Detailed reasoning

The full reasoning behind this checkpoint is preserved in:

`docs/foundations/003_admissibility_risk_and_assurance.md`

## Next conceptual transition

The project has now developed enough separate conceptual objects that the next bottleneck is their persistent relationship to one another.

The next major question is:

> **How should the system represent and manage analytical questions, project facts, assumptions, evidence, claims, decisions, risks, controls, approvals, dependencies, unresolved issues, and next actions as the core persistent project state?**

This should be investigated conceptually before choosing databases, graph technologies, workflow engines, or other storage/orchestration infrastructure.
