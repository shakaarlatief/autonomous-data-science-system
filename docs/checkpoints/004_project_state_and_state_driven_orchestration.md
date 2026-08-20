# Checkpoint 4: Project State and State-Driven Orchestration

**Date:** 2026-08-08  
**Status:** Historical design checkpoint  
**Checkpoint class:** DESIGN  
**Project stage:** Conceptual research and system definition  
**Scope:** Records the historical milestone described by this checkpoint: Project State and State-Driven Orchestration.  
**Authority:** Historical provenance; current canonical documents and promoted sources govern current interpretation.  
**Design session:** 01  
**ChatGPT project:** Autonomous Data Science System  
**Session title:** 01 - Foundations & Checkpoint 0  
**Implementation status:** Not started

## Why this checkpoint exists

Since Checkpoint 3, the project has developed a coherent conceptual unit around persistent project state, dependency-aware revision, invalidation and staleness, and next-action selection.

This material is now substantial enough that continuing into project initialization without preserving it would create unnecessary continuity risk.

The detailed reasoning is preserved in:

`docs/foundations/004_project_state_dependency_and_state_driven_orchestration.md`

## 1. Main conceptual shift

Persistent project state should not be treated as passive memory.

The current strong hypothesis is that it should represent the project's evolving epistemic and operational situation strongly enough to determine:

- what the system currently knows;
- what it only assumes;
- what remains unresolved;
- what evidence supports or contradicts important claims;
- why decisions were made;
- what risks, controls, and approvals are active;
- what artifacts are current, stale, superseded, or invalid;
- which downstream conclusions depend on changed upstream state;
- what obligations arise from those changes;
- and what action should happen next.

## 2. Candidate first-class project-state objects

The current minimal conceptual vocabulary includes:

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

This is a strong design hypothesis, not a finalized ontology or schema.

The important principle is separation of epistemic roles. A fact is not an assumption, evidence is not a claim, a claim is not a decision, and a decision is not an approval.

## 3. Questions as a likely orchestration backbone

The project has strengthened the hypothesis that analytical questions may be more fundamental orchestration objects than conventional pipeline stages.

Questions may be project-defining, validity-related, assurance-related, or value-improving. They may also differ in blocking power and completion importance.

A question may be sufficiently resolved even when the empirical result is inconclusive, provided the remaining uncertainty is acceptable for the current decision and project intent.

This is important for avoiding endless experimentation.

## 4. Evidence, claims, and decisions

The current direction preserves a chain such as:

```text
question
    -> investigation
    -> evidence
    -> claim
    -> decision
```

with the possibility of later evidence reopening the question or decision.

Evidence should preserve how it was generated. Claims should preserve their support and assumptions. Decisions should preserve rationale, alternatives, and dependencies.

Rejected alternatives may be worth preserving so later agents do not repeatedly propose already-considered paths without understanding why they were rejected.

## 5. State and history are separate requirements

The system needs both:

- a current view of what should be believed and acted upon now; and
- historical preservation of how important state changed.

Important objects should not simply be overwritten when their status changes. The project should remain able to reconstruct what was believed, why it changed, and which downstream work depended on the earlier state.

No event-sourcing or storage architecture has been selected.

## 6. Validity and currency are different

The project now distinguishes conceptually between whether an object is methodologically valid and whether it is current.

Examples:

- a correct experiment on an older dataset may be valid but stale;
- a leakage-contaminated experiment is invalid;
- a previous accepted model can be valid but superseded;
- a result affected by a changed assumption may require review.

This prevents one overloaded status such as `invalid` from representing every form of non-current state.

## 7. Typed dependencies are central

The project-state hypothesis has become explicitly dependency-aware.

Candidate relationship semantics include:

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

The exact relationship set is not final.

The important requirement is that relationships carry enough semantic meaning for the system to understand what an upstream change should do to downstream state.

## 8. Different dependencies propagate differently

Several dependency classes have emerged conceptually:

- **hard validity dependency**: invalidating the upstream premise can invalidate the downstream object;
- **support dependency**: losing one evidence item should trigger claim reassessment rather than automatic falsification;
- **provenance dependency**: a new upstream version often causes staleness rather than invalidity;
- **requirement dependency**: loss of approval or prerequisite blocks an action;
- **mitigation dependency**: control failure increases or reopens residual risk.

This distinction is necessary for reliable change propagation.

## 9. Impact analysis and change propagation

A major current hypothesis is that consequential state changes should trigger an impact-analysis loop:

```text
new fact / revision / invalidation / new version
        -> identify changed object
        -> traverse typed dependencies
        -> determine impact semantics
        -> apply deterministic effects
        -> mark uncertain effects for reassessment
        -> reopen questions and decisions where necessary
        -> generate new obligations
        -> prioritize repair, rerun, review, or clarification
```

This is a major mechanism through which the future system could become self-correcting rather than merely well documented.

## 10. Invalidation should create obligations

Marking an experiment or claim invalid is not enough.

The system should determine what now needs to happen, such as:

- redefining validation;
- rerunning affected experiments;
- reopening model comparison;
- revising claims;
- reassessing risk;
- reopening approval;
- refreshing dependent report sections.

These new obligations feed back into orchestration.

## 11. Not all affected state should be repaired immediately

A change may affect many historical objects. The system should distinguish objects that are affected from objects that must be repaired now.

Repair priority should depend on current relevance, downstream impact, risk, deliverable importance, resource cost, and expected value.

This prevents dependency tracking from degenerating into full-project reruns after every change.

## 12. Materiality matters

A target-definition change can be highly material. A tiny dataset update may be immaterial for some analyses. A documentation correction may have no analytical effect.

The system therefore needs some notion of materiality when propagating changes.

The exact materiality model remains open.

## 13. Information lineage is broader than computational lineage

One of the strongest insights in this checkpoint is that code and data lineage alone are insufficient.

A human or LLM can inspect final-test results and use that information to design a later model even if the later code never reads the test labels directly.

The project therefore currently distinguishes conceptually:

```text
computational / provenance lineage
    dataset -> transformation -> model -> prediction

epistemic / information lineage
    fact -> question -> evidence -> claim -> decision -> action

governance lineage
    constraint -> control -> approval -> action
```

These may eventually be represented in one typed dependency structure, but the conceptual distinction matters for leakage, review, and provenance.

## 14. Dependency structure can reveal fragile conclusions

A dependency-aware system could detect:

- claims with only one support path;
- multiple apparently independent experiments sharing one flawed validation ancestor;
- assumptions with a very large downstream blast radius;
- circular support structures;
- high-leverage unresolved questions.

This creates a useful concept of an **epistemic single point of failure**.

Higher-risk projects may justify independent evidence or review for such nodes.

## 15. Plans should be derived from state

The current direction is that static project plans should not be the deepest source of truth.

A plan should be a current projection of richer project state.

When evidence, assumptions, risks, approvals, or intended use changes, the plan should be recomputed rather than followed mechanically.

## 16. Candidate actions should arise from unresolved state

Every consequential next action should ideally be traceable to an unresolved question, obligation, risk, constraint, deliverable need, repair requirement, or accepted decision.

This discourages method-first work performed merely because a tool or model is available.

## 17. Runnable frontier

The discussion introduced the conceptual **runnable frontier**: the currently useful candidate actions whose prerequisites are satisfied and which are not blocked by admissibility, approvals, unresolved dependencies, resource constraints, or required reviewer independence.

The orchestrator can then choose from this frontier instead of asking what fixed project stage comes next.

## 18. Hard gates should be separated from prioritization

Mandatory validity, admissibility, or assurance obligations should not compete on equal terms with optional optimization experiments.

A strong candidate control policy is:

1. identify hard blockers and mandatory obligations;
2. remove actions that are not admissible or executable;
3. satisfy prerequisites needed to unlock consequential work;
4. prioritize remaining candidate actions according to expected project value.

This preserves methodological integrity while allowing configurable depth.

## 19. Candidate action-priority factors

Current candidate factors include:

- blocking power;
- validity or admissibility importance;
- risk reduction;
- probability of changing an important decision;
- uncertainty reduction;
- dependency leverage;
- deliverable relevance;
- urgency;
- compute and human cost;
- reversibility;
- parallelizability;
- project objectives and depth preferences.

The project has not selected a weighted score and should avoid false numerical precision prematurely.

## 20. Value of information

A useful qualitative intuition is:

```text
value of investigation
    ~ probability it changes an important decision
      x importance of that decision
      - cost of obtaining the information
```

Risk reduction and high downstream dependency leverage can increase the value considerably.

This provides a more principled basis for deciding whether to investigate leakage, verify an assumption, run another model, ask the human, or stop.

## 21. Parallelism should follow dependencies

Independent, admissible, resource-compatible investigations may run concurrently.

Work that depends on unresolved upstream design choices should wait. Independent reviews may also require intentionally restricted information views to avoid anchoring.

The state model therefore has the potential to determine what can run, what must wait, and what should remain isolated.

## 22. Human clarification is a first-class action

Asking the human should participate in the same action-selection process as experiments or research.

If a high-impact semantic, normative, domain, or authority question cannot be resolved reliably from available evidence, human clarification may be the highest-value next action.

This supports dynamic rather than fixed human involvement.

## 23. Stopping and completion

The current direction distinguishes local stopping from project completion.

A question may stop when remaining uncertainty is decision-irrelevant, evidence is sufficient for the current purpose, further work has low expected value, or the available data cannot discriminate alternatives.

A project may be complete when mandatory epistemic, admissibility, assurance, approval, and deliverable obligations are sufficiently resolved, critical state is internally consistent, no important current output depends on known invalid state, and remaining optional work has insufficient expected value for the project's objectives and budget.

The final completion rule remains open.

## 24. Consolidated state-driven orchestration hypothesis

The current strongest behavioral loop is:

```text
CURRENT PROJECT STATE
        -> identify unresolved questions, obligations, risks,
           stale/invalid objects, approvals, deliverable needs
        -> generate candidate actions
        -> filter by admissibility, prerequisites, resources,
           and required independence
        -> identify mandatory blockers
        -> prioritize remaining runnable candidates
        -> execute one action or compatible parallel set
        -> produce evidence, artifacts, decisions, approvals, or revisions
        -> update dependencies and perform impact analysis
        -> recompute current state and runnable frontier
```

This is a design hypothesis, not an implementation architecture.

## 25. Project state may be more fundamental than the orchestrator

A conceptual shift occurred during this checkpoint.

The orchestrator may not be the deepest center of the system. Instead, project state may be the durable core, with reasoning, execution, review, and orchestration acting on it.

Conceptually:

```text
                 PROJECT STATE
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      reasoning    execution    review
          |           |           |
          +-----------+-----------+
                      |
                      v
                STATE UPDATE
                      |
                      v
             NEW ACTIVE FRONTIER
```

No storage, graph, workflow, or agent technology follows automatically from this conceptual structure.

## 26. Explicit non-decisions

Checkpoint 4 does **not** decide:

- whether project state is stored in a graph database;
- whether event sourcing is used;
- exact state-object schemas;
- exact relationship vocabulary;
- exact status machines;
- exact materiality rules;
- exact priority formula;
- whether value of information is quantitative or qualitative;
- exact parallel scheduler;
- orchestration framework;
- agent framework;
- database technology;
- final completion rule.

## 27. Next continuation point

The next major design question is:

> **How should a new project enter the system and be initialized into this project-state model when the user's initial request, data, documentation, constraints, and intended use may all be incomplete or partially wrong?**

Important subquestions include:

- What should the system extract before inspecting the data?
- What should it infer versus ask the human?
- How should project intent be initialized?
- How should intended use and analytical questions be established?
- What early facts should trigger project characterization?
- When should admissibility and risk assessment begin?
- Which uncertainties should block modelling immediately?
- How should the system avoid asking the user dozens of unnecessary questions?
- How does initial inspection create the first runnable frontier?

This is the recorded continuation point after Checkpoint 4.